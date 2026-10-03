# Uniform enclosure availability is distinct from final accuracy

This is the independent mathematical contract for the additive `range_native_driver` correction. Its motivation is the actual diagnostic receipt: 73 finite, FLINT-success uniform inner results were rejected only because their component radii exceeded `2^20`. No outer analytic preflight was reached. This note does not claim that the proposed correction will make the physical tile converge.

## Validity argument

Let `H(y)=integral_[a,b] G(x,y) dx`, where G is the unchanged transformed physical integrand. For the entire outer parameter box Y, the inner quadrature, its node evaluations, and its analytic truncation bound all retain Y. Conditional on the existing whole-box domain/holomorphy premises and outward backend operations, a finite successful inner integration returns a ball B with

`{H(y): y in Y} subset B`.

There is no mathematical requirement that B's radius be below the arbitrary intermediate `2^20` cap in order for this inclusion to be useful as an outer callback value. A large valid ball is a valid range enclosure. Its uncertainty must remain in the value delivered to the outer quadrature, rather than being removed, clipped, centered, or silently subtracted.

More explicitly, fix any `y in Y`. Every inner callback ball at an inner node or trial box X contains the corresponding `G(X,y)`, since it was evaluated with the complete Y. Each accepted inner Gauss-Legendre panel uses a complex-domain magnitude bound valid for every y in Y, so its analytic truncation bound is also uniform in y. Outward weighted sums of the complete node balls, followed by addition of that uniform truncation ball, enclose the exact panel integral for this fixed y. The same is true for direct range panels. Finite outward panel addition therefore encloses H(y) for every y in Y. Interval arithmetic may allow independent choices of y at different nodes, producing a larger Minkowski sum; that loses correlation and sharpness, but cannot exclude the common-y integral. The adaptively chosen partition is common to the whole call, and every one of its accepted panels has the same uniform inclusion property.

For outer order0, FLINT requires this complete range/value enclosure. For outer order1 it additionally requires holomorphy in Y. The unchanged preflight and callback branch guards establish joint holomorphy on the relevant product neighborhoods; uniform compact integration then makes H holomorphic. A wide enclosure is still a valid upper magnitude bound for the outer Cauchy/Gauss-Legendre argument. No new order1 assertion is inferred from the width or from FLINT's success code alone.

FLINT's outer direct range estimate multiplies that complete B by its panel length. Its Gauss-Legendre method uses complete point-node enclosures and an order-1 analytic magnitude bound. Both operations propagate the full uncertainty. The unchanged outer final radius gate still determines whether the final compact integral meets `2^-52` for the designated tile. Therefore delivering a wider **intermediate** uniform enclosure does not relax the final error criterion or lose rigor; it merely avoids replacing valid information by an indeterminate value before the outer method can use it.

The tight point-inner gate remains useful for obtaining accurate node values, but it does not by itself prove the final `2^-52` bound. That bound is certified only when the full outer enclosure, including point-evaluation uncertainty, parameter radii, truncation and arithmetic rounding, passes the existing achieved component-radius gate **and** its exact serialized endpoint halfwidth passes the driver's `2^-52` check. A failure of either final check remains a rejected primitive.

The observed failure arose because such indeterminate outer ranges received infinite error in FLINT's heap. They were repeatedly selected before finite panels. The outer queue reached its fixed limit without any analytic outer trial. Returning the actual finite enclosures removes this artificial source of infinite heap entries. Actual widths may still be too large for useful quadrature, and the same finite resources may still be exhausted.

## Exact scope of the correction

Introduce a distinct internal status such as `ENCLOSURE_AVAILABLE`, meaning only: the whole-parameter result is finite, the underlying FLINT invocation succeeded, its original domain/holomorphy contract was respected, and no shared budget stopped. Its `achieved_radius_accepted` flag must remain false. This status must not be reported as `RADIUS_MET` or a completed scientific primitive.

Only the branch that already selects the **uniform-inner** plan may return this internal status for a radius above the previous intermediate cap. The outer callback may consume it as a finite function-value enclosure. The following remain unchanged:

- Tight point-inner returned-radius checks, including tiny but nonzero outer node radii that select the point plan.
- The top-level final returned-radius gate, its explicit success status and all serialized interval checks.
- Physical input, signed107 terms, coordinate map/Jacobian, principal branches and all whole-box guards.
- The existing outer analytic preflight. This correction does not implement segmented preflight.
- Uniform requested absolute tolerance `2^20`, relative goal64, precision128, task/window, integration/evaluation/panel/degree/memory/wall limits.
- Fatal contract/resource/exception behavior. No FLINT nonconvergence or nonfinite result is promoted to an available enclosure.

The status separation is essential: range availability and final accuracy are different contracts. Increasing `2^20` to an arbitrary larger threshold would obscure that distinction and introduce another scale-dependent obstacle. Accepting a finite range with its full outward uncertainty expresses the actual mathematical requirement directly.

## Required narrow verification

The additive implementation should verify that a finite successful **wide uniform** result receives the new internal status, while the same overwide result under a point or final-accuracy contract remains rejected. Resource stops and nonfinite/unsuccessful FLINT returns remain failures. A synthetic analytic integral should still contain its exact oracle, with all final gates intact. The existing actual failed tile may then be run once with the same precision, target radius and resource caps; its source/build identity is new, and its outcome must be recorded whether it succeeds or fails.

No successful partial tile, synthetic oracle or wide intermediate ball establishes full W1/W3 coverage, a global endpoint composition, normalization, final D/epsilon/gap certification or NCP production admission.
