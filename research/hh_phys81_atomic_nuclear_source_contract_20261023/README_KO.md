# PHYS81 — 원자 source 구간과 방사 포획 에너지 계약

PHYS80 실제 최종 HEAD `951182dd59bbb59dba454bbaab78ad56d029355a`의 additive 연구 단원이다. 현재 S0는 최신 접근 가능 refs/전달 기록 대조와 후속 연구 계약을 보존한다. 현재 과학 상태는 `STAGE_STATUS.json`과 `EXECUTION_LEDGER.json`이 소유한다.

## 선택한 연속 작업

1. Bell1983 실제 표를 읽어 H 계수 전사 충돌을 닫고, H/He/Li 분석함수의 전 에너지 양성을 정확 대수로 검토한다.
2. 최신 C22D H1 finite Maxwell 코드를 재사용한다. He4의 24.6–60eV, Li7의 6–15eV author-data window를 별도 ground-product 계약으로 연결한다. 결측 저온 문턱 구간과 high-energy tail은 full physical rate와 구별한다.
3. 동일 common-temperature CI parcel을 cumulative neutral hazard로 환원하고 에너지 첫 적분과 analytic Jacobian을 먼저 유도한다. 새 source를 사용하는 실제 계산만 수행한다.
4. 이미 완료된 REI beta/RR ledger를 재사용하고, 세 radiative capture의 광자/핵 recoil 분할 및 nuclei-number 온도항을 새로 닫는다. Nuclear rate activation과 stopping/escape의 물리 입력은 별도 의무다.

각 단계 후 게시와 이중 백업을 기록하고 다음 승인 단위로 계속한다. 전체 collisional/thermal/network completion은 이 단원의 완료와 다르다. HH_R10=OFF, Production admission NOT_ISSUED.
