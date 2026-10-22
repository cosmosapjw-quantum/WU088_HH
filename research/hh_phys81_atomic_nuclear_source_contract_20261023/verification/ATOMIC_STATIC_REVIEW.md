# PHYS81 independent atomic review

Review owner: `/root/atomic_review`.

Scope: the selected finite electron-impact ionization operator, its added energy moment and temperature derivative, the fixed-density CI-only parcel reduction, and the primary-source interpretation required by those equations. The reviewer owns only `/tmp/phys81_review/atomic/` and has not edited the unit source or theory. No old PHYS78/79/80 or C22D scientific suite has been run.

## Current decision and execution status

The positive-endpoint PL formulas in `source/finite_ci.py` implement the stated finite-window Maxwell integral, its incident-energy mean, and its analytic temperature derivative correctly at the level of algebra. The hazard reduction and rank-at-most-two Jacobian in the theory file are correct under the normalization and positivity conditions written below. Binary64 accuracy and executable guards are **not yet numerically checked by this reviewer**.

The supplied NIST evidence closes the electronic ground-product argument for the selected He and Li windows, conditional on ground-state targets and the selected single-impact collision model. It does not provide missing low-energy cross sections, experimental validation of the 2026 unpublished He curve, or isotope-resolved CCC cross sections. A physical full-rate admission is outside the evidence available here.

An executable bounded verifier is prepared as `verify_atomic_finite.py`. Its `py_compile` syntax check completed with exit code 0. Root must run the verifier under the shared lease. There is no ODE in the verifier. Numerical results must be attributed to the run receipt subsequently produced by that command, not to this static note or its compilation.

## Findings and concrete corrections

### A1. State the stationary-target collision approximation

**Observed target.** The contract says “common-T” while the rate uses electron mass and a source tabulated in electron laboratory incident energy. A complete relative-velocity average of two moving Maxwellian species at common temperature uses their reduced mass after the corresponding energy-variable transformation. It is a different kinetic closure.

**Impact.** The current integral is a well-defined stationary-target/electron-mass operator. Calling its reduction exact is valid for that operator and the reservoir EOS, but does not prove finite-target-mass kinetic equivalence.

**Minimum correction.** State in the contract, derivation, and API documentation that common T describes the shared thermal reservoir/EOS, while the collision kernel uses the inherited stationary-target/electron-mass approximation. Keep the numerical 255–50000 K domain separate from a physical accuracy domain. Root accepted this correction in the review conversation. The actual edited bytes still need to be bound to the final review identity.

For reference, with neutral mass M and reduced mass mu = m_e M/(m_e+M), the laboratory-equivalent relative electron energy has effective Maxwell temperature T_eff = (m_e/mu)T. Adding such a correction would require reviewing the source energy and threshold conventions; it is not silently part of this review or verifier.

### A2. State the normalized abundance units and the invertible hazard domain

**Observed target.** The theory gives dz_s/dt = n_ref x_e K_s and T = u/(1.5 k_B N_g) without explicitly assigning units to all abundance and energy symbols, and initially describes z_s = -log(N_s/N_s0) without N_s0 > 0.

**Impact.** The displayed equations are dimensionally correct when N_s, X_s, B_s, x_e and N_g are dimensionless counts per reference particle, n_ref is in cm^-3, and u is thermal eV per reference particle. The logarithmic map is invertible for strictly positive initial neutral abundance, while N_s0 = 0 would require removing that coordinate or explicitly allowing a redundant parametrization.

**Minimum correction.** Declare these units; require n_ref > 0, N_s0 > 0, X_s0 >= 0, B_s = N_s0+X_s0, and charge neutrality x_e = sum X_s for the selected singly ionized species. Require positive thermal energy and a temperature inside the numerical rate domain wherever the kernel is evaluated. Do not infer strict binary64 positivity once exp(-z) underflows: the mathematical neutral is positive for finite z, while the floating-point representation can reach zero.

### A3. Make the omitted bound-bound channels explicit in the CI-only control

**Observed target.** The initial contract explicitly lists expansion, PI, RR and CX as zero. The thermal equation has only CI chemical loss and no level populations.

**Impact.** The displayed energy first integral requires omission of collisional excitation/de-excitation and associated radiative losses, or an exact cancellation separately established for them. Ground residual-ion kinematics do not remove neutral excitation channels from a real gas.

**Minimum correction.** Name bound-bound collisional excitation/de-excitation and radiative losses among the omitted processes in this CI-only control. This is a scope clarification of the equations already given, rather than a new reaction model.

### A4. Keep isotope provenance statements attached to the actual evidence

**Observed target.** The initial contract calls the chemical ionization potentials “NIST ASD isotope-qualified.” The saved He II and Li II level pages explicitly identify 4He and 7Li; the saved elemental He/Li ionization-query pages do not themselves contain an isotope statement. The registry correctly states that CCC curves are electronic-target data without a newly certified isotope shift.

**Impact.** The residual-excitation threshold evidence has an explicit isotope note. The chemical-I query provenance and the electronic cross-section provenance should not be promoted into a stronger isotope-resolved measurement claim by the project species labels.

**New independent source result.** The delegated narrow source check found a new neutral He I page that explicitly identifies 4He and contains the same 24.587389011 eV ionization limit. I inspected those raw bytes, so the He part of this finding closes when this evidence is attached. For Li, a substantive mismatch remains: the saved NIST Li I level page gives 43487.11420 cm^-1 with reference L12261, while the original-author primary abstract for that same reference, Bushaw et al., Phys. Rev. A 75, 052503 (2007), explicitly gives the 7Li limit as 43487.15940(18) cm^-1. The bibliography mapping was independently checked. These are distinct source literals. A natural-isotope average may explain the difference, but the narrow official-source search did not establish that explanation, and this review does not assert it.

**Minimum correction.** For He, attach the neutral He I evidence. For Li, either identify the current 5.391714996 eV value as an explicitly adopted elemental-Li approximation, or use the isotope-qualified primary limit `I(7Li) = h*c*43487.15940 cm^-1`, with its stated uncertainty, after root performs and records the unit conversion under the shared lease. If the latter is adopted, update the chemical registry, the Li daughter-excitation threshold sum, and parcel energy/Jacobian expectations. The finite cross-section samples, K, energy mean, and their temperature derivatives are unchanged by a chemical-I-only correction. No numerical conversion was performed by the source subreview or this reviewer.

Raw evidence is retained under `isotope/`: `nist_hei_levels_eV.html`, `nist_li_i_levels_cm_inv.html`, `nist_li_reference_L12261.html`, and `pnnl_bushaw_2007_primary_abstract.html`. `PRIMARY_FETCH_FINAL_RECEIPTS.json` contains exact URLs, HTTP status, bytes, retrieval times and SHA256 values. The primary Li7 abstract has SHA256 `dfe6056f9915ddbf0ef98bfa7e28b24606e7f484c81979ec650ecd45ebaab1e0`; the NIST Li cm^-1 page has SHA256 `ecbd99d96fa8571eb2f0340155f144bc2e00dbd709c28b625f05f8b6458b5a01`.

## Independent mathematical derivation

### Maxwell coefficient and units

For stationary targets and isotropic Maxwellian electrons, let E and theta = k_B T be measured in eV, and let sigma be in cm^2. Multiplication of the normalized Maxwell energy density by speed gives

\[
K(T)=C\,\theta^{-3/2}M_1(T),\qquad
C=100\sqrt{\frac{8\,\mathrm{eV_J}}{\pi m_e}},\qquad
M_p(T)=\int_a^b E^p\sigma(E)e^{-E/\theta}\,dE.
\]

The factor 100 converts velocity from m/s to cm/s. With eV_J carrying J/eV, C has dimensions cm s^-1 eV^-1/2; M_1 has cm^2 eV^2; therefore K has cm^3/s. The H conversion `(100*A0_M)**2` converts a0^2 to cm^2. Combining that conversion with C reproduces the retained vendor prefactor `1e6*A0_M**2*sqrt(8*EV_J/(pi*ME_KG))` exactly as an algebraic unit identity.

The chemical potential I_s does not enter this kernel. It enters the event energy accounting separately. This matches the code: `_reference_eV` comes from the first active PL cell, while `Ichemical_eV` is retained independently and constrained not to exceed the source floor.

### Positive endpoint formulas

On a cell E = L+ht, t in [0,1], sigma = s_l(1-t)+s_r t, define

\[
J_n(y)=\int_0^1t^n e^{-yt}\,dt,\qquad y=h/\theta.
\]

Direct expansion gives the coefficients of the left and right endpoint cross sections:

\[
\begin{aligned}
A_{1,l}&=L(J_0-J_1)+h(J_1-J_2),\\
A_{1,r}&=LJ_1+hJ_2,\\
A_{2,l}&=L^2(J_0-J_1)+2Lh(J_1-J_2)+h^2(J_2-J_3),\\
A_{2,r}&=L^2J_1+2LhJ_2+h^2J_3.
\end{aligned}
\]

Each cell contributes `h exp(-(L-reference)/theta) (s_l A_p,l+s_r A_p,r)` to the exponentially scaled moment. These are the four coefficient expressions in the implementation. Their mathematical positivity follows directly from the integral weights t^n and t^n(1-t). Removing a cell with both sigma endpoints zero is exact for PL interpolation.

The added J3 branch is also algebraically correct:

\[
J_3(y)=\frac{6P(4,y)}{y^4}\quad(y>0),\qquad
J_3(y)=\sum_{k=0}^{\infty}\frac{(-y)^k}{k!(k+4)}.
\]

For 0 <= y <= 1/2, the alternating Taylor remainder after k=18 is bounded in exact arithmetic by `2^-19/(19!*23)`. This is a truncation bound for the analytic series, not a floating-point error bound. The new large-y sequential divisions avoid explicitly forming y^4. The inherited J0/J1/J2 code identity is reused and is not re-proved by rerunning its old suite.

### Mean and temperature derivative

The event-weighted mean incoming energy is M2/M1, because the event weighting is E sigma(E) exp(-E/theta). Nonnegative cross section and a finite fixed window imply a <= mean E <= b and M1 > 0. The code checks those properties.

Compact support and T bounded away from zero justify differentiation inside the integral. The derivative is

\[
\frac{d\log K}{dT}=\frac{\langle E\rangle/\theta-3/2}{T},\qquad
\frac{dK}{dT}=K\frac{d\log K}{dT}.
\]

The implementation preserves log K after rate underflow and computes dK/dT through its own logarithmic magnitude, so a representable derivative is not forced to zero merely because K rounded to zero. The prepared synthetic test isolates this branch without attributing physical meaning to the artificial cross-section scale.

### Event energy and daughter states

For the defined ground-to-ground CI event, neutral count decreases by one, singly charged ion count increases by one, and free electron count increases by one. If all outgoing kinetic energy and recoil thermalize into the same reservoir, the thermal loss is I_s. Subtracting the incoming mean E as an additional loss would count kinetic energy already retained among the products a second time.

The primary NIST data supplied in `NIST_GROUND_PRODUCT_WINDOW_EVIDENCE.json` give the lowest electronic daughter excitation thresholds as

\[
24.587389011+40.8130309000=65.4004199110\ \mathrm{eV}
\]

for He, and

\[
5.391714996+59.020708=64.412422996\ \mathrm{eV}
\]

for the initial generic-Li chemical entry. Finding A4 identifies the isotope-qualified Li7 replacement; a corrected Li7 threshold sum must use it. Both supplied Li source literals lie far above the 15 eV endpoint once the 59.020708 eV daughter excitation is included, so this provenance correction does not change the exclusion argument. The respective source upper endpoints 60 and 15 eV lie below the internal-energy requirements. Nonnegative recoil energy cannot lower the required incident laboratory energy. The initially supplied neutral double-ionization internal thresholds, 79.0051545392 and 81.031811996 eV, are higher still; the Li numeric sum has the same chemical-I dependency. A bare proton has no electronic excitation branch. This establishes the claimed residual **electronic** ground state inside the stated model and windows.

The He II page identifies 4He in its explanatory note and displays the lowest 2p J=1/2 level at 40.8130309000 eV. The Li II page identifies 7Li below its ionization limit and displays the bracketed 1s2s triplet value [59.020708] eV. The source bracket convention and correlated uncertainty caveat must be preserved; no new covariance-free uncertainty estimate is made here.

### Hazard map and Jacobian

Under the conditions in finding A2, use

\[
N_s=N_{s0}e^{-z_s},\quad
\Delta X_s=N_{s0}(1-e^{-z_s}),\quad
X_s=X_{s0}+\Delta X_s.
\]

The increment form supports `-expm1(-z)` at small z and avoids losing the initial X_s0 by subtracting two nearly equal nucleus and neutral abundances. The original reaction flux is R_s = n_ref x_e N_s K_s(T), so dN_s/dt = -R_s implies dz_s/dt = n_ref x_e K_s(T).

Nucleus conservation removes three independent directions from the seven-state abundance-plus-energy system. Conservation of thermal plus chemical energy gives

\[
u=u_0-\sum_s I_s\Delta X_s,\quad
N_g=\sum_s B_s+x_e,\quad
T=\frac{u}{cN_g},\qquad c=\frac32 k_B.
\]

This removes the fourth direction and yields the three hazard coordinates on the appropriate invariant manifold. It is an exact coordinate reduction of this specified reaction/EOS model. It is not a QSS elimination or a kinetic-theory equivalence statement.

Since dX_j/dz_j = N_j and du/dz_j = -I_j N_j,

\[
\frac{\partial T}{\partial z_j}
=-\frac{N_j(I_j+cT)}{cN_g},\qquad
J_{ij}=n_{\rm ref}\left[N_jK_i+x_eK_i'\frac{\partial T}{\partial z_j}\right].
\]

The two terms are the outer products `n_ref outer(K,N)` and `n_ref*x_e outer(Kprime,dTdz)`. Thus rank J <= 2 analytically for this model. Cross derivatives need not be positive because the temperature feedback term is negative when Kprime is positive. The dimensions are dz/dt in s^-1 and J in s^-1. The represented energy first integral cannot independently establish trajectory accuracy; comparison to separately integrated original equations belongs to root's trajectory verification.

## Source and numerical scope

The selected source windows are H: 13.6058–968.61 eV with 87 rows; He: 24.6–60 eV with 27 selected rows; Li: 6–15 eV with 13 selected rows. The He author README explicitly says the values were unpublished as of 13-Apr-2026 and identifies Fursa and Bray, Phys. Rev. A 52, 1279 (1995), as the underlying CCC method. A method reference is not an experimental uncertainty certificate for that table. The Li source identifies Phys. Rev. A 49, 1066 (1994).

All three source floors differ from the chemical ionization energies. The omitted interval is particularly material to any proposed low-temperature full-rate claim for Li, whose first included energy is 6 eV while its chemical threshold is approximately 5.392 eV. This review supplies no bound on that missing contribution or on the upper omitted support. The finite operator remains mathematically defined by zero outside its chosen support.

The prepared verifier uses original literal rows and independent slope-based adaptive quadrature, with exponential scaling at the selected window floor. That construction avoids falsely accepting an all-zero quadrature reference when a cold He rate underflows. It tests the new J3 branch, mean, derivative, and generic-wrapper behavior. The retained vendor is evaluated only once at 25370.66308424773 K to test the newly required parent-temperature conversion/equivalence. No old scientific test suite or old ODE is invoked.

## Actual commands and identities

Read-only `cat`, `rg`, and `sha256sum` commands completed with exit 0, with two scope-resolving exceptions: `cat vendor/REUSE.json` returned 1 because the real path is `source/vendor/REUSE.json`; the later corrected read returned 0. A search for explicit isotope text in the saved elemental He/Li ionization pages returned 1 with no matches; this was evidence for finding A4, not a tool failure.

Actual syntax command:

```text
python3 -m py_compile /tmp/phys81_review/atomic/verify_atomic_finite.py
exit_code: 0
```

Prepared numerical command, **not run by this reviewer**:

```text
python3 /tmp/phys81_review/atomic/verify_atomic_finite.py --output /tmp/phys81_review/atomic/ATOMIC_NUMERICAL_RESULT.json
```

Initial reviewed snapshot hashes are recorded in `REVIEWED_INPUTS.json`. A final source/contract snapshot and parcel implementation review will be added after root supplies the relevant changed files. No scientific success is inferred from compilation, file existence, hashes, or an execution command that has merely been prepared.

Bell positivity certificates and nuclear capture calculations are separate review scopes. This note does not claim to have independently verified them.
