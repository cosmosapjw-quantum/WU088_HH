# Reproduce PHYS23

The package is self-contained for exact downstream algebra and the PDF source. Python 3.11+ and mpmath are required. The retained PHYS22 archive includes its own original data and reproducibility instructions.

```sh
python checks/compute_and_check.py
cd report
xelatex -interaction=nonstopmode -halt-on-error REPORT_KO.tex
xelatex -interaction=nonstopmode -halt-on-error REPORT_KO.tex
```

The checker reads inputs/PHYS22_INTERVAL_RESULT.json and refuses a SHA mismatch. It uses independently written Fraction Gaussian elimination. The imported rate-ratio intervals are the observed current Wolfram bounds; 330 high-precision direct formula evaluations cross-check them without claiming a second full interval proof. It writes results and the current audit with measured runtime.

The exact evaluator requests are preserved in wolfram/numeric_run_v2.wl and wolfram/xact_run.wl. Each runs in a fresh Wolfram kernel. To print the returned association:

```sh
wolframscript -code 'Print[Get["wolfram/numeric_run_v2.wl"]]'
wolframscript -code 'Print[Get["wolfram/xact_run.wl"]]'
```

Those scripts retrieve a pinned public PHYS22 JSON and the official xAct1.3.0 archive, verify their SHA256, and then evaluate. They do not activate a native receiver or run any ODE. The observed result field files are transcriptions of actual tool output, not claims of original terminal-file identity.

The report requires XeLaTeX with kotex, Liberation Serif/Sans and Noto Serif/Sans CJK KR. Fonts are runtime dependencies and are not redistributed.

A successful execution of this package establishes the declared mathematical/prescription/operator result. Physical cross-section uncertainty, a physical omission budget and native-roundoff certification are separately tracked in DECISION.json.
