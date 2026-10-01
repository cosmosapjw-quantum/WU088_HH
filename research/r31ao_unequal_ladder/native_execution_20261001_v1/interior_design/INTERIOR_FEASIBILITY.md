# Source-bound compact-interior feasibility

This note concerns the unchanged Frozen107 primitive index 0 and the W3 window `[2^-8,2^192]^2`. No callback, integral or endpoint component was evaluated by this design module. The endpoint W3 certificate remains an independent, conditional disk bound outside this whole rectangle.

## Two different execution blockers

The prior worker chose `margin=min(1,l_t,l_u)/2^20`. For W3 that is `2^-28`, whereas for positive a,b,

`sigma(T,T)=(1/(a+T)+1/(b+T))/2 < 1/T = 2^-192`.

The unchanged callback requires the whole computed real part of sigma to exceed margin. Thus a real part of the requested integration domain is refused regardless of numerical precision. The additive worker fixes this by using

`margin=min(1,l_t,l_u,(1/(a+T_t)+1/(b+T_u))/2)/2^20`.

The real-path bound follows from monotonicity in both variables. It changes a domain guard, not the source function or requested error tolerance. All computed complex balls must still pass the original guards. This does not promise that a large complex trial rectangle will be accepted.

The second problem is the initial range request. The pinned FLINT integrator first calls a simple quadrature step with an order-0 callback on the entire interval. The old host wrapper treats any nonfinite order-0 result as a global failure. A broad Arb input enclosure can cross zero due to midpoint/radius rounding or intermediate interval overestimation even though all exact real arguments are positive. In particular, the exact midpoint of `[2^-8,2^192]` requires 201 significand bits; 128 bits cannot preserve both endpoint scales in that midpoint. Merely lowering margin cannot fix a computed ball that includes zero. The native review's separate `1/t` probe is intended to distinguish refinable box refusal from global exhaustion; no host-wrapper retry semantics are changed here.

Uniform-inner range width is another legitimate limitation. `integrate_uniform_inner` passes the complete outer complex box, and a true parameter-image width need not vanish under inner quadrature refinement. Its current finite radius gate can refuse such a trial. Repeatedly tightening inner tolerance does not prove or remove this width. Record domain refusal, achieved width and resource exhaustion separately.

## Immediate bounded experiments

`runtime/pilot_plans/` contains exact source-validated plans and limits for:

| Plan | Rectangle | Purpose |
|---|---|---|
| CENTRAL | `[1,2]^2` | First actual nontrivial compact piece of the same primitive |
| TINY_CENTRAL | `[1,257/256]^2` | Predetermined smaller piece if broad range/width refusal blocks the first |

Both preserve precision 128, accepted component radius `2^-48`, relative goal 64, 20,000 dispatched evaluations, 1,024 integration calls, queued-panel limit 64, degree limit 64, 30-second cooperative wall cap and the existing 1024MiB process memory limit. No full-D tolerance is inferred from these settings. The actual process wrapper adds its existing hard wall termination margin. Returned ball radii, native status and source/build identities must be retained. A successful microbox is a compact-interior diagnostic only.

No endpoint bound was computed for these microboxes. Their endpoint-plan records serve only as exact window/parameter identities for the existing native API. Do not join a microbox with the W3 endpoint result: their window and task identities differ, and most of the W3 interior is missing.

## Exact decomposition if a compact pilot works

The bounded planner partitions each positive axis by `[x,min(2x,T)]`. Every endpoint is an exact dyadic and every interior point lies in exactly one tile, except shared boundaries of measure zero. The target is analytic on the positive rectangle, so the finite Cartesian sum of tile integrals equals the original compact integral. For W3 this produces 200 intervals per axis and 40,000 rectangles. The planner records this count and **does not dispatch this grid**.

A future adaptive tile driver should begin with a finite set of aspect-ratio-controlled rectangles, subdivide only failed or too-wide tiles within predeclared global limits, and store accepted tile enclosures with their original global task identity plus exact tile endpoints. A local failure may justify subdivision only when the backend identifies it as a refinable trial-domain/width issue; input corruption, exhausted callback budgets and hard wall limits remain fatal to that attempt. No unlimited retry is permitted.

Full-window acceptance requires an exact no-gap/no-duplicate coverage proof, outward summation of every accepted tile rectangle, and the **original global endpoint disk added exactly once**. Adding an endpoint remainder per tile would duplicate uncertainty and change the contract. The current primitive join correctly refuses mixed window identities; a tile-aware collector is an additional explicit implementation obligation.

For a padded tile, the planner uses a rational extension `p=min(l/4,(T-l)/4)`. If `x=a+Re(t)` and `|Im(t)|<=Y`, then

`Re(1/(a+t)) >= min(x_low/(x_low^2+Y^2), x_high/(x_high^2+Y^2))`.

The derivative in x changes sign only at a maximum. Summing the two reciprocal lower bounds and dividing by two gives a strictly positive sigma bound over the entire padded product. Exact tests verify this geometry. This proof is not permission to discard parts of a computed Arb ball; safe image intersection would need a separately implemented outward inclusion step.

## Transform option, not yet implemented

A log-coordinate map could compact the dynamic range: `t=2^x,u=2^y`, with exact transformed integrand `(log 2)^2 * 2^(x+y) * F(2^x,2^y)` on `[-8,192]^2`. The change of variables is exact. A complex strip with `|Im(x)|,|Im(y)|<pi/(2 log 2)` maps into positive real parts, and all old whole-box checks still apply to the transformed images. This may control multiplicative scale better than a linear monolith, but it adds a Jacobian and an analytic adapter requiring new source binding/native verification. It is not included in the present worker. First obtain the two compact-pilot observations before selecting a transform or a broad tile campaign.

Remaining feasibility is measured work, not an absence of a formal finite-domain theorem. Neither the small pilot nor the endpoint-only result establishes a usable full primitive, final D enclosure or frozen decision certificate.
