# Independent review of the centered angular contraction

Status: **PASS for the finite Taylor coefficient error split and its implementation.**
This review does not assert that a new physical panel, the full campaign, or the
fixed absolute goal has passed. The first pilot is immutable evidence of an
insufficient enclosure; it is not relabeled as a successful certificate.

## Why the change is needed

The original fast contraction maps both angular vectors from the orthonormal
Legendre basis into monomials. Applying that map directly to uncertain
coefficient balls can greatly enlarge their radii: the cancellations between
large monomial coefficients do not restore dependencies lost by interval
arithmetic. The new implementation sends exact dyadic midpoint coefficients
through that map and treats their uncertainty in the original angular basis.
It changes neither the physical finite sum nor the fixed numerical goal.

## Precise coefficient statement

Put $t=r-c$, let $N$ be the retained Taylor degree, and write

\[
U_a(t)=\sum_{p\geq0}u_{a,p}t^p,\qquad
U_b(t)=\sum_{q\geq0}u_{b,q}t^q,\qquad
V_L(t)=\sum_{s\geq0}V_s t^s.
\]

The vectors have components indexed by the original orthonormal angular modes.
For $p\leq N$, the already constructed ball coefficient encloses $u_{a,j,p}$.
Its exact dyadic midpoint is $m_{a,j,p}$, and

\[
|u_{a,j,p}-m_{a,j,p}|\leq e_{a,j,p},
\]

where $e$ is the sum of the real and imaginary rectangular radii. Correlation
between different balls is immaterial to this upper bound. Define

\[
A_a=\sum_{j,p\leq N}h^p
 (|\Re m_{a,j,p}|+|\Im m_{a,j,p}|),\qquad
E_a=\sum_{j,p\leq N}h^p e_{a,j,p},
\]

and define $A_b,E_b$ identically. These nonnegative quantities dominate the
weighted sums of Euclidean vector norms for the midpoint and error
coefficients. The implementation rounds their bounds upward.

For the original multiplication operator restricted to the finite orthonormal
angular basis, the physical disk bound gives

\[
\sup_{|t|\leq\rho}\|V_L(t)\|_2\leq M_V.
\]

This follows by restricting the angular multiplication operator; it does not
require entrywise summation over angular indices. Cauchy's coefficient formula
then yields

\[
\|V_s\|_2\leq M_V\rho^{-s},\qquad
B_V:=\sum_{s=0}^N h^s\|V_s\|_2
\leq\frac{M_V}{1-h/\rho},\quad 0<h<\rho.
\]

The bilinear contraction retains its transpose: for complex vectors,
$|x^T V_s y|\leq\|x\|_2\|V_s\|_2\|y\|_2$. Using a norm inequality does
not introduce complex conjugation into the computed coefficient.

Let $T_N$ denote Taylor projection through degree $N$, and let $m_a,m_b$ be
the finite midpoint polynomials. All coefficients of order at most $N$ in the
true integrand depend only on the already enclosed coefficients of $U_a,U_b$
through degree $N$. In the quotient algebra modulo $t^{N+1}$,

\[
T_N(U_a^T V_L U_b-m_a^T V_Lm_b)
=T_N(\delta_a^T V_Lm_b+m_a^T V_L\delta_b+
      \delta_a^T V_L\delta_b).
\]

Here $\delta$ is the polynomial of coefficient differences through degree
$N$. For every retained output coefficient, expand the sums with
$p+q+s\leq N$, apply the norm inequality, and multiply by $h^{p+q+s}$.
All resulting terms are nonnegative. Dropping this degree restriction only
enlarges the bound. Thus the weighted norm of the **projected** difference is
at most

\[
E_{\mathrm{coef}}=
\frac{M_V}{1-h/\rho}
 (E_a A_b+A_a E_b+E_a E_b).
\]

Consequently, its magnitude is at most $E_{\mathrm{coef}}$ throughout the
real panel, and the error of its panel integral is at most
$2hE_{\mathrm{coef}}$. The error-error product is included once; discarding
it would be incorrect even when both midpoint vectors are small.

## Projection is an essential part of the argument

A bound on the untruncated product on the real axis alone is insufficient.
For example, take $N=2$, $\delta_a(t)=\epsilon t^2$, and
$m_b(t)=1-t^2/h^2$. The full product vanishes at both panel endpoints, while
its degree-two projection is $\epsilon t^2$. Their integrals are respectively

\[
\frac{4\epsilon h^3}{15}
\quad\hbox{and}\quad
\frac{2\epsilon h^3}{3}.
\]

The implemented coefficient convolution bound controls the second quantity.
The independent regression includes this example explicitly.

## Separation from analytic truncation and arithmetic error

The existing whole-integrand majorant $M_I$ bounds the actual analytic
$U_a^TV_LU_b$ on the complex disk. Its Taylor tail remains

\[
E_{\mathrm{tail}}=
M_I\frac{(h/\rho)^{N+1}}{1-h/\rho}.
\]

The final panel interval is obtained from the ball integral of the computed
midpoint contraction by adding the disk bound

\[
2h(E_{\mathrm{coef}}+E_{\mathrm{tail}}).
\]

This accounting has three separate sources:

1. The midpoint contraction retains the monomial moments' coefficient balls,
   basis normalization balls, and arithmetic roundoff in its output balls.
2. $E_{\mathrm{coef}}$ covers only the removed response coefficient radii in
   retained Taylor degrees.
3. $E_{\mathrm{tail}}$ covers degrees above $N$ in the actual full integrand.

No separate truncated-$U$ tail is needed in the coefficient split: coefficients
above $N$ cannot affect retained coefficients. Adding such a tail again is
unnecessary and would obscure the accounting. Existing primitive Cauchy
uncertainties already enclosed in the response coefficients are included in
$E_a,E_b$; they must not be removed when constructing the split.

## Source readback and actual verification

The reviewed `centered_angular_contraction` constructs exact dyadic midpoint
complex coefficients, computes upward weighted coordinate-L1 amplitude and
radius bounds, calls the existing contraction on midpoint series, and returns
the coefficient error as a separate upward bound. The physical builder adds
$2h$ times this bound plus the unchanged analytic tail. The original source
response construction, primitive propagation, angular normalization, and
moment construction are unchanged.

`tests/test_phys71_centered_angular.py` executed once: **4/4 methods PASS**.
The independent oracles use exact rational complex polynomial arithmetic.
They cover sixteen endpoint choices of complex coefficient uncertainty,
including a retained error-error cross term; exact projected polynomial
integrals; the projection example above; a nonconstant analytic multiplier
with zero response uncertainty and complex signs; and invalid radii/majorants.

The first raw output, source hashes, and timing are preserved in
`CENTERED_ANGULAR_TESTS_01_STARTED.json`, `CENTERED_ANGULAR_TESTS_01.json`, and
the associated stdout/stderr logs. Unittest reported 0.005 seconds; the
captured process took approximately 0.119 seconds. This review and these tests
performed **zero physical D3 panels, zero Coulomb evaluations, and zero old
integrations**. A revised physical pilot is a separate remaining gate.

The fixed request, $10^{-78}$ goal, original units, original source identity,
and `HH_R10=OFF` are preserved. Higher Born orders and original source-driven
$\xi$ remain outside this coefficient certificate.
