# WU088_HH R21 | Reactive HD exact-flow thermal/mechanical energy ledger

2026-10-29. Research unit: `WU_HD_REACTIVE_STATE_ENERGY_LEDGER_R21`. WU-only auxiliary; the proposed source-qualified physical `Q_event` is NOT yet supplied. Parent WU PR157 HEAD `52f9ff3213ac8f156bc47d610624cce061fdf485`; sibling WU PR158 HEAD `1a5c6f47350da2b74e0b7e3071c4db3502810500` is referenced by immutable identity, NOT merged. Canonical science 34/49, HH_R10 OFF, L4 false, production NOT_ISSUED.

## R1-R3. Authority, definitions, applicability
Original DIGITAL.CSIC GL2022 supplementary PDF (`a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`, 273554 bytes): Table 2, source-native SQM H+ + HD(v=0,j=2) -> D+ + H2(v'=0,j'=1), printed rate at discrete 105 K `1.15e-16 m^3 s^-1`; other supported original grid temperatures are 15,55,105,255,505,1005,1505,2005,2505,3005 K. R20 PR157 exact nonautonomous source-grid flow and R20 PR158 density/clock conversion can be reused under same identity. No Boltzmann-population or spin 3/4 multiplication is permitted. Printed rate nominal is not a physical uncertainty interval.

Define physical number densities `n=(H+,HD02,D+,H201)` [m^-3], reference volume ratio `v(t)=V(t)/V0>0`, proper time t [s], chemical comoving numbers `N=v*n` [reference m^-3], stoichiometry `nu=(-1,-1,+1,+1)` and extent `xi` [events per reference m^3]. Source-locked nonautonomous forward reaction `dN/dt=nu [k(T)/v] N1 N2` gives `d xi/dt=(k/v)(a-xi)(b-xi)>=0`; R20 exact exposure `A=int k(T)/v dt`, `N=N0+nu xi(A)`. Source spectral states are *fixed labels*; no internal-state excitation or de-excitation beyond this single reaction. Reaction is externally thermostatted and volume/temperature history externally prescribed, not a coupled Einstein/thermodynamic evolution.

Introduce **not-yet-admitted** constant species state reference energies `e_i` [J/particle, including the selected rovibrational state and correct asymptotic masses]. The event energy release is

`Q_event = -(e^T nu) = e_H+ + e_HD02 - e_D+ - e_H201` [J/event].

Gauge shifts `e -> e + alpha_h*h + alpha_d*d + alpha_q*q` do not change Q, since conserved covectors `h=(1,1,0,2)`, `d=(0,1,1,0)`, `q=(1,0,1,0)` annihilate nu. A common arbitrary shift of all four e_i also leaves Q invariant because `sum_i nu_i=0`. A source-native reaction rate does **not** determine these energies or physical Q. The 2019 Lepers, Guillon & Honvault primary paper (*MNRAS* 488, 4732, DOI10.1093/mnras/stz1797, Section 1) states a 39.5 meV **ground-(0,0) to ground-(0,0)** endothermicity, decomposed as 35.8 meV zero-point difference and 3.7 meV ionization-potential difference; it also notes a Born-Oppenheimer scattering approximation omitting a ~3 meV isotope ionization offset. These are NOT the requested HD(0,2)->H2(0,1) Q. Transporting 39.5 meV directly to the present channel would violate the state contract. This separate spectroscopy/PES convention must be reconciled before Q can be admitted. Independently authenticate spectroscopy/zero-point and asymptotic ion masses before a physical Q value is issued.

## R4-R5. Constructive caloric model and exact identity
Assume a *dilute classical ideal mixture*: all four species have Maxwellian **translational** kinetic energy `(3/2)k_B T` per particle and ideal pressure `p=n_tot k_B T`; chemical/rovibrational energy is solely in the fixed e_i. This is a declared auxiliary closure, not a complete molecular partition function. The reaction conserves particle count `nu·1=0`, hence `N_tot=sum_i N_i=sum_i N_i(0)` is constant. Keep `k_B=1.380649e-23 J K^-1` explicit and `c,hbar` implicit in not-yet-sourced e_i. The chosen metric signature is (-,+,+,+) but no spacetime equations are solved.

Material internal energy per reference volume [J m^-3(ref)]:
`U_mat = sum_i e_i N_i + (3/2) N_tot k_B T`.
With `d(e·N)=-Q_event dxi`, obtain
`dU_mat = -Q_event dxi + (3/2) N_tot k_B dT`.
Mechanical pressure work by the material, referred to V0, is
`dW_by = p d(V/V0) = N_tot k_B T d(ln v)`.
Define `dB` [J m^-3(ref)] as **heat entering the bath from the material**. The material first law `dU_mat = -dB-dW_by` gives the exact differential identity

`dB = Q_event dxi - (3/2)N_tot k_B dT - N_tot k_B T d(ln v)`.

It follows for arbitrary externally prescribed positive v and piecewise T, interpreted as a Stieltjes integral at T-jumps,
`Delta B = Q_event xi_f - (3/2)N_tot k_B(T_f-T_i) - N_tot k_B int T d(ln v)`.

For R20 segments with exact source-grid T_i and prescribed constant theta_i = d ln v/dt, duration dt_i>0,
`W_by = N_tot k_B sum_i (T_i theta_i dt_i)`, `Delta U_trans=(3/2)N_tot k_B(T_final-T_initial)`,
`Delta B = Q_event xi_f - Delta U_trans - W_by`.
Within each segment, work is EXACT even when the chemistry rate is time dependent because N_tot is conserved. This is **not** an approximation using endpoint volume or midpoint pressure. A discontinuous T jump contributes to `Delta U_trans` but causes no instantaneous pressure-volume work at continuous v.

In particular, the R19 formal bath ledger `B=Q xi` is a special limit for constant T and `v=1`, not the general prescribed-volume isothermal law. Isothermal expansion draws bath heat `+W_by` into the gas, so heat entering bath is `Q xi - W_by`. Compression reverses the sign of the pressure-work correction. Setting Q=0 as a *synthetic null test* is not a physical attribution of the H+ + HD channel.

## R6-R8. Mathematical checks and limit tests
(1) H/D/charge and particle-count left covectors; (2) gauge invariance of Q; (3) bath sign through first law; (4) dimensions: Q [J/event], xi [events m^-3(ref)], N k_B T [J m^-3(ref)]; (5) T constant,v=1: `B=Q xi`; (6) expansion theta>0 with Q=0: `B=-Ntot k_B T ln v`; (7) compression theta<0 reverses work sign; (8) T jump v=1: `B=Q xi-(3/2)Ntot k_B Delta T`; (9) nonreactive a=0: xi=0 but thermal/mechanical bath terms need not vanish; (10) Theta=0 limit continuous.

The ledger is **affine in an unknown Q**: `B(Q)=xi_f*Q + B_known`; `B_known=-(Delta U_trans+W_by)`. Before source-qualified Q and energy-owner admission, report only these two coefficients, do NOT issue a physical bath heat number. This model does not specify collisions of the bath or heat capacity of omitted degrees, reverse reactions, full network, entropy production, observed CMB heating or physical Q. Strong stability or observational inference is not established.

## R9-R10. Implementation contract, provenance, stop condition
A read-only R21 module invokes R20's original `load_native_grid(PDF)` and `evolve_source_grid(grid,n0,segments)` to produce the exact source-locked extent, then computes `xi_coeff` and `B_known` with compensated arithmetic. Output a symbolic affine ledger and quantities `W_by`, `Delta U_trans`, total count and source hashes; JSON must contain `physical_Q_J: null`, `physical_bath_energy_J_per_ref_m3: null`, `owner_bound:false`, `L4:false`, `production:NOT_ISSUED`. A separately provided `Q_synthetic` is permitted solely for testing the algebra and must never be labeled physical. Match numerical source identity rather than fabricating grids. Test stiff, zero extent, expansion/contraction, temperature discontinuity, sign, units, and negative inputs. R6 distinct-author independent review remains NOT_RUN if delegation is not exposed; in-context or CAS checks are not independent-author.

Source ownership: GL2022 DOI10.1063/5.0128598; original R18 NativeGrid module blob `be2a845263b215b604f255ffe5deabe55be9dd7b`; WU R20 PR157 exact-flow `grid_exposure.py`; WU R20 PR158 owner preflight. Other-owner REC/CR/REI/BASS/HE modifications are forbidden absent actual owner ACK. Canonical WU 34/49 remains unchanged; R21 only auxiliary.
