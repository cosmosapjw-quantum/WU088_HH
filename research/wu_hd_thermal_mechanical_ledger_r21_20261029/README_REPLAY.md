# WU R21 read-only standalone replay

Source PDF must have exactly 273554 bytes and SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`, supplied under `ORIGINAL_SOURCES/GL2022_CSIC_supplement.pdf` from an authorized archive. The Git repo's parent R20 PR157 supplies R18 native_rates.py, R19 nominal_exchange.py and R20 grid_exposure.py under the pinned branch. Preserve those modules unchanged.

From archive-extraction root, after ensuring Python >=3.10, scipy, numpy, mpmath, pytest or unittest, pdftotext are available:

```bash
export PYTHONPATH="$PWD"
python -m unittest discover -s research/wu_hd_thermal_mechanical_ledger_r21_20261029/tests -v
python -O -m unittest discover -s research/wu_hd_thermal_mechanical_ledger_r21_20261029/tests -v
python research/wu_hd_thermal_mechanical_ledger_r21_20261029/tests/independent_mpmath80.py
python research/wu_hd_thermal_mechanical_ledger_r21_20261029/tests/scipy_ivp_reference.py
python research/wu_hd_thermal_mechanical_ledger_r21_20261029/figures/render_ledger.py
python -m research.wu_hd_thermal_mechanical_ledger_r21_20261029.src.thermal_ledger --source-pdf ORIGINAL_SOURCES/GL2022_CSIC_supplement.pdf --schedule-json research/wu_hd_thermal_mechanical_ledger_r21_20261029/results/EXAMPLE_SCHEDULE.json --initial-m3 1000000 1000000 0 0 --output NEW_OUTPUT.json
```

All writes use a fresh worktree or an exclusive-new output path; CLI rejects existing paths. The archive includes the source PDF; no source PDF is committed to public Git. Interpretation: `Q_event` unknown, `physical_bath_delta` null; only affine Q coefficient and external-work/temperature intercept issued. Independent-author R6/C9 NOT_RUN.
