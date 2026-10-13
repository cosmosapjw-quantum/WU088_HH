# Reproduction contract

## Fixed scientific target

Read `INPUTS.json` and `report/REPORT_KO.tex`. Use the declared real-valued model, exact dyadic NPZ IC, source-decimal constants, f=3/38, all 2904 photon modes and proper seconds [0,1e11]. Initial conditions, external HM12 source, prescribed geometry and closure are shared for all lambda. No baseline or tangent ODE run is necessary for this certificate.

Observed runtime: Wolfram Engine 15.0.0 for Linux x86-64, xTensor 1.3.0. Original interval execution wall time16.55s, maxRSS111396KiB. The formula-only xAct rerun is approximately11s. Reserve one process and 512MiB; the archive has no HPC launcher. Python checker needs Python3 and NumPy and took less than0.01s in the observed environment.

## Read-only closure check on retained evidence

```bash
python checks/audit_certificate.py
```

This checker recomputes the exact-rational comparison algebra and binds input bytes. It consumes the saved Wolfram majorants; it does not regenerate their interval evaluation. It updates `checks/EXACT_AUDIT.json` in the selected working copy.

## Fresh CAS reproduction in an isolated copy

```bash
ROOT="$PWD"
WORK="$(mktemp -d /tmp/hh22-reproduction.XXXXXX)"
cp -a "$ROOT/." "$WORK/"
cd "$WORK"
# Only generated outputs in the isolated copy are removed.
rm -f wolfram/interval_result_v3.json wolfram/xact_result_v2.json
wolframscript -file wolfram/finite_response_interval_v3.wl
python -c 'import json; v=json.load(open("wolfram/interval_result_v3.json")); assert v["status"]=="PASS_INTERVAL_TUBE_AND_FINITE_COMPARISON"'
cp wolfram/interval_result_v3.json results/interval_result_v3.json
wolframscript -file wolfram/xact_checks_v2.wl
python -c 'import json; v=json.load(open("wolfram/xact_result_v2.json")); assert v["all_literal_zero"] and v["residual_count"]==11'
python checks/audit_certificate.py
```

The observed interval script downloads the two exact inputs from the embedded immutable receiver URLs and requires their original SHA256. The same NPZ and emissivity bytes are also in `inputs/` for source inspection and offline adaptation. The commands above document the observed entrypoints and guarded sequence; the entire shell block was not executed as an additional campaign. All original outputs and failures are retained under `raw/`.

A different Wolfram build may change outward endpoint widths while still giving a valid enclosure. Preserve both runs. Do not silently swap the declared number representation or call a source-fit error a roundoff error. Do not infer a PASS from shell exit0 alone: the first original syntax failure had exit0 and no scientific result.

## Return fields

Return actual source SHA, input hashes, kernel and xTensor identities, command and exit, output SHA, first-exit ratios, weighted gain, exact rational finite-response endpoints, domain checks, and the separate algebraic audit. Keep any new failures; no native source switch or production merge follows automatically.
