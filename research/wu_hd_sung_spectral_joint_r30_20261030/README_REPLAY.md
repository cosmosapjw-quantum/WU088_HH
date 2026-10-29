# WU R30 | Original-source HD line photon + chemical branch reproducibility

1. Extract the full R30 SOURCE ZIP into an empty directory. It includes the unmodified `archive/WU_R29_SOURCE_ORIGINAL_20261030.zip` (SHA-256 `65ed097acb02f8eb91ff6518c26c8ad61e721e3fadd9b904aa2157e3508cb0ea`). The extraction of this parent archive is automatic in `src/spectral.py` and source bytes are verified each time. It does **not** use network access or fetch model substitutions.
2. Run from the R30 directory:

```bash
PYTHONPATH=. python -m src.spectral --out results
PYTHONPATH=. python -m unittest discover -s tests -p 'test_r30.py' -q
PYTHONPATH=. python -O -m unittest discover -s tests -p 'test_r30.py' -q
PYTHONPATH=. python tests/independent_mpmath.py
python -m compileall -q src tests
```

Dependencies: Python >=3.10, NumPy, SciPy (parent R29 test only), mpmath. Tests target 7 printed GL2022 temperature nodes, prescribed nH+, 5-level tracer, full photon/reaction absorption. No HPC. `evidence/` has actual output logs and Wolfram result.

New source: `sources/REC164_SUNG2022_PRIMARY_TABLE4_LOCK.json` is an exact **four-line subset transcription**, with Git source blob `23626dd9a77aa4e6214f6f9c792ea18270b3940c` and internal R30 file SHA validation. The original publisher PDF and laboratory full covariance were not acquired. Do not call this byte-exact original lab PDF. Original reactions and downward SQM computed rates are original 2022 data nested in the R29 archive. EMAA2023 numeric raw not acquired.

Output:
- `results/R30_CASES_210.csv/json`: 210 physics model inputs, photon-reaction observables and 2011-vs-2022 measured-level sensitivity.
- `results/R30_PHOTON_ATLAS_840.csv`: line-specific photon wavelengths/frequency/first-photon probability and mean photon energy.
- `results/R30_RESTRICTED_H2_JOINT_2100.csv`: J' product and joint photon/no-photon outcome.
- `results/INDEPENDENT_MP75.json`: separate mathematical implementation evaluation.
- `results/SUMMARY.json`: explicit claim-gates and one representative physics result.

All results are conditional computed source-based physics, **not full cosmology, PES-native quantum scattering or measured astrophysical signals**. Central DAG 34/49 unchanged. Do not merge production, alter REC/CR or claim distinct-author independent review.