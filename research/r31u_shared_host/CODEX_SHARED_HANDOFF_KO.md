# R31U: 실행 중인 세 Codex 세션 공통 추가 안내

현재 run을 중단/재시작하지 않는다. 기존 exactly-once,budget,deadline,scientific thresholds,stop contract를 이 안내로 덮지 않는다.

1. 자기 repo URL/HEAD/tree/workroot/runID,supervisor PID+starttime,own descendants,cgroup,actual affinity를 read-only로 확인한다. 다른 세션의 프로세스를 kill/resize/migrate하지 않는다. 과거 evidence PID를 현재 PID로 재사용하지 않는다.
2. bass_cr F1-R2가 진행 중이면60worker/3600s/4000KRW/1회실행/no-auto-retry-resume 계약을 보존한다.12worker로 줄이거나 deadline을 늘리지 않는다. 다른 세션은 새로운 대형 pool을 시작하지 않고 자기 정상checkpoint 경계에서 다음dispatch만 보류한다. 이미 완료된 결과를 지우지 않는다.
3. 각 session의 whitelist inventory를 자기 repo의 새 evidence/runID에 push한다. job_identity,execution_authorization,protected_run,requested_CPU,memory_peak_observed,cgroup_path,actual_affinity,own_descendants,next_expensive_stage를 기록한다. credentials/full environment/secret command line은 제외한다. live mapping이 없으면 unknown/null이다.
4. session 공통 cpu.stat을 사용했다면 shared accounting으로 표시한다. contaminated benchmark와 numerical result validity를 구분한다. numerical exactness를 확인한 자료까지 폐기하지 않는다.
5. HH를 coordinator 후보로 해서 단일 host resource plan을 제안한다. 타repo 승인권한을 만들지 않는다. 현재 protectedrun이 끝난 뒤 짧은 exclusive M3B창을 제안한다. 다른 세션은 UI/문서작업을 계속하되 heavy compile/native/압축을 그 창과 겹치지 않는다.
6. future HH32/HE16/CR12/control4는 아직 proposal이다. 현재CR60one-shot에 적용하지 않는다. 실제 allocation-aware runner,measured memory headroom,job-local cgroup 계측을 검증하고 승인받기 전에는 배포하지 않는다. CPU mask만으로 공유L3/메모리대역 interference가 사라진다고 하지 않는다.
7. HH source에서 hard64 saved-probe gate와 실제job budget을 분리하는 additive adapter의 짧은 설계를 먼저 제출한다. 기존 persistent spawn pool은 재사용한다. 비교 histogram은12pair×11=132 performance tasks로 고정한다. 기존M3A를 모두재실행하지 않고 co-finalist의 필요한 부분만 새계획으로 비교한다.
8. 이미 계산한 expected reference를 source/model/grid/build/pair/precision/rounding identity로 저장하는 cache를 설계한다. correctness preparation에서만 reuse하고 실제 throughput 측정의 H0/native output을 memoize하지 않는다. raw x87 padding hashes를 numerical equality로 쓰지 않는다.
9. R31U의 actual metric defect와 Hermite candidate failure를 읽는다. 새 phase/envelope/connection-aware 방법은 별도 연구분기다. raw source를 symmetrize하거나 independent dotO를 D+D†로 대체하지 않는다. H/G 원threshold와 minimum width는 보존한다.
10. M4async를 건너뛰는 synchronous-safe discriminator는 아직 제안이다. 이 안내로z1/M5/trajectory/production을 실행하지 않는다. systemd service 설치/start,cgroup live migration,새VM,auto retry,forcepush,PR merge는 하지 않는다.

반환: 각 session branch/commit/tree/evidencepath,현재 확인된execution scope,resource request,measured use,protectedrun상태,다음 최소조치. 변경제안은 proposal로,미검증 liveallocation은null로 둔다. 결과를 VM안에만 두지 말고 작은nonsecret JSON을 GitHub로push한다.
