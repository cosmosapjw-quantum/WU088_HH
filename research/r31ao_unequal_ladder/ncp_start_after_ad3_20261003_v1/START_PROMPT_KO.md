# AD3 이후 NCP local Codex 시작

NEXT_ACTION=NCP_PINNED_BACKEND_AND_SIX_CELL_PILOT_READINESS
PROJECT=cosmosapjw-quantum/WU088_HH
BRANCH=research/r31ao-unequal-order-ladder-20260930

DELIVERY_INDEX.json에 고정된 WU088_HH_NCP_START_BUNDLE_20261003_v1.zip을 새 빈 작업 디렉터리에 복원하고, 내부 WU088_HH_NCP_START_20261003_v1에서 `sha256sum -c SHA256SUMS`를 확인하라. NCP_LOCAL_CODEX_PROMPT_KO.md, NCP_START_CONTRACT.json, EXECUTION_RUNBOOK_KO.md와 reference 원문을 읽고 실제 준비를 수행하라. 전체 프롬프트와 원 실행코드는 private 전달 ZIP이 기준이다.

이 인계는 전체 이론 종료나 새 과학 실행승인이 아니다. 이전 master research loop 종료를 전제로 하는 coordinator 템플릿을 자동 활성화하지 않는다. 이미 닫힌 단계의 결과를 재사용하고 실제 남은 native 실행 의존성을 처리한다.

원자 충돌 데이터와 불확실성·출처만 담당한다. Bianchi 기하·광자수송·가스 시간진화는 rei_bianchi의 소관이며 다른 저장소를 수정하지 않는다. AD4나 추가 synthetic 감사로 우회하지 않는다.

먼저 최신 remote HEAD/tree/PR와 현재 작업트리, 기존 runtime root/run_registry/RUN_STARTED/raw/RETURN을 회수한다. 과학 checkpoint는 3677d0fe58f434813bb2e2f7630c71c7fd12a949/tree a82f6a0d79fc04c4648f1ba0bf353351eefed8d4이지만 과거 SHA로 reset하지 않는다. 새 handoff 게시 commit은 과학 실행 증거가 아니다.

패키지에는 AD3 상태 archive와 W3_COVERAGE native 실행 archive 두 개가 원 bytes 그대로 있다. 원 verifiers와 runbook을 따라 nested STRIP source snapshot과 W3 overlay를 복원한다. publication clone과 hash-locked runtime snapshot을 구분한다. 과거 PREPARED의 절대경로와 hash를 새 NCP 설정으로 사용하지 않는다.

실제 CPU affinity/quota, cgroup memory, compiler/FLINT/GMP/MPFR/ABI와 비특권 containment를 관측하고 기존 build-host/probe-host/backend/worker를 준비한다. 호환 build가 이미 검증돼 있으면 재사용한다. 64core/128GB 목표를 관측값으로 만들지 말고 원 finite-cgroup 최소6GiB 및 CPU 조건을 지켜라. fixture 주입, 자원 guard 삭제, cache purge나 타 작업 종료는 하지 않는다.

원 prepare 이후 실제 승인 근거가 source/input/plan 및 새 runtime binding을 덮는 경우에만 원 runtime_adapter.py run으로 고정6셀 [275,67,288,272,16,0]을 한 번 실행한다. 기존 승인이 충분하면 다시 요청하지 않는다. 부족하면 모든 준비결과와 승인 대상 hash를 반환하고 멈춘다. 백업 권한이나 승인처럼 보이는 JSON 문자열을 과학 승인으로 바꾸지 않는다.

고정 한도:2workers,128bit,radius_exp=-57,relative_goal128,셀당 evaluation200000/inner1024,native120s/host125s/worker180s,각1GiB,reserve6GiB,queued_panels64,degree_limit64. 첫 거절 후 신규dispatch 중단·진행중 회수,자동재시도 금지. 기존20셀·endpoint·AD1~3·완료producer는 재실행하지 않는다. B22 claim은 삭제·격리·수정하지 않는다.

모두 성공해도 최대26/289이며 전체D/epsilon·sigma/k·production은 아니다. 신규 geometry, 전체269셀/2592primitive,trajectory,정밀도·계수·Q·phase·ETF·tolerance변경,64worker/MPI최적화는 이번범위 밖이다.

WORK_REPORT_KO.md,NCP_HANDOFF_RETURN.json,COMMANDS.jsonl,FILE_MANIFEST.json,build/환경/ABI/승인/registry와 모든 pilot 원 evidence를 반환하라. 원 EXTERNAL_RETURN.schema.json을 바꾸지 않는다. 누락 파일은 absent와 이유를 기록한다. 원 rate/epsilon null을0으로 대체하지 않는다.

같은branch 새경로에만 non-force additive 게시하고 기존 Drive/Dropbox에 create-only 백업한다. ACK·objectID·size/hash와 실제restore를 구별한다. 도구 부재면 검증된 로컬 패키지와 blocker를 반환한다. 이 first bounded 결과에서 종료하고 다음 범위는 반환 검토 뒤에 정한다.
