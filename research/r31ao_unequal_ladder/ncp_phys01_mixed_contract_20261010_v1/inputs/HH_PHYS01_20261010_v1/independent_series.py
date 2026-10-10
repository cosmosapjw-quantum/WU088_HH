"""Independent finite series composition checks; no nonlinear root calls."""
from pathlib import Path
import argparse,json
import sympy as s
from src.mixed_response import WEIGHTS

t,eps,eta=s.symbols('t eps eta');x,w,p,a,q,chi,g,C,P=s.symbols('x w p a q chi g C Pi',positive=True)
beta=s.symbols('beta',real=True);u=s.symbols('u',nonnegative=True)
checks={}
def check(name,e):
    r=s.simplify(e);assert r==0,(name,r);checks[name]=True
# Verify the two-half rooted tree coefficients by composing an independently
# chosen nonlinear polynomial scalar BE Taylor map, rather than copying weights.
y,c0,c1,c2=s.symbols('y c0 c1 c2');f=c0+c1*y+c2*y*y;fp=s.diff(f,y);fpp=s.diff(f,y,2)
def step_at(Y,h):
    return Y+h*f.subs(y,Y)+h*h*(fp*f).subs(y,Y)+h**3*(fp**2*f+s.Rational(1,2)*fpp*f*f).subs(y,Y)
first=y+t*f/2+t*t*fp*f/4+t**3*(fp*fp*f+fpp*f*f/2)/8
second=(first+t*f.subs(y,first)/2+t*t*(fp*f).subs(y,first)/4+t**3*(fp*fp*f+fpp*f*f/2).subs(y,first)/8)
series=s.series(second,t,0,4).removeO().expand()
check('twohalf_order1',series.coeff(t,1)-f)
check('twohalf_order2',series.coeff(t,2)-s.Rational(3,4)*fp*f)
check('twohalf_order3',series.coeff(t,3)-fp*fp*f/2-s.Rational(5,16)*fpp*f*f)
# Differentiate the EOS of a symbolic endpoint rather than differentiating its
# first-order temperature equation or dropping its Hessian cross contribution.
T=C*w/P
for name,(ar,br,c2r) in WEIGHTS.items():
    ar=s.Rational(ar.numerator,ar.denominator);br=s.Rational(br.numerator,br.denominator);c2r=s.Rational(c2r.numerator,c2r.denominator)
    fx=ar*(-2-beta)-2*br; fw=-chi*ar*(-2-beta)-2*br*g
    dx=eps*t*q+eta*c2r*t*t*a*u+eps*eta*t**3*a*q*fx
    dw=-eps*t*chi*q+eta*c2r*t*t*a*u*g+eps*eta*t**3*a*q*fw
    eos=C*(w+dw)/(P+dx)
    exact=s.expand(s.diff(eos,eps,eta).subs({eps:0,eta:0})).coeff(t,3)
    expected=a*q*((C*fw-T*fx)/P+c2r*u*(2*T+C*chi-C*g)/P**2)
    check(name+'_temperature_hessian',exact-expected)
    check(name+'_chem_heat_photon_identity',fw+chi*fx+(chi+g)*2*br)

pa=argparse.ArgumentParser();pa.add_argument('--output',required=True);args=pa.parse_args();out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
with out.open('x') as f:json.dump({'checks':checks,'count':len(checks),'same_author_different_symbolic_construction':True,'independent_agent_review':False,'native_IVP_roots':0},f,indent=2);f.write('\n')
print(f'{len(checks)} series-composition/EOS checks passed')
