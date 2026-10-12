# PHYS17 원 source·유도 독립 대조

검토일: 2026-10-13 KST. 검토자: /root/hh_phys17_literature_review.

판정 대상은 고정된 admissible coefficient 선택 \(\alpha\), 원 COMMON과 전역 \((\lambda,b)\in[0,1]^2\), 원 \(C^2\) source/root family에서의 \(d=g_2-g_F\)와 \(\Delta T=T_2-T_F\)의 1차 미분이다. PHYS16 contracts/PARAMETER_RESPONSE_CONTRACT.json의 P1–P4를 기준으로, 새 이론 원고와 실제 실행 source를 원 Rust source 및 저장된 Jet의 의미에 직접 대조했다.

## 1. \(C^2\) 전제와 잔차 부호

\(x=g_F,\ y=g_2,\ d=y-x,\ r=H(y,\theta)\), \(J_F=H_g(x,\theta)\)라 두면, 원 방정식 \(H(x,\theta)=0\)의 미분은

\[
J_Fx_\theta+H_\theta(x,\theta)=0.
\]

따라서 \(J_Fd_\theta=J_Fy_\theta+H_\theta(x,\theta)\). 다른 한편 \(r_\theta=H_g(y,\theta)y_\theta+H_\theta(y,\theta)\)다. 두 식의 차이를 같은 선분 \(y-sd\)에서 전개하면

\[
J_Fd_\theta=r_\theta-\int_0^1
\left\{H_{gg}(y-sd,\theta)[d,y_\theta]
+H_{g\theta}(y-sd,\theta)d\right\}\,ds.
\]

두 correction 모두 빼는 부호다. \(d_\theta\)를 우변의 Hessian remainder에 다시 넣지 않는다. \(H_g\)와 \(H_\theta\)에 각각 1차 기본정리를 적용했으므로 \(C^2\)면 충분하다. \(C^3\) 정보를 요구하는 Hessian remainder의 재미분을 하지 않는다.

원 sourcebox.rs의 export는 G_g_lambda[i][j]=residual[i].hessian[j][4], G_g_b[i][j]=residual[i].hessian[j][5], G_gg[i][j][k]=residual[i].hessian[j][k]다. 원 \(H=G\)의 시간계수와 부호가 이미 포함되어 있다. PHYS17은 이 배열에 다시 \(-2h\)를 곱하지 않는다. 독립 산술에서 96개 slot 등식을 확인했다.

## 2. 원 thermal source에서의 helium 소거

읽은 원 source의 고정 식은

\[
F_x=n e\{(1-x)\beta_H(T)-x\alpha_H(T)\},
\]

\[
F_w=ne\{-\chi_H(1-x)\beta_H(T)-x\kappa_H(T)
+f k_{\rm He}(y,z,T)\}.
\]

여기서 \(F\)는 photon·HH·팽창 항을 더하기 전의 nonphoto이고, \(f=n_{\rm He,stored}/n_H\)다. 원 phys04_mixed.rs는 internal photo \(\sigma\)를 0으로 둔 FT03 결과를 nonphoto=f.clone()으로 보존한 뒤 HH와 외부 photon 및 팽창을 추가한다. 원 collisional-ionization 열항과 수소 분율항에 들어간 \(\chi_H\)는 같은 captured binary64 leaf다. 따라서

\[
U=\frac{F_w+\chi_HF_x}{ne}
=-x\{\kappa_H(T)+\chi_H\alpha_H(T)\}+f k_{\rm He}(y,z,T).
\]

\(\Pi=1+f+x+fy+2fz\), \(T=C_Tw/\Pi\)에서
\(\xi=e_x+(w/\Pi)e_w\)는 \(D_\xi T=0\)이고 \(y,z\)도 고정한다. 그러므로

\[
k_{\rm He}=\frac{U-xDU[\xi]}f.
\]

임의 방향 \(v\)에 대해

\[
Dk_{\rm He}[v]
=\frac{DU[v]-v_xDU[\xi]-x\{D^2U[v,\xi]+DU[D\xi[v]]\}}f.
\]

PHYS17의 density_bridge는 바로 이 식을 저장된 nonphoto value/gradient/Hessian에 적용한다. \(D\xi[v]\)의 마지막 성분은 \(v_w/\Pi-w(\ell_ev)/\Pi^2\)다. 새 fit 또는 \(k_{\rm He}\)를 독립 계수로 가정하는 변경은 없다. 값에 대해서만 PHYS16의 이미 포함된 kwHe와 교차하며, derivative는 위 항등식을 직접 계산한다.

## 3. 작은 density/time 차이의 보존

첫 source 시각과 Full source 시각의 exact \(n_1,n_2,f_1,f_2\)를 유지한다. \(\Delta f=f_1-f_2,\ \sigma=y+2z,\ \Pi_1=1+f_1+e_1\)일 때

\[
g^*=g+\delta w e_w,\qquad
\delta w=-\frac{w\Delta f(1+\sigma)}{\Pi_1}
\]

는 정확히 \(T_2(g^*)=T_1(g)\)를 만족한다. 계수비
\(r_e=(n_1/n_2)(e_1/e_2)\)는

\[
r_e-1=(n_1/n_2-1)+(n_1/n_2)\Delta f\,\sigma/e_2,
\quad
D r_e[v]=(n_1/n_2)\Delta f\,
\frac{e_2D\sigma[v]-\sigma De_2[v]}{e_2^2}
\]

로 평가한다. 이 표현은 근접한 \(r_e\)와 1을 먼저 독립 구간으로 계산하여 빼는 확대를 피한다.

nonphoto source 차이의 미분에서 \(r_e-1\), \(\delta w\), \(\Delta f\)를 먼저 인수로 남겨, gradient 차이는 원 whole-\(X\) Hessian을 적분한 항으로 닫는다. thermal helium 잔여는
\[
n_1\Delta f\{De_1[v]\,k_{\rm He}+e_1Dk_{\rm He}[v^*]\}.
\]
HH rate \(q\)도 같은 pullback을 쓰며, HH 직접 forcing은 \(\delta_{\theta\lambda}\Delta q\)다. density_bridge의 np_v, he_v, q_v는 이 곱규칙과 일치한다.

원 SOURCE_CENTRE는 gas 좌표만 고정하고 \(\lambda\in[0,1]\) 및 incoming의 \(b\) 범위를 그대로 둔다. 따라서 gas-centered Taylor 포함은 모든 parameter에 대해 유효하다. Full source hull, \(g_1\)–\(g_2\) 선분, \(g\)–\(g^*\) 선분은 기존 convex \(X\) 안에서 평가된다. 원 \(C^2\) 선언은 fixed-coefficient real source에 관한 것이다. interval clipping이나 반올림 연산 자체를 미분 가능한 물리 함수로 해석하지 않는다.

## 4. 공통 stage response와 일곱 photon 항

실제 \(v=g_{1,\theta}\), \(u=g_{2,\theta}\)와 같은 stage 방정식에서 얻은 \(s_\theta=(g_2-g_1)_\theta\)를 gas movement와 opacity difference 양쪽에 공유한다. main run의 st는 stage 방정식으로 계산한 포함을 상속된 \(u-v\) 포함과 교차한 값이다. 검토에서는 상속 carry의 정확 동등성 대신 원 Fraction 구간을 포함하는 외향 복사임을 확인했다.

원 \(A_1,A,A_F,L,L_F\)와 \(C_1=\tau A^2A_F,\ C_2=\tau^2A^2A_F\)를 사용한다. parameter_response_application.py는 일곱 원 항을 1차 dual로 평가하며, forcing_feedback_decomposition.py는 같은 식을 수동 곱규칙으로 나누어 평가한다. 후자는 실제 \(g_1,g_2\)를 고정한 직접 \(\lambda,b\) forcing과 실제 stage/opacity feedback을 구별한다. 특히 \(b=0\)에서 birth 값은 0이지만 \(\partial_b b=1\) 항은 남는다.

commutator의 순서는 \(RA-AR\)이고, 광자 guard 두 성분은 absorption projection에 기여하지 않는다. 모든 33개 원 group과 2개 guard를 유지했다. 실행 결과의 일곱 항 × 35성분 × 2매개변수, 총 490개 manual/dual 합 포함 교차가 비어 있지 않음을 독립 확인했다. 이것은 동일 물리식의 서로 다른 산술 평가가 양립함을 보이는 검사다. 일곱 항이 원 absorption residual과 같은 항등식이라는 근거는 직접 유도 및 일반 비가환 2-slot Wolfram 대수 검산에 별도로 연결한다.

## 5. 같은 inverse와 유한 온도

원 \(C,B,q,S\)를 고정하고 \(|I-CJ_F|\le B,\ \|B\|_S\le q<1\)를 사용한다. 후보의 Gaussian elimination과 독립적으로 24항 Leibniz determinant에 의한 Cramer 식으로 \((I-B)m=|Cf_\theta|\)를 풀었다. \(m\ge0\), 초기 tail, 세 번의 signed 교차, 마지막 상속 \(u-g_{F,\theta}\) 교차가 모두 포함 조건을 만족한다.

\[
\Delta T=\frac{C_Td_w-T_2d_e}{\Pi_F},
\qquad \Pi_F=\Pi_2-d_e>0
\]

를 그대로 미분하면

\[
(\Delta T)_\theta=
\frac{C_Td_{w,\theta}-T_2d_{e,\theta}-T_{2,\theta}d_e
-\Delta T(\ell_eu-d_{e,\theta})}{\Pi_F}.
\]

각 sector에는 같은 행
\[
\frac{C_Te_w-(T_2-\Delta T)\ell_e}{\Pi_F}
=\frac{C_Te_w-T_F\ell_e}{\Pi_F}
\]
을 적용한다. geometry 항
\((-T_{2,\theta}d_e-\Delta T\ell_eu)/\Pi_F\)를 모든 sector마다 중복하지 않고 총 feedback에 한 번 넣는다. 직접 forcing과 feedback이 공유하는 inverse·온도 분모·goal row가 이와 일치한다. \(\theta\)가 무차원이므로 결과 단위는 K/parameter이고, gas 응답의 마지막 좌표는 eV/H/parameter다.

## 6. 유한 Neumann, 모서리와 continuation

\(M_F=I-CJ_F\)에서 2차 유한 다항식을 적용한 응답 오차는 \(q^3a_\theta\),
\(a_\theta=\|Cf_\theta\|_S/(1-q)\) 이하이다. \(M_y=I-CJ_y\)를 쓰면

\[
\varepsilon_y\le\{q^3+L_Ha(1+q+q^2)\}a_\theta.
\]

\(J_y-J_F\)는 선분 위 Hessian 적분이므로 차이의 계수는 1이다. PHYS16 primal endpoint remainder의 \(1/2\)를 가져오지 않는다. Kelvin 오차에는 위 동일 goal row의 weighted one-norm을 곱한다. 원 \(a\)의 외향 복사와 \(d/S\)의 확대를 보수적으로 반영한 실제 \(a\)를 독립 Fraction으로 대조했다.

strict \(\partial_\lambda\Delta T<0,\ \partial_b\Delta T>0\)에서 따라오는 원고 §9.1은 같은 고정 \(\alpha\)에 대해 성립한다. 모서리 극값·비음 좌표 증가의 유한 변화 구간은 좌표 선분 적분, 등결함 곡선은 implicit function theorem에 의한 \(-\partial_\lambda\Delta T/\partial_b\Delta T\)다. 양의 분모와 uniform slope bound, 원 compact box의 open extension으로 원고의 continuation 조건이 충분하다. 네 모서리 혼합 contrast는 \(\lambda\) 도함수 폭으로 포함할 수 있지만, 이 사실이 mixed derivative의 부호를 정하지는 않는다. corollary JSON의 다섯 exact 구간 및 십진 외향 표기를 모두 독립 확인했다.

## 7. Wolfram/xAct 실행의 정확한 역할

실제 parameter_response_checks.wl과 WOLFRAM_XACT_EXECUTION.json을 읽었다. official xAct 1.3.0 archive SHA256을 검증한 뒤 xTensor 1.3.0과 xPerm 1.2.4의 Wolfram Language group backend로 계산했다. 외부 canonicalizer는 사용하지 않았다.

6개 tensor check는 P2 cancellation·Hessian 대칭·공통 adjoint 등의 dummy-index 및 수축 대수다. 9개 scalar group의 15개 값은 고정 온도 tangent, He projector와 derivative, P4, 공통 온도 row, 일반 비가환 2-slot photon 일곱 항의 값/미분, \(m=2\) Neumann 항등식이다. 실제 출력은 모두 exact 0이고 완료 상태 및 빈 message list를 확인했다.

이 결과는 해당 대수 항등식의 검산이다. 물리 원 source의 동일성, 35-slot 구간 포함, root family의 존재, \(q<1\)은 원 자료와 이 문서 및 별도 exact arithmetic에 연결되어 있다.

## 8. 원 source 식별

아래 source를 직접 읽었으며, PHYS16 evidence/intake/SOURCE_COOLING_AUDIT_KO.md를 재사용했다.

| 원 파일 | SHA256 |
|---|---|
| PHYS15 inputs/phys14/inputs/ncp07/candidate/src/ft03_interval.rs | 886580a810b8ec29c8f0b6199c0e35d82fde1f46d984a5f8f1da304326a42a42 |
| PHYS16 inputs/ncp07_proofsrc/phys04_mixed.rs | 0fa10fdea11cb24aa1a191a2ea81cf4c8442299fde7278a191553b42a26585d3 |
| PHYS15 inputs/phys14/inputs/ncp07/src/sourcebox.rs | d771968e9c12c0cce5a9e3ec5fa7311d0040ac63d1f4f4a6f54f048972f674ae |
| PHYS15 inputs/phys14/src/phys14_advance.py | d20d9797278b8da71d38a3db229325dc7792d3991863f07bcdb7f72f2ba5567a |

마지막 helper는 후보의 rounding/Taylor 의미를 파악하기 위해 읽었다. 독립 검산 프로그램은 이를 import하지 않으며 자체 Fraction 구간과 determinant 연산만 사용한다. 핵심 비교 문헌의 원문 조건 및 인용 범위는 literature/LITERATURE_REVIEW_KO.md와 references.bib에 기록했다.

이 검토에서 원 source·closure·정규화 또는 시간계수의 불일치는 발견되지 않았다. 최종 채택 범위와 실행 식별은 INDEPENDENT_REVIEW.json에 고정한다.
