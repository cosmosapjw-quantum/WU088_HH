# W1 완료 checkpoint에서 이어가기

현재 base HEAD는 `957714bff2d6c97cc5b3541baa3f2f83fdfa3182`이며 새 END_HEAD/TREE는 별도 `WU088_HH_W1_PARALLEL_DELIVERY_RECEIPT_20261002.json`에서 확인한다. 같은 연구 브랜치를 유지한다.

1. 배포 영수증과 최신 remote HEAD/tree를 먼저 대조한다. 새 결과를 과거 SHA로 reset하지 않는다.
2. `runtime/W1_CAMPAIGN/COLLECTED.json`, `EXECUTION_LEDGER.json`, `review/ACTUAL_CAMPAIGN_REVIEW.json`, `STAGE_DELTA.json`을 읽는다. primitive 0 W1의 16타일은 완료됐다. 기존 tile0 포함 어느 타일도 자동 재실행하지 않는다.
3. Frozen107·binary/backend·plan pins와 runner SHA `37f2b99abb6d2f6951243c88feccfb16225cc109eb70748221c905a8c8d9fe29`를 보존한다. 새 host는 frozen driver의 실행 경계만 대체한다. MPI adapter는 아직 이 range solver에 연결·실측되지 않았다.
4. 완료 캠페인의 잔존 claim 6개는 bytes를 보존한 제한적 reconciliation과 strict readback으로 처리한다. B22 원인은 미확정이다. 어떤 다른 stale claim도 PID만 보고 지우거나 해당 작업을 다시 배정하면 안 된다. worker/native 종료 근거와 원본 receipt부터 확인한다.
5. 다음 계산 설계는 W1 밖의 오차다. 기존 W3는 physical `[1/256,2^192]²`, log2 `[-8,192]²`다. 현재 step3을 단순 확대하면 4,489타일이다. 16타일 collector 한도를 수정하는 것만으로 실행하지 말고, 비균등 분할/analytic grouping의 정확 coverage·오차 배분·호출비용을 먼저 설계한다. 무한 endpoint scan을 반복하지 않는다.
6. 실제 모든 primitive, global endpoint 단일 적용, source-prescribed contraction·정규화·phase·post-integral conjugation, D_col/D_row와 epsilon, represented model-gap 및 frozen decision은 남아 있다. W1 성공을 scientific/production admission으로 승격하지 않는다.
7. NCP에 실제 연결되는 접근 경로를 확보한 뒤 quota/NUMA/affinity/메모리·compiler·backend를 확인하고 2-rank→64-core 범위를 검증한다. 이 환경에서 관측한 것은 quota8/8GiB·3개 direct process 병렬 실행이다. OpenMPI의 root 거절을 우회하지 않는다.

현재 DB는 이전 wide-domain DB의 모든 표·행을 유지하면서 `w1_*` 표를 추가한다. 실제 새 실행은15회, 이전 결과 재사용은1회다. DB 행·synthetic·nested integration_calls를 실행 수로 세지 않는다. 현재 SQL dump는 새 SQLite 논리 복원용이며, byte-exact 이전 DB 재구축은 이전 배포 영수증에 연결된 파일을 사용한다. backend tar도 기존 백업을 재사용한다.
