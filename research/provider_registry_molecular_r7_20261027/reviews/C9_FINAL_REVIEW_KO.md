# R7 독립 C9 최종 심사

**판정: PASS_SCOPED_CONDITIONAL_NONLINEAR_FEEDBACK_CODE.**

새 비선형 event-feedback의 조건부 이론과 이를 구현한 유한 exact-rational/directed-dyadic bound 코드를 root가 범위 내에서 채택할 근거가 충족되었다. **열린 material finding은 0건**이다. 첫 실행 전 발견한 CPU 측정 표기 문제는 수정되고 실제 실행 기록으로 닫혔다. 추가 과학 실행이나 replay는 요구하지 않는다.

심사는 앞서 저장한 독립 이론 검토, 생산·reference 정적 대응, 실제 원본 결과 판독을 **한 번의 연속된 review pass**로 수행했다. 심사자는 이론·생산·reference를 작성하지 않았고, proof/code/DAG를 수정하지 않았다. 심사자의 solver/CAS/import 실행과 과거 과학 재실행은 모두 0회다.

## 1. 실제 실행과 identity

| 근거 | 실제 결과 | OS process CPU |
|---|---|---:|
| Primary, 1회 | **144/144 PASS**, failures0, exit0 | 0.239641 s |
| 독립 reference, 1회 | **376/376 PASS**, failures0, exit0 | 4.632575 s |
| Wolfram, 1회 | 24개 zero residual 반환, 실제 경고 동반 | kernel 0.278886 s |

Primary와 reference CPU는 각각 `raw/PRIMARY_PROCESS.json`, `raw/REFERENCE_PROCESS.json`의 OS child 측정값으로 import와 직렬화를 포함한다. 결과 내부의 finalize/main 측정값과 구분했다. 남은 신규 allowance는 **primary/reference/Wolfram=[0,0,0]**이며, 기존 R6/PHYS91의 [0,0,0]을 전용하지 않았다.

실제 실행 identity는 다음과 같다.

- 생산 core: `002a66a30961b21e566a940462468c9ea8e1bc868d98549d3ea79d164c239957`.
- Primary runner: `9c77f020b82b8bf8b3868c4f91d8a0e8111aa92d579f1505ca1566098cf95a97`.
- Primary input: `3ff9c2535e5c0ce6ffa5e9671de15aad6649e0996cd9b9e275cc290facd8d330`.
- Primary result: `6eaf3c0eed7968cf4023180e15373a180bb5b1bab2e56cd4a8547387ed337a15`.
- Reference script: `ef5b0ada9edd711551aec27cd43718771114c9908526940dea9df1d706b7f083`.
- Reference input: `2039ddf826beb97b875249bd7a66cfe9c7be087ab746ef56f94e78d613046bf1`.
- Reference result: `e403c7803c080fd4f26be71a93b782b02d874f80ef11c85a706bea71e2a743cd`.

현재 파일과 preexecution freeze의 **11개 identity가 모두 일치**했다. 결과가 기록한 core·runner·input·proof와 실제 보존 파일도 연결된다. 상세 binding은 동반 JSON에 보존했다.

## 2. 정적 대응 판정

**양의 급수와 나머지 항.** 생산 코어는 C를 먼저 위로 반올림한 C_up으로 계산한다. 각 양의 행렬 항도 정수 올림 나눗셈으로 감싼다. Tail에 사용하는 z는 반올림 전의 작은 norm이 아니라 실제 C_up의 유도 무한 norm이다. `N+2>z` 조건과 위쪽 scalar term으로 기하급수 tail을 덮는 방향이 맞다. 다음 positive product가 정확히 0인 경우의 종료도 안전하다.

**Reciprocal exponential.** 아래쪽 positive partial sum은 exp(q)의 하계이므로 그 위쪽 역수는 exp(−q)의 상계다. 위쪽 partial sum+tail의 아래쪽 역수는 반대쪽 포함값을 준다. q=0은 정확한 [1,1]이다. Coordinate scaling과 복원은 양의 대각 similarity 및 forcing 변환과 일치한다.

**Endpoint와 블록 전체.** `T00=W_upper00-1+rho`를 유리수로 정확히 뺀다. 음의 d는 endpoint·pointwise 계산에 유지한다. 전체 블록만 `Bplus[d]=max(d,0)`의 비음수 시간 단조 비교계로 감싼다. Endpoint를 이전 구간 전체의 상계로 대체하지 않는다. B 역행렬 없이 singular/zero/nilpotent 경우를 처리한다.

**반응과 입력.** 정수 사건 열, exact H/D/charge, simplex alpha, 동일 invariant class, source model 단일 선택, nominal K/H/rho와 feedback-accounted 조건이 구현에 반영됐다. 지수0은 거듭제곱 전에 미분0으로 처리한다. q/theta, coarse source defect 및 full-interval box의 유효성은 명시적 caller evidence이며, 고정 primary는 실제 exact 값 또는 invariant-class 선분으로 이를 대조했다.

**Reference 독립성.** Reference는 생산 코어와 R6 코어를 import하지 않는다. 별도 augmented SciPy expm과 직접 event propensity fine/coarse RHS를 사용한다. coarse_kf_offset이 있는 eta 식의 부호, residual의 −wQD r 및 q0X, 65-clock 공유 endpoint 인덱싱, 5-point 생산 query 대응이 일치한다. Source K/H/rho는 저장 R6 자료의 identity와 family 포함 여부를 읽어 재사용하며 과거 Gibbs/rate/uniformization을 실행하지 않는다.

## 3. 실제 수치 근거의 범위

고정 primary는 affine 5개와 HD 4개를 저장했다. 각 HD는 3블록이며, reference는 블록당 65시각을 공통 경계에서 공유하여 **각 사례 193개의 서로 다른 시각**을 저장했다. 생성 시점이 늦은 forcing, source defect, negative d, singular B 및 source/invariant/domain guard를 실제 결과에 포함한다.

Reference는 모든 저장 시각의 R/E, 별도 endpoint 상계, 보존량, 양성, scalar eta 및 residual 항등식을 지지한다. Native-K conditional 사례의 최대 H/D/charge drift는 약 `1.11e-14`, eta 항등식 잔차는 `3.02e-16`, residual 항등식 잔차는 `2.45e-16`이다.

이는 **binary64 수치 보강**이다. 예를 들어 무반응 사례의 정확한 coarse error 0에 대해 reference는 일부 시각에서 약 `1.11e-16`의 차이를 반환한다. 고정된 수치 비교 허용 오차를 적용한 사실을 유지한다. Floating reference나 유한 저장 시각을 exact outward proof 또는 물리적 측정 불확실성으로 바꾸지 않는다. 전체 구간의 보증은 이미 심사한 조건부 정리·산술 방향·invariant box에서 나온다.

## 4. 발견·수정 이력

**R7_C9_F01 — LOW, CPU accounting.** 최초 runner의 `actual_process_cpu_seconds_at_finalize`는 `time.process_time()-cpu0`여서 Python 시작·stdlib import·입력 판독을 제외한 구간 값이었다. Process 전체라는 이름과 allowance 판정 범위에 맞도록 누적 `time.process_time()`를 기록하고, 기존 차이는 `actual_run_cpu_seconds_at_finalize`로 보존하도록 수정했다.

수정은 **첫 primary 전**에 반영됐다. 실제 결과에는 process finalize 0.194160618 s, run-local 0.123682181 s가 별도로 저장됐고, 외부 OS receipt는 직렬화까지 포함한 0.239641 s를 보존한다. 원래 RLIMIT_CPU도 process 전체에 걸려 있었으므로 상계 산술이나 이전 과학 결과에 영향은 없었다. **CLOSED**, repair science run0이다.

작성자가 첫 실행 전에 추가한 core의 `Interval -> {lo,hi}` exact export도 판독했다. 초기 e669…에서 freeze002a…로의 100-byte 변경은 serialization 지원이며 상계 알고리즘을 바꾸지 않는다.

## 5. CAS의 제한된 역할

Wolfram의 실제 raw response에는 24개 zero residual과 함께 **Power::infy, Infinity::indet 및 General::messages**가 있다. 경고 원인은 **NOT_ESTABLISHED**이며 warning-free 결과로 표현하지 않는다. 이 결과의 역할은 **qualified symbolic corroboration**으로 한정한다.

독립 일반 증명, 정적 산술 방향 검토, primary·reference의 실제 결과가 scoped adoption의 주근거다. 경고를 숨기거나 성공한 출력을 새로 얻기 위해 재실행하지 않는다. 원시 응답과 제한 표기를 유지하는 현재 방식으로 충분하다.

## 6. 채택 범위

코드는 일반 종1–16, 최대64 사건, 반응 차수 최대4, HD 상태1–13을 지원한다. 지수 상계의 유한 domain은 rounded scaled norm<=16, N+2>z, degree0..256, bits128..512다. 이 범위 밖의 입력은 거부하며 임의 clamp하지 않는다.

실제 공통 H2/HD pool, state/branch mapping, density/history, physical clock, GL2022 state-to-state destruction 배열 및 named physical consumer는 별도 입력이다. 저장된 9-state K의 사용도 **합성 reaction control을 결합한 조건부 수학 사례**로 유지한다. Metadata 문자열은 물리적 source binding을 자동 증명하지 않는다.

Root가 해당 조건부 이론과 코드 노드를 채택하도록 권고한다. 이 심사자는 DAG를 변경하지 않았다. **HH_R10=OFF, production=NOT_ISSUED, L4_ready=false, central/physical delta0**을 유지한다. 이 bound API는 실제 fine physical ODE의 invariant-preserving 적분기 자체가 아니다.

