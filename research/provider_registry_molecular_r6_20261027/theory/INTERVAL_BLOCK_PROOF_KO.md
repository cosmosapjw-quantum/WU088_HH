# WU088_HH R6: literal Gibbs 구간과 강제 유한 블록 전파자

정식화일: 2026-10-27 UTC. 이 문서는 source literal에서 outward Gibbs 구간, 시간가변 Markov 전파자의 유한 블록 수축, 강제항을 포함한 비교식까지 연결한다. 0–7절은 독립 심사를 받은 기여 초안의 핵심 증명을 보존하고, 심사의 N1·N2 명확화를 반영했다. 8–9절은 그 식과 실제 생산 코어를 연결한다. 일반 유한 차원 정리와 실행 가능한 함수의 경계를 구분하며, 실제 수치 실행·코드 수용 상태는 `EXECUTION_LEDGER.json`, `raw/`, `reviews/`에 기록한다.

## 0. 고정한 선행 근거와 이번 변경 의무

고정 저장소는 `cosmosapjw-quantum/WU088_HH`, commit `35bb7f296abc8ff6c8b38c2c08cc14dd498d4c99`이다. 실제 읽은 선행 파일은 `research/provider_registry_molecular_r5_20261027/theory/DYNAMIC_LIFT.md`, `theory/HD_GRAPH_BLOCK.md`, `followup/NEXT_INPUT_CONTRACT.json`이다. 파일별 blob SHA와 읽은 범위는 별도 `SOURCE_MANIFEST.json`에 기록한다.

R5가 이미 유도한 유한 상태 column convention을 재사용한다. 모든 벡터는 column이다.

\[
x'=Kx-hDx+f,\quad D=\operatorname{diag}(d),\quad X=\mathbf1^Tx,
\quad r=x-\pi X,\quad Q=I-\pi\mathbf1^T.
\]

여기서 \(K\)는 비대각 성분이 음이 아니고 column sum이 0인 생성자, \(\pi\)는 확률벡터이다. \(\pi\)는 국소 절대연속, 그 밖의 계수는 국소 유계 가측으로 두며 강제항은 국소 적분가능하다. 정확한 식은

\[
r'=Lr+cX+Qf,\quad L=K+h(\pi d^T-D),
\quad c=K\pi-\dot\pi-h(D\pi-\pi d^T\pi).
\]

\(r,c,Qf\)의 합은 0이다. 이번 의무는 (i) 17자리 근사 열확률을 원천의 decimal literal과 SI 정의상수로부터 증명된 구간으로 바꾸고, (ii) 순간 수축률이 0인 희소 그래프에도 적용되는 강제 유한 블록 bound를 구현 가능한 형태로 유도하는 것이다. 이미 저장된 REC54DB/24LTE, R5 비교식과 native LAMDA 그래프는 재사용 근거이며 새로운 수치 결과로 세지 않는다.

Native 100 K source application의 범위는 제공된 HD para-H2 회전 여기 그래프이다. GL2022 반응성 파괴율 \(d_j\), 물리적 collider density, 명명된 REC/REI consumer는 이번 조사에서 결합되지 않았다. 따라서 원천 그래프에 실제 적용할 때는 \(A=K,\kappa=0\)이며, 이하 \(L,d,h,f\) 정리는 향후 입력을 위한 조건부 일반 정리이다. 제공되지 않은 전이는 `MISSING_NOT_ZERO`, 진동 양자수는 선행 원천의 미지정 상태를 유지한다.

## 1. 정확한 상수와 literal 열가중치

원천 에너지가 파수 \(\tilde\nu_i\,[\mathrm{cm}^{-1}]\)로 주어지고 기준 준위 차가 음이 아니면

\[
z_i=\frac{h_{\rm P}c_{\rm light}\,100(\tilde\nu_i-\tilde\nu_0)}{k_{\rm B}T},
\qquad w_i=g_i e^{-z_i},\qquad
\pi_i=\frac{w_i}{\sum_jw_j}.
\]

BIPM의 SI 정의상수 표에서 \(h_{\rm P}=6.62607015\,10^{-34}\,\mathrm{J\,s}\), \(c_{\rm light}=299792458\,\mathrm{m/s}\), \(k_{\rm B}=1.380649\,10^{-23}\,\mathrm{J/K}\)는 정확하다. 출처는 https://www.bipm.org/en/measurement-units/si-defining-constants 이다. 따라서 source decimal literal, degeneracy, \(T=100\,\mathrm K\)를 명시한 뒤 \(z_i\)를 유리수로 구성할 수 있다. 이것은 source 에너지의 실험적 불확실성이 0이라는 주장과 다르다. 제공되지 않은 측정 오차나 공분산은 미지정이다.

에너지 gap \(E_i\in[E_i^-,E_i^+]\), 온도 \(0<T^-\le T\le T^+\), \(E_i^-\ge0\)가 주어진 일반 수학 입력에는

\[
z_i\in\left[\frac{E_i^-}{k_BT^+},\frac{E_i^+}{k_BT^-}\right]
\]

를 사용한다. 기준 에너지 자체가 불확실하면 먼저 올바른 gap 구간을 만들어야 한다. 공통 기준 에너지를 서로 독립인 오차로 처리해 상관관계를 지우지 않는다. 이 일반식은 source에 없는 온도에서 충돌률을 물리적으로 보간하거나 생성할 권한을 주지 않는다. 이번 native 적용은 고정 100 K이다.

### 1.1 유리수 지수함수 enclosure

\(z\ge0\)가 유리수라고 하자. \(s\ge0\)를 골라 \(y=z/2^s\in[0,1]\)로 만들고

\[
S_N(y)=\sum_{k=0}^N\frac{(-y)^k}{k!}
\]

라 하자. 교대급수 나머지 정리와 항의 감소성으로, \(m\ge1\)일 때

\[
0<S_{2m+1}(y)\le e^{-y}\le S_{2m}(y),
\qquad
S_{2m}(y)-S_{2m+1}(y)=\frac{y^{2m+1}}{(2m+1)!}.
\]

\(y=0\)이면 양 끝은 정확히 1이다. 하한의 양성은 \(S_3(y)=1-y+y^2/2-y^3/6>0\) on \([0,1]\)와 교대 부분합의 단조성으로 확인한다. 양의 수에 대한 거듭제곱은 단조이므로

\[
S_{2m+1}(y)^{2^s}\le e^{-z}\le S_{2m}(y)^{2^s}.
\]

모든 덧셈, 곱셈, 나눗셈, 거듭제곱을 정수/유리수로 수행하면 IEEE 부동소수점 반올림을 가정하지 않아도 된다. 표시용 소수만 별도로 outward rounding한다. 구간 \([z^-,z^+]\)에는 감소성을 적용해 \(e^{-z^+}\)의 하한과 \(e^{-z^-}\)의 상한을 취한다. 최종 너비는 초기 Taylor gap과 같지 않으므로 구현은 거듭제곱 후 실제 유리수 구간 너비를 보고해야 한다. 정확한 enclosure는 차수 선택과 무관하게 성립하며, 목표 너비 달성 여부는 별도 acceptance gate이다.

큰 지수에 대한 대안은 양의 급수 \(e^z\)의 부분합과 기하급수 꼬리이다. \(N+2>z\)이면

\[
T_N=\sum_{k=0}^N z^k/k!,\quad
R_N\le\frac{z^{N+1}/(N+1)!}{1-z/(N+2)},\quad
\frac1{T_N+R_N}\le e^{-z}\le\frac1{T_N}.
\]

이번 구현은 첫 번째 range reduction 방식을 선택하면 충분하다. 두 방식을 중복 실행할 필요는 없다.

### 1.2 정규화 확률의 enclosure와 상관관계

\(0<\ell_i\le w_i\le u_i\)이면

\[
\boxed{\quad
\pi_i^- =\frac{\ell_i}{\ell_i+\sum_{j\ne i}u_j}
\le\pi_i\le
\frac{u_i}{u_i+\sum_{j\ne i}\ell_j}=\pi_i^+ .\quad}
\]

증명: \(w_i/\sum_jw_j\)는 자신의 가중치에 대해 증가하고 다른 모든 가중치에 대해 감소한다. 독립 가중치 box에서는 이 좌표별 극값이 달성되므로 식은 좌표별로 sharp하다. 실제 Gibbs family의 공통 온도/에너지 상관관계를 포함하면 여전히 유효한 외측 box이지만 모든 좌표의 극값이 동시에 달성된다는 뜻은 아니다. \(\pi\in\Delta_{n-1}\)를 계속 유지하며, \(\sum_i\pi_i^-=1\) 또는 \(\sum_i\pi_i^+=1\)을 요구하지 않는다.

이 정규화의 단조성은 Wei et al. (2023), section 2.1, eqs. (5a–b)의 constant softmax bounds와 같은 기본 원리이다: https://proceedings.mlr.press/v206/wei23c/wei23c.pdf . 새 수학 정리라고 주장하지 않는다. 본 기여는 원천 literal, 정확한 상수, 검증 가능한 지수함수 계산 및 후속 생성자 구간을 연결하는 것이다.

상세균형 상향률은 정규화된 box의 비율을 다시 나누기보다

\[
\frac{\pi_u}{\pi_l}=\frac{g_u}{g_l}
\exp[-(E_u-E_l)/(k_BT)]
\]

를 직접 감싼다. source downward coefficient \(q_{l,u}\)와 동일 pair ratio를 사용해 \(q_{u,l}=q_{l,u}\pi_u/\pi_l\)로 정의하면 실제 literal Gibbs 분포에 대한 pairwise balance가 정확하다. 모든 제공된 쌍을 그렇게 구성하고 diagonal을 column sum 0으로 정하면 실제 \(K\pi=0\)이다. 독립 구간산술에서 \(K\pi\)가 넓은 구간으로 보이는 것은 의존성 손실이며 새로운 비평형 결함이 아니다. 이 폐쇄 그래프 선언은 누락된 다른 물리 채널이 0이라는 주장도 아니다.

초기 잔차가 유리수 대표 확률 \(\hat\pi\)로 계산된다면 \(\epsilon_\pi=\sum_i\max(|\pi_i^--\hat\pi_i|,|\pi_i^+-\hat\pi_i|)\)로 두어

\[
\|x_0-\pi X_0\|_1\le\|x_0-\hat\pi X_0\|_1+X_0\epsilon_\pi
\]

를 사용할 수 있다. 대표값의 정확도와 enclosure의 타당성은 구분한다.

## 2. 시간가변 생성자 family의 유한 블록 certificate

### 2.1 입력 조건

\(A(t)\)가 column Markov generator이며 모든 관심 시간에 \(i\ne j\)에 대해

\[
0\le a_{ij}^-\le A_{ij}(t)\le a_{ij}^+,
\qquad A_{jj}(t)=-\sum_{i\ne j}A_{ij}(t)
\]

라고 하자. \(a^\pm\)는 각각 entrywise boundary이고 임의의 matrix-box 대각을 별도 허용하지 않는다. \(\lambda>0\), \(\lambda\ge\max_j\sum_{i\ne j}a_{ij}^+\)를 선택하고

\[
P(t)=I+A(t)/\lambda,\qquad
(P_-)_{ij}=a_{ij}^-/\lambda\ (i\ne j),\quad
(P_-)_{jj}=1-\sum_{i\ne j}a_{ij}^+/\lambda
\]

로 둔다. 그러면 \(P(t)\)는 column-stochastic, \(0\le P_-\le P(t)\), \(P_-\)는 column-substochastic이다. 최대 exit 상한이 양수이면 \(\lambda=2\max_j\sum_{i\ne j}a_{ij}^+\)가 모든 diagonal에 \(1/2\) 이상의 하한을 준다. 최대 exit가 0이면 그 식으로 0을 나누지 말고 임의의 양의 \(\lambda\)를 택한다.

### 2.2 Ordered uniformization의 직접 증명

\(\Phi_A(t,s)\)를 전파자라 하자. \(A(t)=\lambda(P(t)-I)\)에 integrating factor를 적용한 Peano–Baker series는

\[
\Phi_A(s+H,s)=e^{-\lambda H}
\sum_{m=0}^{\infty}\lambda^m
\int_{s<t_1<\cdots<t_m<s+H}
P(t_m)\cdots P(t_1)\,dt_1\cdots dt_m.
\]

\(m=0\) 항은 \(I\)이다. 유한 차원에서 \(P(t)\)의 induced 1-norm은 1이므로 급수는 norm에서 절대 수렴하고, 유계 가측 계수에서도 적분식과 해의 유일성으로 이 표현을 얻는다. van Dijk (1991), section 3, Theorem 1은 시간가변 uniformization의 primary 선행 근거이다: https://research.vu.nl/ws/portalfiles/portal/73611171/Scanjob%20199100006 . 그 원문의 연속성 가정 대신 사용한 가측 유한 차원 버전은 위 직접 유도에 의존한다.

비음수 행렬곱의 성분별 단조성으로 모든 ordered product는 \(P_-^m\) 이상이다. 적분 simplex의 부피가 \(H^m/m!\)이므로

\[
\boxed{\quad
R_N(H)=e_-\sum_{m=0}^{N}\frac{(\lambda H)^m}{m!}P_-^m
\ \le\ \Phi_A(s+H,s),\qquad
0\le e_-\le e^{-\lambda H}.\quad}
\]

이것은 \(s\)에 독립인 하한이다. \(e_-\)는 1.1의 유리수 하한으로 얻는다. 부분합에서 빠진 항들은 모두 비음수이므로 lower bound를 위해 tail upper bound를 계산할 필요가 없다. 비음수 성분을 아래쪽으로 반올림하는 각 중간 계산도 하한 방향을 보존한다. 양의 항을 음수로 만드는 반올림 규칙은 허용하지 않으며, exact rational 선택이면 이런 문제가 없다. \(R_N\)의 column sums는 1 이하이다. 더 큰 \(N\)은 같은 \(e_-\)를 유지할 때 성분별 하한을 개선하지만, 필요 이상 반복 계산할 이유는 없다.

### 2.3 Pair overlap에서 수축률까지

\(n\ge2\)에서

\[
\beta_N=\min_{j<k}\sum_i\min\{(R_N)_{ij},(R_N)_{ik}\},
\qquad\rho=1-\beta_N
\]

로 둔다. \(0\le\beta_N\le1\)이다. Column-stochastic \(S\)의 zero-sum subspace \(Z=\{z:\mathbf1^Tz=0\}\)에 대한 induced 1-norm은

\[
\|S\|_{Z,1}=\frac12\max_{j,k}\|S e_j-S e_k\|_1
=1-\min_{j,k}\sum_i\min\{S_{ij},S_{ik}\}.
\]

첫 식은 양/음 부분을 각각 같은 질량의 확률분포로 정규화한 뒤 column-pair differences의 convex combination으로 표현하면 나온다. 둘째 식은 두 확률벡터의 \(\ell^1\) 거리와 공통 질량 항등식이다. 따라서

\[
\|\Phi_A(s+H,s)z\|_1\le\rho\|z\|_1\qquad(z\in Z).
\]

Gaubert–Qu (2015)의 primary 저자 PDF는 이 Dobrushin 공통 질량 특성을 제공한다: https://www.cmap.polytechnique.fr/~gaubert/PAPERS/GaubertQuIEOTD14QuFinal.pdf . 원문은 row convention을 쓰므로 여기서는 transpose를 취했다. 이산 전파자의 \(\rho\)와 R5 연속시간 생성자의 instantaneous coefficient \(\delta(A)\)는 다른 양이다.

같은 family bounds가 모든 이동 창에 유효하면 임의 \(t\ge s\)에 대해 full block과 길이 \(<H\) remainder로 분해하여

\[
\boxed{\quad\|\Phi_A(t,s)z\|_1
\le\rho^{\lfloor(t-s)/H\rfloor}\|z\|_1.\quad}
\]

나머지 창에는 Markov nonexpansiveness만 사용한다. \(\rho<1\)이더라도 \(-\log\rho/H\)를 prefactor 1인 순간 수축률로 대입하지 않는다. 원하면 \(C=\rho^{-1}\), \(\alpha=-\log\rho/H\)로 \(C e^{-\alpha(t-s)}\)형을 얻을 수 있으나 여기서는 불필요하고, \(\rho=0\) 예외도 별도이다. \(\beta_N=0\)은 이 certificate가 양의 수축을 입증하지 못했다는 뜻이며 전역 불가능성 정리가 아니다. \(n=1\)이면 \(Z=\{0\}\)이어서 잔차는 자명하게 0이다.

### 2.4 R5 path certificate의 재사용 위치

모든 column \(j\)에서 공통 root \(o\)로 길이 \(\ell_j\le m\)의 양의 하한 경로가 있고 root self-loop 하한이 양수이면

\[
\eta_j=(P_-)_{oo}^{m-\ell_j}
\prod_{q=1}^{\ell_j}(P_-)_{v_q,v_{q-1}},\quad
\eta=\min_j\eta_j>0.
\]

\((P_-^m)_{oj}\ge\eta\)이므로 단 하나의 급수 항만으로도

\[
\beta(H)\ge e^{-\lambda H}(\lambda H)^m\eta/m!.
\]

\(H=m/\lambda\)에서 \(e<3\)를 쓰면 R5 형태 \(\beta\ge m^m\eta/(3^m m!)\)가 복구된다. R5 HD의 \(m=8\) 경로는 이 정리의 재사용 가능한 존재 증거이며, 전체 nonnegative polynomial의 overlap은 여러 경로와 여러 항의 공통 질량을 합쳐 이보다 더 유용한 수축을 줄 수 있다. 어느 쪽도 새 rate source를 발명하지 않는다.

## 3. 공통 killing을 중복 계수하지 않고 분리하기

\(v(t)=h(t)d(t)\), \(L=K+\pi v^T-\operatorname{diag}(v)\)라 쓰자. 상수 \(\kappa\ge0\)가 모든 관심 시간에 \(\kappa\le\min_jv_j(t)\)를 만족한다고 하자. \(\tilde v=v-\kappa\mathbf1\ge0\)와

\[
A=K+\pi\tilde v^T-\operatorname{diag}(\tilde v)
\]

를 정의한다. \(A\)는 column Markov generator이다. 정확히

\[
L=A+\kappa(\pi\mathbf1^T-I),\qquad
L|_Z=A|_Z-\kappa I|_Z.
\]

따라서 zero-sum 잔차의 전파자는 \(\Phi_L(t,s)|_Z=e^{-\kappa(t-s)}\Phi_A(t,s)|_Z\)이고,

\[
\boxed{\quad\|\Phi_L(t,s)z\|_1
\le e^{-\kappa(t-s)}\rho^{\lfloor(t-s)/H\rfloor}\|z\|_1.\quad}
\]

여기의 \(\rho\)는 **전체 \(A\)**의 edge/exit bounds로 계산해야 한다. \(K\)만의 \(\rho\)를 비가환인 추가 reset generator에 그대로 붙이지 않는다. \(\kappa\)를 \(A\)에서 이미 분리한 뒤 R5의 같은 killing damping을 다시 더하면 중복 계수이다.

예를 들어 \(K_{ij}\in[K_{ij}^-,K_{ij}^+]\), \(\pi_i\in[\pi_i^-,\pi_i^+]\), \(v_j\in[v_j^-,v_j^+]\), \(v_j^-\ge\kappa\)인 경우

\[
a_{ij}^-=K_{ij}^-+\pi_i^-(v_j^--\kappa),\qquad
a_{ij}^+=K_{ij}^++\pi_i^+(v_j^+-\kappa)\quad(i\ne j)
\]

가 유효하다. 독립 box sum의 exit 상한 대신 simplex 구조를 사용하면

\[
\operatorname{exit}_j(A)
\le\sum_{i\ne j}K_{ij}^++(1-\pi_j^-)(v_j^+-\kappa)
\]

로 개선할 수 있다. 이 개선 exit 상한으로 \(P_-\)의 diagonal을 만들려면 실제 exit 전체를 감싼다는 증명을 함께 유지한다. 비대각 entrywise 상한 합과 일치하지 않아도 actual matrix에 대한 lower bound라는 사실이 충분하다. 이 경우도 \(P_-\) column-substochastic 조건은 직접 확인하거나 actual stochastic matrix에 의해 지배됨으로 정당화한다.

시간가변 하한 \(\kappa(t)\)도 \(e^{-\int_s^t\kappa}\)로 일반화되지만 실제 구현은 한 certificate family에서 공통 상수 하한을 써도 충분하다. \(h=0\)일 때 나눗셈을 만들지 않는 \(v\) 표기는 이 경계를 자동으로 처리한다.

## 4. 강제항을 포함한 block convolution

\(r'=Lr+u\), \(u(t)\in Z\), \(\|u(t)\|_1\le G(t)\), \(\|r(0)\|_1\le U_0\)라 하자. Duhamel formula와 3절 결과에서

\[
\|r(t)\|_1\le e^{-\kappa t}\rho^{\lfloor t/H\rfloor}U_0
+\int_0^t e^{-\kappa(t-s)}\rho^{\lfloor(t-s)/H\rfloor}G(s)\,ds.
\]

forcing은 매 순간 생성되므로 homogeneous factor를 전체 source mass에 한 번 곱하는 식은 일반적으로 틀리다. 특히 최근 \(<H\) 시간에 들어온 forcing에는 아직 full-block 수축을 주장할 수 없다.

### 4.1 블록 끝과 블록 내부의 서로 다른 경계

\(t_n=nH\), \(G(s)\le G_n\) on \([t_n,t_{n+1}]\)라 하고

\[
\Psi_\kappa(a)=\int_0^ae^{-\kappa u}\,du
=\begin{cases}(1-e^{-\kappa a})/\kappa,&\kappa>0,\\a,&\kappa=0.\end{cases}
\]

로 둔다. 해석적 비교 수열을 \(V_0=U_0\)와

\[
\boxed{V_{n+1}=\rho e^{-\kappa H}V_n+G_n\Psi_\kappa(H)}
\]

로 정의하면 \(\|r(t_n)\|_1\le V_n\)이다. 시간가변 \(G_n\)에서도 반복해 유효하다. 모든 \(\tau\in[0,H)\)에 대해

\[
\|r(t_n+\tau)\|_1\le e^{-\kappa\tau}V_n+G_n\Psi_\kappa(\tau)
\le V_n+G_nH.
\]

블록 내부와 오른쪽 끝에는 각각 이 within-block bound와 \(V_{n+1}\)를 사용한다.

유리수 구현이 저장하는 수열은 별도로 \(\widehat U_0=U_0\)라 두고, \(e^{-a}\le1/(1+a)\), \(\Psi_\kappa(H)\le H\)를 사용해

\[
\boxed{\widehat U_{n+1}=\frac{\rho}{1+\kappa H}\widehat U_n+G_nH,
\qquad \widehat U_n^*=\widehat U_n+G_nH}
\]

로 정의한다. 비음수 초기값과 같은 \(G_n\) 아래 \(V_n\le\widehat U_n\), \(\|r(t_n)\|_1\le\widehat U_n\)이고, 모든 \(\tau\in[0,H]\)에서 \(\|r(t_n+\tau)\|_1\le\widehat U_n^*\)이다. 이 두 저장값은 서로 다른 시간 범위를 인증한다. `forced_step`의 `endpoint["U"]`와 `whole_block["U"]`가 이 식에 대응한다.

더 조밀한 지수함수 구간을 이미 계산했다면 \(e_-\le e^{-\kappa H}\le e_+\)에서

\[
\Psi_\kappa(H)\le\min\{H,(1-e_-)/\kappa\}\quad(\kappa>0)
\]

를 사용할 수 있다. 실제 생산 코어는 위 단순 유리수 갱신을 채택하므로 \(\kappa=0\)에서 나눗셈 특이점이 생기지 않는다.

### 4.2 상수 forcing의 명시적인 transient/ultimate bound

\(G(t)\le G\), \(q=\rho e^{-\kappa H}<1\)이면 해석적 수열은

\[
V_n=q^nU_0+G\Psi_\kappa(H)\frac{1-q^n}{1-q},
\qquad\|r(t_n)\|_1\le V_n.
\]

\(t=nH+\theta\), \(0\le\theta<H\)에서 convolution kernel의 적분은 정확히

\[
J(t)=\Psi_\kappa(H)\sum_{k=0}^{n-1}q^k+q^n\Psi_\kappa(\theta).
\]

따라서 \(\|r(t)\|_1\le e^{-\kappa t}\rho^nU_0+GJ(t)\)이다. \(\kappa=0\)이어도 \(\rho<1\)이면 블록 끝에서 \(GH/(1-\rho)\)가 유한한 ultimate bound이다. \(q=1\)인 비수축 경계에서는 geometric quotient 대신 \(n\)을 사용한다. \(\rho=0\)일 때 \(0^0=1\)은 homogeneous zero-block convention으로 둔다.

유리수 저장 수열에는 자신의 계수 \(\widehat q=\rho/(1+\kappa H)\)를 사용한다. 상수 \(G\)와 \(\widehat q<1\)일 때

\[
\widehat U_n=\widehat q^nU_0+GH\frac{1-\widehat q^n}{1-\widehat q}.
\]

\(\widehat q=1\)이면 \(\widehat U_n=U_0+nGH\)이다. 이 식은 `forced_step`이 선택한 보수적인 수열의 닫힌 형식이다. 위 \(V_n\) 식은 실제 잔차의 해석적 상계이며, 더 큰 \(\widehat U_n\) 자체를 그 식으로 상계한다는 진술은 사용하지 않는다.

## 5. R5 삼각 비교계와의 결합

R5의 positive-system 조건을 명시적으로 유지한다. \(x_0\ge0\), \(f(t)\ge0\), \(h(t),d_j(t)\ge0\)이고 \(\pi(t)\)는 simplex 값의 국소 절대연속 함수이다. 전체계와 coarse total equation에는 **같은 prescribed \(F(t)=\mathbf1^Tf(t)\)**를 사용한다. 초기 비교값 \(M_0,\widehat U_0,E_0\)와 상한 \(q_c,g,F_+,s_+\)는 모두 비음수이다.

\(X\le M\), \(\|r\|_1\le\widehat U\), \(|X-\bar X|\le E\)로 두고, 한 블록 전체에서 거의 모든 시간에

\[
0\le k\le h\min d,\quad 0\le b\le h\bar d,\quad
\|c\|_1\le q_c,\quad\|Qf\|_1\le g,
\quad F\le F_+,\quad h\,\operatorname{osc}(d)/2\le s_+
\]

가 성립한다고 하자. 이 전제는 \(1+kH,1+bH,1+\kappa H\ge1\)도 보장한다. 그러면

\[
M_n^*=M_n+F_+H,\quad G_n=q_cM_n^*+g,
\quad M_{n+1}=M_n/(1+kH)+F_+H
\]

와 4절의 endpoint \(\widehat U_{n+1}\), whole-block \(\widehat U_n^*\)를 함께 사용한다. \(M\)의 damping \(k\)와 잔차의 분리 damping \(\kappa\)는 각각 다른 비교량에 적용된다. 잔차의 전파자에는 3절에서 분리한 killing을 한 번 적용한다.

Total discrepancy는 \(E'\le-bE+s_+\|r\|_1\)인 비교계로 제어된다. 위 within-block envelope를 적분하면

\[
\int_0^H\|r(t_n+\tau)\|_1d\tau
\le H\widehat U_n+\tfrac12G_nH^2.
\]

따라서 전부 유리수인 안전한 저장값은

\[
\boxed{E_{n+1}=\frac{E_n}{1+bH}
+s_+\left(H\widehat U_n+\tfrac12G_nH^2\right),\qquad
E_n^*=E_n+s_+\left(H\widehat U_n+\tfrac12G_nH^2\right).}
\]

이 식은 forcing convolution에서 \(E\)의 damping을 버려 상계하고 homogeneous \(E_n\) 부분에만 rational damping을 적용한 것이다. 적분에는 블록 내부의 선형 상계를 사용한다. \(\kappa>0\)이면 더 조밀한 잔차 면적 \(\widehat U_n\Psi_\kappa(H)+G_n[H-\Psi_\kappa(H)]/\kappa\)도 가능하지만, 현재 생산 코어는 특수분기 없는 위 유리수 식을 사용한다.

고정 온도에서 동일 Gibbs ratio로 \(K\pi=0\), \(\dot\pi=0\)를 보장한다면 \(q_c=h\|D\pi-\pi\bar d\|_1\le h\operatorname{osc}(d)/2\)이다. 마지막 부등식은 구간에 놓인 확률변수의 평균 절대편차가 구간 폭의 절반 이하라는 사실에서 나온다. 이 선택적 개선은 실제 \(d,h\) 입력이 있을 때 수치화한다.

## 6. 적용 조건, 종료 조건, 심사 항목

이 결과는 정상상태 근사, 물리적 파괴율 복원, source 밖의 온도 보간, chemical Q의 추정, production 승인 또는 새로운 강한 no-go를 뜻하지 않는다. 최소한 다음 항목을 분리해 기록한다.

1. **수학 상태:** 1–5절의 조건부 직접 유도. Dobrushin, uniformization, softmax 단조성은 문헌의 표준 결과이며 새로운 발견이라고 주장하지 않는다.
2. **원천 상태:** native 에너지 decimal literal과 100 K 제공 rate graph에 대한 mathematical closure. 미제공 transition과 GL2022 destruction array는 미입력이다.
3. **구현 상태:** `src/interval_block.py`와 `verification/run_primary.py`가 해당 연산과 고정 입력을 제공한다. 실제 실행 상태와 결과 identity는 `EXECUTION_LEDGER.json` 및 `raw/`가 관리한다.
4. **검증 상태:** exact rational 계산, source parsing, lower-bound 방향, interval nesting, block endpoint/whole-block 구분, common-killing 분리를 서로 독립적으로 확인한다. 단순 재실행은 독립 증명이 아니다.
5. **종료 상태:** 새 의무의 certificate를 얻으면 미입력 물리값을 채우기 위해 무제한 검색하거나 옛 suite를 반복하지 않는다. 실제 source/consumer 바인딩이 나올 때 다음 물리 의무를 연다.

독립 심사자는 특히 (a) column convention, (b) \(R_N\le\Phi\)의 시간 순서, (c) \(\rho\)를 순간 gap으로 오인하지 않았는지, (d) \(A\) 전체 exit 상한, (e) \(U_{n+1}\)와 whole-block envelope 구분, (f) literal precision과 물리적 measurement uncertainty 구분을 점검해야 한다.

## 7. 문헌 읽기 수준

- Wei et al. (2023): primary PDF 추출문에서 section 2/2.1 및 eqs. (2), (5), (6)를 실제 읽음. 더 강한 nonlinear convex bounds는 이번 알고리즘에 채택하지 않음.
- van Dijk (1991): VU primary repository PDF의 model section, section 3/Theorem 1, ordered-product Poisson representation을 실제 읽음. OCR 수식 일부가 손상되어 최종 열벡터 수식은 위 직접 유도로 재구성함.
- Gaubert–Qu (2015): 저자 PDF의 introduction, zero-sum induced norm, Doeblin common-mass 설명 및 Theorem 1.1을 읽음. 전체 논문의 모든 정리를 검증했다는 주장은 하지 않음.
- BIPM defining constants: primary HTML 표 전체를 읽음. NIST Planck page도 정확값을 확인했으나 k/c 개별 fetch는 숫자를 반환하지 않아 근거로 사용하지 않음.
- GL2022 IFF-CSIC: 새 기관 publication page의 반환된 전체 본문을 읽음. 논문 범위를 확인했지만 수치 파괴율 배열이나 download manifest는 반환문에 없음. 이 관측은 전 세계 데이터 부재를 입증하지 않음.


## 8. Dyadic 생산 구현의 하한 방향

생산 코어의 `finite_block`은 \(S=2^p\)와 \([x]_-:=\lfloor Sx\rfloor/S\)를 사용한다. `uniformization_lower`가 만든 정확한 유리수 \(P_-\)를 \(\widetilde P=[P_-]_-\)로 낮추고,

\[
M_0=I,\qquad M_{m+1}=[M_m\widetilde P]_-,
\quad w_0=[e_-]_-,\qquad
w_{m+1}=[w_m\mu/(m+1)]_-,\quad\mu=\lambda H
\]

로 계산한다. 정수 행렬에서는 곱의 성분별 dot product 전체를 더한 뒤 한 번 `// S`를 적용한다. 비음수 행렬곱의 단조성으로 귀납하면

\[
0\le M_m\le P_-^m,\qquad
0\le w_m\le e_-\mu^m/m!.
\]

최종 저장 행렬은

\[
\widehat R_N=\sum_{m=0}^N[w_m M_m]_-
\le R_N\le\Phi_A(s+H,s).
\]

합산된 항을 뺄 일이 없으므로 같은 한 번의 계산에서 추적한 partial overlap은 차수에 따라 감소하지 않는다. 일부 매우 작은 항이 0으로 반올림되어도 하한 방향은 유지된다. 그 영향은 \(\beta\)가 작아져 덜 강한 certificate가 되는 것으로 나타난다. `finite_block`은 양의 수축이 검증되었다고 추정하는 대신 실제 \(\beta\)를 반환한다.

`exp_neg`는 \(y\le1/2\)로 range reduction한다. 정확한 odd/even Taylor 부분합을 먼저 구한 뒤, 정수 하한 \(l\)과 상한 \(u\)에

\[
l\leftarrow\lfloor l^2/S\rfloor,\qquad
u\leftarrow\lceil u^2/S\rceil
\]

를 적용한다. \(e^{-z}\le1\)이므로 상한은 필요할 때 \(S\)로 잘라도 유효하다. `threshold=2^{-(p+16+s)}`는 초기 Taylor 차수 선택에 쓰는 계산량 기준이고, 최종 error certificate는 거듭제곱 이후의 **실제 두 유리수 endpoint**이다. 코드가 `threshold`를 최종 interval width로 보고하는 일은 없다.

입력 범위는 \(1\le n\le9\), \(0\le N\le512\), \(128\le p\le768\), \(0\le z\le256\), \(0<\lambda H\le256\)이다. Native source에는 thermal \(p=256\), polynomial \(p=512\)를 선택한다. 더 낮은 정밀도에서 positive exponential의 lower endpoint가 0이 될 수 있다. 지수함수 구간 자체는 유효하지만, `normalize_weights`는 엄밀히 양의 weight lower bound를 요구하므로 그런 normalized input은 명시적으로 거절한다.

\(n=1\)에서는 zero-sum 공간이 \(\{0\}\)이다. `_overlap_integer`는 이 경우 \(\beta=1,\rho=0\)을 **zero-space convention**으로 반환한다. 이는 \(\widehat R_N\)의 단일 column mass가 1이라는 주장이 아니며, 일반 \(j<k\) 공통 질량의 빈 최솟값을 계산하지 않는다. \(n\ge2\)에서는 실제 저장 행렬의 pair overlap을 그대로 사용한다.

## 9. 원천 단위와 코드 경계

`native_hd_source`는 고정 SHA-256의 LAMDA bytes와 고정 REC parser를 읽고, `parse_hd`의 원문 decimal literal만 사용한다. 파수의 \(\mathrm{cm}^{-1}\to\mathrm m^{-1}\) 변환 인자는 100이고, `thermal_from_levels`의 exponent는 정확히

\[
z_i=\frac{100h_{\rm P}c_{\rm light}(\widetilde\nu_i-\widetilde\nu_0)}{k_BT}.
\]

코어 상수 `H_PLANCK`, `C_LIGHT`, `K_BOLTZMANN`은 1절의 SI 정의값을 유리수로 저장한다. 생산 parser의 binary64 `upward_rate`는 호출하지 않는다. Native 100 K의 downward coefficient를 \(\kappa_{\rm ref}=10^{-11}\,\mathrm{cm^3/s}\)로 나누어 무차원 \(K\)를 만들고, reverse edge에는 `pair_ratio`의 직접 구간을 곱한다. 물리 시간과의 대응은 \(\tau=n_{\rm coll}\kappa_{\rm ref}t\)이며 density가 아직 입력되지 않았으므로 certificate는 무차원 clock으로 제공한다.

`GeneratorBox`는 각 column의 lower diagonal을 minus upper exit, upper diagonal을 minus lower exit로 묶는다. `reset_generator_bounds`는 \(\pi\)의 simplex 구간과 \(v_j^-\ge\kappa\)를 확인하고 3절 전체 \(A\)의 비대각 구간을 구성한다. 코드는 보수적인 비대각 상한 합을 exit 상한으로 사용한다. 3절의 optional simplex-improved exit는 현재 구현에 채택하지 않았다.

`forced_step`의 `k_lower`, `b_lower`, `q_upper`, `g_upper`, `s_upper`, `F_upper`는 5절의 \(k,b,q_c,g,s_+,F_+\)이다. 내부 키 `U`는 \(\widehat U\)를 뜻한다. 입력은 모두 비음수이고 \(H>0,\rho\in[0,1],\kappa\ge0\)이어야 한다. 이 scalar 함수는 외부 모델의 구간 전체 유효성이나 \(\rho\)의 generator identity를 스스로 확인할 수 없으므로, 호출자는 그 입력 provenance와 block length를 함께 보존한다. 고정 synthetic fixture는 실제 전체 \(A\)에서 만든 certificate와 같은 \(H\)를 export한다.

실제 상태별 파괴율, source의 미제공 채널, source 밖 온도 보간, 물리 density 및 named consumer는 `CONTRACT.json`의 입력 경계에 남는다. 이번 코드의 실행 가능한 새 기여는 literal thermal enclosure와 finite-block forced certificate의 연결이다.
