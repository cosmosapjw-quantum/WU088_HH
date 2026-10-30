# WU R34 | source-first conditional two-stage physics, clean replay

Requires Python>=3.10, numpy, scipy. The source ZIP deliberately contains **exact unmodified original R33 full SOURCE ZIP** nested under `archive/`, which itself holds the full immutable R32 source. The code verifies original input ZIP SHA256, ZIP CRC and critical R33 numeric output hashes, safely restores R33 original material to `parents/R33` on the first run (this extracted directory is a disposable worktree), and generates the four physical tables deterministically.

```bash
python3 -m src.bridge --out results
PYTHONPATH=. python3 -m unittest discover -s tests -p test_bridge.py -v
PYTHONPATH=. python3 -O -m unittest discover -s tests -p test_bridge.py -v
python3 -m compileall -q src tests
```

Use `python3 src/bridge.py --out results` as an alternative from the extracted package root. Source-only archive, no external live HTTP or credentials needed. The 2005 K malformed original R32 source is not included; no data are invented. The scenario is restricted to R32 first vibrational quench ending v0 J≤4 followed by R33 chemistry and blackbody. For `CMB_label=OFF`, spontaneous radiative emission still exists. The 504 root tests are endpoint-sign-bracketed on z=0..300; non-bracketed does not imply absent root.

Reproducibility: verify the generated file SHA256 against `evidence/OUTPUT_SHA256.json`; this is a byte-deterministic package for the tested Python environment, not a claim about arbitrary floating point/software versions. No additional physics source is inferred by including an original parent ZIP.