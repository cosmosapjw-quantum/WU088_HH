# Pinned FLINT 3.4.0 Petras host draft

`petras_host.hpp/.cpp` implements the missing integration caller around
`acb_calc_integrate` and the G4 `wu088::Slice`/`slice_callback` interface.
The source is a **native draft with static checks only**: no native compilation,
linking, synthetic executable run, or actual HH evaluation occurred here.
Python Fraction pilot measurements do not verify this native implementation.

## Numerical contract

`integrate_1d` initializes FLINT options explicitly: degree, per-call evaluation,
queued-panel limit (`depth_limit` in this FLINT release), heap selection, and
working precision. Relative and absolute tolerances are requests. Acceptance
requires `ARB_CALC_SUCCESS`, a finite returned ball, and both actual component
radii no larger than the declared acceptance cap. A nonconvergent, resource-
limited, or invalid result returns nonfinite output. For a finite-but-too-wide
result the output is also refused, but `Report.real_radius_dump` and
`imag_radius_dump` preserve the exact FLINT `mag_dump_str` radius bounds for
diagnosis. These are rectangle component radii, not a circular complex radius.

Endpoints must be finite, real, and exact in Acb, so this interface supports
exactly representable **dyadic endpoint choices**. Use these same exact values
for G5 tails. Do not replace a non-dyadic rational such as 1/3 by its midpoint
approximation or silently change an existing endpoint contract.

`integrate_nested_2d` passes each outer Acb box, including both component radii,
unchanged into all inner evaluations. The inner contract must be uniform over
the entire outer parameter box. When either outer or inner integration asks
for analytic order 1, the bivariate callback is asked for joint holomorphic
evaluation. G4 field binding makes a fresh Slice and assigns the complete
`outer_box`; no midpoint accessor appears in the wrapper. The supplied
`Bivariate` proof flags and reference are caller authority declarations,
not a proof checker. Actual HH adoption requires G1/G4 premises to be admitted.

The parameter image itself can have nonzero width. Consequently, a tight
point-evaluation tolerance cannot always be met for a broad outer complex box.
The plan has separate `uniform_inner` and `point_inner` policies. Order 1 or
an input box above the declared radius threshold uses the uniform policy;
tight quadrature-node boxes use the point policy. Both return full uniform
enclosures and must pass their actual returned-radius caps. This selector is
an algorithm policy; it makes no assumed Lipschitz or source-error estimate.
The broad synthetic default cap 2^20 is not an HH epsilon or scientific budget.

Analytic trial boxes may cross the callback's domain. They return nonfinite
bounds so Petras may try smaller domains. For an outer order-1 trial, an initial
whole-inner-path/whole-outer-box query refuses an invalid domain before starting
an inner adaptive loop. Such domain, width, or nonconvergence trial refusals are
nonsticky. Actual outer order-0 domain failure, contract failure, or shared
resource exhaustion stays sticky. The extra native fixture tests that a refused
outer analytic trial does not prevent a subsequent valid trial; it is written
but **not executed** in this environment.

## Resource and build contract

One `SharedBudget` counts outer and inner callback entries, dispatched evaluator
calls, integration calls, active nesting, and analytic-box refusals. Dispatched
evaluator calls have a strict shared cap. FLINT may call the refusing shim again
after that cap: these entries are counted, return nonfinite, and never dispatch
the evaluator. FLINT's documented per-call `eval_limit` is only approximate.
Its `depth_limit` bounds queued intervals, not a strict local bisection depth.
Precision is fixed, capped at 4096 bits, and must match G4 Contract.precision.
FLINT internal threading must be one to avoid shared-state races.

The wall check is cooperative and cannot interrupt FLINT or a running callback.
This native wrapper does not claim a hard memory cap. Use the separate
`host_guard/run_guarded.py` after verifying the built binary and linked
libraries. That guard supplies a process-group timeout and per-process
RLIMIT_AS/CPU; it is not an aggregate process-tree RSS bound and does not grant
actual HH execution authorization.

Build only on the authorized host after backend provenance admission:

```sh
export WU088_BACKEND_PREFIX=/absolute/verified/backend
export WU088_BUILD_PROVENANCE=/absolute/verified/backend_provenance.json
export WU088_PETRAS_BUILD_OUT=/absolute/new/petras-synthetic-build
bash interior_pilot/build_petras_host.sh
```

The script checks FLINT 3.4.0, GMP 6.3.0, MPFR 4.2.2 and the existing G4
build-input verifier, builds the wrapper plus synthetic executable, and records
compiler/linkage/source/binary identities. It does not execute the binary.
Check the actual linked-library identities against provenance before running:

```sh
python -B host_guard/run_guarded.py --wall-seconds 60 --memory-mib 2048 \
  --output-dir /absolute/new/petras-synthetic-run -- \
  /absolute/new/petras-synthetic-build/native_petras_synthetic
```

The executable contains only ten polynomial/contract/refusal fixtures: exact
1/3 and 1/6 targets, uniform z/3 rational corners, midpoint-only refusal,
shared dispatch/nesting caps, nonfinite and width refusals, missing G4 Slice,
and nonsticky analytic trial rejection. It has no HH input loader. These host
commands are instructions for a later approved build/run and were not run here.

## Evidence scope

`evidence/PETRAS_API_PIN_CHECK.json` binds the FLINT source archive and actual
primary headers/docs/source files. Static checks verify API names/signature,
structure, source hashes and shell syntax; they do not replace compilation or
runtime validation. Initial missing-wrapper RED and review RED evidence are
retained. Review P01 is the nested analytic-trial refusal defect, P02 the
too-strong interval-in-interval fixture assertion (replaced by exact rational
corners), and P03 the missing actual-radius diagnostics. Source repairs do not
close native runtime verification or B05. An API scanner false positive on a
C++ member initializer is also preserved and classified separately from a
library/API or numerical failure.
