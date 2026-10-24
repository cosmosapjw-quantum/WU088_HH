# Final delta followup: 고정된 공개 원문의 사실 기록

이 문서는 과학 판정·채택·실행을 하지 않은 read-only intake다. 실제 호출은 **28회**: 신규 PR get_pr_info4, 고정 base→head compare6, 선택 file18. 모든 응답이 성공했다. 원응답28개를 이 디렉터리에 보존했다. 각6HEAD에서 source3개씩 읽었고, 18개 모두 content 원 UTF-8 bytes로 Git blob SHA1을 계산하여 응답의 blob SHA와 일치했다. 정확한 byte 사본은 `pinned_sources/`, 매핑은 `PINNED_SOURCE_MANIFEST.json`이다. `sources/`는 줄 단위 검토용 사본이다. 상세 원문·metadata·출처·직접 인용·published receipt는 `FOLLOWUP_FACTS.json`에 있다.

## Actual metadata pins

| Repository PR | Actual HEAD | updated_at | 변경 파일 수 |
|---|---|---|---:|
| rec_bianchi131 | c7cdabd871ab2ef6f722594ff063b8ce8550e6b4 | 2026-10-24T01:50:26Z |81|
| BASS_HE94 | d8bae9f7e24ad3494e399f7ab46c4167a5623d48 | 2026-10-24T02:50:43Z |56|
| bass_cr100 | 8e4e06361d714939513a11f64a27f02822bde2fa | 2026-10-24T02:50:31Z |111|
| bass185 | c2e6f1f80417e62c95e607c80115e89de1925ca9 | 2026-10-24T02:36:31Z |62|

모두 metadata에서 open/draft=true다. 앞선 final_delta가 확인한 이동 HEAD rei_bianchi222=`6cf7c53757ce4049046a3463c57f36bece555830`, BASS_HE93=`bf3c21a39b1111497ed77667d05b8a853ffe6646`도 동일 pin으로 읽었다. 이 두 PR get_pr_info를 이번에는 반복하지 않았다.

## REC131 — 실제 입력 범위 판정과 보존 한계

출처 HEAD c7cdabd871ab2ef6f722594ff063b8ce8550e6b4의 `research/rec_history_input_admission_20261024/REPORT_KO.md`, `HANDOFF_KO.md`, `delivery/FINAL_COMPANION_RECEIPT.json`.

직접 표기: `COMPLETE_SCOPED_INPUT_ADMISSION`, `physical_reference_admitted=false`, H5=`INPUT_DEPENDENT_UNCALIBRATED`, REC_HISTORY=`PARTIAL`.

원문은 h/2 U5의 retained causal prefix가 고정313query 모두의 보간 cell을 제공하지만 target T0/nH0 불일치와 reference/endpoint/curvature uncertainty가 남았다고 적는다. Primary1회386checks, independent review1회3probes, figure3회; 누적 CPU5.928528894s/wall6.09275194699876s, newIVP/native/oldreplay0을 기록한다.

보존은 `PARTIAL_AFTER_WORKSPACE_RESET`. 원 SUMMARY의 exact SHA256은 복구했으나 원1,252상세rows·313querytable·checks·과거controller·원PNG/PDF가 미복구라고 명시한다. 이번 intake는 검증을 재실행하지 않았다.

Published companion receipt에 최종 ZIP613327B / SHA256199d28152b5e6065bc6c11e685705e4a59e43b5101ed955be6216b5a13b611f4, Dropbox completed ACK와 singleGET whole-byte/CRC/84payload PASS가 기록돼 있다. Drive는 ACK/ID없음, whole-byte NOT_RUN, complete_dual_provider_backup=false다. 이 설명은 고정 Git receipt를 읽은 결과이며 이번에 provider download를 새로 수행하지 않았다.

REC 원문은 별도 중앙 PR223/44d0a6d8703f50bf3d7548812a1ab13d9b2c3877 observation을 가리킨다. 이번 대상 REI222 branch HEAD와 다른 게시 identity이며, 이를 REI222 containing commit으로 바꾸어 기록하지 않는다.

## HE94 — 측정 DDCS20 부분 window

출처 HEAD d8bae9f7e24ad3494e399f7ab46c4167a5623d48의 `research/he_ang_ddcs20_window_20261024/RESULTS_KO.md`, `CONTRACT.json`, `CLAIM_GATE.json`.

직접 표기: unit=`COMPLETE_SCOPED`, implementation=`NUMERICALLY_CHECKED_SCOPED`, parent_HE_ANG=`SOURCE_INPUT_PENDING`. 원문은 E0=20eV, E3–6eV, theta15–120도의 조건부 검출 window를 정의한다. 원40값/8uncertainty를 보존하고32값을 주 계산에 사용한다. 8tests/실제11checks, R6 PASS/C9 PASS_SCOPED, CPU1.957005s/wall2.104758353s, scientific child3/repair0을 기록한다. full support·joint electron event law·finite-mass/recoil·event normalization은 완료로 표기하지 않는다.

PR body는 checkpoint Dropbox/Drive metadata-size ACK를 적고 final science+central archive/C10 receipt를 후속으로 둔다. 이 science pin의 변경 파일 목록에는 최종 receipt가 없고 `delivery/CHECKPOINT1_BACKUP_ACK.json`만 있다. 이번3file선택은 report/contract/claim이었다. 따라서 checkpoint actual provider raw ACK나 최종 remote byte verification을 이번 intake에서 별도로 확인하지 않았다.

## CR100 — 조건부 D43K PI/RR/CX 장부

출처 HEAD8e4e06361d714939513a11f64a27f02822bde2fa의 `research/cr_c23e_d43_source_binding_20261024/RESULTS_KO.md`, `FROZEN_CONTRACT.md`, `HANDOFF_KO.md`.

직접 표기: `COMPLETE_SCOPED / NUMERICALLY_CHECKED_SCOPED`, fresh Astra PASS_SCOPED; N5 parent=`PARTIAL`, empirical D PI/RR·Milne/full21 coverage=`OPEN`.

104checks/18순간상태/3newD-target quadratures/9bandorders; childCPU2.161932s/wall2.171415343s, 별도 delivery repair29checks와 과학호출0을 기록한다. ODE/완료science replay/NCP0.

WU 관련 직접 원문: “PI primary energy는 fast pool로 들어가며 thermal heat와 중복되지 않는다. RR은 thermal pool만 소비한다.” 같은 potential의 PI/RR/CX를 사용하며 PHYS79의 kr-preserving D43K CX를 재사용했다고 적는다. 상세 handoff는 WU PHYS79 PR134 science338fb772/final3304d16d를 완료 재사용 근거로 열거한다. Full nuclear/general Bianchi HOLD, stopping/finitebath/새cosmological trajectory OPEN이다.

최종 새 provider IDs는 후속 PUBLICATION/BACKUP_RECEIPTS/FINAL_AUTHORITY가 기준이라고 적는다. 이 pinned changed-file 목록에는 그 최종 파일들이 없고 PR body도 새 배송본 진행이라고 적는다. 따라서 **새C23E backup actual IDs/readback은 이번 intake에서 미확인**이다. 과거 C23D/oldN4 Drive UNKNOWN_NO_ACK를 승격하지 않는다.

## BASS185 — detached REC LINE01 사건률과 단일 소유권

출처 HEAD c2e6f1f80417e62c95e607c80115e89de1925ca9의 `research/bass_b3a_event_source_20261024/REPORT_KO.md`, `CONTRACT.md`, `delivery/BACKUP_ACK.json`.

직접 표기: B3a detached instantaneous adapter PASS_SCOPED, B3b finite-stock/population transaction/receiver와 B3c coupled test 미완료. Supplier는 REC@93e1bdc8298db9a7c16f77d4bf64985a0c3f25aa LINE01 standalone_detached이며 proper-time/matter-rest 및 atomic excitation partner를 보존한다. U/J transfer와 PiRate를 caller의 current state Source.pi와 분리해 반환한다. Duplicate key는 `(owner, epoch, transfer_id)`라고 적는다.

원문 counters: independent Fraction23/23, initial suite12/12 뒤 independent defect 발견, targeted RED 실패6, repair targeted3/3, final15/15. 계측된 새 부분합 CPU6.359076642999999s/wall6.3684287650103215s는 Wolfram 실제 kernel비용·모델·네트워크를 포함하지 않는다고 명시한다. 새IVP/과거campaign replay0.

Published BACKUP_ACK는 새60-file capsule300983B/SHA2562d164acc74b4a788a524b0b084533f79c55164ab2246590a5150279553371050의 Dropbox completed/size ACK와 Drive success ACK를 기록한다. 같은 receipt는 `remote_full_byte_readback=NOT_RUN`을 명시한다. 따라서 양쪽 ACK와 whole-byte restore를 구분한다. 현재 containing HEAD는 receipt-only 후속까지 포함하며 PR body의 scientific payload pin f4f12a162b446f7fc42759f88d544749435fb35b와 다르다.

## 이동한 HE93와 REI222

HE93 compare15053fe4445a32e0544d644e864fe27780d08743→bf3c21a39b1111497ed77667d05b8a853ffe6646는1commit/6files. 읽은 source는 `research/he_ang_source_hex_20261024/RESULTS_KO.md`, `HANDOFF_RESEARCH_KO.md`, `delivery/FINAL_ARCHIVE_ACK.json`.

Hex intake COMPLETE_SCOPED/HE-ANG SOURCE_INPUT_PENDING을 유지한다. resourceCPU18.434312s/wall18.739398924000852s, 실패catalogue2/완료1·nominal8CPUovershoot 보존. Archive8855085B/SHA25677ac5f1599805fae102f1c6591aa9ae7c1227f32dbb06ebaa7c3f39f52a75b68의 Dropbox/Drive 완료ACK·size-match가 기록돼 있고 independent remoteSHA256 comparison은 NOT_AVAILABLE라고 적는다.

REI222 compare68420637a9ab54ada92afd786c5733bc0764b8c9→6cf7c53757ce4049046a3463c57f36bece555830는5commits/9paths: assembly/DAG, HE·CR handoff각1, HE Hex/backup/review/DDCS20 returns, C23D EE·C23E D43 returns. **AGENTS/WU handoff 경로는 changed list에 없다.** 그러므로 unchanged 파일을 다시 fetch하지 않았다. 읽은3source는 `research/orchestration_longterm_20261023/assembly/DAG.json`, `HANDOFF_bass_cr_KO.md`, `returns/CR_N4_STOPPING_C23D_EE_BRIDGE_20261024.json`이다.

DAG/return은 N4 stopping parentPARTIAL/OPEN, C23D EE child COMPLETE_SCOPED·NUMERICALLY_CHECKED_SCOPED를 따로 둔다. Return의 actual_new_trajectories=4/admission_trajectories=3/newcoupledcosmologicalODE0/oldreplay0. 해당 C23D archive5989522B/SHA256c7040ba442a8d3079547c1aeb8dcb60491617c4471638db44ab55c743f19a4b9의 Library/Dropbox publishedR3 PASS, DriveUNKNOWN_NO_ACK/NOT_RUN을 기록한다. 이 반환문의 proof-level은 published receipt를 읽은 것이며 이번 provider재검증은 아니다.

## 조회 범위와 판단 경계

새 source실행·scientific suite·providerupload/download·remote변경0. Wholebranch inventory반복0. Pinned파일 원문과 PR/compare metadata만 확인했다. Parent root가 물리 의미와 WU claim adoption을 판정한다. 추가 최신 ref polling이나 새PR223 HEAD확인을 자동 수행하지 않았다.
