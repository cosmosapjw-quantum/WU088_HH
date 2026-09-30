# Codex handoff: R31AN B192 reference-certification preflight

Repository: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31an-reference-certification-20260930`
Base: `research/r31am-post-z075-stop-policy-20260930`
Pinned parent: `34eaa2ab52fc782825235629dade382b2322d2a4`
Parent tree: `f2a43200e79f45b5cfd57b81afd4da99c7d402c3`

목표는 frozen R31AK model을 더 수정하지 않고, z=0.75 B192 direct reference의 수치 정확도를 인증하기 위한 order ladder와 rigorous-source gate를 pre-output으로 잠그는 것이다.

이번 handoff에서는 새 B-order scientific computation을 실행하지 않는다.

## 0. 시작 identity

현재 remote HEAD/tree와 successor diff를 확인한다. reset/force/main merge 금지. R31AK model freeze receipt와 authorized z0.75 RETURN을 읽는다.

Required frozen identities:

- R31AK aggregate `50a5f0eeda63d6e04795e301f6b07a41fd11a4b145e267cfc608261356d49b30`
- eight-node manifest `d978792bef0c3bf2b670d4e73d70dcea391645f38555f1070323037610162ece`
- B192 z0.75 OD `7e7b5782cc698a364aeac608620e56c7bfdc64035ffe5dfee501608dae7970df`
- B192 z0.75 JVP `53569e92875254e897a7e23b55620cca9c5acf9f86124dc0a73198ad41d1df87`
- source accuracy status `SOURCE_ACCURACY_BOUND_UNAVAILABLE`
- interpolation model freeze action `FREEZE_R31AK_LOCALLY_SUPPORTED__PIVOT_TO_REFERENCE_CERTIFICATION`.

Model/knot/training state를 변경하지 않는다.

## 1. producer/source feasibility audit

Recovered runtime/archive source를 read-only로 검사하여 기존 OD/JVP CLI의 `--n` parameter가 n=144 및 n=256을 source modification 없이 허용하는지 확인한다.

Check:
- grid/weights generation source
- radial native source
- exact weight source
- special-function branches
- precision/dtype
- n-dependent caches/array shapes
- hidden n parity/divisibility assumptions
- phase/order convention.

Source가 임의 n을 authority 있게 지원하지 않으면 `REFERENCE_ORDER_INPUT_BLOCKED`로 종료한다. 새 구현을 즉석에서 만들지 않는다.

## 2. existing output inventory

z=0.75에서 B144, B256의 complete mixed

- O
- D_col
- D_row
- independent dotO

가 기존 archive/local/provider에 존재하는지 metadata/member inventory만 수행한다.

Existing complete result가 있으면 identity/hash/source contract를 기록하고 재실행하지 않는다.

없으면 `B144_REQUIRED=true`, `B256_REQUIRED=true` 등으로 기록한다.

Title search 0건을 absence proof로 쓰지 않는다.

## 3. order-ladder contract

Frozen ladder:

`B144 -> B192 -> B256`

Refinement ratio:
`r=4/3`.

B192는 existing direct z0.75 output을 재사용한다.

Future new orders의 required outputs ONLY:

- mixed O 47x2
- mixed D_col 47x2
- mixed D_row 2x47
- independent mixed dotO 47x2.

금지:
- H
- neutral47
- ionic2
- full49
- trajectory
- new interpolation knot
- new geometry
- M3/reference-production side work.

## 4. pre-output comparator

각 block에 대해 direct order differences를 저장:

`Delta_144_192 = Q192-Q144`
`Delta_192_256 = Q256-Q192`.

Record:
- spectral 2-norm
- max abs
- raw dtype
- per-entry complex difference arrays.

Derived diagnostics:

`rho_norm = d192256/d144192`

if positive finite.

If `d144192>d192256>0`:

`p_norm = log(d144192/d192256)/log(4/3)`.

그러나 norm-based p를 actual quadrature order라고 부르지 않는다.

Optional scalar/entry analysis는 error direction/phase를 보존해 별도 기록한다.

## 5. conditional extrapolation diagnostics

Power-model assumption

`Q_n=Q_inf+C n^{-p}`

under fixed scalar or fixed matrix-error direction only:

`E192_cond=d192256/(1-(3/4)^p)`

`E256_cond=d192256/((4/3)^p-1)`.

Status must contain:
`CONDITIONAL_ASYMPTOTIC_DIAGNOSTIC`
`rigorous=false`.

Observed three orders alone do not certify continuum error.

If a mathematically independent proof gives future contraction

`||Delta_(k+1)|| <= q ||Delta_k||`

for all later orders, only then geometric tail bound may be labeled rigorous.

## 6. verdict-stability targets

Existing z0.75 reference-perturbation sensitivity budgets:

PRIMARY R31AK-vs-R31Z:
- K radius open: 0.15991171777803362 /t_a
- Dmax radius open: 0.16672847023818352 /t_a.

SECONDARY refined-vs-coarse:
- K radius open: 0.028566210013241087 /t_a
- Dmax radius open: 0.04391029313990087 /t_a.

Joint target is governed by secondary K:
`0.028566210013241087/t_a`.

These are sensitivity budgets, NOT B192 error estimates.

After future order study, recompute primary+secondary comparisons using B256 as an alternate finite-order reference and report `B_ORDER_VERDICT_STABLE` only if both frozen verdicts remain unchanged.

Do not relabel that as continuum/source certification.

## 7. rigorous source-certification feasibility audit

Read source/math only; no heavy runs.

Decompose potential reference error:

`epsilon_ref <= epsilon_order + epsilon_special_function + epsilon_roundoff + epsilon_assembly`.

Determine whether project source provides enough authority to bound:

- quadrature truncation/order remainder,
- Boys/special-function approximation,
- long-double/binary128 rounding path,
- compensated summation/assembly.

Existing sumabs without outward rounding is diagnostic only.

Existing H B160/B192 anchor comparison is finite-order evidence only and cannot certify mixed O/D/JVP.

If rigorous ingredients are absent, return:
`RIGOROUS_REFERENCE_CERTIFICATION_BLOCKED_BY_MISSING_ERROR_BOUND`.

Do not invent derivative bounds.

## 8. future authorization scope

If B144/B256 are missing and producer support is verified, create a structured one-shot authorization scope for **same geometry z=0.75**, exactly two new orders B144 and B256, with OD+independent JVP at each order.

This is one bounded reference-certification transaction with four producer commands.

Set:
`execution_authorized=false`.

Create:
- `REFERENCE_ORDER_STUDY_SCOPE.json`
- canonical bytes/hash
- authorization envelope template
- user authorization prompt
- frozen comparator/adapters/rules.

이번 handoff에서는 실행하지 않는다.

## 9. stop condition

Return:

- remote identity
- source feasibility verdict
- B144/B256 existing-output inventory
- frozen order-study contract
- comparator/adaptor hashes
- rigorous-certification feasibility
- authorization scope/hash if needed
- science_node_count=0
- interpolation model unchanged/frozen
- source/full-cell/review/production gates.

Ordinary non-force publication + create-only Drive/Dropbox backup 허용.
Raw restore 없이는 `RESTORE_VERIFIED=false`.

Stop after certification preflight. 자동 B144/B256 실행 금지.
