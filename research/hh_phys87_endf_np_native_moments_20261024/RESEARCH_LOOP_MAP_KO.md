# PHYS87 이론·코딩 연구 루프 대응표 — S2 준비

**이 PHYS87 한정 루프의18/20 의무가 COMPLETE_SCOPED이며 R10/C10 전달은 IN_PROGRESS다.** 전 프로젝트 물리 완료율은null이다. Root가 실제 독립 C9 PASS_SCOPED를 채택했고 scientific scope는 `NUMERICALLY_CHECKED_SCOPED_SOURCE_NATIVE_FINITE_WINDOW`다. `NUCLEAR_PHYSICAL_FINITE_T_EVENT_SUPPLIER` 부모는PARTIAL, 다음 atomic-to-bare remap은OPEN이다.

R1–R10은 workflow 단계이며 `HH_R10=OFF`와 다른 이름공간이다. 같은 과학 campaign을 단계마다 새 실행으로 세지 않는다.

| 단계 | 실제 수행·남은 의무 | 근거 | 현재 상태 |
|---|---|---|---|
| R1 연구 위치·계약 | PHYS86 exact parent/현재 authority·source-native child 계약 | `CONTRACT.json; SURVEY_SYNTHESIS_KO.md` | COMPLETE_SCOPED |
| R2 근거·재사용 | 51repo/2234refs metadata 및 PHYS83/85/86 완료 identity 재사용 | `SURVEY_SYNTHESIS_KO.md; source_data/` | COMPLETE_SCOPED |
| R3 주장·전제 정렬 | Atomic AWR/QI, 공통-T·등방 Jüttner·finite source window와 bare remap 분리 | `CONTRACT.json; theory/` | COMPLETE_SCOPED |
| R4 가설·표현 탐색 | GNDS checksum failure 보존; 원 ENDF 보간/각법칙과 exact coefficient cancellation 선택 | `source_data/INTAKE_FAILURE_LEDGER.json; implementation/` | COMPLETE_SCOPED |
| R5 구성적 유도 | COM rotation·boost marginal·rate·joint moments·caloric owner 유도 | `theory/NATIVE_FINITE_T_MOMENTS_KO.md` | COMPLETE_SCOPED |
| R6 독립 검증 | 독립 이론 검토 및 Wolfram12/12 exact zero; 실제 raw C9 재결속 | `reviews/THEORY_REVIEW.json; theory/WOLFRAM_RESULT.json` | COMPLETE_SCOPED |
| R7 판별 검증 | Primary12integrals=8full+4FD,18angular,16owner 및 독립 kve/quad reference | `results/primary001/RESULT.json; INDEPENDENT_REFERENCE.json` | COMPLETE_SCOPED |
| R8 결과 판정 | Root가 독립 C9 PASS_SCOPED와 한정 numerical claim 채택 | `reviews/INDEPENDENT_REVIEW.json` | COMPLETE_SCOPED |
| R9 정식 결과·코딩 연결 | 같은 원전/프레임/단위/measure의 JSON·CSV supplier 및 소비자 경계 | `implementation/README.md; results/primary001/OWNER_ROWS.csv` | COMPLETE_SCOPED |
| R10 종료·재개 | 완료 결과·resume·S0/S1 ACK 보존; S2/FINAL 게시·복원·handoff 진행 | `results/RESUME_OBSERVATION.json; delivery/S0_BACKUP_ACK.json; S1_BACKUP_ACK.json` | IN_PROGRESS |
| C1 목표·baseline | 동결 source/input/code identity 및 새 단일 bounded campaign | `CONTRACT.json; implementation/PRIMARY_IDENTITY.json` | COMPLETE_SCOPED |
| C2 식–데이터–코드 | MF3/MF6 parser,153 source rows, native interpolation, common moment 경로 | `source/native_moments.py; verification/independent_reference.py` | COMPLETE_SCOPED |
| C3 수치 설계 | Positive152nativecells GL16/32, stable6term Bessel, centered variances, 독립 adaptive reference | `theory/; implementation/README.md` | COMPLETE_SCOPED |
| C4 실행 DAG·자원 | Fresh pinned lease 매 child,CPU0/8,1worker/thread,reserve1.5+job0.5GiB | `results/primary001_lease.json; reference001_lease.json; figures001_lease.json` | COMPLETE_SCOPED |
| C5 구현 | Frozen source·runner·read-only resume·실제 prelaunch admission·saved-only plot | `implementation/FROZEN_IMPLEMENTATION_MANIFEST.json; reviews/CODE_REVIEW_PREEXEC.json` | COMPLETE_SCOPED |
| C6 구현 검증 | 147/147 assertions,그 안의24guards,energy/count/radiation와resumeSKIP | `results/primary001/RESULT.json; RESUME_OBSERVATION.json` | COMPLETE_SCOPED |
| C7 과학 검증 | 153exactpositiveknots/152convexcells,4reference fields+closure 및 frozen residuals | `results/primary001/POSITIVITY_WITNESS.json; reviews/INDEPENDENT_REVIEW.json` | COMPLETE_SCOPED |
| C8 수치·재현성 | GL/FD/independent raw,source612field,immutable manifest,resume0callback,2PNG+2PDF | `results/SAVED_RESULT_SUMMARY.json; primary001/OUTPUT_MANIFEST.json` | COMPLETE_SCOPED |
| C9 독립 검토 | Fresh Astra actual source/code/raw/PNG 검토 PASS_SCOPED,open blocking0 | `reviews/INDEPENDENT_REVIEW.json` | COMPLETE_SCOPED |
| C10 판정·인계 | S0/S1 실제 게시+dualACK;S2 준비 및 FINAL 실제 양쪽 복원/외부JSON 인계 진행 | `delivery/S0_BACKUP_ACK.json; S1_BACKUP_ACK.json; results/EXECUTION_LEDGER_FINAL_APPEND.json` | IN_PROGRESS |

## 분리한 실제 축

| 축 | 실제 상태 |
|---|---|
| 유도 | 이론·독립 검토 PASS_SCOPED; cloud formal residual12/12=0 |
| 코드 | 동결 identity `bc8a07546cab87dc79de5efee1e0d1917f7e88e851cdd8d5e7856f50f8c1c53d`; 원본 shared gate byte 보존 |
| 검증 | Primary147/147, 별도 exact153knots/152cells, independent4fields+closure, actual PNG inspection; evidence categories를 합산하지 않음 |
| 실제 실행 | Local3children/3success/0failure/autoRetry0; primary1/reference1/saved-figure1; resume1SKIP(callback0,rewrite0) |
| 실제 비용 | Outer child CPU4.364383s, launch-inclusive child wall4.369048669001131s; coordinator CPU 별도; 모든 own lease release3 |
| S0 게시/백업 | `b4e606c433bc0d7969227635b62f33e67a56c705`; 양쪽 actual ACK/metadata, FINAL whole restore와 별도 |
| S1 게시/백업 | `94d3b35bb66df184cf370035f498effbb4534cc6`; 양쪽 actual ACK/metadata, FINAL whole restore와 별도 |
| S2 게시/백업 | `PREPARED_PENDING_EXPECTED_SHA_PUSH`; 실제 push/ACK 미완료 |
| FINAL 전달 | Actual dual whole GET/SHA/CRC/payload/Git/extraction 및 externalJSON dual raw readback 완료를 주장하지 않음 |
| DAG | Root-adopted scoped child 결과만 기록; 부모PARTIAL/atomic-to-bareOPEN; 이 갱신은 DAG 파일을 수정하지 않음 |

## 누적 예산과 보존

새 Wolfram1회는 이전 PHYS85/86의4회와 분리하고 lineage evaluator count5를 유지한다. 이전 추가 allowance0이며 money/spend/remaining은UNKNOWN/null, reset=false다. Local child의 per-child caps는primary12CPU/60wall,reference20/60,figures8/30이며 실제1worker/thread, reserve1.5+job0.5GiB를 유지했다. Cap 합40CPU/150wall은 이미 동결된 세 개별 할당의 합으로 새 global budget이 아니다. Old replay/새ODE/stopping/network activation은0이다. 더 수행할 child는 승인되지 않았다.

## 과거 preexecution 기록

S1 이전 NOT_RUN/zero-child/preexec gate 상태는 S1 commit의 원래 세 파일과 EXECUTION_LEDGER의 historical snapshot/preexecution에 보존했다. 현재 결과를 기록하면서 과거 상태를 실패나 완료로 소급 변경하지 않았다. 현재 actual evidence는 results/SAVED_RESULT_SUMMARY.json, EXECUTION_LEDGER_FINAL_APPEND.json과 개별 raw/lease/figure 영수증을 따른다. `.mpl_config/**`는 runtime cache이고 publication 대상에서 제외한다.

Source-window 밖의 단면적·tail, source covariance/angular uncertainty/physical CI, neutral-population/charge-state validity, named consumer/thermal-fast activation, stopping·photon feedback·coupled history 및 production admission은 남아 있다. HH_R10=OFF, production NOT_ISSUED.
