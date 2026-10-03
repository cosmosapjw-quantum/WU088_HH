# 이전 체크포인트와 MPI 증거 마감 검토

`RECOVERY_INVENTORY.json`에 등록된 이전 `native_execution_20261001_v1` 파일 **472개 전부의 SHA-256과 크기가 일치**했다. 누락·변경은 없었고 mtime 변화도 없었다. mtime은 참고값으로만 비교했으며 합격 조건으로 삼지 않았다. Scope에 고정된 inventory 자체의 SHA도 일치한다.

MPI 실행기와 검사 소스 5개의 현재 SHA가 구현자 결과 및 두 최종 독립 검토 영수증과 일치한다. 구현자 로그의 10개 검사 이름은 현재 검사 소스와 일치하고 종료는 성공이다. 독립 검토 12개도 모두 통과했다. 서로 겹칠 수 있는 두 검사 묶음을 합쳐 고유 검사 수라고 주장하지 않았다. 수치 실행이나 검사는 이번 마감 검토에서 반복하지 않았다.

**MPI 실행 상태는 여전히 차단**이다. 보존된 실제 probe는 root 거부로 종료 코드 2를 반환했고, 현재도 UID/EUID가 0이며 해당 cgroup parent에 `cpu memory pids` subtree 제어가 활성화돼 있지 않다. root 우회는 없었다. 실제 cgroup 격리 실행·MPI 실행·이 실행기를 통한 HH 적분은 각각 0회다. mock cgroup 검사와 실제 kernel containment를 구분한다.

nonroot 위임 환경에서 필수 detached-session containment probe 및 실제 OpenMPI/NCP 실행이 남아 있다. 이 실행기는 기존 native driver에 결합되어 있고 이번 log/refined driver의 MPI 연결을 인증하지 않는다. 과학적 승인과 production 승인도 그대로 보류한다.

기계 판독 영수증: `PRIOR_AND_MPI_REVIEW.json`.
