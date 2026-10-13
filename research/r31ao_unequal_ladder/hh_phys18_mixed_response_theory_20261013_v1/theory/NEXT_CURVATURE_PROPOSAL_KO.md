# 다음 이론 단위 — HH_DEFECT_PARAMETER_CURVATURE

## 1. 목표와 현재 확보한 교차항

PHYS18의 원 \(C^2\) 계열에서 \(F_{\lambda b}\)와 네 모서리 interaction은
\[
[L_m,U_m]=[-2.668505746423,-2.118796636045]\times10^{-12}\ {\rm K}
\]
에 포함된다. 축 응답을 보존하는 현재 재구성은 이미
\[
F(\lambda,b)
=F(\lambda,0)+F(0,b)-F(0,0)+c_m\lambda b+R_m,
\]
\[
c_m=-2.393651191234\times10^{-12}\ {\rm K},\qquad
|R_m|\le2.748545551890\times10^{-13}\lambda b\ {\rm K}
\tag{C1}
\]
로 닫혔다.

다음 물리 질문은 **HH와 birth의 각 단독 축 응답이 rectangle 전체에서 얼마나 선형에 가까운가**다. 새 목표는 나머지 두 pure defect curvature
\[
F_{\lambda\lambda},\qquad F_{bb}
\tag{C2}
\]
를 실제로 포함하고, 전체 bilinear response representation의 오차를 Kelvin 단위로 인증하는 것이다. 원 \(C^2\), 같은 COMMON·\(\alpha,\lambda,b\), 원 gas 영역·물리 계수·35개 photon/guard slot을 유지한다.

이번 파일은 pure-response 시작식·입력·수용 기준을 구성했다. 새로운 pure-response application 상태는 not_run이다. 현재 혼합 결과와 선형 preconditioner 입력 준비의 실제 계산은 현재 PHYS18 결과로 보존한다.

## 2. 첫 half와 Full의 pure implicit 도함수

\(\theta\in\{\lambda,b\}\), \(\delta_\lambda=\partial_\theta\lambda\),
\(\delta_b=\partial_\theta b\)라 두자. 따라서 두 \(\delta\)는 0 또는 1이고 서로 곱은 0이다. 경로 \(k\)에서 \(p_k=g_{k,\theta}\),
\(K_k=g_{k,\theta\theta}\)라 쓴다. \(K\)는 보통 두 번째 도함수다.

고정 COMMON에서 출발하는 첫 half·Full의 residual \(H_k(g_k;\lambda,b)=0\)에 대해
\[
\boxed{
J_kK_k
=-\{H_{k,gg}[p_k,p_k]+2H_{k,g\theta}p_k+H_{k,\theta\theta}\}.
}
\tag{C3}
\]

**증명.** \(J_kp_k+H_{k,\theta}=0\)를 \(\theta\)로 한 번 더 미분한다. \(D_\theta J_k=H_{k,gg}[p_k,\cdot]+H_{k,g\theta}\), \(D_\theta H_{k,\theta}=H_{k,g\theta}p_k+H_{k,\theta\theta}\)이므로 (C3)를 얻는다. □

원 첫 half와 Full의 fixed-gas source는 \(\lambda,b\)에 affine이어서 \(H_{k,\lambda\lambda}=H_{k,bb}=0\)이다. \(p_k\)에는 원 PHYS09의 U 또는 V를 사용한다. \(\lambda\) curvature에는 G_g_lambda가 두 번, \(b\) curvature에는 G_g_b가 두 번 들어간다. G_gg는 원 residual Hessian이므로 시간 인수를 다시 곱하지 않는다.

### 2.1 실제 first-half 선형 readiness

원 first-half SOURCE_BOX/A_Gg의 \(J_1\) 포함을 사용해
\[
S_1=\operatorname{diag}(1,1,1,13.5),\qquad C_1=I
\]
로 둔 유한 Neumann 준비를 실제 exact-Fraction 산술로 계산했다. 행별 상계의 근삿값은
\[
(5.395474227883633\times10^{-4},\ 
5.754973208761884\times10^{-6},\
1.6396465800093544\times10^{-7},\
1.020829868979607\times10^{-4}),
\]
따라서
\[
\|S_1^{-1}(I-J_1)S_1\|_\infty
\le q_1<5.396\times10^{-4}<1.
\tag{C4}
\]
정확한 rational 상계·원 입력 SHA·실제 명령은 CURVATURE_INPUT_PREFLIGHT.json에 있다. 이 결과는 pure RHS를 전송할 선형 inverse 준비이며 아직 \(K_{1,\theta\theta}\)를 계산한 결과는 아니다.

Full에는 원 \(C,B,q,S\)를 그대로 사용한다. 둘째 half에는 PHYS14 ADVANCE_RESULTS의 linear_certificates/L_hFg, root_certificate/scaled_inf_scales, refined_contraction_upper를 재사용한다. 각 inverse는 해당 경로의 원 Jacobian에 결박한다.

## 3. carried 순서에서 pure incoming photon 구성

첫 half incoming은
\[
Q_1=RZ_0+bJ_\gamma,\quad Q_{1,\theta}=\delta_bJ_\gamma,
\quad Q_{1,\theta\theta}=0.
\tag{C5}
\]
\(a_{kj}=cn_k\sigma_j\), \(A_k=(1+ha_k(1-x_k))^{-1}\)라 두면
\[
A_{k,\theta}=ha_kA_k^2p_{k,x},\qquad
\boxed{
A_{k,\theta\theta}
=ha_kA_k^2K_{k,x}+2(ha_k)^2A_k^3p_{k,x}^2.
}
\tag{C6}
\]
첫 half pure \(K_1\)를 (C3)에서 포함한 뒤
\[
\begin{aligned}
Z_{1,\theta}&=A_{1,\theta}Q_1+A_1\delta_bJ_\gamma,\\
Z_{1,\theta\theta}
&=A_{1,\theta\theta}Q_1+2A_{1,\theta}\delta_bJ_\gamma,\\
Q_{2,\theta}&=RZ_{1,\theta}+\delta_bJ_\gamma,\\
\boxed{Q_{2,\theta\theta}=RZ_{1,\theta\theta}}&
\end{aligned}
\tag{C7}
\]
를 구성한다. 원 first-half/second-half value·U·V carry와 첫 도함수 포함을 교차한다. 두 번째 pure slot은 (C7)에서 실제로 새로 생성해야 한다. 모든 식에서 33개 node와 두 guard를 유지한다.

## 4. 둘째 half의 pure gas 응답

둘째 단계는
\[
g_2-g_1=hB_2(g_2,\lambda)+V_{\rm ph}L_2(g_2)Q_2(\lambda,b).
\]
\(J_2=I-hB_{2,g}-V_{\rm ph}(L_{2,g}Q_2)\)를 원 둘째 half Jacobian이라 하면
\[
\boxed{\begin{aligned}
J_2K_2={}&K_1+hB_{2,gg}[p_2,p_2]
+2h\delta_\lambda Dq_2[p_2]\nu_H\\
&+V_{\rm ph}\{L_{2,gg}[p_2,p_2]Q_2
+2L_{2,g}[p_2]Q_{2,\theta}
+L_2Q_{2,\theta\theta}\}.
\end{aligned}}
\tag{C8}
\]

**증명.** 둘째 단계식을 두 번 미분하고 \(L_{2,g}[K_2]Q_2\)와 \(hB_{2,g}K_2\)를 왼쪽으로 옮긴다. 이전 stage \(K_1\)와 incoming \(Q_{2,\theta\theta}\)는 (C3),(C7)에서 이미 계산된 입력이다. □

이 식은 물리 stage 순서를 따라 유한 선형 포함 두 번으로 닫힌다. 첫 단계 pure photon을 둘째 단계의 independent fixed input으로 취급하는 것은 해당 단계 \(g_2\)에 대한 편미분에서만 하는 구분이다. 전역 \(\theta\) 의존성은 \(Q_{2,\theta}\), \(Q_{2,\theta\theta}\)에 모두 남는다.

## 5. 상관된 pure endpoint 결함

\[
K_d=K_2-K_F,\quad p=p_2,\quad
d_\theta=p-p_F,\quad s_\theta=p-p_1,\quad
s_{\theta\theta}=K_2-K_1.
\]

Full residual에 대해 직접식은
\[
\boxed{
J_FK_d=J_FK_2+H_{gg}(g_F)[p_F,p_F]+2H_{g\theta}(g_F)p_F.
}
\tag{C9}
\]
\(L=J_y-J_F\), \(\Delta H_{gg}=H_{gg}(g_2)-H_{gg}(g_F)\),
\(\Delta H_{g\theta}=H_{g\theta}(g_2)-H_{g\theta}(g_F)\)라 두면
\[
\boxed{\begin{aligned}
J_FK_d={}&r_{\theta\theta}-LK_2-\Delta H_{gg}[p,p]\\
&-2H_{gg}(g_F)[d_\theta,p-d_\theta/2]\\
&-2\Delta H_{g\theta}p-2H_{g\theta}(g_F)d_\theta.
\end{aligned}}
\tag{C10}
\]

**증명.** \(r_{\theta\theta}=J_yK_2+H_{gg}(g_2)[p,p]+2H_{g\theta}(g_2)p\)를 (C9)에 대입한다. 대칭 bilinear 항등식
\[
K[p,p]-K[p-d_\theta,p-d_\theta]
=2K[d_\theta,p-d_\theta/2]
\]
로 공통 Hessian 차이를 묶는다. 원 fixed-gas \(H_{\theta\theta}=0\)를 썼다. □

PHYS18에서 구성한 HI rational Hessian 공간차, HH gradient 선분식, 원 \(C^2\) signed nonphoto/HH Hessian 차이를 재사용한다. 원 mixed 수치 값은 (C10)의 pure RHS로 대입하지 않고, 동일 source·inverse 구조와 최종 reconstruction의 별도 교차항으로 유지한다.

### 5.1 실제 stage 순서에서 \(r_{\theta\theta}\)

\[
\boxed{\begin{aligned}
r_{g,\theta\theta}=h\{&
B_{1,g}K_1-B_{2,g}K_2\\
&+B_{1,gg}[p_1,p_1]-B_{2,gg}[p,p]\\
&+2\delta_\lambda(Dq_1p_1-Dq_2p)\nu_H\}.
\end{aligned}}
\tag{C11}
\]
여기서
\[
\begin{aligned}
B_{1,g}K_1-B_{2,g}K_2
={}&D\delta B_t(g_1)K_1-B_{2,g}(g_2)s_{\theta\theta}\\
&-\int_0^1B_{2,gg}(g_1+ts)[s,K_1]\,dt,\\
B_{1,gg}[p_1,p_1]-B_{2,gg}[p,p]
={}&\Delta B_{gg}[p_1,p_1]
-2B_{2,gg}[s_\theta,(p+p_1)/2],\\
Dq_1p_1-Dq_2p
={}&D\delta q_t(g_1)p_1-Dq_2(g_2)s_\theta\\
&-\int_0^1D^2q_2(g_1+ts)[s,p_1]\,dt.
\end{aligned}
\tag{C12}
\]
PHYS17의 첫 density derivative를 \(v=K_1\) 또는 \(v=p_1\)에 적용한다. 필요한 최고 source derivative는 여전히 Hessian이다.

광자 \(p_{\theta\theta}\)는 PHYS18의 같은 일곱 sector graph에
\[
(AB)_{\theta\theta}=A_{\theta\theta}B+2A_\theta B_\theta+AB_{\theta\theta}
\tag{C13}
\]
를 적용한다. \(b f\) sector는 \(b f_{\theta\theta}+2\delta_bf_\theta\)다. survival·\(\Delta A_1\)에서
\[
\zeta_{\theta\theta}
=-h\{c\sigma(n_2-n_1)K_{2,x}+a_1s_{\theta\theta,x}\}
\]
를 먼저 인수 분해한다. 전체 \(r_{\theta\theta}=r_{g,\theta\theta}+V_{\rm ph}p_{\theta\theta}\)를 (C10)에 사용한다.

단계 차이 자체도
\[
s_{\theta\theta}
=h\{B_{2,g}K_2+B_{2,gg}[p,p]
+2\delta_\lambda Dq_2[p]\nu_H\}
+V_{\rm ph}P_{2,\theta\theta}
\tag{C14}
\]
와 \(K_2-K_1\)의 교차로 조일 수 있다.

## 6. 유한 온도 pure curvature

\(\ell_e,C_T,\Pi_2,\Pi_F,n_F\)는 PHYS18의 같은 readout이다. 그러면
\[
\boxed{
T_{2,\theta\theta}
=\frac{C_TK_{2,w}-T_2\ell_eK_2-2T_{2,\theta}\ell_ep}{\Pi_2},
}
\tag{C15}
\]
\[
\boxed{\begin{aligned}
F_{\theta\theta}
=\frac1{\Pi_F}\{&
n_FK_d-T_{2,\theta\theta}d_e
-2T_{2,\theta}d_{e,\theta}\\
&-2F_\theta P_\theta-F\ell_eK_2\}.
\end{aligned}}
\tag{C16}
\]
**증명.** \(C_Tw_2=T_2\Pi_2\)와 \(N=F\Pi_F\),
\(N=C_Td_w-T_2d_e\)를 각각 같은 \(\theta\)로 두 번 미분한다. \(P_{\theta\theta}=\ell_e(K_2-K_d)\)를 넣으면 \(K_d\)의 계수는 \(n_F\)로 묶인다. □

## 7. \(C^2\) bilinear interpolation 오차 정리

네 corner의 실제 같은-family 값으로
\[
\begin{aligned}
\mathcal L F={}&(1-\lambda)(1-b)F_{00}
+\lambda(1-b)F_{10}\\
&+(1-\lambda)bF_{01}+\lambda bF_{11}
\end{aligned}
\tag{C17}
\]
을 정의한다. \(F_{00}=F(0,0)\) 등이며 이들은 같은 \(\alpha\)에 결박된 coefficient다. pure curvature의 전역 포함이
\(F_{\lambda\lambda}\in[L_{\lambda\lambda},U_{\lambda\lambda}]\),
\(F_{bb}\in[L_{bb},U_{bb}]\)이면
\[
\boxed{
F-\mathcal L F\in
-\frac{\lambda(1-\lambda)}2[L_{\lambda\lambda},U_{\lambda\lambda}]
-\frac{b(1-b)}2[L_{bb},U_{bb}].
}
\tag{C18}
\]
따라서 \(M_{\theta\theta}=\max(|L_{\theta\theta}|,|U_{\theta\theta}|)\)에서
\[
\boxed{
|F-\mathcal L F|
\le\frac{M_{\lambda\lambda}}2\lambda(1-\lambda)
+\frac{M_{bb}}2b(1-b)
\le\frac{M_{\lambda\lambda}+M_{bb}}8.
}
\tag{C19}
\]

**증명.** 한 변수 선형 interpolation \(I_x\)에 대해
\[
f(x)-I_xf(x)=\int_0^1K_x(t)f''(t)\,dt,\quad
K_x(t)=
\begin{cases}
-t(1-x),&0\le t\le x,\\
-x(1-t),&x\le t\le1.
\end{cases}
\]
이 식은 각 구간에서 부분적분하면 직접 확인된다. kernel은 음수이고 적분은 \(-x(1-x)/2\)다. 따라서 \(f''\in[L,U]\)이면
\(f-I_xf\in-x(1-x)[L,U]/2\).
\(\mathcal L=I_\lambda I_b\)이고
\[
F-I_\lambda I_bF=(I-I_\lambda)F+I_\lambda(I-I_b)F
\]
다. 두 번째 항의 \(I_\lambda\)는 양의 convex weight를 가진다. 각 축의 curvature 포함을 대입해 (C18)을 얻고 절댓값을 취해 (C19)를 얻는다. □

또한
\[
\mathcal L F=F_{00}+a_\lambda\lambda+a_bb+\mathcal I\lambda b,
\quad a_\lambda=F_{10}-F_{00},\ a_b=F_{01}-F_{00}
\tag{C20}
\]
에서 \(\mathcal I\)는 PHYS18의 확립된 음의 범위다. 원 PHYS17의 전역 first derivative를 적분하면 \(a_\lambda,a_b\)의 포함도 있다. 이 coefficient들을 같은-family 관계와 함께 저장하면 새 four-corner root 실행 없이 현재 전체 계열에 대한 검증된 response representation을 만들 수 있다. 절대 anchor \(F_{00}\)의 해상도는 실제 결박한 기존 endpoint 포함으로 명시한다.

## 8. 다음 실행의 수용 기준

1. (C3),(C7),(C8)로 첫 half·Full·둘째 half의 두 pure gas 및 photon 응답을 실제로 포함한다.
2. 각 stage의 원 Jacobian 또는 실제 저장 Jacobian 포함에 대한 유한 inverse certificate를 붙인다. first-half는 (C4)의 identity 전처리 준비를 사용할 수 있다.
3. (C9)의 직접 포함, (C10)–(C14)의 상관 포함, 원으로부터 새로 생성한 \(K_2-K_F\)를 교차한다.
4. (C15)–(C16)으로 \(F_{\lambda\lambda},F_{bb}\)를 실제 계산하고, 부호가 결정되면 convexity/concavity를 해당 scope에서 진술한다. 0을 포함하면 실제 폭과 지배 항을 기록한다.
5. (C18)–(C20)의 bilinear remainder·coefficient 포함을 실제 Kelvin 단위로 계산한다. 이미 확보한 mixed negative interval과 (C1)을 입력으로 유지한다.
6. 새 pure coefficient 2, carried incoming, guard ledger, finite-temperature quotient를 독립 검토 및 새 Wolfram/xAct 계산으로 확인한다.

source callback·비선형 root·history 실행은 현재 계획에 없다. heavy_queue는 빈 배열이며 launch=false다. 이 다음 단위의 수치 상태는 not_run이고, 목표는 새 pure-curvature 포함과 실제 bilinear 오차 경계다.
