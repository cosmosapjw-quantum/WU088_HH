# Codex handoff: R31AO authority-compliant unequal order ladder preflight

Repository: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31ao-unequal-order-ladder-20260930`
Base: `research/r31an-reference-certification-20260930`
Pinned parent: `5f2fb0e87d6cf42cd1dd7e9f26b902e06c04b1cf`
Parent tree: `4f53b7220c453aaf3a93efb772316bec8c925109`

목표는 blocked B144/B192/B256 ladder를 producer 변경 없이 source-authorized B128/B160/B192 unequal ladder로 대체할 수 있는지 NCP에서 닫고, 필요한 경우 B128+B160 one-shot order-study authorization을 pre-output으로 생성하는 것이다.

이번 handoff에서는 science computation을 실행하지 않는다.

## 0. frozen state

R31AK interpolation model freeze 유지.
z=0.75 B192 existing direct output 재사용.

R31AN 상태 유지:
- SOURCE_ACCURACY_BOUND_UNAVAILABLE
- rigorous reference certification blocked
- full-cell/fixed-Q physical invariance/BR01/BR02/review/production gates open.

B256 지원을 위해 OD source를 수정하지 않는다.
B144 frozen grid를 즉석 생성하지 않는다.

## 1. authority audit: B128/B160/B192

Parent R31AN evidence의 hashes를 재확인한다.

Frozen grids:

B128:
7b83cf7baf606cb430b576f3661b81cad6c31a686000974a04ba616e5cc59bc9

B160:
787d2d58c41e8b67d3d0f0273e46af281ac5ef4bb7bcfd1fef09b1cb844e211c

B192:
e1959e1bbb66b5e27410daa3d3bdb0815885919f11af3a014d86a47f15b96301

Verify source:
- h0_backend.py n<=192
- h0_fused.cpp n<=192
- mixed_derivative/run.py frozen_grid_n{n}.npz requirement
- exact_laplace_weights.py intended B96--B192 range.

Create ALTERNATE_LADDER_AUTHORITY.json.

Verdict may be SOURCE_AUTHORITY_COMPLIANT_UNEQUAL_LADDER only if B128/B160/B192 satisfy unchanged OD/JVP/grid contract.

No producer/source mutation.

## 2. existing output inventory

At z=0.75 inventory complete B128/B160:

- O 47x2
- D_col 47x2
- D_row 2x47
- independent dotO 47x2.

Search local runtime/archive member tables and provider metadata.
Title search 0 alone is not absence proof.

Write B128_B160_OUTPUT_INVENTORY.json.
Reuse complete authoritative outputs; do not rerun.

## 3. frozen unequal ladder

Orders:
B128 -> B160 -> B192

Ratios:
r12=5/4
r23=6/5

For each block preserve:
Delta128160 = Q160-Q128
Delta160192 = Q192-Q160

Record:
- raw complex difference arrays
- spectral 2-norm
- Frobenius norm
- max abs
- raw dtype
- hashes.

## 4. conditional observed-order diagnostic

Under conditional scalar/fixed-error-direction model

Q_n=Q_inf+C n^{-p}, p>0,

rho=d128160/d160192 satisfies

rho=((5/4)^p-1)/(1-(5/6)^p).

For p>0 the ratio function is strictly increasing with lower endpoint

rho_min=log(5/4)/log(6/5)=1.2239010857415446...

Classification:

if rho <= rho_min:
POSITIVE_POWER_MODEL_INCOMPATIBLE_NORMWISE

if rho > rho_min:
unique p_cond exists; record
CONDITIONAL_UNEQUAL_RATIO_ASYMPTOTIC_DIAGNOSTIC

Conditional errors:

E192_cond=d160192/((6/5)^p-1)
E160_cond=d160192/(1-(5/6)^p)

Always rigorous=false.

For matrices additionally record direction diagnostics:
- normalized real Frobenius inner product
- best positive scalar fit if defined
- residual after scalar fit

Do not turn these into a new proof threshold.

## 5. finite-order verdict stability

Using B128, B160, B192 separately as finite-order references, replay frozen z=0.75:

PRIMARY:
R31AK vs R31Z

SECONDARY:
R31AK refined vs R31AD coarse

using unchanged E_K/E_Dmax Pareto rules and tolerance.

If all 3 orders preserve both verdicts, record:

B_ORDER_VERDICT_STABLE_OVER_128_160_192

Do not call this continuum/source certification.

## 6. rigorous claim ceiling

Even with clean convergence:

- SOURCE_ACCURACY_BOUND remains UNAVAILABLE
- rigorous reference certification remains blocked
- no interval enclosure
- no special-function/roundoff/assembly bound.

Sensitivity budgets are not source-error estimates.

## 7. future one-shot scope

If B128/B160 outputs are missing AND source authority is closed:

create one bounded authorization transaction at the same geometry z=0.75.

B128:
- mixed OD
- independent JVP

B160:
- mixed OD
- independent JVP

B192:
reuse existing only.

Four producer commands total, two new order nodes.

Create:
- ORDER_STUDY_SCOPE.json
- canonical bytes/hash
- authorization envelope template
- user authorization prompt
- pre-output raw-array comparator/adapters/rules.

Set execution_authorized=false.
Do not execute here.

## 8. tests

Run only new R31AO helper/tests plus compile/replay.
Do not repeat historical suites without need.

Required:
- rho threshold
- p solver recovery
- no positive p below threshold
- conditional E160/E192 formulas
- authority-ladder policy.

## 9. RETURN

RETURN.json:
- current commit/tree
- alternate-ladder authority verdict
- grid/source hashes
- B128/B160 inventory
- unequal-ladder comparator hashes
- conditional diagnostic contract
- finite-order verdict replay contract
- rigorous certification still blocked
- authorization scope/hash if created
- science producer command count=0
- science node count=0
- R31AK frozen/unchanged
- remaining gates.

ordinary non-force publication + create-only Drive/Dropbox backup allowed.
Raw restore 없이는 RESTORE_VERIFIED=false.

Stop after alternate-ladder preflight and optional authorization-scope creation.
