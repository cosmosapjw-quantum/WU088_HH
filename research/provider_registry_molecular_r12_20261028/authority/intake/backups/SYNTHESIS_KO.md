# R12 백업·대화 조사 — 읽기 전용

## 판정

새로운 백업 변경이 있다. R11 FINAL 뒤에 VigilODE matrix-bound A와 B ZIP이 양쪽 provider에 생겼고, B의 실제 원본을 읽어 **15/20의 조건부 행렬 연구·최종 심사 대기** 상태를 확인했다. 기존 native metric 단위는 **20/20 전달 완료**지만 실제 적용은 `BLOCKED_INPUT`이다. 두 연구 모두 WU의 실제 HD reactive array나 named physical consumer/density/clock binding을 공급하지 않는다. 이 판정은 읽은 변경 source의 범위에 한정하며 모든 미공개 자료의 부재를 뜻하지 않는다.

R11 FINAL은 `c0b97999b928acb04a805bf3e5283af73aff9831`, tree `503d048cc83b5813f15cd5996277403f16166db4`로 재사용했다. 3,760,940 bytes·SHA-256 `b25a49a5d2acc221bc8a97e5e0ab3a6f41c9149a9f5948ab317e367ec251fb2e`는 기존 detached FINAL receipt의 identity다. 이번 actual metadata에서 Drive·Dropbox 이름과 크기가 모두 일치했다. R11 원본 GET·ZIP 재계산·과학 재실행은 하지 않았다. FINAL 자신의 영수증을 source에 소급 삽입하지 않는다. R11 workflow **20/20**, DAG **23/38**은 보존한다. 근거: [FINAL_R11_METADATA.json](FINAL_R11_METADATA.json).

## 실제 열거 범위

| 범위 | 실제 반환 | 종료·한계 |
|---|---:|---|
| Dropbox root 직접 항목 | 511 | 1페이지, `has_more=false` |
| Dropbox BASS_DERIVATION 지정 계층 | 5,249 | 9페이지(600×8+449), `has_more=false` |
| Dropbox 추가 관련 3개 계층 | 326 | 각 1페이지, 모두 `has_more=false` |
| Dropbox 위 scope의 고유 합집합 | 6,086 | file5,810·folder275·mount1; 무관한 모든 하위 계층까지 읽었다는 뜻은 아님 |
| Drive 접근 가능한 folder discovery | 553 | 4페이지(430,13,7,103), provider next token 소진 |
| Drive 관련 folder 270개 직접 목록 | 고유3,933 | 상위 BASS folder만1,000개 cap |
| Drive root 직접 목록 | 337 | 관련209개; 파일 list에 cursor가 노출되지 않음 |
| Drive 관련 folder+root 관련 목록 | 고유4,142 | cap-hit parent의 완전성은 미확립 |
| 다른 대화 원문 | 0 | personal-context 실제 호출 결과 unavailable |

Dropbox의 최초 R10 5,193 terminal과 이번5,249는 서로 다른 시점의 조사다. 차이56을 정확한 변경 파일56개로 해석하지 않았다. 지정 Dropbox main subtree에서는 R11 FINAL의 04:29:30 UTC보다 늦은 항목을 보지 못했지만, root에서 새 VigilODE A/B를 찾았다. 따라서 지정 subtree의 결과를 전체 provider의 무변경 주장으로 확대하지 않는다.

Drive `list_folder`는 `url/top_k`만 받으며 cursor·시간 필터가 없다. 10,000 요청은 실제400 오류로 거절되어1,000을 사용했다. `search`의 raw q/시간 필터를 사용해 대체 열거를 시험했으나, 현재 metadata로 존재가 확인된 R11 FINAL ZIP의 정확한 이름 검색도0건, cap-hit parent의10월 ZIP 범위 검색도0건이었다. WU folder 직접 목록664개와 문서 검색99개도 다르다. 따라서 이 검색 결과를 binary ZIP 전체 목록이나 부재 증명으로 사용하지 않았다. 세부 page/count·제약·probe는 [ENUMERATION_COUNTS.json](ENUMERATION_COUNTS.json)과 [DRIVE_CAP_AND_SEARCH_PROBES.json](DRIVE_CAP_AND_SEARCH_PROBES.json)에 있다.

기록된 첫 조사 checkpoint는 2026-10-28 04:38:54.731 UTC(13:38:54.731 KST)다. 그 이전 초기 호출의 정확한 시작시각은 따로 계측하지 않아 null로 남겼다. 관련 Drive 목록의 기록시각은04:40:39.583–04:41:13.999 UTC, root 확인은04:43:37.630 UTC다. 원본 content 확인은 그 뒤에 수행했다. 이 조사는 원자적 snapshot이 아니다.

비공개 표지가 있는 Dropbox37항목·Drive9항목은 집계만 남겼으며 무관한 root 내용도 개별 공개하지 않는다. 공개 최근 metadata128행 중83행은 양쪽에서 같은 이름을 확인했고 크기 불일치0이다. 이름·크기 일치는 byte equality나 새 업로드 ACK를 뜻하지 않는다. 반대쪽 record가 null인 경우도 조사한 선택 목록에 없다는 뜻이다. [PUBLIC_RECENT_BACKUPS.json](PUBLIC_RECENT_BACKUPS.json)을 따른다.

## 새 VigilODE matrix B 원본과 심사 경계

| 항목 | 확인값 |
|---|---|
| 이름 | VIGILODE_V8_MATRIX_BOUNDS_20261028_B_RESULTS.zip |
| 크기 | 9,285,519 bytes |
| SHA-256 | `2be53029a19c48e2e68e393d0a0c74626ba9b3632b6fcf90769230ad1f2c4a64` |
| Archive | 299 members, 전체 ZIP CRC PASS |
| Drive | `1kTQAB48vvyqOwqhkpcevb_SNWtJJmVj8`,04:38:02.158 UTC |
| Dropbox | `id:BSpOijBcT10AAAAAAEDJUw`,04:38:10 UTC |
| 원본 검증 | Dropbox GET bytes를 로컬에서 검증; Drive는 raw file reference 반환까지이며 두 원본 bytes의 독립 비교는 하지 않음 |

기본 shell의 첫 다운로드는 browser-proxy 연결 오류(exit7)로 실패했고, 허용된 읽기 전용 escalated 경로에서 실제 GET이 exit0으로 성공했다. 자동 승인 심사의 거절은 없었다. 이 네트워크 오류는 과학 실행 실패가 아니며, 과학 코드를 실행하거나 import하지 않았다.

단위는 `V8_FIXED_METRIC_JACOBIAN_LOGNORM_20261028`이다. 고정 BASS `cc602e209e7deeb511ab2a1f3b2268d55206c43c`와 30 reduced/33 physical/31 query, `x=ln(a/a_ref), a_ref=1/21`의 metric에서 **공급된 interval matrix**의 operator/lognorm certificate를 만드는 연구다. 실제 Jacobian이 그 box에 속한다는 검증과 실제 linking path/corridor는 외부 전제다. 계약은 WU l1 certificate를 전용하지 않는다고 명시한다.

2026-10-28 04:37:37.544344 UTC snapshot의 stage는 R1–R7와 C1–C8이 완료되어 **15/20**이다. R8,R9,R10,C9,C10은 pending/delivery_pending이다. 저장된 실행 요약은 Python10 control groups·실패/오류0, Wolfram25/25 True를 기록하지만 최종 scientific admission은 `PENDING_REVIEW_AND_ROOT`이다. 이를 새 독립 완료 심사나 actual model closure로 승격하지 않았다. `actual_model_enclosure_verified=false`, `owner_provenance_verified=false`, 중앙28/88·own delta0, Git `HOLD_TOOL_CALL_REJECTED_NO_ACK`·new mutation0을 보존한다. Git HEAD가 변하지 않았다는 사실과 새 백업 연구가 없다는 주장은 다르다.

Archive에서 contract,budget,publish plan,stage map,intake,execution summary,preexecution review의7개 member만 읽고 byte identity를 보존했다. [MATRIX_B_SELECTED_MANIFEST.json](MATRIX_B_SELECTED_MANIFEST.json), [MATRIX_B_ARCHIVE_MEMBERS.json](MATRIX_B_ARCHIVE_MEMBERS.json), [selected source](changed_source/VIGILODE_MATRIX_B/SCIENTIFIC_CONTRACT.json)를 따른다. 원본 ZIP에는 미심사 provider/intake wrapper도 포함되므로 공개용 출력 폴더 밖에 보관하고, 선택 심사한 source만 게시 대상으로 삼는다.

## 다른 변경과 대화

BASS의 BF1/BF2/BF3A/BF3B/QSS/LYA, REI C5/C6/C7 및 literal binding, REC native source split parts·C10 companion·late payload metadata를 현재 목록에서 확인했다. GitHub 담당자가 immutable source를 직접 읽고 있으므로 같은 본문을 재수집하지 않았다. 특히 REC의 새 actual recovery와 오래된 recovery handoff의 미복구 표시는 시점을 구분해야 한다. 메타데이터만으로 임의의 actual WU binding을 만들지 않는다.

VigilODE native metric의 작은 handoff와 detached FINAL_ACK 원문은 직접 읽었다. 연구20/20·중앙28/88·delta0이지만 actual application `BLOCKED_INPUT`, production `HOLD`, L4 false다. [VIGILODE_NATIVE_METRIC_FETCHED_TEXT.json](VIGILODE_NATIVE_METRIC_FETCHED_TEXT.json)은 추출 text representation이며, 추출된 텍스트를 원본 bytes와 같다고 가정하지 않는다.

personal-context skill과 실제 callable tool을 사용했지만 응답은 “Personal context is unavailable for this conversation.”였다. 다른 전체 대화 원문은0건이며 현재 대화와 제공된 R10/R11 인계서는 재사용했다. [CONVERSATION_ACCESS.json](CONVERSATION_ACCESS.json)에 이 실제 접근 경계를 저장했다. 전체 대화가 조사됐거나 존재하지 않는다고 주장하지 않는다.

## 다음 연구에 넘기는 경계

이 조사 자체의 provider write/upload/science/CAS/solver import는 모두0이다. 새 actual HD 또는 named physical WU consumer/density/clock는 읽은 변경 backup content에서 식별되지 않았다. root는 별도의 공개 HD 자료·GitHub 조사와 결합해 다음 단위를 정해야 한다. R10/R11과 R9/R8/R7/R6/PHYS91 allowance는 늘리지 않고, global remaining/full historical CPU는 null을 유지한다. 기존 완료 과학·ODE·독립 심사를 통상 재개 절차로 반복할 근거가 없다.
