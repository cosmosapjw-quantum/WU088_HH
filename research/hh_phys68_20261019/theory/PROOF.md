# PHYS68: finite-L second Born term from validated analytic panels

Independent derivation and numerical-contract review, 2026-10-19 UTC.
This note derives the target and error bounds. The numerical certificate and
its achieved tolerance are determined by the separately recorded execution,
not by this note. Read LITERATURE_RETRIEVAL.json for actual primary-source reads.

## 1. Fixed physical object and units

The original Hamiltonian, atomic coordinates and frozen source remain fixed:
B=27, k=7/10, E=49/200 Hartree, shift R0=7/10 and
h=-Delta/2-1/r-(1+1/d) exp(-2d). The physical inverse-length DtN convention
is Z=+u' u^{-1}, with the radial derivative in the direction of increasing r.
The screened radial equation is

\[
u''+(Q_C+V)u=0,\quad
Q_{C,\ell}=k^2+2/r-\ell(\ell+1)/r^2,\quad
V(r,\mu)=2(1+1/d)e^{-2d}.
\]

Here all displayed coordinate numbers are in r/a0 and k*a0. Numerical D and q
values acquire a0^{-1}; numerical V, K and the D2 integrand acquire a0^{-2}.
An integration differential contributes a0. The two components in the
first-order ODE majorant below are (F,d_(r/a0)F), so they have equal numerical
dimension. No norm compares dimensional F and d_(physical r)F without this
coordinate conversion.

The outgoing Coulomb convention is H^+=G+i F_C with eta_C=-10/7, rho=k r,
and d_r=k d_rho. The symbol F_C in this sentence denotes NIST's regular
Coulomb function. In the rest of this note

\[
F_\ell(r):=H_\ell^+(r)/H_\ell^+(B)
\]

denotes the normalized outgoing ratio, not F_C, the source map F, eta=Fy,
or the original source-driven xi=Fy-phi. NIST DLMF 33.2.1, 33.2.11,
33.2.12 and 33.4.4 fix the ODE, outgoing choice, Wronskian and derivative
recurrence. The real-axis Wronskian implies H^+(B) is nonzero.

The scoped numerical target is the original physical second Born term
D_{2,21,20}^{(L=28),m=0}(B), initially with the screen truncated at T=65.
Axisymmetry preserves m; every internal mode j=0,...,28 is retained.

## 2. Riccati sign, source factor and finite-cutoff definition

Introduce a formal parameter lambda multiplying the original V and set
Z=Z_C+D. The exact Riccati difference is

\[
D'+Z_CD+DZ_C=-\lambda V-D^2.
\]

For a screen cut at T, D(T)=0 because the exterior beyond T is exactly
Coulomb. Writing D=sum_{n>=1} lambda^n D_n gives

\[
D_1'+Z_CD_1+D_1Z_C=-V,\qquad
D_2'+Z_CD_2+D_2Z_C=-D_1^2.
\]

Thus both backward integral formulas have positive signs. The factor 2
arising from the original -Delta/2 Hamiltonian is already in V=2S.
There is no additional factor 2 multiplying the second-order convolution:
lambda^2 in D^2 is D_1D_1.

Let P(r,t)=diag(H_l^+(t)/H_l^+(r)). Then

\[
D_1^T(r)=\int_r^T P(r,t)V(t)P(r,t)\,dt.
\]

For each required pair define

\[
K_{\ell j}(r)=F_\ell(r)F_j(r)V_{\ell j}(r),\qquad
q_{\ell j}(r)=F_\ell(r)F_j(r)D_{1,\ell j}^T(r)
             =\int_r^T K_{\ell j}(t)\,dt.
\]

Consequently q'=-K and q(T)=0. Real-axis V is real symmetric in the
normalized m=0 basis, and its analytic continuation is transpose symmetric.
D1 and q inherit this transpose symmetry. Expanding the matrix product,
using F_l(B)=1, and cancelling the external normalized factors gives

\[
\boxed{
D_{2,\ell p}^T(B)=
\sum_{j=0}^{L}\int_B^T
       \frac{q_{\ell j}(r)\,q_{p j}(r)}{F_j(r)^2}\,dr .
}
\]

This product is complex bilinear. Complex conjugation would change the
Riccati coefficient. Each integrand has units a0^{-2}, and D2 has a0^{-1}.
At V=0 all q and D2 vanish. Scaling V by lambda scales q linearly and D2
quadratically. These checks distinguish the physical coefficient from an
unscaled epsilon-normalized coefficient.

An independent manufactured algebra check takes one channel, F=1 and
V=kappa constant. Then q=kappa(T-r), and the formula gives
D2(B)=kappa^2(T-B)^3/3. Choosing kappa=i gives a negative real D2.
An inserted conjugate would give the opposite sign; an extra factor 2
would double the exact coefficient. This check concerns the algebraic
contract and is not a substitute model for the original physical run.

For real r>T the cut-source solution is zero. For local analytic estimates
near T, however, q^T(z) is the analytic primitive integral from z to T of the
original uncut K(z). It continues through T and need not vanish on the
other side. The panel algorithm must not insert a Heaviside cutoff inside
a complex Cauchy disk. On the required real interval [B,T], this primitive
is exactly the physical cut-source q.

## 3. Analytic screened-potential bound on a complex radial disk

Take z in a closed disk |z-c|<=s with c real and
a=c-s-R0>0. For mu in [-1,1], put

\[
w=z-R_0\mu,\qquad b^2=R_0^2(1-\mu^2)\ge0,\qquad
d(z,\mu)=\sqrt{w^2+b^2}
\]

with the principal square root. Write w=x+i y. Then x>=a>0. If y is nonzero,
Im(w^2+b^2)=2xy is nonzero. If y=0, w^2+b^2=x^2+b^2>0. The radicand
therefore avoids both zero and the principal square-root branch cut.
This proves the relevant branch is holomorphic on the entire half-plane
Re z>R0, uniformly on compact subsets in mu.

Let u=Re sqrt(w^2+b^2)>0. The exact square-root identity gives

\[
u^2=\frac{|w^2+b^2|+x^2-y^2+b^2}{2}.
\]

To prove u>=x it suffices to establish
|w^2+b^2|>=x^2+y^2-b^2. If the right side is nonpositive this is immediate.
Otherwise both sides are nonnegative and

\[
|w^2+b^2|^2-(x^2+y^2-b^2)^2=4x^2b^2\ge0
\]

proves the inequality by squaring. Hence Re d>=x>=a and |d|>=a, so

\[
|(1+1/d)e^{-2d}|\le(1+1/a)e^{-2a}.
\]

For the m=0 orthonormal angular basis
phi_l(mu)=sqrt((2l+1)/2) P_l(mu), one has
V_lj(z)=integral_{-1}^1 phi_l(mu)V(z,mu)phi_j(mu)dmu.
Cauchy-Schwarz for these normalized basis functions yields

\[
\boxed{\sup_{|z-c|\le s}|V_{\ell j}(z)|
       \le M_V(c,s):=2(1+1/a)e^{-2a}.}
\]

There is no angular dimension factor. The same bound works for other
normalized fixed-m angular functions, although the present implemented
coefficient formula is scoped to m=0. Compact uniform domination also
justifies holomorphic dependence of each angular matrix entry on z.
This bound treats the original exact angular integral; no floating
Gauss node, weight or basis approximation is used in the majorant.

At b=0 equality Re sqrt(w^2)=Re w holds on Re w>0. For mu=+1 and real z>R0,
the distance is z-R0 and the potential amplitude bound is attained.
Thus the branch estimate has the correct axial and zero-shift limits.

## 4. Coulomb Taylor coefficient and disk contract

Write x=z-c and F_l(c+x)=sum_{n>=0} f_{l,n} x^n. The exact radial ODE
coefficient expansion is

\[
Q_{\ell,n}
=\delta_{n0}k^2+
 \frac{2(-1)^n}{c^{n+1}}-
 \frac{\ell(\ell+1)(n+1)(-1)^n}{c^{n+2}}.
\]

Starting from enclosed F_l(c) and F_l'(c), the recurrence

\[
f_{\ell,n+2}
=-\frac{\sum_{s=0}^{n}Q_{\ell,s} f_{\ell,n-s}}
        {(n+1)(n+2)}
\]

encloses each exact Taylor coefficient. Computing a polynomial with this
recurrence alone does not establish a remainder estimate.

For a larger disk |x|<=R, c-R>R0, set

\[
Q_* = k^2+2/(c-R)+\ell(\ell+1)/(c-R)^2,\quad
A_*=\max(1,Q_*).
\]

The first-order system for (F,F') has infinity-norm coefficient bound A_*.
Integrating along a straight complex segment of length at most R and applying
the integral inequality gives

\[
M_{F,\ell}(R)=
 \max(|F_\ell(c)|,|F_\ell'(c)|)\exp(R A_*)
 \ \ge\ \sup_{|x|\le R}|F_\ell(c+x)|.
\]

The ODE coefficients are analytic in a neighborhood of the closed disk.
Initial data select the same outgoing solution by local uniqueness; no
asymptotic replacement of the original Coulomb function is made.

For any analytic g with sup_{|x|<=R}|g(c+x)|<=M and coefficients through
degree N, the Cauchy bound |g_n|<=M/R^n implies, for 0<=s<R,

\[
E_g(s):=M\frac{(s/R)^{N+1}}{1-s/R},\qquad
\left|g(c+x)-\sum_{n=0}^N g_nx^n\right|\le E_g(s)
\quad(|x|\le s).
\]

The same formula remains valid with enclosed coefficients when the finite
polynomial evaluation retains their full balls.

To use a reciprocal on a smaller disk rho<R, calculate the outward bound

\[
m_\ell=
 |f_{\ell,0}|_{\rm lower}
 -\sum_{n=1}^N |f_{\ell,n}|_{\rm upper}\rho^n-E_{F,\ell}(\rho).
\]

Only m_l>0 proves zero-freeness and |1/F_l|<=1/m_l on that disk. Failure
to obtain a positive lower bound is an unresolved disk estimate, not a
proof of a zero. The real-axis Wronskian by itself does not establish this
complex-disk gate.

## 5. Kernel and first-order profile enclosure

K_lj=F_l F_j V_lj is analytic on the large disk and has the bound

\[
M_{K,\ell j}(R)=M_{F,\ell}(R)M_{F,j}(R)M_V(c,R).
\]

Its coefficients through N are the exact finite convolution of the
enclosed Coulomb coefficients and the enclosed exact-angular Laurent
formula from PHYS67. Terms of order <=N depend only on input coefficients
of order <=N; no discarded higher coefficient can enter these terms.

A sharper inner-disk kernel bound can be obtained without new function
evaluations:

\[
M_{K,\ell j}(\rho)=
 \sum_{n=0}^N |K_{\ell j,n}|_{\rm upper}\rho^n
 +E_{K,\ell j}(\rho).
\]

The current implementation instead obtains M_K(rho) directly as
M_F,l(rho) M_F,j(rho) M_V(c,rho), rerunning the same proved first-order
ODE majorant formula at radius rho. Both formulas are rigorous; the latter
is the actual code path local_coulomb_majorant and small_k.

All factors, absolute upper bounds and exponentials in these expressions
must be outward ball bounds, never diagnostic decimal values.

Consider a real panel [c-h,c+h], 0<h<=rho<R, and let q_right be a ball
containing the exact q(c+h). The initial panel at T starts from q(T)=0.
Because q'=-K,

\[
q(c)=q(c+h)+\int_0^hK(c+x)\,dx .
\]

The center enclosure uses q_right plus
sum_{n=0}^N K_n h^{n+1}/(n+1), inflated by h E_K(h).
This inflation is a valid conservative bound on the half-panel integral.
The next left endpoint can be computed directly as

\[
q(c-h)=q(c+h)+
 2\sum_{\substack{0\le n\le N\\n\ {\rm even}}}
       K_n\frac{h^{n+1}}{n+1}
 +\mathcal E,\qquad |\mathcal E|\le2h E_K(h).
\]

For the local degree-(N+1) profile, the nonconstant Taylor coefficients are
q_n=-K_{n-1}/n, n=1,...,N+1; the q_0 ball contains the complete center
uncertainty, including earlier-panel carry and this half-panel integral.
At an offset |x|<=h, its primitive remainder is bounded by |x| E_K(|x|).
The degree-N D2 series below only needs q coefficients through degree N;
discarding q_(N+1) from that product does not alter those coefficients.

The exact primitive is bounded on |x|<=rho by

\[
M_{q,\ell j}(\rho)
=|q_{\ell j}(c+h)|_{\rm upper}
 +(\rho+h)M_{K,\ell j}(\rho).
\]

Indeed, the straight segment from h to any x in the radius-rho disk remains
inside that convex disk and has length at most rho+h. Cauchy's estimate
with this majorant supplies a uniform profile remainder. Propagating
intervals without their correlations can widen these enclosures, but it
does not remove the exact profile from them.

## 6. Certified second-order panel integral

For j=0,...,L, assume the strictly positive zero-free bound m_j on the
same radius-rho disk has actually been obtained. Define

\[
I_j(z)=q_{\ell j}(z)q_{p j}(z)/F_j(z)^2,\qquad
M_{I,j}=
 M_{q,\ell j}(\rho)M_{q,p j}(\rho)/m_j^2.
\]

All three factors are analytic there, so I_j is analytic and has the stated
supremum bound. Reciprocal coefficients are computed by the exact series
identity F_j(1/F_j)=1; the finite coefficient arithmetic is performed in
balls and includes the full q_center balls.

Let i_{j,n}, n=0,...,N, enclose the Taylor coefficients of I_j. Then

\[
J_j=2\sum_{\substack{0\le n\le N\\n\ {\rm even}}}
       i_{j,n}\frac{h^{n+1}}{n+1}
\]

is the polynomial panel integral, with exact-function truncation bound

\[
\boxed{
\left|\int_{c-h}^{c+h}I_j(r)\,dr-J_j\right|
\le 2h M_{I,j}
 \frac{(h/\rho)^{N+1}}{1-h/\rho}.
}
\]

The accepted pre-run request uses R=2, rho=1/2, h=1/4, N=80, arithmetic
precision 384 bits and angular coefficient precision 1024 bits. It satisfies
all strict radius relations; 76 adjacent panels cover [27,65] exactly.
The earlier proposal N=64 also obeys the theorem but is not the current
execution request.
Their boundaries and powers are rational. If a numerical gate fails, its
failure must be reported or the radius/precision/degree changed in a new
explicit request; a failed reciprocal may not silently become a midpoint
division.

Summing these containing balls for all 29 internal j values and all panels
contains the exact finite-cutoff D2 entry. The same q profiles can be
reused within this computation. No first-order NCP campaign or completed
PHYS67 point certificate needs to be rerun to justify this algebra.

For even N, one may sharpen the displayed conservative integration tail:
the first omitted odd term integrates to zero, and an admissible bound is

\[
\frac{2h M_{I,j}}{N+3}
 \frac{(h/\rho)^{N+2}}{1-(h/\rho)^2}.
\]

The simpler bound is already sufficient for rigor; any use of the sharper
formula must be identified in the execution contract.

## 7. PR115 radial cutoff and exact claim gate

PR115 defines D_(n,T) by setting the physical screen to zero for r>T.
This is precisely the endpoint construction above. For the unchanged
finite projection, the inherited theorem gives

\[
|D_{2,21,20}^{L}(B)-D_{2,21,20}^{L,T}(B)|
\le\beta_2=a\chi e^{-2(T-B)},\quad
a=\Gamma\delta/2,\quad
\chi=\Gamma^2\delta/2,\quad \delta=3\,10^{-23}.
\]

The uniform Gamma64=32400 is valid for L28 and gives the existing
outward bound beta2(T65)<7.541139e-66 a0^{-1}. A smaller Gamma28 may be
used only after binding it to the inherited ratio maximum over every
ell=0,...,28. Gamma21 from the earlier single D1 calculation cannot be
substituted: the present D2 contains j up to 28.

The pre-run absolute goals are 1e-45 a0^{-1} for every required D1 pair
at B, including beta1, and 1e-62 a0^{-1} for the full-radial D2 target,
including beta2. The selected two rows contain 57 distinct symmetric pairs
and all 29 intermediate j values. The D1 tolerance is a B-endpoint goal;
uniform panel enclosures alone do not assert this tolerance at every r.

If C_num is the reported numerical center and e_num an outward absolute
complex radius of the finite-T result, then

\[
|D_2^{L}(B)-C_{\rm num}|\le e_{\rm num}+\beta_2.
\]

The exact numerical ball and the analytic tail must remain separately
available in the receipt. If a Euclidean error disk is stored by inflating
both Cartesian radii, the resulting box is an enclosure; however, its
reported scalar radius must use the chosen Euclidean/L1 convention
consistently. Printing a rounded decimal center does not preserve the
small error claim unless display-rounding error is also included.

This closes numerical integration, coefficient roundoff, exact-angular
evaluation and continuous Coulomb/profile approximation for the stated
finite-L D2 computation when its numerical gates pass. It leaves the
higher-order sum, excluded-angular response, original xi, origin/incoming
adjoint, sigma(E) and Maxwellian k_HH(T) as their existing distinct
obligations. PHYS63 remains ESTABLISHED and HH_R10 remains OFF.

## 8. Implementation obligations and independent decision

The implementation must preserve all of the following contracts:

1. Original physical V=2S, increasing-r derivative and H+=G+iF.
2. Every internal j=0,...,28 and no complex conjugation in q_lj q_pj.
3. Exact rational centers/radii/parameters and full ball coefficients.
4. Analytic uncut K across T for Cauchy disks, even on the last panel.
5. Proved large-disk majorants, not sampled maxima.
6. Positive computed lower bounds for each complex reciprocal disk.
7. q terminal/carry uncertainty retained in every center and coefficient.
8. Outward Taylor-integral remainder on each panel and complete sums.
9. Separate numerical, cutoff and final absolute-radius fields.
10. Hash-bound request, runtime versions and actual achieved-goal check.

No mathematical obstruction was found in the stated construction.
The derivation is accepted under these explicit premises. Whether the
reference degree/precision delivers the requested radius is a numerical
execution question, and is not asserted in advance. No new strong no-go
is claimed. The independently reviewed new object is the finite-L D2
profile/integration certificate, not a reopening of previously closed
physical existence or completed execution obligations.

## Primary-source correspondence

- NIST DLMF https://dlmf.nist.gov/33.2 and https://dlmf.nist.gov/33.4:
  Coulomb ODE, outgoing convention, Wronskian and derivative recurrence.
- NIST DLMF https://dlmf.nist.gov/1.9:
  analytic Taylor expansions and Cauchy coefficient estimates.
- Official FLINT https://flintlib.org/doc/acb_calc.html:
  analytic-domain checks and piecewise Taylor integration with Cauchy
  remainder. The fetched page identifies itself as 3.7.0-dev documentation;
  this source is methodological context, not installed-version evidence.
- Fredrik Johansson (2018), https://arxiv.org/abs/1802.07942,
  DOI 10.1007/978-3-319-96418-8_30:
  validated ball integration and the need to assess the actual output
  radius instead of treating a requested tolerance as an achieved result.

SciSpace and Exa were both used. The unsuccessful fetch of Berz (1997)
is recorded but is not a proof dependency. These primary sources support
the general analytic/numerical principles. The application-specific
complex-screen bound, transformed D2 formula and error assembly above
were directly derived here; no literature-priority claim is made.

