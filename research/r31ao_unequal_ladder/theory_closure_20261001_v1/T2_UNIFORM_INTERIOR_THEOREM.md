# T2: uniform nested integration and a constructive interior fallback

This is a mathematical result with explicit symbolic premises. It is not an
execution of the HH callback, a proof of a FLINT binary, or an actual-input
certificate. The elementary fallback below does not use Petras. Its finite
point evaluator is supplied by the source-function construction in T4, and
its complex-domain majorant is supplied by T1.

## 1. Exact objects and premises

Let \(a<b\), \(c<d\) be finite exact dyadic numbers, let
\(R=[a,b]\times[c,d]\), \(A=(b-a)(d-c)>0\), and let
\[
I=\int_a^b\int_c^d f(t,u)\,du\,dt,\qquad
H(t)=\int_c^d f(t,u)\,du .
\]
The integration variables and endpoints in \(I\) are real. Complex arguments
are used to enclose values and prove analyticity. Changing a cutoff changes
the target unless the same exact cutoff is used in the endpoint calculation.
There is no endpoint midpoint rounding in this theorem. Zero-length rectangles
have integral zero and are handled separately.

Here \(f\) is the selected holomorphic source integrand, such as an O/G
primitive or its finite source-prescribed linear combination. A literal
conjugation of a complex integration variable is not holomorphic. The
source-prescribed post-integral row conjugation is handled after integration,
as described in T1, and is not inserted into the premise for \(f\).

The following premises are individually necessary for the stated conclusions.

**P1, domain.** The selected, single-valued \(f\) is jointly holomorphic on an
open neighborhood of the compact product
\[
K_t\times K_u,\quad
K_t=[a-\delta_t,b+\delta_t]+i[-\delta_t,\delta_t],\quad
K_u=[c-\delta_u,d+\delta_u]+i[-\delta_u,\delta_u],
\]
where \(\delta_t,\delta_u>0\) are exact rational numbers. Branch choices and
nonzero denominators are part of this statement; a finite sampled value does
not establish it. T1 provides this product domain for the selected source
expressions, with positive real-part margins. If additional parameters are
present, every claim must hold for their complete declared parameter set.

**P2, explicit bound.** A finite, nonnegative rational \(\widehat M\) is
certified to satisfy \(|f(t,u)|\leq\widehat M\) on the whole product above.
T1 provides a symbolic expression for such a majorant. Replacing its
transcendental or root factors by certified rational upper bounds is allowed.
For example, for rational \(x>0\),
\(x^{-3/2}\leq\max(x^{-1},x^{-2})\), and a known factor \(e^{-x}\), \(x\geq0\),
can be bounded by 1. Thus a loose rational majorant is sufficient; no actual
HH constant is evaluated in this document.

**P3, effective exact-point evaluation.** For each required exact dyadic
complex point in the certified domain and each rational \(\eta>0\), a finite
algorithm returns a rational complex center \(q\) and certified component
radii \(r_{\rm re},r_{\rm im}\geq0\), with
\[
f(t,u)\in q+[-r_{\rm re},r_{\rm re}]
                 +i[-r_{\rm im},r_{\rm im}],\qquad
r_{\rm re}+r_{\rm im}\leq\eta .
\]
Therefore \(|f(t,u)-q|\leq\eta\). This is a proved computability requirement,
not a tolerance flag. T4 supplies a construction for the selected source
function from fixed exact coefficients using finite elementary-function
enclosures and a hypergeometric-series tail bound. Holomorphy and a bound
alone do not imply P3: even a constant function can contain a noncomputable
constant. For a different integrand, P3 must be established separately.

For rational but nondyadic endpoints the same proof gives an exact rational
grid if the point evaluator accepts those points. The dyadic formulation
matches the current native endpoint contract and needs no such extension.

## 2. Holomorphic parameter integration

**Lemma T2.1.** \(H\) is holomorphic on the open \(t\)-domain whose product with
\([c,d]\) lies in the certified open neighborhood. In particular, it is
holomorphic on an open neighborhood of every admitted compact outer box
\(T\subset K_t\). For each nonnegative integer \(m\),
\[
H^{(m)}(t)=\int_c^d \partial_t^m f(t,u)\,du,\qquad
|H(t)|\leq(d-c)\widehat M \quad(t\in K_t).
\]

**Proof.** Around any fixed \(t_0\), compactness of \([c,d]\) gives a common
closed disk in the \(t\) variable whose product with that interval stays
inside the open domain. On a slightly smaller disk the Cauchy integral
formula uniformly bounds every required derivative of \(f\). The Cauchy
formula for \(f(t,u)\) can be integrated over \(u\); the finite contour and
real interval have a continuous bounded integrand, so interchange is valid.
It yields the Cauchy formula and derivative formula for \(H\). This proves
holomorphy and all derivative identities. The last bound is the integral
triangle inequality. Continuity on the compact real rectangle also gives
the Fubini identity defining \(I\). No numerical partition occurs in this
argument. \(\square\)

**Cauchy constants on the real rectangle.** The closed radius-\(\delta_t\)
disk centered at each real \(t\in[a,b]\), with real \(u\in[c,d]\), lies in
\(K_t\times K_u\), and similarly for \(u\). Hence
\[
|\partial_t f|\leq L_t:=\widehat M/\delta_t,\qquad
|\partial_u f|\leq L_u:=\widehat M/\delta_u \quad\hbox{on }R.
\]
More generally
\(|\partial_t^m\partial_u^n f|
\leq m!n!\widehat M\,\delta_t^{-m}\delta_u^{-n}\) on \(R\).
These particular derivative constants must not silently be reused at the
outer boundary of \(K_t\) or \(K_u\). On the half-width tubes
\(K_t^{1/2},K_u^{1/2}\), the safe corresponding constants are
\(2\widehat M/\delta_t\), \(2\widehat M/\delta_u\).

## 3. Full-box inner evaluation contract

A complex rectangle is a set, not its midpoint. For every requested outer
rectangle \(T\), an inner evaluator may return one of the following.

* **ENCLOSED:** a finite rational/outward-rounded complex rectangle \(B\),
  together with a domain/proof identifier, satisfying
  \(\{H(t):t\in T\}\subseteq B\).
* **REFUSED/INCONCLUSIVE:** no value enclosure is asserted. Domain failure,
  exhausted resources, unproved analytic continuation, or a radius exceeding
  an application cap can produce this result.

If an evaluator computes an approximation family \(Q(t)\) and proves a
uniform error \(E\), a valid construction is
\[
\{Q(t):t\in T\}\subseteq B_Q,\quad
\sup_{t\in T}|H(t)-Q(t)|\leq E,\quad
B=B_Q+[-E,E]+i[-E,E].
\]
Proving the error only at the center of \(T\) is insufficient. A direct
uniform bound, for example
\([-(d-c)\widehat M,(d-c)\widehat M]+
i[-(d-c)\widehat M,(d-c)\widehat M]\), is mathematically valid
although often too wide for an application.

**Lemma T2.2, adaptive partitions.** The partition used by an inner call may
depend on the complete input box, precision, tolerance request, and previous
inclusion results. It may differ from the partition of every other call.
This does not affect soundness if the completed finite partition covers
\([c,d]\) without omitted or double-counted positive-length panels, each
panel's enclosure is valid uniformly for every \(t\in T\), and the returned
sum includes all panel and rounding errors.

**Proof.** Fix an arbitrary \(t\in T\). Additivity of integration over the
completed partition and the individual panel inclusions imply inclusion of
\(H(t)\) in their outward sum. The same proof holds for every \(t\in T\).
The rule selecting the partition is irrelevant to the inclusion argument.
An early stop with uncovered panels supplies no such argument. \(\square\)

The algorithmic map \(T\mapsto B\) need not be analytic or continuous.
Analyticity is a property of the single exact function \(H\), not of chosen
partitions, widths, or rounded endpoints. One cannot instead regard a
piecewise-selected midpoint approximation as the analytic function \(H\).

## 4. What an outer Petras callback must promise

This section specifies a sufficient mathematical interface. It does not
verify the implementation of a quadrature library.

1. The target function is the same exact \(H\) for all calls, including all
   branch conventions and exact inner endpoints. Extra physical parameters
   remain fixed, or retain their complete explicitly declared boxes.
2. For order 0, a finite response contains \(H(T)\) for the entire input
   rectangle. Nonzero input radii must not be discarded even if the request
   is described as a “point” evaluation.
3. For order 1, the finite response again contains \(H(T)\), and \(H\) is
   proved holomorphic on an open neighborhood of the entire requested
   complex rectangle. An admitted T1 product domain covering
   \(T\times[c,d]\) plus Lemma T2.1 is sufficient. Checking only quadrature
   nodes or only the midpoint is insufficient. Here order 1 requests the
   zeroth Taylor coefficient (the value) with an analyticity guarantee,
   **not** a first derivative. Orders above 1 require the corresponding
   derivative/Taylor-coefficient contract or an explicit refusal.
4. If either level requests analytic evaluation, every lower-level proof
   used for that level must cover its complete complex argument box and the
   complete retained parameter box. A branch/domain certificate cannot be
   inferred from a finite result alone.
5. Failure to establish an order-1 trial domain returns a refusal/nonfinite
   bound, so a library may try a smaller domain. It is not a finite
   certificate and does not establish global nonintegrability. Resource
   exhaustion and actual invalid path data are separately classified.
6. Requested tolerances and precision are control inputs. An accepted result
   must be finite and its actual returned component radii must meet the
   application error budget. A success return code or requested tolerance
   is not a substitute for checking those radii.

**Conditional composition theorem T2.3.** Suppose an admitted outer
quadrature implementation is sound for the interface just stated, and every
inner response meets that interface. Every outer enclosure admitted by its
soundness contract contains \(I\). Additional radius-based acceptance implies
the claimed component-radius bound.

**Proof.** Lemmas T2.1–T2.2 establish that every supplied response encloses the
same exact holomorphic \(H\). Substitution into the outer method's stated
soundness theorem then gives an enclosure of \(\int_a^bH(t)\,dt=I\).
The numerical size claim follows from the checked output radii, not from a
requested tolerance. \(\square\)

The antecedent concerning the outer implementation is explicit. Existing
FLINT headers, documentation, static checks, synthetic tests, or a return
code are not a proof of its complete binary implementation. The pinned
FLINT 3.4.0 documentation describes order 0/1 in this way and explicitly
warns that cumulative error can exceed the requested goals. That describes
the intended interface; this document does not claim verified Petras
termination, performance, host execution, or implementation admission.

## 5. A finite constructive method independent of Petras

**Theorem T2.4.** Under P1–P3, for each positive rational \(\varepsilon\)
there is an explicitly constructed finite exact-arithmetic certificate
\[
I\in Q+[-E,E]+i[-E,E],\qquad E\leq\varepsilon .
\]
There is no fixed-resource guarantee.

Partition \(R\) into finitely many closed rectangles \(R_{ij}\) with disjoint
interiors, side lengths \(h_i,k_j\), centers \(m_{ij}\), and areas \(A_{ij}\).
At each center use P3 to obtain \(q_{ij}\) with
\(|f(m_{ij})-q_{ij}|\leq\eta_{ij}\). Form the exact rational complex number
\(Q=\sum A_{ij}q_{ij}\). A valid bound is
\[
E=\sum_{ij}A_{ij}\left(
       L_t h_i/4+L_u k_j/4+\eta_{ij}\right).
\tag{T2-ERROR}
\]
For a product grid with maximum side lengths \(h_t,h_u\) and uniform
\(\eta\), this gives
\[
|I-Q|\leq A(L_t h_t/4+L_u h_u/4+\eta).
\tag{T2-UNIFORM}
\]

**Proof of the bound.** On one cell, integrate the derivative of \(f\)
first along the real \(t\) coordinate and then along the real \(u\)
coordinate. The derivative bounds give
\[
|f(t,u)-f(m_{ij})|
\leq L_t|t-m_t|+L_u|u-m_u|.
\]
The integral of distance from the midpoint over an interval of length \(h\)
is exactly \(h^2/4\). Integrating the last display over the cell and adding
\(A_{ij}|f(m_{ij})-q_{ij}|\) therefore proves its term in (T2-ERROR).
The complex integral triangle inequality and summation prove the formula.
There is no unestimated midpoint-rule remainder and no reliance on observed
convergence. The formula also applies to a finite adaptive rectangular
partition by summing its actual cell side lengths and areas. \(\square\)

The proof certifies the disk error \(|I-Q|\leq E\). Storing it as a complex
rectangle with both component radii \(E\) is a safe outer enclosure but gives
a whole-rectangle modulus-radius bound of at most \(2E\) by the rational
triangle bound (or \(\sqrt2 E\) if a square-root bound is used). Downstream
contraction budgets must use the convention they actually consume; component
radius, disk error, and diameter are not interchangeable.

**Explicit finite choice.** Choose nonnegative integers \(n_t,n_u\) by
rational comparisons and doubling until
\[
h_t=(b-a)2^{-n_t}\leq\frac{\varepsilon}{A L_t}
       \quad(L_t>0),\qquad
h_u=(d-c)2^{-n_u}\leq\frac{\varepsilon}{A L_u}
       \quad(L_u>0).
\]
When a derivative bound is zero, choose the corresponding \(n=0\).
Set \(\eta=\varepsilon/(2A)\). Each derivative contribution is at most
\(\varepsilon/4\), and the evaluation contribution is at most
\(\varepsilon/2\). Hence \(E\leq\varepsilon\).
All grid endpoints and centers are dyadic; all weights and error accounting
are exact rational numbers. The doubling loops terminate because the
positive right-hand sides are fixed rationals. The number of calls is the
finite integer \(2^{n_t+n_u}\), and each call terminates by T4/P3. This proves
finite termination for any requested accuracy, without a particular bit,
time, memory, panel, or evaluation cap.

An implementation may enumerate cells sequentially, accumulate \(Q\) and
the nonnegative error budget, and retain a finite audit record of the
individual enclosures or their independently checkable construction.
If it stops before all cells are covered, it must return INCONCLUSIVE or add
a valid enclosure for every omitted cell. Repeatedly reducing a requested
tolerance under an unchanged fixed precision or fixed resource cap is not
this constructive algorithm.

## 6. Uniform complex parameter boxes and the width obstruction

The one-dimensional version of (T2-ERROR), uniform for \(t\in T\), gives
\[
H(T)\subseteq B_Q+
 [-E_u,E_u]+i[-E_u,E_u],\qquad
E_u=\sum_j k_j(L_u k_j/4+\eta_j),
\]
provided \(B_Q\) encloses the full family
\(\{\sum_j k_j q_j(t):t\in T\}\) and
\(\sup_{t\in T}|f(t,m_j)-q_j(t)|\leq\eta_j\).
Point-oracle P3 alone does **not** supply this full-family premise.

A constructive alternative avoids that gap. Let \(T\) be a convex complex
rectangle in the half-width \(t\) tube with exact dyadic center \(t_0\), and let
\(\rho_T\geq\sup_{t\in T}|t-t_0|\) be a rational upper bound (the sum of the
two component radii is sufficient). The Cauchy bound on that half-width
tube gives \(L_t^*=2\widehat M/\delta_t\). Compute a scalar inner midpoint
certificate for \(H(t_0)\) using P3, with error \(e\), and center \(q\).
Then
\[
H(T)\subseteq q+[-W,W]+i[-W,W],\qquad
W=e+(d-c)L_t^*\rho_T .
\tag{T2-PARAM}
\]
Indeed integrate the complex \(t\)-derivative along the straight segment
from \(t_0\) to \(t\), which stays in the convex half-width tube, and then
integrate over \(u\). The scalar inner certificate is computed using
\(|\partial_u f(t_0,u)|\leq\widehat M/\delta_u\), since the radius-\(\delta_u\)
disk at real \(u\) is still in \(K_u\). Thus (T2-PARAM) is finite and
uniform, and Lemma T2.1 supplies its order-1 analyticity certificate.

The same argument covers an extra finite-dimensional convex complex
parameter box \(P\). If certified bounds
\(|\partial_{p_j}f|\leq L_{p_j}\) hold on the corresponding product domain,
then
\[
|I(p)-I(p_0)|\leq A\sum_jL_{p_j}\rho_j .
\]
A finite dyadic subdivision of a box \(P\) with dyadic endpoints, plus T2.4
at each center, makes each
local enclosure arbitrarily narrow. It need not make the single enclosing
hull of all of \(I(P)\) narrow: different exact parameters can have genuinely
different exact values. Uniform quadrature error tending to zero and total
range width tending to zero are different statements.

## 7. Exact counterexamples

Take the entire polynomial \(f(t,u)=t u^2\), \(u\in[0,1]\). Its exact
parameter integral is \(H(t)=t/3\).

**Midpoint-only failure.** For \(T=[0,1]\), evaluating the inner integral only
at the outer midpoint gives the singleton \(\{1/6\}\). But \(H(0)=0\) and
\(H(1)=1/3\). The singleton excludes both exact endpoint values. An inner
computation can therefore have zero scalar numerical error and still fail
the outer box callback contract. This is an exact algebraic counterexample,
independent of any library behavior.

**Uniform-width obstruction.** For
\(T=[1,2]+i[-1,1]\), the exact image is
\[
H(T)=[1/3,2/3]+i[-1/3,1/3].
\]
Every rectangular enclosure has real radius at least \(1/6\) and imaginary
radius at least \(1/3\). No precision increase, inner panel refinement, or
smaller requested tolerance can produce a correct whole-box enclosure with
both radii below \(1/10\). The obstruction is intrinsic parameter variation,
not an integration error. A policy using a larger uniform order-1 bound and
tighter point bounds can be sensible, but its termination still needs proof
or the finite fallback above.

The optional exact-arithmetic checks in theory_checks exercise these
algebraic examples and the error-budget arithmetic only. The proofs are the
arguments above; successful tests are not theorem authority.

## 8. Closure and remaining implementation obligations

T2 closes the mathematical uniform-inclusion obligation and supplies a
finite requested-accuracy interior construction using the explicit T1
domain/majorant and the proved T4 point evaluator. It does not assume that
the existing inner/outer Petras heuristic terminates, or that its current
native wrapper has been verified. The fallback is a separate certified
algorithm, not an empirical claim about that implementation.

Actual source/input binding, actual bound magnitudes, practical work cost,
native binary/runtime verification, and admission of an eventual output
remain separate. Neither this theorem nor its synthetic checks accesses HH
arrays, computes HH constants/integrals, or certifies epsilon/eta.

## Primary interface source

Pinned local FLINT 3.4.0 documentation:
gap_work/backend_reference/doc/source/acb_calc.rst, callback contract
lines 14–53 and 103–169. Its SHA256 and the source archive pin are recorded
in the companion T2 JSON. The mathematical arguments in Sections 1–7 are
given in full here and do not depend on accepting a numerical library.
