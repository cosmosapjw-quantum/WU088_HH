# G6 synthetic exact range integration

From the containing loop directory:

```sh
python -B -m unittest interior_pilot.test_interior -v
python -B -m interior_pilot.run_synthetic_pilot
```

The second command runs only nine explicit toy cases, never a supplied HH
dataset or callback. The general library entry point is
`integrate_range(callback, integration_box, parameter_box, *, caps=..., budget=...)`.
Supply one shared `Budget` to all nested calls so evaluation/panel/state/time
caps include inner work. Inputs and enclosure arithmetic are exact integers or
`fractions.Fraction`; host floats appear only in clocks and reported timings.

Every callback must return `RangeClaim(enclosure, integration_box,
parameter_box, uniform=True, proof_reference=...)` for the full requested
Cartesian product. Mismatched boxes and explicitly midpoint-only results are
rejected. This validates a callback contract, not the mathematical truth of an
arbitrary callback declaration. The proof of the three provided toy callbacks
is in `INTERIOR_PILOT_REPORT.md`; scientific callbacks need their own admission.

`TARGET_WIDTH_MET` means the achieved full complex rectangle image width meets
the requested width. For a nonzero-width parameter rectangle, this includes
the unavoidable parameter image width; it is not automatically an integration
error radius. `CERTIFICATE_INCONCLUSIVE_WIDTH` records a valid but unresolved
width. Resource exhaustion may return a previously complete valid enclosure
with `CERTIFICATE_INCONCLUSIVE_RESOURCE_LIMIT`. Domain/contract/implementation
failures return no accepted enclosure.

The max-memory policy limits an accounted state estimate, not process RSS.
`tracemalloc` measures Python allocation peak during each measured case but is
also not RSS. Callback temporaries and native allocation cannot be bounded by
this estimate. Requesting a hard memory cap is rejected. Wall guards operate
before/after callbacks; an in-flight callback cannot be interrupted. The HH
host runner must supply admitted process limits if hard caps are required.

The primary FLINT/Arb + Petras route has not been built/run here. The simple
range-sum algorithm is an auxiliary verified integration mechanism, not proof
that it will be efficient for HH. B05 actual-HH feasibility stays `UNMEASURED`.
