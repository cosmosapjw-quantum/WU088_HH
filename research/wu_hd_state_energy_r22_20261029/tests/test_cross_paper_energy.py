from __future__ import annotations
import json
import math
from pathlib import Path
import tempfile
import unittest
from decimal import Decimal
from research.wu_hd_state_energy_r22_20261029.src.cross_paper_energy import (
    source_literals, projections, run_from_r21_source, with_r21_ledger, ProjectionContractError,
    Candidate, E_CHARGE_EXACT_C, decimal_token,
)
from research.wu_hd_source_bound_r18_20261029.src.native_rates import load_native_grid, SourceContractError
from research.wu_hd_source_grid_r20_20261029.src.grid_exposure import Segment
from research.wu_hd_thermal_mechanical_ledger_r21_20261029.src.thermal_ledger import build_ledger

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
SOURCE=ROOT/'source'/'CROSS_PAPER_LITERALS.json'
PDF=REPO/'ORIGINAL_SOURCES'/'GL2022_CSIC_supplement.pdf'
SCHEDULE=REPO/'research'/'wu_hd_thermal_mechanical_ledger_r21_20261029'/'results'/'EXAMPLE_SCHEDULE.json'

class R22Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj,cls.digest=source_literals(SOURCE)
        cls.rate_grid=load_native_grid(PDF)
        cls.flow,cls.ledger=build_ledger(cls.rate_grid,(1e6,1e6,0,0),
                    [Segment(105,5e9,0),Segment(255,5e9,0)])

    def test_source_hash(self):
        self.assertEqual(self.rate_grid.source_sha256,'a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754')
        self.assertEqual(len(self.digest),64)

    def test_source_rate(self):
        self.assertEqual(self.rate_grid.lookup(105).nominal_m3_s,Decimal('1.15e-16'))

    def test_ground_rates_dont_specify_Q(self):
        self.assertIsNone(self.obj['physical_Q_J_per_event'])
        self.assertIsNone(self.obj['owner_ACK'])

    def test_level_values_exact(self):
        a,b,c,check=projections(self.obj)
        self.assertEqual(check['HD_rotational_J2_minus_J0_eV'],'0.0331139561')
        self.assertEqual(check['H2_rotational_J1_minus_J0_eV'],'0.0146911424')

    def test_three_thresholds_exact(self):
        rows=projections(self.obj)[:3]
        self.assertEqual([c.threshold_eV for c in rows], [Decimal('0.0174288329'),Decimal('0.0210771863'),Decimal('0.0211288329')])

    def test_Q_sign(self):
        for c in projections(self.obj)[:3]:
            self.assertLess(c.Q_eV,0)
            self.assertEqual(c.threshold_eV,-c.Q_eV)
            self.assertFalse(c.qualified)

    def test_baseline_disagreement_exact(self):
        self.assertEqual(projections(self.obj)[3]['cross_paper_baseline_disagreement_eV'],'0.0000516466')

    def test_differences_not_uncertainty(self):
        self.assertFalse(projections(self.obj)[3]['difference_is_physical_uncertainty'])
        self.assertIsNone(projections(self.obj)[1].uncertainty)

    def test_si_exact_convention(self):
        self.assertEqual(E_CHARGE_EXACT_C,Decimal('1.602176634e-19'))
        self.assertEqual(projections(self.obj)[1].Q_eV*E_CHARGE_EXACT_C, Decimal('-0.0210771863')*Decimal('1.602176634e-19'))

    def test_literal_schema_mismatch(self):
        payload=json.loads(SOURCE.read_text());payload['schema']='INVALID'
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';p.write_text(json.dumps(payload))
            with self.assertRaises(ProjectionContractError):source_literals(p)

    def test_wrong_channel_is_rejected(self):
        obj=json.loads(SOURCE.read_text());obj['locked_ionic_rate']['initial']='H+ + HD(v0,j0)'
        # The admission firewall requires exact states including input/output labels.
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';p.write_text(json.dumps(obj))
            with self.assertRaises(ProjectionContractError):source_literals(p)

    def test_source_value_mutation_rejected(self):
        obj=json.loads(SOURCE.read_text());obj['neutral_diatom_source']['states']['H2_v0_j1']='0.285'
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';p.write_text(json.dumps(obj))
            with self.assertRaises(ProjectionContractError):source_literals(p)

    def test_owner_ack_mutation_rejected(self):
        obj=json.loads(SOURCE.read_text());obj['owner_ACK']='CLAIMED'
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';p.write_text(json.dumps(obj))
            with self.assertRaises(ProjectionContractError):source_literals(p)

    def test_source_attested_Q_mutation_rejected(self):
        obj=json.loads(SOURCE.read_text());obj['physical_Q_J_per_event']='0.123'
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';p.write_text(json.dumps(obj))
            with self.assertRaises(ProjectionContractError):source_literals(p)

    def test_nonfinite_token_rejected(self):
        for s in ('NaN','Inf','-Infinity'):
            with self.assertRaises(ProjectionContractError):decimal_token(s)

    def test_wrong_state_object_rejected(self):
        with self.assertRaises(ProjectionContractError):Candidate('X',Decimal('0.2'),Decimal('0.2'))

    def test_source_flow_exact(self):
        self.assertAlmostEqual(self.flow.extent_reference_m_minus3,660441.4261460102,places=7)
        self.assertEqual(self.flow.temperature_nodes_K,(105,255))

    def test_ledger_affine(self):
        result=with_r21_ledger(self.obj,self.digest,self.ledger)
        self.assertEqual(len(result['candidates']),3)
        self.assertEqual(result['caloric_model']['affine_bath_delta_per_reference_m3']['physical_bath_delta_J_per_ref_m3'],None)
        self.assertIsNone(result['physical_bath_heat'])
        for c in result['candidates']:
            self.assertIsNone(c['physical_bath_energy_J_per_reference_m3'])
            self.assertIsNone(c['physical_Q_J_per_event'])
            xi=Decimal(str(self.ledger.reaction_extent_events_per_ref_m3))
            expect=xi*Decimal(c['Q_event_eV_exact_literal'])*E_CHARGE_EXACT_C
            self.assertAlmostEqual(float(c['diagnostic_Q_times_extent_J_per_reference_m3']),float(expect),delta=1e-26)

    def test_attempt_physical_admission_rejected(self):
        with self.assertRaises(ProjectionContractError):with_r21_ledger(self.obj,self.digest,self.ledger,admit_physical=True)

    def test_invalid_ledger_rejected(self):
        with self.assertRaises(ProjectionContractError):with_r21_ledger(self.obj,self.digest,object())

    def test_nonreactive_zero_extent(self):
        _,l=build_ledger(self.rate_grid,(0,1e6,0,0),[Segment(105,1e9,0)])
        out=with_r21_ledger(self.obj,self.digest,l)
        self.assertEqual(l.reaction_extent_events_per_ref_m3,0)
        self.assertTrue(all(Decimal(row['diagnostic_Q_times_extent_J_per_reference_m3'])==0 for row in out['candidates']))

    def test_expansion_contraction_physical_heat_null(self):
        for th in (+1e-13,-1e-13):
            _,l=build_ledger(self.rate_grid,(1e6,1e6,0,0),[Segment(105,1e9,th)])
            out=with_r21_ledger(self.obj,self.digest,l)
            self.assertIsNone(out['physical_bath_heat'])
            self.assertGreater(l.volume_ratio_final,1) if th>0 else self.assertLess(l.volume_ratio_final,1)

    def test_parent_example_cli(self):
        out=run_from_r21_source(SOURCE,PDF,SCHEDULE)
        self.assertEqual(out['parent_source_flow']['source']['temperature_nodes_K'],[105,255])
        self.assertIsNone(out['physical_state_energy_Q'])
        self.assertFalse(out['invariants']['L4'])

    def test_off_grid_fails(self):
        with self.assertRaises(SourceContractError):self.rate_grid.lookup(100)

    def test_source_pdf_corruption_detected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.pdf';p.write_bytes(PDF.read_bytes()+b'x')
            with self.assertRaises(SourceContractError):load_native_grid(p)

    def test_no_thermally_weighted_rate(self):
        o=run_from_r21_source(SOURCE,PDF,SCHEDULE)
        self.assertFalse(o['parent_source_flow']['source']['Boltzmann_population_applied'])
        self.assertFalse(o['parent_source_flow']['source']['thermal_spin_applied'])

if __name__=='__main__':unittest.main()
