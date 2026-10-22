#!/usr/bin/env python3
"""One bounded C99/Fraction verification pass; no ODE or historical replay."""
import ctypes as C
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import tempfile
import time

ROOT=Path(__file__).resolve().parent
class Ledger(C.Structure):
    _fields_=[(k,C.c_double) for k in ('thermal','binding','radiation','electron','photon_number')]
def frac(x):return F.from_float(float(x))
def expected(kind,I,E,R):
    i,e,r=map(frac,(I,E,R))
    return [(e-i)*r,i*r,-e*r,r,-r] if kind==0 else [-e*r,-i*r,(i+e)*r,-r,r]

def main():
    start=time.perf_counter()
    flags=['-std=c99','-O2','-Wall','-Wextra','-Werror','-pedantic','-fPIC','-shared']
    with tempfile.TemporaryDirectory(prefix='hh1_') as d:
        libpath=Path(d)/'libhh1.so'
        cmd=['cc',*flags,str(ROOT/'hh1_energy_adapter.c'),'-lm','-o',str(libpath)]
        built=subprocess.run(cmd,capture_output=True,text=True,timeout=10)
        assert built.returncode==0,built.stderr
        lib=C.CDLL(str(libpath))
        lib.hh1_d_threshold.argtypes=[C.c_double,C.c_double,C.POINTER(C.c_double)]
        lib.hh1_event.argtypes=[C.c_int,C.c_double,C.c_double,C.c_double,C.POINTER(Ledger)]
        lib.hh1_temperature_rhs.argtypes=[*[C.c_double]*6,C.POINTER(C.c_double)]
        kb=1.380649e-23/1.602176634e-19
        delta=43.0*kb
        out=C.c_double()
        assert lib.hh1_d_threshold(13.6,delta,C.byref(out))==0
        ID=out.value
        count=0;max_ledger=0.;max_component=0.
        cases=[]
        for I in (13.6,ID):
            for R in (0.,1e-30,1e-12,1.):
                for E in (I,math.nextafter(I,math.inf),18.,30.,60.):cases.append((0,I,E,R))
                for E in (0.,kb*255.,kb*300.,kb*25370.663084247735):cases.append((1,I,E,R))
        example={}
        for kind,I,E,R in cases:
            result=Ledger()
            assert lib.hh1_event(kind,I,E,R,C.byref(result))==0
            values=[getattr(result,k) for k,_ in Ledger._fields_]
            truth=expected(kind,I,E,R)
            scale=max(sum(abs(float(v)) for v in truth[:3]),1e-300)
            for v,e in zip(values,truth):
                err=abs(float(frac(v)-e))/scale
                max_component=max(max_component,err)
                assert err<=16*math.ulp(1.)
            residual=abs(math.fsum(values[:3]))/scale
            max_ledger=max(max_ledger,residual)
            assert residual<=16*math.ulp(1.)
            assert sum(truth[:3])==0
            count+=1
            if I==ID and E==18. and R==1. and kind==0:example['D_PI_18eV']=dict(zip([k for k,_ in Ledger._fields_],values))
            if I==ID and E==kb*300. and R==1. and kind==1:example['D_RR_capture_kT_300K']=dict(zip([k for k,_ in Ledger._fields_],values))
        # New threshold gap: inherited H PI is admitted but D PI is rejected.
        gap=(13.6+ID)/2
        result=Ledger(1,2,3,4,5)
        frozen=bytes(result)
        assert lib.hh1_event(0,ID,gap,1.,C.byref(result))==2 and bytes(result)==frozen
        assert lib.hh1_event(0,13.6,gap,1.,C.byref(result))==0
        # Reject invalid and overflowing values without modifying the output.
        negatives=[(0,ID,18.,-1.,1),(0,ID,math.nan,1.,1),(4,ID,18.,1.,1),
                   (1,ID,-1.,1.,1),(0,ID,18.,math.inf,1),
                   (1,ID,1e308,1e308,3),(0,ID,math.nextafter(ID,0.),0.,2)]
        for kind,I,E,R,status in negatives:
            result=Ledger(1,2,3,4,5);frozen=bytes(result)
            assert lib.hh1_event(kind,I,E,R,C.byref(result))==status
            assert bytes(result)==frozen
        # Exact independent chain rule from differentiation of u=(3/2)kNT.
        temp_cases=0;max_temp=0.
        for T in (255.,300.,25370.663084247735):
            for N in (1.,1.5,2.):
                for q,dx,H in ((0.,0.,1e-17),(1e-12,1e-13,0.),(-1e-12,-1e-13,1e-17)):
                    t,n,k=map(frac,(T,N,kb))
                    u=F(3,2)*k*n*t
                    udot=-2*frac(H)*u+frac(q)
                    truth=(udot-F(3,2)*k*t*frac(dx))/(F(3,2)*k*n)
                    got=C.c_double()
                    assert lib.hh1_temperature_rhs(T,N,q,dx,H,kb,C.byref(got))==0
                    scale=max(abs(float(truth)),abs(2*H*T),abs(q/(kb*N)),abs(T*dx/N),1e-300)
                    err=abs(float(frac(got.value)-truth))/scale
                    max_temp=max(max_temp,err);assert err<=32*math.ulp(1.)
                    temp_cases+=1
        # Closed H PI -> D CX -> D RR cycle, exact energies only.
        EH=frac(18.);IH=frac(13.6);DI=frac(ID);capture=frac(kb*300.)
        gas=(EH-IH)-(DI-IH)-capture
        radiation=-EH+(DI+capture)
        binding=IH+(DI-IH)-DI
        assert gas+radiation+binding==0 and binding==0
        compiler=subprocess.run(['cc','--version'],capture_output=True,text=True,timeout=2).stdout.splitlines()[0]
    receipt={'schema':'HH1_C99_FRACTION_VERIFICATION_V1','status':'PASS_SCOPED',
        'event_cases':count,'invalid_or_domain_cases':len(negatives)+1,'temperature_cases':temp_cases,
        'closed_cycle_checks':1,'max_relative_energy_residual':max_ledger,
        'max_scaled_component_error':max_component,'max_scaled_temperature_error':max_temp,
        'I_D_eV':ID,'delta_model_eV':delta,'kb_eV_K':kb,'examples':example,
        'wall_seconds':time.perf_counter()-start,'compiler':compiler,'flags':flags,
        'platform':platform.platform(),'machine':platform.machine(),
        'precision':'C double / Python float binary64; exact Fraction oracle on binary64 inputs',
        'source_sha256':{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in
            ('hh1_energy_adapter.h','hh1_energy_adapter.c','verify_hh1.py')},
        'execution_counts':{'new_ode':0,'historical_replay':0,'ncp':0,'primary_verification_pass':1},
        'scope':'Event energy component only. D rates/cross sections and full coupled model remain OPEN.'}
    (ROOT/'HH1_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
