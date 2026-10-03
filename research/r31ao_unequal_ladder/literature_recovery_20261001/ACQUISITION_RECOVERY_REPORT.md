# WU088_HH 문헌 확보 복구 보고서 — 2026-10-01

상태: **LITERATURE_ACQUISITION_COMPLETE_WITH_DOCUMENTED_UNOBTAINABLE_ITEMS**.
기존 acquired 58 source record와 hash 검증된 168 payload를 재사용했다. 원문 2편·소스 1개를 새로 확보했고, 신규 파일은 설명·공식 문서를 포함하여 6개다. 기존 status!=ACQUIRED 9건 중 7건을 원문/동일 논문 reference로 닫았다. INTLAB·COSY raw source와 원 Deep Research DB ZIP은 미확보다.

## 원격·원 archive identity

- inspected HEAD/tree: `08be330906512eebfe840c40a16b94dc9759e545` / `58f6042a510eb13abc26842feca45eebd1f14d04`.
- archive/infrastructure-only collector HEAD/tree: `46a0889ed4b0cd775117541f91d3cad4557dd7e5` / `8ff35c2c729191dd097cfcd9e7b45c126600f041`.
- v1: 106272651 bytes; SHA256 `df453c892349f622258edd7ee65939338be39f781a22921c6916e7d30876f508`.
- v1의 169 ZIP member 전체를 `previous_v1/`에 보존했다. 원 manifest의 168 payload hash/size가 모두 일치한다. 기존 acquired source를 upstream에서 다시 다운로드하지 않았다.

## 새 원문·코드의 representation

| Work | 확보 형식·경로 | 검증·authority 상태 |
|---|---|---|
| Petras, DOI 10.1016/S0377-0427(01)00586-6 | Wuppertal 공개 author preprint `vipaf.ps`, 15 pages | PostScript magic·제목·저자·abstract literal 및 기관 index 확인. TeX timestamp 2000-12-19. `PREPUBLICATION_SAME_WORK`; 2002 publisher PDF 확보 아님. Final의 정리/식 번호·revision 차이는 unresolved. |
| Gautschi–Varga, DOI 10.1137/0720087 | Purdue 저자 archive의 17-page journal scan `085.pdf` | PDF magic·1983 issue·저자·제목·1170–1186 page range·게재 layout 확인. `institutional_repository`; `EXACT_PUBLISHER_VERSION`은 게재 layout 분류다. Publisher-served PDF와의 byte equality는 미검증이며 publisher direct acquisition count는 0이다. |
| Petras `cinte` | Wuppertal 공식 current unversioned `cinte.tgz` | 13 archive members, 모든 regular member size·압축 읽기 검증. Source snapshot만 보존. Stable version/tag/Git repository 식별 불가; current upstream bytes hash로 pin. COSY 대체 구현으로 취급하지 않는다. |
| COSY INFINITY | 공식 download/registration page 및 10.2 Programmer's Manual, 110 pages, April 2023 | 최신 공식 공개 문서에서 10.2를 선택했다. 개인 등록·서명 licence가 필요한 raw source는 확보하지 않았다. |

R31AO에서 현재 고정된 실제 API authority는 FLINT 3.4.0의 `acb_calc`/`acb_hypgeom` source/documentation이다. 새 Petras/Gautschi 파일은 방법론·문헌 계보를 보존하며, 기존 endpoint theorems A–E나 callback contract의 정리 authority를 자동 교체하지 않는다. 새 manuscript의 theorem/equation 번호를 실행 certificate에 binding하지 않았다. 원문을 읽어 보존했다는 사실과 numerical certificate를 만들었다는 사실은 별개다.

## 실패 citation 5건의 closure

| 기존 ID | 보존한 equivalent |
|---|---|
| URL10, SIAM Accurate Sum and Dot Product | 기존 P08 원문 재사용 |
| URL11, SIAM Gautschi–Varga | P06-R2 저자 archive scan |
| URL24, ResearchGate Taylor Models | 기존 P05 원문 재사용 |
| URL25, ResearchGate Richardson estimate | 기존 P09 원문·코드 재사용 |
| URL26, ScienceDirect Petras | P04-R2 기관 preprint |

원 URL의 실패 evidence와 기존 immutable record는 그대로 유지했다. URL snapshot 확보와 논문 원문 확보를 혼동하지 않는다. Successor DB의 `effective_sources`, `recovery_updates`, `representation_identity`가 새 상태를 제공한다.

## Version 선택

FLINT project pin **3.4.0** 및 기존 NumPy **2.3.5**, MPFR **4.2.2**, GMP **6.3.0**, MPFI **1.5.4**, INTLAB target **14.1**, 기존 resolved commit/tree를 보존했다. FLINT 3.6.0의 기존 shadow archive도 재사용하며 project pin으로 승격하지 않았다. COSY에는 기존 구현 pin이 없어서 공식 10.2 stable document target을 선택했다. raw source는 registration 때문에 미확보이며, 따라서 `latest_stable_used_where_unpinned=false`는 안정판 source를 확보·사용했다고 주장하지 않는다는 뜻이다. `latest_stable_target_selected_where_available=true`. CINTE는 upstream에 release/tag/Git가 식별되지 않아 version/commit/tree/release date를 null로 두고 current official archive bytes만 pin했다. Last-Modified, tar member mtime, PDF creation timestamp를 software release date로 둔갑시키지 않았다. Licence/dependency가 확인되지 않은 필드도 null과 unresolved 사유로 보존했다.

## 원 Deep Research DB

원 ZIP expected reported SHA256: `ab875d3e4fa771b34bdc1026042c38553b473b98f23e00e809d21c3b367948a9`. 접근 가능한 파일의 exact/short title 검색, Drive filename 검색, 지정 Dropbox folder에서 찾지 못했다. `original_deep_research_db_recovered=false`.

`WU088_HH_R31AO_LITERATURE_DATABASE_RECONSTRUCTED_20261001_v1.zip`를 별도 생성했다. 원 보고서의 명시적 SQL schema·source CSV 4개·blocker CSV 5개, 전체 보고서/표와 acquisition crosswalk만 복원했다. 원 보고서가 주장한 전체 19 source/9 theorem/9 module/15 test/7 artifact/8 blocker export는 원 record가 없어 재현하지 않았다. Semantic equivalence는 `UNVERIFIED_NOT_CLAIMED`; 재구성본을 원본으로 부르지 않는다.

## 남은 gap과 bounded 종료

INTLAB 14.1은 개인 유료 licence 경로, COSY 10.2는 개인 registration·서명 licence 경로다. 이를 우회하거나 등록·서명·결제를 하지 않았다. 공개 legal fallback 탐색은 성공 경로 또는 명시적 licence wall에서 종료했다. 새로운 동일 URL retry는 1회 이하이고, PDF 오류 HTML을 원문으로 저장하지 않았다. 두 논문에 arXiv 정확 일치본은 검색에서 확인되지 않았으나 기관 원문으로 closure했다. 원 DB는 접근 가능한 bytes가 없어 부분 재구성까지 수행했다. 이것은 환경 때문에 모든 fallback 탐색을 수행 못한 C 상태가 아니라, 원문 회수 작업을 끝내고 3개의 명시적 미확보 항목을 남긴 B 상태다.

## 검증·범위

`science_commands=0`, `science_producer_commands=0`, `numerical_certificate_runs=0`, `downloaded_code_executions=0`, `native_builds=0`.
`B_ORDER_VERDICT_STABLE_OVER_128_160_192`, `SOURCE_ACCURACY_BOUND_UNAVAILABLE`, `RIGOROUS_REFERENCE_CERTIFICATION_BLOCKED_BY_MISSING_ERROR_BOUND`, `certified_epsilon=null`, `certified_eta=null`, `rigorous=false`를 보존한다.
Original DB rows를 그대로 유지하고 child/versioned record만 추가했다. SQLite integrity와 원 row 포함 여부를 확인했다. New PDF 2개 magic/page count, PostScript magic/DSC 15 pages, source tar 13 member integrity를 검사했다. OCR, PS 실행/변환, scientific code 실행은 하지 않았다.

## 봉인·publication·backup binding

이 self-contained 패키지는 provider upload와 최종 Git metadata publication 전에 봉인된다. 실제 upload ACK·object ID·remote parent/path·metadata size/checksum 및 final commit/tree는 detached `RETURN.json`/backup receipt에 기록한다. 이 파일의 수집 completion과 remote backup verification은 분리한다. Content-part ZIP들의 member union은 canonical package tree와 동일하도록 검증한다. 실제 remote download/readback가 없으면 `RESTORE_VERIFIED=false`다. 기존 두 automatic acquisition workflow는 collector commit에서 제거했고, 성공 결과를 보존한 후 새 임시 workflow도 최종 metadata commit에서 제거한다. Public Git에는 원문·third-party archive를 넣지 않는다.
