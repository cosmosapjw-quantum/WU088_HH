# PHYS84 독립 구현 검토

## 판정과 범위

현재 판정은 **STATIC_REVIEW_PASS_NUMERICAL_ADMISSION_WAIT**이다. 복구된 v4 전체와 v5의 실제 변경은 독립 정적 검토를 통과했다. 승인된 최초 검증 요청은 공유 lease의 memory 기준에서 exit 75로 대기했고 child는 시작되지 않았다. 수치 검증, fixture interface 호출, mock callback, 실제 application은 모두 0이다. 고정 자원 정책을 유지하며, 실제 가용 headroom이 달라진 근거가 생긴 뒤 부모가 다음 bounded 요청을 결정한다. 이번 상태는 수치 실패나 과학 결과 완료가 아니다.

이 문서는 `/root/adapter_independent_review`의 fresh-context C9 검토이다. 구현 작성에 참여하지 않았고, 새 모듈 import, 수치 테스트, 원전 rate 계산, population solve, ODE, 실제 application callback을 실행하지 않았다. 허용된 쓰기는 이 보고서와 동반 JSON 두 파일뿐이다. 부모 연구의 원전 물리 판정과 이미 완료된 PHYS83 실행을 재심사하거나 반복하지 않는다.

실제 읽은 저장소 HEAD는 `ce14c0bfc0318662673b021a08f4029d6a36c7a7`이며 PHYS84 S0이다. PHYS83 부모 완료 HEAD는 `6a2fc5aacb6182a916b9434c316e99e750e8273c`이다. 본 검토는 아직 커밋 전인 PHYS84의 동결 코드 snapshot을 대상으로 하며, 원격 게시·백업 상태는 이 검토가 인증하지 않는다.

## 고정 근거

- `CONTRACT.json` revision 2: SHA256 `01528db5b31bd27cb0a9ae623b92cd0821ac4b42bfb4b3792ce3cc56c6e8280f`.
- 이론 유도 및 `reviews/THEORY_CONTRACT_REVIEW_KO.md`의 기존 독립 물리 판정을 재사용했다.
- PHYS83 scientific identity `e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c`는 저장 입력이다. 기존 132 rate / 324 steady / 732 transient rows의 과학 실행을 추가하지 않는다.
- 정적 검토 기준본은 `implementation/pretest_frozen_v2/SHA256.json` 및 그 코드 원문이다. S1/S2 이전 원문과 수리 diff도 보존되어 있다.
- S3–S5 재검토는 `implementation/S3_S4_S5_REPAIR.diff`, `S3_S4_S5_REPAIR_RECEIPT.json`, `pretest_frozen_v4/SHA256.json` 및 실제 변경 위치를 대상으로 했다. `source/source_adapter.py`와 `source/fixtures.json`은 v2와 동일하다.

적용한 skill은 physmath-research-loop 1.3.0의 `SKILL.md`, `references/POLICY_INTEGRATION.md`, `references/CODING_LOOP.md` C9, `references/SUBAGENT_MODE.md`이다. 한 번의 독립 검토 안에서 실제 지적과 최소 수정만 다루며, 수정된 부분 외의 완료 계산을 재실행하지 않는다.

## 식과 코드의 대응

7개 사건의 순서는 CE 상향 2S/2P, CE 하향 2S/2P, 2S 두 광자, 2S M1, 2P E1이다. `source_adapter.evaluate`는 저장한 정확한 T 라벨에서만 rate를 선택한다. 상·하향 충돌은 해당 H 상태와 전자 밀도의 곱, 자발 방출은 excited-state 밀도와 A의 곱으로 구성된다. Δ는 source-native `10.20435 eV`이다.

| 검토 대상 | 실제 대응과 판단 |
|---|---|
| 1S/2S/2P incidence | 각 상향 사건은 바닥상태를 줄이고 해당 excited state를 늘린다. 하향·방사 사건은 역방향이다. 열벡터는 충돌 상향 음, 하향 양이다. |
| 원자 여기 저장 | Δ와 세 상태 incidence를 일관되게 연결한다. 자발 방출은 원자 여기 저장을 줄인다. |
| 두 광자 사건 | 방출 에너지는 Δ 한 번, 광자 수는 두 번이다. M1/E1의 광자 수는 한 번이다. |
| 에너지 소유권 | `gas_thermal`, `chemical_binding`, `atomic_excitation`, `radiation_injected`, `escaped_radiation`, `source_reservoir` 여섯 열만 합산한다. `Q_emitted`는 중복 합산하지 않는 진단이다. |
| radiation route | `immediate_escape`와 `emissivity_handoff`는 배타적이다. 첫 route는 escaped, 둘째는 injected에 같은 방출 에너지를 기록한다. |
| 중복 방출 방지 | `detached_own_spontaneous`, `explicit_1S_2S_2P`, `native_radiative_owner_active is False`가 필요하다. |
| 열 입자·전자 | 이 bound-bound 사건의 전자·열 입자 수 source는 0이다. spectator를 허용한 양의 `N_thermal`을 분모로 사용한다. |
| 온도 source | `Q_th == 0`에서 0, 그 외에는 `(2/(3 k_B))*(Q_th/N_thermal)`로 계산한다. |

상태는 nonnegative finite density 범위와 정확한 키 집합을 검사한다. `N_thermal`은 active H 상태 수와 전자 수의 합보다 작을 수 없다. T 보간·외삽은 없고 66개 저장 float64 라벨만 받는다. 이 8개 constructed local state와 두 route는 실제 cosmological charge/thermal history를 정의하지 않는다.

## 수치 설계와 검증 경계

양의 곱의 overflow와 양의 값이 0으로 내려가는 underflow를 명시적으로 거부한다. 합산은 `math.fsum`을 사용하고, residual을 0으로 강제하지 않는다. 아주 작은 state에 대한 보수적 거부는 이번 표현 가능 범위의 경계이며 물리적 불가능성 명제가 아니다.

독립 reference는 저장 CSV의 십진 literal과 상수·incidence를 직접 `Fraction`으로 읽는다. production의 이벤트/에너지 계산 helper를 reference에 호출하지 않는다. 취소가 큰 signed 값은 작은 결과 자체가 아닌 gross-event / gross-energy / gross-temperature scale로 정규화한다. 양의 사건·광자·방출량은 상대 오차, 영 gross에서는 exact zero를 확인한다. 고정 tolerance는 positive relative `2e-12`, signed 및 보존 residual normalized `2e-13`이다.

계획된 matrix에는 16개 fixture×route 호출, 독립 수학값 비교, 잘못된 domain·owner·route·pin·parser 입력 거부, mock-only persistence, 실제 callback sentinel, 기존 science import 방지가 포함되어 있다. mock 실패 보존과 mock resume는 실제 science application 또는 실패의 수에 더하지 않는다. 실제 검증 결과는 아직 없으므로 이 단계에 PASS 수치 assertion을 기재하지 않는다.

## 지적과 해결 이력

| ID | 관측된 문제·영향 | 최소 수정과 현재 상태 |
|---|---|---|
| S1/S2 선행 | 최초 코드의 COMPLETE whitespace 수용과 무의미한 callback guard. | 동결 v1, diff, v2를 보존했다. v2에서 canonical 검증과 실제 sentinel이 추가되었다. 아래 C9-S1B는 S1의 남은 숫자형 경계이다. |
| C9-S3 | Python implementation/version이 scientific application identity에 들어가 runtime 차이만으로 완료 identity가 달라졌다. | 부모 승인 S3. v4에서 runtime은 lease attempt 진단으로 옮겼고 code/contract/input/fixture pin을 유지했다. 정적 CLOSED. |
| C9-S4 | outer env가 없는 경우 상속 lease module import가 보존된 부모 경로에 bytecode를 쓸 수 있었다. | 부모 승인 S4. import 이전 `sys.dont_write_bytecode=True`. 정적 CLOSED. |
| C9-S5 | 첫 fixture 실패에도 보고서의 actual interface evaluations가 literal 16으로 표시될 수 있었다. | 부모 승인 S5. 호출 직전 실제 counter 증가, expected 16과 actual을 분리했다. 정적 CLOSED. |
| C9-S1B | v4는 `complete == expected`와 `encoded(complete) == complete_bytes`를 검사한다. Python의 `16.0 == 16` 때문에 canonical `row_count: 16.0` 변조는 두 조건을 모두 통과할 수 있다. 정확한 완료 bytes 계약이 닫히지 않았다. | 예상 object 자체의 직렬화 `encoded(expected)`를 실제 COMPLETE bytes와 비교한다. 같은 unexecuted matrix에 numeric-type mutation mock guard를 추가하면 충분하다. v4 당시 BLOCK_NOW였고 v5의 실제 diff/readback으로 CLOSED_STATIC이다. 수치 계산이나 물리식 수정은 하지 않았다. |

## 실행·자원·후속 단계

검토자 실행은 정적 파일 읽기와 metadata/hash 확인뿐이다. 새 수치 검증 0, 실제 application 0, 과거 완료 identity 재실행 0이다. 첫 lease 요청과 그 영수증은 있으며, memory 기준으로 배정되지 않아 실제 검증 child는 NOT_RUN이다. 공유 lease의 1 worker / 1 thread / 0.5 GiB 요청, 검증 CPU 30 s / wall 60 s, application CPU 10 s / wall 20 s, 자기 child의 timeout 처리만 있는 경로를 정적으로 확인했다. 상속된 금액 예산 unknown/null을 0 또는 새 예산으로 재설정하지 않는다.

C9-S1B 수정 readback을 마쳐 `GO_TARGETED_VERIFICATION`으로 전이했다. 그 판정은 부모가 최초 계획된 검증 실행 한 번을 승인할 수 있다는 뜻이다. raw 결과와 코드 hash를 읽은 뒤 별도로 16-row 실제 application 진입 판정을 내린다. 실제 application 결과는 다시 읽기 전용으로 검토하며 과학 재실행은 하지 않는다.

REI-L1 연결, consumer-native state/energy binding, transport·spectrum·absorption, coupled thermal/charge trajectory는 OPEN이다. 이 검토는 전역 `CONSUMER_ADMITTED` 또는 production admission이 아니다. `HH_R10=OFF`, `Production admission NOT_ISSUED`를 유지한다. sampled algebraic/energy residual은 continuum certificate가 아니다.


## Workspace 복구와 v5 표적 재검토

환경 초기화는 S0 게시 이후, PHYS84 첫 수치 실행 이전에 발생했다는 부모 보고를 받았다. 실제 복구된 Git HEAD는 동일한 `ce14c0bfc0318662673b021a08f4029d6a36c7a7`이다. `CONTRACT.json`과 이론 유도의 SHA256은 기존 값과 동일하다.

v4의 5개 코드·fixture 파일은 초기화 전 별도로 기록한 해시와 실제 복구 snapshot의 해시가 전부 일치한다. 검토 문서 두 개는 대화에 남은 원래 apply_patch payload에서 복구했다. 초기화 전 검토 문서 파일 해시는 없으므로, 문서에는 원문 복구와 현재 SHA 관측만 주장한다. 원래 HOLD 이력은 동반 JSON과 `/tmp/wu84_review_recovery/reviews/`에 남아 있다. 복구 영수증은 `/tmp/wu84_review_recovery/RECOVERY_RECEIPT.json`과 `/tmp/wu84_code_recovery/RECOVERY_RECEIPT.json`이다.

승인된 v5 변경은 `run_source.persist`의 예상 완료 canonical bytes 비교 한 줄과 해당 숫자형 변조 mock guard뿐이다. `implementation/C9_S1B_REPAIR.diff` 및 실제 변경 위치를 읽었고, 현재 5개 파일은 `implementation/pretest_frozen_v5/SHA256.json`과 일치했다. `source_adapter.py`, `fixtures.json`, `leased_call.py`는 v4와 같다. 변경된 `run_source.py` SHA256은 `a6df009ee87aae6941d5b7bf651338b4594aeb8392cc4c9d74c9cfe05f1516da`, `verify_source.py`는 `1dafea3f8f369d41deeb750aa7181c0d7b0a29146522c1b4e479cece187d8c46`이다.

현재 차단 지적은 0이다. 복구와 정적 재검토는 수치 검증·과학 실행 횟수를 늘리지 않았다. 후속 순서는 공유 lease 아래 원래 검증 한 번, raw 결과의 읽기 전용 독립 판정, 부모의 실제 16-row application 승인이다. 완료된 부모 결과의 재실행이나 추가 검토 순환은 요구하지 않는다.


## 최초 검증 요청의 실제 자원 대기

`verification/ATTEMPT_01.json`과 `ATTEMPT_01_EXTERNAL_RECEIPT.json`을 읽었다. 공유 lease 요청 1회, outer exit 75, lease null, admissible slots 0, live leases 0이다. child와 `verification/attempt_01`은 생성되지 않았다. 예정 fixture interface 16과 실제 호출 0을 분리한다. 검증 PASS assertion, mock 실행, 실제 source application, 새 rate/ODE 결과는 없다. numerical failure 0과 resource-WAIT 1을 구별한다.

`reviews/RESOURCE_GATE_REVIEW_KO.md`가 독립 resource gate 분석이다. 현재 pinned `max-current` 기준에서 available은 약 1.05 GiB이고 reserve1.5 GiB+job0.5 GiB에 미달한다. file cache 진단은 메모리 charge의 구성을 설명하지만, 현재 gate에 active cache credit을 더하는 것은 동일 정책의 단순 보정이 아니다. 부모는 WAIT를 수용하고 pinned guard·reserve·job·공유 lock·hard cap을 유지하기로 했다. 이 reviewer는 guard 변경, reclaim, 자원 재시도 또는 수치 실행을 하지 않았다.

현재 허용되는 후속 작업은 준비된 코드와 실제 WAIT 근거의 게시·백업·인계이다. 과학 실행 S2 완료를 주장하지 않는다. 새로운 평상시 자원 관측이 기존 2 GiB 이상 headroom 및 나머지 lease 조건을 만족함을 보여 줄 때만 부모가 다음 시도를 승인할 수 있다. 이전 PHYS83 완료 science는 계속 재사용한다.
