# R31AO authorized unequal-order study

- Executed commit/tree: `0a099f8436999331791944170bbe6d113e697fb1` / `4db2c3643f976e1ee1294c531bea4a11153576b4`.
- Scope: `b0abd297847c17741b29a67fae02b9cfd5ddb3fbbe676163867675928cf54a4c`. First scientific checkpoint consumes the one-shot authorization.
- Four original stages completed in order, exit 0; 144 pair checkpoints per stage. Two new order nodes, one existing geometry z=0.75. B192 reused without producer execution.
- Frozen comparator invoked once, exit 0: `B_ORDER_VERDICT_STABLE_OVER_128_160_192`.

| Finite reference | PRIMARY R31AK vs R31Z | SECONDARY refined vs coarse |
|---|---|---|
| B128 | PARETO_SUPPORTED_AT_SELECTED_HOLDOUT | REFINED_PARETO_SUPPORTED_AT_Z075 |
| B160 | PARETO_SUPPORTED_AT_SELECTED_HOLDOUT | REFINED_PARETO_SUPPORTED_AT_Z075 |
| B192 | PARETO_SUPPORTED_AT_SELECTED_HOLDOUT | REFINED_PARETO_SUPPORTED_AT_Z075 |

Primary labels above are the exact frozen comparator labels; they denote relative support at z=0.75 only. All mandatory model errors and direct/candidate metric-identity residuals are in `FINITE_ORDER_REPLAY.json` and `RETURN.json`.

## Conditional diagnostics and direction

| Block | rho | p_cond | E192_cond | Real Frobenius alignment |
|---|---:|---:|---:|---:|
| O | 81.11871366015237529 | 19.629570706981212 | 7.4877069024078e-11 | -0.23585613893259104853 |
| dotO | 90.86898531689985174 | 20.143574370319584 | 1.219639574795615e-11 | -0.6218401272115578015 |
| D_col | 82.900872916121762825 | 19.728013784843824 | 3.8126817546974886e-11 | -0.21689966695018013967 |
| D_row | 87.989754121387229395 | 19.997805273925223 | 4.054468961124895e-11 | -0.3645322158853154079 |
| K | 84.96363475991639741 | 19.839330316254745 | 3.938851450619672e-11 | -0.29391720089858802768 |

Every direction result is `NO_POSITIVE_SCALAR_MINIMIZER`. The represented increments have negative real Frobenius alignments; stable positive matrix error direction is not established. Formal normwise p/E roots retain `CONDITIONAL_UNEQUAL_RATIO_ASYMPTOTIC_DIAGNOSTIC`, `rigorous=false`; they do not establish actual quadrature order or source error.

Raw differences and their spectral/Frobenius/maxabs norms retain complex256/longdouble arithmetic. Model-error comparisons retain original complex128 diagnostic arithmetic. Per-array byte hashes, source/dtype identities and the raw difference NPZ are preserved.

## Unchanged claim ceiling

`SOURCE_ACCURACY_BOUND_UNAVAILABLE` and `RIGOROUS_REFERENCE_CERTIFICATION_BLOCKED_BY_MISSING_ERROR_BOUND` remain. Common implementation bias may cancel in order differences. Conditional estimates, decision tolerance, metric residual and bridge tolerance are not reference-error upper bounds. Finite-order verdict stability is separate from rigorous certification.

No interval-wide, all-cell, transition, trajectory, full-cell, fixed-Q physical invariance, BR01/BR02, independent project review, H-skip or production admission. No new interpolation knot or model change; z=0.75 remains held out.

Raw restore was not performed: `RESTORE_VERIFIED=false`. Provider ACK, metadata-size checks, content hash and restore verification are reported separately in the backup receipt.
