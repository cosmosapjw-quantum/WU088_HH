# NCP local readiness v2 — PREPARATION_BLOCKED

2026-10-03, WU088_HH의 AD3 이후 원 W3 실행 패키지를 실제 NCP에 복원했다. 신규 과학 dispatch는 0회이며 고정 6셀 scope는 소비하지 않았다. 입력 재업로드는 요구하지 않았다.

원격 연구 branch HEAD `d0b10d946ba8d769bb5e0d889541ad334643d1f3`, tree `e02129bd29135aee906e94131fe160c2ffa01674`, PR33 OPEN을 확인했다. 기존 `/root/WU088_HH` checkout과 다른 runtime은 보존하고 별도 publication clone과 hash-locked runtime snapshot을 사용했다. 게시 이후 HEAD/tree와 cloud ACK는 detached delivery receipt를 따른다.

Drive와 Dropbox에서 정확한 NCP bundle object ID, 이름, 66,780,472 bytes를 확인했다. rclone·provider CLI·sync/mount·기존 cache를 실제 조사했다. Drive file reference의 NCP GET은 HTTP403으로 실패했고, Dropbox에서 한 번 회수한 bytes의 SHA256 `37e7b8b1c0525aa377c82ed2d4d3f8fcad7fb8dab444fba994e186c2e981fdf6`이 일치했다. content-addressed cache를 canonical input으로 고정했다. Dropbox의 지정 input object에만 RESTORE_VERIFIED=true다. Drive는 metadata 확인이며 restore=false다.

통합 manifest 21항목, 내부 AD3 65개·W3 85개 payload, 복원한 W3 SOURCE_LOCK 1,834개 파일을 검증했다. AD3/W3 ZIP을 provider에서 따로 다시 받지 않았다. 기존 accepted raw20을 원 validator로 읽고 고정 6개의 offline plan/PREPARED를 생성했다. endpoint·producer·AD1~3 생성과 기존 scientific suite는 재실행하지 않았다. W3 source/coverage/queue의 bounded contract 검사 40개는 exit0, failures0이다. 이 검사는 새 과학 수렴이나 admission 증거가 아니다.

실제 환경은 CPU affinity64, 가시적 CPU quota 무제한, RAM total135,050,547,200 bytes, Python3.12.3/GCC13.3.0이다. 모든 가시적 cgroup의 memory.max가 max여서 원 finite>=6GiB gate는 BLOCKED다. 원 adapter의 root `/sys/fs/cgroup/cpu.max`도 없다. 목표 하드웨어 수치를 gate 통과 근거로 대체하지 않았다. EUID는0이며 system-wide 설치는 하지 않았다. 독립적인 nonroot UID 실행 identity는 검증하지 않았다.

원 host launcher를 동일 flags로 새 위치에 build했고 nofork/exec synthetic probe는 통과했다. 이는 B22 원인이나 모든 process lifecycle을 입증하지 않는다. 원 backend source GMP6.3.0/MPFR4.2.2/FLINT3.4.0을 검증하고 `--jobs 2`, 원 strict flags로 딱 한 번 빌드했다. GMP configure 후 `make -j2`가 makeinfo 미설치로 문서 생성 단계 exit2를 반환했다. 실패 로그와 111MiB 부분 workspace를 보존했고 자동 재빌드는 하지 않았다. pinned prefix와 성공 provenance가 없어 원 native preflight도 exit2다. primitive worker compile/link/ABI admission은 미완료다.

PREPARED self-hash: `0e06c0f959684e808f1ef1f6d8465e00079e0b6401eba311b804e458bac0f3a0`.
고정 scope self-hash: `91f8f304f2c0aa8668a1d8bc18b1972348768772fa308d8b3c9483cc8c254a5b`.
scope는 primitive0, `[275,67,288,272,16,0]`, 2workers,128bit,radius_exp=-57 및 원 예산 그대로다. backend/native build와 resource binding이 미완료이므로 전체 EXECUTION_BINDING hash는 없다. 새 runtime까지 덮는 실제 human science authorization도 찾지 못했다. 코드/JSON의 승인 문자열과 소비된 B128/B160 승인은 재사용하지 않았다. 원 runtime_adapter run/worker 및 primitive_worker를 호출하지 않았고 새 registry/RUN_STARTED/raw/RETURN은 absent다.

B22의105/57 claim bytes·SHA·PID 문자열과 원 HOST_EVENTS를 보존했다. ZIP 추출의 local mtime과 역사적 source-host mtime을 구분해 기록하고, 새 복원본 두 파일에만 원 source-host nanosecond mtime을 복원했다. 기존 runtime claim은 변경하지 않았다. 삭제·격리·rename·retry는 없으며 root cause는 OPEN_UNDETERMINED다.

accepted20/289, missing269의 기여는 미상계다. epsilon_C/R=null, scientific/production=false, R31AK frozen, z0.75 holdout, B128/B160 consumed, B192 reuse를 유지한다. 준비 실패를 science failure로 해석하지 않는다. 물리 rate·sigma/k·full49·trajectory를 승인하지 않는다.

다음 최소 조치는 원 adapter가 현재 한도를 읽을 수 있는 finite delegated cgroup/namespace 준비와 원 builder clean PATH의 makeinfo 제공이다. 이 실패 workspace를 보존하고 새 non-science build continuation을 검토해야 한다. backend/primitive ABI 및 host gate가 닫힌 뒤 source/input/plan/build/runtime 전체 binding과 미소비 registry를 확인하고 exact science authorization을 연결한다. 지금 6셀 실행 승인을 요청하거나 자동 retry하지 않는다.

결과 ZIP에는 COMMANDS, CLOUD_INTAKE, RECOVERY_INVENTORY, AUTHORITY_CHECK, FILE_MANIFEST, 실제 host build·probe·backend 실패 로그와 부분 산출물, PREPARED 및 plans를 넣는다. 원 native return schema는 별도로 보존하고 coordinator summary는 NCP_HANDOFF_RETURN에 둔다. 같은 research branch의 새 continuation path만 additive non-force 게시하며 결과 ZIP·보고서·detached receipt는 기존 Drive/Dropbox 목적지에 create-only 백업한다. 실제 output restore가 없으면 output RESTORE_VERIFIED=false다. DB는 변경하지 않아 새 DB artifact가 없다.
