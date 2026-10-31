# WU R39 | Velilla native 3-body Jacobi PES, COM translation, isotropic-C4 barriers and TIQM erratum

### 1. Sources, scope, conventions
- Parent Git WU088_HH PR #177 immutable HEAD `93d5eb0aefb9a94d722e9e4107a09b2e3066677c`; parent chemistry and BO spectra unchanged.
- Velilla et al. (2008), JCP 129, 084307, DOI 10.1063/1.2973629: original AIP EPAPS `h3plus.f`, SHA256 `8dbf8b7e3852d02504ba92317f79593051d689f1357263ac0891a3a24084ed8c`. Native output `DIMH3P` ground PES `e1` in Hartree and distances in Bohr; `h2` is molecular H2 electronic BO potential.
- Lepers, Guillon, Honvault (2019), MNRAS 488, 4732–4739, DOI 10.1093/mnras/stz1797; **essential 2021 published erratum** MNRAS 500, 430–431, DOI 10.1093/mnras/staa3146.
- R38 mass convention: m_p/m_e=1836.152673426, m_d/m_e=3670.482967655. Computational units: a0, Eh, m_e, with conversions Eh/kB=315775.024804 K, Eh=27.211386245981 eV. No nonadiabatic molecular correction or hyperfine effects.

### 2. Genuine three-body geometry and nuclear masses
Arrange diatom nuclei A and B on the z axis about its **mass** COM:
`x_A=-[m_B/(m_A+m_B)] r z`, `x_B=+[m_A/(m_A+m_B)]r z`; projectile C at `R` and `cosθ=(Rhat·zhat)`. This yields

`r_AB=r`,
`r_AC²=R²+[m_B/(m_A+m_B)]² r²+2Rr[m_B/(m_A+m_B)]cosθ`,
`r_BC²=R²+[m_A/(m_A+m_B)]² r²-2Rr[m_A/(m_A+m_B)]cosθ`.

The genuine BO three-body interaction is
`U(R,r,θ) = V_native_ground(r_AB,r_AC,r_BC) - V_native_h2(r)`;
`μ_r=m_A m_B/(m_A+m_B)` and `μ_R=m_C(m_A+m_B)/(m_A+m_B+m_C)`.
- Entrance `H+ + HD`: (m_A,m_B,m_C)=(m_p,m_d,m_p), μ_R=1377.000578101595 m_e.
- Exit `D+ + H2`: (m_A,m_B,m_C)=(m_p,m_p,m_d), μ_R=1835.696965554379 m_e.
`T_nuc=-ħ²/(2μ_r)∇_r²- ħ²/(2μ_R)∇_R²`, before angular coupling. The **actual wave equation/S-matrix are not solved** here.

### 3. Angular moments, coordinate artifact, and potential anisotropy
For each fixed bond r and radius R, evaluate 32-node Gauss–Legendre quadrature in c=cosθ and define `a_l(R,r)=(2l+1)/2 ∫_{-1}^1 U(R,r,c)P_l(c)dc`, l=0,…,4. The raw electronic PES is permutation invariant. With unequal HD masses, the **geometrical** midpoint of nuclei lies at `δ=(m_A-m_B)r/[2(m_A+m_B)]` relative to the diatom COM, so the electronic reference vector is `R_mid=R-δ z`. Thus `R_mid²=R²+δ²−2Rδ c`, `c_mid=(Rc−δ)/R_mid`. Evaluating the *same* source PES at the translated H2-symmetric midpoint gives the original HD-COM PES to native floating precision. Therefore odd angular moments seen for the HD COM geometry are coordinate-origin terms, **not a newly certified permanent HD electric dipole**. This is numerically checked for 192 points.

### 4. Long-range isotropic model, NOT reaction threshold
For the rigid r=1.4 a0 reference, isolate `a_0(R)` and infer source-native `C4_iso≈lim_{R→∞}[-R⁴ a_0(R)]` from R=60–160 a0 by linear fit in 1/R². Numerical result `C4_iso=2.5884219506088395 Eh a0⁴`. The fact that fixed-angle potential contains a leading quadrupolar ~R^-3 contribution means this isotropic average is **not the full noncentral dynamics**.
The **diagnostic** j=0 isotropic atom-diatom relative orbital model has

`V_eff,ell(R) = ħ² ell(ell+1)/(2 μ_R R²) − C4_iso/R⁴`, ell≥1.

Direct differentiation gives the stationary (maximum) radius `R_ell = sqrt(4 μ_R C4_iso/[ħ² ell(ell+1)])` and height `E_ell = ħ⁴[ell(ell+1)]²/(16 μ_R² C4_iso)`; in a.u. ħ=1. For ell=1, model barriers =0.01608475563 K (H++HD) and 0.00905067005 K (D++H2); the ratio =1.7771894844 = (μ_R,exit/μ_R,entrance)². Results with R_ell<20 a0 are flagged `short_range_extrapolation_not_physical`. No centrifugal radius is a certified true reactive S-matrix threshold.

### 5. Nuclear-spin erratum and incompatibility of original rates
Lepers et al. 2019 original thermal fit, as in published (not original preprint), `1.95×10^-9 exp(-428/T)` cm³ s^-1 for 100≤T≤400 K, was corrected by the 2021 erratum to `9.94×10^-10 exp(-439/T)` cm³ s^-1. Para/ortho separate fits: `2.30×10^-10 exp(-407/T)`, `7.66×10^-10 exp(-450/T)` cm³ s^-1. The correction weights **original TIQM** v=0 to v'=0 j' even by 1/4 and j' odd by 3/4; 2019 thermal total Eq.(3) includes j=0…6, Boltzmann population and degeneracy. The three corrected independent fits need not sum *exactly* at finite T. It would be **incorrect to reapply** 2021 weights to GL2022 state-specific rates if the latter are already weighted using Eq.(6-7). The R38 70-channel table annotates the published correction for source comparison, WITHOUT altering GL2022 rates, R37 probabilities, R38 BO levels or 50 disputed cells.

### 6. Scientific admission
- **derived and numerically checked**: native 3-body PES 5,376 rows, Legendre moments 168 rows, exact coordinate-translation check 192 rows, mass-dependent isotropic model centrifugal diagnostics 24 rows.
- **literature-supported, generated from explicit published analytic fit**: 12 temperature cases of corrected vs superseded TIQM fits; 70 R38 channel metadata crosswalk; NO new TIQM scattering measurement.
- **unresolved**: native 3-body quantum S matrix and full physical isotope Q; GL–EMAA 50-cell owner attribution; distinct-author R6/C9; cosmological full network rates/production admission.
- **scientific promotion**: canonical WU DAG remains 34/49 (+0); isolated auxiliary R39 1/1 scoped only; production HOLD, `NO_MAIN_MERGE=true`.
