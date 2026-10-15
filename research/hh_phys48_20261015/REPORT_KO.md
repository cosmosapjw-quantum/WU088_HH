# WU088_HH PHYS48: Coulomb centrifugal barrier in the original H-H model

2026-10-15 KST. Parent PHYS47 SHA 9b36c2ddb72c267cfb6a12414e4e38da36af8895.
Original frozen H(1s)+H(1s): h=-Delta/2-1/r-(1+1/s)exp(-2s),
R=kappa=7/10, s=|x-R zhat|, length a0, energy Ea=2I0.
Original trial: 6 radial panels, 21 partial waves ell=0..20,
1386 complex128 values, SHA256
f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
Original eta=F y, F=exp(exp(-s)), xi=F y-phi unchanged.

## Constructive exact rational theorem

At B=20, the central Coulomb reference radial equation has
q_l(r)=kappa²+2/r-l(l+1)/r² and centrifugal forbidden potential
U_l(r)=l(l+1)/r²-2/r-kappa². Its positive turning point
r_t(l)=[sqrt(1+kappa² l(l+1))-1]/kappa² is exact as an algebraic
expression. For ell>=15, U_l(20)>0. On [20,r_t],
U_l'(r)=2[r-l(l+1)]/r³<0, hence g_l=sqrt(U_l) decreases.

The ACTION integral A_l=int_20^rturn sqrt(U_l(r))dr is rigorously
enclosed by exact Fraction monotone rectangles. For any rational
mesh 20=r0<r1<...<rn=b<=rturn, the right rectangle sums with
isqrt-based DOWNWARD g bounds are rigorous lowers, and the left
rectangle sums with UPWARD g bounds are rigorous uppers.
The remaining turning sliver is bounded above by
(rturn_upper-b)*g_upper(b) and below by zero.

An important physically unchanged representation refinement:
instead of integer b=floor(rturn_lower), use the exact rational
b=floor(10^8*rturn_lower)/10^8. This removes the dominant
turning-point sliver error, especially ell=15 and ell=21.
No new radial trial samples, original incoming source or
scattering amplitudes are created.

Independent optional adaptive mesh follows the bass_cr PR71
TRUE-CHILD positive-bound scheduling *methodology* only:
split the cell with largest certified local upper-lower gap.
Each bisection preserves positive exact coverage; neither
physical input nor error budget is transferred from bass_cr.

Mathematical claim: rigorous ACTION brackets for the original
central Coulomb reference in the classically forbidden region.
This is NOT a rigorous tunneling probability, Coulomb irregular
H_l amplitude, noncentral screened infinite-l outgoing Green,
or a completed physical H-H ionization rate.

## Certified actions and independent Coulomb reference

Canonical uniform 1024-cell exact Fraction inclusions at r=20 a0:

| ell | lower bound | upper bound |
|---:|---:|---:|
| 15 | 0.01225020711523 | 0.01226821252637 |
| 20 | 2.97671327745284 | 2.98155300182790 |
| 21 | 3.87109623781129 | 3.87750649583268 |
| 24 | 6.94902476180021 | 6.96114569205517 |
| 28 | 11.80369695209235 | 11.82563240537532 |
| 33 | 18.82641864764983 | 18.86399540808576 |
| 41 | 31.79240978283436 | 31.86257216754310 |
| 61 | 70.95003194903357 | 71.14146138064778 |
| 80 | 114.55501665761322 | 114.91374638145794 |
| 120 | 220.30853027641067 | 221.18454568219287 |

Independent 55-digit mpmath action integrals agree with all
positive exact-rational enclosure intervals. The same
Coulomb G+iF reference has numerical log|H_l+(20)| values
3.86590122137 (ell21), 31.32939063392 (ell41),
70.32816687373 (ell61), 219.67835604996 (ell120).
The outgoing irregular reference H+(20) grows enormously
with ell: the tiny PHYS47 direct screened angular coefficient
alone does not certify propagated high-ell Coulomb waves.
These H+ values are NONCERTIFYING numeric diagnostics.

## Actual representation and optimization experiments

The previous integer turning-cut at 256 quadratic cells
bounded ell21 action in [3.7817148252,3.9274704494],
width 0.14576. With the exact rational 1e-8 turning cut,
256 uniform cells give [3.8612686285,3.8869096607],
width 0.02564. At 1024 uniform cells the ell21 width
decreases to 0.0064103. The underlying physics and frozen
source are not reinterpolated or modified.

At matched 256 cells, adaptive true-child gap refinement
bounds ell120 with width 2.82061, versus uniform width
3.50406. The additional exact heap/partition cost is
generally not efficient at this small task size.
At 1024 uniform cells, ell120 width becomes 0.87602.
Independent 1-worker and 2-worker runs use the exact
same physical source and their scientific outputs are
compared without conflating process/timing metadata.

Local Wolfram Engine15 verifies turning root, barrier
derivative, strict decreasing region and ell14/15 sign
crossing symbolically, exit0. Python tests verify original
frozen source, exact monotone inclusion, independent
75dps Coulomb action values, adaptive parent-child
monotonicity, source mutation rejection, serial/parallel
science parity. Full project suite evidence is captured
separately under the results directory.

## Connections to other current original research repos

The newest source-pinned rei_bianchi PR139 genuinely supplies
short proper-time H/He electron histories to gamma-only Thomson
radiation transport. PR140 adds source-integrated massive BASS
radial moments in an Einstein background. These do NOT provide
a microscopic H+H physical ionization cross section or
Maxwellian k_HH(T); HH_R10 stays OFF.

Only computational methodology from bass_cr PR71 (true-child
positive interval gap scheduling) is reused. The original
BASS_HE and rei_bianchi source clocks/chemistry were not copied
into this Coulomb reference boundary problem.
Active owner rei_bianchi checkout remained untouched.

## Scientific interpretation and next PHYS49

The action integral rigorously quantifies where the high-l
Coulomb classically forbidden barrier lies and how large its
WKB phase/action is. It is not by itself a proof of
propagated tunneling suppression or of the Green kernel.
The numerical size of the outgoing irregular Coulomb H+(20)
illustrates why all-l operator uniformization needs an
l-dependent boundary normalization and weighted Hilbert space.

Next construct an actual rigorous high-l Coulomb Green
comparison estimate or Dirichlet-to-Neumann block with
centrifugal barrier and correct outgoing radiation, and
combine it with the original PHYS47 angular Chebyshev
coupling bounds. Then retain the original driven physical
xi=F y-phi exterior, origin, incoming adjoint, cross section
and physical k_HH(T) with identical-pair convention before
any rei_bianchi admission.

Primary literature:
N. Michel, Uniform WKB approximation of Coulomb wave
functions for arbitrary partial wave, EPL 83, 10002 (2008),
DOI 10.1209/0295-5075/83/10002.
S.-Y. Chung, Uniform bounds, zero separation and monotonicity
for regular Coulomb functions, arXiv:2409.17305.
Neither reference is substituted for an unproved Jost
inverse bound in this original two-centre model.

Local Codex: NOT_USED; native subagent: NOT_RUN (no host
native delegation tool). No changes to rei_bianchi owner.
