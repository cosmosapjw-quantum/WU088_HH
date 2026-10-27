# R6 production code 독립 정적 심사

## 현재 판정

**PASS_STATIC_PREEXECUTION_SCOPED.** Production core의 enclosure 방향과 비교계 산술에서 blocking 오류를 발견하지 않았다. 입력 계약의 실제 guard 누락 두 건 F01/F02를 발견하여 root에 즉시 전달했고, root가 수정한 파일을 다시 읽어 **정적으로 닫았다**.

**최종 C9는 아직 PENDING**이다. 실제 primary/reference 결과를 보지 않았으며, guard test나 수치 결과를 실행 성공으로 표시하지 않는다. 필요한 S05 게시 이후의 계약된 단 한 번 primary에서 두 수정의 실제 rejection이 기록되어야 한다.

검토자는 production core, primary runner, independent reference를 작성하지 않았다. 코어 import, 수치 테스트, CAS, IVP, 과거 suite 실행, 외부 쓰기를 모두 0으로 유지했다.

## 고정한 코드와 입력

| 자료 | SHA256 |
|---|---|
| Core `src/interval_block.py` | dbc4767b31775fb6655a92fb20d299f8bea9578f8340bd7bcff4d4f677cab551 |
| 원 runner | f714ef9bfa96351807911ac13b2524144c7fa52cd0f142bd23834f0edec2c246 |
| 수정 runner | 38cf5268831bbd3d2b17d356817ebae4b68f08e676da1e2cbf2cb313d7c6deb5 |
| PRIMARY_INPUT | 40c059e324783492254831ca110e8d7d9b5e644fd7565eb0c6ad1eab8f3f2f15 |
| 현재 CONTRACT | 1a034fcecd2056d400089e3aa5abe53e067ded5a7625b92970d72da15e9d41a8 |
| 독립 reference | 11650b677ebbd96f9bab9463d8b14d102185e233f402a26d8170fe3d6c1596a8 |

Core 전체, 원 runner 전체와 수정 부분, 고정 primary 입력, 현재 계약, independent reference를 읽었다. 기존 REC parser는 source identity/구조 검사와 entry-point 경계를 읽었으며 기존 diagnostics를 실행하지 않았다.

## F01 — native clock scale 선언이 검사되지 않음

**대상:** `Primary.source`.

원 runner는 source hash, native100K, collider2를 확인하지만 입력의 `rate_unit_cm3_s`를 읽어 검증하지 않았다. Core는 항상 \(10^{-11}\,\mathrm{cm^3/s}\)로 rates를 나누므로, 입력이 다른 clock scale을 선언해도 그 선언과 다른 generator를 만들 수 있었다.

현재 고정 입력은 원래 정확한 \(10^{-11}\)이므로 이 발견은 실행된 fixed-input 결과의 오염 증거가 아니다. 첫 과학 실행 전의 선언 계약 누락이다.

**최소 수정과 실제 readback:** native 계산 전에

\[
Q(\texttt{rate\_unit\_cm3\_s})=\texttt{RATE\_SCALE\_CM3\_S}
\]

를 요구하도록 수정했다. 잘못된 \(10^{-10}\) 선언의 reject control도 추가됐다. 수정 위치가 `native_hd_source` 호출 앞이므로 잘못된 scale에서 source 계산이 시작되지 않는다.

**상태:** CLOSED_STATIC_PENDING_RUNTIME_CONTROL.

## F02 — positive total H만으로는 switching clock이 유효하지 않음

**대상:** `Primary.switched`.

원 runner는 각 duration을 합한 \(H\)를 `finite_block`에 넘겼다. 각 segment duration의 양성은 검사하지 않아 \(-1/4,+3/4\)처럼 총시간은 양수지만 chronological Markov evolution이 아닌 입력을 primary control로 만들 수 있었다. 독립 reference는 이미 비양수 duration을 거부했다.

고정 입력의 두 duration은 모두 \(+1/4\)이므로 역시 예정 fixed-input의 수학값을 바꾸는 수리가 아니다.

**최소 수정과 실제 readback:** 모든 duration을 exact \(Q\)로 먼저 읽고, 비어 있지 않으며 각 값이 양수인 경우에만 generator를 구성한다. \(H\)는 그 검증된 목록에서 합산한다. 음수 segment·양수 총시간 reject control도 추가됐다.

**상태:** CLOSED_STATIC_PENDING_RUNTIME_CONTROL.

## Directed arithmetic 검토

### Exact 입력과 지수 enclosure

`Q`는 bool과 binary float를 거부한다. Integer, Fraction, bounded decimal/rational 문자열을 exact Fraction으로 해석한다. Decimal exponent와 입력 길이에 제한이 있고, denominator0·비유한 표현·복합 division을 거부한다. Degree, bit count와 state count는 정확한 built-in int만 받는다.

`floor_scaled`, `ceil_scaled`의 정수 나눗셈 방향은 맞다. 부호 있는 interval에도 floor/ceiling 정의가 유지된다. 지수 primitive는 \(y=z/2^s\le1/2\)로 줄이고, odd Taylor partial sum을 lower, 그 직전 even sum을 upper로 유지한다. Odd degree에서 정지하므로 두 sum의 대응이 맞다.

양의 반복 squaring에서 lower는 내리고 upper는 올린다. Upper를1로 줄이는 것은 \(e^{-z}\le1\)이라는 독립적인 전역 상한을 사용하므로 유효하다. Degree/precision/argument 범위가 제한되고, 유한 precision에서 lower가0이 될 수 있다는 사실 자체는 enclosure 오류가 아니다. Thermal normalization은 strict positive lower weight를 별도로 요구한다.

### Thermal literal, normalization과 source

정의상수는 exact Fraction이다. Source energy decimal, degeneracy, temperature를 binary64를 거치지 않고 사용한다. 모든 energy가 기준 준위 이상이고 \(g_i,T\)가 양수인지 검사한다.

Normalization은 own lower/other upper 및 own upper/other lower의 정확한 좌표 극값 공식을 구현한다. Pair ratio는 normalized pi box를 다시 나누지 않고 원 Gibbs energy gap에서 계산한다. 이는 서로 관련된 Gibbs weight와 rate를 수학적으로 같은 family에 묶는 방법이다.

Source와 parser의 고정 hash를 읽은 뒤 parser를 import한다. Parser는 level ID1..9, J, degeneracy, 증가 energy, 정확한 pair 순서, collider identity, native50/100/200K를 확인한다. 따라서 core의 level index와 pair ID 대응은 이 고정 source에서 정당하다. 호출된 entry point는 parsing이며 기존 REC diagnostic suite가 아니다.

적용은 native100K para-H2의 제공된9개 downward pair와 선언된 reverse closure다. 미제공 전이를 물리적0으로 승격하지 않는다.

## Generator family와 lower propagator

### Diagonal과 full A

`GeneratorBox`는 lower diagonal을 upper exit의 음수, upper diagonal을 lower exit의 음수로 요구한다. Off-diagonal box의 각 actual generator는 자신의 column sum이0인 diagonal을 갖는다는 의미를 유지한다.

`reset_generator_bounds`는 \(\pi\) box가 simplex point를 포함하는지, \(v_j^-\ge\kappa\ge0\)인지 검사한다. Full

\[
A=K+\pi(v-\kappa\mathbf1)^T-\operatorname{diag}(v-\kappa\mathbf1)
\]

의 off-diagonal bounds를 만들고 전체 exit를 다시 계산한다. Runner는 이 full \(A\)에서 \(\rho\)를 구한다.

\(\lambda\)는 full upper exit의 최댓값을 지배한다. Explicit undersized rate는 거부되고, zero generator에는 양수1을 사용한다. \(P_-\)의 비음수성과 column-substochasticity를 직접 검사한다.

### Dyadic matrix powers와 Poisson weights

실제 계산은 exact \(P_-\)를 다시 아래쪽 dyadic \(P_d\)로 내린다. 정수 matrix product의 각 dot product를 scale로 나눈 뒤 floor하므로

\[
D_m\le P_-^m\Longrightarrow
\operatorname{floor}_{\rm dyadic}(D_mP_d)\le P_-^{m+1}
\]

가 성립한다. 오른쪽 곱을 사용해도 이 귀납은 타당하다. 시간가변 actual matrices의 가환성을 가정하는 논증이 아니다.

초기 Poisson weight는 lower \(e^{-\mu}\)이고, recurrence는

\[
w_{m+1}=\left\lfloor w_m\frac{\mu}{m+1}\right\rfloor
\]

이다. \(\mu/(m+1)>1\)인 초기 구간에서도 양수 곱의 단조성 때문에 lower 방향이 보존된다. 각 matrix-weight 항도 아래쪽 반올림하고 양의 항을 합산한다. Omitted tail을0으로 버리는 방향이 맞다.

Min-pair overlap을 정수로 계산한 뒤 \(\rho=1-\beta\)를 정확하게 반환한다. Column mass가1을 넘지 않는지도 검사한다. \(\beta\)는 lower, \(\rho\)는 upper이다.

### n=1

Singleton에서 반환되는 \(\beta=1,\rho=0\)은 \(Z=\{0\}\)에 대한 명시적 convention이다. Finite truncated scalar \(R_N\)의 mass가 정확히1이라는 뜻은 아니다. Export가 `n1_zero_sum_convention`으로 이 범위를 표시한다. \(n>1\)의 disconnected zero graph는 서로 다른 column overlap이0이라 수축을 주장하지 않는다.

## Forced bounds와 serialization

`forced_step`은 비음수 state, damping, forcing/coupling bounds와 \(0\le\rho\le1\)을 검사한다. Full-block endpoint와 whole-block object를 별도로 반환한다.

\[
G=q(M+FH)+g,\qquad
\int_0^H U(\tau)\,d\tau\le HU+\frac12GH^2
\]

를 사용하여 \(E\)의 source를 적분한다. 감소한 endpoint \(U_+\)를 구간 적분의 대체값으로 사용하지 않는다. Common killing은 residual endpoint의 \(1+\kappa H\)에 한 번 적용된다.

Constant fixture coefficients의 \(K\pi-v\pi+\pi\bar v\), \(Qf\), \(\min v,\bar v,\operatorname{osc}(v)/2\)는 accepted constant finite model과 일치한다. 세 synthetic fixture의 physical-input 상태를 source graph와 구별한다.

정수 parser/formatter는 chunk를 사용해 Python의4300-digit 기본 decimal 변환 제한을 우회하되 전역 설정을 바꾸지 않는다. Fraction은 exact rational string으로 serialize된다. 현재 선언된 source/fixture payload에 대한 경로를 검토한 것이며 임의의 무한 크기 데이터에 대한 reference parser 성능·완전성을 주장하지 않는다.

## Independent reference와 최종 C9 조건

Independent reference는 production module을 import하지 않는다. Source parser와 Decimal250 exponential path가 별도이며, numerical values를 formal outward proof라고 부르지 않는다. SciPy로 constant source, chronological switching product, full-A common-killing split과 augmented forced system을 비교한다.

Within-block quarter samples는 유용한 numerical check이지만 continuous-time supremum의 증명은 아니다. 좁은 interval이 Decimal precision에서 해상되지 않으면 별도 resolution label을 남긴다. Root의 general-n proof와 exact directed arithmetic 심사가 그 numerical observation과 분리되어야 한다.

실제 primary/reference 뒤의 최종 C9는 다음을 읽어야 한다.

1. 실제 실행 source/input/core/runner hash가 수용한 version과 일치하는지.
2. F01/F02가 한 번의 primary에서 실제 DomainError reject로 기록됐는지.
3. 전체 check/failure 기록과 positive source overlap, forcing/source scope가 보존됐는지.
4. Reference가 실제 saved primary를 읽고 mismatch/resource flag를 보고했는지.
5. Numerical PASS와 resource 조건을 별도로 만족하는지.

58CPU-second interrupt와60-second resource flag는 준비됐지만 실행된 자원 수치를 대체하지 않는다. Finalize 시점 측정과 serialization 이후 전체 wrapper 비용도 구별해야 한다. Exit0만으로 resource 성공을 선언하지 않는다.

## 경계

Caller-supplied interval bounds의 물리적 진실성이나 \(\rho\)의 올바른 provider binding을 일반 함수가 자동으로 입증하지는 않는다. 이번 primary는 같은 full \(A,H\)에서 certificate를 만들고 사용한다. 실제 GL2022 destruction과 molecular consumer는 계속 UNBOUND다.

본 정적 심사는 root의 수정 두 건을 readback하여 실행 준비 상태를 확인한 것이며, 아직 실행되지 않은 시험·수치 값·최종 C9를 완료로 세지 않는다.

