# PHYS85 연구 루프와 완료 기준

## 최종 판정: 이론·정적 구현 PASS_SCOPED, 실행 결과 NOT_VERIFIED

아래 S0 표는 시작 당시 기록이다. 최종 R/C 상태는 이 절이 우선한다. 절차를 종료하고 인계하는 것과 과학 검증을 통과하는 것은 별도 상태다. 이론은 DERIVED_SCOPED_REVIEW_PASS, 구현은 STATIC_IMPLEMENTATION_PASS_SCOPED, 실행 결과는 SCIENTIFIC_REFERENCE_NOT_VERIFIED다.

| 단계 | 실제 산출물·역할 | 최종 상태와 남은 의무 |
|---|---|---|
| R1 연구 위치·계약 | 고정 중앙 인계, actual HEAD/AGENTS, PHYS83 owner 완료, PHYS84 동결 입력·백업 대조 | COMPLETE_SCOPED. PHYS83 재실행0; PHYS84 첫 수치 검증 WAIT |
| R2 근거·재사용 | 접근 가능한51repo metadata, 관련6repo1106refs, 최근30PR와 마지막 bounded delta; 접근 가능한 대화·백업; SciSpace/LLNL/Cardall | COMPLETE_SCOPED. 모든 비공개 대화·모든 branch 내용 전수 열람 주장은 하지 않음. Exa402 보존 |
| R3 주장·전제 정렬 | supplied event, NR 공통-T 정리, 물리 supplier, consumer admission을 CONTRACT revision2에서 분리 | FROZEN. 누적 금액 예산 null, reset=false |
| R4 표현 선택 | 소속 변수 h, 같은 사건 measure, rational half-rapidity, 여섯 energy owner | COMPLETE_SCOPED. 에너지 분율만으로 thermal membership을 정하지 않음 |
| R5 구성적 유도 | normal-frame 사건 운동학, 입자수·에너지 incidence, 선택 운동에너지와 rate-slope 온도식 | DERIVED_SCOPED. 실제 단면적·율을 공급하는 정리는 아님 |
| R6 독립 검증 | fresh Astra 식·도메인 검토 후 kinetic nonnegativity·zero-rate domain·기호 정정 | PASS_SCOPED / GO_IMPLEMENT |
| R7 판별 검증 | 계획36event/6ensemble·guards·독립 four-vector oracle·symbolic witnesses를 구현하여 Wolfram 두 호출 | NOT_VERIFIED. 첫 호출 binding 실패, 수정 호출 transport 생략. 계획 수는 결과 수가 아님 |
| R8 결과 판정 | 실제 raw/receipt와 fresh C9 판정 대조 | 판정 완료: 전체 출력 부재로 reference admission 불가. PASS 조각을 완료로 승격하지 않음 |
| R9 정식 결과·코딩 연결 | 열 이름·입자 소속·frame·clock·joint weighting·supplier 의무 | SCOPED 계약 연결 완료; 실행 검증과 physical finite-T supplier OPEN |
| R10 종료·재개 | additive Draft, 단계 ACK, final 전체 복원, Codex·다음thread handoff | 전달 closure. 최종 HEAD·복원 근거는 외부 final-delivery와 PR 최종 본문 |
| C1 목표·baseline | PHYS81 kinetics·PHYS83 완료 재사용, PHYS84 prepared 보존 | COMPLETE_SCOPED. 이전 science replay0 |
| C2 식–입력–코드 | 표시 질량5개 원문 전사, exact rational 입력과 source manifest | FROZEN. 유리수 정확성은 physical mass uncertainty를 제거하지 않음 |
| C3 설계 | exact WL reference, 독립 matrix boost·incidence oracle | FROZEN. finite cases는 continuum certificate가 아님 |
| C4 DAG·자원 | PHYS84 reserve1.5GiB+job0.5GiB lease WAIT; 별도 Wolfram60초/내부55초 cap | 기준 불변. local numerical child0, other process termination0; cloud scheduler UNOBSERVED |
| C5 구현 | lower-tier 요청 gpt-6.1-sol/high, 원본9파일 동결, binding-only repair 별도 보존 | STATIC_IMPLEMENTATION_PASS_SCOPED. 관측 backend identity UNOBSERVED |
| C6 구현 검증 | guard·four-vector·에너지·입자수·covariance verifier를 실제 두 호출에 포함 | 런타임 미확인. attempt01 complete rows0; attempt02 complete row/assertion/guard counts=null |
| C7 과학 검증 | supplied-event reference·NR witnesses의 완전한 raw 요구 | NOT_VERIFIED. valid complete application0, physical nuclear rate0, stopping0, ODE0 |
| C8 재현성·identity | exact request/raw/receipt 보존, source byte 불변 확인, evidence identity | 증거 보존 완료. completed science identity=null; evidence identity는 성공 인증이 아님 |
| C9 독립 검토 | 구현자와 다른 fresh Astra가 code/diff/raw 검토 | 검토 완료: static PASS_SCOPED / scientific reference NOT_VERIFIED. 남은 repair call0 |
| C10 판정·인계 | 실패·cap·null counts·열린 의무 보존 | audit closure. 새 실행은 output transport 설계·검토와 별도 budget/admission 갱신 후 판단 |

Wolfram 평가 호출2 = entrypoint failure1 + transport-unverified1이다. 유효한 완료 reference application은0이고, 두 번째 호출의 실제 내부 전체 계산 수는 미관측이다. 누락 결과를0 residual로 채우거나 JSON을 재구성하지 않았다. 현재 계약의 추가 호출 cap0에서 종료한다.

단계별 commit/hash/ACK는 delivery/PUBLICATION_HISTORY.json 및 delivery/S*_BACKUP_ACK.json, 최종 전체 다운로드·복원은 외부 PHYS85_FINAL_DELIVERY_20261024.json을 본다. upload ACK와 실제 복원은 별개다. 자기 자신의 최종 commit/ZIP hash를 Git 문서 안에 넣는 순환 구조를 만들지 않는다. HH_R10=OFF; production admission NOT_ISSUED.

## S0 시작 당시 기록 — 아래 PENDING/NOT_RUN은 역사적 상태

현재 user가 지정한 physmath-research-loop built-in1.0.0의 R1–R10/C1–C10을 적용한다. 단계별 checkpoint가 모든 물리 목표의 완료를 뜻하지 않는다. 아래는 S0의 실제 상태이며 최종 상태는 STAGE_STATUS와 FINAL_REPORT 및 외부 final-delivery에서 갱신한다.

| 단계 | 실제 산출물·역할 | S0 상태 / 다음 action |
|---|---|---|
|R1 연구 위치·계약|51repo/6repo1106refs·owner·백업·접근 가능한 대화 조사; 현재HEAD에서 부모복구|COMPLETE_SCOPED; PHYS83재실행0|
|R2 근거·재사용|PHYS81 kinetics/663assertions, PHYS83/84, REI/REC/CR/HE/BASS 최신 완료·예약 분리; SciSpace/LLNL/Cardall|COMPLETE_SCOPED; Exa402보존|
|R3 주장·전제 정렬|정확 사건/NR Maxwellian/실제supplier/consumer 네 범위와 null budget|동결 계약revision2|
|R4 가설·표현 탐색|ζ 대신 binary count owner h; 같은 event measure; rational half-rapidity|표현 선택 완료|
|R5 구성적 유도|normal-frame six-column ledger, selected kinetic removal, rate-slope Tdot|유도 완료|
|R6 독립 검증|fresh Astra 직접 식 검토; 세 작은 domain/기호 수정 반영|PASS_SCOPED / GO_IMPLEMENT|
|R7 판별 검증|non-cold36events,6joint ensembles, wrong-owner/route/weight controls, formal σ witnesses|계획동결, 실행NOT_RUN|
|R8 결과 판정|계약→코드→raw Wolfram evidence→독립 판정|PENDING|
|R9 정식 결과·코딩 연결|source supplier가 받을 event incidence/energy/clock schema|구현중; physical supplier OPEN|
|R10 종료·재개|expectedSHA Draft, 단계 ACK·최종전체복원·다음threadhandoff|게시/백업 예정|
|C1 목표·baseline|PHYS84 코드재사용; PHYS85는 별도핵소유권 의무|baseline동결|
|C2 식–데이터–코드|질량·K·boost·μ·owner·route·weights exact rational leaves|FROZEN_INPUTS 작성|
|C3 수치 설계|exact rational WL reference; independentfour-vector oracle|동결; 물리오차나 CI아님|
|C4 실행 DAG·자원|PHYS84 기존sharedlease WAIT; 별도 user-authorized cloud symbolic60s cap, noParallel|지방 숫자실행 기준불변|
|C5 구현|lower-tier agent; 요청모델과 관측UNOBSERVED 구분|IN_PROGRESS|
|C6 구현 검증|guard·incidence·route·identity binding·actual residual|NOT_RUN|
|C7 과학 검증|새 conditional supplied-event output/NR theorem witness|NOT_RUN; physicalrate0|
|C8 수치·재현성|정확 유리수 출력·고정 toolcode·rawreceipt·read-only재사용|실행후 identity동결; 반복실행금지|
|C9 독립 검토|fresh Astra 코드/raw검토, one targeted repair if concretefailure|PENDING|
|C10 판정·인계|claim gate와 source/consumerOPEN 유지; finalhandoff|PENDING|

Astra는 문제·동결 계약·판정·독립 검토를 맡고, 하위 tier는 구현·기계적 전사·허용된 실행·직렬화를 맡는다. 독립 검토는 구현자가 수행하지 않는다. 과거 runtime 버전 차이만으로 완료 identity를 재실행하지 않는다.

새 과학 실행의 분류는 physical nuclear rate/ODE0, conditional exact reference application(예정1), verifier controls, symbolic identities, metadata/checksum, provider delivery를 각각 구분한다. R/C 숫자 완료 개수로 전체 물리 목표의 비율을 만들지 않는다.
