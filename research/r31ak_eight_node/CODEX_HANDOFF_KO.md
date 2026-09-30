# Codex handoff: R31AK eight-node replay + clean holdout selection

Repository: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31ak-eight-node-clean-holdout-20260930`
Base: `research/r31aj-z25-scope-robustness-20260930`
Pinned parent: `a3bf6f0fbb6ab2e0d53a28cb72d403db0e48b925`
Parent tree: `0a384e8e12d3f3c5829e8fe0609cb2c223fb7363`

목표는 z=2.5 protocol-deviated numerical result를 투명하게 successor training으로 소비해 중앙 [2,3]을 local refine한 R31AK eight-node model을 재현하고, future independent validation을 위한 fully fresh quarter-point holdout을 prediction-only로 선택·lock하는 것이다. 이번 handoff에서 새 science node는 실행하지 않는다.

1. 현재 remote HEAD/tree와 successor diff를 확인한다. reset/force/main merge 금지.

2. z=2.5 status:
`NUMERICAL_RESULT_RETAINED__INDEPENDENCE_NOT_ADMITTED__METADATA_ONLY_RECOVERY`.
Frozen numerical verdict=PARETO_SUPPORTED_AT_Z25, independence=false, retroactive repair=false를 유지한다.
Successor role:
`PROTOCOL_DEVIATED_NUMERICAL_COMPARISON_CONSUMED_AS_R31AK_TRAINING`.

3. existing-data only로 z={0,.5,1,2,2.5,3,3.5,4}의 O,D_col,D_row,independent dotO와 exact hashes/source identities를 `EIGHT_NODE_INPUT_MANIFEST.json`에 묶는다. z=2.5는 R31AJ authorized raw evidence를 재사용하고 producer 재실행 금지.

4. unchanged engine
`research/r31ad_five_node/unit_cell_model.py`
SHA256 `ab220248066580fc77af70c412251dbe3ed643a6fadc266cf5c25a7a3a6651a0`
를 사용한다.

Cells:
[0,.5],[.5,1],[1,2],[2,2.5],[2.5,3],[3,3.5],[3.5,4].

Verify eight-node reproduction, O C1, K/D continuity, dense-grid metric identity, source mutation 0. `R31AK_MODEL_REPLAY.json`.

5. z=2.5 indicator:
E_O=0.019184864006565112,
E_K=0.08583702792342718/t_a,
O4>=0.2947800782196966/t_a^4,
K2>=0.13736267798030663/t_a^3,
z-O4>=7.366987778521003/a0^4,
z-K2>=0.6866962233874174/(t_a a0^2).
Necessary bounds only.

6. Future comparator must use `metadata_adapter.py` pre-output. Number/string z identity must be parsed to Decimal before equality checks. Publish/hash-lock adapter, comparator, frozen predictions, model/manifest/rule before any future direct output. Never patch identity parsing after output and call the point independent.

7. Candidate cell midpoints:
{0.25,0.75,1.5,2.25,2.75,3.25,3.75}.
Exclude z=1.5 because prior CP4 direct OD-only exposure is known.
Provisional clean candidates:
{0.25,0.75,2.25,2.75,3.25,3.75}.

Inventory CP4 member names/local/provider metadata without opening direct matrix payloads. Remove any preexposed candidate. Empty title search is not absence proof.

8. For every fresh candidate, compute frozen prediction-only R31AK vs R31Z:
DeltaK, DeltaDcol, DeltaDrow, DeltaDmax,
S=sqrt(DeltaK^2+DeltaDmax^2).
Select max S; exact tie -> lower z.
S is design only.

9. Write `HOLDOUT_SELECTION.json` and `NEXT_VALIDATION_PREREGISTRATION.json` before direct output access. Freeze selected z/time/B192, required four mixed outputs, R31AK/R31Z hashes, eight-node manifest, adapter/comparator, prediction arrays, E_K/E_Dmax Pareto rule tolerance 1e-10/t_a, mandatory secondaries, execution_authorized=false, direct_output_accessed=false.

10. Keep `SOURCE_ACCURACY_BOUND_UNAVAILABLE` unless an actual authoritative bound exists. Never substitute decision tolerance, metric residual or bridge tolerance. z2.5 sensitivity budget 0.06206254082953607/t_a is not an actual source bound.

Forbidden:
- any new direct candidate
- H/neutral47/ionic2/full49/trajectory
- M3/reference production
- automatic B-order run
- degree/family change
- z2.5 independence resurrection.

RETURN.json records commit/tree, eight-node manifest/replay, z2.5 classification/training relabel, candidate inventory, model-only selection table, selected holdout and prereg hash, adapter/comparator hashes, selected direct access=false, science_node_count=0, remaining gates.

Ordinary non-force publication + create-only Drive/Dropbox backup allowed. Raw restore 없이는 RESTORE_VERIFIED=false.

Stop after eight-node replay + clean holdout selection + prereg lock.
