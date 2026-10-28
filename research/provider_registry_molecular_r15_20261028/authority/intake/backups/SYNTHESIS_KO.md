# R15 진입 백업 조사와 연구 문맥 종합

기준은 WU R14 FINAL `6ca324dbc5d3c4b5c064f7621730eb0d6ee5eb51`, 과학 DAG **29/44**다. 이 조사의 과학 채택 증분은 **0**이다. 최신 사용자 지시는 다음 이론·코딩 루프와 예산 증액을 승인한다. 과거 R14의 다음 단위 미승인은 역사 기록으로 유지한다.

## 실제 목록 범위

| 범위 | 현재 실제 결과 | 종료 상태 |
|---|---:|---|
| Drive WU 이름 folder 검색 | 63 candidates, 같은 14 WU roots 선택 | 검색 terminal |
| Drive WU 14 roots와 후손 | 167 folder lists, 1,257 items / 1,104 files / 153 nested folders | queue 0, capped 0, error 0 |
| 이전 R14 같은 폴더 기준 | 1,246→1,257; folder ID 167개 동일 | main R31S만 687→698; 나머지 folder별 count 동일 |
| Drive 동일 document filter | 100+98=198 | terminal; 이전 count 198과 동일 |
| Drive 일반 dossiers parent | 최신 1,000 immediate items | 전체 역사 parent는 cap; 반환순서 modified-desc |
| Drive parent의 folder-only 목록과 추가 후손 | 27 roots terminal; WU 외 15 roots에서 17 lists / 547 items | 추가 후손 queue 0, capped 0 |
| Dropbox root | 530 entries | terminal |
| Dropbox dossiers recursive | 5,381 rows, 600×8+581, 9 pages | terminal |
| Dropbox 같은 WU 13 roots | 1,143 items / 1,017 files | 이전 1,132보다 11 증가 |
| Dropbox BASS_BACKUPS / bianchi / PHYS69 | 231 / 39 / 1 | 모두 terminal |
| WU 기존 34 + R14 11 archive pairs | 45/45 이름·ID·size 일치 | R14 actual receipt 11개와도 일치 |

전체 과거 per-item raw는 현재 baseline public pack에 없다. 따라서 같은 167 folder ID와 각 count, 현재 timestamp, 45개 기존 identity의 직접 대조를 구별했다. 모든 기존 파일이 하나도 바뀌지 않았다는 일괄 명제는 내리지 않는다. WU 범위의 11개 증가와 현재 확인된 R14 S01–S10/FINAL 11개는 일치한다. Dropbox dossiers의 count 증가 50과 timestamp-recent 49도 서로 다른 관찰이다. BASS_BACKUPS의 count 증가 7과 timestamp-recent 6을 억지로 같게 만들지 않는다. 목록은 비원자적 live 조회다.

일반 Drive parent의 top_k=10000 요청은 명시적인 1..1000 제한으로 400 실패했다. 원인에 맞춰 1000으로 수정했고 parent cap은 그대로 표시했다. 별도의 folder-only 27개 목록과 후손은 끝까지 열거했다. 최신 반환 1,000개의 가장 오래된 수정시각은 2026-09-30T09:34:08.707Z로 기준 cutoff보다 이전이다. 이를 전체 parent 역사 열람으로 부르지 않는다. 같은 document filter의 198개는 count 일치이며, 이전 전체 ID 목록이 없으므로 모든 ID의 동일성은 주장하지 않는다.

## 새 백업이 제공하는 실제 연구 문맥

최근 metadata는 CR HE_ENERGY_SUM의 C10/source, HE_ENERGY_CROSS의 R1–R10/C1–C9와 뒤이은 Drive C10/CLOSEOUT, HE_ENDPOINT14의 S01–S09, HE_TANGENT13의 FINAL, BF3E 및 B3H frozen-reset 진행을 가리킨다. 불변 repo 원전을 읽는 branch/PR 조사 담당에게 정확한 파일명·시각을 전달했다. ZIP 파일명 suffix를 자동으로 commit으로 해석하지 않는다.

한 개의 구체적 신규 원전으로 **BASS_BF3E_FINAL_20261028_fc095394.zip**을 실제 HTTP 200으로 읽었다. 크기는 217,005 bytes, SHA-256은 `fc09539429e2cfeb1e55f62d94cfe12e4dfc5d4a96809492e48afa13c2c7cdb9`다. Dropbox content-hash와 ZIP CRC가 일치하고 manifest 48개 member의 size/SHA도 모두 일치했다. HANDOFF, REPORT, OPERATOR_CONTRACT, SCOPED_ADMISSION, CI_ADDENDUM, SOURCE_MAP, MANIFEST의 일곱 텍스트를 읽었다. Archive 이름의 fc095394는 ZIP 해시이며, 실행 코드 commit은 본문의 `60c1ebbb5ef68f8072bc689764f362d6c4df1e4d`다.

이 source는 정적 주기 lapse의 볼로메트릭 I/Q/U/V·normal-rest Thomson에서 전달과 지연 source-memory를 **9/15 scoped**로 채택한다. 같은 finite-collocation A에 대해 S(u)=L exp(uA)Y_i+∫L exp((u−s)A)B S(s)ds를 독립적으로 풀고, quadratic product integration과 augmented exponential weights를 쓴다. 전체 초기 carrier와 source-null 성분을 보존한다. Continuum inverse-ray kernel과 finite-collocation semigroup, source 보간 다항식과 재구성 moment를 구분한다. 최종 local-angle 구적에 global phase Jacobian을 곱하지 않는 규약도 명시한다.

Source가 보고한 새 13 tests와 installed-wheel 검사는 PASS지만, 별도 repository CI는 portable 62 PASS/2 SKIP/1 FAIL과 native-policy 86 PASS/1 FAIL이다. 기존 Rust 134 tests의 PASS와 새 BF3E native 구현 NOT_RUN을 구분한다. Main nx=17의 국소 보존식 residual 약 3.39199e-5도 보존되어 있다. 작은 전역 energy 변화가 국소 continuum 정확도를 인증하지 않는다는 범위를 유지한다. 이 조사는 그 계산을 재실행하거나 독립 모델 심사를 수행하지 않았다.

WU에 대한 재사용은 **기억항·초기 정보·정확한 시계·이산화 구분을 보존해야 한다는 구체적인 방법론적 문맥**이다. BF3E의 다른 operator/metric/finite collocation을 WU의 full-A all-starts contraction certificate 또는 actual HD array로 치환하지 않는다. 이 새 source에도 named WU physical consumer/state/density/clock 결속은 없다. WU의 해당 입력 상태는 검사한 범위에서 INPUT_PENDING을 유지한다.

## 증거 수준과 다음 연결

WU 45개 archive 대조는 현재 provider metadata와 기존 영수증의 identity 확인이다. 이번 census의 새 upload ACK는 0, WU original archive GET은 0이다. BF3E의 실제 original GET 1회는 별도이며 WU 백업 전체 복구로 일반화하지 않는다. 새로운 science/reference/CAS/ODE/import/compile/remote 쓰기는 모두 0이다.

Parent는 이번 PersonalContext 두 호출이 AVAILABLE이라고 알렸다. 직접 WU 관련 4 labels와 관련 cross-project 7 labels의 정확한 접근 범위는 parent 기록이 권위다. 이전 R14의 UNAVAILABLE은 과거 도구 상태로 남긴다. 대화 전체 enumeration API가 제공되지는 않았으며, 전역 자료 부재를 주장하지 않는다. 첨부 20개의 whole-file SHA-256이 R14와 20/20 같다는 대조도 parent가 수행하고 원 manifest를 보관한다.

Public 핵심 파일은 BACKUP_CONTEXT_CENSUS.json, WU_ARCHIVE_RECEIPT_READBACK.json, CHANGED_BACKUP_LEADS.json, BF3E_BACKUP_SOURCE_READ.json이다. private/의 connector 원응답·original archive·선택 본문은 public 소스팩에서 제외한다. 연구 단위 선택은 이 결과와 repo/PR/대화 원전 종합을 함께 사용해 root가 수행한다.
