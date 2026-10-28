# GL2022 공개 reactive 데이터 경로 조사

**DOI 10.1063/5.0128598의 reactive SQM 배열 원문 바이트는 이번 조사에서 취득하지 못했다. 실제 배열 파일의 SHA·크기·행 순서·온도 grid·missingness는 아직 인증할 수 없다.** 출판사 원문은 반응(1)의 전체 state-to-state 수치가 supplementary material에 있다고 명시한다. 따라서 결론은 `INPUT_PENDING`이며 자료 자체의 부재가 아니다.

이번 범위는 공식 Crossref, AIP 공개 기사·옛 supplement landing 경로, HAL의 본문과 공개 검색 API, DIGITAL.CSIC의 서지·full metadata·OAI, 별도 EMAA DOI의 DataCite metadata다. 접근 통제 우회, 계정 사용, 저자 연락, 다른 owner 쓰기 또는 과학 실행은 하지 않았다.

## 실제 확인한 경로

| 경로 | 실제 관찰 | 판정 범위 |
|---|---|---|
| Crossref `works/10.1063/5.0128598` | Exa fetch가 공식 JSON을 반환. `link` 3항목이 모두 같은 본문 PDF이고 `relation={}` | 이 반환 metadata에 supplement 파일 locator가 없음. Supplement 자체의 부재는 아님 |
| AIP 기사 원문 | reactive 반응(1)의 전체 state-to-state rate 및 두 과정의 SQM 수치가 supplement에 있다고 명시. 추출된 본문의 Supplementary Material 영역은 실제 파일 URL을 노출하지 않음 | 본문과 파일 존재 진술은 확인했지만 실제 array download locator 미확보 |
| HAL `hal-04285297` | Exa가 논문 본문을 반환 | 본문 extraction이며 원본 reactive array 취득이 아님 |
| HAL 공개 API | exact DOI의 1개 record, `fileMain_s=https://hal.science/hal-04285297/document`. 요청한 `fileAnnexes_s`, `researchData_s`, `related_s`는 반환 record에 없음 | 이 deposit metadata에서 별도 supplement locator를 확인하지 못함 |
| DIGITAL.CSIC `10261/305186` | 제목·저자·발행일 서지 확인 | 파일 목록이나 수치 본문을 취득한 것은 아님 |
| CSIC `?mode=full` | Exa `SOURCE_NOT_AVAILABLE` | 도구에서 해당 경로 취득 실패 |
| CSIC public OAI GetRecord | `Making sure you're not a bot!` 응답 | 봇 확인 경계에서 중단. Metadata 부재로 해석하지 않음 |
| 옛 AIP DOI supplement landing | Exa `CRAWL_LIVECRAWL_TIMEOUT` | constructed public DOI landing route의 취득 시간 초과; 존재·부재를 판정하지 않음 |
| Local public GET 4경로 | Crossref/CSIC/HAL/AIP 모두 `URLError: [Errno 1] Operation not permitted` | 로컬 실행 환경에서 네트워크 접근 불가. 사이트의 HTTP403이나 원문 부재라는 뜻이 아님 |

직접 GET 시작·종료는 `PUBLIC_HTTP_ROUTES.json`에 실제 기록되어 있다. **2026-10-28 04:42:47.973361–04:42:47.979259 UTC**, 즉 13:42:47.973361–13:42:47.979259 KST의 4개 공개 요청이다. 그 뒤 같은 local GET를 반복하거나 차단을 우회하지 않았다. 검색/fetch 도구별 원문은 `local_only/`에 분리했으며, 원본 파일 bytes와 tool-extracted text를 혼동하지 않는다.

## 상태·단위에서 확인할 수 있는 범위

논문 III A의 reactive 과정은 H+ + HD → D+ + H2이며, 본문은 HD(v=0,j=0..8)에서 H2(v′=0,j′=0..9)로의 SQM state-to-state 계산을 설명한다. 본문 rate 단위는 cm³ s⁻¹, 연구의 온도 범위 진술은 5–3000 K다. 이는 **논문이 선언한 계산 범위**이고 아직 취득하지 못한 array의 실제 header·순서·grid를 검증한 것은 아니다. 진동 여기 H2를 만드는 별도 예시도 본문에 있지만 전체 supplement의 구조를 추정해 채우지 않는다.

SQM과 TIQM/EQM 비교는 원래 서로 다른 방법의 비교다. 논문의 v=0 진술을 기존 native K의 미지 v에 자동으로 결속하지 않는다. Native `v=UNSPECIFIED`, `MISSING_NOT_ZERO`, TIQM/SQM 구별은 그대로 유지한다. 실제 배열과 named WU physical consumer·density·clock 결속은 아직 성립하지 않았다.

## EMAA DOI의 별도 분류

DataCite 공식 metadata의 DOI **10.17178/emaa_hd_rovibration_805a7aa5**는 *Rovibration excitation of HD by H and H+ collisions*다. 형식은 `Radex`, target은 HD이며 collisional excitation으로 등록되어 있다. Metadata는 52 rovibration energy levels, 368 radiative transitions, H에 대해 1326 collisional transitions/15 temperatures/5–5000 K, H+에 대해 171 collisional transitions/25 temperatures/5–3005 K를 진술한다.

이 metadata는 HD excitation 데이터의 locator이고 H+ + HD → D+ + H2 reactive array로 채택하지 않았다. 논문의 5–3000 K와 dataset metadata의 5–3005 K도 합쳐 쓰지 않는다. 실제 dataset 파일을 받지 않은 상태에서 추가 행 의미·단위·missingness를 추정하지 않았다.

## 후속 처리와 보존

현재 actual reactive payload count는 0, provider-original reactive-file GET 성공은 0이다. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`, central/physical delta=0을 변경하지 않는다. 현재 전체 repo·backup 조사 결과는 root가 별도 종합한다. 이 레인에서 새 물리 입력을 공급하지 못했으므로 기존 R11 저장 근거는 계속 재사용할 수 있으며, 다음 연구 계약은 root가 정한다.

이 조사의 Exa 사용은 search 1회(요청 결과 5개)와 fetch 4회(11 URL)다. 일반 web은 search 5회(15 query)와 open 1회(4 URL)다. 검색 결과의 무관한 논문·다른 DOI는 버렸으며 검색 비발견을 자료 부재로 사용하지 않았다. 과학 primary/reference/CAS/ODE 실행, 생산 import, 기존 repo 수정과 외부 쓰기는 모두 0이다.

## 공식 source locators

- Crossref: https://api.crossref.org/works/10.1063/5.0128598
- AIP: https://pubs.aip.org/aip/jcp/article/157/21/214302/2842276/A-statistical-investigation-of-the-rate-constants
- 본문 PDF(Crossref 등록): https://pubs.aip.org/aip/jcp/article-pdf/doi/10.1063/5.0128598/16555328/214302_1_online.pdf
- HAL: https://hal.science/hal-04285297v1
- HAL API: https://api.archives-ouvertes.fr/search/?q=halId_s:hal-04285297&fl=halId_s,doiId_s,fileMain_s,fileAnnexes_s,uri_s,related_s,researchData_s&wt=json
- DIGITAL.CSIC: https://digital.csic.es/handle/10261/305186
- DataCite: https://api.datacite.org/dois/10.17178/emaa_hd_rovibration_805a7aa5

기계 판독 근거는 `CROSSREF_METADATA.json`, `HAL_METADATA.json`, `PUBLIC_HTTP_ROUTES.json`, `HD_ROUTE_SUMMARY.json`이다. `local_only/`의 search snippets·article extraction은 제3자 원문이며 연구 source 게시 payload에서 제외한다.
