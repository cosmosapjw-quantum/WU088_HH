# Codex handoff: R31AD five-node unit-cell candidate + future midpoint preregistration

Repo: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31ad-five-node-unit-cells-20260929`
Base: `research/r31ac-z1-authorization-protocol-20260929`
Pinned parent: `82d3d076dc229c20236747738f0ed14861a1b741`
Parent tree: `9127841194bd0f252022aac3a6acd320e84e2647`

목표는 새 science node 없이 기존 z=0,1,2,3,4 mixed direct evidence를 조립하여 R31AD unit-cell candidate를 재현하고, 다음 독립 validation midpoint를 **예측만으로 선택·lock**하는 것이다. 새 direct midpoint 계산은 이번 handoff 범위가 아니다.

## 0. 시작

현재 remote HEAD/tree를 확인하고 후속 commit이 있으면 diff를 읽는다. 과거 SHA로 reset하지 않는다. 기존 raw/source/worktree/backups를 보존한다.

읽기:

1. `research/r31ad_five_node/REPORT_KO.md`
2. `MODEL_POLICY.json`
3. `NEXT_VALIDATION_DESIGN.json`
4. `unit_cell_model.py`, tests
5. parent R31AC authorized z1 `RETURN.json` / `Z1_COMPARISON.json`
6. parent R31Z z3 post-hoc comparison
7. parent producer intake/source pins

## 1. existing-data assembly only

No new producer execution.

Assemble direct mixed nodes at z=0,1,2,3,4 from existing evidence:

- z0,z2,z4: existing R31W/R31Y hash-bound fit/archive sources
- z1: R31AC authorized one-shot OD/JVP outputs
- z3: recovered CP4 OD/JVP outputs

For each node bind:

- O 47x2
- D_col 47x2
- D_row 2x47
- independent dotO 47x2
- exact source path/member/object
- SHA/size
- basis/order/phase contract

Write `FIVE_NODE_INPUT_MANIFEST.json`.

Do not silently cast away extended precision provenance. Diagnostic/interpolation dtype must be recorded separately.

## 2. provenance relabel

R31AD model development must mark:

- z0,z2,z4 = TRAINING
- z1 = PRIOR_INDEPENDENT_VALIDATION_CONSUMED_AS_R31AD_TRAINING
- z3 = PRIOR_POST_HOC_TUNING_CONSUMED_AS_R31AD_TRAINING

Therefore `R31AD_independent_validation_points=[]` at model-construction time.

Do not reuse z1 or z3 as validation evidence for R31AD.

## 3. build R31AD candidate

Use exact model contract:

For every cell [j,j+1], j=0..3:

- O = cubic Hermite using endpoint O and physical-time dotO
- K = linear interpolation of endpoint K=(D_col-D_row†)/2
- D_col = dotO/2 + K
- D_row† = dotO/2 - K

Verify:

- all five nodes reproduce O,dotO,K,D
- O is C1 at z=1,2,3
- K/D are continuous at internal nodes
- metric compatibility residual on dense diagnostic grid
- no source array mutation

Write `R31AD_MODEL_REPLAY.json`.

Theoretical factor checks:
- cubic midpoint coefficient h^4/384
- linear midpoint coefficient h^2/8
- width 2 -> 1 coefficient ratios 16 and 4.

These are conditional remainder-coefficient comparisons, not empirical error guarantees.

## 4. next-validation midpoint selection, no science execution

Candidate points are exactly:

`{0.5,1.5,2.5,3.5} a0`.

First inventory whether equivalent direct mixed OD+independent-dotO data already exist. Any pre-accessed/direct-existing candidate is not a fresh validation point and must be marked contaminated/unavailable.

For each still-fresh midpoint, evaluate **predictions only** from:

- R31AD five-node unit-cell model
- R31Z global model

Compute:

- DeltaK_model
- DeltaDcol_model
- DeltaDrow_model
- DeltaDmax_model
- S = sqrt(DeltaK_model^2 + DeltaDmax_model^2)

Select the point with maximum S. Tie -> lower z.

Write `MIDPOINT_SELECTION.json` with all rows, selected point, model hashes, and the rule hash.

Important:
- This S is for experiment design only.
- It is not the final model-selection score.
- Do not read or generate direct output at the selected midpoint in this handoff.

After selection, create `NEXT_VALIDATION_PREREGISTRATION.json` containing the selected z, required minimal mixed outputs, frozen R31AD/R31Z sources, E_K/E_Dmax Pareto rule, and `execution_authorized=false`.

## 5. no new science node

Forbidden in this handoff:

- midpoint direct OD/JVP execution
- H
- neutral47
- ionic2
- full49
- trajectory
- any other z
- M3/reference work
- model retuning after midpoint selection

Science-node count must remain 0.

## 6. claim ceiling

R31Z remains relatively supported at z=1 for the old comparison only. Do not call it interval-wide adequate.

R31AD has no independent validation until a new half-integer direct node is executed later.

Full-cell/fixed-Q physical invariance/BR01/BR02/independent review/production remain separate open gates.

## 7. return

`RETURN.json` must include:

- remote/executed commit+tree
- five-node input manifest
- model replay/test results
- node provenance relabel
- midpoint candidate inventory
- model-only separation table
- selected future validation point
- preregistration hash
- `science_node_count=0`
- unresolved gates

Ordinary non-force push + create-only Drive/Dropbox backup allowed. Raw restore 없이는 `RESTORE_VERIFIED=false`.

Stop after R31AD model replay + midpoint selection + prereg lock. 새 validation node 실행은 별도 승인 결정으로 넘긴다.
