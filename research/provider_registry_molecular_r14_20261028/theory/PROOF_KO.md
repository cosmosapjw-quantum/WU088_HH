# R14 수동 이론 초안: 비정렬 quadratic forcing과 exact cubic residual

상태: root가 선택한 유한 R14 설계를 위한 저자 수동 유도. 이 문서의 저자는 새 과학 Python 실행·import·compile·CAS·ODE를 수행하지 않았다. 독립 심사 판정이 아니며 root의 계약·구현·허용 실행·독립 심사·채택 전에는 R14 채택 결과가 아니다.

## 1. 재사용하는 전제와 새 입력

R11–R13의 조건부 full-generator 전제를 유지한다. 고정 column-conservative Metzler \(K\), 고정 \(\pi,d\), \(H=\pi d^T-\operatorname{diag}(d)\), 전체 인증 \(w\) box에서 \(A_w=K+wH\)를 쓴다. 같은 family의 모든 시작시각에서 zero-mass \(l^1\) propagator가 길이 \(\tau>0\)마다 \(q\in[0,1]\) 이하이고 짧은 나머지에서는 nonexpansive라는 전제로

\[
h(a)=q^{\lfloor a/\tau\rfloor},\qquad h(0)=1
\]

을 재사용한다. \(q=0\)에서도 \(q^0=1\)이다. Nominal \(K\) rho를 full \(A\)에 직접 이식하지 않는다. Zero-mass residual, whole fine/coarse-domain forcing, \(E=|\eta|\), coarse \(l^1=4E\), 고정 \(c\ge0\), 고정 signed \(d_c\)를 보존한다.

원래 rational source partition \(t_0=a_0<\cdots<a_N=T\)의 각 셀에서 \(g_r,g_e\)는 rational quadratic Bernstein triplet \((b_0,b_1,b_2)\)로 주어진다.

\[
g(a_j+\Delta_j u)=b_0(1-u)^2+2b_1u(1-u)+b_2u^2,\quad 0\le u\le1.
\]

\(b_1\)에는 음수를 허용한다. 각 polynomial의 whole-interval 비음수성은 exact 검사한다. 이 검사는 polynomial의 비음수성을 증명한다. 이것이 실제 nonlinear forcing의 whole-domain 상계라는 입력 전제는 별개다. 세 sample로 그 상계 전제를 만들지 않는다. 셀 사이 one-sided source 값은 달라도 된다.

R13과 같은 ideal comparison을 유지한다.

\[
\mathcal R(t)=h(t-t_0)R_0+\int_{t_0}^{t}h(t-s)g_r(s)\,ds,
\]
\[
\mathcal E(t)=e^{d_c(t-t_0)}E_0+
\int_{t_0}^{t}e^{d_c(t-s)}[c\mathcal R(s)+g_e(s)]\,ds.
\]

모든 source history는 원래 \(t_0\)부터 남는다. Observation/source refinement나 kernel block 경계에서 \(\mathcal R\) memory를 reset하지 않는다. Raw lower는 chosen-rational-\(q\) ideal comparison의 lower이며 physical error의 lower가 아니다.

## 2. Full nonnegative quadratic cone의 유한 전처리

입력 power 계수를 \(A=b_0-2b_1+b_2,\ B=2(b_1-b_0),\ C=b_0\)라 하자. 비음수성은 \(C\), \(A+B+C\), 그리고 \(A>0,\ 0<-B/(2A)<1\)인 경우 vertex 값만 검사하면 충분하고 필요하다. 비교는 rational exact이다. Concave/linear polynomial의 최소는 endpoints에 있다.

전처리에서는 \(A\ne0\)인 모든 strict-interior vertex를 삽입한다. 각 원래 source cell의 \(g_r,g_e\) vertex union을 취한다. 한 원래 셀당 새 knot가 최대 둘이므로 \(N_{\mathrm{eff}}\le3N_{\mathrm{src}}\)다.

각 effective piece에서 두 함수는 각각 monotone이고 비음수다. R13의 quadratic Bernstein lemma를 source polynomial에만 재사용한다. 길이 \(D\)에서

\[
\beta_0=P(0),\quad
\beta_1=P(0)+\tfrac D2P'(0)=P(D)-\tfrac D2P'(D),\quad
\beta_2=P(D).
\]

Increasing이면 \(\beta_1\ge\beta_0\ge0\), decreasing이면 \(\beta_1\ge\beta_2\ge0\)다. 따라서 restriction의 세 coefficients는 비음수다. 원래 middle coefficient가 음수인 입력도 허용된다. 원래 source 함수·domain·state/clock을 hash에 결속하고 effective split은 exact equivalent 내부 표현으로 기록한다.

### 2.1 Cubic에 R13 lemma를 자동 이식하지 않는 이유

\[
P(x)=\int_0^x(s-\tfrac14)^2\,ds
=\tfrac{x^3}{3}-\tfrac{x^2}{4}+\tfrac{x}{16}
\]

는 \([0,1]\)에서 비음수·비감소이지만 cubic Bernstein coefficients는 \((0,1/48,-1/24,7/48)\)다. 따라서 nonnegative monotone cubic만으로 coefficient positivity를 주장할 수 없다. 이 예는 그 중간 lemma의 범위만 판별한다. Broad impossibility나 strong no-go는 주장하지 않는다. 다음 positive overlap 구성은 그 이식을 필요로 하지 않는다.

## 3. 정확한 event grid와 positive cubic overlap

\(B_{\max}=\lfloor(T-t_0)/\tau\rfloor\)라 하자. Base event set은 effective source knots를 \(k\tau,\ k=0,\ldots,B_{\max}\)만큼 이동한 점 중 \([t_0,T]\) 안의 점과 observation knots의 exact union이다. \(a_0=t_0\)이므로 initial block knots도 포함된다. \(k=B_{\max}+1\) 이동은 domain 밖이다.

각 effective source \([a,b]\), age strip \(k\)에서

\[
L(t)=\max(a,t-(k+1)\tau),\qquad U(t)=\min(b,t-k\tau)
\]

를 쓴다. Base cell interior에서는 max/min 선택과 overlap의 empty/nonempty 여부가 고정된다. Nonempty overlap에서 \(L,U\)는 affine이고 \(D=U-L\ge0,\ M=(L+U)/2\)다. 알려진 quadratic의 exact Simpson identity는

\[
I(t)=\int_{L(t)}^{U(t)}g_r(s)\,ds
=\frac{D(t)}6[g_r(L(t))+4g_r(M(t))+g_r(U(t))].
\]

이는 입력으로 결속된 quadratic에 대한 exact polynomial identity이며 unknown forcing의 sample quadrature가 아니다.

Base coordinate \(x\in[0,1]\)에서 \(g_r(L),g_r(M),g_r(U)\)는 effective source quadratic의 affine restriction이다. 각 argument는 source interval 안에서 증가하거나 일정하다. De Casteljau restriction은 원래 비음수 coefficients의 convex combination이므로 bracket의 quadratic coefficients \(S_0,S_1,S_2\)는 비음수다. \(D(x)=d_0(1-x)+d_1x,\ d_0,d_1\ge0\)에서 cubic coefficients는

\[
I_0=\frac{d_0S_0}{6},\quad
I_1=\frac{2d_0S_1+d_1S_0}{18},\quad
I_2=\frac{d_0S_2+2d_1S_1}{18},\quad
I_3=\frac{d_1S_2}{6}.
\]

증명은 Bernstein product identity

\[
\mathsf B_i^m(x)\mathsf B_j^n(x)
=\frac{\binom mi\binom nj}{\binom{m+n}{i+j}}\mathsf B_{i+j}^{m+n}(x)
\]

의 \(m=1,n=2\) 경우다. 각 overlap에 \(q^k\)를 곱해 합하고, cell 왼쪽 \(b\)에서 고정된 \(h(b-t_0)R_0\)를 네 coefficients에 모두 더하면

\[
P(x)=\mathcal R(b+\Delta x)=\sum_{i=0}^3B_i\mathsf B_i^3(x),\quad B_i\ge0
\]

를 얻는다. Cell interior와 왼쪽 실제 right-continuous 값에서 exact이며 오른쪽에서는 left limit다. Forcing convolution \(F\)는 연속이고 initial term만 block 경계에서 downward jump할 수 있다. 실제 오른쪽 endpoint는 저장된 \(F\) coefficients와 해당 시각의 initial coefficient로 계산한다. Final \(T\)에서는 last polynomial right value에 \([h(T-t_0)-h(b-t_0)]R_0\)만 더한다. Supremum은 left limit도 포함한다.

## 4. 독립 reference용 primitive identity

\(x_+=\max(x,0),\ n=\lfloor x_+/\tau\rfloor,\ m=0,1,2\)에 대해

\[
J_m(x)=\sum_{k=0}^{n-1}q^k
\frac{((k+1)\tau)^{m+1}-(k\tau)^{m+1}}{m+1}
+q^n\frac{x_+^{m+1}-(n\tau)^{m+1}}{m+1}.
\]

이는 \(\int_0^{x_+}v^mh(v)\,dv\)다. Source \(g(s)=\alpha+\beta(s-a)+\gamma(s-a)^2\), \(x=t-a,\ \Delta J_m=J_m(t-a)-J_m(t-b)\)이면

\[
F_j(t)=(\alpha+\beta x+\gamma x^2)\Delta J_0
-(\beta+2\gamma x)\Delta J_1+\gamma\Delta J_2.
\]

증명은 \(v=t-s\) 치환이다. Production의 positive Simpson 조립과 독립적으로 구현할 수 있고 \(q=0,1\)에서 singular denominator가 없다.

필요하면 normalized samples \(y_i=P(i/3),\ i=0,1,2,3\)의 forward differences \(\delta_1,\delta_2,\delta_3\)로

\[
a_0=y_0,\quad a_1=3\delta_1-\tfrac32\delta_2+\delta_3,\quad
a_2=\tfrac92(\delta_2-\delta_3),\quad a_3=\tfrac92\delta_3
\]

를 얻는다. 오른쪽 sample에는 동일 cell initial coefficient를 써서 left limit를 취한다. Reference는 production module을 import하지 않는다.

## 5. Rational critical-root boxes와 whole-\(\mathcal R\) enclosure

Cubic critical points가 irrational일 수 있으므로 E propagation time knots에 넣지 않는다. Normalized derivative \(D(x)=P'(x)=Ax^2+Bx+C\)에서 rational arithmetic으로 다음을 수행한다.

1. \(A=B=C=0\): constant polynomial, supremum exact.
2. \(A=B=0,C\ne0\): critical root 없음.
3. \(A=0,B\ne0\): \(-C/B\)를 exact 계산하고 strict interior일 때 후보로 보존.
4. \(A\ne0\): rational derivative vertex \(v=-B/(2A)\)가 strict interior이면 \([0,1]\)을 그 점에서 나눔. 각 branch에서 derivative는 strict monotone.
5. Branch endpoints의 exact zero는 exact root 후보. Interior vertex zero는 double root. Endpoint zero를 가진 branch에서 추가 sign-changing root를 추정하지 않음.
6. Strict opposite endpoint signs를 갖는 branch에는 root가 정확히 하나. 최대 96회의 rational midpoint bisection. Midpoint exact zero이면 조기 종결하고 아니면 strict sign bracket 보존.

Distinct interior roots는 최대 둘이다. 초기 normalized width가 1 이하이므로 남은 bracket width는 \(2^{-96}\) 이하이다. 두 brackets가 derivative vertex에서 닿아도 그 shared point는 nonroot이고 branch별 uniqueness가 이미 증명되어 있다. 가까운 roots, boundary 근처 roots, double root, degree reduction은 exact sign/zero 분기로 처리한다.

\[
C_{\max}=\max_iB_i,\qquad M_B=3\max_{i=0,1,2}|B_{i+1}-B_i|
\]

라 하자. Rootbox \([a,b]\)의 width를 \(w\), exact restriction coefficients를 \(c_i\)라 하면 original derivative coefficients \(3(B_{i+1}-B_i)\)의 convex-hull 성질과 chain factor \(w\)로

\[
|c_{i+1}-c_i|\le wM_B/3,\qquad
\max_i c_i-\min_i c_i\le wM_B.
\]

\(P((a+b)/2)\)는 coefficient hull 안에 있다. 각 box에서 \(U_j=\max_i c_i,\ L_j=P((a+b)/2)\)를 취한다. Exact candidates는 \(P(0)\), \(P(1)\) left limit, 모든 exact interior critical values이며 필요하면 actual right endpoint도 넣는다. 각각 exact candidates와 \(L_j\), exact candidates와 \(U_j\)의 최대를 \(L,U\)로 두면

\[
L\le\sup_{[0,1]}P\le U,\qquad
0\le U-L\le M_B2^{-96}\le3C_{\max}2^{-96}.
\]

Cubic maximum은 endpoint 또는 derivative zero에 있으므로 inclusion이 성립한다. \(U\)가 exact candidate이면 gap 0, box \(j\)이면 \(L\ge L_j\)로 gap을 얻는다. 마지막 부등식은 \(B_i\in[0,C_{\max}]\)를 쓴다. \(C_{\max}=0\)이면 모두 0이다.

Observation cell은 그 안의 모든 base enclosures를 max로 합치며 gap은 최대 local gap 이하다. 이것은 irrational supremum을 exact rational 값이라고 주장하지 않는다. Exact rational isolating boxes와 rational supremum enclosure를 출력한다. Lower witness가 left limit이면 유효한 supremum lower지만 attained point sample이라고 표시하지 않는다.

## 6. Degree-three positive exponential integration

Base cell에 제한된 \(g_e\)의 nonnegative quadratic coefficients를 \(e_0,e_1,e_2\)라 하면 degree elevation은

\[
(e_0,(e_0+2e_1)/3,(2e_1+e_2)/3,e_2).
\]

따라서 \(cP+g_e\)의 cubic coefficients \(Q_i\)는 모두 비음수다. \(z=d_c\Delta\)에서

\[
W_i(z,\Delta)=\Delta\int_0^1e^{z(1-u)}
\binom3i u^i(1-u)^{3-i}\,du
\]

를 정의하면 exact endpoint recurrence는

\[
\mathcal E_{\rm next}=e^z\mathcal E_{\rm left}+\sum_{i=0}^3W_i(z,\Delta)Q_i.
\]

\(\mathcal R\)의 endpoint jump는 적분을 바꾸지 않는다. \(z=0\)이면 모든 \(W_i=\Delta/4\)이고 \(\sum_iW_i=\Delta\phi_1(z)\)다.

\(x\ge0\)에서 \(W_i(x,\Delta)/\Delta=\sum_{n\ge0}x^n\beta_i(n)/n!\), 여기서

\[
\beta_0(n)=\frac1{n+4},\quad
\beta_1(n)=\frac3{(n+3)(n+4)},\quad
\beta_2(n)=\frac6{(n+2)(n+3)(n+4)},\quad
\beta_3(n)=\frac6{(n+1)(n+2)(n+3)(n+4)}.
\]

이는 positive exponential series와 beta integral의 직접 계산이다. 모두 positive, nonincreasing, 1 이하이며 \(\beta_i(0)=1/4\)다. \(z<0\)에서는 \(u\mapsto1-u\)로 \(W_i(z,\Delta)=e^zW_{3-i}(-z,\Delta)\)를 얻는다.

R13의 positive integer directed recurrence 및 exponential-tail 증명을 새 네 beta coefficients에 적용한다. Fixed \(N=96,\ 0\le x\le16\)에서 first omitted exponential term 이후 ratio는 \(x/(N+2)<1\) 이하라 geometric tail이 유효하다. \(\beta_i\le1\)이므로 동일 exponential tail은 각 moment의 conservative upper tail이다. Dyadic \(2^{128}\) floor/ceil recurrence, positive rational factors, positive interval products와 sums는 outward enclosure를 보존한다. 기존 degree-two 구현이 새 moments를 계산한다고 주장하지 않는다.

Independent reference는 signed power forcing과

\[
\int_0^\Delta e^{d_c(\Delta-u)}u^m\,du
=m!\Delta^{m+1}\phi_{m+1}(z),\quad m=0,1,2,3
\]

를 사용한다. \(d_c=0\)은 exact rational, 그 외 Decimal precision·guard·small-\(z\) policy는 실행 전 고정한다.

## 7. Whole-\(\mathcal E\)와 endpoint propagation

Base cell의 certified \(\mathcal R\) upper를 \(U_R\), \(g_e\)의 exact quadratic maximum 또는 positive-hull upper를 \(U_e\)라 하자. \(Q_{\max}=cU_R+U_e\ge0\), 유효한 left upper \(E_L\)에서

\[
Y(u)=e^{d_cu}E_L+Q_{\max}\int_0^ue^{d_c(u-v)}\,dv
\]

는 whole cell에서 \(\mathcal E\)를 지배한다. \(Y'(u)=e^{d_cu}(d_cE_L+Q_{\max})\)의 sign은 일정하므로 whole upper는 outward \(\max(E_L,Y(\Delta))\)다. 다음 cell에는 별도로 계산한 더 촘촘한 polynomial endpoint upper를 전달한다.

Rootbox는 whole-\(\mathcal R\)에만 쓰인다. Exact polynomial E recurrence는 rational base cells에서 수행하므로 irrational time lengths나 rootbox clock uncertainty가 없다. Observation closed cells를 gap 없이 덮으며 R memory를 reset하지 않는다.

## 8. 유한 자원

제안 domain은 original source cells 16 이하, observation cells 32 이하, effective source cells 48 이하, horizon blocks 8 이하이다.

\[
N_{\rm base}\le(N_{\rm eff}+1)(B_{\max}+1)+(N_{\rm obs}+1)-1\le473.
\]

512 guard는 보수적이다. Base cells·effective sources·age strips 조합을 한 번씩 precharge하면

\[
N_{\rm base}N_{\rm eff}(B_{\max}+1)\le512\cdot48\cdot9
=221184<250000.
\]

Root bisections는 \(2\cdot96N_{\rm base}\le98304\)다. Input bits 256, derived rational bits 16384, \(|d_c|(T-t_0)\le16\), fixed dyadic128/Taylor96는 별도 finite guards다. Count bound만으로 bit bound를 증명하지 않으며 실제 연산에 checks가 필요하다.

이 overlap bound는 base-cell coefficients 구축 한 번 기준이다. Production endpoint/left-limit/rootbox/midpoint/display는 stored coefficients를 재사용하고 별도 overlap query API를 제공하지 않는다는 root 결정에 결속한다. 추가 F 재합산을 하려면 별도 precharge해야 한다. 실행 횟수·CPU·wall·memory는 root가 실행 전 고정하며 과거 allowance는 증가시키지 않는다.

## 9. 재사용 범위와 남은 의무

R13에서 재사용한 단위는 full-A premise, staircase memory, rational translated events, source용 quadratic Bernstein lemma, positive directed arithmetic 패턴, constant-forcing whole-E majorant다. 새 단위는 full nonnegative quadratic validation·source vertex preprocessing, Simpson-positive cubic construction, derivative-quadratic rational isolation, finite supremum gap, degree-three beta weights다.

Bernstein hull/subdivision/degree elevation과 polynomial-forcing exponential integration은 기존 문헌의 표준 도구다. 실제 읽은 범위는 별도 provenance에 기록한다. 전역 신규성이나 broad impossibility를 주장하지 않는다. 더 작은 proved source bound에서는 positivity로 ideal R/E가 pointwise 작거나 같지만 strict gain은 입력에 달려 있다.

Actual HD reactive array 및 named physical consumer/state/density/clock은 별도 입력 결속 대상이다. Native v=UNSPECIFIED, MISSING_NOT_ZERO, TIQM/SQM 구별을 유지한다. 별도 적격 실제 입력 없이는 HH_R10=OFF, production=NOT_ISSUED, L4=false, central/physical delta=0을 바꾸지 않는다.

이 저자 문서는 독립 PASS가 아니다. 남은 의무는 root의 immutable census/baseline 확정, finite contract, implementation, frozen primary/reference/CAS, independent proof/code review, scoped adoption 및 단계별 실제 publication/backup ACK다.

