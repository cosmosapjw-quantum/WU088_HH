# WU088_HH R15 다음 대화 handoff

이론 R1–R10 / 코딩 C1–C10 완료, **workflow20/20**, **DAG31/46**. 다음 블록을 새 대화에 복사한다. 이 파일 자신의 FINAL commit hash는 자기참조로 넣지 않고, 실제 전달 영수증이 있는 PR150과 최종 응답에 둔다. 아래 science S09 hash는 이미 게시·복원 검증된 불변 지점이다.

```text
WU088_HH R15 연구를 다음 미완 의무에서 이어간다.

Repository: cosmosapjw-quantum/WU088_HH
Branch: research/provider-registry-20261025
Draft PR: https://github.com/cosmosapjw-quantum/WU088_HH/pull/150
Canonical leaf: research/provider_registry_molecular_r15_20261028
Science S09 commit: 1ba1b0727cf3d5ba21931b0f3f14a2beae664f67
Science tree: 0ce9b0de3546bf7ec06782bd70160879fa654827
Scientific payload: 70 files
Payload SHA256: 828888e952c15bd94d37d7dd30c0676df9470ca316bb1dbb8334c6c218b0e909
Frozen manifest SHA256: 5243f3ba03f2a685123025041d644563652007148a13c3117663e7425d27d6f7
R14 parent FINAL: 6ca324dbc5d3c4b5c064f7621730eb0d6ee5eb51
Latest actual paired receipt in this source: S09 1ba1b0727cf3d5ba21931b0f3f14a2beae664f67
FINAL delivery head/archive: take the actual receipt from PR150 or the previous final response; verify current PR head before mutation.

State: R1-R10/C1-C10 20/20; DAG31/46.
Two new conditional completions:
 WU_HD_CUBIC_BERNSTEIN_FORCING_THEORY_R15
 WU_HD_CUBIC_BERNSTEIN_FORCING_CODE_R15
44 inherited node objects unchanged. Central/physical admission delta0.

Result: original nonnegative rational Bernstein-B3 forcing -> positive B4 global memory; zero-aware derivative-variation subdivision gives splits<=3D, visits<=6D+1, D96=>288/577 per cell, exact gap<=M_B*2^-96<=4Cmax*2^-96. Dyadic128 overhead<=2*2^-128. Signed dc propagation uses positive B4 exponential moments; whole-E majorant and polynomial endpoint propagation remain distinct.
Preserve full A=K+wH, H=pi*d^T-diag(d), fixed K/pi/destruction, all allowed start/history certificate, whole fine/coarse forcing bounds, source/state/norm/clock identity, original-t0 memory, E=abs(eta), coarse l1=4E. Constant-w verification does not by itself cover switching histories. Comparison lower is not physical-error lower. Input cone is not every pointwise-nonnegative cubic; R14 quadratic preprocessing remains separately valid.

Actual evidence: primary302/302; independent reference302/302, guarded784/784 with strict Decimal miss59 retained and first50examples. Reference exact238/mixed21/guarded42/metadata1. Wolfram72/72 exact zero, observed warning0. R6 24/24, C9 20/20 material0. 30 frozen files and70payload identities unchanged. Saved PNG2/SVG2 actually visually reviewed.
Actual processes: primary1/reference1/CAS1/renderer1, repairs0, ODE0. Scientific Python CPU~2.629162s, renderer~3.270585s; CAS CPU and full historical/global remainder null.
All base allowances0; unused primary1/reference1 repair reserves expired at C10; future unit allowance0. Existing evidence is reusable. Do not reset old counters or automatically replay complete science.

Accessible census:51repos/2418heads/66pages;1184openPR/85pages; recentclosed51pages. Drive WU167folderlists/1257items and Dropbox dossiers5381rows/9pages terminal;45archive pairs matched. PersonalContext2calls available but no full-conversation enumeration API.20attachments unchanged. Use exact cutoff/read-scope records; do not claim every historical body was read.
S09 actual Dropbox original GET: 1623172bytes, SHA256 9c9af8993a8783fd98b564941f713eb8d753fa5423ce3bb34510552bff5dd5ef; CRC and all243source members match. RemoteGit70payload blob/size match. Other backup ACKs are not automatically original-GET restores.

Next input: actual GL2022 HD reactive array (DOI10.1063/5.0128598), native state/order/units/support, named consumer, density/clock, whole-forcing and full-A certificate binding. Status INPUT_PENDING_IN_INSPECTED_SCOPE; native v UNSPECIFIED; MISSING_NOT_ZERO; TIQM/SQM DISTINCT; HH_R10 OFF; production NOT_ISSUED; L4 false. Optional distinct next theory proposal: exact preprocessing for a broader nonnegative cubic cone; not started and no new nodes/budget.

Read REPORT_KO.md, HANDOFF_KO.md, SCIENTIFIC_ADMISSION.json, DAG.json, CONTRACT.json, POLICY_DELTA.json, EXECUTION_LEDGER.json, SCIENTIFIC_PAYLOAD_MANIFEST.json, reviews/C9_FINAL_REVIEW.json, NEXT_INPUT_CONTRACT.json, delivery/PUBLICATION_INDEX.json.
Use physmath-research-loop with current explicit task scope. User-authorized scope supersedes stale prior policy only where actually applicable. Root-only expected_SHA/force=false research-branch publication; no main merge or other-owner mutation. Preserve source and first failure identities. Return evidence identity, actual commands/resources/results, remaining obligations, and per-stage completed/total DAG counts with actual backup/publication receipts.
```

## 실행 인터페이스와 수용 payload

기존 interface는 `src/cli.py --input ABS_INPUT --output ABS_NEW_OUTPUT`다. Base campaign의 정확한 명령·runtime·resource 기록은 `raw/PRIMARY_PROCESS.json`, `raw/REFERENCE_PROCESS.json`, `raw/CAS_ATTEMPT.json`, `figures/RENDERER_PROCESS.json`에 있다. 기존 source/입력/결과의 identity가 유지되면 해당 실행을 재사용한다. 새로운 입력·계산은 그 변경 범위에 맞는 계약으로 시작한다.

후속 반환에는 immutable source/tree, 입력 SHA와 source/state/clock, actual run count와 CPU/wall/memory, 원래 실패/경고, exact와 guarded 결과의 분류, acceptance 판정, 출력 파일 identity, 실제 게시·백업·복원 여부를 담는다. 현재 scientific payload70파일에 후속 결과를 덮어쓰지 않는다.
