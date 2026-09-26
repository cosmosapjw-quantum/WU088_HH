#!/usr/bin/env python3
"""Measured process/thread configurations on identical foreign-component workloads."""
from pathlib import Path
import argparse,hashlib,json,multiprocessing,os,sys,time
from concurrent.futures import ProcessPoolExecutor
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
ROOT=Path(__file__).resolve().parents[1];sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
import numpy as np
from wu088_hh.native_candidate import ForeignKernel
from wu088_hh.hardware import inspect_host
from build_native import build
STATE=None

def init_worker(libpath,threads,grid,exponents,z,q,cpus):
    global STATE
    os.sched_setaffinity(0,cpus);kernel=ForeignKernel(Path(libpath));kernel.set_threads(threads)
    STATE=(kernel,grid,exponents,z,q)

def work(pair):
    kernel,grid,exponents,z,q=STATE;t,gs,gw,W=grid;i,j=pair
    pars=np.array([exponents[i],exponents[j],z,q]);start=time.perf_counter();cpu=time.process_time()
    out,absolute=kernel(t,gs,gw,W,pars)
    return dict(pair=pair,output=out,absolute=absolute,wall=time.perf_counter()-start,
                cpu=time.process_time()-cpu,team=kernel.observed_threads)

def run_case(libpath,workers,threads,grid,d,z,pairs,cpus):
    start=time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers,mp_context=multiprocessing.get_context('spawn'),
            initializer=init_worker,initargs=(libpath,threads,grid,d['exponents'],z,float(d['v']),cpus)) as pool:
        rows=list(pool.map(work,pairs,chunksize=1))
    return rows,time.perf_counter()-start

def main():
    p=argparse.ArgumentParser();p.add_argument('--runtime',required=True,type=Path)
    p.add_argument('--n',type=int,default=32);p.add_argument('--g',type=int,default=80);p.add_argument('--z',type=float,default=16)
    p.add_argument('--pairs',type=int,default=12);p.add_argument('--repeats',type=int,default=2)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('new report path required')
    if not 4<=a.n<=192 or not 1<=a.g<=192 or not 1<=a.pairs<=12 or not 1<=a.repeats<=5 or not np.isfinite(a.z) or abs(a.z)>64:p.error('invalid benchmark parameters')
    runtime=a.runtime.resolve();profile=json.loads((ROOT/'data/pair_cost_profile.json').read_text())
    source=runtime/'r31a/wide_hybrid_run.py';model=runtime/'inputs/extracted/WU088_HH_R10_FULL_MIXED_BLOCK_OHD_PARTIAL_20260922_v1/inputs/FROZEN_INPUTS.npz'
    for f,h in [(source,profile['scientific_driver_sha256']),(model,profile['model_sha256'])]:
        if hashlib.sha256(f.read_bytes()).hexdigest()!=h:raise ValueError('frozen runtime source changed')
    sys.path.insert(0,str(runtime/'completion/mixed_h'));import native
    d,t,W,gs,gw=native.grid(a.n,a.g);grid=(t,gs,gw,W[0]);hw=inspect_host();budget=min(12,hw['effective_cpu_budget']);cpus=hw['cpus']
    pairs=[(i,j) for i in (0,3,7,11) for j in (0,7,11)][:a.pairs]
    workers=min(budget,len(pairs));configs=[(workers,1)]+[(max(1,budget//th),th) for th in (2,4,6,12) if th<=budget and budget%th==0]
    configs=list(dict.fromkeys(configs));built=build()
    baseline,reference_wall=run_case(built['libraries']['reference']['path'],workers,1,grid,d,a.z,pairs,cpus)
    reference={tuple(r['pair']):r for r in baseline};results=[]
    for rep in range(a.repeats):
        for procs,threads in configs[rep%len(configs):]+configs[:rep%len(configs)]:
            rows,wall=run_case(built['libraries']['candidate']['path'],procs,threads,grid,d,a.z,pairs,cpus)
            equal=all(np.array_equal(r['output'],reference[tuple(r['pair'])]['output']) and np.array_equal(r['absolute'],reference[tuple(r['pair'])]['absolute']) for r in rows)
            record=dict(repetition=rep,processes=procs,kernel_threads=threads,total_thread_budget=procs*threads,
                        batch_wall_including_spawn_s=wall,sum_pair_cpu_s=sum(r['cpu'] for r in rows),
                        numerical_array_exact_equal=equal,observed_teams=sorted(set(r['team'] for r in rows)))
            results.append(record);print(json.dumps(record),flush=True)
            if not equal:raise RuntimeError('parallel configuration changes scientific arrays')
    result=dict(schema='WU088_PROCESS_THREAD_COMPONENT_BENCHMARK_V1',n=a.n,g=a.g,z=a.z,pairs=pairs,
                source_identity={'driver_sha256':profile['scientific_driver_sha256'],'model_sha256':profile['model_sha256']},
                host=hw,build_key=built['build_key'],reference_processes=workers,reference_wall_s=reference_wall,samples=results,
                full_H0_cost_included=False,production_admitted=False,configuration_autopromotion=False,
                scope='foreign-component workload including spawn; select no production configuration from this alone')
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with a.out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':'POOL_BENCHMARK_COMPLETE_NOT_PROMOTED','report':str(a.out)}))
if __name__=='__main__':main()
