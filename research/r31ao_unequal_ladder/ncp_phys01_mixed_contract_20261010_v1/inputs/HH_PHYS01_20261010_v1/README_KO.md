# HH-PHYS01: 광자 방출과 HH 반응의 비가산 물리

읽기: REPORT_KO.md → THEORY_KO.md → CLAIM_LEDGER.json → NCP_LOCAL_CODEX_HANDOFF_KO.md.

이 패키지는 기존 FT03+LCS의 국소 smooth source에서 광자 방출과 HH의 혼합 응답이 세 번째 시간 차수에서 나타나며, near-threshold 조건에서 비가산 억제가 됨을 유도한다. 원 source의 전체 H/He 비광자 반응을 제거하지 않았다. 실제 이력·BE 근·원자 primitive·NCP dispatch는 없다. 저장된 실제 source 상태에 대한 90자리 계수 진단은 유한 timestep의 오차 인증이 아니다.

결과 정본은 results/LOCAL_COEFFICIENTS_FINAL.json이다. results/LOCAL_COEFFICIENTS.json은 최초 numeric 직렬화 실패 시 생성된 빈 파일이며 실패 증거로 보존했다. failures/와 logs/에 원 실패가 있다. 최종 재현은 REPRODUCE_KO.md에 따른다.

원 SSOT bytes 여섯 개를 선택 회수하고 원 manifest와 대조했다. inputs/source/는 참조용 원문이며 실행하지 않는다. 논문의 empirical fit 정확도를 새로 인증하지 않았다. 제3자 독립 과학 심사나 formal proof-assistant 검증은 수행하지 않았다.
