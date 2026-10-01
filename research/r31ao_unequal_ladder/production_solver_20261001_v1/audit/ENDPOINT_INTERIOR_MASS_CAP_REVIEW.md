# Independent review of the final interior-mass cap

Result: **The refinement is a valid upper-bound tightening.** Reviewed planner SHA-256: `53fe8cea32fb24efe9ef2682f480d63595db2bf32525ed57f46df391fe3eb4e6`.

The observed increase in a fixed-panel interior-mass estimate at very large T motivated this bounded change. It does not alter the immutable endpoint engine, source target, precision, coefficients, normalization or disjoint endpoint accounting. Prior attempts and source versions remain historical evidence; their plan/result identities must not be mixed with the new policy.

Let f_i(t) be the same nonnegative mass majorant used by the endpoint engine for the selected donor index i and fixed task parameters mu,a. The inside mass obeys

`integral_inside f_i <= J_t` and `integral_inside f_i <= integral_positive_axis f_i <= W_t`.

Thus `min(J_t,W_t)` remains an upper bound for the inside mass. The planner obtains W_t from `lower_mass_bound(i,mu,a,1) + upper_mass_bound(i,mu,1)` with positive split point 1. Upward compression of this sum preserves validity. The cache is local to one task, so indexing it by i cannot mix different a or mu values.

The refined complement formula is

`E_t * W_u + min(J_t,W_t) * E_u`.

E_t, E_u and W_u remain the original values. E_t is not replaced by an inside bound. The two integration sets stay `(outside_t × all_u)` and `(inside_t × outside_u)`, so no endpoint region is omitted or counted twice. All multiplication/addition operands are nonnegative. The existing upward dyadic compression therefore continues to preserve the final upper bound.

`RELATIVE_DYADIC_UPPER_CAPPED_INTERIOR_V2` binds the minimum formula, full-axis split, additional stage and existing precision/order into the plan/result identity. The majorant values continue to have the explicit source-bound, not-independently-replayed evidence contract. Positivity alone is not treated as proof of a supplied majorant.

## Focused verification

- Reviewer reran the two new tests and changed policy-binding test: **3/3 passed**.
- The synthetic engine regression compares T=2^20 and T=2^100: the uncapped fixed-panel quantity grows by more than 2^70 in that fixture, while the capped quantity does not increase. This is a concrete regression fixture, not a theorem of monotonicity for every parameter/cutoff choice.
- Independent exact rational probe: **108** combinations of true inside mass, two valid upper-bound slacks and nonnegative other factors satisfy both the required lower containment and the two candidate upper inequalities. **3** invalid whole-mass inputs were rejected. Machine-readable evidence: `ENDPOINT_INTERIOR_MASS_CAP_PROBE.json`.
- The author recorded a fresh complete **17-test** endpoint suite in `INTERIOR_CAP_GREEN.log`; the reviewer did not repeat unrelated tests.

The separately authorized final three bounded same-window actual probes may test practical behavior. This review does not establish a required final tolerance, full primitive coverage, native interior feasibility, final D enclosure or production/scientific admission. No actual HH task was run by this reviewer.
