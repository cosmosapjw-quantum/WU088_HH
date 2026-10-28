# WU088_HH R16 scoped exact preprocessing

This source bundle contains only the new R16 mathematical preprocessing and a read-only copy of the frozen R15 engine, **not the entire WU088_HH repository**. It does not contain actual HD reactive rate arrays or a physical consumer.

Run standalone tests (SymPy required):

```bash
python tests/quick_run.py
```

Run the saved exact physical-contract **arithmetic fixture**, with the pinned original R15 core:

```bash
python src/r16_cli.py --input results/R16_FLAT_CONTROL_INPUT.json --output /tmp/r16_NEW_RESULT.json --r15-core external/R15_frozen_cubic_convolution.py
```

The output must not already exist (create-only). The CLI checks the Git blob identity of the R15 engine, rewrites the signed-B3 source into exact positive B3 cells, and calls the original R15 validation/run path. `source_sha256=ffff...` in the test is a conspicuously **synthetic-only marker**, never evidence of real HD input.

See `theory/PROOF_KO.md`, `REPORT_KO.md`, `HANDOFF_KO.md`, `SCIENTIFIC_ADMISSION.json`, and `delivery/DELIVERY_STATUS.json`. Scientific and cloud-publication/backups are independent statuses.
