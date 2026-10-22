# PHYS80 조건부 정확 축약: PHYS79 C01의 22상태 → 4상태

## 1. 결과·적용 조건·읽은 근거

PHYS79 C01의 연속 방정식은 아래 조건에서 **4개 동적 좌표 `(Q,v,h,l)`와 고정된 보존량으로 정확히 재구성된다.** 이는 QSS나 rate 변경이 아니다. D CX-only는 `Q,h,l`이 일정하므로 1차원으로 줄어든다. analytic Jacobian, rate derivative, 21 species RHS 복원, electron·particle·binding·thermal chain의 symbolic residual을 실제 Wolfram 도구로 검산했다. 본 단위에서는 새 ODE·완료 identity 재실행·local numerical test를 수행하지 않았다.

읽은 실제 파일은 `/tmp/hh_phys79_work/WU088_HH/research/hh_phys79_collisional_closure_20261022/`의 `source/collisional.py`, `source/run_controls.py`, `CONTRACT.json`, `inputs/CONTROL_PLAN.json`, pinned `vendor/phys78/source/atomic_network.py`다. 부모가 새로 actual-ref 대조한 PR134 HEAD는 `3304d16db1dc9bf868c185a8eeb6cc9dbc270e50`이다. 이 문서는 부모의 원격 조회를 재사용하며 별도의 원격 전수조사를 주장하지 않는다.

정확 축약의 조건은 다음과 같다.

- active CI row는 `(0,1,3)`: H1/D/T I→II, He3/He4 I→II, Li6/Li7 I→II. isotope별 CI는 원소 rate를 공유한다.
- D CX는 D I+H1 II ⇌ D II+H1 I뿐이다. 선언된 `detailed_balance` 모델을 그대로 쓴다.
- T와 neutron 재고는 0. He III, Li III/IV 초기 population은 0이고 이를 생성하는 row는 활성화하지 않는다.
- He3/He4의 초기 II fraction은 같고 Li6/Li7의 초기 II fraction도 같다. C01은 각각 0.01이다. 실제 binary IC의 미세 반올림을 보존하는 일반화는 §7에 별도로 제시한다.
- 고유밀도 `n=n_H`가 일정하고 Hubble expansion, PI/RR, 외부 열 bath, radiation energy loss가 없다. reacting gas는 단일 온도의 비상대론적 isotropic 이상기체다.

non-tilted LRS Bianchi I와 `(-,+,+,+)`, normal orthonormal frame, gas `pi=0`, collisionless DM의 `pi_m` 소유권은 그대로다. 이 축약은 새 우주론 admission이 아니다. `HH_R10=OFF`, production admission `NOT_ISSUED`.

## 2. 보존량과 복원 지도

기준 H1 핵당 isotope 재고를 `A`(H1), `D`(deuterium), `B3,B4`(He), `L6,L7`(Li)라 하고

\[
B=B_3+B_4,\quad L=L_6+L_7,\quad N_{\rm nuc}=A+D+B+L
\]

로 쓴다. 실제 계약의 재고는 pinned IC에서 읽는다. H1=1, D=`2.460e-5`, He3=`1.074e-5`, Li6=`1.20e-14`, Li7=`5.627e-10`이며 He4는 pinned mass-fraction 환산값이다. 새 상수로 다시 추정하지 않는다.

좌표는

\[
Q=Y_{\rm HII}+Y_{\rm DII},\qquad v=Y_{\rm DII},\qquad
h=Y_{{\rm He3II}}/B_3=Y_{{\rm He4II}}/B_4,\qquad
l=Y_{{\rm Li6II}}/L_6=Y_{{\rm Li7II}}/L_7.
\]

복원식은

\[
\begin{aligned}
Y_{\rm HI}&=A-Q+v,&Y_{\rm HII}&=Q-v,\\
Y_{\rm DI}&=D-v,&Y_{\rm DII}&=v,\\
Y_{{\rm He}j\rm I}&=B_j(1-h),&Y_{{\rm He}j\rm II}&=B_jh\quad(j=3,4),\\
Y_{{\rm Li}j\rm I}&=L_j(1-l),&Y_{{\rm Li}j\rm II}&=L_jl\quad(j=6,7).
\end{aligned}
\]

T·neutron와 나머지 higher-charge 슬롯은 정확히 0으로 복원한다. 각 isotope 합은 입력 재고와 같다. 전자와 총 입자수는

\[
x_e=Q+Bh+Ll,\qquad N=N_{\rm nuc}+x_e.
\]

### fraction equality와 비활성 슬롯의 증명

같은 원소의 두 isotope fraction `f_i,f_j`는 동일한 순간 `T,x_e`에서

\[
\dot f_i=n k(T)x_e(1-f_i),\quad
\frac{d}{dt}(f_i-f_j)=-n k(T)x_e(f_i-f_j)
\]

를 만족한다. 따라서 초기 차이 0이면, source domain 안에서 유일해의 차이는 모든 시간에 0이다. `T,x_e`가 두 isotope의 합에 의존해도 차이식은 변하지 않는다. He/Li equality는 rate·IC 조건에서 나온 불변부분공간이다.

비활성 higher-charge 슬롯에는 active stoichiometric row가 없으므로 derivative가 0이다. T는 neutral CI가 선택되어 있어도 두 T 슬롯이 모두 0인 상태에서 flux가 0이고 생성 source가 없다. neutron도 inert다. 이 증명은 추가 nuclear source나 higher CI를 켠 모델로 자동 확장되지 않는다.

## 3. 공통 ionic potential과 안정적인 에너지 복원

실제 `ionic_potential_eV()`의 neutral-ground potential을 쓴다.

\[
I_H=13.6\ {\rm eV},\quad I_{He}=24.59\ {\rm eV},\quad
I_{Li}=5.392\ {\rm eV},\quad \delta=I_D-I_H.
\]

Voronov rate의 fitted `dE`인 He 24.6 eV, Li 5.4 eV와 이 thermal potential을 혼동하지 않는다. 이론 모델은 `δ=43 k_B K`를 선언한다. **기존 binary 구현과 같은 방정식을 재구성할 때는 저장된 실제 `ε[DII]−ε[HII]`를 `δ_eff`로 사용한다.** round-to-nearest로 저장한 `I_H+43k_B K`에서 차를 취한 값과 별도로 계산한 `43k_B K`는 마지막 bit가 다를 수 있다. DB rate exponent는 원래 코드대로 43 K를 유지한다. 이 수치 상수 차이를 몰래 교정하여 parent identity를 바꾸지 않는다. 아래 식의 `δ`는 해당 구현의 실제 potential difference다.

양의 ionic energy는

\[
b=I_H Q+\delta v+I_{He}Bh+I_{Li}Ll.
\]

CI/CX의 no-radiation event ledger로 `u̇=−ḃ`이므로 `E=u+b`가 일정하다. 따라서 22번째 상태인 `u`를 다음과 같이 복원한다.

\[
\boxed{u=u_0-I_H(Q-Q_0)-\delta(v-v_0)
-I_{He}B(h-h_0)-I_{Li}L(l-l_0).}
\]

이는 `E−b` 또는 `u0−ε·(Y−Y0)`와 같은 실수식이다. 계산에서는 **grouped energy defect의 합**을 `math.fsum` 등으로 누적한다. 큰 H/D potential을 다시 빼서 작은 D isotope heat를 얻는 직접 state dot product를 authoritative 경로로 쓰면 PHYS79 F2 conditioning 문제가 다시 들어온다. 특히 D-only는 `u=u0−δ(v−v0)`로 단순해진다.

\[
c_V=\frac32k_B,\qquad T=\frac{u}{c_VN}.
\]

단위는 eV/H1, eV/K, K, cm⁻³, cm³/s, proper s다. 화학 변화에 따른 전자수 효과는 이 분모에 이미 포함된다. `u` 식에 별도 `3k_BT/2` 항을 다시 넣지 않는다.

## 4. 정확한 4D RHS와 physical/source domain

\[
k=k_{\rm HI,CI}(T),\quad g=k_{\rm HeI,CI}(T),\quad
j=k_{\rm LiI,CI}(T),\quad f=k_{\rm CX,f}(T),\quad r=k_{\rm CX,r}(T).
\]

`x=x_e`, `P=A+D−Q`, `a=D−v`, `b_H=Q−v`, `c_H=A−Q+v`와

\[
Z=f a b_H-r v c_H
\]

를 사용하면

\[
\boxed{
\begin{aligned}
\dot Q &= n kxP,\\
\dot v &= n\{kx a+Z\},\\
\dot h &= n gx(1-h),\\
\dot l &= n jx(1-l).
\end{aligned}}
\]

CX는 H와 D의 charge를 서로 옮기므로 Q에 기여하지 않는다. 이 네 식과 §2의 복원 지도를 미분하면 원래 21개 species derivative가 모두 복원된다. 복원한 `ḃ=I_H Qdot+δ vdot+IHe B hdot+ILi L ldot`는 원래 CI 7개와 CX 두 방향의 event-defect 합이다. 따라서 `u̇`와 `Ṫ=−ḃ/(c_VN)−T ẋ_e/N`도 원래 방정식과 같다. Wolfram에서 21개 reconstruction residual과 나머지 energy/charge residual을 정확한 0으로 확인했다.

physical 영역은

\[
0\le Q\le A+D,\quad \max(0,Q-A)\le v\le\min(D,Q),\quad
0\le h,l\le1.
\]

`v=0`에서는 `vdot=nD(kx+fQ)≥0`; `v=D`에서는 `vdot=−nrD(A−Q+D)≤0`이다. `Q−v=0`에서 HII derivative는 `nA(kx+rv)≥0`; `A−Q+v=0`에서 HI derivative는 `nfA(D−v)≥0`이다. `h,l=0`에서 inward, `h,l=1`에서 derivative0이다. 이 inward-vector-field 조건과 smoothness/uniqueness는 연속 해의 비음 영역 불변성을 준다. 수치 Newton stage의 비음성 보장은 별개의 문제다.

C01 source intersection은

\[
T_{\min}=1\ {\rm eV}/k_B,\qquad T_{\max}=200000\ {\rm K}.
\]

CI 자체의 상한20keV보다 D CX의 상한200000K가 더 엄격하다. 실제 유효영역은 위 physical 영역에

\[
c_VT_{\min}N\le u\le c_VT_{\max}N
\]

를 교차한 집합이다. `u,N`이 좌표의 affine 함수이므로 이 source-domain 조건도 affine inequality다. source-domain 전체가 동역학적으로 불변이라는 증명은 하지 않았다. trajectory가 source 경계를 만나면 source closure가 필요하며 extrapolation·zero-fill로 넘기지 않는다.

## 5. analytic Jacobian — 열 의존성을 포함한 rank-one 형식

좌표순서는 `y=(Q,v,h,l)`다. 행벡터를

\[
d=(1,0,B,L),\quad e=(I_H,\delta,I_{He}B,I_{Li}L)
\]

로 두면

\[
\boxed{\nabla_yT=-\frac{e+c_VT d}{c_VN}.}
\]

고정 T에서의 미분을 `M`, 온도 미분을 `w`라 하면

\[
\boxed{J_y=n\left[M+w\otimes\nabla_yT\right]}
\]

이며

\[
M=\begin{pmatrix}
k(P-x)&0&kPB&kPL\\
ka+fa+rv&-kx-f(a+b_H)-r(c_H+v)&kaB&kaL\\
g(1-h)&0&g\{B(1-h)-x\}&gL(1-h)\\
j(1-l)&0&jB(1-l)&j\{L(1-l)-x\}
\end{pmatrix},
\]

\[
w=\begin{pmatrix}
k' xP\\
k' xa+f'ab_H-r'vc_H\\
g'x(1-h)\\
j'x(1-l)
\end{pmatrix}.
\]

prime는 K 단위 온도로 미분한 rate derivative다. 특히 `T_v=−δ/(c_VN)`은 작지만 0이 아니다. 이를 제거하면 D closed-energy thermal coupling이 달라진다. `T_Q,T_h,T_l`의 particle-number 부분도 생략하지 않는다.

### 실제 rate derivative

Voronov의 `U=dE/(k_BT)`와

\[
k_{CI}=A_0\frac{1+P_0\sqrt U}{X+U}U^K e^{-U}
\]

에 대해

\[
\boxed{\frac{dk_{CI}}{dT}=
\frac{k_{CI}}{T}\left[
U+\frac{U}{X+U}-K-\frac{P_0\sqrt U}{2(1+P_0\sqrt U)}\right].}
\]

현재 neutral row의 `P0=0`이면 마지막 항이 0이다. derivative에도 원래 rate의 domain guard를 적용한다.

Savin reverse를 `r=r1+r2`로 쓰면

\[
r_1=2.06\times10^{-10}T^{0.396}e^{-33/T},\quad
r_2=2.03\times10^{-9}T^{-0.332},
\]

\[
\boxed{r'=r_1\left(\frac{0.396}{T}+\frac{33}{T^2}\right)
-\frac{0.332}{T}r_2,\qquad
f'=e^{-43/T}\left(r'+\frac{43}{T^2}r\right).}
\]

세 derivative와 `J_y`의 16개 성분은 독립 symbolic differentiation과 일치했다. raw forward fit을 선택하는 다른 closure에는 위 `f'`를 전용하지 않는다.

### solver 좌표와 시간 변환

부모의 solver 좌표는 `z=(Q/(A+D),v/D,h,l)`다. `S=diag(A+D,D,1,1)`, `y=Sz`와 `θ=n k_ref t`에 대해

\[
\boxed{\frac{dz}{d\theta}=\frac{S^{-1}F(Sz)}{n k_{ref}},\qquad
J_z=\frac{S^{-1}J_yS}{n k_{ref}}.}
\]

정규화가 ODE를 바꾸지 않는다. `D=0`이면 이 scaling을 쓰지 말고 별도 degenerate network를 선택해야 한다. 현재 재고 D>0이다. 새 solver의 finite tolerance가 parent 22-state tolerance와 자동으로 같은 global error를 보장하지는 않으므로 저장 parent trajectory와 고정 gate 비교가 필요하다.

## 6. D-only scalar flow와 유일 평형

D CX-only에서는 `Q=Q0,h=h0,l=l0,x,N`이 일정하다. `v` 하나만 움직이며

\[
T(v)=T_0-\gamma(v-v_0),\qquad \gamma=\frac{\delta}{c_VN}>0,
\]

\[
\dot v=n r(T(v))G(v),\quad
G(v)=K(v)(D-v)(Q_0-v)-v(A-Q_0+v),\quad K(v)=e^{-43/T(v)}.
\]

physical interval은 `v−=max(0,Q0−A)`, `v+=min(D,Q0)`이다. `A,D>0`, `0<Q0<A+D`이고 이 구간의 온도가 source domain2.7–200000K 안에 있다고 가정한다. `G(v−)>0`, `G(v+)<0`이다. 도함수는

\[
\boxed{G'(v)=
-K\{(D-v)+(Q_0-v)\}
-\{(A-Q_0+v)+v\}
-K(D-v)(Q_0-v)\frac{43\gamma}{T(v)^2}<0.}
\]

따라서 구간 내부의 평형 `v*`가 유일하고, `v<v*`이면 증가, `v>v*`이면 감소한다. `V=(v−v*)²/2`는 평형 밖에서 `Vdot<0`이다. 양의 bounded rate와 compact source interval에서 해는 평형으로 단조 접근한다. 안정성은 `G'<0`에서 나오며, **전체 `F'(v)`가 모든 v에서 음수라고 별도로 가정하지 않는다.**

scalar analytic Jacobian은

\[
\boxed{F_v=n\left[-\gamma r'(T)G+r(T)G'\right].}
\]

평형에서는 `F_v(v*)=n r(T*)G'(v*)<0`이다. solver가 `d=v/D`를 쓰면 `dd/dt=F(Dd)/D`이고 그 도함수는 `F_v`; `θ`에서는 다시 `n k_ref`로 나눈다. `Q0=0` 또는 `Q0=A+D`는 반응할 수 없는 singleton interval이다. source restriction이 physical interval을 잘라 평형을 제외하는 경우에는 admitted equilibrium의 존재를 주장하지 않는다.

평형 root만 구하는 `brentq`는 finite-time flow가 아니다. 실제 finite-time scalar flow는

\[
t-t_0=\frac1n\int_{v_0}^{v(t)}\frac{ds}{r(T(s))G(s)}
\]

의 단조 역함수로 쓸 수 있다. 평형에서 적분은 로그 발산하므로 유한 시간에 근을 강제로 대입하면 같은 물리를 계산한 것이 아니다. quadrature/inversion 방식도 실제 구현에서는 각 오차를 수치 budget에 포함해야 한다.

## 7. 저장 binary IC와 동일 rate의 더 일반적인 불변량

실수 모델에서 초기 He/Li fraction이 같다는 조건은 정확하다. 그러나 원래 runner가 isotope마다 `inventory*fraction`을 binary 연산하면 저장된 `YII/A` 비는 마지막 bit까지 같다고 보장되지 않는다. 이는 새로운 rate model이나 물리 오차가 아니라 representation 문제지만, strict reconstruction claim에는 명시해야 한다.

동일 CI rate에서는 neutral isotope ratio도 정확한 불변량이다.

\[
\frac d{dt}\frac{Y_{i,I}}{Y_{j,I}}=0
\]

따라서 원래 저장 IC의 작은 차이도 동적 차원을 늘리지 않고 보존할 수 있다. `A_i=Y_iI(0)+Y_iII(0)`를 해당 입력의 재고로 두고, `B=ΣA_i`, `h0=ΣY_iII(0)/B`, `w_i=Y_iI(0)/ΣY_iI(0)`라 하면

\[
Y_{i,I}=w_iB(1-h),\qquad Y_{i,II}=A_i-w_iB(1-h).
\]

이때 h는 aggregate HeII fraction이고 같은 4D RHS·electron·energy·Jacobian이 성립한다. Li도 동일하다. 원래 정확한 common-fraction IC이면 `w_i=A_i/B`로 §2에 환원한다. 초기 neutral 합이0이면 해당 원소는 이미 완전히 II이고 h=1로 고정한다. 일반 weights의 physical 하한은 모든 `A_i−w_iB(1−h)≥0`을 만족해야 하므로 단순 h≥0보다 약간 더 엄격할 수 있다. 현재 CI-only의 h는 h0에서 단조 증가하므로 초기 비음 상태로부터 안전한 방향이다.

실제 프로그램은 initial reconstruction, isotope totals, source potentials와 inferred reduced IC를 receipt에 기록해야 한다. 이론적 exactness는 real arithmetic의 ODE 대응이며 bitwise 동일 solver trajectory를 뜻하지 않는다. rounded isotope inventory의 덧셈 오차는 parent tolerance 안에서 확인하되, 그것을 이유로 임의 renormalization을 추가하지 않는다.

## 8. QSS는 향후 조건부 선택

`G(Q,v,h,l)=0`의 근을 `v=Φ(Q,h,l)`로 두어 CX를 즉시 평형에 놓으면 3D로 줄일 수 있지만 이는 **정확한 4D 축약과 다른 approximation**이다. `G_v<0`인 영역에서 implicit function theorem은 `Φ_s=−G_s/G_v`를 준다. 그러나 원래 full RHS가 equilibrium manifold에서 갖는 v 속도는 `n kx(D−Φ)`이고, manifold 자체의 속도는 `∇Φ·(Qdot,hdot,ldot)`다. 두 값의 차이

\[
\mathcal R=n kx(D-\Phi)-\nabla\Phi\cdot F_{\rm slow}(s,\Phi)
\]

는 일반적으로 0이 아니다. C01이 처음 CX equilibrium에 놓여 있어도 이후 CI·냉각이 lag를 만든다.

향후 `e=v−Φ(s)`에 대해 exact error equation `edot=H(s,e)`를 만들고, 허용 tube 안에서 `|H(s,0)|≤R`와 `∂H/∂e≤−λ<0`를 실제로 입증하면

\[
|e(t)|\le |e(0)|e^{-\lambda t}+\frac R\lambda(1-e^{-\lambda t})
\]

형태의 bound를 얻을 수 있다. slow-state coupling에는 별도의 Lipschitz/Grönwall bound가 필요하다. tube invariance·uniform λ·R·source domain·최종 observable error를 확인하기 전에는 단지 CX rate가 더 크다는 이유로 QSS를 대체하지 않는다. 이번 단위는 이 수치 bound를 산출하지 않았으므로 QSS admission은 OPEN이다.

## 9. Radau와 splitting의 계산 계약

**현재 제안은 4D/1D exact coordinate에 analytic Jacobian을 넣은 Radau**다. SciPy1.17.0의 Radau는 implicit Radau IIA5, embedded error estimator 및 collocation dense output을 제공하며 callable Jacobian을 받을 수 있다. [공식 문서](https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.integrate.Radau.html). 기존 trace-rate max-step cap을 그대로 복제할 필요는 없다. 다만 실제 정확도·비음성·source admission·비용 이득은 실행 결과로 판정해야 한다. 이 문서는 speedup 수치를 예측하거나 측정했다고 주장하지 않는다.

먼저 parent의 strict nonnegative-stage guard를 유지하는 구현이 적절하다. implicit Newton trial이 physical polytope 밖으로 나가면 mathematical solution의 positivity가 그 trial을 보장하지 않는다. RHS exception을 SciPy가 자동 step rejection으로 처리한다고 가정하지 않는다. 실제 실패가 발생하면 해당 attempt와 입력·trace를 보존하고 그때 원인에 맞춰 수정한다.

나중에 algebraic trial extension이 필요하면 별도 version/identity/contract에서 선언한다. signed trial coordinate에서 polynomial mass-action 식을 평가하더라도 T·rate source domain, finite 결과 검사는 엄격히 유지한다. clipping/projection으로 바꾸지 않는다. accepted step endpoint와 요청161 dense sample은 물리영역·source·energy gate를 모두 만족해야 한다. 이 경우 `strict_nonnegative_stages`가 보장되는 원래 계약과 같다고 표시해서는 안 된다. 161 sampled check는 전체 collocation polynomial의 positivity certificate가 아니다.

CX subflow는 §6의 1D quadrature로 정확한 흐름을 정의할 수 있다. 그러나 정확한 subflow를 사용해도 finite-step splitting이 full flow와 같지는 않다. 이미 frozen-T H/D-only 예에서 vector field `𝒜=CI`, `ℬ=CX`, `K=f/r`에 대해

\[
[\mathcal A,\mathcal B]_v=n^2 k r\,Q(K-1)(D-v)(A-Q+v)
\]

가 일반적으로 0이 아니다. 이 bracket을 Wolfram으로 확인했다. Lie splitting과 symmetric Strang splitting은 각각 splitting-error 의무가 있고, full thermal coupling은 이를 없애지 않는다. 실제 variable-T CI subflow의 elementary exact solution도 이번에 구성하지 않았다. T/rate를 step 시작값에 고정한 뒤 closed-form map을 쓰면 추가 freeze error가 생긴다. QSS 또는 equilibrium projection을 exact CX time step이라고 부르지 않는다.

따라서 splitting은 별도 오차·비용 증거를 얻을 향후 비교 후보이며 지금 exact reduced Radau의 대체로 승인한 것이 아니다.

## 10. 증거·남은 의무

`WOLFRAM_REDUCTION_RECEIPT.json`은 Jacobian16개, species reconstruction21개 및 electron/particle/binding/energy/temperature-chain의 정확한0을 보존한다. `WOLFRAM_SCALAR_RATES_FIXED_RECEIPT.json`은 rate derivative, scalar G derivative, 동일 CI의 neutral-ratio invariant 및 nonzero splitting bracket을 보존한다. `WOLFRAM_CONTEXT.json`은 주제 변경 시 먼저 호출한 context receipt다. context의 일반 검색 설명을 이론 증명의 근거로 전용하지 않았다.

첫 scalar/rate evaluator 입력의 닫는 괄호 오류는 `WOLFRAM_SCALAR_RATES_RECEIPT.json`과 그 `.wl`에 보존했다. 괄호만 교정한 다음 호출이 실제 대수를 계산했다. 그 전에 orchestration JS의 template delimiter 오류로 tool 호출 자체가 시작되지 않은 시도도 있었으며 ODE나 물리 계산 실행으로 세지 않는다. local 과학 코드 실행·ODE·완료 실행 replay는 모두0이다.

확보한 것은 조건부 연속모델의 exact reduction, analytic Jacobian, D-only monotonic equilibrium 및 implementation contract다. parent 저장 결과와의 finite-tolerance 비교, 실제 Radau 성능, accepted/dense-state 검증, 새 구현의 light review는 구현 후 별도 근거가 필요하다. low-T CI, He/Li CX branch·photon moment, D PI/RR energy adapter, recombination→z20 초기 charge, 전체 nuclear/molecular/Compton/spectral closure는 PHYS79처럼 OPEN이다. strong no-go는 주장하지 않는다.
