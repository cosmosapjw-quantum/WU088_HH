# R14 주장·전제·양화

## 결론의 대상

전체 인증 full-A family의 모든 시작시각에서 주어진 block certificate \((q,\tau)\)와 whole fine/coarse-domain forcing bound functions를 전제로 한다. 이 단위는 그 입력의 물리적 유효성을 새로 발급하지 않는다. 명제는 모든 rational source/observation partition, 모든 admissible pointwise-nonnegative piecewise quadratic \(g_r,g_e\), \(R_0,E_0\ge0\), 고정 \(c\ge0,d_c\in\mathbb R\)에 대한 ideal comparison의 유한 구성이다.

\[
R(t)=h(t-t_0)R_0+\int_{t_0}^{t}h(t-s)g_r(s)\,ds,\quad
E(t)=e^{d_c(t-t_0)}E_0+\int_{t_0}^{t}e^{d_c(t-s)}(cR(s)+g_e(s))\,ds.
\]

\(h(a)=q^{\lfloor a/\tau\rfloor},h(0)=1\). \(q=0\) 산술 control에서도 \(0^0=1\) convention을 사용한다. \(H=\pi d^T-\mathrm{diag}(d), A=K+wH\)와 fixed K/pi/destruction, full w box, zero-mass residual을 보존한다. Nominal K certificate를 full A로 옮기지 않는다. \(E=|\eta|\), coarse l1=4E이다.

## 증명과 구현이 각각 확보할 결과

1. Exact endpoint/convex-vertex minimum 검사는 quadratic의 interval 비음수성에 필요충분하다. 이 결과와 실제 forcing의 whole-domain bound라는 별도 source premise를 구별한다.
2. 두 source vertices의 union을 사용한 exact restriction은 원래 forcing function·source/state/clock을 유지하면서 원래 셀당 최대3개의 positive-coefficient pieces를 만든다.
3. Translated event grid에서 global convolution은 비음수 B3 coefficients를 갖는 cubic으로 구성된다. Endpoint drawing이나 sample integration으로 이 성질을 대신하지 않는다.
4. Cubic critical roots는 exact rational points 또는 normalized width≤2^-96의 rational brackets로 보존한다. 저장된 cubic에서 whole-R supremum enclosure를 얻고 exact gap≤M_B·2^-96≤3Cmax·2^-96을 증명한다. Irrational root를 exact rational point로 표시하지 않는다.
5. Positive beta moments와 negative-argument reversal로 signed scalar endpoint enclosure를 얻는다. Whole-E는 별도의 constant-forcing majorant로 인증한다. E 전달은 rational base grid에서만 이루어진다.
6. Independent reference는 J0/J1/J2 및 monomial phi1..phi4 경로를 사용한다. Decimal160 guard 검증은 analytic proof·exact rational checks와 역할이 다르다.

## 경계·정칙성·표현

Forcing은 유한 piecewise polynomial이며 cell 경계의 one-sided 값이 달라도 된다. 경계 한 점의 적분 기여는 0이다. R convolution 부분 F는 연속이고 initial term은 kernel block 경계에서 하향 jump할 수 있다. Whole-cell 값은 maximum이 존재하는 경우와 미도달 left-limit supremum을 모두 다룬다. Actual right endpoint와 right left limit은 별도 field다.

Raw lower는 chosen-rational-q ideal comparison의 lower이다. 물리 error의 lower 또는 오차 보편 감소율이 아니다. Original forcing hash는 원래 source triplets와 state/clock에 결속하고, 내부 source split은 같은 함수의 exact equivalent representation으로 기록한다.

## 유한 code domain

수학 구성과 유한 실행 계약의 경계를 구별한다. Code는 states1..13, original source cells≤16, observations≤32, effective source cells≤48, base cells≤512, full blocks≤8, input rational bits≤256, derived bits≤16384, |d_c|horizon≤16, dyadic128/Taylor96를 받는다. R13의 더 큰 affine source-cell count까지 포함하는 API superset이라고 주장하지 않는다. 초과 입력을 reject하는 유한 guard는 일반 수학적 불가능성 정리가 아니다.

## 채택 제한

새 strong no-go는 제안하지 않는다. Cubic monotonicity만으로 coefficient positivity를 옮길 수 없다는 명시 counterexample은 그 한 중간추론만 판별한다. Classical Bernstein 도구의 문헌 전체 신규성을 주장하지 않는다. 실제 HD array와 named physical consumer/density/clock은 검사한 범위에서 INPUT_PENDING이며 central/physical delta0, HH_R10 OFF, production NOT_ISSUED, L4 false를 유지한다.

### 실행 전 finite parser/serialization 보완

R14-F02/F03에 따라 문자열 입력은 ASCII signed integer 또는 signed p/q, 최대2048자로 명시한다. Decimal point/exponent/whitespace 입력은 받지 않는다. 입력256bit, derived16384bit는 유지한다. 전용 실행의 integer-decimal digit limit는 유한6000이며, derived numerator/denominator의최대4933자리와savedrational최대10000자에대응한다. 과학값이나허용오차는변경하지않는다. 교정전계약과source는revisions에보존한다.
