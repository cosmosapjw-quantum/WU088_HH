# R14 백업·대화·첨부 census

기준은 R13 FINAL `0e6282010665bc9075e073cfd144c226d29e449b`, 과학 DAG **27/42**다. 이번 census의 과학 채택 증분은 **0**이다. 실제 provider 조회 구간은 **2026-10-28T09:03:44.451Z–2026-10-28T09:10:52.281Z**이며 종료 시각은 **2026-10-28 18:10:52.281 KST**다. 목록 조회는 원자적 snapshot이 아니다.

## 확인 결과

| 범위 | 실제 현재 목록 | 종료·증분 |
|---|---:|---|
| Drive 지정 WU 14 roots와 후손 | 167 folder responses, 1,246 unique items / 1,093 files / 153 nested folders | queue 0, capped 0, errors 0 |
| Drive 동일 WU scope의 R13 대비 변화 | 새 ID 11, 제거 0, 기존 안정 metadata 변경 0 | 새 파일은 R13 S01–S10 및 FINAL |
| Drive 동일 이름 document filter | 100+98=198 | terminal; 별도 literal query 162와 비교해 삭제라고 해석하지 않음 |
| Dropbox root | 526 entries, 이 중 folder/mount 77 | terminal |
| Dropbox dossiers 전체 recursive | 600×8+531=5,331 rows | terminal; R13 immediate 3,509와 범위가 달라 산술 차이를 증분으로 삼지 않음 |
| Dropbox 동일 WU roots | 1,132 unique items / 1,006 files | 새 ID 11, 제거 0, 기존 안정 metadata 변경 0 |
| Dropbox BASS_BACKUPS / bianchi / PHYS69 | 224 / 39 / 1 | 모두 terminal; BASS_BACKUPS 새 ID 14 |
| R11/R12/reconciliation/R13 ZIP 교차 metadata | 11+11+1+11=34 | 양 provider 이름·크기 34/34; R13 기존 receipt ID·크기 11/11 |

이번 비교는 실제 목록 metadata와 기존 R13 upload receipt를 결속한 결과다. 새 provider ACK는 **0**이고 archive original GET은 **0**이다. 기존 local CRC/member-SHA와 과거 upload ACK를 현재 다운로드 검증으로 바꾸지 않았다.

## 실제 바뀐 연구 문맥

BASS_BACKUPS에서 새로 관측한 `BASS_B3H_ANCHORED_LAYER_FINAL_HANDOFF_20261028.md`의 tool-returned 전문을 실제 읽었다. 이 handoff는 `cosmosapjw-quantum/bass`, branch `research/bass-b3h-anchor-defect-20261028`, draft PR224, source `97a8c810e6e22c690c9e148b2bcc8313ca143d2e`를 지목한다. source가 기록한 진행은 **18/20**, 독립 저자 R6/C9는 **NOT_RUN**이고 원래 DAG28/88의 증분은 0이다.

source가 보고한 변화는 같은 `Q=q+exp(-B*tau)z` 재구성에서 anchor envelope를 좁혀 whole-cell count-defect 상한을 약 `1.5927768e-26`에서 `6.7265120e-31 m^-3`로 낮춘 것이다. 약23679배라는 값은 **상한 조임 비율**이며 관측 물리 오차·정확도·속도 향상이 아니다. source의 기존 RED/GREEN·primary·독립 reference·CAS 및 provider GET 기록을 재실행하거나 독립 재검증한 것은 아니다. 이 본문은 실제 HD reactive array 또는 named WU physical consumer를 제공하지 않는다. WU 물리 결속으로 승격하지 않는다.

다른 구체적 최신 metadata lead에는 `BASS_HE_TANGENT13_S10_20261028_c9a5632280ec.zip`, `BASS_CR_HE_ENERGY_SUM_C02_20261028_953508f51296.zip`, B3h frozen-reset 및 BF3D 진행 백업이 있다. 객체 시각·ID·크기를 `CHANGED_BACKUP_LEADS.json`에 고정하고 root 및 repo census 담당에게 전달했다. 이 census에서는 해당 ZIP 본문을 읽었다고 주장하지 않는다. 구체적 immutable repo 원전 결속은 repo census 결과에 따른다.

## 대화·첨부 및 읽기 한계

Personal Context를 이번 요청에 맞춰 **새로 1회** 검색했으나 실제 응답은 `Personal context is unavailable for this conversation.`이었다. 다른 대화가 없다는 뜻이 아니며 전수 열람 완료로 표시하지 않는다.

현재 프로젝트 첨부20개, 합계435,180,795bytes의 SHA-256과 크기를 측정했다. 이전 전체 파일 SHA가 없어 과거 대비 byte identity를 주장하지 않는다. 문헌 ZIP7/8 members 및 automation-kit ZIP38 members의 목록·크기는 R13 기록과 일치한다. PDF는 R13의 pdfinfo/첫2쪽 읽기 근거를 재사용하고 이번에는 파일 hash/크기만 측정했다. 첨부04/05/07/08의 네 policy·figure TXT는 이번에 전문을 읽었다. 계약 선행, equation-to-code 결속, 수학/물리 및 구현 이중 심사, 실제 생성 그림 확인, 관련 adversarial check와 유한 micro-repair를 현재 범위에 적용한다. 완료한 과거 과학 실행을 반복하는 근거로 삼지 않는다.

실제로 읽은 범위에서 새 HD array bytes와 named WU physical binding을 확보하지 못했으므로 **INPUT_PENDING_IN_INSPECTED_SCOPE**를 유지한다. 모든 외부 자료의 부재를 주장하지 않는다. 이번 census에서 science/import/compile/ODE/CAS/old replay/remote write는 각각 **0**이다.

## 근거 파일과 공개 범위

`BACKUP_CONTEXT_CENSUS.json`은 범위·terminal·증분·cutoff·실패 분류를, `BACKUP_OBJECTS_R11_R12_R13_RECONCILIATION.json`은34개 교차 metadata 및 기존 receipt 결속을, `CHANGED_BACKUP_LEADS.json`은 새 연구 백업과 실제 읽은 handoff 요약을 담는다. `ATTACHMENT_SCOPE.json`은20개 현재 파일 식별과 읽기 범위를, `LOCAL_RAW_RESPONSE_MANIFEST.json`은 로컬 원응답의 SHA/크기를 담는다. raw provider 응답, 사적 계정 metadata, 무관한 파일명, 저작권 원문은 public packet에서 제외한다.
