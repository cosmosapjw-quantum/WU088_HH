아래 FD1 proposal에 결속된 고정 4회 field callback 진단을
명시적으로 승인한다. 적분은 0회다.
이 사용자 메시지를 승인 원문으로 기록하고, 모든 조건이 충족되면
같은 승인을 반복 요청하지 말고 지정된 진단을 한 번 실행하라.

PROJECT=cosmosapjw-quantum/WU088_HH
BRANCH=research/r31ao-unequal-order-ladder-20260930
PREPARATION_COMMIT=5b95029d9473429bd934a8f525ebdc0b32e716ac
ROOT=/root/WU088_NCP_EXEC_20261003_v2/fd1_prep_20261003_v3
PROPOSAL=$ROOT/evidence/DIAGNOSTIC_PROPOSAL.json

PROPOSAL_SELF_SHA256=4f121182611c1609145728cbddfc5c346fdbbdf9c8424527b25534f282ad37be
PROPOSAL_FILE_SHA256=73993d5f8b642874c521e646847c1f68fa604b4e15e0b641bea5f5e87241c79b
QUERY_SCOPE_SHA256=20ff5d09ea36b1a87489ea80961bb692161ff881fa4075c71637b81afc9cfc51
SIDECAR_SOURCE_SHA256=8850d822137bbe18109457349713682a1e8ae386d8553bb82c7f76630e327056
SIDECAR_BUILD_SELF_SHA256=a65848adb48217b46499b400dfbce5775a912dfa0045c185b54cd8a35706bb79
SIDECAR_BINARY_SHA256=6f47315847a003a8da255bd60b6678a24acaaf813086f03bf00f9c4acb613478

1. 입력과 승인 기록

최신 remote successor를 읽되 과거 commit으로 reset하지 않는다.
기존 NCP workspace와 검증된 cache를 우선 사용한다.
필요한 FD1 package가 없을 때만 아래 cloud object 한 곳에서 회수한다.
사용자에게 파일 재업로드를 요구하지 않는다.

이름= WU088_HH_FD1_PREPARATION_20261003T153408Z.zip
bytes=4176233
SHA256=295cbd7a58e441ce0a4372f9fa77c3ae034b1433003c16c68fe17ccc0e796da0
Drive ID=1gsaNchJEhNMcTkuBTisdOYwzHi25vzP5
Dropbox ID=id:BSpOijBcT10AAAAAADx4Pg

이 사용자 메시지의 원문을 별도 UTF-8 파일에 보존한다.
원 diagnostic_adapter.py의 authorization_check에 맞춰 다음을 포함한
AUTHORIZATION_RECORD를 만들고 원 seal 방식으로 봉인한다.

kind=HUMAN_EXACT_DIAGNOSTIC_AUTHORIZATION
source=EXPLICIT_LATER_USER_MESSAGE
proposal_sha256=위 PROPOSAL_SELF_SHA256
query_scope_sha256=위 QUERY_SCOPE_SHA256
query_keys=[Q272_cached,Q272_reference,Q000_cached,Q000_reference]
max_field_callbacks=4
integrations=0
resource_policy=proposal.future_resource_policy 전체 원 객체
user_message=실제 승인 원문 파일의 ref(path,bytes,sha256)

원 proposal의 science_authorized=false와 self-hash는 변경하지 않는다.
기존 6셀 승인이나 assistant의 승인문 초안을 승인 근거로 재사용하지 않는다.

2. 정확한 실행 범위

순서:
Q272_cached → Q272_reference → Q000_cached → Q000_reference

각 key당 최대1회, 전체 최대4회, workers=1, integrations=0.
primitive_index=0, field=O, orbital=S, ia=0, ib=0, active=0,
precision_bits=128, order=0, ORIGINAL_SIGNED_ORDERED107을 유지한다.

QUERIES와 proposal.geometry의 정확한 Arb dump, 첫 inner box 생성식,
원 log map·margin·계수 순서를 보존한다.
midpoint 대체, box 축소·확대, 추가 field/order/precision 조회는 금지한다.
각 callback의 Contract와 CacheStats는 fresh 상태여야 한다.

3. 실행 직전 검증과 자원

proposal/query/build self-hash와 별도 file byte hash를 각각 확인한다.
source_files·inherited_files·parent raw/plan·geometry·sidecar binary·
backend/system-library linkage·원 host launcher를 대조한다.

소비된 원 6셀 registry는 그대로 둔다.
FD1 future_registry/future_output_root/CALL_STARTED 흔적이 있으면
재실행하지 말고 기존 결과를 회수한다. 새 이름이나 복사본으로 우회하지 않는다.

proposal.future_resource_policy를 그대로 적용한다.
unit=wu088-fd1-diagnostic.service
memory.max=34359738368
cpu.max='400000 100000'
query wall=10초, query memory=1024MiB
전체 unit RuntimeMaxSec=60초
원6GiB 여유·유효 CPU 조건 유지
private mount/cgroup 및 read-only ancestor view 유지
UID0/capabilities0/NoNewPrivs=1을 기록하며 비root 검증으로 부르지 않는다.

새 PID·namespace·소속·조상 한도·사용량·headroom·loader를
원 live_gate로 재확인한다. 과거 준비 unit의 관측으로 대체하지 않는다.
정적 identity나 승인 정책이 다르면 소비 전에 중단한다.

4. 실행 진입점

원 proposal.future_execution_blueprint를 사용한다.
마지막 세 인자는 proposal self-hash, 새 AUTHORIZATION_RECORD 경로,
그 authorization self-hash로 대체한다.

이미 구현된 authorized_namespace.sh → diagnostic_adapter.py run을
한 번 사용한다. 준비 entrypoint를 다시 호출하거나 새 dispatcher를 만들지 않는다.
성공한 backend·primitive worker·sidecar를 재빌드하지 않는다.
--hh-single을 shell에서 직접 호출해 원 gate를 우회하지 않는다.

5. 관측과 중단

Fresh failure/nonfinite가 정상 기록되고 native exit0과 관측 validator가
통과하면 유효한 진단 관측이다. 이것만으로 retry하거나 중단하지 말고
원 adapter대로 다음 고정 비교 호출을 진행한다.

Timeout, native nonzero exit, stale/uncharged error, 횟수·geometry·
source binding 불일치에서는 원 adapter대로 남은 호출을 중단한다.
전체 wall cap으로 final RETURN이 없으면 부분 로그·marker를 보존하고
absent+reason을 기록한다. 실행 여부 불명을 미실행으로 바꾸지 않는다.
4개를 채우기 위한 재시도나 예산 확대는 금지한다.

6. 반환과 보존

승인 원문/AUTHORIZATION_RECORD, fresh outside observation,
LIVE_BINDING, diagnostic registry, 호출별 CALL_STARTED,
native stdout/stderr, OBSERVATION/RETURN, 원 Arb dump,
실제 command/exit/PID/timing과 hash manifest를 반환한다.

네 query의 fresh last_error·calls/failures·CacheStats·physical/mapped
finite flag를 나란히 정리한다. 차이가 있다는 이유만으로 cache 버그나
수학적 발산을 확정하지 않는다. 원인이 결정되지 않으면 UNRESOLVED로 종료한다.

기존24/289, 미상계265, epsilon_C/R=null, B22 OPEN_UNDETERMINED,
scientific/production admission=false를 보존한다.
FD1 결과를 새 수락 셀이나 적분 enclosure로 집계하지 않는다.

같은 연구 branch에 additive/non-force 게시하고 기존 Drive/Dropbox에
Codex가 직접 create-only 백업한다. 사용자 재업로드를 요구하지 않는다.
ACK+metadata와 실제 restore를 구분한다.

이 승인은 고정 진단만 포함한다. 셀 재적분, 추가 box, coverage 확대,
queue/정밀도/허용오차 변경, 최적화, full49·propagation·sigma/k,
Bianchi/rei_bianchi 및 다른 저장소 변경은 포함하지 않는다.
이번 진단 반환 뒤 종료하라.
