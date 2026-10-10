# HH-PHYS02 — 유한시간 photon–HH 혼합 나머지

**완료 판정: `PROMOTE_SCOPED`.** PHYS01의 음의 local cubic 결과를 동일 초기 전체 상태의 frozen continuous source에서 유한시간 부호와 모든 고차 나머지 상계로 확장했다. 독립 최종 심사에 blocking finding은 없다. 실제 macro와 physical/production gate는 계속 HOLD이다.

## 결과

`h=1.25e9 s`, `Sstar=binary64(5e-15) photons/(H s)`, `b=S/Sstar`, `tau=t/h`이다. 모든 `0<lambda,b<=1`, `0<t<=h`에서

    I_x/(lambda*b) in c3*tau^3 + [L4,U4]*tau^4 < 0,
    c3 ~= -2.0159064162896692e-17,
    [L4,U4] subset [5.1715113,5.4191015]e-20.

여기의 4차 도함수 상계는 4차 이후 전체 나머지를 포함한다. `t=h`에서 혼합응답은 `[-2.010735,-2.010487]e-17 * lambda*b`이며, 나머지는 cubic 크기의 `0.268818%` 미만이다. 영 매개변수/영 시간의 축에서는 정확히 0이다.

## 읽는 순서

1. [물리 보고서](WU088_HH_PHYS02_REPORT_KO.md): 물리 의미, 유도, 수치, 한계.
2. [과학 계약](SCIENTIFIC_CONTRACT.md), [입력 identity](INPUT_IDENTITY.json), [주장 원장](CLAIM_LEDGER.json).
3. [256 bit 정본 결과](results/REMAINDER_256_FINAL.json), [독립 최종 판정](independent/DECISION.json), [심사 설명](independent/REVIEW.md).
4. [독립 4차 유도](independent/HH_PHYS02_REMAINDER_DERIVATION_KO.md), [source audit](independent/SOURCE_AUDIT.md).
5. [재현 방법](REPRODUCE_KO.md), [검증 기록](FINAL_VERIFICATION.json), [실행 기록](RUN_LEDGER.json).
6. [PHYS03 인계](WU088_HH_PHYS02_NEXT_HANDOFF_KO.md), [다음 의무](NEXT_DAG.json).

이 패키지의 정본 입력 JSON과 원 Rust 5개 파일은 PHYS01에서 byte 그대로 가져왔다. 부모 과학 suite를 재실행하지 않았다. 새로운 계산은 52성분의 대수적 parametric tube와 시간도함수 상계, 새 미분 연산 검사뿐이다. Native, IVP trajectory, BE root, NCP, legacy integral은 실행하지 않았다.

최초 비방향 decimal 출력과 auditor comparator 실패도 보존했다. `REMAINDER_256_INITIAL.json`은 과거 표시 기록이며, 인증 endpoint는 `_FINAL`의 exact dyadic와 outward decimal이다.

## 봉인 및 게시

`MANIFEST.json`은 자기 자신을 제외한 모든 payload의 SHA-256과 크기를 기록한다. `verify_delivery.py`는 파일 identity만 확인하며 과학 시험을 반복하지 않는다. ZIP SHA, Git commit/tree와 Google Drive·Dropbox의 실제 ACK는 봉인 후 별도 `WU088_HH_PHYS02_PUBLICATION_RECEIPT.json`으로 제공한다. Receipt를 archive 안에 넣어 자기참조 hash를 만들지 않는다.

다음 작업은 **PHYS03의 실제 explicit-time source와 threshold/birth event 혼합 응답**이다. 현재 완료한 PHYS01/PHYS02 또는 ENERGY06E 계약을 반복하는 작업으로 돌아가지 않는다.
