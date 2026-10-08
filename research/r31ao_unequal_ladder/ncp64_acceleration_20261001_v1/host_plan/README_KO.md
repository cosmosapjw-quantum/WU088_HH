# 관측한 자원에 맞춘 단일 호스트 MPI 실행

이 계획기는 사용자가 설명한 NCP 용량을 상한으로 삼되, 실제 Linux affinity·물리 코어·SMT·NUMA·CPU quota·가용 메모리를 읽는다. 원격 접속은 하지 않는다. 실제 NCP 성능은 아직 측정하지 않았다. 여기서 수행한 검사는 작은 합성 토폴로지와 Python 실행 경계 검사이며, Fortran/MPI 빌드·실행은 미검증이다.

## 먼저 계획만 확인

이 overlay의 root에서:

```bash
python3 -B host_plan/planner.py
```

`plan`과 `mpi` JSON을 출력한다. 필수 도구가 없으면 `MISSING_MPIRUN`/`MISSING_MPIFORT`, 자원이 부족하면 구체적인 `blocked_reasons`를 남긴다. 패키지를 설치하거나 SSH로 다른 호스트에 연결하지 않는다. 현재 실행 환경의 관측은 `HOST_INTAKE_OBSERVED.json`에 있다. 이 환경은 cgroup CPU quota 8개, memory.max 8 GiB이고 MPI 도구가 없으며, 기본 16 GiB 여유를 적용하면 실행이 차단된다.

| 항목 | 기본 정책 |
|---|---|
| CPU | 실제 affinity, quota의 내림값, 접근 가능한 서로 다른 package/core 수, 64 중 최소 |
| SMT | 기본 제외. `--smt`를 명시하면 접근 가능한 논리 CPU를 사용하되 같은 quota/64 상한 적용 |
| MPI ranks | coordinator를 포함한 수. 64개 물리 코어와 충분한 메모리라면 64 ranks = coordinator 1 + workers 63 |
| rank 1 | 단일 프로세스의 coordinator/worker 순차 fallback |
| 메모리 | min(128 GiB, MemAvailable, MemTotal, 각 가시 cgroup ancestor의 limit-current)에서 16 GiB를 예약, job 상한 112 GiB |
| 프로세스 | worker/coordinator 각각 1 GiB 계획, rank의 RLIMIT_AS 적용. task AS/RSS 계약이 worker 예약을 넘으면 차단 |
| 내부 스레드 | OpenMP/OpenBLAS/MKL/BLIS 등 1. 실제 FLINT 호출의 thread1 설정은 native worker의 별도 계약 |

GiB는 2³⁰ bytes이며, 사용자가 말한 128 GB와 동일하다고 가정하지 않는다. cgroup v1/v2 모두 leaf부터 보이는 mount root까지 CPU·메모리 제한을 검사한다. cgroup namespace 밖의 숨은 ancestor는 관측하지 못한다는 한계도 기록한다. OS affinity는 kernel이 허용한 cpuset 교집합으로 취급한다. NUMA 정보는 기록하지만 측정 없이 NUMA speedup을 주장하지 않는다.

## executor와 MPI dispatcher 연결

먼저 `executor/` 계약에 맞는 **SYNTHETIC_ONLY** manifest와 `mpi_fortran/` exporter의 worklist를 준비하고, 같은 호스트에서 검증한 OpenMPI 4 또는 5로 dispatcher를 빌드한다. 실행 파일은 새 build directory의 `ncp64_dispatch`다. manifest에는 정확한 executable/input/library identity, 고정 precision을 포함한 원래 argv, task별 wall/AS/RSS/output 한도가 들어간다. launcher는 precision·허용오차·계산 순서·task argv를 바꾸지 않는다.

```bash
python3 -B host_plan/launcher.py \
  --manifest /absolute/run_inputs/synthetic_manifest.json \
  --worklist /absolute/run_inputs/synthetic_worklist.txt \
  --mpi-binary /absolute/mpi_build/ncp64_dispatch \
  --output /absolute/host_attempt_001 \
  --ranks 8 --wall-seconds 900
```

이 명령은 argv와 BLOCKED/PLAN_READY 계획만 출력한다. 실제 합성 실행은 같은 명령에 `--execute-synthetic`를 붙인다. 계획된 rank 수를 초과하는 `--ranks`는 자동으로 몰래 줄여 실행하지 않고 차단한다. `--reserve-gib`와 `--worker-mib`로 더 작은 호스트의 합성 검사 예산을 명시할 수 있으나, 기본값은 실제 NCP 관측 없이 축소하지 않는다. 동적 라이브러리가 별도 prefix에 있다면 `--backend-library-path /absolute/prefix/lib`를 명시한다. 해당 경로 지정만으로 library provenance가 증명되지는 않으며 manifest의 library pins와 native build 검증이 필요하다.

task output_root는 새 절대 경로다. 이미 저장한 동일 작업을 재개할 때는 `--resume`을 명시하고 **host attempt 출력 디렉터리는 새 경로**를 지정한다. `executor/prepare.py`가 동일 manifest identity 및 완료 파일을 검증해야 MPI 단계에 들어간다. worker는 검증된 완료 task를 재실행하지 않고 재사용한다. 불완전·변조·실패 상태는 executor 계약에 따라 INCONCLUSIVE다.

실행 순서는 prepare READY → MPI 완료 → 모든 rank binding receipt 확인 → collector COLLECTED다. 전체 선언 task 개수와 완료 개수 및 canonical payload digest까지 확인한 뒤에만 `EXECUTION_COMPLETE`를 기록한다. 이 상태는 합성 실행의 완결성만 의미하며 scientific certificate나 성능 향상을 뜻하지 않는다.

## OS CPU와 hwloc ID를 섞지 않는다

OpenMPI 4/5의 `--cpu-list`는 Linux OS CPU 번호가 아니라 hwloc 논리 core ID를 해석한다. 따라서 계획한 OS CPU 배열을 그 옵션이나 rankfile에 넣지 않는다. 이 launcher는 다음 mapping을 사용한다.

```text
mpirun -np P --host localhost:P --map-by slot --bind-to none --nooversubscribe --report-bindings
```

각 rank가 `rank_guard.py`를 통해 자신에게 배정된 **OS CPU 한 개**에 `sched_setaffinity`를 적용하고 readback을 기록한 뒤 Fortran dispatcher를 exec한다. Fortran이 실행하는 Python worker와 그 자식은 이 affinity를 상속한다. 물리 모드에서는 서로 다른 package/core에서 한 OS thread씩 선택한다. `--report-bindings`의 초기 unbound 표시는 의도된 것이며, 최종 binding 증거는 `bindings/rank_N.json`이다. 표준 `--map-by core --bind-to core`도 OpenMPI 옵션이지만 이 실행기에서는 OS ID 대응을 추측하는 데 사용하지 않는다.

launcher는 job wall과 process-tree RSS를 주기적으로 감시하고 제한 시 process group 및 추적한 descendant를 종료한다. `/proc`가 상위 PID namespace에 mount된 경우 동일 `ns/pid`와 `NSpid`를 사용해 현재 namespace의 PID/부모 PID로 변환하며, 대응을 확인할 수 없으면 시작 전에 차단한다. task별 제한은 executor가 적용한다. **RSS 감시는 hard aggregate cgroup 한도가 아니며**, Fortran/Python supervisor overhead는 예약 메모리를 소비한다. 실행 직전에 자원을 다시 읽고 최신 snapshot과 더 작은 memory cap을 기록한다. MPI rank의 SIGKILL/통신 단절에 대한 ULFM 복구는 제공하지 않는다.

## 고정 정확도 calibration

`calibration_total_ranks`는 실제 예산 내의 1/2/4/8/16/32/64 중 허용되는 값이다. 64는 worker 64개가 아니라 총 rank 64개다. 각 rank 수에서 같은 task scientific payload, executable/input/library identity, precision, error budget과 argv를 사용하고, 각 측정의 output_root 및 host attempt 디렉터리만 새로 지정한다. 결과의 canonical payload digest가 같아야 timing 비교가 의미가 있다. rank1과 여러 worker 결과가 다르면 속도 결과를 채택하지 않는다. 실제 callback benchmark와 NCP timing은 후속 호스트 측정이며 여기서 speedup을 만들지 않았다. `-march=native`, AVX512, fast-math 또는 precision 변경 옵션을 추가하지 않는다.

## API와 검증

`planner.detect()`는 실제 host snapshot, `planner.plan(snapshot, ...)`은 예산을 반환한다. `cpu_budget`과 `job_memory_budget_bytes`를 다른 build planner가 읽을 수 있다. `python3 -B host_plan/test_host_plan.py`는 64물리/32SMT, fractional/ancestor quota, v1/v2 ancestor memory, 작은 호스트, CPU ID 구분, 최신 memory 재검사, resume 경계, 실제 Linux affinity readback, collector gate를 검사한다. collector gate의 Python test double 검사와 실제 executor prepare/worker/collect CLI 연결 검사를 모두 수행했다. 후자에서도 MPI dispatch는 명시된 Python 대역이며 native MPI 성공으로 계산하지 않는다. 실제 executor 합성 작업의 첫 실행/재개에서 canonical payload digest가 일치했다.

공식 동작 근거:

- [OpenMPI 4.1 mpirun](https://www.open-mpi.org/doc/v4.1/man1/mpirun.1.php)
- [OpenMPI 5.0.7 mpirun](https://docs.open-mpi.org/en/v5.0.7/man-openmpi/man1/mpirun.1.html)
- [OpenMPI 5 host/slot scheduling](https://docs.open-mpi.org/en/v5.0.4/launching-apps/scheduling.html)
- [Linux cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html)
