# PHYS77 generic whole-cell kernel 독립 검토

판정: **PASS_SCOPED_FINITE_REAL_LIFT_CELL_KERNEL**.

검토 대상은 `owner_interval.py`, `cell_enclosure.py`의 수학·구현 대응과 작은 분석적 문제의 동작이다. 별도 agent가 담당한 원본 exporter 및 실제 2592-packet point 검토를 재실행하지 않았다. 새 ODE solver 호출·benchmark·NCP 실행은 0회다.

## 1. 수학과 구현의 대응

`certify_cell`은 slope를 rounded Decimal point로 먼저 정의한다. `p0+t*slope`와 실제 endpoint를 그 이후 outward arithmetic으로 감싸므로, 저장된 target과 exact interpolation이라고 혼동하지 않는다. 실제 초기 enclosure에서 predictor 중심을 빼 `initial_error`를 만들고, 성공한 endpoint enclosure를 다음 cell에 전달한다.

`image = initial_error + [0,h]*defect`가 후보 symmetric error box의 모든 성분에서 strict interior에 있을 때만 성공한다. 성공 후 endpoint는 `initial_error + h*defect`로 따로 계산한다. 이는 first-exit 정리와 일치한다. 전체 시간의 integral hull과 endpoint integral을 혼용하지 않는다.

초기에 고른 반지름과 inflation은 증명 대상 후보를 선택하는 단계다. 매번 전체 RHS box와 모든 inclusion 조건을 다시 검사하므로, 현재 이미 포함된 성분의 반지름을 유지하는 변경은 정리의 전제를 약화하지 않는다. 선언한 반복 수 안에 성공하지 못하면 `NOT_CERTIFIED`와 실제 attempts를 남긴다.

`FiniteOwner`는 다음 대응을 보존한다.

- 캡처된 packet population, q, mu², normalization 및 5×5 matrix를 실수화 입력으로 사용한다.
- nonnegative packet의 finite sum, positive sqrt/divisor와 공통 exponentials를 outward 계산한다.
- `rho_minus_pbar`와 signed packet stress를 대수적으로 동치인 형태로 계산한다.
- `gamma=href/h0`와 `H²/h0²`로 무차원화하되, 동일한 캡처 상수를 RHS와 observables에 사용한다.
- 전체 monopole row를 유지한 `delta_monopole`을 A에 남긴다. 독립적인 unsimplified chain-rule A도 별도로 반환한다.
- matter와 radiation source의 부호를 각각 유지한 뒤 합산하여 total norm을 계산한다.
- `H²>0`, `E0>0`, regular b chart를 확인한다. 이 조건을 box 전체에서 확보하지 못하면 인증하지 않는다.

## 2. 독립 표적 검산 16개

최종 source와 최종 portable test 파일에서 **16/16 PASS**다.

| 검산 | 독립 기준 |
|---|---|
| signed linear growth/decay | `y'=lambda y`, lambda=−2,0,2의 닫힌 해 |
| nonlinear 초기값 family | `y'=y²`, `y=y0/(1-y0 t)`의 정확한 유리수 값 |
| nonzero initial-error 전달 | `y'=1`, 초기 구간을 두 cell 전체에서 그대로 운반 |
| signed endpoint | 상수 음·양 forcing에서 `[0,h]D`와 `hD`의 차이 |
| rounded affine endpoint | precision 16의 1/3 slope가 만드는 실제 endpoint 0.9999999999999999 |
| triangular family | `y1'=0,y2'=20 y1`, 정확한 family와 3회 이내 inclusion |
| cell 내부 forcing peak | 끝점에서 0인 `4t(1-t)`를 whole-cell로 평가 |
| 실패 결과 | 작은 후보와 제한된 반복이 명시적 noncertificate를 반환 |
| singular domain | 후보 tube가 `y=1`의 pole을 포함하면 거부 |
| 잘못된 control | 역방향/길이 0 cell, 잘못된 반복 수·반지름·inflation 거부 |
| 역순 초기 interval | 수정 후 명시적으로 거부 |
| ambient Decimal context | 낮은 외부 precision이 정확한 cell width를 바꾸지 않음 |
| square | exact Fraction endpoint 및 zero-crossing bound |
| sqrt | exact Fraction squared inequalities와 별도 180-digit reference |
| exp | Decimal.exp를 쓰지 않는 exact Fraction Taylor series와 geometric tail |
| elementary boundary | 음수 sqrt domain 및 quiet subnormal neighbor 거부 |

Triangular family는 unweighted whole-step Lipschitz factor가 2여도 first-exit box inclusion이 가능함을 보여 준다. 구현의 특정 줄을 재현하는 테스트가 아니라 닫힌 해와 regular family를 기준으로 한다.

## 3. 실제 발견과 수정

최초 검산은 15 PASS, 1 FAIL이었다. Generic `certify_cell`이 `initial_box=[Interval(2,1)]`를 검증 없이 계산하여 malformed interval을 성공 결과에 남길 수 있었다. 실제 `certify_request`는 정상적인 point/운반된 interval을 생성하므로, 이 발견으로 기존 실제 성공 결과가 무효가 되는 것은 아니다.

최소 수정은 모든 initial interval과 반환 RHS interval의 type·finite·ordering guard다. Root가 이 수정만 반영했다. 같은 16개 검산은 통과했고, 이후 게시 가능한 상대경로 import로 바꾼 최종 test 파일에서도 같은 검산을 통과했다. 최초 실패와 두 후속 receipt를 모두 보존했다.

## 4. 실제 성공 결과의 재실행 없는 source 연결

`INPUT_GUARD_VALIDATION_BRIDGE.json`은 guard 추가 전 source를 실제 성공 receipt의 hash와 대조한다. 다음만 제거한 AST는 전후가 정확히 같다.

- `cell_enclosure.py`의 `_valid_box` import 및 initial/RHS 두 검증 loop;
- `owner_interval.py`의 `_valid_box` 함수 정의 자체.

그 함수의 차이는 Decimal endpoint type 검증의 추가이며, 수치 연산·반환값을 바꾸지 않는다. 기존 실제 성공 결과의 초기·RHS·그 밖의 interval 134개를 읽어 final guard로 검증했다. 중간 candidate의 모든 RHS는 저장되지 않았고 다시 계산하지 않았다. 이 중간값에 대한 연결은 검토한 outward arithmetic이 성공적으로 반환한 interval은 finite/ordered라는 불변식에 근거한다.

따라서 실제 run의 source hash를 현재 hash로 다시 표시하지 않는다. 원래 성공 receipt와 현재의 guard-only 변경을 명시적으로 연결한다. 실제 2592-packet cell 검사와 point 검산은 반복하지 않았다.

## 5. 근거와 남는 범위

최초 실패: `INDEPENDENT_FIRST_TESTS.json`, `independent_first.log`.

수정 확인: `INDEPENDENT_FINAL_TESTS.json`, `independent_after_input_guard.log`.

최종 portable 검산: `INDEPENDENT_PORTABLE_FINAL_TESTS.json`, `independent_portable_final.log`, `test_cell_independent.py`.

Source 연결: `INPUT_GUARD_VALIDATION_BRIDGE.json`, `bridge_input_guard.py`.

미해결 구현 finding은 없다. 이 판정은 finite captured-coefficient real-lift의 cell kernel에 한정된다. 전체 history, 과거 machine trajectory의 정확한 인증, momentum/각도 continuum 및 production 인증으로 확장하지 않는다. `HH_R10=OFF`; production admission은 발급하지 않는다.
