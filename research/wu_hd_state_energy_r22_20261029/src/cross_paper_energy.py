"""Conditional source-mismatched energy projection for a single ionic HD reaction.

IMPORTANT: The 2021 rovibrational levels belong to a NEUTRAL H+HD collision
article, whereas GL2022 rate source is the IONIC H+ + HD -> D+ + H2 process.
The ground endothermicity is a separate 2019 ionic reference. Combining these
is a *cross-paper diagnostic*, not a physical energy-source admission, Q bound,
revised SQM rate, detailed-balance rate, or energy deposition calculation.
"""
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, localcontext
from pathlib import Path
import hashlib
import json
import math

ION_RATE_PDF_SHA256 = 'a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754'
E_CHARGE_EXACT_C = Decimal('1.602176634e-19')  # exact J/eV in 2019 SI
SOURCE_2021_DOI = '10.1093/mnras/stab2381'
SOURCE_2019_DOI = '10.1093/mnras/stz1797'
REQUIRED_STATES = ('HD_v0_j0', 'HD_v0_j2', 'H2_v0_j0', 'H2_v0_j1')
EXPECTED_LEVEL_LITERALS = ('0.2344204966', '0.2675344527', '0.2702721432', '0.2849632856')
EXPECTED_GROUND_LITERALS = ('39.5', '35.8', '3.7')

class ProjectionContractError(ValueError):
    pass


def decimal_token(raw: object) -> Decimal:
    if type(raw) is not str or not 1 <= len(raw) <= 24:
        raise ProjectionContractError('exact finite decimal source token required')
    try:
        v = Decimal(raw)
    except Exception as exc:
        raise ProjectionContractError('invalid exact decimal source token') from exc
    if not v.is_finite():
        raise ProjectionContractError('non-finite source value')
    return v


def source_literals(path: str | Path) -> tuple[dict, str]:
    """Match pinned original article *transcription*, not original webpage byte SHA."""
    content = Path(path).read_bytes()
    payload = json.loads(content)
    if type(payload) is not dict or payload.get('schema') != 'wu.r22.cross_paper_literals.v1':
        raise ProjectionContractError('source transcription schema mismatch')
    n = payload['neutral_diatom_source']
    p = payload['ionic_ground_source']
    rate = payload['locked_ionic_rate']
    if (n.get('DOI') != SOURCE_2021_DOI or p.get('DOI') != SOURCE_2019_DOI
        or n.get('reaction') != 'NEUTRAL H + HD to D + H2, NOT ION H+ + HD'
        or rate.get('pdf_SHA256') != ION_RATE_PDF_SHA256 or rate.get('temperature_K') != 105
        or rate.get('rate_SQM_nominal_m3_s') != '1.15e-16'
        or rate.get('initial') != 'H+ + HD(v0,j2)'
        or rate.get('final') != 'D+ + H2(v0,j1)'
        or rate.get('DOI') != '10.1063/5.0128598'
        or rate.get('energy_source_pinned') is not False
        or payload.get('physical_Q_J_per_event') is not None
        or payload.get('source_uncertainty') is not None
        or payload.get('owner_ACK') is not None):
        raise ProjectionContractError('source/energy/owner authority mismatch')
    if tuple(n.get('states',{})) != REQUIRED_STATES:
        raise ProjectionContractError('noncanonical state order / wrong level labels')
    if tuple(n['states'].values()) != EXPECTED_LEVEL_LITERALS:
        raise ProjectionContractError('printed neutral-molecule values altered')
    keys = ('ground_to_ground_endothermicity_meV', 'zero_point_contribution_meV', 'ionization_potential_offset_meV')
    if tuple(p.get(k) for k in keys) != EXPECTED_GROUND_LITERALS:
        raise ProjectionContractError('2019 rounded ground values altered')
    return payload, hashlib.sha256(content).hexdigest()


@dataclass(frozen=True)
class Candidate:
    name: str
    threshold_eV: Decimal  # positive endothermic
    Q_eV: Decimal          # positive exothermic
    qualified: bool = False
    uncertainty: None = None

    def __post_init__(self):
        if self.qualified or self.uncertainty is not None:
            raise ProjectionContractError('cross-paper candidates cannot be physical energy estimates')
        if self.threshold_eV != -self.Q_eV:
            raise ProjectionContractError('threshold/release signs disagree')
        if self.threshold_eV <= 0:
            raise ProjectionContractError('expected endothermic candidate from pinned values')

    def as_json(self) -> dict:
        return {'name':self.name, 'threshold_eV_exact_literal':str(self.threshold_eV),
                'threshold_meV_exact_literal':str(self.threshold_eV * 1000),
                'Q_event_eV_exact_literal':str(self.Q_eV),
                'Q_event_J_diagnostic_exact_decimal':str(self.Q_eV * E_CHARGE_EXACT_C),
                'physical_source_admitted':False, 'uncertainty':None}


def projections(pinned: dict) -> tuple[Candidate, Candidate, Candidate, dict]:
    n = pinned['neutral_diatom_source']['states']
    g = pinned['ionic_ground_source']
    # All printed digits treated as EXACT DECIMAL STRINGS, not exact physics.
    h0,h2,p0,p1 = (decimal_token(n[k]) for k in REQUIRED_STATES)
    de_hd = h2-h0
    de_h2 = p1-p0
    ground = decimal_token(g['ground_to_ground_endothermicity_meV'])/1000
    ion = decimal_token(g['ionization_potential_offset_meV'])/1000
    neutral_only = p1-h2
    ionic_from_ground_rounded = ground - de_hd+de_h2
    ionic_from_neutral_plus_IP = neutral_only + ion
    cand = (
        Candidate('NEUTRAL_DONOR_BO_NO_ION_OFFSET', neutral_only, -neutral_only),
        Candidate('CROSS_PAPER_2019_GROUND_PLUS_2021_ROTATION', ionic_from_ground_rounded, -ionic_from_ground_rounded),
        Candidate('CROSS_PAPER_2021_NEUTRAL_PLUS_2019_IP', ionic_from_neutral_plus_IP, -ionic_from_neutral_plus_IP),
    )
    checks = {'neutral_ground_offset_eV':str(p0-h0),
              'HD_rotational_J2_minus_J0_eV':str(de_hd),
              'H2_rotational_J1_minus_J0_eV':str(de_h2),
              '2019_rounding_ground_eV':str(ground),
              '2019_ionization_split_eV':str(ion),
              'cross_paper_baseline_disagreement_eV':str(ionic_from_neutral_plus_IP-ionic_from_ground_rounded),
              'difference_is_physical_uncertainty':False,
              'same_PES_source':False}
    if (ionic_from_neutral_plus_IP-ionic_from_ground_rounded != (p0-h0+ion-ground)):
        raise AssertionError('source-offset decomposition failed')
    return *cand, checks


def with_r21_ledger(pinned: dict, literal_sha256: str, ledger: object, *, admit_physical: bool=False) -> dict:
    """Affine *illustration*; retains previous physical bath/Q JSON nulls."""
    if admit_physical:
        raise ProjectionContractError('no GL2022/PES-matched energy-source authority or owner ACK')
    from research.wu_hd_thermal_mechanical_ledger_r21_20261029.src.thermal_ledger import ConditionalCaloricLedger
    if type(ledger) is not ConditionalCaloricLedger or ledger.source_pdf_sha256 != ION_RATE_PDF_SHA256:
        raise ProjectionContractError('actual R21 verified-source caloric ledger required')
    a,b,c,checks=projections(pinned)
    with localcontext() as ctx:
        ctx.prec=75
        xi = Decimal(str(ledger.reaction_extent_events_per_ref_m3))
        intercept=Decimal(str(ledger.bath_known_intercept_J_per_ref_m3))
        rows=[]
        for cand in (a,b,c):
            delta=xi*cand.Q_eV*E_CHARGE_EXACT_C
            rows.append({**cand.as_json(), 'diagnostic_Q_times_extent_J_per_reference_m3':str(delta),
                         'diagnostic_conditional_bath_J_per_reference_m3':str(intercept+delta),
                         'physical_bath_energy_J_per_reference_m3':None,
                         'physical_Q_J_per_event':None})
    return {'schema':'wu.r22.cross_paper_energy_diagnostic.v1',
            'label':'DIAGNOSTIC_CROSS_SOURCE_ONLY_NO_PHYSICAL_Q',
            'source_literal_file_sha256':literal_sha256,
            'locked_rate_pdf_sha256':ION_RATE_PDF_SHA256,
            'sibling_R20_owner_preflight':'1a5c6f47350da2b74e0b7e3071c4db3502810500',
            'parent_R21_HEAD':'fd351d0ff97ef0d7a9cf710bdecad922af7e885e',
            'caloric_model':ledger.as_json(),
            'cross_paper_checks':checks,
            'candidates':rows,
            'invariants':{'canonical_WU_DAG':'34/49','R6_distinct_author':'NOT_RUN',
                          'C9_distinct_author':'NOT_RUN','HH_R10':'OFF',
                          'production':'NOT_ISSUED','L4':False,'owner_ACK':False},
            'source_uncertainty':None,
            'physical_state_energy_Q':None,
            'physical_bath_heat':None,
            'full_A':None}


def run_from_r21_source(source_path: str | Path, source_pdf: str | Path, schedule_json: str | Path,
                        initial_state=(1e6,1e6,0.,0.)) -> dict:
    from research.wu_hd_source_bound_r18_20261029.src.native_rates import load_native_grid
    from research.wu_hd_source_grid_r20_20261029.src.grid_exposure import Segment
    from research.wu_hd_thermal_mechanical_ledger_r21_20261029.src.thermal_ledger import build_ledger
    pinned,digest=source_literals(source_path)
    grid=load_native_grid(source_pdf)
    schedule=json.loads(Path(schedule_json).read_text(encoding='utf8'))
    if schedule.get('schema')!='wu.r20.schedule.v1':
        raise ProjectionContractError('invalid parent schedule')
    segments=[Segment(**s) for s in schedule['segments']]
    flow,ledger=build_ledger(grid,initial_state,segments)
    result=with_r21_ledger(pinned,digest,ledger)
    result['parent_source_flow']=flow.as_json()
    return result


def main(argv=None) -> int:
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--literal-source',type=Path,required=True)
    parser.add_argument('--source-pdf',type=Path,required=True)
    parser.add_argument('--schedule',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args(argv)
    try:
        result=run_from_r21_source(args.literal_source,args.source_pdf,args.schedule)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('x',encoding='utf8') as stream:
            json.dump(result,stream,indent=2,ensure_ascii=False);stream.write('\n')
    except (ProjectionContractError, ValueError, OSError, TypeError) as exc:
        parser.exit(2, f'{type(exc).__name__}: {exc}\n')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
