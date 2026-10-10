from pathlib import Path
import subprocess,json,os,datetime,hashlib,sys
p=Path(__file__).resolve().parent;e=p/'evidence';env=dict(os.environ);env['PATH']='/root/.local/state/bass_cr/fastest_track/rustup/toolchains/1.94.1-x86_64-unknown-linux-gnu/bin:'+env['PATH'];env['CARGO_BUILD_JOBS']='1'
name=sys.argv[1];cmd=sys.argv[2:];assert not (e/(name+'.json')).exists()
r=subprocess.run(cmd,cwd=p,env=env,capture_output=True);(e/(name+'.stdout')).write_bytes(r.stdout);(e/(name+'.stderr')).write_bytes(r.stderr)
a={'name':name,'cmd':cmd,'cwd':str(p),'exit':r.returncode,'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest()};(e/(name+'.json')).write_text(json.dumps(a,indent=2)+'\n')
with (e/'RUN_LEDGER.jsonl').open('a') as f:f.write(json.dumps(a)+'\n')
print(json.dumps(a));print(r.stderr.decode()[-7000:]);sys.exit(r.returncode)
