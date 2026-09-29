# R31AF: z=0.5 a posteriori refinement와 다음 fresh validation

기준 parent는 `1f5aa1584e2e057adc29673689fd5ab6ccdde85a`, tree `a1c327993fde0a0c430b42ce96f624311b98ff5d`이다. R31AE one-shot z=0.5 validation은 `PARETO_SUPPORTED_AT_SELECTED_MIDPOINT`로 종료했고, direct metric identity도 roundoff 수준에서 닫혔다.

## 1. z=0.5 결과의 상대·절대 해석

R31AD five-node unit-cell model:

- E_O = 0.0875296210906087
- E_dotO = 0.06210196649428255 /t_a
- E_K = 0.15030919260543524 /t_a
- E_Dmax = 0.1677736075942363 /t_a

R31Z global:

- E_O = 0.12803431013849245
- E_dotO = 0.1500620371912569 /t_a
- E_K = 0.32379090898828017 /t_a
- E_Dmax = 0.3382471014885593 /t_a.

따라서 R31AD의 상대 개선은 각각 약 31.64%, 58.62%, 53.58%, 50.40%다. 그러나 R31AD 자체의 E_K와 E_Dmax는 0.15--0.17/t_a 수준이므로 absolute adequacy가 닫힌 것은 아니다.

또 R31AD에서 E_K/E_dotO ≈ 2.420이고 E_Dmax/E_K ≈ 1.116이다. 즉 이 midpoint의 남은 D error에서도 connection-sector 오차가 주요 규모다.

## 2. midpoint direct error를 derivative lower bound로 변환

[0,1] cell의 시간 폭은

[
h_t = 2.2358772390338113,t_a,
]

공간 폭은 (h_z=1,a_0)다.

Cubic Hermite midpoint remainder와 linear K interpolation의 표준 norm inequality를 쓰면, 정확한 smooth source가 direct midpoint error를 재현하려면 최소한

[
sup ||d^4 O/dt^4||_2
ge rac{384 E_O}{h_t^4}
=1.3449138103246667/t_a^4,
]

[
sup ||d^2 K/dt^2||_2
ge rac{8 E_K}{h_t^2}
=0.24053574221790144/t_a^3.
]

z-coordinate로는

[
sup ||d^4 O/dz^4||_2
ge33.611374498793744/a_0^4,
]

[
sup ||d^2 K/dz^2||_2
ge1.202473540843482/(t_a a_0^2).
]

이들은 direct z=0.5 residual에서 얻은 **necessary lower bounds**다. Source/roundoff interval enclosure는 아니다.

이 수치는 [0,1] cell이 단순한 low-curvature region으로 취급될 수 없음을 직접 보여준다.

## 3. R31AF adaptive-six-node model

z=0.5는 R31AD에 대한 독립 validation credit을 이미 사용했다. R31AF에서는 이를 training으로 소비한다.

Training nodes:

[
{0,0.5,1,2,3,4}.
]

Cells:

[
[0,0.5], [0.5,1], [1,2], [2,3], [3,4].
]

Interpolation law 자체는 R31AD와 동일하다.

- O: 각 cell endpoint O,dotO의 cubic Hermite
- K=(D_col-D_row†)/2: endpoint linear
- D_col=dotO/2+K
- D_row†=dotO/2-K.

즉 refinement는 모델 family를 바꾸는 것이 아니라 [0,1] cell에 knot 하나를 추가하는 local mesh refinement다.

동일 derivative upper bound라는 **조건부** 가정 아래 cell 폭을 1에서 0.5로 줄이면 midpoint remainder coefficient는

- O cubic: 16배 감소
- K linear: 4배 감소

한다. 이것을 실제 HH error reduction factor라고 단정하지 않는다.

## 4. 왜 local refinement가 방법론적으로 맞는가

SciSpace current-loop 검색에서:

- Jakeman & Roberts, arXiv:1110.0010: hierarchical surplus/local error indicator가 큰 region만 선택적으로 refinement.
- Buffa & Giannelli, DOI 10.1142/S0218202516500019: local a posteriori indicator와 marking을 이용한 hierarchical spline refinement.
- Figueroa, Garau & Morín, DOI 10.1016/j.amc.2024.128616: local spline error indicator와 knot-level adaptive decisions.

이 문헌들은 WU088_HH error bound를 증명하지 않는다. 현재 적용하는 원칙은 **이미 얻은 local direct residual을 refinement indicator로 사용하고, 다른 cell의 validation data를 불필요하게 소비하지 않는 것**이다.

## 5. 다음 독립 validation은 z=3.5

R31AF의 수정은 [0,1]에만 국한된다. 따라서 z=2.5,3.5에서 R31AF prediction은 R31AD와 동일하다.

R31AD의 pre-output fresh candidate table에서:

- z=2.5: S=0.280789512416017
- z=3.5: S=0.2836776637729875.

z=0.5를 training으로 소비한 뒤 동일 selection policy를 적용하면 다음 fresh point는 `z=3.5`다.

z=3.5 frozen R31AF/R31Z model separation:

- DeltaK = 0.19122378403347964 /t_a
- DeltaDmax = 0.2095387347094023 /t_a
- S = 0.2836776637729875 /t_a.

따라서 direct truth와 무관하게 적어도 한 model은

[
E_K ge 0.09561189201673982/t_a,
]

[
E_{D,max} ge 0.10476936735470115/t_a
]

오차를 갖는다.

z=3.5는 z=0.5 refinement의 영향을 받지 않는 다른 cell [3,4]의 midpoint이므로 regional generalization을 검증하는 데 적합하다.

## 6. provenance relabel

R31AF construction 시:

- z0,z1,z2,z3,z4: existing training
- z0.5: PRIOR_INDEPENDENT_VALIDATION_CONSUMED_AS_R31AF_TRAINING
- z3.5: FUTURE_FRESH_VALIDATION_PREREGISTERED_NOT_EXECUTED.

따라서 R31AF는 construction 직후 independent validation point를 0개 가진다.

z=0.5를 R31AF의 validation으로 다시 세지 않는다.

## 7. stop policy

이번 R31AF node에서는 새 science node를 실행하지 않는다.

다음 단계는:

1. existing z=0,0.5,1,2,3,4 source arrays를 NCP에서 조립,
2. adaptive-six-node replay,
3. z=3.5 prereg lock,
4. science-node count 0으로 종료.

z=3.5 실행은 별도 structured authorization을 기다린다.

한 z=3.5 결과로 interval-wide/transition/full-cell/production을 자동 승인하지 않는다.
