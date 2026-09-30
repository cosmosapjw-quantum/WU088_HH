# R31AI: z=3.5 validation을 소비한 adaptive seven-node successor

기준 parent는 `51eb022eb01445ffaef58e8a0078ecd3b779b30c`, tree `068e4de6dce4a50cc28ead4c84a2e935146aee05`이다. R31AG/R31AH one-shot z=3.5 validation은 preregistered Pareto rule에서 `PARETO_SUPPORTED_AT_Z35`로 종료했고, R31AH action tree에 따라 successor refinement 후보를 [3,4] cell에만 허용했다.

## 1. z=3.5 결과의 상대/절대 해석

R31AF adaptive-six-node:

- E_O = 0.028316443455109017
- E_dotO = 0.02180471880970521 /t_a
- E_K = 0.06617406868623811 /t_a
- E_Dmax = 0.06827426878354666 /t_a

R31Z global:

- E_O = 0.07430484151052544
- E_dotO = 0.10523038116989783 /t_a
- E_K = 0.2504316158571644 /t_a
- E_Dmax = 0.26534506458633733 /t_a.

따라서 R31AF의 상대 개선율은 약

- E_O: 61.89%
- E_dotO: 79.28%
- E_K: 73.58%
- E_Dmax: 74.27%

이다.

그러나 R31AF의 absolute E_K, E_Dmax는 여전히 0.066--0.068/t_a이므로 interval-wide adequacy가 닫힌 것은 아니다. E_K/E_dotO≈3.035이며 E_Dmax/E_K≈1.032이므로, 남은 D error 규모도 connection-sector K와 같은 order로 지배된다.

## 2. z=3.5 midpoint residual의 local derivative lower bound

[3,4] cell의 시간 폭은

[
h_t=2.2358772390338113,t_a,
]

z 폭은 (h_z=1a_0)다.

Cubic-Hermite O midpoint error와 linear-K midpoint error에 대한 standard norm remainder inequality를 사용하면, smooth represented source가 direct z=3.5 residual을 재현하기 위해 필요한 necessary lower bound는

[
sup ||d^4 O/dt^4||_2
ge 0.4350890062991452/t_a^4,
]

[
sup ||d^2 K/dt^2||_2
ge 0.10589657526007562/t_a^3.
]

z-coordinate에서는

[
sup ||d^4 O/dz^4||_2
ge 10.873514286761862/a_0^4,
]

[
sup ||d^2 K/dz^2||_2
ge 0.5293925494899049/(t_a a_0^2).
]

이것은 actual direct residual에서 얻은 local necessary bound이며 source/roundoff interval enclosure가 아니다.

## 3. R31AI seven-node model

R31AH policy에 따라 z=3.5 validation credit을 successor training으로 소비한다.

Training nodes:

[
{0,0.5,1,2,3,3.5,4}.
]

Cells:

[
[0,0.5], [0.5,1], [1,2], [2,3], [3,3.5], [3.5,4].
]

Interpolation law는 R31AD/R31AF와 동일하다.

- O: each cell endpoint O,dotO cubic Hermite
- K=(D_col-D_row†)/2: endpoint linear
- D_col=dotO/2+K
- D_row†=dotO/2-K.

즉 새 model family가 아니라 [3,4]에 knot 하나를 추가한 local h-refinement다.

동일 derivative upper bound라는 조건부 가정 아래 [3,4] cell을 반으로 나누면 standard midpoint remainder coefficient는

- O cubic: 1/16
- K linear: 1/4

로 줄어든다. 실제 HH error reduction factor라고 주장하지 않는다.

## 4. 왜 data reuse가 허용되는가

z=3.5는 R31AF의 독립 validation이었지만, R31AI를 만드는 순간 그 independent credit은 소모된다.

R31AI provenance:

- z0,z0.5,z1,z2,z3,z4 = prior training
- z3.5 = PRIOR_INDEPENDENT_VALIDATION_CONSUMED_AS_R31AI_TRAINING
- R31AI independent validation points = [].

z=3.5에서 얻은 support와 z=3.5를 사용해 만든 R31AI를 두 개의 독립 validation evidence로 중복 계상하지 않는다.

SciSpace current-loop 검색은 local residual/error-indicator 기반 knot insertion과 information reuse의 방법론적 배경을 확인했다.

- Galetzka et al., DOI 10.1002/nme.7234: h/p adaptive multi-element collocation에서 기존 model evaluations의 reuse.
- Patrizi et al., arXiv:2001.11236: locally refined spline의 adaptive refinement와 local structural properties.
- Bracco et al., arXiv:2311.09442: local indicator가 refinement location을 결정하는 spline approximation.

이 문헌은 WU088_HH의 error bound를 대신 증명하지 않는다.

## 5. z=2.5를 next fresh holdout으로 보존

R31AI의 새 knot는 [3,4]에만 추가되고, 기존 z=0.5 refinement는 [0,1]에만 있다. 따라서 z=2.5의 [2,3] prediction은 R31AF/R31AD와 동일하게 frozen된다.

Pre-output R31AI-vs-R31Z information:

- DeltaK = 0.1912237840334797 /t_a
- DeltaDmax = 0.20561180584475613 /t_a
- S = 0.280789512416017 /t_a
- truth-independent K half-gap = 0.09561189201673985 /t_a
- truth-independent Dmax half-gap = 0.10280590292237807 /t_a.

z=2.5는 아직 direct output이 접근되지 않았고 future independent validation으로 보존한다.

## 6. current-loop implementation verification

새 successor policy helper는

- py_compile PASS
- focused tests 5/5 PASS

였다. 이 helper는 derivative lower bounds, z=3.5 provenance consumption, seven-node cell layout, z=2.5 holdout information만 다루며 HH native source를 호출하지 않는다.

새 science node count는 0이다.

## 7. 다음 NCP 작업

다음 handoff에서는 새 science 계산 없이 existing z={0,0.5,1,2,3,3.5,4} direct arrays를 조립해 R31AI seven-node model을 실제 재현하고 z=2.5 preregistration을 hash-lock한다.

z=2.5 실행은 별도 authorization decision으로 남긴다.

## claim ceiling

R31AI construction 자체는 다음을 닫지 않는다.

- predictive validation
- interval-wide interpolation error
- transition amplitude/error
- full-cell neutral/H authority
- complete-HH fixed-Q physical invariance
- BR01/BR02
- independent project review
- H-skip
- production.
