# WU088_HH R20: 실제 REC/CR 소비자 결속 조사 및 단위·시계 preflight

- **과학 단위:** `WU_HD_105K_OWNER_CONSUMER_BINDING`, 2026-10-29.
- **변경 금지된 R19 기준:** HEAD `218f353e67ac533b9fb6d54156ec3db6e8827db6`, canonical **34/49**, scoped R19 **18/20**, 비저자 R6/C9 미실행, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`.

## 이론 결과

`THEORY_KO.md`에 source-state 종별·단위·시간 pullback의 정확한 식, conserved H/D/charge covector, chemical rank-one Jacobian, 양의 clock 및 volume domain의 의무를 유도했다. `CONSUMER_CONTRACT.json`은 소유자 ACK가 필요한 typed gate이다. `cm^-3` 저장을 위한 `k_cm3/s = 10^6 k_m3/s = 1.15e-10 cm^3/s`를 명시하였다. Source 온도 105 K 이외에는 반응률을 허가하지 않는다.

## 실제 REC/CR 조사

**REC:** `cosmosapjw-quantum/rec_bianchi` PR156 (`8806a4f757d916b6cf040625be931a66e2f0f6fe`), `research/rec_hd_multichannel_affinity_20261029/code/multichannel.py::generate` (Git blob `029255494bf0a63b93bf8b2715327a8585afb5f3`)는 HD 회전준위 방사·충돌 진단이며 T=50/100/200 K, 9 levels/8 radiative/18 collider edges. H+ + HD02 -> D+ + H2_01의 **4상태 반응 RHS가 아니다**. REC PR156 `CALLSITE_MATRIX.json`도 9개 선택 경로에 대한 감사이지 전 저장소 no-go가 아니다.

**CR:** `cosmosapjw-quantum/bass_cr` PR121 (`6c3c91f9fd6261b6d79383ef7c5c8de7b6004fb6`), `research/cr_generic_budget_ssp_20261029/generic_budget_flow.py::ExactBudgetFlow` (Git blob `fdde86ca6d57dcd5fcdbd8356825153a5fb65db6`)는 정확한 유한 He high-low 예산 flow다. ODE 반응 채널 입력과 밀도 시간 진화가 없다. **따라서 해당 함수에는 결속 불가**.

두 경로 모두 정적 Git blob을 읽어 역할을 확인했지만, 전체 native C/Rust/생성 코드/branch 호출 그래프를 배제하는 전수조사 증거는 아니다. 정당한 owner ACK도 확인되지 않았다.

## 실행된 코드·검증

새 `binding_preflight.py`는 기존 외부 소유자 모듈을 import/수정하지 않는 **WU 측 합성 RHS oracle**이다. 데이터 기반 `assessed_callsite`는 위 두 실제 확인 후보를 이유별로 거부한다. 출처 숫자를 원본으로 다시 읽는 모듈이 아니라 R19의 SHA 및 명목 분수를 고정한 별도 read-only preflight이다. 실제 원본 PDF 재검증, REC/CR production 결속, native IVP, 물리 uncertainty 계산은 이번 코드에서 수행하지 않았다.

- `python -m unittest -v test_binding_preflight`: **14/14 PASS**, exit 0. 첫 13개 통과 이후 서명된 theta의 비유한/문자열 입력 처리 결함을 발견해 `ContractError`로 정정하고 14번째 음성 테스트를 추가했다.
- `python metamorphic_check.py`: 결정론적 **240 상태·clock·permutation 케이스**, 960 단위·순열 비교와 720 보존량 검사 PASS, m^-3 RHS 절대 차이 0 (Decimal 계산 규약 내).
- Wolfram signed theta, permutation·unit conjugation 하에서 characteristic polynomial `(λ+gθ)^3(λ+g[θ+k(n_H+n_HD)])` 직접 평가 PASS. 최초 Wolfram 명령의 protected `D` symbol 사용 실패를 교정한 재실행 결과를 사용한다.
- 모든 자체 검증은 동일 작업 주체/다른 알고리즘 수준이다. **진짜 비저자 R6/C9는 NOT_RUN**.

## Claim gate 및 남은 의무

`PASS_DERIVED_UNIT_CLOCK_CONTRACT`, `PASS_SYNTHETIC_PREFLIGHT`, `HOLD_OWNER_CONSUMER_BINDING`. 실제 owner consumer `repo/path/function/commit`는 **미결속**. positive clock과 105 K thermal history, 실제 density/state semantics, 함수 호출 그래프, owner ACK를 갖춘 새로운 후보에 대해서만 과학적으로 다음 단계 가능. State Q, reverse rates, bath, full-A, source uncertainty는 별도 미완료. 다른 저장소·기존 canonical 49개 노드에는 변경 없음.

`DAG_DELTA.json`과 `HANDOFF_NEXT_THREAD_KO.md`가 재개 계약이다. 신규 R20의 Git 게시 영수증 및 원본 provider ACK는 **발생한 실제 응답만 기록**한다. 과거 R19의 Drive ZIP ACK와 Dropbox Paper 텍스트 영수증을 R20의 백업으로 재사용하지 않는다.
