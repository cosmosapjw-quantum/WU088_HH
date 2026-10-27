# R7: 질량작용 반응의 상태 의존 형성항과 유한 블록 피드백 경계

## 1. 결과와 현재 근거 상태

유한한 양의 반응계에서 상태별 잔차와 집계 모형의 오차를 하나의 비음수 2성분 비교계로 묶는다. 반응률이 공유 반응물 밀도에 의존하여 fine/coarse 형성 총량이 달라도 아래 정리는 적용된다. 길이 H인 블록의 명목 생성자 수축률 rho는 초기 잔차에만 적용하고, 블록 도중 생성되는 반응 피드백은 생성 시점 이후의 전파로 적분한다. 그 결과

\[
w(t_n+H)\le T_n w(t_n)+q_n,\qquad
T_n=e^{B_nH}-(1-\rho_n)e_1e_1^T,\quad
q_n=\int_0^H e^{B_ns}g_n\,ds
\tag{R7.1}
\]

를 얻는다. 이 식은 singular B에도 정의되며 T와 q가 비음수다.

현재 상태는 **직접 유도 완료, 독립 심사 및 신규 실행 전**이다. 기존 R4의 물질 수 열과 R6의 명목 생성자 인증 근거를 재사용한다. 이 문서는 기존 native rate를 다시 평가하거나 물리 IVP를 실행하지 않았다. R7 작업 DAG는 작성 시점 13/30이며 이론/코드의 실제 채택 전에는 이 수를 올리지 않는다.

직접적인 연구 의무는 R6의 후속 계약에 이미 적혀 있다: formation이 상태 의존적이거나 coarse F가 다르면 prescribed common-F 정리 외에 결합/source-difference 경계가 필요하다. R4의 이분자 사건률은 반응물 밀도의 곱이므로 이 의무의 실제 수학적 연결 대상이다. 아래 HD 구성은 그 정수 방향과 공유 저장고를 사용한다.

## 2. 정의, 단위와 정칙성

시간 t는 선택한 동일 clock이다. 물리 적용에서는 proper seconds, 상태는 물리 밀도 cm^{-3}, 이분자 k는 cm^3 s^{-1}, K는 s^{-1}다. 합성 무차원 사례에는 별도 기준 밀도와 시간의 정의를 붙인다. 원 native graph의 tau=n_coll(10^{-11} cm^3 s^{-1})t와 물리 시간의 결속은 실제 collider density/history를 요구한다.

유한 n,m, 유한 사건 수 q를 고정하고 열벡터 관례로

\[
x'=K(t)x+S\,a(t,x),\quad x\in\mathbb R_{\ge0}^n,
\qquad S_{\cdot\ell}=\beta_\ell-\alpha_\ell
\tag{R7.2}
\]

를 둔다. 반응물/생성물 다중도 alpha,beta는 비음수 정수이고

\[
a_\ell(t,x)=k_\ell(t)\prod_i x_i^{\alpha_{i\ell}},\qquad k_\ell\ge0
\tag{R7.3}
\]

이다. 동일한 실제 사건의 TIQM/SQM 방법 대안을 서로 다른 동시 활성 사건으로 더하지 않는다. source에 이미 포함된 spin 가중을 다시 곱하지 않는다.

P는 시간에 무관한 m x n 집계 행렬이다. lift를 \(\mathcal E(t)\)로 쓰며

\[
P\mathcal E=I_m,\quad Q=I_n-\mathcal E P,\quad PK=0,
\quad y=Px,\quad r=x-\mathcal E y\in Z:=\ker P.
\tag{R7.4}
\]

P와 \(\mathcal E\)는 비음수이며 lift는 국소 절대연속이다. K는 명시된 명목 생성자로서 Z를 보존한다. 계수는 각 연구 블록에서 유계 가측이고 반응장과 필요한 Jacobian은 상태에 대해 국소 Lipschitz다. 모든 궤적과 아래 평균값 정리에 쓰는 선분을 포함하는 convex 비음수 box가 공급되어야 한다.

비교할 coarse 궤적은

\[
\bar y'=G(t,\bar y)+\delta(t),\qquad
G(t,y)=PSa(t,\mathcal E(t)y),\qquad e=y-\bar y.
\tag{R7.5}
\]

정확한 같은-source coarse 모형에는 delta=0이다. 수치 궤적을 기준으로 삼거나 별도 coarse source를 쓰면 delta의 실제 defect를 계산하여 경계에 포함한다. 임의의 미공급 delta를 0으로 채우지 않는다.

여기서 K(t)는 명시된 명목 연산자다. 공유 collider 때문에 실제 K가 상태에 의존한다면 그 차이를 잔여 반응장에 포함하여 Jacobian 경계를 더하거나, 해당 전체 계열에 대한 전파 경계를 새로 결속해야 한다. 고정 K 증명에 상태 의존 K의 미분항을 숨기지 않는다.

## 3. 양성, 보존량과 정확한 사영 항등식

### 보조정리 1: 반응계의 양성과 선형 불변량

K가 Metzler이고 x_i=0에서 제거 반응은 해당 x_i를 반응물 인자로 포함하므로 소멸한다. 따라서 비음수 초기 상태에서 식 (R7.2)는 비음수 cone을 보존한다. 계수 정칙성과 유계 invariant box 아래에는 해당 유한 구간의 Caratheodory 해가 유일하다.

행렬 W가 WK=0, WS=0을 만족하면

\[
(Wx)'=0.
\tag{R7.6}
\]

특히 양의 성분을 갖는 보존량 행이 있으면 비음수 상태의 상계를 그 보존량으로 정할 수 있다. 임의의 box를 사후에 궤적에 맞춘 것으로 간주하지 않고, 불변량 또는 별도 enclosure로 그 유효성을 확인한다.

coarse에서 같은 불변량을 보존하려면 W=\(\bar W P\)가 필요하다. 이때 \(\bar W G=WSa=0\)이다. delta=0 또는 \(\bar W\delta=0\)일 때 coarse 불변량도 보존된다. P>=0, \(\mathcal E\)>=0, \(P\mathcal E=I\)이면 y_i=0에서 그 집계에 기여하는 모든 lifted 미시상태가 0이다. fine 반응장의 quasipositivity를 합하면 coarse G의 quasipositivity가 따른다.

### 보조정리 2: 동적 lift 항등식

\[
A_0=K\mathcal E-\dot{\mathcal E}
\]

라 두면 \(P A_0=0\)이며

\[
\begin{aligned}
y'&=PSa(t,x),\\
r'&=Kr+A_0y+QSa(t,x),\\
e'&=PS\{a(t,x)-a(t,\mathcal E y)\}
       +G(t,y)-G(t,\bar y)-\delta.
\end{aligned}
\tag{R7.7}
\]

증명은 r=x-\(\mathcal E Px\)를 미분하고 PK=0, \(P\dot{\mathcal E}=0\)을 쓰는 직접 전개다. \(\dot{\mathcal E}y\)의 부호는 음수다. 집계 formation 총량의 차이는 마지막 식의 G 차이에 그대로 남는다.

잔차 반응장을

\[
F_r(t,y,r)=A_0y+QSa(t,\mathcal E y+r)
\]

로 정의하면

\[
F_r(t,y,r)=F_r(t,\bar y,0)
 +QS\{a(t,\mathcal E y+r)-a(t,\mathcal E y)\}
 +A_0e+QS\{a(t,\mathcal E y)-a(t,\mathcal E\bar y)\}.
\tag{R7.8}
\]

이 분해가 아래의 a,b,g_r를 구분한다. baseline forcing을 잔차 Lipschitz 항과 중복 계상할 필요가 없다.

## 4. 일반 Jacobian 계수의 유효한 계산법

R=||r||_1, E_err=||e||_1로 둔다. 이 절의 E_err는 lift \(\mathcal E\)와 다른 변수다. 각 블록에서 다음 상계를 만족하는 상수를 공급한다.

\[
\begin{aligned}
a&\ge\sup\|QSJ_a(t,z)\|_1,\qquad a\ge0,\\
b&\ge\sup\|A_0+QSJ_a(t,\mathcal E\zeta)\mathcal E\|_1,\qquad b\ge0,\\
c&\ge\sup\|PSJ_a(t,z)\|_1,\qquad c\ge0,\\
d&\ge\sup\mu_1\!\left(PSJ_a(t,\mathcal E\zeta)\mathcal E\right),\\
g_r&\ge\sup\|F_r(t,\bar y,0)\|_1,\qquad
g_e\ge\mathop{\rm ess\,sup}\|\delta(t)\|_1.
\end{aligned}
\tag{R7.9}
\]

z는 x와 \(\mathcal E y\) 사이의 선분, zeta는 y와 ybar 사이의 선분을 포함한다. a,c에는 Z로 제한한 operator norm을 쓰면 더 작은 유효 경계가 가능하지만, 전체 l1 operator norm은 안전한 구현 선택이다. d는 signed one-sided bound이며 음수일 수 있다.

\[
\mu_1(M)=\max_j\left(M_{jj}+\sum_{i\ne j}|M_{ij}|\right).
\tag{R7.10}
\]

대각 성분을 절댓값으로 바꾸면 one-sided damping을 잃는다. interval matrix에서는 대각 상한과 off-diagonal 절댓값 상한을 사용하면 안전한 d 상계를 얻는다. interval dependency를 무시한 독립 box 연산은 상계를 넓힐 수 있으나 방향은 보존된다.

식 (R7.3)에 대해 0<=x_i<=M_i, 0<=k_l<=k_l^+이면

\[
0\le\partial_i a_\ell
\le
k_\ell^+\alpha_{i\ell}
M_i^{\alpha_{i\ell}-1}
\prod_{j\ne i}M_j^{\alpha_{j\ell}}
\tag{R7.11}
\]

이다. \(\alpha_{i\ell}=0\)이면 미분을 먼저 0으로 정의하여 음의 지수나 0/0을 만들지 않는다. 나머지는 다항식의 usual \(x^0=1\)을 사용한다. 이 식은 rate 및 density box의 exact rational upper를 받으면 exact rational로 계산된다. k 또는 branch가 별도의 상태 함수라면 그 미분도 J_a에 포함해야 한다.

P,Q,S,\(\mathcal E\)가 주는 부호와 불변량을 곱셈 전에 보존하면 불필요한 절댓값 손실을 줄인다. 서로 다른 차원의 오차 norm을 고르면 a,d의 단위는 time^{-1}, b,c에는 두 오차 좌표의 변환 단위가 포함된다. 이 문서의 물리 밀도 norm에서는 a,b,c,d 모두 s^{-1}다.

## 5. 명목 전파와 인과적인 블록 정리

각 블록 [t_n,t_n+H]에서 K의 Z 위 전파 \(\Phi_K(t,s)\)에 대해

\[
\|\Phi_K(t,s)z\|_1\le\|z\|_1
\quad(t_n\le s\le t\le t_n+H,\ z\in Z),
\]
\[
\|\Phi_K(t_n+H,t_n)z\|_1\le\rho_n\|z\|_1,\quad 0\le\rho_n\le1
\tag{R7.12}
\]

을 가정한다. 정렬된 블록 endpoint 정리에는 이 두 조건으로 충분하다. 중간 forcing에 길이 H의 수축을 적용하지 않는다. R6의 sliding-window 조건은 더 강한 재사용 근거를 줄 수 있지만, 실제 H와 clock, generator 계열을 맞춰야 한다.

### 정리 1: 일반 유한 블록 피드백 경계

식 (R7.2)–(R7.12)의 전제 아래

\[
B=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
g=\binom{g_r}{g_e},\quad a,b,c\ge0,\quad d\in\mathbb R,
\]

라 두고 \(w_0\ge(R(t_n),E_{\rm err}(t_n))^T\)라 하자. 그러면 0<=u<=H에서

\[
\binom{R(t_n+u)}{E_{\rm err}(t_n+u)}
\le
V(u):=e^{Bu}w_0+\int_0^u e^{Bs}g\,ds,
\tag{R7.13}
\]

그리고 endpoint에서 식 (R7.1)이 성립한다.

**증명.** 식 (R7.8)의 평균값 정리와 (R7.9), 명목 비팽창성에서 거의 모든 시각에
\(R'\le aR+bE_{\rm err}+g_r\)를 얻는다. coarse 식에는 matrix measure 경계를 적용하여
\(D^+E_{\rm err}\le cR+dE_{\rm err}+g_e\)를 얻는다. B는 Metzler이므로 비교 원리에 따라 식 (R7.13)이 성립한다. 이 진술은 절대연속 함수의 거의 모든 점의 미분 부등식으로도 충분하다.

잔차의 Duhamel 식을 endpoint에만 적용하면

\[
R(t_n+H)\le\rho_nR(t_n)
+\int_0^H(aR+bE_{\rm err}+g_r)(t_n+s)\,ds.
\]

적분에 V를 넣고 \(V_1'=aV_1+bV_2+g_r\)를 적분하면 우변은
\(\rho_n w_{0,1}+V_1(H)-w_{0,1}\) 이하이다. 두 번째 성분은 그대로 V_2(H)로 둔다. 이것이 정확히 (R7.1)이다. □

### T의 양성과 반복

Metzler B에 대해 e^{Bu}>=0이다. 초기값 e_1에서 v'=Bv를 풀면
\(v_1'=av_1+bv_2\ge av_1\ge0\)이므로 \(e^{BH}_{11}\ge1\).
따라서 \(T_{11}=e^{BH}_{11}-1+\rho\ge\rho\), 다른 성분도 비음수다. q도 비음수다. d<0이어도 이 증명은 그대로 유효하다.

유효한 블록마다 \(w_{n+1}=T_nw_n+q_n\)를 반복하면 모든 endpoint를 덮는다. whole-block 상계는 \(V_n(u)\)로 별도 보존한다. d<0이면 V_2가 감소할 수 있으므로 endpoint 값을 이전 블록 전체의 상계로 대체하지 않는다.

T가 감소적인 행렬이어야 유한 시간 정리가 성립하는 것은 아니다. 추가로 일정 T,q와 양의 벡터 p, 0<=theta<1에 대해 Tp<=theta p를 입증하면 weighted max norm에서

\[
\|w_n\|_{p,\infty}\le
\theta^n\|w_0\|_{p,\infty}
+\frac{1-\theta^n}{1-\theta}\|q\|_{p,\infty}.
\tag{R7.14}
\]

그 추가 조건이 없으면 (R7.1), (R7.13)의 유한 시간 경계를 사용한다.

## 6. 늦게 들어오는 forcing에 대한 정확한 반례

K=(gamma/2)[[-1,1],[1,-1]], gamma>0, pi=(1/2,1/2)^T를 택한다. Z에서 정확한 길이 H 수축률은 rho=exp(-gamma H)다. x(0)=0이고, 마지막 epsilon 구간 [H-epsilon,H]에만 비음수 formation

\[
f(t)=(J/\epsilon,0)^T,\qquad 0<\epsilon\le H,\quad J>0
\]

를 넣는다. \(Qf=(J/\epsilon)v\), \(v=(1/2,-1/2)^T\), ||v||_1=1이므로

\[
R(H)=J\,\frac{1-e^{-\gamma\epsilon}}{\gamma\epsilon}.
\tag{R7.15}
\]

\(e^z>1+z\) for z>0에서 \((1-e^{-z})/z>e^{-z}\)이고, 따라서
\(R(H)>J e^{-\gamma H}=\rho J\).
전체 적분 forcing J에 rho를 한 번 곱하는 업데이트는 이 양의 선형계에서도 경계를 위반한다. epsilon->0에서 R(H)->J라는 극한이 인과적 이유를 드러낸다. 이것은 잘못된 업데이트 하나에 대한 구성적 반례이며 물리적 불가능성 정리가 아니다.

## 7. HD 공유 저장고 모형과 정확한 불변량

m_HD>=1개 HD 상태를 선언하고 fine 상태 순서를

\[
z=(u,v,w,x_1,\ldots,x_{m_{\rm HD}})^T
\]

로 둔다. u=H2, v=D+, w=H+, x_i=HD_i다. conditional state-matched finite network의 사건은

\[
u+v\longrightarrow w+x_i,\quad
a_i^+=k_f(t)\alpha_i(t)uv,\quad
x_i+w\longrightarrow u+v,\quad a_i^-=d_i(t)wx_i,
\tag{R7.16}
\]

이며 alpha>=0, sum alpha=1이다. K_HD는 HD 상태 간 이동만 담당한다. formation 열은
\((-1,-1,+1,+e_i)^T\), destruction은 그 반대다.

\[
\begin{aligned}
H_{\rm nuc}&=2u+w+\sum_i x_i,\\
D_{\rm nuc}&=v+\sum_i x_i,\\
Q_{\rm charge}&=v+w
\end{aligned}
\tag{R7.17}
\]

는 각 사건 열과 K_HD에 대해 정확히 보존된다. 원소 핵과 전하를 맞추려고 외부에 전자나 광자를 추가하지 않는다.

X=sum x_i, y=(u,v,w,X)^T,
\(\mathcal E_\pi y=(u,v,w,\pi X)^T\), pi>=0, sum pi=1로 둔다.
coarse의 reaction direction은 \(s=(-1,-1,+1,+1)^T\)이며

\[
\bar y'=s\,[k_f\bar u\bar v-\bar d\,\bar w\bar X],
\qquad \bar d=d^T\pi.
\tag{R7.18}
\]

실제 집계는

\[
y'=s\,[k_fuv-\bar d\,wX-wd^Tr].
\tag{R7.19}
\]

### source와 pool의 결속 조건

이 정수 방향은 R4에서 이미 확보된 HD formation/destruction 사건 열과 같다. 원 source의 상태 범위는 그대로 유지한다: Honvault corrected formation의 입사 상태는 p-H2(v=0,j=0), GL2022 destruction은 thermal HD(v=0,j=0..8)와 source spin 가중 H2 제품 합이다. 따라서 (R7.16)을 실제 폐쇄 pool 모형에 적용하려면 두 방향의 common H2/HD pool, state mapping, product branch, collider와 clock을 별도로 결속해야 한다. 정수 열의 반대 방향이라는 사실만으로 두 native 계수를 microscopic detailed-balance pair로 승인하지 않는다.

alpha를 pi와 같게 설정하는 기본값은 없다. d_i도 GL2022 aggregate fit 한 값으로 채우지 않는다. 이 절은 모든 조건을 명시한 유한 network의 정리이며 실제 branch/density/consumer는 여전히 입력 의존 상태다.

## 8. 보존량을 이용한 scalar coarse error와 음의 damping

fine와 coarse 초기 집계가 같은 H_nuc,D_nuc,Q_charge를 가지면 이 세 불변량의 오차는 항상 0이다. 세 보존량 행의 rank는 3이며 그 공통 kernel은 span{s}다. 따라서

\[
e=y-\bar y=s\eta,\qquad \eta=X-\bar X.
\tag{R7.20}
\]

그러므로 u=ubar-eta, v=vbar-eta, w=wbar+eta이고

\[
uv-\bar u\bar v=-U_m\eta,\qquad
wX-\bar w\bar X=W_m\eta,
\]
\[
U_m=\tfrac12(u+v+\bar u+\bar v),\qquad
W_m=\tfrac12(w+X+\bar w+\bar X).
\tag{R7.21}
\]

식 (R7.18)–(R7.21)에서

\[
\eta'=-[k_f U_m+\bar d W_m]\,\eta-wd^Tr.
\tag{R7.22}
\]

모든 상태가 비음수이므로 대괄호는 비음수다. R4의 zero-sum bound를 그대로 적용하면

\[
|d^Tr|\le\tfrac12(d_{\max}-d_{\min})R.
\tag{R7.23}
\]

따라서 이제 \(E_{\rm err}=|\eta|\)를 선택하여 cR+dE_err 경계를 만들 수 있다. 이 좌표의 초기 compatibility 조건을 검사해야 한다. 임의의 서로 다른 보존량을 가진 두 초기 상태에 (R7.20)을 적용하지 않는다. coarse가 수치 defect delta=s*delta_eta를 가지면 같은 scalar 구조를 유지하고 g_e>=|delta_eta|를 더한다. invariant를 보존하지 않는 coarse defect는 일반 벡터 정리로 돌아가 처리한다.

이 scalar 변수는 모든 coarse error를 제공한다: \(|e_i|=|\eta|\), \(\|e\|_1=4|\eta|\). 이 계수를 결과의 observable 변환에 명시한다.

## 9. HD에 권장하는 명시적 interval 계수

whole-block box를
\[
m_u\le u,\bar u\le M_u,\quad
m_v\le v,\bar v\le M_v,\quad
m_w\le w,\bar w\le M_w,\quad
m_X\le X,\bar X\le M_X
\]
로 두고 모든 lower는 비음수다. k_f∈[k^-,k^+], \(d_i\in[d_i^-,d_i^+]\), pi_i∈[pi_i^-,pi_i^+]를 선언한다.

\[
q_0=K_{\rm HD}\pi-\dot\pi,\quad
\vartheta=\alpha-\pi,\quad
v_D=D\pi-\pi\bar d,\quad Q_\pi=I-\pi1^T,
\tag{R7.24}
\]

\[
q_*\ge\|q_0\|_1,\quad
t_*\ge\|\vartheta\|_1,\quad
\Delta_d=\max_i d_i^+-\min_i d_i^-,
\quad v_*\ge\|v_D\|_1,
\]
\[
h_*=2\max_i[d_i^+(1-\pi_i^-)],
\qquad
\bar d^-\le d^T\pi.
\tag{R7.25}
\]

q_*는 실제 K/pi/piDot bound의 입력이다. t_*는 실제 branch/lift box로부터 얻는다. 두 simplex 사이에 t_*<=2라는 보편적인 조건부 경계는 사용할 수 있으나 실제 branch 벡터를 생성한 것으로 기록하지 않는다. \(\bar d^-=\min_i d_i^-\)는 항상 안전하며 추가의 정확한 simplex 정보로 더 크게 만들 수 있다.

\(v_*=\Delta_d/2\)도 항상 안전하다. 증명: pi를 확률 가중으로 본 D의 평균 mu에 대해
Var(D)<= (mu-d_min)(d_max-mu)<=Delta_d^2/4이고,
E|D-mu|<=sqrt(Var(D))<=Delta_d/2다. 첫 부등식은
E[(D-d_min)(d_max-D)]>=0을 전개하면 나온다.
\(\|Q_\pi D\|_1=2\max_i d_i(1-\pi_i)\le h_*\) 역시 각 열을 직접 합하면 얻는다.

HD 잔차의 정확한 식은

\[
r'=K_{\rm HD}r-wQ_\pi D r
       +q_0X+k_fuv\,\vartheta-wXv_D.
\tag{R7.26}
\]

baseline forcing를 \(F_0(y)=q_0X+k_fuv\vartheta-wXv_D\)라 하면, 식 (R7.21)에 따라

\[
F_0(y)-F_0(\bar y)
=\eta[q_0-k_fU_m\vartheta-W_mv_D].
\tag{R7.27}
\]

이에 따른 추천 safe coefficients는

\[
\boxed{
\begin{aligned}
a&=M_wh_*,\\
b&=q_*+k^+(M_u+M_v)t_*+(M_w+M_X)v_*,\\
c&=M_w\Delta_d/2,\\
d&=-\{k^-(m_u+m_v)+\bar d^-(m_w+m_X)\},\\
g_r&=q_*M_X+k^+M_uM_vt_*+M_wM_Xv_*,\\
g_e&=0\quad\text{(정확히 같은-source coarse ODE).}
\end{aligned}}
\tag{R7.28}
\]

generic coarse defect가 있으면 앞 절의 조건 아래 g_e를 해당 상계로 바꾼다. t_*,q_*,v_*를 실제 interval로 더 작게 인증하면 동일한 식을 쓸 수 있다.

a,b,c,d의 물리 단위는 s^{-1}, g_r,g_e는 cm^{-3}s^{-1}다.
d는 lower damping의 음수이므로 API가 자동으로 0으로 clip하지 않는다.
lower density가 0이면 해당 d 기여가 0이 되는 경계도 그대로 허용한다.

### box의 한 구성

비음수 보존량으로부터
\[
u\le H_{\rm nuc}/2,\quad
v\le\min(D_{\rm nuc},Q_{\rm charge}),\quad
w\le\min(H_{\rm nuc},Q_{\rm charge}),\quad
X\le\min(H_{\rm nuc},D_{\rm nuc})
\tag{R7.29}
\]
를 얻는다. 같은 초기 불변량을 쓰면 fine/coarse 모두의 상계다.
양의 lower box를 쓰려면 별도 경계를 입증한다. 예를 들어
u'>=-k^+M_v u이므로
\(u(t_n+s)\ge u(t_n)e^{-k^+M_vs}\).
v,w,X도 respective loss-rate upper로 같은 방식의 lower를 얻는다.
미공급 초기 밀도에서 positive lower를 추측하지 않는다.

### 원 K의 rho를 쓸 수 있는 이유

식 (R7.26)의 상태 의존 destruction/reset 부분 \(-wQ_\pi Dr\) 전체를 aR에 넣었다. 따라서 명목 전파는 실제로 K_HD이며 R6의 K 인증을 같은 계열과 clock으로 결속하여 사용할 수 있다. full \(L=K+w(\pi d^T-D)\)에 K-only rho를 붙인 것이 아니다. 이 항을 full L에 흡수하여 a를 줄이는 구현은 그 full L 계열의 전파 인증을 별도로 요구한다. 같은 destruction을 명목 damping과 forcing 양쪽에서 중복 차감하지 않는다.

## 10. singular/zero B와 정확 산술 구현

지수와 forcing 적분은 B^{-1}을 요구하지 않는다.

\[
e^{BH}=\sum_{j=0}^\infty\frac{H^jB^j}{j!},\qquad
q=H\sum_{j=0}^\infty\frac{H^jB^j}{(j+1)!}\,g.
\tag{R7.30}
\]

- B=0: T=diag(rho,1), q=Hg.
- b=c=0: T=diag(exp(aH)-1+rho,exp(dH)); q_i=g_i*phi(B_ii,H), phi(z,H)=(exp(zH)-1)/z for z≠0, phi(0,H)=H.
- a=d=c=0: B^2=0, T=[[rho,bH],[0,1]], q=(Hg_r+bH^2g_e/2,Hg_e)^T.

부호 있는 Taylor 항을 단순히 버려 entrywise upper라고 주장하지 않는다. 한 안전한 계산법은 augmented Metzler matrix

\[
M=\begin{pmatrix}a&b&g_r\\c&d&g_e\\0&0&0\end{pmatrix},
\quad
e^{HM}=\begin{pmatrix}e^{BH}&q\\0&1\end{pmatrix}
\tag{R7.31}
\]

를 사용한다. 수치 norm의 좌표를 정할 때 밀도/시간 scale을 명시하여 augmented 좌표의 단위를 고정한다. sigma>=max(0,-d), C=H(M+sigma I)>=0, z=||C||_infty로 두고 N+2>z를 택하면

\[
S_N=\sum_{j=0}^N C^j/j!,\quad
\tau_N=\frac{z^{N+1}}{(N+1)!}\frac1{1-z/(N+2)},\quad
S_N\le e^C\le S_N+\tau_N{\bf 1}{\bf 1}^T.
\tag{R7.32}
\]

각 tail의 induced-infinity norm을 scalar exponential tail로 덮고, 이후 항 비율을 z/(N+2)로 덮는 기하급수에서 (R7.32)가 따른다. exp(-sigma H)의 exact rational upper e_+를 곱하면
\(e^{HM}\le e_+(S_N+\tau_N11^T)\).
여기서 T_upper는 좌상단 upper에서 exact \((1-\rho)e_1e_1^T\)를 뺀다. 실제 T>=0이므로 upper도 비음수다. q_upper는 우상단 두 성분이다. exp primitive의 기존 증명/동일 코드 근거는 재사용할 수 있으며 새 domain 밖 입력을 clamp하지 않는다.

실제 구현은 이 방법과 동등하게 입증된 다른 양의 상계 알고리즘을 선택할 수 있다. 출력에는 H,B,g,rho, 선택한 polynomial/shift/precision과 잔여 오차 상계를 남긴다. scientific reference의 floating comparison tolerance는 exact upper proof와 별도로 보고한다.

## 11. 판별 검증에 전달하는 항목

아직 실행하지 않은 신규 검증 의무는 다음과 같다.

1. (R7.7)의 time-dependent lift 부호와 P r=0, W S=0.
2. HD shared-reservoir scalar 식 (R7.22), 잔차 식 (R7.26), (R7.27).
3. 생성 시점을 구별하는 late-forcing 반례 및 rho=1의 ordinary comparison 극한.
4. B=0, diagonal, nilpotent/singular, d<0인 Metzler case.
5. interval Jacobian에서 alpha_i=0와 M_i=0 경계.
6. source method 대안의 중복 활성, 미공급 branch의 기본값, K-only/full-L 혼동을 거부하는 guard.
7. exact upper matrix/integral을 독립 exponentiation/analytic controls와 비교하고 원시 first result 보존.
8. whole-block bound와 endpoint bound를 별도로 확인.
9. 같은 불변량 조건을 가진 HD fixture와 초기 compatibility를 어긴 입력 guard.
10. 원 R6 graph/payload/source 근거는 재사용하며 이전 76/109 체크를 재실행하지 않는다.

R7의 새 유한 실행 계약은 primary 1회/60 CPU s, independent reference 1회/60 CPU s, Wolfram 1회/30 s이다. 이 문서 작성 중 사용한 과학 실행은 0이다. 기존 R6 및 PHYS91 잔여 [0,0,0]은 변하지 않는다.

## 12. 1차 문헌 비교와 기여 범위

[Ovchinnikov et al., CLUE, arXiv:2004.11961v2, §2](https://arxiv.org/html/2004.11961v2)의 Definition 1과 Jacobian invariant-row-space 조건을 실제로 읽었다. 해당 연구는 polynomial ODE에서 선택한 observables를 보존하는 exact linear lumping을 구성한다. R7은 exact lumpability를 가정하지 않고 지정된 positive lift의 잔차와 coarse trajectory 차이를 경계하며, 기존 유한 블록 수축을 인과적으로 조합한다. 비교 대상의 수학은 이미 확립된 선형 사영·다항식 Jacobian·협조계 비교 원리다.

해당 CLUE [2021 correction](https://doi.org/10.1093/bioinformatics/btab258)의 publisher 검색 반환문은 typographical/formatting correction을 명시했다. direct full fetch는 timeout이므로 그 읽기 수준을 metadata/search-returned correction text로 기록한다. 이를 독립적인 새 정리의 근거로 사용하지 않는다.

uniformization/Dobrushin의 원전 및 literal Gibbs enclosure는 R6에 보존된 실제 읽기/증명 identity를 재사용한다. 이 단위의 개선은 기존 WU 사건 열에 state-dependent formation/source-difference 의무를 연결하고, shared-reservoir 불변량과 causal endpoint update를 구현 가능한 exact coefficient 계약으로 만든 것이다. 새 기본 정리의 문헌 우선권이나 strong no-go를 주장하지 않는다.

## 13. 적용 전 남은 실제 입력

GL2022 DOI10.1063/5.0128598의 새로운 HAL metadata 경로에서 hal-04285297v1과 첨부 main PDF 한 개를 확인했다. record/PDF 본문 접근은 Exa SOURCE_NOT_AVAILABLE 및 웹 Anubis Access Denied로 끝났고, 공개 API files_s에는 214302_1_online.pdf 한 개만 반환됐다. 원 state-to-state destruction 배열은 아직 미회수다. 이는 조회한 경로의 상태이며 자료의 전역 부재 주장이 아니다. 옛 실패 supplement URL을 반복 요청하지 않았다.

실제 WU 소비자, density/history, physical clock, formation branch, state-specific destruction vector, x0 및 전체 interval bounds는 별도 공급되어야 한다. HE radiative packet이나 원자 전자 stock은 각각의 실제 상태/소비자에 맞춰 평가하며 HD reactive array 자리에 넣지 않는다. 위 조건부 정리는 이 입력 의존성을 대체하지 않는다.

