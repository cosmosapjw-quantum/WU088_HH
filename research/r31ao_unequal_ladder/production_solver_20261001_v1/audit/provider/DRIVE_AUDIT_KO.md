# WU088_HH Drive 데이터베이스·계획·runtime 근거 조사

외부 읽기만 수행했다. Google Drive plugin의 google-drive 스킬을 따랐으며 외부 쓰기·과학 실행·획득 코드 실행은 없다. 대상은 WU088_HH 및 명시적으로 연결된 R31 자료다. 관련 없는 BASS CR/HE 본문은 읽지 않았다.

## 검색 범위와 완전성

- canonical folder `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM`: `list_folder(top_k=1000)`의 122개 직접 자식 전부. 한도 미달이고 하위 폴더 없음.
- 전역 `search(query="WU088",item_type="document",topn=100)`: provider next_page_token을 그대로 사용하여 100+31개, 두 페이지 종료.
- 전역 `search(query="WU088",item_type="folder",topn=100)`: 12개 폴더, continuation 없음. canonical을 포함한 12개 모두 live folder listing으로 열람. 나머지 11개는 각 3/16/5/6/1/1/1/1/3/2/7개로 cap 미달.
- 상위 BASS folder `1pkohlay5eIfFJsBwPZ_yn2jIZONZjesI`: 1000개로 cap 도달. `list_folder`는 continuation 입력/출력을 노출하지 않는다. top_k=10000은 provider 최대1000으로 거부되었다. 따라서 **전역 모든 binary/archive의 완전한 목록이라고 주장하지 않는다**.
- canonical-parent search, WU088 DATABASE, R31AO, WU088 PROMPT, WU088 RESEARCH LOOP 및 name/modifiedTime filter 검색도 기록했다. 중요하게도 canonical search는0건인데 live listing은122건이다. 검색 인덱스/지원 MIME 범위의 누락을 실제로 확인했으므로 빈 검색을 파일 부재의 증명으로 사용하지 않는다.
- 정확한 tool/args/page별 결과는 `QUERY_COVERAGE.json`, 응답 원본은 `raw/`, 관련 객체270개의 ID·이름·MIME·bytes·날짜·발견 경로는 `INVENTORY.json`이다. 전역 document 결과의 일부는 타 WU088 계열이므로 정규 inventory에서 범위를 제한했다.

canonical 및 조사한 HH folder에서 최신 객체는 coordinator RETURN `1AENKcCzRcDmiloesGEHC5fMzHAa8HE8i`, 2026-10-01T07:19:08.877Z이다. 조사 범위에서07:20UTC 이후의 native/host/runtime RETURN은 발견하지 못했다. 새 native 성공을 추론할 근거가 없다.

## 실제 읽은 최신 DB

Drive `169bY3hBm0lo7hQswz4Dv6Qjprh0HGxYw`의 `WU088_HH_R31AO_DATABASE_20261001_v3.zip`을 한 번 내려받았다. bytes330090, SHA256 `d6b4eb2f059d8a230ce54093317068de413d1062b28c0a0895c2973118ab485d`가 기존 receipt와 일치하며 ZIP CRC도 확인했다. 36개 member 중 본 SQLite는1191936bytes, SHA256 `6be04d2337d82a3712c40e910237920568157a1669b2b4ad6595e861d1026694`다. SQLite는 `mode=ro&immutable=1`로 읽었고 전후 SHA가 같다. `PRAGMA integrity_check=ok`, foreign_key_check 결과0행이다. 함께 포장된 rollback journal은45656bytes이며 실행하거나 재적용하지 않았다.

| 실내용 | 행 수 |
|---|---:|
| canonical source_catalog |68|
| historical source_versions / sources |79 /79|
| acquired_files / assets |66 /66|
| source_file_links |71|
| blocker_map |53|
| code_version_policy |15|
| acquisition_events |103|
| report_sections |22|
| report_example_rows |9|

`DATABASE_CONTENT_AUDIT_RAW.json`에 실제 sqlite_master schema와 모든 table/view count를, `DATABASE_CONTENT_DETAILS.json`에 질문에 관련된 행을 기록했다. 이 DB는 **successor acquisition database**다. `theorems`, `modules`, `tests`, `artifacts` entity table은 없다. 원 보고서에서 명시적으로 회수된 예시는 sources4행·blockers5행뿐이다. `original_research_database_status` 자체가 그 네 entity table이 export되지 않았고 원 DB가 복구되지 않았다고 명시한다.

이는 기존 repo의 T1–T5 증명문서가 없다는 뜻이 아니다. 문헌 획득 DB와 이후 실제 증명/구현 ledger의 권위를 결합해야 하며, DB의 source acquisition 성공을 theorem closure 또는 certificate 성공으로 승격하면 안 된다.

## 서로 다른 DB/아카이브 계보

1. 원 Deep Research DB: `WU088_HH_R31AO_LITERATURE_DATABASE_20261001.zip`, 보고된 SHA `ab875d3e4fa771b34bdc1026042c38553b473b98f23e00e809d21c3b367948a9`. 이번 조사 범위에서 원 객체를 찾지 못했다. 전역 archive 검색 한계 때문에 존재하지 않는다고 단정하지 않는다.
2. v1 acquisition catalog: v2 archive의 `previous_v1/catalog/acquisition.sqlite`, manifest SHA `a2952c1250f33a900983f121bfb1d55eddb31c0f7962e79de391dcf8eb9d1fca`. Library의 개별 `acquisition.sqlite`를 실제 회수하여 이 SHA와 일치함을 확인했다. bytes274432이며 내용검사를 마쳤다.
3. v2 acquisition catalog: `catalog/acquisition.sqlite`, SHA `aff168a3a5f0e4584756dcab2f8f621a443f883439833535aeb231dcf780c1c6`. 이 버전만 아직 manifest identity 검증 수준이며 SQLite 실바이트 내용검사는 미완료다.
4. 부분 재구성 DB ZIP: `reconstructed_database/WU088_HH_R31AO_LITERATURE_DATABASE_RECONSTRUCTED_20261001_v1.zip`,29050bytes, SHA `34e0b4c81ed2b24f2008d8504f47714aa6e70f6da04bf0afbf65d912e2c9b4f1`. Library에서 실제 회수하여 SHA/ZIP CRC를 검증하고 내부 SQLite도 읽었다. 원 DB와 동등성은 주장되지 않는다.
5. v3 acquisition DB: 위에서 실제 내려받아 읽은1191936byte SQLite. 이전 acquisition 행을 보존하고 catalog·file·version·report·backup 조회를 정규화했다.

v1/v2 raw archive와 v3 ZIP은 서로 대체 가능한 동명 복제가 아니다. v3에는 paper/code payload가 들어 있지 않고 v2 content-part union을 참조한다. 조사한 정규 inventory에서 서로 다른 ID의 동일 title 중복은 없었다. byte 중복 여부를 대용량 payload 전체에 대해 새로 검사한 것은 아니다.

v2 parts는 각각 Drive `1KpfvR1QJUcf206bMcK4kpuxhJVNigHci`(54848781B), `1Dkc4zY1biPnXg0Ocn3YvPi1yQCHOP6px`(51909458B)로 존재한다. 원문 manifest와 return을 읽어 위 catalog member identity를 확인했다. 두 part의 streaming fetch는 성공했지만 반환 transport에 대한 workspace Range 요청은 만료 전 HTTP403/error1010으로 거부됐다. 범용 download_file 도구의32MiB 한도를 우회하지 않았다. 이어서 Library의106758217byte 정규 v2 ZIP `libfile_4187dc9a7578819192b266ea9b96f856`을 정확히 찾고 prepare_materialize를 호출했지만 direct workspace 경로 대신 서명 URL을 반환했다. 해당 URL의 정상 GET2회와 Range1회가 모두 HTTP502/Connection refused로 실패했다. `ARCHIVE_TRANSPORT_LIMIT.json`에 두 provider 경로의 한계를 기록했다. **대형 v2 ZIP 복원이나 v2 SQLite 내용검사를 완료했다고 주장하지 않는다.**

## Library 보완 조회와 실제 v1·부분 재구축 내용

정확한 파일명 검색에 이어 2026-09-29T00:00:00Z 이후 Library metadata를200+200+200+133개, 네 페이지의 continuation이 끝날 때까지 읽었다. 해당 기간733개 중 HH 관련 metadata85개를 별도 정리했다. 관련 없는 CR/HE 본문은 열지 않았다. 검색·페이지별 원응답은 `raw/library_*.json`, 정규화 목록은 `LIBRARY_INVENTORY.json`이다. 이 조회는 전 기간 모든 Library 파일에 대한 완전성 주장이 아니다.

| 실제 DB | bytes | 주요 실제 행 수 | integrity / FK |
|---|---:|---|---|
| v1 acquisition catalog |274432|sources67, assets60, attempts20, relations39, blocker_map53, citation_occurrences41, metadata11|ok /0|
| 부분 재구축 연구 DB |86016|sources4, blockers5, theorems0, code_modules0, tests0, artifacts0, 세 join table 모두0|ok /0|

두 SQLite 모두 `mode=ro&immutable=1`로 읽었고 읽기 전후 SHA256이 동일하다. 부분 재구축 SQLite SHA는 `64546bb1b31ec3de4588d79e19a3037f573b7c5422f80a8387d8b3e40f164933`이다. v1은 `metadata.not_original_deep_research_database=true`이며 과학 실행이나 rigorous certificate가 없다는 당시 상태를 명시한다. 부분 재구축은 schema의 존재와 entity 내용의 복구를 구별한다. 원 보고서가 주장한 sources19/theorems9/code_modules9/tests15/artifacts7/blockers8 중 명시 CSV 예시4+5행만 삽입됐으며, 나머지 원 DB 행은 복구되지 않았다. 이후 repo의 증명문서 존재 여부와는 별개다.

실제 v1·v3 비교에서 v1 source ID67개와 asset ID60개가 모두 v3에 존재하고 공유 asset의 SHA 변경은0개다. v3 historical source records는12개 늘어79개이며 canonical source는 C14 한 개가 추가되어68개다. 상세 schema·모든 실제 행은 `DISTINCT_DATABASE_BYTE_AUDIT.json`, 계보별 검증수준은 `DATABASE_VERSION_CATALOG.json`, 비교는 `V1_V3_CONTENT_COMPARISON.json`에 있다. v2 내용을 v3에서 추정해 복원했다고 주장하지 않는다.

Library의 원 Deep Research 보고서 JSON `libfile_863ccecfd60c81918103b2d48302c7cd`도 실제 회수했다(650126bytes, SHA `90021a8379bdd7e077fff33329ce057a6f8fcee35cfab831528ea02802f6dd71`). final report 본문은46605bytes/937lines, SHA `ae78d5b5a5acd9ff7945874598aee8a7a114dbb88eeb2538cf8465c634aaf5a7`로 이미 보존된 원 보고서와 일치한다. 본문의 옛 sandbox ZIP/SQLite/CSV 링크는 원 파일 바이트 복구 증거가 아니다.

## 미확보 항목과 production 관련 문서

v3의 `v_current_missing`은 INTLAB14.1 개인 라이선스 source, COSY INFINITY10.2 등록·서명 라이선스 source, 원 Deep Research DB의3개 항목이다. 이는 chosen exact-rational/FLINT route에서 모두 필수라는 뜻이 아니다. 원 보고서937lines/22sections가 DB에 저장되어 있고 `provenance/ORIGINAL_REPORT.md`로도 포함된다.

Drive에서 두 개의 오래된 HH 모형 문서를 실제 읽었다:

- `WU088_HH_MODEL_FOUNDATION_FINAL_20260923_v1.md`, ID `1flCk0bdGWIfNYaTcmgZmZ_fGUEO6rJTb`, SHA `ff11a0d25a9d00c30b0de3f8ced74408de6b5c244dd12dd87ea541b7f7b7c309`.
- `WU088_HH_MODEL_CLOSURE_REPORT_20260923_v1.md`, ID `1gyKDx6XC_bfw40pxQqThlnUhZvtNO218`, SHA `93ceb0e3e342e778ad459f2feeda147f35e8cd228e61151736934e1af807d778`.

후자는 production 기준을 선택한 고정 유한 원자 모형의 내적 일관성과 정확한 구현으로 정의하며, 당시 전체 HH는HOLD라고 명시한다. mixed-H, ionic cross-centre O/H/D와 독립 dot-O, matrix-provider→propagator 연결, 궤적·끝점·관측량 오차 및 필요하면 b 적분이 남았다고 기록한다. 이는2026-09-23의 historical authority이므로 이후 R31 successor가 항목을 닫았는지는 현재 repo 증거로 별도 연결해야 한다.

이번 Drive 조사에서 원 최초 G0–G9 user prompt의 독립 파일을 찾았다고 주장하지 않는다. root가 따로 원 사용자 attachment bytes를 회수했으므로 그 SHA-bound 입력을 사용해야 한다. 여기의937line Deep Research 보고서는 그 prompt와 다른 artifact다.

## 검증 수준

v3 Drive ZIP, Library v1 catalog 및 부분 재구축 ZIP/SQLite와 원 보고서 본문의 실제 바이트를 새로 검증했다. v2 catalog 실내용은 transport 한계로 미완료다. 문헌 대용량 payload 전체, Dropbox 복원, 원 Deep Research DB 복원, actual HH native/certificate/production은 새로 검증하지 않았다. 이전 이론/실행 판정은 이번 DB 조사로 소급 변경하지 않는다.
