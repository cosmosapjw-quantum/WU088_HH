# WU088 R31AO 후속 수집 DB v3

`WU088_HH_R31AO_ACQUISITION_DATABASE_20261001_v3.sqlite`을 SQLite 도구로 열거나 `INDEX.html`을 브라우저에서 열어 출처를 검색한다. 필드 설명은 `DATA_DICTIONARY.md`, SQL 예제는 `example_queries.sql`에 있다.

이 DB는 기존 수집 DB의 후속본이다. 분실된 원 Deep Research DB를 복원했다고 주장하지 않는다. 원문 payload는 별도 기존 v2 archive에 있고, `files.csv`와 `backup_objects.csv`로 찾을 수 있다. 두 content-part ZIP의 합집합을 사용한다.

빌드: `python build_wu088_database.py --baseline-root /path/to/extracted/v2 --prior-return /path/to/prior/RETURN.json --parts-manifest /path/to/CONTENT_PARTS_MANIFEST.json --output /path/to/new/output --inspected-head 464197cc24936b256cc86ea468c19235c10a63e3 --created-utc 2026-10-01T02:08:50Z`

다운로드 없이 기존 보관본만 읽는다. 새 output 경로가 이미 있으면 중단한다. 별도 패키징 후 `verify_wu088_database.py`로 검사한다. 원격 게시/백업 receipt는 외부 RETURN.json에 있다.
