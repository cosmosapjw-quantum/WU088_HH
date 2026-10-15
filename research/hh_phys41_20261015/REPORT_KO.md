# WU088_HH PHYS41: 6개 frozen radial panel 전체의 Bernstein bulk 인증

2026-10-15 KST. Parent: PHYS40 PR79 head 2729e163086d123008d01c706df74a813a844b1f.
Selected node: C7B_ALL_PANEL_RADIAL_INTEGRATION_AND_CONTINUOUS_OUTGOING_DUAL.
Result: only its original whole-volume broken bulk component is newly certified.
No physical scattering amplitude, HH rate, outgoing inverse or consumer admission.

## Physics and source identities

Original frozen-direct spectator H(1s)+H(1s) Hamiltonian:

\[
h_\lambda=-\tfrac12\Delta-\frac1r-\lambda(1+s^{-1})e^{-2s},
\quad s=|\mathbf r-R\hat z|,\quad R=\kappa=7/10,\ \lambda=1 .
\]

Physical length a0; energy Ea=2 I0=27.211386245980 eV. Preserve the distinct
source I0=13.605693122990 eV and receiver chiH=13.598434599702 eV.
Keep eta=F y, F=exp(exp(-s)) and original PHYS36, PHYS39, PHYS40 source/lift.
Original SHA256 for frozen file FROZEN_U_SUBSET.npz:
f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
Source has 21 l modes, six dyadic radial panels, 11 nodes/panel,
1386 actual complex128 samples, exactly interpolated at their binary64 nodes.
The tiny difference between the actual 0.7 dyadic interface and exact R=7/10
is preserved.

## Derived theorem, same original full-coupled operator

For E(s)=exp(-s) and the actual cusp-conjugated potential

\[
U(s)=E(s)[(1-E(s))/s-1/2-3E(s)/2],
\quad (1-e^{-s})/s=\int_0^1e^{-st}dt,
\]

we have E<=q<=(1) and -1<=U/E<=1/2, hence |U|<=E
including the continuous limit s=0.
With S0(r)=2(1+kappa^2)exp(-r), the exact PHYS40
G=sqrt(4 pi)*physical_residual obeys

\[
G=(A-S_0)-2E\,\hat s\cdot\nabla B-2UB+
 S_0(1-e^{-E}) .
\]

A=sum_l sqrt(2l+1) D_l u_l/r P_l(mu),
B=sum_l sqrt(2l+1) u_l/r P_l(mu),
D_l u=u''+(kappa^2+2/r-l(l+1)/r^2)u.
The unit vector is undefined only at the isolated coalescence point;
the a.e. inequality |hat s . grad B|<=|grad B| is sufficient.
No fake uniform Lipschitz bound and no s^-1 smoothing are used.

For rational tile I=[a,b], a>0, put d=dist(I,R).
Form exact radial polynomial numerators r^2 D_l u_l and r u'_l-u_l.
For l=0 subtract the exact source r^3 S0(r) before any norm.
Represent that exponential term by a 24-order Taylor polynomial centered
at a, with a certified 192-term positive rational exponential enclosure.
The exact r^3 factor cancels before the Taylor error is evaluated, so no
spurious b^3/a^3 error inflation is used.

For p(x)=sum_j c_j x^j on normalized panel and
x=x0+(x1-x0)t, its Bernstein coefficients are exactly

\[
\beta_k=\sum_j c_j\sum_{i=0}^{\min(j,k)}
 {j\choose i} x_0^{j-i}(x_1-x_0)^i
 {k\choose i}/{n\choose i}.
\]

Since each B_{kn}(t)>=0 and sum B_{kn}=1 on [0,1],
sup_I |p|<=max_k |beta_k|. Exact Fraction coefficients and
cached monomial-to-Bernstein rational matrices bind every radial numerator.
The real and imaginary maxima are summed outward, with no complex
cancellation falsely assumed.

Let Z_l, V_l, M_l bound respectively
|r^2 D_l u_l -delta_l0 r^3 S0_approx|, |r u'_l-u_l|,
and |u_l|. The rigorous shell bounds are

\[
Q_D^2=\sum_l (Z_l/a^3)^2,\quad
Q_\nabla^2=\sum_l[(V_l/a^2)^2+l(l+1)(M_l/a^2)^2],\quad
Q_B^2=\sum_l(M_l/a)^2.
\]

Including the certified normalized source approximation epsilon_I,

\[
\sup_{r\in I}\|\mathcal R(r)\|_{L^2(S^2)}
\le Q_D+\epsilon_I+
2e^{-d}(Q_\nabla+Q_B)+2(1+\kappa^2)e^{-(a+d)}=:Q_I.
\]

Exponential upper enclosures are exact inverse positive-Taylor sums;
square-root upper enclosures use integer isqrt/directed decimals.
The full broken bulk certificate is

\[
\|\mathcal R\|_{L^2(r_0<r<20)}
\le \left[\sum_I(b_I^3-a_I^3)Q_I^2/3\right]^{1/2}.
\]

All six actual panels are covered. The cusp shell is not excluded.

For the full H1 norm sqrt(||v||_L2^2+||grad v||_L2^2),
the bulk H^-1 dual norm is bounded by its L2 norm. If instead H0^1
is equipped with the *gradient-only* norm, the dual estimate must use
Poincare: zero-extend to the ball of radius 20, lambda_1=pi^2/400,
pi>223/71, giving upper (1420/223)*bulk L2.
The PHYS38 interface certificate explicitly uses the full H1 norm;
the two dual conventions are not conflated.

## Actual local calculations and benchmark

Same frozen source, Python3.12.3, NumPy2.4.2, SciPy1.17.0.
The pyproject numpy==2.3.5 pin is an uncorrected runtime environment drift,
not a silent model change. CPU oversubscription blocked by
OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1, MKL_NUM_THREADS=1.

| Exact regular-panel divisions | Workers | Tiles | New rigorous broken L2 upper | wall |
|---|---:|---:|---:|---:|
| 16 | 1 | 98 | 4.089392209924 | 34.74 s |
| 16 | 4 | 98 | 4.089392209924 | 13.39 s |
| 32 | 4 | 178 | 3.801538612271 | 18.28 s |

16 regular-panel scientific outputs, all subtiles and intervals,
are identical between 1 and 4 workers after removing timing/worker fields.
Measured speedup 2.59x. Parent-only /usr/bin/time RSS is not the
combined four-child RSS. First panel always uses separate exact rational
3:2 geometric grading near r0, hence 18 rather than 16/32 cells.

P32 panel L2 bounds in order:
0.244241787979, 2.054468343490, 3.091296168606,
0.783465562263, 0.035542839916, 0.002830622486.

Independent NONCERTIFYING original screened s-coordinate full PDE
Gauss diagnostics (all six panels, NumPy float64):
48x128 -> 0.00174473948448157;
96x256 -> 0.00174474274907638.
These are sampled values, NOT a certified convergence order or an
inclusion interval. The P32 rigorous bound is about 2179x looser.
Prior PHYS39 annular full-H1 dual upper 2.516921964597789440
is tighter and REMAINS the inherited accepted envelope.
New scientific progress: original whole-volume all-angle certified
strong bulk + independent float crosscheck, NOT a tighter estimate.

## Implementation and verification

New modules/scripts:
src/wu088_hh/phys33_panel_bernstein.py;
scripts/phys33_panel_bernstein.py;
scripts/phys33_panel_float_preview.py;
tests/test_phys33_panel_bernstein.py.
Evidence in research/hh_phys41_20261015/results.

Cached exact rational Bernstein transform is shared by all 21 complex modes
per radial tile. Safe forkserver multiprocessing with up to 4 workers
uses independently verified original SHA and deterministic panel order.
All source/radial basis operations remain exact rational up to directed
decimal presentation. No local Codex was used; native subagent tools
are unavailable, and process workers are not subagents.

Actual full regression on Ubuntu: 214 passed in 144.92 s,
exit code 0. This comprises the prior full-repository 204 tests plus
10 new PHYS41 tests. Independent source polynomial 85-digit mpmath
diagnostic, exact rational Bernstein sample containment, source SHA,
six-panel coverage, PHYS40 shell containment, invalid-input rejection
and transform cache reuse are exercised. Measured /usr/bin/time and
pytest stdout are stored in results/FULL_SUITE.{resource,stdout}.
Baseline PHYS40 targeted 25/25 had also passed separately.

An initial test wrongly expected cache hits without a repeated call.
Classification TEST_DESIGN_ERROR; fixed, preserving that failure in
the execution narrative. An early redundant b^3/a^3 multiplier was
mathematically conservative but impractically loose, classified as
BOUND_LOOSENESS and removed through exact source factoring.
Wolfram Language algebra checks: source split zero, U identity zero,
quartic Bernstein identity zero in a clean stateless run.
No Wolfram/xAct tensor claim is newly made by PHYS41.

Literature considered: Kato Coulomb cusp/modern coalescence,
Gordon et al. Phys Rev A 73 042505 (2006), DOI 10.1103/PhysRevA.73.042505;
Feldkamp J Chem Phys (1996), DOI 10.1063/1.471754;
arXiv:2204.09897. Literature is context, not a source of our computed bounds.

Other repos actually inspected read-only on 2026-10-15:
BASS_HE PR64 16 saved warm P01 cells and exact ray caching;
bass_cr PR71 source-conditioned adaptive q bin;
rei_bianchi PR118 signed AX08 and guarded state.
Only reuse *cache/interval/adaptive computational methods*;
no helium/photon/radiation histories or cosmological numbers imported.
Cold HH source/production remains OFF. No repo outside WU088_HH mutated.

## Remaining DAG and acceptance gate

Completed scoped: original 6-panel piecewise bulk with rigorous
rational enclosure, source identity, sampled diagnostic,
serial/parallel identity and measured speedup.
NOT DONE: 5 distributional interface sheets in *this* new certificate;
origin r<r0 and screened exterior r>20; physical outgoing DtN,
continuous low-Schur infsup, incoming adjoint,
whole-space intensity, thermal rate and consumer binding.
Next selected node: C7B_STRONG_2D_RADIAL_ANGULAR_COUPLING_ADAPTIVE_ENCLOSURE.
Construct cusp-safe joint (r,s) numerator N=sG bounds to remove
the >2000x triangular-inequality slack, combine PHYS38 jump evidence,
then address physical origin/exterior and continuous inverse.
All physical HH rate fields remain null, no production GO decision.

Run certified: python3 scripts/phys33_panel_bernstein.py --pieces 32 --workers 4 --out /tmp/PHYS41_BULK.json
Run NONcertifying: python3 scripts/phys33_panel_float_preview.py --nr 96 --ns 256 --out /tmp/PHYS41_PREVIEW.json
