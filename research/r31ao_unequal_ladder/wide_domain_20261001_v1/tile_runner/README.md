# Fixed sequential log-tile pilot and raw-receipt normalizer

This thin adapter is pinned to the existing cached log driver, actual compiled
build, collector, and Frozen107 input. It does not compile, launch MPI, retry,
resume, change tolerance, add an endpoint, or authorize arbitrary commands.
`prepare` is read-only scientific work: it validates the original physical plan
and current source/binary/backend identities and writes exact local native plans.
`run` executes these plans sequentially and stops on the first rejection.

```bash
python -B runner.py prepare --global-plan /absolute/W1_PLAN.json \
  --global-plan-sha256 ORIGINAL_PHYSICAL_PLAN_SHA --task-index 0 \
  --output-dir /absolute/new_tile_pilot
python -B runner.py run --prepared-dir /absolute/new_tile_pilot \
  --prepared-sha256 PREPARED_MANIFEST_SHA
```

The output directory and every result are create-only. An existing run start,
result, or claim blocks another execution. There is no automatic continuation
after a crash or failed tile. W1 with log step 3 has 16 tiles, each requiring
component radius `2^-52`, so their exact rectangle sum must meet `2^-48`.
Precision is 128 bits. Each native call keeps 20,000 dispatched evaluations,
1,024 nested calls, 30-second cooperative wall limit, 35-second external limit,
and 1 GiB address-space limit. At most 320,000 evaluations and 560 seconds of
native process hard caps are admitted. Python validation and plan-generation
overhead is explicitly outside that sum. Only one native process runs at once.

`normalize` is also read-only scientific work:

```bash
python -B runner.py normalize --prepared-dir /absolute/prepared \
  --prepared-sha256 PREPARED_MANIFEST_SHA --tile-id 0 \
  --raw-receipt /absolute/existing_native_result.json --output /absolute/new_normalized.json
```

It first validates the original global physical plan, regenerated tile geometry,
exact local native plan, raw receipt selfhash, native result schema and achieved
radius, and complete wrapper. The wrapper must match the actual build, source,
binary, backend linkage, command, exact physical/log windows, limits and fixed
input. The current runtime bytes are checked, including actual `ldd` linkage.
The existing source-bound native output contract remains conditional; no claim
of independently replayed HH integration or cryptographic authenticity is made.
The raw stdout/stderr digest fields are checked as canonical hashes; the old
wrapper retained these hashes rather than separate successful stdout files.

The normalized record binds three different plan identities: the original
physical endpoint plan, the collector's tiling plan, and the local native plan.
`validator_source_sha256` is this file's complete byte SHA, whose literal pins
bind the collector, log driver, fixed build and input. Raw receipt SHA binds the
entire preserved file. Exact dyadic lower and upper endpoints pass to the
collector without a float conversion. Collection occurs only after every tile
passes; no missing tile is replaced with zero. Endpoint, normalization, final D,
full-domain and production admission remain false.

Verification uses the already executed LOG2_CENTRAL receipt read-only for a
one-tile complete collection, adversarial self-resealed wrapper changes, exact
W1/W3 caps, create-only preparation/claims, and mocked sequential partial
failure. These tests launch no HH integral and report no new native HH run.
