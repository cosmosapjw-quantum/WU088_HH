# R9: 인과적 시간 셀의 양의 결합 오차 폐쇄

## 1. 결과와 근거

같은 명목 Markov 계열·상태 순서·시계·잔차 l1 norm에 대한 R8의 인증 커널과 비교 계수를 사용한다. 각 시간 셀의 실제 오차 supremum이 만족하는 두 부등식을 양의 2×2 역행렬로 풀면, 선행 전체 궤도 envelope 없이 첫 셀부터 한 번의 인과적 sweep으로 유한 구간 상계를 구성할 수 있다. 추가 인증 상계가 있으면 같은 닫힌 셀 또는 같은 정확한 시각에서 교차한다.

새 기여 범위는 이 특정 잔차/집계 비교의 셀 폐쇄, signed-d 식, exact outward 구현과 저장 입력에서의 실제 대조다. 양의 선형계 소거, Volterra 비교, interval intersection 자체는 기존 수학 원리다. 현재 문서는 직접 유도이며 수치·구현 채택은 실행 기록 및 독립 C9에 따로 결속한다.

## 2. 전제와 convention

유한 T=Nδ, δ>0에 대해 R,E는 [0,T]에서 비음수 연속이고 유계다. R7/R8의 정칙성·해 존재·불변량·whole-domain coefficient 조건을 재사용한다. a,b,c,g_r,g_e≥0, d∈R는 구간 전체의 유효한 비교 계수이며 R0≥R(0), E0≥E(0)다. 실제 nominal propagator는 동일 clock/state/family의 zero-sum l1 공간에서 비팽창이고, 저장된 uniform-all-starts 수축 인증의 조합이
\[
\| \Phi(t,s)z\|_1\le h_{\lfloor (t-s)/\delta\rfloor}\|z\|_1,\qquad
1=h_0\ge h_1\ge\cdots\ge h_N\ge0
\tag{R9.1}
\]
을 준다. 어떤 구간의 kernel certificate를 다른 generator family나 clock에 이식하지 않는다.

R8의 Duhamel 및 scalar comparison은
\[
R(t)\le h_{\lfloor t/\delta\rfloor}R_0+
 \int_0^t h_{\lfloor (t-s)/\delta\rfloor}
       [aR(s)+bE(s)+g_r]\,ds,
\tag{R9.2}
\]
\[
E(t)\le e^{dt}E_0+
 \int_0^t e^{d(t-s)}[cR(s)+g_e]\,ds
\tag{R9.3}
\]
이다. 충분한 인증 상방값
\[
\bar e\ge e^{d\delta}>0,\qquad
\bar\phi\ge\int_0^\delta e^{du}\,du>0
\tag{R9.4}
\]
를 공급한다. d=0이면 적분은 δ다. 구현은 저장된 R8 rational 값을 그대로 읽으며 새 지수 평가나 기존 producer 실행을 하지 않는다. d≤0인 구현 domain은 추가로 \bar e≤1을 요구한다. 이는 현재 source 값이 만족하는 finite contract다.

시간과 밀도 좌표는 저장 사례의 명시적 무차원 좌표다. 물리 적용의 a,d는 time^{-1}, b,c는 선택 오차 좌표의 변환 단위를 포함하고 δb\barφc는 무차원이다. 관련 물리 단위 변환에서 c, ħ, k_B를 보존한다. metric (-,+,+,+)는 이 유한 반응 비교식의 직접 의존성이 아니다.

## 3. 실제 현재 셀 supremum의 부등식

I_n=[nδ,(n+1)δ]에서
\[
r_n=\sup_{I_n}R,\qquad q_n=\sup_{I_n}E
\]
라 하자. 이전 셀 j<n에 이미 U_{R,j}≥sup R, U_{E,j}≥sup E를 구성했다고 가정하고
\[
F_j=aU_{R,j}+bU_{E,j}+g_r,\qquad
L_j=cU_{R,j}+g_e
\tag{R9.5}
\]
로 둔다. 이 유한 supremum은 compact 구간의 연속성에 의해 존재한다.

과거 셀에서 t-s≥(n-j-1)δ이므로 R 적분의 상계는 δh_{n-j-1}F_j다. 현재 셀 forcing의 전파는 h0=1로만 묶는다. 따라서
\[
A_n=h_nR_0+\delta\sum_{j<n}h_{n-j-1}F_j+\delta g_r,
\qquad
r_n\le A_n+\delta a r_n+\delta b q_n.
\tag{R9.6}
\]
fresh forcing에 전체 block contraction을 곱하지 않는다.

완료된 과거 셀의 coarse 적분은 정확히
\[
\int_{j\delta}^{(j+1)\delta}e^{d(t-s)}ds
=e^{d(t-(j+1)\delta)}\int_0^\delta e^{du}du .
\]
d≤0이면 t=nδ, d>0이면 t=(n+1)δ에서 과거 항과 초기 항의 셀 최대가 생긴다. 현재 셀의 부분 적분은 항상 길이δ의 적분 이하이다. 그러므로
\[
B_n=
\begin{cases}
\bar e^n E_0+\bar\phi\sum_{j<n}\bar e^{n-j-1}L_j+\bar\phi g_e,&d\le0,\\
\bar e^{n+1} E_0+\bar\phi\sum_{j<n}\bar e^{n-j}L_j+\bar\phi g_e,&d>0,
\end{cases}
\tag{R9.7}
\]
\[
q_n\le B_n+\bar\phi c r_n.
\tag{R9.8}
\]
d의 음수 damping을 절댓값으로 치환하지 않는다.

## 4. 셀 폐쇄 정리와 증명

\[
D=1-\delta a-\delta b\,\bar\phi c>0
\tag{R9.9}
\]
라고 하자. 그러면
\[
U^*_{R,n}=\frac{A_n+\delta b B_n}{D},\qquad
U^*_{E,n}=B_n+\bar\phi c\,U^*_{R,n}
\tag{R9.10}
\]
는 I_n 전체에서 유효한 상계다.

증명: (R9.8)을 (R9.6)에 대입하면
Dr_n≤A_n+δbB_n이다. D>0으로 나누고 다시 (R9.8)에 대입하면 결론이다. 같은 식은
\[
\begin{pmatrix}1-\delta a&-\delta b\\-\bar\phi c&1\end{pmatrix}^{-1}
=\frac1D
\begin{pmatrix}1&\delta b\\\bar\phi c&1-\delta a\end{pmatrix}\ge0
\tag{R9.11}
\]
로도 확인된다. D>0은 1-δa>δb\barφc≥0을 함의한다. n=0에서는 과거 합이 비어 있고 유한한 R0,E0,g만 사용한다. 각 완료 셀의 양의 forcing 상계를 다음 셀에 쓰는 귀납으로 n=0..N-1이 모두 닫힌다. 초기 전체-horizon envelope는 이 raw 구성의 전제가 아니다. □

D≤0이면 이 소거법의 충분조건을 만족하지 않는다. 현재 셀 크기/계수로 이 API가 거부하는 사유이며, 실제 반응계 발산 또는 물리 불가능성을 뜻하지 않는다.

## 5. 인증 상계 교차와 endpoint

같은 닫힌 셀의 독립적으로 인증된 C^w_n이 있으면
\[
U_n=\min(U^*_n,C^w_n)
\tag{R9.12}
\]
를 성분별로 취한다. 둘 다 실제 supremum을 덮으므로 최소도 덮는다. 이후 F_n,L_n은 이 U_n으로 계산한다. 이 방식은 capped 결과가 그 source whole cap보다 커지지 않는다는 정확한 보장을 준다.

오른쪽 끝점의 별도 Duhamel bound는
\[
V_{R,n+1}=h_{n+1}R_0+
 \delta\sum_{j=0}^{n}h_{n-j}F_j,
\tag{R9.13}
\]
\[
V_{E,n+1}=\bar e^{n+1}E_0+
 \bar\phi\sum_{j=0}^{n}\bar e^{n-j}L_j .
\tag{R9.14}
\]
I_n은 닫힌 셀이므로 U_n도 오른쪽 endpoint를 덮는다. 같은 정확한 clock의 인증 C^p_{n+1}가 있으면
\[
W_{n+1}=\min(V_{n+1},U_n,C^p_{n+1})
\tag{R9.15}
\]
로 선택한다. cap이 없으면 해당 항을 생략한다. 초기 W0도 공급 초기 상계와 같은 시각의 cap만 교차한다.

저장된 실제 reference trajectory는 numerical observation이지 certificate가 아니므로 어느 min에도 넣지 않는다. 저장된 점 상계를 보간하여 whole-cell cap으로 만들지 않는다.

R8의 whole U²는 유효한 궤도 상계이지만 현재 이산 연산자의 supersolution이라는 전제가 없다. 따라서 모든 가능한 R8 U²에 대한 raw sweep의 일반적 우열은 주장하지 않는다. 실제 저장 사례의 raw 우열은 실행값으로 보고하고 capped의 no-worse는 (R9.12),(R9.15)로 보장한다.

## 6. 유리수 및 방향 반올림

입력은 exact rational로 해독한다. q≥0에
\[
\mathrm{up}_{128}(q)=2^{-128}\lceil2^{128}q\rceil
\tag{R9.16}
\]
를 정의한다. 지정된 scalar 거듭제곱 p_{k+1}=up(p_k\bar e), A_n,B_n, U_R, U_E, F_n,L_n,V 끝값에만 상방 반올림을 적용한다. 유한 합·곱은 Fraction으로 정확히 계산한 뒤 해당 scalar를 올린다.

D는 exact rational (R9.9)로 보존한다. 분모 상방 반올림은 몫의 상계 방향을 뒤집을 수 있어 허용하지 않는다. numerator와 과거 forcing이 각각 유효한 상방값이고 1/D>0이므로 실제 연속 supremum에 대한 방향이 유지된다. U_E는 이미 올린 U_R을 사용한다. 인증 최소값은 정확한 유리수 min으로 취하고 다시 올리지 않는다.

상방 반올림된 벡터는 원래 실제 궤도 상계지만, 그것 자체가 discrete supersolution인지는 다른 조건이다. 여기서는 그 성질을 증명에 쓰지 않는다.

범위는 1..192 cells,128bits,8192-bit exact scalar 입력이다. 실제 source case 수는4HD+5controls이며 모든 허용 입력을 시험했다는 주장은 없다. generic API는 family/grid/provenance의 형식 일치를 검사하고, 실제 kernel/factor/cap 부등식은 호출자의 source-qualified 전제다. 고정 runner는 source SHA와 실제 JSON pointer로 이 전제를 결속한다.

## 7. 독립 수치 검증의 오류 예산

독립 reference는 같은 저장 유리수 h,\bar e,\barφ를 Decimal100으로 읽고 E를 먼저 푸는 Gaussian 소거를 사용한다. 생산 함수를 import하지 않는다. 고정된 exact upper factor와 정확한 exponential의 차이를 동일하다고 가정하지 않는다.

ε=2^-128, 정확한 비반올림 recurrence 값과 생산 recurrence의 차이를 Δ로 쓰면
\[
\Delta p_{n+1}\le\bar e\Delta p_n+\epsilon,\qquad
\Delta A_n\le\delta\sum_{j<n}h_{n-j-1}\Delta F_j+\epsilon,
\]
\[
\Delta B_n\le \Delta p_kE_0+
 \bar\phi\sum_{j<n}[(p_m+\Delta p_m)\Delta L_j+\Delta p_m L_j]+\epsilon,
\]
\[
\Delta R_n\le(\Delta A_n+\delta b\Delta B_n)/D+\epsilon,\quad
\Delta E_n\le\Delta B_n+\bar\phi c\Delta R_n+\epsilon,
\]
\[
\Delta F_n\le a\Delta R_n+b\Delta E_n+\epsilon,\quad
\Delta L_n\le c\Delta R_n+\epsilon.
\tag{R9.17}
\]
k,m는 (R9.7)의 부호별 지수다. min은 성분별 단조이고1-Lipschitz이므로 같은 exact cap과의 교차에도 안전하다. 두 오차 있는 branch의 min에는 두 branch 예산의 maximum을 사용한다. Decimal 계산에는 별도 scale×10^-80 guard를 둔다. 이는 실행되는 고정 사례의 수치 대조 기준이며 일반 실수 정리를 대체하지 않는다.

R7의193시각 binary64 궤적은 재적분 없이 보조 containment로만 읽는다. atol2e-12+rtol2e-10의 의미를 유지하며 연속 궤도 enclosure로 승격하지 않는다.

## 8. 물리 연결, 문헌과 채택 범위

기존 HD invariant-compatible 사례에서 E=|eta|이고 전체 coarse l1은4E다. 저장된 native9의 excitation generator는 동일 source graph를 사용하지만 reaction coefficient/밀도는 명시적 조건부 control이다. v=UNSPECIFIED, 누락 채널 MISSING_NOT_ZERO를 유지한다. 실제 GL2022 reactive state array와 명명된 물리 consumer/density/clock는 별도 입력 의무다.

Mitrophanov2005의 contraction convolution, Michel–Siegle2024의 CTMC initial-error/defect bound, Yazdani–Hadizadeh2012의 piecewise enclosure와 interval intersection은 원전 비교로 기록한다. Hilder–vanMeurs–Sharma2026의 비평형 coarse-graining 결과는 contextual 비교이며 그 상수·가정을 여기로 전이하지 않는다. 정확한 읽기 범위와 DOI/URL은 authority/LITERATURE.json에 있다.

Strong no-go NG1–NG7의 적용 여부를 검토했고 새 배제 정리를 제시하지 않는다. 독립 대입 증명, source-bound 구현, 실제 새 primary/reference와 CAS 결과를 각각 분리해 최종 채택한다.

