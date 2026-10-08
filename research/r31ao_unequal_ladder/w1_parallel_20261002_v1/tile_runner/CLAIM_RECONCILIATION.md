# B22: bounded terminal-claim reconciliation

The completed campaign has fifteen successful new native receipts plus imported tile 00, normal worker terminal returns, native wait receipts and a complete exact compact-interior sum. A later strict inspection found six residual native ownership files for tiles 02, 04, 05, 06, 07 and 15. The frozen runner correctly refused automatic resume. The reason those ownership files remained is undetermined; terminal numerical acceptance does not explain the filesystem observation.

`reconcile_claims.py` applies only to the exact pinned completed campaign, observation artifact and session result. Its read-only plan independently validates all fifteen new source-bound native receipts and streams, input/build/plans, worker returns, imported tile 00, all normalized records and the exact final collection. Unknown, changed, symlinked or unresolved claims fail closed. It cannot launch native work.

After review, `apply` acquires the original campaign ownership lock, repeats validation, writes the plan to a new quarantine directory, and atomically moves each exact observed claim with Linux `renameat2(RENAME_NOREPLACE)`. Each original claim byte sequence is preserved with a step record. A full hash snapshot confirms all nonclaim campaign files are unchanged. Partial movement, an existing quarantine or mismatched evidence requires inspection; nothing is silently overwritten or retried.

This resolves a precisely bounded terminal ownership discrepancy when the archived-claim receipt and subsequent frozen-runner inspection succeed. It leaves the underlying filesystem/root-cause question open. It does not alter the original solver, numerical receipts, arithmetic, tolerances, bounds, native execution count, or production admission.
