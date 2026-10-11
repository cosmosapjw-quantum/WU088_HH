from pathlib import Path
import os,sys,json,time,datetime,subprocess,resource,hashlib
p=Path(__file__).resolve().parent;e=p/'evidence';name=sys.argv[1];mode=sys.argv[2];cmd=sys.argv[3:];assert mode in ('build','target') and not (e/(name+'.json')).exists()
build=mode=='build';wall=120 if build else 30;output=33554432 if build else 8388608
limit=dict(wall_seconds=wall,memory_cgroup_bytes=536870912 if build else 268435456,swap_bytes=0,cpu_percent=100,address_space_bytes=None if build else 268435456,output_bytes=output,concurrency=1)
env=dict(os.environ);env['PATH']='/root/.local/state/bass_cr/fastest_track/rustup/toolchains/1.94.1-x86_64-unknown-linux-gnu/bin:'+env['PATH'];env['CARGO_BUILD_JOBS']='1'
cg=Path('/proc/self/cgroup').read_text();base=Path('/sys/fs/cgroup')/cg.split('::',1)[1].strip().lstrip('/');observed={k:(base/k).read_text() for k in ['cpu.max','memory.max','memory.swap.max']};assert int(observed['memory.max'])==limit['memory_cgroup_bytes'] and int(observed['memory.swap.max'])==0;assert observed['cpu.max'].split()[0]==observed['cpu.max'].split()[1]
def child_limits():
 if not build:resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
 resource.setrlimit(resource.RLIMIT_FSIZE,(output,output))
start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic();proc=subprocess.Popen(cmd,cwd=p,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,preexec_fn=child_limits)
try:out,err=proc.communicate(timeout=wall-1);exitcode=proc.returncode
except subprocess.TimeoutExpired:
 proc.kill();out,err=proc.communicate();exitcode=124
elapsed=time.monotonic()-t;assert len(out)+len(err)<=output;(e/(name+'.stdout')).write_bytes(out);(e/(name+'.stderr')).write_bytes(err);rss=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss*1024
r=dict(name=name,mode=mode,command=cmd,cwd=str(p),utc_start=start,utc_end=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=elapsed,exit=exitcode,max_child_RSS_bytes=rss,limits=limit,cgroup=cg,observed_limits=observed,stdout_sha256=hashlib.sha256(out).hexdigest(),stderr_sha256=hashlib.sha256(err).hexdigest(),raw_stdout=name+'.stdout',raw_stderr=name+'.stderr');(e/(name+'.json')).write_text(json.dumps(r,indent=2));
with(e/'RUN_LEDGER.jsonl').open('a')as f:f.write(json.dumps(r)+'\n')
print(json.dumps(r));print(err.decode()[-4000:]);sys.exit(exitcode)
