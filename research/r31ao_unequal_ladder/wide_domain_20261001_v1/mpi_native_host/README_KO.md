# 고정 native MPI host 경계

이 추가 모듈은 기존 `native_execution_20261001_v1/mpi_native_tasks`의 준비된 task bundle을 같은 디렉터리의 원래 `native_driver`로 실행하는 단일 Linux host wrapper다. **새 refined/log driver에는 연결하지 않았다.** 기존 Fortran dispatcher, C spawn bridge, task adapter, native source는 변경하지 않는다.

`PREPARATION.json`의 외부 바이트 SHA를 받아 manifest/worklist/bound-worker identity를 확인한다. bound-worker는 원래 generator의 정확한 텍스트로 재구성하여 대조한다. 각 task의 입력, build, backend provenance, source 및 compact plan은 원래 adapter가 검증한다. 결과 폴더는 비어 있어야 한다. 재개·덮어쓰기·기존 claim 자동 제거는 지원하지 않는다.

Linux affinity·physical core·보이는 cgroup quota·남은 memory에서 1..64 rank를 입장시킨다. OpenMPI 명령은 localhost, nooversubscribe, 고정 rank guard로만 구성한다. rank guard는 외부 plan SHA, source/binary SHA, 정확한 OS CPU affinity를 확인한 뒤 고정 Fortran dispatcher 인자만 exec한다. 부동소수 reduction, precision/tolerance 변경 및 kernel SIMD를 추가하지 않았다. 단일 rank는 기존 dispatcher의 순차 fallback이다.

## 수명과 자원 제어

nonroot UID/EUID와 **이미 위임된 cgroup v2 parent**가 필요하다. parent의 controller 설정은 변경하지 않는다. 새 자식 cgroup에 memory.max, swap.max=0, pids.max, cpu.max, oom.group=1과 하위 cgroup 생성 금지를 쓰고 값을 다시 확인한다. native task의 memory_mib는 고정 rank당 주소공간 상한 1024 MiB 이하여야 한다. job memory.max는 rank 수 × 1 GiB다. 이는 병렬 Python/native 프로세스의 총 메모리 사용을 제한하며 모든 작업이 그 안에서 완료된다는 보장은 아니다. OOM/비수렴/미완료 결과는 실패로 남긴다.

fork된 launcher 자식은 exec 전에 자기 자신을 새 cgroup으로 이동한다. descendants는 이를 상속한다. native worker의 `start_new_session=True`는 cgroup membership을 바꾸지 않는다. 벽시계 제한, 예외, SIGINT/처리된 SIGTERM, leader 종료 후 남은 descendants에 대해 cgroup.kill을 쓰고 cgroup.events의 populated=0을 확인한다. `/proc` PID scan, process-group-only kill 또는 MPI root 우회로 대체하지 않는다.

MPI 전에 같은 host와 controller에서 **실제 synthetic detached-session probe**를 반드시 실행한다. leader 종료 후 새 session의 grandchild가 살아 있는 조건을 만들고 cgroup.kill/populated=0까지 확인해야 MPI로 넘어간다. 이 probe에는 HH·MPI 계산이 없다.

이 guard는 신뢰하는 같은 UID의 과학 코드에 대한 수명·자원 제어다. 악성 코드가 스스로 다른 위임 cgroup으로 이동하거나 권한을 가진 외부 프로세스가 job을 옮기는 상황을 격리하는 보안 sandbox는 아니다. supervisor 자체가 SIGKILL되거나 host가 종료되는 경우 Python finally는 실행되지 않으므로 production에서는 해당 launcher를 수명 관리하는 기존 system service/scheduler가 필요하다. 여기서 서비스 설치·delegation 생성·권한 상승은 하지 않는다.

Linux 근거: [kernel cgroup v2 문서](https://docs.kernel.org/admin-guide/cgroup-v2.html)의 process inheritance, cgroup.kill, cgroup.events, CPU/memory/pids interface. cgroup.kill은 session 구분 없이 하위 cgroup의 프로세스를 제거하고 동시 fork를 처리한다. populated=0은 살아 있는 하위 프로세스가 없다는 커널 상태다.

## 실행과 반환

정상 nonroot NCP host에서 원래 build 문서에 따라 OpenMPI/Fortran을 구축하고, system runtime의 mpirun 실제 파일과 build receipt를 고정한다. 이 wrapper는 sidecar MPI의 LD_LIBRARY_PATH/OPAL_PREFIX를 임의로 주입하지 않는다. MPI binary의 runtime linkage가 정상인 host가 필요하다. 같은 UID에 위임된 parent의 cpu/memory/pids controller가 이미 활성화되어 있어야 한다.

```bash
python -B launcher.py \
  --preparation ABS_PREPARATION_JSON --preparation-sha256 EXACT_FILE_SHA \
  --mpi-build ABS_MPI_BUILD_JSON --mpi-build-sha256 EXACT_BUILD_FILE_SHA \
  --mpirun ABS_CANONICAL_MPIRUN_BINARY --mpirun-sha256 EXACT_MPIRUN_FILE_SHA \
  --cgroup-parent ABS_EXISTING_DELEGATED_PARENT \
  --output ABS_NEW_RUN_DIRECTORY --ranks 2 --reserve-mib 1024 \
  --wall-seconds 300
```

기본 명령은 계획/입장 점검이다. `--execute`를 추가하면 synthetic containment probe 뒤 MPI를 실행한다. 출력의 HOST_PLAN/HOST_RUN과 각 rank binding은 새 경로에 기록된다. `HOST_RUN`의 성공 상태는 전체 선택 목록의 durable envelope, 정확한 task/build/window/limits, 모든 rank binding, source identity와 빈 cgroup을 검증한 **조건부 compact-interior collection**뿐이다. endpoint/full-domain/normalization/final D/production 판정을 의미하지 않는다. 실패한 run도 partial output inventory를 남기며 성공한 task 재실행을 자동 허용하지 않는다.

## 현재 검증 범위

이 작업 공간은 root 실행이며 위임된 cgroup을 사용할 수 없다. root를 우회하지 않았고 native MPI 및 실제 cgroup containment는 실행하지 않았다. ordinary directory를 cgroup처럼 꾸며도 거부한다. 실제 subprocess로 기존 process-group-only 종료에서 setsid grandchild가 남는 반례와 direct-child wall timeout을 확인했다. 후자의 cgroup API는 mock이므로 Linux cgroup 전체 종료 증명으로 세지 않는다.

독립 검토와 machine-readable `RESULT.json`을 함께 참조한다. source/contract 구현, 실제 detached-session production probe 미실행, 실제 MPI 미실행을 구분한다.
