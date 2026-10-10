"""Independent Decimal100 scalar formula + fixed two-scale centered differences.
Same physical formulas/constants/provider sigma leaves; different arithmetic,
no candidate AD, roots or actual dataset evolution. FD errors are diagnostic,
not certified remainder bounds or native acceptance tolerances.
"""
from decimal import Decimal as D,localcontext
from pathlib import Path
import json,struct

def c(x):return D.from_float(float(x))
def formula(z,sigma):
 y=[c(v) for v in [.8,.2,.4,12.]];u=list(map(c,[.02,-.01,.03,.2]));v=list(map(c,[-.01,.02,-.01,.3]));a,b=z[4:]
 y=[x+z[i]+a*u[i]+b*v[i] for i,x in enumerate(y)];x,y1,y2,w=y
 nh=c(1e-4);nhe=c(1e-4*.083);f=c(.083);particles=1+nhe/nh+x+nhe/nh*(y1+2*y2);ev=c(1.602176634e-12);kb=c(1.380649e-16)
 t=2*ev*w/(3*kb*particles);ne=nh*x+nhe*(y1+2*y2);lower=[nh*(1-x),nhe*(1-y1-y2),nhe*y1];upper=[nh*x,nhe*y1,nhe*y2];j=[D(0)]*3;heat=D(0)
 chi=list(map(c,[13.598434599702,24.587389011,54.41776]));ciA=[21.11,32.38,19.95];cip=[-1.089,-1.146,-1.089];ciC=[.354,.416,.553];cir=[.874,.987,.735];cid=[1.101,1.056,1.275]
 power=lambda x,p:(x.ln()*c(p)).exp()
 for k,L in enumerate([315614.,570670.,1263030.]):
  l=c(L)/t
  if k==1:alpha=c(3e-14)*power(l,.654);slope=c(-.654)
  else:
   q=power(l/c(.522),.470);alpha=c(2 if k==2 else 1)*c(1.269e-13)*power(l,1.503)/power(1+q,1.923);slope=c(-1.503)+c(1.923)*c(.470)*q/(1+q)
  beta=c(ciA[k])*power(t,-1.5)*(-l/2).exp()*power(l,cip[k])/power(1+power(l/c(ciC[k]),cir[k]),cid[k])
  ci=lower[k]*ne*beta/nh;rr=upper[k]*ne*alpha/nh;j[k]=ci-rr;heat-=chi[k]*ci+upper[k]*ne*kb*t*alpha*(c(1.5)+slope)/(nh*ev)
 bits=lambda x:c(struct.unpack('>d',bytes.fromhex(x))[0])
 for fact,B in [(1.,bits('411caf2e364afdee')),(.3,bits('412135e886f9cb6f'))]:
  dr=upper[1]*ne*c(fact)*bits('3f5f8b1ba9b90acb')*power(t,-1.5)*(-B/t).exp()/nh;j[1]-=dr;heat-=dr*kb*B/ev
 out=[j[0],(j[1]-j[2])/(nhe/nh),j[2]/(nhe/nh),heat]
 hh=nh*(1-x)**2*c(1.2e-17)*power(t,1.2)*(-c(157800.)/t).exp();lam=c(.4)+a;out[0]+=lam*hh;out[3]-=chi[0]*lam*hh
 photons=[];n0=list(map(c,[.05,.005,.001]));na=list(map(c,[-.003,.0002,-.0001]));nb=list(map(c,[.01,-.0003,.0002]));nab=list(map(c,[.002,-.0001,.00004]));low=[1-x,f*(1-y1-y2),f*y1]
 for k,e in enumerate([13.7,35.,70.]):
  rates0=[c(29979245800.)*nh*low[i]*c(sigma[k][i]) for i in range(3)]
  n=n0[k]+a*na[k]+b*nb[k]+a*b*nab[k];p=n/(1+c(1e7)*sum(rates0));photons.append(p);rr=[r*p for r in rates0];out[0]+=rr[0];out[1]+=(rr[1]-rr[2])/f;out[2]+=rr[2]/f;out[3]+=sum(r*(c(e)-kchi) for r,kchi in zip(rr,chi))
 out[3]-=2*c(1e-14)*w
 return out+photons

def run():
 probe=json.loads(Path('evidence/derivative_probe_first.stdout').read_text());assert probe['native_counts']==[0]*4
 outputs=probe['rhs']+probe['photons'];result=[]
 with localcontext() as ctx:
  ctx.prec=100;zero=[D(0)]*6;base=formula(zero,probe['sigma']);evaluations=1
  for i,o in enumerate(outputs):assert c(o['value'][0])<=base[i]<=c(o['value'][1]),('primal',i)
  for order in [1,2]:
   for i in range(6):
    for j in ([None] if order==1 else range(i,6)):
     estimates=[]
     for h in [D('1e-12'),D('1e-14')]:
      if order==1:
       zp=zero.copy();zm=zero.copy();zp[i]=h;zm[i]=-h;fp=formula(zp,probe['sigma']);fm=formula(zm,probe['sigma']);est=[(x-y)/(2*h) for x,y in zip(fp,fm)];evaluations+=2
      elif i==j:
       zp=zero.copy();zm=zero.copy();zp[i]=h;zm[i]=-h;fp=formula(zp,probe['sigma']);fm=formula(zm,probe['sigma']);est=[(x-2*y+z)/(h*h) for x,y,z in zip(fp,base,fm)];evaluations+=2
      else:
       vals=[]
       for si,sj in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        z=zero.copy();z[i]=si*h;z[j]=sj*h;vals.append(formula(z,probe['sigma']))
       est=[(pp-pm-mp+mm)/(4*h*h) for pp,pm,mp,mm in zip(*vals)];evaluations+=4
      estimates.append(est)
     for k,o in enumerate(outputs):
      lo,hi=o['gradient'][i] if order==1 else o['hessian'][i][j];witness=estimates[1][k];change=abs(estimates[0][k]-witness);allow=change*2+D('1e-75')
      assert c(lo)-allow<=witness<=c(hi)+allow,('derivative',order,i,j,k,str(witness),lo,hi,str(change))
      result.append({'output':k,'order':order,'i':i,'j':j,'witness':str(witness),'two_scale_change':str(change),'inside_outward_box':c(lo)<=witness<=c(hi)})
 out={'status':'PASS','scope':'ADMISSIBLE_SYNTHETIC_REAL_FT03_LCS_CALLBACK_ONLY','precision':100,'slots':len(result),'scalar_rhs_evaluations':evaluations,'candidate_derivative_evaluations':1,'steps':['1e-12','1e-14'],'actual_native_counts':[0]*4,'finite_difference_bound_is_rigorous':False,'oracle_dependencies':'Shared original physical formulas, binary64 constants, provider cross sections; independent Decimal arithmetic and centered differences, no candidate Jet or FT03 code imported.','results':result}
 Path('evidence/ACTUAL_RHS_ORACLE.json').write_text(json.dumps(out,indent=2)+'\n');print('ActualRhsMixedCallbacks PASS',len(result),'derivative slots',evaluations,'scalar callback evaluations')
if __name__=='__main__':run()
