# 데이터 사전

| 테이블/뷰 | 의미 |
|---|---|
| sources/assets/attempts/relations/blocker_map/citation_occurrences/metadata/recovery_updates/representation_identity/recovery_artifacts | 기존 v2 원형 테이블. 행·JSON 값을 수정하지 않음 |
| source_catalog | canonical 68개 출처의 현재 상태, 요청 판본, 확보 판본, 제한, 백업 연결 |
| source_versions | 기존 source 79행의 canonical parent 및 원 JSON |
| acquired_files | 실제 확보 bytes 66개. 경로는 기존 v2 archive 내부 상대 경로 |
| source_file_links | 직접/판본 파일과 equivalent URL 참조의 명시적 연결 |
| acquisition_events | 원 실패·회수·회복 경로 기록. event 중복 경로는 근거 origin별 보존 |
| code_version_policy | 원 정책 15행 보존. version_acquired는 raw source 없으면 NULL |
| acquisition_gaps/v_current_missing | 주요 미확보 3개와 판본 제한 6개를 구별 |
| backup_objects/v_payload_backup_sets | 기존 v2 각 provider의 두 content parts를 하나의 backup set으로 연결 |
| original_research_database_status | 분실 원 DB, expected reported SHA, 부분 재구성본 범위 |
| report_documents/report_sections/report_search | 원 보고서의 본문/섹션/FTS5 검색. 원 미수출 entity DB와 구별 |
| catalog_search | 제목·저자·식별자·상태 FTS5 검색 |

NULL은 미관측/미확정이다. `publisher_version_available`은 기존 증거에서 출판 레이아웃이 확보됐는지에 대한 값이며 publisher 서버 직접 다운로드 여부와 다르다. `publisher_bytes_compared=0`이고 정리/수식 권위 자동 승격은 0이다. `version_is_latest_stable=NULL`은 확보 bytes가 현재 최신인지 검증하지 않았음을 뜻한다. COSY는 stable target만 선정됐고 코드 미확보다.

`backup_object_ids`는 기존 v2 raw payload 보관 object를 가리킨다. 새 DB/패키지 저장 object는 detached RETURN.json에 있다. `restore_verified=0`은 provider 원격 bytes를 readback하지 않았음을 뜻한다. 로컬 hash/bytes 검증과 혼동하지 않는다. `original_filename`에 HTTP Content-Disposition이 없으면 URL basename이라는 근거를 기록한다. acquired_files의 source_id는 직접 parent이며 alias 파일 연결은 source_file_links에 있다.
