# R31S NCP c64-g3: 설계와 다음 구현자 계약

기준일 2026-09-28. 대상 cosmosapjw-quantum/WU088_HH. parent 5887d2a2239db9f34d5bd5b4840abce420b37f1a. BASS_HE 계획과 섞지 않는다.

## 실제 결과와 비용

R31R z2의 4개 seal 및 CP4 합본을 SHA/CRC로 확인했다. H 288개 pair의 event hash와 internal indices/finite arrays, assembled/result/identity binding을 확인했다. H160/192 차이는 9.312542793123333e-10 Eh, 각각 94개 column/row entry에서 실패 0이다. complex256 저장 정밀도로 order comparison을 수행했다. continuum error bound라는 뜻은 아니다.

z2 full49 metric gap max=6.00910106219364e-15, independent G anti-Hermiticity=1.905653923487404e-14, cond(O)=16.222042892795155. 원 authority gate를 통과했다. full49 complex128은 상속된 R10 lane이며 native kernel precision downgrade가 아니다. 재구성 Gaussian product-rule derivative와 기존 z8 저장 reference 차이는 5.285424859784614e-15이며 exact equality라고 하지 않는다.

[0,4] midpoint z2 linear interpolation은 H error=1.1911459223785104 Eh, whitened G relative Frobenius=0.34502624594182096로 FAIL이다. 원 기준 H<=2e-7 Eh, G<=2e-12를 유지했다. 다음 depth-first 허용점은 z1([0,2] 검사)이다. 최소 폭1인 [0,1] 검사는 이후 z0.5가 필요하다. 폭2의 실패를 최소폭 실패로 오인하지 않는다. cloud admission 전에는 z1을 실행하지 않는다.

| basis | compute waves(s) | queue-to-ACK(s) | two-process slot occupancy |
|---|---:|---:|---:|
| B160 | 491.901931 | 483.004143 | 97.6418% |
| B192 | 720.833247 | 1135.922947 | 97.4607% |

각 basis에는 12 compute waves가 있다. bounded_invocations=13은 13 heavy waves가 아니다. queue-to-ACK는 업로드/readback/retry/제어 지연을 합친 값이지 순수 네트워크 전송 시간이 아니다. 두 항에 포함되지 않는 초기화/final-seal 시간도 있다.

C=1212.735177, A=1618.927090이다. A가 그대로일 때 compute만 s배 가속하면 S=(C+A)/(C/s+A)이고, s=4에서1.4732배, s→∞에서도1.7491배다. 이것은 cloud 실측 speedup 예측이 아닌 조건부 비용식이다. CPU 수64/12로 전체 성능을 예측하지 않는다. 2-process scheduling 점유율은 이미 높으므로 source/kernel/thread utilization과 ACK를 분리해서 측정해야 한다.

## 확인된 c64-g3 계약

공식 product-spec API는 SVR.VSVR.HICPU.C064.M128.G003, High-CPU(c64-g3, vCPU64, Memory128GB), KVM을 명시한다 [N1]. 이것은 물리64core 또는 특정 CPU/SMT/NUMA/L3를 보장하는 정보가 아니다. g3는 KVM/FB·CB storage 계열이고 실제 사용자의 filesystem/mount/IOPS는 probe 대상이다 [N2].

새 probe는 affinity, guest topology, cgroup v2 현재/보이는 ancestor CPU·memory 제한, compiler precision macros, filesystem free를 읽는다 [K1]. missing L3는 None이다. 기존 hardware.py의 cpuN fallback을 숫자 cpulist로 읽는 실패 경로를 사용하지 않는다. cgroup-v1/불명확 namespace는 자동 계획을 차단한다. 보이지 않는 host 상위 제한까지 확인했다고 하지 않는다.

## 두 실행 경로를 분리

호환 경로: 기존 <=12 미ACK pair와 barrier를 유지한다. 기존 orchestrator는 max_new_pairs<=12 및 pool_workers<=wave size이고 autotuner 역시 기본12-pair workload다. 따라서 workers64로 바꾸는 것만으로 outer64가 되지 않으며 64x1/32x2/16x4 tuning 후보가 누락된다. 8x8 등 호환 후보를 시험할 수 있으나 ACK 병목은 남는다. 5900X 2x12 profile은 cloud에 이식하지 않는다.

새 NCP 경로(설계, 아직 실행기 아님): external_host backend를 ChatGPT sandbox의600 CPU-second local-handoff 정책과 분리한다. 단일 coordinator, prebuilt fresh cloud providers, persistent worker pool, immutable grid/source cache, canonical pair/reduction ordering, separate uploader를 둔다. spawn 또는 clean forkserver를 비교하며 OpenMP/BLAS 초기화 뒤 무조건 fork하지 않는다 [P1]. worker 시작 전에 build를 단일 경로로 끝내고 build-cache 경합을 없앤다.

job key에는 model/source/grid/build/geometry/order/pair identity를 포함한다. local commit은 tmp→flush/fsync→검증→원자적 commit 및 복구 가능한 event 순서로 한다. scientific seal은 데이터 allowlist만 포함하고 heartbeat/RUN_STATE/receipt는 분리한다. 원 pair/aggregate를 다시 써서 새 SHA로 맞추지 않는다.

immutable 원 seal을 manifest-bound transport bundle에 묶을 수 있다. 두 provider가 같은 source SHA/size를 검증하기 전에는 ACK하지 않는다. 일반 rclone checksum/파일 크기를 RAW_SHA256_READBACK의 대용으로 쓰지 않는다 [R1]. 새 계산과 backup overlap은 기존 정책 변경이므로 별도 승인/구현/고장 주입 대상이다.

제안 B=128 outstanding pair-equivalents는 아직 승인값이 아니다. R=inflight reservation, L=local/미dualACK, F=실패·미조정이면 R+L+F<=B를 유지한다. dispatch가 credit를 먼저 확보하고 completion은 반환하지 않으며 양 provider verified receipt에서만 반환한다. 한 provider가 실패하면 capacity를 채운 뒤 dispatch가 멈춘다. credit_model.py는 이 상태 전이만 테스트한 in-memory specification이며 durable WAL/uploader를 구현했다고 하지 않는다.

## host tuning과 precision gate

pure-compute 후보는 64x1,32x2,16x4,8x8,4x16,2x32,1x64 및 half-budget이다. 운영은 P*T+control_budget<=effective_CPU로 제한한다. 순수64-slot benchmark 후보를 uploader 동시 실행의 운영 설정으로 자동 채택하지 않는다. 예컨대60 compute+4 control도 별도 후보이지 선택값은 아니다.

memory는 P*measured_private_peak(T,n)+shared_grid+coordinator+spool/cache+margin으로 제한한다. 이전 maximum pair RSS124.5/157.8MiB만으로64-worker peak를 보장하지 않는다. pilot에서 RSS/PSS, memory.current/high/events, swap, throttling/steal을 측정한다. active tree는 승인된 local block filesystem에 두고 immutable artifact만 backup한다.

strict long double/complex 및 cancellation strip의113-bit binary128을 유지한다. x86 ABI16-byte long-double storage는 binary128 precision을 뜻하지 않는다 [G1]. -fno-fast-math,-ffp-contract=off를 유지하고 double downgrade/FMA reassociation/unsafe Boys recurrence를 사용하지 않는다. 원 scalar recurrence, compensated sum 및 canonical gamma h order는 보존한다.

Gaussian factor separation과 exact-zero mask caching은 native candidate에 이미 있다. 새 성과로 재보고하지 않는다. 추가 후보는 동일 identity의 grid memoization, worker-local scratch reuse, repeated Python/native 초기화 제거다. 산술 순서와 rounding을 유지해도 실제 arrays+sumabs regression을 통과해야 한다.

## 물리적 최적화의 근거와 한계

순수 phase H(z)=A exp(i*k*z)의 폭h midpoint chord는 H(mid)*cos(k*h/2)이므로 오차는 |A|*|1-cos(k*h/2)|이다. 작은 kh에서만 |A|k^2*h^2/8이다. 실제 amplitude가 상수/실수라는 가정은 하지 않는다. z2 error가 parent의0.59Eh보다 커졌으므로 parent 값에 무조건 h^2 scaling을 적용하지 않는다.

새 후보는 known channel/ETF phase를 정확히 분리한 envelope interpolation/Chebyshev/Hermite다. 이것은 기존 linear 실패를 소급 PASS로 바꾸는 방법이 아니다. basis Phi_tilde=Phi U(t)이면:

O_tilde=U† O U; H_tilde=U† H U;
D_tilde=U† D U+U† O dotU;
(dotO)_tilde=dotU† O U+U† dotO U+U† O dotU.

물리 시간 coefficient generator A=-i/hbar O^-1 H-O^-1 D는 A_tilde=U† A U-U† dotU로 변한다. H만 dephase하고 D connection을 빼면 다른 dynamics다. 상속 atomic-unit conventions도 고정한다.

O,D,dotO에 같은 linear weights를 주면 대수적 dotO=D+D†은 보존된다. 그러나 실제 interpolated O의 미분은 v*(O_R-O_L)/(z_R-z_L)이고 interpolated dotO와 일반적으로 다르다. z2 mixed column의 최대 차이는0.248069740331951이다. 따라서 interpolated raw metric PASS는 continuous metric-compatible transport PASS가 아니다. 이는 새로운 formulation의 검증 의무로 기록하며 frozen gate를 소급 변경하지 않는다.

독립 JVP slopes 및 exact neutral/phase를 사용하는 후보를 연구하되 D는 독립 원자료에 대해 비교한다. D+D†를 independent dotO 대신 넣거나 실패 데이터를 symmetrize해서 통과시키지 않는다. 새 후보에는 별도 preregistration, withheld direct nodes, 원 frame 역변환 및 derivative/generator 검증이 필요하다.

## 다음 구현자 단계 및 stop contract

M0: read-only probe JSON 반환. instance 구매/설정, credential, firewall, system Python 변경 없음.
M1: 승인된 새 cloud work root/venv, readonly source+reference import, fresh build namespace. 기존 .venv/.so/host-profile을 production으로 복사하지 않는다.
M2: 새 host frozen-reference/candidate를 나란히 build. B160/B192 및 z2/기존 complex-strip stress의 cheap/median/expensive representatives에서 값+sumabs 비교. same-host scheduling 변화는 exact numerical equality, cross-host 차이는 별도 보고/중단; 자동 tolerance 변경 없음.
M3: B32 foreign-only는 coarse screen만. 전체 H0+foreign, grid/build/init/commit/upload/readback/ACK를 production-shaped queue로 측정. 회전 순서, 최소3회, median/p95, CPU/RSS/PSS/throttle/steal 기록.
M4: persistent async executor를 별도 구현·심사. producer crash, fsync 실패, orphan, half receipt, changed bytes, duplicate ACK, lost lease, restart, OOM, deadline/quota 변화를 fault-injection한다. outstanding budget과 hard/graceful deadline 정책 사전 승인. process 종료는 VM 과금 종료가 아니다.
M5: host/build/execution admission 후에만 z1 직접점 하나. 남는 자원 때문에 전체 ladder를 선제 계산하지 않는다.

반환에는 commit/tree, baseline identity, 변경파일, 새 tests와 exit, probe path/SHA, 후보/선택 구분, 실제 heavy node 및 비용, backup tier, 실패분류와 다음 최소 작업을 포함한다. host 미접근은 BLOCKED_HOST_ACCESS다. 이번29PASS는 probe/model/math controls만이며 cloud throughput, native bridge, real-provider fault recovery, 독립심사, production admission을 대신하지 않는다.

## 공식 자료 (2026-09-28 조회)

[N1] https://api.ncloud-docs.com/docs/en/get-product-spec
[N2] https://guide.ncloud-docs.com/docs/en/server-spec-vpc
[K1] https://cdn.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
[P1] https://docs.python.org/3/library/multiprocessing.html
[G1] https://gcc.gnu.org/onlinedocs/gcc-14.1.0/gcc/x86-Options.html
[R1] https://rclone.org/flags/


## Codex execution governance — M0 반환 이후

2026-09-28 NCP host의 사용자 반환으로 M0 top-level probe는
`PROBED_NOT_BENCHMARKED`, `planning_cpu_budget=64`,
`heavy_execution_allowed=false`까지 확인됐다.
full `HOST_PROBE.json` bytes와 SHA는 아직 repository evidence로 ingest되지 않았다.
따라서 64는 **planning budget 관측값**이지 selected production configuration이 아니다.

이번부터 구현 분업을 다음으로 고정한다.

### ChatGPT/R31S gate owner

- scientific/physics/mathematical claim gate
- frozen threshold와 authority 해석
- provenance/SSOT와 stop condition
- Codex 반환의 독립 검토
- M3/M4/M5 진입 승인 여부

### Codex NCP executor

- c64-g3 host-local file/system inspection
- M1 reproducible environment/build namespace 구현
- M2 fresh reference/candidate build
- bounded representative same-host equivalence/tuning probes
- tests/evidence/commit/push
- 실패 분류와 return handoff

Codex는 다음을 결정하거나 변경하지 않는다.

- scientific threshold
- frozen/reference/vendor authority
- interpolation method claim
- production admission
- z=1 scientific execution
- durability policy promotion
- previous pair/checkpoint/receipt bytes

### Codex branch discipline

Codex는 `r31s-ncp-c64g3-redesign`에서
`codex/r31s-ncp-m1-m2`를 새로 만든다.
기존 R31S branch/PR에 직접 force-push하지 않는다.
Codex branch의 draft PR base는 `r31s-ncp-c64g3-redesign`이다.
자동 merge는 하지 않는다.

### M0 ingest contract

Codex 시작 즉시 host-local
`/root/wu088_ncp_probe.djNQYK/HOST_PROBE.json`을 읽는다.

반드시 기록:

- byte size + SHA-256
- schema/status
- allowed logical CPUs
- planning CPU budget
- cgroup quota/memory-bound fields
- guest-reported topology facts
- compiler version/precision macros
- filesystem free
- warnings

보고서에 token/password/credential/private key가 있다면 commit하지 않고
`BLOCKED_SENSITIVE_EVIDENCE`로 반환한다.
probe schema상 그런 정보를 수집하지 않지만 실제 bytes를 보고 판단한다.

64 vCPU 표시는 host physical core=64를 뜻하지 않는다.
guest-reported core/package/L3/NUMA 정보도 KVM 밖의 물리 topology를 독립적으로
증명한다고 쓰지 않는다.

### M1 admission candidate

fresh work root 예시는 `$HOME/wu088_hh_ncp_work`.
system Python이나 global packages를 mutate하지 않는다.
새 venv와 fresh build namespace를 사용한다.
기존 5900X `.venv`, `.so`, host tuning profile은 production input으로 복사하지 않는다.

system package 설치가 새로 필요하면 자동 apt install하지 말고
`BLOCKED_MISSING_SYSTEM_DEPENDENCY`와 필요한 최소 package를 반환한다.

loader injection vars는 trusted native child에서 sanitize하고,
`-fno-fast-math`, `-ffp-contract=off` 및 precision contract를 유지한다.

### M2 bounded native equivalence

same-host reference와 candidate를 **같은 NCP compiler/ABI**에서 fresh build한다.
cross-host 5900X binary identity를 expected equality target으로 쓰지 않는다.

bounded representative set은 cheap/median/expensive pair를 포함해
B160/B192, z=2와 기존 complex/cancellation stress를 커버한다.
전체 144-pair basis는 아직 실행하지 않는다.

same-host scheduling/implementation variant promotion 조건:

- selected sample actual arrays exact equality
- sumabs/conditioning auxiliary identity도 drift 없음
- expected OpenMP team/affinity 관측
- no precision flag drift
- no source/model/grid identity drift

cross-host previous values와 차이가 나면 자동 tolerance를 만들지 않는다.
원인을 분리하여 `BLOCKED_CROSS_HOST_NUMERICAL_EQUIVALENCE` 또는 더 정확한
implementation/environment classification으로 반환한다.

M2 tuning 후보는 64x1,32x2,16x4,8x8,4x16,2x32,1x64 및 half-budget이다.
하지만 실제 cgroup/affinity budget을 넘는 후보는 실행하지 않는다.
candidate configuration은 benchmark 결과가 나오기 전 selected로 표기하지 않는다.

### M3/M4/M5 hard stop

M2 반환 전에는 다음을 실행하지 않는다.

- production-shaped full H0+foreign queue benchmark
- 144-pair B160/B192 scientific basis
- persistent async production executor
- real Drive/Dropbox overlap policy
- z=1 direct scientific node
- trajectory/production propagation

M2가 닫힌 뒤 ChatGPT review가 다음 단계 범위를 새로 승인한다.

### Codex return schema

최종 답변과 committed evidence는 최소한 다음을 포함한다.

- `status`
- `baseline_branch`, `baseline_commit`
- Codex branch, final commit/tree
- changed files
- host probe path/SHA/bytes and normalized facts
- environment versions
- reference/candidate build keys and binary/source hashes
- bounded sample identities
- test commands + exit codes
- benchmark candidates vs selected distinction
- numerical equality results
- measured wall/CPU/RSS/PSS/cgroup throttling if available
- mutations performed
- backup tier
- explicitly NOT performed items
- failure classification
- next minimal action

PASS라는 단어는 실제 test/build/equivalence evidence가 있는 범위에만 사용한다.
