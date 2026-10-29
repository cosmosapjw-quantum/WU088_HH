# WU R29 local clean replay

No network / native PES / owner integration is required to reproduce *this conditional 5-level source-derived physics slice*. All external exact-byte original inputs are in `archives/WU_R28_GL2022_PHYSICAL_SOURCE_ORIGINAL_20261030.zip` and source-derived text files under `sources/`.

Run in the clean extracted R29 full original archive root:

```bash
PYTHONPATH=. python -m unittest discover -s tests -p test_r29.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_r29.py -q
python -m compileall -q src tests
python -m src.network --out results
python -m src.counterfactual
python tests/independent_mpmath.py
```

Expected: 20/20 standard, 20/20 -O; 210 model cases; 2100 restricted H2(v'=0) product-branching cells; 14 explicitly nonthermal down-only counterfactual rows; 210 high-precision independent algorithm recalc. Source identity failure and domain failure must be explicit. Physical source papers: GL2022 DOI 10.1063/5.0128598; published A from Leiden 2021 HD via REC161; historical CDMS2011 v2 text via REC162; 1984 R3 lab through REC163 DOI 10.1139/p84-213. Original source uncertainties and covariance are not inferred from printed digits.