# WU088_HH R26 | GL2022 700-cell rotational-reactive atlas and spin-typed product dynamics

2026-10-30 KST. 이론 우선 연구 P01. SOURCE original: González-Lezana, Hily-Blant & Faure, JCP **157, 214302 (2022)** DOI 10.1063/5.0128598, original supplementary PDF SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754` (273554 B). Frozen parent WU PR164 HEAD `24302ab37ecc3b1220fb90a705ed375fe431b54e`, sibling R22 PR160 read-only. Central DAG 34/49 unchanged; full physical-Q and owner gates hold.

## 1. Actually published source ranges

Original supplement section 3 and Tables 1–10: initial H⁺+HD(X,v=0,J=0..6) -> D⁺+H₂(X,v′=0,J′=0..9), each T∈{15,55,105,255,505,1005,1505,2005,2505,3005} K. Source has **700 printed `(J,J′,T)` literals**, interpreted as mantissa `m(xx)` = m×10^(−xx) cm³ s⁻¹. `0.00(00)` and `.000(00)` are PRINTED ZERO, not a physics-certified exact zero; complete all-channel rates and branching remain undefined at `(J,T)` containing those cells. No new numerical Q or source uncertainty is supplied by these tables.

Original *main article* Eqs. (5)–(7) define a **different observable**, the initial HD rotational Boltzmann average with product nuclear-spin factors. In its Eq. (5), J=0..8 (not 0..6),

\[
Z_8(T)=\sum_{J=0}^8 (2J+1)\exp[-\varepsilon_J/(k_BT)],\quad
k_\mathrm{thermal}(T)=Z_8^{-1}\sum_{J=0}^8(2J+1)e^{-\varepsilon_J/(k_BT)}\left[k_J^\mathrm{even}(T)+k_J^\mathrm{odd}(T)\right],
\]
\[
k_J^\mathrm{even}=\frac14\sum_{J'\in\{0,2,4,6,8\}}k_{JJ'},\quad
k_J^\mathrm{odd}=\frac34\sum_{J'\in\{1,3,5,7,9\}}k_{JJ'}.
\]

The raw source-state rate and Eq(6–7) spin-weighted effective rate are distinct typed arrays. A further manual 3/4 multiplier on any Eq(7) output is wrong. Supplementary Table 11 is the authors' already-averaged rate, but Tables 1–10 **do not include initial J=7,8** and do not tabulate a full state-energy set; Table 11 cannot be exactly reconstructed from only their numeric entries. Do not infer missing J7/J8 as zero or replace with a different-source rate.

## 2. New source quality obligations (literal fidelity, not silent repair)

The exact printed table exhibits potentially problematic cells requiring author/source confirmation:
- Table 2 `(J=5,J′=1)` is character-for-character identical across all 10 T to Table 1 `(J=5,J′=0)`. This is a source duplicate diagnostic, not proof of typo or identical physics.
- Table 8 `(J=3,J′=7,T=2505 K)` is literally `6.72(16)` (confirmed by page screenshot), despite adjacent `4.71(11)` and `8.36(11)`. The 10⁵ jump from neighboring source exponents makes this a source-suspicious cell; do **not** replace its exponent by 11 without an authenticated correction.
- The printed-zero cells, including `.000(00)`, are source-censored. They cannot define a physical exact zero or a canonical complete-normalized branching vector.

The code must maintain exact literal bytes, output `SOURCE_SUSPECT` annotations with raw/derived separation, and avoid silent smoothing, correction, extrapolation or fitting. Source anomalies do not prove a mathematical inconsistency of every other cell.

## 3. Forward-only source-matched multi-initial chemistry model

Given a **declared model policy** `raw_SQM` or `Eq6-7_spin-weighted`, let
\[
 q_{J,J'}(T)=\begin{cases}k_{JJ'}(T),&\text{raw source SQM},\\ w_{J'}k_{JJ'}(T),&\text{Eq6–7 spin policy},\end{cases}
\quad w_{J'}=\begin{cases}\tfrac14,&J'\ \mathrm{even},\\\tfrac34,&J'\ \mathrm{odd}.\end{cases}
\]
The source of `q` is the published rate grid, while the multiplicity factor is from original Eqs(6–7) and must **not** be conflated with thermal HD(J) averaging. For initial state populations `y_J=n_{HD,J}` and proton density `p=n_{H+}`, product populations `z_{J′}=n_{H₂,J′}` and deuteron `d=n_{D+}` in a **fixed-volume, externally prescribed T(t)** compartment, with no backward reactions, rotational redistribution, or expansion,
\[
\dot y_J=-pK_J(T)y_J,\qquad K_J=\sum_{J'}q_{JJ'},
\quad\dot p=-p\sum_JK_Jy_J,
\quad\dot z_{J'}=p\sum_Jq_{JJ'}y_J,\quad\dot d=p\sum_JK_Jy_J.
\]
Units: `q,K` m³/s after exact 10⁻⁶ from cm³/s, `p,y,z,d` m⁻³, time s. H nuclei, D nuclei, charge and total species-particle counts conserve exactly: `H = p + Σ_J y_J + 2Σ_J′ z_J′`, `D=Σ_J y_J+d`, `charge=p+d`, `particles=p+Σy+d+Σz`. Source data are SQM simulations; neither external history nor these population trajectories are cosmological observed data.

For **constant T** and auxiliary collision clock `u(t)=∫₀ᵗp(s)ds`,
\[
y_J(u)=y_{J,0}e^{-K_Ju},\quad d(u)=\sum_J y_{J,0}(1-e^{-K_Ju}),\quad p(u)=p_0-d(u),
\quad z_{J'}(u)=\sum_Jy_{J,0}\frac{q_{JJ'}}{K_J}(1-e^{-K_Ju}),
\]
with `t=∫₀ᵘ ds/[p₀−Σ_Jy_{J,0}(1−e^{−K_Js})]` and `p>0` maintained. This reduces a 19-variable population IVP to a single positive monotonic quadrature/root per constant-temperature segment, preserving all species and channel identities. This is a physical finite-state **restricted forward kinetic model** conditional on externally fixed T and q input, not validated GL2022 full-state chemistry owner.

For multiple initial J with distinct `K_J(T)`, temperature segments generally do not commute. Even with unchanged total exposure durations, the final total extent need not be invariant under segment order, unlike the special single-J R25 model. Compute a concrete fixed-source-grid experiment and check against independent `solve_ivp` with matched equations. Do not invoke detailed balance, reverse rates, physical bath, `Q` or production.

## 4. Admission conditions and counterexample scope

The main Eq(5–7) thermal rate has different coverage from the 700-cell table; a model restricted to J=0..6 is not an exact reproduction of Table11. The GL2022 Eq(3) total-energy vs Eq(4) kinetic-energy ambiguity remains. Actual Velilla2008 numeric ionic asymptotes, H/D BO/isotope energy offset and molecular owner ACK are unavailable; a mass-action rate alone does NOT determine physical Q or a reverse rate. Scientific **claim** for this unit is source-qualified *published computed SQM rate dataset* plus a fully specified **conditional** multi-J forward-kinetic experiment, not physical inference of cosmic HD abundance.

Central: `34/49_UNCHANGED`; prior R23 scoped `18/20`; distinct-author R6/C9 `NOT_RUN`; `GL2022_PES_NATIVE_THRESHOLD=null`, `physical_Q=null`, `source_uncertainty=null`, `owner_ACK=null`, `HH_R10=OFF`, `full_A=null`, `L4=false`, `production=NOT_ISSUED`. No foreign repo mutation or main merge.