# Reproduction commands and identities

Run with Python >=3.10, PyMuPDF (`fitz`), Poppler `pdftotext`, mpmath.

```bash
python -m src.parse_source sources/GL2022_CSIC_supplement.pdf
PYTHONPATH=. python -m src.three_hazard --pdf sources/GL2022_CSIC_supplement.pdf --r27 sources/R27_SOURCE_REACTIVE_RADIATIVE.json --out results
PYTHONPATH=. python -m unittest discover -s tests -p test_r28.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_r28.py -q
python -m compileall -q src tests
PYTHONPATH=. python tests/independent_mpmath.py
```

Source PDF identity sha256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`; R27 row JSON sha256 `b72af2990fbddbc46a496238d9d0d50ad8eb26e61b8e810f27228222e3814339`. Original R27 source ZIP sha256 `a2b7810035fadf8edfe1821660582bec820bcf5aed0d57a636b01321a3ab7aa0`. Sources unmodified; re-running results is byte-for-byte for JSON/CSV in a fixed Python environment and formatting. Do not claim independent publication-grade review merely from multi-algorithm tests.
