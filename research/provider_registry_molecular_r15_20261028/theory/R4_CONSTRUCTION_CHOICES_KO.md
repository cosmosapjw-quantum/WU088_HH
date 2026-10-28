# R15 R4 — positive cubic source에서 유한 quartic certificate로

상태: **R4 후보식·대안 비교·핵심 후보 논증·대표 예제 완료**. 이 문서는 R5 전체 증명, 독립 심사, CAS와 캠페인 실행에 넘길 설계다. 계산 예는 수동 exact 유도이며 저자의 과학 실행은 0회다. DAG는 **29/46**이며 root의 실제 S04 게시·백업 전에는 해당 영수증을 주장하지 않는다.

## 1. 선택한 입력과 출력

원래 source cell \([a,b]\)에서 \(v=(s-a)/(b-a)\)라 놓고

\[
g_r(s)=\sum_{i=0}^3r_i\mathsf B_i^3(v),\qquad
g_e(s)=\sum_{i=0}^3e_i\mathsf B_i^3(v),\qquad r_i,e_i\ge0
\]

를 입력받는다. 계수와 모든 clock은 exact rational이다. 이 함수를 whole fine/coarse-domain forcing bound로 제공한다는 전제는 원래 source/state/clock certificate에 결속된다. 입력은 원래 네 계수의 비음수성을 요구한다.

원래 \(t_0\)에서 시작하는

\[
\mathcal R(t)=h(t-t_0)R_0+\int_{t_0}^t h(t-s)g_r(s)\,ds,
\qquad h(a)=q^{\lfloor a/\tau\rfloor},\quad h(0)=1
\]

와

\[
\mathcal E(t)=e^{d_c(t-t_0)}E_0+
\int_{t_0}^t e^{d_c(t-s)}[c\mathcal R(s)+g_e(s)]\,ds
\]

를 유지한다. 출력은 exact base-cell B4 coefficients, actual endpoint와 left-limit 값, whole-\(\mathcal R\) lower/upper certificate, signed scalar endpoint enclosure와 whole-\(\mathcal E\) upper다. 하한은 입력 forcing bounds로 만든 **ideal comparison 함수**를 둘러싸며 실제 물리 오차의 하한이 아니다. 이전 raw/capped 결과에 대한 보편적 개선은 전제에 넣지 않는다.

## 2. 후보 A: exact positive B4 조립

\(B=\lfloor(T-t_0)/\tau\rfloor\)라 하자. Source knots를 \(k\tau\), \(0\le k\le B\)만큼 이동한 시각 중 domain에 속하는 점과 observation knots를 exact union하여 base grid를 만든다. 각 base cell \([A,A+\Delta]\)에서 \(t=A+\Delta u\), \(0\le u\le1\)를 쓴다. Source \([a,b]\)와 age strip k의 overlap은

\[
L(t)=\max\{a,t-(k+1)\tau\},\quad
U(t)=\min\{b,t-k\tau\},\quad D=U-L,\quad M=(L+U)/2.
\]

Grid가 max/min의 모든 switch를 포함하므로 cell interior의 선택은 고정된다. 빈 overlap은 건너뛰고, 나머지에서는 L/U/M이 source interval 내부의 비감소 affine map이며 \(D\ge0\)다. Cubic의 exact Simpson identity는

\[
I(t)=\int_{L(t)}^{U(t)}g_r(s)\,ds
=\frac{D(t)}6\,[g_r(L(t))+4g_r(M(t))+g_r(U(t))].
\]

이는 제공된 cubic polynomial에 대한 exact identity다. De Casteljau restriction으로 bracket의 B3 coefficients \(S_0,\ldots,S_3\)가 비음수임을 얻는다. \(D(u)=d_0(1-u)+d_1u\), \(d_0,d_1\ge0\)라 하면 product identity의 계수는

\[
\begin{aligned}
I_0&=d_0S_0/6,\\
I_1&=(3d_0S_1+d_1S_0)/24,\\
I_2&=(d_0S_2+d_1S_1)/12,\\
I_3&=(d_0S_3+3d_1S_2)/24,\\
I_4&=d_1S_3/6.
\end{aligned}
\]

각 overlap에 \(q^k\)를 곱해 합하고 \(h(A-t_0)R_0\)를 다섯 coefficients에 더해 \(P(u)=\sum_{i=0}^4B_i\mathsf B_i^4(u)\)를 한 번 만든다. 모든 coefficient는 비음수다. 이후 endpoint, left limit, subdivision, midpoint, 그림용 값은 이 저장된 polynomial을 사용한다. Subdivision은 source convolution을 재조립하거나 memory clock을 재시작하지 않는다.

## 3. 후보 B: mixed derivative leaves만 세분

Quartic derivative의 normalized-u Bernstein-B3 coefficients는

\[
v_i=4(B_{i+1}-B_i),\qquad 0\le i\le3.
\]

Zero를 제거한 list가 비어 있으면 constant다. Nonzero list가 한 부호이면 P가 monotone이므로 endpoints로 exact maximum을 정한다. 양·음 부호를 모두 가지면 mixed leaf로 분류한다. Depth가 96보다 작으면 exact midpoint de Casteljau split을 수행하고, depth96이면 coefficient-hull upper와 endpoint/midpoint sample lower를 저장한다. Leaf는 polynomial 값의 certificate이며 isolated root라는 표시는 하지 않는다.

### 3.1 Cubic에 대한 직접 variation 논증

\(V\)는 zero를 모두 제거한 뒤의 sign-change count다. 임의의 인접 x,y 사이에 convex average를 삽입하면 variation이 증가하지 않는다. 같은 부호이면 average도 같은 부호이고, 다른 부호이면 average의 부호는 두 부호 사이에서 한 번만 바뀐다. Zero도 이 정의로 처리된다. List에서 원소를 삭제하는 작업도 variation을 증가시키지 않는다.

Derivative coefficients를 \((a,b,c,d)\)라 쓰고

\[
e=(a+b)/2,\quad f=(b+c)/2,\quad g=(c+d)/2,
\]
\[
h=(e+f)/2,\quad i=(f+g)/2,\quad j=(h+i)/2
\]

로 둔다. 인접 average를 삽입하고 이전 interior entries를 삭제하면

\[
(a,b,c,d)\longrightarrow(a,e,f,g,d)
\longrightarrow(a,e,h,i,g,d)
\longrightarrow(a,e,h,j,i,g,d)
\]

를 얻는다. 첫 화살표는 e,f,g를 각각 원래 인접 entries 사이에 삽입한 뒤 b,c를 삭제하고, 두 번째는 h,i를 삽입한 뒤 f를 삭제한다. 각 단계에서 variation은 증가하지 않는다.

마지막 list는 left coefficients \(L=(a,e,h,j)\)와 right coefficients \(R=(j,i,g,d)\)를 shared midpoint j를 한 번만 적어 이어 붙인 것이다. j≠0이면 \(V(L)+V(R)=V(\mathrm{concat})\)다. j=0이면 zero를 제거한 후 left/right의 마지막·첫 nonzero 부호 사이에 추가 transition이 생길 수 있으므로

\[
V(L)+V(R)\le V(\mathrm{concat})\le V(a,b,c,d)
\]

다. 한쪽 또는 양쪽 list가 all-zero인 경우도 이 부등식에 포함된다. 따라서 midpoint root, repeated root, 실제 root가 없는 mixed controls를 따로 제외할 필요가 없다. 이 논증은 [Sagraloff Theorem 2(P4)](https://arxiv.org/pdf/1109.6279)의 재사용 조건을 degree3에서 직접 확인한다. Bernstein subdivision 규약은 [Mourrain–Rouillier–Roy §2](https://library.slmath.org/books/Book52/files/24roy.pdf)에 대응한다.

Sharma notes의 인쇄된 Theorem 6과 이어지는 midpoint-multiplicity 문장은 root가 원문 PDF p.6(0-based page5)의 실제 screenshot으로 확인했다. R2의 splitpoint 예는 이 parity 문구를 현재 zero-dropping/open-interval 규약에 그대로 적용하지 않도록 하는 국소 교정이다. 이번 구성에서는 위 직접 inequality를 사용한다.

Child P coefficients에서 \(4\Delta B\)를 다시 계산하면 derivative는 child의 local normalized coordinate를 따른다. 원래-u derivative를 제한한 coefficient와는 **양의 child width**만큼 차이가 나므로 sign variation은 같다. M_B는 계속 원래 base-cell normalized-u derivative에 대해 정의한다.

### 3.2 유한 작업량의 후보 결론

Derivative degree가 3이므로 초기 variation은 최대 3이다. 각 depth의 active mixed nodes의 variation 합은 이전 depth보다 커지지 않고, mixed node는 최소 1의 variation을 소비한다. 그러므로 한 depth에는 mixed nodes가 최대 3개다. Split은 depth0..D−1에서만 하므로

\[
N_{\rm split}\le3D,\qquad N_{\rm visit}=2N_{\rm split}+1\le6D+1.
\]

D=96이면 셀당 288 splits/577 visits다. Nbase≤512에서 147456 splits/295424 visits를 사전 charge한다. 동작은 polynomial extrema의 enclosure이므로 root separation 또는 모든 root의 고립을 종료 조건으로 사용하지 않는다. 이로써 depth limit을 유한 비용과 함께 구현할 수 있다.

## 4. Hull gap의 후보 논증

원래 base-cell coefficients에 대해

\[
M_B=4\max_i|B_{i+1}-B_i|,\qquad C_{\max}=\max_i B_i
\]

로 둔다. Width w인 restricted leaf의 P coefficients를 \(C_i\)라 하자. 원래-u derivative를 해당 leaf에 제한한 coefficients는 원래 \(4(B_{i+1}-B_i)\)의 convex combinations다. 따라서

\[
|4(C_{i+1}-C_i)|\le wM_B,
\qquad \max_iC_i-\min_iC_i\le\sum_{i=0}^3|C_{i+1}-C_i|\le wM_B.
\]

값의 Lipschitz 성질만으로 coefficient hull의 여유를 대신 추정하지 않고 위 계수 차이 관계를 사용한다. Every P sample은 convex hull 안에 있으므로 unresolved depth-D leaf의 hull upper와 sample lower 차이는 \(M_B2^{-D}\) 이하다. Monotone leaf의 local maximum은 exact다. 각 leaf의 lower/upper를 전체에서 각각 max로 합치면

\[
0\le U_{\rm exact}-L_{\rm exact}\le M_B2^{-D}\le4C_{\max}2^{-D}.
\]

마지막 부등식은 원래 \(B_i\ge0\)이므로 \(|B_{i+1}-B_i|\le C_{\max}\)라는 사실을 쓴다. Lower를 dyadic128 floor, upper를 dyadic128 ceil로 변환하면 차이는 추가로 최대 \(2\cdot2^{-128}\) 늘어난다. 이 absolute bound의 units는 \(\mathcal R\)의 units다. Observation whole cells는 포함된 base certificates의 max를 취하므로 gap은 해당 local bounds의 최대 이하로 보존된다.

실제 right endpoint는 같은 시각의 h로 별도 평가한다. Forcing convolution은 연속이고 initial staircase만 하향 jump하므로 이 endpoint는 해당 left limit보다 크지 않다. Supremum은 approaching left limit을 포함하며, 그 witness를 attained point로 표시하지 않는다.

## 5. Signed scalar로의 계산 사상

같은 base cell의 \(g_e\) B3 coefficients를 \((e_0,e_1,e_2,e_3)\)라 하면 B4 elevation은

\[
\left(e_0,\frac{e_0+3e_1}{4},\frac{e_1+e_2}{2},
\frac{3e_2+e_3}{4},e_3\right).
\]

이에 \(cB_i\)를 더한 \(Q_i\ge0\)가 forcing \(cP+g_e\)를 표현한다. \(z=d_c\Delta\)라 할 때

\[
W_i(z,\Delta)=\Delta\int_0^1e^{z(1-u)}\mathsf B_i^4(u)\,du,
\quad
\mathcal E_{\rm next}=e^z\mathcal E_{\rm left}+\sum_{i=0}^4Q_iW_i(z,\Delta).
\]

z≥0의 candidate series는

\[
W_i(z,\Delta)=\Delta\sum_{n=0}^\infty\frac{z^n}{n!}\beta_i(n),
\quad
\beta_i(n)=\binom4i\frac{i!(n+4-i)!}{(n+5)!}.
\]

이를 다섯 rational factor로 쓰면

\[
\begin{aligned}
\beta_0&=\frac1{n+5},&
\beta_1&=\frac4{(n+4)(n+5)},\\
\beta_2&=\frac{12}{(n+3)(n+4)(n+5)},&
\beta_3&=\frac{24}{(n+2)(n+3)(n+4)(n+5)},\\
\beta_4&=\frac{24}{(n+1)(n+2)(n+3)(n+4)(n+5)}.
\end{aligned}
\]

모두 양수·nonincreasing이고 \(\beta_i(0)=1/5\)다. z<0에서는

\[
W_i(z,\Delta)=e^zW_{4-i}(-z,\Delta)
\]

를 사용한다. Taylor degree96의 first omitted index는 97이며, 그 다음 term들의 ratio는 \(|z|/98\le16/98<1\) 이하로 잡는다. R5에서 positive tail, directed sum/product, reciprocal를 포함한 전체 outward arithmetic proof를 닫는다. d_c의 damping sign을 절댓값으로 대체하지 않는다.

Whole-E는 \(Q_{\max}=cU_R+U_e\)와 incoming upper \(E_L\)에서

\[
Y(x)=e^{d_cx}E_L+Q_{\max}\int_0^xe^{d_c(x-v)}dv,
\quad Y'(x)=e^{d_cx}(d_cE_L+Q_{\max})
\]

를 사용한다. Derivative sign이 일정하므로 whole upper는 \(\max(E_L,Y(\Delta))\)를 outward로 계산한 값이다. 다음 셀은 별도의 더 촘촘한 polynomial endpoint enclosure를 받아 진행한다.

## 6. 독립 original-integral reference 사상

Production의 positive overlap 조립 대신 원래 cubic을 \(g_j(s)=\sum_{m=0}^3a_m(s-a_j)^m\)로 둔다. \(x=t-a_j\), \(\Delta J_\ell=J_\ell(t-a_j)-J_\ell(t-b_j)\)에서

\[
J_\ell(x)=\int_0^{\max(x,0)}v^\ell h(v)\,dv,
\quad
F_j(t)=\sum_{m=0}^3a_m\sum_{\ell=0}^m
\binom m\ell x^{m-\ell}(-1)^\ell\Delta J_\ell
\]

를 직접 구현한다. 각 J는 full blocks와 마지막 partial block의 유한 rational power sum이다. 이를 기반으로 독립 power quartic과 derivative critical points를 계산한다. Exact Sturm를 쓰는 reference 내부 Euclid coefficient cap은 root의 C3 계획에서 1,048,576 bits로 분리한다. Production/saved-derived cap16,384 bits, input256 bits, CPU·memory와 guard는 유지한다.

Scalar reference의 coordinate를 명확히 한다. **Elapsed physical time**의 forcing \(\sum_m a_mx^m\)이면

\[
\int_0^\Delta e^{d_c(\Delta-x)}x^m dx
=m!\Delta^{m+1}\phi_{m+1}(z).
\]

**Normalized u**의 forcing \(\sum_m A_mu^m\)이면 같은 항은 \(\Delta\,m!\phi_{m+1}(z)\)다. 두 좌표의 coefficients를 혼용하지 않는다. 필요한 orders는 phi1..phi5다. Decimal160/고정 relative guard1e-80를 사용하는 부분은 guarded corroboration으로 기록하고 exact component와 strict no-guard misses를 분리한다.

## 7. 비교한 대안과 선택 이유

| 구성 | 얻는 것 | 이번 선택과의 관계 |
|---|---|---|
| Positive B4 + mixed derivative variation subdivision | positivity, exact rational geometry, linear-depth visit bound와 명시적 hull gap | production 후보로 선택 |
| Exact Sturm + critical-point boxes | root multiplicity와 isolating intervals를 독립 power basis에서 다룰 수 있음 | separately authored reference 후보; Euclid intermediate cap 별도 |
| Cubic derivative의 radical formulas | exact algebraic critical points 표현 가능 | repeated-root branch·outward evaluation을 추가 구현해야 하므로 현재 production에는 채택하지 않음 |
| 모든 cell을 uniform depth96까지 분할 | 단순한 mesh-width bound | leaves가 2^96개인 계획은 현재 finite-work 계약 밖이므로 mixed-only traversal 선택 |
| Depth0 Bernstein hull | 즉시 유효한 whole upper | 고정 depth96의 gap 목표를 일반적으로 보장하려면 추가 refinement 필요 |
| 모든 pointwise-nonnegative cubic의 사전 양성화 | 더 넓은 입력 함수를 받는 후속 문제 | 현재 original-coefficient cone을 유지하며 이 전처리는 다음 별도 의무로 남김 |

Cubic derivative를 새로운 추상 객체로 등록하는 대신, sign list → split coefficients → count/gap → saved certificate라는 직접 구현 사상을 사용한다. 이 표현이 줄이는 작업은 overlap 재조립과 root separation에 의존하는 무제한 세분이다.

## 8. 수동 exact 대표 예제와 다음 판별 대상

아래는 모두 실행 전 계산한 목표값이다. 표의 exact identity 확인은 수동 대입·적분이며 캠페인 PASS로 집계하지 않는다. 기본값은 \(t_0=0,R_0=E_0=0,c=1,d_c=0,g_e=0\)다.

| 예제 | 입력 | 수동 목표와 의미 |
|---|---|---|
| 첫 cubic 구성 | \(q=1,g_r(s)=s^3,T=1\) | \(I(t)=t[4(t/2)^3+t^3]/6=t^4/4\); B4=(0,0,0,0,1/4), R(1)=1/4, E(1)=1/20 |
| 차수별 limit | \(q=1,g_r=s^k,T=1,k=0,1,2,3\) | \(R(1)=1/(k+1)\), \(E(1)=1/[(k+1)(k+2)]\) |
| q=0 actual/left 분리 | \(q=0,\tau=1,g_r=s^3,R_0=1,T=1\) | actual R(1)=1/4, left-limit 및 whole supremum=5/4, E(1)=21/20 |
| 원래 history 유지 | \(q=1/2,\tau=1,g_r=s^3,T=5/4\) | R=\(T^4/4-(T-1)^4/8=1249/2048\), E=\(T^5/20-(T-1)^5/40=6249/40960\) |
| 실제 derivative roots 3개 | \(P=1+u^4/4-u^3/2+11u^2/32-3u/32\) | B4=(1,125/128,97/96,125/128,1); P′=(u−1/4)(u−1/2)(u−3/4), V=3; max P=1, interior local maximum P(1/2)=127/128 |
| 비-dyadic repeated root | \(P=1+u^3/3-u^2/3+u/9\) | B4=(1,37/36,1,1,10/9); P′=(u−1/3)^2, derivative B3=(1/9,−1/9,0,4/9); mixed leaves를 root isolation으로 오인하지 않는 depth-cap control |
| Rootless mixed derivative | \(P'(u)=(u-1/2)^2+1/100\) | derivative B3=(13/50,−11/150,−11/150,13/50), V=2이지만 derivative는 항상 양수; mixed라는 이유로 root를 보고하지 않음 |
| z=0 moments | 모든 Q_i=1, z=0 | 모든 W_i=Δ/5, 합=Δ |
| signed constant forcing | Q=1,E0=0,Δ=1,d_c=±2 또는0 | E(1)=(e²−1)/2, (1−e^−2)/2, 1 각각; damping sign·zero limit 판별 |

첫 예제는 candidate map의 실제 결과를 직접 계산한다. 나머지는 implementation guard·mutation·reference 계약의 표적이다. 앞으로 사용할 본격 과학 실행은 root의 frozen primary/reference/CAS allowance에서만 수행한다.

## 9. R5로 넘길 남은 의무

R5는 위 coefficient construction, event coverage, convolution endpoint semantics, direct variation·count·gap, degree-four moment/reflection/tail, scalar comparison을 한 정리의 가정과 결론으로 연결한다. Exact rational positive arithmetic와 derived-cap 처리의 구현 대응도 표시한다. R6는 독립 논증·정적 구현 심사, R7는 실제 허용 실행, R8/R9는 그 근거에 따른 주장별 판정과 계산식 계약을 담당한다. R2/R3/R4 단계 종료가 이 후속 결과를 선행 인정하지 않는다.

실제 HD reactive array와 named consumer/state/density/clock는 별도 source-binding 의무다. 현재 native v UNSPECIFIED, MISSING_NOT_ZERO, TIQM/SQM distinct, HH_R10 OFF, production NOT_ISSUED, L4 false, central/physical delta0을 보존한다. R2에 기록한 `skill_context_used`를 그대로 적용했다.
