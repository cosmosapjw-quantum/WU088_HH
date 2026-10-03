# WU088_HH NCP 준비 복구 R1 반환

종료 상태: **PREPARATION_BLOCKED**. 과학 dispatch=0, scope_consumed=false. 이번에 고정한 backend build 1회는 MPFR build에서 실제 exit 2로 실패했으며, 재시도하지 않았다.

최신 remote `ddd9e62b3b6d356f1bdc0bb7ec59a7751346eac8`의 START_PROMPT와 연결된 상세 prompt를 실제로 읽었다. 상세 prompt는 양 provider metadata를 확인한 뒤 Dropbox에서만 1회 회수했고 13,046 bytes/SHA256 `9557eb6de5235da550c8c5f0c24643d31f43e09904339270fb66c3946b2db49d`를 검증했다. 기존 통합 입력 cache의 SHA도 재확인했으며 재다운로드하지 않았다.

GNU Texinfo 7.1을 configured APT repository의 package hash와 대조하여 workspace 안에 추출했다. dpkg install, system apt install, /usr/bin 변경을 수행하지 않았다. 진짜 texi2any와 Perl data를 호출하는 wrapper를 명시적 도구 목록에 추가했으며, 원 clean_environment의 실제 PATH에서 버전과 작은 texi→info 변환이 모두 exit 0이었다. 원 pinned builder/source bytes와 flags는 유지했고 새 비수치 orchestration identity를 별도로 기록했다.

이미 Delegate=yes인 user@0.service 아래 작업 전용 user transient unit에서 MemoryMax=34,359,738,368 bytes와 CPUQuota=400%를 실제 설정·관측했다. 작업 소속에 진입한 뒤 private mount/cgroup namespace에서 cgroup2를 read-only로 다시 mount했다. 원 adapter resources()가 읽는 /sys/fs/cgroup/{cpu.max,memory.max}에서 실제 `400000 100000` 및 `34359738368`을 읽었고 원 CPU>=2/finite memory>=6GiB gate를 그대로 통과했다. host ancestors, current usage, siblings, host memory, membership, mountinfo와 namespace inode를 기록했다. limit은 RAM 예약이 아니다. host 전역 mount와 다른 작업 cgroup은 변경하지 않았다.

실행 parent/native launcher child 모두 UID/GID 0이며 initial user namespace에 남아 있다. CapPrm/Eff/Bnd/Amb=0, NoNewPrivs=1을 관측했고 native child에서 seccomp filter와 같은 cgroup/namespace를 확인했다. 원 nofork probe도 PASS였다. 이를 별도 비root UID 검증, 모든 cgroup escape 방지 또는 전체 lifecycle race 증명으로 확대하지 않는다. 실패 종료 뒤 전용 cgroup/namespace는 더 이상 live가 아니므로 미래 실행에는 재생성과 즉시 재관측이 필요하다.

원 실패 backend를 그대로 둔 새 prefix에서 원 pins(GMP6.3.0/MPFR4.2.2/FLINT3.4.0), jobs=2, compiler당 2GiB, 원 flags 및 stage/global/disk 예산으로 1회 실행했다. GMP configure/build/check/install 및 MPFR configure는 PASS였다. MPFR build는 `automake-1.17: command not found`로 실패했다. 설치된 Automake/aclocal은 1.16.5다. Autoconf 2.71과 생성된 aclocal.m4의 2.72 차이는 warning으로 별도 기록하며 이번 fatal 원인과 동일시하지 않는다. info/Makefile 재생성의 전체 원인은 확정하지 않았다. FLINT는 시작하지 않았고 worker compile/link/ABI 및 BINDING_PROPOSAL은 생성하지 않았다.

최소 다음 조치는 workspace-local genuine Automake 1.17의 automake-1.17/aclocal-1.17을 실제 clean PATH의 명시적 도구 목록에 결속하고 버전/실제 생성 동작을 검증하는 것이다. Autoconf 호환 warning도 다음 source-bound 계획에서 확인한다. 현재 증거상 시스템 관리자 변경은 필요하지 않다. 이번 1회 build 예산은 소비됐으므로 보존된 실패 tree에서 다시 make하지 말고 별도 검토된 continuation에서 새 prefix/계획/예산을 고정해야 한다. 버전 symlink 위조, mtime/touch 우회, 문서 삭제, numeric flags 변경은 허용되지 않는다.

준비 helper의 초기 PID 비교 및 archive 경로 오류는 build 전에 수정했고 두 실패 로그와 해당 helper bytes를 보존했다. 초기 mount-overmount 진단 실패도 보존했다. 실제 backend build attempt는 1회다. 새 proposal seal 안전 검사 3개는 red→green을 확인했고, 기존 40개 검사는 반복하지 않았다.

기존 manifest 14,477개와 기존 source/failed tree/pilot/evidence 전체 16,380개 항목의 bytes/SHA/mtime 및 symlink target을 검증하여 변경 0을 확인했다. 기존 218개 symlink는 모두 실패 tree 내부에 결속된다. B22 105/057 claim의 bytes/SHA/mtime/PID 문자열을 보존했으며 process 원인을 추정하지 않았다. 원 PREPARED self-hash와 byte hash는 분리되어 있다.

accepted=20/289, missing=269 unbounded, epsilon_C/R=null, B22=OPEN_UNDETERMINED, scientific/production admission=false를 유지한다. 원 run/worker/consume를 호출하지 않았고 registry/RUN_STARTED/raw/RETURN을 새로 만들지 않았다. Bianchi/rei_bianchi/다른 원자 저장소를 수정하지 않았다. 원 native EXTERNAL_RETURN schema와 historical PREPARED는 보존한다.

전체 로그·부분 build tree·실제 도구 data·보존 관측은 결과 ZIP에 포함한다. FILE_MANIFEST는 symlink target bytes를 구분하며 ZIP CRC와 payload SHA를 재검증한다. publication 및 양 provider ACK+name/size/object identity는 detached receipt에 기록한다. output의 실제 content restore를 수행하지 않으면 RESTORE_VERIFIED=false다.
