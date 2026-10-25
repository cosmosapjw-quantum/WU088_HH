# PHYS90 — 표시 정밀도 셀과 공통 소비자 공분산 경계

## 범위와 새 질문

선택 부모는 `NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT`다. PHYS89의 원 표시 F 반례, 원 MF33 decode/eigh, 소비자 측도·clock·normalization 유도를 재사용한다. 이번 유한 자식 `COVARIANCE_FORMATTING_CELL_AND_MATCHED_CONSUMER_ENVELOPE`는 원 평가의 추가 입력을 정량화한다. 원본 정밀도 C의 현재 nominal 결속, nuclear mass/state/kernel/tail 및 named consumer ACK는 별도 미충족 부모 의무다.

F는 PHYS89 SOURCE_TABLE의 정확한 십진 대칭153×153행렬, H는 TOKEN_ROUNDING의 양의 halfULP를 같은 upper-triangle 순서로 대칭 배치한 행렬이다. t≥0에 대해
B_t={F+Δ: Δ=Δ^T, |Δ_ij|≤t H_ij}.
이는 닫힌 성분별 오차 셀이다. t=1을 nearest-formatting과 연결하는 것은 **조건부 모델**이며 evaluator의 실제 formatter 보증이나 물리적 오차 추정이 아니다. 닫힌 끝점은 실제 tie rule을 모를 때의 외포함이다. 실제 stochastic covariance는 추가로 C⪰0 및 source/nominal provenance가 필요하다. F나 원 source bytes를 수정하지 않는다.

## 1. 대칭 원소를 공유하는 정확한 support

u,v∈R^n을 고정하면
u^T Δ v = Σ_i u_i v_i Δ_ii + Σ_{i<j}(u_i v_j+u_j v_i)Δ_ij.
각 독립 upper entry를 계수의 부호에 따라 ±tH로 두어 양/음 극값을 모두 얻으므로
sup_{Δ∈B_t−F}|u^TΔv|
= t[Σ_i H_ii|u_i v_i|+Σ_{i<j}H_ij|u_i v_j+u_j v_i|] =: t s_H(u,v).
이는 전체 대칭 box에 대한 sharp bound다. B_t∩PSD에는 유효한 outer bound이며 그 부분집합에서 항상 sharp하다고 주장하지 않는다. 서로 다른 (u,v)의 극값이 하나의 Δ에서 동시에 실현된다고 해석하지 않는다.

대칭 Y에 대해 support는
h_H(Y)=Σ_i H_ii|Y_ii|+2Σ_{i<j}H_ij|Y_ij|,
sup tr(YΔ)=t h_H(Y).
Y=ww^T이면 h_H(Y)=Σ_ij H_ij|w_i w_j|이다.

## 2. PSD 분리와 정확한 2×2 조건

C⪰0이면 모든 w에 대해 w^TCw≥0. 따라서
w^TFw+t h_H(ww^T)<0
이면 B_t에 PSD 원소가 없다. 보다 일반적으로 Y⪰0이며
tr(YF)+t h_H(Y)<0
이면 같은 결론이다. 이것은 주어진 셀에 대한 유한 인증 규칙이며 원 evaluator 전체에 관한 strong no-go가 아니다.

두 index i,j에 대하여
a=F_ii+tH_ii, b=F_jj+tH_jj,
c=max(|F_ij|−tH_ij,0).
해당 2×2 interval block이 PSD 원소를 갖는 필요충분조건은
a≥0, b≥0, c²≤ab.
필요성: PSD 대각은 비음수이며 actual diagonals≤a,b, |off|≥c이다.
충분성: 대각을 a,b로, off를 주어진 구간에서 0에 가장 가까운 값으로 택하면 두 principal diagonals와 determinant가 비음수다. 이는 해당 block의 존재 증명이며 전체 F의 수정본을 채택하는 절차가 아니다.

모든 singleton과 모든 pair의 이 조건을 만족하는 t 집합은 nested box로 인해 상향 폐집합이다. t_pair는 그 infimum. 실행에서는 t=0,1과 doubling1,2,…,4096 안에서 exact feasibility를 검사하고, bracket을 얻으면40회 dyadic bisection한다. 기록 lo는 실패(특정 pair certificate 포함), hi는 모든 pair 통과이며 폭은 initial_width/2^40이다. t_pair∈(lo,hi]; full PSD에 필요한 t_PSD≥t_pair이므로 lo만 그 하계로 쓴다. hi는 full PSD 상계가 아니다. 최대4096에서도 pair 실패면 실제 실패 witness와 lower-bound-only를 반환한다.

F의 diagonal이 음수인 일반 입력은 singleton 검사를 포함한다. H≥0, finite entries, square/symmetry, t≥0, vector dimensions가 계약 조건이다. t=0의 pair 통과 시 bracket [0,0]를 반환한다. 양의 H가 없는 불가능한 pair를 임의 epsilon으로 통과시키지 않는다.

### 이미 알고 있는 0,10 block에서 새로 유도하는 radius 식

기존 a=0.0004278572, d=10^-10, H_00=H_0,10=H_10,10=d/2를 그대로 쓰면 off가 양인 branch에서 최대 determinant는
(a+td/2)(a−d+td/2)−(a−td/2)^2
=−ad+t(d/2)(4a−d).
따라서 그 block의 최소 radius는 t*=2a/(4a−d), a>d>0. 원 t=0 반례를 다시 계산하지 않고 이 새로운 허용정밀도 조건을 도출한다. Wolfram은 이 새 identity와 fixture algebra만 한 번 검산한다.

## 3. pair 검사와 전역 PSD의 구별

Manufactured n=3 example: F_ii=1,F_ij=−1(i≠j), H_ij=1/10,t=1.
모든 pair에서 upper diagonal11/10, minimum |off|9/10이므로 pair 조건을 통과한다.
w=(1,1,1)에는 w^TFw=−3, h_H(ww^T)=9/10이어서 모든 C∈B_1에서 w^TCw≤−21/10.
이는 pair 통과로 전역 존재를 결론내리는 구현을 거부하는 exact fixture다. 실제153차원 자료의 전역 호환성은 해당 실제 certificate가 없는 동안 UNRESOLVED다.

전역 후속 의무는 PSD Gram primal certificate(C=GG^T가 모든 셀에 속함) 또는 exact PSD dual Y의 분리 certificate로 특정한다. 이번 실행은 SDP나 새 eigensolve를 호출하지 않는다.

## 4. 같은 source를 소비하는 공통 모멘트

PHYS89의 고정 선형 consumer map L 및 normalized first-order B를 재사용한다.
K(C)=L C L^T.
각 K_ab의 중심은 L_a F L_b^T, box radius는 t s_H(L_a,L_b).
아래의 q는 합산할 양의 단위가 일치하도록 정해진 계수다. q^T L=0이면
q^T K(C) q=(q^TL)C(L^Tq)=0,
또한 K(C)q=0.
이 보존은 모든 공통 C에서 exact이다. 각 소비자의 별도 covariance/noise를 독립으로 취급하면 이 관계를 일반적으로 잃는다.

고정 r,a,Z,M에서 normalized response의 B=(a−Mr)/Z와 exact-ratio remainder는 PHYS89에서 재사용한다. 이번 셀 envelope를 B C B^T에 적용할 수 있다. 실제 r,a는 아직 nuclear supplier로부터 공급되지 않았으므로 실제 rate CI, thermal/xe history bound를 발행하지 않는다.

### Sharpness·상관관계 fixture

F=4I_2,H=ones_2,t=1의 전체 box는 diagonal≥3, |off|≤1로 SPD다.
u=(1,1),v=(1,−1)이면 u^TΔv=Δ_11−Δ_22, sharp radius2.
절댓값을 먼저 취한 |u|^T H|v|=4는 유효하지만 덜 날카롭다.
각 variance의 최대12는 별도로 달성되지만 두 variance 합의 최대는20이므로 (12,12)는 공동으로 불가능하다.
L의 세 행을 u,v,−u−v로 두면 q=(1,1,1)에 대해 q^TL=0.
2×2 upper entry의8개 vertex를 exact 열거해 support, 동시제약, common-source conservation을 검증한다. 이는 명시된 manufactured fixture이며 actual thermal/fast/radiation owner 승인이 아니다.

## 5. 구현과 판정 연결

- actual SOURCE_TABLE/TOKEN_ROUNDING은 SHA로 결속한 기존 결과를 읽는다. ENDF decode, 원 eig, PHYS89 witness execution, rate/integral/ODE는0.
- 모든11628pair(singleton별도153; independent upper entries11781)와 exact radius brackets를 새 primary1회에서 계산한다. independent reference는 production kernel을 import하지 않고 별도의 Decimal/exact 계산으로 t=1과 최종bracket, 선택 witness 및 모든 fixture를 대조한다.
- complete finite child와 PARTIAL parent를 분리한다. production NOT_ISSUED, HH_R10 OFF.
