# WU088_HH PHYS17 — 같은 계열의 endpoint 결함에 대한 매개변수 응답

**직접 유도 상태:** `derived`. 이 문서의 정리들은 아래 유지된 전제에서 성립한다. 원 포함 자료에 대한 실제 산술, Wolfram/xAct 검산과 독립 채택 결과는 PHYS17의 해당 실행·심사 기록에 연결한다. 본 문서는 과거 source·근·history를 재실행하지 않고, PHYS16에서 남겨 둔 P1–P4를 구현 가능한 C² 식으로 닫는다.

## 1. 대상, 전제와 표기

같은 초기 COMMON과 하나의 admissible 고정 계수 선택 α에 대해 두 전역 매개변수 θ=(λ,b)∈[0,1]²를 Full과 실제 두 half 경로에 공유한다. 미분할 매개변수는 θ∈{λ,b} 하나이며 점은 도트로도 표기한다. 시간, 밀도, 원 상수, 수송 사상, COMMON의 미래 매개변수 도함수는 고정한다. 원 source family의 작은 열린 매개변수 확장 덕분에 닫힌 rectangle의 경계에서도 해당 1차 미분을 정의한다.

기체 좌표와 endpoint는

\[
g=(x,y,z,w)^T,\quad y_*=g_2,\quad d=g_2-g_F,\quad
v=g_{1,\theta},\quad u=g_{2,\theta},\quad s=g_2-g_1
\]

로 둔다. 이하 `y_*`는 두 번째 endpoint 벡터이고, `y`는 He II fraction이다. w의 단위는 eV/H이며 λ,b는 무차원이다. h=625000000 s, Full 길이는 2h이다. 동일 endpoint 시각의 정확한 density ratio를 f=f₂=exact(nHe,2 stored)/exact(n₂)라 둔다. 물리상수 c,k_B 및 eV-to-erg leaf를 원 값으로 유지한다.

사용하는 가정은 다음과 같다.

1. 원 4차원 convex X의 내부 hull에 g₁,g₂,g_F와 필요한 선분·density pullback이 포함된다. source와 실제 implicit root family는 상속된 C² family이다.
2. 같은 고정 C,B,S,q가 X에서 |I−C H_g(g;λ,b)|≤B, ‖S⁻¹BS‖∞≤q<1을 만족한다. H=H_F는 Full 잔차다.
3. PHYS09/11/14의 원 1차 gas·photon carry와 PHYS16의 상관된 d,s,잔차 포함을 재사용한다. 원 signed gradient/Hessian은 부호 clipping을 하지 않는다.
4. 현재 nonphoto source는 원 FT03의 CI·RR·DR graph이다. HI threshold χ_H는 실제 source의 동일 captured leaf이다. 추가 source 성분은 별도 B 항으로 명시한다.

이 가정과 원본 identity는 PHYS16의 `contracts/PARAMETER_RESPONSE_CONTRACT.json`, PHYS15의 `theory/ASSUMPTIONS_AND_BINDINGS_KO.md` 및 PHYS16의 `evidence/intake/SOURCE_COOLING_AUDIT_KO.md`에 연결된다. 다음 유도에서 정칙성은 C² 안에 유지된다.

원 source 포함의 적용 위치는 아래와 같다. 새로운 연결식이 원 X 밖의 source 값을 요구하지 않는다.

| 식의 평가점 | 도함수 입력과 포함 근거 |
|---|---|
| g₁, g₂ 및 g₁+ts | 원 first-half/실제 second-half root hull의 convex hull ⊂ X; Full nonphoto/q box Hessian과 centre-to-hull gradient 포함 |
| g₁의 온도 정렬점 g*=Ψ(g₁)와 g₁+t(g*−g₁) | PHYS15에서 exact density ratio와 내부 hull로 검토한 pullback; PHYS16 적용에서 같은 값을 재사용 |
| g₂−td, 0≤t≤1 | PHYS16에서 포함한 실제 d=g₂−gF와 원 g₂,gF의 공통 convex X |
| P2의 Hgg와 Hgθ | 원 Full `SOURCE_BOX.json`의 잔차 gas Hessian 및 mixed gas/parameter Hessian; λ slot 4, b slot 5 |

centre 자료를 이용해 값·gradient 포함을 좁힐 때도 Hessian의 권위 영역은 원 X이다. Whole-X Hessian을 새 centred Hessian 값으로 바꾸거나 추가 smoothness를 가정하지 않는다.

## 2. 정리 1 — 작은 endpoint 차이를 먼저 인수 분해한 미분식

\[
H(g)=g-g_0-2hB_2(g,\lambda)-VL_F(g)Q_F(b),\quad
H(g_F)=0,\quad r=H(g_2).
\]

\[
J_y=H_g(g_2),\qquad J_F=H_g(g_F),
\]

\[
\mathcal L(d)v_0=\int_0^1H_{gg}(g_2-td)[d,v_0]dt,\qquad
\mathcal G_\theta=\int_0^1H_{g\theta}(g_2-td)dt
\]

라 두면 정확히

\[
J_y-J_F=\mathcal L(d),\quad
H_\theta(g_2)-H_\theta(g_F)=\mathcal G_\theta d,
\]

\[
\boxed{J_Fd_\theta=f_\theta,
\qquad f_\theta=r_\theta-\mathcal L(d)u-\mathcal G_\theta d.}
\tag{1}
\]

**증명.** H(g_F;θ)=0을 미분하면 J_F(g_{2,θ}−d_θ)+H_θ(g_F)=0이다. 한편 r_θ=J_yu+H_θ(g₂)다. 두 식을 빼고 H_g와 H_θ에 각각 선분 적분을 적용하면 (1)이 성립한다. H_{gg},H_{gθ}의 연속성만 사용한다. □

따라서 새 forcing fθ의 모든 feedback 항은 작은 d를 명시적으로 인수로 갖는다. 이와 동치인 endpoint 기준식은

\[
\boxed{J_yd_\theta=f_\theta+\mathcal L(d)d_\theta.}
\tag{2}
\]

원 Full 기체 1차 carry gF,θ를 사용할 때에는

\[
J_yd_\theta=r_\theta-\mathcal L(d)g_{F,\theta}-\mathcal G_\theta d
\tag{3}
\]

도 같은 dθ를 포함한다. 식 (3)은 두 경로의 원 1차 carry와 상관 잔차의 독립 연결로 사용할 수 있다.

### 2.1 실제 source slot과의 대응

현재 H의 명시적 매개변수 미분은

\[
H_\lambda=-2h q_2\nu_H,\qquad
H_{g\lambda}=-2h\nu_H\otimes Dq_2,
\]

\[
H_b=-2VL_FJ_\gamma,\qquad
H_{gb}=2\sum_j\frac{\ell_jJ_{\gamma j}}{D_{Fj}^2}\nu_j e_x^T,
\quad\ell_j=2ha_{2j}.
\tag{4}
\]

여기서 ν_H=(1,0,0,−χ_H)ᵀ, Jγ=Mγe₂₄, DFj=1+ℓj(1−x)이다. source export의 `G_g_lambda[i][j]`, `G_g_b[i][j]`는 각각 residual[i].hessian[j][4], residual[i].hessian[j][5]에 대응한다. `G_gg`는 이미 Full **잔차** Hessian이다.

## 3. 정리 2 — stage movement의 도함수를 공유하는 gas 잔차

비광자 source를

\[
B_k(g,\lambda)=F_k(g)+\lambda q_k(g)\nu_H-2H_kw e_w
\]

로 쓴다. Fk는 원 nonphoto export이다. PHYS15/16에서

\[
s=hB_2(g_2)+VP_2,\qquad
r_g=h\{B_1(g_1)-B_2(g_2)\}
\]

를 얻었다. 같은 매개변수로 미분하면

\[
\boxed{s_\theta=h\{B_{2,g}(g_2)u+\delta_{\theta\lambda}q_2(g_2)\nu_H\}+VP_{2,\theta}.}
\tag{5}
\]

이 sθ는 정확히 u−v와 같으므로 보존된 두 sensitivity 포함과 교차할 수 있다. g_t=g₁+ts,
δB_t(g)=B₁(g)−B₂(g), δq_t=q₁−q₂로 두면

\[
\boxed{\begin{aligned}
r_{g,\theta}={}&h\{D\delta B_t(g_1)[v]+\delta_{\theta\lambda}\delta q_t(g_1)\nu_H\}\\
&-hB_{2,g}(g_2)s_\theta
-h\int_0^1B_{2,gg}(g_t)[s,v]dt
-h\delta_{\theta\lambda}\int_0^1Dq_2(g_t)[s]dt\,\nu_H.
\end{aligned}}
\tag{6}
\]

**증명.** 정확한 직접 미분은

\[
r_{g,\theta}=h\{B_{1,g}(g_1)v-B_{2,g}(g_2)u
+\delta_{\theta\lambda}[q_1(g_1)-q_2(g_2)]\nu_H\}.
\]

u=v+sθ를 넣는다. B₁,g(g₁)−B₂,g(g₂)는 DδBt(g₁)−∫B₂,gg(g_t)[s,·]dt이고, q₁(g₁)−q₂(g₂)=δqt(g₁)−∫Dq₂(g_t)[s]dt다. 대입하면 (6)이 따른다. □

식 (6)은 평균 source Jacobian 자체를 매개변수 미분한 표현을 endpoint B₂,g(g₂)sθ와 작은 s의 Hessian contraction으로 재구성한다. 원 H₁=H₂이므로 δBt의 팽창항은 정확히 소거되고, B₂,g에는 −2H₂ e_w e_wᵀ를 유지한다.

## 4. 정리 3 — C² nonphoto Jet에서 He thermal derivative를 직접 회수

이 정리는 density pullback의 작은 He 보정에 필요한 도함수를 닫는다. f,n은 endpoint 2의 고정 값이고

\[
e=x+f(y+2z),\quad \Pi=1+f+e,\quad T=C_Tw/\Pi,\quad
\ell_e=(1,f,2f,0)
\]

이다. 다음 정규화된 화학·열 조합과 온도를 유지하는 x 방향을 정의한다.

\[
U(g)=\frac{F_w(g)+\chi_HF_x(g)}{ne},\qquad
\xi(g)=e_x+\frac{w}{\Pi}e_w.
\tag{7}
\]

원 source에서

\[
F_x=ne\{(1-x)\beta_H-x\alpha_H\},
\]

\[
F_w=ne\{-\chi_H(1-x)\beta_H-x\kappa_H
+f k_{w\mathrm{He}}(y,z,T)\}.
\]

따라서

\[
U(g)=-x\{\kappa_H(T)+\chi_H\alpha_H(T)\}
+f k_{w\mathrm{He}}(y,z,T).
\tag{8}
\]

DT[ξ]=0이고 Dy[ξ]=Dz[ξ]=0이므로 식 (8)의 고정 온도 x 미분을 취하면

\[
DU[\xi]=-[\kappa_H(T)+\chi_H\alpha_H(T)].
\]

그러므로

\[
\boxed{k_{w\mathrm{He}}(g)=\frac{U(g)-xDU(g)[\xi(g)]}{f}.}
\tag{9}
\]

임의의 기체 방향 v₀에 대해 이를 한 번 미분하면

\[
\boxed{\begin{aligned}
Dk_{w\mathrm{He}}(g)[v_0]
=\frac{1}{f}\bigg\{
DU[v_0]-v_{0x}DU[\xi]
-x\big[D^2U[v_0,\xi]+DU[D\xi[v_0]]\big]\bigg\},\\
D\xi[v_0]=\left[\frac{v_{0w}}{\Pi}
-\frac{w\ell_ev_0}{\Pi^2}\right]e_w.
\end{aligned}}
\tag{10}
\]

**증명.** (8)은 원 hydrogen CI 항을 동일 χ_H로 소거한 source 항등식이다. ξ를 따라 온도와 He fractions가 고정되므로 첫 방향 미분에서 수소 항의 계수만 남는다. (9)에 ordinary product·chain rule을 적용하고 ξ의 도함수를 계산하면 (10)을 얻는다. (9)는 현재 g에서의 국소 값·도함수 항등식으로, x=0까지 source를 평가할 필요가 없다. □

### 4.1 저장된 source Jet에 바로 적용하는 계산식

L=F_w+χ_HF_x라 두면 e의 Hessian은 0이므로

\[
DU[v_0]=\frac1n\left(\frac{DL[v_0]}e-
\frac{L\ell_ev_0}{e^2}\right),
\]

\[
\boxed{D^2U[v_0,z_0]=\frac1n\left\{
\frac{D^2L[v_0,z_0]}e
-\frac{DL[v_0]\ell_ez_0+DL[z_0]\ell_ev_0}{e^2}
+\frac{2L(\ell_ev_0)(\ell_ez_0)}{e^3}
\right\}.}
\tag{11}
\]

식 (9)–(11)의 입력은 Full `nonphoto[0]`, `nonphoto[3]`의 value, gas gradient, signed gas Hessian뿐이다. e,f,Π가 양수인 원 hull에서 모두 정칙하다. PHYS16의 cooling-cone 값 포함과 식 (9)의 값 포함은 같은 함수에 대한 두 포함으로 교차할 수 있다. 도함수 포함은 식 (10)–(11)에서 직접 얻는다.

## 5. 정리 4 — exact density pullback의 상관된 1차 closure

\[
\sigma=y+2z,\quad e_k=x+f_k\sigma,\quad
\Pi_k=1+f_k+e_k,\quad \Delta f=f_1-f_2,\quad r_n=n_1/n_2,
\]

\[
r_e=r_ne_1/e_2,
\quad\delta w=-w\Delta f(1+\sigma)/\Pi_1,
\quad g_*=g+\delta w e_w.
\]

그러면 T₂(g*)=T₁(g)이고

\[
F_1(g)=r_eF_2(g_*)+n_1e_1\Delta f\,k_{w\mathrm{He}}(g_*)e_w,
\quad q_1(g)=r_nq_2(g_*).
\tag{12}
\]

작은 차이를 보존하는 값은

\[
r_e-1=(r_n-1)+r_n\Delta f\,\sigma/e_2.
\]

방향 v₀를 따라 dotσ=v₀y+2v₀z, dot e_k=ℓe,k v₀라 두면

\[
\boxed{Dr_e[v_0]=r_n\Delta f
\frac{e_2\dot\sigma-\sigma\dot e_2}{e_2^2},}
\tag{13}
\]

\[
\boxed{D\delta w[v_0]=-
\Delta f\left[
\frac{(1+\sigma)v_{0w}+w\dot\sigma}{\Pi_1}
-\frac{w(1+\sigma)\dot e_1}{\Pi_1^2}
\right].}
\tag{14}
\]

F=F₂, q=q₂, δF=F₁−F₂, δq=q₁−q₂, v*=v₀+Dδw[v₀]e_w로 줄여 쓰자. 정확히

\[
\boxed{\begin{aligned}
D\delta F(g)[v_0]={}&(r_e-1)DF(g)[v_0]+Dr_e[v_0]F(g_*)\\
&+r_e\delta w\int_0^1D^2F(g+t\delta w e_w)[e_w,v_0]dt\\
&+r_e(\partial_wF)(g_*)D\delta w[v_0]\\
&+n_1\Delta f\left\{
\dot e_1 k_{w\mathrm{He}}(g_*)
+e_1Dk_{w\mathrm{He}}(g_*)[v_*]
\right\}e_w,
\end{aligned}}
\tag{15}
\]

\[
\boxed{\begin{aligned}
D\delta q(g)[v_0]={}&(r_n-1)Dq(g)[v_0]\\
&+r_n\delta w\int_0^1D^2q(g+t\delta w e_w)[e_w,v_0]dt\\
&+r_n(\partial_wq)(g_*)D\delta w[v_0].
\end{aligned}}
\tag{16}
\]

여기서 ∂wF와 ∂wq는 w 좌표의 도함수다. 구현에서는 각각 `DF[:,3]`, `Dq[3]`로 명시한다.

**증명.** (12)를 v₀로 미분하고 Dg* v₀=v*를 사용한다. `r_e DF(g*)[v₀]−DF(g)[v₀]`를 `(r_e−1)DF(g)[v₀]+r_e(DF(g*)−DF(g))[v₀]`로 나눈 뒤 마지막 차이에 Hessian 선분 적분을 적용한다. HH 식도 r_n이 고정인 같은 계산으로 따른다. He correction의 도함수는 (10)을 직접 대입한다. □

식 (6)의 source-time 항은

\[
D\delta B_t(g)[v_0]=D\delta F(g)[v_0]+\lambda D\delta q(g)[v_0]\nu_H
\]

로 닫힌다. 현재 exact Δf는 약 −6.94525×10⁻¹⁸이고 이 작은 factor가 모든 density-normalization derivative 항에 유지된다. Δf=0이면 g*=g, Dδw=Dr_e=0이므로 (15)–(16)은 정확히 `(r_n−1)DF[v₀]`, `(r_n−1)Dq[v₀]`로 환원된다.

## 6. 정리 5 — 원 photon 일곱 sector의 1차 미분

R,RF와 Z₀는 고정이고 Jγ=Mγe₂₄이다. g₂에서

\[
\tau_j=ha_{2j}(1-x_2),\quad A=(I+\tau)^{-1},\quad
L=I-A,\quad A_F=(I+2\tau)^{-1},\quad L_F=I-A_F,
\]

\[
C_1=\tau A^2A_F,\quad C_2=\tau^2A^2A_F,\quad
Q_1=RZ_0+bJ_\gamma,\quad\Delta R=R^2-R_F.
\]

대각 연산자끼리의 곱은 성분별이다. 기체 전처리 C와 photon C₁,C₂는 구분한다. δ_b=δθb라 두면

\[
\dot Q_1=\delta_bJ_\gamma,\quad
\dot\tau_j=-ha_{2j}u_x,\quad
\dot A=-A^2\dot\tau,\quad \dot L=-\dot A,
\]

\[
\dot A_F=-2A_F^2\dot\tau,\quad \dot L_F=-\dot A_F,
\]

\[
\dot C_1=A^2A_F(1-2\tau A-2\tau A_F)\dot\tau,
\]

\[
\dot C_2=2\tau A^2A_F(1-\tau A-\tau A_F)\dot\tau.
\tag{17}
\]

첫 opacity 차이는 작은 scalar ζ를 먼저 유지한다.

\[
\zeta_j=h\{c\sigma_j(n_2-n_1)(1-x_2)-a_{1j}s_x\},
\quad\Delta A_1=\zeta A_1A,
\]

\[
\dot\zeta_j=-h\{c\sigma_j(n_2-n_1)u_x+a_{1j}s_{\theta,x}\},
\quad \dot A_{1j}=ha_{1j}A_{1j}^2v_x,
\]

\[
\boxed{\dot{\Delta A}_1=\dot\zeta A_1A
+\zeta(\dot A_1A+A_1\dot A).}
\tag{18}
\]

K=I−LR라 두면 PHYS15의 각 p sector와 그 도함수는 다음과 같다.

\[
p_{op}=-K\Delta A_1Q_1,
\quad
\boxed{\dot p_{op}=\dot LR\Delta A_1Q_1
-K\dot{\Delta A}_1Q_1-K\Delta A_1\dot Q_1,}
\tag{19a}
\]

\[
p_{com}=L[R,A]Q_1,
\quad
\boxed{\dot p_{com}=\dot L[R,A]Q_1
+L[R,\dot A]Q_1+L[R,A]\dot Q_1,}
\tag{19b}
\]

\[
p_{loc}=L(I-R)RZ_0,
\quad \boxed{\dot p_{loc}=\dot L(I-R)RZ_0,}
\tag{19c}
\]

\[
p_{stock}=C_2R^2Z_0,
\quad \boxed{\dot p_{stock}=\dot C_2R^2Z_0,}
\tag{19d}
\]

\[
p_{split}=L_F\Delta RZ_0,
\quad \boxed{\dot p_{split}=\dot L_F\Delta RZ_0,}
\tag{19e}
\]

\[
p_{bR}=bLA(R-I)J_\gamma,
\quad
\boxed{\dot p_{bR}=\delta_bLA(R-I)J_\gamma
+b(\dot LA+L\dot A)(R-I)J_\gamma,}
\tag{19f}
\]

\[
p_{bBE}=-bC_1J_\gamma,
\quad
\boxed{\dot p_{bBE}=-\delta_bC_1J_\gamma-b\dot C_1J_\gamma.}
\tag{19g}
\]

**증명.** (17)은 각 대각 유리함수의 미분이다. (18)은 PHYS16의 동일 s에 의한 opacity 차이 식의 미분이고, (19)는 원 일곱 항에 product rule을 적용한 결과다. R과 A의 순서는 바꾸지 않는다. □

식 (19f,g)는 b의 직접 항과 b에 따른 상태·opacity feedback을 함께 담는다. 전체 b 응답에서는 g₁,b와 g₂,b가 다른 모든 sector에도 들어간다.

### 6.1 실제 stage derivative와의 정확한 합 검사

\[
Q_2=RA_1Q_1+bJ_\gamma,\quad
\dot Q_2=R(\dot A_1Q_1+A_1\dot Q_1)+\delta_bJ_\gamma,
\]

\[
\dot P_1=-\dot A_1Q_1+(I-A_1)\dot Q_1,
\quad \dot P_2=\dot LQ_2+L\dot Q_2,
\]

\[
Q_F=R_FZ_0+2bJ_\gamma,\quad
\dot{\widehat P}_F=\dot L_FQ_F+2\delta_bL_FJ_\gamma.
\]

따라서

\[
\boxed{\sum_s\dot p_s=\dot P_1+\dot P_2-\dot{\widehat P}_F,
\qquad r_\theta=r_{g,\theta}+V\sum_s\dot p_s.}
\tag{20}
\]

33개 원 group과 number/energy guard 두 개에 그대로 적용한다. Guard에서 A=1,L=0 및 그 도함수 0을 유지한다.

### 6.2 미분된 photon ledger와 실제 endpoint readout

원 photon number·energy row를 각각 n,uγ라 하고
ΔẐ=Z₂−AF(g₂)QF로 두면

\[
\mathbf1^T\dot p=-\partial_\theta(n\Delta\widehat Z),
\]

\[
E^T\dot p=(1-\rho)\{E^T\dot P_1-\delta_bM_\gamma E_{24}\}
-\partial_\theta(u_\gamma\Delta\widehat Z).
\tag{21}
\]

원 stored heat εj=Ej−χH가 정확하므로 heat ledger는 위 두 식의 같은 선형 결합이다. 실제 Full endpoint에서는

\[
\Delta Z_j=\Delta\widehat Z_j+\Gamma_jd_x,
\quad \Gamma_j=\frac{\ell_jQ_{Fj}}{D_{yj}D_{Fj}},
\quad D_{Fj}=D_{yj}+\ell_jd_x,
\]

\[
\dot\Gamma_j=\frac{\ell_j\dot Q_{Fj}}{D_{yj}D_{Fj}}
+\Gamma_j\ell_j\left(\frac{u_x}{D_{yj}}+
\frac{u_x-d_{\theta,x}}{D_{Fj}}\right),
\]

\[
\boxed{\Delta Z_{j,\theta}=\Delta\widehat Z_{j,\theta}
+\Gamma_jd_{\theta,x}+\dot\Gamma_jd_x.}
\tag{22}
\]

Guard에는 이 opacity 보정이 0이다. 모든 식이 동일 d,dθ,u와 QF,θ=2δbJγ를 공유한다.

## 7. 정리 6 — 원 C,B,q,S에 의한 sensitivity 포함과 finite Neumann

식 (1)의 fθ를 구성한 뒤 원 전처리를 적용한다. E_F=I−CJ_F에 대해 |E_F|≤B이고

\[
d_\theta=Cf_\theta+E_Fd_\theta.
\]

비음수 mθ가

\[
\boxed{(I-B)m_\theta=\operatorname{mag}([Cf_\theta])}
\tag{23}
\]

를 만족하면

\[
\boxed{d_\theta\in[Cf_\theta]+[-Bm_\theta,Bm_\theta],
\quad \|d_\theta\|_S\le a_\theta:=\frac{\|Cf_\theta\|_S}{1-q}.}
\tag{24}
\]

**증명.** ‖S⁻¹BS‖∞<1에서 I−B는 가역이고 역행렬은 비음수 Neumann 급수다. |dθ|≤|Cfθ|+B|dθ|를 그 역행렬로 전달하면 (23)–(24)가 성립한다. □

기존 dθ 포함 또는 g₂,θ−gF,θ와 교차한 뒤

\[
D_\theta\leftarrow D_\theta\cap([Cf_\theta]+[E_F]D_\theta)
\]

로 signed 포함을 조일 수 있다. 이는 원 true endpoint 식에 대한 유한 포함 연산이다.

### 7.1 두 번째 endpoint를 기준으로 한 오차가 있는 유한 보정

\[
M_y=I-CJ_y,\qquad v_{m,\theta}=\sum_{k=0}^mM_y^kCf_\theta.
\]

원 PHYS16에서 C-weighted Hessian bound LH와 a≥‖d‖S를 얻었다. 식 (1)의 L에는 적분 weight가 1이므로

\[
\|C\mathcal L(d)\|_S\le L_Ha.
\]

식 (2)와 유한 geometric identity에서

\[
\boxed{d_\theta=v_{m,\theta}
+\sum_{k=0}^mM_y^kC\mathcal L(d)d_\theta
+M_y^{m+1}d_\theta,}
\tag{25}
\]

\[
\boxed{\|d_\theta-v_{m,\theta}\|_S
\le a_\theta\left[q^{m+1}+L_Ha\sum_{k=0}^mq^k\right].}
\tag{26}
\]

이 식의 Hessian 항에는 1/2가 없다. PHYS16의 primal Taylor 나머지는 `(1−t)`를 적분하여 1/2가 생겼고, 여기의 Jacobian 차이는 weight 1을 적분하기 때문이다. J_F 자체를 기준으로 M_F=I−CJ_F와 유한 다항식을 사용하면 (26)의 `L_H a` 항이 소거되어 오차는 q^(m+1)aθ이다.

원 PHYS16의 a≈4.28320×10⁻⁶, LH≈8.27803×10⁻⁵를 재사용하면 LH a≈3.55×10⁻¹⁰이다. 실제 PHYS17 aθ와 m에 따른 오차는 적용 결과에서 별도로 평가한다.

## 8. 정리 7 — 유한 온도 미분과 모든 forcing에 공통인 adjoint

동일 endpoint f₂에서

\[
d_e=\ell_ed,\quad \Pi_F=\Pi_2-d_e>0,\quad
T_2=C_Tw_2/\Pi_2,\quad
\Delta T=(C_Td_w-T_2d_e)/\Pi_F.
\]

미분하면

\[
\boxed{\Delta T_\theta=
\frac{C_Td_{w,\theta}-T_2d_{e,\theta}
-T_{2,\theta}d_e-\Delta T(\ell_eu-d_{e,\theta})}{\Pi_F}.}
\tag{27}
\]

여기서

\[
T_{2,\theta}=\frac{C_Tu_w-T_2\ell_eu}{\Pi_2}.
\]

T_F=T₂−ΔT,

\[
n_F=C_Te_w^T-T_F\ell_e,\qquad
k_\theta=T_{2,\theta}d_e+\Delta T\ell_eu
\]

로 묶으면

\[
\boxed{\Delta T_\theta=(n_Fd_\theta-k_\theta)/\Pi_F.}
\tag{28}
\]

**증명.** 원 유한 온도 분수의 quotient rule을 적용하면 (27)이다. d_e,θ=ℓedθ이며 T₂−ΔT=TF를 사용해 dθ에 곱해진 두 항을 모으면 (28)을 얻는다. □

같은 true Full Jacobian의 adjoint zF를

\[
J_F^Tz_F=n_F^T
\]

로 정의하면

\[
\boxed{\Delta T_\theta=(z_F^Tf_\theta-k_\theta)/\Pi_F.}
\tag{29}
\]

fθ를 직접 forcing·gas 시간 변화·movement·일곱 photon derivative·endpoint feedback으로 분해했을 때, 모든 항에 **같은 J_F, n_F, Π_F**를 사용한다. 마지막 kθ는 관측량 자체의 상태 의존성에서 오는 공통 보정이다.

finite adjoint row를

\[
z_{m,\theta}^T=n_F\sum_{k=0}^mM_y^kC
\]

로 두고 βF=‖n_FS‖₁, ΠF≥π>0라 하면

\[
\boxed{\left|\Delta T_\theta-
\frac{z_{m,\theta}^Tf_\theta-k_\theta}{\Pi_F}\right|
\le\frac{\beta_Fa_\theta}{\pi}
\left[q^{m+1}+L_Ha\sum_{k=0}^mq^k\right].}
\tag{30}
\]

각 forcing fθ,s의 endpoint response dθ,s=JF⁻¹fθ,s에는
aθ,s=‖Cfθ,s‖S/(1−q)를 써서 같은 식을 적용한다. 전체 합을 이루는 정확한 정의는
ΔTθ=Σs(nF dθ,s)/ΠF−kθ/ΠF다.

원 C 자체가 들어가는 row 차이도 명시할 수 있다. cC=‖S⁻¹CS‖∞, κ=(1−q)⁻¹라 두면

\[
\boxed{\|(z_F^T-z_{m,\theta}^T)S\|_1
\le\beta_F\kappa c_C
\left[q^{m+1}+L_Ha\sum_{k=0}^mq^k\right].}
\tag{31}
\]

**증명.** (25)에 nF를 적용하고 dual scaled norm을 사용하면 (30)이 따른다. 행렬 식
`JF⁻¹−ΣMy^k C=[My^(m+1)+ΣMy^k C L]JF⁻¹`에
‖S⁻¹JF⁻¹S‖∞≤κcC를 적용하면 (31)을 얻는다. □

## 9. 극한, 차원과 과학적 판별

θ가 고정 coefficient와 COMMON을 바꾸지 않는다는 전제가 모든 미분의 기준이다. 수송·density·시간에 대한 추가 매개변수를 도입할 경우 그 직접 도함수를 식 (12),(17),(19)에 추가한다.

* **같은 source 시각 극한:** n₁=n₂와 f₁=f₂이면 (15),(16)의 source-time derivative가 0이다.
* **투명 광자 극한:** 모든 a_kj=0이면 A=A₁=AF=I, L=LF=C₁=C₂=0이고 absorption sector와 그 매개변수 미분은 0이다.
* **b=0:** birth sector 값은 0이지만 b 미분의 δb 항은 남는다. 이는 총 b 응답을 구성하는 직접 injection 방향이다.
* **λ 미분:** δθb=0이어도 원 source가 만든 g₁,λ,g₂,λ를 통해 photon absorption과 모든 opacity feedback에 λ 응답이 들어간다.
* **endpoint 일치:** d=0이면 (1)의 두 correction은 0이다. parameter family 전체에서 두 경로가 같고 rθ=0일 때 dθ=0이다.
* **단위:** rθ,fθ,dθ의 앞 세 성분은 fraction, 마지막은 eV/H이고 모두 단위 무차원 parameter당 값이다. B_g가 s⁻¹을 포함하므로 hB_gsθ는 기체 단위다. 식 (15)의 nΔf DkHe는 eV/H/s이고, (30)의 bound는 K/parameter다.

이번 정리의 실제 판별 대상은 전체 ∂λΔT와 ∂bΔT의 포함·부호 여유다. 판단에 필요한 원 source·root data가 이미 있어, (5),(6),(10),(15)–(20),(1),(24),(27)을 순서대로 적용할 수 있다. PHYS16의 sector별 온도 기여가 이번에는 source forcing과 경로 feedback을 모두 가진 실제 매개변수 응답으로 연결된다.

### 9.1 실제 1차 포함에서 얻는 모서리·유한 변화·등결함 곡선

`checks/application/run02/results/PARAMETER_RESPONSE_RESULTS.json`의 exact rational endpoint를 사용한다. 원 파일은 626092 bytes, SHA256 `fd4fc0fe6bcf035496270bb92f0c56c44ca43d16694cb40296087569a305e7c0`이다. 이하 corollary는 이 원 포함의 직접 결과이며, 실제 채택 상태는 독립 review 기록에 연결된다. 안전한 외향 표기는

\[
\ell_-\le\partial_\lambda\Delta T\le\ell_+<0,
\quad [\ell_-,\ell_+]=[-1.009599125635,-0.8137506081166]\,10^{-8}\ {\rm K},
\]

\[
0<\beta_-\le\partial_b\Delta T\le\beta_+,
\quad[\beta_-,\beta_+]=[6.776348385589,7.185335549648]\,10^{-5}\ {\rm K}
\tag{32}
\]

이다. 하나의 α를 고정하면 rectangle에서

\[
\boxed{\Delta T(1,0)\le\Delta T(\lambda,b)\le\Delta T(0,1).}
\tag{33}
\]

또 Δλ,Δb≥0인 두 점이 원 rectangle에 있으면

\[
\boxed{\ell_-\Delta\lambda+\beta_-\Delta b
\le\Delta T(\lambda+\Delta\lambda,b+\Delta b)-\Delta T(\lambda,b)
\le\ell_+\Delta\lambda+\beta_+\Delta b.}
\tag{34}
\]

특히 각 parameter를 0에서 1로 바꾼 유한 변화는 (32)의 해당 도함수 구간에 포함된다. λ를 증가시켜 얻는 변화는 약 −10.10에서 −8.14 nK이고, b를 증가시켜 얻는 변화는 약 +67.76에서 +71.86 μK이다. 고정 α에서 두 매개변수가 만드는 총 범위는 exact endpoint 적분으로

\[
\boxed{\Delta T(0,1)-\Delta T(1,0)
\in[6.777162136197765,7.186345148772871]\,10^{-5}\ {\rm K}.}
\tag{35}
\]

원 내부 점 (λ₀,b₀)을 지나는 `ΔT(λ,b)=ΔT(λ₀,b₀)`는 ∂bΔT>0에 의해 국소적으로 유일한 C¹ 함수 b=b*(λ)를 정의하고

\[
\boxed{\frac{db_*}{d\lambda}=-\frac{\partial_\lambda\Delta T}{\partial_b\Delta T}
\in[1.132515805968976,1.489886688502190]\,10^{-4}>0.}
\tag{36}
\]

예를 들어 (1−λ₀)·1.489886688502190×10⁻⁴ < 1−b₀이면 λ₀에서 λ=1까지 그 곡선을 이어갈 수 있다. 도함수의 양의 하한과 C² root family의 정칙성이 유지되고, 이 기울기 상계가 b=1에 도달하지 않음을 보장하기 때문이다. 마찬가지로 λ₀·1.489886688502190×10⁻⁴ < b₀이면 λ=0까지 이어갈 수 있다.

**증명.** (33)–(35)는 같은 α에서 좌표 선분별로 (32)를 적분한 결과다. (36)은 implicit function theorem과 분모의 양의 하한에서 따른다. continuation은 위 기울기 상계와 compact 내부 구간의 정칙성으로 닫힌다. □

네 모서리의 HH–birth 혼합 contrast

\[
\mathcal I=\Delta T(1,1)-\Delta T(1,0)-\Delta T(0,1)+\Delta T(0,0)
\]

에는 이번 λ-도함수 폭만으로

\[
\boxed{|\mathcal I|\le1.958485175177039\times10^{-9}\ {\rm K}}
\tag{37}
\]

가 성립한다. 다음 단위는 이 contrast와 ∂λbΔT를 원 mixed carry에서 직접 포함하여 상호작용의 방향과 크기를 정한다. 식 (35)–(37)의 exact rational 계산은 `theory/PARAMETER_COROLLARIES.json`에 보존했다.

## 10. 구현 연결과 확보 범위

1. 저장된 원 centre/box source Jet에서 실제 hull의 F,q 값·gradient와 whole-X signed Hessian을 회수한다.
2. PHYS09/14 U,V와 PHYS11/14 photon carry를 같은 θ에 결박한다. 원 binary64 leaves는 exact rational로 해독한다.
3. 식 (5)의 sθ, (18)의 ΔA₁,θ를 먼저 구성하여 gas movement와 photon sector에 공유한다.
4. 식 (9)–(11)로 kHe와 그 방향 도함수를 회수하여 식 (15),(16)의 source-time derivative를 닫는다.
5. 식 (6),(19),(20)으로 rθ를 조립하고, 원 direct stage derivative 및 보존된 carry와의 포함 교차를 기록한다.
6. 원 Hgg,Hgθ와 PHYS16 d로 식 (1)의 fθ를 포함하고 같은 C,B,S,q로 dθ를 얻는다.
7. 같은 ΠF와 u,d,dθ로 식 (27) 또는 (28)을 적용한다. 실제 산술 출력에서 구간, 부호 margin, 남은 dependency width를 기록한다.
8. Wolfram/xAct는 식의 algebra·tensor contraction을 검산하고, 별도 검토는 원 source 구조·정규화·입력 연결과 실제 산술을 확인한다.

이 파일의 모든 핵심 유도는 완결됐다. PHYS17의 실행 수치와 최종 채택 상태는 해당 원 result·review 파일에 결박한다. 새 strong no-go 주장은 제안하지 않는다.
