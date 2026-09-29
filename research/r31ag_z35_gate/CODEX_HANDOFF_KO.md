# Codex handoff: R31AG z=3.5 authorization gate

Repository: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31ag-z35-validation-gate-20260930`
Base: `research/r31af-adaptive-six-node-20260929`
Pinned parent: `e62c5093b67fa0269069c4e64e6eb17a06c9a37e`
Parent tree: `b52b792d1e59dea0de662f4ddf2b5d0dbc3980da`

목표는 R31AF selected fresh point z=3.5의 science execution을 structured one-shot authorization으로만 열고, 승인 전에는 science computation 0으로 종료하는 것이다.

## 0. start

현재 remote HEAD/tree와 successor diff를 확인한다. 과거 SHA로 reset하지 않는다. 기존 raw/source/worktree/provider backup을 보존한다.

읽기:

- `research/r31ag_z35_gate/REPORT_KO.md`
- `AUTHORIZATION_SCOPE.json`
- `AUTHORIZATION_ENVELOPE_TEMPLATE.json`
- `authorization_gate.py`
- parent R31AF `ncp_followup_20260929/RETURN.json`
- parent `NEXT_VALIDATION_PREREGISTRATION.json`
- parent `SIX_NODE_INPUT_MANIFEST.json`.

## 1. authorization scope preflight

Canonical scope hash:

`f43faaf5746a5fda5cd26593ee69e97c0f2be8239727a62081d49357e3c2a9b4`.

Canonicalization:

- UTF-8 JSON
- recursive key sort
- separators `,` and `:`
- no whitespace
- NaN/Infinity forbidden.

Recompute the digest from `AUTHORIZATION_SCOPE.json`. Mismatch -> `AUTHORIZATION_SCOPE_DRIFT`, science command 0, stop.

## 2. structured authorization

Science execution requires a current affirmative user directive containing exactly this object:

```json
{
  "schema": "WU088_R31AF_Z35_MINIMAL_MIXED_AUTHORIZATION_V1",
  "authorize": true,
  "action": "AUTHORIZE_R31AF_Z35_MINIMAL_MIXED_NODE",
  "scope_sha256": "f43faaf5746a5fda5cd26593ee69e97c0f2be8239727a62081d49357e3c2a9b4",
  "one_shot": true
}
```

Token mention/quote/example/condition/negation is not authorization.

Without a valid envelope:

- `Z35_EXECUTION_STATUS=AWAITING_STRUCTURED_AUTHORIZATION`
- producer commands = 0
- science node count = 0
- return and stop.

## 3. exact authorized node

Only if authorized:

- z = 3.5 a0
- tau = 7.825570336618339 t_a
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
- z2.5 or any other z
- M3/reference
- model/tolerance/phase/order modification.

Use the existing hash-verified mixed OD + analytic JVP producer.

## 4. freeze check before direct output access

Authoritative values from parent prereg:

- R31AF interpolation engine:
  `ab220248066580fc77af70c412251dbe3ed643a6fadc266cf5c25a7a3a6651a0`
- R31AF adaptive policy:
  `720b221a9e01ab7fc1bbd482b600ea785fed0b8c6b80b5834c576a75c2b70756`
- R31Z model:
  `4ba03ba2adbdc9533f6472558b33a7edf86959bfc397e5fc8e3e90f8765ba034`
- six-node manifest:
  `e444e9f1cff7d4cc9425a2f44ff45a6e87199c6bf31ca2b095010364379e7573`
- z35 selection:
  `546026387ecae9952b0397fb0dd26ad0633465739d8bbb82878f0f4c532c545e`
- decision rule:
  `52b995b2f5516cf586cf1cbcdb681ec521f1b911a7538e3999a11d0f3bd62560`
- preregistration:
  `ec4613f5300ec38a488eae75f5c7267a2f1a166c34e45d54bb9fa8b449537447`
- tolerance: `1e-10`.

Any mismatch -> stop before science output.

Also check that no equivalent complete direct z3.5 OD+independent-JVP node has been previously accessed. If found, classify `INDEPENDENCE_CONTAMINATED`.

## 5. one-shot frozen comparison

Frozen models:

- R31AF_ADAPTIVE_SIX_NODE_CUBIC_O_LINEAR_K
- R31Z_GLOBAL_QUINTIC_O_QUADRATIC_K.

Primary:

`E_K`

`E_Dmax=max(E_Dcol,E_Drow)`.

Verdict:

- `PARETO_SUPPORTED_AT_Z35`
- `GLOBAL_SUPPORTED_AT_Z35`
- `TRADEOFF_UNRESOLVED`.

Mandatory secondary:

- E_O
- E_dotO
- E_Dcol
- E_Drow
- direct metric-identity residual
- both candidate metric-identity residuals.

Do not use design score S for final model verdict.

## 6. one-shot semantics

When scientific output identity is created, consume authorization.

Same envelope cannot be reused.

After comparison + evidence publication:

- stop immediately
- no retuning
- no automatic z2.5
- no H/full49/trajectory.

## 7. claim ceiling

One z3.5 result does not admit interval-wide/transition/full-cell/trajectory/H-skip/production claims.

BR01/BR02, fixed-Q physical invariance review and independent project review remain separate.

Ordinary non-force push + create-only Drive/Dropbox backup are allowed. Raw restore 없이는 `RESTORE_VERIFIED=false`.
