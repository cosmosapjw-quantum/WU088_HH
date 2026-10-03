# 선택한 연속 목표 인증 경로의 이론 공백 해소

이번 작업은 `EXACT_CONTINUOUS_TARGET_ENCLOSURE_PLUS_ARCHIVED_RAW_COMPARISON` 경로에서
확인된 수학적 연결을 끝까지 유도했다. 복소 영역의 명시적 상계, 전체 매개변수 상자에
대한 중첩 적분, 임의 정확도 인증의 유한 구성, 고정된 부동소수점 판정의 경계,
raw와 연속 목표 사이의 날카로운 노름 구간을 다섯 증명으로 정리했다.
각 결론은 문서에 열거한 입력·소스 전제 아래 성립한다.

기존 B01–B05 장부에는 수학 정리와 실제 데이터·빌드·실행 의무가 함께 들어 있었다.
새 장부는 원래 상태를 보존하면서 이론 부분의 증명 위치와 남은 실행 의무를 각각
대응시킨다. 실제 HH 데이터를 계산하지 않았으므로 과학적 인증 상태는 바뀌지 않는다.
`epsilon=null`, `eta=null`, `rigorous=false`이다.

## 1. 이번에 증명한 내용

| 증명 | 해소한 이론 공백 | 핵심 결과 |
| --- | --- | --- |
| T1 | 복소 callback의 정의역·분기·균일 상계 | 양의 실수부 여유, 안전한 상자 교집합, 공간 Gaussian 적분으로 얻은 명시적 M 및 Cauchy 미분 상계 |
| T2 | 중첩 적분의 전체 상자 포함성과 종료 논거 | 매개변수 적분의 정칙성, 적응 분할의 포함성, Petras와 독립적인 유한 midpoint 인증 |
| T3 | 실수 부등식과 고정 machine predicate의 관계 | RNE ties-to-even의 정확한 유리수 경계, 두 strict 규칙의 차이, scalar 구간의 충분조건 |
| T4 | ‘충분히 정밀하게 계산하면 된다’의 구성적 증명 | 1F1 급수의 유효 나머지, endpoint의 유효 감소, 전체 목표 entry의 임의 정확도 유한 인증 |
| T5 | Frobenius 상계의 영구적인 보수성과 K 상쇄 | 중심 잔차는 정확한 2×2 Gram으로, 줄어드는 반경만 Frobenius로 감싸 실제 spectral discrepancy에 수렴 |

이전 문헌 목록을 늘리는 대신, 이미 고정된 소스 정의에 이 증명들을 연결했다.
수학 검토와 실제 scientific decision admission은 별도이며 후자는 아직 수행하지 않았다.

## 2. 복소 상계와 적분을 연결하는 방법

복소 상자에서 `A=a+t`, `B=b+u`라 하자. `alpha=inf Re A>0`,
`beta=inf Re B>0`이고 `Q_A>=sup |A|²`, `Q_B>=sup |B|²`이면

\[
\Re\sigma\ge s_0=\tfrac12(\alpha/Q_A+\beta/Q_B)>0,
\qquad |\sigma|\le s_1=\tfrac12(\alpha^{-1}+\beta^{-1}).
\]

따라서 `sigma=(1/A+1/B)/2`의 역수와 반정수 거듭제곱을 정의할 여유가 명시된다.
다만 계산된 큰 구간이 분기선을 가로지르면 그대로 `pow`에 넣을 수 없다.
독립적으로 증명된 `[s0,s1]+i[-s1,s1]`와 교차한 뒤 바깥쪽으로 반올림하고,
양의 실수부 여유를 다시 확인해야 한다. 밀도 U의 `t,u` 분기 조건도 별도로 지킨다.

O/G의 상계는 원래 실수 공간에서 Gaussian을 완전제곱하여 구했다.
`|r1-r2|^k`를 포함한 공간 적분에 복소 contour 이동을 적용하지 않는다.
실수 q의 원래 위상은 절댓값 1이지만, 완전제곱된 복소 식의 개별 위상 인자가
모두 절댓값 1인 것은 아니다. T1은 이 차이와 pz 미분의 +1 항까지 포함한다.

양의 실수 적분 사각형에 여유 `delta_t,delta_u`를 붙인 복소 영역에서
`|f|<=M`을 얻으면 `|∂t f|<=M/delta_t`, `|∂u f|<=M/delta_u`이다.
면적 A의 실수 사각형에 격자 폭 `h_t,h_u`를 쓰고 각 중점 평가의 절대 오차를
eta 이하로 감싸면

\[
|I-Q|\le A\left(\frac{Mh_t}{4\delta_t}
                    +\frac{Mh_u}{4\delta_u}+\eta\right).
\]

각 셀에서 중점까지의 거리 적분이 `h²/4`이므로 얻는 직접적인 부등식이다.
T4의 급수 나머지와 endpoint 감소를 연결하면 모든 양의 목표 오차에 대해
유한 격자와 유한 정밀도로 끝나는 절차가 존재한다. 기존 Petras 구현이 끝나는지와
무관하게, 선택한 목표 자체가 구성적으로 인증 가능함을 보인 것이다.

중첩 방식에서는 내부 적분이 외부 변수의 **상자 전체**에서 유효해야 한다.
호출마다 분할이 달라도 전체 구간을 빠짐없이 덮고 각 패널이 전체 상자에서 유효하면
포함성은 유지된다. 비영점 매개변수 상자에는 본래 함수값의 폭이 있으므로,
내부 적분 정밀도만 높여 그 폭을 0으로 만들 수는 없다.

## 3. raw 오차를 더 날카롭게 감싸는 결과

최종 목표 entry들이 `|D*ij-cij|<=rij`를 만족하고
`rho=sqrt(sum rij²)`라 하자. 정확한 중심 잔차 `D_raw-c`의 spectral norm을
2×2 Gram으로 `[s_minus,s_plus]`에 감싸면

\[
\boxed{\max(0,s_{minus}-\rho)\le
\|D_{raw}-D^*\|_2\le s_{plus}+\rho.}
\]

반경과 Gram radical 구간을 줄이면 양 끝점은 실제 spectral discrepancy로 수렴한다.
기존 entrywise Frobenius 상계는 실제 Frobenius norm으로 수렴하므로 계속 보수적일
수 있다. 예를 들어 0인 목표와 `a I₂`인 raw에서는 spectral 오차가 a이지만
Frobenius 상계는 `sqrt(2)a`이다. 허용 예산이 `5a/4`이면 새 증명은 인증하고
옛 상계는 인증하지 못한다. 이 예는 정확한 합성 행렬이며 실제 HH 값은 아니다.

목표 반경을 줄여도 **고정된 raw 오차가 0으로 가는 것은 아니다**.
허용 예산보다 실제 오차가 작다는 양의 여유가 있어야 유한 단계의 성공이 보장된다.

K는 목표 및 정확한 raw에 대해 `(C-R†)/2`의 중심을 먼저 구성한 뒤 직접 Gram을
적용하여 중심 잔차의 상쇄를 보존한다. 저장된 모델 K는 독립된 입력으로 유지한다.
같은 목표 구간에서 모델 오차를 직접 감싸 얻은 gap과 기존 raw gap±2epsilon을
교차할 수도 있다. 같은 오차를 두 번 더하거나 X0…X8을 다시 붙이지 않는다.

## 4. 고정된 비교식의 정확한 경계

각 목적의 local machine scalar를 a, other scalar를 b라 하고,
tau는 고정된 binary64 `1e-10`의 정확한 값이라 하자. 실수의 정확한 `10^-10`과는
구별한다. T3의 유한·비음수·overflow 보호 영역에서 스칼라 연산이 명시된 binary64 RNE 조건을 만족하면

| 비교 | 실제 식 | 정확한 경계 |
| --- | --- | --- |
| 공통 weak | `a <= RN(b+tau)` | `b-a > -tau-h_minus(a)`, 경계에서는 a의 짝수 significand만 허용 |
| PRIMARY strict | `RN(b-a) > tau` | `b-a >= tau+2^-87` |
| SECONDARY strict | `a < RN(b-tau)` | `b-a > tau+h_plus(a)`, 경계에서는 a의 홀수 significand만 허용 |

여기서 h는 해당 이웃 representable 값까지 간격의 절반이다.
PRIMARY의 등호 허용은 tolerance의 significand가 홀수이기 때문에 정확한 midpoint가
짝수 successor로 반올림되는 결과다. 임의로 strict 조건을 완화한 것이 아니다.

T3은 실수식에서 strict 개선이어도 PRIMARY가 실패하는 예, PRIMARY는 참이고
SECONDARY는 거짓인 예, machine weak는 참이지만 real weak는 거짓인 예를 제시한다.
따라서 exact norm을 계산했다고 기존 SVD 출력 scalar도 정확히 반올림되었다고
간주할 수 없다. 실제 scalar bit 또는 그 계산과 수학량을 연결하는 별도 오차 증거가
필요하며, T3은 그 증거가 있을 때 적용할 정확한 충분조건을 완성했다.

## 5. 종료에 대한 결론과 남은 일

양의 정확도를 요구하는 **목표 적분 인증**에는 유한 구성 증명이 있다.
512-bit·20,000-call·300초와 같은 고정 예산 내 성공은 이 정리에서 나오지 않는다.
실제 budget 여유와 runtime은 계산해야 하는 사실이다.

판정 경계에서 양의 거리가 있으면 충분히 좁은 구간으로 결국 판단할 수 있다.
경계와 정확히 같은 값은 shrinking interval만으로 유한 단계에 equality를 증명하지
못할 수 있다. 이는 이론 공백을 다음 작업으로 미룬 것이 아니라, 보장할 수 있는
명제와 보장할 수 없는 명제를 분리하고 반례로 확인한 결과다. 특정 HH 사례가
결정 불가능하다는 주장은 하지 않는다.

| 남은 항목 | 성격 | 이번 이론 증명과의 관계 |
| --- | --- | --- |
| 실제 입력·stored pref·모델 K·과거 raw ABI 결박 | 데이터/이력 | 수학으로 파일의 과거 의미를 대신 증명할 수 없음 |
| native callback·FLINT/GMP/MPFR·빌드/링크 검증 | 구현/실행 | 정리의 연산·포함성 계약을 실제 코드가 이행하는지 확인 |
| 실제 endpoint·interior·최종 D 구간과 epsilon/eta | 수치 인증 | 임의 정확도 가능성은 증명됨; 값은 미계산 |
| 실제 gap의 양의 여유 및 고정 예산 내 실행 가능성 | 수치/자원 | 보편적 성공 주장을 하지 않음 |
| 최종 과학적 승인 | 별도 admission | 이번 수학적 독립 검토가 이를 대체하지 않음 |

기존 order verdict, PRIMARY/SECONDARY holdout 결과, R31AK freeze, z075 holdout 역할,
B128/B160 소비 상태, B192 기존 출력 재사용 조건은 유지한다.
새로운 실제 HH 계산, native build, source 수정, comparator 재실행은 모두 0회다.

## 증명 및 검증 자료

T1–T5 본문이 증명의 근거다. 44개 합성 점검(8+7+12+4+13)은 유리수 산술·반례·
경계 처리를 확인하며 증명을 테스트로 대신하지 않는다. T1/T2/T4/T5와 T3에 각각
저자와 분리된 한 차례의 반례 중심 검토를 적용했다. 이 과정에서 T5의 유한 예산 배정에
실제 반경 rho와 바깥쪽 상계 rho_bar를 구별해야 한다는 결함 1건을 찾아 수정했다.
94개 entry 각각의 반경이 r 이하일 때 rho_bar=10r이라는 정확한 유리수 상계를
명시하고 회귀 검산을 추가했다. 최종 결과와 파일 hash는
`INDEPENDENT_THEORY_REVIEW.json`, `T3_INDEPENDENT_REVIEW.json`,
`THEORY_CLOSURE_LEDGER.json`, `VERIFICATION.json`에 결박한다.

`RESULT.json`에는 시작 commit만 기록하고, 게시 후 실제 commit/tree 및 두 백업의
영수증은 별도 `DELIVERY_RETURN.json`에 결박한다. 기존 파일을 바꾸지 않는 동일
branch의 추가 commit으로 게시하며 main 병합이나 force push는 하지 않는다.
