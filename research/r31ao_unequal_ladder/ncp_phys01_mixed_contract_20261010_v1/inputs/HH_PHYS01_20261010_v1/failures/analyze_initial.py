"""New pointwise physical coefficients from existing selected source bytes.

Uses exact binary64-to-real input conversion and 90-digit scalar arithmetic.
This is not an interval certificate or a rerun of the source solver.
"""
import argparse,json,hashlib,sys
from pathlib import Path
import mpmath as mp
from fractions import Fraction
from src.mixed_response import factors,energy_factor,temperature_factor
mp.mp.dps=90
ROOT=Path(__file__).resolve().parent

def exact_float(value):
    p,q=float(value).as_integer_ratio();return mp.mpf(p)/q

def show(v):return mp.nstr(v,75)

def compute():
    raw=(ROOT/'inputs/SELECTED_SOURCE.json').read_bytes();d=json.loads(raw)
    x,he1,he2,w=map(exact_float,d['old_gas'])
    nH=exact_float(d['n_h_cm3']);nHe=exact_float(d['n_he_cm3']);r=nHe/nH
    ev=exact_float(1.602176634e-12);kb=exact_float(1.380649e-16)
    C=2*ev/(3*kb);Pi=1+r+x+r*(he1+2*he2);T=C*w/Pi;u=1-x
    chi=exact_float(13.598434599702);E=exact_float(d['energies_ev'][24]);g=E-chi
    sig=exact_float(d['sigma_cm2'][24][0]);a=exact_float(29979245800.0)*nH*sig
    pref=exact_float(1.2e-17);power=exact_float(1.2);activation=exact_float(157800.0)
    k=pref*T**power*mp.exp(-activation/T);q=nH*u*u*k
    logder=power/T+activation/T**2
    Tg=C*g;beta=u/Pi*logder*(T-Tg)
    macro=exact_float(1250000000.0);S=exact_float(5e-15)
    scale=a*q*S*macro**3
    fs=factors(beta);wf=energy_factor(beta,chi,g)
    tf=temperature_factor(beta,chi,g,C,T,Pi,u)
    out={}
    for method,v in fs.items():
        out[method]={'dimensionless_factors':{j:show(mp.mpf(val)) for j,val in v.items()},
          'cubic_mixed_scale_x':show(scale*v['x']),
          'cubic_mixed_scale_P_per_H':show(scale*v['P']),
          'cubic_mixed_scale_J_HH_per_H':show(scale*v['J_HH']),
          'cubic_mixed_scale_J_photo_per_H':show(scale*v['J_photo']),
          'cubic_mixed_scale_w_eV_per_H':show(scale*wf[method]),
          'cubic_mixed_scale_T_K':show(scale*tf[method]),
          'cubic_mixed_scale_ne_cm3':show(nH*scale*v['x'])}
    defect={'x':show(scale*(fs['BE_two_half']['x']-fs['BE_full']['x'])),
            'T_K':show(scale*(tf['BE_two_half']-tf['BE_full'])),
            'w_eV_per_H':show(scale*(wf['BE_two_half']-wf['BE_full']))}
    # Independent local directional derivative of q, no evolution and no root solve.
    def q_photo(s):
        xs=x+s;ws=w+g*s;ts=C*ws/(Pi+s)
        return nH*(1-xs)**2*pref*ts**power*mp.exp(-activation/ts)
    qdir=mp.diff(q_photo,mp.mpf(0))
    expected=q*(-2/u+logder*(Tg-T)/Pi)
    checks={}
    def check(name,value):
        assert value,name
        checks[name]=True
    check('directional_q_90digit',abs((qdir-expected)/expected)<mp.mpf('1e-80'))
    for method,v in fs.items():
        check(method+'_x_event_sum',abs(v['x']-v['J_HH']-v['J_photo'])<mp.mpf('1e-80'))
        check(method+'_photon_event_sum',v['P']==-v['J_photo'])
        check(method+'_energy',abs(wf[method]+chi*v['x']+E*v['P'])<mp.mpf('1e-80'))
        check(method+'_HHe_mixed_sign',v['x']<0)
        check(method+'_w_mixed_sign',wf[method]>0)
        check(method+'_T_mixed_sign',tf[method]>0)
    # Selected smooth source data only; all energies outside support are not evaluated.
    check('LCS_temperature_domain',mp.mpf(35000)<T<mp.mpf(60000))
    check('neutral_positive',0<u<1)
    check('soft_HI_only_birth',exact_float(13.6)<E<exact_float(24.587389011))
    check('near_threshold_thermal_suppression',Tg<T)
    check('no_prior_root_value_used',d['old_gas']!=d['point_gas'])
    # Step-halving scaling follows cubic homogeneity, not observed solver convergence.
    check('algebraic_half_duration_eighth_scale',a*q*S*(macro/2)**3==scale/8)
    return {'task':'HH-PHYS01','status':'DERIVED_LOCAL_ASYMPTOTIC_COEFFICIENTS__POINT_ARITHMETIC_CHECKED',
      'input_sha256':hashlib.sha256(raw).hexdigest(),
      'source_location':d['source_locator'],'local_initial_point':'selected old_gas; not a new physical initial history',
      'constants_semantics':'exact reals of recorded binary64 constants/counts; mathematical pow/exp; not native rounding replay',
      'parameters':{'x':show(x),'neutral':show(u),'nH_cm3':show(nH),'nHe_cm3':show(nHe),'particles_per_H':show(Pi),
        'T_K':show(T),'E_eV':show(E),'chi_eV':show(chi),'excess_eV':show(g),'T_gamma_K':show(Tg),
        'k_LCS_cm3_s':show(k),'q_HH_s':show(q),'a_per_s':show(a),'beta_thermal':show(beta),
        'sigma_cm2':show(sig),'logarithmic_k_temperature_slope':show(T*logder),
        'dlogq_per_photoevent_neutral':show(-2/u),'dlogq_per_photoevent_thermal':show(logder*(Tg-T)/Pi),
        'thermal_to_depletion_ratio':show(beta/2),
        'duration_s':show(macro),'source_S_per_H_s':show(S),'AqS_duration3':show(scale),
        'photo_hazard_duration':show(a*u*macro),'a_duration':show(a*macro),
        'HH_fractional_time_scale':show(q*macro),'current_photon_inventory_per_H':show(sum(exact_float(t) for t in d['old_point_photons']))},
      'coefficients':out,'mixed_BE_two_half_minus_full_cubic_scale':defect,
      'checks':checks,'check_count':len(checks),
      'claims':{'coefficient_general_base_HHe_retained':True,'finite_strength_coefficient_through_cubic':True,
         'actual_finite_duration_response_bound':False,'full_owner_macro_defect':False,'physical_fit_certification':False,
         'actual_new_native_or_IVP_or_root':0,'all_time_or_parameter_interval_certificate':False,
         'reference_values_are_leading_term_diagnostics_only':True}}

if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--output',required=True);a=pa.parse_args();out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x') as f:json.dump(compute(),f,indent=2);f.write('\n')
    print('90-digit local physical coefficient checks complete')
