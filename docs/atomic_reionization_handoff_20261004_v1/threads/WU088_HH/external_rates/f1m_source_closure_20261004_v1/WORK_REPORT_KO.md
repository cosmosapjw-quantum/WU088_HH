# F1M source intake 복구와 현재 coding-loop 반환

F1M 원 ZIP의 54개 payload 검증만으로 직접 SOURCE_LOCK 17개의 closure를 입증할 수 없는 공백을 고쳤다. 원 ZIP에는 F1P DELIVERY_MANIFEST.json이 없었고 나머지 16개는 size/SHA와 일치했다. F1M 원 archive와 검사 파일은 변경하지 않았다.

새 verify_f1m_intake.py는 고정한 F1M/F1P ZIP의 byte identity, CRC와 payload manifest부터 확인한다. F1M만 주면 SOURCE_CLOSURE_INCOMPLETE(exit2,16/17)를 반환한다. 검증된 F1P ZIP을 함께 주면 정확한 원 manifest member를 읽고 F1M이 지정한 9,428 bytes/SHA256=2ccecac31e88d7b1802b08a084035a309d0ff31eb2b2ce189a8bcdf91e0e625e와 대조해 직접17/17을 닫는다. arbitrary overlay나 원 bundle 덮어쓰기는 없다. 이 판정은 F1M 직접 source-lock에 한정하고 재귀적 provenance·물리 admission을 대신하지 않는다.

신규 CLI 검사 고유4개: parent 없는 미완료 거절, 정확한 parent로 closure 및 두 입력 bytes/mtime 보존, 손상 F1M 거절, 손상 F1P 거절. 최종 모두 PASS, 실패/skip0이다. 출력의 직접-source 범위 표기를 추가한 뒤 영향을 받는4개만 최종 재검증했다. 검사 횟수를8개로 합산하지 않는다. F1M의16개 unit/6개 quadrature, 과거26/30/33/40개 suites와 HH callback/적분은 이번에 재실행하지 않았다. 두 ZIP의54/59 payload 검증은 artifact 검사다. 테스트 손상 bytes는 별도 임시 transport fixture이며 scientific input에 쓰이지 않는다.

입력은 기존 인증된 Drive/Dropbox 양쪽의 ID/name/size를 확인하고, cache 부재 뒤 Dropbox에서 artifact당 한 번만 회수했다. 각 ZIP bytes/SHA를 정확히 검증했다. Dropbox input RESTORE_VERIFIED=true, Drive는 metadata만 확인해 false다. F1M/F1P 원 bytes는 content-addressed cache에서 사용한다. 회수한 parent manifest는 별도 witness다.

현재 HH 입력 HEAD=387887b92dd57c88be48c1cf1a37d099f6339562. rei 처음5f3bfe2를 읽은 뒤 도중 dc931a67cd5ed25046a96eb5deb42186d72176da(FT06)가 도착해 새 README/paired projection/NEXT/RETURN/ACK를 읽었다. F00/F02 실제 완료 반환을 follow-up 실행상태 사본에만 반영했다. 원 EXECUTION_STATE와 TASKS는 보존한다. F00 model-lock은 이제 존재한다. HH=0인 synthetic fixture, physical_admitted=false이며 이 값을 actual HH 도메인으로 채택하지 않았다. 지정 science_scenario_v1.json은 최신 dc931a67에서도404다. FT06 paired pilot projection은 full contract의 byte identity나 REI-F07 HH 적용 승인과 같지 않다. 그 연구 suite와 Rust 시험은 반복하지 않았다.

Canonical HH-F1=WAITING_ON_REI_DOMAIN, 미충족 dependency=REI-F07. 실제 temperature/density/redshift/SED/distribution/observable budget/constants/consumer commit/adapter path/domain receipt/process·threshold·thermal·binding owner/numerical tolerance의 HH 적용 결속이 필요하다. 소비자 synthetic 좌표/상수와 FT06 온도 guard를 임의 전용하지 않았다. 다음 canonical 작업은 consumer의 실제 REI-F07 receipt 게시이며, 그때 HH-F1과 확인된 HH-F2 seam을 이어간다. 이번 intake 완료를 HH-F1 전체 완료로 표시하지 않는다.

기존24/289, 미상계265 unbounded, epsilon_C/R=null, B22 OPEN_UNDETERMINED, scientific/production admission=false를 유지한다. 소비6셀/FD1/FD2 registry 및 FD2 proposal/RETURN, B22 raw057/105 claim bytes/SHA/mode/mtime/PID 문자열7개 refs를 실제 대조했고 모두 보존됐다. claim으로 process 원인을 추정하지 않았다. 원 worker/backend/source/DB/PREPARED/실패tree와 다른 repo는 변경하지 않았다.

대화 동기화 대상은 사용자 지정 https://chatgpt.com/c/6abf9e0b-74c0-83e8-8170-aaa51b03415e 이다. 현재 authenticated conversation browser 경로가 없어 직접 읽기/전달은 UNDELIVERED다. active-turn Git checkpoint와 cloud receipt로 내용을 연결하며 background 감시나 대화 확인 성공을 주장하지 않는다. 게시 직전·종료 remote identity와 실제 publication/backup ACK는 detached DELIVERY_RECEIPT가 기록한다. Output ACK+metadata tier는 restore와 별개이며 재다운로드하지 않는 output의 RESTORE_VERIFIED=false다.
