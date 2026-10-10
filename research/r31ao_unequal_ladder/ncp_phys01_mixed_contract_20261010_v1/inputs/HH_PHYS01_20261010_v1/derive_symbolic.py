"""Reproducible symbolic verification of local mixed HH/photon-source response.
No nonlinear roots, time histories, or production source dispatch are executed.
"""
import json
from pathlib import Path
import sympy as s

x, y, z, w, p, lam, source = s.symbols('x y z w p lambda S')
a, chi, g, n, C, r = s.symbols('a chi g n C r', positive=True)
gas = [x,y,z,w]; Z=s.Matrix(gas+[p]); u=1-x
q=s.Function('q')(*gas)
base=s.Matrix([s.Function('c'+str(i))(*gas) for i in range(4)]+[0])
photo=s.Matrix([1,0,0,g,-1]); H=s.Matrix([q,0,0,-chi*q,0]); birth=s.Matrix([0,0,0,0,1])
F=base+a*u*p*photo+lam*H+source*birth
J=F.jacobian(Z)
J2F=J*J*F
F2FF=s.Matrix([(F.T*s.hessian(Fi,Z)*F)[0] for Fi in F])
mixed=lambda expr:s.simplify(s.diff(expr,lam,source).subs({lam:0,source:0}))
Qdir=s.diff(q,x)+g*s.diff(q,w)
X=a*u*Qdir*s.Matrix([1,0,0,-chi,0])
Y=-a*q*photo
checks={}
def eq(name,v,target):
    residual=s.simplify(v-target)
    assert residual==0, (name,residual)
    checks[name]=True
for i in range(5):
    eq('mixed_second_order_'+str(i),mixed((J*F)[i]),0)
    eq('mixed_JJ_F_'+str(i),mixed(J2F[i]),X[i])
    eq('mixed_Hessian_FF_'+str(i),mixed(F2FF[i]),2*Y[i])
methods={'continuous':(s.Rational(1,6),s.Rational(1,6)),
         'BE_full':(s.Integer(1),s.Rational(1,2)),
         'BE_two_half':(s.Rational(1,2),s.Rational(5,16))}
method_coeff={}
for name,(alpha,beta) in methods.items():
    method_coeff[name]=s.simplify(alpha*X+2*beta*Y)
    for i in range(5):
        eq(name+'_coordinate_'+str(i),mixed(alpha*J2F[i]+beta*F2FF[i]),method_coeff[name][i])
    v=method_coeff[name]
    eq(name+'_mixed_energy',v[3]+chi*v[0]+(chi+g)*v[4],0)
    eq(name+'_HeII',v[1],0);eq(name+'_HeIII',v[2],0)
Pi=1+r+x+r*(y+2*z);T=C*w/Pi
k=s.Function('k'); qt=n*u*u*k(T)
nu=s.symbols('nu', real=True)
actual_qdir=s.diff(qt,x)+g*s.diff(qt,w)
kprime=s.Subs(s.Derivative(k(s.Symbol('t')),s.Symbol('t')),s.Symbol('t'),T)
expected_qdir=-2*n*u*k(T)+n*u*u*kprime*(C*g-T)/Pi
eq('EOS_qdir_chain',actual_qdir,expected_qdir)
HH=s.Matrix([1,0,0,-chi]); PH=s.Matrix([1,0,0,g]);
hess_T=(HH.T*s.hessian(T,gas)*PH)[0]
eq('EOS_cross_hessian',hess_T,(2*T+C*chi-C*g)/Pi**2)
# Explicit logistic isothermal reduced model tests the generic rooted-tree coefficients.
b=s.symbols('b',positive=True)
iso=[x,p]; FI=s.Matrix([a*(1-x)*p+lam*b*(1-x)**2,source-a*(1-x)*p])
JI=FI.jacobian(iso); FI2=s.Matrix([(FI.T*s.hessian(f,iso)*FI)[0] for f in FI]);
for name,(alpha,beta) in methods.items():
    coef=mixed((alpha*JI*JI*FI+beta*FI2)[0])
    factor={'continuous':-s.Rational(2,3),'BE_full':-3,'BE_two_half':-s.Rational(13,8)}[name]
    eq(name+'_isothermal_polynomial',coef,factor*a*b*(1-x)**2)
# First-moment/time-order benchmark: no photo, no source, or no HH kills mixed term.
for name,v in method_coeff.items():
    eq(name+'_zero_photo',v[0].subs(a,0),0)

output={'status':'SYMBOLIC_IDENTITIES_VERIFIED','checks':checks,'count':len(checks),
    'definitions':{'mixed':'partial_lambda partial_S at lambda=S=0; equals finite lambda*S coefficient through order duration^3',
    'q':'arbitrary differentiable gas-only q(x,HeII,HeIII,w)',
    'base':'arbitrary smooth photon-independent gas reactions, all H/He thermal feedback retained',
    'no_root_or_history':True},
    'vectors':{name:[s.sstr(v) for v in value] for name,value in method_coeff.items()},
    'higher_order_remainder':'not bounded; smooth local frozen-source analysis only'}
import argparse
pa=argparse.ArgumentParser();pa.add_argument('--output',required=True);args=pa.parse_args();o=Path(args.output);o.parent.mkdir(parents=True,exist_ok=True)
with o.open('x') as f:json.dump(output,f,indent=2);f.write('\n')
print(f'{len(checks)} symbolic equalities verified')
