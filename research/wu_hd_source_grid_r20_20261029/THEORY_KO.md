# WU088_HH R20: 원본 상태별 반응률의 비자율 정확 노출 연산자

2026-10-29. **근거 등급:** 원문 반응률은 literature-supported/source-byte-verified (R18); 수학적 정리는 derived, Wolfram 9/9 symbolic; 수치 구현은 R20 Python 25/25 및 독립 알고리즘 160/160으로 확인. **실제 REC/CR 화학상태 소비자 승인:** unresolved.

## 1. 정의·물리 범위

원문: González-Lezana, Hily-Blant & Faure, *J. Chem. Phys.* **157**, 214302 (2022), DOI [10.1063/5.0128598](https://doi.org/10.1063/5.0128598), [DIGITAL.CSIC 보충자료](https://digital.csic.es/bitstream/10261/305186/2/h_hd_rate_supplementary_material.pdf). 원본 PDF 273,554 bytes, SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. 반응은 오직 `H+ + HD(v=0,j=2) -> D+ + H2(v'=0,j'=1)`의 **SQM reactive** 채널. 10개 온도점 `15,55,105,255,505,1005,1505,2005,2505,3005 K`만 허용한다. 예를 들어 105 K는 `1.15(10)` 즉 `1.15×10^-16 m³/s`, 255 K는 `2.74×10^-16 m³/s`. 원문 인쇄 nominal 값이지 참값의 인증 구간은 아니다. 최종 홀수 준위 3/4와 초기 HD 열분포를 상태별 raw rate에 재적용하지 않는다.

가정: 공간적으로 균질한 한 셀, 4종 수밀도 `n=(H+,HD02,D+,H201)`, 한 방향 mass-action, 다른 채널과 역반응 0인 **선택적 closure**, 외부 등온 bath가 각 구간의 원문 격자온도를 유지, 외부에서 주어진 양의 부피비 `v(t)=V(t)/V(0)>0`, proper time `t` [s], 반응률 `k(T)` [m³/s], 수밀도 [m^-3]. `θ=d ln v/dt` [s^-1]. 실제 우주론적 T(t), Q-event, 광자/전자/상태 간 전이, full-A는 계산하지 않는다.

## 2. 정리 A: 정확한 비자율 scalar exposure

화학양론 `ν=(-1,-1,+1,+1)^T`와 질량작용 법칙은

`dn/dt + θ(t)n = ν k[T(t)] n_H+ n_HD`.

Comoving 수밀도 `N(t)=v(t)n(t)`는

`dN/dt = [k(T(t))/v(t)] F(N), F(N)=ν N_H+ N_HD`.

양의 measurable `v`와 원문 격자에서만 값을 갖는 외부 지정 `T(t)`에 대해

`A(t)=∫_0^t k[T(s)]/v(s) ds` [m³], `A(0)=0`.

그러면 `dN/dA=F(N)`이고, 시간별 벡터장 `α(t)F`의 Lie bracket은 `[α(t)F,α(s)F]=0`이다. α는 상태에 의존하지 않기 때문이다. 따라서 time-ordered evolution은 **하나의** 정확한 반응 flow `Φ_{A(t)}`로 환원되며, `Φ_{A1}∘Φ_{A2}=Φ_{A1+A2}`이다. 이것은 **단일 채널·외부 배경**에만 성립한다. 다른 화학반응이나 T(n) 피드백을 추가하면 일반적으로 commutator가 0이 아니다.

초기 반응물 `a=N_H+(0)`, `b=N_HD(0)`, `m=min(a,b)`, `M=max(a,b)`, `δ=M-m`라 하자. extent `ξ`는

`dξ/dA=(a-ξ)(b-ξ)`, `ξ(0)=0`.

`δ>0`이면

`ξ(A)=m M [1-exp(-δ A)]/[δ+m(1-exp(-δ A))]`.

`δ=0`이면 `ξ(A)=a² A/(1+a A)`. 잔존 반응물 `N_H+=a-ξ`, `N_HD=b-ξ`; 생성물 `N_D+=N_D+(0)+ξ`, `N_H2=N_H2(0)+ξ`. 물리 수밀도는 `n=N/v(t)`이다. `0≤ξ≤m`이므로 양성성·생성물 단조증가가 성립한다. 단조증가는 **comoving 생성물**에 대한 것으로, 팽창 시 물리 생성물 수밀도는 감소할 수도 있다.

H 핵수 `h=(1,1,0,2)`, D 핵수 `d=(0,1,1,0)`, 양전하 `q=(1,0,1,0)`는 `h·ν=d·ν=q·ν=0`을 만족한다. 따라서 `h·N,d·N,q·N`은 보존되고, `h·n,d·n,q·n`은 `1/v`로 희석된다. 실제 전자와 중성 원자·역반응이 없는 모델이므로 **전체 물리계의 charge neutrality**를 보장한다는 주장이 아니다.

## 3. 정리 B: 구간별 정확 노출과 미분

구간 i에서 온도 `T_i`는 원문 격자점, `θ_i`는 외부 고정, 시작 부피비 `v_i`, 구간 길이 `Δt_i>0`라고 하자.

`I_i=∫_0^{Δt_i} ds/[v_i exp(θ_i s)] = (Δt_i/v_i) φ(θ_i Δt_i)`,

`φ(z)=(1-exp(-z))/z`, `φ(0)=1`; `v_{i+1}=v_i exp(θ_i Δt_i)`.

따라서 `A=Σ_i k(T_i) I_i`가 정확하다. `expm1`은 `z→0`에서 소거오차를 줄인다. `I_i>0`이고 원문 `k(T_i)>0`이므로 `A≥0`. 고정된 외부 부피와 구간 분할에서

`∂ξ/∂k_i = I_i (a-ξ)(b-ξ)≥0`.

이 식은 **명목 rate에 대한 조건부 민감도**이지, 출판물에 없는 물리적 rate 불확실성으로부터 도출한 오차막대가 아니다. 서로 다른 T_i의 순서를 바꿀 때 `I_i`가 바뀔 수 있으므로 부피 변화를 포함한 임의 permutation invariance는 주장하지 않는다. `v=1`이면 같은 구간들의 순서 교환은 총 A를 보존한다.

## 4. 실제 CR clock의 읽기 전용 연결 범위

CR PR #120 HEAD `5a8e4ac85a19151a3f9625c91d8e87b38f7a32e7`, 경로 `research/cr_c15_duhamel_20261015/src/continuous_source.py`, blob `b60f3ef6487b340ecb519f9dd77445caf2975833`의 `proper_dt(model,a0,a1,q)`는 `model.hubble(a,q)`에 대한 `d ln a/H`를 2점 Gauss–Legendre로 적분한다. R20의 `cr_gl2_formula`는 **동일 수식의 독립 재현**이고, 원본 owner 함수를 직접 호출하거나 owner의 실제 model/state를 바인딩하지 않는다.

`H(a,q)=d ln a/dt>0`이고 `v(a)>0`가 외부에서 제공되면, 고정 source-grid T에 대한 올바른 반응 노출은

`A = k(T) ∫_{ln a0}^{ln a1} dx/[H(e^x,q) v(e^x)]`.

이것은 `k(T) Δt/v(a_mid)`와 일반적으로 다르다. 검산용 **합성** `H=2×10^-18 s^-1`, `a0=0.1`, `a1=0.2`, `v=(a/a0)^3`에서는

`A_exact = k(T)/(3H) [1-(a0/a1)^3]`.

원본 2점 시간 적분식과 달리 부피가중 노출에는 별도 quadrature가 필요하다. Gauss–Legendre 2점 노출 오차 `0.00379545` 상대, 8점 오차 `~1.06×10^-15`는 이 **특정 매끄러운 합성 모델의 관찰값**이며 일반 오차인증이 아니다. H(a,q),v(a)의 node-level positivity 검사만 수행하며 whole-domain positivity 증명은 없다.

REC PR #155의 `HDDataset.downward_rate(collider_id,upper,lower,T)`는 LAMDA HD의 **비반응성** 충돌·분광 (50/100/200 K, p/o H2 collider)이고 이 SQM reactive 105 K rate 소비자가 아니다. CR의 `species_resolved_affine`는 H/He photon photoevents를 다루므로 HD 4종 chemistry owner가 아니다. 이들은 **명명된 경계/clock 후보**이지만 physical owner admission은 없다.

## 5. 구현·검증·결론

`src/grid_exposure.py`는 R18 원본 PDF에서 발급된 `NativeGrid`만 받아, source temperature 10점 외의 입력을 거절한다. 출력은 원본 rate의 Fraction numerator/denominator, 4종 수밀도, A, v, 구간별 I와 source SHA를 포함한다. source label은 검증된 solver issuance만 발급한다. CLI는 create-only다.

R20 Python 25/25 PASS; 80자리 별도 survivor-ratio 알고리즘 160/160 PASS (max abs density `5.960464477539063e-08 m^-3`, max relative floor-1 `3.051806267813985e-14`); SciPy DOP853 2/8/24/48 구간 4개 PASS (max abs `4.307366907596588e-09 m^-3`); Wolfram symbolic 9/9 True. **비저자 독립 R6/C9는 NOT_RUN**. Synthetic source-grid 105→255 K, 각 5e9 s, v=1, 초기 H+=HD=1e6 m^-3, 생성물0에서 A=`1.945e-6 m³`, 최종 반응물 `339558.5738539898 m^-3`, 생성물 `660441.4261460102 m^-3`.

같은 source-parsing-excluded 로컬 Python timing에서 exact-flow / DOP853 시간비는 2,8,24,48 구간에서 약 139, 203, 219, 215배(최신 재검산; 정확한 값은 `results/NUMERICAL_BENCHMARK.json` 참조)다. 비교 IVP 허용오차는 `rtol=2e-12`, `atol=1e-7 m^-3`, 실제 최대 오차는 `4.31e-9 m^-3`. **이는 한 채널의 조건부 모델 최적화이지 production solver 성능 향상이 아니다.**

WU canonical DAG는 **34/49 불변**. 이번 R20 보조 연구 결과는 재사용 가능하지만 실제 REC/CR 4종 state-density-clock-energy owner ACK, full-A, 원본 rate uncertainty, Q-event, 역반응은 미결이다. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`.
