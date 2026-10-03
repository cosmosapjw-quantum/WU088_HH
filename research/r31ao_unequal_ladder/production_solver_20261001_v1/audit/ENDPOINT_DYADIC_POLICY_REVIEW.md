# Independent endpoint outward-compression review

Result: **Reviewed numerical change preserves a rigorous upper bound.** This closes the arithmetic-component review of the denominator-growth remedy. It does not assert that any actual cutoff meets a final error budget.

Reviewed planner SHA-256: `bba157ff048a8955c25c140f7d44871d9c627c5197c7d115850428a481cbeaf5`.

The earlier reviewed planner `fe979174ac77d962dc9877a7ea39c01950421011e495134b52745bba44a5b4e0` is preserved in `endpoint_tasks/history/planner_before_dyadic.py` with its manifest. Old plans/results retain their old identity. The new policy changes source, plan and task hashes and must not be mixed with those earlier receipts. Native dependency pins and later join contexts must be refreshed accordingly.

## Mathematical argument and implementation

For an exact positive rational q and declared p significand bits, let e=floor(log2(q)), h=2^(e-p+1), and U=ceil(q/h)h. Exact integer bit lengths and one alignment comparison compute e; exact integer ceiling computes U. No floating-point conversion occurs. Since q>=2^e,

`q <= U < q+h <= q*(1+2^(1-p))`.

The inequality is strict at its final upper endpoint for every positive q, including an exact grid point. Zero is handled separately and remains exactly zero. The grid scales with q: tiny positives do not acquire a fixed absolute rounding floor and are never screened to zero.

The evaluator first rounds each positive field majorant and complement mass upward, then rounds the exact positive coefficient product upward, then the cumulative positive sum upward in the stored i,j,k order. Multiplication and addition preserve the upper-bound direction, so every stage remains conservative. Stored coefficients, source parameters and exact-zero decisions are unchanged. The original endpoint engine runs at the same declared precision. This introduces explicit outward enclosure width; it does not reduce source-engine precision, relax an acceptance tolerance or change the target.

`RELATIVE_DYADIC_UPPER_V1` binds the significand bits, source-engine bits, all four rounding stages, zero convention and summation order into the plan/result identity. Result validation checks rounded majorant fixed points and recomputes the rounded product and sequential sum. It continues to assume the source-bound majorant/mass engine output; this is not an independent replay of those engine calls.

The helper rejects nonexact, negative and oversized inputs. Integer input and work caps are 65,536 and 131,072 bits, with checks before shifted allocations. The evaluator additionally bounds serializable integers to 13,280 bits, below Python's default decimal-conversion limit, and preserves the existing wall, memory, call and result limits. Existing source-engine resource refusal remains an inconclusive result with no accepted radius.

## Independent checks

- Fresh endpoint suite: **15 tests passed**, no failures or errors (2.733 seconds).
- Independent exact inequality probe: **1,260 positive cases** across p=16,31,64,128,512, random non-dyadic ratios, exact powers and adjacent values, and exponents from -10,000 through +10,000. Each checked the strict relative inequality, dyadic denominator and idempotence. All passed.
- **7 refusal cases** checked negative, boolean, float, out-of-range precision and oversized numerator/denominator inputs. Exact zero and tiny-positive scale covariance also passed.
- Probe source: `endpoint_quantizer_independent_probe.py`; machine-readable result: `ENDPOINT_QUANTIZER_INDEPENDENT_PROBE.json`.

These are synthetic arithmetic checks, not 1,260 scientific tasks or an actual HH/native run. Actual bounded candidate runs may now test the revised policy's feasibility under their separately declared scope. Full endpoint coverage, interior evaluation, assembly and final scientific admission remain separate.
