# R15 구성적 증명 — cubic Bernstein forcing, quartic memory와 유한 whole-cell enclosure

증거 상태: **범위가 명시된 저자 직접 유도 완료**. 아래 수학 논증은 수동으로 작성했다. 이 파일의 작성 시점에는 새 CAS, primary/reference 캠페인, 과학 import/compile, 독립 R6 심사를 수행하지 않았다. 이 직접 유도와 후속 외부 corroboration·구현 검증·DAG 채택은 별도로 기록한다. R2/R3/R4의 이미 게시된 파일은 보존하고 이 파일을 R5 산출물로 추가한다.

현재 실제 S04는 `3dae38e813f0ef952990698910d1481eee78357f`, workflow **8/20**, DAG **29/46**이다. R5/C5 게시·백업 및 이후 판정은 root의 실제 영수증과 결과에 따른다.

## 1. 정리의 가정과 결론

정확한 유리수 \(t_0<T\), \(\tau>0\), \(0\le q\le1\), \(R_0,E_0,c\ge0\), 고정 signed \(d_c\)를 둔다. Source partition \(t_0=a_0<\cdots<a_N=T\)과 observation partition은 exact rational이며 같은 시작·종료 시각을 갖는다. 각 원래 source cell의 \(g_r,g_e\)는 네 개의 **주어진 비음수 rational Bernstein-B3 계수**로 표현한다. Adjacent cells의 one-sided source 값은 달라도 된다.

물리 비교에 적용할 때에는 고정 column-conservative Metzler \(K\), 고정 \(\pi\ge0\), \(\mathbf1^\top\pi=1\), destruction vector \(d\ge0\), 비음수 w box에서

\[
H=\pi d^\top-\operatorname{diag}(d),\qquad A_w=K+wH
\]

의 실제 evolution operator U에 대해, 전체 인증 w box에서 **허용된 모든 시작시각과 history**에 동일하게

\[
\|U(s+\tau,s)\|_{\mathrm{zero\ mass},1}\le q,
\qquad \|U(s+\delta,s)\|_{\mathrm{zero\ mass},1}\le1
\quad(0\le\delta<\tau)
\]

라는 전제를 둔다. w(t)가 변할 수 있는 family라면 그 허용 switching histories 자체에 대한 certificate가 필요하다. 각 constant-w autonomous operator에 대한 pointwise certificate만 있으면 그 확인된 constant-w histories에 범위를 제한하며 switching histories로 자동 확장하지 않는다. 원래 source family, state order, norm, clock가 이 certificate와 같고 \(g_r,g_e\)가 관련 whole fine/coarse domain의 forcing을 지배해야 한다. Signed scalar differential comparison과 \(E=|\eta|\), coarse \(l^1=4E\)도 보존한다. c는 비교 결합계수다. 입력의 certificate flags는 이러한 전제의 선언과 identity 결속이며 새 물리 certificate를 생성하는 절차가 아니다.

다음 ideal comparisons를 정의한다.

\[
h(a)=q^{\lfloor a/\tau\rfloor}\quad(a\ge0),\qquad h(0)=1,
\tag{1}
\]
\[
\mathcal R(t)=h(t-t_0)R_0+\int_{t_0}^t h(t-s)g_r(s)\,ds,
\tag{2}
\]
\[
\mathcal E(t)=e^{d_c(t-t_0)}E_0+
\int_{t_0}^t e^{d_c(t-s)}[c\mathcal R(s)+g_e(s)]\,ds.
\tag{3}
\]

식(1)의 \(q=0\)은 \(0\le a<\tau\)에서 h=1, \(a\ge\tau\)에서 h=0이라는 뜻이다. 이는 kernel 정의에 포함된 \(q^0=1\) 규약이다.

**정리.** 아래 exact event grid의 각 base cell에서 식(2)의 right-continuous 왼쪽 값, 내부 값 및 오른쪽 left limit는 한 번 조립한 비음수 Bernstein-B4 polynomial로 표현된다. Derivative-B3의 mixed-sign leaves만 깊이 D까지 midpoint subdivision하면 셀당 split≤3D, visit≤6D+1이고, exact supremum enclosure는

\[
0\le U-L\le M_B2^{-D}\le4C_{\max}2^{-D},
\quad M_B=4\max_i|B_{i+1}-B_i|,\quad C_{\max}=\max_iB_i.
\tag{4}
\]

D=96과 dyadic128 outward conversion의 추가 폭 \(2\cdot2^{-128}\)을 적용할 수 있다. 비음수 B4 exponential moments와 signed reflection은 식(3)의 endpoint를 outward로 전달하며, 상수 forcing majorant는 whole-cell \(\mathcal E\) upper를 제공한다. Full-A·forcing 전제가 성립하면 이 ideal comparisons는 원래 residual/scalar error의 상계다.

출력의 lower endpoints는 식(2)·(3)으로 정의한 **ideal comparison 함수**의 하한이다. 실제 물리 오차의 하한을 뜻하지 않는다. Whole-cell lower는 supremum의 하한이며 매 시각의 값보다 작다는 뜻도 아니다. 더 작은 입력 forcing bound가 주어지면 양의 kernel로부터 비교함수의 단조성이 따르지만, R14와 R15의 서로 다른 입력 사이에 보편적 raw/capped/physical gain을 전제하지 않는다.

## 2. Full-A 비교에서 원래 memory까지

나이 \(a=m\tau+\delta\), \(m\in\mathbb N_0,0\le\delta<\tau\)를 m개의 full block과 한 short remainder로 나눈다. 모든 시작시각에 같은 q가 적용되고 operator norm이 submultiplicative이므로 zero-mass propagator norm은 \(q^m\) 이하다. \(\delta=0\)이면 short remainder는 identity다. 따라서 h는 모든 두 시각 사이의 유효한 비교 kernel이다.

Zero-mass Duhamel 식에 norm을 취하고 초기 bound \(R_0\), forcing bound \(g_r\)를 사용하면 residual norm≤식(2)다. Signed scalar comparison

\[
D^+E\le d_cE+c\|r\|_1+g_e
\]

에 positive integrating factor를 사용하면 식(3)을 얻는다. 이 논증은 \(d_c\)의 양·음·0 모두에 적용된다. \(K\)만의 수축률로 full \(A_w\)의 q를 대체하지 않는다.

식(2)의 적분 하한은 모든 base/observation/source refinement에서 원래 \(t_0\)다. 셀 경계마다 \(h\)의 나이나 \(R_0\)를 재설정하면 다른 비교함수가 된다. 이후의 finite subdivision은 polynomial maximum을 평가하는 데만 쓰고 propagation clock에 넣지 않는다.

## 3. Event grid가 모든 branch를 덮음

\(B=\lfloor(T-t_0)/\tau\rfloor\)라 하자. Γ는 observation knots와

\[
\{a_j+k\tau:0\le j\le N,\ 0\le k\le B\}\cap[t_0,T]
\tag{5}
\]

의 sorted exact union이다. Source knot \(a_0=t_0\) 때문에 모든 initial-kernel jump \(t_0+k\tau\)도 들어 있다.

Source cell \([a,b]\)와 age strip k의 적분 구간은 measure-zero endpoint 규약을 제외하면

\[
L(t)=\max(a,t-(k+1)\tau),\quad
U(t)=\min(b,t-k\tau).
\tag{6}
\]

L의 branch switch는 \(a+(k+1)\tau\), U의 switch는 \(b+k\tau\)다. Overlap의 시작·끝은 \(a+k\tau\), \(b+(k+1)\tau\)다. 이들 중 domain 안의 시각은 모두 식(5)에 들어간다. k=B일 때 shift B+1이 필요한 후보는 \(t_0+(B+1)\tau>T\)이므로 domain 밖이다. 따라서 각 열린 base cell에서 branch와 overlap의 empty/nonempty 여부가 고정된다.

Nonempty overlap에서 L,U는 slope0 또는1의 affine functions이고 source interval 안에 있다. \(D(t)=U(t)-L(t)\ge0\), \(M(t)=(L(t)+U(t))/2\)도 affine다. Closed base cell로 연속 확장해도 이 관계는 유지되며, boundary에서 D=0이 되어도 아래 식은 정확히 0을 준다. 시간 t에서 가능한 나이는 0..T−t0이므로 k=0..B가 모든 적분 strip을 포함한다.

## 4. Restriction과 positive B4 overlap

\(\mathsf B_i^n(u)=\binom ni u^i(1-u)^{n-i}\)로 둔다. n차 polynomial의 polar form은

\[
\mathcal B(y_1,\ldots,y_n)
=\sum_{S\subseteq\{1,\ldots,n\}}b_{|S|}
\prod_{j\in S}y_j\prod_{j\notin S}(1-y_j).
\tag{7}
\]

0≤y_j≤1이면 weights가 비음수이고 합이1이다. Diagonal \(y_j=u\)에서 원래 Bernstein polynomial이 되며, affine restriction \(u=\alpha+(\beta-\alpha)v\)의 i번째 Bernstein coefficient는 \(\mathcal B(\alpha^{n-i},\beta^i)\)다. 이는 multi-affinity를 전개하거나 de Casteljau subdivision으로 확인할 수 있다. 따라서 \(0\le\alpha\le\beta\le1\)인 restriction은 원래 coefficient의 convex combinations다. \(\alpha=\beta\)이면 모든 coefficients가 그 점의 값인 constant polynomial이다.

Base coordinate를 \(t=A+\Delta u\)로 둔다. L/M/U가 source interval 안의 비감소 affine maps이므로 \(g_r(L),g_r(M),g_r(U)\)의 B3 coefficients는 모두 비음수다. Source cubic을 L+Dv로 치환하면 Simpson functional과 exact integral은 \(1,v,v^2,v^3\) 각각에서 일치한다. 그러므로

\[
I(t)=\int_{L(t)}^{U(t)}g_r(s)ds
=\frac{D(t)}6\{g_r(L(t))+4g_r(M(t))+g_r(U(t))\}.
\tag{8}
\]

Braces의 B3 coefficients를 \(S_0,\ldots,S_3\ge0\), D의 B1 coefficients를 \(d_0,d_1\ge0\)라 하자. 항등식

\[
\mathsf B_i^m\mathsf B_j^n
=\frac{\binom mi\binom nj}{\binom{m+n}{i+j}}\mathsf B_{i+j}^{m+n}
\tag{9}
\]

에서 식(8)의 다섯 B4 coefficients는

\[
\left(
\frac{d_0S_0}{6},
\frac{3d_0S_1+d_1S_0}{24},
\frac{d_0S_2+d_1S_1}{12},
\frac{d_0S_3+3d_1S_2}{24},
\frac{d_1S_3}{6}
\right).
\tag{10}
\]

각 성분은 비음수다. 모든 source/strip에 \(q^k\ge0\)를 곱해 합하면 convolution의 B4 coefficients를 얻는다. Constant \(h(A-t_0)R_0\)를 다섯 성분 모두에 더해

\[
P(u)=\sum_{i=0}^4B_i\mathsf B_i^4(u),\qquad B_i\ge0
\tag{11}
\]

를 한 번 조립한다. Polynomial degree가 실제로 4보다 작거나 일부 coefficients가 0이어도 같은 표현과 증명이 적용된다. Empty overlap은 0, degenerate affine map은 식(7)의 constant case로 처리한다.

## 5. Continuity, actual endpoint와 left limit

\(G(x)=\int_{t_0}^{\min(x,T)}g_r(s)ds\)를 x≤t0에서0으로 연장한다. Source가 bounded piecewise polynomial이므로 G는 연속이다. 유한 horizon에서 staircase는

\[
h(a)=1+\sum_{n=1}^B(q^n-q^{n-1})\mathbf1_{a\ge n\tau}
\]

로 쓸 수 있으므로 convolution F는

\[
F(t)=G(t)+\sum_{n=1}^B(q^n-q^{n-1})G(t-n\tau).
\tag{12}
\]

따라서 source discontinuity와 age-strip switch에서도 F는 연속이다. 이 signed expression은 continuity와 독립 reference를 설명하는 식이며 production의 positive 조립은 식(8)–(11)을 따른다.

Base cell \([A,B_c]\)에서 P(0)은 실제 \(\mathcal R(A)\), 내부 P는 식(2), P(1)은 \(\mathcal R(B_c^-)\)다. 실제 오른쪽 endpoint는 저장된 F와 정확한 h를 사용해

\[
\mathcal R(B_c)=P(1)+[h(B_c-t_0)-h(A-t_0)]R_0.
\tag{13}
\]

식(13)의 보정은 0 이하이며 initial block jump가 없으면0이다. q=0의 첫 jump와 final T가 block boundary인 경우도 포함한다. Closed interval의 supremum에는 접근 가능한 left limit가 들어가므로 polynomial maximum과 actual endpoint를 함께 취할 수 있다. 여기서는 actual right≤P(1)이어서 supremum은 P의 closed maximum과 같다. 다만 저장된 witness가 P(1)이면 **left-limit witness**이며 attained point sample이라고 표시하지 않는다.

Observation cell의 왼쪽에서 이전 cell의 left limit를 끌어오지 않는다. Observation cell 안에 들어 있는 base cells의 실제 왼쪽 값·내부·오른쪽 left limits로만 그 closed-cell supremum을 구성한다. 이 방식은 내부 경계의 접근값과 실제 경계값을 빠짐없이 포함한다.

## 6. Derivative-B3 subdivision의 직접 variation lemma

Zero를 모두 제거한 real coefficient list의 sign changes를 V로 정의한다. All-zero list에는 V=0을 둔다. 인접 entries x,y 사이에 convex average \((1-\theta)x+\theta y\), 0≤θ≤1를 삽입해도 V는 증가하지 않는다. 같은 부호이면 average가 그 부호이고, 다른 부호이면 세 항 사이에서 한 번만 바뀌기 때문이다. Zero는 제거되어 같은 결론을 준다. Entry 삭제도 V를 증가시키지 않는다. 두 nonzero 바깥 부호 사이의 transition 수는 가운데 부호를 경유한 transition 수 이하이기 때문이다.

원래 cubic coefficients \((a,b,c,d)\)에서

\[
e=(a+b)/2,\ f=(b+c)/2,\ g=(c+d)/2,
\quad h=(e+f)/2,\ i=(f+g)/2,\ j=(h+i)/2
\]

를 만든다. 인접 average 삽입과 entry 삭제를 순서대로 하면

\[
(a,b,c,d)\to(a,e,f,g,d)
\to(a,e,h,i,g,d)
\to(a,e,h,j,i,g,d).
\tag{14}
\]

첫 단계는 e/f/g를 원래 이웃 사이에 모두 삽입한 뒤 b/c를 삭제하고, 두 번째는 h/i를 삽입한 뒤 f를 삭제한다. 마지막 list는 de Casteljau children

\[
L=(a,e,h,j),\qquad R=(j,i,g,d)
\]

를 shared j를 한 번만 적어 붙인 것이다. j≠0이면 \(V(L)+V(R)=V(\mathrm{concat})\)이고, j=0이면 zero를 제거할 때 left/right의 nonzero 끝 부호 사이에 추가 transition 하나가 생길 수 있다. 한쪽 또는 양쪽 all-zero도 포함하여

\[
V(L)+V(R)\le V(\mathrm{concat})\le V(a,b,c,d).
\tag{15}
\]

이것으로 필요한 cubic variation inequality가 직접 증명되었다. Repeated root, splitpoint root, 실제 root가 없는 mixed coefficients를 제외하는 조건은 없다. Sagraloff Theorem2(P4)와 MRR의 Bernstein/Möbius 대응은 같은 classical property의 원전 근거다. Sharma 원문 p.6의 midpoint parity 문구는 root가 실제 화면으로 확인했으며, 해당 문구를 별도의 midpoint multiplicity 처리 없이 적용하지 않는다. 이 증명은 식(15)만 사용한다.

## 7. 극값 알고리즘과 3D/6D+1 작업량

식(11)의 normalized-u derivative는

\[
P'(u)=\sum_{i=0}^3 4(B_{i+1}-B_i)\mathsf B_i^3(u).
\tag{16}
\]

모든 derivative coefficients가0이면 P는 constant다. Zero 제거 후 한 부호이면 derivative는 whole interval에서 같은 weak sign이므로 endpoint maximum이 exact다. Mixed이면 V≥1이다. 다음 규칙을 사용한다.

1. Constant 또는 one-sign leaf: exact endpoint maximum을 local lower와 upper로 저장한다.
2. Mixed leaf이며 depth<D: exact midpoint에서 P를 분할하고 두 children을 방문한다.
3. Mixed leaf이며 depth=D: restricted B4 coefficient maximum을 upper로, endpoints와 midpoint의 exact 값 중 최대를 lower로 저장한다.

P child에서 식(16)을 계산하면 child normalized coordinate의 derivative다. 원래-u derivative를 child interval에 제한한 것에 **양의 interval width**를 곱한 관계이므로 V는 같다. 식(15)는 모든 split에 적용된다.

Derivative degree≤3이므로 초기 V≤3이다. 각 depth의 mixed-node variations 합은 이전 depth의 합 이하이고, mixed node마다 V≥1이다. 따라서 depth마다 mixed nodes≤3이다. Split depth는 0..D−1이므로

\[
N_{\rm split}\le3D.
\]

모든 split은 정확히 두 children을 만들고 root는 하나이므로 complete traversal의 visits는 \(2N_{\rm split}+1\le6D+1\)이다. All-zero/monotone root는 split0/visit1이다. D=0의 mixed root도 즉시 hull terminal이므로 같은 bounds가 성립한다. Active leaves는 전체 구간을 gap 없이 덮고 겹침은 shared endpoints뿐이다.

이 알고리즘은 extrema의 enclosure를 만든다. Mixed terminal leaf에 실근이 존재하거나 하나만 존재한다고 결론내리지 않는다. 따라서 root separation이나 square-free root-isolation 종료를 전제로 하지 않으며, dyadic splitpoint roots와 non-dyadic repeated roots를 그대로 허용한다.

## 8. Coefficient hull에서 exact gap까지

원래-u interval width w의 restricted P coefficients를 \(C_0,\ldots,C_4\)라 하자. 식(7)에 의해 restricted original derivative coefficients는 원래 \(4(B_{i+1}-B_i)\)의 convex combinations이므로 절댓값≤M_B다. Chain rule과 식(16)에서

\[
4(C_{i+1}-C_i)=w\,v_i^{\rm restricted},
\quad |4(C_{i+1}-C_i)|\le wM_B.
\tag{17}
\]

따라서

\[
\max_iC_i-\min_iC_i
\le\sum_{i=0}^3|C_{i+1}-C_i|\le wM_B.
\tag{18}
\]

Every P value는 coefficient hull 안에 있다. Mixed depth-D leaf의 w는 정확히 \(2^{-D}\)이고 sample lower는 적어도 \(\min_iC_i\)이므로 local upper−lower≤식(18)이다. Monotone/constant leaves의 local gap은0이다. 각 leaf의 lower/upper를 \(L_j,U_j\)라 할 때

\[
L=\max_jL_j\le\sup P\le\max_jU_j=U,
\quad U-L\le\max_j(U_j-L_j)\le M_B2^{-D}.
\]

원래 \(B_i\ge0\)에서 \(|B_{i+1}-B_i|\le C_{\max}\)이므로 식(4)의 마지막 부등식이 성립한다. General signed B4에도 첫 M_B bound는 성립하지만 \(4C_{\max}\) 결론은 현재 비음수 B4 전제를 사용한다.

\(Q=2^{128}\), \(\downarrow x=\lfloor Qx\rfloor/Q\), \(\uparrow x=\lceil Qx\rceil/Q\)라 두면

\[
0\le\uparrow U-\downarrow L
\le M_B2^{-D}+2Q^{-1}.
\tag{19}
\]

Observation-cell lower/upper는 그 안의 base bounds를 각각 max로 합치므로 exact gap은 local bounds의 최대 이하로 유지된다. Base cells를 모두 저장한 뒤 다시 source convolution을 조립할 필요가 없다.

## 9. Degree-four exponential moments와 signed reflection

제한된 \(g_e\)의 B3 coefficients \((e_0,e_1,e_2,e_3)\)를 B4로 올리면

\[
\left(e_0,\frac{e_0+3e_1}{4},\frac{e_1+e_2}{2},
\frac{3e_2+e_3}{4},e_3\right).
\tag{20}
\]

이에 \(cB_i\)를 더한 Q_i는 모두 비음수이고 \(cP+g_e\)를 정확히 나타낸다. z=\(d_c\Delta\)에서

\[
W_i(z,\Delta)=\Delta\int_0^1e^{z(1-u)}\mathsf B_i^4(u)du,
\quad
\mathcal E_{\rm right}=e^z\mathcal E_{\rm left}+\sum_{i=0}^4Q_iW_i.
\tag{21}
\]

R의 isolated endpoint jumps는 이 적분을 바꾸지 않으며 E는 연속이다.

z≥0에서는 positive series의 termwise integration으로

\[
W_i(z,\Delta)=\Delta\sum_{n=0}^\infty\frac{z^n}{n!}\beta_i(n),
\quad
\beta_i(n)=\binom4i\frac{i!(n+4-i)!}{(n+5)!}.
\tag{22}
\]

Termwise exchange는 nonnegative terms의 monotone convergence로 정당화된다. Beta integral은 integer powers를 적분하거나 반복 integration by parts로 직접 얻는다. Equivalent rational factors는

\[
\begin{aligned}
\beta_0(n)&=\frac1{n+5},&
\beta_1(n)&=\frac4{(n+4)(n+5)},\\
\beta_2(n)&=\frac{12}{(n+3)(n+4)(n+5)},&
\beta_3(n)&=\frac{24}{(n+2)(n+3)(n+4)(n+5)},\\
\beta_4(n)&=\frac{24}{(n+1)(n+2)(n+3)(n+4)(n+5)}.
\end{aligned}
\tag{23}
\]

따라서 β_i는 양수·nonincreasing이고 \(\beta_i(0)=1/5\)다. z=0에서는 \(W_i=\Delta/5\)가 exact rational이다. \(\sum_i\mathsf B_i^4=1\)이므로

\[
\sum_iW_i=\Delta\phi_1(z),\qquad
\phi_1(z)=\begin{cases}(e^z-1)/z,&z\ne0,\\1,&z=0.\end{cases}
\tag{24}
\]

z<0에서는 v=1−u와 \(\mathsf B_i^4(1-v)=\mathsf B_{4-i}^4(v)\)로

\[
W_i(z,\Delta)=e^zW_{4-i}(-z,\Delta).
\tag{25}
\]

음의 z에 alternating power series를 직접 합할 필요 없이 positive moments와 positive reciprocal exponential을 사용한다. d_c의 부호는 유지된다.

## 10. Taylor96 tail와 outward arithmetic

\(0\le x\le16\), \(t_n=x^n/n!\), N=96이라 하자. First omitted term은 n=97이다. n≥97에서

\[
t_{n+1}/t_n=x/(n+1)\le x/98<1
\]

이므로, b_n이 비음수 nonincreasing이면

\[
0\le\sum_{n=97}^{\infty}t_nb_n
\le\frac{t_{97}b_{97}}{1-x/98}.
\tag{26}
\]

b_n=1은 exp, b_n=1/(n+1)은 phi1, b_n=β_i(n)은 각 B4 moment에 적용된다. x=0이면 first omitted term0이고 exact zero tail이다. \(|d_c|(T-t_0)\le16\)과 0<Δ≤T−t0 때문에 모든 local |z|에 이 bound가 적용된다.

Exact rational partial sum S와 tail bound T를 계산한 뒤 \([\downarrow S,\uparrow(S+T)]\)를 사용하면 유효하다. Δ를 포함하는 moment에는 positive factor Δ를 적용한다. 각 term을 먼저 interval로 outward 계산하는 구현도 positive sums/products의 포함성으로 같은 보장을 얻지만, 그 경우 계산한 실제 interval을 그대로 누적해야 한다.

양의 수 x∈[l,u]와 l>0에 대해 reciprocal는 [1/u,1/l]이고 outward conversion으로 포함성을 유지한다. exp(x)의 lower≥1이므로 음의 exponential의 reciprocal에 0 분모가 생기지 않는다. 식(25)은 positive interval product이므로 reversed moment와 exp(z)의 lower끼리, upper끼리 곱한 뒤 outward 처리한다. Q_i≥0와 nonnegative E interval을 식(21)에 사용하면 lower/upper가 각각 해당 exact endpoint를 감싼다. 이 포함성은 모든 base cells에서 induction으로 보존된다.

여기서 식(19)는 whole-R supremum gap의 명시적 bound다. Scalar E에는 Taylor tail와 각 outward arithmetic의 실제 interval을 전달하며 식(19)를 scalar 전체 오차의 상계로 오용하지 않는다. d_c=0의 moment 식은 exact rational이고, 구현이 최종 dyadic conversion을 하더라도 interval은 그 exact value를 포함한다.

## 11. Whole-E upper와 다음 endpoint

Base cell의 certified R supremum upper를 U_R라 하고, restricted \(g_e\) B3 coefficient maximum을 U_e라 하자. Convex hull로 \(g_e\le U_e\)다. \(Q_{\max}=cU_R+U_e\ge0\), incoming valid E upper E_L에서

\[
Y(x)=e^{d_cx}E_L+Q_{\max}\int_0^xe^{d_c(x-v)}dv,
\quad 0\le x\le\Delta
\tag{27}
\]

를 만든다. Positive scalar comparison으로 \(\mathcal E(A+x)\le Y(x)\)다. Derivative는

\[
Y'(x)=e^{d_cx}(d_cE_L+Q_{\max})
\]

이므로 부호가 일정하고

\[
\sup_{0\le x\le\Delta}\mathcal E(A+x)
\le\max\{E_L,Y(\Delta)\}.
\tag{28}
\]

식(28)은 감소하는 majorant의 **왼쪽 값도 포함**한다. 예를 들어 E_L=1,d_c=−16,Qmax=1이면 오른쪽 값만으로 whole cell을 덮을 수 없다. Y(Δ)는 signed exp/phi의 positive outward arithmetic으로 계산한다. Whole-E lower는 incoming/outgoing E lower의 최대를 사용할 수 있다. 이것은 endpoint 값들에 대한 lower이므로 whole supremum의 lower다.

다음 셀에는 식(27)의 더 큰 endpoint 대신 식(21)의 polynomial-forcing endpoint enclosure를 전달한다. Whole-cell certificate와 endpoint connector는 서로 다른 출력이다. Observation whole-cell bounds는 모든 포함 base-cell bounds의 max로 집계한다.

## 12. 독립 original-integral reference와 좌표 인자

원래 source cubic을 \(g_j(s)=\sum_{m=0}^3a_m(s-a_j)^m\)라 쓰자. \(x=t-a_j\), \(\Delta J_\ell=J_\ell(t-a_j)-J_\ell(t-b_j)\)이고

\[
J_\ell(x)=\int_0^{x_+}v^\ell h(v)dv,\qquad x_+=\max(x,0)
\]

라 둔다. n=\(\lfloor x_+/\tau\rfloor\)에서

\[
J_\ell(x)=\sum_{k=0}^{n-1}q^k
\frac{((k+1)\tau)^{\ell+1}-(k\tau)^{\ell+1}}{\ell+1}
+q^n\frac{x_+^{\ell+1}-(n\tau)^{\ell+1}}{\ell+1}.
\tag{29}
\]

v=t−s 치환과 binomial expansion으로

\[
F_j(t)=\sum_{m=0}^3a_m\sum_{\ell=0}^m
\binom m\ell x^{m-\ell}(-1)^\ell\Delta J_\ell.
\tag{30}
\]

q=0,1 또는 exact block boundary에서도 식(29)는 finite sums이며 singular geometric denominator가 없다. Reference는 이 unsplit original-source route로 exact 값을 얻고, 다섯 rational samples에서 degree≤4 power polynomial을 독립적으로 재구성할 수 있다. 오른쪽 sample에는 같은 base-cell initial coefficient를 사용하여 left limit를 맞춘다. Distinct sample 다섯 개의 polynomial uniqueness가 이 재구성을 정당화한다.

\(\phi_k(z)=\sum_{n\ge0}z^n/(n+k)!\)라 두면

\[
\int_0^1e^{z(1-u)}u^mdu=m!\phi_{m+1}(z).
\tag{31}
\]

식(31)은 positive-series/beta 계산으로 z≥0에서 얻고, absolute convergence 또는 아래 primitive로 모든 real z에 확장한다. z≠0의 primitive는

\[
-e^{z(1-u)}\sum_{k=0}^m\frac{m!}{(m-k)!}\frac{u^{m-k}}{z^{k+1}}.
\tag{32}
\]

미분 시 adjacent terms가 telescope하여 integrand가 되고, endpoints 차이는 \(m![e^z-\sum_{k=0}^mz^k/k!]/z^{m+1}\)다. z=0은 별도로 \(1/(m+1)=m!/(m+1)!\)다.

Elapsed physical-time power forcing \(\sum a_mx^m\)의 항은

\[
\int_0^\Delta e^{d_c(\Delta-x)}x^mdx
=m!\Delta^{m+1}\phi_{m+1}(d_c\Delta).
\tag{33}
\]

Normalized-u forcing \(\sum A_mu^m\)의 항은 **\(\Delta m!\phi_{m+1}(z)\)**다. 두 표현의 coefficient가 \(A_m=a_m\Delta^m\)로 연결되기 때문이다. B4에 필요한 orders는 phi1..phi5다.

Reference의 squarefree/Sturm route는 production의 de Casteljau traversal와 별도로 작성하며 production module을 import하지 않는다. Decimal160 부분은 고정 \(10^{-80}\max(1,|reference|,|lower|,|upper|)\) guard의 corroboration으로 분류하고 exact checks 및 strict no-guard misses와 분리한다. 이 구분은 정리의 수동 증명에 영향을 주는 수치 허용오차 변경이 아니다.

## 13. 유한 계약과 거부 조건

현재 contract는 states1..13, source≤16, observation≤32, base≤512, B≤8, input rational components≤256bits, production/saved-derived components≤16384bits, D=96이다. 따라서 source/strip terms를 base마다 한 번 구축하는 사전 상계는

\[
N_{\rm base}N_{\rm source}(B+1)\le512\cdot16\cdot9=73728<100000.
\]

Subdivision 사전 상계는 512·288=147456 splits와 512·577=295424 visits다. 이 counts는 loops 전에 charge하고 실제 counters도 그 안에서 검사한다. Complete binary tree의 leaf 수는 splits+1이므로 leaf 저장에도 별도 무제한 크기가 생기지 않는다.

공개 run_case는 depth96을 고정한다. 같은 단일 캠페인의 두 고정 quartic에 대한 D=0,4,8,16,32,64,96 진단은 일반-D 증명의 적용이다. 두 control의 14 evaluations에 대한 사전 합계는 splits≤1320, visits≤2654다. 현재 canonical CONTROL_PLAN은 21 models/75 base cells/overlap precharge4811과 이14 diagnostics를 계획하며 아직 실행 결과가 아니다.

Derived bit cap을 넘는 계산은 명시적으로 거부한다. Initial bit cap 안의 모든 input이 derived cap이나 CPU/memory 제한을 통과한다는 보장은 여기서 주장하지 않는다. Exact algebraic work count, guarded arithmetic domain, 실제 OS deadline은 서로 다른 보장이다. Reference 내부의 unserialized Euclid/Sturm intermediates만 별도1,048,576bit guard이며 production/saved-derived16384bit와 고정 CPU/wall/memory는 유지한다.

ASCII signed integer 또는 signed p/q grammar, 2048char input limit, whitespace/decimal/exponent/Unicode-digit/boolean/float 거부, nonzero denominator, 유한6000 decimal-digit 변환 정책을 적용한다. 두16384bit components의 canonical rational 문자열은 부호와 separator를 포함해10000char 한도에 들어가며 실제 saved strings도 그 한도를 검사한다. Grammar/hash/premise flags의 검사는 입력 identity를 검증하며 외부 물리 certificate의 진실을 새로 만들어내지 않는다.

Singleton zero-mass contract에서는 R0와 모든 gr coefficients가0이어야 한다. Scalar ge는 남을 수 있다. Negative original B3 coefficient, 잘못된 clock, tau≤0, q∉[0,1], c<0, 음의 initial value, \(|d_c|(T-t_0)>16\), cap adapter와 identity mismatch는 현재 입력 계약의 거부 대상이다.

## 14. Units와 경계 경우

| 항목 | Units 또는 처리 |
|---|---|
| t,τ,Δ | 같은 source clock의 time units |
| K+wH | 제공된 parameter 규약에서 inverse time |
| gr,ge | 각각 R/time, E/time |
| c,d_c | 각각 E/(R·time), inverse time |
| D·S/6, B_i, M_B | R units; M_B는 normalized-u derivative bound |
| Restricted width w | 원래 normalized-u 좌표의 무차원 길이; physical length는 Δw |
| z,β,φ | 무차원 |
| W_i | time units; W_iQ_i는 E units |
| J_ℓ | time^(ℓ+1), 식(30)은 R units |
| q=0/q=1 | finite kernel 정의와 q^0=1; geometric division 없음 |
| D(overlap)=0 | exact zero integral; source interval width 자체는 strict positive |
| derivative all-zero/한 부호 | exact constant/monotone endpoint maximum |
| zero/repeated/boundary roots | zero-dropping variation와 complete leaf partition에 포함 |
| mixed controls이지만 실근 없음 | 함수 enclosure 규칙을 그대로 사용; root 존재를 보고하지 않음 |
| d_c<0/0/>0 | reflection/exact-zero/positive-series branches |
| source value jump | 적분은 endpoint convention에 무관하고 convolution과 E는 연속 |
| shifted t0 | 모든 식이 clock differences에 의존하므로 같은 shift를 적용하면 비교함수도 동일하게 이동 |

## 15. 수동 검산과 현재 검증 상태

다음 값은 위 식을 직접 적분·대입해 확인한 exact controls다. CAS·캠페인 PASS로 집계하지 않는다.

| Control | 수동 결과 |
|---|---|
| gr=s³,q=1,T=1,R0=E0=0,c=1,d_c=0 | R=1/4, E=1/20, B4=(0,0,0,0,1/4) |
| ge=s³,c=0,T=1,E0=0,d_c=0 | E=1/4 |
| gr=s^k,q=1,T=1,k=0..3 | R=1/(k+1), E=1/[(k+1)(k+2)] |
| Q0_INITIAL_JUMP: gr=s³,R0=1,τ=1,T=1 | actual R=1/4, left-limit/sup=5/4, E=21/20 |
| Canonical GLOBAL_MEMORY: q=1/2,τ=1/2,T=5/4,gr=s³ | R=T⁴/4−(T−1/2)⁴/8−(T−1)⁴/16=2337/4096; E=T⁵/20−(T−1/2)⁵/40−(T−1)⁵/80=12013/81920 |
| Moving-window p=−(u−1/4)(u−1/2)(u−3/4),M=1 | R(2)=1, E(2)=1447/960, sup R on[1,2]=1033/1024 |
| Moving-window p=−(u−1/4)((u−1/2)²−1/8),M=1 | R(2)=97/96, E(2)=1447/960 |
| Constant scalar Q=1,E0=1,Δ=1,d_c=±16 | E_right=e^(±16)+(e^(±16)−1)/(±16); whole majorant also includes left value1 |

Moving-window identity는 q=0,τ=1, gr=M on[0,1], gr=M+p(u) on[1,2]에서

\[
R(1+u)=M+\int_0^up(v)dv,
\quad E(2)=3M/2+\int_0^1(1-u)p(u)du
\]

로 직접 따른다. Canonical controls의 original B3 coefficients는 각각 비음수로 주어진다. 다른 패턴·guards와 실제 코드 동작은 고정 primary/reference 캠페인과 R6/R9에서 확인할 항목이다.

## 16. 원전·재사용 결속과 다음 검증

Bernstein restriction, convex hull, product/degree elevation은 classical tools다. 실제 읽은 원전은 Mourrain–Rouillier–Roy, *The Bernstein Basis and Real Root Isolation* (2005), §2 Prop2.3/2.4/2.8 및 Algorithm2.9 ([PDF](https://library.slmath.org/books/Book52/files/24roy.pdf)); Sagraloff, *When Newton meets Descartes*, arXiv1109.6279v1, Theorem2(P4) ([PDF](https://arxiv.org/pdf/1109.6279)); Sharma notes §3 ([PDF](https://www.imsc.res.in/~vikram/poly-2012/descartes.pdf))다. 원전 재사용 범위는 R2에 기록했다. 이번 fixed-degree insertion/deletion 논증, finite count/gap과 WU memory/scalar 연결은 위에서 직접 유도했다. 전역 최초성 또는 strong no-go를 주장하지 않는다.

Full-A comparison, original memory와 scalar majorant의 선행 근거는 보존된 R14 proof 및 R14 scientific payload다. R14 FINAL은 `6ca324dbc5d3c4b5c064f7621730eb0d6ee5eb51`, science payload SHA256은 `b68ab395e4e36ea7a6b49bb6c0b1f44fb75d10522f223d29657907179ac24e4b`다. 이전 결과의 재실행 없이 조건과 새 차수에 필요한 부분을 연결했다.

다음 독립 R6는 이 증명과 실제 C5 코드의 sign·clock·count·tail·edge-case 대응을 확인한다. Frozen CAS batch는 유한 algebraic identities의 외부 corroboration이며 식(15)의 부등식 증명, 전체 구현 또는 physical source closure를 대신하지 않는다. Primary/reference 실제 결과·warnings·failures는 원본 그대로 기록한다.

실제 HD reactive array 및 named consumer/state/density/clock는 `INPUT_PENDING_IN_INSPECTED_SCOPE`, native v `UNSPECIFIED`다. `MISSING_NOT_ZERO`, TIQM/SQM 구별, HH_R10 OFF, production NOT_ISSUED, L4 false, central/physical delta0을 유지한다. Current skill1.0.0 workflow와1.3.0 POLICY_INTEGRATION/THEORY_LOOP/RESEARCH_POLICY/EVIDENCE_AND_HANDOFF의 실제 context는 R5_AUTHORING_STATUS.json에 결속한다.
