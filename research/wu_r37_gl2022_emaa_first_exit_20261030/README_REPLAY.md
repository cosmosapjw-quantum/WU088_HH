# WU R37 | run from extracted master ZIP root

Python >=3.10; NumPy, SciPy, mpmath installed. This capsule contains immutable exact source files under `sources/`, R36 original parser under `r36_lib/`, original PDF source witnesses, and the original R36 ZIP under `archive/`.

```
python run_r37.py --out reproduced_results
python -m unittest discover -s tests -p 'test_*.py' -v
python -O -m unittest discover -s tests -p 'test_*.py' -v
python -m compileall -q run_r37.py r36_lib tests
python verify_outputs.py reproduced_results
```

`verify_outputs.py` compares the three generated data CSVs and SUMMARY.json to frozen evidence SHA-256, size and row counts. Full original paper PDFs are **private archival inputs**. Do not publish proprietary PDF bytes to public GitHub. All scientific rates in this restricted model come from documented source grids, no interpolation or invented zero. `OFF` retains spontaneous radiation and suppresses only externally stimulated/absorbed terms. 65-digit precision is used for small CTMC inverses.

No rerun of the previous R36 science campaign is needed. R37 adds a new source-restricted first-exit physical observable. Parent PR #175 and all foreign repositories must remain untouched; Draft only, no main merge, no production, canonical DAG 34/49.
