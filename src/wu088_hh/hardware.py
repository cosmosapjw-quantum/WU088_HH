"""Linux affinity/topology/quota intake. No machine-name or historical-RAM assumptions."""
from __future__ import annotations
import json
import math
import os
from pathlib import Path
import platform
import subprocess


def select_resources(topology: dict, allowed: set, quota: float|None, *, requested_workers: int=12,
                     kernel_threads: int=1, use_smt: bool=False) -> dict:
    if not allowed or not allowed<=topology.keys() or kernel_threads<1 or requested_workers<0:
        raise ValueError('invalid affinity/topology/worker request')
    if quota is not None and (not math.isfinite(quota) or quota<=0):
        raise ValueError('invalid CPU quota')
    by_core={}
    for cpu in sorted(allowed): by_core.setdefault(tuple(topology[cpu]),cpu)
    cpus=sorted(allowed) if use_smt else sorted(by_core.values())
    budget=min(len(cpus),max(1,math.floor(quota))) if quota is not None else len(cpus)
    if kernel_threads>budget:
        raise ValueError('kernel threads exceed effective CPU budget')
    workers=min(requested_workers or budget//kernel_threads,len(cpus)//kernel_threads)
    if kernel_threads==1: workers=min(workers,budget)
    if workers*kernel_threads>budget:
        raise ValueError('nested workers*threads exceed effective CPU budget')
    return dict(cpus=cpus,workers=workers,kernel_threads=kernel_threads,effective_cpu_budget=budget,
                physical_allowed=len(by_core),logical_allowed=len(allowed),quota_cores=quota,
                smt_requested=use_smt)


def read_cpu_quota(cgroup_root: Path=Path('/sys/fs/cgroup')) -> tuple[float|None,list]:
    # Current membership plus visible parents. Namespace-root cpu.max is also checked.
    dirs={cgroup_root}
    try:
        for line in Path('/proc/self/cgroup').read_text().splitlines():
            parts=line.split(':',2)
            if parts[0]=='0' and not parts[1]:
                rel=parts[2].lstrip('/')
                if '..' not in Path(rel).parts:
                    p=cgroup_root/rel
                    while p==cgroup_root or cgroup_root in p.parents:
                        dirs.add(p)
                        if p==cgroup_root: break
                        p=p.parent
    except OSError: pass
    quotas=[]; sources=[]
    for d in sorted(dirs):
        f=d/'cpu.max'
        if f.exists():
            fields=f.read_text().split()
            if len(fields)!=2: raise ValueError(f'invalid cpu.max: {f}')
            if fields[0]!='max':
                q=float(fields[0])/float(fields[1]);quotas.append(q);sources.append(dict(path=str(f),cores=q))
    # Common cgroup-v1 fallback, without silently ignoring a discovered bound.
    for d in (cgroup_root/'cpu',cgroup_root/'cpu,cpuacct'):
        qf,pf=d/'cpu.cfs_quota_us',d/'cpu.cfs_period_us'
        if qf.exists() and pf.exists():
            q,p=int(qf.read_text()),int(pf.read_text())
            if q>0: quotas.append(q/p);sources.append(dict(path=str(qf),cores=q/p))
    return (min(quotas) if quotas else None),sources


def inspect_host(*, requested_workers: int=12,kernel_threads: int=1,use_smt: bool=False) -> dict:
    allowed=set(os.sched_getaffinity(0)); topology={}
    for cpu in sorted(allowed):
        base=Path(f'/sys/devices/system/cpu/cpu{cpu}/topology')
        topology[cpu]=(int((base/'physical_package_id').read_text()),int((base/'core_id').read_text()))
    quota,sources=read_cpu_quota()
    r=select_resources(topology,allowed,quota,requested_workers=requested_workers,
                       kernel_threads=kernel_threads,use_smt=use_smt)
    mem={}
    for line in Path('/proc/meminfo').read_text().splitlines():
        k,v=line.split(':',1)
        if k in ('MemTotal','MemAvailable','SwapTotal','SwapFree'):
            mem[k+'_bytes']=int(v.split()[0])*1024
    for key in ('memory.max','memory.current'):
        f=Path('/sys/fs/cgroup')/key
        if f.exists(): mem['cgroup_'+key]=f.read_text().strip()
    cpuinfo=Path('/proc/cpuinfo').read_text()
    model=next((x.split(':',1)[1].strip() for x in cpuinfo.splitlines() if x.startswith('model name')),'unknown')
    r.update(cpu_model=model,platform=platform.platform(),quota_sources=sources,memory=mem,
             topology={str(k):list(v) for k,v in topology.items()},hardware_benchmark_performed=False)
    return r


if __name__=='__main__':
    print(json.dumps(inspect_host(),indent=2))
