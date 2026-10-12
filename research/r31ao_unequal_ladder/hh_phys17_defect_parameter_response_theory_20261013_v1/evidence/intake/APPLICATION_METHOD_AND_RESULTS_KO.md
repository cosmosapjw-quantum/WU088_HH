# PHYS17 실제 매개변수 응답 적용

## 대상과 실행 상태

같은 COMMON, 같은 전역 \((\lambda,b)\in[0,1]^2\), 고정 admissible \(\alpha\)에서
\(d=g_2-g_F\)와 \(\Delta T=T_2-T_F\)의 첫 매개변수 미분을 계산했다.
PHYS16의 원 근·source·endpoint 포함을 보존하고 원 PHYS09/11/14의 signed
U/V carry를 사용했다. 원 source 호출, 반응 fit 평가, 비선형 근 계산,
history 재실행은 각각 0회다. 실제 실행 상태는 `CANDIDATE_COMPUTED`이며
채택 판정은 별도의 독립 심사 기록에 연결한다.

원 코드 `phys14_advance.py`의 변하지 않은 Fraction/directed-dyadic 구간
산술만 import했다. `Source`, `evaluate`, 원 stage main은 호출하지 않았다.
구간 연산마다 256 유효 이진 자리로 바깥 반올림하며, \((I-B)m=|Cr|\)의
4×4 majorant는 유리수 Gaussian elimination으로 정확히 풀었다.

## 실제 적용한 식

\(s=g_2-g_1\), \(v=g_{1,\theta}\), \(y=g_2\), \(y_\theta=g_{2,\theta}\)다.
먼저 같은 actual stage 식에서

\[
s_\theta=h\{B_{2,g}(y)y_\theta+\delta_{\theta\lambda}q_2(y)\nu_H\}
             +VP_{2,\theta}
\]

를 구성하고 원 \(y_\theta-v\) 포함과 교차했다. 이 \(s_\theta\)를 기체
movement와 opacity 변화의 미분 양쪽에 사용했다.

### Source 시간차의 C² 연결

\(F=F^{np}_2\), \(q=q_2\), \(\Delta f=f_1-f_2\), \(r_n=n_1/n_2\),
\(g_*=g+\delta w e_w\)로 둔다. 저장된 밀도 비는 정확한 binary64 유리수
비로 형성하고 \(\Delta f\)를 먼저 인수 분해했다. \(r_e-1\)와
\(\delta w\)의 gas 방향미분을 직접 계산하여

\[
\begin{split}
D\delta F[v]={}&(r_e-1)DF(g)[v]+Dr_e[v]F(g_*)\\
 &+r_e\delta w\int_0^1D^2F(g+t\delta w e_w)[e_w,v]dt
 +r_eF_w(g_*)D\delta w[v]\\
 &+n_1\Delta f\{(\ell_{e,1}v)k_{wHe}(g_*)
                  +e_1Dk_{wHe}(g_*)[v_*]\}e_w,
\end{split}
\]

\[
D\delta q[v]=(r_n-1)Dq(g)[v]
 +r_n\delta w\int_0^1D^2q(g+t\delta w e_w)[e_w,v]dt
 +r_nq_w(g_*)D\delta w[v]
\]

를 포함했다. \(v_*=Dg_*[v]\)다.

Helium 미분에는 다음 정확한 source 항등식을 사용했다.

\[
U=\frac{F_w+\chi_HF_x}{n_2 e},\qquad
u=e_x+\frac{w}{\Pi}e_w,\qquad
k_{wHe}=\frac{U-xDU[u]}{f_2}.
\]

이것을 함수 항등식으로 미분하면

\[
Dk_{wHe}[v]=\frac{DU[v]-v_xDU[u]
 -x\{D^2U[v,u]+DU[Du[v]]\}}{f_2}.
\]

따라서 필요한 \(Dk_{wHe}\)가 보존된 nonphoto 값·gradient·Hessian에서
닫힌다. PHYS16 cooling-cone 구간은 \(k_{wHe}\) 값의 교차에 사용했다.
그 구간 부등식을 미분하는 연산은 없다. 원 source 구조에서 위 항등식의
증명과 convention은 `theory/PARAMETER_RESPONSE_THEOREM_KO.md`에 있다.

기체 movement의 미분은 작은 \(s\)를 보존하는

\[
-hB_{2,g}(y)s_\theta
-h\int_0^1\{B_{2,gg}(g_1+ts)[s,v]
       +\delta_{\theta\lambda}Dq_2(g_1+ts)[s]\nu_H\}dt
\]

로 적용했다. 단순한 넓은 source sensitivity 차이를 사용하지 않았다.

### 일곱 photon 항과 endpoint 보정

원 \(C_1=\tau A^2A_F\), \(C_2=\tau^2A^2A_F\)를 유지했다.
일곱 잔차 sector를 하나의 1차 dual interval graph에서 미분했다.
\(R,R_F,Z_0,\alpha,\rho\)의 매개변수 미분은 0이며
\(Q_{1,\theta}=\delta_{\theta b}J\)를 사용했다. PHYS11의 실제
`outgoing_joint`와 PHYS14 incoming/absorbed U/V를 교차에 사용했다.

이렇게 구한 \(r_\theta\)에 원 Full의 residual Hessian과 mixed Hessian을
적용하여

\[
J_Fd_\theta=r_\theta-
\int_0^1\{H_{gg}(y-td)[d,y_\theta]+H_{g\theta}(y-td)d\}dt
\]

를 포함했다. 원 `G_gg`는 이미 Full 잔차 Hessian이다. \(J_F\)는 원
center Jacobian과 \(G_{gg}\)로 gas endpoint 상자에 제한했고, 원
\(C,B,q,S\)와 signed \(I-CJ_F\) 교차를 그대로 사용했다.

최종 온도식은

\[
\partial_\theta\Delta T=
\frac{C_Td_{w,\theta}-T_2d_{e,\theta}-T_{2,\theta}d_e
 -\Delta T(\ell_e y_\theta-d_{e,\theta})}{\Pi_F},\qquad\Pi_F>0
\]

다. \(d,\Delta T\)에는 채택된 PHYS16 endpoint refinement를 사용했다.

## 실제 결과 — run02

모든 아래 끝점은 원 exact interval에서 바깥 방향으로 표시한 십진수다.
\(\lambda,b\)는 무차원이며 \(w\)의 단위는 eV/H, 온도는 K다.

| 미분 | \(x\) | \(y_1\) | \(y_2\) | \(w\) |
|---|---|---|---|---|
| \(d_\lambda\) | [1.366697436231, 1.689925910794]×10⁻¹³ | [5.928617637399, 9.956711152243]×10⁻¹⁷ | [4.796181447457, 6.313426646227]×10⁻¹⁸ | [−1.686607512876, −1.370408263621]×10⁻¹² |
| \(d_b\) | [−3.127854741570, −2.993844665600]×10⁻⁹ | [1.608398971389, 2.774242695334]×10⁻¹⁵ | [4.434566279600, 4.807180040710]×10⁻¹⁶ | [−3.253014902391, −3.107335579349]×10⁻¹⁰ |

\[
\partial_\lambda\Delta T\in
[-1.009599125635\times10^{-8},\ -8.137506081166\times10^{-9}]\ {\rm K},
\]

\[
\partial_b\Delta T\in
[6.776348385589\times10^{-5},\ 7.185335549648\times10^{-5}]\ {\rm K}.
\]

따라서 현재 고정 계열에서 두 전체 온도 미분의 부호가 결정됐다.
\(d_{\lambda,x}\)와 \(d_{\lambda,w}\)의 구간 폭은 보존된 Full/second-half
sensitivity의 독립 subtraction보다 각각 약 10,373배와 14,428배 작다.
\(b\) 미분의 대응 폭은 약 42.54배와 41.27배 작다. 이 수치는 동일
출발 구간의 표현 방식에 따른 포함 폭 비교다.

## 직접 forcing과 상태 feedback — forcing01

\(g_1,g_2\)를 고정한 명시적 매개변수 미분을 \(r^{exp}_\theta\),
실제 \(g_{1,\theta},g_{2,\theta}\)를 통한 항을 \(r^{fb}_\theta\)로 정했다.
동일한 \(J_F\)를 사용하여

\[
J_Fd^{exp}_\theta=r^{exp}_\theta-\int H_{g\theta}d,
\qquad
J_Fd^{fb}_\theta=r^{fb}_\theta-\int H_{gg}[d,y_\theta],
\qquad d_\theta=d^{exp}_\theta+d^{fb}_\theta
\]

를 적용했다. 온도 분모와 \(T_2\)를 미분하는 기하 항은 상태 feedback에
배정했다. Photon 항의 미분은 이 postprocess에서 수동 product rule로
별도 구현했으며, 두 매개변수 각각의 7×35개 항과 원 dual 결과의 교차가
모두 비어 있지 않음을 확인했다. 이는 두 구현의 일관성 검사이며
그 자체를 독립적인 포함 증명으로 사용하지 않는다.

| 온도 미분 | 직접 forcing, K | 상태·opacity feedback, K |
|---|---|---|
| \(\lambda\) | [−8.547862783773, −6.959235163714]×10⁻⁹ | [−1.548117483502, −1.178280571010]×10⁻⁹ |
| \(b\) | [6.784453758953, 7.193378236380]×10⁻⁵ | [−8.403008830470, −7.759040903738]×10⁻⁸ |

HH의 직접 항과 상태 반응은 모두 결함 온도를 낮춘다. Birth의 양의
직접 응답은 음의 상태 feedback을 포함한 뒤에도 양수다. 여기서
분리한 항은 하나의 전체 매개변수 미분에 대한 선형 전달 성분이다.
PHYS16의 원 잔차 sector attribution과는 미분 정의가 구별된다.

## 유한 Neumann 전달 — neumann02

\(f_\theta\)를 run02의 상관 우변, \(J_y=H_g(g_2)\)로 둔다. 보존된
\(q,L_H,a\)를 사용하면

\[
a_\theta=\frac{\|Cf_\theta\|_S}{1-q},\qquad
\epsilon_{F,2}=q^3a_\theta,\qquad
\epsilon_{y,2}=
\{q^3+L_Ha(1+q+q^2)\}a_\theta
\]

다. 이는 각각 \(J_F\), \(J_y\)로 만든 차수 2 Neumann 다항식과 실제
\(d_\theta\) 사이의 scaled norm 오차다. 두 endpoint Jacobian 차이는
\(\|C(J_y-J_F)\|_S\le L_Ha\)이므로 이 항에는 \(1/2\)가 붙지 않는다.
P4의 공통 온도 covector weighted one-norm은 2232.113973360 K 이하이다.

| 매개변수 | \(a_\theta\) 상한 | \(J_F\) 온도 미분 surrogate 오차 상한, K | \(J_y\) 대응 상한, K |
|---|---|---|---|
| \(\lambda\) | 1.126742971729×10⁻¹¹ | 4.066246749000×10⁻²⁰ | 8.959060026852×10⁻¹⁸ |
| \(b\) | 2.085472922428×10⁻⁷ | 7.526159651071×10⁻¹⁶ | 1.658219981417×10⁻¹³ |

각 계열의 점에서 같은 실제 \(J\), 우변, 유한 온도 분모를 사용하는
다항식의 오차 상계다. 현재 전체 response 구간의 폭과 구별하여 기록한다.

## 실행 기록과 보존

- `run01`: PHYS11의 존재하지 않는 `outgoing` 필드 참조로 계산 전에
  중단했다. 실제 필드는 `outgoing_joint`다. 실패 소스 `SOURCE.py`,
  `STDERR.txt`, `DIAGNOSIS.json`과 원 PRE/RUN 기록을 보존했다.
- `run02`: 해당 입력 대응을 교정한 뒤 exit 0, wrapper 0.666257393 s,
  source 내부 0.599975384 s, peak RSS 40,536 KiB.
- `forcing01`: 동결된 run02의 postprocess. exit 0, wrapper
  0.307982697 s, peak RSS 26,504 KiB.
- `neumann01`: P16의 exact endpoint norm보다 P17의 256-bit outward
  복사 구간 norm이 약 5.15×10⁻⁸³ 큰 것을 일관성 assertion이 검출하여
  결과 전에 중단했다. 두 유효 bound의 최댓값으로 외향 envelope를
  명시하고 상속 값과 실제 적용 값을 모두 출력하도록 교정했다.
- `neumann02`: 해당 교정 후 exit 0, wrapper 0.049938750 s, peak RSS
  16,000 KiB. 원 run02와 forcing01은 변경하지 않았다.

실제 재실행 명령은 각 `PRE_RUN.json`에 있으며 출력별 SHA-256와
입력 identity는 `RUN_RECORD.json` 및 결과 JSON에 있다.
`APPLICATION_FREEZE.json`, `FORCING_FEEDBACK_FREEZE.json`,
`DERIVATIVE_NEUMANN_FREEZE.json`은 독립 심사에
넘긴 소스·출력 identity를 기록한다. 원 두 candidate 출력은 이후 채택
여부와 분리하여 그대로 보존한다.
