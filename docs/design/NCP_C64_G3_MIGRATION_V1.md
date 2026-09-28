# WU088_HH: NCP c64-g3 migration design v1

Status: PROPOSED_DESIGN_ONLY. 이 문서는 구현, 성능 검증, 과학적 승격 또는 유료 자원 생성의 완료 보고가 아니다.

기준 commit: `2d400ea785e2f2cc80a07e1eb0c27de7d00a69c7` (`r31t-z1-discriminator`). 설계 branch 외의 기존 branch, frozen source, runtime, checkpoint 및 원격 백업은 변경하지 않는다.

## 1. 목적, 전제, 완료 기준

사용자가 선택한 Naver Cloud c64-g3 한 대에서 WU088_HH의 남은 heavy source 계산을 이어간다. 사용자 PC는 Ryzen 9 5900X / RAM 96 GB다. 완료된 local anchor, midpoint, z=2 결과는 원래 provenance를 보존한 읽기 전용 입력으로 재사용한다. 클라우드 사용은 기존 heavy-local 운영의 명시적 변경이지만, 수치 정밀도, frozen107 모델, provider family, convergence와 interpolation 기준의 변경을 뜻하지 않는다.

목표는 CPU 사용률 자체가 아니라 **같은 검증 수준으로 승인 가능한 source node 한 개를 얻는 총 wall time과 비용**이다. 총시간에는 초기화, native build, 계산, checkpoint, upload/readback, 최종 seal이 모두 들어간다. c64-g3의 실측 성능과 정확한 CPU 모델은 아직 확인하지 않았다.

이 설계는 한국 일반 VPC, x86-64 Linux를 기본 전제로 한다. 실제 이미지, zone, 계정별 가격, 가용 물량, disk와 network 조건은 생성 콘솔에서 확인해야 한다. 서버 생성, 과금 작업 시작, 계정 권한 변경, 삭제는 이번 문서 게시 범위에 없다.

## 2. 확인된 플랫폼 정보와 미확인 정보

공식 Server 가이드에서 g3는 KVM이며, CPU 타입 접미사가 없는 c 계열은 Intel이다. High CPU 64 vCPU / 128 GB 행의 상한은 network 5 Gbps, storage throughput 1,188 MB/s, 100,000 IOPS다. 이는 서버 수준 상한이지 개별 disk 성능이나 실제 external backup 처리량을 보장하는 수치가 아니다. [S1]

64 vCPU를 64 physical cores 또는 반드시 32 cores x SMT2라고 간주하지 않는다. 실제 Xeon 모델, guest topology, host CPU 배치, NUMA와 cache locality는 별도 확인 대상이다. guest에서 보이는 topology가 물리적 배치를 완전히 설명한다고 주장하지 않는다.

공개 일반 한국 요금표에 High CPU-g3 64/128은 시간당 3,192원, VAT 별도로 표시된다. disk는 별도다. 이는 설계용 공개 견적이며 사용자에게 적용되는 최종 견적은 콘솔에서 재확인한다. [S2]

## 3. 현재 코드에서 이식을 막는 구체적 지점

다음은 기준 commit의 실제 코드에 대한 관찰이다.

| 위치 | 현재 동작 | NCP 설계의 처리 |
| --- | --- | --- |
| `scripts/benchmark_pool.py` | physical budget은 min(12, ...), logical budget은 min(24, ...), pair 표본도 최대 12 | 자원 예산과 workload 크기를 분리하고 최대 64 guest vCPU 구성을 검증 |
| `scripts/wide_hybrid_orchestrator_cost.py` | auto/cloud lane에서 긴 계산을 HANDOFF_LOCAL_REQUIRED로 전환 | sandbox 제한을 우회하지 않고 별도 명시적 ncp lane 추가 |
| 같은 orchestrator | persistent pool은 한 bounded wave 안에서만 유지 | native 초기화와 worker pool을 node 수명 동안 유지 |
| 같은 orchestrator | tuned 경로에서 fork context 사용 | spawn 기반의 import-safe persistent worker 경로를 별도 구성 |
| `hardware.py` | L3가 없으면 cpu0 같은 label을 생성한 뒤 숫자 CPU-list parser에 전달 | virtual/unknown topology를 정상 상태로 처리하고 label과 CPU 목록을 분리 |
| `scripts/build_native.py` | source/flags/compiler/platform으로 build key 생성 | 실제 binary와 의존 library, ABI까지 build identity에 추가 |
| `AGENTS.md` | heavy local 정책 | 사용자 승인에 맞는 ncp lane 계약을 별도 명시 |
| R31T metadata probe | any common checksum 일치 여부를 보고 | MD5-only 일치를 raw SHA256 복원 검증과 동일시하지 않음 |

R31T 문서는 z=2에서 계산 scheduling 효율은 이미 높고 remote delta transaction/readback 지연이 크다고 보고한다. 이 문서는 그 timing을 독립 재실행한 것이 아니다. 더 큰 CPU만으로 전체 시간이 CPU 수에 비례해 줄어든다고 예측하지 않는다.

## 4. 선택한 구조

세 가지 접근을 비교한다.

1. 기존 shell을 거의 그대로 VM으로 옮기는 방법은 변경 위험이 작지만 12/24 제한, host profile 불일치, 반복 초기화와 backup barrier가 남는다.
2. **단일 VM + host-specific tuning + persistent executor + 검증된 비동기 백업**을 권장한다. 기존 scalar/native 수학을 유지하면서 현재 병목에 직접 대응한다.
3. 여러 VM, MPI, Slurm, Kubernetes 또는 GPU 재작성은 현재 144-pair/node 작업에 비해 운영과 검증 범위가 커지므로 이번 범위에서 제외한다.

역할 분리는 다음과 같다.

- GitHub: source, 명세, manifest, 작은 검증 보고서의 정본.
- NCP VM: 새 heavy pair 계산과 bounded regression.
- 사용자 PC: 제어, 기존 데이터 보관, 결과 열람. VM이 멈춰도 사용할 수 있는 stop/watchdog 위치의 후보.
- Sandbox: 가벼운 수식 검산, source audit, assembly 및 gate 후처리.
- Drive + Dropbox: 기존 독립적인 두 원격 백업 경로 유지. NCP Object Storage는 필수 의존성이 아니며 이를 추가해도 두 경로를 자동 대체하지 않는다.

새 workspace는 예를 들어 `/srv/wu088_hh` 아래에 `authority/`, `builds/`, `runs/ncp-c64g3/`, `spool/`, `receipts/`를 분리한다. 이것은 경로 설계이며 아직 존재하는 디렉터리나 실행 명령이 아니다.

## 5. 재사용과 identity 경계

네 종류의 identity를 분리한다.

- Scientific identity: frozen source/model, basis와 phase convention, quadrature grid/weights, geometry, provider family, dtype/precision 요구사항.
- Build identity: compiler binary와 flags, native source, 생성 binary, libm/libstdc++/libgcc/libgomp 등의 실제 의존 library, ABI.
- Execution identity: NCP instance/boot 식별자, guest CPU 정보, affinity/quota, thread layout, OS/kernel, environment와 scheduling policy.
- Artifact identity: 파일의 raw SHA256, size, manifest, remote object/revision 식별자.

완료된 local node는 원래의 build 및 artifact identity 그대로 읽는다. 이를 NCP에서 만들었다고 다시 라벨링하지 않는다. 실행 환경이 달라도 승인된 입력 node를 소비하는 행위와, 다른 build의 primitive pair들을 한 미완성 state에 섞어 재개하는 행위는 다르다.

새 z=1 H160/H192 및 필요한 provider는 새 NCP execution namespace에 기록한다. 기존 host의 미완성 pair와 새 cloud pair의 혼합은 기본 금지한다. 동일 build/입력/ABI를 증명한 별도 resume admission 없이는 hybrid state를 만들지 않는다. 절대경로 변경은 locator adapter로 처리하고 원본 manifest를 편집해서 해시를 맞추지 않는다.

기존 CP4와 runtime seed는 데이터/소스 authority다. 새 venv 및 build cache는 새로 생성한다. CP4에 포함된 오래된 ELF는 무조건 실행하거나 무조건 재컴파일하지 않는다. 원본 bytes와 provenance를 보존하고 compatibility를 먼저 검사한다. rebuild가 필요하면 새 provider build로 분리하고 원본을 덮어쓰지 않는다.

## 6. bootstrap과 cross-host 수치 검증

Native startup 전에 다음을 검사한다.

- 회수할 CP4/runtime/완료 node의 exact archive SHA, 내부 source/array manifest.
- venv 및 dependency lock. 기존 Python/NumPy/SciPy pin을 회수하며, cloud에서 실제 지원되고 동일 grid가 생성되는지 검사.
- shell이 첫 Python을 띄우기 전 child environment에서 LD_PRELOAD와 LD_LIBRARY_PATH 제거. 이미 시작된 process의 loader 효과를 뒤늦게 지웠다고 주장하지 않음.
- ionic call graph의 duffy_polar_double, duffy_polar, diagonal, half_hermite 전체: source-bound SHA, ELF, architecture/loader dependency, owner execute mode. noexec mount도 확인. hash drift는 chmod나 rebuild로 덮지 않고 중단.
- long double storage size와 significand/exponent, byte order, numpy/C ABI, FE_TONEAREST. 16-byte 저장 공간을 113-bit 유효 정밀도로 혼동하지 않음.
- reference와 candidate를 side-by-side build. fast-math와 FP contraction은 기존대로 금지. 처음부터 march=native 등 추가 flags를 넣지 않음.

검증은 세 단계다.

A. **같은 NCP host의 reference 대 candidate**: foreign value와 sumabs의 exact numerical-array equality, thread 수와 affinity 확인.

B. **Ryzen golden data 대 NCP reference**: 같은 입력의 대표 H0/foreign pair, OD/JVP 및 ionic 경로를 비교한다. 우선 exact numerical equality를 목표로 한다. 불일치가 나오면 dtype, signed zero, ABI, libm, 누적오차를 구분한 별도 보고서로 중단한다. H order-comparison의 2e-7 Eh를 migration rounding 허용오차로 재활용하지 않는다. 완화된 기준은 별도 사전 정의와 승인 없이는 도입하지 않는다.

C. **새 node의 본래 과학 gate**: H160/H192 convergence, same-z provider binding, full49, 해당 interval interpolation 검사는 원래 순서대로 수행한다. A/B가 C를 대신하지 않는다.

대표 regression은 기존 실제 pair의 fast/median/slow 및 phase/cancellation 영역을 포함해 작은 사전 고정 집합으로 제한한다. 기존 전체 anchor 계산을 반복하지 않는다. B160만의 일치를 B192 전체 검증으로 승격하지 않는다.

`np.array_equal`에 의한 수치 배열 일치와 NPZ/raw byte 동일성은 구분한다. timing scalar, 압축 메타데이터, long-double padding 때문에 파일 bytes는 별개의 검증이다.

## 7. 64 vCPU 병렬화와 benchmark

관리하는 모든 계산 stage의 예산을 합산한다. 유효 CPU 수는 허용 affinity와 cgroup quota를 함께 반영한다. 불완전한 core/L3 정보 때문에 임의로 하나의 physical core로 축소하거나 가짜 CCD를 만들지 않는다. topology가 충분하지 않으면 guest-vCPU affinity만 사용하는 정상 fallback을 둔다.

H 경로의 실측 후보는 P=outer processes, T=inner native threads로 다음과 같다.

| guest worker budget | 후보 P x T |
| --- | --- |
| 64, 계산 전용 비교 | 64x1, 32x2, 16x4, 8x8, 4x16 |
| 32, 규모효율 비교 | 32x1, 16x2, 8x4, 4x8 |
| control/backup 여유를 둔 비교 | 15x4=60, 10x6=60, 7x8=56 |

16x4와 8x8은 첫 탐색 후보이지 성능 측정으로 선정된 default가 아니다. 초기 보수적 12-unacked 정책에서는 실제 production P가 12를 넘을 수 없으므로 8x8/4x16 등으로 제한한다. 32/64 outer worker science 실행은 아래 V3 정책을 승인한 이후에만 가능하다.

현재 foreign-only benchmark로 전체 H layout을 결정하지 않는다. H0 + foreign + serialization + checkpoint를 포함한 end-to-end workload를 추가한다. P workers 비교에는 최소 2P tasks를 공급하고, 동일한 144개 canonical pair 중 사전 고정 workload를 사용한다. 최소 3회 순서를 회전해 median과 산포, CPU time, memory, steal time, I/O wait, readback 시간을 분리 기록한다. 시간 예산이 부족하면 표본 부족으로 표기하고 최적값을 확정하지 않는다.

OD/JVP는 현재 serial native pair 경로이므로 outer-only P=16,32,64를 별도 평가한다. H용 profile을 그대로 적용하지 않는다. ionic은 기존 thread contract를 유지하며 동시 node 실행 시 전역 CPU 예산을 소비한다.

Guest NUMA와 affinity 정보가 유효할 때만 worker group 및 memory first-touch를 일치시킨다. L3 locality는 측정 가능한 힌트이지 NCP에서 Ryzen CCD 구조가 재현된다는 가정이 아니다.

## 8. 수학을 바꾸지 않는 가속 범위

현재 gamma plane의 독립 계산과 canonical h-order 합산, 각 plane 내부 compensated sum 순서를 유지한다. 새 executor는 작업 순서와 생존 기간만 바꾸며 과학적 덧셈 순서를 바꾸지 않는다.

공통 Gaussian 인자 hoisting과 exact-zero mask는 이미 있는 최적화다. 이를 새 발견으로 세지 않는다. cache는 model/grid/geometry/source key로 묶인 동일 입력의 재사용에 한정한다. 고차원 적분을 근사 table lookup으로 대체하거나 threshold screening을 추가하지 않는다.

현재 long-double 및 binary128 경로를 binary64 SIMD로 바꾸는 것은 migration 범위가 아니다. SIMD 폭이나 AVX 지원이 커져도 해당 scalar 정밀도 경로가 자동 가속된다고 주장하지 않는다. 정확한 reflection은 기존 승인 범위로 유지하고, 검증되지 않은 primitive ia/ib 교환 대칭을 사용하지 않는다.

Raw linear interpolation 실패는 더 큰 CPU로 수학적으로 해소되지 않는다. 예를 들어 F(z)=a exp(i omega z)의 일정 amplitude 중점에서 선형 chord 오차는 |a| |1-cos(omega h/2)|다. 이는 phase-aware 방법을 별도로 연구할 물리적 동기이지 현재 실패의 정량적 설명이나 새 interpolation의 승인 근거가 아니다. 새로운 phase-factored approximation은 기존 실패를 보존한 별도 preregistration에서만 다룬다.

## 9. Persistent executor와 메모리

Worker는 spawn으로 시작하고 자신의 affinity 설정 후 native library와 입력을 초기화한다. parent는 native build를 한 번 수행하되 OpenMP region을 실행한 process를 반복 fork하는 구조에 의존하지 않는다. Python 문서는 multithreaded process의 안전한 fork가 문제될 수 있음을 명시한다. [S3]

Worker pool은 한 node의 여러 checkpoint/ACK 경계를 가로질러 유지한다. grid/immutable coefficient는 읽기 전용 mmap/shared representation으로 전달하고, native scratch buffer는 worker-local이다. geometry 교체 시 cache invalidation과 task identity를 검사한다. 각 archive/state의 writer는 하나다.

Memory 목표는 128 GB를 채우는 것이 아니다. 유효 memory는 guest MemTotal과 cgroup limit의 작은 값으로 정의하고, 계산+cache 목표를 그 75% 이내로 둔다. 처음에는 전체 유효 memory의 20% 이상을 OS/page cache/backup 및 예외 상황에 남긴다. 일관된 자원 산정은 공유 memory를 중복 합산하지 않도록 USS/PSS와 cgroup accounting을 함께 쓴다. 예산이 임계값을 넘으면 새 작업 제출을 중지한다.

Block Storage의 별도 workspace 100 GB를 초기 용량 후보로 두되, 실제 archive+extraction+build+spool 크기와 여유 20%를 확인한 뒤 결정한다. 기존 PC의 2 TB drive를 통째로 복제하지 않는다. checkpoint의 유일한 복사본을 RAM/tmpfs에 두지 않는다.

## 10. Durability: 호환 모드와 제안된 V3 모드

이 둘은 다른 정책이다. 승인 없이 12-pair 계약을 확대하지 않는다.

### M0: 보수적인 이식 검증

기존 최대 12 unacknowledged pair 및 Drive+Dropbox raw SHA256/size readback을 유지한다. NCP 수치 equivalence와 실행 경로를 검증하는 초기 단계다. 유료 성능 비교에서도 이 제한을 숨기지 않는다.

### M1: 권장 V3 bounded async policy, 승인 전 비활성

- 완성된 pair 16개 또는 flush timer 60초에 도달하면 immutable delta를 seal한다.
- 계산과 dual upload/raw readback을 서로 겹친다. worker pool은 계속 유지한다.
- **완료했지만 양쪽 검증을 마치지 않은 pair + 실행 중 예약한 pair의 합을 전역 최대 128개**로 제한한다.
- 추가 spool 한도 64 MiB, 미확인 artifact age 120초를 backpressure 기준으로 둔다. 하나라도 한계에 도달하면 새 계산 제출을 멈추고 검증을 따라잡는다.
- count를 예약한 뒤 task를 제출하여 in-flight 작업 때문에 상한이 뒤늦게 초과되지 않게 한다. 최악 pair payload 상한도 제출 전 byte reservation에 반영한다.
- 120초는 새 제출 중단 기준이지 이미 실행 중인 native call의 완료나 전체 wall time에 대한 hard guarantee가 아니다.
- retry는 횟수와 시간 예산으로 제한하고, 한 provider 장애 시 성공 ACK를 만들어 진행하지 않는다.
- delta와 최종 node seal 모두 처음에는 기존 dual raw SHA256/size readback을 유지한다. 검증 방법을 낮추지 않고 critical path에서 기다리는 시간을 줄이는 설계다.

**Trade-off:** M1은 확인된 데이터의 검증을 약화하지 않지만, VM과 미백업 disk까지 상실했을 때 다시 해야 할 작업의 상한을 12에서 최대 128 pair로 늘린다. 즉 RPO 정책 변경이며 명시적 승인이 필요하다. count에는 아직 완료되지 않은 계산도 포함하므로 실제 유실 파일 수는 이 상한보다 작을 수 있다.

새 V3 queue/receipt schema를 사용하고 old dual-raw ACK history는 수정하지 않는다. 완료 순서와 canonical scientific contraction 순서는 분리한다. raw scientific payload에 volatile lease timestamp를 넣지 않는다. 기존 receipt가 있으면 먼저 해당 sealed object를 재사용/복원하고, 새 ZIP을 덮어쓴 뒤 receipt를 지우는 복구는 금지한다.

Routine metadata 검증으로의 추가 최적화는 이 문서에서도 기본 비활성이다. Dropbox content_hash는 4 MiB block SHA256를 다시 SHA256한 값이지 raw file SHA256가 아니다. Drive의 sha256Checksum은 실제 응답에 있는 경우에만 사용할 수 있다. [S4, S5] 해당 rclone/API 버전에서 크기와 충분한 hash를 얻지 못하면 raw readback으로 fallback한다. MD5-only matching을 strong raw-SHA 검증으로 승격하거나 UPLOAD_VERIFIED를 RESTORE_VERIFIED라고 기록하지 않는다.

## 11. 비용, 운영, 보안

초기 calibration+첫 science node 실행의 예산 후보는 2시간이다. 공개 3,192원/h를 단순 적용하면 VM compute 6,384원이며 VAT, disk, 추가 network 및 관련 자원 비용은 제외된다. 6시간은 같은 방식으로 19,152원이다. 실제 예상시간은 NCP full-pair benchmark 후 산정하며 이 수치는 작업 완료시간 예측이 아니다. [S2]

Job supervisor에 wall/cost cap을 넣고, budget 종료 전에 새 pair 제출 중단, 실행 중 작업 drain, local fsync, 가능한 원격 검증과 최종 ledger를 수행한다. 정해진 grace 이후에도 멈추지 않으면 실패 상태와 last durable manifest를 보존한 채 process를 종료하는 경로를 둔다. 외부 control-plane stop API/콘솔로 instance의 실제 STOPPED 상태를 확인한다. Python 종료나 guest shutdown 명령만으로 billing 종료를 선언하지 않는다. NCP는 stopServerInstances를 제공한다. [S6]

유료 compute idle을 피하기 위해 cloud source node의 최종 seal이 닫히면 VM을 정지하고 후처리는 PC/sandbox에서 한다. 중지해도 storage 등 잔존 요금이 있을 수 있다. 볼륨/instance 삭제는 자동화하지 않는다. [S1]

첫 배포에서는 코드 준비와 기존 source inventory를 유료 VM 생성 전에 끝낸다. SSH key와 실제 접속 IP allowlist를 사용하고 rclone/GitHub/NCP 비밀값을 repo, artifact 또는 로그에 넣지 않는다. 가능하면 VM은 읽기 전용 repo 접근만 사용한다. NCP stop controller 권한은 별도로 최소화하며 광범위한 관리자 key를 scientific worker에 전달하지 않는다. controller/정지 자동화의 실제 설정과 API 실행은 별도 승인 후 수행한다.

## 12. 현재 과학 DAG의 재개 위치

기준 repository의 R31S 결과는 z=2 direct H/full49 PASS, [0,4] interpolation FAIL 및 next z=1이다. 이는 저장된 결과의 상태를 인용하는 것이며 이번 설계에서 그 계산을 다시 실행하지 않았다.

따라서 첫 cloud science 목표는 **z=1 하나**다. H B160/B192, OD192, JVP192, same-z ionic census를 실행 계약으로 묶는다. ionic z=1이 기존에 admitted인지 먼저 확인하고, 없다면 동일 source family의 승인 경로를 수행한다. z=2의 ionic admission을 z=1로 옮겨 쓰지 않는다.

z=1은 [0,2]의 midpoint다. 이 gate가 실패하면 깊이 우선으로 다음 child를 검사한다. minimum interval width=1 a0를 실제로 판정하려면 예를 들어 [0,1]의 midpoint z=0.5가 필요할 수 있으므로 z=1을 최종 width-1 판정이라고 잘못 부르지 않는다. sibling과 넓은 영역의 node를 CPU가 남는다는 이유로 미리 계산하지 않는다.

Interpolation semantics와 H/G thresholds는 freeze한 상태로 유지한다. 과거 provider-block/literal-raw semantics의 구분 역시 report에 명시하며 통과하는 쪽을 사후 선택하지 않는다. 전 구간 interpolation이 승인되지 않으면 trajectory/production은 계속 false다.

## 13. 구현 순서와 acceptance tests

이 항목은 미래 구현 계약이며 현재 PASS 결과가 아니다.

### 단계 A: source/host migration

새 bootstrap, explicit ncp lane, input catalog, host/build identity, separate namespace, CPU/ABI preflight를 만든다. tests는 virtual topology 없음/중복/-1 IDs, L3 없음, cgroup quota, fractional quota, memory limit, malformed manifest, signed-zero/byte-equality 차이를 포함한다. 기존 completed state는 byte-preserving이어야 한다.

### 단계 B: executor와 비용 제한

spawn-import-safe persistent worker, task reservation, canonical assembler, memory/CPU budget, worker failure 및 shutdown 경로를 만든다. initializer 실패/중도 crash에서도 무기한 barrier wait를 금지한다. 서로 다른 stage의 총 thread 예산을 검사하고 stop 후 새 제출이 없어야 한다. 잘못된 결과를 성공으로 seal하지 않는다.

### 단계 C: V3 durability, 승인된 경우만

한 provider 실패, upload 성공 후 ACK 전 crash, pair rename 후 ledger 전 crash, stale lease, local seal overwrite, remote size/hash mismatch, native call hang, 최종 seal 재개를 injection test로 검증한다. acknowledged payload는 검증한 remote identity와 연결돼야 하며 중복 실행으로 확인된 파일을 덮지 않는다. queue count/byte reservation 초과를 거절하고 old receipts는 보존한다.

### 단계 D: NCP numerical bridge와 tuning

같은 host reference/candidate 비교와 cross-host golden comparison을 별도 결과로 남긴다. 제한된 변경 의존성 테스트만 실행하고 과거 전체 scientific suite를 자동 반복하지 않는다. 성능 표에는 full-pair 및 end-to-end 시간을 포함하고 warm/cold start, sample count, deviation과 환경을 기록한다.

### 단계 E: bounded z=1 handoff

선정된 profile, source/build/runtime catalog, 승인된 durability policy, 예산을 하나의 manifest로 고정한다. cloud에서 source만 만들고 최종 dual-sealed 결과를 반환한다. 이후 source convergence/full49/interpolation 판정은 별도 노드로 수행한다.

구현 예상 대상은 `hardware.py`, cloud-specific bootstrap/host profile, `benchmark_pool.py`, new persistent executor/receipt modules, execution-lane policy, migration regression 및 tests다. `native/reference`와 원 scientific source의 bytes는 변경 대상이 아니다.

## 14. 승인 경계

현재 게시한 것은 이 문서 하나다. executable/cloud config 변경, NCP benchmark, 새 z=1 계산, provider promotion, instance 생성/정지/삭제는 수행하지 않았다.

명세 검토 후 구현할 범위는 단일 VM migration과 persistent executor다. V3의 128-unacknowledged 상한 및 비동기 계산/백업은 새로운 RPO 정책으로 별도 확인해야 한다. 해당 승인이 없으면 M0의 12-pair dual-raw fence가 기본값이다.

## Sources

Repository claims above refer to exact baseline commit `2d400ea785e2f2cc80a07e1eb0c27de7d00a69c7`, especially `AGENTS.md`, `scripts/benchmark_pool.py`, `scripts/wide_hybrid_orchestrator_cost.py`, `src/wu088_hh/hardware.py`, `scripts/build_native.py`, `docs/coding/R31T_DELTA_METADATA_PROBE.md`, and `evidence/r31s/R31S_Z2_GATE.json`.

- S1: Naver Cloud, Server 사용 준비: https://guide.ncloud-docs.com/docs/server-spec-vpc
- S2: Naver Cloud, 일반 한국 공개 요금표: https://m.ncloud.com/charge/price/ko
- S3: Python 3.12 multiprocessing, Contexts and start methods: https://docs.python.org/3.12/library/multiprocessing.html
- S4: Dropbox API, Content Hash: https://docs.dropboxapi.com/dropbox-api/docs/technical-reference/content-hash
- S5: Google Drive API v3, Files: https://developers.google.com/workspace/drive/api/reference/rest/v3/files
- S6: Naver Cloud VPC API, stopServerInstances: https://api.ncloud-docs.com/docs/compute-vserver-server-stopserverinstances
