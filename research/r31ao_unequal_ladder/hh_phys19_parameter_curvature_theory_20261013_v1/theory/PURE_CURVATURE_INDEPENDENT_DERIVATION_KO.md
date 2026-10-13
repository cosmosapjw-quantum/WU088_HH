# WU088_HH PHYS19 — 순수 매개변수 곡률의 독립 유도와 검토

## 결과와 근거 상태

PHYS18의 고정된 같은-family 계약에서 다음 순수 응답 식을 독립적으로 유도했다. 첫 half와 Full의 implicit second derivative, carried 둘째 half의 순수 photon jet, 같은 Full Jacobian을 사용하는 endpoint 결함, 일곱 photon sector, 유한 온도 quotient, bilinear 보간 오차가 모두 원 `C2` 정칙성으로 연결된다. 검토한 C3–C20의 수학적 부호·계수는 아래 유도와 일치한다.

이 문서의 근거 상태는 `derived`이며, root가 제작하는 interval application과 독립적인 원식 기반 검토다. 이 분과에서는 새 source callback, nonlinear root, history replay, Wolfram 실행 또는 수치 application을 수행하지 않았다. 수치 구간·실행 판정은 해당 실행 결과와 합류한 뒤 별도로 붙인다.

실제 읽은 기준 문서와 SHA-256:

| 기준 | SHA-256 |
|---|---|
| `theory/NEXT_CURVATURE_PROPOSAL_KO.md` | `6181d5dc65cea93e150ccc469a098b0740ad6b099673ca12d9456cbaf7d4fa92` |
| `contracts/CURVATURE_CONTRACT.json` | `94e39ca1448e2658c966b17e4cd2db29cd0fbe7588d065e53161273955196c56` |
| `theory/MIXED_RESPONSE_THEOREM_KO.md` | `ce264e69de61ec397775eb91db036452c12eabd9e6c3109cb71bb8430c86a262` |

세 파일의 원본 root는 `/workspace/scratch/61df56c29001/work/phys18/HH_PHYS18_THEORY_20261013_v1`이다. 식 번호 C3–C20은 첫 문서, 식 번호 18.x는 마지막 문서에 대응한다.

## 1. 함수 계열과 정규화

하나의 admissible 물리 계수 선택 \(\alpha\), 같은 COMMON, 같은 전역 \((\lambda,b)\in[0,1]^2\)를 고정한다. 매개변수 미분 중에 \(\alpha\), 밀도·수송·상수 leaves, \(R,R_F,Z_0,J_\gamma\), 단계 길이 \(h=625000000\,\mathrm s\)는 고정이다. 원 source는 convex gas 영역과 필요한 연결 선분에서 \(C^2\)이고, 각 root branch는 원 Jacobian certificate로 정칙이다. 닫힌 parameter rectangle의 경계 미분에는 계약의 작은 열린 확장을 사용한다.

\[
g=(x,y,z,w),\quad [w]=\mathrm{eV/H},\qquad
\theta\in\{\lambda,b\},\quad
\delta_\lambda=\partial_\theta\lambda,\quad
\delta_b=\partial_\theta b.
\tag{D1}
\]

\((\delta_\lambda,\delta_b)\)는 각각 \((1,0)\) 또는 \((0,1)\)이다. 이하 prime은 같은 \(\theta\)에 관한 보통 도함수다.

\[
p_k=g_k',\qquad K_k=g_k'',\qquad
\nu_H=(1,0,0,-\chi_H)^T.
\tag{D2}
\]

순수 jet slot \(K_k\)에는 \(1/2!\)를 포함하지 않는다. Taylor 다항식을 출력하는 경우에만 \(g_k(\theta+\varepsilon)=g_k+\varepsilon p_k+\varepsilon^2K_k/2+o(\varepsilon^2)\)로 쓴다. PHYS09의 \(U,V\)는 각각 \(p_k\)의 입력이며, \(W\)는 혼합 \(\lambda b\) 응답으로 유지한다.

원 stage source는

\[
B_k(g,\lambda)=F_k^{np}(g)+\lambda q_k(g)\nu_H-2H_kw e_w.
\tag{D3}
\]

\(B_{k,gg}=F^{np}_{k,gg}+\lambda\nu_H D^2q_k\), \(B_{k,g\theta}=\delta_\lambda\nu_HDq_k\), \(B_{k,\theta\theta}=0\)이다. 팽창항은 \(B_{k,g}\)에는 기여하고 \(B_{k,gg}\)에는 0을 준다. 광자 사상 \(V_{\rm ph}\)의 활성 열은 \((1,0,0,\epsilon_j)^T\)다. 33개 활성 광자 node와 2개 guard를 모두 보존한다.

## 2. 첫 half·Full의 implicit second derivative

고정 incoming 형태의 단계 잔차를 \(H_k(g_k,\theta)=0\), \(J_k=H_{k,g}(g_k,\theta)\)라 쓰면 첫 미분은

\[
J_kp_k+H_{k,\theta}=0.
\tag{D4}
\]

이 식의 총 미분에서

\[
D_\theta J_k=H_{k,gg}[p_k,\cdot]+H_{k,g\theta},\qquad
D_\theta H_{k,\theta}=H_{k,\theta g}p_k+H_{k,\theta\theta}.
\]

\(C^2\) Schwarz 대칭 \(H_{\theta g}=H_{g\theta}\)를 쓰면

\[
\boxed{J_kK_k=-H_{k,gg}[p_k,p_k]-2H_{k,g\theta}p_k-H_{k,\theta\theta}.}
\tag{D5}
\]

이것이 C3다. Hessian은 출력 gas 인덱스 하나와 입력 gas 인덱스 둘을 가지는 bilinear map이다. 지표가 세 개라는 사실과 미분 차수는 구별된다.

첫 half와 Full의 incoming은 각각

\[
Q_1=RZ_0+bJ_\gamma,\qquad Q_F=R_FZ_0+2bJ_\gamma.
\tag{D6}
\]

고정 gas에서 \(H_k\)는 \(\lambda,b\)에 affine이므로 \(H_{k,\theta\theta}=0\)이다. 두 순수 응답의 source 형식을 명시하면

\[
\boxed{\begin{aligned}
J_1K_1={}&hB_{1,gg}[p_1,p_1]
+2h\delta_\lambda Dq_1[p_1]\nu_H\\
&+V_{\rm ph}\{L_{1,gg}[p_1,p_1]Q_1
+2\delta_bL_{1,g}[p_1]J_\gamma\},
\end{aligned}}
\tag{D7}
\]

\[
\boxed{\begin{aligned}
J_FK_F={}&2hB_{2,gg}[p_F,p_F]
+4h\delta_\lambda Dq_2[p_F]\nu_H\\
&+V_{\rm ph}\{L_{F,gg}[p_F,p_F]Q_F
+4\delta_bL_{F,g}[p_F]J_\gamma\}.
\end{aligned}}
\tag{D8}
\]

Full의 마지막 계수 4는 product-rule 계수 2와 \(Q_{F,b}=2J_\gamma\)의 곱이다. Full source의 HH 계수 4는 순수 미분 계수 2와 단계 길이 \(2h\)에서 나온다.

`SOURCE_BOX/G_gg`, `G_g_lambda`, `G_g_b`는 이미 잔차 미분이다. 이 입력을 쓰는 계산식은 D5의 \(-G_{gg}[p,p]-2G_{g\theta}p\)이며, 시간 인수·잔차 부호를 다시 넣지 않는다. `SOURCE_BOX_COMPONENTS/nonphoto/signed_hessian`을 쓰는 source 분해에서는 D7–D8의 시간 인수를 적용한다.

## 3. survival과 carried 순수 photon 응답

각 활성 slot에서

\[
a_{kj}=cn_k\sigma_j,\qquad
\tau_{kj}=ha_{kj}(1-x_k),\qquad
A_{kj}=(1+\tau_{kj})^{-1},\qquad L_{kj}=1-A_{kj}.
\tag{D9}
\]

\(a_{kj}\)는 \(\mathrm{s}^{-1}\), \(\tau,A,L\)은 무차원이다. \(\tau'=-ha p_x\), \(\tau''=-ha K_x\)를 대입하면

\[
A'=haA^2p_x,\qquad
\boxed{A''=haA^2K_x+2(ha)^2A^3p_x^2},\qquad L'=-A',\quad L''=-A''.
\tag{D10}
\]

Full survival에는 \(ha\)를 \(2ha_2\)로 바꾼다. D10은 C6과 일치한다.

첫 half의 outgoing \(Z_1=A_1Q_1\)과 둘째 incoming \(Q_2=RZ_1+bJ_\gamma\)는

\[
\begin{aligned}
Q_1'&=\delta_bJ_\gamma,& Q_1''&=0,\\
Z_1'&=A_1'Q_1+\delta_bA_1J_\gamma,&
Z_1''&=A_1''Q_1+2\delta_bA_1'J_\gamma,\\
Q_2'&=RZ_1'+\delta_bJ_\gamma,&
\boxed{Q_2''&=R\{A_1''Q_1+2\delta_bA_1'J_\gamma\}.}
\end{aligned}
\tag{D11}
\]

이는 C5–C7이다. \(b=0\)에서도 \(\theta=b\)이면 D11의 \(2A_1'J_\gamma\)가 남는다. 한 번 생성된 광자의 생존확률도 같은 \(b\)에 반응하기 때문이다. \(R\)와 diagonal \(A\)의 순서는 바꾸지 않는다.

guard slot에서 국소 absorption은 \(L=0\), survival은 \(A=1\)이며 \(A'=A''=L'=L''=0\)이다. 그러나

\[
(Q_2'')_{\rm guard}=(RZ_1'')_{\rm guard}
\tag{D12}
\]

는 remap이 활성 slot을 guard로 보내면 남을 수 있다. incoming/outgoing guard의 응답은 원 remap으로 계산하고, absorption guard의 응답만 0으로 유지한다.

## 4. 둘째 half의 순수 gas 응답과 선형 solve

실제 둘째 stage 식은

\[
g_2-g_1=hB_2(g_2,\lambda)+V_{\rm ph}L_2(g_2)Q_2(\lambda,b).
\tag{D13}
\]

\(p=p_2\)로 쓰자. photon 항의 두 번째 총 미분을 먼저 모두 전개하면

\[
P_2''=L_{2,g}[K_2]Q_2+L_{2,gg}[p,p]Q_2
+2L_{2,g}[p]Q_2'+L_2Q_2''.
\tag{D14}
\]

따라서 \(J_2=I-hB_{2,g}-V_{\rm ph}(L_{2,g}Q_2)\)에서

\[
\boxed{\begin{aligned}
J_2K_2={}&K_1+hB_{2,gg}[p,p]
+2h\delta_\lambda Dq_2[p]\nu_H\\
&+V_{\rm ph}\{L_{2,gg}[p,p]Q_2
+2L_{2,g}[p]Q_2'+L_2Q_2''\}.
\end{aligned}}
\tag{D15}
\]

이 식은 C8이다. 먼저 D5에서 \(K_1\), 이어 D11에서 \(Q_2''\), 마지막으로 D15에서 \(K_2\)를 포함한다. \(L_{2,g}[K_2]Q_2\)는 Jacobian에 배치되어 있다. D15의 RHS에 이 항을 또 넣지 않는다. \(K_2\)를 구한 뒤 실제 \(P_2''\)를 저장할 때 D14 전체를 사용한다.

단계 차이 \(s=g_2-g_1\), \(s_\theta=p-p_1\), \(s_{\theta\theta}=K_2-K_1\)는 같은 stage 식에서

\[
\boxed{s_{\theta\theta}
=h\{B_{2,g}K_2+B_{2,gg}[p,p]+2\delta_\lambda Dq_2[p]\nu_H\}
+V_{\rm ph}P_2''.}
\tag{D16}
\]

따라서 D16과 \([K_2]-[K_1]\)의 교집합을 사용할 수 있다. 이 단계 차이가 후속 cancellation-preserving 식에 들어간다.

## 5. 같은 Full 역연산자로 전달하는 순수 endpoint 결함

Full 잔차를

\[
H(g;\lambda,b)=g-g_0-2hB_2(g,\lambda)-V_{\rm ph}L_F(g)Q_F(b)
\tag{D17}
\]

로 두고 \(r=H(g_2;\lambda,b)\), \(d=g_2-g_F\), \(d_\theta=p-p_F\), \(K_d=K_2-K_F\)라 쓴다. Full root와 two-half endpoint의 gas Jacobian은 각각 \(J_F=H_g(g_F)\), \(J_y=H_g(g_2)\)다.

D5의 Full 식을 \(K_d=K_2-K_F\)에 대입하면 직접식

\[
\boxed{J_FK_d=J_FK_2+H_{gg}(g_F)[p_F,p_F]+2H_{g\theta}(g_F)p_F}
\tag{D18}
\]

를 얻는다. \(r\)의 두 번째 미분은

\[
r''=J_yK_2+H_{gg}(g_2)[p,p]+2H_{g\theta}(g_2)p.
\tag{D19}
\]

\[
\begin{gathered}
L=J_y-J_F,\qquad
\Delta H_{gg}=H_{gg}(g_2)-H_{gg}(g_F),\\
\Delta H_{g\theta}=H_{g\theta}(g_2)-H_{g\theta}(g_F),\qquad
\bar p_F=(p+p_F)/2=p-d_\theta/2.
\end{gathered}
\tag{D20}
\]

대칭 bilinear map \(\mathsf K\)에 대해

\[
\begin{aligned}
\mathsf K[p,p]-\mathsf K[p_F,p_F]
&=\mathsf K[d_\theta,p]+\mathsf K[p_F,d_\theta]\\
&=2\mathsf K[d_\theta,\bar p_F].
\end{aligned}
\tag{D21}
\]

D19를 D18에 넣고 D21로 묶으면

\[
\boxed{\begin{aligned}
J_FK_d={}&r''-LK_2-\Delta H_{gg}[p,p]
-2H_{gg}(g_F)[d_\theta,\bar p_F]\\
&-2\Delta H_{g\theta}p-2H_{g\theta}(g_F)d_\theta.
\end{aligned}}
\tag{D22}
\]

이는 C9–C10이다. 직접식과 상관식은 동일한 \(J_FK_d\)의 표현이므로 그 RHS 포함과 inverse 적용 후의 포함을 각각 교차할 수 있다. \(J_y^{-1}\)로 바꾸면 D22의 식 자체를 다시 유도해야 한다. 현재 계약의 계산은 원 \(J_F\)를 사용한다.

### 5.1 \(C^2\) Hessian 차이와 대칭 contraction

\(L\)은 기본정리로

\[
L=\int_0^1H_{gg}(g_2-td)[d,\cdot]\,dt
\tag{D23}
\]

이다. 반면 \(\Delta H_{gg}\)의 일반 source 성분에는 원 두 평가점의 signed Hessian 포함을 사용한다. 같은 성분의 범위가 \([a,b]\)이면 차이는 \([a-b,b-a]\)에 속한다. 원 endpoint-specific 포함이 있으면 이를 교차한다. \(C^3\) 또는 Hessian Lipschitz 상수는 추가하지 않는다.

같은 \(\lambda\)를 유지한 source 분해는

\[
\Delta H_{gg}=-2h\{\Delta F^{np}_{2,gg}+\lambda\nu_H\Delta D^2q_2\}
+\Delta H_{gg,\rm ph}.
\tag{D24}
\]

HI rational photo 항은 PHYS18의 정확한 분모차 식으로 \(d_x\)를 인수로 보존한다. HH gas/parameter 항에는

\[
\Delta H_{g\lambda}
=-2h\nu_H\int_0^1D^2q_2(g_2-td)[d,\cdot]\,dt
\tag{D25}
\]

를 사용한다. \(\theta=b\)의 \(\Delta H_{gb}\)에는 원 Full \(Q_{F,b}=2J_\gamma\)와 HI rational 분모차가 들어간다.

대칭 Hessian과 계수행렬의 contraction은

\[
\sum_{j,k}\mathsf K_{jk}A_{jk}
=\sum_j\mathsf K_{jj}A_{jj}
+\sum_{j<k}\mathsf K_{jk}(A_{jk}+A_{kj})
\tag{D26}
\]

로 평가할 수 있다. 특히 D21에서

\[
2\mathsf K[d,\bar p]
=2\sum_j\mathsf K_{jj}d_j\bar p_j
+2\sum_{j<k}\mathsf K_{jk}(d_j\bar p_k+d_k\bar p_j).
\tag{D27}
\]

동일한 signed Hessian 성분을 한 번만 평가하므로 interval dependency 감소를 기대할 수 있다. \(\bar p_F\)도 \((p+p_F)/2\), \(p-d_\theta/2\), \(p_F+d_\theta/2\)의 교집합으로 포함한다. 각 표현은 원 exact relation에서 왔으며 추가 정칙성 전제가 없다.

## 6. 실제 stage 순서의 gas 잔차

두 stage 식을 더하면

\[
r=h\{B_1(g_1)-B_2(g_2)\}+V_{\rm ph}p_{\rm ph},\qquad
p_{\rm ph}=P_1+P_2-L_F(g_2)Q_F.
\tag{D28}
\]

gas 부분의 pure derivative는

\[
\boxed{\begin{aligned}
r_g''=h\{&B_{1,g}K_1-B_{2,g}K_2
+B_{1,gg}[p_1,p_1]-B_{2,gg}[p,p]\\
&+2\delta_\lambda(Dq_1[p_1]-Dq_2[p])\nu_H\}.
\end{aligned}}
\tag{D29}
\]

\(\delta B_t(g)=B_1(g)-B_2(g)\), \(\delta q_t(g)=q_1(g)-q_2(g)\)라 두면 첫 gradient 차이는

\[
\boxed{\begin{aligned}
B_{1,g}(g_1)K_1-B_{2,g}(g_2)K_2
={}&D\delta B_t(g_1)[K_1]-B_{2,g}(g_2)s_{\theta\theta}\\
&-\int_0^1B_{2,gg}(g_1+ts)[s,K_1]\,dt.
\end{aligned}}
\tag{D30}
\]

이는 \(B_{2,g}(g_1)K_1\)를 더하고 빼서 얻는다. 다음으로 \(\Delta B_{gg}=B_{1,gg}(g_1)-B_{2,gg}(g_2)\), \(\bar p_{12}=(p+p_1)/2\)라 두면

\[
\boxed{B_{1,gg}[p_1,p_1]-B_{2,gg}[p,p]
=\Delta B_{gg}[p_1,p_1]-2B_{2,gg}[s_\theta,\bar p_{12}].}
\tag{D31}
\]

HH gradient 차이는

\[
\boxed{\begin{aligned}
Dq_1(g_1)[p_1]-Dq_2(g_2)[p]
={}&D\delta q_t(g_1)[p_1]-Dq_2(g_2)[s_\theta]\\
&-\int_0^1D^2q_2(g_1+ts)[s,p_1]\,dt.
\end{aligned}}
\tag{D32}
\]

D29–D32는 C11–C12와 일치한다. PHYS17의 first density/temperature-pullback derivative를 D30에는 방향 \(v=K_1\), D32에는 \(v=p_1\)로 평가한다. 이는 이미 존재하는 gradient에 현재 벡터를 대입하는 절차다. Hessian 단계차는 D31에서 별도로 평가하므로 density bridge를 두 번 미분할 필요가 없다. 최고 source derivative는 Hessian으로 유지된다.

## 7. 일곱 photon sector의 명시적 순수 그래프

PHYS18의 고정 chronology에서 \(A=A_2\), \(L=I-A\), \(A_F=(I+2\tau)^{-1}\), \(L_F=I-A_F\), \(\tau=ha_2(1-x_2)\)다. PHYS18의 photon coefficient \(C_1,C_2\)를 이 문서에서는 inverse preconditioner와 구별하여

\[
\mathcal C_1=\tau A^2A_F,\qquad \mathcal C_2=\tau^2A^2A_F
\tag{D33}
\]

로 쓴다. diagonal 연산은 성분별이다. \(\Delta R=R^2-R_F\), \(\Delta A_1=A_1-A\)에서

\[
\begin{aligned}
p_{\rm ph}={}&-(I-LR)\Delta A_1Q_1+L[R,A]Q_1
+L(I-R)RZ_0\\
&+\mathcal C_2R^2Z_0+L_F\Delta RZ_0
+bLA(R-I)J_\gamma-b\mathcal C_1J_\gamma.
\end{aligned}
\tag{D34}
\]

\(D=\Delta A_1Q_1\), \(K_R=[R,A]Q_1\), \(Z_R=(I-R)RZ_0\), \(J_R=(R-I)J_\gamma\)를 정의한다. 그러면

\[
\begin{aligned}
D'&=\Delta A_1'Q_1+\delta_b\Delta A_1J_\gamma,\\
D''&=\Delta A_1''Q_1+2\delta_b\Delta A_1'J_\gamma,\\
K_R'&=[R,A']Q_1+\delta_b[R,A]J_\gamma,\\
K_R''&=[R,A'']Q_1+2\delta_b[R,A']J_\gamma.
\end{aligned}
\tag{D35}
\]

순서 있는 곱의 \((AB)''=A''B+2A'B'+AB''\)를 D34에 적용하면

\[
\boxed{\begin{aligned}
p_{\rm opacity}''&=-D''+L''RD+2L'RD'+LRD'',\\
p_{\rm comm}''&=L''K_R+2L'K_R'+LK_R'',\\
p_{\rm stockR}''&=L''Z_R,\\
p_{\rm stockBE}''&=\mathcal C_2''R^2Z_0,\\
p_{\rm remap}''&=L_F''\Delta RZ_0,\\
p_{\rm birthR}''&=\{b(LA)''+2\delta_b(LA)'\}J_R,\\
p_{\rm birthBE}''&=-\{b\mathcal C_1''+2\delta_b\mathcal C_1'\}J_\gamma.
\end{aligned}}
\tag{D36}
\]

이는 C13에 요구된 pure sector 식을 전부 명시한 것이다. 일곱 항의 합을 \(p_{\rm ph}''\)로 두고 \(r''=r_g''+V_{\rm ph}p_{\rm ph}''\)를 D22에 사용한다.

### 7.1 opacity 차이의 인수 분해

\[
\begin{gathered}
\zeta=h\{c\sigma(n_2-n_1)(1-x_2)-a_1s_x\},\qquad
\Delta A_1=\zeta A_1A,\\
\zeta'=-h\{c\sigma(n_2-n_1)p_x+a_1s_{\theta,x}\},\\
\zeta''=-h\{c\sigma(n_2-n_1)K_{2,x}+a_1s_{\theta\theta,x}\}.
\end{gathered}
\tag{D37}
\]

\[
\boxed{\begin{aligned}
\Delta A_1''={}&\zeta''A_1A
+2\zeta'(A_1'A+A_1A')\\
&+\zeta(A_1''A+2A_1'A'+A_1A'').
\end{aligned}}
\tag{D38}
\]

이 식은 \(s,s_\theta,s_{\theta\theta}\)의 작은 차이를 보존한다. \(\mathcal C_i\)는 \(\tau\)의 명시적 rational 함수이므로 \(\mathcal C_i''=c_i'(\tau)\tau''+c_i''(\tau)(\tau')^2\) 또는 같은 ordinary pure jet product rule로 계산한다. 이 rational 함수의 두 번째 미분은 원 source Hessian보다 높은 source 정칙성을 요구하지 않는다.

### 7.2 순수 number·energy ledger

\(\Delta\widehat Z=Z_2-A_F(g_2)Q_F\), 원 number row \(n_\gamma\), energy row \(u_\gamma\), 활성 광자 에너지 row \(E^T\)와 고정 redshift 비 \(\rho\)를 쓰면 PHYS18의 정확한 ledger를 두 번 미분하여

\[
\boxed{\begin{aligned}
\mathbf1^Tp_{\rm ph}''&=-n_\gamma\Delta\widehat Z'',\\
E^Tp_{\rm ph}''&=(1-\rho)E^TP_1''-u_\gamma\Delta\widehat Z''.
\end{aligned}}
\tag{D39}
\]

원 energy ledger의 직접 birth 항 \(-(1-\rho)bM_\gamma E_{24}\)는 \(\theta\theta\) 미분에서 0이다. D39의 row는 두 guard를 포함하며, 흡수 쪽 \(\mathbf1,E\)는 33개 활성 성분에 작용한다. heat ledger는 같은 \(E-\chi_H\mathbf1\) 조합이다.

실제 Full photon endpoint 차이는 \(\Delta Z_j=\Delta\widehat Z_j+\Gamma_jd_x\)이고

\[
\Gamma_j=\frac{\ell_jQ_{Fj}}{D_{yj}D_{Fj}},\qquad
\ell_j=2ha_{2j},\qquad
\boxed{\Delta Z_j''=\Delta\widehat Z_j''+\Gamma_jK_{d,x}+2\Gamma_j'd_{\theta,x}+\Gamma_j''d_x.}
\tag{D40}
\]

guard의 \(\Gamma\)는 0이다. D40은 총 photon endpoint 검산이 필요한 경우 원 same-Full 결박을 유지하는 pure 식이다.

## 8. 유한 inverse certificate와 안전한 포함 교차

해당 stage Jacobian \(J\)에 대해 원 fixed preconditioner \(C\), 비음수 행렬 \(B\), 좌표 scale \(S\)가

\[
|I-CJ|\le B,\qquad \|S^{-1}BS\|_\infty\le q<1
\tag{D41}
\]

를 만족한다고 하자. \(Jv=f\)의 해는 \(v=Cf+(I-CJ)v\)이고,

\[
m=(I-B)^{-1}\operatorname{mag}([Cf]),\qquad
\boxed{v\in[Cf]+[-Bm,Bm]}
\tag{D42}
\]

이다. 증명은 \(|v|\le\operatorname{mag}([Cf])+B|v|\)와 \((I-B)^{-1}=\sum_{k\ge0}B^k\ge0\)를 결합한 뒤 원 식에 다시 대입하는 것이다. \(q<1\)은 각 interval Jacobian의 가역성을 보장한다.

현재 stage 결박은 다음과 같다.

| stage | 사용할 원 inverse |
|---|---|
| 첫 half | PHYS18 preflight의 \(C=I\), \(S=\mathrm{diag}(1,1,1,27/2)\), \(q<0.0005396\) |
| Full | 원 `UNIFORM_ARITHMETIC`의 같은 \(C,B,S,q\) |
| 둘째 half | PHYS14의 \(J_2=I-L\), `L_hFg`, 원 scale 및 refined contraction |
| endpoint \(K_d\) | Full과 동일한 \(J_F,C,B,S,q\) |

D18, D22, 별도 생성한 \(K_2-K_F\)로 얻은 세 포함은 모두 같은 \(K_d\)를 포함하므로 교차한다. signed \([E_F]=[I-CJ_F]\)를 보존하면

\[
[K_d]\leftarrow[K_d]\cap\{[Cf]+[E_F][K_d]\}
\tag{D43}
\]

를 유한 횟수 적용할 수 있다. 다음 관계도 각 exact expression에서 오는 포함 교차다.

\[
\begin{aligned}
[K_F]&\leftarrow[K_F]\cap([K_2]-[K_d]),\\
[K_2]&\leftarrow[K_2]\cap([K_F]+[K_d]),\\
[s_{\theta\theta}]&\leftarrow[K_2-K_1]\cap[\text{D16}].
\end{aligned}
\tag{D44}
\]

교차 후 upstream dependent expression을 다시 평가할 때는 새 구간을 쓰되 같은 root를 포함하는 관계를 유지한다. 공집합이 생기면 해당 정확식·입력 정규화·반올림을 조사한다.

같은 \(E_F\)에서 \(\widehat v_m=\sum_{k=0}^{m}E_F^kCf\)이면

\[
\|v-\widehat v_m\|_S\le
\frac{q^{m+1}}{1-q}\|Cf\|_S.
\tag{D45}
\]

이는 inverse series의 truncation 경계다. source·family interval 폭은 D42–D44에 함께 보존한다.

## 9. 정확한 유한 온도 quotient

두 endpoint의 동일한 최종 density ratio \(f=\operatorname{exact}(n_{\rm He,2}^{stored})/\operatorname{exact}(n_2)\)를 사용한다.

\[
\ell_e=(1,f,2f,0),\qquad
C_T=\frac{2\epsilon_{\rm eV}}{3k_B},\qquad
\Pi(g)=1+f+\ell_eg,\qquad T(g)=\frac{C_Tw}{\Pi(g)}.
\tag{D46}
\]

\(\Pi_2,\Pi_F>0\)가 원 gas 영역에서 유지된다. \(C_Tw=T\Pi\)를 한 번, 두 번 미분하면

\[
T'=rac{C_Tp_w-T\ell_ep}{\Pi},\qquad
\boxed{T''=\frac{C_TK_w-T\ell_eK-2T'\ell_ep}{\Pi}.}
\tag{D47}
\]

분모를 전개한 독립 동등식은

\[
T''=C_T\left\{\frac{K_w}{\Pi}
-\frac{2p_w\ell_ep+w\ell_eK}{\Pi^2}
+\frac{2w(\ell_ep)^2}{\Pi^3}\right\}.
\tag{D48}
\]

\(F=T_2-T_F\), \(d_e=\ell_ed\), \(P=\Pi_F\)라 두면 정확한 통분식은

\[
F=\frac{N}{P},\qquad N=C_Td_w-T_2d_e.
\tag{D49}
\]

\[
\begin{aligned}
N''&=C_TK_{d,w}-T_2\ell_eK_d-T_2''d_e-2T_2'd_{e,\theta},\\
P'&=\ell_ep_F=\ell_e(p-d_\theta),\qquad
P''=\ell_eK_F=\ell_e(K_2-K_d).
\end{aligned}
\tag{D50}
\]

\(N=FP\)를 두 번 미분하면 \(N''=F''P+2F'P'+FP''\)다. \(n_F=C_Te_w^T-T_F\ell_e\)로 묶어서

\[
\boxed{F''=\frac{n_FK_d-T_2''d_e-2T_2'd_{e,\theta}-2F'P'-F\ell_eK_2}{\Pi_F}.}
\tag{D51}
\]

D47의 \(k=2\)와 D51은 C15–C16이다. 마지막 항이 \(-F\ell_eK_2\)인 것은 \(K_d\)의 계수에 \(+F\ell_e\)를 이미 묶었기 때문이다. \(P'\)는 Full의 입자수 응답 \(\ell_ep_F\)다. \(\ell_ep_2\)를 쓰려면 \(-\ell_ed_\theta\)를 함께 보존한다.

D51과 직접 \(T_2''-T_F''\)는 서로 다른 정확식에서 얻는 포함이므로 교차할 수 있다. 실제 thermal readout은 하나의 \(J_F\), \(n_F\), \(\Pi_F\)에서 평가한다. \(J_F^Tz_F=n_F^T\), \(f=\sum_a f_a\)와

\[
\eta=-T_2''d_e-2T_2'd_{e,\theta}-2F'P'-F\ell_eK_2
\]

를 쓰면

\[
\boxed{F''=\sum_a\frac{z_F^Tf_a}{\Pi_F}+\frac{\eta}{\Pi_F}.}
\tag{D52}
\]

이 식은 source·stage·photon·endpoint·온도 분모 기여를 같은 관측량에 투영한다. 기여별 interval 폭의 합과 합계 interval 폭은 의존성 때문에 다를 수 있으므로 실제 합계 포함으로 결론을 판정한다.

Adjoint의 inverse certificate를 따로 구성할 경우 왼쪽 전처리 \(E=I-CJ_F\)에서

\[
J_F^{-T}=C^T(I-E^T)^{-1}
\tag{D53}
\]

의 순서를 유지한다. 원 \(S\)-weighted infinity contraction의 dual은 \(\|S\,\cdot\|_1\)이다. 따라서 transpose에 같은 unweighted infinity bound를 자동 대입하는 대신 원 majorant를 transpose하거나 이 dual norm을 사용한다.

## 10. 전역 bilinear 보간 오차의 증명

고정 \(\alpha\)에서 같은 함수의 네 corner 값을 \(F_{ij}=F(i,j)\)라 하고

\[
\mathcal L F=(1-\lambda)(1-b)F_{00}+\lambda(1-b)F_{10}
+(1-\lambda)bF_{01}+\lambda bF_{11}
\tag{D54}
\]

를 정의한다. 계수 \(F_{ij}\)는 같은 \(\alpha\)에 결박된 실제 값이다.

한 변수 \(u\in[0,1]\)에 대해 \(I_uf=(1-u)f(0)+uf(1)\)를 두자. 구간별 부분적분으로

\[
f(u)-I_uf(u)=\int_0^1K_u(t)f''(t)\,dt,
\quad
K_u(t)=\begin{cases}-t(1-u),&0\le t\le u,\\-u(1-t),&u\le t\le1.\end{cases}
\tag{D55}
\]

\(K_u\le0\), \(\int K_u=-u(1-u)/2\)이므로 \(f''\in[L,U]\)에서

\[
f(u)-I_uf(u)\in-rac{u(1-u)}2[L,U]
=\left[-\frac{u(1-u)}2U,-\frac{u(1-u)}2L\right].
\tag{D56}
\]

이제 \(\mathcal L=I_\lambda I_b\)이고

\[
F-I_\lambda I_bF=(I-I_\lambda)F+I_\lambda(I-I_b)F.
\tag{D57}
\]

\(I_\lambda\)는 비음수 convex weight를 가진다. 따라서 rectangle 전체에서

\[
F_{\lambda\lambda}\in[L_{\lambda\lambda},U_{\lambda\lambda}],\qquad
F_{bb}\in[L_{bb},U_{bb}]
\]

이면

\[
\boxed{F-\mathcal LF\in-rac{\lambda(1-\lambda)}2[L_{\lambda\lambda},U_{\lambda\lambda}]
-rac{b(1-b)}2[L_{bb},U_{bb}].}
\tag{D58}
\]

\(M_{\theta\theta}=\max(|L_{\theta\theta}|,|U_{\theta\theta}|)\)에서

\[
\boxed{|F-\mathcal LF|\le
\frac{M_{\lambda\lambda}}2\lambda(1-\lambda)
+\frac{M_{bb}}2b(1-b)
\lerac{M_{\lambda\lambda}+M_{bb}}8.}
\tag{D59}
\]

이는 C17–C19다. 모든 보간 corner에서 두 weight가 0이 되어 오차가 정확히 0이고, 한 변 위에서는 남은 축의 순수 곡률만 기여한다. \(F=a_0+a_\lambda\lambda+a_bb+c\lambda b\)이면 두 순수 곡률이 0이므로 보간은 정확하다.

### 10.1 계수 1/8의 sharpness와 더 좁은 포함

고정된 비음수 \(M_\lambda,M_b\)와 원 mixed 범위의 임의 \(c\)에 대해

\[
F_*(\lambda,b)=a_0+a_\lambda\lambda+a_bb+c\lambda b
+\frac{M_\lambda}{2}\lambda^2+\frac{M_b}{2}b^2
\tag{D60}
\]

는 \(F_{*,\lambda\lambda}=M_\lambda\), \(F_{*,bb}=M_b\), \(F_{*,\lambda b}=c\)를 만족하며 midpoint의 보간 오차 절댓값은 \((M_\lambda+M_b)/8\)이다. 따라서 D59의 상수는 이 derivative 정보와 양립하는 함수로 달성된다. 더 작은 실제 경계는 해당 물리 계열의 더 좁은 곡률 포함이나 경로별 정보를 사용해 구한다.

축별 또는 edge별 포함이 확보되어 있다면 D57을 더 세밀하게 쓰면 된다.

\[
\begin{aligned}
F-\mathcal LF={}&\int K_\lambda(t)F_{\lambda\lambda}(t,b)\,dt\\
&+(1-\lambda)\int K_b(t)F_{bb}(0,t)\,dt
+\lambda\int K_b(t)F_{bb}(1,t)\,dt.
\end{aligned}
\tag{D61}
\]

\(\lambda,b\)를 교환한 동등식도 함께 평가하고 두 포함을 교차할 수 있다. kernel과 convex weight만 사용하므로 최고 정칙성은 \(C^2\)다.

두 순수 곡률이 모두 비음수이면 \(F\le\mathcal LF\), 모두 비양수이면 \(F\ge\mathcal LF\)이다. 서로 다른 부호이면 D58의 signed 양 끝을 그대로 제공한다.

## 11. 같은-family 계수, 기존 mixed 결과와 실제 surrogate 오차

\[
\begin{gathered}
a_\lambda=F_{10}-F_{00},\quad a_b=F_{01}-F_{00},\\
\mathcal I=F_{11}-F_{10}-F_{01}+F_{00},\qquad
\mathcal LF=F_{00}+a_\lambda\lambda+a_bb+\mathcal I\lambda b.
\end{gathered}
\tag{D62}
\]

원 PHYS18에서 재사용하는 값은

\[
[L_m,U_m]=[-2.668505746423,-2.118796636045]\times10^{-12}\,\mathrm K,
\qquad\mathcal I\in[L_m,U_m].
\tag{D63}
\]

\(a_\lambda=\int_0^1F_\lambda(t,0)\,dt\), \(a_b=\int_0^1F_b(0,t)\,dt\)이므로 PHYS17의 전역 1차 구간은 각 chord coefficient의 포함이다. 또한

\[
a_\lambda+\mathcal I=F_{11}-F_{01},\qquad
a_b+\mathcal I=F_{11}-F_{10}
\tag{D64}
\]

도 같은 전역 1차 포함에 속한다. 예를 들어 \([D_\lambda]\)가 전역 \(F_\lambda\) 포함이면

\[
[a_\lambda]\subseteq[D_\lambda]\cap([D_\lambda]-[L_m,U_m]),
\tag{D65}
\]

이며 \(a_b\)도 같다. 이 경계와 D64의 coupled relation을 함께 저장할 수 있다.

D59는 실제 같은-family corner 값으로 정의한 \(\mathcal LF\)의 approximation error다. 원 \(F_{00}\)와 chord coefficient의 포함 폭은 별도로 보존한다. 수치 하나씩을 선택한 다항식

\[
\widehat P=\widehat F_{00}+\widehat a_\lambda\lambda+\widehat a_bb+\widehat c_m\lambda b
\]

에 대해 각 true coefficient와의 오차 경계가 \(r_0,r_\lambda,r_b,r_m\)이면

\[
\boxed{\begin{aligned}
|F-\widehat P|\le{}&r_0+r_\lambda\lambda+r_bb+r_m\lambda b\\
&+\frac{M_{\lambda\lambda}}2\lambda(1-\lambda)
+\frac{M_{bb}}2b(1-b).
\end{aligned}}
\tag{D66}
\]

corner estimates 자체를 사용하는 경우에는 coefficient radii의 합 대신 convex corner weights에 따른 더 직접적인 경계

\[
|\mathcal LF-\mathcal L\widehat F|
\le(1-\lambda)(1-b)\varepsilon_{00}
+\lambda(1-b)\varepsilon_{10}
+(1-\lambda)b\varepsilon_{01}+\lambda b\varepsilon_{11}
\tag{D67}
\]

를 쓸 수 있다. 새 corner root 실행 없이도 기존 anchor·chord·interaction 포함을 그대로 연결한 검증된 response representation을 얻는다. coefficient 해상도와 곡률에 의한 보간 오차를 별도 필드에 저장하면 선택된 numerical surrogate의 실제 총오차도 추적된다.

## 12. 순수·혼합 곡률을 합친 추가 판별식

최종 순수 구간이 확보되면

\[
\nabla^2F=\begin{pmatrix}F_{\lambda\lambda}&F_{\lambda b}\\F_{\lambda b}&F_{bb}\end{pmatrix}
\tag{D68}
\]

를 같은 rectangle에서 판별할 수 있다. 예를 들어 \(F_{\lambda\lambda}\ge a>0\), \(F_{bb}\ge c>0\), \(|F_{\lambda b}|\le m\)와 \(ac>m^2\)이면 모든 \(v\)에 대해

\[
v^T\nabla^2Fv\ge a v_1^2+c v_2^2-2m|v_1v_2|>0\quad(v\ne0)
\tag{D69}
\]

이므로 joint strict convexity가 성립한다. 두 순수 항이 \(\le-a,\le-c\)이고 같은 조건이면 joint strict concavity다. 두 순수 항의 부호가 엄격하게 반대이면 determinant가 음수여서 Hessian은 saddle signature를 가진다. 이 판별은 새 도함수 계산 없이 얻는 후속 해석이며, 실제 수치 조건을 확인한 경우에 해당 결론을 붙인다.

## 13. 차원·극한·구현 인수의 검토

| 검사 | 유도에서 확인한 결과 |
|---|---|
| 매개변수 단위 | \(\lambda,b\) 무차원, \(p,K,d_\theta,K_d\)는 gas 좌표 단위, \(F'',\mathcal I\)는 K |
| 시간 인수 | source Hessian에는 \(h,2h\); residual Hessian에는 이미 시간·부호 포함 |
| HH 방향 | \(\nu_{H,w}=-\chi_H\); ionization과 thermal-loss 부호 보존 |
| 순수 jet | ordinary derivative; 곱의 중간항에 2 |
| Full birth | \(Q_{F,b}=2J_\gamma\), 따라서 source 형태의 pure cross term에 4 |
| carried incoming | \(Q_2''=RZ_1''\), \(Z_1''\)의 \(2\delta_b A_1'J_\gamma\) 보존 |
| 둘째 half solve | \(L_g[K_2]Q_2\)는 \(J_2\)에 포함하고 실제 \(P_2''\) 복원 시 사용 |
| 대칭 | \(C^2\) Hessian symmetry가 D21, D26–D27, D31의 근거 |
| 투명 극한 | \(\sigma=0\)이면 gas에 \(b\) forcing이 사라져 \(p_b,K_{bb},F_{bb}\) 및 기존 mixed가 0 |
| HH source가 0인 극한 | \(q\equiv0\)이면 fixed COMMON에서 gas \(\lambda\) 응답과 \(F_{\lambda\lambda}\)가 0 |
| birth가 없는 극한 | \(J_\gamma=0\)이면 gas·photon의 \(b\) 응답이 0 |
| \(b=0\) 경계 | affine birth 값은 0, opacity와의 pure \(b\) product term은 남을 수 있음 |
| guard | local absorption jet은 0; transported incoming/outgoing guard 응답은 원 R로 보존 |
| 양의 열 분모 | 같은 final \(f,C_T\), \(\Pi_2,\Pi_F>0\)에서 D47–D51 정칙 |
| 동일 endpoint 계열 | \(g_2\equiv g_F\)이면 \(d,d_\theta,K_d,F,F',F''=0\) |
| bilinear 함수 | 두 순수 curvature가 0이면 D54 정확 |
| 보간 corner | \(\lambda,b\in\{0,1\}\)에서 D58–D59의 오차 0 |

## 14. 검토 판정과 통합 우선순위

수학적 판정은 `pass_scoped`다. C3–C20은 원 \(C^2\), fixed \(\alpha\), 원 Jacobian 가역성·양의 분모 전제에서 일관된다. 다음 항목은 수식 오류 발견이 아니라 실제 application이 보존해야 하는 구체적인 연결이다.

1. D15 RHS와 D14 actual photon pure slot 사이에서 \(L_g[K_2]Q_2\)의 위치를 검사한다.
2. D11·D36·D40·D47·D51의 순수 계수 2와 D8의 Full birth 계수 4를 새 symbolic check에 포함한다.
3. D12와 D39를 같이 검사하여 local absorption guard와 transported guard를 구분한다.
4. first-half·Full·second-half·endpoint의 Jacobian identity를 각 inverse certificate에 연결한다.
5. 직접식 D18, 상관식 D22, 별도 \(K_2-K_F\), 두 온도 readout의 실제 교차를 출력한다.
6. D59의 approximation error와 D66–D67의 coefficient uncertainty를 별도 항목으로 제공한다.
7. 실제 구간이 확보된 후 D52의 dominant contribution, D58의 signed error, D68–D69의 Hessian 판별 조건을 평가한다.

현재 분과의 완료 범위는 독립 유도·원식 대조·차원/극한/부호 검토 및 원고에 재사용할 수 있는 정확식의 작성이다. 수치 application과 Wolfram/xAct 실행 결과는 본문 식의 해당 구현 의무에 합류한다.
