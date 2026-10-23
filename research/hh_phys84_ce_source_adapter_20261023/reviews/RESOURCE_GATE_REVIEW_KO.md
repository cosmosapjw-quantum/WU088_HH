# PHYS84 공유 자원 gate 독립 검토

## 판정

**WAITING_FOR_SHARED_LEASE를 유지한다.** 현재 근거에서 자원 판정 코드의 오독이나 산술 오류는 발견하지 않았다. clean file cache를 가용 메모리에 새로 더하는 것은 현행 판정식의 적용 의미를 바꾸므로, 이번 사건을 정책을 유지한 단순 observation 보정으로 분류할 수 없다. C9의 v5 정적 구현 판정은 `GO_TARGETED_VERIFICATION`으로 유지하지만, 실제 검증은 자원 미배정으로 **NOT_RUN**이다. 수치 실패나 16-row application 실패가 아니다.

이 검토는 `/root/adapter_independent_review`가 실제 receipt와 고정된 `observe_resources`, `resource_slots`, `LeasePool.acquire` 코드를 읽은 독립 분석이다. source guard 수정, lease 획득 재시도, kernel 설정 변경, 수치 테스트, application 실행을 하지 않았다. 이번 판정은 관측한 환경에서의 실행 허용 상태이며, cache를 다루는 모든 미래 자원 정책에 대한 불가능성 명제가 아니다.

## 실제 근거와 실행 회계

| 근거 | SHA256 또는 실제 내용 |
|---|---|
| `verification/ATTEMPT_01.json` | `544b917197ed1e55f580180721ac808e0713ef8bc58f422c1a7545874072f4d1` |
| `verification/ATTEMPT_01_EXTERNAL_RECEIPT.json` | `dfd145eaaadb886fb75ab2efc75b31ce94c86b332f3523332352f1097b56c4cf` |
| `verification/RESOURCE_DIAGNOSIS_01.json` | `a779d79676a96444b1ae5771c607cc725835d36f88cf4c76af29e212b87a1d11` |
| 상속 lease source | `../hh_phys83_ce_completion_20261023/source/vendor/phys78_run_pilot.py`, SHA256 `76ff57ba687fd9830b84c3fcff69eb8ed0e9f6ceab4551e61c67c84d3ea65124` |
| 실행 결과 | outer exit 75, `lease=null`, `admissible_slots=0`, `live_leases=0`, `WAITING_FOR_SHARED_LEASE` |
| 검증 child | 시작되지 않음. `verification/attempt_01`과 실제 검증 REPORT는 없음. |
| 수치 회계 | 검증 테스트 0, fixture interface 호출 0, mock persistence callback 0, 실제 application callback 0, 기존 과학 callback 0 |

처음 승인한 실행 명령이 공유 lease를 요청한 사건은 1회로 보존한다. 이 사건을 완료된 검증 1회나 수치 실패 1회로 집계하지 않는다. 16개 fixture interface 호출은 예정값이며 실행된 값은 0이다. 새로운 rate, population solve, ODE, 완료 identity 재실행도 0이다.

외부 receipt의 `outer_tool_wall_seconds`는 바깥 도구의 관측값이다. 실행되지 않은 child의 CPU 또는 wall 비용으로 바꾸어 적지 않는다. 상속 금액 예산의 spend/remaining/currency는 null로 유지하고, 자원 거부를 예산 0 또는 새 예산의 근거로 쓰지 않는다.

## 고정 판정식의 적용

`observe_resources`는 host의 `MemAvailable`로 시작한 뒤, 각 유한한 cgroup memory limit에 대하여 다음 값을 취한다.

\[
A=\min\bigl(\mathrm{host\ MemAvailable},\ \max(0,\mathrm{memory.max}-\mathrm{memory.current})\ \text{for every finite cgroup}\bigr).
\]

`resource_slots`는 실제 관측 A와 전체 capacity에서 각각 reserve를 뺀 값, 살아 있는 lease의 예약량, CPU headroom을 함께 사용한다. local reserve는 1.5 GiB, 한 job의 lease는 0.5 GiB이다. 따라서 memory 기준으로 새 1개 slot을 열려면 A가 최소 2.0 GiB이어야 하고, capacity 및 CPU 조건도 동시에 충족해야 한다. lock 안에서 live lease를 다시 읽으며 다른 process의 lease를 지우거나 우회하지 않는다.

attempt01에서 A는 `1.0545654296875 GiB`이다. reserve를 뺀 값은 `-0.4454345703125 GiB`이므로 slots 0은 고정식과 일치한다. capacity 8 GiB, sampled idle CPU 약 7.98, live lease 0이어도 memory 최소 조건은 충족되지 않는다. 이 관측에서 필요한 2.0 GiB까지의 headroom 차이는 약 0.9454 GiB이다.

## Cache 진단이 말해 주는 것과 남은 차이

후속 읽기 전용 진단은 다음을 기록했다. 이는 acquire 시점과 다른 시점의 관측이므로 두 snapshot을 합쳐 하나의 동시 관측으로 취급하지 않는다.

| 항목 | 진단에 저장된 bytes |
|---|---:|
| `memory.max` | 8,589,934,592 |
| `memory.current` | 7,447,642,112 |
| `anon` | 107,872,256 |
| `file` | 7,048,933,376 |
| `shmem` | 0 |
| `file_dirty` | 4,505,600 |
| `file_writeback` | 0 |
| `inactive_file` | 484,655,104 |
| `active_file` | 6,564,278,272 |

이 수치는 현재 charge의 대부분이 file 계열이라는 진단을 지지한다. 그러나 이 파일에는 어느 양이 어느 시점에 실제로 회수되어 현행 `memory.current`를 줄일지에 대한 보장이나 관측 결과가 없다. host `MemAvailable`이 충분하다는 부모 보고 역시 제한된 cgroup의 raw charge headroom을 대신하지 않는다. 현재 코드가 두 제한 중 작은 쪽을 쓰는 것은 의도된 동작이다.

낙관적으로 `inactive_file` 약 0.45 GiB 전부를 새 credit으로 더한다고 가정해도 후속 raw headroom 약 1.06 GiB와 합친 값은 약 1.51 GiB로, 2.0 GiB 조건보다 작다. 실제 통과를 만들려면 상당한 active file charge까지 credit으로 인정해야 한다. 이는 현재 gate가 관측하는 `max-current`를 다른 memory admission 추정치로 교체하는 행위이다. 이번 읽기 자료만으로 그 credit을 현행 reserve와 동등한 보장으로 볼 수 없다.

공유 lock은 협력 lease들의 중복 예약을 제어하고 CPU/wall hard cap은 해당 child의 CPU·시간을 제한한다. 이 두 제어가 file cache의 회수량을 보증하거나 별도의 hard memory bound가 되는 것은 아니다. 따라서 lock과 CPU/wall cap을 그대로 남긴다는 이유만으로 memory 측정 정의 변경을 현행 조건과 동등하다고 판정하지 않는다.

## 다음 행동

1. 지금은 source·verification 코드, reserve 1.5 GiB, job 0.5 GiB, 공유 lock, CPU/wall cap과 pinned lease source를 모두 유지한다.
2. kernel reclaim endpoint는 존재하지만 writable=false로 관측되었다. 이 검토는 여기에 쓰거나 sysfs/cgroup 설정을 바꾸는 권한을 부여하지 않는다. 다른 process의 종료, 공유 cache 강제 제거, 메모리 부하를 인위적으로 만들어 회수를 유도하는 동작도 요청하지 않는다.
3. 환경의 가용 headroom이 실제로 달라진 근거가 생기면 부모가 기존 guard를 사용한 다음 bounded 시도를 결정할 수 있다. 같은 관측 상태에서 반복적으로 gate를 호출하거나 callback을 lease 밖에서 실행하지 않는다. 최초 수치 검증은 아직 실행되지 않았으므로 완료 과학을 반복할 이유가 없다.
4. 검증이 시작될 때까지 raw 수치 PASS, 실제 source application 완료, consumer admission을 발급하지 않는다. 정적 코드 snapshot·실제 WAIT 영수증·미실행 상태의 게시 및 백업 준비는 계속할 수 있다.

나중에 cache-aware 자원 관측을 연구한다면 그것은 근거·동등성·공유 소비자 호환성을 명시할 별도 변경이다. 현재 PHYS84의 원래 검증을 통과시키기 위해 이 자리에서 정책을 바꾸지는 않는다. 본 사건의 독립 판정은 **정적 검토 GO / 자원 배정 WAITING / 수치 검증 NOT_RUN / 실제 application 0**이다.
