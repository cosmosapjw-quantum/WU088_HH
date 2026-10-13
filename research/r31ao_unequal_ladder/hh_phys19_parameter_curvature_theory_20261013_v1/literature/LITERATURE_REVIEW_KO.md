# PHYS19 — 순수 매개변수 곡률과 bilinear remainder의 문헌 검토

확인일: 2026-10-13 KST. 문헌 분과 산출물이다. PHYS18의 NEXT_CURVATURE_PROPOSAL_KO.md, LITERATURE_REVIEW_KO.md 및 references.bib를 실제 읽고, SciSpace 1회·Exa 2회 검색 뒤 아래 3개 원전의 해당 본문을 확인했다. Exa Search 스킬의 searching.md와 patterns-papers.md를 적용했다.

## 1. 판정

WU088_HH에 필요한 일반 수학 구조는 기존 문헌과 직접 연결된다. 순수 implicit 2차 응답은 같은 state Jacobian을 사용하는 선형 방정식으로 계산할 수 있다. 단위 사각형의 bilinear interpolation에는 각 축의 순수 2차 도함수 전역 상계만으로 \((M_{\lambda\lambda}+M_{bb})/8\)의 오차 경계가 성립한다. 이번 연구의 구체적인 진전은 이 두 표준 구조에 원 gas–photon carry, 유한 온도 quotient, 공통 endpoint 차이와 검증된 inverse를 결합하여 실제 Kelvin 단위의 포함을 계산하는 데 있다.

원 PHYS18의 순수 곡률 응용 상태는 not_run으로 읽었다. 이 문헌 검토는 PHYS19의 실제 수치 실행이나 최종 gate 결과를 대신하지 않는다. 이번 분과는 새로운 문헌상의 일반 Hessian 정리나 interpolation 정리의 우선권을 주장하지 않는다.

## 2. 직접 채택하는 원전

| ID | 서지와 URL | 실제 읽은 본문 | 근거 상태와 사용 범위 |
|---|---|---|---|
| SLN15 | N. Safiran, J. Lotz, U. Naumann, *Second-order Tangent Solvers for Systems of Parameterized Nonlinear Equations*, Procedia Computer Science 51 (2015), 231–238. DOI: 10.1016/j.procs.2015.05.232. https://publications.rwth-aachen.de/record/569704/files/569704.pdf | §§2–3의 residual·Hessian 정의, §4.2 Thm 4.3, Eq. (7)와 증명, 인쇄 pp.235–236. §4 서두 및 p.236 끝의 기존 Jacobian factorization 재사용 문장도 확인. | supports. \(C^2\) residual, 선택된 exact solution branch와 그 state Jacobian의 가역성을 전제로 두 번째 tangent는 원 state Jacobian의 선형 solve로 구한다. 본문의 theorem은 exact root를 가정하므로 현재 작업에서는 inherited root certificate가 그 입력을 제공한다. |
| R99 | S. M. Rump, *Verified Solution of Large Linear and Nonlinear Systems*, in H. Bulgak and C. Zenger (eds.), *Error Control and Adaptivity in Scientific Computing*, pp.279–298, Kluwer, 1999. https://www.tuhh.de/ti3/paper/rump/Ru99d.pdf | §3, Lemma 3.1, Thm 3.2, Eqs. (3.2)–(3.6); 저자 PDF pp.4–5. 특히 interval matrix의 모든 구성원과 모든 RHS를 포함하는 양화 및 작은 residual 재표현에 관한 문단. | supports. 고정 실수 preconditioner와 interval Jacobian family에 대해 inclusion을 증명하면 family 전체의 가역성과 해 포함이 나온다. 실제 PHYS19 finite Neumann tail의 구체적인 식은 아래 직접 유도로 결박한다. |
| MR09 | B. Mößner, U. Reif, *Error bounds for polynomial tensor product interpolation*, Computing 86 (2009), 185–197. DOI: 10.1007/s00607-009-0062-7. 저자 원고 https://www.mathematik.tu-darmstadt.de/media/mathematik/forschung/preprint/preprints/2580.pdf ; 출판사 https://link.springer.com/article/10.1007/s00607-009-0062-7 | 2009-03-18 저자 원고 §2, Eqs. (1),(4); §3 “Simple Nodes”, Eq. (6), Thm 3.1과 증명, PDF pp.3–5. 출판사에서 저자·권·쪽·DOI를 대조. | supports. 사각형 box, 각 축 pairwise distinct interpolation nodes, bounded pure partial derivatives 아래 tensor-product interpolation의 최대 오차가 pure partials만으로 제어된다. 현재 endpoints 두 개는 이 정리의 가장 직접적인 특수 경우다. |

SLN15의 짧은 원문 확인 문장: “A previously computed factorization of the Jacobian of the residual can be reused.” 이 문장은 p.236, Eq. (7) 증명 직후에 있다.

MR09의 Thm 3.1은 simple nodes와 연속 함수의 순수 \(n_r\)차 편미분의 유계성을 가정한다. 문헌의 \(n_r\)는 interpolation node 개수이며, 각 축 선형 interpolation에는 \(n_r=2\)를 대입한다. 현재 전역 \(C^2\) 가정은 필요한 정칙성을 제공한다. 원고에서 항등연산자 기호가 text extraction 중 탈락하는 곳은 연산자 정의와 정리의 PDF 문맥을 함께 읽어 해석했다.

R99 §3 Thm 3.2의 내용은 고정 \(R\), interval matrix \([A]\), interval RHS \([b]\), 중심 \(\tilde x\), interval \(X\)에 대해
\[
R([b]-[A]\tilde x)+(I-R[A])X\subset\operatorname{int}X
\]
이면 \(R\)과 모든 \(A\in[A]\)가 가역이고, 모든 해당 RHS의 해가 \(\tilde x+X\)에 속한다는 것이다. 현재 작업에서 공통 Jacobian 포함을 재사용할 때 필요한 양화와 일치한다.

## 3. 순수 2차 응답과 carry의 대응

선택된 매개변수 \(\theta\in\{\lambda,b\}\), 상태 \(g(\theta)\), residual \(H(g,\theta)=0\), \(J=H_g\)에 대해
\[
Jp+H_\theta=0,\qquad p=g_\theta
\]
를 다시 미분하면
\[
JK=-\{H_{gg}[p,p]+2H_{g\theta}p+H_{\theta\theta}\},\qquad K=g_{\theta\theta}.
\]
이는 SLN15 Thm 4.3에 같은 parameter seed를 두 번 넣은 식이다. \(K\)는 ordinary second derivative이므로 Taylor 계수 \(1/2\)가 들어가지 않는다. 순수 항의 \(2H_{g\theta}p\)는 Hessian의 두 대칭 off-diagonal block에서 나온다.

첫 half와 Full의 fixed-input residual이 각 \(\theta\)에 affine이면 그 residual의 \(H_{\theta\theta}=0\)를 사용할 수 있다. 둘째 half의 전역 parameter dependence는 첫 half에서 넘어온 \(g_{1,\theta\theta}\), \(Q_{2,\theta}\), \(Q_{2,\theta\theta}\)를 포함한다. 따라서 둘째 half는 현재 proposal의 순서대로
\[
g_1 \longrightarrow Z_1 \longrightarrow Q_2 \longrightarrow g_2
\]
의 2차 chain rule을 적용해야 한다. 첫 단계 값과 매개변수 도함수를 모두 carry하는 구성은 전체 lower-triangular implicit system을 순서대로 미분해 푸는 것과 일치한다.

이 구조는 residual Hessian까지만 요구한다. 원 C2 signed Hessian 범위로부터 얻는 두 endpoint Hessian 차이는 해당 signed range의 집합 차로 포함한다. \(O(\lVert g_2-g_F\rVert)\)형으로 조이려면 별도의 modulus of continuity나 더 강한 smoothness 근거가 필요하다. 현재 proposal에서 HI 유리식을 직접 인수 분해하여 작은 endpoint 차이를 보존하는 부분은 그 명시적 식 자체의 근거를 사용한다.

SLN15의 계산복잡도 비교는 원 정확해에서 implicit derivative를 구할 때 nonlinear solver의 iteration count 의존성을 줄일 수 있다는 계산 구조를 뒷받침한다. 실제 PHYS19 runtime의 speedup은 구현·실행 자료로 따로 측정해야 하는 양이다.

## 4. 유한 Neumann inverse majorant: 실제 사용 식의 직접 연결

고정 preconditioner \(C\), 양의 diagonal scale \(S\), 모든 admissible \(J\in[J]\)에 대해
\[
E(J)=S^{-1}(I-CJ)S,\qquad \sup_{J\in[J]}\|E(J)\|_\infty\le q<1
\]
를 검증했다고 하자. 그러면
\[
J^{-1}=S(I-E)^{-1}S^{-1}C
=S\sum_{k=0}^{N}E^kS^{-1}C+
S\sum_{k=N+1}^\infty E^kS^{-1}C.
\]
RHS \(r\)에 대해 \(z=S^{-1}Cr\)로 놓으면 scaled solution은
\[
S^{-1}J^{-1}r\in
\sum_{k=0}^{N}[E]^k[z]+[-\eta,\eta]\mathbf1,\qquad
\eta=\frac{q^{N+1}}{1-q}\sup_{z\in[z]}\|z\|_\infty.
\]
마지막 tail은 submultiplicativity와 scalar geometric series에서 직접 나온다. 유한 부분의 signed interval 연산과 tail의 바깥쪽 rounding 또는 exact rational 상계가 전체 포함을 만든다. 동일한 \([J],C,S,q\)에 결박되어 있으면 첫 도함수·mixed·pure 도함수의 RHS가 바뀌어도 같은 inverse certificate를 재사용할 수 있다.

R99는 interval family 전체의 해 포함과 가역성을 검증하는 일반 근거로 사용한다. 위 \(N\)-항 tail과 PHYS19의 특정 rational 숫자는 원 식 및 실제 계산의 derived/implementation-verified 근거로 보존해야 한다. Neumann series 자체는 표준 기하급수 구성이다.

## 5. Bilinear remainder와 정확한 상수

\(I_\lambda,I_b\)를 각 축 endpoints의 선형 interpolation으로 두고 \(\mathcal LF=I_\lambda I_bF\)라 하자. MR09 Thm 3.1의 단위구간 특수화에서
\[
w_\lambda=w_b=\frac{\max_{0\le t\le1}|t(t-1)|}{2!}=\frac18,\qquad
\|I_\lambda\|_\infty=\|I_b\|_\infty=1.
\]
따라서
\[
\|F-\mathcal LF\|_\infty\le
\frac18\|F_{\lambda\lambda}\|_\infty+
\frac18\|F_{bb}\|_\infty.
\]
원 사각형이 변의 길이 \(h_\lambda,h_b\)를 가지면 각각의 항에 \(h_\lambda^2,h_b^2\)가 붙는다. 현재 \(\lambda,b\)는 무차원이고 함수 \(F=\Delta T\)의 단위가 K이므로 최종 remainder의 단위도 K다.

현재 proposal의 signed pointwise version은 문헌의 sup-norm 정리를 다음 Peano-kernel 식으로 직접 세분화한 것이다:
\[
f(x)-I_xf(x)=\int_0^1K_x(t)f''(t)\,dt,\qquad
K_x(t)=
\begin{cases}
-t(1-x),&t\le x,\\
-x(1-t),&t\ge x.
\end{cases}
\]
\(K_x\le0\), \(\int K_x=-x(1-x)/2\)와
\[
I-I_\lambda I_b=(I-I_\lambda)+I_\lambda(I-I_b)
\]
및 endpoint weights의 양성으로 proposal C18이 성립한다. 이는 직접 유도로 채택할 수 있고, 일반 tensor interpolation theorem의 신규 기여와 구분해 쓴다.

상수는 sharp하다. 직접 검산 함수
\[
F(\lambda,b)=\tfrac12A\lambda^2+\tfrac12Bb^2+D\lambda b,\quad A,B\ge0
\]
에서
\[
F-\mathcal LF=-\tfrac12A\lambda(1-\lambda)-\tfrac12Bb(1-b)
\]
이고 중심에서 절댓값이 \((A+B)/8\)다. bilinear 교차항은 정확히 재현된다. 이 예는 실제 물리계의 결과값이 아니라 정리 상수에 대한 derived 검산이다.

고정된 동일 \(\alpha\)의 네 corners와 도함수 범위를 사용한다는 양화를 유지해야 한다. 또한 여기서 인증하는 양은 two-half 대 Full 온도 결함 함수의 매개변수 interpolation 오차다. 두 경로 자체의 물리 시간적분 정확도는 원 endpoint defect 정의와 별도의 기준에 결박되어 있다.

## 6. 본 루프에서 채택 가능한 구체적 기여

| 구성 요소 | 기존 지식 | WU088_HH에서 이번 루프가 완성할 내용 |
|---|---|---|
| Pure implicit Hessian | SLN15의 같은 Jacobian 선형화와 2차 chain rule | 첫 half·Full·둘째 half의 실제 \(K_{\lambda\lambda},K_{bb}\), 35개 photon/guard 슬롯의 2차 carry |
| Rigorous inverse | R99의 interval family inclusion과 표준 Neumann tail | 원 source box와 결박된 경로별 \(C,S,q\), 실제 signed RHS와 유한 상계의 재사용 |
| Endpoint defect | 정확한 두 해 차이 및 Hessian bilinear 항등식 | 작은 공통 \(d,d_\theta,s,s_\theta\)를 먼저 묶은 signed defect curvature 포함 |
| Finite-temperature response | quotient의 정확한 chain rule | 원 \(\Pi>0\) 분모와 gas–electron readout을 유지하는 Kelvin 단위의 \(F_{\theta\theta}\) |
| Bilinear representation | MR09의 pure-derivative sup-norm 경계와 Peano kernel | 기존 음의 mixed interval, 동일-family coefficient, 실제 pure curvature를 합친 인증된 response representation |

이번 검색은 특정 benchmark의 최초 물리 응용 여부를 전수조사하지 않았다. 일반 이론의 선행성은 확인했고, 물리계에 결박된 실제 포함값과 재현 가능한 계산이 이번 loop의 성과 단위다.

## 7. 검색·접근 상태와 보존

- SciSpace: 완전한 자연어 질문 1회, 10개 응답 항목. Pacaud 및 Cacuci 중복 표제를 합치면 8개 후보 작업. Xue 2025, Pacaud 2022는 inherited PHYS18의 contextual 후보로 재확인했으며 이번 직접 의존성에 새로 추가하지 않았다.
- SciSpace에서 Hatten–Russell 2018, DOI 10.1007/s40295-018-0131-2가 implicit Runge–Kutta의 1·2차 state-transition sensitivity 관련 후보로 나왔다. 이번에는 abstract만 확인했으므로 contextual/abstract-only로 분류한다. 그 논문의 상세 식이나 성능 숫자는 채택하지 않았다.
- Exa: 서로 다른 두 질문, 각 numResults=6. 스킬의 sources_reviewed 계수는 요청 후보 수 12다. URL 단위 12개 결과 중 Mößner–Reif의 catalog/PDF와 Rump–Ogita의 두 사본을 합치면 작업 단위 후보 10개다. 이 수는 본문을 읽은 논문 수와 구분한다.
- Exa fetch: 1회에 저자 PDF 3개 URL 요청. MR09와 R99의 본문이 돌아왔고 RWTH의 SLN15는 CRAWL_EMPTY_CONTENT. SLN15는 별도 web 원문 open에서 8쪽 PDF의 본문과 Thm 4.3을 읽었다.
- Web: SLN15, MR09 저자 PDF, R99 저자 PDF 및 MR09 출판사 metadata를 직접 열었다. 확인이 끝난 후 추가 검색은 하지 않았다.
- 원 검색 응답 및 본문 캐시는 raw/에 있다. 공개 문서에는 이 검토·서지·읽기 위치·identity를 사용하고, 제3자 논문 전문 캐시는 private source cache로 취급한다.
- 부모 agent는 채팅 citation을 쓰기 전에 아래 3개 primary URL을 직접 open해야 한다. 이 분과의 citation ref는 각각 SLN15 turn0view0, MR09 turn1view0, R99 turn1view1이다.

