# G5 endpoint evaluator와 split 목적함수

`endpoint_bound/engine.py`는 G1에서 채택된 signed Hermite absolute envelope와 Gaussian O/G majorant를 **exact rational outward bound**로 평가한다. 원문 재검색과 HH 입력 읽기는 하지 않는다. 실제 Frozen107 constants·split·적분·D entry는 미평가다. `ENDPOINT_BOUND_VERIFICATION.json`의 IMPLEMENTATION_VERIFIED는 synthetic evaluator에 한정하며 B02 전체 또는 actual epsilon certificate를 닫지 않는다.

## 입력과 출력

입력은 Python `int`/`Fraction`만 받는다. μ,a,b>0, i,j,k∈{0,…,8}, real 3D centers, angular∈{s,px,pz}, field∈{O,G1,G2}, 0<ℓ_t<T_t 및 0<ℓ_u<T_u가 필요하다. `Interval`의 endpoint도 float·bool·문자열을 자동 변환하지 않는다. Caller가 decimal 또는 dyadic serialization을 해석할 때 먼저 exact rational을 명시적으로 만들어야 한다. Nonfinite float, unknown shape 및 부적절한 domain은 enclosure를 반환하지 않는다.

`gaussian_field_majorant`는 primitive bound C_F를 반환한다. `lower_mass_bound`, `upper_mass_bound`, `interior_mass_bound`는 각각 양의 1D envelope의 상계를 반환한다. `complement_bound`는 E_t,E_u,W_u,J_t,C_F와

\[
B_{\mathrm{out}}=C_F(E_tW_u+J_tE_u)
\]

를 exact Fraction으로 반환한다. generic 함수는 전달받은 수가 실제 HH 값인지 판별할 수 없으므로 `actual_hh_evaluation_assertion=null`, `input_scope=CALLER_SUPPLIED_EXACT_PARAMETERS_NOT_CLASSIFIED`로 반환한다. 미래 caller가 실제 HH 입력을 전달했다면 상위 execution receipt는 actual evaluation 사실을 별도로 정확히 기록해야 한다. 첫 구현의 무조건적 `HH_evaluated=false`는 제거했다.

## 증명과 코드의 대응

### 기본 outward arithmetic

Fraction interval의 +,−,×,÷는 정확한 rational endpoint arithmetic과 끝점 극값을 사용한다. 0을 포함한 denominator interval은 거절한다. `sqrt_bounds`는 `isqrt(floor(x 2^(2p)))`로 floor endpoint를 구하고 필요할 때 정확히 한 dyadic ulp를 더한다. `quantize`의 lower는 floor, upper는 ceiling이다. Host floating conversion은 없다.

π는 Machin identity `16 atan(1/5)−4 atan(1/239)`와 alternating-series의 인접 partial sums로 감싼다. `exp_neg_bounds`는 x/2^m≤1까지 range reduction을 하고 e^-y의 alternating Taylor series에서 인접 partial sums를 잡는다. 양의 interval을 m번 square할 때마다 outward quantization하므로 e^-x의 포함관계가 유지된다. 요청 precision은 upper bound의 정확도를 자동 보장하는 certificate가 아니며 실제 반환 width를 사용한다.

### Upper incomplete gamma

x>0에서 b=e^-x/√x와 g=Γ(1/2,x)를 두면 integration by parts로

`g=b−(1/2)Γ(−1/2,x)`, `0≤Γ(−1/2,x)≤g/x`.

따라서 `b/(1+1/(2x))≤g≤b`다. 정확한 upper incomplete gamma 값을 special-function library에 의존해 계산하는 대신 이 analytic enclosure를 사용한다. 양의 recurrence `Γ(s+1,x)=sΓ(s,x)+x^s e^-x`가 모든 필요한 positive half-integer shape에 이를 전파한다. 이 bound는 특히 작은 x에서 넓을 수 있다. 넓음을 invalidity나 producer defect로 분류하지 않는다.

### 1D endpoint와 interior envelope

G1 표기의 λ=μ²/4, ν=i+3/2−r, A_ir>0를 그대로 쓴다. Lower에는

`a^(-3/2) Σ A_ir λ^(1−ν) Γ(ν−1,λ/ℓ)`

를 사용하고, upper에는

`Σ A_ir T^(−ν−1/2)/(ν+1/2)`

를 쓴다. Lower의 gamma는 unregularized **upper** convention이다. Whole-axis bound W는 임의 positive pivot에서 lower+upper를 더해 만든다.

J는 W−E로 만들지 않는다. 유한 panel [left,right]마다 `exp(−λ/t)t^(−ν)`의 maximum은 stationary point λ/ν를 해당 panel에 clamp한 위치에 있다. `(a+t)^(-3/2)≤(a+left)^(-3/2)`와 곱하고 panel width를 곱한 후 양의 합을 취한다. 서로 다른 양의 항의 maximum이 다른 지점에 있어도 항별 maximum의 합은 유효한 상계다. 이것은 signed UU를 양의 quadrature measure로 오해하는 연산이 아니다.

### Gaussian field majorant와 pz 항

실수 Gaussian completion 뒤 X=√(a+t)|r1−a d1/(a+t)|, Y=√(b+u)|r2−b d2/(b+u)|로 둔다. D1≥|d1|,D2≥|d2|를 outward 계산하고

`L1=D1+X/√a`, `L2=D2+Y/√b`, `R=L1+L2`

로 둔다. P=1(s) 또는 L1(px,pz)에 대해 다음 positive polynomials를 적분한다.

| field | majorant polynomial |
|---|---|
| O | R^k P |
| G1 | R^k(2a L1 P + δ_pz) |
| G2 | R^k 2b L2 P |

real wave-number phase는 modulus 1, real Gaussian attenuation은 ≤1이다. Jacobian `(a+t)^(-3/2)(b+u)^(-3/2)`를 밖으로 빼고, 각 monomial X^mY^n에 `M_m M_n`을 곱한다. 여기서 `M_n=2πΓ((n+3)/2)`이며 필요한 n≤10은 exact integer/half-integer recurrence로 처리한다. pz G1의 +1을 보존한다. 이 단계에는 normalization, donor coefficient, orbital coefficient를 곱하지 않았으므로 상위 finite contraction에서 각각 정확히 한 번만 적용해야 한다.

### 2D accounting

Complement partition은 `(E_t×all_u) disjoint_union (I_t×E_u)`다. 코너는 한 번 포함한다. 역방향 partition의 independent upper를 추가로 계산하고 **둘 중 작은 upper**를 택하는 것은 양쪽 유효성이 입증된 경우 가능하다. 현재 구현은 먼저 제시한 한 방향만 평가한다. B_out은 modulus disk bound이고 최종 complex rectangle에 넣는 변환은 G1의 disk/rectangle 규칙을 따른다.

## 유한 split 선택 목적함수

미래 승인된 실제 실행에서 positive rational 후보들의 유한 집합 S를 미리 고정한다. 각 후보 s=(ℓ_t,T_t,ℓ_u,T_u,precision,panels)에 대해 primitive endpoint bound와 선택한 interior algorithm의 예상 cost/width를 분리해서 기록한다. 하나의 예시는

`min_s B_endpoint(s)` subject to predeclared interior work/width caps,

또는 `min_s max(B_endpoint(s)/endpoint_budget, predicted_interior_work(s)/work_cap)`다. cost prediction은 proof authority가 아니다. endpoint upper가 작더라도 실제 interior enclosure가 넓거나 비싸면 전체 certificate는 미완료다. 후보를 target holdout 결과에 맞춰 model retraining하는 행위도 아니다.

현재 G5는 split optimizer를 자동 실행하지 않으며 HH 후보를 선택하지 않았다. 필요한 다음 measured quantities는 실제 C_F 크기, 각 density endpoint contribution, contracted bound, interior final radius와 실제 비용이다. endpoint와 interior radius를 final D ball에 한 번씩만 넣고 X0…X8 producer decomposition을 추가하지 않는다.

## Resource cap과 fail-closed 의미

- precision 16…1024 bits; input/Interval rational numerator·denominator 각각 16384 bits cap.
- exp Taylor ≤4096 terms, 기본 512; range reduction ≤64 squarings.
- arctan ≤1024 terms; Hermite degree 0…8; half-gamma twice-shape ≤41.
- Gaussian moment degree ≤12; integer/half powers의 twice-exponent absolute cap 128.
- interior mass panels 1…128, 기본 8. Bool은 정수 resource 값으로 수용하지 않는다.

Cap 초과는 `ResourceLimit`으로 반환값 없이 중단한다. 현재 evaluator의 caps는 알고리즘의 유한 작업량 제한이며 OS-level wall/RSS hard limit을 대신하지 않는다. 극히 작은 positive 입력에서 absolute dyadic sqrt enclosure의 lower가 0이 되면 reciprocal이 fail closed한다. 정밀도를 명시적으로 늘리거나 scale-aware implementation을 별도 검증해야 한다; midpoint division이나 precision downgrade로 우회하지 않는다.

## 최초 실패와 최종 검증

기존 RED와 FIRST_IMPLEMENTATION은 그대로 보존했다. 최초 12 tests의 실패 두 개는 (1) 서로 다른 interval expression의 upper endpoint를 같다고 요구한 **test defect**, (2) mpmath 미설치 **environment dependency error**였다. 실제 pz field upper의 오류로 분류하지 않았다. 전자는 π³,3π³,4π³에 대한 독립 containment 확인으로 고쳤고, 후자는 stdlib Decimal oracle로 대체했다.

새로 확인한 exact-input 계약 문제는 별도 `RED_INPUT_GUARDS.*`에 보존했다. 5개 tests 내 18개 failing subtests를 관측한 뒤 float/bool/string 암묵수용 및 잘못된 degree/cap 수용을 차단했다. 최종 suite는 17개 unique tests다. 이전 과학 suite나 G1 test 수와 합산하지 않는다.

독립 oracle은 Decimal 90자리, AGM π, erf entire series를 쓰며 engine의 Machin/half-gamma bound와 구현 경로가 다르다. Endpoint integral diagnostics는 synthetic parameter에서 composite Simpson 256/512 panels를 비교했다. 이 numerical oracle와 refinement delta는 **rigorous quadrature enclosure가 아니다**. bounds의 수학적 authority는 위 analytic majorants와 exact outward arithmetic이며 oracle은 구현 오류를 찾는 독립 검산으로만 사용했다.

`certified_epsilon=null`, `certified_eta=null`, `rigorous=false`, actual HH execution count=0.
