# R12 정확한 비정렬 forcing convolution 구현 설계

이 문서는 `WU_NONALIGNED_CONVOLUTION_R12`의 실행 전 구현 계약과 출력 해석을 고정한다. 계산 영역과 과학 전제의 권위는 [CONTRACT.json](CONTRACT.json)이며, 이 문서 작성 시점에는 새 primary/reference/CAS 실행을 하지 않았다. AST 구문 검사와 원본 함수 본문의 byte/AST 비교는 과학 실행과 구별한다. 실제 실행·시간·성공 여부는 이후 root가 작성하는 `raw/PRIMARY_RESULTS.json`, process 기록과 실행 ledger에 따른다.

## 1. 구현 범위와 기존 근거

새 구현은 정확한 유리수 source/observation 격자에서 나이별 kernel의 forcing convolution을 계산하고, 그 경계를 명시적으로 분할하여 signed scalar 비교식을 적분한다. 고정된 R11 full-A의 `q`, `tau`와 동일한 source/family/state/clock 전제를 재사용한다. Nominal K의 수축률을 full A로 직접 옮기거나, generator·행렬지수·ODE·기존 primary/reference를 다시 계산하지 않는다.

`saved_case_sweep`는 다음 실제 파일의 원본 bytes를 요구한다.

- R11 결과: `research/provider_registry_molecular_r11_20261028/raw/PRIMARY_RESULTS.json`
- 고정 SHA-256: `80ed0f8df5c785e47ce737acb8b029485db54b543d57498bf182427093f29b1b`
- R11 산술 원본: `research/provider_registry_molecular_r11_20261028/src/full_generator_blocks.py`
- 산술 원본 SHA-256: `c3720dcc9b4e79e7d44eaa16c420a1a9b0d29d141be2fd994cc77c779cc9fa0f`

`src/positive_arithmetic.py`의 12개 순수 함수는 R11 본문을 그대로 복사했다. 대상은 `Q`, `_positive`, `_ceil`, `_floor_scaled`, `_ceil_scaled`, `down`, `up`, `_tail`, `_positive_series`, `_exp_fraction`, `exp_interval`, `bernstein_weights`다. 원본 파일을 import하지 않는다. 단일 primary는 원본과 복사 함수의 AST를 비교하고, 두 원본 파일의 실제 SHA와 preexecution freeze membership을 확인한다.

R11이 보존한 Native9은 native K와 synthetic conditional reaction의 결합 fixture다. 이 구현은 actual HD reactive array 또는 named physical consumer/density/clock을 새로 결속하지 않는다. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`, physical/central delta=0, `native_v=UNSPECIFIED`, `MISSING_NOT_ZERO`, TIQM/SQM 구별이 유지된다.

## 2. 공개 API와 명시적 전제

```python
nonaligned_sweep(
    q, tau, c, d, g_r, g_e, source_knots, observation_knots, initial,
    *, binding, certificate, cap_source_bytes=None, cap_case_id=None,
    bits=128, degree=96,
)

saved_case_sweep(r11_source_bytes, case_id, grid_variant="aligned")
```

일반 산술 API는 `binding`과 `certificate`를 별도로 받는다. `binding`에는 family ID, clock, source SHA, `l1_on_kerP` norm 및 순서가 있는 고유 state ID가 있어야 한다. certificate의 q/tau와 binding은 산술 입력과 정확히 같아야 하며, validity interval은 전체 `[t0,T]`를 포함해야 한다. `uniform_all_starts`, `same_family_composition`, `remainder_l1_nonexpansive`, `zero_mass_forcing`, `whole_domain_forcing`은 명시적으로 true여야 한다.

이 metadata 검사는 선언한 전제의 결속을 확인한다. 일반 API가 외부 certificate의 과학적 타당성을 새로 증명한다는 뜻은 아니다. 실제 saved-case wrapper만 고정한 원본 bytes와 case를 직접 검증하며, R11에서 이미 채택한 조건부 certificate를 가져온다. 산술 control의 status는 `ARITHMETIC_CONTROL_PREMISE`다. 특히 q=0 control은 kernel 산술의 경계 사례이며 어떤 유한 CTMC의 정확한 실현 가능성을 주장하지 않는다.

수학적 전제는 다음과 같다. 동일한 full-A family의 모든 허용 경로와 시작시각에 대해 길이 tau의 zero-mass l1 propagator norm이 q 이하이며, 나머지 시간 구간에는 Markov l1 nonexpansiveness가 적용된다. `g_r`, `g_e`는 선언한 source cell 전체에서 유효한 비음수 forcing bound이고, residual forcing의 질량합은 0이다. `c>=0`, signed `d`는 sweep 전체에서 고정된다. `R0>=0`, `E0>=0`이고 `E=abs(eta)`, coarse l1=`4E`다. 초기 시각은 일반 control에서 음수 유리수도 가능하다.

## 3. 정확한 overlap과 전체 경계 분할

`h(u)=q**floor(u/tau)`, `h(0)=1`, `0**0=1`로 정의한다. source cell `[a_j,a_(j+1)]`의 forcing이 일정할 때 다음 양의 overlap 합을 `Fraction`으로 정확히 계산한다.

\[
 F(t)=\sum_j g_{r,j}\sum_{k=0}^{\lfloor(T-t_0)/\tau\rfloor}
 q^k\max\{0,\min(a_{j+1},t-k\tau)-\max(a_j,t-(k+1)\tau)\}.
\]

kernel powers, 각 overlap 길이, `F(t)`와 `R(t)=h(t-t0)R0+F(t)`는 반올림하지 않는다. 입력 q의 dyadic upper 자체를 고정한 비교계의 유리수로 사용한다. 그 q 이전에 있던 이상적 최적 수축률이나 실제 물리 오차의 lower를 계산하지 않는다.

refined grid는 observation knots, source knots, `t0+k*tau`, 모든 `a_j+k*tau`, cap source의 old knots의 합집합이다. 범위 밖 경계는 제외하고 정확히 같은 유리수만 합친다. 단순히 `t0+k*tau`만 넣으면 비정렬 source의 이동 경계를 놓치므로, 모든 source knot를 이동시킨 경계를 포함한다.

각 refined segment `[b_i,b_(i+1)]`의 내부에서는

\[
 L_i=h(b_i-t_0)R_0+F(b_i),\qquad
 V_i=h(b_i-t_0)R_0+F(b_{i+1})
\]

를 잇는 affine 함수가 R 비교값이다. `V_i`는 **셀의 오른쪽 끝점에 왼쪽에서 접근한 극한**이다. 그 끝점에서 kernel이 내려가면 실제 point 값 `R(b_(i+1))`은 V와 다르다. whole-cell R은 `max(L_i,V_i,R(b_(i+1)))`를 포함한다. 새 cell마다 초기 R이나 forcing의 나이를 다시 시작하지 않는다.

## 4. Signed E 적분과 양의 산술

길이 `Delta=b_(i+1)-b_i`에 대해 raw E는

\[
 E_{i+1}=e^{d\Delta}E_i+
 c(W_0 L_i+W_1 V_i)+(W_0+W_1)g_{e,j}
\]

를 outward dyadic128 구간으로 계산한다. 여기서 j는 해당 segment 전체를 포함하는 source cell이다. `x=d*Delta>=0`이면

\[
 W_0=\Delta\sum_{k\ge0}\frac{x^k}{k!(k+2)},\qquad
 W_1=\Delta\sum_{k\ge0}\frac{x^k}{k!(k+1)(k+2)}.
\]

`x<0`에서는 양수 `-x`의 series를 사용하고 두 weight를 바꾼 뒤 `exp(x)`를 곱한다. `d=0`은 두 weight가 `Delta/2`, 그 합이 Delta인 연속 극한이다. Taylor96과 기하급수 tail majorant는 R11 산술과 같다. 음수 exponent는 양수 exp enclosure의 reciprocal로 감싼다. 모든 곱의 계수가 비음수이므로 lower/upper를 각각 전파할 수 있다.

`g_r`와 `g_e`의 source cell 위치는 source knot의 오른쪽 값을 사용하되, 유한 개 끝점의 forcing 정의는 적분을 바꾸지 않는다. Whole-cell 인증은 source cell 전체의 forcing 가정을 요구한다. raw E whole upper는 왼쪽 E upper, 오른쪽 affine 적분 upper, 같은 segment의 R whole upper를 상수 forcing으로 사용한 끝점 upper의 최댓값이다. 상수 forcing의 signed scalar 해는 segment에서 단조이므로 이 끝점 최댓값은 전체 segment를 감싼다.

R12 공개 API의 exact scalar 입력 한도는 1024 bits다. 복사한 내부 산술 helper의 원래 8192-bit 변환 guard는 그대로 두었다. 이는 입력 유리수의 차·합으로 생기는 derived segment length를 수용하기 위한 내부 한도이며, 공개 입력 범위를 늘리지 않는다. 매 E recurrence는 dyadic128로 내림/올림하여 누적 분모 증대를 제한한다. 정확한 q powers와 overlap 합은 계약한 유한 block/term 수 안에서 유지한다.

## 5. Source-backed cap transfer의 정확한 순서

cap 적용에는 metadata 사전이나 새로 만든 cap 배열을 받지 않는다. actual R11 bytes와 정확한 case ID를 요구한다. raw/capped saved q, tau, initial, coefficients, binding, cell 수가 서로 같아야 한다. 새 forcing 표현은 모든 양의 길이 overlap에서 기존 forcing과 같아야 한다. saved constant 배열을 한 source cell로 압축하는 것은 모든 원소를 exact equality로 확인한 뒤에만 허용한다.

old knots를 refined grid에 넣으므로 새 subcell `[b_i,b_(i+1)]`은 어떤 old **닫힌** cell `[a_j,a_(j+1)]`에 온전히 포함된다. 전체 horizon이 다르거나 포함 관계에 gap이 있으면 거부한다. old point cap은 새 시각과 old knot의 정확한 유리수 equality가 있을 때만 사용한다. 새 point가 old knot이면 양옆 old closed cell의 whole upper도 그 point에 유효하다. point cap을 보간하지 않는다.

한 refined cell에서 순서는 다음과 같다.

1. `rs=min(raw_Rwhole[i], old_Rwhole[j])`를 고정한다. 이는 그 cell 전체의 조건부 R upper다.
2. `left_E`는 이전 capped point E, 현재 raw point E, 그 cell의 old whole E, 왼쪽 point를 포함하는 모든 old closed-cell E upper, 정확히 같은 old point E cap의 최솟값이다. 왼쪽 R point도 현재 R point, rs와 유효한 old point/whole upper를 교차한다.
3. `scalar_right=up(exp_upper*left_E + phi_upper*(c*rs+g_e[j_source]))`를 계산한다.
4. 새 whole E upper는 `min(raw_Ewhole[i], max(left_E,scalar_right), old_Ewhole[j])`다.
5. 오른쪽 E point는 raw point, scalar_right, 새 whole E, 오른쪽 point에 유효한 old whole/point cap을 교차한다. 오른쪽 R point도 raw point, rs 및 유효한 old whole/point cap을 교차한다.
6. 모든 segment의 전파가 끝난 뒤 출력 point만 양옆 새 capped whole upper와 다시 교차한다. 이 마지막 출력 교차로 과거 cell을 다시 전파하지 않는다. 이는 유효한 upper들을 추가로 교차하는 연산이다.

`capped.propagation`에 `old_cell_index`, `left_E_used`, `R_whole_used`, `unclipped_scalar_right_upper`, `whole_E_upper`, `right_E_before_output_neighbor_intersection`를 보존한다. 정확한 R의 전역 kernel/forcing 메모리는 cap 연산 전후에 불변이다. Capped lower 배열은 `null`이다. 서로 다른 유효한 조건부 upper를 교차한 결과에 raw 비교계의 lower를 붙이지 않는다.

요청한 cell upper는 그 cell을 빈틈없이 분할하는 refined closed-cell upper들의 성분별 최댓값이다. 요청 point 출력은 정확히 같은 refined knot를 선택한다. 요청 grid의 점들을 그림에서 선으로 잇는 것은 whole-cell 인증과 다른 표현이다.

## 6. 유한 자원 계약과 입력 거부

| 항목 | 고정 영역 |
|---|---:|
| 순서가 있는 state 수 | 1–13 |
| source / observation / old cap cell 수 | 각각 1–192 |
| refined cell 수 | 최대 2048 |
| 완전한 kernel block 수 `floor((T-t0)/tau)` | 최대 8 |
| 검사할 overlap 항 수 | 최대 200000 |
| exact 입력 numerator/denominator 크기 | 각각 최대 1024 bits |
| `abs(d)*(T-t0)` | 최대 16 |
| scalar arithmetic | dyadic128 / Taylor96 |
| 새 primary / reference | 각각 1회, 60 CPU초 / 90 wall초 |
| 기존 R11 및 선행 실행 allowance 증가 | 0 |

overlap term count는 refined point 수 × source cell 수 × `(full_blocks+1)`로 미리 제한한다. 양의 overlap만 실제 합에 기여하지만, 자원 guard는 0이 되는 잠재 항까지 센다. primary의 내부 58 CPU초/88 wall초 guard는 root의 외부 60/90 한도보다 앞서 중단하기 위한 보조 수단이며 전체 process CPU의 권위는 OS rusage다.

모든 scalar/grid 항은 int, Fraction 또는 rational text여야 한다. float/bool, 음수 forcing, 길이가 0인 cell, 뒤집힌·중복 knot, 다른 horizon, 음수 initial, q 범위 밖, tau<=0, c<0, state 중복/초과, certificate q/tau/binding/validity 불일치, 유효하지 않은 cap bytes/case/forcing/clock은 거부한다. 하나의 state에서는 zero-mass residual 공간이 0이므로 `R0=g_r=0`을 요구한다.

primary runner는 인자를 받아 개별 case를 재실행하는 CLI를 제공하지 않는다. 최초 `PRIMARY_RESULTS.json`이 있으면 덮어쓰지 않는다. source/input/core/helper/runner/contract와 상속 source가 preexecution freeze에 있어야 하며 실제 bytes/sha가 같아야 한다. 실행 실패는 예외·traceback·이미 완료된 검사를 최초 출력에 남긴다. 실패를 성공으로 다시 쓰거나 old allowance를 늘리는 경로가 없다.

## 7. 단일 primary의 판별 사례와 검사

4개 saved case 각각에서 original aligned192와 지정된 nonaligned192 observation grid를 계산한다. 비정렬 interior knot는 odd n에서 `(n+1/3)*delta`, even n에서 `(n-1/5)*delta`이며 양 끝은 원래와 같다. 원래 old knots는 cap transfer를 위해 refined grid에 남는다. 정렬 결과와 비정렬 결과의 공통 old knot에서는 exact F/R가 같아야 하며, 동일한 ideal E를 감싸는 outward 구간은 겹쳐야 한다. 서로 다른 요청 시각의 수치를 같은 point의 개선으로 비교하지 않는다.

고정한 11개 control은 다음과 같다.

| ID | 판별하는 의무 |
|---|---|
| `q1_polynomial_nonaligned` | q=1, d=0의 정확한 polynomial; 최종 R=3, E=6 |
| `q0_late_source_nonaligned` | h0=1의 fresh forcing; 최종 R=1/4, E=1/32 |
| `translated_source_breakpoints` | source 이동 경계 8/15, 13/15와 signed d<0 |
| `block_jump_left_limit` | t=2/5에서 left limit 1과 point 1/2의 구별 |
| `positive_d_nonaligned` | d>0 및 13-state 경계 |
| `near_zero_d_positive` | d=+10^-30 |
| `near_zero_d_negative` | d=-10^-30 |
| `near_one_q` | q=1-2^-128 및 8-block 상한 |
| `shifted_clock` | 동일 문제의 정확한 -5/7 시각 이동 |
| `observation_refinement_fine` | 같은 ideal 함수의 더 세밀한 observation 분할 |
| `singleton_zero_residual` | 1-state zero-mass residual R=0 |

일반 geometry, closure, positivity, interval order, exact R containment, V 포함, cap inclusion, source byte identity와 잘못된 입력 guard를 같은 bounded primary 안에서 확인한다. 같은 구현을 다시 호출하는 별도 테스트 실행은 계획하지 않는다. 독립 reference는 별도 소스에서 finite primitive J로 F/R를 구성하고 Decimal160 closed-form scalar moment를 사용한다. Production helper를 import하거나 복사하지 않는다.

## 8. Reference와 후처리를 위한 출력

단일 primary 최상위 schema는 `WU_R12_PRIMARY_RESULTS_V1`이다. `hd_cases`의 각 record는 `id`, `source_scope`, `variants.aligned`, `variants.nonaligned`, `comparison`을 갖는다. `controls`는 `id`, 원래 control `parameters`, `result`를 갖는다. 모든 Fraction은 정확한 rational string으로 serialize한다.

각 sweep의 schema는 `WU_R12_NONALIGNED_CONVOLUTION_V1`이며 다음 필드를 유지한다.

- `parameters`: q/tau/c/d/initial/t0/T, binding, certificate.
- `source`, `requested_times`, `refined_times`: 전체 정확한 source/observation/refined clock 및 forcing.
- `exact`: kernel powers, 각 refined point의 kernel/F/R, 각 segment의 L/V/whole_R.
- `refinement`: source cell index, 요청 point index, 요청 cell의 gap-free refined index range, left-limit 방향.
- `Bernstein_weights_by_length`: 각 서로 다른 길이에 사용한 exp/W0/W1/phi 구간과 Taylor tail.
- `raw`: 요청 및 refined point lower/upper, requested/refined whole-cell upper, affine L/V의 outward 구간.
- `capped`: 같은 upper 필드와 위에서 명시한 전파 기록. Lower는 null.
- `caps`: 실제 source SHA/case/pointer, old knots/point/whole upper, 각 새 subcell의 old cell index, exact old-point mapping, point를 포함하는 old closed-cell 목록.
- `work`, `rounding`, `h0`, `R_memory_reset`, `physical_consumer_admitted`, `old_science_replay`, `new_ODE_calls`: 자원 범위와 의미를 독립적으로 검토할 수 있는 기록.

Raw lower는 고정한 rational-q ideal comparison의 lower다. 실제 물리 오차의 lower나 새로운 물리 closure가 아니다. Capped 결과가 기존 cap 이하인 것은 동일한 전제와 정확한 point/cell 결속하에서의 upper 교차 성질이다. Raw의 보편적 우위 또는 다른 clock에서의 point 개선은 주장하지 않는다. 기존 R8 원래 실패, R10/R11 tolerance-qualified sample 기록, CAS 경고와 `NOT_ESTABLISHED` 원인은 변경하지 않는다.

## 9. C3–C6 작업 상태와 skill context

적용한 선택 skill은 PhysMath Research Loop 1.3.0, `c38/physmath-research-loop`다. `SKILL.md`, `references/CODING_LOOP.md`의 C3–C6, `references/POLICY_INTEGRATION.md`, `references/SUBAGENT_MODE.md`를 사용했다. C3는 exact geometry/forcing/cap 결속 오류를 분리했고, C4는 새 유한 run·bit·cell·term 예산을 고정했으며, C5는 source identity, signed arithmetic, 비정렬 적분과 reference-facing 출력을 구현했다.

C6의 실제 계산 결과는 이 설계 문서에서 미리 PASS로 표시하지 않는다. 현재 저자 작업의 실행 수는 0이며, root의 freeze 및 실제 단일 primary/reference 이후 기록으로 판정한다. 파일 작성과 AST 검사는 새 solver 실행 allowance를 소비하지 않았다. 그 이후 중대한 변경이 필요하면 원래 실패/출력을 보존하고 바뀐 의무와 유한 수선 범위를 먼저 명시한다.
