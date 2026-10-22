# PHYS81 — 유한 원자 source와 핵 방사 포획 에너지 계약

PHYS80 실제 최종 HEAD `951182dd59bbb59dba454bbaab78ad56d029355a`의 additive Draft PR137 연구 단원이다. 현재 S1에서 최신 접근 가능 refs/전달 기록 종합, source/energy 유도, 구현 및 독립 검증을 보존했다. 실제 상태는 `STAGE_STATUS.json`, `EXECUTION_LEDGER.json`, `DAG_OVERLAY.json`을 따른다.

- C22D H finite Maxwell 코드와 PHYS80 Bell kernel을 byte identity로 재사용한다.
- He4 24.6–60 eV, Li7 6–15 eV author-data를 ground-product finite operator로 연결한다. Li7 chemical energy는 Bushaw2007 7Li 원전으로 교정했다.
- 고정 밀도 CI-only common-T parcel은 정확한 연속 좌표변환으로 7→3 상태, analytic Jacobian rank≤2다. 새3 IVP만 실행해 원래7상태와 비교할 준비를 마쳤다.
- 세 bare radiative capture의 photon/recoil 및 explicit ζ 에너지 회계는 독립 수치 검증을 통과했다. Nuclear rates와 thermal-population/stopping은 OPEN이다.

`RESEARCH_LOOP_MAP_KO.md`가 R1–R10/C1–C10과 실제 산출물의 연결을 설명한다. 기존 연구 identity 재실행0, NCP0, benchmark0. 단계 백업 ACK와 최종 full-byte restore를 구별한다. HH_R10=OFF; Production admission NOT_ISSUED.
