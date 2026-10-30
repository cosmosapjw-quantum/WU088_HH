# WU R35 source-locked photon cumulants: reproduce

## Source

This ZIP includes immutable original `archive/WU_R34_SOURCE_ORIGINAL_20261030.zip` (8,412,812 bytes, SHA-256 `a43d9fa8a39f64bde756b9b2d942b831d3d2560717198dac98a0a228bf5a370e`) with all older R33/R32 source recursively nested. No new EMAA raw text has been synthesized or added. Python >=3.10 with NumPy and SciPy is needed.

## Clean commands

```bash
unzip -q WU_R35_SOURCE_ORIGINAL_20261030.zip -d R35_CLEAN
cd R35_CLEAN
PYTHONPATH=. python -m src.fcs --out results
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=. python -O -m unittest discover -s tests -p 'test_*.py' -v
python -m compileall -q src tests
```

`src.fcs` extracts R34 to `parents/R34` only as a generated working copy; it is not itself an original. The R34 original ZIP recursively restores R33. In a clean extraction, the old R34 generated output CSVs are supplied in its immutable archived source. Compare the three R35 CSV and JSON summary against `evidence/OUTPUT_SHA256.json`. This is a small finite-state theory/code physical-data run, not external HPC production.

## Outputs

`FCS_CONDITIONAL_3528.csv`, `FCS_ZERO_MEAN_ROOTS_324.csv`, `SOURCE_RESTRICTED_H2_BRANCH_BOUNDS_35280.csv`, `SUMMARY.json`. Only probability moments conditional on first v1 quench landing in v0 J<=4 are source-qualified; R35 does NOT produce a full-chemistry, sky-intensity, observational or global-root-uniqueness result. Main DAG 34/49 unchanged.