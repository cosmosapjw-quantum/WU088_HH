from pathlib import Path
import os,json,subprocess,hashlib,select,time
W=Path(__file__).parent;worker=W/'c1/energy06e_c1_identity_candidate'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=subprocess.Popen([str(worker),'--identity-live'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
try:
 assert select.select([p.stdout],[],[],10)[0];identity=p.stdout.readline();assert 'science_dispatch=0' in identity
 proc=Path('/proc')/str(p.pid);assert p.poll() is None
 exe=(proc/'exe').resolve();assert exe==worker and sha(proc/'exe')==sha(worker)
 status={l.split(':')[0]:l.split(':')[1].strip() for l in (proc/'status').read_text().splitlines() if l.startswith(('Uid:','CapEff:','CapBnd:','NoNewPrivs:'))}
 cg=Path('/sys/fs/cgroup'+(proc/'cgroup').read_text().split('::')[1].strip());anc=[]
 for a in [cg,*cg.parents]:
  if str(a).startswith('/sys/fs/cgroup'):anc.append({'path':str(a),'values':{n:(a/n).read_text().strip() if (a/n).exists() else None for n in ['cpu.max','memory.max','memory.current','memory.swap.max']}})
 assert anc[0]['values']['cpu.max']=='100000 100000' and anc[0]['values']['memory.max']=='1073741824' and anc[0]['values']['memory.swap.max']=='0'
 assert status['CapEff']==status['CapBnd']=='0000000000000000' and status['NoNewPrivs']=='1'
 maps=(proc/'maps').read_text();libs=sorted({l.split()[-1]for l in maps.splitlines() if len(l.split())>=6 and l.split()[-1].startswith('/')})
 x={'status':'LIVE_NEW_IDENTITY_PROCESS_OBSERVED','pid':p.pid,'starttime_ticks':(proc/'stat').read_text().split()[21],'identity':identity,'binary':{'path':str(worker),'sha256':sha(worker)},'loader_maps':{n:sha(Path(n))for n in libs if Path(n).is_file()},'ancestors':anc,'execution':status,'observed_while_worker_alive':True,'scientific_dispatch':0,'scope_proposal_sha256':sha(Path('/root/WU088_HH_ENERGY06C_20261009/run/TWO_CELL_NEW_SCOPE_PROPOSAL_V3.json')),'source_sha256':sha(W/'c1/source/wide_domain_20261001_v1/log_native_driver/primitive_worker.cpp'),'future_scientific_execution_binding':None,'UID_policy_admitted':False,'reserve_admitted':False}
 p.stdin.write('RELEASE_IDENTITY_ONLY\n');p.stdin.flush();out,err=p.communicate(timeout=5);assert p.returncode==0
 x.update({'exit':p.returncode,'process_now_exited':True,'future_live_evidence':False});print(json.dumps(x))
finally:
 if p.poll() is None:p.kill();p.wait()
