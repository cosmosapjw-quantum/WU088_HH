아래 proposal에 결속된 WU088_HH 고정 6셀 pilot의 과학 실행을
명시적으로 승인한다. 이 사용자 메시지를 승인 원문으로 기록하라.
아래 조건이 충족되면 같은 승인을 다시 요청하지 말고 실행하라.

PROJECT=cosmosapjw-quantum/WU088_HH
BRANCH=research/r31ao-unequal-order-ladder-20260930
PREPARATION_COMMIT=80e87bcbad5d803e8010fa3c7190b7a425734445

PROPOSAL=/root/WU088_NCP_EXEC_20261003_v2/prep_r2/evidence/BINDING_PROPOSAL.json
PROPOSAL_SELF_SHA256=51a474d473a9a095a1bae68949e63bd1dfdc50d7b12c9a971a85323054f0b57c
PROPOSAL_FILE_SHA256=cdaf21b33cfbf4a3abd1f977332ad983da84d4026b5601443f6b41fd0adeb116
PREPARED_SELF_SHA256=0e06c0f959684e808f1ef1f6d8465e00079e0b6401eba311b804e458bac0f3a0
SCOPE_SHA256=91f8f304f2c0aa8668a1d8bc18b1972348768772fa308d8b3c9483cc8c254a5b
WORKER_BUILD_SELF_SHA256=51493d807432d46106cdee5e83ebc5d1830234fead90b28a0845915da148982e

승인 범위:
- primitive0, 원 signed ordered107 및 동결된 입력·기하.
- 셀 순서 [275,67,288,272,16,0], 최대6회, 각 셀1회, 2-worker.
- precision_bits=128, radius_exp=-57, relative_goal=128.
- 셀당 max_evaluations=200000, max_integration_calls=1024,
  queued_panels=64, degree_limit=64, native wall=120초.
- native/worker memory=1024MiB, host hard wall=125초,
  worker wall=180초 등 원 제한을 그대로 유지한다.
- 첫 거절·실패 뒤 신규 dispatch 중단, 진행 중 작업 회수.
- 자동 retry와 새 scope/output 이름으로 우회한 재실행은 금지한다.

실행 직전:
1. 최신 remote successor와 canonical local runtime/cache를 확인한다.
   과거 commit으로 reset하지 않는다.
2. 원 serializer로 proposal self-hash를 검증하고, 별도로 파일 byte hash,
   PREPARED·6개 plan·입력·원 source·adapter·host launcher·worker binary·
   backend 및 system-library linkage를 대조한다.
3. 원 registry와 RUN_STARTED/EXECUTION_BINDING/raw/RETURN을 확인한다.
   이미 시작한 흔적이 있으면 재실행하지 말고 기존 결과를 회수한다.
4. R2와 같은 실제 작업 전용 cgroup 정책을 새로 적용·관측한다.
   memory.max=34359738368, cpu.max='400000 100000',
   concurrency=2 및 원6GiB 자원 기준을 보존한다.
   조상 제한·현재 사용량·실제 여유·affinity도 확인한다.
5. 동일 private mount/cgroup view, capabilities0, NoNewPrivs와
   기존 host launcher 제한을 유지한다. R2의 UID0 경로를 별도 비root
   UID 검증으로 부르지 않는다.
6. 새 PID·namespace·unit·사용량은 LIVE_REVALIDATION.json에 기록하고
   원 proposal 해시에 연결한다. 원 proposal은 변경하지 않는다.
   정적 identity나 승인 정책이 다르면 scope 소비 전에 중단한다.

실행:
- 성공한 backend/worker를 재빌드하지 않는다.
- prep_r2/namespace_entry.sh는 준비 pipeline을 호출하므로 재호출하지 않는다.
- 필요하면 같은 격리 정책의 실행 전용 얇은 launcher를 새 파일로 만들고,
  source hash·구문·실행 전 거절 경로를 기록한다.
  기능은 live 검사와 원 CLI 호출로 제한한다.
- 모든 조건이 닫힌 뒤 proposal.future_execution_path의 값으로
  원 runtime_adapter.py run을 같은 live 격리 환경에서 한 번 호출한다.
- 원 run/worker/consume를 시험 호출하거나 별도 dispatcher를 만들지 않는다.

보존:
- 기존20셀·endpoint·AD1~AD3·완료 producer 재실행 금지.
- B22 105/057 claim과 원 PREPARED·과거 실패 tree 보존.
- R31AK frozen, z0.75 holdout, B128/B160 consumed, B192 reuse 유지.
- 계수 순서·정밀도·허용오차·기하·Q·phase·ETF 변경 금지.
- 6셀 전부 성공해도 최대26/289이며 전체 D/epsilon 인증이 아니다.
- 나머지 셀,2592 primitive,full49,trajectory,sigma/k,production,
  MPI/Fortran/SIMD 확대와 Bianchi/rei_bianchi 작업은 승인 범위 밖이다.

반환:
AUTHORIZATION_RECORD, LIVE_REVALIDATION, 원 EXECUTION_BINDING/
RUN_STARTED, plans, raw, attempts/worker 로그와 RETURN, normalized,
COVERAGE, 최종 RETURN, registry, 실제 명령·exit code·hash manifest를 남겨라.

누락 자료는 absent+reason으로 기록한다. 자원·ABI·구현·수치 폭/시간초과를
구분하고, 미계산 기여를0으로 처리하지 않는다.

같은 branch에 additive/non-force 게시하고 기존 Drive/Dropbox에
Codex가 직접 create-only 백업한다. 기존 cache를 재사용하고 사용자에게
파일 재업로드를 요구하지 않는다. 결과를 반환한 뒤 이번6셀 범위에서 종료하라.
