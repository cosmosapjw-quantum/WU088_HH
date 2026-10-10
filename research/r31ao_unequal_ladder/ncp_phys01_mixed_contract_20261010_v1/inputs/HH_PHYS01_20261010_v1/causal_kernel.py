"""Leading causal photo/HH competition kernel, on a smooth frozen local stage.
No exact all-time Green function is asserted; the expression is a local jet.
"""
import sympy as s
import argparse,json
from pathlib import Path
b,t,A,q,beta,chi,g=s.symbols('birth duration A q beta chi g',positive=True)
Khh=-A*q*(2+beta)*(t-b)**2/2
Kphoto=-A*q*(t*t-b*b)/2
Kx=Khh+Kphoto
Kp=-Kphoto
Kw=-chi*Khh+g*Kphoto
checks={}
def verify(key,expr):
 assert s.simplify(expr)==0,(key,expr)
 checks[key]=True
verify('HH_integrates_to_cubic',s.integrate(Khh,(b,0,t))+A*q*(2+beta)*t**3/6)
verify('photo_integrates_to_cubic',s.integrate(Kphoto,(b,0,t))+A*q*t**3/3)
verify('gas_integrates_to_cubic',s.integrate(Kx,(b,0,t))+A*q*(4+beta)*t**3/6)
verify('survivors_integrate_to_cubic',s.integrate(Kp,(b,0,t))-A*q*t**3/3)
verify('instant_energy_balance',Kw+chi*Kx+(chi+g)*Kp)
verify('terminal_birth_no_instantaneous_gas',Kx.subs(b,t))
verify('initial_birth_impulse_coefficient',Kx.subs(b,0)+A*q*(3+beta)*t*t/2)
verify('birth_monotonic_derivative',s.diff(Kx,b)-A*q*(b+(2+beta)*(t-b)))
pa=argparse.ArgumentParser();pa.add_argument('--output',required=True);args=pa.parse_args();out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
with out.open('x') as f:json.dump({'task':'HH-PHYS01','checks':checks,'count':len(checks),
 'kernels':{k:s.sstr(v) for k,v in {'HH':Khh,'photo':Kphoto,'HII':Kx,'surviving_photon':Kp,'heat':Kw}.items()},
 'meaning':'leading second-order-in-duration impulse kernel, multiplied by lambda * injected photon mass; integral against constant S gives cubic mixed response',
 'scope':'one smooth frozen local stage; no event crossing; local jets, not certified whole-time kernels',
 'monotonicity':'beta>=0, A>0,q>0, 0<=birth<=duration: HII mixed kernel negative before terminal and increases to zero',
 'native_dispatch':0},f,indent=2);f.write('\n')
print(f'{len(checks)} causal-kernel equalities verified')
