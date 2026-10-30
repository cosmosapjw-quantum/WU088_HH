# WU R36 | EMAA H⁺–HD 171×25 primary-rate crosswalk and source-scoped 19-state kinetics

## Source lock / scientific domain

Inputs: user-supplied full EMAA-format `HD.Rovibration.805a7aa5.radex` (SHA256 `b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94`, 298,618 B), and original GL2022 print transcription retained from the exact R35→R34→R33→R32 source archive chain. **The uploaded bytes are authenticated in this run; independent server-original byte identity is not asserted.** The RADEX header gives dataset DOI 10.17178/emaa_hd_rovibration_805a7aa5; the primary paper is González-Lezana, Hily-Blant & Faure, *J. Chem. Phys.* **157**, 214302 (2022), doi:10.1063/5.0128598. Original PDF supplement SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`.

RADEX includes 52 spectroscopic HD rovibrational levels, 368 radiative transition coefficients (HITRAN 2022 basis), collider 5 (H, 1326×15) and collider 7 (H⁺, **171** downward unordered pairs on the lowest **19** levels × **25** kinetic temperatures, 5–3005 K). We use only collider **7** and the **63** radiative transitions connecting these 19 levels. RADEX state indices are **energy ordered**, not lexicographically ordered in (v,J), and both states of every 171 collision pair must be mapped using the actual `v_J` labels. Original rates are downward by energy, in cm³/s. Collisionally upward rates are *derived*, not source-printed.

### Direct numerical crosswalk

The inherited GL2022 source-printed rate atlas has 1560 transcribed cells over 10 temperatures. Exactly 1548 are classified numeric and non-diagonal, with 1498 *identical as parsed numerical values* to EMAA and 50 nonidentical values distributed over seven physical transitions; 10 printed entries are unphysical diagonal self-transitions and two entries are prior source-flagged unreliable. EMAA supplies **16 transition pairs absent** from the previous GL transcription, each at 25 temperatures = **400 independently tabulated EMAA values**. The 15 EMAA temperature nodes absent from GL account for additional rates, none requiring interpolation. **Numerical agreement is source cross-check, not independent physical-scattering confirmation.**

Most conspicuous mismatches: v1J6→v0J10 has GL/EMAA = 0.1 at 8 middle temperatures (55..2505 K), whereas the 15 K and 3005 K values match. For v1J6→v0J1 all 10 GL/EMAA ratios lie 0.3127..0.3279; other affected 10-point transitions are v1J4→v0J5, v1J6→v0J5 and v1J6→v0J7. Two isolated small differences remain, v0J2→v0J0 and v1J1→v1J0 at 15 K. The old malformed `1.58(10` at v1J2→v0J5 (2005 K) is separately marked; EMAA prints `1.58e-10`. Old suspicious `1.91(11)` at v0J1→v0J0 (1505 K) is separately marked; EMAA prints `1.91e-10`. This does not silently amend the printed PDF or identify an authoritative erratum.

## Model 1. Conditioned first vibrational-quench *collision-only* first passage

Let initial levels be `v=1, J=0..6` (seven states) and terminal levels `v=0, J=0..11` (twelve states) in the 19-state collider-7 connected network. Let `s=∫n(H⁺)dt` denote proton fluence (cm⁻³ s), and let `K` (cm³/s) be the restriction of the 19-level collision generator to v1 transient states; `S` contains all v1→v0 landing fluxes. Then for initial unit vector `e_j`:

\[
 F=(-K)^{-1},\quad B=SF,\quad \sum_{J'=0}^{11} B_{J'j}=1,\quad
 \langle s_j\rangle=\boldsymbol 1^{\mathsf T}F e_j,\quad
 k_{\mathrm{eff},j}=1/\langle s_j\rangle .
\]

This is **first v=0 landing under collisions only**, conditional on no competing v1 radiative, chemical, ionization or other unmodeled events, **not** a full chemical network. Use source gas temperatures only. Since the first-landing event can end at rotationally high v0 levels, do not discard v0 J5..11 or set them to zero. Outputs: 175 initial-state/temperature cases and 2100 individual end-J probabilities.

## Model 2. Nonreactive 19-level collision–radiation *counterfactual* steady state

At prescribed fixed `T_g` and H⁺ number density `n_p`, for any energy ordered pair `E_u>E_l` with published H⁺ de-excitation rate `k_ul(T_g)` (cm³/s), and `g_i=2J_i+1`, use the inverse/upward collision rate *derived* by local detailed balance:

\[
 C_{lu}=n_p k_{ul},\qquad
 C_{ul}=n_p k_{ul}\frac{g_u}{g_l}\exp\!\left[-\frac{E_u-E_l}{k_B T_g}\right].
\]

The energy used is `E_i=100 hc E_i^(cm^-1)` in SI joules, with `h`, `c`, `k_B` retained. For 63 original source Einstein A lines between levels <=19 and prescribed isotropic external Planck background `T_r=2.7255(1+z) K`, use

\[
 \bar n_{ul}=[\exp((E_u-E_l)/(k_B T_r))-1]^{-1},\qquad
 R_{lu}=A_{ul}(1+\bar n_{ul}),\quad
 R_{ul}=A_{ul}\frac{g_u}{g_l}\bar n_{ul}.
\]

Generator `G=C+R` uses **column** convention with off-diagonal transition rates and diagonal negative column sums; it has **no chemical absorption**, by explicit counterfactual construction. This is a controlled nonreactive benchmark, not physical closure or ionization/chemistry. Solve `G p=0, Σ_i p_i=1` with a grounded nonsingular M-matrix (`p_0=1` before normalization) to avoid negative roundoff artifacts. For `n_p>0`, the source graph is connected, apart from representational underflow of astronomically negligible rates at the cold extreme. Define positive outward energy-flow rates per HD molecule:

\[
 \mathcal P_r=-\boldsymbol E^{\mathsf T}R p,\quad
 \mathcal P_c=-\boldsymbol E^{\mathsf T}C p,\quad
 \mathcal P_r+\mathcal P_c=0.
\]

The last identity follows from `Gp=0` and **does not** mean real chemistry or cosmological thermodynamics has zero net heat. Test all 25 original gas temperature nodes against four *prescribed* densities `{1,10^3,10^6,10^9} cm^-3` and five *prescribed* radiation redshifts `{0,10,30,100,300}` = 500 fixed-boundary cases. This grid is a sensitivity atlas, not the cosmic `T_g(z), n_p(z)` history. Retain full state-resolved photon line flux on 63 source transitions, 31,500 records. The v1 population is a conditional **19-level** stationary probability, not an observed abundance.

## Model 3. Source-choice perturbation

At the 10 original printed GL temperatures, replace only the **1548 valid printed values** in the EMAA generator by their GL values. Preserve all source-absent GL edges, all extra 15 temperature points, and both malformed/suspect entries from EMAA, without interpolation or silently completing the print source. This **GL-hybrid** is only a conditional controlled perturbation of 50 mismatches, not an independently source-closed GL model. Compare v1 population, `L1` full population distance, and signed radiative power at 10 gas temperatures ×4 densities ×5 radiation boundaries = **200 cases**.

## Boundary and admission

Default metric signature (-,+,+,+), but no GR background field is solved here. No chemical reaction Q, no same-PES isotope native threshold or photon transport. No full-radiation A beyond the 19-state subset; no source for collisions to HD states 20..52; no native owner ACK, no independent author R6/C9. The prior R35 parent 34/49 canonical DAG is **unchanged**. The new source-qualified auxiliary physics and true source crosswalk may be accepted **within this restricted scope only**. Full production/merge remain HOLD.
