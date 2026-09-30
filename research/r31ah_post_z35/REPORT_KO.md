# R31AH: z=3.5 결과 이후 action tree 사전등록

기준 parent는 `c6d00e79cfd76366af868a3a550aebbee46135cf`, tree `6f935a4ac4284ee317c1575554c81ca74f28f11c`이다. R31AG preflight는 z=3.5 science node를 실행하지 않았고, structured authorization을 기다리는 상태다.

이번 노드는 z=3.5 결과를 보기 전에 **결과 이후의 후속 행동을 고정**한다. 목적은 validation 결과를 본 뒤 모델을 임의로 계속 손보는 self-consuming loop를 막는 것이다.

## 1. z=3.5 verdict 이후의 mutually exclusive action

Frozen prereg verdict는 정확히 셋 중 하나다.

1. `PARETO_SUPPORTED_AT_Z35`
2. `GLOBAL_SUPPORTED_AT_Z35`
3. `TRADEOFF_UNRESOLVED`

### Case A: PARETO_SUPPORTED_AT_Z35

R31AF가 z=3.5에서 relative support를 얻었다고 보고한다. 그러나 interval-wide accuracy나 production을 열지 않는다.

그 뒤에만 z=3.5 direct residual을 [3,4] cell의 local a posteriori indicator로 사용할 수 있다. Successor model을 실제로 만들 경우 z=3.5는

`PRIOR_INDEPENDENT_VALIDATION_CONSUMED_AS_SUCCESSOR_TRAINING`

으로 relabel한다. 즉 같은 z=3.5를 successor의 validation evidence로 다시 세지 않는다.

Successor가 [3,4]만 local refinement한다면 아직 fresh한 다음 독립 point는 z=2.5다. 자동 실행은 금지하고 preregistration만 허용한다.

### Case B: GLOBAL_SUPPORTED_AT_Z35

R31AF adaptive strategy가 unaffected right cell에서 상대 우세를 재현하지 못한 것으로 취급한다. 자동 local refinement나 polynomial retuning을 시작하지 않는다.

`STOP_FOR_MODEL_CLASS_REVIEW`

로 종료하고, local-refinement family를 계속할지 global/nonlocal representation을 재검토할지 별도 연구 node에서 결정한다.

### Case C: TRADEOFF_UNRESOLVED

마찬가지로 자동 retuning을 금지한다.

`STOP_FOR_MODEL_CLASS_REVIEW`

로 종료한다.

즉 z=3.5 결과 하나를 보고 무조건 다음 knot를 추가하는 루프는 허용하지 않는다.

## 2. z=3.5 residual이 support 이후 refinement indicator가 되는 방식

z=3.5는 [3,4] cell의 midpoint다. Cell time width는

[
h_t=2.2358772390338113,t_a
]

이고 spatial width는 (h_z=1a_0)다.

R31AF direct midpoint errors를 (E_O,E_K)라 하면 standard midpoint remainder inequality에서

[
sup ||O^{(4)}||_2 ge rac{384E_O}{h_t^4},
]

[
sup ||K''||_2 ge rac{8E_K}{h_t^2}.
]

z-coordinate에서는

[
sup ||d^4O/dz^4||_2 ge 384E_O,
]

[
sup ||d^2K/dz^2||_2 ge 8E_K
]

(현재 (h_z=1))다.

이 bound는 exact represented midpoint residual을 가정한 necessary lower bound이며 source-error interval enclosure가 아니다.

만약 [3,4]를 [3,3.5],[3.5,4]로 쪼개고 동일 derivative upper bound가 유지된다는 조건부 가정을 하면 standard remainder coefficient는

- cubic O: (1/16)
- linear K: (1/4)

로 감소한다. 실제 HH error가 정확히 그 비율로 줄어든다는 의미는 아니다.

## 3. 왜 z=2.5를 다음 holdout으로 보존하는가

현재 pre-output fresh candidate table에서 z=2.5는 아직 direct truth를 사용하지 않은 점이고

- DeltaK = 0.1912237840334797 /t_a
- DeltaDmax = 0.20561180584475613 /t_a
- S = 0.280789512416017 /t_a

이다.

따라서 direct truth와 무관하게 적어도 한 model은

[
E_Kge0.09561189201673985/t_a,
]

[
E_{D,max}ge0.10280590292237807/t_a
]

오차를 갖는다.

z=3.5 결과를 training으로 소비해 [3,4]를 수정하더라도 z=2.5는 [2,3] cell에 있어 직접 영향권 밖이다. 따라서 successor의 regional generalization을 검사할 fresh point로 남길 수 있다.

## 4. adaptive-data provenance

SciSpace에서 Dwork et al.의 reusable holdout (Science 2015, DOI 10.1126/SCIENCE.AAA9375)과 후속 adaptive-data-analysis 논의를 확인했다. 핵심 방법론적 교훈은 adaptively 본 validation result를 다시 tuning에 사용했다면 그 데이터를 같은 모델의 independent confirmation으로 재사용해서는 안 된다는 것이다.

또 sequential design 문헌은 이미 관측된 local residual을 refinement에 쓰더라도 다음 holdout을 별도로 보존하는 구조가 자연스럽다는 배경을 제공한다.

이 문헌은 WU088_HH의 물리 정확도를 직접 증명하지 않는다.

## 5. stop condition

R31AH는 z=3.5 science node를 실행하지 않는다.

R31AG authorization gate와 scope는 그대로 유지한다.

z=3.5 결과 이후에는 위 action tree만 허용한다. 자동 z=2.5 실행, model retuning, H/full49/trajectory 진입은 모두 금지한다.

## 6. claim ceiling

어떤 z=3.5 verdict도 자동으로 다음을 열지 않는다.

- interval-wide interpolation accuracy
- transition amplitude/error
- full-cell authority
- fixed-Q complete-HH physical invariance
- trajectory
- H-skip
- production
- BR01/BR02
- independent project review.
