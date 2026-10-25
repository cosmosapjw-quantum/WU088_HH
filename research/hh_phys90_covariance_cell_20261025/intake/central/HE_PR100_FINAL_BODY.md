# Analytic direct Coulomb–Born hydrogen model: scoped science and delivery

PASS_SCOPED_DIRECT_CBA, R6PASS/R7PASS_WITH_DIAGNOSTIC/independentC9PASS. DefinedunitD20/20; entireHE-ANG SOURCE_INPUT_PENDING, physicalproviderfalse/globalcompletionnull. DraftPR100unmerged,activationfalse.

# HE-ANG-CBA-NORDSIECK 실제 결과

고정핵 직접 Coulomb–Born 모형의 수소 1s overlap, delta-state 정규화와 절대 labelled TDCS를 유도하고 구현했다. 핵심 식은 THEORY_KO.md의 (1)–(9)다. 전체 HE-ANG physical provider 채택과 이번 analytic model의 확보 범위는 CLAIM_GATE.json에서 분리한다.

## 새 수학과 구현

원전 Eq19/A9의 I는 1/r 적분이다. 1s 전이 overlap K는 eta,p,q를 고정한 -partial_lambda I로 얻는다. eta=lambda/p는 그 뒤 적용한다. 이 순서에서 K(lambda,-p,p;eta)=2I0(lambda-eta*p)/(p²+lambda²)가 되어 같은 Coulomb Hamiltonian의 bound–continuum 직교성을 재현한다. Source Eq18의 추가1/r와 Appendix A7 부호는 실제 읽은 preprint의 문자적 불일치로 기록했고 출판본 교정 여부는 추정하지 않았다. 원전 Eq28의 J와 이번 K는 서로 다른 적분이다.

Matched eta=lambda/p에서 Delta=q+p로 쓰면 K=16*pi*lambda*C*[Delta²-(1+i*eta)Delta.p]/(A²*Bc)다. 작은 Delta의 두 큰 항을 빼지 않는 구현이고 Delta0은 정확히0이다. Generic overlap와 별도로 이 식을 주 경로로 사용했다. Principal Log(Bc)는 lambda,p>0에서 Im(Bc)<0인 연속 가지로 고정했다.

Nc=(2*pi)^(-3/2)exp(pi*eta/2)Gamma(1-i*eta)와 정규화된1s를 사용한 F_D에 대해 TDCS=4*(pf*p/pi_momentum)*|F_D|²/Delta^4다. Box-state 황금률/상태밀도/flux와 delta-state T 양쪽 계수를 맞췄다. 직접 spin-diagonal 채널의 spin factor는1이다. 수소 matched 경로의 nuclear overlap은0이며 eta0 plane-wave control에서는 nuclear subtraction을 유지했다. 단위 a0,p0,E_h와 물리 TDCS a0²/E_h를 명시했다.

## 실제 수치 근거

| 관측 | 범위 | 최대 관측 오차 |
|---|---|---:|
| 표적 테스트 | 14methods, failures0/errors0 | PASS |
| Generic I/K binary64 | 9inputs, mp80 reference | 1.0629567988304066e-15 scaled |
| Formula precision | 같은9inputs mp50–mp80 | 9.183265145706724e-51 scaled |
| 원적분 Eq6 quadrature | 4moderate complex cases,mp50 | 3.506764608003949e-51 scaled |
| Stable tiny transfer | 16parallel/transverse inputs | 4.0063870834280886e-16 true relative |
| Nc/Sommerfeld normalization | 7eta values | 1.5116805406513489e-15 scaled |
| Delta-state TDCS conversion | 73angles×2models | 7.159247292900658e-16 scaled |

Scaled error는 abs(value-reference)/max(1,abs(reference))이다. Tiny-transfer만 nonzero mp80 reference에 대한 true relative error를 썼다. Tolerance를 실행 뒤 바꾸지 않았다. 원적분 quadrature는 K의 parabolic-coordinate 1차원 적분이며 closed I의 수치 미분을 되풀이한 검사가 아니다.

Conditioning 예: pvec=(0,0,0.7),lambda1, transverse Delta=(1e-14,0,0)에서 generic subtraction 식의 상대오차는1.742881133761018e12, 안정식은1.928809976914049e-16이다. 같은 t의 parallel generic error는0.016729855113103972, 안정식은1.8021982992221216e-16이다. 이들은 작은-transfer 수학 fixture이며 실제 ionization kinematics에서 Delta0 사건을 의미하지 않는다. 전체 입력 공간에 대한 uniform/outward error bound는 주장하지 않는다.

Illustration은 source에서 읽은250eV incident/5eV ejected/3degree scattered geometry와 nominal U27.2를 사용했다. Oriented coplanar angle -180..180degree step5의73points에서 표본최대는 두 모형 모두 -50degree에 있다. Direct CBA0.45610407121581825, direct plane0.9421399651692766 a0²/(eV sr²)이다. 이는 새 근사의 계산 예이며 원전 곡선 fit,20/54.4/413.6eV 데이터 재적합 또는 연속각 최대치의 증명이 아니다. 그림은 저장된 JSON만 읽어 만들었다.

## 실제 실행·실패·비용

Three actual children은 tests0.2772319999999999CPU/0.3188933669953258wall, analysis2.580506/2.6289747010014253, saved-output plot2.130236/2.174621346995991초다. 합계4.987974CPU/5.122489414992742wall, 새20/60할당,512MiB/1thread다. Repair reserve1은 미사용이며 이전 예산에서 이전하지 않았다. 변경 없는 이전 suite 및 이번 tests/analysis 재실행은0이다.

첫03_plot 호출은 기존0byte RUN.lock 때문에 scientific START 전에 중단됐다. 실제02session terminalexit0,완성FINISH,관련activeprocess0,03START없음을 확인하고 원시traceback/lockstat를 보존한 뒤 그 lock만 제거했다. 이후 plot child를 처음 실제로 실행했다. Stale-lock 발생/cleanup 실패의 원인은 NOT_ESTABLISHED, prelaunch CPU는 UNKNOWN_NOT_ZERO이다. 이를 scientific child 실패나 reserve 소비로 바꾸지 않았다.

Wolfram original call은12True/5structuralFalse/1unevaluated, targeted diagnostic6residual은Together/FullSimplify/유리수대입 모두0이다. Cancel의 항별 표현을 SameQ로 literal0과 비교한 false-FAIL을 교정했으며 첫 결과를 그대로 남겼다. Evaluator2calls toolwall16.886s,bodyCPU0.304298s/bodywall0.304892s; context1call toolwall20.315s; 합toolwall37.201s다. Remote 전체CPU는 UNKNOWN_NOT_ZERO이다. Third evaluator call은 없었다. SciSpace2search,Exa2search+2fetch(4URLs)의401/timeout 및 이전403도 보존했다.

Metadata preparation0.038864099000000006CPU/0.040913912998803426wall, B1pack0.07220352099999999/0.0722468569947523초를 별도로 기록했다. 모델·provider·IO·prelaunch 및 과거unknown은0으로 환산하지 않았고 end-to-end 총 cap은 입증하지 않았다. PR99의2.484451/2.519181445000868,PR98의3.117567/3.242023329999938,PR97의3.304038/3.4507949489989187 및 모든 이전 원장·실패·reserve 상태는 inherited reference chain에 보존한다.

## 조사와 남은 의무

초기 최신 조사:7repos,14collections,30pages terminal,1339branches/874openPRs. Dropbox4929entries/9pages,Drive926documents/3pages+27folders/1page terminal이다. Drive document 검색은 binary archive 전체를 열거하지 않으므로 knownID metadata 확인과 구분한다. 관련 대화는1query-selected이며 self-echo/stale delivery 요약을 새 근거로 채택하지 않았다. 선택된 PR/원전 본문과 전체 branch metadata의 coverage를 구분한다.

중앙 HEAD는 조사 시작E9600a605에서2354d6e9로 진행했다. 게시 시점의 실제 최신 HEAD와 DAG를 사용하여 그 owner 변경과 모든 oldHE/other39를 보존한다. REC/CR/HH의 scoped 결과·OPEN·비용·실패·unknown은 해당owner 범위에 둔다. C23E 및 미래 partial mu_window theta metadata C9-NB-01도 OPEN으로 유지한다.

전체 HE-ANG은 SOURCE_INPUT_PENDING이다. 다음 실제 연구 입력은 source-consistent physical joint amplitude/event payload와 source validity, spin/exchange/count, full support, frame/finite-M dynamics, calibrated uncertainty다. 이번 fixed-centre amplitude와 PR99 finite-M shell의 결합은 그 별도 의무를 만족한 뒤 수행한다. Event sigma, physical recoil law, HE-X1 empirical angular correction을 이번 단위에서 승인하지 않았다. 새 strong no-go 또는 문헌 최초성 주장은 없다.


## Actual publication correction and final delivery

Final S is a raw-CSV-only successor of S0 `86fc9206d885633b59745fb80dcc22fa163bfd89`. The preserved failure is PUBLICATION_SERIALIZATION_BYTE_IDENTITY_MISMATCH: universal-newline text serialization changed CSV CRLF into LF. The minimal helper fix reads bytes then UTF8-decodes; exact scientific stage/code/results/reviews were unchanged. No physics rerun, new scientific review or local reserve was consumed. Root verified S87/87 and D102/102, C/Ethree blobs each, while preserving88prior research subtrees/14root entries.

Defined-unit D20/20 and the actual E/B3 external tail complete this one delivery. The immutable S18/20 and D/Ehistorical pending fields are not rewritten. Whole HE-ANG remains SOURCE_INPUT_PENDING, physical_provider/event_sigma/physical_recoil/HE-X1 empirical correction=false, global completion=null. Stop after this unit; draft/unmerged, merge=false, activation=false.

Exact D theory/results/ledger/reviews: https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/ . Central E DAG/HEhandoff/return: https://github.com/cosmosapjw-quantum/rei_bianchi/blob/14976bda37b17e8dd8060f4c89adf6ddf9fbcc6a/research/orchestration_longterm_20261023/assembly/ . The stage table below distinguishes B1preexecution inputs from later science/delivery evidence.


## Actual publication identities

| Snapshot | Actual commit | Actual tree |
|---|---|---|
| S | `a891cd4b9a3548e66db669b9eb472fea88a3b78b` | `ee6768ab8a934cb9b47819a24cf5498e4f8b8ece` |
| C | `7caca70d94d03732bff5e7adf2f9aa5cf59310ec` | `ebeaf6623dfd0077adae43933f8494056e8974c8` |
| D | `8e0fb28fea520364d8794bac32840621dd150f95` | `b1cff8c85f9c343f8d0f1d3192e638023f0d5157` |
| E | `14976bda37b17e8dd8060f4c89adf6ddf9fbcc6a` | `722c8103ba2d68d6c2b86e2be4d64348c34a3dfc` |

## Actual backup receipts

| Checkpoint | Archive / bytes / members | Uploaded bytes SHA256 | Drive / Dropbox |
|---|---|---|---|
| B1 | HEANG_CBA_NORDSIECK_B1_PREEXECUTION_20261025.tar.gz / 792680 / 77 | `afa42e0e7ed6b8d963528a0cb480bbb5373cfcaa18c1791429b6afbf731ccdcf` | 18KqAWKFtZE5K0t0-TzVUMFEQJXc-oTWo / id:BSpOijBcT10AAAAAAD_9qA |
| B2 | HEANG_CBA_NORDSIECK_SCIENCE_20261025_a891cd4b_7caca70d.tar.gz / 2054451 / 142 | `a3525a7d739695f2755de50f761524b98190b4d7b4dbcb67392e9cd6da4c2911` | 10VI1GXobkRS-r1dWrxb-_nSHjg9phvRV / id:BSpOijBcT10AAAAAAD_9tg |
| B3 | HEANG_CBA_NORDSIECK_DELIVERY_20261025_8e0fb28f_14976bda.tar.gz / 734417 / 140 | `9027c29a0b441ac6028a0cae673342fa6f60f9e97e758ad130aff153ec02fa28` | 1WJsOVDtjKOACcz3ieGI7LI_fzAsf_BZ- / id:BSpOijBcT10AAAAAAD_9tw |

Upload/metadata acknowledgments and local member verification are the observed backup scope. Independent remote whole-GET/SHA256 verification is not asserted. Immutable S18/20, D20/20 and their historical pending-tail fields remain unchanged; this PR body carries the actual external E/B3 tail.

## Defined-unit stage evidence

| Stage | Name | Actual status | Evidence | Checkpoint scope |
|---|---|---|---|---|
| R1 | 연구 위치·계약 | COMPLETE_SCOPED | [FROZEN_CONTRACT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/FROZEN_CONTRACT.json); [evidence/survey/AGENTS_REUSE_CHECK.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/survey/AGENTS_REUSE_CHECK.json); [evidence/survey/entry/ENTRY_PREFLIGHT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/survey/entry/ENTRY_PREFLIGHT.json); [evidence/survey/FRESH_CENTRAL_BASE_RECEIPT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/survey/FRESH_CENTRAL_BASE_RECEIPT.json); [evidence/survey/CENTRAL_CHANGE_OBSERVATIONS.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/survey/CENTRAL_CHANGE_OBSERVATIONS.json); [evidence/survey/post_S/FRESH_CENTRAL_BASE_RECEIPT.v2.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/survey/post_S/FRESH_CENTRAL_BASE_RECEIPT.v2.json); [evidence/survey/post_S/POST_S_CENTRAL_CHANGE_OBSERVATIONS.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/survey/post_S/POST_S_CENTRAL_CHANGE_OBSERVATIONS.json) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| R2 | 근거·재사용 | COMPLETE_SCOPED | [evidence/source/SOURCE_REPORT.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/source/SOURCE_REPORT.md); [evidence/source/SOURCE_CALL_LEDGER.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/source/SOURCE_CALL_LEDGER.json); [evidence/survey/INHERITED_LEDGER_REFERENCES.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/survey/INHERITED_LEDGER_REFERENCES.json) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| R3 | 주장·전제 정렬 | COMPLETE_SCOPED | [THEORY_KO.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/THEORY_KO.md); [FROZEN_CONTRACT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/FROZEN_CONTRACT.json) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| R4 | 가설·표현 탐색 | COMPLETE_SCOPED | [THEORY_KO.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/THEORY_KO.md); [evidence/source/SOURCE_REPORT.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/source/SOURCE_REPORT.md) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| R5 | 구성적 유도 | COMPLETE_SCOPED | [THEORY_KO.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/THEORY_KO.md); [reviews/R6_REPORT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/reviews/R6_REPORT.json) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| R6 | 독립 검증 | COMPLETE_SCOPED | [reviews/R6_REPORT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/reviews/R6_REPORT.json); [reviews/R6_REVIEW.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/reviews/R6_REVIEW.md) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| R7 | 판별 검증 | COMPLETE_SCOPED | [evidence/wolfram/CBA_SYMBOLIC.wl](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/wolfram/CBA_SYMBOLIC.wl); [evidence/wolfram/ACTUAL_EVALUATOR_RESULT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/wolfram/ACTUAL_EVALUATOR_RESULT.json); [evidence/wolfram/DIAGNOSTIC.wl](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/wolfram/DIAGNOSTIC.wl); [evidence/wolfram/ACTUAL_DIAGNOSTIC_RESULT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/wolfram/ACTUAL_DIAGNOSTIC_RESULT.json); [reviews/R7_DIAGNOSTIC_REVIEW.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/reviews/R7_DIAGNOSTIC_REVIEW.json); [evidence/wolfram/WOLFRAM_SUMMARY.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/wolfram/WOLFRAM_SUMMARY.json) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| R8 | 결과 판정 | COMPLETE_SCOPED | [reviews/ROOT_ADMISSION.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/reviews/ROOT_ADMISSION.json); [CLAIM_GATE.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/CLAIM_GATE.json); [RESULTS_KO.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/RESULTS_KO.md) | Later result/review/delivery outside B1; S/B2 science; D/E/B3 actual tail |
| R9 | 정식 결과·코딩 연결 | COMPLETE_SCOPED | [THEORY_KO.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/THEORY_KO.md); [FROZEN_CONTRACT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/FROZEN_CONTRACT.json); [evidence/preparation/MAPPING_DESIGN.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/preparation/MAPPING_DESIGN.md) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| R10 | 종료·재개 | COMPLETE_AT_DELIVERY_COMMIT | [HANDOFF_RESEARCH_KO.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/HANDOFF_RESEARCH_KO.md); [delivery/PUBLICATION.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/PUBLICATION.json); [delivery/S_PUBLICATION_RECEIPT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/S_PUBLICATION_RECEIPT.json); [delivery/C_PUBLICATION_RECEIPT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/C_PUBLICATION_RECEIPT.json); [delivery/B2_BACKUP_ACK.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/B2_BACKUP_ACK.json); [delivery/FINAL_BACKUP_ACK.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/FINAL_BACKUP_ACK.json) | Later result/review/delivery outside B1; S/B2 science; D/E/B3 actual tail |
| C1 | 목표·baseline | COMPLETE_SCOPED | [FROZEN_CONTRACT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/FROZEN_CONTRACT.json); [evidence/survey/LOCAL_DURABILITY.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/survey/LOCAL_DURABILITY.json) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| C2 | 식–데이터–코드 | COMPLETE_SCOPED | [evidence/preparation/MAPPING_DESIGN.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/preparation/MAPPING_DESIGN.md); [code/cba.py](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/code/cba.py) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| C3 | 수치 설계 | COMPLETE_SCOPED | [evidence/preparation/FIXTURES.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/preparation/FIXTURES.json); [code/test_cba.py](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/code/test_cba.py); [code/run_analysis.py](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/code/run_analysis.py) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| C4 | 실행 DAG·자원 | COMPLETE_SCOPED | [FROZEN_CONTRACT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/FROZEN_CONTRACT.json); [evidence/preparation/HOST_RESOURCE_OBSERVATION.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/preparation/HOST_RESOURCE_OBSERVATION.json); [evidence/execution/RESOURCE_LEDGER.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/execution/RESOURCE_LEDGER.json); [delivery/B1_BACKUP_ACK.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/B1_BACKUP_ACK.json) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| C5 | 구현 | COMPLETE_SCOPED | [code/cba.py](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/code/cba.py); [code/test_cba.py](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/code/test_cba.py); [code/run_analysis.py](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/code/run_analysis.py); [code/plot_results.py](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/code/plot_results.py); [code/run_bounded.py](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/code/run_bounded.py); [evidence/preparation/SYNTAX_ONLY.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/preparation/SYNTAX_ONLY.json); [evidence/execution/PRELAUNCH_03_FAILURE.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/execution/PRELAUNCH_03_FAILURE.json); [evidence/execution/PRELAUNCH_03_CLEANUP_AUTHORIZATION.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/execution/PRELAUNCH_03_CLEANUP_AUTHORIZATION.json); [evidence/publication/S0_BYTE_IDENTITY_MISMATCH.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/publication/S0_BYTE_IDENTITY_MISMATCH.json); [evidence/publication/PUBLICATION_NEWLINE_HELPER_CORRECTION.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/publication/PUBLICATION_NEWLINE_HELPER_CORRECTION.json) | B1 prepared inputs only; S/B2 retained science; D/E/B3 actual delivery |
| C6 | 표적 검증 | COMPLETE_SCOPED | [results/TEST_REPORT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/results/TEST_REPORT.json); [evidence/execution/01_01_tests/START.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/execution/01_01_tests/START.json); [evidence/execution/01_01_tests/FINISH.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/execution/01_01_tests/FINISH.json) | Later result/review/delivery outside B1; S/B2 science; D/E/B3 actual tail |
| C7 | 판별 계산 | COMPLETE_SCOPED | [results/ANALYSIS.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/results/ANALYSIS.json); [evidence/execution/02_02_analysis/START.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/execution/02_02_analysis/START.json); [evidence/execution/02_02_analysis/FINISH.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/execution/02_02_analysis/FINISH.json) | Later result/review/delivery outside B1; S/B2 science; D/E/B3 actual tail |
| C8 | 결과 해석·시각화 | COMPLETE_SCOPED | [results/figures/PLOT_RECEIPT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/results/figures/PLOT_RECEIPT.json); [reviews/C9_REPORT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/reviews/C9_REPORT.json); [results/figures/CBA_NORDSIECK.png](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/results/figures/CBA_NORDSIECK.png); [results/figures/CBA_NORDSIECK.svg](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/results/figures/CBA_NORDSIECK.svg); [evidence/execution/03_03_plot/FINISH.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/execution/03_03_plot/FINISH.json) | Later result/review/delivery outside B1; S/B2 science; D/E/B3 actual tail |
| C9 | 독립 코드·결과 검토 | COMPLETE_SCOPED | [reviews/C9_REPORT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/reviews/C9_REPORT.json); [reviews/ROOT_ADMISSION.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/reviews/ROOT_ADMISSION.json) | Later result/review/delivery outside B1; S/B2 science; D/E/B3 actual tail |
| C10 | 저장·전달 | COMPLETE_AT_DELIVERY_COMMIT | [CLAIM_GATE.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/CLAIM_GATE.json); [HANDOFF_RESEARCH_KO.md](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/HANDOFF_RESEARCH_KO.md); [delivery/PUBLICATION.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/PUBLICATION.json); [delivery/B2_BACKUP_ACK.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/B2_BACKUP_ACK.json); [delivery/S_PUBLICATION_RECEIPT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/S_PUBLICATION_RECEIPT.json); [delivery/C_PUBLICATION_RECEIPT.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/C_PUBLICATION_RECEIPT.json); [delivery/FINAL_BACKUP_ACK.json](https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/delivery/FINAL_BACKUP_ACK.json) | Later result/review/delivery outside B1; S/B2 science; D/E/B3 actual tail |

## Copyable handoff

```text
# HE-ANG-CBA-NORDSIECK — 실제 전달 완료 인계

사용자가 선택한 physmath-research-loop builtin1.0.0을 유지한다. 정의된 analytic direct-CBA 이론·코딩 단위는 실제 D에서20/20 scoped이며 R6PASS, R7PASS_WITH_DIAGNOSTIC, 독립 Astra C9/root PASS_SCOPED_DIRECT_CBA다. 전체 HE-ANG은 SOURCE_INPUT_PENDING, global physical completion=null이다. 이 정의된 한 단위의 전달을 닫고 중단한다. 새 loop, unusedreserve 소비, merge, activation을 시작하지 않는다.

## 1. 정확한 identity와 첫 읽기

Repository cosmosapjw-quantum/BASS_HE; branch research/he-ang-cba-nordsieck-20261025; stacked base research/he-ang-finitemass-shell-20261024. Draft/open/unmerged PR100: https://github.com/cosmosapjw-quantum/BASS_HE/pull/100 . Actual PR HEAD는 D이며 merge=false/activation=false다.

S commit a891cd4b9a3548e66db669b9eb472fea88a3b78b; tree ee6768ab8a934cb9b47819a24cf5498e4f8b8ece
C commit 7caca70d94d03732bff5e7adf2f9aa5cf59310ec; tree ebeaf6623dfd0077adae43933f8494056e8974c8
D commit 8e0fb28fea520364d8794bac32840621dd150f95; tree b1cff8c85f9c343f8d0f1d3192e638023f0d5157
E commit 14976bda37b17e8dd8060f4c89adf6ddf9fbcc6a; tree 722c8103ba2d68d6c2b86e2be4d64348c34a3dfc

중앙 repository cosmosapjw-quantum/rei_bianchi, canonical branch research/orchestration-sandbox-20261022. Current E는 root가 actual threeblobverification을 확인한 immutable identity다. S는87files/18of20, D는102files/20of20. C와E는 각각3files의 ownHE관측/인계/별도return만 변경했고 other39nodes/40contracts/7authorities/17integrationedges 및 oldHEfields를 보존했다. S/D의 역사적 E/B3pending을 소급 수정하지 않았으며 이 최종 외부 PR100receipt가 actualtail을 연결한다.

첫 읽기:
https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/FROZEN_CONTRACT.json
https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/THEORY_KO.md
https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/RESULTS_KO.md
https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/LOOP_PROGRESS.json
https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/CLAIM_GATE.json
https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/reviews/ROOT_ADMISSION.json
https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/reviews/C9_REPORT.json
https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/execution/RESOURCE_LEDGER.json
https://github.com/cosmosapjw-quantum/BASS_HE/blob/8e0fb28fea520364d8794bac32840621dd150f95/research/he_ang_cba_nordsieck_20261025/evidence/survey/INHERITED_LEDGER_REFERENCES.json
https://github.com/cosmosapjw-quantum/rei_bianchi/blob/14976bda37b17e8dd8060f4c89adf6ddf9fbcc6a/research/orchestration_longterm_20261023/assembly/DAG.json
https://github.com/cosmosapjw-quantum/rei_bianchi/blob/14976bda37b17e8dd8060f4c89adf6ddf9fbcc6a/research/orchestration_longterm_20261023/assembly/HANDOFF_BASS_HE_KO.md
https://github.com/cosmosapjw-quantum/rei_bianchi/blob/14976bda37b17e8dd8060f4c89adf6ddf9fbcc6a/research/orchestration_longterm_20261023/assembly/returns/RETURN_HEANG_CBA_NORDSIECK_20261025.json

## 2. 수학·규약·검증 범위

THEORY_KO(1)–(9)의 고정핵 비상대론 수소1s labelled direct Coulomb–Born model이다. eta,p,q를 고정해 no1/r overlap K=-partial_lambda I를 먼저 유도하고 뒤에 matched eta=lambda/p를 적용한다. Hydrogen은 lambda1,eta1/p다. K(lambda,-p,p;eta)=2I0*(lambda-eta*p)/(p²+lambda²)이며 matched orthogonality와 Delta0의 exact0을 보존한다. Matched directDelta polynomial은 K=16*pi*lambda*C*[Delta²-(1+i*eta)Delta.p]/(A²*Bc). Generic 두큰항 subtraction과 구분하고 주경로로 사용한다. lambda,p>0에서 Im(Bc)<0이며 principal Log(Bc) 가지를 고정했다.

Nc=(2*pi)^(-3/2)*exp(pi*eta/2)*Gamma(1-i*eta), normalized1s와delta-state F_D에 대해 TDCS=4*(p_f*p_B/p_i)*abs(F_D)^2/Delta^4다. Box-state golden-rule/density/flux와 delta-state계수를 독립적으로 맞췄다. 직접 spin-diagonal 채널 spinfactor1, exchange absent, labelled role/count이다. eta0 plane-wave control은 nuclear subtraction을 유지한다. a0,p0,E_h 및 physical TDCS a0²/E_h scaling을 명시했다. finite-Mcoupling=false이며 PR99kinematic shell에 임의 결합해 source-consistent finite-M dynamics라고 부르지 않는다.

실제14targetedtests PASS; generic9, original-integral Eq6 mp50quadrature4, tinytransfer16, normalization7, illustration73 controls PASS. 최대 관측오차: binary64generic scaled1.0629567988304066e-15; mp50-vs80 scaled9.183265145706724e-51; quadrature3.506764608003949e-51; stabletiny true-relative4.0063870834280886e-16; normalization1.5116805406513489e-15; TDCScoefficient7.159247292900658e-16. Scaled=abs(v-ref)/max(1,abs(ref)); tiny nonzero mp80reference만true-relative다. Frozen tolerance는 실행 뒤 바꾸지 않았다. Global/outward bound를 주장하지 않는다.

Tinytransverse t1e-14 fixture의 genericrelativeerror1.742881133761018e12와stable1.928809976914049e-16, parallelgeneric0.016729855113103972/stable1.8021982992221216e-16은conditioning진단이다. 물리 Delta0ionizationevent를 뜻하지 않는다. Illustration은250eV incident/5eV ejected/3degree scattered, nominal27.2eV/Hartree, -180..180degree step5의73angles다. 표본최대 -50degree에서 directCBA0.45610407121581825/directplane0.9421399651692766 a0²/(eV sr²). Fit/data재계산/연속각max증명이나20/54.4/413.6eV calibratedphysicalvalidity를 주장하지 않는다. 그림은 savedJSON만 읽어 생성하고 C9/root가 실제PNG를 보았다.

## 3. 원전 위치와 남겨 둔 문자적 문제

Primary author preprint arXiv:physics/0411013v2, https://arxiv.org/pdf/physics/0411013 ,326595bytes/SHA256b14f054de037722bb21ab8911b0b3917f0978b18dab9c916427d02115ccceda1. Related publication DOI10.1103/PhysRevA.71.062705의 published equations와동등성/교정 여부는 확인하지 않았다. Eq19/A9 Iendpoint와bra Γ(1-iη),1F1(iη;1;i[pr+p.r]) conventions를 사용하고 scalar fluxnormalization/no1r overlap은 독립유도했다.

Eq18의 extra1/r는 Eqs5–7/16과 문자적으로 다르고, AppendixA1 exponent와A7의 -Q=q+p 부호도 문자적불일치로 유지한다. Source Eq28J는1F1(1+iη;2;...)의 별도적분이며 이번K와다르다. Source Eq19reference16은 Massey–Mohr ProcRoySocA140,613(1933); Nordsieck1954 PhysRev93,785의reference로오인하지 않는다. PublishedPDF401/이전403와Nordsieck/RoyalSocietyaccess401/timeout은 접근실패로 보존하며 부재/no-go를 추론하지 않는다. FullPDF/text/pageimages/rawsourceproviderbody는 공개/backup에서 제외했고 bibliographic metadata,hash와선택식만 유지했다.

## 4. 실제 실행·실패·비용과 이전 원장

현재3scientificchildren: testsCPU0.2772319999999999/wall0.3188933669953258; analysisCPU2.580506/wall2.6289747010014253; saved-outputplotCPU2.130236/wall2.174621346995991s. 합CPU4.987974/wall5.122489414992742s. 새할당20CPU/60wall,512MiB/1thread. Repairreserve1미사용,기존budget/reserve이전·초기화0, oldsuite 및 currenttests/analysis replay0.

첫03plot 호출은0byte RUN.lock으로 START/child전에막혔다. 실제02terminalexit0/FINISH/관련activeprocess0/03START없음을 확인하고 rawtraceback/lockstat/cleanupauthorization을 보존한 뒤 그lock만제거했다. 이후 첫actualplotchild PASS. Lock발생/cleanup실패원인 NOT_ESTABLISHED,prelaunchCPU UNKNOWN_NOT_ZERO. Scientificchildfailure/reserve사용으로 바꾸지 않았다.

Wolfram original1call:12True/5structuralFalse/1unevaluated. Targeteddiagnostic1call의6residuals는Together/FullSimplify/exactrational모두0. Cancel항별표현을SameQliteral0으로비교한false-FAIL을 교정했고original을유지했다. Evaluator2toolwall16.886/bodyCPU0.304298/bodywall0.304892s; genericcontext1toolwall20.315s; alltoolwall37.201s. Thirdcall없음,remote전체CPU UNKNOWN_NOT_ZERO. SciSpace2search/Exa2search+2fetch4URLs와각401/timeout은 actualcurrentcounts다.

S0=86fc9206d885633b59745fb80dcc22fa163bfd89,tree0bb5ec1818488bf92828d3e4f92c8a20d6468ec6의CSV CRLF→LF는PUBLICATION_SERIALIZATION_BYTE_IDENTITY_MISMATCH다. unit_delivery.read_text universalnewline이 원인이고 successorS가 rawCSV한파일만expectedS0/forcefalse로교정했다. OriginalS87stage/failedpacket/failurereceipt보존; no physics/numericschange, no scientificrerun/newC9/localreserve. FinalrawCSV6069bytes/74CRLF,blob4fb9ffe5353c2526b9a16d6e47aae196c1c5b1a6. RootverifiedS87/87,D102/102,각C/E3blob. D는6allowedcurrentdocs+15operationalevidence이며81Sfiles/39science-code-raw-review-execution byte동일;88otherresearchtrees/14rootentries동일.

별도운영CPU/wall(s): metadataprep0.038864099000000006/0.040913912998803426; B1pack0.07220352099999999/0.0722468569947523; Sassembly0.04895616800000001/0.050382883004203904; Cassembly0.050501431/0.05072827399999369; B2pack0.161368652/0.16143304800061742; Dassembly0.060255385999999994/0.06030375500267837; Eassembly0.050843099999999995/0.050844377001340035; B3pack0.11422022600000001/0.1143476159995771. 이들은완전한project총비용이아니다. 모델/provider/host/IO/prelaunch/remoteunknown을0으로환산하지않고 end-to-endcap을입증하지않는다. 최종prose/metadataIO CPU도별도UNKNOWN_NOT_ZERO다.

ParentPR99 actualS8d481ed47f57774f48bcfb412671ff927601316e,C407381b302d8b98f251b54d277823997bc4fca9f,Dbec636ffa3014035292c1078a758c7aa1827174d,E9600a605f6380bc2262d0cfce5ff00290e594a5a,20of20scopedkinematics다. LocalCPU2.484451/wall2.519181445000868,3children8/30,reserve0used1remaining이나추가실행권없다. PR98TDCS413CPU3.117567/wall3.242023329999938,4children10/40,reserve1used0remaining. PR97PWBEtotal5attemptsCPU3.304038/wall3.4507949489989187,8/30,reserve1used0remaining. TDCS54CPU1.887889/wall1.9431963300012285; CCCCPU1.410021/wall1.4436621759814443; DDCS20CPU1.9570049999999999/wall2.104758352987119; HexCPU18.434312000000002/wall18.739398924000852과모든실패/overshoot/unknown은원본exactreferencechain을재사용한다. HE-ANG-CONTRACT/X1/HE38/D10도그원장·identity연결을보존한다. 과거suite/ledger를재실행하거나grandtotal/reserve를리셋하지않았다.

## 5. 실제 backup과 복원

B1: HEANG_CBA_NORDSIECK_B1_PREEXECUTION_20261025.tar.gz
bytes 792680; members 77; uploadedbytes SHA256 afa42e0e7ed6b8d963528a0cb480bbb5373cfcaa18c1791429b6afbf731ccdcf
Drive 18KqAWKFtZE5K0t0-TzVUMFEQJXc-oTWo; Dropbox id:BSpOijBcT10AAAAAAD_9qA; revision 65e9d4324fca80af03d47

B2: HEANG_CBA_NORDSIECK_SCIENCE_20261025_a891cd4b_7caca70d.tar.gz
bytes 2054451; members 142; uploadedbytes SHA256 a3525a7d739695f2755de50f761524b98190b4d7b4dbcb67392e9cd6da4c2911
Drive 10VI1GXobkRS-r1dWrxb-_nSHjg9phvRV; Dropbox id:BSpOijBcT10AAAAAAD_9tg; revision 65e9ddf554b230af03d47

B3: HEANG_CBA_NORDSIECK_DELIVERY_20261025_8e0fb28f_14976bda.tar.gz
bytes 734417; members 140; uploadedbytes SHA256 9027c29a0b441ac6028a0cae673342fa6f60f9e97e758ad130aff153ec02fa28
Drive 1WJsOVDtjKOACcz3ieGI7LI_fzAsf_BZ-; Dropbox id:BSpOijBcT10AAAAAAD_9tw; revision 65e9def9675500af03d47

세checkpoint는 exactlocalmemberverification,actualdualproviderupload와별도metadata ID/sizeACK다. Independentremote wholeGET/SHA256은 이번B1/B2/B3에대해 수행했다고주장하지않는다. B1은preexecutionhistoricalsnapshot이다. 최신복원은B2 exactS87/C3와wholeB1once/inherited/dependency/publicationcorrection/postS scope를복원한뒤 B3 exactD102/E3 actualreceipt/preservation overlay를적용한다. B3자신의미래ACK는archive안에넣지않았고 최종PR100externalreceipt가실제tail을연결한다. Finalcopyhandoff/PRbody는그actualACK뒤작성된외부인계다. ParentPR99B1/B2/B3 actualreceipt/복원범위는PR99_CONSTANTS와INHERITED_LEDGER_REFERENCES를읽고 이새checkpoint와구분한다.

## 6. 조사·병렬 owner와 아직 열린 물리 입력

초기조사는7repos/14collections/30pages terminal,1339branches/874openPRs다. Dropbox4929entries/9pages,Drive926documents/3pages+27folders/1page terminal이나documentsearch는binaryarchives전체목록이아니다. KnownIDbackupmetadata확인과구분한다. Conversation은1query-selected이며selfecho/stalePR98B3pending요약을새authority로쓰지않았다. 모든branch본문·모든대화·모든backup전체를실독했다고주장하지않는다.

중앙은oldE9600→2354d6e995fde736fffbcad2d0e40473218cb8c4(CRneutralownerreturn)→b0f02efc6925a98e670136027561d267f9fa601f(PHYS89covariancediagnosis/interface)→actualC→actualE로진행했다. Cachedexactbyte와freshrootref를함께확인해최신owner변경을보존했다. CRneutralchildreportedCPU4.364423/knownlineage34.234445114,coordinator0.028243258분리,fullN4/N5PARTIAL/OPEN/N6N7gated,missingrates/null/DrivehistoricalUNKNOWN유지. PHYS89source-diagnostic/typedfiniteinterface는displayedcovariancestochasticadmissionDISALLOWED,source-defectcauseNOT_ESTABLISHED,physicalparentPARTIAL_INPUT_DEPENDENCIES/BASSnuclearconsumerNOT_BOUND/HH_R10OFF/productionNOT_ISSUED다. Ownerreported3children(2success1failure)CPU0.41658999999999996/wall0.4201385129999835,wholeGET/CRC/restore보고는owner기록이며HEworker가재실행하지않았다. REC135/central227 thermodynamicblockscoped20/20/parentPARTIAL,CPU8.362847/wall8.336637456,primaryserializationfailure/continuation/CI실패와H5uncertainty/H6trace/fullH7OPEN도각owner관측으로유지한다. Canonicalauthority로임의승격하지않았다.

HE-ANG physicaljointamplitude/event의source validity,exchange/spin/count/fullsupport,labCOMframe/finite-Mdynamics/recoil,calibrateduncertainty/consumeradmission은OPEN이다. 이번analyticfixedcentre모델과parentfiniteMshell의결합은별도그의무를충족해야한다. C9-NB-01 futurepartialmu_window/thetametadata,C23E,모든otherownerOPEN,HHphysicalparentsPARTIAL/sourceequivalence/tails/consumer/stoppingOPEN,ANGTHERM02READ_ONLY를유지한다. physical_provider=false,event_sigma=false,physical_recoil_distribution=false,HE-X1empiricalangularcorrection=false,globalcompletion=null. 새strongno-go/문헌최초성주장없다.

## 7. 중단과 향후 재개

ActualS/C/D/E와B1/B2/B3finalPR100readback을확인한뒤이정의된단위를닫고중단한다. 새로운단위가요청될경우먼저actualHEAD/AGENTS/parallelowners/backup/원장identity를읽고유효한근거를재사용한다. 새계약/실행범위가생기기전unusedreserve를소비하거나oldcompletedkernel/suite를재실행하지않는다. 현재newloop/merge/activation권한없음.

```
