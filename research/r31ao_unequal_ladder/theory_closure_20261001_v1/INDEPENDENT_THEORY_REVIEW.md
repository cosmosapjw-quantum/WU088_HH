# T1·T2·T4·T5 독립 이론 검토

판정은 **명시된 전제 아래 조건부 수용**이다. 최종 작성 중 추가된 T5.5의
유한 정확도 배분에서 누락 1건을 발견했고, 저자의 수정 후 이를 확인했다.
미해결 수학 finding은 없다. 이는 실제 HH 입력, 구현된
callback, FLINT binary, 역사적 ABI 또는 최종 과학 판정을 승인한다는 뜻이 아니다.
`independent_review_admitted=false`, 실제 `rigorous=false`,
`certified_epsilon=null`, `certified_eta=null`을 유지한다.

검토자는 `/root/review_gram`이다. T1/T2/T4/T5 본문 전체를 읽고, 아래 유도와
경계 사례를 직접 점검했다. T3는 별도 검토자 범위다. 이전에 채택된 source
functional identity·radial continuation·Hermite density 식은 이번 증명의
전제로 사용했으며, 그것을 다시 증명하거나 이전 코드를 재감사하지 않았다.
저자 문서는 수정하지 않았다. 실제 HH 계산, native 실행, 추가 합성 suite 실행은
모두 0회다. 여기서의 판단 근거는 수학적 논증이며 sampling PASS가 아니다.

## T1 — 복소 domain, branch, explicit majorant

`Re A≥alpha>0`, `|A|²≤Q_A`에서 `Re(1/A)≥alpha/Q_A`가 따라온다.
B에도 적용하면 sigma의 양의 실수부 하한과 modulus 상·하한을 얻는다.
따라서 A/B/sigma의 principal logarithm과 실수 지수의 거듭제곱은 해당 compact
product의 열린 근방에서 branch를 고정할 수 있다. Bilinear source scalar
`s=sum(delta_j²)`의 정의를 바꾸지 않으면서
`|s|≤sum|delta_j|²≤(H1+H2)²`로 상계하는 논리도 타당하다.

Density의 t/u cut 조건을 A/B의 Gaussian 조건과 분리한 것이 필요하다.
예를 들어 `a=1,t=-1/2`에서는 `Re A>0`이지만 principal t power의 cut에 놓인다.
T1은 이를 별도 조건으로 제외한다. Cut에서 떨어진 rectangle에 대한
`tau_T`와 `exp(lambda max(0,-x_-)/tau_T²)` bound는 부호를 포함해 유효하다.

Sigma image에 대한 독립적인 enclosing rectangle과 기존 outward enclosure의
교집합은 같은 정확한 image를 포함한다. 따라서 교집합 자체는 유효한 enclosure
축소다. 이는 원래 branch-crossing ball에 branch-sensitive 연산을 적용하는
허가가 아니다. T1은 교집합의 outward 재표현 후 양의 margin을 다시 확인하도록
요구하므로 그 논리적 경계를 지킨다. Empty intersection도 올바르게 실패로
분류한다.

Spatial majorant는 실수 r-domain에서 real-part Gaussian만 완전제곱한다.
따라서 `|r1-r2|^k`에 대한 부적절한 complex contour translation이 없다.
`kappa_a`의 endpoint maximum, `Z_a`의 가능한 증폭, Jacobian,
G1의 pz derivative 상수항을 모두 포함한다. 선호하는 양의 half-plane에서는
`D1+X/sqrt(a)`가 `|r1|`와 `|r1-d1|`을 동시에 상계하므로 단순화한
`R=L1+L2`도 유효하다. Completed-square 표현의 일부 phase에 modulus 1을
잘못 적용하지 않고 원래 real-domain phase에서만 사용하는 점도 적절하다.

마지막으로 통합된 bound만으로 holomorphy를 추론하지 않는다. 고정된 decaying
Gaussian과 polynomial의 pointwise domination을 따로 제시하고, t/u derivative가
공간 다항식만 추가함을 사용한다. 이로부터 joint holomorphy와 Cauchy bound가
따라온다. Real rectangle 중심의 radius delta에는 `M/delta`를 쓰고,
half-width tube에서는 `2M/delta`를 쓰는 구분도 맞다. Complexified center/q에
동일한 unit-phase proof를 확장한다는 주장은 수용 범위에 포함되지 않는다.

## T2 — full-box nesting과 midpoint fallback

Inner numerical map이 analytic일 필요는 없고, 모든 호출이 동일한 exact
holomorphic H의 전체 box image를 포함해야 한다는 구분이 옳다. Adaptive
partition이 호출마다 달라도 각 finite partition이 경로를 완전히 덮고
panel enclosure가 retained parameter box 전체에 균일하면 합산 inclusion이
성립한다. 미완성 partition의 일부 합을 반환하는 것은 이 논증에 포함되지 않는다.

Petras 부분은 구현 soundness를 명시적 antecedent로 둔 composition theorem이다.
Pinned local `acb_calc.rst`의 order 0/1 설명과 실제 returned error가 requested
goal을 초과할 수 있다는 설명도 확인했다. Order 1은 첫 derivative를 요구하는
것이 아니라 value와 holomorphy 보장을 요구한다. 이 문서의 수학은 특정 binary의
soundness나 heuristic의 종료를 증명한다고 주장하지 않는다.

독립적인 midpoint construction은 다음 계산으로 닫힌다. 한 cell에서
`|f(t,u)-f(mid)|≤L_t|t-mid_t|+L_u|u-mid_u|`이고,
`integral |x-mid| dx=h²/4`이므로 cell의 오차는
`area*(L_t h/4+L_u k/4+eta)` 이하이다. 두 좌표 mesh error에 각각
epsilon/4, point evaluation에 epsilon/2를 배분하면 유한 dyadic grid가
명시적으로 결정된다. Point evaluator의 종료는 P3/T4가 별도로 공급하므로
여기에 숨겨진 convergence oracle이 없다.

복소 parameter rectangle에서 center만 계산한 뒤 derivative margin 없이
재사용하면 안 된다. `H(t)=t/3` 예는 정확한 center 평가여도 실패함을 보인다.
T2-PARAM은 전체 convex half-tube에서 derivative를 적분하여
`W=e+(d-c)*(2M/delta_t)*rho_T`를 추가하므로 이 반례를 회피한다.
반대로 고정된 nonzero-width parameter image의 hull이 임의로 좁아진다는
주장은 하지 않는다. Point quadrature error와 intrinsic image width가 정확히
구별돼 있다.

## T4 — effective point evaluation과 complete target

Hypergeometric majorant의 비율은 정확히
`R |a_h+n| / ((b_h+n)(n+1))`이다. 이를
`R(1+|a_h|)/(b_h+n)`로 상계하고 n≥N에서 q_N<1로 묶으면,
N 이후 remainder는 `T_(N+1)/(1-q_N)` 이하이다. N0 이후 q≤1/2를
확보하는 유한 선택이 있으므로 다음 항들을 계산하며 bound를 좁히는 절차가
종료한다. Nonpositive integer a_h의 종료 다항식과 zero derivative prefactor를
별도로 처리하여 0으로 나누는 비율 논증을 피한다. Unregularized 1F1 및
half-integer gamma ratio의 선택은 문서의 source premise와 일치한다.

Elementary part도 닫혀 있다. Positive rational roots의 bisection, Machin
pi enclosure, complex exponential의 absolute tail, positive-real-part complex
square root의 explicit formula가 충분하다. Rational t/u와 rational source
data에서 means/sigma/s/주요 exponential·1F1 arguments가 rational이고,
나머지는 유한한 nonsingular expression tree다. Reciprocal denominator
separation과 product error bound를 사용하므로 holomorphy만으로 computability를
가정하지 않는다.

Endpoint lower tail의 gamma recurrence와 upper tail의 power bound의 지수·계수를
확인했다. `Gamma(1/2,x)≤x^(-1/2)e^(-x)`에서 finite recurrence로 얻은
`e^(-x)P_m(x)`는 `M! x^(-M)P_m(x)`로 상계할 수 있고, M을 모든 exponent보다
크게 고르면 모든 항이 감소한다. 따라서 incomplete gamma의 작은 tail을
수치적으로 계산하는 oracle 없이도 finite cutoff search의 종료가 증명된다.
`S_i W_j+J_i S_j`의 disjoint complement와 `J_i≤W_i`는 안전하며,
서로 무관한 upper bounds를 빼서 interior mass를 만드는 오류는 없다.

Finite tails, constructive interior, finite computable normalization·phase·assembly를
합치면 prescribed positive entry tolerance의 finite certificate가 존재한다.
이는 고정된 512-bit/시간/메모리 cap의 성공을 뜻하지 않는다. 또한 target disk
반지름을 줄이는 것은 fixed raw error 자체를 줄이는 것과 다르다.
Strict interior Pareto margin이 있는 경우만 finite interval decision이 보장되며,
equality boundary의 별도 한계를 적절하게 남긴다. T3의 machine rounding-cell
문제와 SVD scalar authority를 이 norm theorem이 대신 해결하지 않는다.

## T5 — sharp residual, coupled K, model gaps

Exact two-column Gram의 eigenvalue formula와 adjoint로 처리하는 two-row 경우는
맞다. Inner radical width delta가 eigenvalue width delta/2를 주고,
`sqrt(u)-sqrt(l)≤sqrt(u-l)`를 적용하면 outer rounding을 포함한
`sqrt(delta/2)+2delta` bound가 나온다. 따라서 zero/repeated singular value에도
spectral gap 가정이 필요 없다.

`A=D0-c`, `E=D*-c`, `||E||_2≤||E||_F≤rho`에서 reverse triangle
inequality를 적용하면 T5.1이 직접 따른다. Frobenius를 사용한 대상은 shrinking
uncertainty E이며 fixed center residual A가 아니다. Width가
`w_s+2*rho_bar` 이하이므로 radii와 radical width를 줄이면 실제 spectral
discrepancy로 수렴한다. 이 discrepancy는 0일 필요가 없다. `A=a I2`에서는
정확한 spectral norm a와 Frobenius norm sqrt(2)*a의 차이가 영구히 남으며,
새 bound가 이 차이를 제거한다는 synthetic 예도 정확하다.

Target/raw K의 center 차이를 먼저 exact하게 만들고 uncertainty만 radius에
합산하면 center cancellation을 보존한다. C/R 불확실성의 독립성은 필요 없다.
`min(U_K,(U_C+U_R)/2)`와 Dmax의 max bound는 각각 유효하다. 저장된 model K를
model C/R에서 재구성하지 않는 제약도 유지한다.

각 model의 direct target error interval에 max와 interval subtraction을 적용하면
같은 target의 gap을 포함한다. 별도의 raw-gap perturbation interval도 같은
scalar를 포함하므로 intersection은 유효하며, empty intersection은 premise나
identity 실패다. Direct interval은 실제 gap으로 수렴하지만 raw perturbation
interval의 nonzero epsilon은 남을 수 있다는 구분도 맞다. Producer terms나
legacy eta를 여기에 다시 더하지 않는 것이 적절하다.

## T5-R01 — 유한 radius 예산 누락, 수정 확인

최종 source hash 기록 중 새로 추가된 T5.5 accuracy allocation을 확인했다.
수정 전에는 `rho≤sqrt(94)*r`만으로 error interval width가
`w+2sqrt(94)*r` 이하라고 주장했다. 그러나 실제 T5.1은 computed outward
upper bound `rho_bar`를 사용하므로 width bound는 `w+2*rho_bar`다.
P6의 `rho_bar→0`은 특정 finite 단계의 정량 bound를 제공하지 않는다.

반례는 실제 HH 값 없이 기존 dyadic sqrt 규칙으로 구성된다. `m=1`,
94개 radius를 `r=1/160`, target과 disk centers를 0으로 둔다.
Model center residual은 `2 I2`를 47×2에 zero padding한 행렬이다.
Center norm은 정확히 2이므로 `w=0`이다. `rho²=94/25600`을 `p=1`에서
enclosing하면 `floor(4*94/25600)=0`이므로 sqrt interval은 `[0,1/2]`이고
`rho_bar=1/2`다. T5.1 interval `[3/2,5/2]`의 width는 1인데, 수정 전
주장한 `2sqrt(94)/160`은 1/8보다 작다. 이후 p를 증가시키는 sequence는
P6도 만족할 수 있으므로 P6만으로 이 반례를 배제할 수 없다.

저자는 최종 문서에서 이 allocation에 사용할 **exact rational upper bound
`rho_bar_C=rho_bar_R=rho_bar_K=10r`를 직접 지정**했다. 이는 모든 블록에서
`rho≤sqrt(94)*r≤10r`이므로 유효하며, 별도의 radical rounding 오차를 남기지
않는다. 새 gap-width bound는 `2w+40r`다. Positive margin m에 대해 예컨대
positive `r=m/160`, `w=m/8`을 선택하면 `2w+40r=m/2<m`이므로
필요한 finite decision implication이 복구된다. 이 수정은 읽고 직접 유도하여
확인했으며, 추가 suite나 실제 수치 실행을 사용하지 않았다.

Finding **T5-R01은 수정 확인 후 닫혔다.** 수정 전 affected MD SHA256은
`092a0d7ecac5f55c1c0ede90a7a5584936b911c9aa7a9cc155a28d5949a7ff41`,
수정 확인한 최종 MD SHA256은
`c1c4a372e83ea161065f580f75f20e705780797d0ce59b4a372d1f5c6746992a`다.
원래 sharp residual theorem과 T4의 존재 정리는 이 누락의 영향을 받지 않는다.

## 조건부 수용 뒤에도 남는 사실

수학적 존재·수렴과 다음 사실은 별개다: 실제 stored bytes의 exact decoding,
historical ABI, source formula/normalization/order의 실제 binding, actual domain
margin과 coefficient enclosure, production evaluator의 implementation verification,
실제 시간·메모리 안의 성능, 실제 source discrepancy와 예산의 대소관계,
actual model gaps, frozen floating predicate authority, 최종 독립 scientific admission.
이번 검토는 이들의 값을 계산하거나 status를 닫지 않았다. 한 번의 bounded
theory review를 여기서 종료하며 추가 재귀 감사는 제안하지 않는다.

검토한 네 MD 파일의 SHA256·byte count와 참고한 pinned API 문서 identity는
`INDEPENDENT_THEORY_REVIEW.json`에 기록했다. 작성 중인 저자 JSON은 hash
authority로 사용하지 않았다.
