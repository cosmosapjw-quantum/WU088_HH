# WU088_HH FD2 고정 후보 callback 반환

상태: FD2_CANDIDATE_FIELD_FINITE_AND_CONSISTENT_AWAITING_REVIEW. 원 최종 RETURN의 candidate_field_finite_and_107_complete_and_overlap=true를 각 raw/OBSERVATION, 107항 카운터, 원 reference source 전체 loop 및 저장 출력 비교로 검증했다. 네 field callback을 승인 순서로 각1회 실행했고 저장 구간 비교4회는 field0회 경로였다. 적분0회, retry0회이며 FD2 scope는 영구 소비됐다.

| Query | calls/failures 전→후 | fresh last_error | physical/mapped finite | terms 완료 근거 | native PID |
|---|---|---|---|---|---|
| Q272_cached | 0/0 → 1/0 | empty | true/true | 107/107 | 246264 |
| Q272_reference | 0/0 → 1/0 | empty | true/true | reference full loop | 246265 |
| Q000_cached | 0/0 → 1/0 | empty | true/true | 107/107 | 246267 |
| Q000_reference | 0/0 → 1/0 | empty | true/true | reference full loop | 246268 |

호출 전 Contract/CacheStats/last_error는 모두 fresh0/empty다. 호출 후 calls1/failures0, last_error empty, fresh_failure=false, physical callback/log map return0이다. cached 두 호출은 terms_started=terms_completed=107, L/R/S requests107/107/107, evaluations8/8/9, hits99/99/98이다. Reference CacheStats는 미사용0이며 0항 계산을 뜻하지 않는다. 원 source의 전체107 ordered-term loop와 clean finite return을 완료 근거로 기록했다.

Q272와 Q000 각각 cached/reference physical 및 mapped 구간 overlap을 원 --compare-balls로 확인했다. 네 비교 모두 overlap=true 및 양방향 contains=true이며 같은 쌍의 원 Arb dump가 byte 동일하다. 원 nonfinite FD1과 overlap을 강제하지 않았다. 모든 원 dump/box/log map/margin/signed107을 stdout/OBSERVATION 및 QUERY_COMPARISON에 보존했다.

유한성·구간 일관성을 확인했으나 구간 폭은 크다. 아래 수치는 저장 dump의 정확한 dyadic 반경이고 전체 component 폭은 반경의2배다. cached/reference 쌍의 폭은 동일하며 모든 component가0을 포함한다. 반경을 축소하거나 midpoint로 대체하지 않았다.

| Query | 출력 | component | 정확한 반경 | 0 포함 |
|---|---|---|---|---|
| Q272_cached | physical | real | 639923959 × 2^(-27) | True |
| Q272_cached | physical | imag | 916562923 × 2^(-28) | True |
| Q272_cached | mapped | real | 38431677 × 2^(10) | True |
| Q272_cached | mapped | imag | 440365449 × 2^(6) | True |
| Q000_cached | physical | real | 561726113 × 2^(56) | True |
| Q000_cached | physical | imag | 537044209 × 2^(55) | True |
| Q000_cached | mapped | real | 539766027 × 2^(43) | True |
| Q000_cached | mapped | imag | 1032098071 × 2^(41) | True |

관측 성공, 후보 field 유한성, 동일 입력의 cached/reference 구간 일관성과 적분 수렴은 서로 다른 판정이다. 이 고정 box 결과만으로 정확도, cell enclosure, 적분 수렴, 전체 도메인 또는 후보 promotion을 승인하지 않는다. 별도 독립 결정 review도 이번 반환으로 만들어지지 않는다.

최신 remote 및 preparation commit은6c4c85eef33ef4fe733716a76523476e4aab7eef였다. 승인 사용자 원문 UTF-8 6603 bytes/SHA feda9f4455f80b3b099e4e57af7873b12823787b716d58160f0f40c5b9edb9ed를 보존했다. AUTHORIZATION_RECORD self SHA 448a0163ec9cb0d2b1885241078c2f13f592f3120f7f29495f1f1dd00c2545f7, proposal self SHA c7bbb5cb80629d57553a06b835d6b8a81348a2c6f5a3a573cfa1fa9717b59692, file SHA 4ab58ad2a1946f4541557e2969cb31ae5f9cedee3dc9f2a0f0b2fcaf6e67fb53, query scope 3aee33191de95106a62b2bdc91bc9487680701697a5123004ee03cbf1266e937, build self a8dcf6b1c41a3f3c54ef9fbe3f254bd4d30cc86901ad79abd0c7ddb68c6ec021, candidate source e508057f4a1dfb9422a0bb7b678072b08f77dcff54f4466c0fce1d57d375e14a, binary SHA e469a7d0af30d71ce870afce57c5a6512405e9bd7d96283bc1e26764c12c2072다. 원 proposal science_authorized=false와 self-hash는 변경하지 않았다. 원 serializer/validator와 별도 byte identity를 대조했다. 기존 verified preparation ZIP을 재사용했고 양 provider metadata를 조회했으며 input download0이었다.

승인 blueprint의 마지막 세 인자만 교체하여 authorized_namespace.sh → diagnostic_adapter.py run을1회 호출했다. 새 unit의 실제 finite memory.max34359738368, cpu.max400000 100000, RuntimeMaxSec60, 원6GiB headroom 및 effective_CPU4.0를 원 live_gate가 소비 전에 관측했다. 새 private PID246243/mount·cgroup namespace/read-only ancestor view, UID0/capabilities0/NoNewPrivs1, loader/backend/system-library/host identity를 LIVE_BINDING에 결속했다. UID0를 비root 검증으로 부르지 않는다. live host MemAvailable=131210436608 bytes, affinity count=64다. 원 capacity concurrency2와 이번 workers1 순차 dispatch를 구분한다. 각 query wall10초/memory1024MiB 및 원 host 제한, 전체 unit wall60초를 유지했다. 바깥 post-run ldd와 원 private preflight loader 검증은 구분한다.

원 blueprint wrapper wall=1.264486175초, manager Service runtime1.229초/CPU1.108초/peak23.8M/swap0B로 기록됐다. callback PID246264/246265/246267/246268, read-only comparison PID246269/246270/246271/246272다. /proc observer는 요청 delay5ms에 directory scan 시간이 추가되므로 exact5ms 주기로 부르지 않는다. 미관측 /proc 및 원 adapter가 기록하지 않은 exact native timing/개별 comparison marker는 ABSENT_FILES에 사유를 기록했다. callback marker→RETURN 시간은 launch/wait/validation을 포함한 파일 event 구간이다.

준비/33개 scalar suite/backend/primitive worker/FD1·FD2 sidecar 재빌드0회다. 증거 coordinator의 첫 사전 검사는 package 내 과거 FD1 marker를 광범위 검색하여 중단했으며 callback0/scope 미소비였다. marker proposal/scope를 대조해 archived consumed FD1 증거로 분류한 뒤 사전 검사를 완료했다. 실패 기록을 보존했고 원 adapter/source/proposal을 수정하거나 실행을 재시도하지 않았다. Provider metadata 직렬화의 첫 NameError도 science0인 coordinator 오류로 별도 보존했다.

기존 보호 파일/링크 74466개는 bytes/SHA/mode/mtime/target 변화0이다. 원 PREPARED/실패tree/DB/수락24셀/소비6셀·FD1 registry/원 backend·worker·FD1 binary, B22 105/057 claim bytes/SHA/mtime/PID 문자열을 보존했다. PID 문자열로 process/race 원인을 확정하지 않는다. accepted24/289, missing265 unbounded, epsilon_C/R=null, B22 OPEN_UNDETERMINED, scientific/production admission=false를 유지한다. 미계산 기여를0으로 놓지 않았으며 새 수락셀을 추가하지 않았다. R31AK frozen/z0.75holdout/B128B160consumed/B192reuse를 유지하고 Bianchi/rei_bianchi/다른repo를 변경하지 않았다.

승인 원문/봉인 기록, fresh outside/LIVE_BINDING/registry, 네 CALL_STARTED/stdout/stderr/OBSERVATION/RETURN, 네 비교 stdout/stderr/aggregate comparison, 최종원 RETURN, 실제 command/exit/PID/timing/hash manifest를 반환한다. 같은 branch additive/non-force publication과 Drive/Dropbox create-only ZIP/보고서/receipt의 ACK/object/metadata는 detached receipt로 기록한다. ACK+metadata와 실제 restore를 구분하며 출력 RESTORE_VERIFIED=false다. 이번 고정 후보 결과 뒤 추가 query·적분·재실행을 수행하지 않는다.
