# W3 endpoint-design audit append

This additive builder copies the pinned W1 audit SQLite with the SQLite backup API and appends only six `w3_` tables. It verifies every inherited table, schema object and row against the read-only predecessor, checks integrity and foreign keys, and restores its SQL dump into a second local SQLite database for exact logical comparison. Final output is create-only and must remain outside both source trees. The delivered SQLite must fit within 32 MiB.

## Explicit accounting boundary

Only `ACTUAL_ENDPOINT_SELECTION` and `ACTUAL_ENDPOINT_CROSSCHECK` may enter the new execution ledger. Both must declare primitive index 0, an actually observed worker, zero native integration invocations and a separate nonnegative integer candidate-polynomial evaluation count. Those fields are checked against the source-bound wrapper receipt. The receipt must bind a distinct current output file by SHA-256; old hashes recorded anywhere in the inherited artifact tables and duplicate output hashes cannot count as new operations. Historical W3 endpoints and W1 interiors are source references, not new executions. A failed result can be recorded with `accepted=false`; no scientific admission follows from an audit row.

Receipt shape required by the builder:

```json
{
  "kind": "ACTUAL_ENDPOINT_SELECTION",
  "primitive_index": 0,
  "accepted": true,
  "status": "SOURCE_BOUND_STATUS_FROM_EXECUTION",
  "native_integration_invocations": 0,
  "candidate_polynomial_evaluations": 5,
  "actual_worker_observed": true,
  "output": {
    "namespace": "continuation",
    "path": "runtime/SELECTION_RESULT.json",
    "sha256": "EXACT_64_CHARACTER_SHA256"
  }
}
```

The ledger repeats these scalar fields and adds `record_id` plus `receipt={namespace,path,sha256}`. The audit validates byte identities and explicit accounting, not the endpoint theorem, execution provenance authenticity, numerical correctness or interior integral. Those remain the responsibility of the root execution record and independent source/result review. In particular, a hash is not proof that a worker ran.

`STAGE_DELTA.json` must have exactly G0–G9 and each prior status must match both the pinned W1 JSON and its `w1_stage_delta` SQL row. All evidence uses explicit SHA-bound relative paths in `continuation` (this tree), `prior` (W1 tree), or `inherited` (common ladder parent, excluding aliases into the first two trees). Every path component must be nonsymlink, and namespace alias checks use resolved paths. The inherited namespace adds explicit currently read source evidence; it does not itself assert previous DB inclusion. Current files are inventoried once and checked again at completion; changing/adding a file requires a new create-only output directory.

## Invocation

Use `python -B build_w3_db.py --root NEW --prior W1 --prior-db PINNED_W1_DB --prompt ORIGINAL_PROMPT --output EXTERNAL_CREATE_ONLY_DIRECTORY` only after root has finalized this tree and `PUBLICATION_CONTENTS.json`.

Tests use small synthetic databases and records. They do not execute any HH kernel, endpoint evaluation, MPI operation or cloud restore. `W3_DB_VERIFICATION.json` is generated outside the source tree only after an actual final append and SQL restoration succeed; it must not be fabricated from the test result.
