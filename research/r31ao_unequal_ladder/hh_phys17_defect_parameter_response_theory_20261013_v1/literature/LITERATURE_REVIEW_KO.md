# PHYS17 — 매개변수 결함 응답의 문헌 대응

검색·원문 확인일: 2026-10-13 KST. 대상은 WU088_HH의 같은 COMMON, 고정 admissible \(\alpha\), 전역 \((\lambda,b)\in[0,1]^2\)에서 \(d=g_2-g_F\), \(\Delta T=T_2-T_F\)의 1차 매개변수 응답이다.

Exa 검색 4회(요청 후보 수 합계 20)와 SciSpace 자연어 검색 1회(실제 반환 10개)를 수행했다. 원문 fetch 4회와 필요한 원 스캔 읽기를 추가했다. Exa 후보 수는 중복을 포함하는 요청 수다. 새 핵심 비교 원전은 아래 네 개이며, PHYS16에서 대조한 Rump 2010과 Rannacher 2003의 전제·결과는 해당 기록을 재사용한다. 검색 원 응답과 논문 전문은 별도 private source cache에 보존하고, 공개 연구 묶음에는 서지·근거 위치·이 문서의 자체 대응만 싣는다.

## 1. 문헌으로 확인한 위치와 이번 구성

Implicit root의 1차 미분
\[
x_\theta=-\mathcal H_g(x,\theta)^{-1}\mathcal H_\theta(x,\theta)
\]
와 adjoint를 통한 관측량 미분은 기존 방법이다. 검증된 전처리로 그 선형식의 해를 외측 포함하고 같은 매개변수의 slope를 유지하는 구성도 기존 검증 수치해석에 근거가 있다.

이번 연구의 직접 구성은 작은 **두 경로의 결함 \(d\)** 를 미분식에 먼저 인수 분해하고, 기존 Full의 signed \(\mathcal H_{gg},\mathcal H_{g\theta}\) 및 실제 stage carry에 연결하는 것이다. PHYS16의 원 잔차·유한 온도 분모를 그대로 사용하여, 같은 \(\theta\)의 직접 forcing과 state/opacity feedback을 함께 포함한다. 따라서 새 기여는 원 WU088_HH 자료에 대한 이 상관 응답식의 유도·평가와 그 부호 판정이다.

## 2. 새 핵심 원전

| ID | 원전과 실제 읽은 위치 | 확인한 조건·결과 | PHYS17에 채택하는 대응 |
|---|---|---|---|
| N89 | A. Neumaier, *Rigorous sensitivity analysis for parameter-dependent systems of equations*, J. Math. Anal. Appl. 144(1) (1989), 16–25. DOI 10.1016/0022-247X(89)90357-0. 저자 스캔 pp.17–24, Thms 2.1, 3.1, 4.1, Cor.4.2. | \(F\in C^1\), convex \(D\times T\), regular state slope enclosure \(A\), parameter slope \(B\), known reference root에서 \(x(t)\in x^0+S(t-t^0)\), \(S\supseteq-A^{-1}B\). Cor.4.2는 slope 폭에 따른 과대포함 반경의 계산 가능한 경계를 준다. | 같은 \(\theta\)를 보존한 slope/mean-value 표현을 사용할 근거. 현재 \(d_\theta\)는 P2에서 직접 유도하고 원 전처리로 포함한다. |
| R90 | S. M. Rump, *Rigorous sensitivity analysis for systems of linear and nonlinear equations*, Math. Comp. 54 (1990), 721–736. DOI 10.1090/S0025-5718-1990-1011445-5. 저자 PDF Thms 3, 4, 6, 7 및 §3. | 전처리 fixed-point의 strict inclusion으로 선형 interval family의 regularity와 외측 포함을 얻는다. \(C^1\) 비선형 family의 공통 Jacobian enclosure로 확장한다. 입력을 독립적으로 변동시키는 집합에 대한 inner hull 추정도 따로 다룬다. | \(J_Fd_\theta=v_\theta\)를 같은 \(C,B\)로 외측 포함하는 구조. 실제 shared-parameter 집합은 그 직사각형 완화 안에 들어가므로 외측 포함을 채택한다. 독립 tolerance 집합에 관한 inner sharpness는 현재 HH 결과의 근거에 포함하지 않는다. |
| G08 | A. Goldsztejn, *Sensitivity Analysis Using a Fixed Point Interval Iteration*, arXiv:0811.2984 (2008). §§1–2, Thm 2, Eqs (5)–(6), Rem.3. | Parameter box 전체에서의 Hansen–Sengupta inclusion 및 존재·유일성 검사를 제시한다. Jacobian box와 residual enclosure가 모든 parameter/state 조합을 포함해야 한다. 고정 preconditioner를 먼저 곱한 centered parameter expression이 더 좁은 포함을 줄 수 있음을 설명한다. | 원 family가 box 전체에서 존재한다는 상속 근거와 외측 연산의 양화를 정렬하는 비교. 기존에 확인한 근을 새로 계산할 의무를 추가하지 않는다. |
| MB22 | C. C. Margossian and M. Betancourt, *Efficient Automatic Differentiation of Implicit Functions*, arXiv:2112.14217v2 (26 Feb 2022). §§2.2.2–2.3.1, 원 PDF pp.18–24. | 비특이 constraint Jacobian 아래 \(-C_y^{-1}C_x\)로 implicit derivative를 계산하며, transpose solve로 그 covector 수축을 계산한다. 직접 trace AD와 implicit derivative 계산의 대상·계산 구조를 구별한다. | 원 Full 근의 \(g_{F,\theta}\)와 현재 observable derivative의 표준 연결. 실제 PHYS17의 작은 차이 분해·구간 상계는 원 source와 P2–P4에서 직접 증명한다. |

원문 URL:

- N89: https://arnold-neumaier.at/scan/60.pdf
- R90: https://www.tuhh.de/ti3/paper/rump/Ru90a.pdf
- G08: https://arxiv.org/pdf/0811.2984
- MB22: https://arxiv.org/pdf/2112.14217v2

N89는 텍스트 추출이 되지 않는 스캔이었다. 저자 PDF 343,719 bytes를 실제 읽고 회전·crop한 페이지 이미지로 Thm 3.1과 Cor.4.2의 조건과 부호를 확인했다. 파일 SHA-256은 `1832b6b342fdd396f783cc6bbf84e04cb9087c064de5e71ab7e9eaf371443e87`다. Exa가 반환한 MB22 표지의 원 arXiv version/date와 본문의 구별은 해당 v2 PDF를 기준으로 고정했다.

## 3. 재사용한 PHYS16 원전

Rump 2010의 interval inverse 전달과 Rannacher 2003의 goal-oriented adjoint 비교는 PHYS16 `literature/LITERATURE_REVIEW_KO.md` 및 `references.bib`의 읽기 기록을 재사용한다.

- S. M. Rump, *Verification methods: Rigorous results using floating-point arithmetic*, Acta Numerica 19 (2010), 287–449. DOI 10.1017/S096249291000005X. 현재 연결은 fixed \(C,B,q,S\)와 포함 연산이다.
- R. Rannacher, *Adaptive Finite Element Methods for Partial Differential Equations*, arXiv:math/0305006. 현재 연결은 하나의 goal covector로 잔차를 가중하는 구조다. 원 Galerkin Lagrangian의 cubic remainder와 현재 \(C^2\) finite-dimensional 식의 전제는 PHYS16에서 이미 구분했다.

현재 새 미분 유도는 PHYS16의 Hessian remainder를 다시 미분하지 않는다. 원 implicit 식을 미분하고 \(\mathcal H_g\) 및 \(\mathcal H_\theta\)의 선분 차이를 각각 전개하므로, 원 \(C^2\) 자료에서 필요한 모든 항이 닫힌다.

## 4. PHYS17의 직접 유도와 문헌 대응

\(x=g_F\), \(y=g_2\), \(d=y-x\), \(r=\mathcal H(y,\theta)\)라 두면
\[
\mathcal H_g(x)d_\theta
=\mathcal H_g(x)y_\theta+\mathcal H_\theta(x).
\]
이 식과
\[
r_\theta=\mathcal H_g(y)y_\theta+\mathcal H_\theta(y)
\]
를 빼고 같은 선분 \(y-sd\)에서 적분하면
\[
\mathcal H_g(x)d_\theta
=r_\theta-\int_0^1\{
\mathcal H_{gg}(y-sd)[d,y_\theta]
+\mathcal H_{g\theta}(y-sd)d
\}\,ds.
\]
이는 N89의 common slope 원리와 MB22의 implicit differentiation을 현재 작은 결함에 맞게 결합한 직접 식이다.

상태 비 \(f_2\)와 \(C_T\)를 고정하면
\[
\Delta T=\frac{C_Td_w-T_2\ell_ed}{\Pi_F},\qquad
\Pi_F=\Pi_2-\ell_ed,
\]
따라서
\[
(\Delta T)_\theta=
\frac{C_Td_{w,\theta}-T_2d_{e,\theta}
-T_{2,\theta}d_e-\Delta T(\ell_ey_\theta-d_{e,\theta})}{\Pi_F}.
\]
이 정확한 분모가 매개변수 미분의 단위를 K/무차원 \(\theta\)로 유지한다. 독립 유도는 `review/INITIAL_FORMULA_REVIEW_KO.md`에 있으며, 실제 포함 및 채택 상태는 새 후보의 독립 심사에 연결한다.

## 5. 인용 범위의 최소 교정

MB22 §2.1에는 Jacobian 가역성과 implicit 함수의 존재를 “if and only if”로 설명하는 문장이 있다. \(c(p,x)=(x-p)^3\)는 유일한 매끄러운 해 \(x=p\)를 가지면서 해에서 \(c_x=0\)이므로, 그 문장의 필요조건 방향은 일반적으로 성립하지 않는다. 본 연구에서는 **원 \(C^2\) source와 확인된 \(J_F\) 가역성**을 충분조건으로 고정하고 §§2.2.2–2.3.1의 미분 항등식만 인용한다. 이 교정은 현재 WU088_HH의 어느 입력·성공 기준도 변경하지 않는다.

SciSpace에서 반환한 interval reachability, SIVIA·Monte Carlo, inverse parameter estimation 및 electromagnetic surrogate 문헌은 해당 목적과 현재의 유한 차원 implicit endpoint 미분의 차이 때문에 핵심 증명의 의존성에서 제외했다. 원 state와 parameter를 동시에 미분하는 데 직접 필요한 항목을 위 원전으로 한정했다.

## 6. 다음 판정에 사용할 검토 범위

1. P2–P4의 동일 매개변수, residual/source 부호와 차원.
2. 원 \(\mathcal H_{gg},\mathcal H_{g\lambda},\mathcal H_{gb}\) slot과 시간계수의 대응.
3. 실제 photon carry의 모든 explicit birth 및 opacity feedback.
4. 원 \(C,B,q,S\)의 immutable identity, 선형 포함과 \(\Pi_F>0\).
5. 실제 결과 구간, 필요한 부호 여유, 독립 arithmetic와 Wolfram/xAct 기록.

현재 문헌 검토의 결론은 **해당 조건 아래 P1–P4의 구성과 표준 inverse/adjoint 연결을 채택**하는 것이다. 새 수치 적용의 판정은 `review/INDEPENDENT_REVIEW.json`에 기록한다.

