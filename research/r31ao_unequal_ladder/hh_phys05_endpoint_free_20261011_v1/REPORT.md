# PHYS05 endpoint-free local components

The new checker uses the frozen PHYS04 selected source and read-only owner
interval_rhs. It computes exact rational remap and reduced-photo component
identities. Its independent sparse polynomial ring and PHYS04 D2 quotient
arithmetic use different multiplication/derivative paths.

The signed directions span all four gas and 25 photon coordinates. Inactive
photon directions give zero photo response in this source's active quotient.
Both signs remain legitimate tangent directions at zero stock; they are not
asserted to be realizable finite negative photon populations.

The direct formal BE substitutions are finite time-series algebra. Transport
on/off isolates the remap term. Separate nonzero polynomial gas-only jets
check the isolation's cancellation; these are algebraic witnesses, not numerical
evaluations of FT03 or the HH physical coefficient. Source-exact K, opacity,
energy weights and the stored binary64 leaves are retained.

The conditional propagation equation and named FT03/HH Hessians are recorded
in CONTRACT.md. No actual endpoint, W, nonlinear root, tube, finite mixed
remainder, history or continuum claim follows from these identities.

Execution result, complete arrays and exact residuals are in
EXACT_CHECK_FIRST.json; original stdout/stderr are check_first.stdout and
check_first.stderr. A first failure, if any, is preserved as FIRST_FAILURE.json.
Independent Astra review approved PASS_SCOPED for these endpoint-free exact
component identities; its scope and remaining HOLD items are in REVIEW.json.

All six excluded execution counters (native, root, IVP, history, atomic,
old-suite) remain zero. No source file, PHYS04 artifact, original checkout,
commit or remote state is changed. HARNESS_UNAVAILABLE is recorded in CONTRACT.md.
