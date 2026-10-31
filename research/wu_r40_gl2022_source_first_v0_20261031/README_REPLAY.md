# WU R40 reproducible original-source first-hitting experiment

**Inputs:** user-supplied `214302_1_epaps.zip` SHA256 3db766f912d7cc9010f6c5b95ab8f2a98aceae5e7ad261d677e80ad1c57c8c4d; contained PDF SHA256 a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754. R36 EMAA RADEX source SHA256 b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94. R33 700-token archival source JSON is used **only** to check PDF parsing byte-for-byte source tokens.

**Original science contract:** static 19-HD-level proton collisions at exact 10 original temperature values. 7 HD(v=1) transient states, 12 HD(v=0) absorbing landing levels; first-v0 hitting probability B, mean hitting time and conditional net HD internal energy release. `n(H+)=1 cm^-3` time normalizer. EMAA source versus GL2022 printed-valid hybrid, not a claimed author correction; original PDFs not public redistributed.

**Execution:** requires Python 3, NumPy, SciPy, mpmath, Matplotlib, pandas, and `pdftotext` (Poppler). Inside extracted master archive:

```bash
python generate.py --root . --out results
python -m unittest test_science
python -O -m unittest test_science
python plot_physics.py
```

Read `THEORY_KO.md`, `REPORT_KO.md`, `REFEREE_SELF_ADVERSARIAL_KO.md`, `HANDOFF_NEXT_THREAD_KO.md`, `results/SUMMARY.json`. Verify original source hashes before use. Compare `verification/OUTPUT_SHA256.json` for six generated CSVs after a clean replay. Missing host package is an environment blocker, not a physics no-go. Original raw data and PDFs have access/licensing constraints and are only in private master; GitHub contains generator, tests, generated new physical results and numerical evidence, not full third-party paper/EPAPS.

**Status:** canonical DAG 34/49 unchanged; R40 auxiliary 1/1 scoped; R/C 18/20 scoped, R6 and C9 distinct-author NOT_RUN, no production or main merge.
