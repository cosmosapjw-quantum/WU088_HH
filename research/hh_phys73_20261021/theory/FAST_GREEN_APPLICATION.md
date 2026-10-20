# PHYS73: exact linear-work application of the outgoing Coulomb Green operator

## Result and inherited operator

The PHYS72 outgoing Dirichlet kernel admits an exact two-sweep application to
any fixed radial quadrature. A ratio form needs neither an explicitly dense
Green matrix nor individually large Dirichlet/outgoing basis values. Each
angular channel and right-hand side costs O(Nr) work and O(Nr) output memory;
the dense reference costs O(Nr^2) work. These are operation counts. Actual
timing measurements are recorded separately by the native implementation.

All formulas retain B=27, k=7/10, E=49/200, eta_C=-10/7 and

\[
 A_0=-\partial_r^2+J/r^2-2/r-k^2,\qquad
 V=2(1+d^{-1})e^{-2d},\quad d=|r\mathbf n-\tfrac7{10}\hat z|.
\]

The reduced measure is dr dOmega. The completed PHYS72 operator is
R0+=(A0^D-i0)^(-1), with zero trace at B and outgoing Coulomb radiation.
Its all-angular weighted inverse bound, the growing C_j boundary weights,
and the PHYS63 existence/uniqueness result are reused without alteration.
None of the following finite-grid algebra changes those continuum claims.

For one angular index j write f=H_j^+(r)/H_j^+(B) and let a denote the
PHYS72 Dirichlet solution phi_j: a(B)=0, a'(B)=1. The use of a here separates
this fundamental solution from the atomic orbital phi=e^(-r)/sqrt(pi).
The PHYS72 convention gives a'f-af'=1 and

\[
 G_j(r,s)=a(\min(r,s))f(\max(r,s)).                 \tag{1}
\]

This is complex symmetric. Complex conjugation does not appear in (1).

## 1. Continuous and quadrature sweeps

For a smooth compact radial source g,

\[
 u(r)=f(r)\int_B^r a(s)g(s)\,ds
       +a(r)\int_r^\infty f(s)g(s)\,ds.           \tag{2}
\]

Differentiate once: the two moving-endpoint terms cancel. Differentiate
again and use a''=Q a, f''=Q f, Q=j(j+1)/r^2-2/r-k^2. Then
u''=Q u+(f'a-a'f)g=Q u-g, hence A0 u=g. The boundary and radiation condition
are those of (1). Density and the already established weighted inverse
extend this identity to the PHYS72 source space X+.

Let B<=r_0<...<r_(n-1), let w_i be the chosen radial quadrature weights,
and set x_i=w_i g(r_i). The *same quadrature matrix* is applied exactly by

\[
 y_i=f_i\sum_{a\le i}a_a x_a
       +a_i\sum_{a>i}f_a x_a.                     \tag{3}
\]

The diagonal belongs to the first sum once. There is no half-diagonal term
and no extra r^2, Coulomb factor two, or Hermitian conjugation. Nonuniform
weights are already included in x. Formula (3) changes the work required to
apply a quadrature; it does not alter that quadrature's accuracy.

For product integration, first choose a piecewise polynomial density g_h
on radial cells. Precompute the cell moments integral(a g_h) and
integral(f g_h), then accumulate (2). At cell-boundary targets no cell
straddles the derivative kink. At an interior target the containing cell
must be split at r before its two moments are taken. A global Gauss rule
across the kink cannot be assigned its smooth-integrand convergence order.
This is the same issue discussed by McBain and Armfield (2005), but the
kernel, boundary and norm here are the actual HH Coulomb ones.

## 2. Ratio representation and numerical domain

At real positive radius, H+=G+iF is nonzero because the Coulomb Wronskian
is nonzero; PHYS44 and DLMF 33.2 establish the same fact. Define

\[
 D_i=a_i f_i,\qquad \tau_i=f_i/f_{i-1}\quad (i\ge1).
\]

For any i,a,

\[
 G_{ia}=D_{\min(i,a)}
        \prod_{s=\min(i,a)+1}^{\max(i,a)}\tau_s.  \tag{4}
\]

The empty product is one. The implementation's protocol calls these arrays
d_i and t_i; d_i in this protocol is a diagonal Green value, not the
physical two-centre distance d(r,mu).

Compute the lower part in increasing radius and the upper factor in
decreasing radius:

\[
 L_0=D_0x_0,\quad L_i=\tau_i L_{i-1}+D_i x_i,
\]
\[
 T_{n-1}=0,\quad T_i=\tau_{i+1}(x_{i+1}+T_{i+1}),
 \qquad y_i=L_i+D_iT_i.                           \tag{5}
\]

Expanding the recurrences gives (4) term by term, including its diagonal.
Unlike dividing by a_i, (5) is regular at every zero of the Dirichlet
solution. It also avoids separately storing a very large a_i and very
small f_i in the forbidden high-j region. If the first node is B, D_0=0;
if it is a strict interior quadrature node, D_0 need not vanish.

There is also a useful exact profile-generation identity. With z=f'/f,

\[
 D'=1+2zD,\quad D(B)=0,\qquad
 \tau_i=\exp\!\int_{r_{i-1}}^{r_i}z(s)\,ds.       \tag{6}
\]

It follows from a'f-af'=1. Formula (6) is a mathematical alternative for
producing input profiles; the current Python preparation uses actual
high-precision Coulomb functions and records that provenance. A new
certified z-integration is not inferred from the identity alone.

Every input, output and intermediate must remain finite. Binary64 input
conversion, loss of a small term, subnormal arithmetic and product underflow
remain part of the floating arithmetic error. Avoiding the large basis
factors does not certify them. The native executable reports diagnostic
agreement with a dense calculation using the same supplied arrays; it
does not turn those arrays into special-function enclosures.

## 3. A local propagation bound when input enclosures are available

The error can be propagated without assuming a fixed relative condition
number. Suppose exact inputs lie in complex discs centered at the stored
values Dhat, tauhat, xhat with radii eD, etau, ex. Suppose an elementary
complex multiply/add has an independently bounded local arithmetic error
rho_i. Then a valid forward error recurrence is

\[
 eL_i\le(|\widehat\tau_i|+e\tau_i)eL_{i-1}
 +e\tau_i|\widehat L_{i-1}|
 +( |\widehat D_i|+eD_i)ex_i+eD_i|\widehat x_i|+\rho_i.
\]

For the backward recurrence, define Uhat_i=xhat_(i+1)+That_(i+1) and
eU_i=ex_(i+1)+eT_(i+1)+rho_add,i. Then

\[
 eT_i\le(|\widehat\tau_{i+1}|+e\tau_{i+1})eU_i
       +e\tau_{i+1}|\widehat U_i|+\rho_{mul,i}.
\]

Finally eY_i is bounded by eL_i+(|Dhat_i|+eD_i)eT_i+
eD_i|That_i| plus the final local arithmetic errors. These bounds follow
by adding and subtracting each centered product; they allow cancellation
in the answer and do not assert a relative error when the true answer
vanishes. Their practical use requires actual input radii and outward
arithmetic error bounds. This release keeps the native result's
`certified:false` status rather than inventing those inputs.

## 4. Angular multiplication and scheduling correspondence

The original V(r,mu) is axisymmetric, so signed m blocks are independent.
Use Y_jm(mu,azimuth)=p_jm(mu) exp(i m azimuth)/sqrt(2pi), with orthonormal
p_jm in L2([-1,1]). For a fixed positive angular quadrature, let P_bj be
p_jm(mu_b). Then its multiplier matrix and its matrix-free application are

\[
 V_h(r)=P^T\operatorname{diag}(w_b V(r,\mu_b))P,
 \quad V_h v=P^T[\,w_b V(r,\mu_b)(Pv)_b\,].       \tag{7}
\]

Both expressions are the same finite quadrature. Equation (7) can avoid
building an Nr-by-L-by-L matrix when few right-hand sides are required.
For many reused right-hand sides, building and caching the dense angular
matrix can be faster; the choice depends on measured workload. No
commutation of V with J is used. The all-j C_j still grow linearly, and
the excluded-angular error is estimated in its proper infinite space.

One independent (j,m,right-hand-side) sweep has O(Nr) work. Running such
jobs concurrently preserves their scalar arithmetic order and can give
bit-identical per-job results across worker counts. The current native
implementation follows this route. If only a single very long channel is
available, each affine recurrence L_i=t_i L_(i-1)+b_i has the associative
composition

\[
 (t_2,b_2)\circ(t_1,b_1)=(t_2t_1,t_2b_1+b_2),
\]

so a parallel prefix tree has O(Nr) work and O(log Nr) span in exact
arithmetic. Blelloch's scan construction supplies the abstract parallel
pattern. A floating tree changes summation order; this release does not
claim the tree and serial float result are bit-identical or implement a
tree merely to fill 64 cores. Independent jobs and independent profile
generation provide the available parallel work.

The NCP resource constraint is C_jobs*T_job<=64 with an aggregate memory
budget below 128 GiB and explicit OS/headroom reserve. Internal BLAS or
OpenMP pools must not multiply that allocation. A completed certificate is
reused even when a batch has idle cores. Hardware utilization is not a
reason to replay a closed campaign.

## 5. Verification and source scope

Connected Wolfram was actually called for two symbolic checks: a generic
five-point weighted kernel gave five exact zero differences between dense
and direct sweeps; the weighted matrix equaled its transpose, and the
ratio recurrence gave five exact zeros and the D' identity zero. These
finite symbolic identities check the implementation algebra; the arbitrary
n proof is the explicit recurrence expansion above. A failed initial
Wolfram Context call remains in the tool receipt; the evaluator succeeded.

Literature context is limited to the cited methods. McBain--Armfield's
two-point product integration, Blechta et al.'s finite-interval Chebyshev
Green matrix, and Blelloch's prefix scan do not supply the HH outgoing
boundary, Coulomb constants or all-j estimate. VigilODE's reflecting-grid
model likewise contributes no boundary condition or physical constant.
The actual HH mapping is (1)--(7), with PHYS72's independently proved
residual gain reused in ORIGINAL_SOURCE_AND_ERROR_BUDGET.md.

### Primary references

- NIST DLMF 33.2, Coulomb definitions and Wronskians:
  https://dlmf.nist.gov/33.2
- G. D. McBain and S. W. Armfield, *Two-point boundary value problems,
  Green's functions, and product integration*, ANZIAM J. 46 (2005),
  https://journal.austms.org.au/ojs/index.php/ANZIAMJ/article/view/957
- J. Blechta, V. Prusa, L. Trnka, K. Tuma, *Fast construction of the
  discrete Green operator for a second order ordinary differential
  equation*, arXiv:2412.06242, https://arxiv.org/abs/2412.06242
- G. E. Blelloch, *Prefix Sums and Their Applications*, CMU-CS-90-190,
  https://www.cs.cmu.edu/afs/cs.cmu.edu/project/scandal/public/papers/CMU-CS-90-190.html

Search and actual tool results are summarized in TOOL_EVIDENCE.json.
