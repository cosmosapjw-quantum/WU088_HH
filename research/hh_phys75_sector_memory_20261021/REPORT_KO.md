# PHYS75: matter/radiation shear memory and finite collisionless 3-state representation

This is a compact Git report. The full Korean report, original raw new-control outputs, selected upstream data, figures, tests, failure logs and handoffs are in the source-bound FULL archive identified in DELIVERY.json. The archive is not a full Git clone.

## Current sources and reuse
Parent HH127 71e925938387b73958c8881a06ef387e6874fafe. REI198 8bd35af5f11c7ea5945b656be1c013d1c1933498 and REI213 d32cd99fa19c65aa1ca63dbc8aab8741834270e8 already contain separate-sector pilots. REI198 long1231 (625radiation+600matter+6mixed) and HH74 control63 are separately processed from immutable saved data. REI213 warm short729 is a different C15 HHe/UV model; its live publication/backup receipt was read, not all423MB raw. Do not replay these sweeps. No source/closure/rate/tolerance change or production merge.

## Definition and direct derivation
Proper-time H,s in s^-1; pressures in J/m^3. In the common normal orthonormal frame sigma=diag(-s,-s,2s), pi_A=diag(-p_A,-p_A,2p_A). K=8*pi*G/c^2. Source signed half-contraction coordinates are S_h=sqrt(3)*s/H and P_Ah=sqrt(3)*K*p_A/H^2. Full Frobenius magnitudes are sqrt(2)*abs of these. Matter and radiation remain separate. Total norm is the norm of their signed tensor sum, not the sum of norms.

From ds/dt+3Hs=K(p_m+p_r), with x=ln(a/a_i):
S_f=exp[-3(x_f-x_i)]*(H_i/H_f)*S_i + integral exp[3(x-x_f)]*(H/H_f)*P_m dx + analogous radiation term.
This is along the actual coupled path, not a counterfactual species-removal experiment. Sector energy work per ln(a) is -6(s/H)p_A; normalized by K/H^2 it is -2*S_h*P_Ah.

## Actual saved-data result
All5747 REI archive payloads and137 HH archive payloads verified. Long1231/80015samples and separateHH63/5103samples processed without ODE calls. Long maximum absolute memory closure is7.345344276397936e-12 in half convention; scalar scipy.simpson comparison differs by at most1.0842021724855044e-19. These are saved-node diagnostics, not continuum error bounds. Nearzero scaled residuals0.1819/0.5305 are retained; their absolute defects are~1e-20.

For initial half coordinates (S,Pi_m,Pi_r)=(0,+.0004,-.0004), final full-Frobenius signed shear is-6.941018368192255e-5. Separate full path contributions: matter+6.759995594823329e-5, radiation-1.3701013695216808e-4, absolute reconstruction defect2.6779877711232e-12. Initial stress cancellation does not cancel the histories.

## Exact finite-system reduction and actual controls
Original even-L8 collisionless owner has E'=b'*M*E with constant actual5x5M. Therefore E=exp[(b-bi)M]*Ei; no division by b', so zero crossings are allowed. New code marches only(tau,b,q), reconstructs E and calls the unchanged physical RHS. State8->3 is a62.5%coordinate reduction, not a measured speedup. This is NOT valid for UV/Thomson/noncommuting source paths and is not an infinite-angular theorem.

Prepared eigenbasis with expm1 and scipy.linalg.expm fallback; actual eigenvector condition4.003330611482946. E(0) preserves initial bytes. Three NEW-input paired controls (6actual IVPs), unchanged rtol3e-11/atol3e-13 and65samples: maximum physical-field difference3.6158685366629445e-11, reconstructed8-state difference2.6991120449793016e-10, direct-expm comparison1.1102230246251565e-16, within predeclared1e-8 comparison gate. Adaptive norms differ between3and8 coordinates; equality of tolerances is not a uniform accuracy guarantee.

18focused unit tests passed. Complex-input silent casts were corrected after two failing tests. Wolfram symbolic identities returned zero residuals WITH undefined-symbol warnings retained. Separate numerical algorithms are not independent-personnel review; native_subagent=NOT_RUN. Unavailable b was removed from HH packet rather than represented as a physical zero. Plot permission/overlap repairs and old attempts are preserved. Benchmark0, NCP0, completed-sweep replay0.

## Actual external reuse
SciPy expm (matrix exponential and fallback): https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.expm.html
SciPy simpson (independent sampled quadrature): https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.simpson.html
NumPy read-only sharing: https://numpy.org/doc/stable/reference/thread_safety.html
VigilODE reflecting-grid bounds are not transferred to this different system.

## Execution and limits
Recover FULL archive via DELIVERY and verify manifest. Run `python source/analyze.py analyze --packet packet --out results/replay_<UTC>` on a new output path to reproduce data processing. The six controls are already complete and are not a pending campaign. Code is opt-in; original defaults remain.
For genuinely new approved tasks reuse parent HH74 resources.py advisory leases, actual CPU/cgroup/free-memory checks, cap64CPU/128GiB, headroom16GiB, BLAS/OpenMP1. Other sessions are not a veto: smaller fitting chunks proceed; no foreign process signals or budget resets. New PHYS75 NCP queue is empty because requested pilots are already available.

Full cold EoR, general non-LRS, continuum accuracy and HH matched xi/rates remain separate obligations. HH_R10=OFF. Publication/backup closure is separately recorded by DELIVERY; no full CI/production claim.
