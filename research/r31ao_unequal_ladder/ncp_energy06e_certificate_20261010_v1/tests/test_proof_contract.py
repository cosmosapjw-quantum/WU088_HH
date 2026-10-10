import unittest,sys
from pathlib import Path
from fractions import Fraction as Q
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from proof_contract import *
class ProofContract(unittest.TestCase):
 def fixture(self):
  z=[Q(0)]*4;p=[point(0)]*4;box=[Interval(Q(-1),Q(1))]*4;jac=[[point(0) for _ in range(4)]for _ in range(4)];c=[[Q(int(i==j))for j in range(4)]for i in range(4)]
  return z,p,box,p,jac,Q(1),c,[Q(1)]*4
 def test_arithmetic_is_not_certificate(self):
  x=check_krawczyk_contract(*self.fixture());self.assertEqual(x['scaled_contraction'],0);self.assertFalse(x['root_certified'])
 def test_missing_or_forged_certificate_rejected(self):
  for c in [None,{}, {'root_certified':True}, {'radius':1e-30}]:
   with self.assertRaises(MissingPremise):require_source_certificate(c)
 def test_strict_boundary_rejected(self):
  x=list(self.fixture());x[3]=[point(1)]*4
  with self.assertRaises(MissingPremise):check_krawczyk_contract(*x)
 def test_contraction_one_rejected(self):
  x=list(self.fixture());x[6]=[[Q(0)]*4 for _ in range(4)]
  with self.assertRaises(MissingPremise):check_krawczyk_contract(*x)
 def test_full_photon_chain_and_carry(self):
  # P=N/(1+d*k); differentiating P*(1+d*k)=N is independent check.
  n,np,k,kp,d=map(Q,[7,3,2,5,4]);p,pp=photon_chain(n,np,k,kp,d)
  self.assertEqual(pp*(1+d*k)+p*d*kp,np)
  self.assertNotEqual(pp,np/(1+d*k))
  # A source-independent second birth adds no derivative; accepted stock carries.
  p2,pp2=photon_chain(p+Q(11),pp,Q(3),Q(2),Q(4))
  self.assertNotEqual(pp2,Q(0));self.assertEqual(pp2*13+p2*8,pp)
 def test_scaled_norm_detects_noncontraction(self):
  x=list(self.fixture());x[4][0][1]=point(Q(1,2));x[7]=[Q(1),Q(3),Q(1),Q(1)]
  with self.assertRaises(MissingPremise):check_krawczyk_contract(*x)
if __name__=='__main__':unittest.main()
