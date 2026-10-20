# PHYS71: separating input coefficient uncertainty before the polar transform

Independent derivation, 2026-10-20 UTC. This review responds to the actual
first-panel enclosure: its reported numerical L1 radius was about
1.4690349306218242e-72, while its analytic integrand Cauchy remainder was about
5.55368284e-86. The fixed total goal remains1e-78; N=80, working precision
384bits and the source/kernel/geometry premises remain unchanged.
The exact saved pilot remains evidence of that first implementation. This
note does not execute or replace the pilot.

The raw `../d3/run_l36_t65/panel_0000.json` has SHA256
`4612e873215fd66e3cfe9d1615145a69440167cd8ca643ac159fff054fcfab9c`.
The invocation receipt is `../verification/D3_PILOT_EXECUTION.json`.
It completed one new valid enclosure whose radius fails the allocated
accuracy; it did not complete the76-panel campaign. The substantially
smaller analytic remainder motivates the hypothesis that interval
dependency in the Legendre-to-monomial contraction dominates this first
radius. The revised algorithm must be tested before attributing the
observed failure exclusively to that mechanism. The remaining75 panels
are not justified by the first pilot's radius.

## 1. What may be replaced and what must be bounded

Let U_a(z), U_b(z) be the exact analytic finite-L bulk response vectors
on a panel disk |z-c|<=rho. Let N be the retained Taylor degree and h<rho
the real half-width. Suppose Acb coefficient balls contain all exact
coefficients u_a,j,n and u_b,j,n for0<=n<=N. The existing profile and
forward-primitive construction provides that inclusion.

For each ball choose its exact dyadic complex midpoint p_a,j,n and a
nonnegative absolute error bound epsilon_a,j,n. The sum of its Cartesian
Arb radii is suitable. Thus

\[
u_{a,j,n}=p_{a,j,n}+e_{a,j,n},\qquad
|e_{a,j,n}|\le\epsilon_{a,j,n}.
\]

Define the finite midpoint polynomials p_a(z),p_b(z) through degree N.
Choosing midpoints alone would discard real uncertainty. The proposal
below explicitly bounds its effect in the original normalized angular
basis, before the Legendre-to-monomial transform enlarges componentwise
ball uncertainties through cancellation.

## 2. A weighted coefficient norm for the truncated product

For coefficient vectors in the original fixed-m basis define

\[
P_a(h)=\sum_{n=0}^{N}\sum_j |p_{a,j,n}|h^n,\qquad
E_a(h)=\sum_{n=0}^{N}\sum_j\epsilon_{a,j,n}h^n,
\]

and similarly for b. Cartesian absolute midpoint sums can replace
|p|; they only enlarge the positive bound. No angular basis conversion
is used to calculate P or E.

On |z-c|<=rho the existing multiplier majorant M_V bounds every
normalized angular entry V_jk(z). Entrywise Cauchy therefore gives

\[
|V_{jk,n}|\le M_V\rho^{-n},\qquad
V_*(h):=M_V\sum_{n=0}^{N}(h/\rho)^n.
\]

The finite geometric sum is bounded by M_V/(1-h/rho), which is a valid
simple implementation choice. The bound follows
from the full analytic V, not from a truncated numerical approximation.

Let T_N denote Taylor truncation at degree N around c. A coefficient
of degree<=N in a product of analytic power series uses only input
coefficients of degree<=N. Consequently

\[
T_N(U_a^T V U_b-p_a^T V p_b)
=T_N(e_a^T V p_b+p_a^T V e_b+e_a^T V e_b),
\]

where the e vectors on the right are the finite coefficient-error
polynomials. This equality concerns the truncated coefficients; it does
not equate the full analytic U with its finite polynomial.

For every x with |x|<=h, the triangle inequality and the nonnegative
coefficient convolution imply

\[
\boxed{
|T_N(U_a^T V U_b-p_a^T V p_b)(c+x)|
\le V_*(h)\{E_aP_b+P_aE_b+E_aE_b\}=:\mathcal E_{\rm coeff}.
} \tag{1}
\]

One way to see (1) is to sum the absolute value of each retained
coefficient times h^n and then enlarge the restricted convolution
n1+n2+n3<=N to the product of three nonnegative finite sums. This is
where all higher product degrees are handled: the bound enlarges a
finite nonnegative sum, without treating them as physical Taylor data.

The angular norm is deliberately a vector1-norm combined with an
entrywise matrix majorant. It introduces no hidden dimension factor;
the explicit sums over j and k already cover the finite basis. An
operator2-norm refinement is possible, but unnecessary for validity.
All contractions remain complex bilinear: the elementary inequality
|x^T A y| <= sum_jk |x_j| |A_jk| |y_k| holds without inserting a
conjugation into the physical integrand. The use of absolute values in
this norm estimate does not turn the transpose into an adjoint.

## 3. Integral enclosure with the existing true-function Cauchy bound

Let I(z)=U_a(z)^T V(z)U_b(z). The existing analytic bound

\[
M_I=M_V(\rho)
\left(\sum_jM_{U_a,j}(\rho)\right)
\left(\sum_kM_{U_b,k}(\rho)\right)
\]

bounds this true I on the rho disk. Therefore

\[
\left|\int_{-h}^{h}[I(c+x)-T_NI(c+x)]dx\right|
\le2hM_I\frac{(h/\rho)^{N+1}}{1-h/\rho}
=:\mathcal E_{\rm Cauchy}. \tag{2}
\]

Use exact midpoint coefficient polynomials as input to the existing
fast73-moment contraction. Outward Arb/Acb arithmetic then encloses the
coefficients of J=p_a^T V p_b through N, including every newly introduced
normalization, moment and arithmetic error. If Q encloses its integrated
Taylor polynomial, then

\[
\boxed{
\int_{c-h}^{c+h}I(r)\,dr
\in Q+\operatorname{disk}\!\left(
2h\mathcal E_{\rm coeff}+\mathcal E_{\rm Cauchy}\right).
} \tag{3}
\]

There is no need to assert a Cauchy bound for J or add a separate U-tail
bound. Equation(1) handles the coefficient replacement within T_N;
equation(2) handles the true full I minus its own T_N. Inserting only a
pointwise bound for U-p without addressing truncation would not establish
this particular formula; the coefficient argument does.

If the implementation encloses an absolute complex error disk by adding
its radius independently to both Cartesian radii, the final reported L1
box radius may grow by twice that amount. Acceptance must use the actual
reported enclosing radius and include all later panel carries/printing.
The coefficient replacement is an error decomposition, not a relaxation
of the fixed1e-78 physical goal.

## 4. Implementation obligations and discriminants

1. Retain the original ball-valued P carries and all analytic majorants.
   Only inputs to the angular contraction become midpoint polynomials.
2. Obtain midpoints and radii directly as exact Arb/Acb values. No Python
   float conversion is permitted.
3. Calculate P_a,E_a,P_b,E_b in the normalized channel basis using outward
   nonnegative arithmetic. Bound V's coefficient sum by the actual
   analytic disk majorant and the same N,h,rho.
4. Keep the true-function integrand Cauchy bound from the original U
   majorants, and add the separate coefficient-replacement allowance.
5. Record both error components in the panel payload so a reviewer can
   distinguish propagated input uncertainty, new ball arithmetic and
   analytic truncation.
6. A manufactured coefficient-box test should compare an independently
   contracted exact endpoint choice inside the original boxes with the
   midpoint result plus(1). Include degree1 or higher complex polynomial
   inputs and a nonconstant matrix V so the test checks the truncated
   coefficient argument. A scalar degree0 identity alone would not test
   the relevant concern.
7. The preserved original pilot and the changed-contraction pilot have
   different algorithm identities. A new targeted execution is justified
   by the changed error propagation; the unchanged75remaining panels must
   wait until the actual revised pilot meets its allocated budget.

No new physics integration, Coulomb evaluation or test execution was
performed by this derivation. The result is a constructive error
decomposition that tests the suspected interval dependency mechanism.
It makes no strong no-go claim.
HH_R10=OFF.

## 5. Actual revised-pilot readback

The subsequent revised pilot was read from
`../d3/run_l36_t65_stable_errors/panel_0000.json`, SHA256
`b01e8ebb7047557b0b89a1314e3390ecb8e812445ea4f654e60a3b23a95d90d8`.
Its invocation receipt is
`../verification/D3_STABLE_PILOT_EXECUTION.json`. This was a new candidate
implementation of the same physical panel, justified by the failed
accuracy gate and the change in uncertainty propagation. It is not a
repeat of an already accepted campaign or a replacement of the original
pilot evidence.

| Observed quantity | First pilot | Revised pilot |
|---|---:|---:|
| Numerical enclosure L1 radius | 1.4690349306218242e-72 | 5.554828422675563e-86 |
| True-integrand pointwise Cauchy tail | 5.5536828434976105e-86 | 5.5536828434976105e-86 |
| Projected coefficient-error bound | Included implicitly in ball propagation | 1.1455722635485645e-89 |
| Retained Taylor degree | 80 | 80 |
| Working precision in bits | 384 | 384 |
| Fixed all-angular/all-radial target | 1e-78 | 1e-78 |

Both Cartesian midpoint dyadics and every saved source-response carry
are exactly equal between these two payloads. The inherited payload
hashes, integrand disk majorant and analytic tail also agree. Source
readback shows that the finite-panel core changed only by adding the
centered contraction, using it in place of the original contraction,
and adding/recording the coefficient-error budget. The observed radius
reduction factor is approximately 2.6446090e13. These controlled
differences provide evidence that amplification of the propagated input
radii in the monomial representation dominated the first enclosure.
They do not assert that moment arithmetic or analytic tails are zero.

The revised coefficient budget equals an upward enclosure of
V_*(E_a P_b+P_a E_b+E_a E_b), and the final panel radius covers that
allowance plus the unchanged analytic tail and retained ball arithmetic.
The independently executed four manufactured tests are recorded in
`../verification/CENTERED_ANGULAR_TESTS_01.json`; this review read their
source and receipt without executing them again. They include complex
coefficient-box corners, retained quadratic cross terms, a nonconstant
analytic multiplier, and a case distinguishing projected from full
polynomial-product error.

Only the revised first panel is assessed by this readback. Its radius
uses about 1.9296274e-7 of the full campaign's remaining numerical and
printing allowance, 2.878705214756388e-79, using the corrected upward
radial decimal described below. This is a justified gate to
continue the same revised campaign; it is not a complete76-panel
certificate or a claim about higher Born orders. Both the unsuccessful
first pilot and the revised candidate remain in the evidence history.

## 6. Subsequent radial-decimal correction

The independent completed-result audit found that the inherited short
decimal 1.484322e-79 is below the true PR115 radial bound, approximately
1.4843223148855875485e-79. It is therefore not a valid upward endpoint.
The previously stated remaining allowance, 2.878705529646388e-79,
used that insufficient decimal and is superseded here. The actual PR115
proof prints the outward value 1.48432231489e-79. Exact rational comparison
with the stored exponential-series enclosure in
`../verification/RADIAL_DECIMAL_INWARD_ROUNDING.json` verifies that this
longer decimal is an upper bound.

The corrected remaining numerical and printing allowance is

\[
10^{-78}-A_{36}-1.48432231489\,10^{-79}
=2.87870521475638818933497\ldots\,10^{-79}.
\]

Here A_36 is the exact Fraction bound in ANGULAR_D3.md and its saved
machine result, rather than a rounded display used as an equality.

This correction changes the analytic aggregation only. It does not alter
the midpoint stability proof, any numerical panel, any source-response
carry, or the measured old/new pilot comparison. The raw completed
`CERTIFICATE.json` with SHA256
`8d0d3a45196c89cecbecae70b59b0b93b72bae5ca600e24bcc3864ffab0c012f`
must remain as producer evidence; its original aggregate is not accepted
as the final all-angular/all-radial certificate. A separate corrected
`ALL_ANGULAR_CERTIFICATE.json` and printing budget require their own
validation. This note does not infer that validation from the unchanged
numerical result or from the available error margin.

The original producer source and fingerprint must also be retained.
Correcting the future runner constant changes its source identity; that
new source must not be presented as the producer of the saved panels.
No physical integration or test was repeated for this correction.
