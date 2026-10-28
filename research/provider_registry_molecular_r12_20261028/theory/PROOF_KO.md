# R12 정확한 비정렬 forcing convolution과 닫힌 셀 세분화 정리

## 1. 질문과 재사용 경계

R11에서 채택한 전체 생성자와 모든 시작시각의 block certificate를 고정한다. 이 문서는 source cell과 observation cell이 서로 다르고 tau의 정수분할도 아닐 때, 같은 연속시간 비교함수를 정확한 유한 계산으로 표현한다. R11의 K, pi, destruction, w box, 초기 상태, whole-domain forcing 및 q 인증을 다시 계산하지 않는다. 새 물리 closure나 HD reactive data를 가정하지 않는다.

배경 문헌은 interval indicator의 convolution이 piecewise polynomial을 만든다는 표준 사실과 knot에서 양측 극한을 구별하는 convention을 제공한다. 여기서 필요한 geometric step kernel, all-starts 조건, source-bound cap 귀납은 아래에서 직접 증명한다. 근거의 정확한 적용 범위는 authority/literature/LITERATURE.json과 기존 R11 theory/PROOF_KO.md다.

## 2. 전제와 기호

유한 상태의 column-conservative Metzler 생성자
\[
H=\pi d_{\rm dest}^{T}-\operatorname{diag}(d_{\rm dest}),\qquad
A_w(t)=K+w(t)H
\]
에서 K, pi, d_dest는 family 전체에 고정한다. pi는 probability vector이고 d_dest는 비음수다. 인증된 전체 w box의 모든 measurable path에 대해 U_w(t,s)는 양의 column-stochastic propagator다. zero-mass 부분공간에서, 동일 family/state/clock에 대해
\[
\sup_{w}\sup_{s:[s,s+\tau]\subset I}
\|U_w(s+\tau,s)|_{\mathbf1^\perp}\|_1\le q,\qquad
0\le q\le1,\quad \tau>0
\tag{2.1}
\]
를 전제한다. I는 실제 계산구간 [t0,T]를 포함한다. 모든 shorter remainder에 대한 Markov l1 nonexpansiveness도 같은 family에 성립한다. R11의 실제 저장 certificate가 네 사례에서 이 전제를 공급한다. 인증 객체의 문자열만으로 외부 과학 전제가 입증되는 것은 아니므로, saved wrapper는 고정 결과의 실제 bytes/SHA/case를 검사한다.

잔차 r과 scalar error eta는
\[
r'=A_w r+f,\quad \mathbf1^Tr=\mathbf1^Tf=0,\quad
\|f(t)\|_1\le g_r(t),
\]
\[
D^+E(t)\le cR(t)+d_c E(t)+g_e(t),\qquad
R=\|r\|_1,\quad E=|\eta|,\quad c\ge0
\tag{2.2}
\]
를 만족한다. d_c는 signed constant다. g_r,g_e는 source partition
\(t_0=a_0<a_1<\cdots<a_J=T\)에서 비음수 상수이고, fine/coarse 전체 domain에서 유효한 bound다. observation partition
\(t_0=o_0<\cdots<o_N=T\)은 별개의 정확한 rational partition이다. 비교 초기값 R0,E0는 실제 오류의 비음수 상계다. coarse l1 error는 4E다.

c,d_c의 차원은 inverse time, g_r,g_e의 차원은 해당 오류/time이다. tau와 모든 knot는 동일한 source clock이다. 상대 age의 원점은 항상 t0다. (-,+,+,+) convention 및 c_light,hbar,kB의 보존 정책은 유지되며 이 단위에서 별도 시공간/온도 변환을 하지 않는다.

## 3. 모든 age의 propagator bound

\(t-s=m\tau+\theta,\ 0\le\theta<\tau\)라 하자. 연속하는 m개의 full block과 한 remainder로 propagator를 시간순 합성한다. 각 full block의 시작이 s+k tau로 이동하므로 (2.1)의 모든 시작시각 전제가 필요하다. zero-mass 부분공간의 불변성과 induced norm의 submultiplicativity로
\[
\|U_w(t,s)|_{\mathbf1^\perp}\|_1
 \le q^m=:h(t-s),\qquad
h(u)=q^{\lfloor u/\tau\rfloor}.
\tag{3.1}
\]
여기서 h(0)=1이고 q=0일 때도 \(0^0=1\)이다. 따라서 Duhamel formula와 양의 norm bound는
\[
R(t)\le {\cal R}(t):=h(t-t_0)R_0+F(t),\qquad
F(t)=\int_{t_0}^{t}h(t-s)g_r(s)\,ds
\tag{3.2}
\]
를 준다. 현재 새 forcing은 age0에서 계수1로 들어간다. 이전 observation이나 cap 교차 시점에서 age를 재설정하지 않는다.

## 4. Positive-overlap 식과 전체 knot 집합

각 source cell [a_j,a_(j+1)]와 age strip [k tau,(k+1)tau]의 교집합을 s 변수로 쓰면 길이는
\[
\ell_{jk}(t)=
\left[\min(a_{j+1},t-k\tau)
-\max(a_j,t-(k+1)\tau)\right]_+
\tag{4.1}
\]
이다. 끝점의 포함/배제는 적분값을 바꾸지 않는다. 따라서
\[
F(t)=\sum_{j=0}^{J-1}g_{r,j}
 \sum_{k=0}^{B}q^k\ell_{jk}(t),\qquad
B=\left\lfloor\frac{T-t_0}{\tau}\right\rfloor .
\tag{4.2}
\]
k>B이면 t-k tau<t0이므로 모든 overlap은0이다. 각 항이 비음수여서 floating cancellation을 피할 수 있고, 본 구현은 exact Fraction으로 길이와 q^k를 평가한다.

한 box convolution의 slope가 바뀌는 지점은 source 양끝에 k tau 또는 (k+1)tau를 더한 곳뿐이다. 따라서 모든 F kink는
\[
\{a_j+k\tau:0\le j\le J,\ k\ge0\}\cap[t_0,T]
\tag{4.3}
\]
에 포함된다. F 자체는 연속이다. 더 직접적으로 아래 primitive J가 연속이고 F가 그 유한 차이합이므로 확인된다.

계산 event grid는 다음 유한 합집합을 exact rational로 정렬·중복 제거한다.
\[
{\cal B}=\{o_n\}\cup\{a_j\}
 \cup\{t_0+k\tau\}
 \cup\{a_j+k\tau\}
 \cup\{\text{inherited cap knots}\},
\tag{4.4}
\]
각 집합은 [t0,T]와 교차시킨다. t0+k tau는 초기항의 점프를 위해 반드시 필요하며 a0=t0일 때에도 이를 명시적으로 검사한다. Source knots는 g_e의 값 변경도 포함한다. 현재 c,d_c는 sweep 전체 상수다.

### 독립 primitive와 대표 반례

\(x_+=\max(x,0)\), \(n=\lfloor x_+/\tau\rfloor\)에 대해
\[
J(x)=\tau\sum_{k=0}^{n-1}q^k+q^n(x_+-n\tau)
\tag{4.5}
\]
라 두면 J(0)=0이고 \(J'=h\) a.e.다. 각 n tau에서 왼쪽식의 마지막 q^(n-1)tau가 다음 식의 유한합에 들어가므로 J는 연속이다. q=1이면 J=x_+, q=0이면 J=min(x_+,tau). 따라서
\[
F(t)=\sum_j g_{r,j}\{J(t-a_j)-J(t-a_{j+1})\}.
\tag{4.6}
\]
이 식은 reference가 production overlap loop와 독립적으로 사용한다.

예를 들어 q=1/2,tau=1/3, g_r=1 on[0,1/4], 그 밖에는0, t=1/2라 하면
\(F(1/2)=(1/2)(1/6)+(1/12)=1/6\)이다. 같은 source cell의 일부는 age<tau, 일부는 age>tau다. 셀 하나에 단일 index weight를 대입하는 방식은 이 split을 보존하지 못한다. 이 예는 비정렬 source의 구체적 구현 의무를 보여주며 일반적인 불가능성 정리가 아니다.

## 5. 열린 세분 구간의 affine R와 닫힌 셀

연속 event knots b_l<b_(l+1) 사이에는 F의 kink와 h의 jump가 없다. 그러므로
\[
h_l=q^{\lfloor(b_l-t_0)/\tau\rfloor},\quad
L_l=h_lR_0+F(b_l),\quad
V_l=h_lR_0+F(b_{l+1})
\tag{5.1}
\]
로 두면 구간 내부의 raw comparison은
\[
{\cal R}(b_l+u)
=(1-u/\Delta_l)L_l+(u/\Delta_l)V_l,\quad
\Delta_l=b_{l+1}-b_l.
\tag{5.2}
\]
L_l는 왼쪽 knot의 right-continuous 값이고 V_l는 **오른쪽 끝점에 왼쪽에서 접근한 극한**이다. b_(l+1)가 block jump이면 point 값
\(h(b_{l+1}-t_0)R_0+F(b_{l+1})\)은 V_l보다 작을 수 있다. 이 구별은 실제 연속 오류의 jump를 뜻하지 않으며, 사용한 upper comparison의 형태다.

따라서 closed-cell 상계
\[
\overline R_l=\max\{L_l,V_l,{\cal R}(b_{l+1})\}
\tag{5.3}
\]
가 유효하다. Exact ideal에서는 q<=1이므로 마지막 항이 V_l보다 크지 않지만, directed arithmetic의 independent endpoint rounding도 안전하게 포함하기 위해 구현은 명시적 max를 취할 수 있다. Raw lower/upper는 이 ideal comparison을 둘러싼 수치 enclosure이지 실제 물리 오류의 lower/upper 쌍이 아니다. 실제 오류에 대해서 주장하는 것은 upper뿐이다.

## 6. Signed scalar E의 정확한 affine 적분

현재 구간에서 \(x=d_c\Delta\)라 하자. 아래 모든 적분 weight는 d_c의 부호와 무관하게 비음수다.
\[
e=e^x,\quad
W_0=\int_0^\Delta e^{d_c(\Delta-u)}(1-u/\Delta)\,du,\quad
W_1=\int_0^\Delta e^{d_c(\Delta-u)}u/\Delta\,du,\quad
\phi=W_0+W_1.
\tag{6.1}
\]
비교 초기값 \({\cal E}_l\)로부터
\[
{\cal E}_{l+1}
=e{\cal E}_l+c(W_0L_l+W_1V_l)+\phi g_{e,j(l)}
\tag{6.2}
\]
를 얻는다. 이는 (2.2)에 (3.2)를 대입한 global raw ideal scalar comparison의 정확한 integration이다. E는 R comparison의 jump에서도 연속이며, 점에서 다른 forcing 값은 적분을 바꾸지 않는다.

x>=0이면 양의 급수
\[
W_0=\Delta\sum_{k\ge0}\frac{x^k}{k!(k+2)},\qquad
W_1=\Delta\sum_{k\ge0}\frac{x^k}{k!(k+1)(k+2)}
\tag{6.3}
\]
를 사용한다. x<0이면 y=-x>0에 대해 \(W_0(x)=e^xW_1(y)\),
\(W_1(x)=e^xW_0(y)\)다. x=0에서는 두 weight가 Delta/2다. R11에서 이미 증명한 dyadic128/Taylor96 함수를 본문 그대로 재사용한다. 각 positive term의 outward rounding과 degree96 이후 exponential tail bound를 함께 보존하므로 near-zero d에서 닫힌식의 cancellation을 피한다.

Reference의 별도 닫힌식은 x!=0에서
\[
W_0=\Delta\frac{(x-1)e^x+1}{x^2},\qquad
W_1=\Delta\frac{e^x-1-x}{x^2}
\tag{6.4}
\]
이고 Decimal160 및 실행 전 고정 guard1e-80로 corroborate한다. 이것을 rigorous interval reference라고 부르지 않는다. Exact Fraction F/R 검사는 guard를 사용하지 않는다.

### Whole-cell E

구간의 실제 R이 \(\overline R_l\) 이하이고 왼쪽 E의 upper가 z_l이면
\[
Y(u)=e^{d_cu}z_l+
 \phi(d_c,u)\{c\overline R_l+g_e\}
\tag{6.5}
\]
가 그 구간의 E upper다. 미분하면
\(Y'(u)=e^{d_cu}(d_cz_l+c\overline R_l+g_e)\)이므로 부호가 구간 전체에서 고정된다. 따라서
\[
\sup_{0\le u\le\Delta}E(b_l+u)
\le \max\{z_l,Y(\Delta)\}.
\tag{6.6}
\]
Signed damping에도 이 논증이 성립한다. Raw affine endpoint 적분 (6.2)와 whole-cell용 상수 R majorant (6.5)를 구별한다.

## 7. 실제 source-bound cap의 세분화 정리

이전 source가 exact closed cells [z_i,z_(i+1)]에
\((R,E)\le(C^R_i,C^E_i)\)를 인증하고, exact point z_i의 별도 upper P_i를 제공한다고 하자. 그 source의 family/state/clock/initial data와 현재 대상은 같아야 한다. 본 구현의 cap supplier는 고정 R11 actual PRIMARY_RESULTS bytes/case이며 SHA 및 모든 선택 field를 검사한다. 임의 표본이나 metadata label은 cap supplier가 아니다.

(4.4)에 old z_i를 모두 넣었으므로 각 새 subcell [b_l,b_(l+1)]은 하나의 old closed cell에 포함된다. 포함관계는 정확한 rational 부등식으로 확인한다. 그러면
\[
\widehat R_l=\min(\overline R_l,C^R_{i(l)})
\tag{7.1}
\]
는 그 subcell 전체에 유효하다. 새 point가 old knot와 **정확히 같은 rational**일 때만 P_i를 쓰고, 다른 point에는 그 point를 포함하는 old whole-cell upper를 사용한다. Old endpoint를 선형보간해 새 point/whole cap으로 만들지 않는다.

귀납적으로 b_l에서 z_l가 실제 E의 upper라 하자. z_l를 raw E point upper, 해당 old closed-cell E cap 및 사용 가능한 exact old point cap과 교차해도 유효성이 유지된다. \(\widehat R_l\)와 같은 source cell의 g_e를 (6.5)에 넣어 오른쪽 point upper와 whole upper를 만든다. Whole upper는 raw whole E, old whole E 및 scalar whole upper끼리만 교차한다. 오른쪽 point upper는 raw right-point upper, scalar right-point upper, 이미 유효한 해당 whole upper 및 정확히 일치하는 old right-point cap과 교차한다. Old point cap을 whole upper에 사용하지 않는다. 각 교차는 동일한 대상 범위의 upper들 사이에서만 이루어지므로 유효성을 유지한다. 새 오른쪽 point upper가 다음 구간의 귀납 가정을 공급한다. Endpoint는 인접한 양쪽 closed cell에도 속하므로 마지막 output-only intersection 역시 유효하다.

이 귀납은 E의 local scalar majorant만 전파한다. R의 global h(t-t0)R0와 F(t)는 처음 source history 전체에서 계속 계산하며 cap 때문에 재시작하지 않는다.

Observation cell [o_n,o_(n+1)]은 refined closed cells의 gap-free union이다. 따라서 각 component의 observation whole upper는 그 안의 refined whole upper들의 maximum이다. Observation point는 exact event knot를 직접 선택한다. 경계 양측이 닫힌 구간이라 모든 endpoint가 포함된다. 순서·누락·overlap의 잘못된 coverage나 다른 clock/source/case는 입력 오류로 거절한다.

## 8. 표현 세분화, 오차 및 안정성

Source의 constant forcing을 동일 값의 작은 cell로 나누거나 같은 구간의 source cells를 합치는 것은 (3.2)의 동일 함수를 표현한다. 추가 observation knots로 (6.2)를 나눠 적분해도 exponential semigroup와 적분의 가법성에 의해 같은 raw ideal F/R/E를 준다. 이는 exact analytic equality이며 rounded output의 bit equality를 요구하지 않는다.

**Capped E 값 자체에는 refinement invariance를 주장하지 않는다.** (7.1)의 local Rwhole 및 (6.5)의 constant majorant가 세분화에 따라 줄 수 있으므로 더 작은 유효 upper가 나올 수 있다. Capped 검증 대상은 안전성·source inclusion·old cap 대비 no-worse이며 수치값 불변이 아니다. Raw 및 capped의 보편적 우위나 모든 grid에서 단조인 roundoff width도 주장하지 않는다.

Source forcing bounds를 전제로 이 계산에는 grid quadrature/forcing interpolation error가 없다. q 자체는 R11에서 outward 채택한 rational upper이고, 추가로 표시된 enclosure 폭은 finite exponential series와 directed arithmetic에 따른 것이다. Observation grid refinement는 새로운 ODE solve가 아니다. 비교식과 실제 fine/coarse dynamics 사이의 차이는 기존 whole-domain certificate에 남으며 물리 closure를 새로 만들지 않는다.

## 9. 유한 구현 영역과 증거

CONTRACT의 입력 limits는 states1..13, source/observation/old cap cells1..192,
refined cells<=2048, full blocks<=8, overlap terms<=200000, exact input scalar<=1024bits,
|d_c|(T-t0)<=16다. 범위 밖 입력이나 bool/float clock은 명시적으로 거절한다. 이 제한은 새 코드의 유한 지원 영역이며 수학 정리의 일반성 제한이나 전역 no-go가 아니다.

생산 구현은 positive overlap, 독립 reference는 exact primitive J와 별도 Decimal closed forms를 사용한다. 고정 controls는 q0/q1, fresh forcing, source-shift knots, block left-limit, signed/nearzero d, shifted clock, observation refinement와 singleton zero-mass limit를 구별한다. 네 저장 사례의 aligned grid는 새 알고리즘의 R11 저장 결과 호환성을 확인하고, nonaligned grid는 새 기능을 검사한다. 이전 runner, CAS, ODE, native source exponential은 호출하지 않는다.

이 문서의 정리는 직접 유도한 조건부 방법 결과다. 정식 과학 채택은 별도 한 번의 독립 R6/C9 검토와 실제 유한 primary/reference/CAS 증거가 갖춰진 뒤 두 새 DAG 노드에만 적용한다. 실제 HD array/named physical consumer/density/clock는 INPUT_PENDING, HH_R10=OFF, production=NOT_ISSUED, L4=false, central/physical delta0을 유지한다.
