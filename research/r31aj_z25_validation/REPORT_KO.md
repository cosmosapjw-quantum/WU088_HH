# R31AJ: 중앙 cell 검증 범위와 reference-error 판정 강건성

## 기준과 현재 결론

정본은 WU088_HH R31AI branch의 commit `5058dee8862df87715be2aac75d3b8c4422ee096`, tree `33207b4d926b2b79110bb24c41cbf75af129fb6d`다. `research/r31ai_adaptive/ncp_followup_20260930/RETURN.json`과 원 preregistration, decision rule 및 변경 없는 interpolation engine을 직접 읽었다. Preregistration과 decision-rule 사본을 원문 형식으로 보존하고 SHA-256을 재계산해 원 보고값과 일치시켰다. 원 배열 일곱 세트를 다시 계산하거나 다운로드한 것은 아니다.

R31AI NCP 반환은 기존 일곱 node 재현, 내부 연속성, 401-point metric identity 최대 1.865411113237405e-16, focused 5 PASS를 보고한다. z=2.5 direct data는 미접근이며 execution_authorized=false다. 이는 parent의 실행 증거다. 이번 단계의 자체 검증은 별도의 새 진단 tests와 exact Wolfram 계산이며 합산하지 않는다.

다음 과학 실험은 이미 고정된 z=2.5 B192 mixed OD + independent JVP 한 점이다. 이번 단계는 새 node를 실행하지 않으며 원 모델, 입력, selection, primary rule을 변경하지 않는다. 새 핵심 결과는 (i) 그 검증이 시험할 수 있는 범위를 수식으로 제한하고, (ii) reference 불확실성이 상대 판정을 움직일 수 있는 한계를 유도한 것이다.

## 1. z=2.5는 무엇을 검증하는가: 직접 유도

시간 t에서 cell [t2,t3], h=t3-t2>0, u=(t-t2)/h라 하자. h=2.2358772390338113 t_a이며 archive 단위 t_a=hbar/E_h, z 단위는 a0다. O는 무차원, dotO,D,K는 inverse-time이다. C=D_col, B=D_row^dagger는 각각 47x2이며 K=(C-B)/2다. K는 full connection의 anti-Hermitian 부분에 속하는 mixed block이지, 직사각형 K 자체에 K=-K^dagger를 요구하지 않는다.

변경 없는 engine의 cubic Hermite O와 linear K는 cell 양 끝 자료만 사용한다. u=1/2에서

    O_mid = (O2+O3)/2 + h(dotO2-dotO3)/8,
    dotO_mid = 3(O3-O2)/(2h) - (dotO2+dotO3)/4,
    K_mid = (K2+K3)/2,
    Dcol_mid = dotO_mid/2 + K_mid,
    Drow_mid^dagger = dotO_mid/2 - K_mid.

따라서 [0,1]이나 [3,4]에서 knot를 추가해도 [2,3] endpoint 자료를 바꾸지 않는 한 이 식은 달라지지 않는다. Parent는 실제 z=2.5 prediction의 predecessor 차이를 다섯 block 모두 0으로 보고했다. 이번에는 SHA-verified 동일 engine을 사용한 synthetic test에서 외부 knot와 모든 외부 값을 바꿔도 [2,3) 내부 31개 probe의 다섯 block이 원소별로 같음을 확인했다.

결론: z=2.5는 여전히 valid fresh single-point test이지만, 직접 시험하는 대상은 중앙의 기존 [2,3] local interpolant와 R31Z global의 상대 성능이다. 양끝 추가 knot의 error-reduction factor나 refined half-cell 정확도를 직접 검증하는 실험은 아니다. 그 의미에서 이전의 regional validation 표현은 가능하지만 refinement gain validation이라는 표현은 불가하다. 다음 점이나 기존 selection을 이 이유로 바꾸지 않는다.

## 2. 큰 model separation의 한계: 명시적 반례

동일 normed response에서 A,G를 고정하고 미지의 direct response X를 두면

    ||A-G|| <= ||A-X|| + ||G-X||.

따라서 max(E_A,E_G)>=||A-G||/2다. z=2.5의 기존 half-gap 0.09561189201673985/t_a 및 0.10280590292237807/t_a는 이 의미에서 유효하다.

그러나 X=(A+G)/2라 두면 E_A=E_G=||A-G||/2다. Model separation을 임의로 크게 해도 승자가 정해지지 않는다. 따라서 separation/tolerance가 약 10^9라는 것은 원래의 finite-precision tie tolerance 대비 prediction 차이가 크다는 뜻이지, statistical power, 승자 확률, source-noise 대비 signal-to-noise ratio의 계산이 아니다. Historical HIGH_DISCRIMINATION_EXPECTED를 원 문서에서 지우지 않되, 이 보고서에서는 이를 확률적 보증으로 해석하지 않는다.

## 3. metric compatibility는 K의 accuracy certificate가 아니다

임의의 같은 크기 복소행렬 M에 대해

    C_new=C+M, B_new=B-M

이면 C_new+B_new=C+B이지만

    K_new=(C_new-B_new)/2=K+M.

따라서 dotO-C-B의 residual은 정확히 보존하면서 K 오차는 임의로 커질 수 있다. Wolfram의 exact symbolic 결과와 큰 M을 사용한 NumPy synthetic test에서 이 identity를 확인했다. 이는 실제 HH producer에 그런 오류가 있다는 주장도, physical basis를 바꾸자는 제안도 아니다. Metric-identity residual만으로 K의 source approximation error를 상계할 수 없다는 수학적 반례다.

Consequently, primary tolerance 1e-10/t_a, source-bridge tolerance, 약1e-16의 metric residual, B192 continuum quadrature error는 각각 별도의 양이다. 서로 대입하지 않는다. B192 numerical reference와의 relative agreement는 의미가 있지만, 그 값이 exact continuum reference라고 독립 입증되었다고 보지는 않는다.

## 4. reference 오차가 Pareto margin에 미치는 영향

같은 frozen representation에서 B192 reference를 R_hat, 관심 있는 정확한 reference를 R_star라 하고 ||R_hat-R_star||<=epsilon이 실제 확보되었다고 가정한다. 고정된 model prediction P에 대해 reverse triangle inequality로

    | ||P-R_star|| - ||P-R_hat|| | <= epsilon.

각 primary response i=K,Dmax의 관측 margin을

    delta_i = E_global,i - E_adaptive,i

로 정의한다. 양수는 adaptive를 지지한다. 두 error 각각에 위 부등식을 적용하면

    delta_i - 2 epsilon_i <= delta_i_star <= delta_i + 2 epsilon_i.

계수 2는 일반적으로 줄일 수 없다. 실수 scalar G=2,A=-2,R_hat=0,R_star=epsilon, 0<=epsilon<2에서 margin 변화는 정확히 -2 epsilon이다. Wolfram으로 exact 검산했다.

직접 block bounds가 epsilon_col,epsilon_row이면

    epsilon_K <= (epsilon_col+epsilon_row)/2,
    epsilon_Dmax <= max(epsilon_col,epsilon_row).

후자는 product-block norm max(||C||2,||B||2)를 사용한다. 모델을 다시 fitting하지 않고 prediction matrices를 고정하는 theorem이다. 모델 자체의 perturbation bounds alpha_A,i,alpha_G,i까지 포함하려면 radius를 2 epsilon_i+alpha_A,i+alpha_G,i로 확장해야 한다. 현재 물리모델 전체에 대한 그러한 bounds는 없다.

기존 Pareto rule의 tolerance를 tau라 하자. 모든 i에서 delta_i-2epsilon_i>=-tau이고 적어도 하나에서 delta_i-2epsilon_i>tau이면 adaptive support가 해당 uncertainty balls 전체에서 유지되는 충분조건이다. 원 primary rule과 별개인 supplementary conditional assessment이며, primary verdict를 덮어쓰지 않는다.

Reference bounds가 없을 때 epsilon=0으로 두지 않는다. `SOURCE_ACCURACY_BOUND_UNAVAILABLE`로 기록하고 원래 B192-reference verdict는 그대로 반환한다. 이 추가 진단 때문에 새 quadrature 계산을 자동 시작하지도 않는다.

## 5. 기존 z=3.5 결과의 sensitivity budget

원 `Z35_COMPARISON.json`의 R31AF/R31Z 값으로 계산한 관측 margin은

    delta_K    = 0.18425754717092629/t_a,
    delta_Dmax = 0.19707079580279067/t_a.

두 primary reference-error bound가 공통 epsilon 이하라고 가정하면

    epsilon < min_i (delta_i-1e-10/t_a)/2
            = 0.092128773535463145/t_a

에서 두 margin 모두 strict support를 유지한다. 이것은 편리한 보수적 충분조건으로, 가장 큰 Pareto robustness radius라고 주장하지 않는다. 특히 0.09212877/t_a는 actual source-error bound가 아니라, 추후 별도 source bound가 주어졌을 때 비교할 sensitivity budget이다. 현재 epsilon이 이 값보다 작다고 검증한 것은 아니다. 이 해석은 과거 z=3.5 primary verdict를 취소하거나 재분류하지 않는다.

## 6. 문헌과 근거 상태

SciSpace에서 numerical-reference uncertainty와 surrogate verification 문헌을 검색했고, 다음 원 논문 metadata/abstract를 web에서 대조했다.

[1] Bect et al., On the quantification of discretization uncertainty: comparison of two paradigms, arXiv:2103.14559 (2021). Discretization uncertainty를 model inadequacy 및 다른 uncertainty와 구분한다.
[2] Haasdonk et al., A new certified hierarchical and adaptive RB-ML-ROM surrogate model for parametrized PDEs, arXiv:2204.13454; DOI 10.1137/22M1493318. Certification에는 실제 a posteriori error bound를 사용한다.
[3] Galetzka et al., An hp-adaptive multi-element stochastic collocation method for surrogate modeling with information re-use, arXiv:2206.14435; DOI 10.1002/nme.7234. 기존 evaluations를 local refinement에 재사용한다. Preprint는 2022, journal publication은 2023이다.

이 문헌들은 HH의 정확성을 인증하지 않는다. 본 보고서의 locality, metric-null perturbation, margin bounds는 위에 제시한 직접 유도이며, Wolfram exact checks와 별도 synthetic tests를 수행했다. WolframContext retrieval의 무관한 snippets는 근거로 사용하지 않았다.

## 7. 실행과 남은 범위

새 tests: 18 PASS, failure/error/skip 0. Py_compile/replay exit0. RED에서 미구현 새 함수로 인한 14 failures와 기존 engine/반례 checks의 4 passes를 보존했다. 새 과학적 HH 배열·native node·trajectory는 0이며 z=2.5 direct값은 미접근이다. Parent NCP tests 5개를 재실행하거나 합산하지 않았다.

새 파일은 additive research diagnostics와 실행 인계뿐이다. 원 R31AI/R31Z, seven-node data, preregistration, primary rule을 수정하지 않는다. Scope는 ASCII JSON의 decimal-string quantities로 정의하고 exact canonical bytes 파일을 제공하여 float serialization 차이를 피한다. 이 문서는 실행 승인 자체가 아니다.

다음 행동은 사용자가 별도로 승인한 경우에만 기존 prereg의 z=2.5 B192 mixed OD/JVP 한 번을 실행하고 원 Pareto verdict와 mandatory secondary outputs를 반환하는 것이다. 이미 source가 변하지 않은 동일 preflight 결과가 있으면 동일 preflight만 반복해 새 PR을 만들지 않는다. 승인 없으면 현재 상태를 한 번 알리고 멈춘다. 승인된 결과 뒤에는 automatic training consumption, new knot, second node 없이 종료한다.
