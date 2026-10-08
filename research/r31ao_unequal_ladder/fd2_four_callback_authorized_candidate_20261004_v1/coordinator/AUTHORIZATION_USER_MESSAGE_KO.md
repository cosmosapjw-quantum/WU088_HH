아래 FD2 proposal에 결속된 고정 4회 후보 field callback 실행을
명시적으로 승인한다. 적분은 0회다.
이 사용자 메시지를 승인 원문으로 보존하고, 모든 실행 전 조건이
충족되면 같은 승인을 다시 요청하지 말고 한 번 실행하라.

PROJECT=cosmosapjw-quantum/WU088_HH
BRANCH=research/r31ao-unequal-order-ladder-20260930
PREPARATION_COMMIT=6c4c85eef33ef4fe733716a76523476e4aab7eef
ROOT=/root/WU088_NCP_EXEC_20261003_v2/fd2_prep_20261004_v2
PROPOSAL=$ROOT/evidence/FD2_CANDIDATE_PROPOSAL.json

PROPOSAL_SELF_SHA256=c7bbb5cb80629d57553a06b835d6b8a81348a2c6f5a3a573cfa1fa9717b59692
PROPOSAL_FILE_SHA256=4ab58ad2a1946f4541557e2969cb31ae5f9cedee3dc9f2a0f0b2fcaf6e67fb53
QUERY_SCOPE_SHA256=3aee33191de95106a62b2bdc91bc9487680701697a5123004ee03cbf1266e937
BUILD_SELF_SHA256=a8dcf6b1c41a3f3c54ef9fbe3f254bd4d30cc86901ad79abd0c7ddb68c6ec021
CANDIDATE_SOURCE_SHA256=e508057f4a1dfb9422a0bb7b678072b08f77dcff54f4466c0fce1d57d375e14a
BINARY_SHA256=e469a7d0af30d71ce870afce57c5a6512405e9bd7d96283bc1e26764c12c2072

1. 회수·승인 결속
최신 remote successor를 읽되 과거 commit으로 reset하지 않는다.
기존 workspace/cache를 우선 사용한다. 준비 ZIP이 없을 때만
인증된 Drive/Dropbox 한 곳에서 다음 객체를 직접 회수한다.
사용자에게 재업로드를 요구하지 않는다.

name=WU088_HH_FD2_NCP_CANDIDATE_PREPARATION_20261004T074747Z.zip
bytes=4246085
SHA256=cdde98085605babf968348e611b6a62e0cf49fe437d32b739c3d0be31a4b55be
Drive ID=12aEsnLRCQ9VJDo8jkzR_auJ5lUrlUU4s
Dropbox ID=id:BSpOijBcT10AAAAAADx4_Q

승인 원문을 별도 UTF-8 파일로 보존하고, 봉인된
diagnostic_adapter.py의 authorization_check에 맞는 기록을 작성한다.
kind=HUMAN_EXACT_FD2_CANDIDATE_AUTHORIZATION
source=EXPLICIT_LATER_USER_MESSAGE
proposal_sha256=위 proposal self-hash
query_scope_sha256=위 query scope
query_keys=[Q272_cached,Q272_reference,Q000_cached,Q000_reference]
max_field_callbacks=4
integrations=0
resource_policy=proposal.future_resource_policy 전체 원 객체
user_message=실제 사용자 승인 원문 ref(path,bytes,sha256)

원 coverage_contract.seal 방식으로 authorization_sha256을 생성한다.
Proposal의 science_authorized=false와 self-hash는 변경하지 않는다.
원 FD1·6셀 승인이나 assistant 초안의 존재를 이번 승인으로 사용하지 않는다.

2. 승인 범위
Q272_cached → Q272_reference → Q000_cached → Q000_reference 순서.
각 key 최대1회, 총 최대4 field callback, workers=1, integrations=0.
Cached와 reference 모두 FD2 후보에 결속된 구현을 사용한다.

Primitive0, fieldO, OrbitalS, ia0/ib0/active0, order0, precision128,
원 exact box·log map·margin·signed ordered107을 유지한다.
추가 box/field/helper 조회, midpoint 대체, 정밀도·급수·guard·tail 변경은 금지한다.

3. 실행 전 조건
Proposal/query/build self-hash와 별도 byte hash, source_files,
inherited_files, candidate include closure, parent raw/plan,
sidecar binary, backend/system-library linkage, host launcher를 대조한다.

FD2 future_registry/future_output_root/CALL_STARTED 흔적이 있으면
재실행하지 말고 기존 결과를 회수한다. 새 이름·경로로 우회하지 않는다.
소비된 원 FD1·6셀 registry는 그대로 보존한다.

Proposal의 원 자원 정책을 그대로 적용하고 live_gate를 통과한다.
unit=wu088-fd2-candidate.service
memory.max=34359738368
cpu.max='400000 100000'
query wall=10초, query memory=1024MiB, unit RuntimeMaxSec=60초
원6GiB headroom·유효CPU·private cgroup/mount·read-only ancestor view,
UID0/capabilities0/NoNewPrivs1 조건을 유지한다.

새 PID·namespace·소속·조상 한도·현재 여유·loader를 관측하고
LIVE_BINDING으로 원 proposal에 연결한다.
역사적 준비 관측으로 대체하거나 원 proposal을 덮어쓰지 않는다.
정적 identity나 승인 정책이 다르면 scope 소비 전에 중단한다.

4. 실행
Proposal.future_execution_blueprint를 사용하고 마지막 세 인자만
proposal self-hash, 새 승인 기록 경로, 승인 self-hash로 대체한다.

이미 구현된 authorized_namespace.sh → diagnostic_adapter.py run을
한 번 호출한다. 준비 pipeline·33개 scalar suite·backend/sidecar
재빌드를 반복하지 않는다. --hh-single 직접 호출로 gate를 우회하지 않는다.

정상적으로 기록된 fresh nonfinite는 유효한 부정 관측이다.
원 adapter대로 남은 고정 비교를 진행하되 retry하지 않는다.
Timeout/native nonzero/stale error/binding 오류에서는 남은 호출을 중단한다.

5. 결과 판정
Native exit0이나 OBSERVATIONS_AWAITING_REVIEW만으로 성공을 선언하지 않는다.
아래 조건을 실제 결과로 확인한다.
- 네 호출의 clean finite physical/mapped 출력.
- Cached terms_started=terms_completed=107.
- Reference의 고정 전체 loop와 clean finite return.
- 같은 query의 후보 cached/reference physical·mapped 구간 overlap.

원 adapter의 --compare-balls는 저장된 출력만 비교하는 field0회 경로다.
최대4개 저장 구간 비교도 원 전체 자원 예산 안에서 수행한다.
원 nonfinite FD1과 overlap을 강제하지 않고 width를 그대로 보존한다.

최종 RETURN의 candidate_field_finite_and_107_complete_and_overlap과
CANDIDATE_ENCLOSURE_COMPARISON.json을 확인한다.
관측 성공, 후보 유한성, 구간 일관성, 적분 수렴을 구분한다.
미완료·nonfinite·disjoint는 원 증거로 반환하고 추가 계산하지 않는다.

6. 반환·백업
승인 원문/기록, fresh outside observation/LIVE_BINDING, registry,
호출별 CALL_STARTED/stdout/stderr/OBSERVATION/RETURN, 원 Arb dump,
구간 비교와 최종 RETURN, command/exit/timing/hash manifest를 보존한다.
없는 파일은 absent+reason, 실행 여부 불명은 unknown으로 기록한다.

같은 branch에 additive/non-force 게시하고 기존 Drive/Dropbox
목적지에 Codex가 직접 create-only 백업한다. Credential을 기록하지 않는다.
ACK+metadata와 실제 restore를 구분한다.

기존24/289, 미상계265, epsilon_C/R=null, B22 OPEN_UNDETERMINED,
scientific/production admission=false를 유지한다.
기존 결과·PREPARED·실패tree·원DB·소비 registry를 변경하지 않는다.

이번 승인은 두 셀 적분, 추가 query, queue/허용오차 조정,
production 설치, full49/propagation/sigma/k, Bianchi/rei_bianchi와
다른 저장소 변경을 포함하지 않는다. 고정 후보 결과를 반환한 뒤 종료하라.
