# WU088_HH R41 private source master | Reproducible source-conditional physics

Original data and code in `source_private` are immutable owned/source-verified copies from earlier R36/R40; this master is PRIVATE only. Original full articles remain in R40 secure master and are not redistributed. This project is not an astrophysical history or chemical network simulation.

Prerequisites: Python 3.11+, numpy, scipy, mpmath, pandas, matplotlib; no network needed.

```bash
python generate.py
python -m unittest test_science
python -O -m unittest test_science
python plot_physics.py
python plot_external.py
```

Inputs verified at runtime SHA256: `source_private/{emaa_primary.py,HD.Rovibration.805a7aa5.radex,GL2022_1560_INELASTIC_SOURCE_TOKENS.csv}`, original R40 `FIRST_V0_HIT_BRANCHES_1680.csv` historical reference checked in unittest. `INITIAL_CHECKPOINT.json` holds input size and hash. `verification/OUTPUT_SHA256.json` holds exact output hashes. Run in clean extraction and compare exact seven/new CSV and summary files, plus source files.

Physical outputs: `R41_FIRST_V0_MECHANISM_SUMMARY_3500.csv`, `R41_FIRST_V0_TERMINAL_BRANCHES_126000.csv`, `R41_SOURCE_CONTRAST_1750.csv`, `R41_PHOTON_LINE_EVENTS_4704.csv`, `R41_HALF_RADIATIVE_DENSITY_700.csv`, `R41_HALF_DENSITY_SOURCE_CONTRAST_350.csv`, `R41_19LEVEL_RADIATIVE_LINES_63.csv`, `R41_KNOWN_RADIATIVE_OUTSIDE_EXIT_3500.csv`, `R41_OUTSIDE_RADIATIVE_ESCAPE_LINES_124.csv`, and `SUMMARY.json`.

Quality status: source-qualified, numerically checked, not an owner source correction; R41 auxiliary 1/1, canonical DAG 34/49 unchanged, distinct-author R6/C9 NOT_RUN. Git-public package must exclude `source_private` source files; include only owned new code and conditional derived results, notices and source DOI pointers.
