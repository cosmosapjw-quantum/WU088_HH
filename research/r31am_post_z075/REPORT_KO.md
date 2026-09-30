# R31AM: z=0.75 post-result stop policy

기준 parent는 R31AL remote HEAD `799797778d01edf74e73c1faf4dcf15bd41e3df2`, tree `fb343fab95a3ac087b7e7a90834c59c987019697`이다. R31AL은 z=0.75 direct output을 보지 않은 채 primary R31AK-vs-R31Z와 secondary R31AK-refined-vs-R31AD-coarse 비교, metadata adapter, comparator, prediction arrays 및 one-shot scope를 모두 lock했다. Authorization scope SHA-256은 `2f22f11f279b8d7f98efb2a4bff1fbfb79145f7f5010ce5081ca6ebfcc147357`이고 execution_authorized=false다.

## 1. R31AM의 목적

R31AM은 새 science gate를 만들지 않는다. 결과를 본 뒤 다시 knot를 넣는 adaptive 메타루프를 차단하기 위해, z=0.75 결과의 primary 3 verdict x secondary 3 verdict에 대한 post-result action matrix를 direct output 전에 고정한다.

같은 z=0.75 direct output을 사용하는 primary와 secondary는 서로 다른 deterministic question에 답한다.

- primary: R31AK vs R31Z
- secondary: R31AK refined vs R31AD coarse

그러나 같은 direct geometry를 공유하므로 독립 validation evidence 두 개로 계상하지 않는다. evidence count는 1이다.

## 2. Stop matrix

### A. primary=PARETO_SUPPORTED_AT_Z075

1. secondary=REFINED_PARETO_SUPPORTED_AT_Z075

`FREEZE_R31AK_LOCALLY_SUPPORTED__PIVOT_TO_REFERENCE_CERTIFICATION`

해석: fresh z=0.75에서 R31AK가 R31Z보다 상대 우세하고, 동시에 z=0.5 knot를 넣은 local h-refinement가 pre-refinement R31AD coarse cell보다 직접 우세하다.

이것이 현재 adaptive interpolation ladder의 성공 stop condition이다.

- R31AK를 이 상태로 freeze한다.
- z=0.75를 자동 training으로 소비하지 않는다.
- 새 knot를 자동 추가하지 않는다.
- 다음 science node를 자동 실행하지 않는다.
- 다음 연구축은 SOURCE_ACCURACY_BOUND_UNAVAILABLE 해소, reference/B-order certification, full-cell authority/physical claim audit이다.

2. secondary=COARSE_PARETO_SUPPORTED_AT_Z075

`STOP_H_REFINEMENT__REVIEW_LOCAL_KNOT_POLICY`

R31AK가 global baseline보다 낫더라도 local knot insertion 자체는 fresh point에서 악화되었다. 추가 h-refinement를 자동 수행하지 않고 knot-selection/local model policy를 검토한다.

3. secondary=REFINEMENT_TRADEOFF_UNRESOLVED

`FREEZE_R31AK_RELATIVE_SUPPORT__REFINEMENT_GAIN_UNRESOLVED__PIVOT_REFERENCE_REVIEW`

External baseline 대비 상대 support만 유지한다. Refinement gain은 미해결이므로 추가 knot를 금지하고 reference uncertainty/cell coverage review로 전환한다.

### B. primary=GLOBAL_SUPPORTED_AT_Z075

Secondary verdict와 무관하게 `STOP_FOR_MODEL_CLASS_REVIEW`.

Local refinement가 coarse보다 좋아도 R31Z global baseline에 지면 current local family를 자동 확장하지 않는다. Global/nonlocal representation, node placement, source/reference systematics를 다시 검토한다.

### C. primary=TRADEOFF_UNRESOLVED

- secondary=REFINED_PARETO_SUPPORTED_AT_Z075이면 `STOP_EXTERNAL_COMPARATOR_UNRESOLVED__LOCAL_GAIN_ONLY`.
- 나머지는 `STOP_FOR_MODEL_CLASS_REVIEW`.

즉 local h-refinement gain만 확인되더라도 external comparator가 unresolved이면 자동 refinement ladder를 계속하지 않는다.

## 3. 왜 여기서 자동 adaptive loop를 멈추는가

SciSpace에서 Dwork et al.의 reusable holdout (Science, DOI 10.1126/SCIENCE.AAA9375)와 Guilt-free data reuse (CACM, DOI 10.1145/3051088), Bibaut & Kallus arXiv:2405.01281을 검토했다. 이들은 adaptive data reuse가 inference 의미를 바꾸므로, data exposure 이후의 추가 분석/설계가 원래의 fixed validation과 동일한 의미를 갖지 않는다는 점을 강조한다.

이 문헌을 WU088의 통계적 theorem으로 직접 적용하지 않는다. 현재 deterministic validation ladder에서는 더 보수적으로, prelocked z=0.75 한 점에서 두 비교를 수행하되 그 하나의 direct observation을 두 independent evidence로 세지 않고, favorable result가 나와도 자동 successor training으로 소비하지 않는 stop rule을 채택한다.

## 4. z=0.75 pre-output facts

Parent selection:

- DeltaK(R31AK,R31Z)=0.3418463058618517/t_a
- DeltaDmax=0.3504308143080971/t_a
- S=0.4895514808965761/t_a
- half gaps: 0.17092315293092586/t_a, 0.17521540715404854/t_a.

z=0.75는 [0.5,1] refined half-cell midpoint다. Wolfram exact derivation에서 z=0.5 direct-minus-coarse correction deltaO,deltadotO,deltaK가 z=.75에 미치는 refined-minus-coarse correction은

[
Delta O = delta O/2 + H delta dotO/16,
]
[
Delta dotO = -3 delta O/H - delta dotO/4,
]
[
Delta K = delta K/2.
]

Historical z=.5 residual로 ||DeltaK||=0.07515459630271762/t_a이며, O 및 dotO separation도 0이 아닌 norm interval로 제한된다. 따라서 secondary refinement comparison은 실제로 구별 가능한 두 prediction을 fresh direct truth와 비교한다.

## 5. Reference uncertainty

Primary/secondary 모두 같은 direct B192 reference를 사용한다. 실제 authoritative reference bound epsilon_i가 별도로 확보된 경우에만 각 observed margin delta_i에 대해

[
delta_i^* in [delta_i-2 epsilon_i, delta_i+2 epsilon_i]
]

를 supplementary sensitivity로 계산할 수 있다.

현재는 `SOURCE_ACCURACY_BOUND_UNAVAILABLE`이며 1e-10 tolerance, metric-identity residual, bridge tolerance를 epsilon으로 대입하지 않는다.

## 6. Verification

새 post-result policy helper는 py_compile PASS, focused 7/7 PASS다. 9개 primary-secondary 조합이 모두 정의되고, 모든 조합에서

- auto_consume_z075_as_training=false
- auto_add_knot=false
- auto_execute_next_node=false

임을 테스트했다.

새 science node는 0개이며 direct z=0.75 output은 접근하지 않았다.

## 결론

R31AM 이후 다음 실제 physics action은 이미 R31AL에서 준비된 one-shot z=0.75 execution이다. 그 결과가 나오면 primary와 secondary를 prelocked order로 한 번 계산하고, 이 R31AM matrix의 action을 그대로 적용한 뒤 종료한다. 추가 knot/validation은 자동으로 열지 않는다.
