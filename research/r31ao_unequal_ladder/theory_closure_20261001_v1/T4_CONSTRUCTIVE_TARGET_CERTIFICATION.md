# T4 — constructive continuous-target certification and its stopping limits

This theorem closes effective computability and convergence obligations of the
selected continuous-target route. It neither evaluates actual HH inputs nor
admits a native numerical implementation. T1, T2, T3 and T5 name the companion
proofs in this directory. The accepted finite Hermite, spatial Gaussian and
endpoint identities are those in the immutable
`../endpoint_enclosure_review_20260930/NEW_THEOREM_REVIEW.md` (A–D).

## 1. Explicit input premises

Fix a finite source instance. Its Gaussian exponents a,b and mu are strictly
positive exact rational numbers; stored finite binary numbers have their exact
dyadic values, not their shortened decimal printouts. Centers, wave numbers,
contraction coefficients, stored prefactor and phase energies are real exact
rationals; the phase denominator v is nonzero. Degrees i,j,k are nonnegative
integers in a finite registry. The source normalization formula and orbital,
adjoint, cusp and parity conventions are fixed. Every denominator and every
radicand requiring positivity has its stated sign; formulas involving
normalization have finite, strictly positive normalization quantities.

The target uses the exact continuous integrals, followed by the same finite
source assembly. In particular D_row conjugation is performed after integration
on the real domain. No conjugation of a complex integration variable is
introduced. The radial s is the bilinear quadratic expression of the source,
not a Hermitian squared magnitude. Exact decoding and identity of actual input
bytes remain separate, unevaluated premises. The theorem is about this finite
source-defined target, not a proof of complete-HH physical adequacy.

## 2. A finite point evaluator, with explicit series tails

**Lemma T4.1.** At an exact rational complex pair (t,u) in the positive
half-planes, each selected O/G source expression, its finite contraction, and
its Laplace density product admits rational complex enclosures of arbitrarily
small prescribed radius by a finite algorithm.

### Hypergeometric part

For fixed rational a_h and b_h>0 and exact complex rational z, write

\[
F(z)={}_1F_1(a_h;b_h;z)=\sum_{n=0}^{\infty}
 { (a_h)_n\over (b_h)_n n!}z^n.
\]

Choose rational R>=|z| (|Re z|+|Im z| suffices), and define
T_n=|(a_h)_n|R^n/((b_h)_n n!). If a_h is a nonpositive integer,
the series terminates exactly and is evaluated as that polynomial. Otherwise
the positive majorants obey, whenever R>0,

\[
{T_{n+1}\over T_n}
= {R|a_h+n|\over (b_h+n)(n+1)}
\le {R(1+|a_h|)\over b_h+n}.
\]

The inequality follows from |a_h+n|<=n+|a_h|<=(n+1)(1+|a_h|).
If R=0 the value is 1 without a tail. Pick N with
q_N=R(1+|a_h|)/(b_h+N)<1. All ratios after term N are bounded by q_N,
so the error after retaining terms 0 through N satisfies

\[
\left|F(z)-\sum_{n=0}^{N}{(a_h)_n z^n\over(b_h)_n n!}\right|
\le {T_{N+1}\over1-q_N}.
\tag{T4-HYP}
\]

All quantities on the right are rational. First choose N0 with q_N0<=1/2.
For N>=N0 the majorants then decrease at least geometrically, proving that
testing successive rational bounds terminates for any positive target error.
Cancellation can increase cost but cannot invalidate the absolute remainder.
The case of a zero Pochhammer factor is handled by the terminating polynomial,
not by division through a zero T_n.

The source radial moment and its first two derivatives use

\[
M_k=(2\sigma)^{k/2}{\Gamma((k+3)/2)\over\Gamma(3/2)}
 {}_1F_1(-k/2;3/2;-s/(2\sigma)),
\]

with derivative parameters a_h=-k/2+r, b_h=3/2+r for r=0,1,2 and the
finite chain/Pochhammer factors. A zero derivative prefactor is evaluated as
zero before unnecessarily calling a series. At rational t,u, the Gaussian
means, sigma, bilinear s and z are complex rationals; sigma is nonzero by T1.
For k=2m the gamma ratio is (3/2)_m; for k=2m+1 it is
2(m+1)!/sqrt(pi). Thus no general gamma-function oracle is left unproved.

### Elementary part

Positive rational square roots are enclosed by rational bisection. Positive
fourth roots follow by two such enclosures. A rational interval strictly away
from zero permits reciprocal bounds; exact symbolic nonzero or positive
premises ensure eventual separation. For sigma=x+iy with x>0 use

\[
u_0=\sqrt{(|\sigma|+x)/2}>0,\qquad
v_0=y/(2u_0),\qquad \sqrt\sigma=u_0+i v_0.
\]

This gives the principal square root with no sign test at y=0 and agrees
with T1's branch. Integer powers and this square root suffice for all fixed
integer/half-integer source powers; positive normalizations use the same
bisection construction. The constant pi is computable from Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239), enclosing each arctangent by its alternating
series and next omitted term. For a rational complex w and R>=|w|, the
exponential series tail after N is at most

\[
 {R^{N+1}\over (N+1)!}\,{1\over1-R/(N+2)}\qquad (N+2>R).
\]

After a finite index its ratio is at most 1/2, giving the same effective
termination argument. This covers the real attenuation and complex phase.
If an intermediate argument is enclosed rather than exact rational, compact
local derivative bounds, for example |exp'(w)|<=exp(|w|), propagate its
argument error; refine that argument and the series error together. The
fixed formulas here permit rational arguments for the principal exponential
and hypergeometric calls in the point callback.

Finite sums/products, exact rationals, roots, reciprocals separated from zero,
and the preceding series therefore have effective enclosing evaluations.
Refining all elementary errors through a finite expression tree yields any
requested component error. This follows directly from interval continuity
at each nonsingular operation, proved for products by
|xy-c_xc_y|<=|c_x|r_y+|c_y|r_x+r_xr_y and for reciprocal by
|1/x-1/c|<=r/(|c|(|c|-r)) when r<|c|. Addition sums radii, and
roots are uniformly continuous, including the positive real zero boundary
when it occurs in auxiliary norm calculations. Fixed positive denominator
margins remove the reciprocal singularity. This proves T2.P3 without assuming
that holomorphy alone implies computability. QED.

## 3. Endpoint envelopes converge effectively to zero

Put lambda=mu^2/4. Each positive summand of the accepted absolute envelope is

\[
\Phi(t)=A\,e^{-\lambda/t}t^{-\nu}(a+t)^{-3/2},
\qquad A>0,\quad\nu>1,
\]

where nu is a positive half-integer. For 0<ell<T, its lower and upper tails
are bounded by

\[
L(\ell)=A a^{-3/2}\lambda^{1-\nu}
 \Gamma(\nu-1,\lambda/\ell),\qquad
U(T)={A\over\nu+1/2}T^{-\nu-1/2}.
\tag{T4-END}
\]

**Lemma T4.2.** Certified rational upper bounds for L(ell)+U(T) can be made
arbitrarily small by a finite search over ell_n=lambda/2^n and T_n=2^n,
starting sufficiently far out that ell_n<T_n. These cutoffs are dyadic when
the input mu is dyadic. Rational inputs otherwise allow rational cutoffs,
or outward dyadic cutoffs shrinking the same tails.

**Proof.** The upper tail is an explicit negative power of T_n. Set
s=nu-1=m+1/2 with integer m>=0. For x>0,

\[
\Gamma(1/2,x)=\int_x^\infty y^{-1/2}e^{-y}dy
\le x^{-1/2}e^{-x},\qquad
\Gamma(s+1,x)=s\Gamma(s,x)+x^s e^{-x}.
\]

The latter follows by integration by parts. Finite recurrence gives
Gamma(m+1/2,x)<=e^{-x}P_m(x), where P_0=x^{-1/2} and
P_{m+1}=(m+1/2)P_m+x^{m+1/2}; every coefficient is nonnegative rational.
Choose an integer M larger than every exponent in P_m. The positive
exponential series gives exp(x)>=x^M/M!, hence
exp(-x)P_m(x)<=M! x^{-M}P_m(x), an explicit finite sum of negative powers.
At x=2^n this converges effectively to zero. Rational upper bounds for its
half-integer powers and the fixed positive constants follow by bisection.
Thus even evaluation of a small incomplete gamma tail is unnecessary for
this existence proof. A finite search for a strict upper bound below the
requested positive tolerance terminates. QED.

An explicit finite whole-domain bound is
W<=A a^{-3/2}lambda^(1-nu)Gamma(nu-1), summed over the finite density terms;
Gamma(nu-1) is a half-integer gamma value, computable by recurrence from
sqrt(pi). Let S_i=L_i+U_i and let W_i be an independently valid whole-domain
upper bound for the corresponding absolute density envelope. The disjoint
rectangle-complement proof bounds each primitive by

\[
C_F(S_i W_j+J_i S_j)\le C_F(S_i W_j+W_i S_j),\qquad J_i\le W_i.
\]

No subtraction W-S of unrelated upper bounds is used. Corners are charged
once in the first expression. Both expressions tend to zero. Taking finite
absolute contractions and source assembly factors preserves effective
convergence. This is a proof for the continuous tail; it makes no assertion
about omitted nodes of a stored quadrature rule.

## 4. Arbitrarily narrow enclosures of the complete target

**Theorem T4.3.** Under Section 1's premises and the fixed source identities,
for every positive rational delta there is a finite rational certificate of
every selected continuous-target matrix entry as a complex disk with radius
at most delta. All matrices form a finite set. The construction does not
require termination of Petras or acceptance of a particular FLINT binary.

**Proof.** First use Lemma T4.2 and the finite contractions to place the
endpoint contribution below a chosen fraction of delta. The remaining
closed rectangle has positive lower endpoints. Choose strictly smaller
positive rational tube widths, for example less than half the corresponding
lower endpoint. T1 supplies holomorphy, positive denominator/branch margins,
and a finite explicitly computable product-domain majorant. Enclose that
majorant above by a rational M. Lemma T4.1 supplies exact-point evaluation.
T2's constructive midpoint quadrature then gives an interior complex absolute
error bounded by

\[
\operatorname{area}(R)\bigl(Mh_t/(4\delta_t)
                     +Mh_u/(4\delta_u)+\eta\bigr),
\]

which falls below any chosen positive budget after finitely many mesh
bisections and finite point evaluations. Here delta_t,delta_u are tube widths,
not the final entry tolerance delta. Endpoint and interior errors add once.

The number of primitive integrals and subsequent operations is finite.
Source normalization, prefactors and phase have computable enclosures by
Lemma T4.1 and remain finite with their stipulated denominator margins.
Conjugation after the real integration preserves disk radius. Finite
products and sums are continuous with the explicit error rules above;
refine primitive integrals and coefficient/phase enclosures until each final
entry radius is below delta. If rectangular component radii are returned,
use a disk radius at least sqrt(r_re^2+r_im^2), or the simpler r_re+r_im,
and allocate the budgets accordingly. The final entry radius includes all
these operations; it is not followed by another charge for the same phase
or assembly error. QED.

The finite algorithm can be extremely expensive. It proves no bound of
512-bit precision, 20,000 callback calls, 300 seconds, or any other fixed
resource cap. Failure under such a cap is an operational result, not a
counterexample to this theorem. Conversely, this existence proof is not an
implementation verification or an actual-input numerical certificate.

## 5. What refinement can and cannot settle

T4.3 makes uncertainty in D* arbitrarily small. It does **not** make
epsilon=||D_raw-D*||_2 arbitrarily small: the raw matrix is fixed.
T5's centered spectral residual interval converges to that fixed discrepancy;
the older entrywise Frobenius majorant may converge to a strictly larger
bound. T5 therefore removes a permanent source of avoidable conservatism.
Whether epsilon is below the actual budget remains a numerical fact.

For a real two-objective Pareto comparison with gaps
g_j=e_B,j-e_A,j and tolerance tau, the desired condition is
g_1>=-tau, g_2>=-tau, and max(g_1,g_2)>tau. Suppose

\[
d=\min(g_1+\tau,g_2+\tau,\max(g_1,g_2)-\tau)>0.
\]

T5's direct target gap intervals shrink to their true values. Eventually
their lower endpoints exceed -tau for both objectives and exceed tau for
one objective, proving the comparison. Existence of d>0 suffices; its value
need not be known by the certificate-search procedure. Robust failure, when
one weak inequality is strictly violated or both gaps are strictly below
the strict threshold, is likewise eventually detected by upper bounds.

Equality boundaries are different. Intervals [-2^-n,2^-n] enclose the exact
number zero for every finite n, yet do not prove its sign or exact equality
by endpoint comparison alone. Thus convergence alone supplies no universal
finite decision guarantee on boundary cases. An exact symbolic identity may
still decide a particular equality. No undecidability claim about this HH
instance is made.

The original machine predicates require T3's exact rounding-cell boundaries,
not merely a real gap relative to tau. If uncertain machine scalar operands
have certified bounds separated from all relevant cell boundaries, their
predicate is eventually certified by T3. If exact scalar bits are already
known, an exact rational emulator decides the elementary comparison even
at ties. Without those bits or a verified bound for the actual scalar
computation, an exact norm enclosure is not automatically an enclosure of
an SVD-produced floating-point scalar. T3 records this necessary authority
premise; this theorem does not assume correctly rounded SVD or BLAS.

## 6. Closure scope

The previously implicit mathematical links now have explicit constructions:
point computability, endpoint decay, compact interior certification, complete
target convergence and robust-decision termination. Actual source decoding,
positive input checks, normalization identity, backend and ABI admission,
finite numerical margins, and independent scientific admission remain
execution/data obligations. The optional stored-rule route has not been
selected or repaired. No actual epsilon or eta is assigned: both remain
null and rigorous=false for the actual reference certificate.
