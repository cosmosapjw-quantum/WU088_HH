# Reproduce WU R31 conditional HD energy ledger

This archive contains the exact **unmodified R30 original full SOURCE ZIP** in `archive/`, SHA256 `d1aa63fedb6527d6aab59df447f1f2b4aa557fab98789b962464a2b86bb5bf16`. R30 itself contains the unmodified R29 original ZIP SHA256 `65ed097acb02f8eb91ff6518c26c8ad61e721e3fadd9b904aa2157e3508cb0ea` and the GL2022 source. Neither source requires network access. The new unit uses no new uncertified EMAA or PES data.

From a clean extraction directory with Python ≥3.10, numpy, scipy (parent tests), mpmath and matplotlib for optional plot:

```bash
sha256sum archive/WU_R30_SOURCE_ORIGINAL_20261030.zip
PYTHONPATH=. python -m src.energy_ledger
PYTHONPATH=. python -m unittest discover -s tests -p 'test_r31.py' -v
PYTHONPATH=. python -O -m unittest discover -s tests -p 'test_r31.py' -v
PYTHONPATH=. python tests/independent_mp.py
python -m compileall -q src tests
```

Outputs: exactly 210 main source-grid cases, 2100 collisional edge-energy rows, 1050 terminal state-energy rows, 840 photon rows, 35 matched-density policy pairs, summary JSON. Preconditions: positive source rate cells at exactly source T nodes; 5 HD v0 J0..4 only, fixed T and n(H+) with collision detailed balance and REC161 spontaneous A, chemical absorption to selected H2(v'=0) products. No original collision cross-section, unknown Q remains NULL. Parent source intentionally byte-immutable and new untrusted replacements fail. All stage checkpoint ZIPs are auxiliary evidence and rely on this complete SOURCE ZIP for full physics replay.