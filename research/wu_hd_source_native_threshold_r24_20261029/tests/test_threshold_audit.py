"""R24 source typing and exact native-grid threshold-inference stress tests."""
from __future__ import annotations
import copy
from decimal import Decimal, localcontext
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

BASE=Path(__file__).resolve().parents[1]
MOD=BASE/'src/threshold_audit.py'
spec=importlib.util.spec_from_file_location('r24_threshold_audit',MOD)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
SRC=BASE/'sources/R24_LOCKED_SOURCE_CONTRACT.json'
R21=BASE/'dependencies/WU_R21_SOURCE_ORIGINAL_20261029.zip'
R23=BASE/'dependencies/WU_R23_MOLECULAR_IONIZATION_SOURCE_ORIGINAL_20261029.zip'

class TestR24OriginalSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record,cls.sha=m.strict_source(SRC)
        cls.ts,cls.tokens,cls.rates,cls.native=m.inspect_native_rate_zip(R21)
        cls.result=m.calculate(cls.record,cls.sha,cls.ts,cls.tokens,cls.rates,cls.native)

    def _mutate(self,transform):
        x=copy.deepcopy(self.record); transform(x)
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'candidate.json';p.write_text(json.dumps(x),encoding='utf8')
            with self.assertRaises(m.AuditContractError):m.strict_source(p)

    def test_01_r21_sha(self): self.assertEqual(m.byte_sha(R21),m.R21_SHA)
    def test_02_r23_sha(self): self.assertEqual(m.byte_sha(R23),m.R23_SHA)
    def test_03_original_pdf_verified(self):self.assertEqual(self.native['pdf_sha256'],m.PDF_SHA)
    def test_04_original_parser_blob_verified(self):self.assertEqual(self.native['r18_git_blob'],m.R18_BLOB)
    def test_05_original_ten_nodes(self):self.assertEqual(self.ts,m.TEMPS)
    def test_06_original_tokens(self):self.assertEqual(self.tokens,m.TOKENS)
    def test_07_105K_rate(self):self.assertEqual(self.rates[2],m.Fraction(23,200000000000000000))
    def test_08_255K_rate(self):self.assertEqual(self.rates[3],m.Fraction(137,500000000000000000))
    def test_09_rate_turnover(self):
        self.assertGreater(self.rates[4],self.rates[3]);self.assertLess(self.rates[-1],self.rates[4])
    def test_10_guard_wrong_channel(self):self._mutate(lambda a:a.update(scope='NEUTRAL H+HD'))
    def test_11_guard_wrong_method(self):self._mutate(lambda a:a['gl2022'].update(method='TIQM'))
    def test_12_guard_wrong_reaction_temperature(self):self._mutate(lambda a:a['gl2022']['source_rate_temperature_K'].__setitem__(2,100))
    def test_13_guard_source_rate(self):self._mutate(lambda a:a['gl2022']['source_row_tokens'].__setitem__(2,'9.9(10)'))
    def test_14_guard_improper_mass_source(self):self._mutate(lambda a:a['gl2022'].update(nuclear_mass_convention_verified=True))
    def test_15_guard_improper_IP_source(self):self._mutate(lambda a:a['gl2022'].update(IP_isotope_offset_application_verified=True))
    def test_16_guard_electronic_limit(self):self._mutate(lambda a:a['velilla2008'].update(this_value_is_isotopic_rovibrational_threshold=True))
    def test_17_guard_wrong_PES_limit(self):self._mutate(lambda a:a['velilla2008'].update(electronic_H2_plus_Hplus_above_H3plus_minimum_cm1='37160'))
    def test_18_guard_wrong_product(self):self._mutate(lambda a:a['lepers2019'].update(end_state="H2(v'=0,j'=1)"))
    def test_19_guard_spectroscopy_as_PES(self):self._mutate(lambda a:a['external_spectroscopy'].update(external_source_is_GL2022_PES_native=True))
    def test_20_guard_physical_Q(self):self._mutate(lambda a:a['null_gates'].update(physical_Q_J_per_event='1e-20'))
    def test_21_guard_production(self):self._mutate(lambda a:a['null_gates'].update(production='ISSUED'))
    def test_22_conditional_arithmetic(self):
        
        with localcontext() as ctx:
            ctx.prec=75
            o=self.result['conditional_literature_cross_path']; a=Decimal(o['j2_to_j0_2019_BO_printed_approx_meV']);b=Decimal(o['H2_j1_from_external_spectroscopy_meV']);self.assertEqual(a+b,Decimal(o['mixed_j2_to_j1_threshold_meV_NOT_PES']))
    def test_23_conditional_difference(self):
        
        with localcontext() as ctx:
            ctx.prec=75
            o=self.result['conditional_literature_cross_path'];self.assertEqual(Decimal(o['external_R23_candidate_meV'])-Decimal(o['mixed_j2_to_j1_threshold_meV_NOT_PES']),Decimal(o['cross_model_difference_meV_NOT_UNCERTAINTY']))
    def test_24_toy_zero_shift(self):self.assertEqual(m.shift_laplace_factor(Decimal('0'),105),Decimal(1))
    def test_25_toy_forward_positive(self):self.assertGreater(m.shift_laplace_factor(Decimal('3'),255),m.shift_laplace_factor(Decimal('3'),105))
    def test_26_toy_negative_temperature(self):
        with self.assertRaises(m.AuditContractError):m.shift_laplace_factor(Decimal('3'),0)
    def test_27_source_barrier_not_constant(self):
        b=[Decimal(z['effective_barrier_p0_meV']) for z in self.result['model_rejection']['p0_effective_barriers']]
        self.assertEqual(len(b),9);self.assertGreater(max(b)-min(b),Decimal('30'))
    def test_28_source_barrier_sign_changes(self):
        b=[Decimal(z['effective_barrier_p0_meV']) for z in self.result['model_rejection']['p0_effective_barriers']]
        self.assertGreater(b[0],0);self.assertLess(b[-1],0)
    def test_29_no_physical_admission(self):
        with self.assertRaises(m.AuditContractError):m.calculate(self.record,self.sha,self.ts,self.tokens,self.rates,self.native,admit_physical=True)
    def test_30_invalid_rate_token(self):
        with self.assertRaises(m.AuditContractError):m.calculate(self.record,self.sha,self.ts,('fake',)+self.tokens[1:],self.rates,self.native)
    def test_31_all_null_gates(self):
        self.assertTrue(all(self.result['claims'][k] is None for k in ['GL2022_native_PES_threshold_meV','physical_Q_J_per_event','physical_bath_heat_J_per_ref_m3','source_rate_uncertainty','reverse_rate','REC_CR_owner_ACK','full_A']))
    def test_32_source_flux_same(self):
        for a,b in zip(self.result['source_grid'],self.rates):
            self.assertEqual(m.Fraction(int(a['k_m3_per_s_exact']['numerator']),int(a['k_m3_per_s_exact']['denominator'])),b)
    def test_33_root_dag_unchanged(self):self.assertEqual(self.result['claims']['canonical_DAG'],'34/49_UNCHANGED')
    def test_34_temperatures_no_interpolation(self):self.assertIs(self.native['rate_interpolation'],False)

    def test_35_positive_laplace_bound_source_nodes(self):
        b=[Decimal(x['max_threshold_meV_from_positive_Laplace_support'])
           for x in self.result['positive_Laplace_support_test']['adjacent_nominal_threshold_upper_meV']]
        self.assertEqual(len(b),9)
        self.assertEqual(min(b),Decimal(self.result['positive_Laplace_support_test']['global_nominal_upper_meV']))
        self.assertTrue(Decimal('15.18')<min(b)<Decimal('15.20'))
    def test_36_last_digit_upper_is_robust(self):
        b=Decimal(self.result['positive_Laplace_support_test']['15_55_last_digit_rounding_only_conservative_upper_meV'])
        self.assertTrue(Decimal('15.19')<b<Decimal('15.20'))
        self.assertGreater(b,Decimal(self.result['positive_Laplace_support_test']['global_nominal_upper_meV']))
    def test_37_spectroscopy_violation_exact_factor(self):
        f=Decimal(self.result['positive_Laplace_support_test']['candidate_15_55_violation_factors']['external_R23_spectroscopy'])
        self.assertTrue(Decimal('25.60')<f<Decimal('25.62'))
    def test_38_BO_mixed_violation_exact_factor(self):
        f=Decimal(self.result['positive_Laplace_support_test']['candidate_15_55_violation_factors']['mixed_BO2019_plus_spectroscopy'])
        self.assertTrue(Decimal('5.12')<f<Decimal('5.13'))
    def test_39_zero_threshold_is_not_excluded(self):
        self.assertLess(m.support_discrepancy_factor(15,55,self.rates[0],self.rates[1],Decimal('0')),1)
    def test_40_bound_rejects_swapped_temperature(self):
        with self.assertRaises(m.AuditContractError):m.threshold_upper_bound_meV(55,15,self.rates[1],self.rates[0])
    def test_41_invariance_under_rate_normalization(self):
        s=m.Fraction(7,9)
        self.assertEqual(m.threshold_upper_bound_meV(15,55,self.rates[0],self.rates[1]),
            m.threshold_upper_bound_meV(15,55,self.rates[0]*s,self.rates[1]*s))
    def test_42_threshold_gates_not_promoted(self):
        p=self.result['positive_Laplace_support_test']
        self.assertIs(p['PES_threshold_certified'],False)
        self.assertIs(p['GL2022_algorithm_inconsistent_certified'],False)
        self.assertIsNone(p['source_rate_uncertainty'])

if __name__=='__main__':unittest.main()
