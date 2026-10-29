"""Different algorithm: mpmath high-precision bisection of integrated rate identity.
Independent mathematical method, SAME AUTHOR: not distinct-author R6/C9.
"""
from pathlib import Path
import json,random
import mpmath as mp
from research.wu_hd_state_energy_r22_20261029.src.cross_paper_energy import source_literals,projections,E_CHARGE_EXACT_C,with_r21_ledger
from research.wu_hd_source_bound_r18_20261029.src.native_rates import load_native_grid
from research.wu_hd_source_grid_r20_20261029.src.grid_exposure import Segment
from research.wu_hd_thermal_mechanical_ledger_r21_20261029.src.thermal_ledger import build_ledger

HERE=Path(__file__).resolve().parents[1]
ROOT=HERE.parents[1]
P,D=source_literals(HERE/'source'/'CROSS_PAPER_LITERALS.json')
GRID=load_native_grid(ROOT/'ORIGINAL_SOURCES'/'GL2022_CSIC_supplement.pdf')
mp.mp.dps=80
rng=random.Random(20261029)
DIAGNOSTIC_THRESHOLDS=[mp.mpf('0.0174288329'),mp.mpf('0.0210771863'),mp.mpf('0.0211288329')]
K=mp.mpf('1.15e-16'); QJ=mp.mpf('1.602176634e-19')
max_abs=0.0;max_rel=0.0;max_energy_abs=0.0
for i in range(160):
    a=10**rng.uniform(2,6); b=10**rng.uniform(2,6); t=10**rng.uniform(5,12)
    # Add exact-degeneracy and missing-source tests.
    if i%8==0:b=a
    if i%17==0:a=0.0
    _,ledger=build_ledger(GRID,(a,b,0,0),[Segment(105,t,0)])
    rr=with_r21_ledger(P,D,ledger)
    # Independent integrated inverse time law, bisect the monotonically increasing extent.
    aa=mp.mpf(repr(a));bb=mp.mpf(repr(b));tt=mp.mpf(repr(t));
    if aa==0 or bb==0:
        true=mp.mpf(0)
    else:
        m=min(aa,bb); M=max(aa,bb); target=K*tt
        def cumulative(x):
            if aa==bb:return x/(aa*(aa-x))
            return mp.log(aa*(bb-x)/(bb*(aa-x)))/(bb-aa)
        left=mp.mpf(0);right=m*(1-mp.mpf('1e-65'))
        for _ in range(240):
            mid=(left+right)/2
            if cumulative(mid)<target:left=mid
            else:right=mid
        true=(left+right)/2
    err=abs(mp.mpf(str(ledger.source_Q_coefficient_events_per_ref_m3))-true)
    max_abs=max(max_abs,float(err))
    max_rel=max(max_rel,float(err/max(mp.mpf(1),abs(true))))
    for row,th in zip(rr['candidates'],DIAGNOSTIC_THRESHOLDS):
        expected=-th*QJ*mp.mpf(str(ledger.source_Q_coefficient_events_per_ref_m3))
        energy_err=abs(mp.mpf(row['diagnostic_Q_times_extent_J_per_reference_m3'])-expected)
        max_energy_abs=max(max_energy_abs,float(energy_err))
        assert energy_err<mp.mpf('1e-35')
    assert err <= mp.mpf('6e-8')+mp.mpf('2e-11')*abs(true),(i,float(err))

out={'schema':'wu.r22.independent_mpmath80.v1','cases':160,'precision_digits':80,
     'method':'independent inverse-integral bisection of mass-action extent; 240 halvings; printed-decimal Q projection',
     'max_absolute_extent_error_events_per_ref_m3':max_abs,
     'max_relative_extent_error_floor1':max_rel,
     'max_energy_projection_abs_error_J_per_ref_m3':max_energy_abs,
     'verdict':'PASS', 'distinct_author':False}
(HERE/'results'/'MPMATH80_160.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
