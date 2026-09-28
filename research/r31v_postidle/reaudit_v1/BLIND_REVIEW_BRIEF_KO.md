# WU088_HH R31V 제한된 blind reviewer 입력

너는 구현자·실행자와 분리된 새 reviewer다. 너에게 이전 대화, 구현자의 보고서, 성능 승자 추천, 테스트 통과 수가 노출되었다면 그 노출을 먼저 기록하고 blind라고 주장하지 마라.

대상은 orchestrator가 명시한 exact commit/tree의 bounded B192/G80/z=2 benchmark control code와 그 evidence contract다. source와 raw가 의미하는 범위만 검토한다. native kernel을 실행하거나 수정하지 않는다. 세션을 만들었다는 이유만으로 적격 reviewer admission이 성립한 것으로 보지 말고 실제 harness/session identity를 기록한다.

먼저 볼 자료: repository AGENTS.md; research/r31v_postidle/m3_postidle.py, controls.py; research/r31s_ncp/m3_throughput.py, m3_full_pair_screen.py, authority_m3/m3_h0_authority.py, authority_seed/grid_seed.py; src/wu088_hh/native_candidate.py. 원 실행 자료는 research/r31v_postidle/evidence/ncp_host/20260928T132239Z_r31v 아래 m3b_132.json, reference_prepare.json, GRANT.json, HOST_INVENTORY.json, SOURCE_BUILD_AUDIT.json 및 reference_cache다. 기존 pilot/equality는 research/r31s_ncp/evidence/ncp_host/20260928T092409Z_18dd6940 아래에 있다.

동일 12 pairs x 11 repeats, configuration당 3회, explicit prepare와 cache-only benchmark 분리, source/build/geometry/ABI identity, current grant 및 관측 자료, failure 보존이 계약이다. byte identity, numerical equality, performance comparison, scientific admission을 구분한다. 자원 관측의 의미와 단위, provenance의 충분성, 입력과 오류 처리 경계를 스스로 검토하라. 잘못된 입력을 만드는 경량 synthetic test는 허용하되 실제 reference를 synthetic 배열로 교체하지 않는다.

첫 review를 동결하기 전에는 기존 INDEPENDENT_DECISION_REVIEW*, POSTREVIEW_NCP_HANDOFF_KO.md, CODEX_NEXT_PROMPT_KO.md, 이번 REPORT_KO.md/RESULT.json/RED·GREEN logs, 새 test_adversarial_reaudit.py, PR discussion을 읽지 마라. 독립적인 반례를 먼저 작성하라. 위 자료의 내용이 도구 output에 섞여 들어오면 exposure를 기록한다.

산출: reviewed commit/tree와 읽은 파일의 identity, exposure/admission 상태, 실제 실행한 경량 검사, 위치·반례·영향·수정이 필요한 이유가 있는 findings, 미검증 범위. 증거 없이 finding 수를 늘리지 않는다. critical issue가 없다는 것과 production 승인도 같지 않다. BLIND_REVIEW.json/md를 먼저 저장하고 SHA-256으로 동결한 뒤 orchestrator에게 반환한다. 그 다음에만 구현자 보고서와 비교한다.
