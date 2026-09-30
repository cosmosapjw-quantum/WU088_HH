# R31AJ Codex handoff: z=2.5 고정 비교와 supplementary robustness

Repository: cosmosapjw-quantum/WU088_HH
Research branch: research/r31aj-z25-scope-robustness-20260930
Base: research/r31ai-adaptive-seven-node-20260930 (Draft PR #27)
Pinned parent: 5058dee8862df87715be2aac75d3b8c4422ee096
Parent tree: 33207b4d926b2b79110bb24c41cbf75af129fb6d
New publication identity: companion PUBLICATION_RECEIPT.json을 읽는다. 미래 commit을 추정하지 않는다.

## 시작

Current remote HEAD/tree를 읽고 후속 diff가 있으면 검토한다. Reset, force push, main merge 금지. 기존 raw/dirty worktree/runtime/source/backup을 보존한다. REPORT_KO.md, SOURCE_PINS.json, AUTHORIZATION_SCOPE.json, 원 R31AI ncp_followup_20260930의 RETURN/NEXT_VALIDATION_PREREGISTRATION/FROZEN_Z25_DECISION_RULE을 읽는다.

R31AJ는 모델을 바꾸지 않는다. z=2.5는 unchanged [2,3] cell의 fresh relative test이지 양끝 refined half-cell 개선 효과의 direct test가 아니다. 지점이나 원 판정 규칙을 변경하지 않는다.

## 1. 승인과 scope

이 handoff 및 envelope template은 실행 승인이 아니다. 현재 사용자 지시가 USER_AUTHORIZATION_PROMPT_KO.md와 같은 명시적 실행 의도를 주고 아래 envelope를 승인 payload로 제공했을 때만 진행한다.

Schema: WU088_R31AI_Z25_MINIMAL_MIXED_AUTHORIZATION_V1
Action: AUTHORIZE_R31AI_Z25_MINIMAL_MIXED_NODE
authorize=true, one_shot=true
Scope SHA256: 78d960c041536f2baa2160639e5a60878f43f73aadee2e3174ffd5a27d8a68e7

정확한 canonical bytes는 AUTHORIZATION_SCOPE_CANONICAL.json이며 trailing LF/BOM이 없다. SHA-256을 재계산하고 pretty scope와 의미가 같은지 확인한다. ASCII keys/strings, integers, booleans, null, arrays/objects만 허용한다. Quantities는 decimal strings여서 float serialization ambiguity가 없다. validation_diagnostics.canonical_scope_bytes를 사용할 수 있다. 이는 원 scientific numerical convention 변경이 아니다.

설명문/인용/예시/부정문이나 이전 z0.5/z3.5 envelope는 승인 아님. 승인 없으면 AWAITING_EXPLICIT_USER_AUTHORIZATION, new science commands=0으로 멈춘다. 이미 동일 preflight가 닫혔으면 unchanged tests와 문헌탐색을 또 실행하거나 이를 위한 새 gate branch를 만들지 않는다.

## 2. output 이전의 immutable locks

원 preregistration SHA256:
10d05889a336541c81f2153bb232f254c406ebe45d22da6e5470230b40b1a691

원 primary decision rule:
c5712e2539a7db7dda02c563c327c51edc27fb30741df180f19d1cee0cb21d86

R31AI model aggregate:
9d78ed48963f2da9d77e85a4466fd09f6f0f243508b887cbfc96121a46c949c5

Engine:
ab220248066580fc77af70c412251dbe3ed643a6fadc266cf5c25a7a3a6651a0
Policy:
f200fd1837938020c4a99673b1a32f6e652cc4bdcb215318f5588530eb6ac388
Helper:
9709bd806d95915c353f5ef95fc36212ac779feedc8c1128818d5c2437b332d3
Seven-node manifest:
57a1379cc7b658fb8f9eebe2f47cb48f806c3f0ca0292e8e52f53d82d703835b
R31Z model:
4ba03ba2adbdc9533f6472558b33a7edf86959bfc397e5fc8e3e90f8765ba034
Prediction-only record:
64f47cc6a5e6906071636a10d022d4575f9f458c10c31f59881e1808d7b5fba4
Producer CP4 archive:
c10c932a6cdad817982e00920a893733b367827b116d058791bf5aacad517cd9

각 canonical path는 parent prereg/source manifest에서 해석한다. Aggregate serializer를 임의로 발명하지 말고 parent 생성 알고리즘을 그대로 사용한다. 모든 component bytes를 별도로 확인한다. Mismatch면 실행 전 IDENTITY_OR_SCOPE_BLOCKED. z2.5 prior scientific output 또는 consumed grant가 발견되면 duplicate execution하지 말고 data-exposure/independence 상태를 반환한다.

## 3. 승인된 단일 node만

z=2.5 a0, B192. Reported tau=5.589693097584528 t_a; parent computed tau=5.5896930975845285 t_a. Producer의 원 tau=z/velocity 계산을 그대로 쓰고 양 값을 구분해 기록한다.

Required outputs: O47x2, D_col47x2, D_row2x47, independent dotO47x2.
No H matrix, neutral47, ionic2, full49, trajectory, other z, M3/reference work. 변경 없는 OD fused kernel의 internal T/moment intermediates와 H matrix assembly는 구분한다. H block을 새로 조립·저장하지 않는다.

기존 성공한 z3.5 OD.argv.json/JVP.argv.json에서 확인한 CLI 형태는 다음이다. RUNTIME은 hash-verified CP4 source가 있는, 기존 raw를 덮지 않는 runtime이어야 한다. PY는 검증된 기존 venv를 확인해 사용한다. 아래 명령은 승인/locks가 닫힌 경우에만 실행한다.

```bash
cd "$RUNTIME"
"$PY" completion/mixed_h/od_run.py --n 192 --z 2.5 --workers 1
"$PY" completion/mixed_derivative/run.py --z 2.5 --n 192
```

Source/phase/order/tolerance/precision을 수정하지 않는다. Native prerequisites가 없으면 기존 source/빌드계약에 따른 준비만 허용하며 새 최적화·패키지 설치는 하지 않는다. 실제 argv, env, compiler/binary/source identity, exits, 분리 stdout/stderr와 pair checkpoints를 보존한다.

한 geometry의 OD와 JVP는 하나의 승인 transaction이며 science_node_count=1, producer_command_count=2다. 최초 scientific output identity 생성 시 grant를 consumed로 기록하지만 그 transaction의 예정된 두 단계는 완료한다. Partial failure 뒤 전체 node를 같은 grant로 다시 시작하지 않는다. 완료하지 못하면 partial evidence와 정확한 failed stage를 반환한다.

## 4. 원 frozen comparison

Direct output access 전에 comparator/adapter, prediction arrays, prereg/model/rule hashes를 PRE_OUTPUT_LOCK에 게시한다. 원 R31AI replay의 seven-node assembly와 R31Z model을 재사용한다. Existing z3.5 comparator의 wrapper를 필요 범위에서 geometry/7-node manifest로 연결할 수 있으나, model과 primary formula는 변경하지 말고 wrapper를 출력 전에 lock한다. 새로 작성해야 하는 불명확한 authority가 있으면 결과를 보기 전에 차단한다.

Frozen models:
R31AI_ADAPTIVE_SEVEN_NODE_CUBIC_O_LINEAR_K
R31Z_GLOBAL_QUINTIC_O_QUADRATIC_K

원 c571... rule의 E_K/E_Dmax Pareto, tolerance 1e-10/t_a를 한 번 적용한다.
PARETO_SUPPORTED_AT_Z25 / GLOBAL_SUPPORTED_AT_Z25 / TRADEOFF_UNRESOLVED.

Mandatory: E_O, E_dotO, E_Dcol, E_Drow, direct/candidate metric-identity residuals. Raw maxima와 complex128 spectral norms를 구분하고 원 extended-precision bytes를 유지한다. Design score S는 final score가 아니다.

## 5. R31AJ supplementary diagnostics

원 verdict를 계산한 후 observed margins delta_i=E_global,i-E_R31AI,i를 기록한다. 실제로 확보된 reference-error upper bounds가 없으면 SOURCE_ACCURACY_BOUND_UNAVAILABLE로 둔다. 1e-10, source bridge tolerance, metric residual을 epsilon으로 대입하지 않는다.

Bounds가 별도 authority와 함께 있는 경우에만 conditional margin interval delta_i +/- 2 epsilon_i를 부록에 기록한다. validation_diagnostics.margin_bounds는 supplied bound의 타당성을 인증하지 않는다. 이 부록은 기존 primary verdict를 변경하지 않으며 추가 B-order/source node를 자동 요청하거나 실행할 이유가 아니다.

테스트가 필요하면 새 R31AJ tests만 실행한다. Helper는 기존 data를 다시 fitting하거나 producer를 호출하지 않는다. Parent 5/7/... historical suites를 합산하거나 반복하지 않는다.

## 6. 종료, 게시, 백업

어느 verdict든 한 점의 regional relative comparison으로 반환한다. R31AI 독립 검증은 지금 read-only output-unseen 계약의 의미이며 i.i.d. 표본, 모집단 통계적 신뢰수준을 주장하지 않는다. 양끝 refinement gain, interval-wide accuracy, transition error, full-cell, fixed-Q physical invariance, BR01/BR02, project independent review, production/H-skip은 별도 gate다.

이번 승인 범위에서는 output 뒤 모델 retuning, z2.5 training consumption, 새 knot, 다음 node를 실행하지 않는다. 결과를 숨기거나 임계값을 바꾸지 말고 정확히 반환한 뒤 종료한다.

RETURN.json: current/executed commit+tree, actual user authorization reference, pre-output locks, source and binary identity, raw/pair checkpoints, primary/secondary errors, reference-bound status, all independent/claim gates, mutation scope를 기록한다.

기존 방식의 non-force research publication 및 create-only backup:
Drive parent 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
Dropbox /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928

ACK/object ID/size와 실제 제공된 checksum으로 선택한 tier를 닫고 반복 raw redownload를 하지 않는다. Raw restore 없이 RESTORE_VERIFIED=false. 백업 본체와 detached receipt 성공 여부를 각각 기록한다.
