# Codex handoff: R31AL z=0.75 primary + refinement-gain prelock

Repository: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31al-z075-refinement-gate-20260930`
Base: `research/r31ak-eight-node-clean-holdout-20260930`
Pinned parent: `8bfd2494839dacb2124a8e9fc4fadc9d010e7003`
Parent tree: `d26802b8169ff97407f184f75a4be96e3fb2b1a1`

목표는 selected fresh z=0.75의 기존 primary R31AK-vs-R31Z preregistration을 변경하지 않은 채, direct output access 전에 R31AK refined-vs-R31AD coarse h-refinement comparison을 secondary로 추가 lock하고 final one-shot authorization scope를 준비하는 것이다.

이번 handoff에서는 z=0.75 direct node를 실행하지 않는다.

## 0. start

현재 remote HEAD/tree와 successor diff를 확인한다. 과거 SHA로 reset하지 않는다. 기존 raw/source/runtime/provider backup을 보존한다.

읽기:

- `research/r31al_z075_gate/REPORT_KO.md`
- `SECONDARY_REFINEMENT_POLICY.json`
- `refinement_gain.py`
- parent R31AK `ncp_followup_20260930/RETURN.json`
- parent `HOLDOUT_SELECTION.json`
- parent `NEXT_VALIDATION_PREREGISTRATION.json`
- parent `EIGHT_NODE_INPUT_MANIFEST.json`
- parent metadata adapter/comparator source.

## 1. parent primary locks

z = 0.75 a0
time = 1.6769079292753586 t_a
B192.

Parent hashes:

- R31AK aggregate:
  `50a5f0eeda63d6e04795e301f6b07a41fd11a4b145e267cfc608261356d49b30`
- R31Z:
  `4ba03ba2adbdc9533f6472558b33a7edf86959bfc397e5fc8e3e90f8765ba034`
- eight-node manifest:
  `d978792bef0c3bf2b670d4e73d70dcea391645f38555f1070323037610162ece`
- metadata adapter:
  `41a8a67d0b3de90aa22ea4c1f011cbeb0cb48c417dd47b5d958ac26f52f63619`
- comparator:
  `5443b1ef98b1b70044b8a2e5e8bb065a1d927824066c6a142be3935bfc695394`
- frozen predictions:
  `6d29acbe1aee9bb34cf3627c04136d67e27b5a44b44ee7b3104cdcd3fe1ff88c`
- selection:
  `f01460fe12920280f09281d0763c896986574061806eb0568839b50fcccd096e`
- parent prereg:
  `44b2273afeddb4a6befa73ce485ae84d8f8777a92ac75c4de2fd90d0fea74b81`
- primary decision rule:
  `08ad89d35c31e133bce39da1f5c8b59eb782b647fb1e4e26da522e010ed6d995`
- tolerance:
  `1e-10/t_a`.

Parent primary comparison must remain byte/semantic identical.

## 2. R31AD coarse comparator assembly

No direct z0.75 truth.

Use existing source-bound z=0 and z=1 arrays only:

- O
- independent dotO
- D_col
- D_row
- K=(D_col-D_row†)/2.

Use unchanged engine:

`research/r31ad_five_node/unit_cell_model.py`
SHA256:
`ab220248066580fc77af70c412251dbe3ed643a6fadc266cf5c25a7a3a6651a0`.

R31AD policy Git blob:
`aba52d2c8ffdf97079999cc5f54bd20154bdf4a2`.

Compute R31AD coarse [0,1] prediction at z=0.75, B192 representation, without accessing direct z0.75 output.

Record exact arrays SHA256 in
`Z075_COARSE_PREDICTION.json` + machine array file.

## 3. exact refinement-propagation cross-check

Let direct z0.5 minus R31AD coarse-midpoint corrections be deltaO,deltadot,deltaK.

Verify numerically from existing z0.5 evidence:

`R31AK(z=.75)-R31AD(z=.75)`

equals

- O: deltaO/2 + H*deltadot/16
- dotO: -3 deltaO/H - deltadot/4
- K: deltaK/2
- Dcol: DeltaDot/2 + DeltaK
- Drow†: DeltaDot/2 - DeltaK

with H=2.2358772390338113 t_a.

Required norm cross-check:

`||DeltaK|| = 0.07515459630271762/t_a`

to numerical roundoff.

The stored z0.5 norm-only bounds are:

- O separation in [0.03508653720881643, 0.05244308388179227]
- dotO separation in [0.1019178360724072, 0.1329688193195485]/t_a.

Mismatch -> REFINE_PROPAGATION_CONTRACT_MISMATCH and stop before any science execution.

## 4. lock secondary refinement comparison

Models:

- refined: R31AK_ADAPTIVE_EIGHT_NODE_CUBIC_O_LINEAR_K
- coarse: R31AD_FIVE_NODE_UNIT_CELL_CUBIC_O_LINEAR_K.

Secondary primary metrics:

- E_K
- E_Dmax=max(E_Dcol,E_Drow).

Tolerance:
`1e-10/t_a`.

Secondary verdict set:

- REFINED_PARETO_SUPPORTED_AT_Z075
- COARSE_PARETO_SUPPORTED_AT_Z075
- REFINEMENT_TRADEOFF_UNRESOLVED.

Mandatory secondary output:
E_O,E_dotO,E_K,E_Dcol,E_Drow,E_Dmax for both models,
direct/refined/coarse metric identity residuals,
improvement fractions.

This secondary rule is pre-output and does not alter parent primary verdict.

Write:

- `SECONDARY_REFINEMENT_PREREGISTRATION.json`
- `Z075_REFINEMENT_PRE_OUTPUT_LOCK.json`.

## 5. final authorization scope

Before any direct output access, build one authorization scope that references:

- parent primary prereg hash
- secondary prereg hash
- R31AK selected prediction hash
- R31Z selected prediction hash
- R31AD coarse prediction hash
- metadata adapter hash
- primary comparator hash
- secondary comparator hash
- model/manifest identities
- exact z/time/B192 and four required mixed outputs.

Use ASCII JSON + decimal-string quantities and literal canonical bytes, following R31AJ/R31AK hardened scope practice.

Create:

- `AUTHORIZATION_SCOPE.json`
- `AUTHORIZATION_SCOPE_CANONICAL.json`
- `AUTHORIZATION_SCOPE.sha256`
- `AUTHORIZATION_ENVELOPE_TEMPLATE.json`
- `USER_AUTHORIZATION_PROMPT_KO.md`.

Set:

- execution_authorized=false
- direct_output_accessed=false.

Do not execute z=0.75.

## 6. future science scope

Future authorized node only:

z=0.75 a0
B192
producer tau=z/velocity.

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
- another z
- M3/reference production work
- output-after model/rule/adapter modification.

Metadata adapter must be used unchanged before any direct array read.

## 7. future outcome hierarchy

First report parent PRIMARY:

R31AK vs R31Z
E_K/E_Dmax Pareto
parent verdict vocabulary unchanged.

Then report SECONDARY:

R31AK refined vs R31AD coarse
secondary verdict vocabulary above.

Secondary never overwrites primary.

A refined win directly supports local h-refinement gain only for fresh z=0.75 in [0.5,1]. It does not certify all refined cells or interval-wide convergence.

## 8. source/reference uncertainty

`SOURCE_ACCURACY_BOUND_UNAVAILABLE` 유지.

Decision tolerance, metric residual, bridge tolerance를 source/reference epsilon으로 대입하지 않는다.

새 B-order/source calculation 자동 실행 금지.

## 9. no science execution in this handoff

science producer command count = 0
science node count = 0
direct z0.75 output access = false.

## 10. RETURN

RETURN.json:

- current commit/tree
- parent primary lock verification
- R31AD coarse prediction identity
- refinement-propagation exact check
- secondary prereg hash
- primary+secondary comparator hashes
- final authorization scope hash
- user authorization prompt path
- direct_output_accessed=false
- execution_authorized=false
- science_node_count=0
- unresolved source/full-cell/review/production gates.

Ordinary non-force publication and create-only Drive/Dropbox backup allowed.
Raw restore 없이는 `RESTORE_VERIFIED=false`.

Stop after secondary lock + final authorization scope.
