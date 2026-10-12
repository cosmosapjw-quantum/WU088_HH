# WU088_HH 개발계획 독립 검토

**판정: ACCEPT_PLAN_WITH_PRESERVED_SCIENCE_BOUNDARIES.** 계획·진입 문서·작업 의존성·인터페이스 정의·NCP 분담을 검토했으며 blocking finding은 없다. 이 판정은 새 과학 PROMOTE나 PHYS11 재심이 아니다.

15개 동결 파일 167,597 bytes가 REVIEW_INPUTS.json과 일치했다. 최종 입력 manifest SHA256은 `f9438050b32eed9ce126f667729a673b02a3951782a1cd6ce3fe686479a44d04`다. 같은 검토 중 evidence locator를 bundle-root 기준으로 고친 두 파일을 확인했고, 나머지 13개 파일 및 네 역사적 진입 문서의 기존 본문은 그대로다.

## 채택 근거

- 독립 HH microscopic 연구를 유지하면서 LCS 유효 소스, FT03 native 인증, frozen107 충돌 연구와 외부 A/B/C를 분리했다.
- 첫 HERE 결과는 b_amp=1 고정의 lambda on/off ΔxHII·Δw다. 기존 mixed I와 의미를 구분하며, uniform U의 적용 전제 확인 이후에만 FTC를 사용하는 계획이다. 아직 실행하지 않았다.
- 수치오차·입력 포함 폭·closure 차이·천체물리 scenario와 절대/상대오차의 의미가 분리되어 있다. 작은 shear 신호나 scenario 폭을 HH 무시 상한으로 사용하지 않는다.
- xHII/xe, proper density, 시간·opacity 부호·c, angular-mean intensity와 표적당/체적당 heating을 구분했다. mean-volume redshift는 방향별 관측 redshift와 다르다.
- 원 native·시간·전역·full49·production의 열린 조건을 유지한다. 다른 저장소의 코드나 실행을 변경하지 않는다.
- NCP queue는 비어 있다. 독립 HH 자체의 과학 질문도 정당한 이관 근거로 허용하되, 실제 미완료 입력·비용·병렬 단위가 없는 작업을 만들지 않는다.

## 남은 범위

L0의 동일 계열·uniform U 전제 확인과 L1 이후의 수치 결과는 후속 연구다. 외부 수송 interface는 아직 미구현이며 실제 density/intensity/clock의 같은 gas-rest 또는 comoving frame 결속이 필요하다. Tilted 전자계로 현재 scalar opacity식을 자동 확장할 수는 없다. 이 사항은 후속 구현의 적용 범위이며 이번 계획 채택의 추가 실행 gate가 아니다.

최종 ZIP 구성과 실제 Git·양쪽 backup identity는 작성자가 게시 단계에서 확인해야 한다. 이 검토는 업로드나 원격 복원 완료를 인증하지 않는다.

검토자 `/root/audit_scope_review`는 후보 계획·코드·과학 파일을 작성하거나 수정하지 않았다. 새 과학 실행, native/source 호출, benchmark, NCP job과 원격 호출은 모두 0회다. 상세 입력 hash와 검토 항목은 PLAN_REVIEW.json에 있다.
