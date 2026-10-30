# WU088_HH R35 physical-data report

## Primary science generated

- Conditional source-qualified GL2022 HD5 photon first and second energy cumulants: 3,528 physical rows, actual computed CSV.
- At 324 previously bounded z-balance roots: new 324 source-derived second-cumulant entries (root standard deviation min 1.8561926925252014e-21 J, max 1.6932528957686704e-20 J). Mean balance does not imply stochastic radiative inactivity; no actual sky-intensity observable is claimed.
- H2 J'=0..9 product probability interval atlas: 35,280 rows, with unknown high-J first-quench landing mass explicit. Source-selected fraction 0.2363696354–0.3686497092; 63–76% untracked, which prevents extrapolation to unconditioned full physical model.
- Source/executable: unmodified 8,412,812 byte R34 original zip preserved, original R33 and R32 recursively immutable.

## Evidence and independent checks

- Python FCS 9/9 normal and 9/9 `python -O` tests and compileall PASS, tests include exact two-state Bernoulli toy, tilt derivative finite difference, positive variances, zero-mean roots, missing mass bounds, no-external-radiation limit and original R34 mean identity.
- Wolfram standalone symbolic 2-state FCS calculation returned exactly `phi=1-p+p exp(s)`, d/ds = p, variance p(1-p), both differences 0.
- Same-author adversarial review found that using the wrong dimensionless energy scale for the derivative finite-difference probe caused a test failure; corrected E0=100*100*h*c J and retested. Using a too-large tilt (e.g. s=0.003 with the originally incorrect scaling) crossed the resolvent convergence radius and yielded nonsense; bounded finite-difference derivative now uses s=1e-4 at the correct reference unit. Neither issue changes the physical J, J2 moments in source outputs.
- A separate-author blind referee was not run because native subagent dispatch is not exposed; original R6/C9 remains NOT_RUN. The present skepticism pass is a same-author check with independent Wolfram computation.

## Scientific admission

RESULT: NUMERICALLY_CHECKED / SOURCE_RESTRICTED. Implementation tests PASS. First two photon cumulants within 5-state absorbing model are derived, not empirical observations. R35 auxiliary scope 1/1; central WU canonical 34/49 (+0), R/C stage status 18/20 (different-author R6 and C9 not run). No full Q, native PES, owner ACK, EMAA equality or physical cosmological transfer.

## New external sources

- The 2026 REC-HD PR #169 now includes original 2011 CDMS v2 HD.fit/.par/.lin/.egy files and official 2026 Neufeld HD rate source. This was read only and does not automatically authorize transport into WU's accepted data or imply full-precision covariance.
- EMAA official HD-H+ 171 transitions x25 temperatures: https://doi.org/10.17178/emaa_hd_rovibration_805a7aa5; official interactive access https://emaa.osug.fr/details/HD (Rovibration, H+, Download). Original numeric ASCII NOT_ACQUIRED.
