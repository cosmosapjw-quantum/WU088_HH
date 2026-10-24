# Assemble the external PHYS85 final delivery JSON

The stdlib helper reads actual final receipts, validates their cross-identities, and creates a fresh external JSON. It performs no network operations, publication, scientific evaluation or replay. It does not pack a ZIP. No synthetic tests were run; use the eventual actual final assembly as the operational validation.

## CLI

```bash
python3 research/hh_phys85_nuclear_particle_ownership_20261024/delivery/assemble_final_delivery.py \
  --request /absolute/path/to/FINAL_ASSEMBLY_INPUTS.json \
  --output /workspace/scratch/ebcaaaa20861/wu_next_20261024/artifacts/PHYS85_FINAL_DELIVERY_20261024.json
```

The request is a JSON object containing these keys. Replace every placeholder with the actual final identity or actual existing path. No counts are supplied or guessed.

```json
{
  "repo": "/workspace/scratch/ebcaaaa20861/WU088_HH",
  "head": "ACTUAL_FULL_FINAL_COMMIT_SHA1",
  "tree": "ACTUAL_FULL_FINAL_TREE_SHA1",
  "base": "d5c2c8dbbbd77bc81526dda6e74df534fba3c4e5",
  "stage": "FINAL",
  "branch": "research/hh-phys85-nuclear-ownership-20261024",
  "pull_request": {"number": 142, "mode": "draft"},
  "evidence_identity_path": "/absolute/path/to/results/EVIDENCE_IDENTITY.json",
  "status_path": "/absolute/path/to/results/RESULT_STATUS.json",
  "pack_receipt_path": "/absolute/path/to/ACTUAL_FINAL_PACK_RECEIPT.json",
  "providers": {
    "Drive": {
      "upload_receipt_path": "/absolute/path/to/ACTUAL_DRIVE_UPLOAD_ACK.json",
      "download_receipt_path": "/absolute/path/to/ACTUAL_DRIVE_SINGLE_GET_RECEIPT.json",
      "restore_receipt_path": "/absolute/path/to/ACTUAL_DRIVE_RESTORE_RECEIPT.json"
    },
    "Dropbox": {
      "upload_receipt_path": "/absolute/path/to/ACTUAL_DROPBOX_UPLOAD_ACK.json",
      "download_receipt_path": "/absolute/path/to/ACTUAL_DROPBOX_SINGLE_GET_RECEIPT.json",
      "restore_receipt_path": "/absolute/path/to/ACTUAL_DROPBOX_RESTORE_RECEIPT.json"
    }
  },
  "stage_history_paths": [
    "/absolute/path/to/delivery/S0_BACKUP_ACK.json",
    "/absolute/path/to/delivery/S1_BACKUP_ACK.json",
    "/absolute/path/to/delivery/S1R_BACKUP_ACK.json"
  ],
  "freeze_check_paths": [
    "/absolute/path/to/verification/BYTE_FREEZE_CHECK.json"
  ],
  "provenance_paths": [
    "/absolute/path/to/ACTUAL_PUBLICATION_OR_RECOVERY_PROVENANCE.json"
  ],
  "additional_json_paths": [
    "/absolute/path/to/EXECUTION_LEDGER.json",
    "/absolute/path/to/STAGE_STATUS.json"
  ]
}
```

`additional_json_paths`, `branch`, and `pull_request` are optional. All other displayed keys are required; `provenance_paths` may be an empty list when provenance is fully present in the other supplied receipts. Stage history and freeze receipts must be nonempty. A combined final upload ACK file can be supplied for both providers when its root has `drive` and `dropbox` sections. Otherwise supply each raw successful provider response separately; wrappers with `structuredContent` are accepted. The original upload evidence is embedded after removing transport URL/secret fields.

## Required actual evidence

- The final pack must have stage `FINAL`, `status=PACK_CREATED`, and the requested actual Git commit/tree/base. The local archive is streamed once for size/SHA256 comparison against its pack receipt.
- Downloader receipts must be from the reused configured downloader: `status=PASS_SINGLE_FULL_GET_REOPENED_BYTES`, `operation=download`, one GET, zero automatic retries, HTTP200, complete response, matching expected/received/written/reopened bytes and SHA256.
- Both restores must come from `delivery85.py`: `status=RESTORE_VERIFIED`. Commit/tree/base/stage, archive identity and every required CRC/payload/Git/extraction count must match the pack receipt. The GET output path must equal that provider's actual restored archive path. The two provider download files must be distinct. Their current bytes are rehashed.
- Each actual extracted `MANIFEST.json` must match the pack receipt's manifest SHA256, the same Git/stage identity, and the other provider's manifest exactly. The full manifest is embedded.
- The root's `EVIDENCE_IDENTITY.json` must have `identity_kind=NON_SCIENTIFIC_EVIDENCE_ONLY`, null completed science and false scientific completion. The canonical descriptor SHA256 is checked, and descriptor final status must equal the supplied `RESULT_STATUS.json`.
- Every supplied file within the repository must match the corresponding final ZIP manifest entry's size and SHA256. This prevents silently embedding dirty working-tree versions of public evidence after the final package was fixed.
- Freeze receipts must explicitly PASS and contain no mismatches. Their actual counts and provenance are embedded; the assembler does not reinterpret scientific claims.

The resulting `PHYS85_FINAL_DELIVERY_V1` JSON binds final Git identity, non-scientific evidence identity, root status/counters, full ZIP manifest, both actual full GET and restore receipts, actual stage ACK history, final freeze checks, provenance and source-file byte hashes. Historical nested restoration stays the explicit reused state already recorded in the pack/restore evidence.

## Transport privacy and non-recursion

Do not supply live downloader request files or credentials as evidence. Live downloader request objects and attachment names containing temporary-URL markers are rejected; the `--request` configuration itself is read only as input paths/metadata and is not embedded. URL/token/password/secret/authorization/cookie/header/credential fields and transport request contents are removed from embedded receipts. HTTP(S) strings are stripped, including ordinary stable URLs; actual provider IDs remain available where their original keys are IDs.

The external JSON contains no hash, provider IDs or future ACK/readback results for **itself**. On success, stdout reports the newly created file's bytes and SHA256 for root's subsequent upload and actual raw byte readbacks. Those external transport identities must be bound in a separate outer receipt or PR body. Original input hashes identify exact raw receipt files; embedded redacted receipts are labeled by removed field paths. Existing output files are never overwritten.
