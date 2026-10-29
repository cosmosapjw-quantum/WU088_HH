# WU088_HH R22: state-resolved ionic H⁺+HD energy provenance

**Scoped theoretical result, no physical admission; 2026-10-29.** R21 Draft PR159 HEAD `fd351d0ff97ef0d7a9cf710bdecad922af7e885e`; separate R20 parent PR157 and sibling PR158. Central 34/49 and R21 18/20 unchanged; R6/C9 distinct-author NOT_RUN; `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`.

## 1. Energy zero, reaction and sign

Only this ionic reaction and specific rovibrational states:
`H+ + HD(X, v=0, J=2) -> D+ + H2(X, v=0, J=1, ortho)`.
Let E(H) and E(D) be neutral atomic internal ground-state references; set E(H+)=E(H)+I_H and E(D+)=E(D)+I_D. Define molecular 0K dissociation energies by E(HD,00)=E(H)+E(D)-D0(HD) and E(H2,00)=2E(H)-D0(H2). Then for the exact labelled states,

`delta_E = E_out - E_in = (I_D-I_H) + [D0(HD)-D0(H2)] + [epsilon_H2(01)-epsilon_HD(02)]`.

`Q_event = -delta_E` is energy *released* (negative for endothermic). Cancellation of all arbitrary atomic neutral-ground zeros is exact. The molecular rotations are above their respective J=0 levels and therefore cannot be replaced by a spin weight, thermal partition fraction, or the 2019 39.5 meV ground-to-ground endothermicity. Rest-mass and electronic asymptotic differences are contained consistently in the definition of dissociation energies and ionization potentials, rather than appended twice.

## 2. Authority and provenance chain

- Primary GL2022 González-Lezana, Hily-Blant & Faure, JCP 157, 214302, DOI 10.1063/5.0128598. Exact original source supplemental PDF SHA `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754` (273554 bytes), Table 2 SQM source-native rate, ten T nodes only. The supplementary source does NOT supply a physical `Q_event` nor explicitly fix a cross-method PES-native corrected threshold for this state.
- HD ground dissociation: Hölsch et al., PRA 108, 022811 (2023), Table IV `36405.78253(7) cm^-1`, DOI 10.1103/PhysRevA.108.022811. This directly supersedes 2010 Pachucki–Komasa `36405.7828(10)`. The 2023 experiment resolved a previous theory–experiment discrepancy. Its D0 is inferred from an ionization-energy cycle involving both atomic ionizations and HD+ dissociation, so the quoted marginal uncertainties cannot be treated independent of atomic I_H and I_D.
- H2 ground dissociation: Doran et al., PRX accepted 2026-08-31 DOI 10.1103/42c4-pc1s, `36118.0696646(58) cm^-1` from a 45-interval joint network, para-H2 (v=0,N=0).
- Atomic I_H `109678.77174307(10)` and I_D `109708.61455294(17) cm^-1`: Hölsch et al. (2023) Table IV rows 6/7, consistent with NIST ASD. Their difference includes the *isotopic ionization asymptotic correction* (~29.84280987 cm^-1 = ~3.7 meV).
- H2 J1-J0 `118.48684(10) cm^-1`: PRL 107 043005 (2011), experimental level comparison; note product J1 ortho and reference J0 para, explicitly not a thermal spin reweighting.
- HD J2-J0 `8,006,533,168(26) kHz`: Cozijn, Diouf & Ubachs, EPJD 76, 220 (2022), DOI 10.1140/epjd/s10053-022-00552-x, direct R(0)-P(2) combination difference. Convert with **exact** c=299792458 m/s.

## 3. Derived spectroscopy-level result and uncertainty policy

`delta_E = +168.973316084208608... cm^-1 = +20.950021151300... meV`.
`Q_spectroscopic_candidate = -20.950021151300... meV/event = -3.35656...e-21 J/event`.

The six quoted marginal uncertainty magnitudes, after unit conversion and absolute addition, sum to approximately `0.000176937 cm^-1 ≈ 0.000021937 meV`. This is **not a confidence interval, certified bound or independent Gaussian sigma**: HD D0 and atomic ionizations share a thermochemical cycle; 2026 H2 D0 also uses atomic IP; no joint covariance was supplied. A root-sum-square of these six errors is unjustified. The recorded figure is a diagnostic sum of literature error magnitudes, not an issued physical rate/heat uncertainty.

Equivalent thermochemical-cycle formulation (when all conventions match):
`D0(HD)=EI(HD)+D0(HD+) - I_H - I_D`, `D0(H2)=EI(H2)+D0(H2+) - I_H`; substitution yields `delta_E=EI(HD)+D0(HD+)-EI(H2)-D0(H2+)-I_H+rot_diff`. This exposes cancellations of shared atomic constants and is a route to future *joint-covariance* reconstruction, not an independently measured alternative threshold.

## 4. Critical source-method distinction

GL2022's SQM state rates are printed from a scattering dynamical model with its own channel threshold and asymptotic energy convention. The physical spectroscopy threshold includes isotope-specific IP and nonadiabatic/QED information. The 2019 Lepers–Guillon–Honvault paper explicitly treats Born–Oppenheimer PES scattering without a ~3 meV isotope IP correction; this does *not* establish which pieces GL2022 itself included. Until its PES/channel threshold energies have been directly matched to these six spectroscopic inputs, `Q_GL2022_PES_native`, `physical_Q_event_J_per_event`, and bath heat must remain **NULL** in the software. No silent injection of `Q_spectroscopic_candidate` into R21.

A sign check: physical ground-ground threshold from this source mix is ~39.37 meV; removing HD(J2)-H2(J1) excitation difference reduces the target's endothermicity to ~20.95 meV, consistent in rough scale with (but not equal to) the 2019 rounded 39.5 meV ground-ground statement. This comparison does not validate GL2022's exact PES alignment.

## 5. Scope and next binding gate

The forward reaction remains *single-channel*, source-grid-only, externally prescribed thermal history. Reverse detailed balance is NOT implied by Q alone (partition functions, symmetry/statistical factors, inverse cross sections still required). No physical thermal bath, photon deposition, CR clock binding, REC/CR owner ACK, full-A or production. R22 is a separable spectroscopy **candidate-data computation**, not an update of R21 physical runtime or WU canonical DAG.
