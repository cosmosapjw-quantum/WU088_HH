# Endpoint cutoff probe: exact observed comparison

Same actual Frozen107 primitive index 0, same geometry/model/term order, precision 128, panels 4. Each attempt was predeclared at 30 seconds and 512 MiB. All three revised attempts returned conditional endpoint bounds; total observed wall time was below 3 seconds. Exact rational bounds and identities are in RESULT.json and W1/W2/W3_RESULT.json. No interior integral or final D error was evaluated.

| Candidate | Lower cutoff | Upper cutoff | Exact binary bracket of reported upper bound | Engine calls |
|---|---:|---:|---|---:|
| W1 | 1/16 | 256 | 2^54 ≤ B < 2^55 | 39 |
| W2 | 1/64 | 18446744073709551616 | 2^95 ≤ B < 2^96 | 39 |
| W3 | 1/256 | 6277101735386680763835789423207666416102355444464034512896 | 2^165 ≤ B < 2^166 | 39 |

The intervals in this table describe the computed majorant B, not a two-sided enclosure of the unknown actual integral error. A larger B does not imply a larger true error.

The original three 128-bit attempts are preserved in ../endpoint_cutoff_probe: W1 failed rational-token validation, W2 exhausted the exact result bit budget, and W3 returned no JSON. Their correction preserves the old planner bytes and applies explicitly bound upward relative-dyadic compression; an independent reviewer checked 1260 exact cases. The source endpoint engine still runs at 128 bits.

Increasing T while retaining four equal-width interior-mass panels is counterproductive for this majorant. The first panel width grows proportionally to T, while its density maximum can remain at a fixed small t. Thus the upper estimate J_t can grow with T and is multiplied by the nonzero lower-u contribution to E_u. This explains a conservative-bound mechanism, not divergence of the target and not an interior integrator failure.

A source-supported next refinement is to cap J_t by a separately proved whole-positive-domain mass bound W_t: J_t_new=min(J_t,W_t), with W_t=lower_mass_bound(i,mu,a,pivot)+upper_mass_bound(i,mu,pivot) at a fixed positive pivot. The interior mass is bounded by each quantity, so their minimum is valid. This changes neither the disjoint complement sets nor normalization. It would require a separately versioned arithmetic policy and new bounded execution evidence; it is not implemented or evaluated in these records.

No arbitrary primitive threshold is treated as a final D budget. Contracted final-D amplification, actual compact-interior feasibility and certificate admission remain unevaluated.
