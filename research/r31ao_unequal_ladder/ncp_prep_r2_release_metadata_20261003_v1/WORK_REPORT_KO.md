# WU088_HH NCP prep R2 실제 반환

종료 상태: **READY_FOR_EXACT_SCIENCE_AUTHORIZATION**. science_dispatch_count=0, scope_consumed=false, accepted20/289를 유지한다.

최신 remote successor bab33a3d95c7298411ee82cb7f46b49588edb5da의 시작 문서와 상세 cloud prompt/candidate package를 실제 읽었다. 양 provider metadata를 대조한 뒤 각 입력 bytes는 Dropbox에서만 1회 회수하고 상세 prompt 10,949 bytes/SHA e3a9fc6652e9f3cf97d7521e61ad3dabffe6e5ed8ea234dad5c723a17f75984e, 후보ZIP 1,945,164 bytes/SHA e44eff52486e04ae147933462e52b1c6479e8137aa85b376deb4a88653941396을 검증했다. 원 verified input/cache/R1 workspace를 재사용했다.

후보 payload manifest와 source lock을 확인하고 release_extract의 host compatibility 검사 12개 PASS, failures0/skip0을 기록했다. 과거 40개 및 R1의 3개 검사는 반복하거나 이번 검사 수에 더하지 않았다. 원 archive 세 개의 SHA/size/type/mode/mtime와 새 extraction의 전체 member 내용을 대조했다. bytes와 원 기록된 정수초 mtime은 정확히 일치한다. mode는 원 pinned extractor가 사용한 실행성 기준 0644/0755 정규화를 그대로 유지하며, FLINT tar의 0664/0775 group-write mode가 그대로 복원됐다고 주장하지 않는다. 임의 touch나 원 실패 tree의 metadata 수정은 없다.

fresh MPFR의 Makefile.in/configure에 대한 격리 dependency query는 두 target 모두 exit0이었다. 원 package make를 cheap preflight로 호출하지 않았다. 실제 MPFR configure/build/check/install 동안 기존 generated-source bytes/mtime 변화가 없음을 전후 observation으로 확인했다. original FLINT bootstrap의 생성 동작은 원 명령대로 유지하고 전후 metadata를 별도 저장했다.

실제 clean PATH에서 기존 genuine Autoconf2.71, Automake/aclocal1.16.5, autom4te/autoheader/autoreconf, M4, libtoolize, Perl, R1의 workspace Texinfo7.1과 shebang/data-file hashes를 결속했다. 작은 libtool/automake generated-build sample에서 autoreconf/configure/compile 및 makeinfo 변환이 PASS였다. 새 unit의 capability/namespace 안에서도 generator 검증을 통과했다. FLINT AC_PREREQ2.62와 실제 bootstrap 성공이 선택 근거다. 불필요한 Automake1.17/Autoconf 설치나 가짜 version alias는 하지 않았다.

기존 user@0.service 위임 안의 새 wu088-prep-r2 unit에서 실제 memory.max=34359738368, cpu.max=400000 100000을 재관측했다. membership에 들어간 뒤 private mount/cgroup namespace에서 cgroup2를 read-only remount하여 원 adapter가 읽는 경로와 맞췄다. UID/GID0, initial user namespace, capabilities0/NoNewPrivs1을 parent/launcher child에서 관측하고 child의 같은 membership/namespace 및 seccomp filter를 기록했다. 원 nofork probe PASS. 이는 별도 비root UID 또는 모든 탈출/lifecycle race 검증은 아니다. limit은 RAM 예약이 아니며 host ancestors/current/여유/siblings를 별도로 기록했다. host-global mount/기존 계정/다른 작업 cgroup은 변경하지 않았다. unit 종료 이후 private namespace/cgroup은 historical observation이므로 미래 실행은 재생성/재관측이 필요하다.

CONTINUATION_PLAN_R2 self-hash와 byte hash를 분리해 먼저 봉인한 뒤 새 backend source/prefix에서 최대1회 실행했다. 원 GMP6.3.0/MPFR4.2.2/FLINT3.4.0 pins, jobs2, 원 budget과 -O2 -fno-fast-math -ffp-contract=off를 유지했다. 명시적 새 orchestration의 extraction 경계에서 후보를 호출했으며 frozen module 수정/숨은 monkeypatch는 없다. backend record와 별도 supplement가 새로운 extractor/tool/orchestration identities를 드러낸다. 원 provenance gate의 BYTE_CHAIN_VERIFIED를 독립 실행/과학 심사로 확대하지 않는다. FLINT check는 arb/acb/acb_hypgeom/acb_calc 선택 모듈이며 전체 upstream suite가 아니다.

backend 실제 결과: PINNED_BACKEND_BUILD_IDENTITY_VERIFIED, 시도 1회. 완료/실패 stage의 실제 stdout/stderr/exit/시간은 PREP_REMEDIATION_RETURN 및 원 STAGE receipt에 있다. worker/proposal 존재: True. 모든 backend 단계가 성공한 뒤에만 원 cached worker를 compile/link/ABI 검증했다. primitive_worker/원 runtime_adapter run/worker/consume를 실행하지 않고 hash-locked BINDING_PROPOSAL만 작성했다.

FLINT build의 upstream compiler warning은 원 stderr 로그와 COMPILER_DIAGNOSTICS에 그대로 보존했다. warning-free 또는 independent scientific accuracy를 주장하지 않는다. 원 source/flags를 바꾸어 경고를 숨기지 않았다.

원 source snapshot, 이전 두 실패 backend tree, R1 결과, 원 PREPARED/registry/raw/B22의 32913개 항목은 bytes/mode/mtime/symlink target 변경0으로 확인했다. B22 105/057 claim bytes/SHA/mtime/PID 문자열은 그대로이며 process 원인을 추정하지 않았다. 새 scientific EXECUTION_BINDING/RUN_STARTED/raw/RETURN은 없다. scope 안의 JSON authority 문자열은 이번 과학 실행 승인이 아니다.

다음 최소 action: Separate exact human science authorization covering the sealed proposal, then fresh runtime/cgroup/static identity and one-shot registry revalidation; this turn performs no science.

missing269는 unbounded이며 contribution0이 아니다. epsilon_C/R=null, B22OPEN_UNDETERMINED, scientific/production admission=false, R31AK frozen/z0.75 holdout/B128-B160 consumed/B192 reuse를 유지한다. DB나 Bianchi/rei_bianchi/다른 원자 저장소를 변경하지 않았다.

결과 package는 evidence, 실제 build prefix/worker/logs, 후보 source와 명시적 helper를 포함한다. 성공 시 재생성 가능한 disposable source/metadata-probe/sample 중간 산출물은 local tree manifest에 identity를 보존하고 ZIP에서 제외할 수 있다. 실패 시 새 부분 backend tree를 포함한다. ZIP CRC와 각 payload SHA를 검증한다. same-branch additive/nonforce publication 및 Drive/Dropbox create-only ACK+name/size/object identity는 detached receipt에 남긴다. 실제 output content restore가 없으므로 RESTORE_VERIFIED=false다.
