# C0A: corrected G7와 균일 3차 나머지

## 정의와 적용 범위

부호 (-,+,+,+), 정상 물질 congruence u=n, 고정 주축 또는 서로 가환하는 Bianchi-I shear history를 사용한다. σ의 단위는 시간^-1, S=∫σ dt는 차원 없는 실대칭 trace-free 행렬이다. 등방 FLRW 적색편이를 먼저 분리한다. e는 초기 tetrad에서의 단위 방향이며 평균은 초기 구면의 균일 확률측도 dΩ/(4π)다. 최종 관측자 하늘 측도, 방향별 source/opacity 가중, finite tilt, 일반 비가환 history에는 같은 식을 무검증 적용하지 않는다.

Δ(e)=log(E_final/E_initial after isotropic redshift)=½ log(eᵀ exp(-2S)e).
q=eᵀSe, r=eᵀS²e. R2N 원 correction notice에서 회수한 식은
Δ=-q+r-q²+O(||S||³),
<q>=0, <r>=Tr(S²)/3, <q²>=2 Tr(S²)/15,
따라서 <Δ>=Tr(S²)/5+O³, <Δ²>=2 Tr(S²)/15+O³다.

F(0)≠0, f=F/F(0), A=f'(0), B=f''(0)이 동일한 observable·frame·측도에서 정의되면
<f(Δ)>-1=(A/5+B/15)Tr(S²)+O³.
원 R1의 B/15만 쓰는 식은 선형화 Δ=-q에 대한 검사로는 맞지만 정확한 characteristic의 2차 평균을 모두 포함하지 않는다. 과거 자료는 수정하지 않고 적용 범위를 분리한다.

## 이번에 직접 유도한 유한 나머지 상계

s=||S||₂, 구현에서는 계산 가능한 sbar=max_i Σ_j|S_ij|≥s를 사용한다. 행렬이 실대칭이므로 이 상계가 유효하다. 아래 증명은 고유값의 존재만 쓰며 실제 고유값 수치 계산을 요구하지 않는다.

고유값 λ_i∈[-s,s], e의 고유축 성분 제곱 w_i≥0, Σw_i=1로 놓고
h(t)=½log[Σ_i w_i exp(-2tλ_i)] (0≤t≤1)라 하자.
p_i(t)=w_i exp(-2tλ_i)/Σ_j w_j exp(-2tλ_j)를 확률분포로 정의하면
h'(t)=-E_t[λ],
h''(t)=2 Var_t(λ),
h'''(t)=-4 E_t[(λ-E_t λ)³].

평균 μ가 [-s,s]에 속하고 분산은 s² 이하이다. 마지막 명제는 a≤X≤b일 때
E[(X-a)(b-X)]≥0에서 Var(X)≤(b-μ)(μ-a)≤(b-a)²/4를 얻고 a=-s,b=s를 넣으면 된다.
또한 |λ-μ|≤2s이므로
|E[(λ-μ)³]|≤E|λ-μ|³≤2s Var(λ)≤2s³.
따라서 |h'''|≤8s³, |h''|≤2s²다.

h(0)=0, h'(0)=-q, h''(0)=2(r-q²)이므로 Taylor 적분 나머지에 의해, 각 방향에서
|Δ+q-r+q²|≤(4/3)s³.                                      (1)
동일하게 1차 나머지는 |Δ+q|≤s²다. 고유값의 범위에서 |Δ|≤s 및 |q|≤s이므로
|Δ²-q²|=|(Δ+q)(Δ-q)|≤2s³.                               (2)
구면 평균을 취하면 (1),(2)의 같은 상계를 유지한다.

추가로 f가 [-sbar,sbar]에서 C³이고 |f'''|≤M3가 실제로 증명되어 있다면
|f(Δ)-1-AΔ-BΔ²/2|≤M3|Δ|³/6≤M3 sbar³/6.
세 나머지를 삼각부등식으로 합하면

|<f(Δ)>-1-(A/5+B/15)Tr(S²)|
≤ [4|A|/3+|B|+M3/6] sbar³.                              (3)

이 상계는 sharp하다고 주장하지 않는다. 허용된 M3 전제가 있으면 유한 sbar에서도 유효하지만, 큰 sbar에서 유용한 작은 오차를 보장하지 않는다. 실제 광이온화 반응의 M3, source-support/threshold가 만드는 비매끈성, 0에 가까운 F(0)은 아직 인증하지 않았다. M3 숫자를 함수에 넘기는 것 자체가 그 전제의 증명이 아니다. A,B의 계산 불확실성은 (3)에 포함되어 있지 않으며 별도 owner다.

## 정확 산술 및 소형 수치 검사

g7_reference.py는 int/Fraction만 받아 bool/float·잘못된 shape·비대칭·비영trace·과대 정수를 거절한다. 대칭 trace-free S의 moment와 response, 조건부 (3)을 exact Fraction으로 반환한다.

독립적인 degree-four 구면 cubature: 6축 각각 weight1/15, 8cube-corner 각각3/40. cube는 v_i v_j/3으로 계산하여 sqrt(3)을 도입하지 않는다. 이 규칙은 q,r,q²에만 사용하며 log/exp의 정확 적분법이라고 하지 않는다. 243개 비대각 STF 사례에서 tensor-contraction과 정확히 일치했다.

새 수치 fixture는 S=h diag(-1/2,-1/2,1), f(Δ)=exp(2Δ)다. 이 경우
<f>=Tr exp(-2S)/3=(2exp(h)+exp(-2h))/3,
second-order response=h²,
[f-average-1-h²]/h³ → -1/3.
0≤h≤1/100에서 |f'''|≤8exp(2h)≤8/(1-2h)≤400/49<9이므로 M3=9를 사용할 수 있다. h=1/100,1/200,1/400,1/800을 Decimal80으로 검사했다. 이 Decimal 실행은 구간 인증이 아니라 소형 수치 검산이며, 물리적 광이온화율·HH 적분을 수행하지 않았다.

## 소스 상태

원 correction notice는 Library file_00000000cde081fd9d63953b2ba3e999에서 실제 materialize했다. SHA/bytes는 SOURCE_LOCK.json에 있다. 여기서 쓴 새 기준 구현은 과거 R2N 구현 코드의 복원이 아니다. R2N의 실제 rate/G7 함수 몸체와 원 full receipt는 아직 회수되지 않았다. 원 보고서의 과거 PASS를 현재 환경의 재실행 PASS로 세지 않는다.
