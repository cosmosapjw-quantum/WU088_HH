# Observational diagnostic native driver

This additive directory copies the frozen log driver and the previously refined
Petras host. It adds observations without changing callback expressions, ordered
terms, coordinate map, source input, quadrature settings, refinement policy,
precision, error acceptance, or shared resource limits. The log-map header is
byte-identical to the frozen source. Existing drivers and historical sources
remain untouched. Extra recording has runtime overhead inside the same wall cap.

The build/run CLI is identical to `../log_native_driver/driver.py`; cached is the
default. Build schema is `WU088_LOG2_DIAGNOSTIC_NATIVE_DRIVER_BUILD_V1`, native
result schema `WU088_LOG2_DIAGNOSTIC_INTERIOR_RESULT_V1`. Source identity includes
the copied host, diagnostics header, worker, driver, and log map. Normal failure
receipts still retain native JSON in `native_stdout`; accepted results include
the validated `diagnostics` object directly.

The intended next observation is exactly the previously failed tile
`[1/16,1/2]^2`, primitive 0, at unchanged 128 bits, radius `2^-52`, 20,000
dispatched evaluations, 1,024 integration calls, degree/queued limits 64,
30-second cooperative wall cap, external 35-second cap and 1 GiB address space.
This directory's owner did not execute any HH integral. Root coordinates the
single authorized actual diagnostic attempt and its interpretation.

`diagnostics.counters` distinguishes whole-inner-path analytic preflight refusal
from actual inner FLINT nonconvergence, achieved-radius refusal, nonfinite,
resource, and invalid-contract outcomes. It also counts outer request kinds and
whether their failures were refinable or fatal. `peak_active_integrations` is
the existing nesting level, not FLINT's internal subdivision depth.

`inner_outcomes` has dimensions `[3][2][6]` in this exact order:

| Axis | Index order |
|---|---|
| Outer request | order 0 exact; order 0 nonexact; order 1 |
| Selected inner policy | point; uniform |
| Inner return status | radius met; radius too wide; FLINT no convergence; nonfinite; resource limit; invalid contract |

Order-0 nonexact inputs can be tiny numerical-radius quadrature nodes. The name
`order0_range` means nonexact, and does not establish that the box is wide.
This is why selected policy and request kind are recorded separately. Preflight
refusal returns before an actual inner integration and is not counted as an
actual inner-call status in this matrix.

`failure_samples` keeps the first seven and latest outer failure, at most eight.
Each records request kind, selected precision/tolerances/relative goal, report
status/reason, and exact `arb_dump_str` outer real/imaginary balls. If an inner
FLINT call returned, `inner_return` captures status and finite real/imaginary
balls plus radii **before** the host invalidates a rejected result. These are
observations, never accepted enclosures. Preflight failures have no inner return.
Strings are bounded at 2,048 characters; a `truncated` flag explicitly marks
loss of full representation. No callback is reevaluated for diagnostics.

Verification: 23 Python boundary tests pass, including diagnostic schemas and
caps. The bounded native analytic suite passes nine checks, with exactly the
same 9,456 polynomial and 1,162 inverse-product dispatch counts as the frozen
log driver. The tests also observe preflight/fatal-resource counters and bounded
samples. The first diagnostic build's warning-as-error is retained in attempt
1; attempt 2 compiled and passed. These are component tests, with zero HH runs.
