# Codex handoff: R31AH post-z3.5 decision policy

Repository: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31ah-post-z35-policy-20260930`
Base: `research/r31ag-z35-validation-gate-20260930`
Pinned parent: `c6d00e79cfd76366af868a3a550aebbee46135cf`
Parent tree: `6f935a4ac4284ee317c1575554c81ca74f28f11c`

목표는 z=3.5 result를 보기 전에 결과 이후 action tree를 hash-lock하는 것이다. 이번 handoff 자체에서는 z=3.5를 실행하지 않는다.

## 0. start

현재 remote HEAD/tree를 확인하고 후속 commit이 있으면 diff를 읽는다. 기존 raw/source/worktree/provider backup을 보존한다.

읽기:

- `research/r31ah_post_z35/REPORT_KO.md`
- `POST_Z35_DECISION_POLICY.json`
- `post_validation_policy.py`
- parent R31AG `ncp_followup_20260930/RETURN.json`
- parent R31AF preregistration and six-node manifest.

## 1. no science execution

R31AG structured authorization semantics를 변경하지 않는다.

Current user instruction에 valid z=3.5 authorization envelope가 없다면:

- science producer commands = 0
- science node count = 0
- z=3.5 direct output access = false

를 유지한다.

## 2. freeze post-result action tree

Preregistered z=3.5 final verdict 셋에 대해:

### PARETO_SUPPORTED_AT_Z35

- report relative support
- do not admit interval-wide accuracy
- z=3.5 direct residual may then be used as [3,4] local refinement indicator
- if a successor model is actually constructed, relabel z3.5:
  `PRIOR_INDEPENDENT_VALIDATION_CONSUMED_AS_SUCCESSOR_TRAINING`
- successor may refine [3,4] only
- next fresh validation candidate = z=2.5
- do not execute z=2.5 automatically
- do not retune any other cell automatically

### GLOBAL_SUPPORTED_AT_Z35

- `STOP_FOR_MODEL_CLASS_REVIEW`
- no automatic local refinement
- no automatic new validation node
- preserve z2.5 fresh

### TRADEOFF_UNRESOLVED

- `STOP_FOR_MODEL_CLASS_REVIEW`
- no automatic retuning/refinement
- preserve z2.5 fresh.

Write exactly this to `POST_Z35_DECISION_POLICY.json`.

## 3. formula replay

Verify helper/tests only.

For any future z3.5 R31AF midpoint errors E_O,E_K with h_t=2.2358772390338113:

[
O4_{m lower}=384 E_O/h_t^4
]

[
K2_{m lower}=8 E_K/h_t^2.
]

At h_z=1:

[
O4_{z,m lower}=384E_O,
quad
K2_{z,m lower}=8E_K.
]

Conditional coefficient change if [3,4] is split into two half-cells:

- cubic O remainder coefficient factor = 1/16
- linear K remainder coefficient factor = 1/4.

These are not source-error certificates.

## 4. preserve z=2.5 information

Pre-output frozen z2.5 separation:

- DeltaK=0.1912237840334797/t_a
- DeltaDmax=0.20561180584475613/t_a
- S=0.280789512416017/t_a
- K half gap=0.09561189201673985/t_a
- Dmax half gap=0.10280590292237807/t_a.

Do not read/generate direct z2.5 output.

## 5. evidence semantics

If z3.5 is later used to modify a successor model, it cannot be reused as that successor's independent validation.

Do not combine:
- R31AF z3.5 independent result
with
- successor model tuned using z3.5
as two independent pieces of evidence.

## 6. stop

This handoff stops after:

- policy replay/tests
- action-tree lock
- evidence publication
- create-only dual backup.

No science node.

Ordinary non-force push allowed. Raw restore 없이는 `RESTORE_VERIFIED=false`.
