# WU088_HH PHYS07

PHYS06 NCP 반환 이후 실제 소스의 C² 영역, whole-box source/derivative enclosure와 참조 first-stage family의 유한 혼합응답을 계산한 연구 package다.

읽는 순서:

1. `REPORT_KO.md`: 물리적 의미, 수치 결과, 적용 범위.
2. `review/DECISION.json`, `review/REVIEW_KO.md`: 독립 최종 판정.
3. `theory/SOURCE_C2_DOMAIN_KO.md`, `theory/REFERENCE_ROOT_THEOREM_KO.md`: 소스와 uniform/finite 증명.
4. `results/SOURCE_ANALYSIS.json`: 정확한 유리수 endpoint와 stage별 계산 결과.
5. `handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md`: 다음 NCP의 실행 계약.

## 전달과 복구

별도 `WU088_HH_PHYS07_DELIVERY_RECEIPT_20261011_v1.json`이 core commit/tree, archive SHA256 및 실제 Drive/Dropbox object ID를 결박한다. `WU088_HH_PHYS07_NCP_START_KO.md`에서 attachment 없이 시작한다. Archive 안의 root는 `HH_PHYS07_20261011_v1/`이고, Git의 package prefix는 `research/r31ao_unequal_ladder/hh_phys07_source_domain_20261011_v1/`다. 두 경로의 payload bytes는 동일하다.

원 seed, 선택한 NCP source snapshot, 실행 입력·출력·첫 로그, pure-Python 구현, 두 Astra v4 harness archive와 전체 handoff가 포함돼 있다. Python 구현은 표준 라이브러리만 사용한다. 과거 science suite나 성공한 이번 diagnostic의 재실행은 기본 다음 작업이 아니다. 우선 봉인된 결과를 읽고 handoff가 지정한 새 source producer 작업을 진행한다.

`results/full`과 `results/first_half`는 동일 COMMON 입력에서 출발한 각각의 first stage다. 참조 uniform root와 mixed/finite 포함은 해당 실수 residual에 대한 수학적 결과다. Native direction/libm/PreBE/input tuple 일치, 실제 native root/W/I, carried second-half 및 실제 full/two-half defect는 아직 미해결이다.

## 보존 원칙

`CANDIDATE_SHA256.json`은 독립 reviewer가 받은 후보 bytes를 고정한다. `MANIFEST.json`은 최종 package payload를, `SHA256SUMS`는 manifest까지 포함해 검증한다. 첫 실행 로그와 발견된 finite birth leaf 표기의 원문·수정 기록을 보존했다. 백업 업로드 ACK와 파일 metadata 검증은 실제 remote restore 실행과 구분해 receipt에 기록한다.
