# R4 준비: 7개 저장소의 현재 권위·병렬 작업·보존 근거 대조

## 판정과 조사 종료점

이 조사는 **R4의 입력 권위를 고정할 수 있는 상태로 완료**했다. WU의 원래 로컬 20개 노드는 **엄격한 scoped 완료 5/20**, 별도 구현 검증 통과 2/20이다. 준비·부분 완료를 완료로 세지 않는다. 중앙의 실제 88개 노드에서 `COMPLETE*` 상태는 **18/88**이며, owner가 선언한 더 넓은 scoped 집계 **27/88**, 별도 미병합 작업 집계 **32/88**와 구분한다. 어떤 값도 전체 물리망의 완료율이 아니다.

원격 목록은 7개 저장소 모두 마지막 페이지까지 확보했다. 마지막 선별 ref 관측은 **2026-10-27 03:37:53 UTC**다. 이후 움직이는 다른 owner를 계속 추적하며 이 조사를 무기한 연장하지 않는다. Root가 추가로 관측한 CR `e7075044550dc04fd09f8ea633076d85d4ae7a99`(03:39:33 UTC)는 별도 후속 preflight 관찰이며 이 고정 조사에서 과학 판정을 내린 commit이 아니다.

## 실제 목록 조사 범위

| 저장소 | 열린 PR 수 | PR 페이지별 건수 | 브랜치 수 | 브랜치 페이지별 건수 |
|---|---:|---|---:|---|
| WU088_HH | 150 | 100, 50 | 159 | 100, 59 |
| rei_bianchi | 222 | 100, 100, 22 | 279 | 100, 100, 79 |
| rec_bianchi | 104 | 100, 4 | 157 | 100, 57 |
| BASS_HE | 102 | 100, 2 | 107 | 100, 7 |
| bass_cr | 106 | 100, 6 | 185 | 100, 85 |
| bass | 162 | 100, 62 | 277 | 100, 100, 77 |
| vigilode | 59 | 59 | 215 | 100, 100, 15 |
| 합계 | **905** | 모두 종료 페이지 확인 | **1,379** | 모두 종료 페이지 확인 |

각 목록은 `per_page=100`을 사용했고 100 미만을 반환한 마지막 페이지까지 받았다. 번호·제목·head/base·갱신 시각·URL·모든 브랜치 head는 `REMOTE_LISTING_SNAPSHOT.json`에 있다. 이 전수 범위는 **열린 PR과 브랜치의 metadata 목록**이다. 모든 과거 PR 본문, 닫힌 PR, 개인 대화, 모든 논문·과학 artifact를 읽었다는 뜻이 아니다. 선택한 최신 PR 본문과 실제 문서의 범위는 각각 `SELECTED_PR_BODIES.json`, `DOCUMENT_SNAPSHOTS.json`에 고정했다.

PR 목록만으로 최신 작업을 결정하지 않았다. REC의 새 source-synthesis와 VigilODE의 adapter-switcher 작업은 열린 PR 없이 브랜치에 있었다.

## 현재 WU와 정확한 분모

WU의 로컬·원격 head는 [bfdeed6766](https://github.com/cosmosapjw-quantum/WU088_HH/commit/bfdeed676617c8b75ed81ac5e79e800fa69f83db), PR150이다. 로컬 worktree가 clean인 것을 확인했고 최신 root AGENTS blob은 `10e761bfecb8ebc620caefce95e14a4f49811b81`이다. R3 원행·source·registry·admission과 기존 결과는 재실행하지 않았다.

| 원20노드의 분류 | 개수 | 해석 |
|---|---:|---|
| `COMPLETE_*` | **5** | CE83, R1 supplier rows, R2 original-target identity, R2 integer columns, R3 EXFOR source |
| 구현/PASS만 인정 | **2** | 합성 finite compiler와 R1 projection의 구현 근거 |
| PARTIAL | 8 | 전체 registry·물리 source/binding 등 미완 |
| READY_DESIGN | 2 | 설계 준비, 완료 아님 |
| SOURCE_INPUT_PENDING | 2 | 실제 선행 입력 미완 |
| OPEN | 1 | He/Li CX 상태·에너지 공급 의존성 |

정확한 node ID와 원 status는 `WU_ORIGINAL20_COUNTS.json`에 있다. 완료 5개에도 원자료 회수와 정수 장부 하위 계약이 포함되므로 **물리 consumer 5개 완료**라고 표현하지 않는다. 원19 target·28방향의 source-reference availability는 **28/28**이지만 실제 rate/Q/state/branch/energy/consumer/activation 승인은 별개다.

Root가 R4 하위노드 4개를 별도로 추가하면 확장된 분모는 24가 된다. 초기 표기는 **확장 DAG 5/24, 원20 기준 5/20, 구현 통과 2개 별도**이며, 새 하위노드 추가만으로 완료 수를 늘리지 않는다. 연구 R1–R10와 코딩 C1–C10의 20단계 진척, 게시와 각 백업 상태도 별도 축으로 기록해야 한다.

## 중앙 권위 변화

중앙 head는 a5db4bac에서 [12f6007a83](https://github.com/cosmosapjw-quantum/rei_bianchi/commit/12f6007a83a40d76f80574e41a5402676e81fc7a)로 이동했다. 큰 DAG의 raw-file 읽기는 400을 반환했지만, exact Git blob fetch로 이전·현재 전체 JSON을 직접 받아 대조했다.

- 이전 blob: `f898e3130242e108c05bfc75751cb5d268654019`
- 현재 blob: `1f1cf17308c01614eef1334a619e79e6b68c999b`
- 노드 88개, authorities 15개, edges 17개를 보존했다.
- 바뀐 것은 B3g, B3i, B2-G1C의 상태·후속 행동·관찰 필드뿐이다.
- 다른 85개 노드와 **WU lead 14개 전체 객체는 동일**하다. 따라서 중앙에 WU R1–R3의 최신 진전이 수신 승인됐다고 가정하지 않는다.
- 기존 중앙 문서의 87-node frozen snapshot과 pending 문구는 역사적 원본이다. 현재 88-node DAG 및 해당 후속 영수증을 우선 해석한다.

[PR236의 GLOBAL_DAG_STATUS](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/ee94bef85b56d879dc38f184856a5c613575e9e1/research/rei_expanded_event_consumer/coupled_source_20261027/GLOBAL_DAG_STATUS.json)는 작업32/88, 중앙27/88, 미병합, 새 canonical 완료0을 명시한다. Literal COMPLETE 18/88과 이 declared scoped 집계를 섞어 한 완료율로 만들지 않는다.

## 실제 새 병렬 결과와 재사용 경계

| 소유자·관측 head | 직접 확인한 현재 상태 | WU가 보존할 경계 |
|---|---|---|
| REI PR237, `20b9160649` | [C5 IMPLEMENTED_NOT_EXECUTED](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/20b91606493fb7bad015c62fd62e2faa971faee0/research/rei_expanded_event_consumer/thermal_assimilation_20261027/stages/C5.md). Native25 thermal join/JVP/checker 작성, 실행 전 | PW19 source와 HE caloric 호출의 기존 결과 재사용. 조건부 relaxation을 물리 stopping provider로 승격하지 않으며 이 구현을 중복 작성하지 않는다. |
| REC 별도 branch, `6d0ddf5f57` | [R8 theory decision](https://github.com/cosmosapjw-quantum/rec_bianchi/blob/6d0ddf5f575616babd049638294b28bd5f4d31a5/research/rec_source_synthesis_20261027/THEORY_DECISION.json): HD paired thermal·retiming/chord 유도, 코딩 준비 | 24 HD 진단값·313 retiming 실제 새 계산은 아직 열려 있다. 원 7/8 line-gap FAIL, H5 epsilon=null·0/313, H6/H7 OPEN을 보존한다. |
| CR PR107, `6d6e872a43` | [R8](https://github.com/cosmosapjw-quantum/bass_cr/blob/6d6e872a430d0a9dcbdb578312007be55676b6e1/research/cr_heiii_ground_rr_20261027/stages/R08.md): 이론8/20, HeIII consumer0/1, bounded implementation 채택 | Elemental-He→He4 조건부 대응, stationary target, ground spontaneous, fixed saved bath를 유지한다. HeIII RR consumer를 중복 실행하지 않는다. |
| HE PR102, `ac6042a6b0` | 기존 HE-EXP-INTAKE01의 source·조건부 구현 전달 | 31 distinct methods와 원 첫 실패/표적 수정, HE101 C8/reserve0를 재사용한다. 20,000 K·92 IDs에 관한 새 대화는 게시 계획으로 확인됐고 새 검증된 commit을 확보하지 못했으므로 완료에 더하지 않는다. |
| BASS PR192, `af14fc72d9` | [새 admission](https://github.com/cosmosapjw-quantum/bass/blob/af14fc72d99f6d0e396f60aedadcdb5d05213280/research/bass_b3g_midpoint_transport_20261027/ADMISSION.json): 512 midpoint/final map, finite RK4 bound, 10 checks, 2 final RHS 소비 | Manufactured cold/non-tilted/recoil-free 모델 한정. 실제 물리 radii·흡수·calibration은 OPEN이며 현재 새 source의 백업을 이전 ZIP으로 대신 인증하지 않는다. |
| VigilODE 별도 branch, `0d3c7c510c` | deterministic work/cap·direct 9-cell 동일성에 대한 adapter economy 결과 | Wall-time 표는 drift 때문에 진단용이다. 새 WU physical RHS/Jacobian/domain, 일반 V6, 생산 승인을 뜻하지 않는다. |

개인 문맥에서 언급된 “V03 PR41”의 실제 `vigilode#41`은 **2026-08-31 candidate-free handoff**이며 head `9fbdd84c…`였다. 새로운 V03 게시와 일치하는 locator를 확인하지 못했으므로 완료로 더하지 않는다.

## CI 알림의 실제 의미

기존 run/job/log를 읽었고 실행·재시작·수정은 하지 않았다.

| 실제 head / run | 직접 관측한 실패 | 후속 과학 시험 |
|---|---|---|
| REI 중앙12f6007 / 40443802688 | `cargo fmt --check`의 Rust formatting diff, exit1 | cargo test SKIPPED |
| REI fdc782b / 40444261003 | 동일 formatting gate | cargo test SKIPPED |
| REC22fde058 / 40443051429 | `verify_repo --quick`의 committed-feature whitespace/EOF gate | pytest SKIPPED |
| REC6d0ddf5 / 40444586094 | 같은 gate; 기존 파일과 새 survey EOF 항목도 포함 | pytest SKIPPED |

REC의 workflow명이 `verify-durable-backup`이라는 사실은 cloud ZIP 유실이나 업로드 실패를 증명하지 않는다. CI green을 주장하지 않으며 scoped 과학 admission도 이 서식 실패만으로 취소하지 않는다. 실제 job ID·단계·짧은 직접 로그 발췌는 `CI_OBSERVATIONS.json`에 있다.

## 게시·백업 locator

`DELIVERY_LOCATORS.json`은 저장소에 게시된 실제 영수증에서 source commit, stage, ZIP SHA/size, Dropbox/Drive ID를 회수했다. Root가 정확한 ID의 현재 cloud metadata를 별도로 대조한다.

- **WU R3:** 7,274,563 B, SHA `f83ea212…`, Dropbox `id:BSpOijBcT10AAAAAAEC3dA`, Drive `1Glyh10AUFixjz4cTWJPNx6ypm-3ErnuX`. 기존 양쪽 actual-byte 확인을 재사용했다.
- **REI preexecution:** 237,911 B, SHA `85110ebc…`, Dropbox `id:BSpOijBcT10AAAAAAEC3oA`, Drive `1jpOGQ9k-xWpGNUxD2rWXsPaSo0e3CMqf`. R2–R6/C1–C4 snapshot을 보존하며 이후 C5 자동 포함을 뜻하지 않는다.
- **REC R7:** 3,856 B, SHA `9b73d7d0…`, Dropbox `id:BSpOijBcT10AAAAAAEC3og`, Drive `1PKlK9w5lV5099Rq3n1xwyHDDXUzNsvp4`.
- **CR R7:** 81,392 B, SHA `20f3c7f2…`, Dropbox `id:BSpOijBcT10AAAAAAEC3pQ`, Drive `1m1IQ8D00ILg_AB4CNziQdPM-9CSNeUlY`.
- **HE의 기존 source:** 1,013,057 B, SHA `0405ee88…`, Dropbox `id:BSpOijBcT10AAAAAAEAbGA`, Drive `1yANHEfXKlBQqMX5PbLvty_Fdm_C1_kgf`.
- **BASS 새 af14 source:** 검토한 science commit에는 성공 후 작성될 새 전달 영수증이 아직 없다. 이전 B3g 38,152,861 B ZIP과 그 ACK는 이전 결과의 보존 근거다.
- **VigilODE D5 S3:** 565,668 B, SHA `99128c00…`, Dropbox `id:BSpOijBcT10AAAAAAD_9zg`; Drive는 `NOT_ATTEMPTED_AFTER_TWO_UNACKNOWLEDGED_CALLS`다. 새로운 양쪽 백업 성공을 주장하지 않는다.

WU를 제외한 위 선별 새 stage 영수증의 대부분은 **upload ACK + metadata size** 범위다. 이를 새 whole-byte SHA 재다운로드로 바꾸어 표현하지 않는다.

## R4에 적용할 결정

R4는 WU가 실제로 소유하는 한 source/state/branch/measurement binding을 고정하여 진행한다. 현재 진행 중인 REI thermal join, CR HeIII RR, REC HD/retiming, BASS midpoint, VigilODE performance 작업은 재사용·참조 대상으로 남긴다.

검토한 최신 반환에서 실제 MeV photon number-density/flux·time/volume consumer는 발견하지 못했다. REI frozen PW19 support는 0–49,945.58 eV이며 이를 핵 광붕괴의 MeV 영역으로 외삽하지 않는다. Root의 별도 원자료 intake에서 회수한 구체적 WU 입력과 C1 계약을 사용하고, source/구조 승인과 실제 rate/Q/consumer 승인을 분리해야 한다.

사용자 지정 physmath 1.0.0/e1 규약과 요청된 전체 R1–R10/C1–C10을 유지한다. 설치 plugin의 단일-stage 기본값을 전체 루프 축소에 사용하지 않는다. 모든 기존 source·계산·실패·예산을 보존했고 foreign repository 수정과 과학 재실행은 모두 **0**이다.

