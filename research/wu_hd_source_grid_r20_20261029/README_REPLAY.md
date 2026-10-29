# R20 clean replay and claim boundary

Dependencies: Python >=3.10, `pdftotext` (Poppler), `pytest`, `numpy`, `scipy`, `mpmath`, `matplotlib`. Runtime availability must be probed in each new session.

From a full Git checkout with R18/R19 ancestors:

```bash
export REPO_ROOT=/path/to/WU088_HH
export WU_R20_SOURCE_PDF=/path/to/verified/GL2022_CSIC_supplement.pdf
export PYTHONPATH="$REPO_ROOT:$REPO_ROOT/research/wu_hd_source_grid_r20_20261029"
cd "$REPO_ROOT"
python3 -m pytest -q research/wu_hd_source_grid_r20_20261029/tests/test_grid_exposure.py
python3 research/wu_hd_source_grid_r20_20261029/tests/independent_reference.py
python3 research/wu_hd_source_grid_r20_20261029/tests/numerical_benchmark.py
python3 research/wu_hd_source_grid_r20_20261029/figures/render_r20.py
python3 -m src.grid_exposure --source-pdf "$WU_R20_SOURCE_PDF" \
  --schedule-json research/wu_hd_source_grid_r20_20261029/EXAMPLE_SCHEDULE.json \
  --initial-m3 1e6 1e6 0 0 --output /new/output/path.json
```

From the self-contained R20 SOURCE ZIP extracted into `R20_RESTORE` (contains `parent/research` and original PDF):

```bash
cd R20_RESTORE/parent
export PYTHONPATH="$PWD:$PWD/.."
export WU_R20_SOURCE_PDF="$PWD/ORIGINAL_SOURCES/GL2022_CSIC_supplement.pdf"
python3 -m pytest -q ../tests/test_grid_exposure.py
python3 ../tests/independent_reference.py
```

The R20 Git unit is only the new `research/wu_hd_source_grid_r20_20261029` directory; the original PDF is **not** added to public Git. Source PDF must match SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. Output is create-only. Source rates only at ten original discrete temperatures. CR `proper_dt` is signature/formula matched, not executed against owner model. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`.
