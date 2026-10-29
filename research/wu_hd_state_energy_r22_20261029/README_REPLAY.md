# WU R22 scoped spectroscopy data audit

Python only; no physical source replacement. From folder root:
```
python -m unittest discover -s tests -v
python -O -m unittest discover -s tests -v
python src/state_energy.py --source SPECTROSCOPY_SOURCE.json --out results/new_result_create_only.json
```
Do not overwrite result files; `open('x')` intentionally fails when present. The package includes only source-decimal literals, links and code. Original R21 GL2022 PDF remains in its immutable source ZIP SHA5ace176... supplied separately; not republished here. This is NOT full molecular chemical provenance, and not an independent-author R6/C9 audit.
