# WU R38 native BO sibling reconciliation, source qualified

Restore this ZIP to any writable directory, then run (no other external files required to recreate **these** crosswalk outputs):

```bash
python src/reconcile.py --spectral inputs/spectral --fd inputs/finite_difference --out results
python src/independent_audit.py --root .
python -m unittest discover -s tests -v
python -O -m unittest discover -s tests -v
python src/plot_physics.py
```

Compare regenerated output files against `evidence/OUTPUT_SHA256.json` for byte identities. Input byte SHA are recorded in `evidence/PROVENANCE.json`. `source_original/084307_1_supplements.zip` is an immutable upstream AIP supplement; reproduction of the crosswalk uses the included source-generated **R38 spectral** and **R38 finite-difference** CSV files, not repeated full PES eigenvalue calculation. To regenerate upstream source CSVs from raw Fortran, separately restore the frozen R38 spectral and FD archival capsules cited in the provenance record and run their published `README_REPLAY.md` commands. Those archives are in Library and have verified SHA-256; not duplicated here to reduce library use.

Precision/data interpretation: `P_H2_J_before_first_exit` is original R37 source-frozen first-exit mass; no chemical source reconstruction. `Q` is diatomic BO internal-energy channel difference, not net baryon heat. No full three-body quantum scattering. `z_boundary` denotes prescribed external blackbody condition and is not observed cosmological redshift.
