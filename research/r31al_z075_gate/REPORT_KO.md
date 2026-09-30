# R31AL: z=0.75 refined-half-cell validation design

기준 parent는 `8bfd2494839dacb2124a8e9fc4fadc9d010e7003`, tree `d26802b8169ff97407f184f75a4be96e3fb2b1a1`이다. R31AK NCP follow-up은 새 science node 없이 eight-node model을 재현하고, fresh prediction-only 후보 중 z=0.75 a0를 선택해 preregistration을 잠갔다.

## 1. primary selected holdout

Parent selection에서 z=0.75:

- time = 1.6769079292753586 t_a
- DeltaK(R31AK,R31Z) = 0.3418463058618517 /t_a
- DeltaDmax = 0.3504308143080971 /t_a
- S = 0.4895514808965761 /t_a.

따라서 direct truth와 무관하게 적어도 한 primary model은

[
E_Kge0.17092315293092586/t_a,qquad
E_{D,max}ge0.17521540715404854/t_a
]

오차를 갖는다.

두 번째로 큰 candidate z=3.25의 S=0.41211921575445415와의 margin은 0.07743226514212193, 상대 약 18.79%다. Selection은 direct truth 없이 수행되었고 z=0.75 direct output은 미접근이다.

이 S는 experiment-design criterion일 뿐 final verdict score가 아니다. Primary frozen comparison은 parent prereg의 R31AK-vs-R31Z E_K/E_Dmax Pareto rule을 그대로 사용한다.

## 2. z=0.75가 특별한 이유: 실제 h-refinement gain을 직접 시험

z=0.75는 R31AK cell [0.5,1]의 정확한 midpoint다. 이 cell은 과거 z=0.5 direct validation을 training knot로 소비하여 coarse [0,1]을 split하면서 생겼다.

Pre-refinement predecessor R31AD는 coarse [0,1] cell을 사용했다. 따라서 같은 fresh z=0.75 direct truth로:

1. R31AK refined [0.5,1] prediction,
2. R31AD coarse [0,1] prediction

을 동시에 비교하면 local h-refinement 자체가 실제 out-of-sample error를 줄였는지 직접 측정할 수 있다.

이 secondary comparison은 point selection 후이지만 direct output access 전에 정의되므로, primary를 변경하지 않는 pre-output secondary amendment로 lock한다.

## 3. exact refinement-propagation identity

coarse [0,1]의 시간 폭을 H라 하고 z=0.5에서 direct-minus-coarse correction을

[
delta O,quad deltadot O,quad delta K
]

라 하자. Coarse cubic을 [0.5,1]에 restrict한 polynomial과 refined cubic은 z=1 endpoint를 공유하며 z=0.5 endpoint만 위 correction만큼 다르다.

Wolfram exact algebra와 별도 NumPy synthetic test로 z=0.75에서

[
O_{m ref}-O_{m coarse}
=rac12delta O+rac{H}{16}deltadot O,
]

[
dot O_{m ref}-dot O_{m coarse}
=-rac{3}{H}delta O-rac14deltadot O,
]

[
K_{m ref}-K_{m coarse}
=rac12delta K
]

를 확인했다. 따라서

[
D_{m col,ref}-D_{m col,coarse}
=rac12(dot O_{m ref}-dot O_{m coarse})
+(K_{m ref}-K_{m coarse}),
]

[
D_{m row,ref}^{dagger}-D_{m row,coarse}^{dagger}
=rac12(dot O_{m ref}-dot O_{m coarse})
-(K_{m ref}-K_{m coarse}).
]

## 4. 이미 관측된 z=0.5 correction이 z=0.75 prediction에 주는 최소 정보

R31AD의 z=0.5 direct errors:

- ||delta O|| = 0.0875296210906087
- ||delta dotO|| = 0.06210196649428255 /t_a
- ||delta K|| = 0.15030919260543524 /t_a
- H = 2.2358772390338113 t_a.

따라서 z=0.75에서 refined-vs-coarse K prediction separation은 정확히

[
||Delta K||=0.07515459630271762/t_a.
]

방향 정보 없이 norm만 사용하면

[
0.03508653720881643
le||Delta O||le
0.05244308388179227,
]

[
0.1019178360724072/t_a
le||Deltadot O||le
0.1329688193195485/t_a.
]

즉 refined와 coarse prediction은 z=0.75에서 실질적으로 다른 model prediction이다. 특히 K shift는 primary R31AK-vs-R31Z K separation의 약 21.98%다.

이는 refinement가 개선되었다는 증명은 아니다. Direct z=0.75 truth가 어느 prediction에 더 가까운지는 아직 미지다.

## 5. secondary refinement-gain preregistration

Primary는 변경하지 않는다:

- R31AK_ADAPTIVE_EIGHT_NODE_CUBIC_O_LINEAR_K
- R31Z_GLOBAL_QUINTIC_O_QUADRATIC_K
- E_K, E_Dmax
- tolerance 1e-10/t_a
- parent verdict set 유지.

Secondary는 direct output 전에 다음으로 고정한다:

- refined = R31AK_ADAPTIVE_EIGHT_NODE_CUBIC_O_LINEAR_K
- coarse = R31AD_FIVE_NODE_UNIT_CELL_CUBIC_O_LINEAR_K
- primary secondary-metrics = E_K, E_Dmax
- same tolerance 1e-10/t_a
- verdicts:
  - REFINED_PARETO_SUPPORTED_AT_Z075
  - COARSE_PARETO_SUPPORTED_AT_Z075
  - REFINEMENT_TRADEOFF_UNRESOLVED.

Mandatory secondary 기록:

- both models의 E_O,E_dotO,E_K,E_Dcol,E_Drow,E_Dmax
- direct/candidate metric identity residual
- actual improvement fractions refined vs coarse.

Secondary verdict는 primary R31AK-vs-R31Z verdict를 덮어쓰지 않는다.

## 6. literature context

SciSpace current-loop review:

- Thomas et al., Bézier projection, arXiv:1404.7155: element-local refinement/coarsening과 local projection.
- Dębski, DOI 10.7494/CSCI.2020.21.4.3932: C1 cubic Hermite-type interpolation의 numerical comparison.
- Bertrand et al., DOI 10.1007/s00211-023-01366-8: local a posteriori error control과 adaptive refinement effectiveness validation.

이 문헌들은 WU088_HH accuracy를 증명하지 않는다. 여기서 사용하는 refinement-propagation identity는 직접 유도했다.

## 7. protocol hardening

R31AK가 z=2.5 protocol deviation 뒤 preimplemented한 metadata adapter를 그대로 사용한다. JSON number/string z를 Decimal로 normalize하는 adapter는 direct output 전에 이미 hash-lock되어 있다.

R31AL NCP follow-up은 direct output 전에:

1. R31AD coarse z=0.75 prediction을 existing z=0,1 source arrays에서 생성,
2. R31AK refined prediction과 비교,
3. secondary prediction/comparator/rule을 hash-lock,
4. parent primary prereg와 secondary amendment를 함께 묶은 final authorization scope를 생성

하고 stop해야 한다.

새 science node는 실행하지 않는다.

## 8. claim ceiling

z=0.75 한 점이 future execution에서 refined model을 지지하더라도:

- interval-wide accuracy,
- 모든 refined cell의 convergence,
- B192 continuum/source accuracy,
- transition error,
- full-cell authority,
- fixed-Q physical invariance,
- BR01/BR02,
- trajectory,
- H-skip,
- production

은 자동 승인하지 않는다.

현재 SOURCE_ACCURACY_BOUND_UNAVAILABLE도 유지한다.
