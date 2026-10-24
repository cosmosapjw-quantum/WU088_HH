# PHYS87 mechanical stage delivery

`delivery87.py` packages existing bytes and checks recovery. It does not import scientific modules, evaluate a reference, acquire a lease, mutate Git, upload, download, or issue a scientific decision. Root owns publication and Drive Browser uploads. Dropbox uploads require the separate explicit stage instruction.

## Payload and byte identity

Each S0/S1/S2/FINAL package contains the published commit's **PHYS87 unit only**, the current private intake, one whole pinned PHYS86 FINAL ZIP, and `MANIFEST.json`. The private intake root is selected by root and contains current inventory, backup context and original PHYS87 source bytes. The sole parent dependency is:

| File | Bytes | SHA256 |
|---|---:|---|
| PHYS86_FINAL_20261024_f4a6d5505c84.zip | 11759665 | d41454b0900ca9afbd127632ac0c84c3561288a24587af8d53cee04f09fccb42 |

The parent appears once in each package as `dependencies/...`; it is not recursively restored or recompressed as a new scientific source. The helper stores its ZIP bytes directly. PHYS86 scientific identity and completed references are reused.

Native repository blobs are read from the explicit published commit. Before packing, each working file must have the same native blob identity, calculated by `git hash-object --no-filters --stdin` over its raw bytes. The helper streams binary bytes throughout; it does not decode or rewrite ENDF records, source files, CRLF endings or archive content. Payload SHA256 and native Git blob SHA1 serve their distinct byte-identity roles.

Every input file has a before/after stat snapshot and whole-byte SHA256. Input enumeration, stats and bytes must match the root-adopted frozen manifest before and after packing. Symlinks, nonregular Git entries, unsafe ZIP names, duplicate members and encrypted ZIP entries are rejected. Temporary/signed-link request files are excluded from private intake. Public output JSON uses payload-relative paths and artifact basenames; it does not serialize local absolute roots, credentials, or signed transport requests.

## Stage sequence

1. Root publishes the exact scoped stage and supplies its full commit SHA. No archive is made from an unpublished working-tree approximation.
2. Create a fresh input freeze outside the private intake, then return its SHA256 for root adoption. The freeze records only identities, relative input names and stats; it is not scientific evidence.
3. Pack using that exact adopted freeze SHA. The pack rechecks all inputs before and after writing, retains any failed new output and never overwrites an old archive or receipt.
4. Immediately before each provider upload, run `verify-upload` on the **exact source pathname that will be uploaded**. Match the pack receipt's size/SHA and stable stats. This matters separately for each provider and each repair filename; a previous hash is not current byte evidence. Do not copy a file or change its path after that check without checking the actual new upload source again.
5. Root performs Drive Browser upload; the delivery worker performs Dropbox upload only after explicit authorization. Record the actual provider ID, filename, size and completion acknowledgement. Stage ACKs do not claim whole remote restoration. Unknown calls and failed/short objects remain in the record; a new attempt or create-only repair requires root's concrete decision.
6. FINAL requires a distinct actual complete provider GET for each whole ZIP, original size/SHA, all CRCs/payload hashes/native Git blobs, actual extraction and extracted-file rehash. Each downloader must **finish with its receipt before restore starts**. No HEAD, Range request, preflight, automatic retry or nested parent science is needed.
7. Root binds final receipts and exact final/head/claim status in an immutable external JSON. Its own future upload/readback receipt remains separate. Earlier snapshots retain their original bytes and timestamps.

Stages S0/S1/S2 use actual dual-provider ACKs. FINAL uses both actual whole-byte restoration receipts. The root scientific decision and saved-result scope remain separate from all packaging outcomes.

## CLI

Use actual paths and published full SHAs supplied by root; the examples are placeholders and were not executed during helper preparation. Every output and receipt must be new. Parent directories must exist.

```bash
python delivery87.py freeze --repo REPO --head FULL_PUBLISHED_STAGE_SHA --stage S0 --private-root PRIVATE_INTAKE --dependencies-root PARENT_DIRECTORY --output FRESH_INPUT_FREEZE.json --receipt FRESH_FREEZE_RECEIPT.json
python delivery87.py pack --repo REPO --head FULL_PUBLISHED_STAGE_SHA --stage S0 --private-root PRIVATE_INTAKE --dependencies-root PARENT_DIRECTORY --freeze-manifest ADOPTED_INPUT_FREEZE.json --freeze-sha ROOT_ADOPTED_FREEZE_SHA256 --output FRESH_STAGE.zip --receipt FRESH_PACK_RECEIPT.json
python delivery87.py verify-upload --archive EXACT_UPLOAD_SOURCE.zip --expected-bytes PACK_BYTES --expected-sha256 PACK_SHA256 --receipt FRESH_PREUPLOAD_RECEIPT.json
python delivery87.py restore --repo REPO --head FULL_FINAL_SHA --stage FINAL --archive ACTUAL_PROVIDER_DOWNLOAD.zip --expected-sha256 ORIGINAL_FINAL_SHA256 --output FRESH_EXTRACTION_DIRECTORY --receipt FRESH_PROVIDER_RESTORE_RECEIPT.json
```

The manifest hash is returned by `pack`; it binds exact `MANIFEST.json` bytes without putting the whole archive's own hash inside itself. Local Git identity is read natively; no Git object, index or branch is written by this helper.

The provider folders remain the existing WU Drive folder `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM` and Dropbox `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/`. Actual IDs come from provider responses or root Browser observations and exact-ID metadata, never from prediction or absence in search.

## Failure and cost reporting

Keep each create-only failure receipt and partial file. A source-byte or packaging mismatch does not change scientific validity by itself. Report the concrete object, expected identity, actual identity and affected delivery operation. No failed file is silently reused as an upload source. No package or test reruns completed science.

Mechanical CPU/wall/money totals are unknown unless measured and recorded; do not reset inherited costs to zero. PHYS87's numerical/symbolic budgets and resource gates are controller-owned and unchanged by this helper. HH_R10 remains OFF and production admission remains NOT_ISSUED.
