# Codex handoff: R31AB z=1 authorization gate

Repository: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31ab-z1-decision-20260929`
Draft PR: `#20`
Pinned starting remote: `2ebdd94325b54125d95578860fd16042c3fea514`
Starting tree: `892e702b3460070c61887b85a9fd3a373da43a9c`

이 handoff의 목적은 새로운 모델 개발이 아니라 **명시적 승인 유무에 따라 한 번의 최소 z=1 validation node를 실행하거나 실행하지 않고 종료하는 것**이다.

## 0. 시작

먼저 현재 branch remote HEAD/tree를 읽는다. 후속 commit이 있으면 diff를 읽고 현재 contract를 갱신한다. 과거 SHA로 reset하지 않는다. 기존 raw/source/worktree/provider backups를 보존한다.

읽기:

1. `research/r31ab_z1_decision/AUTHORIZATION_RECOMMENDATION_KO.md`
2. `AUTHORIZATION_DECISION_V2.json`
3. 기존 `DECISION.json`
4. `Z1_PREREGISTRATION.json`
5. `ncp_followup_20260929/RETURN.json`
6. `ncp_followup_20260929/Z1_PREREGISTRATION_LOCK.json`

## 1. authorization parsing

Science-node 실행에는 상위 지시에 exact token

`AUTHORIZE_Z1_MINIMAL_MIXED_NODE`

이 있어야 한다.

Token이 없으면:

- `Z1_EXECUTION_STATUS=AWAITING_EXPLICIT_AUTHORIZATION`
- science producer command 0개
- science-node count 0
- authorization preflight return만 작성
- ordinary push/backup 가능
- 종료

한다.

일반적인 “계속 진행”, “연구 루프 진행” 또는 backup/tool permission을 science-node authorization으로 해석하지 않는다.

## 2. 승인된 경우에만 실행할 최소 node

Geometry:

- `z=1.0 a0`
- `tau=2.2358772390338113 t_a`
- `B192`

기존 hash-verified producer source/phase/order/tolerance를 그대로 사용한다. 새로운 구현으로 다시 작성하지 않는다.

Required output only:

- mixed `O` 47x2
- mixed `D_col` 47x2
- mixed `D_row` 2x47
- independent mixed `dotO` 47x2

금지:

- H
- neutral47
- ionic2
- full49
- trajectory
- 다른 z node
- M3/reference preparation
- model-source 수정

Producer argv/env/source SHA와 output SHA/size를 보존한다.

## 3. prereg/model freeze를 output access 전에 검증

다음 identity가 direct z=1 output을 읽기 전에 parent lock과 동일해야 한다.

- preregistration SHA-256 `803b0968bd7f1fab41310469578b455ef03a64aae5beac1f23c1bab8afa19ddb`
- R31Z model source SHA
- R31AA model source SHA
- metric/rule aggregate hash
- decision tolerance `1e-10`

하나라도 바뀌었거나 z=1 equivalent direct node를 이전에 읽었다는 증거가 나오면
`INDEPENDENCE_CONTAMINATED`로 분류하고 independent-validation claim을 하지 않는다.

## 4. direct output 이후 단 한 번의 preregistered comparison

Frozen models:

- `R31Z_GLOBAL_QUINTIC_O_QUADRATIC_K`
- `R31AA_LOCAL_PIECEWISE_CUBIC_O_LINEAR_K`

Primary metrics:

[
E_K=||K_{m pred}-K_{m direct}||_2
]

[
E_{D,max}=max(||D_{m col,pred}-D_{m col,direct}||_2,
||D_{m row,pred}-D_{m row,direct}||_2)
]

Decision tolerance (10^{-10}).

- `PARETO_SUPPORTED_AT_Z1`: local <= global+tol in both primary metrics and improves one by >tol.
- `GLOBAL_SUPPORTED_AT_Z1`: reverse dominance.
- `TRADEOFF_UNRESOLVED`: otherwise.

Mandatory secondary outputs:

- E_O
- E_dotO
- E_Dcol
- E_Drow
- direct metric-identity residual
- each candidate metric-identity residual

새 weighted score, 새 threshold, post-output model tuning 금지.

## 5. information-value reference

Output 전 이미 frozen models의 z=1 separation은

- K: `0.2165779475378074/t_a`
- Dmax: `0.21927766897126583/t_a`

이다. 따라서 direct truth와 무관하게 적어도 한 모델은

- E_K >= `0.1082889737689037/t_a`
- E_Dmax >= `0.10963883448563291/t_a`

오차를 갖는다.

이 수치는 z=1이 높은 discriminating-power point라는 사전 근거일 뿐 어느 모델이 이길지 예측하지 않는다.

## 6. claim ceiling / fixed-Q

한 z=1 결과로:

- interval-wide accuracy
- transition error
- trajectory
- full-cell
- production
- H-skip

을 승인하지 않는다.

Q는 `FIXED_Q_MODEL_DEFINITION_ESTABLISHED`, `dotQ=0 BY_MODEL_DEFINITION`이다. Complete HH physical invariant-sector proof는 별도 미완료 gate다.

BR01/BR02와 independent review도 유지한다.

## 7. stop condition

승인이 없으면 preflight에서 즉시 종료한다.

승인이 있으면 z=1 node 생성 -> direct output identity 기록 -> preregistered comparison -> evidence publication까지 수행하고 **즉시 종료**한다.

결과를 본 뒤:
- 모델 재튜닝 금지
- 두 번째 validation node 자동 생성 금지
- trajectory/H/full49 자동 진입 금지

한다.

Ordinary non-force push와 create-only Drive+Dropbox backup은 허용된다. Provider ACK/object ID/size/checksum 범위를 receipt에 기록하고 raw restore 없이는 `RESTORE_VERIFIED=false`다.
