# WU088_HH R29 | GL2022 원전 rate의 HD 5준위 화학 흡수·복사 회전망

2026-10-30 KST. Parent immutable WU PR #167 HEAD `cd85b157fdfdf6be0bbe372ff5c282c20a4ca07e`. 연구 단위 `WU_R29_HD5_REVERSIBLE_COLLISION_ABSORBING_REACTION`. Canonical WU `34/49`, source-derived auxiliary `1/1_SCOPED`, canonical promotion `+0`. 원본 R28 SOURCE ZIP 및 내부 GL2022 PDF는 SHA-256 고정. R6/C9 다른 저자 심사 미실행, full-A/physical-Q/REC-CR owner 허가는 별개.

## 1. Source와 물리 범위

원본 GL2022, González-Lezana, Hily-Blant, Faure, JCP **157,214302 (2022)**, doi:10.1063/5.0128598. R26 원본 reactive Table 1–10의 `H+ + HD(v0,J) -> D+ + H2(v'0,J')` state-to-state SQM **계산된** 700셀, R28 original SI Tables 12–28의 `H+ + HD(v,J) -> H+ + HD(v',J')` 비반응성 **계산된** 1560셀 재사용. 원본 PDF 273554B SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. REC161 HEAD `5bf22a4258ba571e8aebb1cfedab9cafe7ac6481`의 Leiden 2021 Einstein A *전사표*와 REC162 HEAD `4d60f74db02d7435add062eaefb15739e68c4b55`의 CDMS Dec2011 v2 *공식 렌더 텍스트 전사표*로만 상태·복사 에너지 데이터를 묶는다. 전사표는 각각 원본 LAMDA `hd.dat` 2289B나 CDMS raw `.egy` byte identity를 새로 인증하지 않는다. REC163 1984 실측 회전선은 독립 *계산 모델* 검증이 아닌 단순 출처 일치 검사만 한다.

지정 원본 온도 `T = {55,105,255,505,1005,2005,3005} K`, 초기 HD `J=0..4`, 최종 반응 `H2(v'=0,J'=0..9)` **조건부 채널만**. T15에는 해당 reactive 인쇄 0이 있으며, T1505에는 HD J1 비반응 수치의 원본 의심 지수, T2505에는 reactive J3->H2 J'7의 원본 의심 지수가 있어 전체 5준위 체인을 수용하지 않는다. J5의 중복 인쇄 위험을 보호하기 위해 J5와 연결될 수 있는 J6 이상의 상태를 전이망에 포함하지 않는다. 각 허용 온도에서 5×10=50개의 reactive **positive** 소스 rate, J>i의 10개 downward **positive** 이력 rate. 원본 총 350 reactive source-rate cells와 70 inelastic downward cells 실제 이용. 대각/원본 의심 셀을 0으로 채우거나 원본에 없는 온도 보간을 하지 않는다.

## 2. 미시적 상세평형을 통한 상향 충돌의 구성

HD는 heteronuclear molecule이므로 회전 준위 통계중량의 J-의존 부분은 `g_J=2J+1` (상수 핵스핀 승수는 비율에서 소거). 분자 물리에서 source-downward collision rate를 `d_{j i}(T)=k_{j->i}(T)` (j>i)로 기록한다. 공통 thermal H+ bath, Maxwell 분포, 동일 PES와 충돌 입구·출구 내부 에너지 차이를 적용하는 *추가 가정* 아래

\[
 E_j=hc\widetilde E_j,\quad \pi_j(T)\propto (2j+1)e^{-E_j/(k_BT)},\quad
 k_{i\to j}^{\uparrow}=k_{j\to i}^{\downarrow}\frac{2j+1}{2i+1}e^{-(E_j-E_i)/(k_BT)}.
\]

이때 `\pi_j k_{j\to i}^{\downarrow}=\pi_i k_{i\to j}^{\uparrow}`가 정확히 성립한다. 상향 rate는 원본 GL2022 표에 새로 인쇄된 수치가 아니라, **source-derived conditional detailed-balance rate**다. REC162 에너지 출처 오차·연관 공분산이 알려지지 않아 현대 분광 정밀도 인증이 아니다.

## 3. 화학적 흡수 Markov 연산자

선택한 source policy `raw_SQM` 또는 `Eq6-7_spin_effective`에 따라 화학 생성물별 rate `q_{j a}`를 정의한다. 앞의 경우 원래 인쇄 `k_{ja}` 그대로, 뒤의 경우 H2 최종 J' 짝수/홀수에 각각 1/4, 3/4를 **한 번만** 곱한다. 두 정책의 차이는 uncertainty band가 아니다. `K_j=\sum_{a=0}^9 q_{ja}`. HD가 희박한 tracer이고 `n=n_{H+}` 및 T가 외부 공급으로 고정인 구획을 가정한다. 각 transient J→i 콜리전 rate는 `n k_{j i}`, 복사는 `A_j` 단일 J→J-1, 화학 반응 흡수율은 `n K_j`. 5×5 생성자 `G`는 column convention `\dot{x}=Gx`이며 아래 행렬 구조를 갖는다:

\[
 G_{ij}\ (i\ne j)=n k_{j\to i}^{\rm coll}+\delta_{i,j-1}A_j,\qquad
 G_{jj}=-nK_j-\sum_{i\ne j}n k_{j\to i}^{\rm coll}-\mathbf1_{j\ge1}A_j.
\]

모든 J의 K>0, n>0이라 `-G`는 nonsingular M-matrix, `(-G)^{-1}\ge0`, `\int_0^\infty e^{Gt}dt=(-G)^{-1}`. 초기 J=j의 점유시간 벡터 `m^{(j)}=(-G)^{-1}e_j`. 이에 따라

\[
 \mathbb E[t_{\rm ex}]=\mathbf1^Tm^{(j)},\quad
 P(\mathrm{H2},J'=a)=\sum_{i=0}^4 n q_{ia}m_i^{(j)},\quad
 \mathbb E[N_\gamma]=\sum_{i=1}^4 A_i m_i^{(j)}.
\]

또한 `1^T G=-(nK)^T`이므로 `\sum_a P(H2,J'=a)=1`은 **선택된 반응성 v'0 채널만 있는 폐쇄 흡수 모형 안에서** 수학적으로 필연적이다. 현실의 전체 H2 진동/ion bath 생성 확률이 1이라는 의미가 아니다. 첫 방출 이전에 복사를 absorbing event로 바꾼 `G_γ`에서 `m_γ=(-G_γ)^{-1}e_j`를 얻어

\[
 P(N_\gamma\ge1\text{ before restricted exchange})=\sum_{i=1}^{4}A_i(m_\gamma)_i.
\]

이 양은 `P(최초 사건이 복사)` 및 평균 광자수와 서로 다르다. Coulomb/PES 에너지 영점, 이온화 offset, reverse reaction, heat/Q, full cosmological bath의 해석을 포함하지 않는다.

## 4. 실제 계산과 물리적 의미

7 source temperatures × 2 서로 다른 반응률 정책 × `n/ncrit_J2∈{0.1,1,10}` × 5개 초기 J = **210** 조건부 first-passage 사례. 각 사례에서 10개 H2 J' 분기 확률 총 **2100** 결과 셀. 밀도 기준 `ncrit_J2=A_{2→1}/K_2`는 **각 source policy의 계산된 척도**이며 관측된 우주 밀도가 아니다. 원본 350개 반응률, 70개 비반응률, REC161 A 및 REC162 인쇄 회전 에너지 조합이 결과의 실제 물리적 입력이다.

105 K, J2, n=ncrit, `Eq6-7_spin_effective`: `n=3954.418182... cm^-3`, 첫 사건이 바로 photon일 확률 `0.091265...`, 반응이 일어날 때까지 광자 1개 이상 방출할 확률 `0.473628517450...`, 평균 광자수 `0.888027556749...`, 제한적 교환 평균 대기시간 `173.6286 days`, 최종 H2(v'=0) 홀수 J' 비중 `0.592566851212...`. R28의 최초 사건 3경쟁 확률 `0.092926...`은 상향 충돌을 제거한 별도 모형이므로 양자간의 1:1 동일 사건 확률 비교가 아니다. 누적 광자 방출과 단일 최초 사건을 구분한 것이 과학적 차이.

REC163 source-pinned 1984 lab `HD v0 J4→3` R(3) wavenumber `350.852 ±0.002 cm^-1`와 REC162 CDMS2011 v2 nominal `E4-E3=350.852958 cm^-1` 간 차이 `+0.000958 cm^-1`, 제공된 1984 숫자 ± 범위 내부. 두 원천이 측정 계보를 공유할 수 있어 독립 통계 검증이나 모델 rate 정확도 증거가 아니다.

## 5. Claim Gate

SOURCE_ORIGINAL 2022 computed SQM and named printed line inputs established/literature-supported; upwards detailed balance, absorbing network, positivity, photon/prod observables **derived**, 210-run numeric outputs **numerically_checked**, implementation-tested; different-author independent R6/C9 **NOT_RUN**. Exact physical PES native `σ(E)`/threshold and Q remain NULL; molecular REC/CR owner ACK absent; HH_R10 OFF; full_A NULL; L4 false; production NOT_ISSUED. WU canonical DAG remains 34/49; R29 source-conditional physical-slice auxiliary 1/1, not a new canonical admission.

다음 물리 원천 우선순위: 동일 Velilla2008 H3+ PES (`EPAPS E-JCPSA6-129-612834`)와 정규화된 충돌 에너지별 σ(E) 원본, 또는 EMAA 2023 H+ HD 171-transition/25-temperature 원시 파일 byte acquisition 후 현재 printed rate와 상태-label 및 온도 정합 검증. EMAA 반응 생성물 채널과 H+ induced HD nonreactive channel은 구분해야 한다. 전체 vibrational/up/down/charge-nuclear species owner 승인 전에는 production/final cosmic heating 금지.

## 6. 상세평형 상향 충돌의 직접적인 영향 (명시적 반사실적 대조)

`src/counterfactual.py`는 소스의 하향 충돌·화학 reaction·A 전이만 남기고 **상향 충돌을 의도적으로 제거한 비열적 반사실적 모형**을 별개로 계산한다. 이 모형은 thermal detailed balance를 충족하는 완전 네트워크가 아니다. `T=105 K`, `Eq6-7_spin_effective`, 초기 J2, n=ncrit에서 반응 전 광자 ≥1개 확률은 상향 포함 `0.473628517450...`, 상향 제거 `0.106826008176...`이다. 55 K에서는 각각 `0.755839559516...`와 `0.046087045532...`이다. 하나의 동역학에 서로 다른 최초사건 확률을 섞는 것이 아니라, 동일 소스에서 상향 전이 포함 여부라는 실제 closure 차이를 비교한 결과다. 낮은 온도에서 작은 상향 rate도 화학 소멸이 느린 상태에 여러 번 작용할 수 있어 방출 광자 누적률에 크게 기여한다. 이 결과는 미공개 H2(v'>0) 생성물, collisional H2/HD other partners, nonthermal populations를 제외한 선택 채널 모형에 한정된다.