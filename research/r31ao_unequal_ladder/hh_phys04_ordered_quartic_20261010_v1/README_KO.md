# WU088_HH PHYS04

Source-ordered mixed quartic, fixed-grid remap opacity와 reduced-BE 혼합 감도,
NCP local Codex 이식 계약을 담은 2026-10-10 연구 패킷이다.

## 읽는 순서

1. FINAL_STATUS_KO.md와 review/DECISION.json: 독립 최종 판정과 claim ceiling.
2. FINAL_REPORT_KO.md: 물리 결과와 해석, 실제 구현 범위 및 다음 연구.
3. NCP_LOCAL_CODEX_HANDOFF_KO.md: NCP local Codex에 전달할 전체 실행 지시.
4. NCP_TASKS.json 및 NCP_RETURN_TEMPLATE.json: 작업 의존성과 실제 반환 계약.
5. REMAP_OPACITY_THEORY_KO.md, quartic/PHYS04_ORDERED_QUARTIC_KO.md,
   IMPLICIT_MIXED_THEORY_KO.md: 유도와 코드의 세부 전제.
6. RUN_LEDGER.json, FINAL_VERIFICATION.json과 원 results/logs:
   새 검산, preserved first failure/correction, provenance.

REPORT_KO.md는 독립 리뷰가 읽은 고정 후보를 그대로 보존한다.
FINAL_REPORT_KO.md는 그 본문에 최종 판정의 상태 설명을 반영한 전달본이다.
review/에 있는 evidence audit는 과학 suite 재실행과 구분한다.

## 실행 의미

선택 spectrum의 pure-remap 결함, P₀=0 local quartic 특수화와
manufactured implicit sensitivity는 서로 다른 계산이다.
Actual finite common-state gas response나 native trajectory 인증으로
사용하지 않는다. 현재 native science budget는 0이다.
Physical/production HOLD와 과거 consumed run scope를 보존한다.

## 재현

봉인된 payload 확인은 아래 명령으로 한다.

~~~bash
python3 -B reproduce.py --verify-only
~~~

완료된 과학 suite를 intake만을 이유로 다시 실행하지 않는다.
선택적 새 PHYS04 재현의 명시적 방법은 REPRODUCE_KO.md에 있다.

## 게시 identity

원 owner pin은 569b04cd71e45756e0fd476aef6643bd9434f4fa,
연구 parent는 93e04c51c682216d9cb662b77a52a5783b15c71f다.
새 publication commit/tree와 봉인 ZIP hash는 자기참조를 피하기 위해
외부 WU088_HH_PHYS04_DELIVERY_RECEIPT.json에서 확인한다.
Google Drive/Dropbox ACK는 실제 restore 검증과 구분한다.
