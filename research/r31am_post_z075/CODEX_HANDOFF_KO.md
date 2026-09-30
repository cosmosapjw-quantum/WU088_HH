# Codex handoff: R31AM post-z=0.75 stop policy

Repository: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31am-post-z075-stop-policy-20260930`
Base: `research/r31al-z075-refinement-gate-20260930`
Pinned parent: `799797778d01edf74e73c1faf4dcf15bd41e3df2`
Parent tree: `fb343fab95a3ac087b7e7a90834c59c987019697`

이 handoff의 목적은 R31AL의 z=0.75 execution contract를 바꾸는 것이 아니라, future result 이후의 action matrix를 output 전에 hash-lock하는 것이다. 새 science node를 실행하지 않는다.

## 0. 시작

현재 remote HEAD/tree와 successor diff를 확인한다. Reset/force/main merge 금지. 기존 raw/source/runtime/provider backup을 보존한다.

읽기:
- `research/r31am_post_z075/POST_Z075_DECISION_POLICY.json`
- `REPORT_KO.md`
- parent R31AL `ncp_followup_20260930/RETURN.json`
- parent primary prereg
- parent secondary prereg
- parent authorization scope.

## 1. Parent R31AL contract를 변경하지 않는다

Expected one-shot scope SHA256:
`2f22f11f279b8d7f98efb2a4bff1fbfb79145f7f5010ce5081ca6ebfcc147357`.

Primary:
R31AK vs R31Z, E_K/E_Dmax Pareto, tolerance 1e-10/t_a.

Secondary:
R31AK refined vs R31AD coarse, E_K/E_Dmax Pareto, same tolerance.

Result order:
1. primary
2. secondary.

Metadata adapter/comparators/predictions/rules는 parent lock 그대로 사용한다.

## 2. R31AM policy replay

`post_z075_policy.py` focused tests를 수행하고 `POST_Z075_DECISION_POLICY.json`과 의미가 같은지 확인한다.

중요 universal rule:

- primary와 secondary는 같은 z=.75 direct output을 공유하므로 independent evidence count=1.
- auto_consume_z075_as_training=false.
- auto_add_knot=false.
- auto_execute_next_node=false.

## 3. Future action matrix

Primary=PARETO_SUPPORTED_AT_Z075:

- Secondary=REFINED_PARETO_SUPPORTED_AT_Z075
  -> `FREEZE_R31AK_LOCALLY_SUPPORTED__PIVOT_TO_REFERENCE_CERTIFICATION`.

- Secondary=COARSE_PARETO_SUPPORTED_AT_Z075
  -> `STOP_H_REFINEMENT__REVIEW_LOCAL_KNOT_POLICY`.

- Secondary=REFINEMENT_TRADEOFF_UNRESOLVED
  -> `FREEZE_R31AK_RELATIVE_SUPPORT__REFINEMENT_GAIN_UNRESOLVED__PIVOT_REFERENCE_REVIEW`.

Primary=GLOBAL_SUPPORTED_AT_Z075:
- any secondary
  -> `STOP_FOR_MODEL_CLASS_REVIEW`.

Primary=TRADEOFF_UNRESOLVED:
- Secondary=REFINED_PARETO_SUPPORTED_AT_Z075
  -> `STOP_EXTERNAL_COMPARATOR_UNRESOLVED__LOCAL_GAIN_ONLY`.
- otherwise
  -> `STOP_FOR_MODEL_CLASS_REVIEW`.

결과를 보고 새로운 10번째 branch를 추가하지 않는다.

## 4. Strong-success stop condition

Primary adaptive support + secondary refined support가 동시에 나와도:

- z=.75를 자동 training으로 소비하지 않는다.
- [0.5,1]을 다시 split하지 않는다.
- 다른 direct node를 자동 실행하지 않는다.

R31AK를 locally supported frozen research model로 보존하고 다음 research axis는:

1. SOURCE_ACCURACY_BOUND_UNAVAILABLE 해소,
2. B-order/reference discretization certification,
3. full-cell authority,
4. complete-HH fixed-Q physical invariance,
5. BR01/BR02,
6. independent project review,
7. production claim audit

중 명시적으로 선택한다.

## 5. Reference uncertainty

실제 authoritative reference-error bound epsilon_i가 있을 때만

delta_true in [delta_observed-2 epsilon_i, delta_observed+2 epsilon_i]

를 supplementary sensitivity로 계산한다.

현재 bound가 없으면 `SOURCE_ACCURACY_BOUND_UNAVAILABLE`.

1e-10, metric residual, bridge tolerance를 epsilon으로 사용하지 않는다.

## 6. No science execution

이번 handoff:
- science producer commands=0
- science node count=0
- direct z=.75 output access=false.

R31AL user authorization prompt 자체를 이 handoff가 승인으로 해석하지 않는다.

## 7. RETURN

RETURN.json:
- current commit/tree
- R31AM policy hash
- focused tests
- parent R31AL locks unchanged
- direct_z075_output_accessed=false
- execution_authorized=false
- science_node_count=0
- unresolved reference/full-cell/review/production gates.

Ordinary non-force publication + create-only Drive/Dropbox backup allowed. Raw restore 없이는 `RESTORE_VERIFIED=false`.

Stop after post-z075 action policy lock.
