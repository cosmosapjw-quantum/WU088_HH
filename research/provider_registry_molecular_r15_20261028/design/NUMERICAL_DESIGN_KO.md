# R15 C3 수치 설계와 오차 예산

상태: **AUTHORED_NOT_IMPLEMENTED_NOT_EXECUTED**. 이 문서는 C2 API에 대응하는 실행 전 설계이다. DAG 29/46이며 새 이론·코드 노드는 아직 채택되지 않았다. 실제 구현, 독립 검토, 소스 동결, 제한된 실행, 결과 판독은 이후 단계이다.

## 1. 계산 대상과 전제

원래 source cell마다 주어진 네 개의 비음수 Bernstein-B3 계수를 그대로 사용한다. 이는 모든 점별 비음수 3차식을 포함한다는 주장이 아니다. 예를 들어 `(u-1/2)^2`의 B3 계수 `[1/4,-1/12,-1/12,1/4]`는 함수 자체가 비음수여도 이번 입력 원뿔 밖이므로 거부한다.

`q,tau`는 고정 K/pi/destruction, 전체 w 구간, 모든 시작시간, zero-mass residual에 대한 full-A 인증 입력이다. 코드에서 nominal K의 수축률로 대체하거나 인증을 새로 계산하지 않는다. `c>=0`는 비교식 결합상수이며 광속 기호와 다르다. R 및 E의 하한은 공급된 bound-forcing이 정의하는 이상 비교함수의 하한이고, 실제 물리적 오차의 하한이 아니다. E=abs(eta), coarse l1=4E를 유지한다.

원래 t0를 보존한 `h(age)=q^floor(age/tau)`를 사용한다. q=0에서도 h(0)=1이다. 실제 오른쪽 연속 끝점과 왼쪽 극한을 구분하며, 셀 전체 상한에는 양쪽이 필요한 경우 각각 포함된다. 어떠한 cap 변환기도 도입하지 않는다.

## 2. 정확한 셀 구성과 4차식

base clock은 observation knots와 `[t0,T]` 안에 있는 `source_knots+k*tau`, k=0..B의 정확한 합집합이다. 계산상 극값 분할점은 이 시간격자에 삽입하지 않는다. source cell `[a,b]`와 age block k가 주는 겹침 구간은

\[
L(t)=\max(a,t-(k+1)\tau),\qquad U(t)=\min(b,t-k\tau)
\]

이며, 비어 있지 않은 한 base cell에서는 L,U 및 중점이 affine이다. 원래 B3를 de Casteljau로 이 경로들에 제한한다. 3차식 Simpson 항등식

\[
\int_L^U g(s)ds=\frac{U-L}{6}\{g(L)+4g((L+U)/2)+g(U)\}
\]

으로 비음수 B1과 비음수 B3의 곱을 얻는다. D의 B1 계수를 D0,D1, 중괄호의 B3 계수를 S0..S3라 하면 출력 B4의 k번째 계수는

\[
\frac16\left(\frac{4-k}{4}D_0S_k+\frac{k}{4}D_1S_{k-1}\right),\quad k=0,\ldots,4,
\]

정의되지 않은 항은 0이다. 모든 overlap을 q^k로 가중해 더하고, 셀 내부에서 일정한 h(left-t0)R0를 더한다. 동일 셀의 4차식은 한 번만 구성한다. 독립 reference는 이 Simpson/Bernstein 경로를 읽거나 호출하지 않고 원래 source 다항식의 J0..J3 적분을 수행한다.

## 3. 극값 분할, 정확한 틈, 작업량

B4 계수 B의 정규화 도함수 B3 계수는 `4*(B[i+1]-B[i])`이다. 정확한 0을 삭제한 부호변화 V를 계산한다. V=0인 비상수 도함수는 한 약한 부호이므로 셀의 정확한 최대는 끝점에서 얻는다. 도함수가 모두 0이면 상수 셀이다. V>0이면 정규화 중점에서 정확히 이분하며 깊이96에서 멈춘다.

깊이 제한 잎에서는 끝점과 중점의 실제 값 중 최댓값을 하한으로, 제한된 B4 계수 최댓값을 상한으로 저장한다. 완전한 잎 분할을 보존한다. 이는 잎마다 근이 하나라는 주장이 아니며, dyadic 분할 경계의 근과 중근을 허용한다. 독립 검증은 경계 공유 및 중복도를 고려한다.

도함수 차수가 최대3이므로 한 깊이의 양의 variation 노드 수는 최대3이다. 따라서 한 셀에서 split<=3*96=288, visit<=6*96+1=577이다. **이 variation-diminishing 근거는 R6 검토를 통과해야 실행할 수 있는 증명 의무이다.** 런타임에서도 실제 누적수를 검사한다.

\[
M_B=4\max_i|B_{i+1}-B_i|,\qquad
0\le U-L\le M_B2^{-96}\le4C_{\max}2^{-96}.
\]

마지막 부등식은 이번 모델의 비음수 B4에 사용한다. 일반 부호 B4에 그대로 적용하지 않는다. dyadic128 변환으로 추가되는 전체 폭은 최대 `2*2^-128`이다. observation 구간에 여러 base cell이 있으면 exact_lower, exact_upper, M_B, Cmax, proved_gap_bound를 각각 자식 셀의 max로 집계하고, 집계된 exact_gap과 dyadic outward bounds를 따로 계산한다.

## 4. 부호 있는 스칼라 전달

각 base cell 길이를 Δ, z=d_c*Δ라 하고

\[
W_i(z)=\Delta\int_0^1 e^{z(1-u)}\binom4i u^i(1-u)^{4-i}du
\]

를 계산한다. z>=0에서는 `W_i=Δ sum_(n>=0) z^n/n! * beta_i(n)`의 양의 급수를 사용한다.

| i | beta_i(n) |
|---|---|
| 0 | 1/(n+5) |
| 1 | 4/((n+4)(n+5)) |
| 2 | 12/((n+3)(n+4)(n+5)) |
| 3 | 24/((n+2)(n+3)(n+4)(n+5)) |
| 4 | 24/((n+1)(n+2)(n+3)(n+4)(n+5)) |

0..96차 항을 정확히 합산한다. 첫 누락항 n=97에서 이후 비는 최대 `16/98<1`이므로 양의 기하급수 상계로 꼬리를 감싼다. exp와 phi에도 각각의 양의 항을 사용한다. z<0은 `W_i(-z)=exp(-z)W_(4-i)(z)`와 exp의 양의 reciprocal 구간으로 처리한다. z=0은 Wi=Δ/5를 정확히 사용한다. signed d의 어느 경우에도 양의 가중치를 빼서 cancellation을 만들지 않는다.

`cR+g_e`는 B4로 표현한다. 양의 moment와 현재 E 구간으로 다음 끝점 E를 outward 계산하고, 각 누적 단계에서 dyadic128 방향 반올림을 수행한다. 셀 전체 E는 `Qmax=c*Rsup_upper+max(restricted g_e B3)`와 왼쪽 E upper에서 시작한 같은 signed-d 상수 forcing majorant로 감싼다. 이 majorant의 도함수는 일정한 부호이므로 양 끝점의 max가 전체를 감싼다. 다음 셀에는 별도로 계산한 다항 forcing 끝점 E를 전달한다.

## 5. 서로 구분하는 오차와 보장

| 항목 | 이번 계산의 처리 |
|---|---|
| 입력 source 표현 | 주어진 정확한 유리 B3. source 근사오차를 새로 추정하지 않는다. |
| original-memory convolution | 정확한 Fraction overlap; 수치적분 오차 없음 |
| 4차 극값 | 유한 깊이로 남는 명시적 `M_B*2^-96` 틈 |
| 스칼라 exponential moment | Taylor96의 증명된 양의 꼬리와 dyadic 방향 반올림 |
| 독립 Decimal160 | 고정 상대 guard `1e-80`; interval reference가 아닌 guarded corroboration |
| 물리적 forcing/certificate | 외부 전제이며 이번 산술 대조군의 성공으로 대체하지 않는다. |

reference는 strict 무-guard 포함 실패의 개수와 예시를 별도로 저장한다. guard는 결과를 본 후 조정하지 않는다. 모든 후보 합격은 실제 저장 결과와 검토가 끝난 뒤에만 판정한다.

## 6. 유한 캠페인과 자원 한계의 의미

CONTROL_PLAN.json의 21개 full model은 설계상 총75 base cells, overlap precharge 합4811이다. 최다 source16/observation32/full blocks8 경계는 정렬된 상수 forcing 한 모델로 다룬다. 7개 reachable quartic 도함수 패턴으로 세 단순근, 대수적 근, 중근, 삼중근, 경계근, mixed-coefficient 무근, 상수를 다룬다. 양·음 d의 허용 끝값 ±16을 별도 두 모델로 포함하여 Taylor 꼬리의 경계도 실제 한 캠페인 안에서 검증한다. 별도 무제한 스캔은 없다.

이 조합론적 작업 상계는 실행시간이나 메모리의 보편적 상계가 아니다. 입력 bit256, 파생 bit16384, base512의 모든 허용 조합이 CPU120초/1GiB 안에서 끝난다고 주장하지 않는다. 그 자원 제한은 실제 동결된 캠페인에 적용되는 OS 한도이다. 자원 중단은 실패/중단 기록이며 PASS가 될 수 없다. CLI는 정수 변환 limit6000을 유지하고 출력 rational 문자열은10000자를 넘기지 않는다.

R14는 source 구조, parser/binding, dyadic 방향 반올림, 원래 t0 기억 및 저장된 결과 형식의 근거로 재사용한다. R14 결과를 다시 실행하거나 이번 B3/B4 변경의 검증으로 대신하지 않는다. baseline commit과 SHA는 API_MAP.json에 명시했다.

## 7. 저장 결과만 사용하는 수렴 그림

같은 단일 primary 캠페인 안에서 ROOT_THREE_RATIONAL과 ROOT_THREE_MIXED_ALGEBRAIC의 두 번째 셀에 해당하는 양의 B4를 고정하고 D=0,4,8,16,32,64,96에서 내부 extrema 진단을 수행한다. 이는 새 full model이나 새 실행이 아니다. 공개 run_case의 깊이는96으로 고정하며 내부 진단만 일반 D의 증명된 `3D` splits, `6D+1` visits, `M_B*2^-D` 틈을 사용한다.

14개 진단의 exact bounds/gap, 이론적 gap bound, 실제 splits/visits를 checks의 DEPTH_SWEEP 행으로 저장한다. depth0은 즉시 hull terminal이므로 splits0/visit1로 정의한다. 두 대조군 전체의 사전 작업량은 splits<=1320, visits<=2654이다. dyadic 근 대조군은 일찍 정확한 극값을 얻고, 대수적 근 대조군은 큰 깊이에서도 양의 틈을 남겨 수렴을 볼 수 있다. renderer는 이 저장 값과 모델의 끝점/whole-cell 값을 사용하며 과학 코드를 다시 실행하지 않는다.
