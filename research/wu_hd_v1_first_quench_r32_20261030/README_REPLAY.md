# WU R32 reproducibility contract

1. `archive/WU_R31_SOURCE_ORIGINAL_20261030.zip` is immutable full parent, SHA256 `3286e22a7663ab3114685698e7653b00ac3ea1ec439af466b5c4ae5483e42078`. It contains R30, R29 and R28 original sources. `sources/GL2022_1560_INELASTIC_SOURCE_TOKENS.csv` and `sources/GL2022_CSIC_supplement.pdf` are byte-exact original/source-preserved copies (SHA locked in `src/quench.py`).
2. `sources/CDMS2011V2_RENDERED_V0V1_LEVELS.json` records 2011 v2 historical *rendered* official `.egy` values; it is NOT the original downloaded `.egy` file, nor its uncertainty covariance.
3. Full source-temperature grid is 10 points, with malformed (v1,J2)→(v0,J5) at 2005 K deliberately held. There are 9 qualified temperatures and two distinguishable restricted generator policies, giving 126 cases. No missing rate is silently filled.
4. From this directory, with Python >=3.10, numpy and mpmath:

```bash
PYTHONPATH=. python -m src.quench --out results
PYTHONPATH=. python -m unittest discover -s tests -p 'test_r32.py' -v
PYTHONPATH=. python -O -m unittest discover -s tests -p 'test_r32.py' -v
python tests/independent_mp.py
python -m compileall -q src tests
```

5. Outputs: `results/ATLAS_QUENCH_126.csv`, `TERMINAL_V0_BRANCHES_1386.csv`, `ROTATIONAL_EVENTS_3969.csv`, `DERIVED_V1_UPWARD_189.csv`, `SOURCE_V1_890.csv`, `SUMMARY.json`, `INDEPENDENT_MP85.json`. These are conditional original-SQM-source + displayed spectroscopy calculations, not observed interstellar data.
6. Do not promote production or canonical DAG from this test. Distinct-author R6/C9 NOT_RUN. Each stage JSON and checkpoint ZIP is retrospective provenance, not a separate science execution. Numeric output checks refer to the actual run logs.
