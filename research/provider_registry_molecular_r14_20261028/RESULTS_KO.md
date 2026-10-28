# R14 과학 결과 — 비정렬 이차 forcing, positive cubic memory, 유리수 극값 인증

## 1. 확보한 결과

R14는 R13의 비정렬 affine forcing을 **셀 전체에서 비음수인 piecewise quadratic forcing**으로 확장했다. 원래 quadratic Bernstein middle coefficient가 음수여도 exact minimum 검사를 통과하면 받는다. 원래 source의 꼭짓점에서 정확히 나눈 뒤 positive Simpson/Bernstein product로 global residual convolution의 cubic coefficients를 구성한다. Cubic의 critical roots는 exact rational points 또는 유리수 격리 구간으로 저장하고, whole-cell supremum의 명시적 간격을 인증한다. Scalar E는 rational base clock에서 signed positive B3 exponential moments로 전달한다.

이 결과는 주어진 full-A block certificate와 whole fine/coarse-domain forcing bounds에 대한 **조건부 comparison 구성**이다. 새 실제 HD reactive array, named physical consumer/state/density/clock을 발급한 결과가 아니다. 최신 조사에서 실제 읽은 원문 범위의 입력 상태는 INPUT_PENDING이고, HH_R10=OFF, production=NOT_ISSUED, L4=false, central/physical delta=0이다. 독립 심사와 최종 채택 상태는 reviews/C9_FINAL_REVIEW.json 및 SCIENTIFIC_ADMISSION.json의 실제 기록을 따른다.

### 실제 실행 결과

| 항목 | 실제 결과 |
|---|---|
| Primary | **621/621 PASS**, valid31/31, guards46/46, 실패0 |
| 독립 reference | **691/691 PASS**, component comparisons **51,547**, 실패0 |
| 비교 구성 | metadata11,296 / exact27,094 / coverage8,026 / Decimal5,131 |
| 실행 횟수 | primary1 / reference1 / 새CAS1 / 새ODE0 |
| Primary 전체 OS process CPU | 3.224500초 |
| Reference 전체 OS process CPU | 1.195646초 |
| 두 과학 process CPU 합계 | **4.420146초**, import·serialization 포함 |
| 동결 실행 의존 파일 | **20개**, 실행 전 SHA-256 고정 |
| 실제 CAS | **32개 zero residual**, 이번 반환 warning0 |
| 정밀도·사전 guard | production dyadic128/Taylor96, root bisections96, independent Decimal160, 사전 고정 relative1e-80 |
| Guard 없는 strict Decimal containment | **false**, 83건; 예시50개 보존 |
| 남은 R14 primary/reference/CAS | **0/0/0** |

Reference의 PASS는 고정된 relative guard 아래의 고정밀 수치 대조이다. Decimal 계산을 interval reference로 표시하지 않는다. 83건의 strict comparison 차이를 숨기거나 tolerance를 사후 조정하지 않았다. Exact rational 검증과 수동 directed-rounding 증명은 별도 근거다. 이 Decimal 지표는 R10/R11의 물리 sample readout과 다른 값이다.

## 2. 입력 전제와 양화

고정 column-conservative Metzler K, 고정 pi와 destruction d에 대해

\[
H=\pi d^T-\operatorname{diag}(d),\qquad A_w=K+wH
\]

를 유지한다. 전체 인증 w box와 모든 시작시각에서 zero-mass l1 propagator가 길이 tau마다 q 이하이고 짧은 나머지는 nonexpansive라는 full-A 전제를 사용한다. Nominal K rho를 full A에 직접 이식하지 않는다. R11의 q_add와 q_minor derivation 및 고정 source family는 기존 근거로 보존하며 이번에 다시 실행하지 않았다.

\[
h(a)=q^{\lfloor a/\tau\rfloor},\quad h(0)=1,
\qquad 0\le q\le1,\quad\tau>0.
\]

q=0 control에서도 h(0)=1이다. R forcing memory는 원래 t0에서 시작하여 모든 source·observation·kernel 경계를 지나 보존한다.

\[
\mathcal R(t)=h(t-t_0)R_0+\int_{t_0}^t h(t-s)g_r(s)\,ds,
\]
\[
\mathcal E(t)=e^{d_c(t-t_0)}E_0+
\int_{t_0}^t e^{d_c(t-s)}[c\mathcal R(s)+g_e(s)]\,ds.
\]

R0,E0≥0, c≥0와 signed d_c는 horizon 전체에서 고정한다. E=abs(eta), coarse l1=4E이다. Raw lower는 chosen-rational-q ideal comparison의 lower이며 실제 물리 error의 lower가 아니다. Case의 full-A/whole-forcing 선언과 source SHA 검증은 선언된 입력의 결속이다. 선언만으로 실제 물리 전제가 검증되었다고 하지 않는다.

Forcing은 source cell별 quadratic polynomial이다. 셀 경계에서 one-sided source 값이 달라도 되고, observation은 nonaligned rational times여도 된다. 실제 nonlinear forcing을 이 polynomial이 whole domain에서 지배한다는 source premise는 별도로 필요하다. 세 개 sample을 통과했다는 사실로 그 premise를 만들지 않는다.

## 3. Full nonnegative quadratic cone

원래 source cell의 normalized coordinate u∈[0,1]에서

\[
g(u)=b_0(1-u)^2+2b_1u(1-u)+b_2u^2
\]

로 입력한다. b1은 음수여도 된다. Power coefficients를 A=b0−2b1+b2, B=2(b1−b0), C=b0로 두면 endpoints C와 A+B+C, 그리고 A>0이며 interior vertex v=−B/(2A)가 있을 때 g(v)를 exact 비교하면 비음수성에 필요충분한 검사가 된다.

그다음 gr/ge의 모든 strict-interior vertices를 union하여 나눈다. Concave maximum vertex도 포함한다. 두 quadratic은 각 effective piece에서 monotone이므로 restricted B2 coefficients가 모두 비음수가 된다. 원래 셀당 vertex가 최대 둘이어서 effective source cells는 최대3배이다. Original whole-forcing SHA는 원래 source triplets/state/clock에 그대로 결속하고 내부 split을 같은 함수의 exact equivalent representation으로 기록한다.

단순한 cubic monotonicity로 positive B3를 추론할 수는 없다. 예를 들어

\[
P(x)=x^3/3-x^2/4+x/16=\int_0^x(s-1/4)^2ds
\]

는 비음수·비감소이지만 B3 coefficients는 (0,1/48,−1/24,7/48)이다. R14는 이 특정 중간추론의 반례를 보존하고, 실제 overlap 적분에서 positive coefficients를 직접 구성한다. 이 사례를 broad strong no-go로 채택하지 않았다.

## 4. Global positive cubic convolution

Effective source knots의 k*tau translations와 observation knots를 합친 exact base grid를 만든다. 이 grid에는 initial block jumps도 들어간다. Base cell interior에서 source interval [a,b]와 age strip k의 overlap은

\[
L(t)=\max(a,t-(k+1)\tau),\quad U(t)=\min(b,t-k\tau)
\]

이며 max/min branch가 고정된다. D=U−L과 M=(L+U)/2는 affine이고 D≥0이다. 입력으로 결속된 quadratic에 대해 Simpson identity가 정확하므로

\[
I(t)=\frac{D(t)}6\{g_r(L(t))+4g_r(M(t))+g_r(U(t))\}
\]

를 사용한다. 이는 unknown forcing을 sample quadrature로 근사하는 식이 아니다. D의 positive B1과 bracket의 positive B2를 곱하면 positive B3가 나온다. 각각 q^k를 곱하여 합하고 initial constant를 더한다.

각 base cell의 coefficient는 **한 번만** 구축한다. Endpoint F/R, actual right endpoint, right left limit, critical roots, whole-cell bounds, display가 모두 저장된 coefficient를 재사용한다. 별도 endpoint query에서 overlap을 다시 합산하지 않는다.

F convolution은 연속이고 initial hR0만 block 경계에서 downward jump할 수 있다. 따라서 actual R(T)와 T에 접근하는 left limit을 구분한다. Closed-cell upper는 미도달 left-limit supremum도 포함한다.

## 5. Irrational critical points의 유한 인증

Stored cubic P의 normalized derivative는 quadratic이다. Constant·linear·quadratic reduction, endpoint roots, double root를 exact branch로 처리한다. Quadratic derivative를 rational vertex에서 monotone branches로 나누고 opposite signs가 있는 branch만 bisection한다. Distinct interior roots는 최대 둘이다. 각 unresolved root에 96회의 exact midpoint bisection을 적용하면 normalized width≤2^-96이다. Exact rational root를 만나면 조기 종료한다.

Critical roots는 E의 propagation clock으로 삽입하지 않는다. Rootbox에서 cubic coefficients를 de Casteljau로 restriction하여 hull upper와 midpoint lower를 얻는다. Endpoint와 exact critical candidates까지 합치면

\[
L\le\sup P\le U,\qquad
0\le U-L\le M_B2^{-96}\le3C_{\max}2^{-96},
\]

\[
M_B=3\max_i|B_{i+1}-B_i|,\qquad C_{\max}=\max_iB_i.
\]

Restriction derivative의 chain factor w가 이 gap bound의 핵심이다. Dyadic outward endpoints의 추가 간격은 최대2*2^-128이다. Irrational supremum 자체를 exact rational이라고 표시하지 않는다.

31개 실행의 저장 결과에는 base cells 총334개, unresolved critical rootboxes 총23개가 있다. One-irrational control의 최대 exact gap은 약1.0958015047080374e-59이고, two-irrational control은 약1.3697518808850467e-60이다. 두 사례의 최대 outward dyadic whole-R width는 각각2^-128이다. 이들은 해당 저장 사례의 관측값이며 일반 bound를 그 값으로 좁히지 않는다. 모든 셀의 exact gap은 고정된 일반식으로 검증됐다.

## 6. Signed scalar E와 whole-cell 인증

Restricted ge를 B3로 degree-elevate하고 cR을 더해 Q_i≥0을 얻는다. z=d_c*Delta에서

\[
W_i(z,\Delta)=\Delta\int_0^1e^{z(1-u)}\binom3i u^i(1-u)^{3-i}\,du
\]

를 사용하여 E_next=e^z E_left+sum W_i Q_i를 전달한다. Positive z에서는 beta coefficients

\[
\beta_0(n)=\frac1{n+4},\quad
\beta_1(n)=\frac3{(n+3)(n+4)},
\]
\[
\beta_2(n)=\frac6{(n+2)(n+3)(n+4)},\quad
\beta_3(n)=\frac6{(n+1)(n+2)(n+3)(n+4)}
\]

의 양의 Taylor series를 dyadic128로 directed rounding한다. Degree96 뒤의 exponential tail은 |z|≤16에서 geometric upper로 제한한다. Negative z에는 W_i(z)=e^z W_(3−i)(−z)를 적용한다. d=0이면 모든 W_i=Delta/4이다. Production은 작은 z에서 subtractive phi를 사용하지 않는다.

Whole E에는 별도 constant-forcing majorant를 사용한다. Qmax=c*Rsup_upper+ge_upper에서 Y'=d_cY+Qmax, Y(0)=E_left_upper로 두면 Y'의 sign은 일정하여 max(Y(0),Y(Delta))가 whole-cell upper다. 다음 셀에는 polynomial endpoint bound를 전달한다. Observation cell은 포함 base cells의 upper를 max로 합친다.

독립 reference는 원래 unsplit source의 J0/J1/J2 primitives, 네 exact 값의 power cubic interpolation, analytic rational/surd derivative roots, signed monomial phi1..phi4를 사용한다. Production import와 root bisection replay는 없다. Classical Bernstein 및 exponential-integration 도구의 사용 범위와 primary-source 읽기 범위는 authority/literature/LITERATURE.json에 명시했다.

## 7. 판별 controls

다음 값은 고정된 arithmetic controls이다. 별도 표시가 없으면 R0=E0=0,c=1,d_c=0이다.

| Control | Exact 결과 |
|---|---|
| q=1, gr=s², T=1 | R=1/3, E=1/12 |
| q=1, gr=s, T=1 | R=1/2, E=1/6 |
| q=1, gr=1, T=1 | R=1, E=1/2 |
| gr=(s−1/4)², negative B2 middle | R(1)=7/48, E(1)=1/32, source split1/4 |
| gr/ge vertices1/4,3/4 | effective pieces3, E(1)=17/96 |
| One irrational maximum | sup R=1/3+sqrt(2)/6, E(2)=7/12 |
| Two critical roots in one base cell | roots=(1±1/sqrt(2))/2, sup R=(95+sqrt(2))/48, E(2)=45/16 |
| Golden discriminant control | sup R=(5sqrt(5)−3)/12, E(2)=2/3 |
| Double critical root | root1/2 multiplicity2, R(2)=25/12, E(2)=23/8 |
| Endpoint critical roots | roots0,1, R(2)=13/6, E(2)=35/12 |
| Initial q=0 jump, gr=s²,R0=1,T=1 | actual R(1)=1/3, left-limit sup4/3, E(1)=13/12 |
| Global memory q=1/2,T=5/4,gr=s² | R=83/128, E=1249/6144 |

첫 세 controls에서 s²≤s≤1이므로 같은 valid whole-source ordering을 전제로 quadratic ideal endpoint는 constant case보다 R에서2/3, E에서5/6 작다. Affine s case와 비교하면 R에서1/3, E에서1/2 작다. 이는 이 synthetic conditional controls의 exact comparison ratios이며 보편적 raw 우위, R11 capped 개선률, 실제 물리 정확도 또는 speedup이 아니다. Zero control의0/0 비율은 null이다.

## 8. 실제 유한 자원과 교정

Finite domain은 states1..13, original source≤16, observations≤32, effective≤48, base≤512, fullblocks≤8, input256bits, derived16384bits, |d_c|horizon≤16이다. 입력 문자열은 최대2048자의 ASCII signed integer 또는 signed p/q만 받는다. Decimal/exponent/whitespace 문자열은 입력으로 받지 않는다. Original forcing hash는 canonical exact values와 source/state/clock에 결속한다.

이 domain에서 base cells≤473이라는 수동 upper를 얻었으며 implementation guard512는 보수적이다. Full overlap charge≤512*48*9=221184<250000, root bisections≤98304이다. 실제 largest fixture는 original16/observations32/effective48/tau2/17/fullblocks8, base248, overlap combinations107136, geometric nonempty8916, actual root bisections1536/precharge47616을 기록했다. 이 실제 count와 직접 work-helper의512-cell 경계 검사를 섞지 않는다.

독립 preflight는 수학18의무와 code14의무를 수동 검토하고 다음 세 항목을 실행 전에 고쳤다.

- F01: reference가 primary의 실제 PASS_SCOPED 상태를 기대하도록 한 줄 교정.
- F02: bit 검사 전에 exponent text가 확장되지 않도록 변환 전 문법 검사. 기존43 guards에 lexical3개를 추가해46개.
- F03:16,384-bit numerator/denominator는최대4933digits이므로전용runtime의유한digitlimit6000을설정. 실제9867-character경계serialization/parse roundtrip을primary단일campaign안에서확인.

각 교정 전 source와 author records의 실제 원본 bytes를 보존했다. Production D01은 이보다 이른 counter 의미 조율이며 그 이전 snapshot은 기록된 patch로 재구성한 것으로 표시했다. contemporaneous original이라고 하지 않는다. 과학 campaign의 실제 실패는0이며 preflight 발견을 실행 실패로 바꾸어 세지 않는다.

## 9. CAS·그림·재사용의 경계

새 CAS는 beta16개와 Simpson/product/elevation/derivative/restriction/chain factor6개, sign reversal4개, controls6개 등32 identities에서 모두 exact0을 반환했다. Actual submitted code3,551bytes는 동결 script와 byte-identical이며 추가 LF는0이다. 반환 경고는0이지만 R11/R13 경고 원인 NOT_ESTABLISHED를 고치지 않는다. 이번 CAS는 finite corroboration이고 전체 코드 실행 검증이나 physical closure가 아니다.

그림은 saved outputs만 사용한다. Endpoint를 잇는 선과 저장 cubic의 표시, whole-cell certificate, 실제 endpoint와 left limit, 화면에서 보이지 않을 만큼 좁은 rootbox를 구별한다. Renderer와 PNG/SVG 및 actual visual review는 figures/의 기록으로 결속한다. 추가 scientific/ODE run은 없다.

R13은311/125/8408/CPU1.334749/frozen14, R12는531/317/133502/CPU4.202434/frozen30, R11은214/900/19195/CPU1.477435/frozen18의 기존 근거를 그대로 유지한다. R10 primary175/reference469/components9860/CPU0.511886/frozen14, R8 original726/727+1FAIL과별도phi24/24도변경하지않는다. R10원래sample4.0013206434938575e-12, R11sample4.001332174731647…e-12/tolerance4.377656370786352e-11/strictfalse349는이번Decimal83과별개다. Historical first failures, DOC01/META02, R11F01/F02·PNGunknown·S08temporary/S09deletion, R13F01/F02/F03도원기록으로보존한다.

이전 완료 과학·ODE·독립 심사를 통상 재개 절차로 반복하지 않았다. R14와 이전 remaining은 각 unit별로 기록하고 global remaining/full historical CPU는 null을 유지한다. 현재 source/payload/admission/delivery의 최종 정확한 identity는 해당 manifest와 closeout에 연결한다.
