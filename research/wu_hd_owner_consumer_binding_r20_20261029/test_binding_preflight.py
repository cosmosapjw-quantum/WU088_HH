import unittest
from decimal import Decimal
from fractions import Fraction
from binding_preflight import (
    RATE_SI, INSPECTED, SOURCE_STATES, ContractError,
    assessed_callsite, chemical_rhs, invariant_residual,
)

class BindingPreflightTests(unittest.TestCase):
    def test_printed_exact_rate(self):
        self.assertEqual(RATE_SI, Fraction(23, 200000000000000000))
    def test_rejected_rec_and_cr(self):
        for name in INSPECTED:
            with self.subTest(name=name):
                v=assessed_callsite(name)
                self.assertFalse(v['physical_binding'])
                self.assertEqual(v['actual_owner_ack'], 'NOT_OBTAINED')
                self.assertIn('NO_EXACT_FOUR_STATE_NETWORK',v['reason_codes'])
    def test_rec_node_is_not_105(self):
        self.assertIn('NO_SOURCE_105K_NODE',assessed_callsite('REC_PR156_ROTATIONAL')['reason_codes'])
    def test_reject_unknown_owner(self):
        with self.assertRaises(ContractError):assessed_callsite('UNKNOWN')
    def test_si_rhs(self):
        r=chemical_rhs([1_000_000,1_000_000,0,0],SOURCE_STATES,'m^-3',1)
        self.assertEqual(r[0],Decimal('-0.000115'))
        self.assertEqual(r[1],r[0]);self.assertEqual(r[2],-r[0]);self.assertEqual(r[3],-r[0])
    def test_centimetre_conversion(self):
        r=chemical_rhs([1,1,0,0],SOURCE_STATES,'cm^-3',1)
        self.assertEqual(r[0],Decimal('-1.15e-10'))
        self.assertEqual(r[0]*Decimal(1_000_000),chemical_rhs([1e6,1e6,0,0],SOURCE_STATES,'m^-3',1)[0])
    def test_permutation_similarity(self):
        names=(SOURCE_STATES[1],SOURCE_STATES[0],SOURCE_STATES[3],SOURCE_STATES[2])
        r=chemical_rhs([1,2,3,4],names,'cm^-3',1)
        q=chemical_rhs([2,1,4,3],SOURCE_STATES,'cm^-3',1)
        self.assertEqual(r,(q[1],q[0],q[3],q[2]))
    def test_clock_expansion_and_conserved(self):
        state=[1,2,3,4];g='2.5';theta='0.0003'
        r=chemical_rhs(state,SOURCE_STATES,'cm^-3',g,theta)
        self.assertEqual(invariant_residual(state,r,SOURCE_STATES,g,theta),{'H':0,'D':0,'charge':0})
    def test_zero_reactant(self):
        self.assertEqual(chemical_rhs([0,2,3,4],SOURCE_STATES,'m^-3',1),(0,0,0,0))
    def test_temperature_gate(self):
        with self.assertRaises(ContractError):chemical_rhs([1,1,0,0],SOURCE_STATES,'m^-3',1,temperature_K=100)
    def test_clock_gate(self):
        for clock in [0,-1,'NaN','Infinity']:
            with self.subTest(clock=clock),self.assertRaises(ContractError):
                chemical_rhs([1,1,0,0],SOURCE_STATES,'m^-3',clock)
    def test_units_and_duplicates_gate(self):
        with self.assertRaises(ContractError):chemical_rhs([1,1,0,0],SOURCE_STATES,'mol/m^3',1)
        with self.assertRaises(ContractError):chemical_rhs([1,1,0,0],[SOURCE_STATES[0]]*4,'m^-3',1)
    def test_signed_expansion_and_malformed_theta(self):
        r=chemical_rhs([1,2,3,4],SOURCE_STATES,"cm^-3","2","-0.3")
        self.assertEqual(invariant_residual([1,2,3,4],r,SOURCE_STATES,"2","-0.3"), {"H":0,"D":0,"charge":0})
        for bad in ["not-a-number", "NaN", "-Infinity", True]:
            with self.subTest(bad=bad),self.assertRaises(ContractError):
                chemical_rhs([1,2,3,4], SOURCE_STATES, "cm^-3",1,bad)
            with self.subTest(invariant=bad),self.assertRaises(ContractError):
                invariant_residual([1,2,3,4],r,SOURCE_STATES,1,bad)
    def test_bad_physical_states(self):
        for val in [-1,True,'NaN']:
            with self.subTest(val=val),self.assertRaises(ContractError):
                chemical_rhs([val,1,0,0],SOURCE_STATES,'m^-3',1)

if __name__=='__main__':unittest.main()
