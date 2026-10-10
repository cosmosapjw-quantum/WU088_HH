from fractions import Fraction as F
import unittest
from src.mixed_response import factors,energy_factor,temperature_factor

class MixedResponseTests(unittest.TestCase):
    def test_continuous_shared_target_is_subadditive_without_thermal_feedback(self):
        self.assertEqual(factors(F(0))['continuous']['x'], -F(2,3))
    def test_full_BE_isothermal_factor(self):
        self.assertEqual(factors(F(0))['BE_full']['x'], -3)
    def test_two_half_isothermal_factor(self):
        self.assertEqual(factors(F(0))['BE_two_half']['x'], -F(13,8))
    def test_mixed_defect_is_positive_not_physical_boost(self):
        r=factors(F(0));self.assertEqual(r['BE_two_half']['x']-r['BE_full']['x'],F(11,8))
    def test_positive_thermal_factor_increases_subadditivity(self):
        for key,val in factors(F(1,5)).items(): self.assertLess(val['x'],factors(F(0))[key]['x'])
    def test_event_counts_close_hydrogen(self):
        for v in factors(F(7,13)).values(): self.assertEqual(v['x'],v['J_HH']+v['J_photo'])
    def test_photo_events_close_photon_number(self):
        for v in factors(F(-2,3)).values():self.assertEqual(v['P']+v['J_photo'],0)
    def test_all_three_energy_identities(self):
        b,chi,g=F(1,6),F(13598,1000),F(102,1000)
        for k,v in factors(b).items():self.assertEqual(energy_factor(b,chi,g)[k]+chi*v['x']+(chi+g)*v['P'],0)
    def test_zero_neutral_limit_product_is_finite_zero(self):
        # q=n*u^2*k; beta also tends to zero, no division by u in the final product.
        for v in factors(F(0)).values():self.assertEqual(F(0)**2*v['x'],0)
    def test_source_off_or_HH_off_kills_mixed_term(self):
        for v in factors(F(1,8)).values():
            self.assertEqual(F(0)*v['x'],0)
    def test_photo_temperature_crossover_not_ionization_cutoff(self):
        b,chi,g,C,T,Pi,u=F(0),F(13),F(1),F(1),F(1),F(2),F(1,10)
        # At T=Cg, beta=0, target depletion is still present.
        self.assertEqual(factors(b)['continuous']['x'],-F(2,3))
        self.assertGreater(temperature_factor(b,chi,g,C,T,Pi,u)['continuous'],0)
    def test_no_universal_sign_when_thermal_suppression_hypothesis_fails(self):
        # An algebraic beta outside the near-threshold regime is not a physical S0 example.
        self.assertEqual(factors(F(-4))['continuous']['x'],0)
        self.assertGreater(factors(F(-5))['continuous']['x'],0)

if __name__=='__main__':unittest.main()
