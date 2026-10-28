# R14 수치 설계와 실제 계산 순서

1. Exact rational 입력과 original source binding을 검사한다. Whole quadratic 비음수성을 endpoint 및 필요한 interior minimum에서 검사한다. 각 source의 g_r/g_e vertex union으로 effective source를 구성한다.
2. Effective source knots의 kτ translations와 observation knots를 exact union한다. 필요한 모든 initial jumps가 포함된다. Base/effective/block counts를 사용해 overlap과 root work를 실제 구축 전에 precharge한다.
3. Base cell마다 source/age-strip overlap을 한 번만 조립한다. D=U−L의 B1 coefficients와 g(L)+4g((L+U)/2)+g(U)의 B2 coefficients를 positive Bernstein product로 곱한다. 모든 endpoint·rootbox·plot용 계수는 저장된 이 polynomial을 사용한다.
4. Derivative degree에 따라 constant/linear/quadratic을 분기한다. Quadratic derivative는 rational vertex에서 monotone branch로 나누고 exact roots를 deduplicate한다. Strict sign-changing branch에는 최대96회의 exact bisection을 적용한다. Critical roots는 E clock으로 삽입하지 않는다.
5. Rootbox의 cubic restriction hull과 midpoint witness, endpoint와 left limit으로 exact R supremum bracket을 만든다. Dyadic outward rounding은 각 끝에서 최대2^-128을 더한다. Exact gap bound와 rounded gap을 별도로 출력한다.
6. g_e를 B3로 degree-elevate하고 cR을 더한다. Positive B3 beta moment를 dyadic128/Taylor96으로 감싸 E endpoint를 전달한다. Negative d는 e^zW_(3-i)(−z) 항등식을 적용한다. 작은 z에 subtractive phi를 쓰지 않는다.
7. 다음 셀에는 polynomial endpoint upper를 전달한다. Whole E는 각 셀의 R supremum upper와 g_e hull에 대한 constant-forcing majorant를 별도로 계산한다. Observation cell의 whole bound는 포함 base-cell bounds의 max로 합친다.

## Directed positive series의 오차 계약

S=2^128, x=|d_c|Δ∈[0,16], x_lo=floor(Sx)/S, x_hi=ceil(Sx)/S로 둔다. Integer term bounds T_0^lo=T_0^hi=S에서

\[
T_{n+1}^{lo}=\left\lfloor T_n^{lo}X_{lo}/(S(n+1))\right\rfloor,\quad
T_{n+1}^{hi}=\left\lceil T_n^{hi}X_{hi}/(S(n+1))\right\rceil
\]

를 사용하면 induction으로 실제 x^n/n!를 감싼다. Positive beta_i(n)를 곱할 때도 각 항을 directed rounding한다. n=0..96 부분합에 양의 나머지 upper

\[
\frac{x_{hi}^{97}}{97!}\frac1{1-x_{hi}/98}
\]

를 더하면 exp와 beta_i≤1인 각 moment의 전체 series를 감싼다. β_i(0)=1/4이다. Duration 곱, reciprocal exp, positive interval products와 sums는 outward rounding을 사용한다. 새 module은 derived16384 guard를 일관되게 적용하며 이전 helper를 import하여 다른 bit bound를 숨겨 적용하지 않는다.

## 독립 경로

Reference는 J0/J1/J2 primitives와 독립 power polynomial 구성, analytic derivative-root formulas, monomial exponential moments를 사용한다. Decimal160, relative guard1e-80·max(1,|reference|,|lower|,|upper|)는 실행 전에 고정한다. 이것은 rounding의 수학적 증명을 Decimal 비교로 대체하지 않는다. d=0에서는 exact rational moment와 control을 사용한다. 실제 reference의 small-z policy와 series cap은 freeze manifest에 기록한다.

## 비용과 비교

Source preprocessing은 original cell당 최대3조각이다. Full overlap charge는 Nbase·Neffective·(B+1)≤221184, root bisection charge≤98304다. Endpoint 또는 그림에서 overlap을 다시 계산하지 않는다. Source refinement는 ideal 함수의 동일성을 보존하지만 directed rounding의 bitwise identity를 자동 주장하지 않는다. Pointwise 더 작은 유효 forcing을 입력하면 positive kernels로 ideal comparison은 작거나 같다. Strict 개선율은 별도 synthetic controls의 값으로만 보고한다.

## 문자열 자원과 직렬화

문자열 문법과 길이는 Fraction 변환 전에 검사한다. Exact 입력값의bit검사는이후별도수행한다. Python integer-decimal conversion은무제한해제없이6000digits로고정하여16,384-bit경계의직렬화·재파싱을지원한다. 허용값경계의roundtrip과 lexical거부는동결primary캠페인의구체적인검증대상이다. Savedreference parser는입력256bit문자열과derived출력16384bit문자열의길이계약을구별한다.
