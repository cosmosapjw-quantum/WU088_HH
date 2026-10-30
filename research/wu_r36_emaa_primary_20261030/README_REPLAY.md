# R36 source-owned replay

Archive master includes unchanged user-uploaded EMAA RADEX source, frozen GL2022 printed CSV transcription, original source supplementary PDF, and nested byte-exact R35 master archive as provenance anchor. Outputs are deterministic from the exact raw bytes and source Python in `src/emaa_primary.py`; the original raw input is **never modified**. Dataset DOI is metadata; upstream byte identity requires official independent readback, which this run did not establish.

Requirements: Python >=3.10, NumPy, SciPy, mpmath. From extracted master root:

```bash
PYTHONPATH=. python -m src.emaa_primary --out results
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=. python -O -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=. python tests/independent_mpmath.py
python -m compileall -q src tests
```

Compare SHA256 and size of CSVs and SUMMARY.json to `evidence/OUTPUT_SHA256.json`; the mpmath script writes comparison diagnostics to `evidence/MPMATH80.json`. All physics is source-scoped/conditional and no further node auto-start or production merge is authorized.
