# Host process guard

`run_guarded.py`는 Linux에서 single-process native job을 실행하는 유한 자원 wrapper다. 이 도구는 실제 HH 실행 승인을 부여하지 않는다. native synthetic acceptance에 먼저 사용하며, 실제 science 명령에는 별도의 유효한 실행 범위가 필요하다.

wall timeout에는 process group에 SIGKILL을 보낸다. leader가 먼저 종료해도 남은 group을 종료하고 `PROCESS_CONTRACT_VIOLATION`을 반환한다. 종료 요청 후 orphan zombie의 재수거까지 보장한다고 주장하지 않는다. 의도적으로 새 session/group으로 이탈하는 자식은 이 single-process 계약 밖이다.

메모리 상한은 프로세스별 `RLIMIT_AS` virtual address space다. 전체 process-tree RSS 합계의 hard cap이 아니다. CPU time과 개별 output file size도 제한한다. 부모가 읽는 로그 preview는 64 KiB이고 CLI 실행 시 전체 로그는 새 output directory에 남긴다. process exit 0은 수학적·과학적 성공이 아니다. native returned ball radius, provenance와 acceptance 조건은 별도로 확인한다.

합성 검증은 정상 종료, 초과 allocation 거부, timeout, 잘못된 budget 거부, leader 이후 descendant 차단을 포함한다. 실제 HH binary나 callback은 실행하지 않았다.

```bash
python -B host_guard/run_guarded.py --wall-seconds 60 --memory-mib 2048 \
  --output-dir /absolute/new/synthetic-run -- /absolute/verified/native_synthetic
```
