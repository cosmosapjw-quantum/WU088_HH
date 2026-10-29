"""R24 isolated threshold provenance and inverse-temperature diagnostic.

The external BO-j2->j0 approximate value and spectroscopy H2 rotation do
NOT constitute the GL2022 SQM PES-native j2->j1 threshold. This module never
emits physical Q, reverse rates, bath heat or a corrected GL2022 rate.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
from zipfile import ZipFile

SCHEMA="wu.r24.source_native_threshold_diagnostic.v1"
TARGET="H+ + HD(X,v=0,j=2) -> D+ + H2(X,v'=0,j'=1,ortho)"
R21_SHA="5ace176fdba1b1ed01cedbd11e381b98ee242475ef1a401d89dcfcf0b7a3d220"
R23_SHA="3d05412495bda39b949d835725426e704e9bcb6a1f548eb60bbb3d93f17750c6"
PDF_SHA="a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754"
R18_BLOB="be2a845263b215b604f255ffe5deabe55be9dd7b"
TEMPS=(15,55,105,255,505,1005,1505,2005,2505,3005)
TOKENS=("3.99(14)","2.92(11)","1.15(10)","2.74(10)","3.33(10)","3.18(10)","2.85(10)","2.55(10)","2.30(10)","2.08(10)")
H=Decimal("6.62607015e-34")
C=Decimal("299792458")
E=Decimal("1.602176634e-19")
KB=Decimal("1.380649e-23")

class AuditContractError(ValueError):pass


def byte_sha(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strict_source(record_path:Path)->tuple[dict,str]:
    raw=Path(record_path).read_bytes()
    record=json.loads(raw)
    if not isinstance(record,dict) or record.get("schema")!=SCHEMA or record.get("scope")!=TARGET:
        raise AuditContractError("wrong source schema or ionic state target")
    if (record.get("base_r23_head")!="2f214319ca8600475b1d4e85d1ca21a0249136a8" or
        record.get("r23_source_zip_sha256")!=R23_SHA or
        record.get("r21_source_zip_sha256")!=R21_SHA or
        record.get("r21_native_rate_module_blob")!=R18_BLOB or
        record.get("gl2022_supplement_pdf_sha256")!=PDF_SHA):
        raise AuditContractError("source lineage or parent HEAD mismatch")
    gl=record["gl2022"]
    if (gl.get("doi")!="10.1063/5.0128598" or gl.get("method")!="SQM" or
        gl.get("PES")!="Velilla2008 H3+ global electronic ground PES" or
        gl.get("source_rate_temperature_K")!=list(TEMPS) or
        gl.get("source_row_tokens")!=list(TOKENS) or
        gl.get("native_PES_state_threshold_meV") is not None or
        gl.get("nuclear_mass_convention_verified") is not False or
        gl.get("IP_isotope_offset_application_verified") is not False):
        raise AuditContractError("GL2022 typed source or physical threshold tampered")
    vel=record["velilla2008"]
    if (vel.get("doi")!="10.1063/1.2973629" or
        vel.get("electronic_H2_plus_Hplus_above_H3plus_minimum_cm1")!="37170" or
        vel.get("this_value_is_isotopic_rovibrational_threshold") is not False or
        vel.get("original_EPAPS_and_GL2022_channel_input_bytes_obtained") is not False):
        raise AuditContractError("electronic PES limit incorrectly promoted")
    lep=record["lepers2019"]
    if (lep.get("doi")!="10.1093/mnras/stz1797" or
        lep.get("BO_j2_to_j0_endothermic_meV_printed_approx")!="3.4" or
        lep.get("end_state")!="H2(v'=0,j'=0)" or
        lep.get("same_numerical_SQM_channel_threshold_verified") is not False or
        lep.get("target_state_is_not_j0") is not True):
        raise AuditContractError("2019 approximate BO wrong-state provenance")
    sp=record["external_spectroscopy"]
    if (sp.get("H2_J1_minus_J0_cm1")!="118.48684" or
        sp.get("R23_molecular_ionization_threshold_meV")!="20.95002099384045759056749544382632657967" or
        sp.get("external_source_is_GL2022_PES_native") is not False):
        raise AuditContractError("spectroscopy source mismatch")
    gates=record["null_gates"]
    for key in ("physical_Q_J_per_event","physical_bath_heat_J_per_ref_m3","reverse_rate", "GL2022_PES_threshold_meV","actual_REC_CR_owner_ACK"):
        if key not in gates or gates[key] is not None:
            raise AuditContractError("physical source or owner falsely admitted: "+key)
    if gates.get("HH_R10")!="OFF" or gates.get("production")!="NOT_ISSUED" or gates.get("L4") is not False or gates.get("canonical_WU_DAG")!="34/49_UNCHANGED":
        raise AuditContractError("science DAG or production promoted")
    return record,hashlib.sha256(raw).hexdigest()


def inspect_native_rate_zip(r21_zip:Path)->tuple[tuple[int,...],tuple[str,...],tuple[Fraction,...],dict]:
    """Actual original R18 PDF-verified parser, not a new PDF table transcription."""
    if byte_sha(r21_zip)!=R21_SHA: raise AuditContractError("R21 binary source identity mismatch")
    with ZipFile(r21_zip) as z:
        if z.testzip() is not None:raise AuditContractError("source zip CRC failed")
        mp="research/wu_hd_source_bound_r18_20261029/src/native_rates.py"
        pp="ORIGINAL_SOURCES/GL2022_CSIC_supplement.pdf"
        module_data=z.read(mp)
        blob=hashlib.sha1(b"blob "+str(len(module_data)).encode()+b"\0"+module_data).hexdigest()
        if blob!=R18_BLOB:raise AuditContractError("original R18 native loader Git blob mismatched")
        pdf=z.read(pp)
        if len(pdf)!=273554 or hashlib.sha256(pdf).hexdigest()!=PDF_SHA:
            raise AuditContractError("source original supplementary PDF identity mismatch")
        with tempfile.TemporaryDirectory(prefix="r24_source_") as tmp:
            p=Path(tmp);(p/"native_rates.py").write_bytes(module_data);(p/"native.pdf").write_bytes(pdf)
            spec=importlib.util.spec_from_file_location("wu_r24_verified_native_r18",str(p/"native_rates.py"))
            mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod
            try:
                spec.loader.exec_module(mod)
                grid=mod.load_native_grid(p/"native.pdf")
                temperatures=tuple(c.temperature_K for c in grid.cells)
                tokens=tuple(c.original_token for c in grid.cells)
                rates=tuple(c.nominal_m3_s for c in grid.cells)
                source_sha=grid.source_sha256
                page_sha=grid.extracted_page_sha256
            finally:sys.modules.pop(spec.name,None)
    if temperatures!=TEMPS or tokens!=TOKENS or source_sha!=PDF_SHA:
        raise AuditContractError("original source ten nodes or printed tokens mismatched")
    return temperatures,tokens,rates,{"pdf_sha256":source_sha,"r18_git_blob":blob,"page_text_sha256":page_sha,"rate_interpolation":False,"uncertainty":None}


def shift_laplace_factor(delta_meV:Decimal,T_K:int)->Decimal:
    """Only for rigid shift E*sigma_D(E)=g(E-D)*1[E>=D]; NOT GL2022 rate."""
    if type(T_K) is not int or T_K<=0 or type(delta_meV) is not Decimal or not delta_meV.is_finite():
        raise AuditContractError("finite shift and strictly positive integer K required")
    with localcontext() as ctx:
        ctx.prec=70
        return (-delta_meV/(KB*Decimal(1000)*Decimal(T_K)/E)).exp()



def _as_positive_decimal_rate(rate:Fraction)->Decimal:
    if type(rate) is not Fraction or rate<=0:
        raise AuditContractError("positive source-verified rational rate required")
    return Decimal(rate.numerator)/Decimal(rate.denominator)


def threshold_upper_bound_meV(Tcold:int,Thot:int,rate_cold:Fraction,rate_hot:Fraction)->Decimal:
    """Maxwellian one-channel support upper bound from two *nominal* k(T) values.

    If sigma(E)>=0, independent of T, and sigma(E)=0 below E=Delta,
    F(beta)=k(T)/beta**(3/2)/C is the Laplace transform of E*sigma(E).
    For beta_c>beta_h, F_c/F_h<=exp[-Delta*(beta_c-beta_h)].
    Consequently Delta<=k_B*ln[F_h/F_c]/(1/Tcold-1/Thot).
    This is not a measured/source uncertainty nor proof about GL2022 implementation.
    """
    if type(Tcold) is not int or type(Thot) is not int or not 0<Tcold<Thot:
        raise AuditContractError("strictly increasing positive integer temperatures required")
    with localcontext() as ctx:
        ctx.prec=70
        rc,rh=_as_positive_decimal_rate(rate_cold),_as_positive_decimal_rate(rate_hot)
        tc,th=Decimal(Tcold),Decimal(Thot)
        log_F_ratio=(rh/rc).ln()+Decimal('1.5')*(th/tc).ln()
        return (KB*Decimal(1000)/E)*log_F_ratio/(Decimal(1)/tc-Decimal(1)/th)


def rounded_mantissa_15_55_meV_bound()->Decimal:
    """Bound using only +/-0.005 on the 3-digit mantissas, not rate errors."""
    return threshold_upper_bound_meV(15,55,Fraction(3985,10**23),Fraction(2925,10**20))


def support_discrepancy_factor(Tcold:int,Thot:int,rate_cold:Fraction,rate_hot:Fraction,
                               candidate_threshold_meV:Decimal)->Decimal:
    """Observed F_c/F_h divided by maximum F_c/F_h for candidate Delta.

    Factor >1 rejects the candidate under *all* shared-T-independent nonnegative
    sigma(E) with threshold >= candidate Delta; factor<=1 is only necessary.
    """
    if type(candidate_threshold_meV) is not Decimal or not candidate_threshold_meV.is_finite():
        raise AuditContractError("finite Decimal candidate threshold required")
    with localcontext() as ctx:
        ctx.prec=70
        bound=threshold_upper_bound_meV(Tcold,Thot,rate_cold,rate_hot)
        dbeta=(E/(Decimal(1000)*KB))*(Decimal(1)/Decimal(Tcold)-Decimal(1)/Decimal(Thot))
        return ((candidate_threshold_meV-bound)*dbeta).exp()


def calculate(record:dict,digest:str,temperatures:tuple[int,...],tokens:tuple[str,...],rates:tuple[Fraction,...],source:dict,*,admit_physical:bool=False)->dict:
    if admit_physical:raise AuditContractError("physical GL2022 PES-native threshold is unresolved")
    if temperatures!=TEMPS or tokens!=TOKENS or len(rates)!=len(TEMPS) or not all(x>0 for x in rates):
        raise AuditContractError("original rate source not verified")
    with localcontext() as ctx:
        ctx.prec=70
        mev_per_cm1=H*C*Decimal(100)*Decimal(1000)/E
        j1_spect=Decimal(record["external_spectroscopy"]["H2_J1_minus_J0_cm1"])*mev_per_cm1
        j2j0_printed=Decimal(record["lepers2019"]["BO_j2_to_j0_endothermic_meV_printed_approx"])
        mixed=j2j0_printed+j1_spect
        external=Decimal(record["external_spectroscopy"]["R23_molecular_ionization_threshold_meV"])
        difference=external-mixed
        # The rigid shape g(y) is unknown for actual GL2022. This is a pure sensitivity fixture.
        toy=[str(shift_laplace_factor(difference,t)) for t in TEMPS]
        support_bounds=[]
        for i in range(len(TEMPS)-1):
            support_bounds.append({
                "start_K":TEMPS[i],"end_K":TEMPS[i+1],
                "max_threshold_meV_from_positive_Laplace_support":str(
                    threshold_upper_bound_meV(TEMPS[i],TEMPS[i+1],rates[i],rates[i+1]))})
        support_lim=min(Decimal(z["max_threshold_meV_from_positive_Laplace_support"]) for z in support_bounds)
        conservative=rounded_mantissa_15_55_meV_bound()
        factors={"mixed_BO2019_plus_spectroscopy":str(support_discrepancy_factor(
                    15,55,rates[0],rates[1],mixed)),
                 "external_R23_spectroscopy":str(support_discrepancy_factor(
                    15,55,rates[0],rates[1],external))}
        barriers=[]
        for i in range(len(TEMPS)-1):
            ti,tj=map(Decimal,(TEMPS[i],TEMPS[i+1]))
            ki=Decimal(rates[i].numerator)/Decimal(rates[i].denominator)
            kj=Decimal(rates[i+1].numerator)/Decimal(rates[i+1].denominator)
            # For toy sigma_D(E)=G(E-D)/E, k(T)*sqrt(T) proportional exp(-D/kT).
            b=(KB*Decimal(1000)/E)*((kj/ki).ln()+(tj/ti).ln()/2)/(1/ti-1/tj)
            barriers.append({"start_K":int(ti),"end_K":int(tj),"effective_barrier_p0_meV":str(b),
                             "is_PES_threshold":False})
        out={
            "schema":"wu.r24.threshold_convention_stress.v1",
            "source_contract_sha256":digest,"source_original":source,
            "state_target":TARGET,
            "reference_categories":{
                "Velilla2008_37170_cm1":"ELECTRONIC_PES_GEOMETRY_ABOVE_H3PLUS_MINIMUM_NOT_ISOTOPIC_02_TO_01",
                "Lepers2019_3p4_meV":"BO_TIQM_APPROXIMATE_02_TO_00_DIFFERENT_OUTPUT_STATE",
                "R23_20p950_meV":"EXTERNAL_SPECTROSCOPY_CYCLE_NOT_GL2022_PES"
            },
            "conditional_literature_cross_path":{
                "j2_to_j0_2019_BO_printed_approx_meV":str(j2j0_printed),
                "H2_j1_from_external_spectroscopy_meV":str(j1_spect),
                "mixed_j2_to_j1_threshold_meV_NOT_PES":str(mixed),
                "external_R23_candidate_meV":str(external),
                "cross_model_difference_meV_NOT_UNCERTAINTY":str(difference),
                "qualified_PES_native":False,"uncertainty":None
            },
            "source_grid":[{"T_K":t,"native_token":tok,"k_m3_per_s_exact":{"numerator":str(k.numerator),"denominator":str(k.denominator)}} for t,tok,k in zip(temperatures,tokens,rates)],
            "positive_Laplace_support_test":{
                "scope":"NECESSARY_CONDITION_FOR_SINGLE_T_INDEPENDENT_NONNEGATIVE_SIGMA_WITH_STRICT_ENDOTHERMIC_THRESHOLD",
                "thermal_formula":"k(T)=C*beta^(3/2)*integral_Delta^inf[E*sigma(E)*exp(-beta*E)]dE, beta=1/(k_B*T)",
                "proof":"F(beta)=k(T)/beta^(3/2)/C; for beta_c>beta_h: F_c/F_h<=exp[-Delta*(beta_c-beta_h)]",
                "adjacent_nominal_threshold_upper_meV":support_bounds,
                "global_nominal_upper_meV":str(support_lim),
                "15_55_last_digit_rounding_only_conservative_upper_meV":str(conservative),
                "last_digit_rounding_assumption":"source mantissas 3.99 and 2.92 rounded to nearest 0.01; not source rate uncertainty",
                "candidate_15_55_violation_factors":factors,
                "conditional_rejections":{"mixed_BO2019_plus_spectroscopy":bool(mixed>support_lim),
                                          "external_R23_spectroscopy":bool(external>support_lim)},
                "GL2022_algorithm_inconsistent_certified":False,
                "PES_threshold_certified":False,
                "unknowns":["verify GL2022 Eq4 E reference and input cross sections", "resolve isotope and rovibrational channel opening", "check source-native cross-section and quadrature at 15/55K"],
                "source_rate_uncertainty":None
            },
            "model_rejection":{
                "assumed_toy_sigma":"E*sigma_D(E)=g(E-D)*indicator(E>=D), g independent of D",
                "rigid_shift_factor_toy_only_vs_T": [{"T_K":t,"exp_minus_delta_over_kBT":z} for t,z in zip(temperatures,toy)],
                "p0_effective_barriers":barriers,
                "single_p0_arrhenius_threshold_fits_all_source_nodes":False,
                "reason":"the nine adjacent p=0 inverse-temperature secants are not constant",
                "actual_Gl2022_cross_section_shape_known":False,
                "measured_or_source_rate_changed":False
            },
            "claims":{"GL2022_native_PES_threshold_meV":None,"physical_Q_J_per_event":None,"physical_bath_heat_J_per_ref_m3":None,"source_rate_uncertainty":None,"reverse_rate":None,"REC_CR_owner_ACK":None,"full_A":None,"HH_R10":"OFF","production":"NOT_ISSUED","L4":False,"canonical_DAG":"34/49_UNCHANGED","R6_distinct_author":"NOT_RUN","C9_distinct_author":"NOT_RUN"}
        }
        return out


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source",type=Path,required=True)
    p.add_argument("--r21-original-zip",type=Path,required=True)
    p.add_argument("--r23-original-zip",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    ns=p.parse_args(argv)
    rec,digest=strict_source(ns.source)
    if byte_sha(ns.r23_original_zip)!=R23_SHA:raise AuditContractError("immutable parent R23 zip mismatch")
    tt,ts,kr,src=inspect_native_rate_zip(ns.r21_original_zip)
    result=calculate(rec,digest,tt,ts,kr,src)
    ns.output.parent.mkdir(parents=True,exist_ok=True)
    with ns.output.open("x",encoding="utf-8") as stream:
        json.dump(result,stream,indent=2,ensure_ascii=False);stream.write("\n")
    return 0
if __name__=="__main__":raise SystemExit(main())
