# WU 다음 연구 루프: 백업 current delta

- 조사 기준시각: `2026-10-23T22:11:41Z` 이후.
- 관찰 상한: `2026-10-24T00:47:23Z`.
- 역할: 읽기 전용 metadata corroboration과 작은 저장 receipt/capsule의 텍스트 확인.
- 원응답: 이 디렉터리의 JSON 파일. 기계 판독 요약은 `BACKUP_DELTA_SUMMARY.json`.
- 과학 실행, 과학 재실행, test, lease 획득, archive 전체 다운로드, provider 변경: 모두 0.

## 판정

WU 양쪽 알려진 백업 폴더에서는 기준시각 이후 새 PHYS84 완료·예약 또는 PHYS85 artifact를 관찰하지 않았다. 기존 PHYS84 final ZIP/JSON의 provider ID와 크기는 주어진 완료 인계와 일치한다. 이 agent는 원격 archive bytes를 다시 받거나 SHA/CRC/payload를 검증하지 않았다. 그 작업은 root의 분리된 복구 경로에 맡겼다.

관련 lane에서는 기준 이후 **Drive BASS B3a 검토 전 capsule 1개**와 **Dropbox VIGILODE V1Q 단계 archive 3개**가 새로 확인되었다. 전자는 텍스트를 읽었고, 후자는 metadata만 읽었다. 둘을 WU science 완료로 세거나 전체 결합 solver 완료로 승격하지 않는다.

## 조사 범위

| Provider와 범위 | 반환 entry | 페이지·한계 | 기준 이후 |
|---|---:|---|---:|
| Drive WU 폴더 `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM` | 527 | top_k1000, cursor 미노출 | 0 |
| Dropbox WU 지정 폴더 | 496 | has_more=false, direct children 완료 | 0 |
| Dropbox dossier root | 3,396 | 6페이지, 고유ID3,396, has_more=false | 0 |
| Dropbox `/BASS_BACKUPS` | 127 | has_more=false | 0 |
| Dropbox dossier의 `bass_cr` | 76 | has_more=false | 0 |
| Drive dossier root `1pkohlay5eIfFJsBwPZ_yn2jIZONZjesI` | 1,000 | 제한 도달; 별도 parent+time 검색0 | 0 |
| Drive BASS backup 폴더 `1fFxb-qgExWbEomt3EbbOjGKcslFpGv3y` | 74 | cursor 미노출 | 1 |
| Drive CR 폴더 `1V4ZQza59dWVC7apeRz9P1TL66eaVYyJy` | 74 | cursor 미노출 | 0 |
| Drive REC 연구백업 root | 17 | direct children, 대부분 과거 폴더 | 0 |
| Drive REC 20261016 폴더 | 16 | direct children, 과거 폴더 | 0 |
| Drive REI 별도 root | 13 | direct children, 과거 폴더 | 0 |
| Drive REI 연구백업 폴더 `1phclg92jkhC5KgvnXhks8GbOFlya4qGe` | 182 | cursor 미노출 | 0 |
| Dropbox `/bianchi/rec_bianchi/20261016` | 96 | has_more=false | 0 |
| Dropbox `/bianchi/research_backups/rei_bianchi` | 90 | has_more=false | 3 |

위의 명시적인 exhaustion은 **해당 Dropbox 폴더의 direct children**에만 적용한다. 모든 하위 폴더, 모든 branch tree, 비공개 대화, 다른 저장 위치까지 전수 판독했다는 뜻이 아니다.

## WU 기존 완료 artifact의 현재 metadata

| Artifact | bytes | Drive ID | Dropbox ID |
|---|---:|---|---|
| PHYS84_FINAL_20261023_d5c2c8dbbbd7.zip | 7,891,881 | `1rxXN-56CUfPU8fDk1l-TJ8nP6OSoiMUD` | `id:BSpOijBcT10AAAAAAD_6ug` |
| PHYS84_FINAL_DELIVERY_20261023.json | 307,868 | `16Zepz-r4hWxIpoOzDACYE7nLF4LHFiDV` | `id:BSpOijBcT10AAAAAAD_6vQ` |

주어진 ZIP SHA256은 `dd68666ae61b202c21d9bff502bf9972d06926159018eb703c5518c4fff038cc`, final JSON SHA256은 `5bc989c1549eb4473b99cb6d3cc3502e98dc18ca561988e8f6d23d7c409f8395`다. 이 두 값은 parent가 준 기대 identity이며, 이 agent의 새 bytes 검증값으로 표기하지 않는다. Drive metadata 요청에서 SHA field를 요청했지만 normalized 응답은 hash를 반환하지 않았다.

Drive ZIP modified는 22:01:22.297Z, Dropbox ZIP은22:01:29Z다. Drive JSON은22:09:06.581Z, Dropbox JSON은22:09:10Z다. S0/S1 단계 artifact도 목록에 있지만 해당 ACK와 final 전체복원은 별개 수준이다.

## 새 BASS B3a capsule

[Drive 문서](https://docs.google.com/document/d/18hTBCoLnlKcOd1AlM48BkF6dyga0n7Xj-BiONxMAMlU/edit) 제목은 `BASS_B3A_20261024_PRE_REVIEW_RESEARCH_CAPSULE`, modified는 **2026-10-23T22:11:51.573Z**다. 원문은 `BASS_B3A_NEW_CAPSULE.json`에 저장했다.

문서가 스스로 제한하는 범위는 다음과 같다.

- BASS PR184 / owner HEAD `28b7705cbb236c26e1b273335f6da7e9da4d1aaf` 기준의 **PRE-REVIEW** 준비 연구다.
- 국소 Wolfram 참조 구현은 21개 시험그룹 true, 0 false, 12 covariance 사례, 6 electron-rest 비교를 기록한다. 이는 저장된 저자 결과로 재사용하며 이번에 실행하거나 독립 검증한 것이 아니다.
- native Python/Rust adapter, independent model review, source push, 실제 REC/HE 결합 history는 **NOT_RUN**이다. production은 **HOLD**다.
- 일반 emission에서 `Q0 = beta·Qsp + alpha/gamma`를 보존하며 elastic shortcut의 적용 범위를 제한한다. electron momentum source와 전체 gas closure도 구분한다.
- 기존 remaining budget은 null이고 reset=false다. 새 WL 요청6개의 timeConstraint합120s는 사용 완료, 측정 kernel 부분합은 wall0.693829s/CPU0.697921s이며 전체 connector 경과시간이 아니다.
- CloudExport가 `$Failed`를 반환한 사실을 보존한다. Native Doc text identity와 원 Wolfram Export source bytes identity는 별개다.
- B3a의 준비용 결과를 B3 전체결합 또는 R/C20단계 전체완료로 승격하지 않는다.

## 새 VIGILODE metadata

| 단계 archive | Dropbox ID | bytes | modified UTC |
|---|---|---:|---|
| VIGILODE_V1Q_S1_20261024.zip | `id:BSpOijBcT10AAAAAAD_6vg` | 10,388 | 2026-10-23T22:12:51Z |
| VIGILODE_V1Q_S2_20261024.zip | `id:BSpOijBcT10AAAAAAD_6vw` | 1,390,704 | 2026-10-23T22:21:24Z |
| VIGILODE_V1Q_S3_20261024.zip | `id:BSpOijBcT10AAAAAAD_6wA` | 1,406,678 | 2026-10-23T22:30:56Z |

위 파일들은 `/bianchi/research_backups/rei_bianchi`의 실제 목록과 별도 VIGILODE 검색에서 일치했다. archive의 완료·검토·runtime·budget·입력 identity는 **내용 미판독**이다. 파일 이름 S3만으로 완료로 판단하지 않는다. 동일 cutoff로 Drive VIGILODE name 검색은0이지만 다른 위치/접근성까지 포함한 부재 증명은 아니다.

## 함께 읽은 과거 소형 receipt

### HE-ANG

`HEANG_DELIVERY_INDEX.json`은 Dropbox `id:BSpOijBcT10AAAAAAD_6mA`의 읽기 결과다.

- science pin `896e5427100ad48d017deff2697b6f992ba029cd`, delivery pin `0a11bf9e1f6ffcc696625de0caf1c581c27cf7f0`.
- science manifest SHA256 `ea7a49e97515195317972b5897ba6511527093484aa8ed5025a5cd01e96bfc3f`.
- contract COMPLETE_SCOPED이지만 parent HE-ANG은 SOURCE_INPUT_PENDING, next HE-ANG-SOURCE다.
- 백업 claim은 local SHA와 upload ACK/Drive size-ID metadata다. immediate remote-byte redownload는 하지 않았다고 명시한다.

그 후의 source recovery/diagnosis metadata도 보인다. Dropbox 최신 diagnosis는 `id:BSpOijBcT10AAAAAAD_6tg`,18,990bytes,21:38:58Z다. Drive에는 다른 이름의 code-recovery15908bytes가 있어 이를 동일 archive로 등치하지 않는다. 이들은 기준시각 이전이고 내용은 읽지 않았다.

### CR C23C

`C23C_TERMINAL_TRANSPORT_RECEIPT.json`은 Dropbox `id:BSpOijBcT10AAAAAAD_6lg`의 읽기 결과다.

- science commit `54c2ff11e8308d45c545679301059bc1fcf268eb`, document commit `6c760dc1f0ce5820263b276fa7263e87c1285bd2`.
- N4 cutoff binding과 N5 bookkeeping contract는 COMPLETE_SCOPED이다. stopping kernel, physical heating/stopping, full empirical coverage, coupling과 new parcel은 OPEN이다.
- main/final-document Library+Dropbox R3 복원 claim을 보존한다. main Drive는 UNKNOWN_NO_ACK, final-documents Drive는 NOT_ATTEMPTED라는 차이를 보존한다.
- 현재 Dropbox CR 폴더 latest는 N4_ADMISSION_RECOVERY archive `id:BSpOijBcT10AAAAAAD_6tA`,4,927,084bytes,21:36:04Z다. 그 archive 내용은 읽지 않았다.

### REC

`REC_HISTORY_FINAL_CHECKPOINT_RECEIPT.json`은 Dropbox `id:BSpOijBcT10AAAAAAD_6mw`의 과거 receipt다. parent REC_HISTORY는 PARTIAL이며 당시 publication blocked 상태를 기록한다. 이 과거 상태는 이후 PR130의 현재 publication 근거를 덮어쓰지 않는다.

checkpoint ZIP의 SHA256은 문서상 `3f579aca52addb0bc1b638ca23d8e733567696f5479323c00489d097c5d5f110`,8,642,495bytes다. Drive `1Famz_CeEmmf813Ex1M3CvzRKl5cNV862`의 현재 metadata도 같은 size/title을 반환했다. 해당 receipt는 ACK+metadata와 remote whole-byte readback NOT_RUN을 구분한다.

Dropbox REC 최신은 `REC_HISTORY_ADM01_STAGE_A_20261024_3ec64a7e04f2.zip`, `id:BSpOijBcT10AAAAAAD_6uw`,307,368bytes,22:05:13Z다. 기준 이후 추가 object는 direct listing에서 관찰하지 않았다.

## 검색과 주장 한계

Dropbox 넓은 REI/REC/CR/BASS 검색은 last_modified_after와 title_only를 줬는데도 2024항목, folder, `BOTH_FILENAME_AND_CONTENT`를 반환했다. 따라서 검색 결과의 has_more=false를 그 시간대 전수성으로 해석하지 않았다. HE 검색은 INVALID_ARGUMENT/internal error를 반환했다. 원응답과 실패를 보존하고 실제 폴더 pagination을 주된 근거로 삼았다.

Drive search와 list는 접근 가능한 object를 반환하는 connector 관찰이다. 미노출 cursor, root listing의1000제한, 다른 폴더·비공개 대화·전체 branch contents는 남는 범위 제한이다. 현재 조사에서 관찰한 metadata만으로 새로운 과학적 수용, resource lease, 예산 재설정 또는 production admission을 부여하지 않는다.

