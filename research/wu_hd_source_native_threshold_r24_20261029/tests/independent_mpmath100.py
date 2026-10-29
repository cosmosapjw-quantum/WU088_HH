"""Independent script: source-table literal rates only, no threshold_audit import."""
from mpmath import mp
import json
from pathlib import Path
mp.dps=100
kb=mp.mpf('1.380649e-23'); e=mp.mpf('1.602176634e-19')
tc=mp.mpf('15');th=mp.mpf('55')
kc=mp.mpf('3.99e-20');kh=mp.mpf('2.92e-17')
betagap=(e/(1000*kb))*(1/tc-1/th)
bound=(mp.log(kh/kc)+mp.mpf('1.5')*mp.log(th/tc))/betagap
rbound=(mp.log(mp.mpf('2.925e-17')/mp.mpf('3.985e-20'))+mp.mpf('1.5')*mp.log(th/tc))/betagap
mixed=mp.mpf('18.09049588228285015972265140398995483041103943599267345200841319971466')
spec=mp.mpf('20.95002099384045759056749544382632657967')
obj={'schema':'wu.r24.independent_mpmath100.v1','input':'Original GL2022 Table2 printed 15K/55K rates in SI, direct independent high precision evaluation','precision_digits':100,
    'delta_max_meV':mp.nstr(bound,98),'delta_max_last_digit_upper_meV':mp.nstr(rbound,98),
    'mixed_excess_factor':mp.nstr(mp.exp((mixed-bound)*betagap),70),
    'spectroscopic_excess_factor':mp.nstr(mp.exp((spec-bound)*betagap),70),
    'physical_Q_J_per_event':None,'GL2022_native_PES_threshold':None,
    'scope':'CONDITIONAL_SHARED_T_INDEPENDENT_POSITIVE_MAXWELL_LAPLACE_CROSS_SECTION'}
p=Path(__file__).resolve().parents[1]/'results'/'INDEPENDENT_MPMATH100.json'
if p.exists():raise SystemExit('exclusive-create output already exists')
p.write_text(json.dumps(obj,indent=2)+'\n')
print('MPMATH100_PASS delta_max_meV='+mp.nstr(bound,35))
print('MPMATH100_PASS rounded='+mp.nstr(rbound,35))
print('MPMATH100_PASS factors='+mp.nstr(mp.exp((mixed-bound)*betagap),30)+','+mp.nstr(mp.exp((spec-bound)*betagap),30))
