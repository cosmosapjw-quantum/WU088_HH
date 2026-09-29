# Codex handoff: R31AE z=0.5 selected-midpoint authorization gate

Repo: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31ae-z05-validation-gate-20260929`
Base: `research/r31ad-five-node-unit-cells-20260929`
Pinned parent: `0383a3b3c66a3b3e820c7deb228f7cd90b249995`
Parent tree: `94de041166451db62e0cc653a745933daffcddda`

목표는 R31AD selected midpoint z=0.5의 science execution을 **명시적 structured authorization**으로만 열고, 승인 전에는 science computation 0으로 종료하는 것이다.

## 0. 시작

현재 remote HEAD/tree를 읽고 후속 commit이 있으면 diff를 읽는다. 과거 SHA로 reset하지 않는다. 기존 raw/source/worktree/provider backup을 보존한다.

읽기:

1. `research/r31ae_z05_gate/REPORT_KO.md`
2. `AUTHORIZATION_SCOPE.json`
3. `AUTHORIZATION_ENVELOPE_TEMPLATE.json`
4. parent R31AD `ncp_followup_20260929/RETURN.json`
5. parent `MIDPOINT_SELECTION.json`
6. parent `NEXT_VALIDATION_PREREGISTRATION.json`
7. parent `FIVE_NODE_INPUT_MANIFEST.json`.

## 1. scope canonicalization

Scope digest는 다음 algorithm으로만 다시 계산한다.

- UTF-8 JSON
- recursive lexicographic key sort
- separators exactly `,` and `:`
- no whitespace
- NaN/Infinity forbidden.

Expected:

`f9872cb045fef146987829620c669fb99f2417a787d74cde26dfee107153a567`

Mismatch면 `AUTHORIZATION_SCOPE_DRIFT`, science command 0, 종료.

## 2. authorization semantics

실행은 현재 상위 user instruction이 다음 object를 affirmative directive로 제공할 때만 허용한다.

```json
{
  "schema": "WU088_R31AD_Z05_MINIMAL_MIXED_AUTHORIZATION_V1",
  "authorize": true,
  "action": "AUTHORIZE_R31AD_Z05_MINIMAL_MIXED_NODE",
  "scope_sha256": "f9872cb045fef146987829620c669fb99f2417a787d74cde26dfee107153a567",
  "one_shot": true
}
```

설명/인용/예시/조건/거부문에 action string이 나타나는 것은 승인 아님.
authorize != true, schema/action/hash mismatch, one_shot != true도 unauthorized.

Unauthorized이면:

`Z05_EXECUTION_STATUS=AWAITING_STRUCTURED_AUTHORIZATION`

science producer commands=0, science-node count=0으로 반환하고 종료.

## 3. 승인된 경우 exact scope

Exactly one node:

- z=0.5 a0
- tau=1.1179386195169057 t_a
- B192.

Required only:

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
- any other z
- M3/reference work
- post-output model retuning.

기존 hash-verified mixed OD/JVP producer를 그대로 사용하고 tolerance/order/phase/source를 수정하지 않는다.

## 4. output access 전 freeze check

다음을 output access 전에 확인:

- R31AD model SHA256
  `ab220248066580fc77af70c412251dbe3ed643a6fadc266cf5c25a7a3a6651a0`
- R31Z model SHA256
  `4ba03ba2adbdc9533f6472558b33a7edf86959bfc397e5fc8e3e90f8765ba034`

- five-node manifest SHA256
  `05f4068dffad51080942c466e19943a73c508b004d3d46f3b9a2b69a58cefc49`
- selection SHA256
  `2761664a75d7609c7ac0b1df4daf36a50e01d82a80b28a42885a22c5042a800b`
- selection rule SHA256
  `835c0a53719849652557737ef61d343c58222d847cf6d1b2ee6fb4831fb656dc`
- prereg SHA256
  `a111005296954c303563be6aaab10379d22694c544576fb1869a37938ab9247d`
- tolerance `1e-10`.

실제 parent prereg와 한 항목이라도 다르면 science execution 전에 종료.

## 5. frozen comparison

Models:

- R31AD_FIVE_NODE_UNIT_CELL_CUBIC_O_LINEAR_K
- R31Z_GLOBAL_QUINTIC_O_QUADRATIC_K.

Primary:

`E_K = ||K_pred-K_direct||_2`

`E_Dmax = max(||Dcol_pred-Dcol_direct||_2, ||Drow_pred-Drow_direct||_2)`.

Tolerance `1e-10`.

Verdict:

- `PARETO_SUPPORTED_AT_SELECTED_MIDPOINT`
- `GLOBAL_SUPPORTED_AT_SELECTED_MIDPOINT`
- `TRADEOFF_UNRESOLVED`.

Mandatory secondary:

- E_O
- E_dotO
- E_Dcol
- E_Drow
- direct metric-identity residual
- each candidate metric-identity residual.

Design score S를 final decision에 사용하지 않는다.

## 6. independence

z=0.5 independent validation은 다음이 모두 참일 때만 인정:

- direct output access 전에 model/prereg/selection hashes unchanged
- searched sources에서 equivalent full mixed OD+independent-JVP node를 사전 사용하지 않음
- selection에 direct truth 미사용
- output 뒤 model/tolerance/rule 변경 없음.

위반하면 `INDEPENDENCE_CONTAMINATED`.

## 7. one-shot / stop

Scientific output identity 생성 시 authorization consumed.
같은 envelope로 rerun 금지.

Comparison/evidence publication 후 즉시 stop.

결과 뒤:

- model retuning 금지
- z=2.5/3.5 자동 실행 금지
- H/full49/trajectory 진입 금지.

한 point로 interval/transition/full-cell/production/H-skip 승인 금지.

Ordinary non-force push와 create-only Drive+Dropbox backup 허용.
Raw restore 없이는 `RESTORE_VERIFIED=false`.
