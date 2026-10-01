# Independent native review before backend execution

The original native worker has two material **feasibility** findings. Neither finding establishes a false accepted enclosure; both are conservative rejection paths. Native compilation, achieved HH integral radii, historical ABI admission and production admission remain unproved at this initial review checkpoint.

Scope: `production_solver_20261001_v1/native_driver/{primitive_worker.cpp,driver.py}`, immutable `gap_closure_20261001_g0_g6_v1/{validated_callback,interior_pilot}`, and the existing `ncp64_acceleration_20261001_v1/native_cache` candidate. Repository `AGENTS.md` and its four required documents were read. Old sources were not edited. `INDEPENDENT_SOURCE_PROBE.json` binds the inspected native sources and original FLINT archive/member bytes.

## Findings

### F1 — High confidence: the old positivity margin excludes valid large real endpoints

The worker chooses `min(2^-20, l_t*2^-20, l_u*2^-20)`, while the callback applies that same margin to

\[
\sigma(t,u)=\tfrac12((a+t)^{-1}+(b+u)^{-1}).
\]

For every positive `a,b`, at `t=u=T`, `sigma < 1/T`. The exact independent probe shows that the old margin is already larger than this strict upper bound for the previous W2 and W3 endpoint windows. Thus the old worker cannot evaluate those real endpoints under its own guard, regardless of increased working precision. This is an execution blocker, not evidence against the mathematical target.

The new additive worker change was independently read: include the exact positive lower bound `sigma_min=((a+T_t)^-1+(b+T_u)^-1)/2` before division by `2^20`, retaining the default cap. Since sigma is decreasing in each positive real variable, this is valid on the closed real rectangle. It does not approve a complex trial box; the unchanged callback still checks each computed whole box. Building that margin correction is reasonable. This review statement is source/mathematics evidence, not a compiled result.

### F2 — High confidence source finding; numerical reproduction pending: refinable range failures are global aborts

Pinned FLINT `src/acb_calc/integrate.c` begins with `quad_simple`, an order-zero evaluation on the entire path interval. If this range query is nonfinite, FLINT ordinarily attempts bisection. In the immutable wrapper, `counted_callback` instead stops the shared budget for nonfinite order-zero evaluations, except its explicit speculative-parameter mode. `outer_callback` similarly stops on an order-zero uniform inner result whose enclosure is too wide. A conservative range failure can therefore prevent the adaptive integrator from subdividing a regular path.

At 128-bit midpoint precision, the W3 dynamic range `[2^-8,2^192]` also cannot be represented as a narrow-endpoint-preserving single initial interval ball. A reciprocal integrand on this positive path is a small analytical reproduction, independent of HH. `refinable_interval_probe.cpp` compares the old wrapper against direct FLINT and `log(b)-log(a)` with bounded evaluation, queue and degree settings. The probe has **not yet been compiled or run** at this checkpoint. W2 is not used for this particular reproducer: its endpoint ratio can fit within 128-bit midpoint precision, so a claim that it must lose the positive lower bound would be too strong.

Do not change exception semantics solely from this initial source finding. First execute the analytical reproducer and the authorized small actual `[1,2]^2` pilot. A later additive change should preserve fatal handling of resource/precision/contract failures and allow only refinable enclosure failures to reach the integrator. Alternatively, bounded exact geometric subdivision avoids the largest initial range query; full coverage and outward summation would still be necessary for a full rectangle.

## Correctness checks and limits

| Requirement or risk | Evidence inspected or executed | Result |
|---|---|---|
| Correct inverse-Laplace density polynomial | Independent exact recurrence `U_(i+1)=-d_mu U_i`, starting from `U_0`, compared to all native closed forms `i=0..8` | 9 exact identities pass |
| Holomorphic callbacks for order 1 | Positive real whole-box guards on `t,u,a+t,b+u,sigma`; powers use only these right-half-plane quantities, while the selected 1F1 is entire in its last argument and has positive half-integer second parameter | Source argument consistent; runtime enclosure behavior still untested |
| Native radial and center derivatives | Read `moment`, `geometry` and `spatial`; checked moment derivative factors and Gaussian log-derivative `2a(m-d)`, and first/second center signs | No additional formula defect found by this review; not an independent full theorem certification |
| Nested parameter uncertainty | Whole outer complex box copied into each inner callback; analytic outer trials demand joint positivity guards and a whole-real-inner-path preflight | No midpoint substitution found |
| Absolute/relative tolerance and acceptance | FLINT tolerance requests followed by finite result and both achieved component radius checks; acceptance also requires an unstopped global budget | No tolerance-as-proof substitution found |
| Uniform-inner coarse tolerance | Its wide ball propagates through outer interval arithmetic; only the outer achieved radius authorizes acceptance | Numerically conservative, potentially costly; F2 concerns refusal policy |
| Exact serialization | Dyadic endpoint construction, `arb_get_interval_fmpz_2exp`, exponent/mantissa allocation guards, Python exact-Fraction width check | No IEEE midpoint conversion in acceptance path |
| Shared resource accounting | One FLINT thread; dispatch/call/depth/time limits; external wall/address/output caps | Fail-closed design; actual host behavior still pending |
| Source/input binding | Exact NPZ re-decode, source pins, build identity, binary/backend/linkage identities and explicit task/plan hashes | Source-bound trusted native output; not independent replay |

The generic `joint_holomorphy_proved` boolean is not an independent proof. In this route its justification is the actual callback formula and the branch-domain guards. Likewise a JSON checksum or native executable identity cannot independently establish that the native calculation is mathematically correct. The conditional evidence contract and false scientific/production admission flags must survive joining and assembly.

## Existing cache candidate

The pre-existing cache imports the immutable callback implementation once, memoizes helper results only inside one invocation, and retains the left-associated coefficient/density/spatial product and original ordered sum. It does not key on rounded midpoints, quantize inputs, screen terms, lower precision, or share mutable caches across workers. This is a suitable first performance candidate once compiled equivalence is demonstrated.

For the actual exact Frozen107 archive, the 107 nonzero terms use **8 left-density degrees, 8 right-density degrees and 9 spatial degrees**. The cache therefore reduces the modeled helper calls from 214 density plus 107 spatial calls to 16 density plus 9 spatial calls. This count is not a measured speedup.

`actual_callback_cache_probe.cpp` independently compares the existing baseline and cache using the generated exact Frozen107 loader and canonical geometry. Its planned 72 unique cases cover all 18 active/field/orbital combinations in four configurations: 128-bit real point `(ia,ib)=(0,0)`, 128-bit complex box `(11,0)`, 256-bit real point `(0,11)`, and 256-bit complex box `(11,11)`. Eight selected cases get three alternating paired timings, yielding 88 paired comparisons in total. The required check is exact `acb_equal` and component-dump equality, plus unchanged contracts and complete signed-term coverage. The probe is not yet compiled or executed at this checkpoint. It computes callback values, not HH integrals or NCP throughput.

## Initial verdict

Specification and engineering verdicts are **partial**. The source review supports bounded compilation and small native experiments, with F1 corrected additively and F2 investigated through direct execution. It does not support full compact-window feasibility, all 2,592 primitives, actual D/epsilon/final decision, 64-core performance, or scientific/production admission.
