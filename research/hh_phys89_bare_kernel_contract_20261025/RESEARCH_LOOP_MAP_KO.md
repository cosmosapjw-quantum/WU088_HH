# PHYS89 연구 루프 단계별 근거

이 표는 ENDF_MF33_PULLBACK_AND_TYPED_NUCLEAR_CONSUMER_INTERFACE 자식의 유한 workflow이다. 선택 물리 노드는 PARTIAL_INPUT_DEPENDENCIES, 전체 물리 완료율은null이다.

| 단계 | 역할 | 현재 근거/상태 |
|---|---|---|
| R1 | 연구 위치·계약 | 복원 계약·이론·원전·부모identity 재사용 완료 |
| R2 | 근거·재사용 | 복원 계약·이론·원전·부모identity 재사용 완료 |
| R3 | 주장·전제 정렬 | 복원 계약·이론·원전·부모identity 재사용 완료 |
| R4 | 가설·표현 탐색 | 복원 계약·이론·원전·부모identity 재사용 완료 |
| R5 | 구성적 유도 | 복원 계약·이론·원전·부모identity 재사용 완료 |
| R6 | 독립 검증 | 독립 R6 revision4 actualPASS; P89-R6R-01 CLOSED |
| R7 | 판별 검증 | 새 원행렬/유한fixture 실제 검증 대기 |
| R8 | 결과 판정 | 실제 검증과독립판정후 |
| R9 | 정식 결과·코딩 연결 | S2보고서예정 |
| R10 | 종료·재개 | FINAL게시·복원·중앙·인계 대기 |
| C1 | 목표·baseline | CONTRACTrev4의식·domain·수용조건 완료 |
| C2 | 식–데이터–코드 | CONTRACTrev4의식·domain·수용조건 완료 |
| C3 | 수치 설계 | CONTRACTrev4의식·domain·수용조건 완료 |
| C4 | 실행 DAG·자원 | lower-tier 구현완료·독립staticPASS; source실행0 |
| C5 | 구현 | lower-tier 구현완료·독립staticPASS; source실행0 |
| C6 | 구현 검증 | S1게시와dualACK이후 bounded실행 |
| C7 | 과학 검증 | S1게시와dualACK이후 bounded실행 |
| C8 | 수치·재현성 | S1게시와dualACK이후 bounded실행 |
| C9 | 독립 검토 | 독립raw검토예정 |
| C10 | 판정·인계 | FINAL인계대기 |

S0 actual9/20=R1–R6+C1–C3; R6 revision4 actualPASS로 채택했다. S1 11/20, S2 18/20, 최종R10/C10 완료20/20은 서로 다른 시점의 불변 snapshot으로 보존한다.
모든 단계의 completed는 해당 자식 범위이며 nuclear supplier와 named consumer를 물리적으로 완료했다는 뜻이 아니다.

S1 current11/20=R1–R6+C1–C5. Scientificidentity `c688ab6b06ab1e94781645e174cd555423ba49fc15d6b76c31acef3890f2e8b2`; 실제primary/reference는아직0.
