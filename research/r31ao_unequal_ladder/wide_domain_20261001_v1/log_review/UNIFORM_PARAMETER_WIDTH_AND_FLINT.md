# Uniform parameter width and pinned FLINT stopping behavior

This note reviews FLINT 3.4.0 source behavior to guide additive counters. It does not change a numerical tolerance, host algorithm or accepted result, and it performs no HH evaluation.

## Relative goal is not an additional stricter tolerance

The pinned `src/acb_calc/integrate.c` initializes

`new_tol = max(absolute_tol, lower_magnitude(initial_range_integral) * 2^(-goal))`.

Subsequent updates again take a maximum with the current tolerance. Thus for a uniform-inner request with `absolute_tol=2^20`, `goal=64` cannot reduce the operative tolerance below `2^20`. It does not require an additional 64-bit relative condition independently of the absolute tolerance. Raising or removing the relative goal cannot be justified as the identified fix for the present failure without other evidence.

The adaptive integrator initially computes a direct full-range enclosure `(b-a)*F([a,b])`. It attempts Gauss-Legendre only when that enclosure is finite. Otherwise it bisects, subject to its evaluation and queued-panel limits. The configured `depth_limit=64` is a queued-interval cap. A final `ARB_CALC_NO_CONVERGENCE` code does not identify which particular callback premise failed; observed nested-call counts alone do not establish the cause.

## Outer parameter width remains part of a uniform result

For a fixed outer box Y, a valid inner result encloses all `H(y)=integral F(x,y) dx` with y in Y. If those values vary, their image has a nonzero width even if quadrature error is arbitrarily small. Subdividing only the inner integration path cannot remove this genuine parameter variation. Arithmetic dependency in interval evaluation can add further excess width.

The pinned `integrate_gl_auto_deg.c` separately bounds quadrature truncation using an order-1 callback over a complex trial box, then sums order-0 node enclosures and adds the truncation bound. These node enclosures retain the outer parameter uncertainty. A small truncation bound therefore does not imply a small final returned component radius. The project host independently checks the achieved component radii after FLINT returns success; a uniform-inner `RADIUS_TOO_WIDE` can occur even after successful quadrature. This is distinct from FLINT nonconvergence and from a nonfinite preflight box.

The same observations also prevent the converse mistake: an excessively wide returned ball does not establish physical nonconvergence or a branch violation. It is a feasibility/acceptance failure for that uniform range request.

## Necessary diagnostic distinctions

Counters should distinguish the following without adding any callback evaluation or changing control flow:

- Full-inner-path order-1 preflight calls and nonfinite refusals.
- The selected point-inner or uniform-inner numerical plan.
- The actual inner return status, including `RADIUS_MET`, `RADIUS_TOO_WIDE`, `INTEGRATOR_NO_CONVERGENCE`, `NONFINITE_CALLBACK`, `RESOURCE_LIMIT`, and invalid contract.
- The outer request category: order 1, order 0 with exact input, or order 0 with nonexact input. Tiny-rounding-radius quadrature nodes are nonexact too; “nonexact” must not be relabeled “wide.”
- Refinable versus fatal outer refusal, and global budget stop reason.
- For an already computed finite failed inner result, its returned radius dumps and the corresponding outer-box real/imaginary radii can help distinguish parameter width from a domain refusal. Recording these values must not trigger a second callback or computation.

A cross-tabulation of selected inner plan, outer request category and inner status is more informative than separate marginal totals. Failure details may be bounded to counts plus the first/last few events. Recording more precision, new calls or different tolerance settings would change the experiment rather than merely observe it.

The accepted original and log driver sources remain frozen. Any instrumented host must be an additive source with its own manifest and must preserve the previous arithmetic, branch guards, caps, status decisions and invalidation behavior. An instrumented bounded retry of the same failed tile can diagnose those control paths; it is not a new algorithmic success claim.
