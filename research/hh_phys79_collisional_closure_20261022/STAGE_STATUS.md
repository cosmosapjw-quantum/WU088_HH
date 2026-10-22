# PHYS79 — science complete within the declared subset

| Stage | State | Evidence |
|---|---|---|
| Source and derivation | Complete for domain-guarded CI and declared D/H model | theory/, Wolfram receipts |
| Implementation | Complete for the selected operator | source/collisional.py |
| Light verification | 24 unique tests PASS; C9 findings closed | verification/ |
| Saved-history analysis | 322 unique epochs; 2 postprocessing executions; 0 ODE | analysis/saved_operator/ |
| New science execution | 3 successful ODE = 2 isolated controls + 1 refinement | results/ISOLATED_SUMMARY.json |
| Exact-identity resume | 3 skips; 0 new ODE; NPZ bytes unchanged | results/ISOLATED_RESUME_STDOUT.json |
| Science publication | S0/S1/S2 complete in Draft PR134 | delivery/S2_PUBLICATION_RECEIPT.json |
| Science backup | S2 both providers: full bytes SHA256, CRC, 156 payload SHA PASS | delivery/S2_*_RESTORE_RECEIPT.json |
| Final delivery | Final metadata HEAD, final ZIP and final JSON IDs are externally attested to avoid self-reference | delivery/FINAL_DELIVERY_POINTER.json; PR134 body |
| Full collisional cosmology DAG | PARTIAL_WITH_EXECUTABLE_SUBSET; remaining source/energy obligations OPEN | DAG_OVERLAY.json |

S2 science commit: 338fb7728e8b41f49551200b1f1ba73c047fb90c.
S3 changes delivery/report/handoff metadata only. No new ODE or scientific dependency change.
HH_R10=OFF. Production admission NOT_ISSUED.
