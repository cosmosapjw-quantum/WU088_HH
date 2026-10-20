# PHYS72 independent angular multiplier review

**Disposition: PASS_SCOPED; no correction required.** This is an independent
read-only analytical and code review of the new angular addendum. It does
not rerun the main exact bound evaluator, a test suite, an inherited
campaign, or any physical integration.

## Reviewed identities

| Subject | SHA-256 |
| --- | --- |
| `theory/ANGULAR_MULTIPLIER_ADDENDUM.md` | `20c9f556fddcbba38011713c8d46971945004fba86692b1f235989cf75d6cac8` |
| `implementation/angular_weights.py` | `f30c427b659b66f0d068952ca6b764b9d481052424d8605c8ac9b7d0d5d30708` |
| Required unchanged `implementation/bounds.py` | `2036fc4b0d76a825d98e3ea3f2342c67c3029f4ed6fbe67686c1d70042762e7c` |

The independent derivation was checked before reading the final addendum;
the final proof and scalar code were then read in full. The author was
notified that the single planned exact scalar evaluation could proceed.
Its execution and output receipts belong to the author and are separate
from this review.

## Analytical checks

The gradient is the gradient on the **unit sphere**, with reduced bulk
measure `dr dOmega`. The identity
`d^2-r^2(1-mu^2)=(r*mu-a)^2` proves `|grad_S d|<=a` at every angle,
including the continuous extension at the poles. Differentiating the
original screen gives

\[
\frac{d\log V}{dd}=-2-\frac1{d(d+1)}.
\]

At `a=7/10`, `d>=263/10`, the exact angular log-gradient bound is
`502943/358995`, and its distance below `3/2` is
`71099/717990>0`. This uses the actual noncentral multiplier; it makes
no angular averaging or central replacement.

For complex-valued angular fields the product rule and the vector-valued
`L2` triangle inequality give the stated estimate with
`p=||g||_L2` and `t=||grad_S g||_L2`. The last step is precisely

\[
4(p^2+t^2)-\{p^2+(t+\tfrac32p)^2\}
=\tfrac34(p-2t)^2\ge0.
\]

Thus the factor `2` is valid in the angular `H1` multiplication bound.
Multiplication by the radial weights commutes with angular
differentiation, and `r^2 exp[-2(r-B)]` decreases on `r>=27`.
Consequently the radial/angular bound is `2 B^2 delta`.

The actual central outgoing Dirichlet Green operator commutes with
`(1+J)^(1/2)` on the finite-harmonic compact-source core. Applying the
already proved resolvent estimate to this angularly weighted source,
then extending by density, preserves the same resolvent constant
`C_*=253/1000`. This argument does not assert that `V` commutes with `J`.

For `w_j^2=1+j(j+1)`, the inherited weights satisfy
`2w_j<=C_j<=77w_j` on every degree. The low-degree lower margin is
`77^2-4(1+28*29)=2677>0`. On the infinite high-degree range,
`w_j^2<=(j+1)^2<=2w_j^2`, `(800/189)^2>4`, and
`2(800/189)^2<77^2` prove both comparisons without enumeration.
The number `77` in this equivalence is not a uniform upper bound on
the growing sequence `C_j`.

The resulting `H_C` multiplication bound is `77 B^2 delta`. The
diagonal angular spectral weight `C(J)` commutes with the actual
Green operator on the same core, so its resolvent constant is again
`C_*`. The final contraction bounds are therefore

\[
\|R_0^+V\|_{X_-(H^1)\to X_-(H^1)}
\le2q=1.106622\times10^{-20},
\]

\[
\|R_0^+V\|_{X_-(H_C)\to X_-(H_C)}
\le77q=4.2604947\times10^{-19}.
\]

Both sufficient Neumann conditions include `lambda=1`. Their scope is
explicitly `K=R0^+V` on the named weighted spaces. They are not asserted
as identical `H1` or `H_C` bounds for `sqrt(V) R0^+ sqrt(V)`. The
unweighted bulk `L2` sandwich estimate and the sharper fourth-and-higher
DtN remainder retain the original `q=5.53311e-21`.

## Fixed scalar implementation

The reviewed code uses `Fraction` operations for the constants and all
13 comparisons. The shear positive-semidefinite witness, both angular
comparison margins, the radial weighted constants, and the exact
identities `q_H1=2q`, `q_HC=77q` agree with the proof. The unchanged
main evaluator's source SHA is checked. The output is create-only and
binds both the scalar source and the addendum SHA.

The program correctly identifies the analytic envelope and outgoing
Green theorem as assumptions of its scalar audit. Evaluating the
finite rational witnesses does not by itself claim to sample or prove
the continuum inequalities. No source change, additional test suite,
physical run, Coulomb evaluation, old panel/profile replay, or change
to `HH_R10=OFF` is required by this review.
