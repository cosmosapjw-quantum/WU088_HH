# Final dependency recovery addition

The current helper has two authorized changes after the original S0_RECOVERY package: S1/S2 are accepted `pack --stage` labels, and a `FINAL` archive's full `restore` automatically recovers exactly five mandatory parent dependency files. Stage labels identify packaging stages; they do not issue scientific acceptance or imply an application completed.

Current helper SHA256: `b93dc1cee7c236d4ea857b752023c11e1b9a79d86bf9c0be97b30fc8f46ed7a9`.

- Workspace helper: `/workspace/scratch/ebcaaaa20861/wu84_delivery_tools/delivery.py`
- Identical latest mirror: `/tmp/wu84_delivery_recovery/delivery_with_dependencies.py`
- Original S0 helper `59aa2ffe...` remains at `/tmp/wu84_delivery_recovery/delivery.py`.
- S1/S2-only helper `d04ab850...` remains at `/tmp/wu84_delivery_recovery/delivery_S1_S2.py`.
- Prior helper bytes are also preserved in the workspace under explicit `delivery_pre_...` names.
- Successful S0 archive, receipts, and original mirrors remain unchanged.

The initial README's raw-only nested policy still describes the historical whole-parent restoration scope. The new independent section below adds five-file dependency recovery for final deliveries, without rerunning or claiming a new full CRC/hash restoration of all 385 historical parent ZIP members.

## Exact final behavior

After completing all existing full outer ZIP comparisons and actual extraction, the helper reads the nested PHYS83 ZIP and parent delivery JSON **from the actual outer downloaded payload extraction**. It validates both raw pinned identities before and after dependency recovery. It validates the nested archive metadata structure, exact nested manifest path coverage and parent commit/tree/scope. Safe historical bytecode paths are permitted only during nested metadata scanning; no bytecode is extracted or imported.

It reads the nested byte manifest with CRC/size validation and extracts only:

1. `research/hh_phys83_ce_completion_20261023/results/rate_grid.csv`
2. `research/hh_phys83_ce_completion_20261023/CONTRACT.json`
3. `research/hh_phys83_ce_completion_20261023/results/SCIENCE_IDENTITY.json`
4. `research/hh_phys83_ce_completion_20261023/results/COMPLETE.json`
5. `research/hh_phys83_ce_completion_20261023/source/vendor/phys78_run_pilot.py`

All five have explicit size/SHA256/Git blob SHA1 pins in the helper, checked against the immutable nested manifest and recomputed bytes. The four data pins are also compared against the restored child's `CONTRACT.json` `input_pins`. The fifth is the actual lease implementation, SHA256 `76ff57ba687fd9830b84c3fcff69eb8ed0e9f6ceab4551e61c67c84d3ea65124`; it is treated solely as bytes.

Outputs are created under the fresh restore operation's directory:

`dependency_restore/research/hh_phys83_ce_completion_20261023/...`

Exactly five files totaling 89,283 bytes receive CRC, explicit pin, Git blob, create-only write/fsync/close, regular-file mode and reopened byte/hash/blob checks. Outer archive payload/member/extraction counts remain unchanged. A separate `mandatory_parent_dependencies` result section records the five-file counts, one nested manifest CRC, actual paths and identities, and unchanged parent ZIP/JSON hashes. A dependency failure fails the overall final restoration and preserves partial output. Nonfinal stage restoration does not invoke this addition.

The normal final command is unchanged; use the latest helper:

```bash
python /tmp/wu84_delivery_recovery/delivery_with_dependencies.py restore \
  --original ORIGINAL_FINAL_ZIP \
  --downloaded ACTUAL_PROVIDER_FINAL_DOWNLOAD \
  --git-manifest FRESH_FINAL_GIT_MANIFEST \
  --output-dir NEW_RESTORE_DIRECTORY \
  --provider Drive
```

An optional `--freeze-manifest` remains a byte-only check of an explicitly supplied subset of the restored child files. A seven-file static freeze can identify prepared contract/source/fixture/verifier/theory bytes without implying that a scientific application ran or results exist.

Validation so far is `ast.parse` only. No dependency extraction, test, scientific import, rate evaluation, ODE, or provider operation was executed while adding this function. Actual final provider download/restoration is the intended mechanical validation.
