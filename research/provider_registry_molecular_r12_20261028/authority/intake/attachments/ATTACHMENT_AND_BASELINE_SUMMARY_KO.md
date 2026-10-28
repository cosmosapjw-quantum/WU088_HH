# R12 시작 조사: 첨부 동일성과 R11 로컬 기준

**명시된 첨부 20개는 이전 R10 조사 입력과 파일명·크기·SHA-256가 모두 같다. R11의 과학 payload 50개, 동결 파일 18개와 상속 입력 7개도 모두 로컬 원문과 일치한다. 복구가 필요한 기준 파일은 0개다.** 이 조사는 바이트·메타데이터 가용성과 채택 범위 확인이며 완료한 과학 검증의 재실행이 아니다.

## 1. 첨부 범위와 조사 재사용

현재 지정 경로는 `/workspace/scratch/d813e058ed8f/project_sources/`이고, 최초 `rg --files` 목록의 명시된 20개를 확인했다. SHA·크기 대조의 최종 시각은 **2026-10-28 13:40:07.843389–13:40:08.153233 KST**다. UTC는 04:40:07.843389–04:40:08.153233이다.

| 항목 | 결과 |
|---|---:|
| 실제 읽어 SHA-256를 계산한 첨부 | 20 |
| 총 첨부 바이트 | 435,180,795 |
| 기존 이름·크기·SHA-256와 동시 일치 | 20/20 |
| 바뀐 첨부 또는 새 첨부 | 0 |
| 기존 목록에서 사라진 첨부 | 0 |
| 이번 새 archive 해제·OCR·본문 재조사 | 0 |

대조 기준은 R10 FINAL source에 보존된 `research/provider_registry_molecular_r10_20261028/authority/backup_literature/ATTACHMENT_IDENTITY.json`이다. 기준 파일은 7,307 bytes, SHA-256 `cb05bbb43c60d102bffd93a28db89f04818dbd0ce5f8152783b174301bb4af1b`이다. 이 기록은 R9 FINAL `7a1430afb21736804286ca5284e0d8243016f2f4`에 들어 있는 R7 `CURRENT_PROJECT_ATTACHMENTS.json`의 Git blob `9cb2c9ad29aac85d4a0bac49987b7789c9eae8ab`와 연결된다.

따라서 R10 `authority/backup_literature/INTAKE_SUMMARY_KO.md`에 보존된 **archive member metadata 60,882개와 문헌 PDF 텍스트 15개 조사**를 재사용한다. 이는 이번에 그만큼의 본문을 새로 읽었다는 뜻이 아니다. `20-report-1-.pdf`를 포함해 첨부 원문이 모두 같으므로 변경·신규 본문 조사 대상은 없다. 각 파일의 현재 크기와 SHA는 `ATTACHMENT_IDENTITY.json`에 있다.

이 범위의 첨부 변화로부터 새 actual HD reactive array나 named WU physical consumer/density/clock 입력을 추가로 식별하지 않았다. 이전 `INPUT_PENDING` 판정을 첨부 범위에서 유지한다. 다른 저장소·백업의 이번 전수 조사는 별도 레인의 근거로 종합해야 하며, 이 결과로 전역 자료 부재를 주장하지 않는다.

## 2. R11 로컬 기준의 가용성

최종 로컬 기준 검사는 **2026-10-28 13:40:08.153786–13:40:08.175300 KST**에 수행했다. `AGENTS.md` 최신 R11 entry와 아래 종료 문서가 모두 존재한다.

- `REPORT_KO.md`, `HANDOFF_KO.md`, `SCIENTIFIC_ADMISSION.json`, `SCIENTIFIC_PAYLOAD_MANIFEST.json`, `CONTRACT.json`.
- `DAG.json`, `WORKFLOW_RECORD.json`, `EXECUTION_LEDGER.json`.
- `reviews/C9_FINAL_REVIEW.json`, `reviews/ADMISSION_DELTA_REVIEW.json`.
- `authority/closeout_delta/CLOSEOUT_SUMMARY_KO.md`, `followup/NEXT_INPUT_CONTRACT.json`, `delivery/PUBLICATION_INDEX.json`.

| 동일성 검사 | 결과 | 의미 |
|---|---:|---|
| AGENTS와 필수 R11 문서 | 14/14 존재 | 재개 기준을 로컬에서 읽을 수 있음 |
| R11 scientific payload | 50/50 SHA·size 일치 | 과학 S09 채택 원문 재사용 가능 |
| Canonical payload digest | 일치 | `e7e345e26142522394bc1e7b3eeccfaacf5347cf4f802bcfd344f9fbbcbfdae0` |
| R11 preexecution freeze | 18/18 SHA·size 일치 | 원래 실행 입력·코드 동결 상태 유지 |
| R11 INPUT_IDENTITY 상속 입력 | 7/7 SHA·size 일치 | R6/R7/R9/R10 저장 근거 로컬 이용 가능 |
| missing/mismatched 기준 파일 | 0 | 새 source 복구 불필요 |

상속 입력은 R10 DAG·primary, R7 exact input·primary·reference, R9 primary, R6 primary다. R11의 실제 primary/reference 출력과 생산·독립 코드도 위 payload와 freeze의 확인 대상이다. 이 조사에서 repository source, AGENTS, 기존 ledger와 payload는 수정하지 않았다.

R11 scientific S09는 `e1db71bade6ff94959a74d8f297ad2568c247056`, tree는 `9c4108ffa1fc8a4c4489bd6be19a93183cc25133`이다. C9는 `PASS_SCOPED_FINAL_C9`, SHA-256 `538bc823b6aabd776abe7b2ee52a8d1c3dedb52c47786f6f31dd3d1badbf2e94`, 열린 중대 지적 0이다. Admission delta도 `PASS_SCOPED_ADMISSION_METADATA_DELTA`, 열린 중대 지적 0이다. 이 값들은 기존 저장 판정을 읽은 것이며 새 C9 pass가 아니다.

`PUBLICATION_INDEX.json`에는 실제 단계 이중 백업 10/10이 보존되어 있다. **FINAL 자신의 receipt는 source 밖 PR150 및 종료 응답의 권위**다. 이 로컬 조사 레인은 외부 FINAL receipt를 새로 조회하지 않았으며, 이를 source 내부에 소급 삽입하거나 로컬 manifest만으로 FINAL 원격 동일성을 추정하지 않는다.

## 3. DAG·자원·물리 상태 보존

| 기준 | 완료/전체 | 상속 객체 비교 |
|---|---:|---|
| R9 | 19/34 | 원래 기준 |
| R10 | 21/36 | R9의 34개 객체와 정확히 같음 |
| R11 | 23/38 | R10의 36개 객체와 정확히 같음 |

R11 workflow는 20/20이다. Primary/reference/CAS remaining은 0/0/0이며 R10/R9/R8/R7/R6/PHYS91의 allowance도 원래 0 상태다. Global remaining과 full historical CPU는 `null`이다. 현재 NEXT_INPUT의 후속 제안 allowance 역시 0이다. 이번 조사는 새 실행 계약을 만들거나 예산을 할당하지 않았다.

Actual HD reactive array와 named physical consumer/density/clock은 `INPUT_PENDING`, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`, central/physical delta=0을 보존한다. Native `v=UNSPECIFIED`, `MISSING_NOT_ZERO`, TIQM/SQM의 구별도 같다.

R8 original 726/727 PASS +1 FAIL과 별도 exact phi 24/24, R10 최초 후처리 ID 실패·DOC01/META02, R11 F01/F02와 첫 PNG 절단·S08 temporary→S09 삭제 기록은 원래 자료에 그대로 있다. 기존 과학·ODE·CAS·독립 reference 재실행은 0회다.

## 4. 다음 연구에 전달할 경계

R11의 정확한 재사용 가능 범위와 비정렬 clock 제한은 `R11_REUSE_BOUNDARY_KO.md`에 정리했다. 이번 첨부·로컬 기준 조사만으로 실제 물리 입력이 새로 공급되었다고 볼 근거는 없다. Root가 다른 전수 조사 결과와 합친 뒤 실제 입력 결속 여부 또는 별도 비정렬 forcing 단위의 유한 proof/code/resource 계약을 결정한다. R12 구현은 아직 작성하지 않았다.

근거: `ATTACHMENT_IDENTITY.json`, `R11_LOCAL_AVAILABILITY.json`, R10 `authority/backup_literature/INTAKE_SUMMARY_KO.md`, R11 `CONTRACT.json`, `SCIENTIFIC_ADMISSION.json`, `followup/NEXT_INPUT_CONTRACT.json` 및 위 종료 문서. 재생산용 `verify_current_inputs.py`는 파일 해시·JSON·객체 비교만 수행한다.
