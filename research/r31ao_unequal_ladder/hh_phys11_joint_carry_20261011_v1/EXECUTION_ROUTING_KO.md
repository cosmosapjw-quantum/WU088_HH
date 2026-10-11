# PHYS11 실행 위치와 NCP 자원 배정

## 현재 배정

사용자는 짧은 경량 연구·계산은 이 대화 환경에서 끝내고, 실제로 길고 무거우며 독립 병렬 실행으로 이익을 얻는 부분만 64코어·128 GiB NCP에 넘기도록 지시했다. PHYS11의 source-aligned group 및 ledger carry 계산은 이곳의 bounded task다. 현재 `heavy_queue=[]`, `launch=false`이며 NCP 반환은 `NO_HEAVY_JOB_READY`다.

PHYS11의 수정 후 실행 `carry_v2`는 실제 **4.029582589995698 s**, 최대 RSS **29900 KiB**, exit 0으로 완료했다. **168 assertions / 8 semantic cases**, 각 단계 33 groups와 165 carry intersections를 기록했다. 19개 source/input bindings는 전후 동일하다. 이것은 이곳에서 완료한 새 경량 계산이며, 과학적으로 채택하는 범위는 `review/DECISION.json`을 따른다.

| 작업 | 현재 처리 | 실행 근거 |
|---|---|---|
| PHYS08 scalar gate | `REUSED_EXISTING_COMPLETE` | 기존 NCP08 실제 완료 반환 |
| PHYS09 projected-energy gate | `REUSED_EXISTING_COMPLETE` | 기존 NCP09 실제 완료 반환 |
| PHYS10 gas/photon ledger | `REUSED_EXISTING_COMPLETE` | 실제 0.7208253940043505 s, RSS 23924 KiB, exit 0 |
| PHYS11 group 및 ledger carry | `COMPLETE_HERE` | `carry_v2`, 4.029582589995698 s / 29900 KiB / exit 0 |
| PHYS11 NCP heavy | `NO_HEAVY_JOB_READY` | 활성 목록 없음 |

PHYS11의 계산 범위는 33개 group의 값·\(U,V,W\), quotient 포함과의 교집합, absorbed number·source number/energy·HH event/heat·thermal work·source-derived escape \(\Gamma_*\) ledger carry와 joint composition 정리다. 소스에서 이미 계산된 complete Jets와 PHYS09 기체 응답을 사용한다. 새 source·provider·native endpoint·root·inverse·기존 callback 재호출은 0이다. 원 물리 코드를 다시 실행하는 대신 기존 output을 입력으로 삼는 새로운 bounded 후처리라는 점을 결과에 표시한다. 새 실제 기록은 `results/carry_v2/SUMMARY.json`, `results/carry_v2/CARRY_RESULTS.json`, `evidence/carry_v2/EXECUTION.json`에 연결하며 최종 판정은 `review/DECISION.json`이다. 기존 PHYS10 기록은 `inputs/phys10/SUMMARY.json`, `inputs/phys10/EXECUTION.json`, `inputs/phys10/DECISION.json`으로 재사용한다.

두 단계 모두 node 24의 mixed photon carry는 엄격히 양수, node 16–23의 8개는 엄격히 음수, 나머지 24개는 0을 포함한다. Source-derived escape와 thermal work를 더한 증대 mixed ledger의 저장 구간은 Full `[-5.788230243389953e-40, 6.862357933552255e-39]`, first_half `[-6.9733119029796365e-40, 8.2693439649913e-39]` eV/H다. 이는 PHYS10에 물리 bookkeeping 항을 추가한 **다른 관측량의 source identity 잔여**다. 수치 정확도가 수십 자릿수 개선됐다거나 전역 보존·actual time evolution이 증명됐다는 뜻이 아니다. 두 구간은 0을 포함한다.

첫 후보 `carry_first`는 0.1667173830064712 s, RSS 19728 KiB, exit 1이었다. `COMMON_INPUT_SCOPE.old_gas`의 실제 full Jet를 bare interval로 읽어 `KeyError: lo_bits`가 발생했고, 첫 물리 stage는 완료되지 않았다. 입력 schema 처리의 구현 오류이며 물리적 반례나 실행환경 실패가 아니다. 첫 snapshot과 raw logs를 보존하고 full Jet를 `jread`로 읽어 값과 0인 미래 partial을 확인하는 부분만 고쳤다. 입력·tolerance·precision은 바꾸지 않았다. 이 수정과 결과는 `evidence/FIRST_FAILURE_AND_CORRECTION.json`, `evidence/carry_first/`, `evidence/carry_v2/`에 남았다. 이번 기록은 새 과학 후보 실행 시도 2회, 입력 schema 수정 1회, 완료 실행 1회다. 실패를 NCP에서 다시 실행하지 않는다.

## 실제 기존 비용과 재사용

| 원 실행 | wall time | 메모리 해석 |
|---|---:|---|
| NCP08 build | 1.421572867 s | cumulative child max 130424 KiB |
| NCP08 gate | 0.004196964 s | 같은 cumulative max; gate 단독 peak 아님 |
| NCP08 consumer | 0.667819977 s | 같은 cumulative max; consumer 단독 peak 아님 |
| NCP09 build | 0.7668457250110805 s | named-child peak 148952 KiB |
| NCP09 gate | 0.06280682899523526 s | named-child peak 11408 KiB |
| NCP09 consumer | 0.08337335399119183 s | named-child peak 20628 KiB |
| NCP07 Full source export | 2.087629673 s | RSS 44040192 bytes |
| NCP07 first_half source export | 2.110921434 s | RSS 44040192 bytes |
| PHYS10 `ledger_first` | 0.7208253940043505 s | RSS 23924 KiB |
| PHYS11 `carry_v2` | 4.029582589995698 s | RSS 29900 KiB |

기존 결과의 identity는 PHYS11의 현재 source intake와 보존된 PHYS10 evidence에서 확인한다. PHYS10 parent는 `7a5eb687515aa29934de764d04fd7493f289ac24`, core subtree는 `b7592637e565666ad92047b7ea25067a4d6bd34b`다. NCP08 head `5288fd50148755f5ed37391e3dcb612d8d51f130`, NCP09 head `e6a72c3df5803b5b23f9a38918dad6a1eba7e1f7`도 이번 intake에서 그대로였다. 최신 source intake는 51 branch refs와 최근 갱신 PR 12개를 읽었고 새 NCP10 Git 반환을 관측하지 않았다. 이 제한된 Git 조사를 모든 백업 위치에서의 부재 증명으로 확대하지 않는다.

위 시간은 각 원 실행 호스트에서 실제 측정한 값이다. 호스트 사이 speedup이나 64코어 scaling 측정이 아니다. Toolchain 부재·payload 다운로드·단순 coefficient capture는 실행환경 또는 자료 가용성 문제이며 긴 물리 계산의 증거가 아니다. 기존 build/gate/consumer를 NCP의 새 작업으로 다시 만들지 않는다.

## Group carry와 실제 joint state

Source residual의 \(D_j=1+d\sum_a c\,n_H\,\sigma_{ja}l_a\)는 ray에 독립이다. 같은 고정 source family에서는 ray quotient의 합과 group quotient가 일치한다. 그러나 다음 transport는 ray별 geometry ratio와 guard state를 사용한다. 33 group만으로 4,224 ray·node의 angular pattern을 복원할 수 없다.

현재 PREBE JSON은 33 complete group Jets, sourceN/U Jets, 128 birth weight 포함을 저장한다. 원 `prebe_words.bin`은 ray·guard를 포함하며 단계별 4,123,688 bytes의 identity가 NCP07 MANIFEST에 있다. 현재 materialization이 없다면 이는 해당 저장 자료의 intake 의무다. 4.1 MB 입력을 확보하거나 decode하는 작업을 heavy job으로 부르지 않는다.

`phys04_distribute_after_be`는 scalar coefficient `fl(fl(sigma*c)*nH)`를 캡처하고 현재 residual은 각각 고정된 c/nH/sigma leaf를 곱한다. Scalar product bits를 새로 읽어 확인해야 한다면 그 33×3 상수 비교도 경량 작업이다. 값 차이의 조건부 rounding 상계가 native root·derivative·compensation의 동등성을 증명하지 않는다.

\(\Gamma_*\)는 저장 FT03 nonphoto Jets에서 유도한 source-family radiative observable이다. 실제 native `escaped_energy_rate`의 반환 Jet나 실제 escape state의 권한을 만들지 않는다. 기존 primal ledger·energy compensation과 역사 HH ON은 보존하고, 미래 실수-family derivatives와 구분한다.

Full과 first_half는 같은 COMMON에서 각각 시작한다. Actual second_half는 first_half의 gas·ray photons·guard·source/work/HH/escape ledger·compensation·clock을 연결해야 한다. 새 source domain과 branch 조건을 확보하기 전에는 같은 COMMON의 half 결과를 second_half로 재명명하지 않는다.

## 다음 연구와 병렬 단위

`NEXT_DAG.json`의 다음 의무는 필요한 실제 ray·guard 자료의 결박, source/native product graph와 escape 연결, complete joint state, 실제 다음 단계 coverage와 history다. 이론 유도·작은 구현·필요한 경량 검증을 여기서 진행한다. 현재 데이터가 없는 곳을 합성 실제 상태로 채우지 않는다. Analytic examples는 joint composition의 의미 검증에만 사용한다.

물리적으로 필요한 장시간 campaign이 준비되면 독립 physical family의 전체 history를 worker 단위로 한다. 각 family 안에서 시간 carry와 적응 timestep 판정은 순차로 유지한다. 같은 4차원 gas를 공유하는 energy groups를 독립 gas solve로 나누지 않는다. 이미 완료된 source export·작은 matrix contraction을 worker 수만큼 복제하지 않는다.

Inner ray parallelism은 같은 단계의 독립 출력 버퍼로 나눌 수 있으나 canonical reduction과 source trace 의미를 보존해야 한다. 기존 소스는 ray 순서대로 Jet를 합하고 전역 trace mutex를 사용한다. 실제 이익이 측정되지 않은 단일 source call에 새 parallel rewrite를 끼워 넣지 않는다. Frozen107 atomic pair/OpenMP, full49, 1440개 완료 pair는 별도 lane이며 HH의 코어 점유용 작업으로 가져오지 않는다.

## 미래 NCP admission과 memory governor

현재 이 절은 실행 명령이 아니다. 활성 heavy 목록이 생겼을 때에만 적용할 운영 정책이다.

1. 물리 질문, 유한한 미완료 task manifest, 각 task의 실제 source/input/parameter/closure/grid/clock identity를 먼저 정한다. 완료 identity와 checkpoint는 제외한다. 자원 점유를 위해 scan·grid·family 수를 늘리지 않는다.
2. 새 실제 task의 필요한 작은 대표 실행을 여기서 먼저 할 수 있으면 수행하고 wall/CPU time, peak RSS, 출력 bytes를 기록한다. 완료 pilot도 과학 결과로 재사용한다. NCP에서만 가능한 대표 측정은 먼저 해당 실제 workload의 장시간·병렬 필요성과 입력 계약이 갖춰진 경우의 신규 bounded pilot으로 명시한다. 이전 수 초 sourcebox를 긴 history 비용으로 외삽하거나 같은 pilot을 반복하지 않는다.
3. 이전에 정한 planning heuristic은 대표 측정으로 뒷받침된 미완료 직렬 work 600 s, 독립 family 8개를 예시 문턱으로 삼았다. 이는 물리적 필요조건이나 자동 실행 규칙이 아니다. 독립 작업 2개가 각각 충분히 크고 NCP 이익이 뒷받침돼도 새 구체적 비용 계약으로 검토할 수 있다. 예시 문턱에 맞추려고 작업을 제조하지 않는다. Recovery·serialization·I/O·checkpoint 비용도 포함한다.
4. 사용자 target ceiling은 64코어·128 GiB다. 미래 pool 상한은 56 single-thread workers와 112 GiB, reserve는 8 CPU 상당과 16 GiB다. 실행 직전에 actual cpuset·CPU quota·physical core/SMT/NUMA topology·cgroup limit·가용 memory·경쟁 작업을 읽고 낮은 실제 예산을 적용한다. 64코어가 이 환경에서 관측됐다거나 scaling이 측정됐다고 선언하지 않는다.
5. Worker 한도는 `min(미완료 task 수, usable CPU budget, floor(pool memory budget / worker memory limit))`다. Task 종류별 실제 representative RSS와 선언된 필요량에서 한도를 정하고 실행 전에 집행한다. 기본 제안은 `max(2×representative peak RSS, explicit memory requirement)`다. Peak RSS는 미래 사용량의 증명이 아니므로 실제 사용량을 계속 기록하고 한도 실패의 원 로그를 보존한다. Nested BLAS/OpenMP threads는 구체적 task 계약이 없으면 1이다.
6. 각 family의 immutable task key, source/binary/입력과 predecessor checkpoint, raw stdout/stderr, 실제 exit/timeout/resource 기록을 보존한다. 실제 topology에 맞게 job pool을 배치하되 전역 시스템 설정이나 runtime을 임의 교체하지 않는다. 완료 checkpoint를 재사용하고, 새 증거 없는 동일 실패 재시도는 하지 않는다. Checkpoint와 backup ACK의 의미를 scientific validation 및 restore verification과 구분한다.

미래 56 workers의 throughput·speedup·RAM scaling은 `NOT_MEASURED`다. 현재 empty queue에 이 정책을 적용해 새 프로세스를 생성하지 않는다.

## 이번 NCP intake의 종료

게시 시점의 실제 detached header에서 Git 또는 백업을 확보해 final contract·실행·독립 decision·현재 task list를 읽는다. PHYS08/09/10 완료 evidence를 재사용하고 PHYS11의 actual result만 새 연구 상태에 연결한다. `heavy_queue=[]`와 `launch=false`가 확인되면 `NO_HEAVY_JOB_READY`, `new_scientific_runtime_calls=0`을 반환하고 종료한다.

Actual native root/U/V/W/I는 null, native_authority는 false다. 실제 ray/native half2, paired defect, time/continuum remainder, 전역 transport 에너지 수지, full49/production 및 모든 inherited OPEN을 보존한다. Empty queue의 주기적 readiness polling은 요청하지 않았다.
