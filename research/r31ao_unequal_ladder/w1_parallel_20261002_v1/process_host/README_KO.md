# 단일 native process 실행 경계

이 모듈은 기존 range solver의 수학·compiled kernel·입력·허용 오차를 변경하지 않는다. frozen `driver.run_task`의 입력, plan, source, binary, backend linkage 검증을 그대로 실행하고 `execute_bound_native` 함수만 명시적으로 대체한다. 새 wrapper의 `process_host` 항목은 이 차이와 새 executor source/build identity를 기록한다. 이전 tile00 receipt에는 이 항목이 없으므로 해당 실행에 소급 적용하지 않는다.

`guarded_exec.c`는 Linux `PR_SET_PDEATHSIG(SIGKILL)`을 설정하고 호출 시점에 넘겨받은 부모 PID를 재검사한 다음 동일 PID에서 `execv`한다. dispatcher가 실행하는 Python worker와 worker가 실행하는 native에 각각 적용한다. 단순 process group 종료에 의존하지 않는다. native는 별도 session으로 실행되지만 부모 사망 신호는 유지된다. setuid/setgid 및 file capability 실행 파일을 거절하며, 일반 실행 파일의 byte/path 안정성은 frozen driver와 동일하게 실행 직전 검사 이후 host filesystem이 안정적이라는 가정을 가진다.

native 전용 seccomp filter는 `fork`, `vfork`, `clone`, `clone3`를 EPERM으로 거절한다. 따라서 이 경로의 native에는 별도 자손 PID가 만들어지지 않는다. x86-64의 x32 syscall 경로도 거절한다. 지원하지 않는 architecture 또는 seccomp/rlimit 설정 실패는 실행 전 거절한다. pinned native source는 `flint_set_num_threads(1)`을 설정하며, worker/range integrator/cached callback/assembly source에서 process/thread 생성 호출이 없다. 이 경계는 임의의 적대적 executable을 위한 sandbox가 아니다.

각 native는 RLIMIT_AS 1024MiB, core 0, stdout/stderr file별 16MiB, CPU 125초 및 부모의 wall 125초 종료 제한을 가진다. 내부 solver의 wall 예산 120초는 그대로 유지한다. Python worker는 RLIMIT_AS 1024MiB 및 CPU 180초이며 dispatcher가 wall 180초를 관리한다. hard RLIMIT_AS는 자손에 상속되므로 512MiB wrapper에서 1024MiB native를 생성하려는 구성은 사용하지 않는다. 관측된 8GiB host에서는 3 workers × (wrapper 1024MiB + native 1024MiB) = 6GiB를 최대 주소 공간 합으로 잡고, 나머지 2GiB를 coordinator와 host overhead에 남긴다. 이 계산은 주소 공간 cap의 합이며 실제 RSS benchmark가 아니다.

일반 완료와 wall cap 경로에서는 직접 native PID를 `wait`해서 회수한다. 예외는 살아 있는 직접 child를 종료하고 wait한 후 전파한다. coordinator/worker 자체가 SIGKILL로 사라진 경로에서는 Linux가 부모 사망 신호를 전달하며 이 Python 코드가 native를 직접 reap했다고 주장하지 않는다. synthetic 검사에서 두 단계 cascade의 pipe EOF를 확인했다. `/proc`의 namespace별 PID 목록이나 cgroup `populated=0`을 증거로 사용하지 않는다. 커널 정상 작동 및 SIGKILL 처리라는 통상적인 운영체제 가정이 있다.

새 실행은 성공 여부와 무관하게 정확한 stdout/stderr bytes를 `<receipt>.stdout`, `<receipt>.stderr`에 저장하고 hash/size를 wrapper에 기록한다. validator는 실제 receipt 경로에 대응하는 sidecar만 읽는다. `Popen` 성공만으로 HH primitive 실행을 집계하지 않으며, 정확한 task/plan/input/build identity를 갖는 native JSON stdout이 반환됐을 때만 `native_execution_observed=true`를 기록한다. native가 output 이전에 종료되면 실행 여부를 입증하는 stdout이 없다는 상태를 남긴다. accepted result는 별도로 frozen native result validator, 실제 serialized radius, sidecar↔receipt equality를 통과해야 한다.

이 작업은 direct process 병렬화다. MPI 실행, NCP 64코어 측정, cgroup containment, full-domain scientific admission 또는 production admission이 아니다. host lifecycle 테스트는 synthetic Python 프로그램만 사용하며 HH 계산 호출은 0회다.

재현 명령:

```bash
python -B process_host/host.py build
python -B process_host/test_host.py
```

build 디렉터리는 create-only이며 host source 변경 후 기존 manifest를 조용히 덮어쓰지 않는다. numerical kernel은 이 build에서 다시 compile하지 않는다.
