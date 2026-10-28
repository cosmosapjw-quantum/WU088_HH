# R11 full-A uniform finite-block certificate와 forcing convolution

## 정리의 범위

CONTRACT.json과 PREMISES_AND_MAP_KO.md의 고정 K, pi, destruction d, 전체 가측 w family, 모든 시작시각, whole-domain forcing, 같은 state/clock/initial invariant 전제를 사용한다. 이 문서는 원래 HD residual과 coarse scalar 비교식을 R10에서 재사용하고, 새로운 full-A block certificate에서 정확한 셀 계산까지 연결한다. n>=2에서 증명하고, n=1의 zero-mass 공간은 {0}이므로 R0=g_r=0인 코드 convention으로 포함한다.

rho(T)=sup_{1^Tz=0,||z||1=1}||Tz||1. 열확률행렬에 대해

\[
\rho(T)=\frac12\max_{j,k}\sum_i|T_{ij}-T_{ik}|
=1-\min_{j,k}\sum_i\min(T_{ij},T_{ik}).
\]

첫 등식은 z의 양·음 부분을 같은 질량의 확률벡터로 분리하고 simplex extreme pairs를 취하면 얻는다. 두 번째는 두 확률벡터의 l1 거리와 공통 질량의 항등식이다. 따라서 rho는 convex, Z를 보존하는 합성에 대해 submultiplicative이며 stochastic T에 대해 rho<=1이다. 이 표준 수축계수는 Gaubert–Qu와 Mitrophanov의 선행 결과를 열 관례로 사용한다.

## 1. 전체 생성자와 ordered Duhamel

H=pi*d^T-diag(d)의 비대각은 pi_i d_j>=0이고, 열합은 d_j(sum pi_i-1)=0이다. 따라서 A_w(t)=K+w(t)H는 모든 허용 w에서 보존적 Metzler다. 유한차원 bounded measurable coefficient의 적분방정식으로 U_w(t,s)가 존재한다. 충분한 scalar shift 뒤 Peano–Baker 급수의 모든 항이 비음수이므로 U_w>=0이고, 1^T A=0으로 1^T U_w=1^T이다. 따라서 U_w는 column stochastic이고 l1 유도노름1, zero-mass 공간Z를 보존한다.

P(v)=exp(Kv)라 두면 거의 모든 u에서

\[
\frac{d}{du}\{U_w(t,u)P(u-s)\}
=-U_w(t,u)w(u)HP(u-s).
\]

양끝을 적분해 정확한 순서의 Duhamel 식을 얻는다.

\[
U_w(t,s)-P(t-s)
=\int_s^tU_w(t,u)w(u)HP(u-s)\,du.
\]

z∈Z에 적용하고 두 Markov propagator의 l1 nonexpansiveness를 사용하면

\[
\|U_w(s+\tau,s)z\|_1
\le\{\rho(P(\tau))+\tau M_w\|H\|_1\}\|z\|_1.
\]

원래 stochastic 상한1과 교차하여, 저장된 rho(P(tau))<=q_K에 대해

\[
\boxed{\rho(U_w(s+\tau,s))\le q_{\rm add}
=\min\{1,q_K+\tau M_w\|H\|_1\}.}
\]

이 증명은 시작시각 s나 특정 trajectory에 의존하지 않으므로 전체 가측 w family와 모든 s에서 uniform하다. Bound=1일 때 해당 식은 nonexpansiveness를 인증한다.

## 2. 양의 공통 성분으로 strict block 인증

각 H 열의 절대합은

\[
|-(1-\pi_j)d_j|+\sum_{i\ne j}\pi_i d_j
=2d_j(1-\pi_j).
\]

따라서 b_H=max_j d_j(1-pi_j)=||H||1/2이고 H+b_H I>=0이다. B_w(t)=A_w(t)+b_H w(t)I라 두면 B_w(t)>=K이다. 두 Metzler propagator의 variation-of-constants 비교는

\[
U_B(t,s)-P(t-s)
=\int_s^tU_B(t,u)[B_w(u)-K]P(u-s)\,du\ge0
\]

를 준다. Scalar shift는 모든 행렬과 commute하므로

\[
U_w(t,s)=e^{-b_H\int_s^t w(u)du}U_B(t,s)
\ge\alpha_w P(t-s),\quad
\alpha_w=e^{-b_H\int_s^t w}.
\]

0<=alpha<1이고 stochastic U,P가 U>=alpha P이면 Q=(U-alpha P)/(1-alpha)는 stochastic이다. 따라서 rho(U)<=alpha rho(P)+(1-alpha). alpha=1에서는 같은 열합과 U>=P가 U=P를 준다. 또한 alpha_w>=exp(-b_H M_w tau)이므로

\[
\boxed{\rho(U_w(s+\tau,s))
\le q_{\rm minor}=1-e^{-b_HM_w\tau}(1-q_K).}
\]

q_K<1, finite b_HM_wtau이면 q_minor<1이다. 임의의 reaction path를 허용하면서도 K의 finite mixing gap을 명시적으로 보존한다. 이는 nominal rho를 full A에 직접 이식한 것이 아니라 전체 propagator에 대한 새 비교식이다.

epsilon=b_H M_w tau에 대해 1-exp(-epsilon)<=epsilon이므로 q_minor<=q_K+epsilon(1-q_K)<=q_K+2epsilon이다. Additive 후보를 별도 결과로 보존하며 구현은 두 upper를 교차한다. 수치화는 exp(-epsilon)의 lower를 써 positive gap을 아래쪽으로 좁히고 q를 위로 반올림한다. 계산된 유리수 q가1이면 strictness=false를 반환한다. 수학적 strictness와 유한 정밀도에서 저장된 strictness를 구별한다.

## 3. 모든 시작시각에서의 block 합성과 Duhamel forcing

0<=q<=1이 모든 허용 시작시각에서 rho(U_w(s+tau,s))의 상계라 하자. t-s=N*tau+r, 0<=r<tau로 쓴다. N개 full blocks와 한 remainder에 대해 submultiplicativity와 stochastic nonexpansiveness를 적용하면

\[
\rho(U_w(t,s))\le h(t-s),\qquad
h(u)=q^{\lfloor u/\tau\rfloor},\quad h(0)=1.
\]

q=0에서도 q^0=1이다. 작은 u<tau의 fresh forcing에는 multiplier1이 필요하다. 실제 finite conservative CTMC의 exact q=0을 주장하지 않으며 q0은 numerical convolution API의 supplied-kernel control이다.

r'=A_w(t)r+f_r(t), 1^T r=1^T f_r=0, ||f_r||1<=g_r에서

\[
R(t)\le h(t-t_0)R_0+\int_{t_0}^t h(t-u)g_r(u)du.
\]

forcing multiplier의 인수는 age t-u다. 초기 residual의 나이를 모든 forcing에 공통으로 적용하지 않는다. 이 결론의 all-starts 의무는 forcing이 임의의 u에 들어오기 때문에 필요하다. Nominal K certificate가 저장 grid의 한 block에만 있고 homogeneous K인 사실이 없다면 이 연결은 별도 의무다. 현재 고정 K는 exp(K(t-s))이므로 저장 certificate가 모든 시작시각을 덮는다.

일반 가측 forcing에는 이 적분형 정리가 성립한다. 현재 구현은 정확한 균일 grid와 그 셀별 constant forcing을 대상으로 다음 유한식을 사용한다.

## 4. 정확한 aligned-grid convolution과 닫힌 셀

현재 저장 clock 원점 t0=0, t_n=n*Delta, tau=m*Delta이며 m은 양의 정수다. g_r(t)=g_j를 [jDelta,(j+1)Delta)에 둔다. h_n=q^floor(n/m)이면 끝점 t_n에서 한 source cell의 age가 [(n-1-j)Delta,(n-j)Delta]에 놓인다. 그 내부의 h값은 h_(n-1-j)이므로

\[
F_n=\Delta\sum_{j=0}^{n-1}h_{n-1-j}g_j,\qquad
R_n=h_nR_0+F_n.
\]

끝점 한 점의 값은 적분에 영향을 주지 않는다. 특히 n=1일 때 F1=Delta*g0이며 앞서 q를 곱하지 않는다.

셀 n에서 t=nDelta+u, 0<u<Delta라 하자. 각 과거 source cell의 적분은 두 인접 age bins 사이를 선형 이동한다. 따라서 forcing convolution은

\[
F(t)=F_n+\frac{u}{\Delta}(F_{n+1}-F_n).
\]

그 내부 initial kernel은 h_n이므로 R envelope는

\[
\mathcal R_n(u)=(1-u/\Delta)L_n+(u/\Delta)V_n,
\quad L_n=h_nR_0+F_n,\quad V_n=h_nR_0+F_{n+1}.
\]

오른쪽 endpoint의 actual envelope는 R_(n+1)=h_(n+1)R0+F_(n+1)<=V_n이다. 따라서 닫힌 셀의 supremum은 max(L_n,V_n)이며, outward 구현은 보고한 rounded R_(n+1)까지 max에 포함한다. 오른쪽 block 경계의 V_n은 셀 안에서 접근한 left limit이므로 반드시 포함한다. 셀 시작 직전의 old left limit은 해당 셀 밖이므로 포함할 필요가 없다.

## 5. signed scalar coupling의 정확한 E 적분

D+E<=cR+d_cE+g_e, c>=0에 scalar integrating factor를 적용한다. 같은 셀의 affine R envelope를 대입하면

\[
\mathcal E_{n+1}=e^{d_c\Delta}\mathcal E_n
+c(W_0L_n+W_1V_n)+\Phi g_{e,n},
\]

\[
W_0=\int_0^\Delta e^{d_c(\Delta-u)}(1-u/\Delta)du,\quad
W_1=\int_0^\Delta e^{d_c(\Delta-u)}u/\Delta\,du,\quad
\Phi=W_0+W_1.
\]

모든 weight는 d_c의 부호와 관계없이 양수다. x=d_c Delta>=0에서 지수급수와 비음수 적분을 교환하면

\[
W_0=\Delta\sum_{k=0}^\infty\frac{x^k}{k!(k+2)},\qquad
W_1=\Delta\sum_{k=0}^\infty\frac{x^k}{k!(k+1)(k+2)}.
\]

x<0에서는 exp(x)*exp(-x*u/Delta)를 전개한다. 두 양의 급수를 서로 교환한 뒤 exp(x)를 곱하면 같은 integral을 얻는다. x=0에서는 W0=W1=Delta/2, Phi=Delta이다. Reference는 독립적인 closed forms

\[
W_0=\Delta\frac{(x-1)e^x+1}{x^2},\qquad
W_1=\Delta\frac{e^x-1-x}{x^2}
\]

와 explicit x=0 branch를 Decimal160으로 사용한다. 1e-80 relative guard는 실행 전에 고정한다. Production은 이 뺄셈식을 사용하지 않으므로 nearzero cancellation이 생기지 않는다.

## 6. directed arithmetic의 enclosure

S=2^128이고 exact input x의 floor/ceil dyadic endpoints를 x_l,x_u로 만든다. 양의 exp항 recurrence는 term_l←floor(term_l*x_l/(S*k)), term_u←ceil(term_u*x_u/(S*k))이다. 귀납으로 각 exact term을 둘러싼다. Moment term에는 각각 k+2 또는 (k+1)(k+2)로 나누며 같은 directed rounding을 적용한다. 96차 이후 remainder는 0<=x_u<=16에서

\[
T_{96}\le\frac{x_u^{97}}{97!}\frac1{1-x_u/98}.
\]

추가 분모가1이상인 두 moment에도 이 exp tail이 상계다. exp(-x)의 enclosure는 exp(x)의 양의 reciprocal로 얻는다. 각 weight의 outer product, h powers, 양의 forcing sums 및 E recurrence를 동일한 directed rounding으로 수행하므로 선택된 exact rational q의 ideal comparison endpoints를 enclosing한다. 임의의 floating tolerance를 interval widening으로 쓰지 않는다.

하나의 ideal comparison의 lower는 actual R,E의 lower가 아니다. Actual R,E는 이 comparison의 upper에 의해 제한되며, raw lower의 의미는 ideal selected-q envelope에만 한정된다.

## 7. whole-cell E와 source-backed caps

닫힌 셀의 유효 R상계 R_*가 주어지면

\[
y(u)=e^{d_cu}E(a)+\Phi_{d_c}(u)(cR_*+g_{e,*})
\]

가 E(a+u)를 덮는다. y'(u)=exp(d_cu)[d_c E(a)+cR_*+g_e]이므로 미분 부호가 일정하다. 따라서 max(y(0),y(Delta))가 셀 전체의 상계다. 코드는 outer weights를 쓰고 reported outward E endpoint도 max에 포함한다. d_c<0라는 사실만으로 E endpoint가 whole maximum이라고 추정하지 않는다.

R10 point 또는 whole cap은 실제 source SHA, JSON pointer, family/state/clock, Delta, cells가 같은 경우의 해당 upper로 입력된다. 두 유효 upper의 min은 동일한 물리량의 upper다. Capped Rpoint와 Rwhole은 global block convolution과 R10의 해당 upper를 교차한다. Capped E는 이전 유효 Epoint와 capped Rwhole을 위 scalar 비교식에 넣고, raw E 및 R10 같은 point/whole cap과 교차한다. 양의 scalar flow는 초기값과 forcing에 대해 단조이므로 이 귀납은 안전하다.

끝점이 양옆 닫힌 셀에 속하므로 마지막 output-only 단계에서 adjacent whole upper와도 min을 취할 수 있다. 이때 전역 R age나 이전 forcing sum을 reset하지 않는다. Array metadata 검사는 scientific truth를 대신하지 않는다. 실제 runner는 pinned R10 bytes에서 cap을 읽고 독립 reviewer는 원래 인증 상태를 재사용한다.

## 8. 적용과 문헌 대비

세2state controls와 native9는 저장된 same-family coefficient와 initial state를 사용한다. Native9는 native K+synthetic conditional reaction fixture이고 실제 HD reactive array/physical consumer는 INPUT_PENDING이다. c,d_c,g_r,g_e는 R7의 whole invariant box에서 얻은 값을 바꾸지 않는다. 물리 HH_R10=OFF, production=NOT_ISSUED, L4=false, physical/centraldelta0.

Mitrophanov2005 Theorem2.1의 geometric-block forcing bound와 Theorem3.1의 ergodicity-coefficient perturbation bound를 원전에서 확인했다. 여기서는 전체 measurable w family에 대한 positive minorization과 exact source/grid/cap 결속을 직접 증명·구현한다. 일반 Duhamel, Dobrushin, block convolution의 새 우선권이나 sharpness는 주장하지 않는다. Strong no-go는 새로 제안하지 않는다.

독립 예비 유도: /root/independent_theory. 정식 HD/API 연결 및 positive Bernstein·directed-rounding·cap proof 통합: root. 별도 /root/dependency_delta의 R6/C9가 이 증명과 source/code/reference를 독립 심사한다. 수치 표본은 모든 w와 모든 시작시각의 이 해석적 증명을 대체하지 않는다.
