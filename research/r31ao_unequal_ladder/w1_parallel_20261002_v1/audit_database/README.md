# Additive W1 audit snapshot

`build_w1_db.py` opens the pinned prior wide-domain SQLite read-only, copies it
with SQLite's backup API, and appends only `w1_*` tables. Every inherited table,
index, view and trigger is compared by logical contents/schema after the append.
The prior database's byte SHA is checked before and after. The generated SQL is
restored locally and compared by logical SHA, integrity check and foreign keys.

The output directory is create-only and must be outside both source trees.
A failed output is retained for inspection. Complete the continuation's source
files, reviews, report and `PUBLICATION_CONTENTS.json` before calling the builder.
Adding or changing a source file afterwards invalidates the snapshot and requires
a new output directory. Cache folders and `.pyc` files are excluded explicitly.

## Inputs

`RECOVERY_INVENTORY.json` must identify base commit
`957714bff2d6c97cc5b3541baa3f2f83fdfa3182`.

`STAGE_DELTA.json` uses schema `WU088_W1_PARALLEL_STAGE_DELTA_V1` and includes
`base_commit`, `original_prompt_sha256`, `prior_database_sha256`, and `stages`.
G0 through G9 must occur exactly once. Each stage supplies `id`, `prior_status`,
`current_status`, `scope`, `remaining_gates`, and nonempty `evidence`. Previous
labels must match both the pinned prior JSON and its SQLite table.

Each evidence reference is `{namespace, path, sha256}`. Namespace `continuation`
means this new source tree; `prior` means `wide_domain_20261001_v1`. Paths are
canonical relative POSIX paths, and the file bytes must match the declared SHA.

`EXECUTION_LEDGER.json` uses schema
`WU088_W1_PARALLEL_EXECUTION_LEDGER_V1`, the same three identity fields, and
`records`. Each record contains:

- `record_id`, nonempty unique text;
- `kind`: `ACTUAL_NATIVE_INVOCATION` or `REUSED_ACCEPTED_RECEIPT`;
- `tile_id`, nonempty text, and `primitive_index`, integer zero;
- `accepted`, a Boolean, `native_execution_observed`, exactly true;
- `receipt`, an evidence reference, and `status`, nonempty observed text;
- optional nonnegative integer `evaluations`, `integration_calls`, `elapsed_wall_ns`.

Actual invocations must refer to continuation receipts. Reused receipts must
refer to prior accepted results. Receipt SHA values are unique across both kinds
to prevent counting one receipt twice. A receipt SHA already recorded in the
prior artifact tables cannot count as new, even when copied into the continuation.
A reused receipt's path and SHA must be present in the pinned prior snapshot.
Ledger acceptance, native observation,
index, status and supplied counters are checked against the referenced receipt.
Rejected driver receipts may carry the native status/counters in `native_stdout`;
otherwise the recorded rejection `reason` supplies the status. This preserves
failures without manufacturing accepted output.

Optional `host_events` is a list of declared event objects. Launch refusal and
host-only events belong there or in separate artifacts; they are not native
invocations. Optional `counts`, if supplied, must equal all five computed fields:
`actual_native_invocations`, `accepted_current_invocations`,
`rejected_current_invocations`, `reused_accepted_receipts`, and
`host_events_not_invocations`.

## Boundary of the evidence

This builder does not launch HH, validate native numerical enclosures, or infer
scientific admission. The source-bound runner and independent review are the
authority for those claims. All new regular files are inventoried, but only
explicit stage/receipt references become relational links. Prior tables are
preserved without recursively expanding their SHA references.

The SQL restore check is local. It does not mean a Google Drive or Dropbox restore
was performed. Upload/readback verification belongs in the detached delivery
receipt, outside this snapshot to avoid self-reference.

## Invocation

```bash
python -B build_w1_db.py \
  --root /absolute/path/to/w1_parallel_20261002_v1 \
  --prior /absolute/path/to/wide_domain_20261001_v1 \
  --prior-db /absolute/path/to/wide_domain_audit.sqlite \
  --prompt /absolute/path/to/ORIGINAL_USER_RESEARCH_PROMPT.txt \
  --output /absolute/path/to/new-output-directory
```

Output: `w1_parallel_audit.sqlite`, its SQL dump, a local restored SQLite,
`W1_SOURCE_MAP.json`, and `W1_DB_VERIFICATION.json`. The SQLite and SQL both
retain the inherited audit tables. The restored SQLite need not be packaged a
second time. The builder rejects a database larger than 32 MiB and retains the
failed output for inspection. The verification file records exact output sizes.

Focused test command: `python -B test_w1_db.py`. Tests use small synthetic storage
fixtures and never run a scientific kernel.
