# PHYS17 독립 시작식 검토

검토 범위: PHYS16의 \`NEXT_PARAMETER_RESPONSE_PROPOSAL_KO.md\` P1–P4와 같은 fixed-\(\alpha\), 동일 COMMON, 전역 \(\theta\in\{\lambda,b\}\) 계열. 현재 문서는 원 시작식에 대한 독립 유도이며, 새 수치 적용의 판정은 후보 출력 이후 별도로 기록한다.

## 1. 전제와 표기

\(\mathcal H(g,\theta)=0\)의 Full 근을 \(x(\theta)=g_F\), 실제 second-half 끝점을 \(y(\theta)=g_2\)라 쓴다. \(d=y-x\), \(r=\mathcal H(y,\theta)\)이다. 원 source는 관련 convex 상태 영역 및 매개변수 계열에서 \(C^2\)이고, 원 Full 전처리 포함은 \(J_F=\mathcal H_g(x,\theta)\)의 가역성을 보장한다. 원 근의 미분가능성과 stage carry를 상속한다. 닫힌 \([0,1]^2\)의 경계에서 미분은 같은 매끄러운 계열의 제한으로 읽는다.

\(f_2=n_{\rm He,2}/n_{\rm H,2}\), \(C_T\), 각 endpoint 시각, \(h\), \(V\), remap 계수 및 고정 \(\alpha\)는 현재 \(\lambda,b\) 미분에서 상수다. \(\ell_e=(1,f_2,2f_2,0)\), \(\Pi(g)=1+f_2+\ell_eg\)를 사용한다. 두 매개변수는 무차원이다.

## 2. P2의 독립 유도

원 Full 방정식을 먼저 미분한다:
\[
J_Fx_\theta+\mathcal H_\theta(x,\theta)=0.
\]
따라서
\[
J_Fd_\theta
=J_Fy_\theta+\mathcal H_\theta(x,\theta).
\tag{I1}
\]
한편 실제 carried 끝점에서 잔차를 미분하면
\[
r_\theta=\mathcal H_g(y,\theta)y_\theta+
\mathcal H_\theta(y,\theta).
\tag{I2}
\]
(I2)에서 (I1)을 빼면
\[
r_\theta-J_Fd_\theta
=\{\mathcal H_g(y,\theta)-\mathcal H_g(x,\theta)\}y_\theta+
\{\mathcal H_\theta(y,\theta)-\mathcal H_\theta(x,\theta)\}.
\]
같은 선분 \(\gamma(s)=y-sd\), \(0\le s\le1\)을 두 차이에 적용한다. 고정 \(\theta\)에서 \(d\)와 \(y_\theta\)는 선분 적분의 상수 방향이므로
\[
\mathcal H_g(y)-\mathcal H_g(x)
=\int_0^1\mathcal H_{gg}(y-sd)[d,\,\cdot\,]\,ds,
\]
\[
\mathcal H_\theta(y)-\mathcal H_\theta(x)
=\int_0^1\mathcal H_{g\theta}(y-sd)d\,ds.
\]
결국
\[
\boxed{
J_Fd_\theta=r_\theta-
\int_0^1\left\{
\mathcal H_{gg}(y-sd)[d,y_\theta]+
\mathcal H_{g\theta}(y-sd)d
\right\}ds
}.
\tag{I3}
\]
두 항의 부호는 모두 음수다. 적분 integrand는 Hessian 한 번과 mixed derivative 한 번만 포함하여 \(C^2\)에서 연속이다. PHYS16의 가중 Taylor 나머지를 다시 미분하지 않고 원 implicit 관계를 사용했으므로 이 유도의 정칙성 요구는 원 계약과 동일하다.

원 Hessian \(\mathcal H_{gg}\) 및 mixed arrays는 **잔차**의 미분이다. Source \(\mathcal B\)의 미분에서 가져오는 경우에만 잔차에 포함된 시간 계수와 부호를 명시적으로 변환한다. 같은 배열을 두 번 변환해서는 안 된다.

## 3. P3의 정확한 의미

PHYS15에서 채택된 항등식
\[
r=h\{\mathcal B_1(g_1,\theta)-\mathcal B_2(y,\theta)\}+Vp
\]
을 같은 \(\theta\)에서 미분하면
\[
r_\theta=h\{
\mathcal B_{1,g}g_{1,\theta}+\mathcal B_{1,\theta}
-\mathcal B_{2,g}y_\theta-\mathcal B_{2,\theta}
\}+Vp_\theta.
\tag{I4}
\]
\(\mathcal B_{i,\theta}\)는 상태를 고정한 partial derivative이고 \(r_\theta\)는 실제 경로를 따라가는 total derivative다. \(p_\theta\)에는 공통 birth amplitude와 incoming carry, 단계별 opacity의 state response가 모두 들어간다. \(V\)는 이 계열에서 \(\theta\)-독립이다.

이 식을 구간화할 때 각 root response의 큰 상자를 단독으로 빼기보다, 공통 \(g_{1,\theta},y_\theta\), 잔차의 작은 차이와 source 차이를 보존한 계산 그래프를 사용한다. 이는 포함의 진리조건을 유지하면서 dependency 폭을 줄이는 실제 구성 선택이다.

## 4. P4의 독립 유도

\[
T(g)=C_Tw/\Pi(g),\quad
d_e=\ell_ed,\quad
\Pi_F=\Pi_2-d_e>0.
\]
두 온도의 유한 차이에 공통 분모를 취하면
\[
T_2-T_F
=\frac{C_Td_w-T_2d_e}{\Pi_F}
=\frac{N}{\Pi_F}.
\tag{I5}
\]
이제
\[
N_\theta=C_Td_{w,\theta}-T_{2,\theta}d_e-T_2d_{e,\theta},
\quad
(\Pi_F)_\theta=\ell_ey_\theta-d_{e,\theta}.
\]
(I5)를 미분하여
\[
\boxed{
\partial_\theta\Delta T=
\frac{C_Td_{w,\theta}-T_2d_{e,\theta}
-T_{2,\theta}d_e-\Delta T\{\ell_ey_\theta-d_{e,\theta}\}}
{\Pi_F}
}.
\tag{I6}
\]
\(T_{2,\theta}=C_T(w_{2,\theta}\Pi_2-w_2\ell_ey_\theta)/\Pi_2^2\)이다. 모든 항은 K/무차원 매개변수 단위이고, 마지막 분모 보정은 정확한 quotient derivative에서 나온다.

## 5. 경계·극한과 상태

- \(d=0\)인 한 매개변수 점에서도 \(d_\theta\)는 일반적으로 0일 필요가 없다. (I3)는 이때 \(J_Fd_\theta=r_\theta\)를 준다.
- 한 열린 매개변수 구간 전체에서 \(d\equiv0\)이면 \(r\equiv0\)와 \(d_\theta\equiv0\)가 함께 성립한다.
- 두 implicit 경로의 동일한 매개변수를 사용해야 위 \(d_\theta\)가 정의된다. 부분 잔차 성분의 온도 기여는 원 전체 경로의 미분으로 연결할 때 state feedback을 포함한다.
- 원 기체 Hessian의 마지막 두 gas slot 대칭은 원 \(C^2\) 전제에서 나오고, Wolfram/xAct는 이를 선언한 후 tensor 수축과 대수식을 확인한다.

판정: **P1–P4 derived 및 독립 검토 일치.** 수치 후보 출력, 원 mixed slot 대응과 구간 inverse 전달, 실제 Wolfram/xAct 출력을 함께 읽은 뒤 PHYS17 전체의 채택 판정을 내린다.

