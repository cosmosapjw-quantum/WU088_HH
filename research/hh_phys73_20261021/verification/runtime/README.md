# Recorded runtime and independent checks

These are byte-identical copies of the original sandbox receipts. COPY_RECEIPT.json records original paths, sizes, and SHA256 values. The observed host was the shared 8-CPU / 8-GiB cgroup sandbox, not the NCP 64-core / 128-GiB host.

RUST_INSTALL_AND_SMOKE.json records the actual scoped Rust 1.94.1 install, compiler/cargo versions, smoke build and run. The archive SHA is recorded; the detached signature was not verified against a selected trusted key. The copied runtime_smoke.rs is the executed source. Installer scripts, compiler binaries, the archive, and an earlier partial manifest are intentionally not copied here.

INDEPENDENT_BATCH_REVIEW_INITIAL.json and INDEPENDENT_BATCH_REVIEW_FINAL.json preserve earlier failing attempts. INDEPENDENT_BATCH_REVIEW_FINAL_PASS.json records the later 14/14 pass with exact source hashes; those preparation hashes precede integration of the positive analytic angular default. The current analytic/default/cache path is checked by ../cache/CACHE_CHECK_RECEIPT.json and ../cache/integrated/INTEGRATED_PIPELINE_RECEIPT.json.

ANALYTIC_SCREEN_CHECK.json contains selected 180-dps angular-integral and Bessel comparisons, not a uniform floating-point certificate. No completed HH scientific panels or profiles were integrated by these checks.
