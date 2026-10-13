# Reproduction

## Local checks (no network, no ODE or atomic scattering)

Run from the extracted package root with Python3 and mpmath installed:

```bash
python checks/build_outputs.py
python checks/close_evidence.py
```

Expected:58 passing checks followed by4 independent CAS endpoint comparisons,0 failures. The package retains the predecessor23 input tree used by these checks. Weight endpoints in the Python file are explicitly selected transcriptions of actual Wolfram output; they are not an independently generated interval implementation. Independent mpmath gamma-function evaluation and quadrature check them, while the continuous-temperature coverage follows the report's monotonicity proof.

## Symbolic and interval checks

The two normalized Wolfram sources are mathematically equivalent to the actual compact evaluator submissions. Use a licensed Wolfram runtime:

```bash
wolframscript -code 'Print[Get["wolfram/verify_kernel_xact.wl"]]'
wolframscript -code 'Print[Get["wolfram/verify_endpoint_cones.wl"]]'
```

The first source downloads the official pinned xAct1.3.0 archive and checks its SHA256. It requires network access. The second has no external dependency. Actual observed summaries and source hashes are in wolfram/OBSERVED_RESULTS.json. A command's exit code alone is insufficient:inspect the returned status and residual fields.

## Report

```bash
cd report
xelatex -interaction=nonstopmode -halt-on-error REPORT_KO.tex
xelatex -interaction=nonstopmode -halt-on-error REPORT_KO.tex
```

Required fonts are named in the TeX source; no font binaries are distributed. Actual PDF compilation/render checks are recorded in checks/PDF_VALIDATION.json. The report uses LaTeX/Korean text packages and xelatex.

## Physical input

NEXT_INPUT_CONTRACT.json intentionally keeps calibrated cross sections/slopes/tail and scientific omission budgets null. The provided uniform1e-18cm2 cap and endpoint witness are specified mathematical examples. A physical application must first provide a matching channel/event/frame and full-support envelope. The local functions are research verification utilities, not a production chemistry callback.
