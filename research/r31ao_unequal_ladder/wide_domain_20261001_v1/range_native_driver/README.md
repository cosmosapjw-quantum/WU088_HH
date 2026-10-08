# Finite uniform enclosures without an intermediate width cutoff

This additive driver corrects the measured heap starvation in the diagnostic
tile-0 attempt. It has a local host header and explicit `ENCLOSURE_AVAILABLE`
status. Existing log, diagnostic, and historical sources remain immutable.
Build/run CLI is unchanged. Native schema is `WU088_LOG2_RANGE_INTERIOR_RESULT_V1`
and build schema is `WU088_LOG2_RANGE_NATIVE_DRIVER_BUILD_V1`.

## Source-bound failure mechanism

The original failed tile had 125 outer order-0 calls: 52 returned a finite inner
enclosure and 73 were rejected solely by the uniform `2^20` achieved-radius
gate. The inner FLINT calls themselves returned success; no inner FLINT
nonconvergence occurred. There were zero outer analytic requests.

Pinned FLINT `acb_calc/integrate.c` attempts Gauss–Legendre only when the current
heap-top crude estimate is finite. Converting a valid, wide inner enclosure to
indeterminate assigns infinite error to that outer panel. Infinite-error panels
remain ahead of all finite panels. The 125 crude calls equal the initial call
plus two calls for each of 62 bisections. The queue reaches 63 panels, the
`depth_limit - 1` stop condition for the configured 64-panel limit. It contains
52 finite leaves and 11 infinite leaves. The finite leaves never reach the top
before this stop, so no outer analytic quadrature is attempted.

This identifies a control-flow obstruction caused by the intermediate gate.
It does not show that the physical integral diverges or that 128 bits are
intrinsically insufficient.

## Correction and enclosure argument

For a selected uniform-inner policy, a finite successful inner FLINT result is
a range enclosure of `H(y)=integral F(x,y) dx` over the complete outer parameter
ball. Its width includes genuine variation with `y`, which need not shrink as
inner quadrature is refined. Such a range enclosure is valid input to the outer
integrator even when it is wide. The outer algorithm propagates the full ball;
it does not replace the ball by its midpoint.

The new host therefore returns `ENCLOSURE_AVAILABLE`, with
`achieved_radius_accepted=false`, for selected-uniform finite results only after
FLINT success and all shared-budget/domain checks. The outer callback consumes
this status only when its selected policy is uniform, the result is finite,
FLINT succeeded and the budget remains live. The status is never accepted as a
top-level integral result.

Point-inner and final outer results retain their strict achieved-radius tests.
The complete complex-box guards, analytic preflight, exact exponential map,
callback terms/order, requested uniform absolute tolerance `2^20`, precision,
relative goal, resource limits and endpoint exclusion remain unchanged. The
change admits a valid range to the next quadrature stage; it does not assert
that this intermediate range meets a pointwise accuracy target.

The diagnostic matrix is now `[3][2][7]`: the six previous statuses retain their
indices and index 6 is `ENCLOSURE_AVAILABLE`. A matching counter records these
returns. Other diagnostic fields and bounded failure samples are unchanged.

## Meaningful regression and a separate policy finding

The analytic oracle is the entire polynomial `2^40*x*y` on `[1,2]^2`, whose exact
integral is `9*2^38`. Both old and corrected hosts use 128-bit arithmetic and
the same resource/error limits. In this focused high-amplitude fixture both use
relative goal 128, so the relative stopping threshold is sufficiently strict:

| Host | Dispatches | Integration calls | Outer analytic calls | Result |
|---|---:|---:|---:|---|
| Old width-gated host | 1375 | 126 | 0 | Nonconvergence; 119 inner-width refusals |
| Corrected host | 132 | 12 | 8 | Final radius `2^-52` met; exact oracle contained |

Nine uniform enclosures were consumed in the corrected regression. Separate
checks reject an overwide point result, nonfinite callback and unsuccessful
FLINT return. Twenty-four Python boundary tests pass, including refusal to
promote `ENCLOSURE_AVAILABLE` to top-level success.

The earlier goal-64 corrected fixture is retained. It reached eight outer
analytic calls but then correctly rejected an overwide **point-inner** result.
FLINT uses a threshold at least as large as the relative goal permits, so a
`2^40` amplitude with goal 64 can request much less accuracy than the independent
point-radius gate. Tightening the focused fixture to goal 128 did not change the
production default of 64. This is a separate stopping-policy issue to diagnose
in actual HH evidence, not a reason to weaken the final radius requirement.

No HH integral was executed by this component's owner. The root's first actual
comparison keeps the failed tile's identical 128/-52/goal-64 settings. A later
change of relative goal or precision must have its own explicit result/limits
identity. No full campaign, endpoint join or production admission is implied.
