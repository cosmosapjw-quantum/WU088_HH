# WU088_HH PHYS18 — HH–birth 혼합 endpoint 응답

## 1. 결과와 적용 범위

같은 COMMON에서 출발하는 Full과 실제 두 half의 온도 차이를 \(F(\lambda,b)=T(g_2)-T(g_F)\)라 하자. 원 \(C^2\) source·carry 자료를 사용한 실제 포함 계산은

\[
\boxed{
F_{\lambda b},\ \mathcal I
\in[-2.668505746423,-2.118796636045]\times10^{-12}\ {\rm K},
}
\tag{18.1}
\]

를 얻었다. 여기서 \(\mathcal I=F(1,1)-F(1,0)-F(0,1)+F(0,0)\)다. 따라서 같은 고정 계수 선택의 전역 rectangle에서 혼합 응답과 interaction이 모두 음수다. 직접 mixed implicit 식도 음의 포함을 주며, 작은 endpoint·stage 차이를 보존한 상관식이 이 범위를 조였다.

아래에서는 혼합 기체 결함 \(W_d=\partial_{\lambda b}(g_2-g_F)\), 일곱 광자 sector, 원 Full inverse, 유한 온도 분수와 interaction의 정확한 연결을 증명한다. 수치 결과의 machine-readable 원본은 checks/application/run02/results/MIXED_RESPONSE_RESULTS.json 및 SUMMARY.json이다. 수치 따름정리와 최종 검토 상태는 같은 theory 폴더의 MIXED_RESPONSE_NUMERICAL_COROLLARY_KO.md, MIXED_RESPONSE_CLAIMS.json과 review/DECISION.json에 결박한다.

고정된 admissible 계수 선택 \(\alpha\)마다 하나의 전역 \((\lambda,b)\in[0,1]^2\)를 Full과 두 half에 공유한다. \(\alpha\)에는 COMMON, 원 source leaves, 수송 및 밀도·상수 자료가 들어가며 미래 매개변수 미분에서 고정된다. source와 implicit root의 작은 열린 확장을 포함하는 원 \(C^2\) 전제를 사용하므로 rectangle 경계에서도 혼합 미분이 정의된다.

| 전제 | 이번 사용 |
|---|---|
| 같은 COMMON·같은 \(\alpha,\lambda,b\) | 동일 물리 계열의 경로 차이와 매개변수 미분 |
| 원 convex \(X\), 내부 root hull 및 연결 선분 | 원 source 값·gradient·signed Hessian 포함 |
| 첫 half·Full·carried 둘째 half의 원 \(U,V,W\) | \(W=\partial_{\lambda b}g\)인 보통 혼합 도함수 |
| 원 Full \(C,B,S,q\) | \(J_F^{-1}\)의 공동 유한 포함 |
| \(e_i,\Pi_i,D_{kj}>0\) | source pullback·흡수·온도 분수의 정칙성 |
| \(C^2\) source/root | mixed implicit 식과 Hessian 값의 signed 포함 |

\[
g=(x,y,z,w)
=(x_{\mathrm{HII}},y_{\mathrm{HeII}},y_{\mathrm{HeIII}},w),
\qquad [w]=\mathrm{eV/H}.
\tag{18.2}
\]

시간은 \(h=625000000\,\mathrm{s}\), \(t_0=160000000000\,\mathrm{s}\), \(t_1=t_0+h\), \(t_2=t_0+2h\)다. 끝 stage의 정확한 density ratio \(f=\operatorname{exact}(n_{\mathrm{He},2}^{stored})/\operatorname{exact}(n_2)\)를 사용한다. \(c,k_B\)와 eV-to-erg 변환은 captured leaf를 그대로 사용한다. 이 축약된 homogeneous gas/photon 계에서는 시공간 metric을 새로 도입하지 않는다.

원 source Hessian의 좌표는 gas slot \(0,\ldots,3\), \(\lambda\) slot 4, \(b\) slot 5다. SOURCE_BOX의 G_gg, G_g_lambda, G_g_b, G_lambdab는 각각 잔차의 gas/gas, gas/\(\lambda\), gas/\(b\), \(\lambda/b\) 편미분이다. G_gg에는 Full 잔차의 시간 인수 \(-2h\)가 이미 들어 있다. SOURCE_BOX_COMPONENTS/nonphoto의 Hessian에는 그 시간 인수가 아직 없다.

## 2. 원 단계식과 표기

비광자 source와 HH source를 각각 \(F_k^{np},q_k\), HH 반응 방향을 \(\nu_H=(1,0,0,-\chi_H)^T\)라 쓰면

\[
B_k(g,\lambda)=F_k^{np}(g)+\lambda q_k(g)\nu_H-2H_kw e_w.
\tag{18.3}
\]

광자 수송·흡수에서 \(V_{\mathrm{ph}}\)는 photons/H를 gas 변화로 보내는 고정 선형 사상이다. 활성 열은 \(\nu_j=(1,0,0,\epsilon_j)^T\)이며 \(\epsilon_j\)는 captured heat leaf다. 광자와 guard의 전체 차원은 35, 실제 광자 node는 33개다. 기체 birth sensitivity \(V\)와 \(V_{\mathrm{ph}}\)를 구분한다.

\[
\begin{aligned}
g_1-g_0&=hB_1(g_1,\lambda)+V_{\mathrm{ph}}P_1,\\
g_2-g_1&=hB_2(g_2,\lambda)+V_{\mathrm{ph}}P_2,\\
H(g;\lambda,b)&=g-g_0-2hB_2(g,\lambda)
-V_{\mathrm{ph}}L_F(g)Q_F(b).
\end{aligned}
\tag{18.4}
\]

\[
H(g_F;\lambda,b)=0,\quad r=H(g_2;\lambda,b),\quad
d=g_2-g_F,\quad s=g_2-g_1.
\tag{18.5}
\]

이하 \(U=g_{2,\lambda}\), \(V=g_{2,b}\), \(W=g_{2,\lambda b}\), 첫 half는 \(U_1,V_1,W_1\)이다. Full의 도함수와 작은 차이를

\[
\begin{gathered}
d_\lambda=U-U_F,\quad d_b=V-V_F,\quad W_d=W-W_F,\\
s_\lambda=U-U_1,\quad s_b=V-V_1,\quad s_{\lambda b}=W-W_1
\end{gathered}
\tag{18.6}
\]

로 둔다. \(U_F=U-d_\lambda\), \(V_F=V-d_b\)는 같은 함수에 대한 정확한 관계다. interval 구현은 원 Full carry와 이 관계를 각각 포함으로 만들어 교차한다.

## 3. 정리 1 — \(C^2\) mixed implicit 식

\(J_F=H_g(g_F)\), \(J_y=H_g(g_2)\)라 두고

\[
\mathcal B(g;p,q)
=H_{gg}(g)[p,q]+H_{g\lambda}(g)q
+H_{gb}(g)p+H_{\lambda b}(g)
\tag{18.7}
\]

를 정의한다. \(\mathcal B\)는 mixed forcing이며 원 비음수 inverse majorant 행렬 \(B\)와 다른 대상이다. 그러면

\[
\boxed{
J_FW_F=-\mathcal B(g_F;U_F,V_F),\qquad
J_FW_d=J_FW+\mathcal B(g_F;U_F,V_F).
}
\tag{18.8}
\]

**증명.** 첫 미분은 \(J_FU_F+H_\lambda(g_F)=0\)이다. 이를 전역 \(b\)로 미분하면

\[
J_FW_F+H_{gg}(g_F)[U_F,V_F]
+H_{gb}(g_F)U_F+H_{g\lambda}(g_F)V_F
+H_{\lambda b}(g_F)=0.
\]

두 번째 식은 \(W_d=W-W_F\)를 대입한 결과다. 총 두 번의 미분만 사용한다. \(H_{gg}\)가 잔차 출력 인덱스를 포함한 세 인덱스 tensor라는 사실은 source 미분 차수를 바꾸지 않는다. □

원 고정 gas 식에서

\[
H_\lambda=-2hq_2\nu_H,\quad
H_b=-2V_{\mathrm{ph}}L_FJ_\gamma,\quad
\boxed{H_{\lambda b}=0}.
\tag{18.9}
\]

마지막 항등식은 \(\lambda q_2\)와 \(bJ_\gamma\)의 원 affine 구조에서 나온다. 실제 source export의 G_lambdab 포함은 이 0과 교차한다. 상태 \(g_F(\lambda,b)\)가 두 매개변수에 함께 반응하므로 \(W_F,W_d,F_{\lambda b}\)는 나머지 mixed forcing으로 결정된다.

## 4. 정리 2 — 작은 endpoint 차이를 보존하는 상관식

\[
L=J_y-J_F=\int_0^1 H_{gg}(g_2-td)[d,\cdot]\,dt,
\quad
\Delta H_{gg}=H_{gg}(g_2)-H_{gg}(g_F).
\tag{18.10}
\]

\(\Delta H_{g\theta}\), \(\Delta H_{\lambda b}\)도 같은 두 평가점의 차이로 정의한다. 그러면

\[
\boxed{\begin{aligned}
J_FW_d={}&r_{\lambda b}-LW-\Delta H_{gg}[U,V]\\
&-H_{gg}(g_F)[d_\lambda,V]
-H_{gg}(g_F)[U_F,d_b]\\
&-\Delta H_{g\lambda}V-H_{g\lambda}(g_F)d_b\\
&-\Delta H_{gb}U-H_{gb}(g_F)d_\lambda
-\Delta H_{\lambda b}.
\end{aligned}}
\tag{18.11}
\]

**증명.** 합성함수 \(r=H(g_2;\lambda,b)\)의 mixed 미분은
\(r_{\lambda b}=J_yW+\mathcal B(g_2;U,V)\)다. 식 (18.8)에 \(J_FW=(J_y-L)W\)와 이 식을 대입한다. 남은 같은 Hessian의 bilinear 차이는

\[
H_{gg}(g_F)[U,V]-H_{gg}(g_F)[U_F,V_F]
=H_{gg}(g_F)[d_\lambda,V]+H_{gg}(g_F)[U_F,d_b].
\tag{18.12}
\]

mixed gas/parameter 항은 선형 차이로 분리된다. 원 \(\Delta H_{\lambda b}=0\)를 마지막에 적용한다. □

### 4.1 \(C^2\) Hessian 공간차의 포함

같은 Hessian 성분의 두 값이 원 signed interval \([\underline K,\overline K]\)에 속하면

\[
\Delta K\in
[\underline K-\overline K,\ \overline K-\underline K].
\tag{18.13}
\]

더 좁은 두 endpoint 포함이 있으면 그 차와 교차할 수 있다. 이 식은 \(C^2\)에서 바로 유효하며 \(U,V\)의 곱에 곱한 실제 폭을 계산한다. \(\Delta K=O(\|d\|)\)의 수치 상수는 여기서 가정하지 않는다. 이번 실제 계산에서는 이 signed source Hessian 차이의 온도 기여 폭이 약 \(4.58\times10^{-16}\,\mathrm K\)여서 음의 혼합 부호를 닫는 데 충분했다.

원 source 분해를 먼저 사용하면

\[
\Delta H_{gg}
=-2h\{\Delta F^{np}_{2,gg}+\lambda\nu_H\Delta q_{2,gg}\}
+\Delta H_{gg,\mathrm{ph}}.
\tag{18.14}
\]

같은 \(\lambda\)는 Hessian 두 개를 독립적으로 빼기 전에 인수로 남긴다. 팽창항은 \(w\)에 선형이어서 이 Hessian 차이에 기여하지 않는다.

### 4.2 공통 Hessian의 대칭성과 균형 표현

모든 bilinear \(K\)에 대해 \(\bar U=(U+U_F)/2\), \(\bar V=(V+V_F)/2\)라 두면

\[
\boxed{\begin{aligned}
K[U,V]-K[U_F,V_F]
&=K[d_\lambda,V]+K[U_F,d_b]\\
&=K[d_\lambda,V_F]+K[U,d_b]\\
&=K[d_\lambda,\bar V]+K[\bar U,d_b].
\end{aligned}}
\tag{18.15}
\]

**증명.** 각 오른쪽을 전개하면 모두
\(K[U,V]-K[U-d_\lambda,V-d_b]\)가 된다. □

실제 Hessian은 \(C^2\)에서 \(K_{jk}=K_{kj}\)이므로 coefficient matrix \(A\)와의 contraction을

\[
\sum_{j,k}K_{jk}A_{jk}
=\sum_jK_{jj}A_{jj}
+\sum_{j<k}K_{jk}(A_{jk}+A_{kj})
\tag{18.16}
\]

로 계산할 수 있다. 같은 Hessian 성분을 한 번만 interval로 평가하는 식이다. 식 (18.15)의 세 표현과 (18.16)를 각각 포함으로 구성한 교집합은 원 \(C^2\) 전제에서 유효하다. 이 균형 표현은 추가 tightening 경로이며 주 수치 부호는 원 직접·상관 포함으로 이미 닫혔다.

## 5. 정리 3 — HI·HH endpoint 공간차의 정확한 인수 분해

\(\ell_j=2ha_{2j}\), \(D_{yj}=1+\ell_j(1-x_2)\),
\(D_{Fj}=D_{yj}+\ell_jd_x\)라 둔다. Full incoming은
\(Q_F=R_FZ_0+2bJ_\gamma\)다. \(a_{2j}=cn_2\sigma_j\)이고 guard에서는 0이다.

\[
H_{gg,\mathrm{ph}}(g)
=2\sum_j\frac{\ell_j^2Q_{Fj}}{D_j^3}
\nu_j e_x^T\otimes e_x^T,\quad
H_{gb}(g)=2\sum_j\frac{\ell_jJ_{\gamma j}}{D_j^2}
\nu_j e_x^T.
\tag{18.17}
\]

따라서

\[
\boxed{
\Delta H_{gg,\mathrm{ph}}
=2\sum_j
\frac{\ell_j^3Q_{Fj}d_x(D_{Fj}^2+D_{Fj}D_{yj}+D_{yj}^2)}
{D_{yj}^3D_{Fj}^3}
\nu_j e_x^T\otimes e_x^T,
}
\tag{18.18}
\]

\[
\boxed{
\Delta H_{gb}
=2\sum_j
\frac{\ell_j^2J_{\gamma j}d_x(D_{Fj}+D_{yj})}
{D_{yj}^2D_{Fj}^2}\nu_j e_x^T,
}
\tag{18.19}
\]

\[
\boxed{
\Delta H_{g\lambda}
=-2h\nu_H\otimes
\int_0^1D^2q_2(g_2-td)[d,\cdot]\,dt.
}
\tag{18.20}
\]

**증명.** \(L_F=1-D^{-1}\)에서 \(L_{F,x}=-\ell D^{-2}\),
\(L_{F,xx}=-2\ell^2D^{-3}\)다. \(H_{\mathrm{ph}}=-V_{\mathrm{ph}}L_FQ_F\)를 미분해 (18.17)을 얻는다. 분모 차이
\[
D_y^{-m}-D_F^{-m}
=\frac{(D_F-D_y)\sum_{a=0}^{m-1}D_F^{m-1-a}D_y^a}
{D_y^mD_F^m}
\]
에서 \(m=3,2\)와 \(D_F-D_y=\ell d_x\)를 대입하면 (18.18)–(18.19)가 성립한다. 식 (18.20)은 \(H_{g\lambda}=-2h\nu_HDq_2\)의 선분 기본정리다. □

식 (18.19)의 2는 Full \(Q_{F,b}=2J_\gamma\)에서 온다. 이 항들을 원 residual의 G_gg, G_g_b, G_g_lambda 범위와 교차할 수 있다. 같은 \(d_x\)를 식 전체에서 보존한다.

## 6. 정리 4 — stage mixed residual의 구성

식 (18.4)을 더해 Full 잔차에 대입하면

\[
r=h\{B_1(g_1)-B_2(g_2)\}
+V_{\mathrm{ph}}(P_1+P_2-\widehat P_F),
\quad
\widehat P_F=L_F(g_2)Q_F.
\tag{18.21}
\]

gas 부분의 혼합 미분은

\[
\boxed{\begin{aligned}
r_{g,\lambda b}=h\{&
B_{1,g}W_1-B_{2,g}W\\
&+B_{1,gg}[U_1,V_1]-B_{2,gg}[U,V]\\
&+(Dq_1V_1-Dq_2V)\nu_H\}.
\end{aligned}}
\tag{18.22}
\]

**증명.** \(B_k(g_k(\lambda,b),\lambda)\)의 \(\lambda/b\) 총 미분은
\(B_{k,g}W_k+B_{k,gg}[U_k,V_k]+Dq_kV_k\nu_H\)다.
고정 gas \(B_{k,g\lambda}=Dq_k\nu_H\), \(B_{k,gb}=B_{k,\lambda b}=0\)를 사용했다. 이 정확한 식을 두 stage의 차이에 적용한다. □

\(\delta B_t(g)=B_1(g)-B_2(g)\),
\(\delta q_t(g)=q_1(g)-q_2(g)\)로 두면

\[
\boxed{\begin{aligned}
B_{1,g}(g_1)W_1-B_{2,g}(g_2)W
={}&D\delta B_t(g_1)W_1-B_{2,g}(g_2)s_{\lambda b}\\
&-\int_0^1B_{2,gg}(g_1+ts)[s,W_1]\,dt,
\end{aligned}}
\tag{18.23}
\]

\[
\boxed{\begin{aligned}
B_{1,gg}[U_1,V_1]-B_{2,gg}[U,V]
={}&(B_{1,gg}-B_{2,gg})[U_1,V_1]\\
&-B_{2,gg}[s_\lambda,V_1]-B_{2,gg}[U,s_b],
\end{aligned}}
\tag{18.24}
\]

\[
\boxed{\begin{aligned}
Dq_1(g_1)V_1-Dq_2(g_2)V
={}&D\delta q_t(g_1)V_1-Dq_2(g_2)s_b\\
&-\int_0^1D^2q_2(g_1+ts)[s,V_1]\,dt.
\end{aligned}}
\tag{18.25}
\]

식 (18.23), (18.25)는 같은 함수의 gradient 차이를 먼저 선분 적분으로 묶은 결과다. 식 (18.24)는 bilinearity로 직접 전개된다. \(\bar U_{12}=(U+U_1)/2\), \(\bar V_{12}=(V+V_1)/2\)를 쓰면 (18.24)의 마지막 두 항은
\[
-B_{2,gg}[s_\lambda,\bar V_{12}]
-B_{2,gg}[\bar U_{12},s_b]
\tag{18.26}
\]
와 같다. 단계 Hessian 차이는 해당 first-half/full signed 포함으로 평가한다.

### 6.1 source 시각 gradient의 원 \(C^2\) 연결

PHYS17에서 증명한 density/temperature pullback을 재사용한다. \(f_i=\operatorname{exact}(n_{\mathrm{He},i}^{stored})/\operatorname{exact}(n_i)\),
\(e_i=x+f_i(y+2z)\), \(\Pi_i=1+f_i+e_i\),
\(\Delta f=f_1-f_2\), \(r_n=n_1/n_2\)라 두고

\[
\Psi(g)=g+\delta w\,e_w,\quad
\delta w=-\frac{w\Delta f(1+y+2z)}{\Pi_1},
\quad r_e=\frac{n_1e_1}{n_2e_2}.
\tag{18.27}
\]

동일 온도 \(T_2(\Psi g)=T_1(g)\)를 맞추면

\[
F_1^{np}(g)
=r_eF_2^{np}(\Psi g)
+n_1e_1\Delta f\,k_{\mathrm{He}}(\Psi g)e_w,\quad
q_1(g)=r_nq_2(\Psi g).
\tag{18.28}
\]

이를 방향 \(v\)로 한 번 미분한 정확한 차이는

\[
\begin{aligned}
D\delta F^{np}[v]
={}&(r_e-1)DF_2^{np}(g)[v]+Dr_e[v]F_2^{np}(\Psi g)\\
&+r_e\delta w\int_0^1D^2F_2^{np}(g+t\delta w e_w)[e_w,v]\,dt\\
&+r_eDF_2^{np}(\Psi g)[e_w]D\delta w[v]\\
&+n_1\Delta f\{De_1[v]k_{\mathrm{He}}(\Psi g)
+e_1D(k_{\mathrm{He}}\circ\Psi)[v]\}e_w,
\end{aligned}
\tag{18.29}
\]

\[
\begin{aligned}
D\delta q_t[v]
={}&(r_n-1)Dq_2(g)[v]\\
&+r_n\delta w\int_0^1D^2q_2(g+t\delta w e_w)[e_w,v]\,dt\\
&+r_nDq_2(\Psi g)[e_w]D\delta w[v].
\end{aligned}
\tag{18.30}
\]

\(D\delta B_t[v]=D\delta F^{np}[v]+\lambda D\delta q_t[v]\nu_H\)에서 방향 \(v\)는 gas 방향으로 취한다. \(H_1=H_2\)인 원 captured 자료에서 source 시각 팽창차는 0이다.

원 He thermal projector는
\[
\mathscr U=\frac{F_{2,w}^{np}+\chi_HF_{2,x}^{np}}{n_2e_2},
\quad \xi=e_x+\frac{w}{\Pi_2}e_w,\quad
k_{\mathrm{He}}=\frac{\mathscr U-xD\mathscr U[\xi]}{f_2}.
\tag{18.31}
\]
\(DT_2[\xi]=0\)이며,
\[
Dk_{\mathrm{He}}[v]
=\frac{D\mathscr U[v]-v_xD\mathscr U[\xi]
-x\{D^2\mathscr U[v,\xi]+D\mathscr U[D\xi[v]]\}}{f_2}.
\tag{18.32}
\]
따라서 (18.29)의 첫 방향 미분에는 원 nonphoto 값·gradient·Hessian만 필요하다. 이번 mixed residual에서는 (18.29)를 \(v=W_1\)에 적용한다. 이 표현을 매개변수로 또 미분하는 절차를 사용하지 않는다. 원 signed Hessian의 단계 차이는 (18.24)에서 따로 포함한다.

## 7. 정리 5 — 일곱 광자 sector의 혼합 그래프

### 7.1 Primitive와 mixed product

\[
\begin{gathered}
Q_1=RZ_0+bJ_\gamma,\quad Z_1=A_1Q_1,\quad
Q_2=RZ_1+bJ_\gamma,\quad P_2=LQ_2,\\
\tau_j=ha_{2j}(1-x_2),\quad
A=(I+\tau)^{-1},\quad L=I-A,\\
A_F=(I+2\tau)^{-1},\quad L_F=I-A_F,\quad
C_1=\tau A^2A_F,\quad C_2=\tau^2A^2A_F.
\end{gathered}
\tag{18.33}
\]

diagonal 연산은 성분별이다. 고정 선형 \(R\)와 diagonal \(A\)의 순서를 유지한다. \(R_F=R(\rho^2)\), \(\Delta R=R^2-R_F\)다. 원 node remap에서 일반적으로 \(R^2\)와 \(R_F\)는 다른 행렬이다.

스칼라·벡터·행렬의 순서 있는 곱에 대해

\[
(AB)_{\lambda b}
=A_{\lambda b}B+A_\lambda B_b
+A_bB_\lambda+AB_{\lambda b}.
\tag{18.34}
\]

혼합 2-jet은 \((v,v_\lambda,v_b,v_{\lambda b})\)를 저장한다. 각 slot은 보통 도함수이며 mixed slot에 \(1/2\) 인수는 없다.

\[
\begin{aligned}
A_{k,\theta}&=ha_kA_k^2 g_{k,\theta,x},\\
A_{k,\lambda b}
&=ha_kA_k^2W_{k,x}
+2(ha_k)^2A_k^3U_{k,x}V_{k,x}.
\end{aligned}
\tag{18.35}
\]

Full survival에서는 \(ha_k\)를 \(2ha_2\)로 바꾸고 평가점의 \(U,V,W\)를 쓴다. \(L_\theta=-A_\theta\), \(L_{\lambda b}=-A_{\lambda b}\)다.

\[
Q_{1,\lambda}=0,\quad Q_{1,b}=J_\gamma,\quad
Q_{1,\lambda b}=0.
\tag{18.36}
\]

\[
\begin{gathered}
\zeta_j=h\{c\sigma_j(n_2-n_1)(1-x_2)-a_{1j}s_x\},\\
\Delta A_{1j}:=A_{1j}-A_j=\zeta_jA_{1j}A_j,\\
\zeta_{j,\theta}
=-h\{c\sigma_j(n_2-n_1)g_{2,\theta,x}+a_{1j}s_{\theta,x}\},\\
\zeta_{j,\lambda b}
=-h\{c\sigma_j(n_2-n_1)W_x+a_{1j}s_{\lambda b,x}\}.
\end{gathered}
\tag{18.37}
\]

**증명.** \(A_1-A=(D_2-D_1)/(D_1D_2)\)이고
\(D_2-D_1=h\{c\sigma(n_2-n_1)(1-x_2)-a_1(x_2-x_1)\}\)다. 나머지는 두 번의 scalar differentiation이다. □

### 7.2 일곱 sector와 명시적 mixed 식

정확한 광자 잔차 \(p=P_1+P_2-\widehat P_F\)는

\[
\boxed{\begin{aligned}
p={}&-(I-LR)\Delta A_1Q_1+L[R,A]Q_1\\
&+L(I-R)RZ_0+C_2R^2Z_0+L_F\Delta R Z_0\\
&+bLA(R-I)J_\gamma-bC_1J_\gamma.
\end{aligned}}
\tag{18.38}
\]

이는 PHYS15의 같은 흡수 chronology를 재사용한 식이다. 각 항의 혼합식은 다음과 같이 직접 전개된다. \(D=\Delta A_1Q_1\), \(K=[R,A]Q_1\),
\(J_R=(R-I)J_\gamma\), \(Z_R=(I-R)RZ_0\)라 두면

\[
\begin{gathered}
D_\lambda=\Delta A_{1,\lambda}Q_1,\quad
D_b=\Delta A_{1,b}Q_1+\Delta A_1J_\gamma,\\
D_{\lambda b}=\Delta A_{1,\lambda b}Q_1
+\Delta A_{1,\lambda}J_\gamma,\\
K_\lambda=[R,A_\lambda]Q_1,\quad
K_b=[R,A_b]Q_1+[R,A]J_\gamma,\\
K_{\lambda b}=[R,A_{\lambda b}]Q_1+[R,A_\lambda]J_\gamma.
\end{gathered}
\tag{18.39}
\]

\[
\begin{aligned}
p_{\mathrm{opacity},\lambda b}
={}&-D_{\lambda b}+L_{\lambda b}RD
+L_\lambda RD_b+L_bRD_\lambda+LRD_{\lambda b},\\
p_{\mathrm{comm},\lambda b}
={}&L_{\lambda b}K+L_\lambda K_b+L_bK_\lambda+LK_{\lambda b},\\
p_{\mathrm{stockR},\lambda b}
={}&L_{\lambda b}Z_R,\\
p_{\mathrm{stockBE},\lambda b}
={}&C_{2,\lambda b}R^2Z_0,\\
p_{\mathrm{remap},\lambda b}
={}&L_{F,\lambda b}\Delta RZ_0,\\
p_{\mathrm{birthR},\lambda b}
={}&\{(LA)_\lambda+b(LA)_{\lambda b}\}J_R,\\
p_{\mathrm{birthBE},\lambda b}
={}&-\{C_{1,\lambda}+bC_{1,\lambda b}\}J_\gamma.
\end{aligned}
\tag{18.40}
\]

**증명.** 식 (18.34)를 (18.38)의 각 순서 있는 곱에 적용한다. \(Z_0,R,R_F,J_\gamma\)는 매개변수에서 고정이다. \(b\)를 명시적으로 가진 마지막 두 항에서는 \(b_b=1\), \(b_\lambda=b_{\lambda b}=0\)이므로 표시된 직접 \(\lambda\)-도함수 항이 남는다. □

\(b=0\)에서 birth sector의 값은 0이지만 mixed 응답의 \((LA)_\lambda J_R\), \(-C_{1,\lambda}J_\gamma\)는 일반적으로 남는다. 이들은 HH가 opacity를 바꾸어 새 birth 광자의 흡수를 바꾸는 직접 혼합 작용이다.

### 7.3 mixed stage increment와 원 carry의 교차

두 번째 단계식의 mixed 미분으로

\[
\boxed{
s_{\lambda b}
=h\{B_{2,g}W+B_{2,gg}[U,V]+Dq_2[V]\nu_H\}
+V_{\mathrm{ph}}P_{2,\lambda b}.
}
\tag{18.41}
\]

이 포함을 원 \(W-W_1\)과 교차한다. \(Q_1,Z_1,Q_2,P_2\)의 value·\(\lambda\)·\(b\)·mixed slot도 원 PHYS11/14 carry 포함과 교차한다. 이 방식은 광자 그래프와 implicit gas carry가 공유하는 같은 해를 유지한다. Guard에서는 \(A=1,L=0\)과 모든 absorption 도함수 0을 그대로 사용한다.

### 7.4 혼합 number·energy ledger

\(\Delta\widehat Z=Z_2-A_F(g_2)Q_F\)라 하자. \(n_\gamma\)는 number guard를 포함한 총 number row, \(u_\gamma\)는 energy guard를 포함한 총 energy row다. \(E\), \(\mathbf1\)은 실제 광자 absorption 33개 성분에 작용한다. 그러면

\[
\boxed{\begin{aligned}
\mathbf1^Tp_{\lambda b}&=-n_\gamma\Delta\widehat Z_{\lambda b},\\
E^Tp_{\lambda b}
&=(1-\rho)E^TP_{1,\lambda b}
-u_\gamma\Delta\widehat Z_{\lambda b}.
\end{aligned}}
\tag{18.42}
\]

**증명.** PHYS15 number·energy ledger의 정확한 식을 두 번 미분한다. 원 energy chronology의 직접 birth 항
\(-(1-\rho)bM_\gamma E_{24}\)는 \(b\)에 affine이므로 mixed 미분이 0이다. \(R\)의 원 guard 보존과 energy scaling, 그리고 fixed \(\rho\)가 나머지 항을 준다. □

실제 Full photon endpoint 차이는
\[
\Delta Z_j=\Delta\widehat Z_j+\Gamma_jd_x,\qquad
\Gamma_j=\frac{\ell_jQ_{Fj}}{D_{yj}D_{Fj}}
\]
이므로
\[
\boxed{
\Delta Z_{j,\lambda b}
=\Delta\widehat Z_{j,\lambda b}
+\Gamma_jW_{d,x}
+\Gamma_{j,\lambda}d_{b,x}
+\Gamma_{j,b}d_{\lambda,x}
+\Gamma_{j,\lambda b}d_x.
}
\tag{18.43}
\]
\(\Gamma\)의 mixed slot은 양의 두 분모에 (18.34)를 적용하여 계산한다. Guard의 \(\Gamma\)는 0이다. 원 \(\epsilon_j=E_j-\chi_H\)에서 gas heat ledger는 (18.42)의 같은 선형 결합이다.

## 8. 정리 6 — 원 inverse majorant에 의한 포함

직접식 (18.8) 또는 상관식 (18.11)의 오른쪽을 \(f_{\lambda b}\)라 하자. 원 Full 조건

\[
|I-CJ_F|\le B,\quad B\ge0,\quad
\|S^{-1}BS\|_\infty\le q<1
\tag{18.44}
\]

을 사용한다. \(C\)는 원 fixed preconditioner, \(S\)는 원 radius의 diagonal matrix다. 원 저장값은 \(q=\operatorname{exact64}(0.00011736830563768177)\), radius는 원 exact64 값 \((0.015,0.01,0.01,0.5)\)다.

\[
m=(I-B)^{-1}\operatorname{mag}([Cf_{\lambda b}]),\qquad
\boxed{W_d\in[Cf_{\lambda b}]+[-Bm,Bm].}
\tag{18.45}
\]

**증명.** \(W_d=Cf_{\lambda b}+(I-CJ_F)W_d\)다. \(B\)의 가중 spectral radius가 1보다 작으므로 \((I-B)^{-1}=\sum_{k\ge0}B^k\ge0\).
\(|W_d|\le |Cf_{\lambda b}|+B|W_d|\)에서 \(|W_d|\le m\)을 얻어 원 식에 넣는다. □

세 포함을 구성하여

\[
[W_d]=[W_d]_{\mathrm{direct}}
\cap[W_d]_{\mathrm{corr}}
\cap([W]-[W_F])
\tag{18.46}
\]

로 교차한다. 이어 \([E_F]=[I-CJ_F]\)의 signed 포함으로
\[
[W_d]\leftarrow[W_d]\cap
\{[Cf_{\lambda b}]+[E_F][W_d]\}
\tag{18.47}
\]
를 유한 횟수 적용할 수 있다. 원 \(B,q,S\)는 바꾸지 않는다.

같은 \(J_F\)에 대한 finite Neumann 예측
\[
\widehat W_m=\sum_{k=0}^mE_F^kCf_{\lambda b},\qquad
a=\frac{\|Cf_{\lambda b}\|_S}{1-q}
\]
에는
\[
\|W_d-\widehat W_m\|_S\le q^{m+1}a
\tag{18.48}
\]
가 따른다. 이것은 inverse truncation 성분의 경계이며 입력 interval의 전체 물리 폭은 (18.45)–(18.47)에서 따로 유지한다.

## 9. 정리 7 — 정확한 유한 온도 mixed 응답

\[
\ell_e=(1,f,2f,0),\quad
C_T=\frac{2\,\epsilon_{\mathrm{eV}}}{3k_B},\quad
\Pi(g)=1+f+\ell_eg,\quad T(g)=C_Tw/\Pi(g).
\tag{18.49}
\]

\(d_e=\ell_ed\), \(\Pi_2=\Pi(g_2)\), \(P=\Pi_F=\Pi_2-d_e\),
\(T_2=T(g_2)\)라 두면

\[
F=\frac{N}{P},\qquad N=C_Td_w-T_2d_e.
\tag{18.50}
\]

각 1차 \(\theta\)에 대해 \(P_\theta=\ell_e(g_{2,\theta}-d_\theta)\),
\(P_{\lambda b}=\ell_e(W-W_d)\)다. \(N=FP\)를 두 번 미분하면

\[
\boxed{
F_{\lambda b}
=\frac{N_{\lambda b}-F_\lambda P_b-F_bP_\lambda-FP_{\lambda b}}{P},
}
\tag{18.51}
\]

\[
N_{\lambda b}
=C_TW_{d,w}-T_2\ell_eW_d
-T_{2,\lambda b}d_e
-T_{2,\lambda}d_{e,b}-T_{2,b}d_{e,\lambda}.
\tag{18.52}
\]

같은 Full 온도 \(T_F=T_2-F\)와 공통 covector
\(n_F=C_Te_w^T-T_F\ell_e\)를 사용하면

\[
\boxed{\begin{aligned}
F_{\lambda b}=\frac1{\Pi_F}\{&
n_FW_d-T_{2,\lambda b}d_e
-T_{2,\lambda}d_{e,b}-T_{2,b}d_{e,\lambda}\\
&-F_\lambda P_b-F_bP_\lambda-F\ell_eW\}.
\end{aligned}}
\tag{18.53}
\]

두 번째 endpoint의 온도 혼합은

\[
\boxed{
T_{2,\lambda b}
=\frac{C_TW_w-T_2\ell_eW
-T_{2,\lambda}\ell_eV-T_{2,b}\ell_eU}{\Pi_2}.
}
\tag{18.54}
\]

**증명.** 식 (18.50)은 같은 \(\Pi_2,\Pi_F\)로 두 온도를 통분한 결과다. (18.51)은 \(N=FP\)의 mixed product rule, (18.52)은 \(N\)의 정의를 미분한 결과다. \(P_{\lambda b}=\ell_eW-\ell_eW_d\)를 (18.51)에 넣으면 \(W_d\)의 계수가
\(C_Te_w^T-(T_2-F)\ell_e=n_F\)가 되어 (18.53)을 얻는다.
\(C_Tw_2=T_2\Pi_2\)를 두 번 미분하면 (18.54)다. □

### 9.1 같은 adjoint에서의 기여 분해

\[
J_F^Tz_F=n_F^T,\qquad
\eta=-T_{2,\lambda b}d_e-T_{2,\lambda}d_{e,b}
-T_{2,b}d_{e,\lambda}
-F_\lambda P_b-F_bP_\lambda-F\ell_eW.
\]

\(f_{\lambda b}=\sum_a f_a\)이면

\[
\boxed{
F_{\lambda b}
=\sum_a\frac{z_F^Tf_a}{\Pi_F}+\frac{\eta}{\Pi_F}.
}
\tag{18.55}
\]

source 시각항, gas 이동·곡률, 일곱 photon sector, endpoint feedback, 온도 분모항을 이 하나의 \(z_F,\Pi_F\)에서 비교한다. 각각의 contribution interval은 같은 선형 functional의 포함이다. 성분을 따로 평가한 interval 폭의 합은 합계 폭보다 클 수 있으므로 dominance 판정은 실제 width decomposition과 함께 한다.

## 10. 정리 8 — 음의 interaction과 유한 rectangle

\[
\boxed{\begin{aligned}
\mathcal I
&=F(1,1)-F(1,0)-F(0,1)+F(0,0)\\
&=\int_0^1\!\int_0^1F_{\lambda b}(\lambda,b)\,db\,d\lambda.
\end{aligned}}
\tag{18.56}
\]

**증명.** \(C^2\)에서 \(F_{\lambda b}\)는 연속이다. 먼저 \(b\) 방향 기본정리를 \(F_\lambda\)에 적용하고, 이어 \(\lambda\) 방향으로 적분한다. 유한 닫힌 rectangle에서 적분 순서도 교환할 수 있다. □

전역 \(F_{\lambda b}\in[L_m,U_m]\)이면 \(\mathcal I\in[L_m,U_m]\)다. 더 일반적으로 \(\lambda_0\le\lambda_1\), \(b_0\le b_1\)인 subrectangle에서

\[
\begin{aligned}
&F(\lambda_1,b_1)-F(\lambda_1,b_0)
-F(\lambda_0,b_1)+F(\lambda_0,b_0)\\
&\hspace{2em}\in
(\lambda_1-\lambda_0)(b_1-b_0)[L_m,U_m].
\end{aligned}
\tag{18.57}
\]

실제 (18.1)의 \(U_m<0\)에서 양의 면적을 가진 모든 subrectangle의 interaction은 엄격히 음수다. 따라서 \(F\)는 이 rectangle에서 strictly submodular다. PHYS17의 전역 \(F_\lambda\) 폭에서 얻은
\[
|\mathcal I|\le1.958485175177039\times10^{-9}\,\mathrm{K}
\tag{18.58}
\]
보다 새 magnitude bound가 약 733.93배 작다.

### 10.1 marginal response의 정렬

\[
\begin{aligned}
F_\lambda(\lambda,b_1)-F_\lambda(\lambda,b_0)
&\in(b_1-b_0)[L_m,U_m],\\
F_b(\lambda_1,b)-F_b(\lambda_0,b)
&\in(\lambda_1-\lambda_0)[L_m,U_m].
\end{aligned}
\tag{18.59}
\]

이는 (18.57)에서 한 방향의 기본정리를 적용한 결과다. PHYS17의 \(F_\lambda<0\), \(F_b>0\)와 결합하면 birth 증가가 HH의 음의 결함 응답을 더 음으로 만들며, HH 증가는 birth의 양의 결함 응답을 조금 줄인다. \(F_{\lambda b}\)의 규모가 \(10^{-12}\,\mathrm K\)여서 이미 확립한 두 1차 부호는 유지된다.

### 10.2 축 응답을 보존한 교차항 재구성

축 위 실제 함수값을 그대로 사용하는 additive model
\[
F_{\mathrm{ax}}(\lambda,b)
=F(\lambda,0)+F(0,b)-F(0,0)
\]
에 대해
\[
\boxed{
F-F_{\mathrm{ax}}\in\lambda b[L_m,U_m],\qquad
|F-F_{\mathrm{ax}}|\le2.668505746423\times10^{-12}\lambda b\ {\rm K}.
}
\tag{18.60}
\]

**증명.** rectangle \([0,\lambda]\times[0,b]\)에 (18.57)을 적용한다. □

보고한 외향 decimal 포함의 중심과 반폭을
\[
c_m=-2.393651191234\times10^{-12}\ {\rm K},\qquad
r_m=2.748545551890\times10^{-13}\ {\rm K}
\tag{18.61}
\]
로 잡으면
\[
\boxed{
F=F_{\mathrm{ax}}+c_m\lambda b+R_m,\qquad
|R_m|\le r_m\lambda b.
}
\tag{18.62}
\]

이 결과는 현재 \(C^2\) mixed 포함으로 이미 성립한다. 축 함수 \(F(\lambda,0),F(0,b)\)의 자체 비선형성은 정확히 보존했다. 다음 단위에서 남은 두 pure curvature를 계산하면 축까지 직선으로 대체하는 bilinear interpolation의 오차를 따로 닫을 수 있다.

## 11. 실제 혼합 기작의 수치 해석

같은 \(J_F,n_F,\Pi_F\)를 적용한 readout01의 묶음별 결과는 다음과 같다. 모든 수치는 K다.

| 기여 묶음 | 외향 포함 |
|---|---|
| HH gradient 5개 항 | \([-2.329668009361,-1.928397581837]\times10^{-12}\) |
| 광자 chronology 7개 항 | \([-3.024678223968,-1.735793802686]\times10^{-13}\) |
| 나머지 gas·endpoint 항 | \([2.819648272515,11.40914739344]\times10^{-16}\) |
| 유한 온도 geometry | \([-3.666218766444,-1.794167181955]\times10^{-14}\) |

HH gradient의 가장 큰 두 항은 stage \(-hDq_2[s_b]\nu_H\)와 endpoint \(-H_{g\lambda}(g_F)d_b\)다. 각각
\[
[-1.167214625761,-0.9657458571171]\times10^{-12}\ {\rm K},
\]
\[
[-1.162669577536,-0.9632570909223]\times10^{-12}\ {\rm K}
\]
에 포함된다. 같은 birth parameter에 대한 stage 변화 \(s_b\)와 Full/two-half 차이 \(d_b\)가 HH source gradient를 통해 온도 결함의 혼합 응답으로 전달되는 기작이다. 광자 birth backward-Euler 항도
\([-2.162954512589,-1.072305628653]\times10^{-13}\,\mathrm K\)로 음의 기여다.

이 해석은 먼저 gas ionization·thermal 좌표로 forcing을 구성하고, 공통 Full inverse와 유한 온도 covector에 투영한 실제 결과에 근거한다. source Hessian 값의 차이는 가장 큰 폭 요인이 아니며 원 \(C^2\) 포함을 유지한 채 총 mixed 부호가 닫혔다.

## 12. 차원·부호·극한 검사

| 검사 | 식에서의 결과 |
|---|---|
| 단위 | \(\lambda,b\) 무차원; \(U,V,W,d_\theta,W_d\)는 gas 좌표 단위, \(F_{\lambda b},\mathcal I\)는 K |
| 시간 | \(hB\)는 gas 변화; Full source 잔차 Hessian은 \(-2h\) 포함 |
| HH 방향 | \(\nu_H=(1,0,0,-\chi_H)^T\); HH ionization과 thermal loss의 원 부호 유지 |
| photo 잔차 부호 | \(H_{\mathrm{ph}}=-V_{\mathrm{ph}}L_FQ_F\), \(L_{F,x}<0\)이므로 활성 \(x\)-열의 원 부호 유지 |
| Full birth 배수 | \(Q_{F,b}=2J_\gamma\); (18.19)의 2 보존 |
| Schwarz 대칭 | \(H_{gg,jk}=H_{gg,kj}\); \(\partial_{\lambda b}=\partial_{b\lambda}\) |
| 투명 극한 | \(\sigma=0\) 및 고정 COMMON에서 gas의 \(b\) dependence가 사라져 \(V,W,d_b,W_d,F_{\lambda b}=0\) |
| \(b=0\) | birth 값은 0, birth mixed 직접 항은 (18.40)에 따라 남음 |
| guard | absorption·opacity 도함수 0; number/energy ledger는 원 두 guard 포함 |
| 열 분모 | \(\Pi_2,\Pi_F>0\); 같은 exact \(f,C_T\)로 유한 quotient 구성 |

## 13. 근거·코딩 연결

contracts/ACTIVE_MIXED_RESPONSE_CONTRACT.json이 PHYS15–17 입력 identity와 이번 실행 범위를 결박한다. 직접·상관 RHS, 원 \(W-W_F\), mixed photon graph, 공통 finite temperature 분수는 서로 다른 정확한 표현에서 나온 inclusion이므로 교차할 수 있다. 실제 Wolfram/xAct 검산은 새 tensor contraction과 scalar quotient·photon 식을 대상으로 한다. 독립 검토는 원 입력, 새 유도 및 실제 interval 결과를 함께 평가한다.

이론식의 실제 수치 적용은 다음 연결을 완료한다.

1. 원 carry와 PHYS16/17의 \(d,d_\lambda,d_b,s,s_\lambda,s_b\)를 결박한다.
2. (18.35)–(18.41)의 mixed photon graph와 stage \(s_{\lambda b}\)를 구성한다.
3. (18.22)–(18.30) 및 photon sector로 \(r_{\lambda b}\)를 만들고 (18.8), (18.11)을 각각 계산한다.
4. (18.45)–(18.47)로 \(W_d\)를 포함하고 (18.53)–(18.55)의 같은 \(\Pi_F,J_F,n_F\)로 온도에 전달한다.
5. (18.56)–(18.62)의 interaction·marginal ordering·축 보존 교차항 오차를 평가한다.

다음 단위 HH_DEFECT_PARAMETER_CURVATURE는 두 pure response \(F_{\lambda\lambda},F_{bb}\)와 전체 rectangle bilinear interpolation 오차를 다룬다. NEXT_CURVATURE_PROPOSAL_KO.md와 CURVATURE_CONTRACT_DRAFT.json에 원 \(C^2\) 자료에서 출발하는 식·입력·수용 기준을 적었다. 새 pure-curvature 수치 실행은 다음 단위의 미실행 의무다.

이 단위는 source/root/history 재실행 없이 원 \(C^2\) 자료를 연결하여 음의 HH–birth 혼합 응답과 interaction을 얻었다. 새 strong no-go 명제를 주장하지 않는다. 채택 근거는 완결된 유도, 원 입력의 실제 포함 계산, 독립 검토, 새 Wolfram/xAct 실행이다.
