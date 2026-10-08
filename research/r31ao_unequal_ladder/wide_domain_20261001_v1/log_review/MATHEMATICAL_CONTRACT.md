# Independent log-coordinate contract review

Scope: an additive change of integration coordinates for the existing exact Frozen107 continuous primitive. This review does not change the physical target, donor coefficients, principal-power branches, endpoint bounds, normalization, assembly, final decision rule or runtime admission. It does not evaluate an HH callback or execute an HH integral.

## Exact map and measure

Let the original compact integral be

\[
I=\int_{\ell_u}^{T_u}\int_{\ell_t}^{T_t}F(t,u)\,dt\,du,
\qquad 0<\ell_t<T_t,\quad0<\ell_u<T_u.
\]

For physical endpoints that are exact integer powers of two, write
\(\ell_t=2^{a_t},T_t=2^{b_t},\ell_u=2^{a_u},T_u=2^{b_u}\), with integer exponents. The exact change of variables is

\[
t=e^{xL},\quad u=e^{yL},\quad L=\log 2,
\qquad
I=\int_{a_u}^{b_u}\int_{a_t}^{b_t}
  L^2e^{xL}e^{yL}F(e^{xL},e^{yL})\,dx\,dy.
\]

The Jacobian is **both** factors \((Lt)(Lu)\), each once. The original `polynomial_field` includes no coordinate Jacobian. Center derivatives already encoded as G1/G2 remain the same fields; this substitution is not an additional center derivative. Since both real maps are increasing, no orientation sign changes. Rejecting physical dyadics that are not powers of two is a deliberate supported-input boundary; taking a floating `log2` and pretending its output is an exact endpoint is forbidden.

The constant L must be an outward Arb enclosure. Finite-precision Acb exponentiation and multiplication then enclose the exact mathematical map and Jacobian. Reusing the same L ball does not assert statistical independence: interval dependency can widen the result, but does not invalidate inclusion. Comparing transformed and untransformed results by bit identity is incorrect because operation association and quadrature nodes change. Independent rigorous enclosures of the same target must overlap; overlap is a consistency check, not by itself proof that either implementation is correct.

## Holomorphy and branch domains

For z=x+i y,

\[
\Re(e^{Lz})=e^{Lx}\cos(Ly)>0
\quad\text{when}\quad |y|<\frac{\pi}{2\log2}.
\]

Thus the product of these open strips maps to the product of right half-planes. With the original positive real a,b, A=a+t and B=b+u remain in the right half-plane. Their reciprocals do also, hence \(\sigma=(A^{-1}+B^{-1})/2\) has positive real part. These domains retain the original principal powers and the already derived analytic continuation of the radial moments. The 1F1 denominator parameters remain 3/2,5/2,7/2. The bilinear square in the radial argument and absence of complex conjugation inside the integrand are unchanged. Multiplying the jointly holomorphic F by the entire coordinate/Jacobian functions preserves joint holomorphy wherever the physical-domain premises hold.

The strip statement is mathematical domain information, **not permission to clip a backend input**. Acb stores rectangular enclosures, and the rectangular hull of an exponential image can include points not in that image. The original callback must still prove all of its full-ball positive-margin checks (t,u,A,B,sigma) and finite special-function results. If its rectangular enclosure fails a guard, returning indeterminate is conservative. Replacing the image by its midpoint, discarding its radius, silently intersecting with an unimplemented domain theorem, or permitting a branch-crossing enclosure is invalid.

The physical real-window margin remains

\[
2^{-20}\min\left(1,\ell_t,\ell_u,
\frac{(a+T_t)^{-1}+(b+T_u)^{-1}}2\right)>0.
\]

This uses exact physical endpoints and parameters, not their logarithms. It is strictly below all corresponding real-path lower bounds. A smaller domain guard here does not relax the integral-error criterion. Passing the real-path margin calculation alone does not admit an arbitrary complex trial box.

The pinned FLINT integration implementation calls order 0 for range/node values and order 1 for a value plus a holomorphy assertion over a complex trial box. Order 1 does not request the derivative of the transformed function, so no additional derivative-chain formula belongs there. Unsupported higher orders must invalidate every requested coefficient rather than returning one plausible coefficient.

## Uniform nested integral

For a whole outer complex box Y, the inner callback must enclose

\[
\{L^2 2^x2^y F(2^x,2^y):x\in X,\ y\in Y\}
\]

for every inner range/node X passed by the integrator. Consequently the returned inner integral must enclose \(\{H(y):y\in Y\}\), where H is the exact integral over the fixed inner real path. Passing the entire mapped outer box to the old callback and applying the entire mapped Jacobian preserves this requirement. Adaptive inner partitions may vary between calls if each output remains a uniform enclosure. A wide outer image is real parameter dependence, not quadrature error that can be removed by demanding a smaller inner tolerance.

Inherited finite integration, callback, wall, memory, degree and panel caps remain binding. Contract violations, exact-point failures, exceptions and shared budget exhaustion remain fatal to the attempt. Trial-box/domain refusals can be refinable without being successful evaluations. Final acceptance requires the achieved finite returned component radii, not merely the requested tolerance or FLINT success status.

## Observed wide-image limitation

The independent `log_image_probe.cpp` runs no callback and no integral. It evaluates only the outward image `exp(log(2)*[a,b])` against exact powers-of-two endpoints using the pinned built FLINT 3.4.0 backend. At both 128 and 256 bits, all exact endpoints were enclosed, but the full image could not prove a positive real part for `[-8,24]`, `[-8,56]`, or `[-8,192]`. `[0,1]` and `[-4,8]` did prove positivity at both precisions.

This is a conservative enclosure failure, not evidence that the positive real mathematical image contains zero. The inherited outer order-1 preflight applies the callback over the **whole inner path**. Therefore W3's 200-bit physical scale range can still make that preflight fail even for a narrow outer box. Log coordinates improve the quadrature-coordinate scaling but do not automatically solve this full-image problem; increasing significand precision from 128 to 256 did not solve it in the measured range diagnostic. No W3 success is inferred from the transform proof or this test.

Evidence: `geometry_runtime/REVIEW_RUN.json`, including compiler/source/backend/linkage identities, 512 MiB address-space cap, 30-second compile cap and 10-second run cap. Ten geometry cases are not ten scientific integrations.

## Safe finite tile continuation

Choose finite strictly increasing exact integer log grids A and B spanning the original log-window endpoints. The Cartesian tiles `[A_i,A_{i+1]] × [B_j,B_{j+1]]` have disjoint interiors and cover the window exactly; shared boundaries have measure zero. Transforming each tile maps it to exactly the corresponding physical powers-of-two rectangle. The original callback guards and uniform complex-box requirements apply within each tile. Subdivision helps feasibility; it does not authorize a result for a rejected tile.

For each physical primitive and global window, admit the sum only after verifying:

1. Every expected tile is present exactly once, with exact expected coordinates. No missing tile, duplicate, overlap of positive area or out-of-window rectangle is accepted. Tile count alone is not a coverage proof.
2. All tiles bind the same exact input/archive, physical primitive, callback target and reviewed backend/build identity. A per-tile plan identity may differ because its window differs; the global collector must explicitly bind that local-to-global mapping.
3. Every tile returned a valid finite enclosure under its original finite caps. Failure or exhausted global resources cannot become a zero contribution or an unrecorded retry.
4. Sum the **serialized exact dyadic lower and upper endpoints** separately. Exact rational/dyadic addition incurs no new roundoff; otherwise outward native summation must include its roundoff. The final exact interval widths are the acceptance authority.
5. For global component radius bound `2^E` and N tiles, a convenient conservative per-tile radius budget is `2^(E-ceil(log2 N))`, so their sum is at most `2^E`. The final serialized halfwidth still has to pass the global cap; requested tolerances and internal pre-serialization radii are insufficient evidence if serialization or summation enlarged the intervals.
6. Add the original global-window endpoint disk exactly once, after the entire compact interior is present. Per-tile endpoint records cannot replace or multiply the global complement bound. A partial compact sum is not a full-window integral.

An optional bounded pilot of at most 16 predefined tiles is compatible with this contract when its total caps are declared before execution. No grid was executed by this review. No 40,000-tile campaign, production D construction or NCP scaling result is implied.

## Review boundary

The coordinate transformation is mathematically valid under the stated source/branch/enclosure premises. Concrete adapter source and its receipts require their own source-pin review. Synthetic polynomial/inverse-power oracles can detect Jacobian, orientation and box-propagation mistakes; they do not validate all odd radial HH special-function values or final D. Actual primitive comparisons, full 2,592-task coverage, endpoint/normalization composition, raw D discrepancy, final epsilon/gap decision and NCP MPI admission remain separate evidence obligations.
