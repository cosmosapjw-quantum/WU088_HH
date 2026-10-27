# EXFOR Target 6 최초 독립 intake 검토 — 실패 기록 보존

2026-10-27. 검토자 `/root/provider_rows`, source 작성자 `/root/molecule_sources`.

첫 실행 `independent01`은 **FAIL, 8/9 검토군 통과**였다. 판정 원문은 [INTAKE_REVIEW.json](INTAKE_REVIEW.json), 실행·비용은 [RECEIPT](../raw/independent01/RECEIPT.json), 정확한 최초 checker는 [REQUEST](../raw/independent01/REQUEST.json)의 `python -c` command argv에 보존된다.

실패 분류는 **checker 기대값의 구현 오류**이다. G6가 main 4개와 auxiliary 1개 모두에 `PRIMARY_SOURCE_ROW`를 요구했으나, M0011003은 source packet에서 올바르게 `AUXILIARY_MULTIPOLE_SOURCE_ROW`로 분리되어 있다. Main 4개의 G6 조건 28개는 통과했고 auxiliary의 첫 분류 조건에서 실패했다. 원행·source packet을 고칠 문제는 발견되지 않았다.

첫 실행은 705개 assertion을 수행했다. 이 수는 원행 전사·locator·분류를 검사한 구현 조건의 수이며 물리 승인·독립 실험 수가 아니다. 다음 8개 군의 성공은 입력 identity가 유지되는 동안 재사용한다.

| 군 | 실제 범위 | 최초 결과 |
|---|---|---|
| G1 | 동결 packet/manifest와 원본 Git blob·SHA | pass_scoped |
| G2 | 주 TABLE 4개, 36행·124개 native 숫자 cell | pass_scoped |
| G3 | DATA/BIB/COMMON 및 parent의 정확한 locator | pass_scoped |
| G4 | SIG/DA, lab/CM, 단위와 에너지 bin | pass_scoped |
| G5 | ERR-S와 M0826의 beam systematic 상한 | pass_scoped |
| G6 | isotope·direction·state·Q·admission 분리 | **fail: auxiliary record-class 기대값** |
| G7 | 동일 D 정규화·같은 실험의 관측량 구분 | pass_scoped |
| G8 | E2 auxiliary 7행 별도 보존 및 CURVE 제외 | pass_scoped |
| G9 | 출처·재배포 및 제한된 승인 범위 | pass_scoped |

최소 교정은 main 4개 `PRIMARY_SOURCE_ROW`, auxiliary 1개 `AUXILIARY_MULTIPOLE_SOURCE_ROW`를 구분하고 뒤의 미완료 auxiliary 조건을 확인하는 것이다. 원래 36개 주 행이나 통과한 8개 군은 다시 실행하지 않는다. 후속 판정은 별도 [INTAKE_REVIEW_FINAL.json](INTAKE_REVIEW_FINAL.json)과 [INTAKE_REVIEW_FINAL.md](INTAKE_REVIEW_FINAL.md)에 기록하며 이 실패 JSON 및 raw는 바꾸지 않는다.

동결 provider SHA256: `d8b0b92f0374f73fa7f838db5ca07be45bd448696654b07c6db71c5847235ac2`.

최초 실패 review SHA256: `eb430e6ddbb0a6688b690b6d553f30a5b0d6e91a9a4e58873988b2fb39f4c654`.

Rate·Q·각도 적분·새 consumer 결속·기존 compiler 호출·과거 계산 재실행은 모두 0이다.
