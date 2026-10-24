# PHYS85 scoped delivery helper

`delivery85.py` uses only Python's standard library. It performs no network access, Git publication, scientific execution, deletion, or overwrite. Run with Python 3.10 or newer. Outputs, optional receipts and restore directories are create-only; failed new partial output is preserved for inspection.

## Package a fixed published commit

After the root has fixed the actual full commit SHA, choose a fresh stage name, archive name and receipt name:

```bash
python3 /workspace/scratch/ebcaaaa20861/wu_next_20261024/tools/delivery85.py pack \
  --repo /workspace/scratch/ebcaaaa20861/WU088_HH \
  --head ACTUAL_FULL_COMMIT_SHA1 \
  --stage S0 \
  --output /workspace/scratch/ebcaaaa20861/wu_next_20261024/artifacts/PHYS85_S0.zip \
  --private-root /workspace/scratch/ebcaaaa20861/wu_next_20261024/intake \
  --dependencies-root /workspace/scratch/ebcaaaa20861/wu_next_20261024/recovery \
  --receipt /workspace/scratch/ebcaaaa20861/wu_next_20261024/artifacts/PHYS85_S0_PACK.json
```

Both public prefixes must exist in that commit. Every tracked regular blob under exactly `research/hh_phys85_nuclear_particle_ownership_20261024/` and `research/hh_phys84_completion_20261024/` is streamed from Git's object database. Uncommitted working-tree bytes and the rest of the repository are omitted. Git symlinks/submodules are rejected. The manifest binds the explicit commit, tree, fixed parent base, stage, every payload member's length/SHA256, and every repository member's Git blob SHA1/mode.

Every regular private-root file is included under `private/intake/`, except files whose normalized name contains both `url` and `tmp` or `temporary`. Exclusions are listed in the manifest. Ordinary provenance URLs within JSON remain part of the original evidence. Symlink inputs are rejected. Root should pass the exact intake directory, which must be stable during the brief package operation.

The two fixed PHYS84 recovery dependencies are included under `dependencies/`. Their pinned lengths and SHA256 values are checked before packing and against streamed bytes. The nested historical ZIP is stored without recompression. A single root `MANIFEST.json` lists payload members and has no self-referential archive hash. The whole archive SHA256 appears in the separate pack receipt.

## Verify a real provider download and extract everything

The root uploads the ZIP, obtains the provider readback identity, and downloads it once into a fresh local file through its existing configured HTTPS downloader. Run the helper once for each actual provider ZIP, with the pack receipt's archive SHA256 and the same explicit Git commit/stage:

```bash
python3 /workspace/scratch/ebcaaaa20861/wu_next_20261024/tools/delivery85.py restore \
  --repo /workspace/scratch/ebcaaaa20861/WU088_HH \
  --head ACTUAL_FULL_COMMIT_SHA1 \
  --stage S0 \
  --archive /absolute/path/to/actual_provider_download.zip \
  --expected-sha256 ACTUAL_PACK_RECEIPT_ARCHIVE_SHA256 \
  --output /workspace/scratch/ebcaaaa20861/wu_next_20261024/artifacts/PHYS85_S0_PROVIDER_RESTORED \
  --receipt /workspace/scratch/ebcaaaa20861/wu_next_20261024/artifacts/PHYS85_S0_PROVIDER_RESTORE.json
```

Restore checks whole downloaded ZIP bytes, every member CRC, the exact member set, every payload SHA256, manifest Git commit/tree/base/prefix identities, repository path/blob/mode identities against a fresh `git ls-tree` of the explicit commit, and Git blob SHA1 from the actual member bytes. It validates pinned nested dependency whole bytes only. It then extracts **all** archive members into a new directory and rehashes every actual extracted file, including `MANIFEST.json`. The JSON receipt reports each check count separately.

Historical parent restore evidence is explicitly marked as reused. This operation does not rerun PHYS83/PHYS84 science or expand/replay the nested historical archive. A local pack does not establish provider backup completion. A successful restore establishes verification of that one downloaded ZIP; root's external provider identity/upload/download receipts establish which provider it came from. The helper never accesses or modifies the existing `delivery_configured_proxy.py` downloader.

## Verification status

No synthetic test campaign or old scientific workload is run. The first actual authorized package and the two real provider restore operations supply the operational verification evidence. If the explicit commit has not yet been created, packaging must wait for it; do not substitute a guessed HEAD or infer backup completion.
