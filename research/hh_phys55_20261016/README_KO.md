# WU088_HH PHYS55 sandbox reproduce

Source-lock input in the expected relative path is already in this portable ZIP; on
existing repository the same tracked file is used (do not overwrite it).

```bash
export PYTHONPATH=src OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
python3 -m pytest -q tests/test_phys55_hybrid_outgoing.py
python3 scripts/phys55_hybrid_outgoing.py
```

The main source module has only Python standard library and mpmath requirements.
The optional finite FEM diagnostic additionally needs NumPy and SciPy.
The exact all-ell proof is in `research/hh_phys55_20261016/REPORT_KO.md` and
is NOT established by the finite sampled plots. PHYS54 PR94 parent SHA
`9a3054487db04feea99ff7d5714398043e15425d`.

Only central Coulomb outgoing r>=27, with the original noncentral screened
collar 20..27. Physical noncentral screened outgoing Z_S remains open.
`HH_R10=OFF`.

GitHub additive patch contents: src, scripts, tests and research/hh_phys55_20261016
excluding the frozen NPZ (already in the repo). Portable capsule includes original
frozen NPZ for recovery. Do not use the contents as a substitute for live WU repo
without reading its current branch and original AGENTS.md.
