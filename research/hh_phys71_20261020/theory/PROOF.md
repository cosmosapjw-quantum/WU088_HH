# PHYS71 — certified third Born computation from two inherited rows

The new analytic result is the all-angular third coefficient identity and
explicit angular convolution bound in [ANGULAR_D3.md](ANGULAR_D3.md).
This document derives the finite computation that uses it. The numerical
coefficient, actual execution status, and publication/backup receipts are
recorded separately. The original atomic Hamiltonian, B=27, k=7/10,
E=49/200 Hartree, eta_C=-10/7, H+=G+iF_C and Z=+u'u^-1 are unchanged.
The source variables eta=Fy and xi=Fy-phi keep their original meanings.

## 1. Exact quantity and reuse

Write A_lambda=2h_C-k²-lambda V with V=2(1+1/d)exp(-2d) and
d=|x-0.7 zhat|. PHYS63 gives the actual all-angular outgoing boundary map;
PHYS69 identifies its analytic coefficients near lambda=0. We compute
D3=Z'''(0)/6 for the single entry (21,20),m=0. The local expansion and the
positive Dirichlet Green derivative at B give

\[
D_{3,ab}=\sum_{j,k}\int_B^\infty U_{a,j}(r)V_{jk}(r)U_{b,k}(r)\,dr,
\qquad U_{a,j}(r)=f_j(r)P_{a,j}(r),
\]
\[
P_{a,j}'(r)=q_{aj}(r)/f_j(r)^2,\quad P_{a,j}(B)=0,
\qquad q_{aj}(r)=\int_r^\infty f_a(s)f_j(s)V_{aj}(s)\,ds.
\]

There is no complex conjugation in this formula. The Taylor factorial is
already in the definition D3=Z'''(0)/6. Differentiating U=fP directly,
using f''+Q_j f=0 and q'=-f_a f_j V_aj, yields
-U''-Q_j U=f_a V_aj. This fixes both the sign and the homogeneous boundary
condition. The transpose symmetry gives D3_ab=D3_ba.

For the finite computation, replace infinity in q by T=65 and retain
j,k=0,...,36. We reuse the complete PHYS68 low-band and PHYS69 high-band
certificates. Their archives contain 76+76 immutable panel records with
73 distinct q pairs on every common panel. They contain q endpoint and
center balls, analytic majorants, and a coefficient reconstruction rule;
they do not contain a full D1/D2 matrix or all Taylor arrays. Only a=20,21
are required. There are 74 directed P carries because the shared pair
q_20,21 has different denominators f_20² and f_21² in the two responses.

The new reader verifies the original NPZ, both archive hashes, both
request/certificate hashes, all saved payloads, engine bytes, the terminal
zero data, and exact predecessor rectangle containment. Reconstructing
Coulomb/angular Taylor coefficients under current enclosed arithmetic is
new downstream evaluation. No previous Volterra or D2 integration is run.
Producer runtime and current reader/evaluator runtime remain distinct
provenance fields even when their versions coincide.

## 2. A forward primitive with a certified analytic remainder

Each saved radial panel is [c-h,c+h], h=1/4. The inherited q function is
analytic on the disk of radius rho=1/2 around c. The underlying Coulomb
disks have majorant radius 2. PHYS68 supplies the analytic Coulomb and
angular formulas and the zero-free disk test. All new coefficient
operations use complex Arb balls at 384 bits; exact angular constants
are formed at 1024 bits. The working degree is N=80.

Let K=f_a f_j V_aj. The new q coefficients are

\[
q_0\in Q_0^{\rm saved},\qquad q_{n+1}=-K_n/(n+1).
\]

The full saved q-center ball is retained. It includes the old upstream
carry and integration uncertainty. Computing a new lower-degree Taylor
polynomial does not erase that uncertainty. The high band originally used
degree96; its saved analytic function and disk majorant are still valid
when only the first81 coefficients are used for the new operation.

For every j, require a strictly positive lower bound ell_j on |f_j(z)|
for |z-c|<=rho. An unresolved gate stops the new panel. Define

\[
S_{a,j}(z)=q_{aj}(z)/f_j(z)^2,
\quad M_{S,a,j}=M_{q,a,j}/\ell_j^2,
\quad E_S=M_S\frac{(h/\rho)^{N+1}}{1-h/\rho}.
\]

Series inversion computes the first N+1 coefficients of S. The Cauchy
bound E_S controls the missing coefficients for every real |x|<=h.
From the already enclosed left value P_-, compute

\[
P_0\in P_-+\int_{-h}^0 S_N(x)\,dx+\mathbb D(hE_S),
\qquad
P_+\in P_-+\int_{-h}^{h}S_N(x)\,dx+\mathbb D(2hE_S).
\]

Here D denotes an absolute complex error disk, implemented by an enclosing
Cartesian square. Polynomial integrals use exact rational powers and
division; Arb encloses all coefficient and arithmetic error. The P Taylor
coefficients are P_0 and S_(n-1)/n. Each successor consumes the full
enclosed P_+ of its predecessor.

The closed disk |z-c|<=rho is convex and contains c-h. Integrating S on
the straight segment from c-h to z, of length at most rho+h, gives

\[
M_P=|P_-|+(\rho+h)M_S,\qquad M_U=M_f M_P.
\]

This bounds the actual analytic P and U on the entire disk, including
the carried uncertainty. It does not treat a finite Taylor polynomial
as the exact analytic function. The majorants M_f use the inherited
local Coulomb ODE estimate.

## 3. Angular contraction without numerical angular quadrature

For m=0 the normalized polar basis is
y_j(mu)=sqrt((2j+1)/2) P_j(mu). At each radial Taylor center form the two
ordinary angular polynomials

\[
A(\mu)=\sum_{j=0}^{36}U_{21,j}y_j(\mu),\qquad
B(\mu)=\sum_{j=0}^{36}U_{20,j}y_j(\mu).
\]

Their coefficients are radial power series with ball coefficients. Let
A(mu)B(mu)=sum_n W_n mu^n. Then the exact finite angular contraction is

\[
I(r)=\sum_{n=0}^{72}W_n(r) I_n(r),\qquad
I_n(r)=\int_{-1}^{1}\mu^n V(r,\mu)\,d\mu.
\]

The change d=r+t, t in [-R0,R0], gives

\[
\mu=-t/R_0+(R_0^2-t^2)/(2R_0r),
\]
\[
I_n(r)=\frac{2e^{-2r}}{R_0}
\int_{-R_0}^{R_0}e^{-2t}\mu(t,r)^n[1+(t+1)/r]dt.
\]

The inherited exact exponential-moment recurrence expresses the last
integral as a finite Laurent polynomial in 1/r with exact rational
coefficients multiplying exp(±2R0). Therefore angular integration is
algebraic and complete for every retained mode. The implementation needs
73 moment functions rather than1369 separately generated V_jk functions.
The polar basis contributes a factor1/2 and V=2S contributes a factor2;
the displayed formulas include both. Matrix multiplication and polynomial
products remain complex bilinear.

The moment transformation can have cancellation in a monomial basis.
The first actual pilot exposed severe dependency inflation when all input
ball radii were transformed in that basis. Its successful checkpoint did
not meet the fixed numerical goal and is preserved. The revised evaluator
transforms the exact dyadic midpoints of the response coefficients and
bounds their coefficient uncertainties in the original orthonormal basis.
The projected weighted-convolution proof is in
[ANGULAR_ERROR_STABILITY.md](ANGULAR_ERROR_STABILITY.md). It supplies a
separate nonnegative coefficient-error bound E_c. Moment evaluation and
midpoint-transform roundoff remain enclosed by ball arithmetic. The fixed
degree, precision, physics and goal have not been relaxed. Tests compare
the contraction with independently assembled angular entries, including
high and complex modes, and check projected uncertainty cases.

## 4. Whole-integrand bound and radial integration

For complex r in the same rho disk and real mu, PHYS68 gives a uniform
multiplier bound M_V=2(1+1/a)exp(-2a), a=c-rho-R0>0. Orthonormality and
Cauchy–Schwarz imply |U_a^T V U_b|<=M_V||U_a||_2||U_b||_2. We use the
slightly larger computable bound

\[
M_I=M_V\left(\sum_j M_{U_{a,j}}\right)
          \left(\sum_j M_{U_{b,j}}\right).
\]

Although the product is bilinear, its absolute value obeys this usual
Euclidean inequality. This is a bound on the true analytic integrand.
With the computed midpoint degreeN polynomial I_N and the bound E_c on
its difference from the true retained coefficients, each panel integral lies in

\[
\int_{-h}^{h}I_N(x)dx+
\mathbb D\left(2h\left[E_c+M_I\frac{(h/\rho)^{N+1}}{1-h/\rho}\right]\right).
\]

Adding all76 panel balls at the bound working precision encloses the
finite-L36, finite-T65 coefficient. The L1 sum of the final real and
imaginary radii bounds absolute complex error about the exact stored
dyadic center. This single numerical radius includes Coulomb evaluation,
all new primitives, angular coefficient arithmetic, radial Taylor
remainders, carried inherited uncertainty, and roundoff.

## 5. Compose finite arithmetic and infinite tails

Let z be the exact dyadic midpoint of the completed finite result and
e_num its L1 numerical radius. PR115 applies to every finite L<=64 and
supplies beta3(L64,T65)<=1.48432231489e-79. The new angular theorem supplies
A3(36)<=5.63697247035361181066503e-79. Both are all-radial/full-cutoff
statements with the same coefficient normalization. Thus

\[
|D_{3,\infty}(21,20)-z|
\le e_{\rm num}+\beta_3(64,65)+\mathcal A_3(36).
\]

The shorter summary decimal1.484322e-79 was found to round inward by an independent exact exponential-series audit. The original producer aggregate is retained as rejected analytic evidence; ALL_ANGULAR_CERTIFICATE.json applies the corrected upward endpoint without any repeated physical integration. The two finite-to-infinite steps are added once each. No stored D2
error, native ODE tolerance, or all-order Born remainder is inserted in
this D3 budget. The new explicit D3 goal is1e-78; it leaves approximately
2.8787052147e-79 for e_num after the two analytic tails. The earlier D2
goal1e-62 and its completed certificate remain unchanged. Printing a
rounded decimal center requires adding its exact L1 displacement from z.

## 6. Verification, status and next mathematical obligation

Wolfram checked the differential identity, scalar exponential model and
angular change of variable. The first angular expression used the token
rR instead of r*R; its nonzero output and corrected second call are both
saved. Undefined-symbol messages in the symbolic calls are preserved.
The exact outputs after correcting that input are0 for the angular
identity and1/6 for the radial integral, yielding D3=v³/96.

Independent derivations and code tests are in ../verification/. The
angular module uses only Fraction arithmetic; its initial generalized
b=28 split failure and correction are preserved. A successful test is
implementation evidence; the whole-domain claims depend on the analytic
arguments and inherited premises above.

Primary background used: [DLMF33.2](https://dlmf.nist.gov/33.2) for the
Coulomb convention; [Johansson2017](https://arxiv.org/abs/1611.02831) for
ball arithmetic; [Johansson2018](https://arxiv.org/abs/1802.07942) and
[FLINT calculus documentation](https://flintlib.org/doc/acb_calc.html)
for the distinction between analytic integration remainders and enclosed
arithmetic. We reuse the existing Taylor construction, not a new claim
that a requested floating tolerance is a certified error. The explicit
HH D3 identity, convolution constants and reuse algorithm are derived
here; no literature novelty or strong no-go theorem is asserted.

The all-order lambda=1 remainder needs a further summable operator
estimate; polynomial C_j growth cannot be replaced by Gamma64 at infinite
j. Original source-driven xi, origin and original incoming adjoint,
sigma(E), and Maxwellian k_HH(T) remain separate obligations. HH_R10=OFF.
