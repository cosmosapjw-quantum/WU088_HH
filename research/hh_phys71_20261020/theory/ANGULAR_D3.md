# PHYS71: the all-angular third Born coefficient and its explicit angular tail

Date: 2026-10-20 UTC. This note supplies the new two-intermediate-index
identity and an exact, summable majorant. The actual application is in
`../angles/RESULTS.json`, with timing and code identity in
`../angles/EXECUTION.json`. The finite-block coefficient enclosure, native
diagnostic, publication and backup have separate records.

## 1. Object and inherited premises

Keep atomic coordinates, B=27, k=7/10, E=49/200 Hartree, R0=7/10 and

\[
h=-\Delta/2-1/r-(1+1/d)e^{-2d},\qquad
d^2=r^2+R_0^2-2rR_0\mu,\qquad V=2(1+1/d)e^{-2d}.
\]

The outgoing channel is

\[
H_j(r)=G_j(-10/7,kr)+iF_j^C(-10/7,kr),\qquad f_j(r)=H_j(r)/H_j(B),
\]

and the boundary convention is Z=+u'(B)u(B)^{-1}. The Coulomb parameter
eta_C=-10/7 is distinct from eta=Fy and xi=Fy-phi. Put
A_lambda=2h_C-k^2-lambda V and

\[
Z_\lambda-Z_0=\sum_{n\ge1}\lambda^n D_n,
\qquad D_3=Z'''(0)/6.
\]

PHYS63's actual all-angular real-axis LAP/Poisson/DtN result remains
ESTABLISHED_REUSED. PHYS69, Sections 1–2, identifies the Taylor coefficients
of the actual outgoing boundary map near zero through the weighted resolvent
K=R0+ V; its local inverse exists for sufficiently small |lambda|. No new
numeric radius of this inverse is assumed here.

The following quantitative premises are inherited, with their hypotheses
unchanged:

1. PHYS65/PR114 and PHYS68 give
   |H_j(t)/H_j(r)|<=77 for 0<=j<=28 and all B<=r<=t. In particular the
   external product C_a C_b is bounded by Gamma_ext=77^2=5929 when a,b<=28.
2. PHYS69's all-j theorem gives
   |H_j(t)/H_j(r)|<=s(j+1), s=800/189, for every j>=20 and the same whole
   radial domain. For a single majorant we use
   C_j=77 for j<=28 and C_j=s(j+1) for j>=29.
3. The whole-exterior real multiplier obeys
   |V(r,mu)|<=delta exp[-2(r-B)], delta=3e-23. PHYS67's Bernstein E10
   analyticity bound for S=V/2 is M=1/(4*10^19).
4. PHYS69's exact angular selection argument therefore gives, for a
   normalized fixed-m basis and every allowed pair,

\[
|V_{ij}^m(r)|\le v_{|i-j|}e^{-2(r-B)},\qquad
v_d=\min\{\delta,c\,10^{-d}\},\quad c=40M/9=1/(9\,10^{18}). \tag{1}
\]

For d>=1 the analytic part of (1) is precisely
(4M/9)10^{1-d}; for d=0 the real multiplier bound supplies delta. Since
c*10^-3>delta and c*10^-4<delta, v_d=delta for d=0,1,2,3 and
v_d=c*10^-d for d>=4. Both bounds are multiplier/operator bounds in the
normalized angular basis, so no angular multiplicity is inserted. The
implementation includes all indices starting at zero. For |m|>0 this adds
nonnegative majorant terms below the admissible indices and remains an
upper bound. The numerical target in this unit is a=21,b=20,m=0.

The definitions and signs agree with [DLMF 33.2](https://dlmf.nist.gov/33.2),
[DLMF 33.11](https://dlmf.nist.gov/33.11) and the source-specific matching
already established in `../../hh_phys69_20261019/theory/PROOF.md`. The
analytic polynomial selection estimate is inherited from that proof's
application of [Trefethen, ATAP chapter 8](https://github.com/chebfun/ATAP/blob/development/chap8.m).

## 2. Two first-order response vectors give the third coefficient

The central outgoing Dirichlet Green kernel from PHYS69 is

\[
G_j(r,s)=f_j(r)f_j(s)\int_B^{\min(r,s)}f_j(t)^{-2}\,dt. \tag{2}
\]

Its derivative jump is -1 for A0=-d²/dr²-nu_j, and
partial_r G_j(B,s)=+f_j(s). It is symmetric under r↔s as a complex
bilinear kernel. The Coulomb Wronskian ensures no real-axis zero of f_j.

For external index a define the first-order bulk response

\[
U_{a,j}(r)=\int_B^\infty G_j(r,s)V_{ja}(s)f_a(s)\,ds,
\quad
q_{aj}(t)=\int_t^\infty f_a(s)f_j(s)V_{aj}(s)\,ds. \tag{3}
\]

For fixed j, substitution of (2) and interchange over
B<=t<=min(r,s) give

\[
\boxed{U_{a,j}(r)=f_j(r)\int_B^r\frac{q_{aj}(t)}{f_j(t)^2}\,dt.} \tag{4}
\]

The nonnegative estimates below also justify the absolute interchange.
In particular U_a,j(B)=0; this is a bulk response with a homogeneous
Dirichlet value, not a new boundary value f_j(B).

The resolvent expansion and the boundary identity give

\[
D_3=(P_0^-)^*V R_0^+ V R_0^+V P_0^+.
\]

For the real fixed-m polar basis, conjugation of the incoming Poisson
factor produces the outgoing factor in (2). Transpose symmetry of G_j
and V identifies the a-th left response with U_a. Consequently

\[
\boxed{(D_3)^m_{ab}=\sum_{j,k=|m|}^{\infty}
\int_B^\infty U_{a,j}(r)V_{jk}^m(r)U_{b,k}(r)\,dr.} \tag{5}
\]

This is a complex bilinear product, with no conjugation of either U.
The factor 2 from the Hamiltonian already occurs in V. Formula (5) is
the lambda³ coefficient, so it has no further factor 2, 3 or 6. Its
transpose symmetry follows by j↔k and a↔b. The incoming Coulomb factor
used to identify this coefficient does not resolve the separate original
source-driven incoming-adjoint problem.

For a cutoff at T, replace the upper limit in q by T, use the same (4)
on B<=r<=T, and integrate (5) only to T. The usual finite-L projection
retains j,k<=L. Since the central Green kernel commutes with that
projection, finite-L D3 consists exactly of those retained pairs; there
is no additional implicit response term from the excluded block.

## 3. A whole-radial estimate and the factor 1/96

Set x=r-B. In the double integral giving (4), s>=t and r>=t. The two
ratios of channel j can therefore both be bounded in the permitted
direction, while |f_a(s)|<=C_a. Thus

\[
\begin{split}
|U_{a,j}(r)|
&\le C_a C_j^2 v_{|a-j|}
  \int_B^r\int_t^\infty e^{-2(s-B)}\,ds\,dt\\
&=\frac{C_a C_j^2 v_{|a-j|}}4(1-e^{-2x}).
\end{split} \tag{6}
\]

This estimate retains the squared, degree-dependent C_j. It is not
obtained by assuming a uniform ratio bound as j tends to infinity.
Combining two instances of (6) and (1), the radial integral is exactly

\[
\frac1{16}\int_0^\infty e^{-2x}(1-e^{-2x})^2\,dx
=\frac1{96}. \tag{7}
\]

The same bound holds for the finite-T primitives: their inner positive
majorants are no larger than those used in (6). Define the positive
angular weight

\[
W_{ab}(j,k)=C_j^2C_k^2
v_{|a-j|}v_{|j-k|}v_{|b-k|}.
\]

Then both the all-radial full coefficient and its omitted angular part
obey

\[
|D_{3,ab}^m|\le\frac{\Gamma_{\rm ext}}{96}
 \sum_{j,k\ge0}W_{ab}(j,k), \tag{8}
\]

\[
\boxed{|D_{3,ab}^m-D_{3,ab}^{m,L}|
\le\frac{\Gamma_{\rm ext}}{96}\big[T_{ab}(L)+T_{ba}(L)\big],}
\quad
T_{ab}(L)=\sum_{j>L,k\ge0}W_{ab}(j,k). \tag{9}
\]

The right side of (9) counts the positive j>L,k>L overlap twice.
This is an explicit union bound, and the certificate records that fact.
It also bounds the finite-T angular difference. It does not add a radial
truncation error to a finite-T numerical value; that separate component
must still be supplied when constructing an all-radial enclosure.

As an independent normalization check, take a manufactured one-channel
kernel f=1 and V=d exp(-2x). Direct integration yields
U=d(1-exp(-2x))/4 and D3=d³/96. If d=i, this coefficient is -i/96;
inserting a complex conjugate would change the result. This manufactured
case is a check of (5)–(7), not an execution of the original HH model.

## 4. Exact summation of the infinite angular convolution

The middle v_|j-k| is retained. Dropping it in favor of delta would
discard useful path decay and produce a much less accurate tail.
Put w_j=C_j², y=1/100, and

\[
B_b(j)=\sum_{k\ge0}w_k v_{|j-k|}v_{|b-k|}.
\]

For any fixed j, let N=max(28,j+3,b+3). The finite sum k=0,...,N
contains all nongeometric exceptions. For k>=N+1, both angular factors
are geometric and w_k=s²(k+1)². Therefore

\[
B_b(j)=\sum_{k=0}^{N}w_kv_{|j-k|}v_{|b-k|}
 +s^2c^2 10^{j+b}\sum_{k=N+1}^{\infty}(k+1)^2 y^k. \tag{10}
\]

This is already an exact finite-plus-tail formula, but using it for an
infinite number of j is unnecessary. Let K=max(28,b+3), and suppose
j>=K+4=max(32,b+7). Split the k sum into the four consecutive regions
0...K, K+1...j-4, j-3...j+3, and j+4...infinity. Empty second regions
are allowed. All four sums can be written

\[
\boxed{B_b(j)=10^{-j}P_b(j),} \tag{11}
\]

where the following is a polynomial of degree at most three:

\[
\begin{split}
P_b(j)={}&A_b+c^2 10^b s^2[Q_2(j-3)-Q_2(K+1)]\\
&+\delta c10^b s^2\sum_{d=-3}^{3}(j+d+1)^2 10^{-d}\\
&+c^2 10^{b-8}s^2\left[
\frac{(j+5)^2}{1-y}+\frac{2(j+5)y}{(1-y)^2}
+\frac{y(1+y)}{(1-y)^3}\right],\\
A_b={}&c\sum_{k=0}^{K}w_k10^k v_{|b-k|},\qquad
Q_2(n)=n(n+1)(2n+1)/6.
\end{split} \tag{12}
\]

The fourth term follows by k=j+4+n. Its 10^-8 factor is the product
of the two geometric offsets 10^-4. The third term uses
v_|j-k|=delta for |j-k|<=3. The low sum extends through K rather than
only 28, which is necessary for external b=26,27,28; otherwise some
near-diagonal v factors would incorrectly be treated as geometric.

Choose
J=max(L+1,32,a+4,b+7). For j>=J, w_j=s²(j+1)² and
v_|a-j|=c10^{a-j}. Consequently

\[
\begin{split}
T_{ab}(L)={}&\sum_{j=L+1}^{J-1}w_jv_{|a-j|}B_b(j)\\
&+s^2c10^a\sum_{j=J}^{\infty}(j+1)^2P_b(j)y^j. \tag{13}
\end{split}
\]

The first sum is short; for the actual a=21,b=20,L>=28 it has at most
three rows. The remaining polynomial has degree at most five. Every
geometric moment is evaluated as the exact rational identity

\[
\sum_{n=0}^{\infty}n^d y^n
=\sum_{t=0}^{d}\left\{\!\begin{matrix}d\\t\end{matrix}\!\right\}
\frac{t!y^t}{(1-y)^{t+1}}, \tag{14}
\]

using Stirling numbers of the second kind. Binomial expansion of
(J+n)^d then evaluates the tail in (13). The d=0 case includes n=0.
The implementation performs every sum, comparison and budget decision
with exact Python Fractions. Decimal outputs use upward rounding only
for display. Signed monomial coefficients in P_b do not create a
roundoff or cancellation issue in this exact calculation.

Equations (10)–(14) prove convergence of the infinite positive majorant,
with a tail bounded by a polynomial of degree five times 100^-L.
Tonelli applied to the absolute radial estimates, followed by this
finite bound, justifies the angular/radial interchanges in (5). Together
with the inherited actual-map Taylor identification, this proves (5)
and (9) for the all-angular coefficient, rather than only a formal
finite-dimensional expansion.

## 5. Actual exact application and validation

For (a,b,m)=(21,20,0), the following displayed endpoints round upward:

| L | All-radial excluded-angular D3 bound, a0^-1 |
|---:|---:|
| 28 | 3.45716107716002415432785e-64 |
| 35 | 4.45815477016082342197050e-77 |
| 36 | 5.63697247035361181066503e-79 |
| 40 | 1.21471050862947663398945e-86 |
| 64 | 1.81089325144712534358499e-133 |

The complete coefficient also has the independent zero-centered bound
|D3|<=2.58800673242300254003397e-57 a0^-1 from (8). This is an analytic
bound; it is not a computed center for the original coefficient.
Among L>=28, the angular budget 1e-78 is first met at L36, and 1e-80
is first met at L37. These are new component-budget examples and do
not modify the fixed earlier D2 absolute goal 1e-62.

The five-cutoff exact application took 0.0243 seconds on this session's
Python runtime. It made zero radial integrations, Coulomb evaluations,
and angular quadratures. Ten new tests check the scalar normalization,
geometric-moment translation identity, polynomial-tail difference,
inner-convolution identity, one-sided-tail differences across all
piecewise transitions, transpose symmetry, monotonicity, budget
selection, the full double sum against a finite block, rational
serialization and invalid inputs.

The initial test run exposed two failures for the generalized b=28
boundary case. The low convolution sum had ended at28 although
near-diagonal potential exceptions continue through b+3. Extending it
to K=max(28,b+3) and changing the square-sum subtraction fixed both
identities. The actual target b=20 and its swapped a=21 case were
unaffected. Initial and final logs are preserved as
`../verification/ANGULAR_D3_TESTS_01.log` and `ANGULAR_D3_TESTS_02.log`.
The final run passed 10/10 in 0.261 seconds. These are ten distinct tests;
the runs produced no new HH trajectories.

## 6. Reuse boundary and remaining obligations

The actual stored PHYS68/69 data contain the two external q rows,
q_right/q_center/q_left, local majorants and per-j D2 panel integrals.
They do not contain a full D1 or D2 matrix profile. Their Taylor arrays
are represented by the reconstruction contract
q_0=q_center, q_(n+1)=-K_n/(n+1), K=f_a f_j V_aj. A downstream
application of (4) can reuse those boundary enclosures and reconstruct
coefficients using the same pinned analytic kernels. It must describe
new coefficient evaluation and new U/D3 integration accurately; it
must not claim that all arrays were already serialized, or replay the
old D1/D2 campaign to recover them.

Equations (8)–(14) concern D3 only. They do not produce an all-order
operator norm for R0+V or a nonlinear remainder at lambda=1. Polynomial
C_j growth cannot be replaced by Gamma64 outside its finite block.
The inherited finite-L PR114 high-order Born remainder and PR115
beta3 radial cutoff remain available in their original scope.

The PHYS69 all-angular D2 certificate stays complete. The parent node
`PHYS70_ALL_ANGULAR_D3_AND_HIGHER_REMAINDER` must retain separate child
states for the proved D3 identity/tail, the computed D3 coefficient,
and the still-open all-order remainder. Original source-driven xi,
origin/incoming adjoint, sigma(E) and Maxwellian k_HH(T) remain separate.
HH_R10=OFF. This construction makes no strong no-go claim.
