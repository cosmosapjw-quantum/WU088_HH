# WU088 R31AO 데이터베이스 구축 결과

검증된 v2 acquisition.sqlite를 기반으로 후속 DB를 만들었다. 기존 10개 테이블의 모든 행은 그대로 보존했다. 새 원문을 수집하거나 과학 계산을 실행하지 않았다.

- 고유 출처: 68개 (원 Deep Research DB artifact 1개는 별도)
- 기존·회복 판본 기록: 79개
- 실제 확보 파일: 66개, 전부 SHA256/bytes 재검증
- 회복 이전의 실패 기록, 성공 파일 회수 기록, 회복 경로 기록을 각각 구별한 event: 103개
- 코드 버전 정책: 15개 (COSY 이전 조사와 공식 10.2 대상 구별)
- 주요 미확보: INTLAB raw package, COSY raw package, 원 Deep Research DB bytes
- 별도 판본 제한: P04 출판판 비교, 5개 인용 URL의 원래 snapshot

P04는 저자의 기관 PostScript manuscript이며 publisher PDF가 아니다. P06은 Purdue에서 확보한 출판 레이아웃 scan이며 publisher 서버 bytes와 직접 비교하지 않았다. COSY 10.2 manual은 원 코드 확보를 뜻하지 않는다. CINTE는 COSY의 대체 구현으로 채택하지 않는다.

FLINT 3.4.0 프로젝트 pin, FLINT 3.6.0 조사본, NumPy 2.3.5 기존 참조를 구별해 보존했다. COSY 10.2는 이전 회복 단계에서 확인한 공식 stable 대상이며 raw source는 미확보다. 이 단계에서는 최신판을 다시 조사하거나 변경하지 않았다. 알 수 없는 release date/license/dependencies는 NULL과 기존 근거 상태로 보존했다.

원 `WU088_HH_R31AO_LITERATURE_DATABASE_20261001.zip`은 여전히 미복구다. 기존 부분 재구성본은 명시적으로 복구 가능한 source 4행과 blocker 5행만 담는다. 원 보고서의 나머지 theorem/module/test/artifact 행을 만들어내지 않았다. 대신 원 보고서 본문과 22개 섹션에 읽기 전용 검색을 제공한다. 원 DB와 의미적 동등성은 주장하지 않는다.

DB 파일과 CSV/JSON, schema.sql, example_queries.sql, offline INDEX.html, 재현 스크립트를 제공한다. 원문 PDF/PS와 코드 tar/ZIP은 이미 보존된 v2 원문 archive에 있다. 새 패키지는 해당 원문 66개의 경로·해시·출처·기존 이중 백업 object IDs를 기록하며 대용량 payload를 중복 포함하지 않는다. 각 provider의 part01+part02 union이 한 전체 payload backup set이다. 개별 파일이 어느 part에 속하는지는 추정하지 않았다.

검증: SQLite integrity, 외래키, 기존 전체 행 보존, 201개 baseline manifest payload와 203개 content-union path, 파일 66개의 해시·크기·magic/archive headers, 11개 논문 원문 연결, 5개 동등 참조, 명시적 버전 pin 및 검색을 확인했다. ZIP CRC 확인과 archive metadata 읽기는 실행 없는 파일 검증이다.

기존 과학 상태는 그대로다: `B_ORDER_VERDICT_STABLE_OVER_128_160_192`, `SOURCE_ACCURACY_BOUND_UNAVAILABLE`, `RIGOROUS_REFERENCE_CERTIFICATION_BLOCKED_BY_MISSING_ERROR_BOUND`. `certified_epsilon=null`, `certified_eta=null`, `rigorous=false`. science/producer/certificate/downloaded-code 실행 모두 0이다.

새 Git 게시 및 Drive·Dropbox create-only 백업 결과는 외부 `RETURN.json`에 기록한다. DB 내부 backup object는 기존 v2 원문 보관본에 대한 prior receipt 근거다. Provider 검증은 ACK + object ID + parent/path + metadata size이며 실제 원격 bytes download/readback은 수행하지 않았으므로 `RESTORE_VERIFIED=false`다.

최종 수집 상태: `LITERATURE_ACQUISITION_COMPLETE_WITH_DOCUMENTED_UNOBTAINABLE_ITEMS`.
