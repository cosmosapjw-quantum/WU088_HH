# R3 source-reference overlay 독립 구현 검토

**판정: `PASS_SCOPED_STATIC_SOURCE_REFERENCE_OVERLAY_IMPLEMENTATION`. 차단 결함은 없습니다.** 공급자 원자료의 셀·EXFOR 의미 승인은 별도 `INTAKE_REVIEW`의 범위이며, 이번 검토는 builder와 실제 build01 산출물의 연결·보존을 확인합니다.

실제 target 행 차이는 `TARGET19:06:target_forward`의 다섯 key뿐입니다: `experimental_table_provider_refs`, `has_primary_source_record_reference`, `primary_provider_refs`, `source_reaction_identity_matches_target`, `supplier_status`. 나머지19 target/28 direction의 기존 내용과 target6의 물리 필드는 같습니다. 최상위에는 unit_id와 R2 출처/R3 변경 범위 메타데이터만 바뀝니다. 역반응이나 조건부 inverse rule을 새로 만들지 않습니다.

`reused_target6_event.json`의 saved_row는 R2의 `TARGET19_PHOTONUCLEAR:06` 행 전체와 동일합니다. 기존 USER_TARGET19 정체성, compiler SHA, 두 D의 정수 계수, 에너지 미승인과 inactive 상태를 그대로 참조합니다. EXFOR 수치를 이 열의 물리 rate/Q로 결속하지 않았으며 새 compiler import·호출도 없습니다.

| 공급자 | 원행 수 | 보존한 관측량·단위 |
|---|---:|---|
| M0011002 |14|SIG, MICRO-B, 명시 EN|
| M0475002 |12|CM 각미분 DA, NB/SR, ANG-CM/ADEG|
| M0475003 |6|SIG, NB, 명시 EN|
| M0826002 |4|SIG, MICRO-B, 입사 EN-MIN/EN-MAX bin|

24 SIG 행과12 DA 행은 별도 대안으로 남습니다. 입사 energy bin은 sigma dE 적분이 아니며, bin 응답 가중치·event normalization을 발명하지 않습니다. Auxiliary7행과 CURVE 자료는 main36행에 포함하지 않습니다. Catalog는 source packet의 완전한 상태·단위·불확실성·locator를 정확한 SHA와 유일한 ID selector로 참조하므로 자체적으로 이를 단일 rate나 공분산으로 축약하지 않습니다.

11개 pinned input 참조는 실제 파일 SHA와 일치하고, 4개 provider selector는 각각 유일한 frozen packet 행으로 해석됩니다. 6개 실제 JSON 출력의 SHA는 첫 build01 stdout과 일치합니다. build01은 exit0, CPU0.065589초, wall0.07114883000031114초의 기존 결과로 재사용했습니다. 출력은 exclusive-create 방식이며 기존 파일을 덮어쓰지 않습니다.

`28/28`은 원래19개 target의 명시28개 방향에 source reference가 존재한다는 뜻입니다. 기존 physical binding gap에는 target6이 계속 남고 rate/Q/state-domain/consumer/activation 승인은 false입니다. 전체 미래 isotope/state/molecular 과정의 완료나 L4를 선언하지 않습니다.

현재 HEAD87933da와 pre-build 원격·AGENTS·병렬 작업·백업 관측은 계약과 일치합니다. 게시 expected parent도87933da이며 source snapshot과 후속 metadata delivery를 분리합니다. 이 단계는 실제 게시 완료를 주장하지 않습니다. 기존 tracked R1/R2/AGENTS/고정 handoff/compiler 변경은 없습니다.

검토 방식은 코드 정적 읽기, JSON 차이·저장된 행의 동일성·SHA 참조 확인입니다. Builder·compiler·과학 계산·이전 검사를 실행하거나 새 다운로드를 하지 않았습니다. `independent01`은 공급자 원행 검토에 예약된 상태이며, 이번 검토는 두 review 문서만 썼습니다. 정확한 검토 파일 SHA 목록은 동명 JSON에 있습니다.
