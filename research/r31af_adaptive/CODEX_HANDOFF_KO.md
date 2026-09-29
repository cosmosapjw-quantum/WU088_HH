# Codex handoff: R31AF adaptive-six-node replay + z=3.5 preregistration

Repo: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31af-adaptive-six-node-20260929`
Base: `research/r31ae-z05-validation-gate-20260929`
Pinned parent: `1f5aa1584e2e057adc29673689fd5ab6ccdde85a`
Parent tree: `a1c327993fde0a0c430b42ce96f624311b98ff5d`

목표는 z=0.5 validation 결과를 [0,1] cell local refinement에만 소비해 R31AF adaptive-six-node model을 재현하고, 영향을 받지 않는 right-cell midpoint z=3.5를 다음 fresh validation으로 preregister하는 것이다. 새 science node는 실행하지 않는다.

## 0. 시작

현재 remote HEAD/tree를 확인한다. 후속 commit이 있으면 diff를 읽고 반영하되 과거 SHA로 reset하지 않는다. 기존 raw/source/worktree/provider backup을 보존한다.

읽기:

1. `research/r31af_adaptive/REPORT_KO.md`
2. `MODEL_POLICY.json`
3. `NEXT_VALIDATION_PREREGISTRATION.json`
4. `adaptive_policy.py`
5. parent R31AE `authorized_z05_20260929/Z05_COMPARISON.json`
6. parent R31AD five-node manifest/model source.

## 1. existing-data assembly only

No new producer execution.

Assemble source-bound direct mixed arrays for:

[
z={0,0.5,1,2,3,4}.
]

Required at every node:

- O 47x2
- D_col 47x2
- D_row 2x47
- independent dotO 47x2.

Bind exact path/member/object, SHA/size and phase/order/source contract in `SIX_NODE_INPUT_MANIFEST.json`.

Provenance:

- z0,z1,z2,z3,z4 = TRAINING
- z0.5 = PRIOR_INDEPENDENT_VALIDATION_CONSUMED_AS_R31AF_TRAINING.

R31AF construction-time independent validation points = [].

## 2. adaptive model replay

Reuse the R31AD interpolation engine unchanged:

`research/r31ad_five_node/unit_cell_model.py`.

Times correspond to z nodes under the same constant velocity contract.

Cells:

- [0,0.5]
- [0.5,1]
- [1,2]
- [2,3]
- [3,4].

Each cell:

- cubic Hermite O from endpoint O,dotO
- linear K=(D_col-D_row†)/2
- D_col=dotO/2+K
- D_row†=dotO/2-K.

Verify:

- six nodes reproduce O,dotO,K,D
- O C1 across all interior knots
- K/D continuity
- dense-grid metric identity
- source arrays unchanged.

Write `R31AF_MODEL_REPLAY.json`.

Do not alter the interpolation family or polynomial degree.

## 3. a posteriori local indicator

Reproduce the z=0.5 direct midpoint error and derived necessary lower bounds:

- E_O = 0.0875296210906087
- E_K = 0.15030919260543524 /t_a
- sup ||d4O/dt4|| >= 1.3449138103246667 /t_a^4
- sup ||d2K/dt2|| >= 0.24053574221790144 /t_a^3
- sup ||d4O/dz4|| >= 33.611374498793744 /a0^4
- sup ||d2K/dz2|| >= 1.202473540843482 /(t_a a0^2).

These are local necessary bounds, not certified source-error enclosures.

## 4. next fresh validation preregistration

Do not execute it.

Selected future point:

- z = 3.5 a0
- tau = 7.825570336618339 t_a
- B192.

Reason:

R31AF differs from R31AD only on [0,1], so z=3.5 predictions are unchanged from the already frozen pre-output R31AD selection table.

Frozen R31AF vs R31Z separation at z=3.5:

- DeltaK = 0.19122378403347964 /t_a
- DeltaDmax = 0.2095387347094023 /t_a
- S = 0.2836776637729875 /t_a.

Truth-independent half gaps:

- E_K >= 0.09561189201673982 /t_a for at least one model
- E_Dmax >= 0.10476936735470115 /t_a for at least one model.

Future required outputs only:

- mixed O 47x2
- mixed D_col 47x2
- mixed D_row 2x47
- independent mixed dotO 47x2.

Future primary metrics:

- E_K
- E_Dmax

Decision:

- PARETO_SUPPORTED_AT_Z35
- GLOBAL_SUPPORTED_AT_Z35
- TRADEOFF_UNRESOLVED.

Tolerance remains 1e-10 unless authoritative parent rule says otherwise. No weighted score.

Create `NEXT_VALIDATION_PREREGISTRATION.json` with model/source/manifest/rule hashes and `execution_authorized=false`.

## 5. no science execution

Forbidden in this handoff:

- z3.5 producer execution
- z2.5 producer execution
- any H
- neutral47
- ionic2
- full49
- trajectory
- M3/reference
- model retuning after prereg lock.

science_node_count=0.

## 6. claim ceiling

R31AD was independently supported relative to R31Z at z=0.5 only.

After z=0.5 is consumed into R31AF training, R31AF itself has no independent validation until a new fresh point is run.

Do not claim interval-wide accuracy, transition error, trajectory, full-cell, H-skip or production.

## 7. return

RETURN.json must include:

- current commit/tree
- SIX_NODE_INPUT_MANIFEST
- R31AF model replay/test results
- local refinement indicator
- z0.5 provenance relabel
- z3.5 preregistration hash
- science_node_count=0
- unresolved full-cell/review/production gates.

Ordinary non-force push and create-only Drive+Dropbox backup allowed. Raw restore 없이는 `RESTORE_VERIFIED=false`.

Stop after R31AF replay + z3.5 prereg lock.
