# 게시 후 권위·복원 규칙

이 파일은 최종 commit에 들어간다. 자기 commit 또는 자기 ZIP hash를 파일 안에 미리 써서 고정하지 않는다. 실제 final HEAD/tree, 최종 ZIP 이름·bytes·SHA256·provider IDs·전체 복원 receipt, 외부 final-delivery JSON의 bytes/hash/IDs는 **PR142 최종 본문과 외부 delivery receipt**에서 확인한다.

## 권위 순서

1. PR142 actual head와 branch ref를 읽고, 마지막 게시의 expected_sha lease와 remote commit/tree가 일치하는지 확인한다.
2. PHYS85_FINAL_DELIVERY_20261024.json의 final_commit/tree, evidence identity, stage history, 원본 ZIP identity와 provider별 actual GET/restore receipt를 읽는다.
3. ZIP의 MANIFEST.json과 모든 payload를 검증한다. owned 두 연구 경로는 exact published Git blobs로 생성된다. 원시 private intake는 공개 Git source와 구분한다.
4. 각 provider에서 받은 실제 ZIP의 whole SHA256, CRC, payload hashes, Git object identities와 전체 추출 수를 읽는다. 다운로드 링크 발급이나 upload ACK만으로 복원 PASS를 쓰지 않는다.
5. 외부 final JSON도 양쪽 실제 raw bytes를 다운로드하여 SHA와 parsed identities를 대조한다. JSON 자신에 자기 SHA/자기 provider ID를 넣는 순환 구조는 만들지 않는다. 최종 transport readback receipt와 PR 본문이 그 terminal binding을 기록한다.

## 보존 범위

S0/S1/S1R/S2는 각 당시의 공개 Git 증거와 접근한 private intake, 원본 PHYS84 dependencies를 담는 cumulative checkpoint다. 이전 단계의 upload ACK와 최종 whole-archive restore는 다른 증거다. 최종 ZIP은 처음 생성한 원본과 각 provider actual download가 bytes로 같아야 한다. full extraction은 manifest를 포함한 모든 outer member에 대해 수행한다.

원본 PHYS84 ZIP/JSON의 전체 bytes/hash는 nested dependency로 검증한다. 이번에 과거 PHYS84 내부 추출·과학 실행을 새로 반복하지 않는다. 과거127/126/89/127 복원 및8/5 freeze checks는 과거 receipt 재사용으로 표시한다. 최종 outer restore가 모든 과거 연구의 새 과학 재검증이라는 주장은 하지 않는다.

## 최종 과학 상태

PHYS85 theory PASS_SCOPED, static implementation PASS_SCOPED, scientific reference NOT_VERIFIED. evidence identity d78adc5c293c28d2032a8a391ee317988390f504884847e79da4d1635ad024af는 audit identity이며 completed_science_identity=null이다. 두 Wolfram calls와 실패·생략 이력은 immutable evidence로 보존한다. transport/backup 성공이 science NOT_VERIFIED를 바꾸지 않는다.

PHYS84는 first numerical WAIT다. 새 reference/physical nuclear rate/stopping/ODE 또는 completed identity replay를 복원 과정에서 호출하지 않는다. HH_R10=OFF, production admission NOT_ISSUED를 유지한다.
