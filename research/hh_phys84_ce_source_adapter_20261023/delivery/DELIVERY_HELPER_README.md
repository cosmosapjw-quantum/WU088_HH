# PHYS84 delivery recovery helper

This helper is explicitly **REIMPLEMENTED_AFTER_WORKSPACE_LOSS**. Its identity is new. No match to the lost helper SHA256 is asserted. The original S0 ZIP (8,496,264 bytes, SHA256 `b655b5bc5b6d7f2fb0032d138f3e81e5329ec0df4b15f4c4a1818e69526df255`) is unavailable and was not uploaded. Its original 51 private intake files are unavailable. The new `S0_RECOVERY` archive exports the exact recovered S0 Git unit with currently available evidence and the two unchanged PHYS83 recovery pins; it is a distinct archive with a new SHA256.

`delivery.py` uses only the Python standard library and read-only Git commands. No scientific imports or callbacks occur. Syntax is checked with `ast.parse`; no tests or scientific computations are run.

## Archive structure and checks

Repository payloads are only tracked regular blobs under `research/hh_phys84_ce_source_adapter_20261023/` at the explicit full commit SHA. `git ls-tree` and `git cat-file` supply paths/modes/blobs/content. Raw commit headers supply actual parents, including at shallow boundaries. S0 and S0_RECOVERY require parent `6a2fc5aacb6182a916b9434c316e99e750e8273c`. Worktree/untracked files are never repository payloads.

Private evidence comes only from the explicitly supplied intake directory and is placed under `private_evidence/wu84_intake/`. Symlinks are rejected; `.git`, `__pycache__`, `.pyc`, and `.pyo` are excluded. `wu84_recovery_requests.json` is forbidden. Private single-use download requests must stay under `/tmp`, outside intake. Do not put private URLs or credentials in intake.

`parent_recovery/` contains the raw pinned PHYS83 ZIP (7,473,461 bytes, SHA256 `65f8969ec76e1971374f34638a8a9821f96bf9fcd52238a6600fb7e7c8c52d3a`) and delivery JSON (868,689 bytes, SHA256 `789c627dcf54fe54038ac6bc59ee7d188939981f645df7bfa7364d30fe4ae772`). Nested parent verification checks these outer raw bytes only; historical dual restoration evidence is reused separately.

`BYTE_MANIFEST.json` binds selected commit/tree/parents, actual local HEAD observed at pack time, stage, optional science identity, recovery provenance, and every payload filename/bytes/SHA256/kind, plus Git blob SHA1 and regular-file mode for repository files. The manifest does not list itself.

All outputs are create-only. Writes complete through write-all loops (or explicit ZIP-member write loops), fsync, close, reopen, and byte/hash checks. Unsafe/absolute/traversal/duplicate paths, nonregular ZIP members, encrypted members, and file/directory collisions fail closed. ZIP parsing uses immutable copies of the fully hashed input bytes. Restore extracts real regular files into a new output directory, checks every ZIP member's full CRC in both archives, every payload's hash/size, repository blobs against the supplied fresh Git manifest, actual extraction, Git mode, and reopened file bytes/hash. Counts must close before PASS.

## Fresh Git manifest

After the owner independently fetches the actual remote commit, generate a manifest. This command does not fetch or change Git; remote freshness remains the owner's separate receipt.

```bash
python /workspace/scratch/ebcaaaa20861/wu84_delivery_tools/delivery.py git-manifest \
  --repo /workspace/scratch/ebcaaaa20861/WU088_HH \
  --commit ce14c0bfc0318662673b021a08f4029d6a36c7a7 \
  --output /workspace/scratch/ebcaaaa20861/wu84_delivery/S0_RECOVERY_FRESH_GIT_MANIFEST.json
```

That S0 recovery manifest already exists; use unused filenames for later operations.

## Single full GET

Create a private `/tmp` JSON with exactly these keys and actual expected identity from the pack receipt:

```json
{"url":"PRIVATE_HTTPS_DOWNLOAD_URL","name":"PHYS84_S0_RECOVERY_DRIVE_download.zip","expected_bytes":123,"expected_sha256":"64_lowercase_hex_characters"}
```

```bash
python /workspace/scratch/ebcaaaa20861/wu84_delivery_tools/delivery.py download \
  --request /tmp/wu84_drive_recovery_download_request.json \
  --output-dir /workspace/scratch/ebcaaaa20861/wu84_delivery \
  --receipt /workspace/scratch/ebcaaaa20861/wu84_delivery/S0_RECOVERY_DRIVE_DOWNLOAD_RECEIPT.json
```

Exactly one HTTPS GET attempt, no HEAD, Range, redirects, retry, proxy discovery, or content decompression. Unbuffered write-all/fsync/close/reopen validation must complete before acceptance. Failure preserves partial bytes and available received/written/persisted counts in a create-only receipt. Request contents, URLs, response headers, and network exception text are never included in receipts. A failed single-use URL must not be retried automatically.

## Full restoration

```bash
python /workspace/scratch/ebcaaaa20861/wu84_delivery_tools/delivery.py restore \
  --original /workspace/scratch/ebcaaaa20861/wu84_delivery/PHYS84_S0_RECOVERY_20261023_ce14c0bfc031.zip \
  --downloaded /workspace/scratch/ebcaaaa20861/wu84_delivery/PHYS84_S0_RECOVERY_DRIVE_download.zip \
  --git-manifest /workspace/scratch/ebcaaaa20861/wu84_delivery/S0_RECOVERY_FRESH_GIT_MANIFEST.json \
  --output-dir /workspace/scratch/ebcaaaa20861/wu84_delivery/S0_RECOVERY_DRIVE_RESTORE \
  --provider Drive
```

Use distinct downloads, receipts, and new restore directories for each provider. `--provider` is a receipt label and does not prove provider origin. `RESULT.json` provides complete local restoration counts and identities.

Optional `--freeze-manifest FILE` supplies a JSON object with nonempty `entries`, each using the archive row format: `filename`, `bytes`, `sha256`, `kind`, plus `git_blob_sha1` and `mode` for repository rows. Full archive-relative filenames are required. This verifies extracted bytes only and never imports science.

## Later final packaging

Run `pack` with explicit actual final `--commit`, `--stage FINAL`, optional `--science-identity`, current `--intake`, `--parent-recovery /tmp/wu84_owner_recovery`, and new `--archive`/`--receipt` paths. Generate a new fresh Git manifest from the independently fetched final commit before each provider's actual full restore. Provider mutations are the owner's responsibility.

An identical copy of this helper, README, recovery archive, pack receipt, and fresh Git manifest is preserved under `/tmp/wu84_delivery_recovery/`. Mirror receipts record SHA256 and reopened byte equality.
