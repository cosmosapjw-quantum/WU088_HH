# Exact finite tile planning and collection

This component implements finite exact Cartesian coverage and exact dyadic
rectangle addition for one compact physical primitive. It launches no worker,
performs no HH callback evaluation, and adds no endpoint bound. Its output is a
new `WU088_EXACT_TILED_COMPACT_INTERIOR_V1` record; it is not an old primitive-join
receipt and cannot automatically enter the old assembly admission path.

## API and authority boundary

```python
geometry = plan_grid(global_window, index, global_radius_exp,
                     max_log_step=3, max_tiles=16)
plan = bind_plan(geometry,
    global_endpoint_plan_sha256=original_physical_endpoint_plan_hash,
    archive_sha256=input_archive_hash,
    input_record_sha256=canonical_input_record_hash,
    build_manifest_sha256=native_build_manifest_hash,
    build_source_sha256=native_build_source_hash,
    validator_source_sha256=upstream_native_validator_source_hash)
result = collect(plan, validatedtiles)
```

`global_window` has exactly `l_t,T_t,l_u,T_u` with canonical positive rational
strings that are exact powers of two. Their reduced numerator and denominator
are limited to 512 bits. Primitive indices are 0 through 2591. Precision is
fixed at 128 bits. Global radius exponents are integer -1024 through 0; the
derived per-tile exponent must also lie in the native supported range. The
current pilot uses global exponent **-48**. The integer log step is 1 through 8,
default 3, and the execution count cap is 1 through 16. Exceeding the cap refuses
the plan; no execution instructions are returned for a larger campaign.

`global_endpoint_plan_sha256` identifies the original physical global-window
endpoint plan. It is distinct from the collector's `plan_sha256` (which binds
the grid plus the six authority identities), and from each local native tile
plan SHA. Keeping all three identities prevents their later accidental conflation.

The caller must first validate each original native receipt with the pinned
upstream validator and all required raw file, input, local plan, build, source,
native result, precision, resource and status bindings. The caller must also
verify that the local native plan's physical window is exactly this tile and
that its requested tolerance is the derived tile tolerance. The normalization
step retains those verified identities. A SHA string or a self-consistent
normalized envelope alone is **not** proof that those external checks occurred.
This collector does not independently authenticate raw native evidence.

Each normalized record has exactly the fields constructed in the clearly
synthetic `fixtures()` in `test_collector.py`: schema, tile ID, primitive index,
global collector plan SHA, physical window, requested radius exponent,
128-bit precision, `RADIUS_MET`, `accepted=true`, endpoint and normalization
flags false, the six bindings, local `native_plan_sha256`, whole raw
`native_receipt_sha256`, `rectangle`, `reported_radius`, and `record_sha256`.
Each rectangle component has canonical exact dyadic strings `lower,upper`;
`reported_radius` is its exact serialized halfwidth, not an internal native
radius copied before endpoint serialization. The native mantissa/exponent
format must be converted by exact integer/rational operations. Each input
numerator and denominator is limited to 8192 bits.

`seal_normalized_record(record)` adds only an integrity digest of the canonical
JSON envelope. It does not confer validation authority. The six plan bindings
must come from the caller's already verified records, not be inferred from the
first tile. This is a trusted-normalization interface, not a standalone native
receipt validator.

## Exact coverage and error budget

The planner uses strictly increasing integer log-axis breakpoints, preserving
the exact two endpoints and a final shorter interval if needed. Physical
coordinates are exact powers of two. The Cartesian tiles therefore have
disjoint interiors and cover the compact window; shared edges have zero area.
The collector regenerates this geometry and rejects altered, missing,
duplicated, swapped or out-of-window coordinates and duplicate raw receipts.
Matching counts alone is insufficient. Every tile binds the same primitive,
archive, canonical input record, source, build and validator.

For N tiles and global component radius `2^E`, every tile must request and meet
`2^(E-ceil(log2(N)))`. Lower and upper serialized dyadic endpoints are added
separately with `Fraction`, so the sum adds no rounding error. Every reported
tile halfwidth must agree exactly with its serialized interval, and the exact
sum halfwidth is checked again against `2^E`. The complete expected tile set
must pass before any compact-interior result is returned. Failure is never
replaced by a zero contribution.

For W1 `[1/16,256]^2`, the default step gives **16 tiles**, each requested at
radius `2^-52` for global `2^-48`. W3 `[2^-8,2^192]^2` exceeds this pilot cap;
this component refuses that execution plan. Smaller log spans can reduce wide
exponential image enclosure failures, but do not prove that any HH tile will
converge. The original complex-box guards and all native resource caps remain
binding. See `../log_review/MATHEMATICAL_CONTRACT.md` for the transform and
uniform nested enclosure premises.

The original global endpoint disk may be composed exactly once **after** all
compact tiles are accepted, with its original global-window plan identity.
That operation is not implemented here. Normalization, final D/epsilon/gap,
full-domain integral and production admission remain false.

## Verification

Run `python -B -m unittest -v test_collector` in this directory. The 17 unit
tests use independent closed antiderivatives for real `F(t,u)=t+2u` and imaginary
`F(t,u)=tu`. Their 16 exact tile intervals sum to the independently evaluated
global primitive, with deliberately saturated global radius `2^-48`. The
fixtures are synthetic and source identities are synthetic hashes; they are
not HH native receipts. Adversarial tests cover geometry, duplicate/missing
tiles, source and global endpoint-plan mismatch, corrupt envelopes, reported
radius mismatch, overwidth, precision/tolerance/status changes, and unsupported
geometry or values. No native worker, MPI process or scientific integral is run.
