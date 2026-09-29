# Codex handoff: R31AC one-shot z=1 authorization protocol

Repository: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31ac-z1-authorization-protocol-20260929`
Base: `research/r31ab-z1-decision-20260929`
Pinned parent: `91aa8a0aeb4ddd3d89f0ef295cba2ddaac255f27`
Parent tree: `d4dc56edda2a4685c3a666a4b9ea7748428052e8`

목표는 z=1 science-node 실행 여부를 **structured authorization envelope**로 판정하고, 승인이 있으면 exactly-once 최소 node를 실행하는 것이다. 추가 interpolation 연구나 새 validation design을 하지 않는다.

## 0. remote / authority

현재 remote HEAD/tree를 먼저 읽고 후속 commit diff를 확인한다. 과거 SHA로 reset하지 않는다. 기존 raw/source/worktree/provider backup을 보존한다.

읽기:

- `research/r31ac_z1_authorization/REPORT_KO.md`
- `AUTHORIZATION_SCOPE.json`
- `AUTHORIZATION_ENVELOPE_TEMPLATE.json`
- parent R31AB `authorization_gate_followup_20260929/RETURN.json`
- parent `Z1_PREREGISTRATION.json` 및 lock
- R31Z/R31AA model source identity.

## 1. authorization rule

문자열 `AUTHORIZE_Z1_MINIMAL_MIXED_NODE`의 단순 존재는 승인 증거가 아니다.

실행은 현재 상위 user instruction에 다음 object가 affirmative directive로 있을 때만 허용한다.

```json
{
  "schema": "WU088_Z1_MINIMAL_MIXED_AUTHORIZATION_V1",
  "authorize": true,
  "action": "AUTHORIZE_Z1_MINIMAL_MIXED_NODE",
  "scope_sha256": "730cf09525d3b09e3b45fab7b8cec78cce631182b2c87e7008f766a10839787c",
  "one_shot": true
}
```

다음이면 무조건 unauthorized:

- quoted/example/condition/negation 문맥,
- authorize != true,
- action/schema mismatch,
- scope hash mismatch,
- one_shot != true.

Unauthorized면
`Z1_EXECUTION_STATUS=AWAITING_STRUCTURED_AUTHORIZATION`
으로 science command 0개, science-node count 0을 기록하고 종료한다.

## 2. scope hash preflight

Canonical scope hash:

`730cf09525d3b09e3b45fab7b8cec78cce631182b2c87e7008f766a10839787c`

Scope에 묶인 identity:

- z=1.0 a0
- tau=2.2358772390338113 t_a
- B192
- prereg SHA256 `803b0968bd7f1fab41310469578b455ef03a64aae5beac1f23c1bab8afa19ddb`
- metric/rule SHA256 `68b0d4c4b80443f374b9c49fa4c1737a8e2f39ed6b06f7340d052aa8c7c537b6`
- R31Z source `4ba03ba2adbdc9533f6472558b33a7edf86959bfc397e5fc8e3e90f8765ba034`
- R31AA source `f24d2acc0506e97dbefea107c126e53891d9879311aad60b9dd3b8e9a1be05d5`
- producer archive `c10c932a6cdad817982e00920a893733b367827b116d058791bf5aacad517cd9`.

Mismatch가 있으면 `AUTHORIZATION_SCOPE_DRIFT`로 실행 없이 종료한다.

## 3. authorized one-shot node

Required outputs only:

- mixed O 47x2
- mixed D_col 47x2
- mixed D_row 2x47
- independent mixed dotO 47x2.

Forbidden:

- H
- neutral47
- ionic2
- full49
- trajectory
- any other z node
- M3/reference work.

기존 verified producer source를 그대로 사용한다. 구현/tolerance/order/phase를 바꾸지 않는다. Exact argv/env/source hashes와 output hashes를 보존한다.

Scientific output이 생성되면 authorization은 consumed다. 같은 envelope로 rerun하지 않는다.

## 4. frozen comparison

Output access 전 model/prereg/rule hashes를 다시 기록한다.

Primary:

`E_K = ||K_pred-K_direct||_2`

`E_Dmax = max(||Dcol_pred-Dcol_direct||_2, ||Drow_pred-Drow_direct||_2)`

Tolerance `1e-10`.

Verdict:

- `PARETO_SUPPORTED_AT_Z1`
- `GLOBAL_SUPPORTED_AT_Z1`
- `TRADEOFF_UNRESOLVED`.

Mandatory secondary:

- E_O
- E_dotO
- E_Dcol
- E_Drow
- direct and candidate metric-identity residuals.

Weighted score나 threshold modification 금지.

## 5. independence

z=3은 R31AA tuning/post-hoc data다.

z=1 independent status는 다음이 모두 참일 때만 true:

- structured authorization 전에 no direct z1 output access,
- prereg/model/rule hashes unchanged,
- equivalent existing z1 mixed node를 사전에 사용하지 않음,
- output 뒤 model source/tolerance/rule 수정 없음.

위반 시 `INDEPENDENCE_CONTAMINATED`.

## 6. claim ceiling / stop

한 z=1 결과로 interval/trajectory/transition/full-cell/H-skip/production을 승인하지 않는다.

승인된 실행의 stop condition:

1. minimal z1 output 생성,
2. frozen comparison,
3. evidence publication,
4. create-only dual backup,
5. return.

그 뒤 model retuning, second node, H/full49/trajectory를 자동 시작하지 않는다.

Ordinary non-force push와 create-only Drive+Dropbox backup 허용. Raw restore 없이는 `RESTORE_VERIFIED=false`.
