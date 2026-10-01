# Native MPI 실행기 독립 검토

검토 결론은 **소스 및 실제 입력 결합 검증 통과, MPI·cgroup 실행 미검증**이다. 이 검토는 원래 수치 소스와 과거 실행 결과를 변경하지 않았다. 검토자가 새로 만든 준비 묶음에도 적분 결과는 없다.

## 확인한 경계

- 원래 `native_execution_20261001_v1`의 고정 native driver·Frozen107 입력·central plan·cached build에 연결되는 실제 준비 묶음을 생성했다. 외부 preparation SHA, manifest, binary, backend provenance, task index와 한계 설정을 실제로 검사했다.
- preparation에 새 SHA를 다시 넣더라도 임의 Python worker와 잘못된 작업 목록은 거부됐다. 실행기는 원래 생성기의 worker 내용을 재구성하고 작업 목록의 ordinal 및 기한을 직접 비교한다. CLI에는 임의 작업 명령을 받는 인수가 없다.
- 이미 존재하는 결과 또는 `.claim`은 재사용되지 않는다. 성공 수집은 예상 결과 파일 집합, native envelope의 전체 결합 조건, 모든 rank의 CPU 결합 영수증을 요구한다. 실패 후 파일 목록은 성공 수집과 구분된다.
- root는 계획 또는 cgroup 접근 전에 거부한다. 일반 디렉터리를 cgroup-v2로 오인하지 않도록 실제 파일시스템 유형을 검사한다. 위임된 domain parent와 `cpu memory pids` 제어기가 필요하다.
- child는 `exec` 전에 새 job cgroup에 들어간다. 이후 MPI rank·native worker가 새 session을 만들어도 cgroup 소속은 유지된다. 종료 처리는 process group 열거 대신 `cgroup.kill`과 `cgroup.events populated=0`을 사용한다. 이 문장은 코드 구조 검토 결과이며, 현재 환경에서 커널 격리를 실행해 확인했다는 뜻이 아니다.
- job별 총 메모리·swap·PID·CPU 상한을 읽어 확인하고, rank는 지정한 단일 OS CPU 결합을 읽어 확인한다. worker의 과학 계산 정밀도나 허용 오차는 이 계층에서 낮추지 않는다.

## 발견하여 수정한 문제

1. native manifest는 8 GiB까지 허용하지만 rank의 상속 hard address-space limit는 1 GiB였다. 이제 1 GiB를 넘는 요청을 MPI 시작 전에 거부한다. 더 큰 작업을 지원하려면 별도 예산 설계가 필요하다.
2. MPI 시작 표시가 `Popen`보다 먼저 참으로 설정됐다. 이제 시작 시도와 실제 process 생성 결과를 구분하며, pre-exec 실패는 시작으로 세지 않는다. 정리 자체가 실패해 증거를 반환하지 못한 경우 시작 여부를 임의로 확정하지 않는다.
3. 처음에는 launcher 자신의 cgroup 제한만 관측했다. 이제 지정한 target parent의 관측 가능한 조상 CPU·메모리 제한을 합치고 effective cpuset과 교집합을 취한다. 별도 mock 계층 검사에서 target quota가 1 CPU이고 cpuset이 `{2,3}`일 때 2-rank 요청 거부와 CPU 2의 1-rank 계획을 확인했다.

독립 검토의 최종 12개 경계 검사는 모두 통과했다. 세부 결과와 동결된 실행 소스 SHA는 `contract_run_final/REVIEW_RUN.json`에 있다. 앞선 9개 검사도 삭제하지 않고 남겼다. 추가로 구현자의 직접 subprocess 검사는 mock cgroup을 사용하므로 실제 cgroup 격리 증거로 취급하지 않았다. 구현자가 발견한 probe의 최초 문법 오류와 수정 이력도 보존돼 있으며, 최종 독립 검사는 수정된 모듈의 import와 root 거부를 확인했다.

## 남은 실행 조건

현재 root 작업 공간에서는 실제 MPI 또는 위임된 cgroup 실행을 수행하지 않았다. root 우회도 하지 않았다. 실행기는 지원되는 nonroot 호스트에서 `setsid` grandchild를 포함한 필수 실제 containment probe를 먼저 실행하도록 되어 있다. 그 결과와 NCP에서의 실제 rank·메모리·MPI 반환이 확보돼야 실행 경로를 검증했다고 할 수 있다.

이 계층은 신뢰하는 동일 UID의 연구 프로세스를 감독한다. 악의적인 cgroup 탈출이나 supervisor 자체의 `SIGKILL`을 격리하는 보안 sandbox가 아니며, 실제 운영에서는 외부 service manager가 필요하다. 자원 관측은 노출된 cgroup mount 범위이고 가용 메모리는 시간에 따라 변하므로 계획은 NCP 성능 또는 모든 실행 용량을 보증하지 않는다. 커널 상한과 후속 실패 검사는 그대로 적용된다.

또한 이 실행기는 원래 native driver에 결합된다. 이번에 추가한 log/refined driver, 전체 2,592개 과학 적분, 최종 D/epsilon, 전 영역 정확도 또는 production 승인을 이 검토로 통과시키지 않는다.
