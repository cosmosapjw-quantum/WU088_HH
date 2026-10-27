# R5 독립 수학 검토

검토자: /root/r5_primary_sources. 날짜: 2026-10-27.
이 문서는 새로운 과학 실행 없이 기존 독립 유도 및 검토를 보존한다. 강한 신규성·no-go 주장을 하지 않는다.

## Dynamic closure: ACCEPT

x'=Kx-hDx+f, D=diag(d), K는 column-conservative Metzler, x(0),f,d,h>=0.
pi>=0, 1^T pi=1, Q=I-pi1^T, X=1^Tx, r=x-pi X, dbar=d^Tpi,
b=Dpi-pi*dbar, beta=||b||1.

고정 stationary pi에 대해 정확히
r'=[K+hB]r-hbX+Qf, B=pi*d^T-D.
B는 column-conservative Metzler: 1^TB=0, B_ij=pi_i*d_j>=0 (i!=j).
따라서 state-dependent killing의 r 선형항은 generator contraction으로 처리된다.

delta(L)=min_(i!=j)[L_ij+L_ji+sum_(k!=i,j) min(L_ki,L_kj)].
Zero-sum 공간에서 ||exp(Lt)z||1<=exp(-delta(L)t)||z||1.
이는 작은 epsilon의 column-stochastic I+epsilon L에 대한 column-overlap 계수와 semigroup product limit에서 따른다.

a=delta(K+hB)를 직접 쓸 수 있다.
prefactor-one zero-sum L1 contraction alpha_K가 실제 제공된 경우
a>=alpha_K+h*delta(B)를 쓸 수 있다.
delta(B)=min_(i!=j)[pi_i*d_j+pi_j*d_i+(1-pi_i-pi_j)min(d_i,d_j)]>=dmin.
단순 spectral gap 또는 C exp(-alpha t), C>1를 alpha_K로 대입하면 안 된다.

M'=-h*dmin*M+F, M(0)=X(0), F=1^Tf;
U'=-a*U+h*beta*M+||Qf||1, U(0)=||r(0)||1;
E'=-h*dbar*E+h*omega*U, E(0)=|X(0)-Xbar(0)|;
omega=(dmax-dmin)/2, Xbar'=-h*dbar*Xbar+F.
그러면 X<=M, ||r||1<=U, |X-Xbar|<=E.
입력 f가 state-dependent이면 동일 prescribed F 사용 또는 별도 forcing bound를 계약해야 한다.

d->d+c1이면 B|zero_sum->B|zero_sum-cI이며 beta와 osc(d)는 불변이다.
시간 의존 pi에 대해서는 정확한 forcing 계수가
c=Kpi-pi_dot-h(Dpi-pi*dbar)이며 U forcing에 ||c||1 M+||Qf||1를 쓸 수 있다.
Kpi residual과 pi_dot를 누락하면 안 된다.
h=0 또는 d constant이면 matching initial total에 대해 aggregate closure는 정확하다.
n=1의 경우 r=0. Zero damping은 적분형으로 처리하며 0으로 나누지 않는다.

## Rational endpoint step: ACCEPT

연속 비교계 M'=-kM+F, U'=-aU+qM+g, E'=-bE+sU.
M,U,E,k,a,b,F,q,g,s>=0이며 step 동안 계수는 상수이고 dt>=0.
Mstar=M+Fdt, C=qMstar+g, Ustar=U+Cdt.
Mplus=M/(1+kdt)+Fdt;
Uplus=U/(1+adt)+Cdt;
Eplus=E/(1+bdt)+sUstar dt.

0<=tau<=dt에서 M(tau)<=Mstar, U(tau)<=Ustar.
Variation of constants와 exp(-z)<=1/(1+z), forcing integral<=dt*sup(forcing)로
세 plus 값이 step 끝점에서 연속 비교해의 상계임을 얻는다.
Update map은 비음수 시작 상태에 대해 단조이므로 여러 step을 연결할 수 있다.
dt=0은 identity이고, Taylor expansion은 vector field와 O(dt^2)까지 일치하므로 1차 일관성이 있다.
입력과 dt가 유리수이면 위 연산은 정확한 유리수 연산으로 구현 가능하다.
이 산술 성질은 source uncertainty나 실제 물리 오차에 대한 interval certificate가 아니다.

범위 교정:
1. plus 값은 endpoint bounds다. 전체 step 구간에는 Mstar,Ustar,Estar=E+sUstar dt를 사용할 수 있다.
2. 시간 의존 계수에는 damping k,a,b의 구간 LOWER bounds,
   forcing/coupling F,q,g,s의 구간 UPPER bounds가 필요하다.
3. 이 lemma 검토를 위한 새 numerical execution은 0회다.

## Sparse graph block minorization: ACCEPT

고정 column-conservative Metzler K에 대해 lambda=2 max_j(-K_jj)>0,
P=I+K/lambda, states 0,...,8. P는 column-stochastic이고 P00>=1/2.
각 j에 대해 j->j-1->...->0 후 0에서 대기하는 길이 8 path가 모두 양수라면
eta_j=(product_(k=1,...,j) P_(k-1,k))*P00^(8-j)>0,
eta=min_j eta_j>0이며 (P^8)_(0,j)>=eta_j.
모든 column의 row0 공통 질량으로 tau(P^8)<=1-eta.

t0=8/lambda에서 uniformization의 m=8 항만 이용하면
||exp(Kt0)z||1 <= [1-eta*exp(-8)*8^8/8!]*||z||1
<= [1-eta*8^8/(3^8*8!)]*||z||1, 1^Tz=0,
왜냐하면 e<3이다.

이것은 고정 연산자의 block contraction이다. prefactor-one instantaneous rate a로 승격할 수 없다.
여러 block에는 rho^floor(t/t0) bound를 사용할 수 있다.
Root가 보고한 41개 source-geometry 검사 및 CAS 결과는 이 검토에서 재실행하지 않았다.
Source scope는 제공된 9개 edge, 명시된 rational thermal weights 및 연산자 구성에 한정된다.
누락 전이의 물리적 0, 실제 collider density/physical time, GL2022 destruction 완성을 주장하지 않는다.

## Prototype evidence

원래 JavaScript V8 binary64 두 상태 closed-form 검산:
K=[[-1,2],[1,-2]], pi=(2/3,1/3), d=(1,4), h=1, x0=pi.
f=0 및 f=(1,0), t={0,.05,.2,.5,1,2,4}; positivity, X<=M, ||r||1<=U, |e|<=E,
총 56/56 PASS. 이 값들은 물리율과 결속하지 않은 무차원 fixture다.
원 code/result/provenance는 인접 verification files에 보존한다.
모든 시간에 대한 근거는 comparison proof이며 유한 표본 검산을 증명으로 승격하지 않는다.
