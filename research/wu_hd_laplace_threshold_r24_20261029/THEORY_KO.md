# WU R24: GL2022 원본 열반응률의 양의 Laplace 지지문턱 검사

**연구 상태:** 직접 유도/수치 검산된 **조건부 필요조건**. GL2022 실제 PES-native threshold, physical-Q, bath-heat 인증은 아님. 2026-10-29 KST.

## 1. 고정 물리 채널, 원본, 가정

반응: `H+ + HD(X,v=0,j=2) -> D+ + H2(X,v'=0,j'=1)` (이온 교환; 중성 H+HD 산란 아님). R18 원본 Git HEAD `f7371c7c389cac9c1b504f6e741b80ea80d776f1`, row blob `08fdadd5dc366c00b8b546fcc9820bf030f3ae6c`, GL2022 부록 Table 2 p.6, PDF SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. 10개 온도와 원문 인쇄 지수형 토큰을 src JSON에 고정. 원 논문 doi:10.1063/5.0128598, Velilla PES doi:10.1063/1.2973629.

다음은 **GL2022의 현재 구현에서 증명된 사실이 아니라 이 검사를 정의하기 위한 조건**이다.

(A1) GL2022 Eq. (4)의 E는 반응물 입사 채널에 상대적인 **충돌 운동에너지**로 `E>=0`이고, 해당 상태의 고정 온도 비의존 단면적 σ(E)로부터 Maxwell 평균을 정확히 계산한다.

(A2) σ(E)>=0이며 문턱 θ>=0 아래에서 σ(E)=0이고, 모든 고려 온도에서 동일한 함수이다. 총 회전 열분포/상태별 동역학, 온도의존 혼합 또는 충돌 에너지 축 이동은 없다.

(A3) 원문 인쇄된 `(0,2)->(0,1)` 10개 k(T)는 상태별 raw 값이며, 외부 홀수 j'=1 핵스핀 3/4 가중치나 단위 변환은 온도 **상수** 배율이라 비율에서 소거된다. 인쇄 반올림만으로 원본 계산 정확도가 인증되지는 않는다.

기본 SI k_B=1.380649e−23 J/K 및 e=1.602176634e−19 J/eV 정확한 상수를 사용하여 `k_B = 0.086173332621451774... meV/K`로 변환한다. μ는 고정 입사 감소질량이므로 본 비율에서는 소거된다.

## 2. 직접 유도: 에너지 지지 문턱 상한

원문 Eq. (4)의 상태별 반응률을

`k(beta)=sqrt[8/(pi mu)] beta^(3/2) int_0^infty sigma(E) E exp(-beta E) dE`

로 쓴다. `g(E)=E sigma(E)>=0`, `L(beta)=int_theta^infty g(E) exp(-beta E) dE`, `k=C beta^(3/2) L`.

서로 다른 β1>β2>0에서 E>=θ이므로 `exp(-β1 E) <= exp[-θ(β1-β2)] exp(-β2 E)`. 양의 g로 적분하여

`L(β1)/L(β2) <= exp[-θ(β1-β2)]`.

따라서 (두 양의 반응률에서만 정의됨)

`θ <= Θ12 = { ln[k(T2)/k(T1)] + (3/2) ln[β1/β2] } / (β1-β2)`.

이는 Arrhenius fit, 단면적 상수성 근사, 높은 온도 asymptotics가 필요없는 **필요조건**이다. 모든 i<j (45쌍)에 성립한다. 일반 정규화 factor `c>0`, SI 단위 cm^3→m^3, T에 독립적인 3/4 spin weight는 정확히 상쇄된다. 이 결과로 θ의 **하한** 또는 θ의 유일한 추정은 얻지 못한다.

추가 필요조건: 충분한 적분가능성을 가정하면 `-∂β log L = <E>β >= θ`, `∂²β log L=Varβ(E)>=0`. 양의 Laplace 변환은 log-convex하므로 점별 인접 secant들의 순서도 제한된다. 10개 인쇄값은 이 **이산 log-convex 필요조건을 통과**하지만 그것만으로 모든 물리/쿼드러처 적격성이 증명되는 것은 아니다.

## 3. 원본 채널 15 K / 55 K 적용

원문 인쇄 Table 2: 15 K k=3.99e-14 cm³s^-1, 55 K k=2.92e-11 cm³s^-1. 소수부/지수 분리에서 `(14)`는 ±14 오차가 아니라 10^-14 지수다.

정확한 SI 상수 + Decimal70로 계산하면

`Θ15,55 = 15.18630382175889727368776395345... meV`.

모든 45쌍의 최소 필요 상한이 이 15–55 K 쌍이다. 원문 유효숫자 `3.99`,`2.92`가 각자 ±0.005의 nearest-rounding 표현이라고 **가정한 경우만** 최대 `15.19157320477320978... meV`. 자료의 알려지지 않은 모델·수치·물리오차를 포괄하는 보증 bound는 **아니다**.

R23의 이론적으로 독립인 외부 분광학적 후보 `θ_spectro=20.950020993840457590567... meV`는 이 상한보다 `5.7637171720815603... meV` 높다. A1–A3과 θ>=θ_spectro가 모두 참이라면 55 K에서 15 K로의 반응률비는 인쇄값의 최대 약 **1/25.6083089316742**이어야 한다. 따라서 여기에는 심각한 **조건부 모델·에너지축·원본 데이터 대조 필요성**이 있다. 아직 논문 오류, 물리적 반응열 값, 실제 Velilla-PES 문턱의 부정은 인증되지 않았다.

## 4. 에너지 변수의 원문 ambiguity

GL2022 본문 Eq.(3)의 입사 wave number는 `k_vj²=2 μ (E−E_vj)/ħ²` 형태로 총에너지와 입사 내부 에너지 차이를 사용한다. Eq.(4)의 적분은 `int σ(E) E exp(-β E) dE`로 표기되어 E의 zero가 **입사 충돌 에너지로 다시 설정됐는지** 명시적 코드 경로·입력 grid 또는 문턱표를 통해 대조해야 한다. 수식 문자의 재사용 자체를 논문 버그로 단정하지 않는다.

선행 연구 Lepers et al. (2019, doi:10.1093/mnras/stz1797)는 같은 Velilla-PES를 쓰는 **별도 코드**에서 H/D 원자 이온화 차이를 생략한다고 밝힌다. 이 사실만으로 GL2022가 포함했는지 생략했는지를 판단할 수 없다. PR #160의 cross-PES diagnostic, PR #161/R23의 spectroscopic Q는 GL2022-native PES 문턱이 아니다.

현재 가능한 분기: (i) source-native θ가 분광학적 θ보다 낮음, (ii) 열반응률 적분의 E 원점/변환이 다름, (iii) 실제 인쇄/계산/가중/온도 수입이 A1–A3과 다름. 위 분석은 **판별 실험의 위치**를 지시하지 어느 한 가설을 증명하지 않는다.

## 5. 양의 finite-Laplace inverse 비유일성: 구성적 예

온도 β_i가 서로 다른 유한 n개(현재 n=10)일 때 양의 분포 g(E)의 Laplace 값 L(β_i)만으로 support의 infimum을 항상 유일하게 정할 수 없다. n개의 서로 다른 E_j>θ_0에 대한 `M_ij=exp(-β_i E_j)`은 exponential Chebyshev system에 의해 가역이다. 양의 a_j=1, 더 낮은 E_low<θ_0에서 v_i=exp(-β_i E_low)를 정의하고 `c=-M^-1 v`라 하자. 충분히 작은 δ>0을 택하면 `a_j+δ c_j>0`이고

`Σ_j a_j exp(-β_i E_j) = Σ_j (a_j+δc_j) exp(-β_i E_j) + δ exp(-β_i E_low)`

이 모든 i에서 **정확히** 성립한다. 따라서 두 양의 이산 measure의 onset은 달라도 10개 Laplace 관측은 같다. 적절한 서로 떨어진 좁은 C∞ bump로 M을 대체하면 행렬식의 연속성과 양의 계수 여유를 통해 같은 현상의 부드러운 g(E)>=0 예가 존재한다. 이는 broad nonnegative-function class에 대한 수학적 구성이지 실제 원본 k(T) 혹은 quantum S-matrix가 두 PES를 허용한다는 뜻은 아니다.

mpmath125 구현 예는 support `{20,23,...,47}` meV와 12 meV extra point를 사용했다. Added weight = `1.505336651056789...e-6`이고 고에너지 계수 최소 `0.561170049... >0`, 10개 sample 상대 잔차 최고 `<1e-125`. 코드의 discrete δ measure가 물리적 연속 단면적은 아님을 명시한다. 이 결과는 새로운 strong no-go의 문헌상 독창성 주장 없이 제한된 양성 역문제의 구조적 주의점으로 사용한다.

## 6. 수용/차단 경계

**Derived + Wolfram + Decimal/mpmath checked:** 위 필요조건, 15–55 K 상한, 합성 양의 measure 증인.

**Literature-supported:** Velilla2008 PES 사용, 2022 Eq3/Eq4의 서로 다른 energy notation, R18 인쇄 10개 source table, 2019 별도 BO 이온화 보정 생략.

**Unresolved:** GL2022 Eq4 실제 numerical E-axis/threshold (0,2)->(0,1), 원본 cross-section grid, total-to-collision conversion, state-specific scatter code ionization correction, actual physical Q, thermal bath, reverse chemistry, full-A, target REC/CR owner ACK.

R6/C9 독립 저자 심사 NOT_RUN. WU canonical DAG **34/49 UNCHANGED**, scoped **18/20**, HH_R10 OFF, L4 false, production NOT_ISSUED. No activation or foreign repository change.

**최소 R25 판별 수행 조건:** original cross-section capture-grid numeric source 또는 state channel energy list와 convention; 동일 입력으로 E_total−E_vj mapping과 k(15)/k(55) 재적분을 확인. 실패하면 `BLOCKED_SOURCE_NATIVE_ENERGY_GRID`로 남겨 새 physical-Q를 발급하지 않음.
