"""Deterministic same-author metamorphic numerical probe; NOT R6/C9."""
from __future__ import annotations
from decimal import Decimal, localcontext
from itertools import permutations
from random import Random
import json
from binding_preflight import SOURCE_STATES, chemical_rhs, invariant_residual

def run():
    rng = Random(20261029)
    trials = 0
    max_abs = Decimal(0)
    with localcontext() as ctx:
        ctx.prec = 60
        for p in permutations(range(4)):
            labels=tuple(SOURCE_STATES[i] for i in p)
            for _ in range(10):
                x=[Decimal(rng.randrange(0,100000)) / Decimal(10000) for i in range(4)]
                g=Decimal(rng.randrange(1,1000))/Decimal(200)
                theta=Decimal(rng.randrange(-1000,1000))/Decimal(100000)
                sr=chemical_rhs([v*Decimal(10**6) for v in x], SOURCE_STATES, 'm^-3',g,theta)
                tr=chemical_rhs([x[i] for i in p],labels,'cm^-3',g,theta)
                for j,i in enumerate(p):
                    delta=abs(tr[j]*Decimal(10**6)-sr[i]);max_abs=max(max_abs,delta)
                    if delta>Decimal('1e-45')*max(Decimal(1),abs(sr[i])):
                        raise AssertionError((p,x,g,theta,i,delta))
                invariant=invariant_residual([x[i] for i in p],tr,labels,g,theta)
                for name,v in invariant.items():
                    if abs(v)>Decimal('1e-45'):
                        raise AssertionError((p,x,g,theta,name,v))
                trials+=1
    return {"schema":"wu.r20.metamorphic.v1","seed":20261029,"permutations":24,"state_clock_cases_per_permutation":10,"cases":trials,"unit_and_permutation_checks":trials*4,"conserved_covector_checks":trials*3,"max_absolute_rhs_SI_residual":str(max_abs),"result":"PASS","different_author":False}

if __name__=='__main__': print(json.dumps(run(),indent=2))
