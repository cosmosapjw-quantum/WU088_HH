# WU R7 백업·대화·첨부 intake 결과

## 결론과 현재 기준점

새로 확인한 실물 자료는 HE PHOTON05, 그 후속 ANGULAR06, CR proper-source closeout 및 low-birth causal RR 계약이다. PHOTON05와 ANGULAR06은 EXFOR의 핵반응 좌표에 대한 실제 조건부 수치 결과를 제공한다. CR 후속은 초기 cohort, proper clock, H/He density와 RR operator의 새 모델 계약을 구체화했다. 이 자료들 및 현재 첨부 문헌에서 **GL2022 분자 파괴율 수치 배열이나 WU HD 상태공간에 결속한 x0/piDot/K/d/h/f/density/clock 전체 입력 packet은 확보하지 못했다.** 이는 아래에 명시한 읽기 범위의 자료 상태다.

WU 현재 기준은 R6 metadata HEAD `0713cb7ef6df5769def878b475ba18f4068331fa`, scoped DAG **13/28**이다. R4 S10/R5 11개 기존 archive의 22회 원본 byte 검증과 R6 최종 dual backup 영수증을 재사용했다. 기존 archive 재다운로드와 과학 실행은 0이다. 외부 게시·업로드·삭제·Git mutation도 0이며, 새 파일은 이 intake 디렉터리에만 작성했다.

관측은 단계별 시점이 있는 snapshot이다. 최종 Drive freshness 목록의 가장 늦은 새 객체는 **2026-10-27 13:18:05.246 UTC**의 CR C03이다. 그 이후 live head를 계속 추적하지 않았다. GitHub 전수 branch/repo 조사는 별도 inventory 담당자의 근거와 결합해야 한다.

## 실제 조회한 범위

| 공급자/대상 | 실제 반환·읽기 | 정확한 범위 |
|---|---:|---|
| Dropbox `BASS_DERIVATION_DOSSIERS_20260912` | 3,438개, 6 pages, has_more=false | direct child 완전 목록. 과거 모든 하위 폴더의 재귀 내용 조사는 아님 |
| Dropbox `bass_cr` | 170개, has_more=false | 최초 intake 시점 direct child 완전 목록 |
| Dropbox WU 폴더 | 577개, has_more=false | R6 최종 metadata ZIP 및 기존 복구 ZIP 확인 |
| Drive dossiers 폴더 | 최신 1,000개 | modified-time 내림차순 경계가 2026-09-28. 이번 2026-10-27 변경창은 포함되며 더 오래된 전체 목록은 partial |
| Drive `bass_cr` | 최초 152개, 최종 157개 | 요청 한도 1,000 미만. R08 이후 R09/R10/C01–C03 추가 관측 |
| Drive WU 폴더 | 609개 | 요청 한도 1,000 미만. 최신 R6 최종 metadata source0713cb 확인 |
| Personal Context | 실제 검색 호출 | `Personal context is unavailable for this conversation.` 반환 |
| 현재 project_sources | 20개 | 현재 SHA256 계산. 이전 20개와 이름·크기 동일. 이전 목록에는 SHA256이 없어 전체 byte 불변 비교는 불가 |
| papers/literatures 첨부 | PDF 15개, 추출문자 8,889,049개 | 전체 추출 가능한 본문 검색. OCR은 하지 않음 |

정확한 폴더 ID·경로·query·cutoff·새 객체 ID는 `FINAL_QUERY_SCOPE_AND_COVERAGE.json`에 있다. Dropbox search의 title/date 필터 요청에도 오래된 off-title 결과가 반환되어 그 검색의 0건·100건을 완전성 근거로 삼지 않았다. 직접 폴더 목록으로 보강했다. Drive 일반 검색은 알려진 ZIP도 누락한다. `list_folder(top_k=5000)`은 실제 page-size 허용 범위 1–1000 오류를 반환했다. 허용된 최신 1,000개와 확인된 시간 경계를 사용했다.

대화 원문은 회수되지 않았다. 현재 대화와 parent가 제공한 R6 identity·PHOTON05 포인터는 supplied context로 유지한다. 다른 repo archive 안의 대화 요약이나 handoff를 전체 이전 대화의 검색 결과로 표시하지 않는다.

## 새 자료의 실제 내용

### HE PHOTON05

Drive delivery 원본 2,203,799 bytes, SHA256 `25ac28965be174457a1b5e57f73f387185fc0674c9c152172a845906c206883a`를 읽었다. Source는 `251c6baa6c3359b1d6997dbce51cea65500b53d6`, delivery는 `4db5ce7297a7ded4624b93721873aacc9b4ebf30`이다. 별도 source ZIP 20,425,864 bytes의 존재도 양쪽 metadata에서 확인했으나 다시 내려받지 않았다. 읽기 근거는 `PHOTON05_READ_RECORD.json`과 해당 `reads/PHOTON05_DELIVERY/` 파일이다.

실제 결과는 photon + stationary bare alpha → 두 bare ground-state deuteron의 유한질량 반동·응력·단일 에너지 원장이다. EXFOR M0475002의 12 native 좌표, photon energy 213/258/330 MeV 및 CM angle 46/61/73/87도를 사용하고 NIST2022 nuclear masses에 조건부다. 원 결과는 24/24 PASS다. 원 그림은 CPU 4.40726504 s가 cap4 s를 넘어 FAIL이며, 이 실패를 유지한다. 로컬 DAG는 4 complete +1 partial +3 physical open /8이다.

이 자료에는 실제 photon encounter flux, 완전한 angular law, global species ID 및 named deposition이 결속되지 않았다. Native flux0은 caller 예제다. `Gamma_thermal`, `Cv`, species heating, thermal deposition은 null이고 birth pool은 UNASSIGNED다. 물질 핵 수 +1과 열적 수·에너지를 같게 두지 않으며 binding은 population rest-energy witness가 한 번 소유한다. 수백 MeV 핵반응의 conditional event 결과를 HD+para-H2 회전준위 파괴율로 옮기지 않는다.

### HE ANGULAR06

S02 `a4745150c30af2c6a71b6b61bde0a7e17b8b9ddc`와 이후 S03 archive `4349f3cc9254`를 읽었다. S03의 SHA256은 `8888521bce0824ffc7d8504bc74b5c0b3e754b018afc8c6f982c916428dbb5b9`다. S03 결과는 conditional CM→lab angular map, Jacobian, 한/두 역상, fold/stopped/threshold 처리, branch별 weighted pushforward 및 identical-daughter normalization이다.

S03 기록에는 새 26/26 PASS, CPU0.273874185 s와 새 그림 CPU5.791514953/6 s PASS가 있다. 로컬 조건부 제품은 5/8 complete, 물리 입력 3개는 open이다. PHOTON05의 이전 plot FAIL은 변경되지 않는다. `MODEL_CONTRACT.json`의 f_CM은 caller가 제공하는 함수이며, `SOURCE_MANIFEST.json`의 original normalization과 complete angular law는 UNRESOLVED다. S03 결과에서도 actual encounter flux와 named consumer는 open이다. 새 조건부 사상과 실제 실험률 입력을 각각 그 범위로 재사용한다.

PHOTON05/ANGULAR06 source·central publication은 읽은 기록에서 false다. 공개 GitHub source push가 차단된 이력과 로컬 backup/source identity를 구분했다. 공개 HE branch가 유지되었다는 관측만으로 이 로컬 연구가 존재하지 않는다고 결론내리지 않는다. 이 intake는 HE 게시를 시도하지 않았다.

### CR proper-source와 low-birth 후속

Proper closeout의 actual science source는 `022c163726b814885805bd9a7ab988fe963cda4a`다. 기존 PHYS02 실제 source를 재사용한 유한 proper-volume electron source에 대해 18 actual rows와 256 scoped controls/checks가 기록되어 있다. 원 source는 T100 K, nH140 m^-3, YHe0.248, xHII=xHeII0.01, proper time[0,10^10]s, native electron0.1–900 eV다. 원 closeout의 actual nb/native25/RR는 null이고 100 K source와 예전 10000 K RR join은 열려 있다.

새 CR low-birth R08에서 실제로 읽은 named contract는 `CR_PHYS02_LOW_BIRTH_CAUSAL_RR_V1`이다. 선택 source tag는 `direct_0p1_10`; ramp q_j(t)=tA_j, initial cohort0, 같은 proper[0,10^10]s를 선언한다. 새 H1/He4-only 모델 inventory는 nHe=1085/94, ne=2849/1880, nb=8750/47 m^-3다. 이것은 추가 모델 선언이며 과거 source가 원래 nb를 제공했다는 근거로 소급하지 않는다.

새 operator 계약은 3200 active electron nodes에서 downward Coulomb drift d_j=b_j/ΔE와 ground-state H/He RR hazards λ=n_ion vσ이다. GL2022 molecular destruction d_j와 입자·상태공간·물리 정의가 다르다. C03 `10a68e5838fa`의 `CODING_BASELINE.json`은 새 코드가 authored/not_executed임을 명시한다. `OUTPUT_SCHEMA.md`의 PREPARED.npz/ARRAYS.npz, lambda_H/lambda_He와 occupancy 배열은 prospective output이다. 이 C03 archive에 실제 새 coefficient/result 배열이 생성되었다는 기록은 없다.

같은 archive의 REI selected finite-cohort 계약은 piecewise-affine h(s), same frozen response/state/frame/proper clock을 요구한다. K_AB=G(B−τ)−G(A−τ)의 정보집합 경계 방법은 유효한 수학적 interface다. 물리적인 source history의 구간 밖 continuation, 실제 recipient nb와 이온별 source chemistry는 별도 입력으로 남아 있다. CR에 복사된 WU 진행률과 백업 상태는 12:20/12:42 시점의 역사적 관측이다. 현재 WU R6 final0713cb 및 완료된 archive 배송으로 대체해 읽었다.

## 첨부 문헌에서 확인한 범위

현재 20개 파일은 이전 목록과 이름·크기가 모두 같았다. 새 SHA256 manifest를 `CURRENT_PROJECT_ATTACHMENTS.json`에 작성했다. 16번 checksum 파일의 SHA256은 실제 17번 Rust archive와 일치한다. 이전 전체 파일 SHA 목록이 없어 다른 19개 파일의 과거 byte 불변성은 주장하지 않는다.

`18-literatures.zip` 7개 PDF와 `19-papers.zip` 8개 PDF는 전체 추출 가능한 본문을 검색했다. 모든 pdftotext가 exit0이었고 DOI5.0128598, GL2022/Lezana, molecular-HD-reactive 및 WU named-consumer 검색 패턴 매칭은 0이다. 확인된 제목들은 상대론적 우주론·운동론·CMB/Bianchi 자료다. PDF 이미지 안의 글자나 OCR이 필요한 부분은 이 결과의 범위 밖이다. 이 scan에서 새 GL2022 numerical table을 회수하지 못했다. 원문 PDF의 전체 텍스트를 공개 보고서로 복사하지 않았고 기록에는 파일 identity·검색식·문자수·일부 제목만 남겼다.

## WU 입력 계약으로 넘길 결과

| 요청 입력 | 이번 읽기에서 확인한 상태 |
|---|---|
| GL2022 destructive rates/arrays | 실제 수치 배열 회수 없음. 첨부 15 PDF와 선택한 신규 HE/CR source 읽기 범위의 결론 |
| WU HD x0 | 새로운 실제 상태 population vector를 제공한 자료 없음 |
| WU HD piDot, K | R6의 기존 HD rate/Gibbs 근거 재사용. 이번 HE/CR 자료에서 같은 상태공간의 새 complete input 없음 |
| WU HD d/h/f | 분자 destruction·formation·forcing 전체가 실제 data로 결속된 packet 없음 |
| collider density와 physical clock | WU에 결속된 n_coll은 제공되지 않음. CR의 명명된 electron/H/He density와 proper clock은 해당 모델 전용 |
| 이용 가능한 새 다른 영역 결과 | PHOTON05 native12 conditional recoil, ANGULAR06 conditional angular measure, CR explicit conditional H/He inventory/response contract |
| conversation provenance | Personal Context unavailable; supplied context와 archive handoff를 구별 |

다음 실제 입력은 WU source state IDs와 온도·collider/channel 정의에 연결된 숫자 배열, 단위·시간 변수·밀도·초기조건, d/h/f의 원전·유효구간, uncertainty 해석을 함께 제공해야 한다. 실제 packet이 들어오면 그 바뀐 의존성만 검사하면 된다. 현재의 입력 공백은 이미 완성한 R6 정리나 구현의 지위를 변경하지 않는다.

## 산출물과 재사용 영수증

- `FINAL_QUERY_SCOPE_AND_COVERAGE.json`: 정확한 질의·범위·최종 freshness 증거.
- `NEW_SOURCE_ARCHIVE_INVENTORY.json`, `LATEST_DELTA_ARCHIVE_INVENTORY.json`: 새 6개 archive identity와 member 목록.
- `PHOTON05_READ_RECORD.json`, `TARGETED_SOURCE_READS.json`, `LATEST_DELTA_READ_RECORD.json`: 실제 선택 파일·SHA256·읽기 수준.
- `CURRENT_PROJECT_ATTACHMENTS.json`, `ATTACHED_PDF_SOURCE_SCAN.json`: 첨부 identity와 검색 결과.
- `INTAKE_REPORT.json`: machine-readable 결론·차단·재사용 경로.

기존 복구 증거는 `/workspace/scratch/16df962c9b4e/wu_resume_20261027/recovery_delivery/R4S10_R5S01_S05_DUAL_READBACK_INDEX.json`의 6/6 PASS와 `R5_S06_S10_DUAL_READBACK_INDEX.json`의 5/5 PASS다. R6 final 증거는 `wu_resume_20261027/r6_delivery/FINAL_METADATA/DUAL_BACKUP.json`의 DUAL_UPLOAD_AND_ORIGINAL_BYTES_VERIFIED다. 기존 과학·그림·ZIP·원본 readback을 재실행하지 않았다.
