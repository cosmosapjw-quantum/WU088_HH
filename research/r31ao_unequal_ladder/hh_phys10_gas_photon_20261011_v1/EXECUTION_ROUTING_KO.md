# PHYS10 실행 위치와 NCP 자원 배정

## 완료 상태와 현재 배정

**PHYS08/09의 실제 Rust 완료 결과는 재사용했고, 새 PHYS10 기체–광자 에너지 ledger 계산은 이 대화 호스트에서 완료했다. 현재 NCP의 `heavy_queue`는 빈 목록이며 `launch=false`다.** 짧은 build·gate·exact consumer를 NCP에 다시 배정하지 않는다. 물리적으로 필요한 장시간 병렬 작업이 준비되면 그 작업만 넘긴다.

| 작업 | 현재 상태 | 실제 계산·검증 근거 |
|---|---|---|
| PHYS08 저장 scalar gate | `REUSED_EXISTING_COMPLETE` | `inputs/current_return/files/ncp08/VALIDATION.json` 및 원 실행 기록 |
| PHYS09 projected-energy gate | `REUSED_EXISTING_COMPLETE` | `inputs/current_return/files/ncp09/NCP_RETURN.json`, `ORACLE_CHECK.json` 및 원 실행 기록 |
| PHYS10 기체–광자 ledger | `COMPLETE_HERE` | `results/ledger_first/SUMMARY.json`, `evidence/ledger_first/EXECUTION.json` |
| 새 NCP heavy 작업 | `NO_HEAVY_JOB_READY` | `NCP_TASKS.json`, `NEXT_DAG.json` |

PHYS10 첫 실행은 **0.7208253940043505 s**, 최대 RSS **23924 KiB**, exit 0, **35 assertions / 7 semantic cases**다. 실행 기록의 before/after 19개 binding 항목은 동일하며 `bound_files_unchanged=true`다. 이 결과는 저장된 Jet에 대한 새로운 exact-rational ledger contraction이다. 완료한 PHYS09 역행렬·기체 응답 증명을 재계산하지 않았다. 최종 과학 채택 범위는 `review/DECISION.json`을 따른다.

## 기존 실행이 경량임을 보여 주는 실제 기록

| 실행 | 실제 wall time | 메모리 기록의 의미 |
|---|---:|---|
| NCP08 build | 1.421572867 s | 누적 child max RSS 130424 KiB |
| NCP08 gate | 0.004196964 s | 같은 누적 max; gate 단독 peak 아님 |
| NCP08 exact consumer | 0.667819977 s | 같은 누적 max; consumer 단독 peak 아님 |
| NCP09 build | 0.766845725 s | named-child wait4 max RSS 148952 KiB |
| NCP09 gate | 0.062806829 s | named-child wait4 max RSS 11408 KiB |
| NCP09 exact consumer | 0.083373354 s | named-child wait4 max RSS 20628 KiB |
| NCP07 source export, full | 2.087629673 s | measured RSS 44040192 bytes |
| NCP07 source export, first_half | 2.110921434 s | measured RSS 44040192 bytes |

NCP08 원 기록은 `inputs/current_return/files/ncp08/hh_phys08_weighted_first/`의 각 `EXECUTION.json`, NCP09 원 기록은 `inputs/current_return/files/ncp09/execution/`에 있다. NCP07 기록은 `inputs/ncp07/raw/evidence/`에 보존했다. 요약 추출본은 `evidence/EXECUTION_COST_EVIDENCE.json`이며, 포함된 원 기록과 `inputs/current_return/FETCHED_FILE_IDENTITY_MANIFEST.json`이 실제 provenance 포인터다. 위 시간은 각 원 실행 호스트의 관측이며 이 대화 호스트의 실행시간 또는 호스트 간 속도 향상 비교가 아니다.

실제 NCP08 head `5288fd50148755f5ed37391e3dcb612d8d51f130`와 NCP09 head `e6a72c3df5803b5b23f9a38918dad6a1eba7e1f7`를 intake했다. NCP09 원 실행 commit은 `638af93295c5205c1683c33c9e2b97fe8f3e910d`이며 후속 반환은 동일 완료 evidence 재사용이다. 50개 exact-oracle 구간 전체 포함을 기존 범위로 인정하고, 같은 gate를 새 NCP 작업으로 만들지 않는다. 새 C++ 대체 포팅도 필요 없어 작성하지 않았다.

현재 호스트에서 Python 3.12.14와 gcc/g++ 경로가 관측됐다. 제한된 PATH·통상 경로 확인에서 Rust toolchain은 미관측이다. Affinity 9 logical CPUs, cgroup CPU quota 8 CPU 상당, memory.max 8 GiB를 `evidence/HOST_READ_ONLY_OBSERVATION.json`에 기록했다. Toolchain 부재는 실행환경 의존성이며 장시간 계산의 증거가 아니다. 이번 PHYS10은 설치 없이 Python으로 끝냈다.

## 실제 source graph의 병렬성과 시간 의존성

고정 `phys04_prepare_family`는 `spectral_subdivisions=8`, `n_mu=8`, `n_phi=16`을 강제한다. 이 계열은 33 energy nodes, 128 rays, 총 4224 photon Jets다. 더 큰 grid를 다룰 수 있는 일반 함수의 존재는 현재 source-family의 해상도·계수·정칙성 조건을 변경할 근거가 아니다.

- 고정 geometry와 입력에서 같은 단계의 ray 수송은 독립 출력 버퍼로 나눌 수 있다. 그러나 원 source는 canonical d 순서로 모든 Jet 성분을 합산하며 전역 trace mutex를 사용한다. 향후 병렬화는 ray 출력을 독립 저장한 뒤 원 순서로 합산하거나 별도 수치 계약으로 변경을 검증해야 한다. 현재 수 초의 첫 단계 호출만으로 병렬 이익을 주장하지 않는다.
- Energy groups는 같은 4차원 gas state를 통해 결합한다. Group별 독립 gas solve로 분할하면 원 문제를 바꾼다. 작은 행렬 계산을 64 worker에 복제하지 않는다.
- Full과 first_half는 같은 COMMON에서 독립적으로 시작하지만 second_half는 first_half의 gas/photon/guard/ledger carry에 의존한다. 시간 조각을 독립 실행한 뒤 붙이는 방식은 이 의존성을 충족하지 않는다.
- 실제 장시간 campaign의 우선 병렬 단위는 **각자 고정된 물리 입력을 가진 독립 family의 전체 history**다. Family 내부의 시간 carry와 적응 시간 간격 판단은 순차로 유지한다.

원 repo의 frozen107 atomic pair/OpenMP lane은 별도 계산이다. 완료된 1440 pairs, 새 dotO/ionic 입력, full49 gate를 현재 HH/photo 루프의 임의 heavy workload로 가져오지 않는다.

## 다음 물리 단계의 전제

다음 연구는 `NEXT_DAG.json`에 정의했다. 우선 같은 family의 joint carry를 명시한다. Carry는 gas 값과 U,V,W뿐 아니라 photon stock, lower guard number/energy, source·흡수·redshift·thermal work·HH ledger 및 실제 compensation 상태를 포함해야 한다. 모든 photon·event stock의 per-H 정규화, eV/H 에너지 단위, geometry와 clock, stage f와 stored-density ratio의 차이를 유지한다. 과거 ledger와 미래 derivative ledger를 섞지 않는다.

그 뒤 실제 first-half 출력에 결박된 다음 단계 source coverage와 chart를 확보해야 한다. 같은 COMMON에서 얻은 first_half export를 carried second_half의 입력으로 재명명하지 않는다. 초기조건·정규화·입사 광자/source history·배경/시간 사상·계수·closure가 지정되지 않은 family는 임의 상수나 합성 데이터로 채우지 않는다. 합성 예제는 의미 검증에만 쓰고 실제 history의 evidence로 쓰지 않는다.

새 native issuer/root 또는 실제 carried-history 결과가 필요한 경우 해당 소스/실행의 identity와 관측 가능한 acceptance를 먼저 연결한다. Source-only 조건부 (C^2) 정리와 현재 ledger 결과가 native 권한을 자동으로 만들지 않는다. 이어지는 유도·작은 구현·경량 검증은 여기서 우선 수행한다. 현재 handoff는 새 source/native/root/IVP/history 호출을 배정하지 않는다.

## 향후 NCP 비용·메모리 admission 정책

아래는 **미래 실행에 적용할 운영 정책**이며 관측된 NCP 속도 향상이나 현재 시작 권한이 아니다. 현재는 active queue가 비어 있으므로 적용해 시작할 작업이 없다.

1. 물리 질문에 필요한 유한 task 목록과 각 task의 불변 identity가 있어야 한다. 이미 완료한 동일 task는 제외한다. 코어 점유율을 위해 parameter 범위·grid·task 수를 늘리지 않는다.
2. 새로 필요한 대표 task를 여기서 가능한 작은 범위로 먼저 수행해 wall time, CPU time, peak RSS, 출력량을 얻는다. 완료 pilot은 유효한 연구 결과로 재사용한다. 기존 2초 sourcebox를 긴 history의 측정값으로 외삽하지 않는다.
3. 새 campaign이 실제 긴 계산이고 충분한 미완료 독립 family가 있을 때만 NCP admission을 검토한다. 선택한 기본 기준은 대표 측정으로 뒷받침되는 미완료 직렬 work가 600 s 이상이고 독립 family가 8개 이상인 경우다. 이는 속도 보장이 아닌 운영 문턱이며, 다른 명시적 heavy 계약이 필요하면 그 계약을 따로 작성한다. 기준을 맞추려고 family를 제조하지 않는다. Recovery/serialization/I/O까지 포함한 예상 NCP 비용이 유리해야 한다.
4. 명목 64코어·128 GiB에서는 task pool의 정책 상한을 56개 단일-thread worker와 112 GiB로 두고 8코어·16 GiB를 남긴다. 실제 cpuset, quota, physical core/SMT, cgroup 잔여 RAM과 다른 작업을 먼저 읽는다. 자원이 더 적으면 같은 reserve를 뺀 값까지 낮추며 usable budget이 없으면 실행하지 않는다.
5. Worker 메모리 상한은 해당 task 종류의 새 representative peak RSS의 2배와 명시된 실제 필요 메모리 중 큰 값으로 제안하고, 그 상한을 cgroup 또는 동일 의미의 제한으로 집행할 수 있어야 한다. Peak RSS는 미래 peak의 증명이 아니므로 실제 사용량을 관측하고 상한 실패를 보존한다. `workers <= min(pending_tasks, usable_cpu_budget, floor(pool_memory_budget/worker_memory_limit))`를 만족시킨다. Nested OpenMP/BLAS thread는 task가 별도 승인하지 않으면 1로 고정한다.
6. 각 family는 분리된 실행·checkpoint 경로를 쓰고 canonical source/계수/input/parameter/grid/closure/binary identity를 task key에 결박한다. 같은 identity의 완료 checkpoint는 재사용하고 실패는 첫 로그를 보존한다. 새 증거나 수정 없는 동일 재시도를 하지 않는다. 진행 checkpoint와 양쪽 backup ACK는 다음 carry 소비 전에 확인한다.

이 정책은 memory safety를 위한 보수적 자원 상한이다. 56 worker에서의 실제 효율, speedup, 메모리 확장성은 `NOT_MEASURED`다. 장시간 계산이 준비되기 전에는 주기적으로 같은 준비 여부를 polling하지 않는다.

## 이번 NCP 반환

정확한 전달 header의 Git/backup identity로 복구하고, 기존 완료 evidence와 PHYS10 결과를 읽어 연결한다. `heavy_queue=[]`와 `launch=false`를 확인한 뒤 **`NO_HEAVY_JOB_READY`**를 반환한다. 완료 수학 계산·build·gate를 실행하지 않는다. 다음 물리 의무는 설명하되 새로운 입력·권한·작업량을 만들어내지 않는다. Native root/U/V/W/I는 null, native authority는 false이며 carried second_half, paired defect, time/continuum remainder, full49/production은 OPEN으로 유지한다.
