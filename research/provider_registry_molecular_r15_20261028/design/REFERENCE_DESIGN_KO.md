# R15 독립 reference 설계 — C3

상태: **설계 작성 완료, 구현·실행·과학적 수용 전**. 이 문서는 C3의 독립 계산 경로를 고정한다. C4의 수용 항목과 유한 자원은 `REFERENCE_ACCEPTANCE_MAP.json`에 있다. 이 작성으로 연구 DAG 노드는 완료되지 않는다. 현재 인계받은 연구 DAG 표기는 **29/46**이며, 게시·백업·계약 반영·동결·실행은 root가 담당한다.

## 1. 범위와 독립성

대상 단위는 `WU_CUBIC_BERNSTEIN_FORCING_R15`이다. 독립 reference는 다음 파일만 교환 인터페이스로 사용한다.

- R15 `CONTRACT.json`, 현재 `AGENTS.md`의 R15 선행 지시, 이론 정의·전제 문서.
- production 작성자의 `API_SCHEMA.md`, `INPUT_SCHEMA.json`, `OUTPUT_SCHEMA.json`, `API_MAP.json` 및 동결할 `verification/CASES.json`.
- root가 실제 primary 실행 후 저장한 `raw/PRIMARY_RESULTS.json`.

production 구현, 이전 production 구현, production의 subdivision·overlap·moment 함수는 읽거나 import하지 않는다. `API_MAP.json`의 식과 입출력 의미는 공유하지만 reference의 계수 계산·다항식 연산·Sturm 판정·scalar 적분은 별도로 작성한다. 작성 시점에 과학 실행, 과학 import, CAS 호출은 모두 0이다. 이 문서는 앞으로 수행할 검증을 기술하며 관측된 PASS를 선언하지 않는다.

공유 control의 마지막 설계는 `CONTROL_PLAN.json`이다. root의 동결 manifest 경로는 `verification/FROZEN_FILES.json`이고 `{schema,created_utc,files:[{path,bytes,sha256}],scope,...}` 구조다. root wrapper가 실행 전 전 항목을 검증한다. reference는 이를 기록하고 자신의 코드·입력·primary의 hash를 확인하며, production 구현을 열어 독립성을 훼손하거나 manifest를 덮어쓰지 않는다.

입력은 원래 소스 셀마다 주어진 비음수 유리수 Bernstein-B3 계수 네 개이다. 이는 명시적으로 공급된 계수 원뿔이며 모든 비음수 3차 다항식에 대한 입력 정리가 아니다. 전역 기억은 원래 `t0`에서 시작한다. `h(0)=1`은 `q=0`에서도 유지한다. `d`는 부호를 유지하는 비교식의 `d_c`이고, `c>=0`은 비교 결합계수이다. `E=abs(eta)` 및 coarse l1=`4E`를 유지한다.

source/state/clock/full-A 인증 항목의 일치는 산술 입력의 결합 검사이다. 실제 HD 배열, 명명된 physical consumer/state/density/clock의 충분한 출처가 확보되었다는 뜻으로 바꾸지 않는다. `INPUT_PENDING`, `MISSING_NOT_ZERO`, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`, central/physical delta=0의 현재 범위는 이 reference가 바꾸지 않는다.

## 2. 원래 소스 적분으로 R을 다시 계산

원래 소스 셀을 `[a,b]`, 길이를 `ell=b-a`, 정규화 좌표를 `x=(s-a)/ell`이라 하자. 입력 B3 계수를 `b0,b1,b2,b3`라 쓰면 독립 power 계수는

\[
\begin{aligned}
a_0&=b_0,\\
a_1&=3(b_1-b_0),\\
a_2&=3(b_0-2b_1+b_2),\\
a_3&=-b_0+3b_1-3b_2+b_3.
\end{aligned}
\]

kernel age strip `k`에서 움직이는 정확한 겹침 끝점은

\[
L=\max(a,t-(k+1)\tau),\qquad U=\min(b,t-k\tau)
\]

이다. `U<=L`이면 해당 적분은 0이다. 양의 겹침에는 원래 소스의 원시함수를 직접 적용한다.

\[
J_m(L,U)=\frac{\ell}{m+1}
\left[\left(\frac{U-a}{\ell}\right)^{m+1}
-\left(\frac{L-a}{\ell}\right)^{m+1}\right],\qquad m=0,1,2,3.
\]

\[
F(t)=\sum_{j,k}q^k\sum_{m=0}^{3}a_{jm}J_m(L_{jk},U_{jk}),
\qquad R(t)=h(t-t_0)R_0+F(t).
\]

`k=0..B`, `B=floor((T-t0)/tau)`를 사용하고, 실제 빈 겹침은 정확히 0으로 처리한다. `q=0`에서는 `k=0`의 가중치만 1이다. 소스 원시함수 경로에는 Simpson 공식, production의 Bernstein overlap 곱, production cell 계수가 들어가지 않는다.

이 문서의 `J_m(L,U)`는 source-local power primitive를 뜻한다. R4의 age-moment `J_ell(x)=integral v^ell*h(v)dv`와는 같은 convolution을 다른 변수로 적분한 동치 경로이다. 구현은 여기 고정한 움직이는 overlap 끝점의 원래 소스 원시함수 경로 하나를 사용한다.

base clock은 관측 knot와 원래 source knot의 `k*tau` 이동점 중 `[t0,T]` 안의 정확한 유리수 합집합으로 다시 만든다. `source_knots`에 `t0`가 있으므로 초기 kernel jump도 포함한다. 과거 source의 age를 새 셀에서 0으로 되돌리지 않는다. root subdivision의 중간점은 이 clock에 추가하지 않는다.

## 3. 정확한 독립 quartic과 일방향 끝점

각 base cell `[alpha,beta]`에서 `u=(t-alpha)/(beta-alpha)`를 사용한다. 다섯 **내부** 좌표

\[
u=1/6,\ 2/6,\ 3/6,\ 4/6,\ 5/6
\]

에서 제2절의 원래 적분을 유리수로 평가하고, 독립 Lagrange 또는 Newton 다항식 연산으로 차수 4 이하의 `P(u)`를 재구성한다. exact event clock 안에서는 각 겹침 끝점의 affine branch가 고정되므로 원시함수의 차수는 4 이하이다. 따라서 이 다섯 값은 셀의 다항식을 결정한다. 별도의 고정 좌표 `1/7,2/7,4/7,6/7`에서도 원래 적분과 `P`의 exact 일치를 확인한다. 이는 부동소수점 보간이 아니다.

초기 staircase는 셀 내부에서 일정하다. 따라서 `P(0)`은 왼쪽의 실제 right-continuous 값이고 `P(1)`은 오른쪽의 **left limit**이다. 실제 오른쪽 값 `R(beta)`는 제2절의 global kernel로 따로 다시 계산한다. 특히 `q=0`의 최초 block 끝에서 `P(1)`과 `R(beta)`를 혼동하지 않는다. 연속 convolution의 두 셀 경계값은 일치해야 하며, 초기항의 하향 jump만 별도로 허용한다.

원래 소스의 `g_e`도 그 셀의 power cubic을 affine 합성하여 직접 제한한다. `f(u)=cP(u)+g_e(alpha+Delta*u)`의 power quartic을 만든다. production이 보고한 power/B4/B3 계수는 독립 `P,g_e,f`와 exact 항등식으로 비교할 대상이다. 그 값을 reference 다항식의 입력으로 재사용하지 않는다.

## 4. 모든 셀의 exact supremum upper 판정

### 4.1 비음수 판정 보조정리

유리수 다항식 `Q`의 차수가 4 이하일 때 `[0,1]`에서 `Q>=0`인지 다음 순서로 정확히 판정한다.

1. 영 다항식과 상수를 먼저 처리한다.
2. `Q`의 monic 부분에 대해 유리수 gcd와 squarefree 분해를 시행한다. `Q`의 원래 부호/상수배는 최종 값 판정에 보존한다.
3. 홀수 중복도의 squarefree 인수만 곱하여 `O`를 만든다. `O`의 0과 1의 근은 제거한 후 열린 구간 `(0,1)`의 근 수를 Sturm variation 차로 센다.
4. 홀수 중복도 내부 근이 하나라도 있으면 부호가 그 근을 가로질러 바뀌므로 `Q>=0`은 거짓이다.
5. 그런 근이 없으면 모든 근이 아닌 내부점에서 부호가 같다. 고정 좌표 `1/6,2/6,3/6,4/6,5/6` 중 처음으로 `Q!=0`인 값을 택한다. 0이 아닌 차수 4 이하 다항식에는 서로 다른 5개의 근이 없으므로 반드시 하나가 존재한다. 그 부호와 양 끝점의 부호를 확인한다.

이 판정은 simple/repeated/triple/quadruple root와 임의로 가까운 근에 적용된다. 근 간격이나 임계값의 Decimal 근삿값을 전제로 하지 않는다. 영 다항식이 아닌데 다섯 probe가 모두 0이면 reference 구현의 불일치로 기록한다.

### 4.2 독립 upper와 lower

보고된 base-cell exact upper를 `U_R`라 할 때 독립 원래 적분에서 만든 `P`에 대해 `Q=U_R-P`를 위 보조정리로 판정한다. 동시에 실제 오른쪽 값도 `R(beta)<=U_R`인지 exact 비교한다. 둘이 성립하면 닫힌 셀의 supremum upper이다.

lower는 production leaf의 rational 끝점 및 DEPTH_LIMIT 중간점 위치에서 **독립 P를 다시 평가한 값**으로 검증한다. `u=1`은 left-limit witness로 표시한다. 실제 오른쪽 값도 별도 witness이다. 보고된 exact lower가 공유된 최대 witness 규칙과 일치하고 exact upper 이하인지 확인한다. 실제 점값과 left-limit의 supremum 증거를 서로 구분한다. 이 lower는 공급된 이상 비교함수의 supremum에 대한 lower이며 미지의 물리 오차의 lower로 해석하지 않는다.

### 4.3 partition과 gap

각 terminal leaf는 유리수 구간이고, 정렬했을 때 `[0,1]`을 빈틈이나 내부 중복 없이 덮어야 한다. 폭은 `2^-depth`, 시작점은 같은 dyadic grid에 있어야 한다. `nodes=2*splits+1`, `leaves=splits+1`, depth/split/node 한계를 exact 정수로 확인한다.

`NONDECREASING`과 `NONINCREASING`의 도함수 부호는 production variation 알고리즘을 재현하지 않고 제4.1절의 비음수 판정으로 독립 검증한다. `CONSTANT`는 독립 제한 다항식의 도함수가 정확히 0인 경우다. DEPTH_LIMIT leaf는 깊이 96, 폭 `2^-96`, 지정 중간점과 독립 평가값을 가져야 한다. 해당 leaf의 B4는 독립 power 다항식을 그 leaf에 affine 합성한 뒤 own power-to-Bernstein 변환으로 exact 비교한다. 이 기저 변환은 production의 subdivision 알고리즘을 호출하지 않는다. leaf별 upper의 유효성은 원래 `P`의 부호 판정에 이미 포함되며, leaf별 최대값 규칙도 별도 exact 확인한다.

모든 단조 leaf는 독립 도함수 부호 검증으로 내부 부호변화가 없음을 확인한다. boundary root는 leaf의 공유 끝점으로 허용한다. DEPTH_LIMIT leaf를 1근 isolating box로 해석하지 않는다. 따라서 반복근이나 경계근을 버리지 않는다.

독립 B4에서 `M_B=4*max|B[i+1]-B[i]|`, `Cmax=max B`를 재계산하고 다음을 exact 비교한다.

\[
0\le U_R-L_R\le M_B2^{-96}\le4C_{\max}2^{-96}.
\]

마지막 부등식의 입력 범위는 비음수 model B4이다. 독립 component control이 signed coefficient를 허용하도록 별도 선언되면 그 경우에는 `M_B` bound까지만 적용하고 `4Cmax`를 무조건 적용하지 않는다. 모든 dyadic enclosure는 exact 값에 대한 outward 방향과 분모 grid 및 합계 `2*2^-128` 이내의 rounding overhead를 확인한다.

관측 셀은 그 안에 들어 있는 base cell의 `exact_lower`, `exact_upper`, `M_B`, `Cmax`, `proved_gap_bound`를 각각 최대값으로 집계한다. gap은 집계 upper−lower이다. 집계 upper−lower는 최대 child gap보다 크지 않으므로 최대 child gap bound가 유효하다. duration이 다른 셀도 각자의 정규화 계수에 이미 duration을 반영한다.

## 5. 독립 critical-root 진단

제4절이 모든 model cell의 upper를 exact 인증한다. 근 격리는 다음 고정 7개 입력의 `[1,2]` 셀에서 root arrangement를 추가로 검증한다.

| Case ID | 사전 지정 구조 |
|---|---|
| ROOT_THREE_RATIONAL | 서로 다른 유리 내부근 3개 |
| ROOT_THREE_MIXED_ALGEBRAIC | 유리 내부근 1개와 비유리 내부근 2개 |
| ROOT_SIMPLE_DOUBLE | 단순근 1개와 중근 1개 |
| ROOT_TRIPLE | 삼중근 1개 |
| ROOT_ENDPOINT_INTERIOR | 0, 1의 끝점근과 내부근 1개 |
| ROOTLESS_MIXED_COEFFICIENTS | 도함수의 혼합 부호 계수에도 내부 실근 없음 |
| ROOT_CONSTANT | 도함수 항등 0 |

이들은 모두 실제 model 입력으로 도달하는 제어이다. `q=0,tau=1`, source `[0,1,2]`, 첫 source `g_r=M`, 둘째 `g_r=M+p(u)`로 구성하면 `[1,2]`에서 독립 적분의 도함수가 `p(u)`가 된다. shared fixture의 구체 B3와 rational final R/E 값은 실행 전 설계 target이며, 독립 원시함수 실행이 이를 검증할 때까지 관측 결과로 부르지 않는다.

도함수 `D=P'`의 중복도를 exact squarefree decomposition으로 찾는다. 0/1의 근을 별도로 기록하고, squarefree 부분의 Sturm chain으로 열린 구간 root count를 구한다. `S0=sf(D)`, `S1=S0'`, 이후 `Snext=-remainder`이다. variation에서 정확한 0은 삭제한다. chain의 한 항만 임의의 음수배로 정규화하지 않는다.

유리 이분법은 최대 깊이 320으로 제한한다. 중간점이 exact root이면 point root로 기록하고 나머지 열린 구간을 정확하게 센다. 깊이 320에서 root count가 2 이상인 구간은 **count가 있는 unresolved cluster**로 보존한다. 그런 경우 근 분리를 성공했다고 쓰지 않는다. 전체 distinct root count와 분해 중복도 및 boundary 분배가 보존되어야 한다.

각 root interval/cluster의 `P` 값은 자체 power Horner interval 연산으로 둘러싸고 끝점 값과 함께 극값 진단에 기록한다. 참고 Decimal 값은 interval 중간점에서만 계산하며 exact 상한 판정을 대신하지 않는다. 진단의 root count, 중복도, interval inclusion 및 완전성은 exact 항목이다. 이미 exact 부호 판정이 완료된 셀에 root isolation을 반복 적용하여 예산을 소비하지 않는다.

### 5.1 고정 depth sweep의 독립 확인

primary의 같은 단일 campaign에는 `ROOT_THREE_RATIONAL`과 `ROOT_THREE_MIXED_ALGEBRAIC`의 두 번째 셀에 대해 `D=0,4,8,16,32,64,96`의 14개 진단이 포함된다. public model API의 depth는 계속 96이다. reference는 `checks[]`의 `kind=DEPTH_SWEEP` record에 있는 B4가 자기 원래 적분의 `P`와 같은지 먼저 확인한다. 각 row의 upper에 대해 `U-P>=0`를 exact 판정하고 `gap=U-L<=M_B*2^-D`, `splits<=3D`, `nodes=2*splits+1<=6D+1`을 확인한다.

이 축약 row에는 leaf witness list가 없으므로 lower는 별도의 exact 존재 판정으로 확인한다. `H=P-L`에 대해 양 끝점 또는 고정 probe 중 하나가 비음수이면 lower가 유효하다. 그렇지 않아도 squarefree `H`가 `(0,1)`에 근을 가지면 그 근의 값이 0이므로 lower가 유효하다. 내부근이 없고 모든 검사점이 음수이면 lower는 거짓이다. 영/상수 다항식은 먼저 처리한다. 이는 rational witness 위치를 새로 추정하거나 전체 dyadic grid를 열거하지 않고 `sup(P)>=L`을 결정한다. 이 진단도 exact 항목이며 Decimal guard를 사용하지 않는다.

## 6. 독립 E endpoint와 moment 교차 확인

`Delta=beta-alpha`, `z=d*Delta`, `f(u)=sum(m=0..4) f_m*u^m`라 하자. 원래 power forcing에서

\[
E_\mathrm{right}=e^zE_\mathrm{left}
+\Delta\sum_{m=0}^{4}f_m m!\,\phi_{m+1}(z),
\qquad
\phi_k(z)=\sum_{j=0}^{\infty}\frac{z^j}{(j+k)!}
\]

를 계산한다. Decimal precision은 160으로 고정한다. `exp(z)`는 Decimal의 exp로 계산하고, `phi1..phi5`는 monomial series의 `j=0..511` 고정 512항으로 계산한다. `|z|<=16`에서 이론적 절단항은 `16^512/(512+k)!` 이후 비율 `<=16/(513+k)`의 기하 bound로 제어된다. 이 절단 분석은 Decimal 연산을 interval 산술로 바꾸지 않는다. 특히 작은 z에서 반복 나눗셈 recurrence를 사용하지 않아 차감 손실을 피한다. 부호가 음수인 z에서도 원래 series를 그대로 계산한다.

위 `f_m`는 정규화된 u의 계수이므로 앞의 시간 계수는 정확히 `Delta` 한 번이다. elapsed physical time의 power 계수를 사용할 때만 `Delta^(m+1)`이 나타난다. 두 좌표계를 혼합하지 않는다. `SIGNED_DOMAIN_POS16`, `SIGNED_DOMAIN_NEG16`은 `z=+16,-16`에서 이 fixed 경로를 검증한다.

`d=0`은 별도 exact rational 경로를 둔다.

\[
E_\mathrm{right}=E_\mathrm{left}
+\Delta\sum_{m=0}^4\frac{f_m}{m+1}.
\]

이는 tolerance 없는 exact endpoint 검사이며 공유된 exact cubic control target도 이 경로와 원래 적분으로 검증한다. 초기 E에서 시작하여 **base cell만** 순차 전파하고 각 관측 endpoint를 이 계산에서 선택한다.

production의 `exp`, `phi`, `W0..W4` interval도 독립적으로 비교한다. B4 basis의 monomial 식을 자체 전개하여 각 moment를 같은 `phi1..phi5`로 계산한다. `z=0`에서는 `W_i=Delta/5`, `phi=Delta`, `exp=1`을 exact 확인한다. 여기서 API의 `phi`는 `Delta*phi1(z)`를 뜻한다.

모든 Decimal interval membership에 사용할 guard는 실행 전 고정한다.

\[
\varepsilon=10^{-80}\max(1,|v_\mathrm{ref}|,|lo|,|hi|).
\]

엄격한 `lo<=v_ref<=hi` 위반 수와 최초 50개 예시는 guard 허용 여부와 상관없이 보존한다. guarded membership 결과는 별도 계수와 예시로 기록한다. 정밀도·guard를 관측 결과에 따라 늘리지 않는다. 이 부분의 증거명은 `GUARDED_CORROBORATION_NOT_INTERVAL_REFERENCE`이다. exact 항등식·부호·분할·정수 검사에 이 guard를 적용하지 않는다.

## 7. whole E의 의미와 검증

whole-cell lower/upper는 **supremum**을 둘러싼다. lower는 해당 셀 왼쪽/오른쪽 endpoint lower의 최대값이다. 이 값을 모든 내부 시점의 pointwise lower로 해석하지 않는다.

보고된 `Qmax=c*Rsup_upper+max(restricted geB3)`는 독립 제한 `g_e` 및 이미 exact 검증한 `Rsup_upper`에서 다시 계산한다. 또한 독립 power forcing에 대해 `Qmax-f(u)>=0`를 제4.1절의 exact 판정으로 확인한다. majorant의 시작값은 left E **upper**이다. 부호 있는 같은 d로

\[
Z(\Delta)=e^{d\Delta}E_{\mathrm{left,upper}}
+\Delta\phi_1(d\Delta)Q_{\max}
\]

를 독립 Decimal로 계산한다. constant-forcing 해의 도함수는 일정한 부호를 가지므로 `max(Eleft_upper,Z(Delta))`가 전체 셀을 덮는다. 공유 record의 `Qmax,left_E_upper,right_majorant_upper`와 upper 구성 규칙을 exact 구조 검사 및 고정 guarded numeric membership으로 나누어 확인한다. 다음 셀은 이 majorant endpoint가 아니라 별도로 계산한 실제 polynomial-forcing endpoint interval에서 전파되어야 한다.

`d=0`에서는 입력 forcing이 비음수이므로 E는 비감소이고 exact endpoint가 whole supremum이다. 이 경우 reference exact 값과 reported whole enclosure를 tolerance 없이 비교한다. 부호 있는 일반 d에서는 E 자체가 단조라고 가정하지 않는다.

## 8. 유리수 크기 제한과 실패 분류

세 종류의 제한을 분리한다.

| 대상 | 제한 | 의미 |
|---|---:|---|
| 원래 입력 rational | 256 bits / 성분, 2048 문자 | ASCII 정수 또는 signed p/q; bool/float/공백/decimal/exponent 배제 |
| 저장된 production derived rational | 16384 bits / 성분, 10000 문자 | canonical reduced 정수 또는 p/q; denominator 양수 |
| reference 내부 미저장 exact Euclid/Sturm rational | 1048576 bits / 성분 | root가 승인한 사전 arithmetic clarification; 입력 또는 저장 출력 한도를 바꾸지 않음 |

프로세스는 JSON parsing과 serialization 전에 integer decimal digit limit을 6000으로 설정한다. primary의 derived rational에 입력용 2048 문자/256 bit guard를 적용하지 않는다. 내부 1048576-bit 객체를 giant decimal string으로 저장하지 않는다. coefficient별 관측 최대 numerator/denominator bit length와 연산 수는 작은 정수 통계로 저장한다.

degree<=4, polynomial long division 최대 5번의 coefficient 제거, 한 gcd/Sturm chain 최대 5번의 division, squarefree multiplicity loop 최대 4회, Sturm chain 최대 5개 다항식으로 제한한다. 각 helper의 반환 coefficient와 연산 경계에서 내부 bit cap을 확인한다. cap 위반은 `REFERENCE_ARITHMETIC_CAP_EXCEEDED`로 unresolved/ref FAIL에 포함하고 case를 삭제하지 않는다. 순간 정수 곱은 유한 두 operand 크기로 제한되며, 최종 memory/CPU/wall 보호는 root wrapper가 담당한다.

source 부재, schema 불일치, exact 수학 불일치, guarded Decimal 불일치, arithmetic cap, wall/CPU/memory 종료를 별도 실패 범주로 기록한다. 실제 실패를 보존하고 원인을 고친 경우에만 root가 동일 수용 기준의 reference repair reserve 1회를 사용할 수 있다. 실패 후 tolerance 변경, 실패 case 삭제, fixture target 갱신은 허용하지 않는다.

## 9. C4로 넘기는 실행 경계

예정 CLI는 `verification/run_reference.py --root ABS_LEAF --output ABS_OUTPUT`이다. root가 동결된 입력과 primary 원시 결과를 제공한 뒤, imports·JSON 읽기·연산·serialization 전체를 포함하여 CPU 180초, wall 240초, memory 1GiB의 reference campaign 1회를 실행한다. 사용 라이브러리는 Python 표준 라이브러리로 제한한다. production module을 import하지 않는다.

현재 고정 control 계획은 full model 21개, 예상 합계 base cell 75개, overlap precharge 합계 4811이다. standalone extrema fixture는 0개이고, 위 14개 depth-sweep row는 두 실제 model cell의 별도 진단이다. 이는 실행 전 설계 개수이며 실제 실행 측정은 별도 raw에 남긴다. freeze 전에 `CASES.json`의 exact ID 집합과 hashes를 매핑한다. 모든 model의 exact 검증과 정해진 7개 root 진단, 14개 depth 진단, scalar 비교를 한 campaign에 포함한다. C5 코드 작성과 C6 이후 실행은 이 문서 전달 후 root의 다음 작업 지시에 따른다.

## 10. 근거와 작성 중 읽은 문서

- R15 canonical `CONTRACT.json`: objective, input/derived caps, budget, fixed Decimal guard, 물리 범위.
- 현재 `AGENTS.md` R15 preamble: 새 unit 허가, inherited DAG 보존, root의 실행·게시 소유권.
- shared `API_SCHEMA.md`, `INPUT_SCHEMA.json`, `OUTPUT_SCHEMA.json`, `API_MAP.json`: original clock, exact record, actual endpoint/left limit, partition 및 supremum 의미. 구현 파일은 읽지 않았다.
- shared `CONTROL_PLAN.json`: 실행 전 21개 model, 75개 base cell, 4811 overlap precharge, 두 signed-domain boundary와 7개 root-pattern의 고정 목표.
- `R3_CLAIM_LEDGER.json`: conditional full-A premise, B3 input cone, 새 proof obligations와 미실행 상태.
- `R4_CONSTRUCTION_CHOICES_KO.md`: source/age primitive의 동치 및 normalized-u/elapsed-time phi 시간 인자의 구분.
- `physmath-research-loop` cloud c38의 SKILL, POLICY_INTEGRATION, THEORY_LOOP, CODING_LOOP, RESEARCH_POLICY, EVIDENCE_AND_HANDOFF: C3/C4 순서, 근거 분리, 유한 실행, 실제 실패 보존, root 게시·인계.

위 식·보조정리·알고리즘 설계는 실행 전 직접 추론이다. CAS 또는 numerical run의 결과로 표현하지 않는다.
