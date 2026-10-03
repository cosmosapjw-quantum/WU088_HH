# DECISION_BOUND_DERIVATION

## Exact target, represented arrays and diagnostic arithmetic

C*=D_col* and R*=D_row* are the fixed Frozen107 continuous source blocks defined in SOURCE_FUNCTIONAL_MAP. C_192,R_192 are exact lifts of the archived raw longdouble complex arrays. Hypothetically let certified nonnegative spectral-norm bounds satisfy

\[
\|C_{192}-C^*\|_2\le\epsilon_C,\quad
\|R_{192}-R^*\|_2\le\epsilon_R.
\]

No such numerical bounds have been obtained: epsilon_C=null, epsilon_R=null. All following bounds are mathematical implications, not acquired certificates.

Frozen model predictions are interpreted as their represented archived arrays, with unchanged hashes. Candidate K is its stored prediction array. This analysis does not recompute a model or replace represented predictions by ideal analytic interpolation. Define exact raw K_192=(C_192-R_192†)/2 and exact target K*=(C*-R*†)/2. Adjoint isometry and the triangle inequality give

\[
\boxed{\epsilon_K\le(\epsilon_C+\epsilon_R)/2}.
\]

For a candidate P,

\[
E_{Dmax}(P;C,R)=\max(\|P_C-C\|_2,\|P_R-R\|_2).
\]

The reverse triangle inequality for each norm and the Lipschitz property of max imply

\[
|E_{Dmax}(P;C_{192},R_{192})-E_{Dmax}(P;C^*,R^*)|
\le\boxed{\epsilon_{Dmax}=\max(\epsilon_C,\epsilon_R)}.
\]

The analogous K error changes by at most epsilon_K. For two candidates, the error gap changes by at most twice that metric bound, including the case where the maximizing row/column block changes.

## Eta: a separate diagnostic boundary

The archived raw bits are the boundary between source epsilon and diagnostic eta. Source epsilon includes every producer error before those bits: input interpretation for I_F, quadrature, stored/generated weights, special functions, Gaussian arithmetic, normalizations, weighted sums, orbital contraction, phase and final D assembly. None of these is charged again to eta.

The frozen `compare_order_study.compare_frozen` lines 99–101 casts raw arrays to complex128, constructs K after that cast, then calls the frozen secondary norm routine. `compare_secondary_refinement.n2/errors`, lines 25–37, uses complex128 subtraction, spectral norm via SciPy and float scalars. Eta is an upper bound for the gap's discrepancy from the exact norm gap using represented predictions and exact raw arrays. It must account for raw-to-complex128 conversion; diagnostic K addition/subtraction and division; any prediction conversion; norm-input subtraction; spectral-norm/SVD arithmetic; scalar gap arithmetic and published decimal transcription. Max introduces no additional real arithmetic beyond its already enclosed arguments. The original metric identity residual is not an eta certificate.

One possible non-overlapping definition is eta_gap,j=eta_error,A,j+eta_error,B,j+eta_scalar,j, with each eta_error comparing the complete diagnostic norm pipeline to the exact represented-array norm and eta_scalar covering only subsequent scalar subtraction/serialization. If implementing a finer split, a cast error contributes once through the norm Lipschitz bound, not again as an SVD input uncertainty. Frozen predictions are the comparison target, so their interpolation residual is not a diagnostic roundoff term. The real Pareto thresholds below implement the original rule; any eventual machine-predicate certificate must also enclose floating addition/subtraction at its decision boundaries. No eta number is currently certified: eta=null, not zero.

## Connection to the original Pareto rule

For PRIMARY let the published gap g_j=E_R31Z,j-E_R31AK,j. For SECONDARY let g_j=E_R31AD,j-E_R31AK,j. Let eta_j bound the absolute gap arithmetic discrepancy. Then

\[
\boxed{\mathrm{lower\_gap}_j=g_j-2\epsilon_j-\eta_j
\ \le\ E_{other,j}^{true}-E_{R31AK,j}^{true}}.
\]

For each comparison separately, both lower_gap_j>=-tol and at least one lower_gap_j>tol suffice for support under the unchanged two-metric Pareto rule, tol=1e-10/t_a. Requiring both lower gaps strictly >tol is more conservative and sufficient; it is not a replacement decision rule. The numerical frozen verdicts remain unchanged regardless of this supplementary derivation.

## Exact decimal budget arithmetic

The following published decimal gaps are transcribed as exact decimals solely to derive symbolic budgets. Publication/binary representation discrepancies would be covered by eta in an actual certificate.

| Comparison | Metric | Published gap (/t_a) | Hypothetical strict budget (g-tol)/2 at eta=0 (/t_a) |
|---|---|---|---|
| PRIMARY R31AK vs R31Z | K | 0.31982343565606726 | 0.15991171777803363 |
| PRIMARY R31AK vs R31Z | Dmax | 0.33345694057636703 | 0.166728470238183515 |
| SECONDARY refined vs coarse | K | 0.05713242012648218 | 0.02856621001324109 |
| SECONDARY refined vs coarse | Dmax | 0.08782058637980173 | 0.043910293139900865 |

If epsilon_C<=epsilon and epsilon_R<=epsilon, both propagated metric bounds are at most epsilon. With hypothetical eta=0, epsilon strictly less than 0.02856621001324109/t_a is sufficient for both metrics in both comparisons to improve strictly beyond tol. Equality at the limiting K budget would only give lower_gap_K=tol and does not meet that strict condition. This is a design target, not actual source/reference error, a probability, or an acquired upper bound. For nonzero eta use (g_j-tol-eta_j)/2 and require a positive resulting budget. EXACT_DECIMAL_BUDGETS.json records Fraction arithmetic only; it does not run scientific arrays or norms.

## Positive-direction single-term interpretation

Let A=Q160-Q128, B=Q192-Q160. The original direction diagnostics give negative normalized real Frobenius alignment for O,dotO,D_col,D_row,K. Under a single-term model Q_n=Q_inf+C n^(-p), p>0, both increments are the same matrix direction with A=alpha B, alpha>0. If s=Re Tr(A†B)<0, then for every alpha>0,

\[
\|A-\alpha B\|_F^2=\|A\|_F^2-2\alpha s+\alpha^2\|B\|_F^2>\|A\|_F^2.
\]

The infimum normalized positive-ray residual is one as alpha approaches zero from above; no positive minimizer attains it. Thus the represented triplet does not fit that positive-direction single-term interpretation. This does not identify the cause of the negative alignment, prove divergence, or establish a producer defect. All original conditional p/E numbers and machine labels remain byte-preserved; they are not actual order estimates or reference-error bounds. Common implementation bias can cancel in order differences. The original finite-order result remains B_ORDER_VERDICT_STABLE_OVER_128_160_192, with one shared geometry and no newly independent geometry validation.
