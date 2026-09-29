# Codex handoff — R31AB z=1 최소 mixed validation 실행 준비

Repo: cosmosapjw-quantum/WU088_HH
Branch: research/r31ab-z1-decision-20260929
Stack base: research/r31aa-validation-design-20260929
Pinned parent: 0566c65655128f0fffb3794860af23b2c3d1fe66
Parent tree: f2638642d85410185beca0a881e0db853adb826a

목표는 R31AB decision replay와 z=1 실행 전 preflight를 수행하는 것이다. **이 handoff 자체는 새 science node 실행을 승인하지 않는다.** 실행 전에 대화/상위 orchestrator에서 정확히 `AUTHORIZE_Z1_MINIMAL_MIXED_NODE`에 해당하는 명시적 승인을 확인았 한다.

## 0. 시작 identity

현재 remote HEAD/tree를 읽고 후속 commit이 있으면 diff를 읽는다. 과거 SHA로 reset하지 않는다. 기존 raw/source/worktree/provider backup을 보존한다. main merge, force push, 타 owner PID/cgroup mutation 금지.

읽기 순서:

1. research/r31ab_z1_decision/REPORT_KO.md
2. DECISION.json
3. Z1_INFORMATION.json
4. parent research/r31aa_validation/ncp_followup_20260929/RETURN.json
5. parent Z3_POSTHOC_MODEL_COMPARISON.json
6. parent Z1_PREREGISTRATION_LOCK.json
7. parent FIXED_Q_CONTRACT_REVIEW.json

## 1. R31AB 경량 replay

hash-locked 기존 input을 사용한다.

- 71,481 bytes
- SHA256 565a9ee6d831f5f9e3e69010270f5319aa3328432950efcfda81cfabf325c079

`z1_information.py`의 py_compile, focused tests, replay만 수행한다. 기존 5/11/20/13/33/134 suite를 반복하지 않는다. 새 native 계산은 없다.

재현 target:

- z1 model separation K = 0.2165779475378074 /t_a
- Dmax separation = 0.21927766897126583 /t_a
- half-gap forced-error K = 0.1082889737689037 /t_a
- half-gap forced-error Dmax = 0.10963883448563291 /t_a
- information verdict = HIGH_DISCRIMINATION_EXPECTED

이 값은 어느 모델이 이기는지를 예측하지 않는다.

## 2. 실행 승인 gate

`DECISION.json`의 `execution_authorized=false`를 임의로 바꾸지 않는다.

명시적 승인 문자열 또는 동등한 상위 지시가 없으면:

- `Z1_EXECUTION_STATUS=AWAITING_EXPLICIT_AUTHORIZATION`
- 새 science computation 0
- preflight/return만 기록하고 종료한다.

승인을 받은 경우에만 다음 최소 node를 실행한다.

### authorized node

- z = 1.0 a0
- tau = 2.2358772390338113 t_a
- radial order B192
- producer contract는 parent R31Y/R31Z에서 검증된 mixed OD + independent JVP source를 그대로 사용

Required outputs only:

- mixed_O_47x2
- mixed_D_col_47x2
- mixed_D_row_2x47
- independent_mixed_dotO_47x2

Forbidden:

- H
- neutral47
- ionic2
- full49
- trajectory
- M3/reference preparation
- 다른 z node

기존 producer command를 z=1에 parameterize하되 source code/tolerance/registry/phase convention을 수정하지 않는다. 새 implementation을 만들지 말고 원 producer를 사용한다. exact argv/environment/source SHA와 output hashes를 보존한다.

## 3. preregistered comparison

z=1 direct arrays를 읽기 전에 다음 두 모델과 metric/decision rule의 source hashes를 저장한다.

Models:

- R31Z_GLOBAL_QUINTIC_O_QUADRATIC_K
- R31AA_LOCAL_PIECEWISE_CUBIC_O_LINEAR_K

Primary metrics:

- E_K = ||K_pred-K_direct||2
- E_Dmax = max(||Dcol_pred-Dcol_direct||2, ||Drow_pred-Drow_direct||2)

Tolerance 1e-10.

Decision:

- PARETO_SUPPORTED_AT_Z1: local <= global+tol in both primary metrics and >tol improvement in at least one.
- GLOBAL_SUPPORTED_AT_Z1: reverse dominance.
- TRADEOFF_UNRESOLVED: otherwise.

Mandatory secondary metrics:

E_O, E_dotO, E_Dcol, E_Drow, source and candidate metric-identity residuals.

No weighted score, no threshold invention after observing z1.

## 4. provenance policy

z3 is `POST_HOC_TUNING_DATA_NOT_INDEPENDENT_CONFIRMATION` for R31AA and must not be combined with z1 as two independent validations.

z1 is the first independent validation of the R31AA form only if:

- prereg hashes are unchanged before node output access,
- producer contract is unchanged,
- z1 equivalent direct mixed node was not previously available/read,
- model source is not modified after output access.

If any condition fails, classify `INDEPENDENCE_CONTAMINATED` and do not claim independent validation.

## 5. fixed-Q/full-cell boundary

Parent review established `FIXED_Q_MODEL_DEFINITION_ESTABLISHED`; dotQ=0 by represented-model definition. Do not reopen dynamic-Q search unless new contrary source evidence appears.

Do not promote fixed-Q to complete-HH physical invariant sector without a separate source/theory review of full dynamics.

z4 neutral47 generation/full-cell trajectory remains outside this handoff.

## 6. return

RETURN.json must include:

- executed/reviewed commit+tree
- explicit authorization evidence or absence
- prereg/model hashes before any z1 output read
- producer source hashes and exact commands
- science-node count
- direct output hashes and source identity if executed
- all primary/secondary errors
- frozen decision-rule verdict
- independence status
- claim ceiling
- unresolved full-cell/BR01/BR02/review/production gates

If not authorized, return without science computation.
If authorized and executed, stop immediately after z1 comparison and evidence publication. Do not tune another model or create a second validation node.

Ordinary non-force push and create-only Drive+Dropbox backup are allowed. Raw restore 없이는 RESTORE_VERIFIED=false.
