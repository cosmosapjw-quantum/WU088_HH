#!/usr/bin/env python3
"""Science-resolution full-pair topology benchmark for the frozen WU088 H source.

Reads existing completed z=2 pair checkpoints as the exact numerical reference.
Recomputes selected pairs in memory under alternate process/thread layouts.
No scientific checkpoint, result, or production provider is modified.
"""
from __future__ import annotations
from pathlib import Path
import argparse, importlib.util, json, math, multiprocessing, os, resource, statistics, sys, time
from concurrent.futures import ProcessPoolExecutor

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts'),str(ROOT/'vendor/orchestration')]
import numpy as np
from build_native import build
from wu088_hh.autotune import validate_tuning_profile
from wu088_hh.fullpair_tuning import candidate_layouts, representative_pairs_from_events, select_exact_layout
from wu088_hh.hardware import inspect_host, partition_affinity_groups
from wu088_hh.promotion import sanitize_trusted_native_environment, validate_science_regression
import hashlib

STATE=None


def sha(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_adapter(runtime:Path, profile:Path, regression:Path, built:dict):
    clean=sanitize_trusted_native_environment(
        os.environ,
        R31K_RUNTIME_ROOT=str(runtime.resolve()),
        WU088_R31M_CANDIDATE_SO=built['libraries']['candidate']['path'],
        WU088_R31M_TUNING_PROFILE=str(profile.resolve()),
        WU088_R31M_REGRESSION=str(regression.resolve()),
        WU088_R31M_BUILD_KEY=built['build_key'],
    )
    os.environ.clear();os.environ.update(clean)
    path=ROOT/'vendor/orchestration/r31m_tuned_local_adapter.py'
    spec=importlib.util.spec_from_file_location('r31t_fullpair_adapter',path)
    if spec is None or spec.loader is None: raise RuntimeError('cannot load R31M adapter')
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    return mod


def _worker_init(adapter,n,z,threads,groups,counter,lock,barrier):
    global STATE
    with lock:
        idx=counter.value;counter.value+=1
    if idx>=len(groups):raise RuntimeError('worker affinity index overflow')
    cpus=set(groups[idx]);os.sched_setaffinity(0,cpus)
    adapter.init(n,80,z,'unit')
    h,d,t,W,gs,gw,length,z0=adapter.base.STATE
    if h.lib.hh_set_num_threads(threads):raise RuntimeError('candidate thread configuration rejected')
    STATE=(h,d,t,W,gs,gw,length,z0,tuple(sorted(cpus)))
    barrier.wait()


def _full_pair(pair):
    h,d,t,W,gs,gw,length,z,planned=STATE
    ia,ib=pair;a=float(d['exponents'][ia]);b=float(d['exponents'][ib]);q=float(d['v'])
    cpu0=time.process_time();wall0=time.perf_counter()
    h0=[];h0sa=[]
    h0start=time.perf_counter()
    for active in (0,1):
        val,sa=h.h0(a,b,t,W,z,q,active);h0.append(val);h0sa.append(sa)
    h0wall=time.perf_counter()-h0start
    fstart=time.perf_counter();foreign,fa=h.foreign(a,b,t,gs,gw,W[0],z,q);fwall=time.perf_counter()-fstart
    norm0=np.sqrt(2)*float(d['pref'])*(2*a/np.pi)**.75*(2*b/np.pi)**.75
    norm=norm0*np.array([[1,2*np.sqrt(a),2*np.sqrt(a)],[1,2*np.sqrt(b),2*np.sqrt(b)]])
    foreign=foreign*norm[None];fa=fa*abs(norm[None])
    return {
      'pair':pair,'H0':np.array(h0),'H0_sumabs':np.array(h0sa),'foreign':foreign,'foreign_sumabs':fa,
      'pair_wall_s':time.perf_counter()-wall0,'pair_cpu_s':time.process_time()-cpu0,
      'h0_wall_s':h0wall,'foreign_wall_s':fwall,'observed_threads':h.lib.hh_last_team_size(),
      'affinity':list(sorted(os.sched_getaffinity(0))),'planned_affinity':list(planned),
      'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }


def _cross_l3(groups,l3_by_cpu):
    return sum(len({l3_by_cpu[c] for c in g})>1 for g in groups)


def _load_reference(folder:Path,pairs):
    out={}
    for ia,ib in pairs:
        p=folder/f'pair_{ia:02}_{ib:02}.npz'
        with np.load(p,allow_pickle=False) as f:
            out[ia,ib]={k:f[k].copy() for k in ('H0','H0_sumabs','foreign','foreign_sumabs')}
    return out


def _run_case(adapter,n,z,pairs,reference,processes,threads,use_smt,topology,allowed,l3_by_cpu):
    groups=partition_affinity_groups(topology,allowed,workers=processes,kernel_threads=threads,use_smt=use_smt,l3_by_cpu=l3_by_cpu)
    ctx=multiprocessing.get_context('fork');counter=ctx.Value('i',0);lock=ctx.Lock();barrier=ctx.Barrier(processes)
    start=time.perf_counter()
    with ProcessPoolExecutor(max_workers=processes,mp_context=ctx,initializer=_worker_init,
        initargs=(adapter,n,z,threads,[sorted(g) for g in groups],counter,lock,barrier)) as pool:
        rows=list(pool.map(_full_pair,pairs,chunksize=1))
    batch=time.perf_counter()-start
    exact=True;max_delta=0.0
    for row in rows:
        ref=reference[tuple(row['pair'])]
        for k in ('H0','H0_sumabs','foreign','foreign_sumabs'):
            same=np.array_equal(row[k],ref[k]);exact=exact and same
            if row[k].size:
                max_delta=max(max_delta,float(np.max(np.abs(row[k]-ref[k]))))
        for k in ('H0','H0_sumabs','foreign','foreign_sumabs'):row.pop(k,None)
    observed={tuple(r['affinity']) for r in rows};planned={tuple(sorted(g)) for g in groups}
    disjoint=(observed==planned and sum(len(x) for x in observed)==len(set().union(*(set(x) for x in observed))))
    return {
      'processes':processes,'kernel_threads':threads,'use_smt':use_smt,'batch_wall_s':batch,
      'sum_pair_cpu_s':sum(float(r['pair_cpu_s']) for r in rows),
      'median_pair_wall_s':statistics.median(float(r['pair_wall_s']) for r in rows),
      'median_h0_pair_wall_s':statistics.median(float(r['h0_wall_s']) for r in rows),
      'median_foreign_pair_wall_s':statistics.median(float(r['foreign_wall_s']) for r in rows),
      'max_rss_kib':max(int(r['max_rss_kib']) for r in rows),
      'observed_teams':sorted({int(r['observed_threads']) for r in rows}),
      'numerical_array_exact_equal':bool(exact),'max_abs_array_delta':max_delta,
      'affinity_disjoint':bool(disjoint),'affinity_groups':[sorted(g) for g in groups],
      'observed_affinity_groups':[list(x) for x in sorted(observed)],
      'cross_l3_workers':_cross_l3(groups,l3_by_cpu),'pairs':len(rows),
    }


def _baseline_stats(folder:Path)->dict:
    events=[json.loads(x) for x in (folder/'events.jsonl').read_text().splitlines() if x.strip()]
    telemetry=[json.loads(x) for x in (folder/'ORCHESTRATION_TELEMETRY.jsonl').read_text().splitlines() if x.strip()]
    pair_rows=[r for r in events if 'ia' in r]
    wave=sum(float(r['wave_wall_seconds']) for r in telemetry)
    start=float(telemetry[0]['timestamp_unix'])-float(telemetry[0]['wave_wall_seconds']);end=float(telemetry[-1]['timestamp_unix'])
    return {
      'pair_count':len(pair_rows),'pair_wall_median_s':statistics.median(float(r['wall_seconds']) for r in pair_rows),
      'pair_cpu_sum_s':sum(float(r['cpu_seconds']) for r in pair_rows),'pair_wall_sum_s':sum(float(r['wall_seconds']) for r in pair_rows),
      'effective_cores_mean':sum(float(r['cpu_seconds']) for r in pair_rows)/sum(float(r['wall_seconds']) for r in pair_rows),
      'max_rss_mib':max(int(r['max_rss_kib']) for r in pair_rows)/1024.0,
      'compute_wave_sum_s':wave,'observed_end_to_end_s':end-start,'noncompute_gap_s':end-start-wave,
      'pool_worker_utilization':sum(float(r['wall_seconds']) for r in pair_rows)/(2*wave),
      'delta_count':len(list((folder/'durable_deltas').glob('delta_*.zip'))),
      'delta_total_bytes':sum(p.stat().st_size for p in (folder/'durable_deltas').glob('delta_*.zip')),
    }


def main():
    p=argparse.ArgumentParser();p.add_argument('--runtime',type=Path,required=True)
    p.add_argument('--tuning-profile',type=Path,default=ROOT/'evidence/host_5900x/HOST_TUNING_PROFILE.json')
    p.add_argument('--regression',type=Path,default=ROOT/'evidence/host_5900x/SCIENCE_RESOLUTION_NATIVE_REGRESSION.json')
    p.add_argument('--z',type=float,default=2.0);p.add_argument('--screen-n',type=int,choices=(160,192),default=192)
    p.add_argument('--pairs',type=int,default=12);p.add_argument('--confirm-repeats',type=int,default=2)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('new benchmark report path required')
    if not 3<=a.pairs<=12 or not 1<=a.confirm_repeats<=4:p.error('invalid benchmark size')
    built=build();profile=json.loads(a.tuning_profile.read_text());selected=profile['selected']
    host=inspect_host(use_smt=True,requested_workers=int(selected['processes']),kernel_threads=int(selected['kernel_threads']))
    validate_tuning_profile(profile,host,built['build_key'])
    reg=json.loads(a.regression.read_text());validate_science_regression(reg,profile_sha256=sha(a.tuning_profile),build_key=built['build_key'])
    adapter=_load_adapter(a.runtime.resolve(),a.tuning_profile.resolve(),a.regression.resolve(),built)
    fullhost=inspect_host(use_smt=True,requested_workers=12,kernel_threads=1)
    topology={int(k):tuple(v) for k,v in fullhost['topology'].items()};allowed=set(fullhost['allowed_logical_cpus']);l3={int(k):v for k,v in fullhost['l3_by_cpu'].items()}
    physical=min(12,int(fullhost['physical_allowed']));logical=min(24,int(fullhost['logical_allowed']))
    folder=adapter.folder_for(a.screen_n,80,a.z,'unit')
    if not (folder/'RESULTS.json').is_file():raise RuntimeError(f'completed reference state required: {folder}')
    saved=json.loads((folder/'RESULTS.json').read_text());identity=json.loads((folder/'IDENTITY.json').read_text())
    if int(saved.get('n',-1))!=a.screen_n or float(saved.get('z',math.nan))!=float(a.z):
        raise RuntimeError('completed reference n/z identity mismatch')
    native=identity.get('native') or {}
    if native.get('R31M_build_key')!=built['build_key'] or native.get('R31M_candidate_binary_sha256')!=built['libraries']['candidate']['sha256']:
        raise RuntimeError('completed reference candidate build identity mismatch')
    events=[json.loads(x) for x in (folder/'events.jsonl').read_text().splitlines() if x.strip()]
    pairs=representative_pairs_from_events(events,count=a.pairs);reference=_load_reference(folder,pairs)
    configs=candidate_layouts(physical_budget=physical,logical_budget=logical,pairs=len(pairs))
    screen=[]
    for cfg in configs:
        row=_run_case(adapter,a.screen_n,a.z,pairs,reference,*cfg,topology,allowed,l3);row['phase']='SCREEN';row['repetition']=0
        screen.append(row);print(json.dumps({k:v for k,v in row.items() if k not in ('affinity_groups','observed_affinity_groups')}),flush=True)
        if not row['numerical_array_exact_equal'] or not row['affinity_disjoint']:raise RuntimeError('full-pair screen violated exactness/affinity')
    exact_sorted=sorted(screen,key=lambda r:(r['batch_wall_s'],r['cross_l3_workers']))
    confirm_cfg=[]
    for r in exact_sorted[:2]+[next(r for r in screen if (r['processes'],r['kernel_threads'],r['use_smt'])==(2,12,True))]:
        key=(r['processes'],r['kernel_threads'],r['use_smt'])
        if key not in confirm_cfg:confirm_cfg.append(key)
    confirm=[]
    for rep in range(a.confirm_repeats):
        order=confirm_cfg[rep%len(confirm_cfg):]+confirm_cfg[:rep%len(confirm_cfg)]
        for cfg in order:
            row=_run_case(adapter,a.screen_n,a.z,pairs,reference,*cfg,topology,allowed,l3);row['phase']='CONFIRM';row['repetition']=rep
            confirm.append(row);print(json.dumps({k:v for k,v in row.items() if k not in ('affinity_groups','observed_affinity_groups')}),flush=True)
            if not row['numerical_array_exact_equal'] or not row['affinity_disjoint']:raise RuntimeError('full-pair confirm violated exactness/affinity')
    chosen=select_exact_layout(confirm)
    report={
      'schema':'WU088_R31T_FULLPAIR_TOPOLOGY_BENCHMARK_V1','host':fullhost,'build_key':built['build_key'],
      'runtime':str(a.runtime.resolve()),'z':a.z,'screen_n':a.screen_n,'pairs':[list(x) for x in pairs],
      'baseline_completed_state':_baseline_stats(folder),'screen':screen,'confirm':confirm,'selected_candidate':chosen,
      'current_layout':{'processes':2,'kernel_threads':12,'use_smt':True},
      'scientific_checkpoint_mutation':False,'provider_promotion_applied':False,'durability_policy_changed':False,
      'claim_ceiling':'host full-pair scheduling benchmark only; exact arrays required; no production route change',
    }
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with a.out.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
    print(json.dumps({'status':'FULLPAIR_TOPOLOGY_BENCHMARK_COMPLETE_NOT_APPLIED','report':str(a.out),'selected_candidate':chosen},indent=2))
    return 0

if __name__=='__main__':raise SystemExit(main())
