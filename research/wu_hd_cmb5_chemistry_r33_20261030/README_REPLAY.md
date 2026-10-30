# WU R33 clean scientific replay

The complete archive includes original unchanged `archive/WU_R32_SOURCE_ORIGINAL_20261030.zip`, SHA256 `01482fdefef303b8cc00bd0efe9b20c23d1886a69679d76eec9d67434fe643e7`. It recursively contains original WU R31/R30/R29 source ZIPs, but R33 uses exact checked original R29 input text and code copies in `sources/` for faster clean execution. `verify_sources` checks immutable ZIP SHA+CRC plus exact copies of the original source data / script. The source copies are not new independent source measurements.

Dependencies: Python >=3.10, NumPy, SciPy, mpmath. Run from clean archive extraction root:

```bash
PYTHONPATH=. python -m src.cmb5 --out results
PYTHONPATH=. python -m unittest discover -s tests -p test_r33.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_r33.py -q
PYTHONPATH=. python tests/independent_mp85.py
python -m compileall -q src tests
```

Results: `R33_CMB_CASES_1470.csv`, `R33_CMB_LINES_5880.csv`, `R33_H2_PRODUCTS_14700.csv`, `R33_FIXED_DENSITY_POLICY_735.csv`, `R33_RADIATIVE_BALANCE_Z_210.csv` and `SUMMARY.json`. Independent same-author method results in `INDEPENDENT_MP85.json`. The literal source z-grid is `OFF`, 0, 5, 10, 30, 100, 300 with external `T_CMB=2.7255(1+z)` K. `OFF` is a no-external-radiation comparison, not z=-1 physical epoch.

**Core physical result** is conditional, state-resolved radiation/chemistry competition for one initially excited HD in a fixed external environment, **not** the CMB specific intensity, whole-gas net heating or an observed cosmological spectrum. No invented missing reactions, no native PES Q, no automatic next node or canonical DAG promotion. All raw source provenance remains in the source files and original nested archives.
