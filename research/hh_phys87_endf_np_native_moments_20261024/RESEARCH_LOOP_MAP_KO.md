# PHYS87 이론·코딩 연구 루프 대응표

이 파일의 R1–R10은 연구 스킬의 단계 번호다. 프로젝트의 `HH_R10=OFF`와 다른 이름공간이다. 단계마다 같은 과학 실행을 새 실행으로 다시 세지 않는다.

## 이론 루프

| 단계 | 수행 내용과 근거 | S1 이전 상태 |
|---|---|---|
| R1 연구 위치 | actual PHYS86 parent, 중앙 원 계약·AGENTS, 현재 refs와 공유 자원 확인 | COMPLETE_SCOPED |
| R2 근거 재사용 | 51repo/2234refs metadata; PHYS83/85/86 완료 identity; 최신6repo 결과·백업; `SURVEY_SYNTHESIS_KO.md` | COMPLETE_SCOPED |
| R3 주장·전제 | native atomic AWR/QI, 공통 T·등방 Jüttner, finite source window; bare remap 별도 | COMPLETE_SCOPED |
| R4 표현 선택 | GNDS checksum mismatch 제외; ENDF 원 보간·Legendre 법칙; exact coefficient cancellation | COMPLETE_SCOPED |
| R5 구성적 유도 | COM angular rotation, boost marginal, rate·joint moments·caloric ownership; `theory/NATIVE_FINITE_T_MOMENTS_KO.md` | COMPLETE_SCOPED |
| R6 독립 검증 | 독립 이론 검토 PASS_SCOPED; Wolfram formal residual12/12=0; pre-exec review가 현재 source hashes 재결속 | COMPLETE_SCOPED |
| R7 판별 계산 | source153knots, 4T GL16/32, 18angular cases, 16owner rows, FD와 독립 reference | NOT_RUN |
| R8 결과 판정 | frozen tolerances와 실제 raw evidence를 대조한 root 판정 | PENDING_R7 |
| R9 코딩 연결 | 같은 원전·프레임·단위·사건 measure를 구현 계약으로 연결 | DERIVED_SCOPED |
| R10 종료·재개 | immutable outputs, no-replay resume, 실제 게시·양쪽 복원과 다음 thread 인계 | PENDING_DELIVERY |

## 코딩 루프

| 단계 | 구현 의무와 근거 | S1 이전 상태 |
|---|---|---|
| C1 목표·baseline | 부모 완료 결과 재사용; 새 source-native child와 단일 bounded run 정의 | COMPLETE_SCOPED |
| C2 식–데이터–코드 | raw MF3/MF6 parser, native interpolation, kinematics, reaction-selected moments | FROZEN_STATIC_REVIEW_PASS |
| C3 수치 설계 | positive native-cell GL16/32, stable scaled Bessel, centered variances, independent adaptive reference | FROZEN_PLAN |
| C4 실행 DAG·예산 | primary12CPU/60wall, reference20/60, figures8/30; 1worker/thread, reserve1.5+job0.5GiB | FROZEN_PLAN_FRESH_GATE_REQUIRED |
| C5 구현 | `source/`와 독립 `verification/independent_reference.py`; requested lower-tier executor/backend UNOBSERVED | FROZEN_STATIC_REVIEW_PASS |
| C6 구현 검증 | exact source binding, 24 negative controls, count/radiation ownership, raw acceptance checks | NOT_RUN |
| C7 과학 검증 | source-native rate/energy/temperature relation 및 same-event closure | NOT_RUN |
| C8 수치·재현성 | GL16/32·FD·independent kve/quad, saved result resume without callback | NOT_RUN |
| C9 독립 검토 | 별도 Astra 정적 검토 후 실제 raw·diff 검토; 한정 판정 | PASS_SCOPED_PREEXEC;RAW_PENDING |
| C10 판정·전달 | expected-SHA Draft, S0/S1/S2 ACK, FINAL 양쪽 whole GET/restore, Codex·다음-thread handoff | PENDING_DELIVERY |

## 분리한 축과 종료 조건

유도, 코드, 검증, 실제 과학 실행, Git 게시, provider ACK/복원, DAG gate는 각각 기록한다. 최신 개별 상태는 `STAGE_PROGRESS.json`, 실행 수와 누적 실패·예산은 `EXECUTION_LEDGER.json`, dependency와 채택 범위는 `DAG_OVERLAY.json`에 둔다.

20개 의무의 완료는 이 PHYS87 한정 루프의 완료다. 전 프로젝트 물리 완료율은 정의하지 않아 null이다. `NUCLEAR_PHYSICAL_FINITE_T_EVENT_SUPPLIER` 부모는 atomic-to-bare remap, full support/uncertainty, named consumer가 남는 동안 PARTIAL이다. 실행 허용과 과학 채택은 별도이며 실제 rates/stopping/ODE 활성화는0이다.
