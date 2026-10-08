# WU088_HH 고정 6셀 pilot 반환

종료 상태: **PILOT_STOPPED_FIRST_REJECTION**. 사용자 원문 승인에 결속된 scope를 원 runtime_adapter CLI로 1회 실행했으며, native dispatch/관측은 6회, scope_consumed=true다. 재빌드·재시도·scope 확대는 없었다.

|셀|원 native 결과|원 validator 결과|평가 수|적분 호출|
|---:|---|---|---:|---:|
|275|RADIUS_MET|수락|642|34|
|67|RADIUS_MET|수락|1358|22|
|288|RADIUS_MET|수락|2|2|
|272|INTEGRATOR_NO_CONVERGENCE|거절|13766|126|
|16|RADIUS_MET|수락|4786|50|
|0|INTEGRATOR_NO_CONVERGENCE|거절|15635|126|

기존20셀과 새 수락4셀을 원 exact coverage 산술로 대조해 **24/289**, missing265를 확인했다. 미계산 기여는 unbounded이며 0이 아니다. epsilon_C/R=null, B22=OPEN_UNDETERMINED, scientific/production admission=false를 유지한다. endpoint·normalization·전체 D·full49·sigma/k·trajectory를 인증하지 않는다.

272와 0은 native exit2/INTEGRATOR_NO_CONVERGENCE, rectangle=null, FLINT status2다. 272의 inner_no_convergence109, 0의124가 보고되었다. Host/worker wall timeout은 없었고, inner_resource_limit 및 inner_invalid_contract 카운터는0이었다. 이는 현재 고정 예산에서 수치 결과가 결정되지 않은 상태다. 근본 source/theory/구현 오류 또는 정확한 실패 원인은 이 반환만으로 확정하지 않는다. Native stderr는 비어 있다. 원 adapter의 전체 exit2는 거절을 반영한다.

첫 거절은272의 RETURN이며, 0은 그 전에 이미 dispatch되어 회수됐다. 승인 순서[275,67,288,272,16,0], 동시 worker2, 각 셀1회, 최대6회를 지켰다. 첫 거절 관측 후 dispatch는 없고 inflight를 모두 회수했다. campaign wall=15.301954초(준비/preflight 제외).

실행 identity

- Remote/preparation HEAD: 80e87bcbad5d803e8010fa3c7190b7a425734445. 과거 commit reset 없음.
- Proposal self SHA256: 51a474d473a9a095a1bae68949e63bd1dfdc50d7b12c9a971a85323054f0b57c
- Proposal file SHA256: cdaf21b33cfbf4a3abd1f977332ad983da84d4026b5601443f6b41fd0adeb116
- PREPARED self SHA256: 0e06c0f959684e808f1ef1f6d8465e00079e0b6401eba311b804e458bac0f3a0
- Scope SHA256: 91f8f304f2c0aa8668a1d8bc18b1972348768772fa308d8b3c9483cc8c254a5b
- Worker build self SHA256: 51493d807432d46106cdee5e83ebc5d1830234fead90b28a0845915da148982e
- 실제 EXECUTION_BINDING self SHA256: aae8b88071c3ab174d839cb722be7957763f1407f6d3575b8445cf3f66839f77
- Live revalidation self SHA256: 3709b40b4d3c5538fb15568515ee9c7796d68f2ee551f4207b7e9eabfcad201d

새 unit의 실제 memory.max34359738368, cpu.max400000/100000, affinity64와 원6GiB/2CPU gate, 조상 제한·현재 사용량·host 가용 여유를 관측했다. Private mount/cgroup view와 read-only cgroup mount, UID0 capabilities0, NoNewPrivs1을 확인했고 원 host launcher child의 동일 소속·namespace와 seccomp nofork 검증을 통과했다. UID0 경로를 비root 검증으로 주장하지 않는다. cgroup-v2 hierarchy root의 제한 인터페이스 부재는 absent 그대로 기록했으며 숫자를 주입하지 않았다. 단위 한도는 RAM 예약이나 모든 escape/경주를 독립 검증했다는 뜻이 아니다. 단위 종료로 leaf가 제거된 후의 live 수치는 재구성하지 않았다.

원 serializer self-hash와 별도 file bytes, 원 SOURCE_LOCK1834개,6개 plan/input/native source, adapter, host launcher, worker binary, backend/system-library linkage를 실행 전 대조했다. 성공 backend/worker를 재빌드하지 않았다. 승인 누락·proposal self/file hash 변경·소비 scope의4개 거절 검사는 dispatch 없이 수행했다. 새 helper의 초기 상대경로 처리 오류를 고쳐 검증했으며, 그 실패 때 run/worker/consume 호출은0회였다. 원40개 suite를 새 검사로 세거나 재실행하지 않았다.

원 raw/sidecar/host receipt/source binding을 읽어4개 결과를 원 normalize로 다시 검증하고,2개 실패를 원 validator가 거절함을 확인했다. 기존20셀 replay는 원 raw 읽기와 산술만 수행했다. 새 과학 실행은 하지 않았다. 원 EXTERNAL_RETURN schema 검증도 통과했다.

기존 자료 73525개에서 bytes/SHA/mode/mtime/symlink 변경0. 원 실패 tree·R1/R2 결과·PREPARED·입력·20셀·B22 105/057 claim bytes/SHA/mtime/PID51/74를 보존했다. claim 존재로 process/race 원인을 확정하지 않았다. 기존 registry 부재를 확인한 후 원 adapter가 정확한 scope marker를 영구 생성했다. 새 directory/이름으로 소비를 우회하지 않는다. R31AK frozen,z0.75 holdout,B128/B160 consumed,B192 reuse를 유지했고 다른 저장소는 수정하지 않았다.

반환 파일

AUTHORIZATION_RECORD 및 원문, LIVE_REVALIDATION, 원 EXECUTION_BINDING/RUN_STARTED, PREPARED·6plans·baseline,6raw/sidecars,6attempts/worker 로그/RETURN,4normalized,COVERAGE와 원 RETURN, registry, 명령/exit logs 및 hash manifest를 패키지에 포함한다. 과거 성공 build와 전체 source/cache는 기존 검증 package를 참조하며 중복 다운로드하지 않았다. 누락 normalized272/000과 종료 후 cgroup leaf는 ABSENT_FILES에 사유를 기록했다.

결과는 같은 branch의 새 continuation 경로에 additive/non-force 게시하고, ZIP·보고서·분리 receipt를 기존 Drive/Dropbox에 create-only 백업한다. ACK+name/size/object identity metadata tier를 사용하고 output RESTORE_VERIFIED=false로 기록한다. Provider의 ACK/metadata는 content restore 증거와 구분한다. 게시/백업의 실제 ID·HEAD·bytes/SHA는 DELIVERY_INDEX/분리 receipt에 기록한다.

다음 최소 action은 보존된 실패2셀의 수치 evidence와 새4셀의 원시 rectangle을 검토하는 것이다. 이번 승인된 scope는 소비되었으며 재실행하거나 추가 셀을 계산하지 않고 종료한다.
