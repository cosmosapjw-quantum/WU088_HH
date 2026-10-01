# Independent endpoint-task component review

Result: **No unresolved blocking defect found in the reviewed final endpoint component.** Review is limited to the conditional endpoint task planner, executor boundary and arithmetic evidence contract. It does not certify a final D matrix or scientific decision.

Reviewed `endpoint_tasks/planner.py` SHA-256: `fe979174ac77d962dc9877a7ea39c01950421011e495134b52745bba44a5b4e0`.

The reviewer read the new planner/tests, immutable Frozen107 adapter, endpoint engine, assembly and callback sources, root AGENTS.md and its required documents. The reviewer did not modify implementation files, run actual HH tasks or compile native code.

## Findings and dispositions

- **Fixed requested-task binding gap:** the subprocess result was originally checked against its own task index, allowing a valid result for a different task to be accepted for the requested output. Final `run_task` requires equality to the requested index. The swapped-worker-result refusal regression passes.
- **Fixed resource-status loss:** the original subprocess boundary discarded every exit-2 result, relabeling a valid resource-limit result as generic execution failure. Final code permits only exit 0/2 with the corresponding validated success/inconclusive status, preserving resource-limit evidence. The regression passes.
- **Explicit trust boundary:** `validate_result` validates binding, coverage, reported arithmetic, nonnegativity and sums. It does not independently recompute the field majorant or complement-mass engine result. A self-rehashed fabricated set of such values is therefore not a replayed proof. Final results and coverage explicitly state `SOURCE_BOUND_ENGINE_OUTPUT_ASSUMED_NOT_INDEPENDENTLY_REPLAYED` and `IDENTITY_AND_REPORTED_ARITHMETIC_ONLY`. This condition must remain visible through later joining and assembly. Default validation must not silently launch another 2,592 actual HH calculations.

## Source and numerical checks

The canonical index is identical to pinned `assembly.cpp`: active 2 × field 3 × orbital 3 × exponent pair 12 × 12, exactly 2,592 entries. All tasks are ordered by that bijection. The source mapping uses the exact selected exponents, mu=1, z=3/4, displacement (-2,0,-3/4) on the selected side, and the stored v on the same phase side. Field and orbital order matches O/G1/G2 and s/px/pz.

The donor scan uses `(i*9+j)*9+k` over all 729 stored slots and omits only coefficients that are exactly zero. Signed real dyadic coefficients are retained in the plan; the endpoint bound uses their exact absolute values. For each task it sums `abs(c_ijk) * C_F(k) * complement_mass(i,j)`. Caching is valid within a task because all geometry, orbital and field parameters are fixed. The complement is the pinned disjoint accounting `(outside_t × all_u) union (inside_t × outside_u)` and uses `E_t W_u + J_t E_u`; it does not double count endpoint corners. This is the unnormalized primitive endpoint component only.

Pinned scope is rebuilt from the original NPZ bytes on validation through the immutable adapter. A self-asserted pinned record or altered archive cannot substitute for that decoding. The plan binds source hashes, exact record, window, resource caps and every task, then recomputes the whole expected plan. Duplicate, missing or mixed-identity results are rejected or reported incomplete. Successful coverage is explicitly conditional endpoint coverage, never a full-domain certificate.

The imported API has cooperative work/time limits; the CLI isolates each selected evaluation under address-space, CPU and external wall limits. Inconclusive execution has no endpoint radius. Output and explicit resume paths are create-only/identity checked. No precision or tolerance relaxation was found.

## Executed verification

Fresh `python -B -m unittest -v test_endpoint_tasks`: **12 tests passed** in 3.112 seconds, no failures or errors. The reviewer observed the intermediate resource-status red test before the author's fix and the final green suite. These are component/synthetic checks only; no actual donor endpoint run was performed by this reviewer. A separately authorized bounded actual task may establish evidence for that selected task only and cannot close 2,592-task coverage or interior/assembly admission.

## Subsequent outward-policy revision

The source hash and 12-test findings above describe the preserved pre-dyadic implementation. The later planner `bba157ff048a8955c25c140f7d44871d9c627c5197c7d115850428a481cbeaf5` adds `RELATIVE_DYADIC_UPPER_V1` to control denominator growth while preserving rigorous upper bounds. It retains both fixed boundary findings and the conditional trust contract. See `ENDPOINT_DYADIC_POLICY_REVIEW.md` for the independent mathematical/code review, fresh 15-test result and 1,260-case exact inequality probe. Old source/history hashes were checked byte-for-byte.

## Final capped-interior policy

A concrete fixed-panel growth finding led to a final upper-bound tightening at planner `53fe8cea32fb24efe9ef2682f480d63595db2bf32525ed57f46df391fe3eb4e6`. The inside-t mass is bounded by the minimum of its panel majorant and an independently valid full-positive-axis majorant. See `ENDPOINT_INTERIOR_MASS_CAP_REVIEW.md` for the proof, source mapping and focused verification. This supersedes the uncapped policy for new attempts while preserving its historical evidence.
