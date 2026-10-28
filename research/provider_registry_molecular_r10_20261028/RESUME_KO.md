# R10 재개 진입점

현재 과학 상태는 **DAG 21/36, 조건부 이론·코드 2개 채택**이다. [HANDOFF_KO.md](HANDOFF_KO.md)와 [REPORT_KO.md](REPORT_KO.md)를 먼저 읽는다. 실제 단계별 전달 상태는 [delivery/PUBLICATION_INDEX.json](delivery/PUBLICATION_INDEX.json), 과학 allowance는 [EXECUTION_LEDGER.json](EXECUTION_LEDGER.json)을 기준으로 삼는다.

과학 채택 commit은 `a2c62aaad2396d1720a12e74774e52374baa4c33`, 41-file payload SHA-256은 `57ee9ad49afbd1a492914fadba480ed787b51e4bcefc8c0be62c31e196590fff`다. R10 primary/reference/CAS는 각 1회 사용했고 잔여 0/0/0이다. 새 세션에서 과거 검사를 재실행하거나 allowance를 초기화하지 않는다.

실제 HD reactive array·consumer·density·clock은 입력 대기다. Native9 raw 상계의 약점, saved-sample 허용오차, Wolfram 경고, 원래 R8 실패를 유지한다. 새 사용자 요청에 따라 다음 실제 입력 또는 구체적 full-A finite-block 증명·구현 의무를 선택한다. [followup/NEXT_INPUT_CONTRACT.json](followup/NEXT_INPUT_CONTRACT.json)의 후보는 아직 실행·채택하지 않았다.

연구 branch와 draft PR150, Drive·Dropbox의 단계별 게시·백업 권한은 기존 사용자 요청에 포함돼 있다. Root가 expected SHA와 force=false로 쓰기를 맡고, main merge나 다른 owner 저장소 변경은 포함하지 않는다. 새 세션에서는 현재 가능한 실행 도구를 확인하되, 과거 세션의 호스트 오류를 현재의 보편적 금지로 옮기지 않는다.
