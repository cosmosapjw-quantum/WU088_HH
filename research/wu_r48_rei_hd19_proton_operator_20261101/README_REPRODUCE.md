# WU R48 full derived atlas: restore/run contract

This source-free package is **WU088_HH** material for the conditional REI Bianchi IGM HD consumer. Original EMAA and original REI third-party source bytes are **not** redistributed in this ZIP; obtain separately from preserved private archives and verify SHA-256 before any run. This is scientific input evidence, not a native REI solver integration.

## Inputs (unaltered)

- WU R43 recovered source-private ZIP containing `source_private/HD.Rovibration.805a7aa5.radex`, ZIP SHA256 `a715301114cfb2fd66361f9519081dc38033765e3b76b517bac5bc78fbe91a50`; **raw** RADEX SHA256 `b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94`.
- REI original accepted tick160 46080-node source ZIP SHA256 `48ad5c6f0922ad946a10a89ce17fefd2c7241ac956b6bac194892a42810312a7`.
- Earlier WU R47 generated source-support CSV for crosscheck test only: `R47_HD_REI_SOURCE_SUPPORT_46080.csv.gz` original source-derived WU file. Its separate original-source adapter `wu_r47_source_adapter.py` is provided here byte-exact SHA256 `61bf5c8789f4a095bbe10f8aa222138db24c6b811accfff5989affc27603eb02`.

## Portable calculation

Python 3.11+ with NumPy, SciPy, Matplotlib. No network or original REI runtime required. Set BLAS threads to 1 for deterministic output.

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
export WU_R48_EMAA_ZIP=/private/path/WU_R43_RECOVERED_HD52_EMAA_GRACKLE_SOURCE_20261031.zip
export WU_R48_REI_ZIP=/private/path/REI_F05_ORIGINAL_ACCEPTED_46080_STATES_20261101.zip
export WU_R48_R47_CSV=/private/path/R47_HD_REI_SOURCE_SUPPORT_46080.csv.gz
python r48_hd19_operator.py --emaa-zip "$WU_R48_EMAA_ZIP" --rei-zip "$WU_R48_REI_ZIP" --out results
python -m unittest test_r48 -q
python -O -m unittest test_r48 -q
python verify_r48.py
python plot_science.py
```

`test_r48` test 14 directly compares selected node transitions against the earlier R47 derived source state, so the exact earlier CSV path is required for *all* unit tests. The main calculation does not use that derivative CSV and loads original REI input directly.

### Outputs and statuses

- `results/R48_ORIGINAL_19STATE_TRANSITION_RATIO_960336.csv.gz`: 5,616 source-supported actual REI nodes ×171 native H+ source pairs, interpolated source coefficients and marginal outer-bound ratio.
- `results/R48_REI_HD19_LEVEL_EXITS_106704.csv.gz`: per-level *H-nucleus-density-normalised* collision-only total exit rates.
- `results/R48_REI_NODE_SUMMARY_5616.csv`: per-source-node min/median/max ratio, collision generator spectral gaps, original 52-level LTE outside19 weight.
- `results/R48_TRANSITION_SUMMARY_171.csv`, five-row witness, original-source result JSON, three PNG + SVG original-physics diagnostic plots.
- `INDEPENDENT_OUTPUT_AUDIT.json`: independent stdlib CSV scan + scalar original-source interpolation control.
- `stages/R01..R10,C01..C10.json`: individual theory/coding checkpoints, **not 20 independent physical experiments**.

Run verification is not a proof that original 26-event F05 interval is accepted. Do not infer absolute collision times without original physical n_H,nuc, or molecular cooling per volume without n_HD and actual level populations. No original H+ rates above HD source level19.

Data units: original `T` K, source `E_i` J, `k` cm³/s, `ratio` dimensionless. Reversible spectral gap of per-H-nucleus-density generator cm³/s; multiply by physical `n_H,nuc` [cm⁻³] to recover physical s⁻¹ when n_H is actually available.

**Official DAG at this research unit:** WU canonical 34/49; REI central 28/88, working 33/88, F05 original accepted ticks 160/131072 and `[160,161]` BLOCKED. `R6/C9` different author NOT_RUN, production HOLD, NO_MAIN_MERGE, AUTO_NEXT_NODE=false.
