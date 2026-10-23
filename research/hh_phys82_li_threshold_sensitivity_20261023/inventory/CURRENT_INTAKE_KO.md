# PHYS82 R2/C2 현재 의존성 조사

## 결론

PHYS82는 확인된 PHYS81 최종 HEAD `b3ec271a96cb67e583bffa9b61533802838236f9`의 후속 작업으로 진행할 수 있다. 이번 read-only intake에서 Li7 실제 문턱–6 eV 원전 공백을 닫는 완료 결과는 확인되지 않았다. `LOW_T_CI_SOURCE_COVERAGE`는 그대로 열린 과학 의무다.

새로 유용한 sibling 결과는 **BASS_CR C23A의 source 공급·전자 침적·β energy coverage**와 **HE37의 제한된 H1 differential gain/net source checkpoint**다. REI ANGTHERM01은 prepared inputs/theory contract이며 아직 새 IVP 결과가 아니다. REC126은 기존 저장 상태의 C2 진단 비용 분석으로, PHYS81 최종 조사보다 먼저 게시됐지만 그때 직접 선택한 본문 목록에는 없던 관련 자료다.

이 판단은 아래 실제 원격 읽기와 고정 commit의 producer 근거를 종합한 것이다. 이 intake가 producer 과학 결과를 재계산하거나 독립적으로 재검증한 것은 아니다.

## 실제 수행 범위

- 2026-10-23 02:22:28 UTC부터 기록된 6개 repo × 최근 갱신 PR 5개 = **30 PR metadata/body**를 읽었다. 요청은 `state=all&sort=updated&direction=desc&per_page=5`다.
- GitHub read-only fetch **31회**, Drive metadata **2회**, Dropbox metadata **2회**, Drive 검색 **2회**, Dropbox 검색 **2회** = connector **39회**.
- 현재 parent와 변경 branch의 별도 ref 읽기 4회, 실제 commit compare 4회가 포함된다.
- 선택된 실제 원격 텍스트 **16개**를 `pinned_sources/`에 보존했다. **15개**는 알려진 Git blob SHA1 또는 보존 parent byte identity와 일치했다. REC126 C3 handoff 1개는 고정 commit에서 받은 내용과 로컬 SHA256까지 결속했으며 별도 원격 blob SHA1은 노출되지 않았다.
- 새 과학 실행 **0**, 완료 과학 재실행 **0**, 구백업 다운로드 **0**, 원격 쓰기 **0**, 외부 host/process inspection **0**.
- 기존 51 repos / 2,175 refs 전수조사는 역사적 근거로 재사용했다. 현재 최신 5 PR 조사로 모든 branch 또는 모든 대화의 완전성을 주장하지 않는다.

`RAW_CURRENT.json`은 실제 요청·관측 UTC·선택 응답을 담는다. PR 본문과 compare 파일 identity 목록은 보존했고 반복되는 actor/repository wrapper는 생략했다. `CURRENT_USE_IDENTITY_MAP.json`은 30 PR의 이전 선택 snapshot과 현재 관측을 연결한다.

## Parent와 정책

[PHYS81 PR137](https://github.com/cosmosapjw-quantum/WU088_HH/pull/137)의 현재 PR head와 별도 `git/ref/heads/research/hh-phys81-atomic-nuclear-source-contract-20261023`는 모두 `b3ec271a96cb67e583bffa9b61533802838236f9`다. Branch base는 PHYS80 `951182dd59bbb59dba454bbaab78ad56d029355a`다. 현재 root가 정한 실제 parent와 일치한다.

고정 HEAD의 `AGENTS.md`는 30,446 bytes, SHA256 `7d21612e3d78d2d849ffa6421ed61cd6b2fa198c832217a129a0aebce2fd0c70`, Git blob `83e41056ef39af8183152f93a32d1285bb1a7f2c`다. 로컬 보존본과 현재 원격 수신 bytes가 같다. 상단 PHYS71 우선순위는 보존된 역사다. 같은 HEAD의 PHYS81 `POLICY_OVERRIDE.json`은 SHA256 `a435743ad5dd9762da3a8e2a1f788df1d17a2df9a87e09eca05419ce95f3aae1`로 현재 수신 bytes와 일치한다.

현재 과학 의무의 변경분만 수행하고, 완료된 과학/입력 identity와 역사 파일은 보존한다. HH_R10=OFF, Production NOT_ISSUED, no main merge, shared lease, 다른 process 종료 없음, source/domain/energy 결속을 먼저 한다는 조건은 유지한다. 이 child는 R2/C2 read-only intake만 수행하며 publication은 root 소관이다.

PHYS81 최종 reference delta 안의 PR137 snapshot은 당시 중간 commit `a27bc238...`였다. 현재 `b3ec271...`와의 차이를 외부 donor의 새 과학 결과로 오해하지 않는다. 해당 PHYS81 최종완료는 parent task와 PR137 최종 delivery identity가 소유한다.

## 변경된 refs와 재사용 판단

| 대상 | 직전 관련 identity | 이번 실제 관측 | 판단 |
|---|---|---|---|
| WU088_HH PR137 PHYS81 | task parent b3ec271… | b3ec271… | 현재 parent 일치 |
| BASS_HE PR89 HE36 | 6403055… | 6403055… | 그대로 재사용 |
| BASS_HE PR90 HE37 | 직전 선택 snapshot에 없음 | 첫 PR collection e7b9851… → 별도 branch d618344… | 조사 중 진행한 새 H1 source checkpoint |
| bass_cr PR96 C23A | ba39fc7… | collection 7643af2… → branch 215defe… | 새 C23A science 뒤 delivery-only 1 commit |
| rei_bianchi PR221 | 73c5e00… | 00303ab… | ANGTHERM01 prepared theory/input checkpoint |
| rec_bianchi PR127 ANGULAR01 | 5185c39… | 5185c39… | 그대로 재사용 |
| rec_bianchi PR125 THERM02 | b28b387… | b28b387… | 그대로 재사용 |
| rec_bianchi PR124 | e6ecef7… | e6ecef7… | 그대로 재사용 |
| rec_bianchi PR126 C2 | 이전 직접선택 없음 | 1206889… | 저장 diagnostic 분석; 새 IVP 없음 |
| bass PR181 / PR180 | 797d665… / 574c3af… | 동일 | 그대로 재사용 |

전체 30행의 역사적 직접선택 비교는 HEAD_IDENTICAL 19, HEAD_CHANGED 3, NO_DIRECT_SELECTED_BASELINE 8이다. HEAD_CHANGED 3에는 방금 설명한 PHYS81 자기 최종화가 포함된다. 직접 baseline이 없는 8개를 모두 새 과학 결과라고 세지 않는다.

### C23A: 유한 source component의 실제 완료 결과

Science commit `7643af28c671a7473754a3c2cd0c6e523bd61aac`, delivery commit `215defe6f631050255b73baec83e9418a8a2b66f`. 첫 compare는 이전 `ba39fc...`에서 새 C23A unit만 추가한다. 두 번째 compare는 `delivery/` 아래 8개 파일만 추가하고 기존 과학 파일을 변경하지 않는다. [고정 보고서](https://github.com/cosmosapjw-quantum/bass_cr/blob/7643af28c671a7473754a3c2cd0c6e523bd61aac/research/cr_c23a_external_supply_20261023/REPORT_KO.md), [최종 handoff](https://github.com/cosmosapjw-quantum/bass_cr/blob/215defe6f631050255b73baec83e9418a8a2b66f/research/cr_c23a_external_supply_20261023/delivery/HANDOFF_KO.md), [최종 DAG](https://github.com/cosmosapjw-quantum/bass_cr/blob/215defe6f631050255b73baec83e9418a8a2b66f/research/cr_c23a_external_supply_20261023/delivery/NEXT_DAG_FINAL.json).

재사용 후보는 다음과 같다.

1. **P19 H/He photo subflow**: 원본 59 redshift × 2 inventory × 7 exposure = 826 saved source responses, 1,652 half-step compositions. 양의 He birth-chain 해석식을 사용하며 283 rate cases / 1,915 calls의 80자리 oracle과 28 invalid cases를 producer가 검증했다. 범위는 고정 proper volume·고정 z, H/He 5-state source component, 0≤z≤15.1이다. z20으로 외삽하지 않으며 Li/D/T까지 포함한 21-state full gas를 대체하지 않는다.
2. **FS2010 유한 전자 침적 연산자**: 10–9937.21 eV, 14×258 원표, 양의 PL spectrum과 정확한 해당 보간모델 사전적분. 21cmFAST MIT mirror의 numeric token identity와 마지막 newline byte 차이를 구분한다. 표의 ionization-coordinate/header 불일치·energy closure defect·He/H 미확정을 보존한다.
3. **β source-domain coverage**: historical ENDF/B-VIII.0 neutron/T의 Q·평균 전자 운동에너지에 결속한 조건부 bound. 같은 frame, 양의 분포, [0,Q] support 가정에서 neutron 전자 운동에너지 중 FS table 밖 비율 ≥97.9467539824%라는 producer 결과다. Heating fraction, confidence bound 또는 실제 β spectrum으로 승격하지 않는다.

P19의 Γ,H 두 moment로 cascade spectrum을 유일하게 정할 수 없다. Producer는 같은 전자 수·평균 100 eV인 두 spectrum의 FS heat가 86.49070834 대 81.91488963 eV인 유한 예를 보존했다. 따라서 PHYS81 nuclear photon/recoil 장부와 결합할 때 actual electron spectrum, source gas composition, 같은 frame, tail continuation, finite stopping, primary binding/photoheat/cascade의 energy owner가 추가로 필요하다. 이 결과를 Li7 CI threshold-to-6 eV 원자료로 사용할 수 없다.

Producer final handoff는 Library/Dropbox main archive·authority의 실제 R3 readback을 보고하고 Drive는 UNKNOWN_NO_ACK로 남긴다. 이 intake는 해당 sibling archive를 다시 받지 않았으므로 producer-reported receipt의 범위다.

### HE37: 진행 중 checkpoint에서 확보된 H1 gain/net source

첫 PR collection은 `e7b985140503dacb4b5d4e666d3fd65cb07bc5be`를 돌려줬고, 뒤의 실제 branch는 `d618344413193950ec3e4e499be526d1ed636d98`였다. 두 commit 사이 64 paths의 1-commit compare를 보존했다. PR body의 “현재 R1” 문구는 최신 HEAD의 내용보다 뒤처져 있다. 고정 HEAD의 실제 source review, R10/C4 문서, net bridge와 diagnostic result를 우선 읽었다. 현재 `NEXT_DAG.json`의 pending 표기도 초기 snapshot이므로 result receipt와 전체 stage-delivery 완료를 별도로 유지한다.

모형은 ground-H1, Le–Cambier Eq85, source-native I=13.6 eV, stationary infinite-heavy-target leading limit, 명시적 isotropic outgoing angular model, common bulk central frame, infinitesimal electron Grad STF다. CCC의 13.6058 eV threshold로 바꾼 혼합모형이 아니다. [고정 계약](https://github.com/cosmosapjw-quantum/BASS_HE/blob/d618344413193950ec3e4e499be526d1ed636d98/research/he37_h1_differential_gain_20261023/CONTRACT.json), [source/theory review](https://github.com/cosmosapjw-quantum/BASS_HE/blob/d618344413193950ec3e4e499be526d1ed636d98/research/he37_h1_differential_gain_20261023/evidence/review/source_theory/REVIEW.md).

Producer receipt상 2000–200000 K의 129 temperature rows, analytic moment와 GL64→96 refinement를 수행했고 선택된 GL96 최대 상대차는 2.2426505097428162e-14다. Net bridge는 conservation, tensor rotation, physical Jacobian, zero states, rejection contracts, representability, thermal/immutability의 **7 groups PASS / 0 fail**다. 새 IVP0이며 CCC saved129 rows를 다시 평가하지 않았다. source/theory review는 해당 제한 모형을 인정하고 mixed-Boolean wording과 paper title에 두 low finding을 기록했다. 현재 compare에는 그 관련 clarification/doc correction도 추가돼 있다.

이 source의 STF는 **electron π_e**에 작용한다. 전체 gas STF로 승격하려면 종별 closure가 필요하다. 유한질량 recoil, 실제 calibrated angular distribution, common-T/u·thermal/fast census, nuclear stopping, coupled gas/metric evolution은 남는다. 20-stage 최종 publication/backup 완료를 이 checkpoint만으로 선언하지 않는다. Li7 source gap에는 직접 대체재가 아니다.

### REI ANGTHERM01: 새 결과가 아닌 준비된 계산 계약

`73c5e00...`→`00303ab27c33a7afa0cec61679af78ef72e3f4aa`는 6개 파일이 추가된 1-commit 변화다. `PREPARED_CHECKPOINT.json`은 **PREPARED_INPUTS_ONLY**, science_IVPs_started=0, donor_IVPs_run=0을 명시한다. 기존 coupled local-flow 결과는 유지된다.

새 계약은 기존 C13/C15/C16 geometry/work와 C22A event heat, 두 preserved z20→2 background에 결속한다. 고정 NPZ SHA256는 grid044 `ae20c278239787c020e45028a6d6804cb9f056b75076a1d5ab045c0a7389733b`, grid022 `5d0ef6ee7adadf3a3acf148a930136cf406fab2b3eb484682e2a93de7119b7c0`다. [고정 실행계약](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/00303ab27c33a7afa0cec61679af78ef72e3f4aa/research/rei_angular_thermochemistry_20261023/EXECUTION_CONTRACT.md). 이 문서는 donor의 연구계획이며 현재 child에게 그 실행을 명령하지 않는다.

### REC126: 저장 진단용 C2 근거

`12068893fab749ae1efb513563d0a86cc1cf649f`의 C2는 기존 8 cases × 64 saved states=512 states corpus에서 geometry7 / atomic3 / thermal2 calls per state를 측정했다. 새 IVP0이며 독립 reviewer가 보존 input/array와 scope를 검토했다고 본문이 보고한다. 후속 `NEXT_STAGE_C3.md`는 HANDOFF_ONLY — C3_NOT_EXECUTED다. 새로운 물리 closure 또는 speedup으로 읽지 않는다.

## PHYS81 백업 metadata 현재성

| 항목 | Drive | Dropbox | 현재 확인 |
|---|---|---|---|
| PHYS81_FINAL_20261023_b3ec271a96cb.zip | 1GEik1y7YsC3obHJsokAD5Kls4qnumjJ7 | id:BSpOijBcT10AAAAAAD_tqg | 이름·size 1,542,353 bytes 일치 |
| PHYS81_FINAL_DELIVERY_20261023.json | 14iQFojLAITCUCFHDWG-72wH955BZ_o1I | id:BSpOijBcT10AAAAAAD_tuw | 이름·size 13,719 bytes 일치 |

Drive modified_time은 ZIP 2026-10-22T23:37:20.293Z, JSON 23:40:12.389Z다. Dropbox rev는 ZIP `65e7658921ee70af03d47`, JSON `65e7662c499690af03d47`; server_modified는 각각 23:37:25Z, 23:40:16Z다. 요청한 checksum/version fields를 Drive connector가 노출하지 않아 현재 checksum 비교를 새로 주장하지 않는다.

이름·크기는 PHYS81 PR137의 frozen final delivery와 일치한다. ZIP SHA256 `6d73c32b2669c8574f013edb06ed5c3aea2bf8b466ef713a6fcf1f2f17e074ed`, JSON SHA256 `df14f9e46e38464148ccf3cc06f68a522dedf7e5dd9b8bdb578e3d4dd7e76091` 및 이전 full-byte restore는 보존된 역사적 receipt 소유다. 이번 확인은 metadata tier이며 old archive download0이다.

같은 백업 folder에서 PHYS82 title query는 Drive/Dropbox 모두0건이었다. Drive “Li” query는0, Dropbox “threshold” query는 2026-10-05의 오래된 ON04 dispatch archive1건뿐이다. 따라서 해당 bounded 검색에서 later PHYS82/Li threshold backup을 찾지 못했다. 전역 부재 증명이 아니다.

## 현재 PHYS82에 전달할 의무

1. **우선 과학 의무 유지**: Li7 physical threshold→6 eV primary source coverage, isotope/energy-axis convention, threshold uncertainty, interpolation/continuation와 low-T Maxwellian 기여를 명시한다. C23A/HE37의 H 또는 H/He source로 이를 대체하지 않는다.
2. **재사용**: PHYS81 Bell positivity/finite moments/hazard reduction/nuclear photon-recoil 결과, 기존 PHYS78/79/80 및 변경 없는 HE36/ANGULAR01/THERM02 donor 결과를 원 identity와 scope로 보존한다. 이번 source 선택 때문에 영향을 받는 항만 재검증한다.
3. **후속 결합**: C23A의 finite electron source와 HE37 event-tensor source는 useful candidate다. source thresholds와 energy frame, number/thermal/fast census, full spectrum과 tail/stopping, electron-vs-gas STF의 별도 의무가 먼저다.
4. **진행 중 donor**: HE37 d618344… 및 REI00303ab…는 관측시각 고정 checkpoint다. 지금 완료상태를 추측하지 않는다. 실제 해당 donor를 새 PHYS82 코드에 의존시킬 때에만 changed-dependency read가 추가로 필요하다.
5. **출처 접근 범위**: 접근 불가능한 private conversations는 검사하지 않았다. live NCP process/lease나 다른 host 실행 상태는 UNOBSERVED다.

## 오류와 종료

외부 read-only connector 호출 39회는 모두 응답했다. 로컬 `git rev-parse HEAD`는 보존 parent directory에 .git이 없어 exit128을 반환했다. 따라서 actual remote PR/ref를 authority로 쓰고 파일은 byte hash로 대조했다. Artifact serializer의 초기 `arr.find` TypeError는 숫자 `files` field와 배열의 구분 누락이었다. 첫 write 전에 발생했고 Array.isArray guard로 수정했다. 과학 결과·원자료 변경은 없다.

이번 범위의 R2/C2 intake는 완료됐다. 모든 owned write는 `/tmp/phys82_work_20261023/intake/` 아래다. 원격 쓰기·새 science·역사 science replay가 없으므로 별도 scientific test를 만들지 않았다. 실제 hash readback과 원격 identity comparison이 이 자료조사의 검증이다.

