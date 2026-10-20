# PHYS70 독립 구현·수학 검토

판정: **PASS_SCOPED_AFTER_TWO_TARGETED_FIXES**.
검토자는 `/root/opt_literature`이며 최적화 구현 코드는 작성하거나 수정하지
않았다. 현재 검토 파일의 SHA는 `INDEPENDENT_REVIEW.json`에 고정했다.

현재 finite-L 원래 HH binary64 경로에서 확인한 블록 소거, callback 식,
단계식과 실패 처리는 채택 가능하다. 두 구체적 결함을 구현 전에 숨기지
않고 기록했으며, 최소 수정과 해당 회귀 시험의 실제 PASS로 닫았다.
기존 PHYS64–69 과학 적분이나 전체 시험을 검토 명목으로 재실행하지 않았다.

## 1. 검토 방법과 범위

원래 `native/phys69_vigilode/src/lib.rs`의 RHS·JVP·time partial을
새 `kernel.rs`, `block.rs`와 대조했다. 추가로 실제 Cargo checkout의
VigilODE commit `a21d573980f66fe02891bd216153443b5352f921`에 있는
`rodas5p_matrix_free_fast.rs::attempt_inner`와 `adaptive.rs`를 열어
raw-U 단계식과 PI controller 호출을 확인했다. 기존 문헌 조사만으로
새 구현의 동등성을 판정하지 않았다.

각 검토 축의 결론은 다음과 같다.

| 대상 | 확인한 내용 | 판정 범위 |
|---|---|---|
| ordered SIMD | scalar `sqrt/exp`, node 누적 순서, `(p_a*p_j)*v` 괄호 보존; lane은 서로 다른 j | 현재 compiler/target의 bit 비교는 실제 시험으로 확인 |
| 복소 shifted solve | oscillator 부호·`1+s²Q` 분모, shared a/b 미분의 두 항, z의 `-2`와 켤레 부재 | 정확 산술의 원래 전체 Jacobian 소거 |
| time partial | `tau=65-r`의 부호와 기존 Q 및 angular 미분 일치 | 원래 비자율 HH 식 |
| raw-U | `hγ f_i + γΣC_ij U_j + h²γγ_i f_t`, 같은 `b_code`, 마지막 U8 WRMS | pinned upstream의 단계·오차식 보존 |
| 캐시 | 시간·상태 bits와 immutable kernel 설정이 같을 때만 재사용 | h-only retry의 operator 재사용, 실패 refresh 무효화 |
| 시계·상태 commit | represented `end-t`, 엄격한 max step, 재거절시 실제 endpoint 단축, accepted 후보만 commit | 종점 38의 완전 도달과 partial 구분 |
| 병렬 요청 | job마다 own solver/workspace, 결과 index 보존, 개별 오류를 batch false로 전달 | 독립 job 실행 구조; 실제 throughput은 별도 측정 |
| 완료 검사 | 정확한 두 시각, 두 상태, 고정 차원, 모든 성분 finite, 실패 exit | 잘못된 complete 승격 방지 |

Frozen JVP의 z 계수를 미리 계산하는 재배치는 수학적으로 맞다. 다만
complex 곱셈과 나눗셈의 순서가 원래 callback과 달라질 수 있으므로
이 경로의 bit identity를 주장하지 않는다. 현재 시험은 수정하지 않은
PHYS69 JVP로 새 inverse의 잔차와 원래 벡터 복원을 확인한다.

## 2. 발견하고 닫은 두 결함

### R70-F1 — 실패한 public freeze 이후 옛 operator가 살아 있음

첫 구현의 `HhKernel::freeze`는 `check` 또는 angular 계산에서 오류가
발생하면 `FrozenJacobian::prepare`에 도달하지 못했다. `prepare` 안에서만
무효화했으므로, 이미 valid였던 Jacobian을 전달한 호출자는 실패 후에도
옛 기준 상태의 `apply`를 사용할 수 있었다. `integrate::attempt`는
별도로 먼저 무효화하고 있었기 때문에 당시 주 적분 경로는 보호됐다.
하지만 public API의 실패 계약을 닫을 필요가 있었다.

수정은 `freeze` 시작에서 `jac.invalidate()`를 실행하는 것이다.
실제 소스에서 이 순서를 확인했다. root가 실행한
`failed_public_freeze_invalidates_previous_operator`와
`failed_refresh_does_not_poison_later_valid_attempt`가 모두 PASS했다.

### R70-F2 — residual normalizer overflow가 0 residual로 보임

원래 잔차 분모는 성분별 `|x|+|s| |Jx|+|b|`의 최대값이었다.
입력과 해가 모두 finite여도 이 합은 overflow할 수 있다. 분모가
`+Inf`이면 유한 양의 분자가 있어도 비율이 0으로 계산되어 guard를
잘못 통과한다.

검토자가 수행한 하나의 짧은 IEEE scalar 계산에서
`r=28, j=0, Q=0.5614285714285714, s=.01`,
`b_f=1e308, b_g=5e307`를 사용했다. 해의 두 성분은 모두 finite였지만
잔차 분자는 `1.99584030953472e292`, 분모는 `+Inf`, 기존 비율은 0이었다.
이는 반례 판별용 작은 산술 계산이며 새 HH 적분이 아니다.

수정은 나누기 전에 분자와 분모가 모두 finite인지 검사하고 그렇지
않으면 `NonFinite`를 반환하는 것이다. 실제 소스를 재독했고,
`overflow_in_residual_normalizer_cannot_pass_as_zero`의 실제 PASS를
확인했다. 극단적 magnitude에서는 보수적으로 실패하며 false-zero로
성공하지 않는다.

## 3. 이미 실행된 새 검증의 재사용

`RUST_TESTS_01.log`의 release 실행에서 **새 시험 13개가 PASS**했다.
검토자는 같은 시험을 다시 실행하지 않고 그 로그와 실제 assertion을
읽었다.

* callback parity는 L21/28/36/64, 네 tau에서 RHS와 explicit time partial의
  scalar/SIMD/기존 코드 bits를 대조한다.
* 원래 JVP를 이용한 shifted inverse 검사, shared external channel 검사,
  모든 raw-U 단계식의 역대입이 포함돼 있다.
* 캐시 재사용·설정 변화·실패 복구·shape/step 제한과 위 두 결함의
  회귀 검사가 있다.
* 나머지 네 시험은 strict cap, 인접한 표현 가능 시각, 거절의 실제
  단축, 마지막 두 ULP 구간의 정확 종점 도달을 확인한다.

상쇄로 매우 작아진 embedded stage 자체를 분모로 쓰는 상대오차는
유용한 채택 기준이 아니다. `benchmark.rs`가 그 raw relative 값을
진단으로 남기고, 원래 상태의 atol/rtol 가중치에 대한 stage 차이와
별도 endpoint 차이로 판별하도록 수정된 점도 확인했다. 이 판별은
현재 최적화 비교의 허용 기준이며 전체 구간 오차 인증을 뜻하지 않는다.

## 4. 상태와 후속 근거

이 검토 시점의 미해결 blocking finding은 없다. 실제 전체 요청의 속도,
peak memory, 병렬 batch 결과와 원래 인증값에 대한 D2 오차는 root의
성공 실행 영수증에서 확인해야 한다. 이 문서는 그런 숫자를 추정하지
않는다. 낮은 backward residual도 binary64의 관측값이며 interval
integration 인증서가 아니다.

| 상태 축 | 실제 기록 |
|---|---|
| 유도·구현 검토 | 위 범위 PASS, 두 finding 모두 수정·표적시험으로 닫음 |
| 검토자의 실행 | 작은 IEEE scalar 반례 1건, 과학 적분 0, 시험 재실행 0 |
| 새 시험 근거 | root의 release 13/13 PASS 로그를 읽어 재사용 |
| 게시·백업 | root의 실제 후속 ACK를 참조 |
| DAG | PHYS70 구현 검토 의무를 닫음; PHYS63·PHYS69 인증 및 원래 xi/반응률 의무의 상태는 보존 |

HH_R10=OFF.
