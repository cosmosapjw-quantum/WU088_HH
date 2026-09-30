from __future__ import annotations
import math

N1,N2,N3=128.0,160.0,192.0
THRESHOLD=math.log(N2/N1)/math.log(N3/N2)

def ratio_model(p: float) -> float:
    p=float(p)
    if not math.isfinite(p) or p<=0:
        raise ValueError("p must be positive finite")
    return ((N2/N1)**p - 1.0)/(1.0-(N2/N3)**p)

def solve_positive_order(observed_ratio: float, *, tol: float=1e-13, max_iter: int=200) -> float:
    rho=float(observed_ratio)
    if not math.isfinite(rho) or rho<=THRESHOLD:
        raise ValueError("no positive-p solution under the conditional power model")
    lo=0.0
    hi=1.0
    while ratio_model(hi) < rho:
        hi*=2.0
        if hi>1024:
            raise RuntimeError("failed to bracket observed order")
    for _ in range(max_iter):
        mid=(lo+hi)/2
        if mid==0:
            mid=math.nextafter(0.0,1.0)
        val=ratio_model(mid)
        if abs(val-rho) <= tol*max(1.0,abs(rho)):
            return mid
        if val<rho:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def conditional_errors(d128160: float, d160192: float):
    d12=float(d128160); d23=float(d160192)
    if not all(math.isfinite(x) and x>0 for x in (d12,d23)):
        raise ValueError("positive finite increments required")
    rho=d12/d23
    p=solve_positive_order(rho)
    return {
        "rho_norm":rho,
        "p_conditional":p,
        "E192_conditional":d23/((N3/N2)**p-1.0),
        "E160_conditional":d23/(1.0-(N2/N3)**p),
        "rigorous":False,
        "stable_error_direction_required":True,
    }

def authority_ladder():
    return {
        "orders":[128,160,192],
        "ratios":[160/128,192/160],
        "equal_ratio":False,
        "OD_source_guard_allows":True,
        "JVP_frozen_grids_present":True,
        "exact_weight_declared_range_includes_all":True,
        "source_modification_required":False,
        "science_execution_authorized":False,
    }
