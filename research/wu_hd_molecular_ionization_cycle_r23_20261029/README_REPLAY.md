# R23 replay: typed independent spectroscopy-only molecular ionization cycle

Environment (actual initial probe): Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0, SymPy available. Install original R21/R22 ZIPs from user-provided bytes; SHA-256 MUST match the pinned exact reference.

```bash
cd research/wu_hd_molecular_ionization_cycle_r23_20261029
PYTHONPATH=. python -m unittest discover -s tests -v
PYTHONPATH=. python -O -m unittest discover -s tests -q
PYTHONPATH=. python src/ionization_cycle.py --source-json sources/MOLECULAR_IONIZATION_LITERALS.json --r21-zip /path/WU_R21_SOURCE_ORIGINAL_20261029.zip --r22-zip /path/WU_R22_SPECTROSCOPIC_CANDIDATE_SOURCE_ORIGINAL_20261029.zip --output results/NEW_RESULT.json
PYTHONPATH=. python tests/independent_high_precision.py
python figures/plot_r23.py
```

CLI output is exclusive-create. Do not overwrite the stored original output. Never treat the generated physical-Q NULL fields as missing zeros or upgrade to production. Original-source ZIPs are needed for full archival identity verification. Reports/figures are diagnostic only.
