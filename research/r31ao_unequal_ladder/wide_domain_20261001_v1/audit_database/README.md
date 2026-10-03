# Wide-domain continuation evidence index

`build_wide_domain_db.py` creates a separate SQLite/SQL snapshot after the current
continuation has stopped writing source and result files. It does no scientific
calculation, provider access, or stage promotion. Previous files are read only.

The fixed identity chain is:

- base commit `449dee7d05c9c055db04f0e7fa730bd4792a385c`;
- previous actual continuation SQLite SHA-256
  `98d9acd99222a0080118157ce1ec2e71bff9630d310bb594ffac05ad414abb71`;
- original prompt SHA-256
  `70071962a6b3dc3cfc0c01034c0d1b6f57711833957510a77b0bb6c4e453969e`;
- previous G0–G9 reconciliation SHA-256
  `575a7ad9e121d6c66d3c3614651c0a4baeb72d259f63ad389bf110893b03c609`.

All current regular files are indexed with exact size and SHA-256, excluding
`.git`, Python/pytest cache directories, and `.pyc`. Symlinks are refused. Every
JSON mapping with an explicit `status`, `STATUS`, `classification`, `exit_code`,
`returncode`, or `return_code` is preserved with its exact JSON pointer and fields.
Nested, aggregate, historical, planned, rejected, and test records can overlap.
**Row counts are database bookkeeping, never scientific execution counts.** A
filename or zero exit code does not set a scientific stage label.

Prior artifact identities are imported from the pinned SQLite with explicit
`MATCHES_PRIOR_DATABASE_RECORDED_IDENTITY` links. This does not claim that all old
payload bytes were reread. Explicit stage evidence instead requires current
regular-file bytes matching its declared SHA. Prior status labels must agree
between the prior SQLite and prior reconciliation JSON.

## Root-authored stage delta contract

Write `../STAGE_DELTA.json` only after reviewing the actual receipts:

```json
{
  "schema": "WU088_WIDE_DOMAIN_STAGE_DELTA_V1",
  "base_commit": "449dee7d05c9c055db04f0e7fa730bd4792a385c",
  "original_prompt_sha256": "70071962a6b3dc3cfc0c01034c0d1b6f57711833957510a77b0bb6c4e453969e",
  "stages": [
    {
      "id": "G0",
      "prior_status": "EXACT_PREVIOUS_CURRENT_STATUS",
      "current_status": "EXPLICIT_CURRENT_ASSESSMENT",
      "scope": "Bounded claim and its scope",
      "remaining_gates": ["Unresolved requirement"],
      "evidence": [
        {"namespace": "prior", "path": "audit_database/STAGE_RECONCILIATION.json", "sha256": "575a7ad9e121d6c66d3c3614651c0a4baeb72d259f63ad389bf110893b03c609"}
      ]
    }
  ]
}
```

The example is a schema illustration, not accepted evidence. Supply G0 through
G9 exactly once. Evidence namespaces are `continuation` (this continuation root)
and `prior` (`native_execution_20261001_v1`); paths are canonical relative POSIX
paths. At least one actual hash-bound evidence file is required per stage.

## Final snapshot command

From the continuation root, after the root coordinator freezes final records:

```bash
python -B audit_database/build_wide_domain_db.py \
  --prior-db /workspace/scratch/6cf5f59cd2d1/native_execution_intake/continuation_db_final/continuation_audit.sqlite \
  --output-root /workspace/scratch/6cf5f59cd2d1/wide_domain_intake/final_audit
```

The output directory must not exist and must be outside both source trees. Use
`--continuation-root`, `--prior-root`, and `--prompt` when restoring elsewhere.
The fixed hashes still apply. Failures preserve any partial new output; retry
with a new path. Do not replace an existing snapshot.

The builder validates SQLite integrity and foreign keys, restores the SQL into a
second SQLite, compares all logical rows/schema, and rechecks source bytes and
the current file set. Late evidence makes an old snapshot stale; rebuild to a
new output directory. The `verify_snapshot` Python function can explicitly test
an existing source map. No upload or restore-to-cloud status is claimed.

Focused contract verification:

```bash
python -B audit_database/test_wide_domain_db.py
```

Tests use actual pinned prior files and synthetic new receipts, exercising real
SQLite, SQL restoration, foreign-key enforcement, create-only behavior, source
mutation/late receipt detection, and invalid lineage/stage rejection. They do
not execute the HH solver or create the final delivery database.
