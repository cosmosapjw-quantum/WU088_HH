"""Exact bounded algebra/contract checks; never a source derivative evaluator or certificate issuer."""
from fractions import Fraction as Q
from dataclasses import dataclass

class MissingPremise(ValueError): pass
@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q
    def __post_init__(self):
        if not isinstance(self.lo,Q) or not isinstance(self.hi,Q) or self.lo>self.hi:
            raise MissingPremise('EXACT_RATIONAL_INTERVAL_REQUIRED')
    def __add__(a,b):return Interval(a.lo+b.lo,a.hi+b.hi)
    def __neg__(a):return Interval(-a.hi,-a.lo)
    def __sub__(a,b):return a+-b
    def __mul__(a,b):
        x=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi];return Interval(min(x),max(x))

def point(x):return Interval(Q(x),Q(x))
def check_krawczyk_contract(centre,parent,box,fcentre,jac,dt,c,scales):
    """Checks submitted enclosures with exact arithmetic; does NOT authenticate them.
    Source-bound residual/Jacobian/preconditioner provenance remains a separate prerequisite.
    No radius reset, C substitution or tolerance fitting is performed.
    """
    if not all(len(x)==4 for x in [centre,parent,box,fcentre,jac,c,scales]) or any(len(row)!=4 for row in [*jac,*c]):
        raise MissingPremise('FOUR_GAS_COORDINATES_REQUIRED')
    if not all(isinstance(x,Q) and x>0 for x in scales):raise MissingPremise('POSITIVE_EXACT_SCALES_REQUIRED')
    if not isinstance(dt,Q) or dt<=0:raise MissingPremise('EXACT_POSITIVE_DT_REQUIRED')
    a=[[point(int(i==j))-point(dt)*jac[i][j] for j in range(4)] for i in range(4)]
    b=[[point(int(i==j))-sum((point(c[i][k])*a[k][j] for k in range(4)),point(0)) for j in range(4)] for i in range(4)]
    q=max(sum(max(abs(b[i][j].lo),abs(b[i][j].hi))*scales[j]/scales[i] for j in range(4)) for i in range(4))
    residual=[point(centre[j])-parent[j]-point(dt)*fcentre[j] for j in range(4)]
    image=[point(centre[i])-sum((point(c[i][j])*residual[j] for j in range(4)),point(0))+sum((b[i][j]*(box[j]-point(centre[j])) for j in range(4)),point(0)) for i in range(4)]
    if q>=1 or not all(box[i].lo<image[i].lo<=image[i].hi<box[i].hi for i in range(4)):
        raise MissingPremise('STRICT_KRAWCZYK_OR_SCALED_CONTRACTION_FAILED')
    return {'image':image,'scaled_contraction':q,'arithmetic_contract_pass':True,'root_certified':False}

def photon_chain(n,nprime,opacity,opacity_prime,dt):
    """Exact derivative of P=N/(1+dt*opacity), for bounded algebra only."""
    den=1+dt*opacity
    if den<=0:raise MissingPremise('POSITIVE_BE_DENOMINATOR_REQUIRED')
    return n/den, nprime/den-n*dt*opacity_prime/(den*den)

def require_source_certificate(certificate):
    # Native endpoint and uniform family derivative producers are not available.
    # Arbitrary JSON, an error bar or a successful arithmetic check cannot issue proof.
    raise MissingPremise('SOURCE_BOUND_NATIVE_ROOT_AND_FAMILY_PRODUCER_OPEN')
