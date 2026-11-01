#!/usr/bin/env python3
"""WU R49 source-conditional public 12-node witness verification.
No third-party raw input required. This is NOT a native REI F05 IVP.
"""
import csv,math
from pathlib import Path
from scipy.constants import Boltzmann
DT_SOURCE_S=4871848749.16828
def rates(T):
    k3=2.18e-9*(T/300.0)**0.355
    return k3,k3*math.exp(-43.0/T)
def verify(path):
    rows=list(csv.DictReader(Path(path).open(encoding="utf-8",newline="")))
    assert len(rows)==12
    valid=0
    for r in rows:
        a,b=float(r["original_T_lo_K"]),float(r["original_T_hi_K"])
        lo,hi=float(r["xHII_lo"]),float(r["xHII_hi"])
        flag=int(r["fit_source_supported"])
        assert 0<lo<=hi<1 and 0<a<=b
        assert flag==int(10<=a<=b<=10000)
        assert int(r["D3_D4_electron_source_exact_zero"])==0
        if not flag:
            assert r["fDp_CE_eq_mid"]==r["ce_efold_nHcrit_cm3_at_orig_tick"]==""
            continue
        valid+=1
        T=(a+b)*0.5;x=(lo+hi)*0.5
        k3,k4=rates(T)
        denom=k3*(1-x)+k4*x
        f=k4*x/denom
        ncrit=1/(DT_SOURCE_S*denom)
        assert math.isclose(f,float(r["fDp_CE_eq_mid"]),rel_tol=5e-13)
        assert math.isclose(ncrit,float(r["ce_efold_nHcrit_cm3_at_orig_tick"]),rel_tol=5e-13)
        assert 0<=f<=x<=1 and -Boltzmann*43<0
    print(f"WU_R49_PUBLIC_WITNESS_PASS {len(rows)}/{len(rows)}; supported={valid}; CE_electron_source=0")
if __name__=="__main__":
    import sys
    verify(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name("R49_WU_PUBLIC_12_NODE_WITNESS.csv"))
