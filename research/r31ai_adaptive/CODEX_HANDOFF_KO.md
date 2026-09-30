# Codex handoff: R31AI adaptive-seven-node replay + z=2.5 preregistration

Repository: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31ai-adaptive-seven-node-20260930`
Base: `research/r31ah-post-z35-policy-20260930`
Pinned parent: `51eb022eb01445ffaef58e8a0078ecd3b779b30c`
Parent tree: `068e4de6dce4a50cc28ead4c84a2e935146aee05`

목표는 이미 성공한 z=3.5 independent validation을 R31AH policy에 따라 successor training으로 소비하여 [3,4]만 local refine한 R31AI seven-node model을 existing data로 재현하고, z=2.5를 다음 fresh holdout으로 preregister하는 것이다. 새 science node는 실행하지 않는다.

## 0. start

현재 remote HEAD/tree와 successor diff를 확인한다. 과거 SHA로 reset하지 않는다. 기존 raw/source/worktree/provider backup을 보존한다.

읽기:

1. `research/r31ai_adaptive/REPORT_KO.md`
2. `MODEL_POLICY.json`
3. `NEXT_VALIDATION_PREREGISTRATION.json`
4. `successor_policy.py` + tests
5. parent R31AH `authorized_z35_20260930/RETURN.json`
6. parent `Z35_COMPARISON.json`
7. parent R31AF six-node input manifest/model replay.

## 1. existing-data assembly only

No new producer execution.

Assemble source-bound direct mixed arrays for

[
z={0,0.5,1,2,3,3.5,4}.
]

Each node requires:

- O 47x2
- D_col 47x2
- D_row 2x47
- independent dotO 47x2
- exact source path/member/object
- SHA/size
- basis/order/phase contract.

Write `SEVEN_NODE_INPUT_MANIFEST.json`.

Provenance:

- z0,z0.5,z1,z2,z3,z4 = TRAINING
- z3.5 = PRIOR_INDEPENDENT_VALIDATION_CONSUMED_AS_R31AI_TRAINING

R31AI independent validation points = [].

Do not count z3.5 again as independent evidence for R31AI.

## 2. model replay

Reuse unchanged interpolation engine:

`research/r31ad_five_node/unit_cell_model.py`

Cells:

- [0,0.5]
- [0.5,1]
- [1,2]
- [2,3]
- [3,3.5]
- [3.5,4].

Each cell:

- O cubic Hermite(endpoint O,dotO)
- K linear endpoint K=(D_col-D_row†)/2
- D_col=dotO/2+K
- D_row†=dotO/2-K.

Verify:

- all seven nodes reproduce O,dotO,K,D
- O C1 at all internal knots
- K/D continuity
- dense-grid metric identity
- source mutation 0.

Write `R31AI_MODEL_REPLAY.json`.

Do not change model degree/family.

## 3. z=3.5 a posteriori indicator

Reproduce direct R31AF midpoint errors:

- E_O = 0.028316443455109017
- E_dotO = 0.02180471880970521 /t_a
- E_K = 0.06617406868623811 /t_a
- E_Dmax = 0.06827426878354666 /t_a.

Necessary lower bounds:

- sup ||d4O/dt4|| >= 0.4350890062991452 /t_a^4
- sup ||d2K/dt2|| >= 0.10589657526007562 /t_a^3
- sup ||d4O/dz4|| >= 10.873514286761862 /a0^4
- sup ||d2K/dz2|| >= 0.5293925494899049 /(t_a a0^2).

Not a certified source-error enclosure.

Record relative z3.5 R31AF-vs-R31Z improvements but keep the original verdict scoped to R31AF at z3.5.

## 4. z=2.5 next fresh holdout preregistration

Do not execute z2.5.

Because R31AI refinements are confined to [0,1] and [3,4], z=2.5 prediction in [2,3] is unchanged from the frozen predecessor.

Future point:

- z = 2.5 a0
- tau = 5.589693097584528 t_a
- B192.

Frozen R31AI vs R31Z separation:

- DeltaK = 0.1912237840334797 /t_a
- DeltaDmax = 0.20561180584475613 /t_a
- S = 0.280789512416017 /t_a
- K half-gap = 0.09561189201673985 /t_a
- Dmax half-gap = 0.10280590292237807 /t_a.

Required future outputs only:

- mixed O 47x2
- mixed D_col 47x2
- mixed D_row 2x47
- independent mixed dotO 47x2.

Primary future metrics:

- E_K
- E_Dmax.

Future verdicts:

- PARETO_SUPPORTED_AT_Z25
- GLOBAL_SUPPORTED_AT_Z25
- TRADEOFF_UNRESOLVED.

Tolerance remains 1e-10 unless an authoritative parent rule supersedes it.

Write `NEXT_VALIDATION_PREREGISTRATION.json` with:

- R31AI engine/model hash
- R31Z model hash
- seven-node manifest hash
- decision-rule hash
- direct_z25_output_accessed=false
- execution_authorized=false.

## 5. no science execution

This handoff forbids:

- z2.5 producer execution
- any other z producer
- H
- neutral47
- ionic2
- full49
- trajectory
- M3/reference work
- model retuning after prereg lock.

Science producer command count = 0.
Science node count = 0.

## 6. claim ceiling

R31AF was independently supported relative to R31Z at z=3.5.

Once z3.5 is consumed into R31AI training, R31AI itself has no independent validation until z2.5 or another fresh point is later run.

Do not admit interval-wide accuracy, transition error, full-cell, trajectory, H-skip or production.

BR01/BR02, fixed-Q complete-HH physical invariance and independent review remain open.

## 7. return

`RETURN.json` must include:

- reviewed/executed commit+tree
- SEVEN_NODE_INPUT_MANIFEST
- R31AI_MODEL_REPLAY
- focused tests
- z3.5 provenance relabel
- z3.5 local indicator
- z2.5 preregistration hash
- direct_z25_output_accessed=false
- science_node_count=0
- unresolved gates.

Ordinary non-force push and create-only Drive+Dropbox backup allowed.
Raw restore 없이는 `RESTORE_VERIFIED=false`.

Stop after R31AI seven-node replay + z2.5 prereg lock.
