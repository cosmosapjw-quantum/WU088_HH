# Reproduce the WU R24 auxiliary conditional test

No original scientific files need modification. All commands from the package root:

```bash
PYTHONPATH=. python -m unittest discover -s tests -v
PYTHONPATH=. python -O -m unittest discover -s tests -v
PYTHONPATH=. python tests/independent_high_precision.py
PYTHONPATH=. python src/threshold_bound.py --source sources/GL2022_R18_EXACT_ROW.json --out results/CREATE_ONLY_NEW.json
PYTHONPATH=. python src/positive_witness.py --out results/CREATE_ONLY_WITNESS.json
python figures/render_diagnostics.py
```

The two CLI `--out` paths must NOT exist. They use exclusive create, not overwrite. Original R18 supplement PDF source remains separately upstream with SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. No physical Q or source scattering cross sections shipped in this auxiliary module.

Local runtime classification: `PYTHON_PASS`; `CPP_PASS` was not probed (not needed); native subagent `NOT_EXPOSED`. Wolfram and mpmath independent calculations are different algorithms, not different authors. Original GL2022's raw interpolation/extrapolation remains forbidden and not done.
