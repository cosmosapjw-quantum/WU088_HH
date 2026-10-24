# PHYS88 static implementation and prescribed dispatch

Authority is frozen CONTRACT revision3, `theory/ATOMIC_BARE_REMAP_KO.md`, and
`theory/POSITIVE_BRANCH_CLOSURE_KO.md`. Exact nominal arithmetic does not make
the displayed masses physical exact quantities. Kernel transport is an explicit
conditional model. Empirical charge-state equivalence, physical covariance,
source-window tails, a named consumer and production remain OPEN.

## Source and implementation mapping

`source/atomic_bare_remap.py` implements the displayed mass-convention identities,
two monotone maps, original-native-Es source composition, new bare thermal
integrals, centered variances/covariances and the disjoint owner ledger. Its
`relabel_event` retains source neutron/photon and H/D velocities and computes
`C=DeltaH*UH-DeltaD*UD` directly. Its separate `bare_event` reconstructs the bare
incoming pair at mapped target-rest LAB energy, boosts both outgoing COM vectors
with that pair and the same prescribed normal boost, and adds no carrier.
The contract's positive S4, mass-shell, carrier-absolute and roundtrip scales are
fixed in code before results. Exact represented endpoints retain their endpoint
labels; out-of-support inputs are refused, never clipped or zero-extended.

The original PHYS87 module is an exact vendor copy. The new module imports only
`NativeSource` and `ScaledBesselSix`; no parent integrator, positivity callback,
runner or historical campaign is called. The saved exact positivity witness and
PHYS87 primary baseline are copied unchanged and reused by identity. The new
integrator samples native Es inside the original152cells and never applies old
INT flags to mapped Eb knots. Cross sections receive no source-coordinate
Jacobian; the integral carries only its declared dKb/dlogEs.

`source/run_primary.py` writes one create-only `results/primary001` directory:
RESULT, four CSVs, ATTEMPT and an output byte manifest. It records16full and4FD
integrals,18relabel events,36bare events,32adopted owner rows, individual residuals,
guards and every failed check. Runtime exceptions preserve partial observations
and integration-call records in FAILURE.json. Parent153positiveknots/152convex
cells are reused witnesses, not new assertions or a repeated positivity campaign.
The `--resume` path uses standard-library hashes/JSON only, imports no scientific
or source module, verifies the complete output set and returns SKIP with zero
scientific callbacks/integrations/rewrites. The output path is fixed so choosing
a new directory cannot silently relaunch this completed identity.

`verification/independent_reference.py` has its own raw ENDF parser and cell
interpolation. Its parser construction is statically reused from the independent
PHYS87 reference; no old reference is executed. For both maps at1e8K it uses
SciPy kve and adaptive quad in x=Es/theta, independently reducing
lambda/(4a²b²)=Eb(2a+Eb)/a² and retaining explicit dKb/dEs. It compares8positive
rate/mean fields using the frozen reference denominator and tolerance, records
actual callbacks/quad cells/error estimates and preserves partial failures.
It imports no production module. It does not independently validate low-T
variance or claim a rigorous global quadrature/physical uncertainty bound.

`source/plot_saved_results.py` renders2PNG+2PDF only from the saved primary JSON,
including the saved PHYS87 baseline. Native knots and four-temperature connecting
lines are visual guides; map differences are not uncertainty bands. Exclude the
renderer-created `.mpl_config` directory from publication.

## Frozen dispatch and resource mechanics

Concrete argv arrays and shell renderings are in
`implementation/EXECUTION_COMMANDS.json`. These are preparations, not execution
authorization. Root dispatches primary, its successful read-only resume, then
reference and figures separately after the applicable publication/ACK and review.
Only the reference argument `__ACTUAL_PRIMARY_RESULT_SHA256__` is replaced with
the actual successful RESULT hash. No automatic retry is available.

The wrapper uses the unchanged full PHYS78 shared gate, SHA
`76ff57ba687fd9830b84c3fcff69eb8ed0e9f6ceab4551e61c67c84d3ea65124`.
Every child requires a fresh own lease, uncontested available CPU0/CPU8 mapping,
one worker/thread and actual available memory at least1.5GiB reserve+0.5GiB job.
The wrapper returns WAIT without a child when resources are unavailable. Caps
are primary24CPU/60wall, reference30CPU/60wall, figures8CPU/30wall. A separate
create-only admission receipt is written after actual acquisition/fresh memory
and coordinator pinning, before the child. The final receipt retains raw stdout,
stderr, original/post-acquisition gate observations, resource costs, caps, affinity
and own-lease release. No peer is killed and no cache credit is used.

`implementation/freeze_implementation.py` mechanically reproduces the runner's
canonical identity using AST literal extraction and file hashes without importing
the runner or candidate. It saves create-only identity, commands, final static
syntax receipt and manifest. AST/code-object compilation is not numerical testing.

All scientific admission belongs to fresh Astra review and root. This preparation
performs no numerical imports, source evaluations, integrations, tests, lease
acquisition, CAS calls, Git publication or backup operations. Historical budgets
and failures stay separate; HH_R10 remains OFF, production NOT_ISSUED.
