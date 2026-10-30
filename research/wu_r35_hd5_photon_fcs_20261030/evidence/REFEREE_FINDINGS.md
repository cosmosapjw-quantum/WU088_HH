# R35 adversarial science review (same author, independent symbolic tool)

Independence: native subagents NOT_EXPOSED; R6_DISTINCT_AUTHOR=NOT_RUN and C9_DISTINCT_AUTHOR=NOT_RUN. This report must not be counted as an external blind referee.

1. **Tilt sign / diagonal / probabilistic semantics**: check tilted generator leaves diagonal invariant and weights only true radiation transitions. Exact two-state Wolfram Bernoulli reduction independently reproduces q^T resolvent. Python analytically differentiated generator agrees with directly tilted resolvent for representative real-source points. **CLOSED for restricted model**.
2. **Unit/scaling error detected in verifier**: initial reference E0 label claimed 100 cm^-1 but numeric factor actually 1 cm^-1. This broke the 2-state Bernoulli test. Corrected E0=100*100 hc J. Physical output J, J^2 uses epsilon=100 hc nu and was unaffected. **FIXED / regression PASS**.
3. **Finite-difference convergence of MGF**: earlier trial with large lambda yielded absurd signs because the MGF resolvent approached/outcrossed its domain. Correct dimensionless reference plus small s=1e-4 gives first/second derivatives within predeclared 1e-5/1e-4 relative criteria for three sources. **CLOSED with bounded test**.
4. **Unmodelled J>4 mass**: R34 uses 23.6%–36.9% first-quench landing into v0 J0..4; omission is 63.1%–76.4%, not small. Product probability bounds [p,p+1-w] are in source-selected two-stage trajectory partition ONLY. There is no validated full-network photon-variance bound. **FULL CHEMISTRY HOLD**.
5. **Energy representation seam**: R32 CDMS-to-R33 Sung seam is not radiation/bath heat. R35 uses R33 line energies consistently and does not reclassify seam. **CLOSED scoped**.
6. **Radiative balance root uniqueness**: only 324 root candidates certified with opposite endpoint signs; zero means with positive variance do not imply LTE, physical thermalization or global uniqueness. **WIDER CLAIM HOLD**.
7. **Independence / source-origin**: REC #169 now holds original CDMS v2 historical files, but EMAA HD-H+ 171x25 original bytes and high-precision spectroscopy covariance are missing from WU input. Different-author R6/C9 not run. **PROMOTION HOLD**.

Verdict: PARTIALLY_CONFIRMED_SAME_AUTHOR, scoped new first and second cumulants NUMERICALLY_CHECKED. No new canonical DAG node. No strong no-go theorem admitted.
