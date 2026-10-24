# PHYS87 Codex 실행 인계 — 2026-10-24 KST

## 현재 채택과 이어갈 위치

PHYS87의 과학 판정은 PASS_SCOPED / NUMERICALLY_CHECKED_SCOPED_SOURCE_NATIVE_FINITE_WINDOW다. 검토된 과학 S2는 `cf48be1b8838a3839fa3c605512c1a5bb4faa8e3`, 실제 실행 코드 S1은 `94d3b35bb66df184cf370035f498effbb4534cc6`다. Source/input/code identity는 `bc8a07546cab87dc79de5efee1e0d1917f7e88e851cdd8d5e7856f50f8c1c53d`다. 이 문서가 들어 있는 최종 commit은 PR144와 외부 final-delivery JSON에서 확인한다. S2만 checkout해 최종 복구 기록을 잃지 않는다.

중앙 WU 관측은 `85f9ba1350c076e8df01f5858342df74c3574215`에 게시됐다. 고정 최초 인계 `rei_bianchi@0f9d9df825be1dac9ca9bdf73cdc2e8908bcba17`와 현재 중앙 PR222의 실제 HEAD/AGENTS/병렬 변경을 읽는다. 과거 priority 문구를 현재 owner 완료보다 앞세우지 않는다. 첫 노드 WU_CE83_OWNER_COMPLETION은 actual PHYS83 final `6a2fc5aacb6182a916b9434c316e99e750e8273c`/identity `e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c`로 재사용했다. PHYS84는 prepared/static, 수치 적용 WAIT로 남아 있다.

## 먼저 읽을 파일

`FINAL_REPORT_KO.md`, `CONTRACT.json`, `DAG_OVERLAY.json`, `EXECUTION_LEDGER.json`, `STAGE_PROGRESS.json`, `RESEARCH_LOOP_MAP_KO.md`, `SURVEY_SYNTHESIS_KO.md`, `LATE_SURVEY_ADDENDUM_KO.md`를 읽는다. 다음으로 `theory/NATIVE_FINITE_T_MOMENTS_KO.md`, `source_data/`, `implementation/PRIMARY_IDENTITY.json`, `implementation/FROZEN_IMPLEMENTATION_MANIFEST.json`, `reviews/SCIENCE_ADMISSION.json`, `reviews/INDEPENDENT_REVIEW.json`, `reviews/S2_CLAIM_REVIEW.json`, `results/SAVED_RESULT_SUMMARY.json`, `results/primary001/`, `results/INDEPENDENT_REFERENCE.json`, `results/RESUME_OBSERVATION.json` 및 `delivery/`를 읽는다.

원래 raw outputs, 정확한 원전 bytes와 과거 실패 기록은 불변이다. runtime가 다르다는 이유로 source·primary·reference를 import/재실행하지 않는다. 실제 resume 1 SKIP/callback0/rewrite0 영수증이 이미 있다. 재현성 확인은 저장 evidence·계약·잔차·identity를 먼저 재사용한다.

## 새 코드가 보장하는 범위

ENDF/B-VIII.1 n+H1 MF3/102와 MF6/102의153native knots/152cells, INT5/INT2, 양의 a1/a2 각법칙을 사용한다. Canonical 원전은671232bytes, SHA3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af이며 LF8832/CRLF0을 보존했다. 실험의 physical confidence interval이나 source 밖 영단면적을 가정하지 않는다.

질량·에너지는 명시한 neutron scale, AWR=.9991673, QI=2224648eV와 effective ²H atomic-equivalent residual의 source-native 규약이다. Parent bare Q와81.63eV 차이는 물리 불확도로 사용하지 않는다. API가 거절하는 bare-network 규약을 임의 remap으로 통과시키지 않는다. T guard255..101e6K, 모든 해당 Bessel z≥1e5와 finite lab support[1e−5,2e7]eV를 유지한다.

공통-T independent isotropic classical Jüttner 입력에서 incoming COM axis를 올바른 invariant measure로 평균한다. 미시 비등방 각법칙을 임의 isotropic source로 치환한 것이 아니다. 두 온도·drift·비평형 target 또는 source 밖 조건에는 별도 유도가 필요하다.

같은 사건의 Kin, photon, daughter energy와 covariance를 유지한다. Energy owners는 `[h<KD>−<Kin>,(1−h)<KD>,−Q,0,Ehandoff,Eescape]`, 합0이고 입자수는 `dNth=h−2,dNfast=1−h,dNe=0`다. 두 photon route는 배타적이다. `h=1`은 instant caloric birth 선택이며 stopping 계산이 아니다. 온도 source는 `Cv*Tdot/R=−<Kin>+un+uH+h*(<KD>−uD)`다.

## 결과와 남은 예산

Primary1/reference1/saved figures1 모두 한 번 성공했다. 147 scalar assertions(24 guards 포함),153 exact-knot witnesses,152 convex cells를 서로 더하지 않는다. Primary12integrations, reference608quad/12810callbacks,2PNG+2PDF를 저장했다. Local CPU4.364383s/launchwall4.369048669s,1worker/thread/ownlease3해제다. 새 cloud symbolic1회/12exactzero, 이전PHYS85/86 evaluator4회와 실패·unknown을 보존했다. 그 계수 범위 누적5회이며 전체 project 지출을 뜻하지 않는다.

동결 child primary/reference/figure 각1회와 PHYS87 cloud1회 allowance는 소진했다. 남은 초를 다른 campaign에 이전하지 않는다. 돈·최대RSS·전체 remote CPU는 unknown이며0으로 리셋하지 않는다. 1.5GiB reserve+0.5GiB job, cachecredit0, shared lease 및 다른 process를 종료하지 않는 규칙을 유지한다.

## 게시·복원 절차

S0/S1/S2는 actual expected-SHA additive Draft와 양쪽 ACK metadata로 기록했다. S2 inline-tree 요청422와 원본 ZIP의 preupload byte mismatch는 전달 실패이며 과학 실패가 아니다. 원래 short ZIP/영수증을 보존하고 같은동결입력의 `PHYS87_S2_RECOVERY1_20261024_cf48be1b8838.zip`를 채택했다. 세 stage ACK를 최종 whole restoration으로 쓰지 않는다.

FINAL은 root가 고정한 containing HEAD에서 원본 bytes로 pack한다. 실패 당시처럼 부분 파일을 사용하지 않도록 파일이 완전히 닫힌 뒤 size/SHA/CRC를 확인하고 새 경로에 완성본을 배치한다. 같은 이름에 덮어쓰지 않는다. Drive·Dropbox upload 뒤 양쪽 전체 다운로드를 끝까지 기다리고 SHA,CRC,payload SHA, 실제 추출을 검증한다. Remote Git identity는 exact FINAL commit의 exhaustive owned subtree IDs와 모든 restored bytes의 Git blob SHA1/path/mode/set equality로 대조한다. Raw Git blobs를 전부 내려받았다고 표현하지 않는다.

외부 `PHYS87_FINAL_DELIVERY_20261024.json`의 실제 원문 양쪽 readback SHA/identity와 후속 terminal receipt/PR144 최종 본문을 함께 읽어 전달 완료를 판정한다. 문서 안의 FINAL 대기는 생성 시점 상태이며 자기 미래 ACK를 재귀적으로 넣지 않는다.

## 다음 연구 노드와 금지된 승격

다음은 `NUCLEAR_ATOMIC_TO_BARE_CAPTURE_REMAP`이다. 원전 lab/COM 에너지, atomic/bare mass·Q, bound electron, residual isotope/target state와 에너지 원점을 먼저 primary source로 정합한다. 그 이론 R1–R10과 frozen contract가 닫힌 뒤 lower-tier가 coding C1–C10을 구현하고 별도 Astra가 검토한다. 이후 full support/covariance/named consumer가 닫혀야 actual nuclear rates/fast stopping을 판정할 수 있다. 현재 supplier parent는 PARTIAL, consumer admission false다.

Late-source 부록의 HE joint PWBE 모형 availability, REC finer data 존재, BASS Bianchi-II INITIAL-DATA stock, REI 실제 pressure admission을 재사용하되 각 source의 physical/consumer gate는 유지한다. 다른 담당자의 완료 science, 그림 repair reserve 또는 미실행 stock proposal을 이번 예산으로 실행하지 않는다.

Non-tilted LRS Bianchi I, reacting gas pi=0와 collisionless DM pi_m 별도, 같은 normal frame signed matter/radiation tensor 합 후 norm을 유지한다. Frobenius=sqrt(2)×half-contraction norm이다. Same-trajectory 분해는 species-off 인과 실험이 아니며 sampled residual은 continuum certificate가 아니다. Li uncertainty·He/Li CX·D PI/RR·recombination-to-z20 charge·hard UV inner shell·full spectral geometry coupling은 OPEN이다. HH_R10=OFF, Production admission NOT_ISSUED, 전체 완료율null.

