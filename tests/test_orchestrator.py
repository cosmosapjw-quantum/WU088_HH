import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[1]


def setup_fake(tmp):
    folder=tmp/'state';folder.mkdir()
    code='''from pathlib import Path
import hashlib,json,os,time
import numpy as np
ROOT=Path(os.environ['FAKE_ROOT']);MIXED=ROOT
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def provider_gate(): return {'status':'TEST_FIXTURE'}
def folder_for(*args):return ROOT
class Hybrid12:
 identity={}
def configuration(*args):return {},np.ones(1),np.ones(1),np.ones(1),np.ones(1),1.
def build_identity_for_orchestrator(*args):return {'driver':'a'*64,'model_sha256':'b'*64}
def init(*args):pass
def pair(task):
 ia,ib,path=task;np.savez(path,ia=ia,ib=ib,value=100*ia+ib)
 return dict(ia=ia,ib=ib,sha256=sha(path),wall_seconds=.001,cpu_seconds=.001)
def assemble(*args):raise AssertionError('completed scientific assembly must not be repeated')
'''
    legacy=tmp/'fake_legacy.py';legacy.write_text(code)
    profile=dict(schema='WU088_PAIR_COST_PROFILE_V1', scientific_driver_sha256='a'*64,
                 model_sha256='b'*64,g=80,gamma_scale='unit',states=[dict(n=160,z=16,costs=[[i,j,(i+1)*(j+1)] for i in range(12) for j in range(12)])])
    p=tmp/'cost.json';p.write_text(json.dumps(profile))
    env=dict(os.environ,FAKE_ROOT=str(folder))
    cmd=[sys.executable,str(ROOT/'scripts/wide_hybrid_orchestrator_cost.py'),
         '--n','160','--z','16','--workers','1','--max-new-pairs','2',
         '--execution-lane','local','--legacy-runner',str(legacy),'--cost-profile',str(p)]
    return folder,cmd,env


def test_actual_executor_uses_cost_order_and_stops_at_budget(tmp_path):
    folder,cmd,env=setup_fake(tmp_path)
    r=subprocess.run(cmd,env=env,capture_output=True,text=True,timeout=20)
    assert r.returncode==0,r.stderr
    rows=[json.loads(l) for l in (folder/'events.jsonl').read_text().splitlines()]
    assert [(x['ia'],x['ib']) for x in rows]==[(11,11),(10,11)]
    assert len(list(folder.glob('pair_*.npz')))==2
    q=[json.loads(l) for l in (folder/'DURABLE_UPLOAD_QUEUE.jsonl').read_text().splitlines()]
    assert len(q)==1
    before=(folder/'events.jsonl').read_bytes()
    r=subprocess.run(cmd,env=env,capture_output=True,text=True,timeout=20)
    assert r.returncode==74
    assert (folder/'events.jsonl').read_bytes()==before
    assert 'BLOCKED_PENDING_DUAL_BACKUP_ACK' in r.stdout


def test_completed_state_not_reassembled(tmp_path):
    folder,cmd,env=setup_fake(tmp_path)
    ident={'driver':'a'*64,'model_sha256':'b'*64}
    ip=folder/'IDENTITY.json';ip.write_text(json.dumps(ident))
    rows=[]
    for i in range(12):
        for j in range(12):
            p=folder/f'pair_{i:02}_{j:02}.npz';np.savez(p,ia=i,ib=j,value=i*100+j)
            rows.append(dict(ia=i,ib=j,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    (folder/'events.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in rows))
    assembled=folder/'ASSEMBLED.npz';np.savez(assembled,H=np.ones((47,2)))
    result=dict(sha256=hashlib.sha256(assembled.read_bytes()).hexdigest(),identity_sha256=hashlib.sha256(ip.read_bytes()).hexdigest())
    (folder/'RESULTS.json').write_text(json.dumps(result))
    before=assembled.read_bytes()
    r=subprocess.run(cmd,env=env,capture_output=True,text=True,timeout=20)
    assert r.returncode==0,r.stderr
    assert 'SOURCE_COMPLETE_REUSED_NOT_REASSEMBLED' in r.stdout
    assert assembled.read_bytes()==before
