# WU088_HH PHYS43: original six-panel coupled annulus bound with cusp / interface closure

2026-10-15 KST. Parent PHYS42 draft PR #81, commit
`6a5c89ccd16dcd4467afaa88e956c726d88941ca`.
Selected incomplete node
`C7B_GLOBAL_SIGNED_JOINT_TILING_WITH_PHYS38_CUSP_LOG_PATCH`;
R5 constructive derivation, local C5/C6/C7/C8 implementation,
science verification and optimization.
**New achievement:** original complete truncated annulus *transformed
D-operator* strong broken bulk and full-H0^1 dual H^-1 bound with exact
cusp strip and all FIVE original interface distributional sheets.
This is **not** a whole-space scattering solution-error estimate.

## 1. Locked physics and authority

Original fixed frozen-direct spectator H(1s)+H(1s):
\[
h_\lambda=-\frac12\Delta-\frac1r-\lambda(1+s^{-1})e^{-2s},
\qquad
s=|\mathbf r-R\hat{\mathbf z}|,\quad R=\kappa=\frac7{10},
\quad\lambda=1.
\]
Electronic three-space is Euclidean. Cosmological metric
convention remains (-,+,+,+). Length unit \(a_0\),
Hamiltonian energy unit \(E_a=2I_0=27.211386245980\,\mathrm{eV}\).
Keep \(I_0=13.605693122990\,\mathrm{eV}\) atomic supply distinct
from \(\chi_H=13.598434599702\,\mathrm{eV}\) receiver heat.
Do not implicitly change \(c,\hbar,k_B\) in source/consumer conversions.

Original \(\phi=e^{-r}/\sqrt{\pi}\), \(\eta=\phi+\lambda\xi=Fy\),
\(F=e^{\lambda e^{-s}}\), original Coulomb final-state phase,
\(S(R)-S(s)\) source, 21 partial waves \(\ell=0,\ldots,20\),
6 radial panels × 11 dyadic nodal samples, 1386 complex128
input values unchanged. Actual frozen SHA256
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`
at
`research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz`.
Original mathematical cusp \(R=7/10\) differs slightly from actual
stored dyadic \(r_{\rm switch}=3152519739159347/4503599627370496\).
The certified physical annulus begins at the exact stored binary64
\(r_0=7378697629483821/73786976294838206464\)
(approximately \(10^{-4} a_0\)) and ends at \(r=20\).

Frozen PHYS37 two-sided cusp-shell JSON SHA256
`a942df8c66f5d8c3817b3e41dc11329420d2cfef9800e827c27c5381a42f1be7`
is bound by the PHYS38 implementation.
All original five PHYS38 interface sheets are from immutable
`INTERFACE_HMINUS1.json`, SHA256
`6760001d384dd39c7aab79a21f60ee78a96b36c0eed84402301787669a2f714d`.
All five zero-value-jump confirmations and their exact dyadic
interface locations must match the frozen source. This immutable
source lock is checked at runtime rather than merely trusting copied
JSON strings.

## 2. Constructive theorem: exact global radial cover and valid local minimization

For \(0<\delta<1/10\) define the rational cusp collar
\(\mathcal C_\delta=\{R-\delta\le r\le R+\delta\}\).
The original six radial panels are clipped only for INTEGRATION:
panel 1 ends at \(R-\delta\), panel 2 begins at \(R+\delta\).
The single PHYS38 collar bridges both, including the true stored
dyadic panel interface and the tiny mismatch to mathematical \(R\).
All original panel interfaces remain the same actual dyadic points.
Sorting the six clipped domains and this collar gives seven
exact rational intervals whose consecutive endpoints are literally
equal; no coverage gap or artificial physical discontinuity exists.
New radial tile boundaries do not modify or reinterpolate the
frozen trial. Therefore they do not introduce spurious delta sheets.

On any noncusp exact tile \(I=[a,b]\), with \(a>0\), PHYS41 supplies a
rigorous positive radial full-angular bound \(B_I\).
PHYS42 supplies a second rigorous signed source-preserving bound:
for exact cosine cells \([\mu_k,\mu_{k+1}]\) tiling \([-1,1]\),
\[
S_I=\sum_k\frac{b^3-a^3}{6}
(\mu_{k+1}-\mu_k)(q_{\Re,k}^2+q_{\Im,k}^2).
\]
Here \(q_{\Re,\Im}\) are outward upper magnitudes of the original
\(G=\sqrt{4\pi}\,\mathcal R\) on that full exact
\((r,\mu)\) cell. The original screened angular coupling
\[
G=(A-S_0)-\frac{2e^{-s}H}{s}-2UB+
S_0\bigl(1-e^{-e^{-s}}\bigr)
\]
is evaluated with the exact 21-term Legendre polynomials,
\(H=(r-R\mu)C-(R/r)T\), original potential
\(U=e^{-s}(1-e^{-s})/s-e^{-s}/2-3e^{-2s}/2\),
exact dyadic radial polynomial and 192-term exponential coefficient
enclosure. Both \(B_I\) and \(S_I\) are upper bounds for precisely
the SAME positive integral over the SAME radial tile.

Therefore \(\min(B_I,S_I)\) is an upper bound, regardless of which
one is selected after evaluation. We round each squared candidate
**UPWARD** to an exact 24-decimal-place rational before summation.
This avoids a representation problem where dozens of mutually
coprime exp-Taylor rational denominators exceeded Python's default
4300-digit integer-to-string output limit. This error occurred on
the first pilot and is classified REPRESENTATION_BOTTLENECK,
not a physics/symbolic defect. Rounding outwards preserves
the inequality without loosening tolerances or downcasting to float.

With \(C_\delta\) the PHYS38 cusp-positive-volume
full screened broken strong L² upper (using the real log unit-vector
modulus), the exact annulus broken bulk obeys
\[
\boxed{
\|\mathcal R\|_{L^2(\mathcal A)}^2\le
C_\delta^2+\sum_{I\subset\mathcal A\setminus\mathcal C_\delta}
\min(B_I,S_I),\qquad \mathcal A=\{r_0<r<20\}.
}
\]
For panels where signed evaluation is not elected, take
\(S_I=+\infty\), so \(\min(B_I,S_I)=B_I\).
The old five original panel first-derivative jumps have a separate
physical \(H^{-1}\) bound \(J=0.0000000000001793\)
for the transformed D-operator. Because the test space is the
**full** \(H_0^1(\mathcal A)\) norm
\(\|v\|_{H^1}=\sqrt{\int(|v|^2+|\nabla v|^2)d^3r}\),
the continuous embedding \(L^2\hookrightarrow(H_0^1)^*\)
with factor 1 and triangle inequality yield
\[
\boxed{
\|\mathcal R_{\mathrm{distribution}}\|_{(H_0^1)^*}
\le \left[C_\delta^2+\sum_I\min(B_I,S_I)\right]^{1/2}+J.
}
\]
For a pure-gradient \(H_0^1\) norm this numerical bound cannot be
copied unchanged; PHYS41 documented the separate Poincare factor.
Likewise the Hamiltonian \(-\Delta/2\) requires the already
documented factor-two conversion from the transformed D residual.
No continuous inverse, outgoing amplitude, solution error,
cross section or thermal rate is inferred from this residual alone.

## 3. Cusp grading, exact rational cache, and local optimization

Implementations:
`src/wu088_hh/phys43_global_hybrid.py`,
`scripts/phys43_global_hybrid.py`,
`tests/test_phys43_global_hybrid.py`.
Original PHYS42 signed interval machinery and PHYS41 Bernstein
fallback are imported unchanged.

The signed joint evaluation is arranged as **one immutable
source-verified CPU worker per radial panel**, with each worker
building its 21 original radial mode polynomials only ONCE,
reusing signed angular Legendre ranges across all cells.
This avoids the earlier PHYS42 design in which each worker
reloaded 1386 original values for each radial slab. No floating
vector kernel replaces the exact certified interval computation;
the existing NumPy/SciPy vectorized full screened original operator
serves as a separate exploratory diagnostic.

The first global pilot (regular division 2 per non-origin panel)
failed at Python Fraction-to-string output because distinct exact
exponential denominators grew together. The repaired code
outward-rounds each squared tile to 24 decimal digits before global
addition, bounding any dropped rational tail explicitly rather
than changing physical precision or allowable error.

Cusp-graded mode preserves EVERY original regular radial cut and
unions them with exact rational additional cuts approaching the
\(R\pm\delta\) collar from the two adjacent panels.
The nearest graded width is bounded by \(\delta\); the step
increases outwards by rational ratio \(3/2\).
This directly targets the largest prior signed rectangle's
\(e^{-s}/s\) interval dependency overestimation, while still
covering every original radial interval exactly.

Local CPU oversubscription was avoided by
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1`
and at most 2 PHYS43 workers in the reported graded campaigns
because a separate user-owned AX08 solver was active.
The parent-only peak RSS must not be misinterpreted as the
sum of process RSS. A matched original frozen
8/16/16/8/8/8, mu8 comparison (exact same cell science)
measured 1 worker wall **41.53 s**, 2 workers wall **23.77 s**,
speedup **1.75×**. The two JSON objects initially compared
unequal because the newer serial run contained newly added
`radial_strategy` and `radial_cuts_exact` metadata,
not because any scientific field changed. After reconstructing
the exact same radial cuts from the older two-worker cells,
all scientific fields and panel/cell intervals matched.
This is classified METADATA_SCHEMA_EVOLUTION, not scientific
numeric disagreement. Best cusp-graded two-worker wall
**50.31 s** versus its same resolution uniform wall
**42.42 s**: the tighter 0.917 bound has a finite extra
CPU cost rather than an unconditional wall-speed improvement.

## 4. Actual original frozen calculation

All configurations use exact cusp half-width \(\delta=1/100\),
PHYS38 certified cusp full broken L² upper
\(C_\delta=0.092921847102\) and ALL five original
interface sheets \(J=0.0000000000001793\).

| Model and full truncation | Total full-H1 dual upper | Note |
|---|---:|---|
| Prior inherited PHYS39 | 2.516921964597789440 | Old accepted annulus envelope |
| PHYS43 signed 8/16/16/8/8/8, mu8, two workers | 2.246314672605 | New complete annulus |
| PHYS43 signed 8/24/24/12/8/8, mu12, two workers | 1.471097983248 | More radial/angular cells |
| PHYS43 signed 8/32/32/16/8/8, mu16, two workers | 1.194398020700 | Finer uniform cells |
| PHYS43 above, *cusp-graded union*, two workers | **0.917114942873** | Scoped best current |

Original PHYS41 coarsely positive-only 2 radial divisions on panels
1–5 plus 18 exact origin-gradings yielded a much wider
\(21.849605683786\), while still scientifically valid.
This intermediate failure-to-tightness motivated the signed
global angular coupling implementation, not a change of model.

In the graded run, all six panels are covered:
- panel 0: 18 radial cells, bound 0.244241787978;
- panel 1: 40 cells, bound 0.487474879769;
- panel 2: 42 cells, bound 0.718356962087;
- panel 3: 16 cells, bound 0.128093927251;
- panel 4: 8 cells, bound 0.051977538222;
- panel 5: 8 cells, bound 0.005752887510.

Cusp adds its own squared full-volume certificate.
The graded result improves the inherited PHYS39 full-H1 dual bound
by approximately 63.56%. This is a **tighter bound on the
same frozen trial's transformed PDE residual**, not evidence
that the approximate scattering solution itself was improved.
A normalized float64 original full-screened six-panel Gauss
diagnostic from PHYS41 is about 0.00174474274907638,
explicitly NONCERTIFYING and substantially smaller than this
bound. Interval slack remains significant.

Exact Python3.12 Fraction (in valid signs and units) is the
scientific arithmetic. Wolfram Engine15+xAct/xTensor1.3.0
independently checked scalar source cancellation, cusp and
angular-volume Jacobians, exact seven-subdomain measure sum,
and Euclidean Green identity. Actual local Wolfram execution:
**8/8 scalar exact zero**, positive-domain certificate minimum TRUE,
and **xAct/xTensor1.3.0 Green tensor expression exact zero**;
final exit code 0 recorded in `results/CAS_XACT.stdout`.
Actual full local Python project regression:
**239/239 tests PASS**, pytest duration 162.47 s,
shell wall 163.31 s, exit0, captured in
`results/FULL_SUITE.{stdout,resource}`.
New PHYS43 tests exercised exact 7-interval radial coverage,
cusp grading positivity, physical source-locked same-tile
positive/signed minima, original five distributional sheets,
negative mutation of the immutable interface JSON, and
invalid geometry/configuration rejection.

## 5. Literature and cross-repo context

Relevant primary sources:
- Berz & Makino (1999), *New Methods for High-Dimensional Verified
  Quadrature*, *Reliable Computing* 5, 13–22,
  DOI 10.1023/A:1026437523641: verified Taylor-model quadrature
  and dependency control. This paper motivates the rigorous
  interval design, not the numerical values of our certificate.
- Dupuy, Dusson & Lygatsika, *A posteriori error estimates for
  Schrödinger operators discretized with linear combinations of
  atomic orbitals*, arXiv:2410.04943. This derives dual-energy
  residual bounds for atom-centred coercive SOURCE/EIGENVALUE
  problems; it is NOT an independent proof of our positive-energy
  outgoing Coulomb resolvent or inverse.
- Gordon, Jirauschek & Kärtner (2006), *Physical Review A*
  73 042505, DOI 10.1103/PhysRevA.73.042505,
  asymptotic discretization near Coulomb cusp. Scope differs
  from our exact fixed archived trial and endpoint interface
  certification.

Actual latest cross-repo metadata read 2026-10-15 KST:
- BASS_HE PR64, 16/16 conditional warm P01 opacity slabs and
  exact ray memoization (physical numbers not transported).
- bass_cr PR71, true-child-moment adaptive q cells and positive
  source envelopes (only **priority scheduling and exact
  reduction pattern** useful here).
- rei_bianchi PR122, actually completed minus-q AX08 history and
  associated signed clock split; plus PR121 AX03 frozen
  background supplier. Completely different photon/gas/
  cosmological source clocks, not new HH atom scattering data.
No other repository, astrophysical source, ionization history
or production owner file was modified by PHYS43.

## 6. Scientific admission, remaining physical obligations

**Certification claim:** SOURCE-LOCKED + DERIVED + LOCAL
IMPLEMENTATION VERIFIED for the *truncated annulus*
frozen original transformed D residual and its full-H0^1 dual.
It includes all original five distribution sheets and
the finite-width cusp log patch. It is not a uniqueness,
continuous inverse or full-space outgoing scattering error theorem.

Remains UNRESOLVED:
1. \(\{r<r_0\}\) physical origin patch/regular partial-wave
   boundary closure with correct source and no invented
   analytic extension of the frozen binary64 trial;
2. \(r>20\) screened exterior including Coulomb outgoing
   Dirichlet-to-Neumann error and tail source;
3. continuous low-Schur infsup/inverse under the actual
   outgoing noncoercive scattering boundary condition;
4. incoming adjoint/physical scattering amplitude,
   thermal HH rate and rei_bianchi consumer admission.

A solver-rate release is NOT justified by a small full
\(H^{-1}\) residual alone at positive scattering energy.
HH production remains OFF. No main-branch merge or
other-repo mutation; future work begins with a bounded
origin/exterior outgoing construction, NOT an unbounded
source and audit replay.
