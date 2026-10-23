# 게시 후 전달 identity와 검증 권위

이 Git 문서는 자신의 최종 commit SHA나 자신을 포함한 ZIP의 SHA를 내부에 예측해 넣지 않는다. 최종 권위는 다음 두 곳이다.

1. [PR141 최종 본문](https://github.com/cosmosapjw-quantum/WU088_HH/pull/141): actual final HEAD, final ZIP/JSON size·SHA·양쪽 provider IDs·readback 판정.
2. 외부 `PHYS84_FINAL_DELIVERY_20261023.json`: actual remote commit/tree/parent, prepared artifact identity, final ZIP 원본과 양쪽 실제 다운로드·전체 복원 영수증, 단계별 ACK, 코드 동결, 누적 실행과 미실행, 다음 재개.

외부 JSON 자신의 SHA와 provider ID/readback 결과는 순환 참조를 피해 PR 본문에 둔다. Git metadata와 stage ACK를 실제 최종 전체 restore로 대체해 읽지 않는다. 실제 최종 공급자 파일을 내려받아 검증한 결과만 외부 JSON에서 PASS로 기록한다.

현재 과학 상태는 고정된 [STAGE_STATUS](STAGE_STATUS.json)와 [ledger](EXECUTION_LEDGER.json)를 따른다. PHYS83 완료는 재사용했고, PHYS84는 v5 준비·정적 검토 통과 뒤 shared lease에서 검증 child 시작 전에 대기했다. 새로운 science identity 또는 결과 16행은 없다. S2 과학 archive도 생성하지 않았다. Final은 준비 artifact의 전달이며 새 수치 완료 주장이 아니다.

## 복원 범위

Final ZIP의 outer payload 전부를 실제 추출하고 각 member CRC, payload SHA, fresh Git blob, 추출 재해시와 8 prepared frozen files를 검증한다. Nested 원 PHYS83 ZIP과 JSON은 exact raw bytes를 유지한다. 추가로 downloaded outer에서 꺼낸 parent ZIP의 필수 입력 4개와 lease 1개, 합계 89,283 bytes를 별도 `dependency_restore` 아래 실제 추출·CRC·SHA·Git blob·재해시한다. Historical parent 전체 385 members / 57 science frozen files의 이전 full restore 근거는 재사용하며 이번에 반복했다고 쓰지 않는다.

Standalone 복원물에서 실행 준비를 할 때 child unit과 dependency_restore의 parent unit을 같은 research 부모 경로에 배치한다. 과거 완료 science를 실행해 복원 여부를 확인하지 않는다. 실행 전에 실제 refs/AGENTS/병렬 변경/백업·budget과 pinned shared lease를 읽는다. Source 계산은 CODEX_HANDOFF의 gate를 따른다.

S0 최초 ZIP은 workspace 초기화 전에 upload가 실패하여 lost/not uploaded이며, S0_RECOVERY는 별도 SHA다. 원 private intake 51개 전부의 exact 복구를 주장하지 않는다. 복구·오류 원인은 recovery와 implementation 영수증에 남아 있다. 양쪽 final-delivery JSON의 원문 SHA/identity readback은 별도 최종 검증이다.

HH_R10=OFF. Production admission NOT_ISSUED. 중앙 및 외부 consumer owner의 승인은 별도다.
