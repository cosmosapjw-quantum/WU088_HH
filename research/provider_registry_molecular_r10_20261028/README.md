# Molecular R10: full-generator triangular bound

고정된 HD 입력에서 projected sink를 보존적 생성자에 포함하고, zero-sum 잔차와 coarse 오차의 삼각 비교계를 정확한 바깥쪽 반올림으로 계산한다. 이론·코드 두 노드는 `COMPLETE_SCOPED_CONDITIONAL`로 채택됐고 과학 DAG는 **21/36**이다. 실제 HD reactive source 및 물리 consumer 연결은 입력 대기다.

## 읽기 순서

1. [REPORT_KO.md](REPORT_KO.md): 최신 source 조사, 유도, 구현, 실제 결과, 제한, 게시·백업.
2. [HANDOFF_KO.md](HANDOFF_KO.md): 다음 대화에서 이어갈 정확한 상태와 복사 가능한 지시문.
3. [SCIENTIFIC_ADMISSION.json](SCIENTIFIC_ADMISSION.json), [SCIENTIFIC_PAYLOAD_MANIFEST.json](SCIENTIFIC_PAYLOAD_MANIFEST.json): 과학 채택과 41개 파일의 정확한 identity.
4. [theory/PROOF_KO.md](theory/PROOF_KO.md), [theory/THEOREM_AND_API_KO.md](theory/THEOREM_AND_API_KO.md): 전체 증명과 구현 계약.
5. [reviews/C9_FINAL_REVIEW.json](reviews/C9_FINAL_REVIEW.json): 최종 독립 심사, 열린 중대 지적 0건.
6. [delivery/PUBLICATION_INDEX.json](delivery/PUBLICATION_INDEX.json): 실제 단계별 source·ZIP·두 provider 영수증.

## 실행 상태

Primary 175/175 PASS, 독립 reference 469/469 PASS, 9,860 성분 비교에서 실패 0. 각 Python 실행은 한 번이며 합계 OS CPU는 0.511886 s다. Wolfram의 15개 zero residual은 실제 경고와 함께 qualified corroboration으로 보존한다. 저장된 표본 비교는 사전 허용오차를 적용했다. Native9 raw 상계의 퇴행도 결과에 보존한다.

이 연구 단위의 primary/reference/CAS 잔여 실행 수는 **0/0/0**이다. 저장 결과를 읽거나 검증 가능한 API를 재사용할 수 있지만, 완료한 실행 allowance를 새 세션에서 초기화하지 않는다. 다음 과학 실행은 바뀐 실제 입력 또는 [새 구체적 의무](followup/NEXT_INPUT_CONTRACT.json)를 별도 유한 계약으로 정한 뒤 수행한다.

## 전달 범위

과학 채택 source는 `a2c62aaad2396d1720a12e74774e52374baa4c33`다. 뒤의 metadata source와 자신의 FINAL ZIP 영수증은 기존 draft [PR150](https://github.com/cosmosapjw-quantum/WU088_HH/pull/150)에서 확인한다. FINAL own receipt를 그 own source에 넣는 자기 참조는 만들지 않는다. 각 ZIP의 범위는 단계별 R10 source·AGENTS·고정 의존 파일 7개이며 전체 Git history mirror는 아니다.
