# HH Atomic-Reuse Plan v2 시작점

이 패키지는 첨부 REI Atomic-Reuse DAG를 WU088_HH의 현재 PHYS12 결과와 연결한 연구계획이다. 새 과학 실행은 0회다.

1. DEVELOPMENT_PLAN_KO.md: 결정·전체 프로그램 내 HH 역할·local DAG·후속 관측량과 종료 조건.
2. NEXT_DAG.json, DAG_CROSSWALK.json, TASK_CARDS.jsonl: local 8개 노드와 원 global 17개 노드의 관계.
3. HH_RETAINED_RESULTS.json: PHYS12의 기존 PROMOTE_SCOPED와 정확 source/result 참조.
4. contracts/: 현재 준비된 HH 제공 계약과 소비 요청·관측량 판정 규칙. runtime admission은 별도다.
5. review/PLAN_REVIEW.json: 독립 계획 검토.
6. NCP_TASKS.json, HANDOFF_KO.md, RETURN_TEMPLATE.json: 현재 queue 없음과 미래 경로별 조건.

첨부 원본과 과거 계획은 inputs/와 baseline/에 보존했다. PHYS12 자체는 원 commit dcea5dc6545736e6f4afa5acf4b7eabd428485e8에 남아 있고 완료 ZIP에는 봉인된 전체 PHYS12 패키지도 포함한다. 새 계획이 global RUX 또는 native/full-history 물리 판정을 올리지는 않는다.
