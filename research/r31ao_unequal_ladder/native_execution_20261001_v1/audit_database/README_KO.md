# Native 실행 후속 감사 DB

이 DB는 c3f0cf25efdd50deca51355a237b863e5fcd631d의 이전 감사 SQL을 해시로 연결하는 새 증거 index다. 기존 DB나 원 문헌 DB를 수정·대체하지 않는다. provider 재조회와 수치 계산은 없다.

```bash
python audit_database/build_continuation_db.py --output-root /absolute/new/continuation_db
```

`--continuation-root`와 `--prior-root`를 지정해 다른 checkout에서도 만들 수 있다. 출력은 두 source tree 밖의 미존재 디렉터리여야 한다. 최종 runtime receipt가 모두 기록된 뒤 새 경로로 다시 빌드한다. 실행 중 source bytes나 파일 목록이 바뀌면 중단한다.

`meta`, `artifacts`, `source_links`, `stage_delta`, `run_records`를 제공한다. 모든 source path는 namespace와 상대 경로로 저장하고 실제 SHA256을 결박한다. JSON에 명시된 status/exit를 보존하며 파일명이나 exit0으로 native/수학/production 승인을 추정하지 않는다. JSON에 status가 없는 계획은 실행 완료 기록이 되지 않는다.

G2 delta는 독립 review와 exact decode 결과의 해시 연결을 확인한 뒤 **두 B192 archive·12개 real/complex NPY**에 한정한다. 전체 historical ABI나 모든 G2 작업 완료를 주장하지 않는다. 다른 단계의 행은 개별 구현/실행 기록의 관측이며 최종 연구 판정을 대신하지 않는다.

SQLite, SQL dump, SQL 복원본, source map 및 검증 JSON을 쓴다. integrity/FK, 복원 행 수와 schema+정렬된 row의 논리 SHA256을 검사한다. 같은 input snapshot은 같은 논리 내용을 만들며 SQLite의 물리 page hash와 구분한다.
