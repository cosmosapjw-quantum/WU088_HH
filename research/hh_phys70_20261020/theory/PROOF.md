# PHYS70: exact HH shifted-block elimination and ordered numerical reuse

Date: 2026-10-20 UTC. Status: **PROVED_SCOPED_ALGEBRA_AND_SOURCE_CONTRACT**.

The original finite-dimensional HH second-Born equations admit a full
Rosenbrock shifted solve with a fixed number of arithmetic operations per
angular channel. The construction retains the derivatives through both shared
external channels, the bilinear second-Born row, and the explicit time
derivative. Its oscillator denominators satisfy the exact uniform bound

\[
\boxed{
 1+(h\gamma)^2Q_j(r)\ \ge\
 \frac{17171964889}{18225000000}>0.94222029569
}
\tag{P70.1}
\]

for every integer \(0\le j\le64\), every \(r\ge27\), and
\(0\le h\le1/2,\ 0<\gamma<53/250\). The implemented driver uses the
narrower physical interval \(27\le r\le65\).

The equations and proofs below concern the original HH model and its existing
finite-\(L\), finite-radius, angular-quadrature client. Actual binary64 checks
are identified in Section 9. The all-angular PHYS69 certificate is inherited
evidence identified in Section 10. This note was written by the independent
reviewer without changing implementation code or running another integration,
test suite, or literature search.

## 1. Fixed physical object and the numerical variables

All coordinates are atomic. Write the Hamiltonian as \(\mathsf H\), reserving
\(h\) for an integration step:

\[
\mathsf H=-\frac{\Delta}{2}-\frac1r-
 \left(1+\frac1d\right)e^{-2d},\qquad
d=|\mathbf x-R_0\hat{\mathbf z}|,\qquad
R_0=\frac7{10}.
\tag{P70.2}
\]

The fixed boundary, wave number, and energy are
\(B=27,\ k=7/10,\ E=k^2/2=49/200\) Hartree. The reduced radial screened
coupling and unperturbed radial coefficient are

\[
V(r,\mu)=2(1+d^{-1})e^{-2d},\quad
d^2=r^2+R_0^2-2rR_0\mu,\qquad
Q_j(r)=k^2+\frac2r-\frac{j(j+1)}{r^2}.
\tag{P70.3}
\]

The outgoing Coulomb normalization is

\[
H_j^+(r)=G_j(\eta_C,kr)+iF_j^C(\eta_C,kr),\quad
f_j(r)=\frac{H_j^+(r)}{H_j^+(B)},\quad
g_j(r)=\partial_r f_j(r),\quad \eta_C=-\frac{10}{7}.
\tag{P70.4}
\]

Thus \(f_j''+Q_jf_j=0\), and \(\partial_r=k\partial_\rho\) in a
Coulomb-function initializer. The Coulomb parameter \(\eta_C\), the original
source \(\eta=Fy\), and the original response \(\xi=Fy-\phi\) are distinct.
The boundary convention remains \(Z=+u'(B)u(B)^{-1}\).

The original frozen source NPZ has SHA256
f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
The executable checks that identity. Its Coulomb initial conditions are
separately supplied by the saved seed input; the source hash check does not
apply the source to solve for \(\xi\).

For \(m=0\), let
\(p_j(\mu)=\sqrt{(2j+1)/2}\,P_j(\mu)\). These real functions are orthonormal
on \([-1,1]\). Consequently

\[
V_{\alpha j}(r)=\int_{-1}^{1}
 p_\alpha(\mu)p_j(\mu)V(r,\mu)\,d\mu .
\tag{P70.5}
\]

The existing angular quadrature uses \(N_q\) Gauss-Legendre nodes and weights.
Denote its mathematical sum by

\[
V_{\alpha j}^{[N_q]}(r)
 =\sum_{q=0}^{N_q-1}
 p_\alpha(\mu_q)p_j(\mu_q)V(r,\mu_q)w_q .
\tag{P70.6}
\]

The implemented sum is evaluated in binary64 using the pinned generator,
the same stored node order, and the same normalized Legendre recurrence as
PHYS69. Superscript \([N_q]\) keeps angular quadrature separate from the exact
angular integral.

For the external indices \(a=21,\ b=20\), set \(n=L+1\), with
\(21\le L\le64\), and \(T=65\). Define

\[
q_{\alpha j}^{T,[N_q]}(r)
  =\int_r^T f_\alpha(s)f_j(s)V_{\alpha j}^{[N_q]}(s)\,ds,
\quad
D_{2,L,T,[N_q]}
  =\sum_{j=0}^{L}\int_B^T
    \frac{q_{aj}^{T,[N_q]}(r)q_{bj}^{T,[N_q]}(r)}
         {f_j(r)^2}\,dr .
\tag{P70.7}
\]

Let \(Z_\lambda\) be the outgoing boundary map for
\(A_\lambda=2\mathsf H_C-k^2-\lambda V\), where
\(\mathsf H_C=-\Delta/2-1/r\). The relation to the physical coefficient is
the inherited PHYS69 identity
\(Z_\lambda-Z_0=\lambda D_1+\lambda^2D_2+O(\lambda^3)\), hence
\(D_2=Z''(0)/2\). In its exact all-angular/all-radial version, (P70.7) has
the exact \(V_{\alpha j}\), all intermediate \(j\), and upper radial endpoint
\(\infty\). Its plus sign follows from the outgoing Green function with
boundary derivative \(+\!f_j\) at \(B\). Its products are complex bilinear:
the incoming adjoint in the boundary identity becomes an outgoing factor
after conjugation in this real angular basis. The coefficient therefore has
neither a further conjugation nor an extra factor two. These identifications
are proved in the [PHYS69 mathematical note](../../hh_phys69_20261019/theory/PROOF.md).

Introduce inward time \(\tau=T-r\), and the exactly represented powers of two
\(S=2^{80}\), \(S^2=2^{160}\). The stored complex state is

\[
y=(f,g,A,B^{\rm row},z),\qquad
A_j=S q_{aj}^{T,[N_q]},\quad
B_j^{\rm row}=S q_{bj}^{T,[N_q]},
\]

\[
z(\tau)=S^2\sum_{j=0}^{L}\int_{T-\tau}^{T}
 \frac{q_{aj}^{T,[N_q]}(s)q_{bj}^{T,[N_q]}(s)}{f_j(s)^2}\,ds .
\tag{P70.8}
\]

Below \(B_j\) means \(B_j^{\rm row}\), whereas unindexed \(B\) is always the
physical boundary radius. The real-interleaved storage dimension is
\(d_{\rm R}=2(4n+1)=8n+2\). Initially \(A=B^{\rm row}=z=0\), and the seed gives
\(f_j(T),g_j(T)\). At \(\tau=38\), \(z/S^2=D_{2,L,T,[N_q]}\) for the exact
ODE with the stated initial data. Roundoff in those data and in integration
is part of the separate numerical error.

Put \(c_{aj}=S V_{aj}^{[N_q]}\) and \(c_{bj}=S V_{bj}^{[N_q]}\).
Differentiating (P70.8) with respect to \(\tau\) gives the original client:

\[
\boxed{
\begin{aligned}
\dot f_j&=-g_j,&
\dot g_j&=Q_jf_j,\\
\dot A_j&=c_{aj}f_af_j,&
\dot B_j&=c_{bj}f_bf_j,\\
\dot z&=\sum_{j=0}^{L}\frac{A_jB_j}{f_j^2}.
\end{aligned}}
\tag{P70.9}
\]

The powers of \(S\) cancel from the last row. Equations (P70.3), (P70.6),
and (P70.9) map directly to the unchanged
[PHYS69 client](../../../native/phys69_vigilode/src/lib.rs) and the new
[kernel](../../../native/phys70_optimized/src/kernel.rs).

## 2. Full frozen Jacobian, including the shared channels

Fix \(r\), and a state in the open set
\[
\Omega_n=\{(f,g,A,B,z)\in\mathbb C^{4n+1}: f_j\ne0
\text{ for every }j\}.
\]
All coefficients are finite. The RHS of (P70.9), denoted \(\mathcal F\),
is holomorphic on \(\Omega_n\). Its complex differential is therefore the
ordinary real Jacobian action under the existing real/imaginary embedding.
No Wirtinger derivative through a conjugated variable is present.

For a direction \(v=(v_f,v_g,v_A,v_B,v_z)\), the frozen Jacobian
\(J=D_y\mathcal F(\tau,y)\) acts by

\[
\begin{aligned}
(Jv)_{f_j}&=-v_{g_j},&
(Jv)_{g_j}&=Q_jv_{f_j},\\
(Jv)_{A_j}&=c_{aj}(f_av_{f_j}+f_jv_{f_a}),&
(Jv)_{B_j}&=c_{bj}(f_bv_{f_j}+f_jv_{f_b}),\\
(Jv)_z&=\sum_j\left[
 \frac{B_jv_{A_j}+A_jv_{B_j}}{f_j^2}
 -\frac{2A_jB_jv_{f_j}}{f_j^3}\right].
\end{aligned}
\tag{P70.10}
\]

In particular, \(j=a\) in the \(A\) row gives
\(2c_{aa}f_av_{f_a}\); \(j=b\) in the \(B\) row gives
\(2c_{bb}f_bv_{f_b}\). Both terms are required even though the external
index is fixed. The \(z\) row contains a negative factor two from
\(D(f_j^{-2})\), and no term proportional to \(v_z\).

For repeated actions, the implementation stores

\[
\alpha_j=\frac{B_j}{f_j^2},\qquad
\beta_j=\frac{A_j}{f_j^2},\qquad
\zeta_j=-\frac{2A_jB_j}{f_j^3}.
\tag{P70.11}
\]

The stored evaluation uses \((B_j/f_j)/f_j\),
\((A_j/f_j)/f_j\), and \(-2(A_j/f_j)(B_j/f_j)/f_j\).
This is the same rational map as (P70.11); its floating-point association
differs from the original division-based JVP. The independent numerical
check therefore evaluates the residual with the unchanged PHYS69 JVP as
well as with the frozen action. Source:
[block.rs](../../../native/phys70_optimized/src/block.rs),
FrozenJacobian preparation and action.

## 3. Constructive inverse of the full shifted Jacobian

**Theorem P70-A.** For a state in \(\Omega_n\), fixed coefficients, and a real
shift \(s\) such that \(\Delta_j=1+s^2Q_j\ne0\) for every \(j\), and every
right-hand side \(\mathbf b\in\mathbb C^{4n+1}\), the unique solution of
\[
(I-sJ)x=\mathbf b
\tag{P70.12}
\]
is obtained by the following three passes:

\[
\boxed{
x_{f_j}=\frac{b_{f_j}-s b_{g_j}}{\Delta_j},\qquad
x_{g_j}=b_{g_j}+sQ_jx_{f_j}.}
\tag{P70.13}
\]

\[
\boxed{
\begin{aligned}
x_{A_j}&=b_{A_j}
 +s c_{aj}(f_ax_{f_j}+f_jx_{f_a}),\\
x_{B_j}&=b_{B_j}
 +s c_{bj}(f_bx_{f_j}+f_jx_{f_b}).
\end{aligned}}
\tag{P70.14}
\]

\[
\boxed{x_z=b_z+s\sum_j
  (\alpha_jx_{A_j}+\beta_jx_{B_j}+\zeta_jx_{f_j}).}
\tag{P70.15}
\]

**Proof.** The first two equations of (P70.12) at channel \(j\) are
\[
\begin{pmatrix}1&s\\-sQ_j&1\end{pmatrix}
\binom{x_{f_j}}{x_{g_j}}=
\binom{b_{f_j}}{b_{g_j}}.
\]
Their determinant is \(\Delta_j\). Solving the second equation for \(x_g\)
and substituting in the first gives (P70.13). Once all \(x_{f_j}\) are
known, both shared values \(x_{f_a},x_{f_b}\) are known. The \(A/B\) diagonal
blocks in \(I-sJ\) are identities, so their equations give (P70.14) directly.
The remaining \(z\) diagonal entry is one, and its equation gives (P70.15).
Substitution into each row recovers the corresponding \(b\), including
arbitrary \(b_z\) and nonzero complex \(A,B\).

Equivalently, in block order \(((f,g),(A,B),z)\), the matrix is lower
triangular by blocks, with independent \(2\times2\) oscillator diagonal
blocks followed by identities. Thus
\[
\det_{\mathbb C}(I-sJ)=\prod_j\Delta_j,\qquad
\det_{\mathbb R}(I-sJ_{\mathbb R})=\prod_j\Delta_j^2.
\]
The diagonal assumptions give uniqueness. This proves the result for any
finite \(n\) and any valid external indices; it does not depend on an
initial \(A=B=0\) state or on a small screen approximation. \(\square\)

The implementation uses this inverse for the entire shifted system.
It discards no shared derivative, coupling row, or \(z\) term. Its
arithmetic count is linear in \(n\); Section 7 specifies the storage and
the angular work that remains.

## 4. Exact oscillator denominator bound on every \(r\ge27\)

**Lemma P70-B.** For every integer \(0\le j\le64\) and all \(r\ge27\),
\[
-\frac{374879}{72900}\le Q_j(r)\le\frac{1523}{2700}.
\tag{P70.16}
\]

**Proof.** The upper bound follows from
\(Q_j\le49/100+2/r\le49/100+2/27=1523/2700\).
For the lower bound, \(j(j+1)\le64\cdot65=4160\), hence
\[
Q_j(r)\ge\frac{49}{100}+2u-4160u^2,\qquad u=1/r.
\]
The right-hand side is concave on the closed interval
\(0\le u\le1/27\). A concave function on an interval is no smaller than
the minimum of its endpoint values. Those values are
\[
\frac{49}{100},\qquad
\frac{49}{100}+\frac2{27}-\frac{4160}{27^2}
 =-\frac{374879}{72900}.
\]
The endpoint \(u=0\) is the harmless \(r\to\infty\) limit, so the bound
holds on the entire stated radial half-line. \(\square\)

The pinned RODAS5P coefficient has
\[
\gamma=0.21193756319429014<\frac{53}{250}.
\]
For \(0\le h\le1/2\), \(s=h\gamma\) obeys \(s^2\le(53/500)^2\).
Combining this with (P70.16) gives
\[
\begin{aligned}
\Delta_j
&\ge1-\left(\frac{53}{500}\right)^2
          \frac{374879}{72900}\\
&=\frac{18225000000-2809\cdot374879}{18225000000}
 =\frac{17171964889}{18225000000}>0.94222029569,
\end{aligned}
\]
which proves (P70.1). This extends the finite-collar statement in
[INDEPENDENT_BLOCK_ANALYSIS.md](INDEPENDENT_BLOCK_ANALYSIS.md) to all
\(r\ge27\) without changing the driver domain.

The tableau is pinned to VigilODE commit
a21d573980f66fe02891bd216153443b5352f921. Its coefficient snapshot SHA256 is
211255f6125b648c6955833c3da537d9c031ec78168b2918563c29fa88c8bce6;
the actual source read is recorded in [API_REUSE.json](API_REUSE.json).

The lemma controls oscillator denominators. The full inverse also contains
the triangular coefficients (P70.11); its operator norm depends on the
frozen state, in particular on \(1/f_j\). The implementation accordingly
checks the state domain, finite coefficients, and finite positive computed
denominators. A larger allowed step, a different energy, or an angular
range above 64 changes the assumptions of this particular lower bound.

## 5. Nonautonomous raw-U RODAS5P contract

### 5.1 Explicit time partial and the eight stage equations

The potential changes explicitly with \(\tau\), even at a fixed state.
Differentiating \(d\) and (P70.3) gives
\[
\partial_r V=
-2e^{-2d}\left(2+\frac2d+\frac1{d^2}\right)
 \frac{r-R_0\mu}{d},\qquad
\partial_\tau Q_j=\frac2{r^2}-\frac{2j(j+1)}{r^3}.
\tag{P70.17}
\]
The angular nodes are fixed, so their quadrature differentiates term by
term. At fixed \(y\),
\[
\partial_\tau\mathcal F=
\left(
0,\;(\partial_\tau Q_j)f_j,\;
-S(\partial_r V_{aj}^{[N_q]})f_af_j,\;
-S(\partial_r V_{bj}^{[N_q]})f_bf_j,\;0
\right).
\tag{P70.18}
\]
In particular the minus sign in the angular rows comes from
\(\partial_\tau=-\partial_r\). The last row has zero explicit partial:
its dependence on \(f,A,B\) belongs to the Jacobian, not (P70.18).

Let \(t\) denote the base value of \(\tau\), and \(J_0=D_y\mathcal F(t,y)\).
The pinned tableau provides eight stages, lower-triangular \(a_{ij}\) and
\(C_{ij}\), abscissae \(c_i\), output weights \(b_i^{\rm code}\), and
time-partial weights \(\gamma_i^{\rm rows}\). In its actual raw-\(U\)
coordinates, \(i=0,\ldots,7\),
\[
Y_i=y+\sum_{j<i}a_{ij}U_j,
\]
\[
\boxed{
(I-h\gamma J_0)U_i
 =h\gamma\,\mathcal F(t+c_i h,Y_i)
  +\gamma\sum_{j<i}C_{ij}U_j
  +h^2\gamma\,\gamma_i^{\rm rows}\,
        \partial_\tau\mathcal F(t,y).}
\tag{P70.19}
\]
Equations (P70.13)–(P70.15) solve precisely this shifted equation with
\(s=h\gamma\). All eight stages use the same frozen \(J_0\); their changing
stage states affect the RHS. The constructor checks \(0\le c_i\le1\) and
the required lower-triangular coefficients. Therefore a capped step within
\(0\le t\le38\) keeps its stage radii in the same physical collar.

The candidate and embedded error are
\[
y_{\rm new}=y+\sum_{i=0}^{7}b_i^{\rm code}U_i,\qquad e=U_7,
\]
\[
\|e\|_{\rm WRMS}=
\left[\frac1{d_{\rm R}}\sum_{k=0}^{d_{\rm R}-1}
 \left(\frac{e_k}
 {\mathrm{atol}+\mathrm{rtol}\max(|y_k|,|y_{{\rm new},k}|)}
 \right)^2\right]^{1/2}.
\tag{P70.20}
\]
The real-component scaling, accumulation order, stage count, tableau, and
PI update are reused. Public finish_step takes the other \(K\)-coordinate
stage representation and its corresponding weights. The HH driver therefore
combines its raw \(U_i\) using (P70.20), as the original matrix-free path does.
This coordinate distinction and the exact public API boundary are recorded
in [API_REUSE.json](API_REUSE.json).

The public coefficient getter and PI function are called directly from
[integrate.rs](../../../native/phys70_optimized/src/integrate.rs).
The upstream public matrix-free workspace supplies the original one-step
comparator. Its internal linear solve is private and has no arbitrary
shifted-solve injection hook, so the new endpoint driver is an HH-specific
implementation of these stage equations.

### 5.2 Reuse, failed refreshes, and the represented clock

The derivative data \((\mathcal F(t,y),\partial_\tau\mathcal F(t,y),J_0)\)
depend on the base time, state, and immutable kernel configuration. They
do not depend on the proposed \(h\). An \(h\)-only retry at the same base
can therefore reuse them exactly as functions while recomputing the shift
and all stage equations.

The workspace's reuse predicate requires identical time bits, every state
component's bits, and the constructed kernel key
\((n,N_q,\mathrm{backend})\); a fresh flag overrides reuse. It invalidates
the old base before any fallible RHS/time-partial/Jacobian refresh and marks
the new base valid only after all three succeed. The public kernel freeze
entry also invalidates its target Jacobian before checking the new input.
This closes the independently found stale-operator path R70-F1. The
radius-only angular cache is separate: its key is the exact radius bits,
and successful complete row evaluation is required before its key is set.

A stage attempt produces a candidate. Accepted state and time are committed
only when the embedded norm is finite and at most one. A failed stage does
not commit a partial candidate; failure during base refresh leaves the base
cache invalid. A failure later in a stage can reuse the unchanged valid
base on a shorter trial, because the next attempt overwrites stages in their
dependency order.

The endpoint-only clock constructs a representable end, uses the actual
step \(h=\mathrm{end}-t\), and verifies
\[
0<h\le h_{\max}\le1/2,\qquad
t+h=\mathrm{end}\le38.
\]
If a rejected proposal rounds to an interval no shorter than the previous
rejected interval, the next lower representable endpoint is used. The four
saved clock tests cover strict caps, adjacent floating-point times, this
rejection case, and a final two-ULP landing. The original public PI updater
receives the requested/trial step and accepted/rejected outcome.

Completion is tied to the represented endpoint \(t=38\). The executable
also requires two endpoint states with the fixed dimension and finite
components; partial/error outcomes remain incomplete and return a failing
process status. These contracts establish what the driver reports. A
finite local error estimate remains a local estimator.

## 6. Ordered SIMD without changing a channel's node sum

For each node \(q\), precompute the same rounded products
\[
P^{a}_{qj}=\operatorname{fl}(p_a(\mu_q)p_j(\mu_q)),\qquad
P^{b}_{qj}=\operatorname{fl}(p_b(\mu_q)p_j(\mu_q)).
\]
Let \(v_q(r)\) be the original scalar evaluation of \(V(r,\mu_q)w_q\).
Each original angular row has the ordered floating-point recurrence
\[
R_j^{(0)}=+0,\qquad
R_j^{(q+1)}
 =\operatorname{fl}\!\left(
 R_j^{(q)}+\operatorname{fl}(P_{qj}^{a}v_q)\right),
\quad q=0,\ldots,N_q-1.
\tag{P70.21}
\]
The derivative row has exactly the same recurrence with the original
scalar value \((\partial_rV)w_q\); the \(b\) rows use \(P^b\).

Group independent \(j\)'s into four lanes. At a given node, lane
\(\ell\) in block \(b\) represents \(j=4b+\ell\) and performs (P70.21).
No lane reads another lane's accumulator. By induction on \(q\), if scalar
and lane multiplication/addition have the same binary64 semantics and
initial data, each retained lane equals the corresponding scalar
accumulator after every node. Precomputation evaluates the original first
product once; it keeps the second multiplication by \(v_q\) and the node
sum order.

The implementation uses wide 1.7.1 lane additions and multiplications, with
the original scalar square root, exponential, and division evaluations.
It introduces neither a horizontal reduction nor mul_add. The final block
is zero-padded to four lanes; only actual channels are copied to physical
rows. The RHS then performs the original sequential \(j\)-sum for
\(\dot z\). No floating-point reduction is parallelized.

This is an operation-level preservation result under stated arithmetic
semantics. The actual compiled target is covered by the saved bitwise
checks in Section 9. Other compiler flags, floating-point environments,
transcendental implementations, and CPU targets require their own execution
evidence before a bitwise claim is transferred. The exact polynomial and
sum identities themselves are independent of the SIMD package.

Official release/API facts and their retrieved provenance are retained in
[LITERATURE_AND_PACKAGES.md](../reuse/LITERATURE_AND_PACKAGES.md) and
[SOURCES.json](../reuse/SOURCES.json). The applied APIs are
[wide 1.7.1 f64x4](https://docs.rs/wide/1.7.1/wide/struct.f64x4.html);
the manifest is the
[published release](https://docs.rs/crate/wide/1.7.1/source/Cargo.toml).
Their version pin and Cargo.lock identify the reused implementation.

## 7. Operation count and retained storage

The frozen preparation traverses \(n\) channels once and stores \(f_j,Q_j\),
\(c_{aj},c_{bj},\alpha_j,\beta_j,\zeta_j\). A shifted solve has an oscillator
pass, a Born-row pass accumulating the \(z\) row, and the full residual
action. Each uses a fixed number of scalar real/complex operations per
channel. Thus preparation, each full shifted solve, and its residual cost
\(O(n)\) arithmetic and require \(O(n)\) working storage.

For the actual vectors in the new implementation:

| Retained arrays | Logical payload size |
|---|---:|
| Frozen \(f,\alpha,\beta,\zeta\), complex binary64 | \(64n\) bytes |
| Frozen \(Q,c_a,c_b\), binary64 | \(24n\) bytes |
| Eight raw stage vectors | \(8d_{\rm R}\) binary64 values |
| Base RHS, explicit partial, stage state, stage RHS, candidate, residual scratch, cached state | \(7d_{\rm R}\) binary64 values |
| Frozen plus stage/base workspace | \(120d_{\rm R}+88n=1048n+240\) bytes |

The last formula gives 30,632 bytes for \(L=28\) and 68,360 for \(L=64\),
using the displayed logical lengths. The actual capacity-reporting method
counts allocated vector capacities. Static tableau storage, vector headers,
result copies, allocator metadata, and total process RSS are separate.

For comparison, the pinned old GMRES workspace prepares both \(p+1\)
basis vectors and \(p\) direction vectors of dimension \(d_{\rm R}\), plus
an \((p+1)\times p\) Hessenberg array. These alone contribute
\[
8\{(2p+1)d_{\rm R}+p(p+1)\}\ \text{bytes},
\]
before its common vectors, correction/action buffers, least-squares
workspace, and the integration driver's own state. The actual definitions
are CommonWorkspace, ArnoldiWorkspace, and GmresWorkspace in the pinned
rodas5p-krylov source. A completed \(p\)-column Arnoldi cycle has \(p\)
operator actions and \(O(d_{\rm R}p^2)\) orthogonalization work; its small
least-squares work is additional.

The existing HH comparison uses restart \(p=40\). If \(p\) is held fixed,
both retained Krylov storage and the new storage are linear in \(L\).
The useful change is elimination of the \(p\)-dependent buffers, repeated
Krylov actions, and orthogonalization through the exact structure. It is
not an assertion that the old fixed-restart path had quadratic storage
in \(L\).

Angular work remains \(O(N_qn)\). In the SIMD path it is implemented with
\(O(N_q\lceil n/4\rceil)\) lane operations plus \(O(N_q)\) scalar
potential/derivative evaluations at a new radius. If \(N_q\) scales with
\(L\), the full angular callback retains that corresponding quadratic
scaling. The \(O(L)\) theorem concerns the shifted linear action.

There is a deliberate storage/time tradeoff in caching two selected
basis-product tables. With \(b_4=\lceil n/4\rceil\), their logical retained
kernel payload is
\[
16N_q+64N_qb_4+256b_4\ \text{bytes},
\]
counting nodes/weights, both product tables, four padded scalar rows, and
four lane accumulator rows. These product tables can exceed the old single
basis table's coefficient storage. They are reported separately from the
driver reduction. All per-attempt arrays are allocated at construction;
the successful stage/linear-action source path contains no heap growth.
Measured timings, allocator traffic, and RSS require the corresponding
execution records and are not inferred from this count.

## 8. Independent requests and bounded parallel semantics

The batch path in [main.rs](../../../native/phys70_optimized/src/main.rs)
creates an explicit Rayon pool and maps over an indexed request list.
Each request constructs its own kernel, frozen operator, integration state,
and controller. The immutable request/source/seed data can be read by
multiple jobs; evolving numerical state is owned by one job.

Because a job has no dependency on another job's intermediate state, changing
their scheduling changes neither that job's sequence of arithmetic
instructions nor its internal reduction order under a fixed runtime
environment. Indexed collection preserves the request order in the returned
array. The batch records the list hash and per-request identities and
requires every result to be complete; any failed or partial result keeps
the batch incomplete. Sequential radial carries within each job remain
sequential.

This is the applicable independence argument. Actual equality across worker
counts and actual throughput are execution observations. The exact
[Rayon 1.12.0 pool API](https://docs.rs/rayon/1.12.0/rayon/struct.ThreadPoolBuilder.html)
and
[indexed iterator API](https://docs.rs/rayon/1.12.0/rayon/iter/trait.IndexedParallelIterator.html)
were read during the saved reuse study; the release and license provenance
are in its source receipt.

## 9. Independent symbolic and binary64 evidence

### 9.1 Actual saved Wolfram residual

[BLOCK_INVERSE_WOLFRAM.wl](BLOCK_INVERSE_WOLFRAM.wl) defines three modes,
external indices 1 and 2 in one-based indexing, and all 13 complex state
variables. It constructs the entire Jacobian by symbolic differentiation
and substitutes (P70.13)–(P70.15) into the full shifted equation. The actual
wolfram_wolframlanguageevaluator output is retained in
[WOLFRAM_RESULT.json](WOLFRAM_RESULT.json):

- complex dimension: 13;
- exact rational-function residual: thirteen zeros;
- all_zero: true;
- new integrations: zero;
- proof scope: exact rational-function algebra.

This finite symbolic identity checks the shared-channel and final-row
algebra by an independent differentiation/substitution route. The proof
for arbitrary \(n\) is the block elimination in Section 3.

The same saved response records the coarser lower estimate
\(-380279/72900\), which drops the positive \(2/r\) term from \(Q_j\).
It is preserved with that meaning. The sharper global lower estimate
\(-374879/72900\) and (P70.1) are proved explicitly in Section 4; they are
not attributed to a Wolfram calculation of the sharper value.

### 9.2 Actual release tests and the two corrected findings

The root-produced [RUST_TESTS_01.log](../verification/RUST_TESTS_01.log)
records **13/13 PASS**: four represented-clock tests and nine contract
tests. The independent reviewer read this log and
[the assertions](../../../native/phys70_optimized/tests/contract.rs);
no test rerun was performed while writing this note.

The meaningful test scopes include:

| Observed check | Actual checked domain |
|---|---|
| Original/scalar/SIMD RHS and explicit partial, identical output bits | \(L=21,28,36,64\); \(N_q=96\) for the first three, 128 for \(L=64\); \(\tau=0,12.125,37.625,38\) |
| Frozen action, inverse action, and full residual via unchanged original JVP | \(L=21,28,64\); \(\tau=0,37.75\); shifts \(s=0,0.01,0.1\); nonzero complex \(A,B\) |
| All eight raw stages evaluated against the original nonautonomous RHS/JVP/partial | \(L=28,N_q=96,\tau=37.25,h=0.002\), plus the original public one-step candidate comparison |
| Shared external derivative | Both product-rule terms in the \(j=a\) row |
| Cache and failure paths | State/time/configuration changes, failed public freeze, recovery after failed refresh |
| Shape, step, and endpoint contracts | Fixed dimension, forbidden shifts/steps, four floating-point clock boundary cases |
| Residual-normalizer overflow | Explicit rejection when a finite-input norm sum overflows |

Each successful structured solve computes the real-component scaled residual
\[
\rho_{\rm obs}=
\frac{\max_k|x_k-s(Jx)_k-b_k|}
 {\max_k\{|x_k|+|s||(Jx)_k|+|b_k|\}},
\tag{P70.22}
\]
with zero returned for the all-zero denominator after finite checks.
It checks both numerator and denominator for finiteness before division
and accepts only \(\rho_{\rm obs}\le512\epsilon_{64}\).
The independent review found that the unguarded denominator could overflow
to infinity even when individual data were finite, spuriously producing
a zero ratio. That observation, R70-F2, led to the present finite guard
and the targeted passing test. R70-F1 is the failed-public-freeze
invalidation corrected in Section 5.2.

The complete review, methods, exact source hashes, and two closed findings
are in
[INDEPENDENT_REVIEW.json](../verification/INDEPENDENT_REVIEW.json) and
[REVIEW_KO.md](../verification/REVIEW_KO.md), status
PASS_SCOPED_AFTER_TWO_TARGETED_FIXES, with no remaining blocking finding
in its reviewed scope. Its one tiny scalar overflow counterexample was a
failure-path diagnostic, not a physical integration.

The recorded bits and residuals are observations of the compiled binary64
implementation. The different linear-solve arithmetic can change adaptive
trajectories even though (P70.19) is the same method in exact arithmetic.
A cancelling embedded stage is judged with the original state-error
weights in the performance comparison; its relative error divided by that
tiny stage's own magnitude is retained as diagnostic telemetry. The
performance experiment and certificate comparisons are separate root
execution receipts.

## 10. Evidence classes and inherited scientific result

| Result | Mathematical or evidential status | Supporting location |
|---|---|---|
| Full shared-channel shifted inverse | Exact algebra on \(\Omega_n\), every allowed nonzero shift denominator | Sections 2–3; saved 13-variable Wolfram residual |
| Uniform denominator margin, every \(r\ge27,\ j\le64\) | Exact rational inequality for the stated physical coefficient and step range | Section 4 |
| Linear cost of shifted action | Fixed-pass operation and logical-storage count | Section 7; block/workspace source |
| Ordered node reduction under lane arithmetic | Inductive operation-level correspondence | Section 6 |
| RHS/time-partial bit equality and original-JVP residuals | Actual binary64 observations in the tabulated tested domain | 13-test log and independent review |
| Finite local WRMS and (P70.22) | Runtime diagnostics of an attempted step | integrate.rs and block.rs |
| All-angular/all-radial physical \(D_2\), external \((21,20),m=0\) | Inherited PHYS69 rigorous enclosure | Certificate identified below |
| Wall time, worker scaling, retained capacities, endpoint errors of new executions | Separate actual performance/execution receipts | Root-owned PHYS70 results/report |
| Uniform error for the complete new numerical trajectory | Separate open numerical-certification obligation | Section 11 |

The preserved
[PHYS69 certificate](../../hh_phys69_20261019/all_angular/CERTIFICATE.json)
has SHA256
965dc9e3d4a1b40fd7e379629f13480c5a7f30b382aa5b240fd7663b56ae9e29.
It certifies the actual all-angular/all-radial \(D_2\) entry
\[
(D_2)^0_{21,20}
 =(7.01774363281637372857673
    +3.20016322230539545153550\,i)\,10^{-48}\ a_0^{-1},
\]
with absolute error about that displayed midpoint at most
\(1.279825889920\times10^{-64}\ a_0^{-1}\), an upward display of its exact
saved bound. That certificate combines finite numerical enclosures with
the radial and excluded-angular estimates under the original conventions.
It is reused; none of its completed integrations were rerun for this note.

Comparison of a new saved binary64 value with the appropriate inherited
enclosure can bound that value's error when the compared quantities and
normalizations match. The callback equivalence and observed linear residual
alone do not supply the Coulomb, angular quadrature, integration, and
roundoff enclosures needed for an independent uniform numerical certificate.
The source-driven response is a different quantity from this \(D_2\) entry.

## 11. Scoped research review, contribution, and remaining obligations

The contribution is constructive: identify and implement the exact HH
shifted inverse, prove its usable denominator margin, retain the
nonautonomous raw-stage contract, and expose ordered SIMD and independent
request execution. No new impossibility or exclusion theorem is proposed.
The physmath-research-loop NG1–NG7 review is therefore closed for the
adopted optimization scope as follows; the status does not assert the
adoption of a strong no-go.

| ID | Closed scoped review and actual evidence |
|---|---|
| NG1: precise object and quantification | \(\Omega_n\), finite \(L\), fixed physical model, original \(a,b\), and all shift/radius conditions are stated in Sections 1–4. The numerical driver has the narrower fixed collar and endpoint contract. |
| NG2: completed proof | Full block elimination and uniqueness are proved in Section 3; the all-radius rational denominator estimate is proved in Section 4. Coefficient reuse is tied to the actual pin. |
| NG3: content and nonvacuity | The inverse includes both shared external derivatives and the nonlinear final row at nonzero \(A,B\); arbitrary RHS directions are handled. The actual contract tests exercise these terms. The contribution removes a solver operation rather than merely renaming the ODE. |
| NG4: mechanism | The constructive mechanism is block triangular dependence with nonsingular oscillator blocks, followed by identities. No obstructing conservation law or impossibility mechanism is asserted, so a strong-no-go obstruction requirement is outside this claim. |
| NG5: concrete consequence | The construction replaces iterative full-system Krylov stage solves with a direct \(O(L)\) action while preserving the original nonautonomous stage equations. Ordered angular evaluation and owned independent jobs provide distinct optimization paths; measured gains remain tied to execution evidence. |
| NG6: primary comparison and contribution scope | The saved 2026-10-20 study used Exa, SciSpace, official package documentation, the original HH source, and pinned/current VigilODE sources. General nonautonomous ROW and work-precision methods are reused; this note derives the HH-specific block action and range bound. It claims no historical priority or general new solver theorem. |
| NG7: independent scrutiny | A separate symbolic full-Jacobian residual, the independent block derivation, the implementation reviewer with zero implementation edits, the two concrete corrected findings, and the saved original-callback tests cover the actual claim. No global norm sharpness or necessity of the 0.5 cap is claimed. |

Overall scope-review status:
**CLOSED_SCOPED_REVIEW / NO_STRONG_NO_GO_CLAIM**.

The primary ROW reference already read is
[Steinebach (2023), DOI 10.1007/s10543-023-00967-x](https://link.springer.com/article/10.1007/s10543-023-00967-x),
equations (1.2)–(1.3) for the nonautonomous shifted stage and Section 4 for
work-precision comparisons. The HH matrix elimination here follows directly
from (P70.9). External benchmark numbers are not used as HH speed evidence.
The saved reuse files preserve search scope, primary URLs, retrieved
responses, package versions, and license facts.

PHYS63 qualitative all-angular real-axis LAP/Poisson/DtN existence remains
**ESTABLISHED_REUSED**, and the PHYS69 \(D_2\) enclosure remains established.
The following distinct scientific obligations retain their own open nodes:
the all-angular \(D_3\)/higher-order remainder; uniform numerical integration,
Coulomb/angular quadrature and roundoff certification of the new binary64
trajectory; original source-driven \(\xi\); its origin/incoming-adjoint
construction; \(\sigma(E)\); and Maxwellian \(k_{\rm HH}(T)\).
The auxiliary incoming adjoint identifying the inherited \(D_2\) coefficient
does not close the original-source adjoint obligation.

This note completes the scoped derivation and its implementation/evidence
mapping. Publication, backup, new NCP execution, and the project DAG are
reported by their own actual receipts. **HH_R10 remains OFF.**
