"""Reproduce only the new lightweight PHYS01 calculations in a fresh output dir."""
import argparse,hashlib,json,os,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
pa=argparse.ArgumentParser();pa.add_argument('--output',type=Path);pa.add_argument('--verify-only',action='store_true');args=pa.parse_args()
from verify_delivery import verify
verify()
if args.verify_only:raise SystemExit(0)
if args.output is None:pa.error('--output is required except with --verify-only')
out=args.output.resolve()
if out==ROOT or ROOT in out.parents:pa.error('output must be outside immutable source folder')
out.mkdir(parents=True,exist_ok=False)
commands=[('unit',[sys.executable,'-B','-m','unittest','discover','-s','tests','-v']),
 ('symbolic',[sys.executable,'-B','derive_symbolic.py','--output',str(out/'SYMBOLIC.json')]),
 ('series',[sys.executable,'-B','independent_series.py','--output',str(out/'INDEPENDENT_SERIES.json')]),
 ('causal',[sys.executable,'-B','causal_kernel.py','--output',str(out/'CAUSAL_KERNEL.json')]),
 ('point',[sys.executable,'-B','analyze.py','--output',str(out/'LOCAL_COEFFICIENTS_FINAL.json')])]
records=[]
for name,cmd in commands:
    tic=time.monotonic()
    with (out/(name+'.stdout')).open('x') as so,(out/(name+'.stderr')).open('x') as se:
        p=subprocess.run(cmd,cwd=ROOT,stdout=so,stderr=se,stdin=subprocess.DEVNULL,timeout=40,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
    records.append({'name':name,'exit':p.returncode,'wall_seconds':time.monotonic()-tic})
    if p.returncode:raise SystemExit(f'{name} failed; raw logs retained')
matches={}
for name in ['SYMBOLIC.json','INDEPENDENT_SERIES.json','CAUSAL_KERNEL.json','LOCAL_COEFFICIENTS_FINAL.json']:
    matches[name]=(out/name).read_bytes()==(ROOT/'results'/name).read_bytes()
    if not matches[name]:raise SystemExit(f'non-identical result: {name}')
(out/'REPRODUCTION.json').write_text(json.dumps({'commands':records,'byte_identical_results':matches,'native_IVP_roots':0,'independent_physical_cases_added':0},indent=2)+'\n')
print('5 commands exited0; 4 scientific JSON files are byte identical')
