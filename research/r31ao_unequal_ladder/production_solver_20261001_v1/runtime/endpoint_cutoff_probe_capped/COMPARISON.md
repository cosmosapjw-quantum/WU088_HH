# Final bounded endpoint comparison

All candidates use the same actual Frozen107 input, primitive index 0, fixed source geometry/model, 128-bit exact endpoint engine and four mass panels. Every successful result is a conditional upper bound on this primitive's omitted positive-domain contribution, not a final D error. Each round predeclared at most three 30-second/512MiB attempts under a90-second budget. The final round completed in2.119 seconds, with55source-engine calls and107stored terms per candidate.

| Window | Lower cutoff | Upper cutoff | Before whole-mass cap | After whole-mass cap |
|---|---:|---:|---|---|
| W1 | 1/16 | 256 | 2^54 ≤ B < 2^55 | 2^54 ≤ B < 2^55 |
| W2 | 1/64 | 2^64 | 2^95 ≤ B < 2^96 | 2^38 ≤ B < 2^39 |
| W3 | 1/256 | 2^192 | 2^165 ≤ B < 2^166 | 2^-21 ≤ B < 2^-20 |

These exact binary brackets enclose the computed majorant B, not the unknown actual error. The exact rational bounds and ratios are in COMPARISON.json; plan/input/source/result hashes remain in the original records.

The final W3 endpoint bound satisfies `1/2097152 <= B < 1/1048576`. This is a single primitive endpoint component. It is not a chosen final-D goal or evidence of achievable interior accuracy. The compact domain extends to `2^192` in both coordinates and has not been integrated. Normalization, contraction, phase and final spectral-error propagation may amplify entry errors.

The capped formula is `E_t*W_u + min(J_t,W_t)*E_u`, with W_t computed from the same i,mu,a at positive pivot1. It keeps the original disjoint integration regions. The minimum of two independently valid inside-mass upper bounds is valid. Fixed-panel J_t inflation can therefore no longer force the second product to grow without the independent full-mass bound. Outward dyadic compression at the declared precision remains applied; input coefficients and source engine precision are unchanged.

Evidence is preserved in three distinct rounds: first3attempts failed representation/resource limits; the next3 used outward dyadic compression and returned valid but increasingly wide bounds; the final3 additionally capped J_t and returned the bounds above. Including the original coarse task0 run, there were10actualendpointattempts,7successfulconditionalbounds. Historical source copies and hashes were retained before each change. No native, producer, interior or comparator run occurred here.

The requested cutoff exploration ends here. Remaining B05 work is actual compact-interior feasibility and final contraction/error budgeting under the fixed model, not another unbounded endpoint scan. No fullD/epsilon/Pareto/scientific admission is asserted.
