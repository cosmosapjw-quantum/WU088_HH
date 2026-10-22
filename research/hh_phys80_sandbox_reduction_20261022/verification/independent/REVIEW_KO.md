# PHYS80 독립 코드·유한 대수 검토

## 판정

**PASS_SCOPED — 검토한 최종 소스에서 세 개의 새 isolated ODE 실행을 막는 잔여 구현 결함을 발견하지 않았다.**

이 판정은 고정된 PHYS79 neutral CI + detailed-balance D/H CX 부분계의 4차원 환원, CX-only 1차원 환원, 유한 상태의 원 연산자 접선 비교, analytic Jacobian, 입력/도메인 거부 및 create-only 실행 identity에 한정된다. 실제 ODE 궤적 실행이나 연속 구간 인증을 이 검토에서 수행하지 않았다. HH_R10=OFF, production admission=NOT_ISSUED를 유지한다.

대상 루트는 `/tmp/hh_phys79_work/WU088_HH/research/hh_phys80_sandbox_reduction_20261022`이다. 원래 지정된 `source/reduced.py`, `source/phys79_bridge.py`, `theory/PHYSICS_TO_CODE_GATE_KO.md`에 더해, 부모가 후속 지정한 `source/run_reduced.py`와 `inputs/REDUCTION_PLAN.json`을 검토했다. 고정된 부모 `vendor/phys79/source/collisional.py`의 별도 event operator를 수치 oracle로 사용했다. 해당 부모의 ODE runner나 기존 test suite는 실행하지 않았다.

## 물리와 미분 구조의 검토

H/D neutral CI는 같은 H kinetic fit을 사용한다. 따라서 두 singly ionized abundance의 합 Q에는 CX 항이 정확히 상쇄되고, `dQ/dt=nH*kH*xe*(H+D-Q)`가 남는다. DII=v의 식에는 D의 CI와 양방향 CX가 남는다. He/Li의 각 중성 isotope abundance는 같은 원소의 CI rate를 곱한 선형 소멸식을 따르므로 초기 중성 비율이 보존된다. 구현의 affine lift는 서로 다른 isotope 초기 ion fraction을 허용하며, 서로 같은 fraction만을 가정하지 않는다.

모든 활성 isotope는 neutral 또는 singly ionized 상태에 있으므로 `xe=Q+B*h+L*l`이고 총 입자수는 보존된 원자핵 수에 xe를 더한 값이다. 부모 global ionic potential을 사용한 anchored thermal energy와 이 입자수에서 온도를 복원한다. D/H CX의 43 K rate exponent와 저장된 두 ionic potential의 뺄셈으로 얻은 energy defect를 구분한 것도 올바르다. CI fit threshold를 thermodynamic potential로 바꾸지 않았다.

Jacobian은 고정 온도에서의 반응 미분과 rate의 온도 미분을 `gradT`로 연결한 항의 합이다. `gradT=-(bgrad+CV*T*xgrad)/(CV*N)`의 부호와 입자수 미분 항을 확인했다. 무차원 좌표에 대한 similarity scaling과 proper-time에서 theta-time으로의 나눗셈도 일치한다. 실제 유한 미분은 별도로 공개 RHS/rate 함수에 적용했다.

## 검토 중 발견하여 수정된 사항

아래 사항은 모두 첫 수치 검토 배치 전에 부모가 수정했다. 과거 버전의 결함을 실제로 재실행해 재현한 증거와 혼동하지 않는다. 최종 버전의 거부 동작은 독립 fixture로 확인했다.

| 발견 사항 | 영향 | 최종 확인 |
| --- | --- | --- |
| truthy 비불리언 `d_cx`가 내부 True로 변환될 수 있었음 | 선언한 물리 설정과 실제 활성 과정 불일치 | `d_cx is True`, 비활성 플래그 `is False` 거부 검사 PASS |
| pinned 파일 SHA 확인 뒤 bare import가 기존 동명 module cache를 사용할 수 있었음 | 검증한 파일과 실제 사용한 모듈이 달라질 수 있음 | 세 부모 모듈의 실제 경로 확인 및 외부 cache 주입 거부 PASS |
| 매우 작은 음의 raw Q/v가 anchored subtraction에서 y=0으로 둥글려질 수 있었음 | lift guard를 통과한 뒤 raw RHS에서 음의 하전량을 사용할 수 있음 | raw HII/HI/DII/DI와 h/l 부호·범위 검사 PASS |
| receipt 없이 남은 NPZ/checksum이 READY로 분류될 수 있었음 | 부분 완료 identity를 다시 적분할 수 있음 | orphan NPZ/checksum 모두 BLOCKED PASS |
| claim 경쟁의 후발 프로세스가 선발 소유자의 실패 receipt를 만들 수 있었음 | 진행 중이거나 성공한 결과의 identity를 오염시킬 수 있음 | 결정적 경쟁 fixture에서 `BLOCKED_UNOWNED_ATTEMPT`, ODE 0, science receipt 쓰기 0 |

추가로 초기 isotope inventory metadata와 reference clock의 일치 검사가 반영된 최종 버전을 확인했다.

## 실행과 결과

| 명령 | 종료 상태 | 해석 |
| --- | --- | --- |
| `python -B /tmp/phys80_review/independent_check.py` | 1 | 16개 논리 점검군 중 15 PASS. 야코비안 차분 fixture 한 점이 물리영역 경계를 가로질러 거부됨. 첫 실패 보존 |
| `python -B /tmp/phys80_review/jacobian_interior_supplement.py` | 0 | 위에서 도달하지 못한 마지막 3점만 검증. 첫 경계점은 새 내부점으로 대체. 완료 야코비안 점 재실행 0 |

첫 실패는 **TEST_FIXTURE_OUTSIDE_STRICT_PHYSICAL_DOMAIN**으로 분류한다. 변형 IC는 Li6의 초기 ion fraction을 정확히 0으로 설정했다. aggregate Li ionization을 감소시키는 중앙차분점은 Li6II를 음수로 만들므로, strict physical guard가 이를 거부하는 것이 올바르다. 생산 코드를 바꾸거나 guard를 완화하지 않았다. 이전의 완결된 9개 야코비안 점은 재사용하고 마지막 세 점만 추가했다. 최초 receipt와 최초 검토 script는 그대로 보존한다.

| 요구·위험 | 유한 증거 | 관측 결과 |
| --- | --- | --- |
| pinned 입력/부모 소스 | 15개 파일 길이 및 SHA256, 실제 import 경로 3개 | PASS |
| 저장 IC와 초기 lift | C01/C02 2개 상태 | y/u/T 복원 오차 관측상 모두 0 |
| 서로 다른 isotope 초기 ion fraction | 추가 2개 IC, 한 isotope 완전 ionized 및 한 isotope ion fraction 0 포함 | 초기 y 복원 오차 0, 초기 lift weights 유한 |
| 원 21-species event operator와 22-state 접선 | 13개 상태 | reaction-constituent 정규화 최대 오차 `3.8179583055020773e-16` |
| 유한 상태 isotope 보존 | 같은 13개 상태 | 최대 상대 오차 `1.8375257965013053e-16` |
| 유한 상태 total energy | 같은 13개 상태 | 최대 상대 오차 `1.6813866964115292e-16` |
| 접선 isotope/energy 보존 | 같은 13개 상태 | isotope 잔차 0; energy 정규화 최대 `7.259795917415648e-17` |
| analytic Jacobian | 본 배치 9점/27열 + 추가 3점/12열 = 12점/39열 | 모든 완료 비교가 사전 `2e-6` gate 통과 |
| 추가 3점의 Jacobian 수치 | 독립 5점 중앙차분, 새 RHS 평가 48회 | component 최대 `2.5029018238764215e-10`, row 상대 최대 `6.5206637494108914e-12` |
| CI/CX rate derivative | 23개 rate/temperature 점 | 최대 상대 오차 `1.3290252564814759e-9`; rate 값은 부모 함수와 정확히 동일 |
| 거부 경로 | 64개 기대 예외 | unsupported IC/물리, 비유한 값, raw 음수, source-domain, off-manifold encode, 손상 receipt/NPZ, mesh 상태 모두 거부 |
| identity 보존/재사용 | 10개 runner fixture | COMPLETE byte-preserving skip, 실패/부분 차단, claim 경쟁 보호 PASS |
| 실제 import 객체의 pin 경계 | 별도 인터프리터 3개 | 세 fake cached module 모두 거부 |

본 배치의 첫 9개 완료 야코비안 점에 대해서는 `2e-6` gate 통과가 기록된 제어 흐름과 완료 counter로 확인된다. 그 뒤 예외가 발생하여 해당 함수의 point별 numeric maxima 반환값은 receipt에 실리지 않았다. 따라서 추가 3점의 maxima를 전체 12점의 최대라고 주장하지 않는다.

### 실행 집계의 의미

16은 논리 점검군 수다. 13개 접선점, 23개 rate 점, 64개 거부 경로, 3개 import subprocess를 각각 별도 논리 test suite 수로 더하지 않는다. 본 배치 1회와 미완료 영역의 보완 배치 1회를 실행했으며, 예전 suite 실행 0, ODE 실행 0, 원격 변경 0, live lease 변경 0이다. 본 검토에서 만든 파일과 fixture는 `/tmp/phys80_review`에만 있다.

첫 receipt의 `finite_difference_function_evaluations=216`은 stencil 진입 때 4씩 더하는 예산 counter다. 마지막 실패 stencil은 첫 함수 평가에서 중단되었으므로 이 숫자를 실제 완료 함수 호출 수로 쓰면 안 된다. 보존한 script의 제어 흐름상 본 배치는 성공 평가 212회와 거부된 평가 1회, 합계 213회다. 보완 배치의 48회는 함수 진입에서 직접 센 실제 RHS 평가 수다. 이 구분은 production 실행 집계와 무관하다.

영수증을 요약하려던 읽기 전용 Python 명령 한 번은 입력 typo로 SyntaxError를 냈고, 즉시 올바른 읽기 명령으로 확인했다. 그 명령은 수치 검사를 수행하지 않았으며 scientific execution 수에 포함하지 않는다.

## runner 정적 검토와 남는 경계

`prepare`의 science identity는 실제 parent physics, parent comparison identity, 새 model, 수치 설정, source manifest 및 Python/NumPy/SciPy 버전을 묶는다. 세 새 identity는 부모 완료 identity와 겹치지 않는다. 표시용 task label만 바꾼 alias는 같은 science identity를 유지하고, 수치 tolerance 변경은 다른 identity가 된다.

`execute_one`은 source manifest를 solve 전후에 확인하고, create-only claim과 호출 marker를 만든 뒤 한 번만 solve를 호출한다. 완료 receipt와 NPZ의 바이트 확인 후 skip하고, 실패 및 부분 identity를 자동 재시도하지 않는다. claim을 소유하지 못한 프로세스는 별도 diagnostic만 남긴다. shared lease는 각 새 실행 앞에서 취득하고 finally에서 반환하는 구조다. 이 검토는 실제 lease를 취득하지 않았고 live 다중 프로세스 과부하 시험을 하지 않았다.

모든 RHS/Jacobian callback은 strict state 및 활성 rate source-domain guard를 거친다. solver가 반환한 모든 accepted endpoint는 `full_states`로 다시 검사한다. 161개 dense sample도 같은 경로로 검사하고, 부모의 저장 궤적 및 기존 보존/열/평형 진단과 비교한다. finite negative-state 및 out-of-source-domain mesh fixture가 거부됨을 확인했다.

현재 코드의 accepted-mesh 정량 진단은 positivity, thermal energy, rate domain 및 total energy다. isotope relative gate는 dense 161개 점에서 별도로 계산한다. accepted mesh의 isotope residual을 추가로 기록하면 보고가 더 분명해지지만, 현재 affine lift와 유한 보존 검토에서 실행 차단 결함은 아니다. mesh 전체의 실제 결과는 root가 새 ODE를 실행한 뒤 별도 receipt로 확인해야 한다.

이 검토로는 아래를 주장하지 않는다.

- 전체 dense interpolant 또는 시간 연속 구간의 positivity/오차 인증.
- 실제 새 ODE의 성공, refinement gate 통과, 부모 궤적과의 최종 수치 일치.
- 원래 CI/CX source의 저온 정확도, 새 물리 과정의 허가, full cosmological admission.
- 실행 시간 성능 향상이나 다른 host의 재현성.
- 지정된 문서의 Wolfram symbolic-zero 결과에 대한 도구 호출·응답 검증. 읽은 시점의 theory 디렉터리에는 계약 문서만 있었고, symbolic receipt는 이 독립 검토의 증거에 포함하지 않았다.
- 원격 Git ancestry, PR publication 또는 backup delivery 확인. 이 검토의 byte identity는 지정된 로컬 snapshot에 대한 것이다.

## 환경과 exact hashes

Python `3.12.14`, NumPy `2.3.5`, SciPy `1.17.0`. OMP/OPENBLAS/MKL/NUMEXPR/VECLIB/BLIS thread 환경값은 모두 1이다. `-B`로 검토 대상 디렉터리의 bytecode 쓰기를 피했다.

| 대상 | SHA256 |
| --- | --- |
| `source/reduced.py` | `2029eac4b5e23e25158742ae79ba47bb9dcacaf95faba59237c7518195b201a9` |
| `source/phys79_bridge.py` | `53d01690dadf20d526e3e352cf01906538b45659dcadcc08210c8c0abc915262` |
| `source/run_reduced.py` | `396c59328ae3cec8f31b06fb9fa97de20b9717526ae8770950c73247ae3da320` |
| `theory/PHYSICS_TO_CODE_GATE_KO.md` | `d1823463fb62e99e40b634f82a9b1d4875a6b41b522cd7398fb074050e74df08` |
| `inputs/REDUCTION_PLAN.json` | `449d80fb3f76caec15685a2b811ee2acc6297b9b77a45d2d373b4a6a682f74dc` |
| `vendor/PHYS79_PROVENANCE.json` | `aca6625e48a23d6325de841ea5a8d9ded92678bb0561b13b6b2d3f30da8c3779` |
| `independent_check.py` | `03fcf321efd0afccd432ad5f3fe37a878ed5da511a51de30a019e7b3389b0ba0` |
| `check_result_001.json` | `32b83ccb002f243600a91b0b5c9ad0fc136ac344bdc229064658df7413fc6654` |
| `jacobian_interior_supplement.py` | `f9af3e2176adb06bd4cff999f6b458bb7b5cc52608cea767c66719d6a7231663` |
| `jacobian_supplement_001.json` | `f46d74f910759832229364b2c66b99cb49ae0e5d232969c18a442f432347599d` |

**HH_R10=OFF. Production admission NOT_ISSUED.**
