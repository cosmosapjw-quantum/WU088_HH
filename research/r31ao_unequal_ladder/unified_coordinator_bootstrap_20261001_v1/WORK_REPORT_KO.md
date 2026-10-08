# 후속 실행·검증 coordinator 인계

선택한 `EXACT_CONTINUOUS_TARGET_ENCLOSURE_PLUS_ARCHIVED_RAW_COMPARISON` 경로의 식별된 추상 이론 의무는 명시된 전제 아래 종결되었다. 이 범위에서 역할 전환을 수용한다. 이제 이 coordinator 상태가 후속 흐름의 정본이고, 이전 연구 상태는 변경하지 않는 근거다. 실제 HH 수치 인증과 과학적 admission은 아직 완료되지 않았다.

현재 원격은 `b66732540d8c428830c957003ea87d705355f49f`, tree `92561187ddbc6f03665253807b235279b052a081`, PR #33은 open/draft이다. 연구 종결 `65a82bf149ae2de02e929cb7776a67022ef163c0`의 직접 후속 commit이며 NCP 가속 구현만 추가한다. 원격 원본과 복구 파일의 Git blob을 대조했고 정확한 개수·해시는 `INPUT_SOURCE_IDENTITIES.json`에 있다. 과거 HEAD로 reset하거나 닫힌 T1–T5 연구를 재실행하지 않았다.

단일 다음 작업은 **NCP_HOST_NATIVE_SYNTHETIC_ACCEPTANCE_AND_RETURN**이다. 현재 세션에는 NCP 접속 정보와 실행 세션이 없고 GNU Fortran/OpenMPI 도구도 없다. 따라서 상태는 **BLOCKED_BY_RUNTIME**이다. 기존 구현 요청에 포함된 합성 host 검증을 실행할 차례이며 새 과학 계산 승인을 먼저 요청하는 단계는 아니다.

| 층 | 현재 상태 | 남은 항목 |
|---|---|---|
| 수학 | T1–T5 조건부 유도 및 범위 한정 독립 검토 종결 | 실제 입력·ABI·machine operand 전제 충족 |
| 구현 | 기존 합성/local 59개 검사 기록 계승 | native callback/assembly/Petras/cache와 Fortran/MPI 실제 acceptance |
| 실행 | 실제 HH 0회, target NCP 측정 없음 | 동일 정확도 host 합성 결과와 성능 측정 |
| 과학 claim | 기존 finite-order verdict 보존, rigorous=false, ε/η=null | actual certificate, 독립 scientific review 및 물리·프로젝트 gate |

가속 builder는 라이브러리만 빌드하고 기존 callback+assembly 및 Petras 합성 acceptance를 호출하지 않는다. cache fixture도 이를 대체하지 않는다. 이번 인계서는 **빠른 backend build 한 번 → 기존 callback/assembly → Petras → cache 정확 일치 → MPI 1/2/4 smoke → 고정 정확도 rank calibration**을 하나로 연결했다. 옛 느린 backend 전체 빌드를 다시 수행하지 않는다. 구현 소스 변경은 없다.

B128/B160 one-shot은 `CONSUMED_FOUR_STAGES_COMPLETE`로 보존한다. 과거 장부의 중간 criteria 상태보다 최종 status·네 stage exit 0·완료 timestamp와 successor RETURN을 따른다. B192는 기존 결과 재사용만 유지한다. actual HH/G7·raw scientific decode는 미승인·미준비다. historical ABI는 새 host probe로 소급 인증하지 않는다.

NCP의 64코어가 물리코어인지 SMT 포함 vCPU인지 측정한 후 rank 수를 선택한다. 충분한 자원이 있을 때 총 64 ranks는 worker 63개와 coordinator 1개다. 정밀도·복소 box·합산 순서·허용오차를 유지하고 floating MPI reduction이나 fast-math를 추가하지 않는다. 이전 local 2.74배 결과는 정수 fixture의 local 측정이며 NCP/Arb 성능이 아니다.

기존 checkpoint가 COMPLETE 반환 뒤 RUNNING으로 관측된 현상의 근본 원인은 여전히 미확정이다. 실패 거절 및 readback 보완과 원인 해결을 구분한다. 모든 실패 attempt는 보존하고 자동 재실행하지 않는다.

문헌 DB v3와 gap-closure SSOT를 계승했다. 원 Deep Research DB의 bytes 복원이나 미확보 라이선스 자료 입수를 주장하지 않는다. 기존 Drive/Dropbox receipt는 선택한 ACK·ID·경로·크기 검증 수준으로 유지한다. 이번에 복원·해시 확인한 것은 이전 NCP package의 특정 Library 객체이고, 새 Drive/Dropbox restore 성공으로 승격하지 않는다.

실행 상세는 `NCP_CODEX_HANDOFF_KO.md`, machine 계약은 `HOST_EXECUTION_CONTRACT.json`, 후속 RETURN 틀은 `HOST_RETURN_TEMPLATE.json`이다. 게시 후 실제 commit/tree와 이중백업 식별자는 별도 `DELIVERY_RETURN.json`에서 확인한다.
