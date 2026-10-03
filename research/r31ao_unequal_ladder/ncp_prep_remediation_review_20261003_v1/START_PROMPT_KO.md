# NCP 준비 복구 R1: 과학 dispatch 0

NEXT_ACTION=NCP_PREP_R1_MAKEINFO_AND_REAL_CGROUP_BINDING
REFERENCE_RETURN_COMMIT=9edc13a8bc92f97aaf21977fc006aa624825acda

이 문서는 readiness 반환 검토와 다음 비과학 준비 인계다. NCP를 여기서 수정하거나 build/HH 적분을 실행하지 않았다. 기존 40개 검사는 반환된 역사 evidence이며 새 검사 수가 아니다. PREPARATION_BLOCKED를 유지하고, 준비가 닫히면 READY_FOR_EXACT_SCIENCE_AUTHORIZATION으로 반환한다. 이 문서는 새 과학 승인이나 시스템 전역 관리자 권한을 부여하지 않는다.

## 사용자가 파일을 다시 올리지 않는 회수

기존 /root/WU088_NCP_EXEC_20261003_v2 와 verified cache를 먼저 읽는다. 원 failed backend, PREPARED, registry, B22 claim과 원 SOURCE_LOCK을 보존한다. 최신 remote successor를 먼저 읽고 과거 SHA로 reset하지 않는다.

상세 prompt를 기존 인증된 Drive/Dropbox 중 한 곳에서만 회수하고 bytes/SHA를 확인해 실행한다.
- file: WU088_HH_NCP_PREP_REMEDIATION_PROMPT_KO_20261003.md
- bytes: 13046
- SHA256: 9557eb6de5235da550c8c5f0c24643d31f43e09904339270fb66c3946b2db49d
- Drive ID: 12PbP5dj1JAQMmJWmD4T6zWsmHLv2m9no
- Dropbox ID: id:BSpOijBcT10AAAAAADxwwg

검토 package에는 원 소스와 선택된 실패 evidence 및 상세 prompt가 있다. 전체 runtime 대체 ZIP은 아니다.
- file: WU088_HH_NCP_READINESS_REVIEW_20261003_v1.zip
- bytes: 84605
- SHA256: 6747db400b4ba2fdeb635689869f6b312d9332f806db7c1fe3b63797534e65ba
- Drive ID: 1PUoZrHDWnvKH2Bh8wbJFtsQsIeQcfhZb
- Dropbox ID: id:BSpOijBcT10AAAAAADxwwQ
- manifest payloads: 21

## 원인과 실행 경계

1. GMP의 실제 실패는 gmp.info 생성 중 makeinfo 부재다. 원 builder는 tools allowlist로 clean PATH를 다시 만들므로 shell PATH만 추가해도 해결되지 않는다. 진짜 GNU Texinfo를 실제 clean 환경에서 --version과 작은 .texi 생성으로 검증하라. 원 source/flags는 유지한다. MAKEINFO=true, 가짜 실행기, touch/mtime/문서 target 제거로 우회하지 않는다. workspace-local tooling wrapper가 필요하면 새 비수치 orchestration identity와 검사를 남긴다.
2. 원 resources()는 /sys/fs/cgroup/cpu.max와 memory.max만 읽는다. finite leaf를 만드는 것과 원 경로가 실제 그 leaf를 보는 것은 다르다. 실제 위임과 finite cap, membership, cgroup2 mount/namespace, ancestor limit, UID/capabilities를 함께 확인한다. 원 observer가 실제 job view를 보게 하거나 별도의 source-bound observer successor를 검증한다. fake file/숫자 주입, gate 완화, host 전역 mount 변경은 금지다. memory.max=max는 RAM 부족 판정이 아니다.
3. 의존성과 resource 준비 후에만 원 실패 tree를 그대로 두고 새 prefix에 --jobs 2와 원 flags/pins/caps로 비과학 backend build를 사전 고정된 한 번의 continuation으로 수행한다. 실패하면 중단하고 로그를 보존한다. 실제 HH로 smoke하지 않는다.
4. 원 run()은 binding 생성 뒤 registry를 소비한다. 승인용 hash를 얻으려 run을 호출하지 않는다. 필요하면 pre-consumption 구성만 사용하는 비dispatch BINDING_PROPOSAL helper를 별도 구현한다. not_authorization=true, scope_consumed=false를 유지한다.

성공 종료는 실제 backend/worker ABI/containment와 source/input/plan/runtime binding proposal을 갖춘 READY_FOR_EXACT_SCIENCE_AUTHORIZATION이다. 아니면 구체적인 PREPARATION_BLOCKED와 필요한 최소 관리자 조치를 반환한다. 시스템 설치/계정/전역 mount 권한을 백업 승인에서 추론하지 않는다.

이번 continuation은 science_dispatch_count=0, accepted20/289, missing269unbounded, epsilon_C/R=null, B22OPEN, scientific/production=false를 보존한다. 기존 6셀을 실행하지 않는다. Bianchi/rei_bianchi/다른 원자 repo를 수정하지 않는다.

동일 research branch에 새 경로만 non-force 게시한다. 새 결과는 기존 Drive parent1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM 및 Dropbox /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/ 에 create-only 이중 백업한다. 입력은 정상 cache를 재사용하고 사용자 수동 재업로드를 요구하지 않는다. ACK+metadata와 content restore는 구분한다.
