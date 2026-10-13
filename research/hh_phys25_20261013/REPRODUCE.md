# Reproduction contract

Python3 with mpmath and sympy is used. The original environment is recorded in checks/FINAL_VALIDATION.json. No compiled native solver, previous ODE run, or private data is required.

```
python checks/final_validate.py
python checks/build_results.py
# Optional regeneration of the new interval calculation only:
python checks/rebuild_intervals.py
```

The first two commands re-evaluate direct source integrals and certificate closure. The optional third writes a separate replay file rather than overwriting the adopted record. Interval arithmetic is built from supported elementary operations and E1's explicit convergent series with a proved tail bound. Source partial rates are defined only between1 and2 source Rydberg thresholds; no tail fit is implicit.

`wolfram/verify_sheldon.wl` is the exact saved input submitted to the cloud evaluator. It downloads xAct1.3.0, checks archive SHA256, loads xTensor and evaluates the returned identities/numbers. To replay locally, call `wolframscript -code 'Print[Get["wolfram/verify_sheldon.wl"]]'` from this directory with networking and a licensed Wolfram installation. No font files are distributed.

PDF source restore: https://ntrs.nasa.gov/api/citations/19660002855/downloads/19660002855.pdf ; SHA25661d91628383e2d4932592ba5dedc32381fb36a2f63ee99cdaae430f9c86d5a9f. Wolfram `Import[path,"PageImages"]` was used to inspect pages4,5,6,7,8,9,10. The source PDF itself is not duplicated in this package. Equations(2)–(18) and the tagged-electron definitions on printedp3 are the authoritative reconstruction target.

Build PDF with XeLaTeX and locally installed Liberation/Noto CJK fonts:
```
cd report
xelatex -interaction=nonstopmode -halt-on-error REPORT_KO.tex
xelatex -interaction=nonstopmode -halt-on-error REPORT_KO.tex
```

Full parent archive has its immutable identity in inputs/PARENT24_IDENTITY.json. Only the exact scientific coefficient inputs used here are copied under inputs/local23/ and inputs/phys22/; build_results.py reads these exact two copied files directly. Every distributed payload is manifest-bound.
