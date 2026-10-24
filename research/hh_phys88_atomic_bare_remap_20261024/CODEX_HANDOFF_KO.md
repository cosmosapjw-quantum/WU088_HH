# PHYS88 Codex handoff — 결과 재사용과 다음 source/consumer 계약

## 먼저 고정할 identity

Repository `cosmosapjw-quantum/WU088_HH`, Draft PR145, branch `research/hh-phys88-atomic-bare-remap-20261024`.
완료 과학 S2는 `a0853f2a3d1a8e9276a8834bfefca5325d0f9a73`, tree `e3f8a4656351b12cd25d199372e36334a83b9cf6`이다.
Parent PHYS87 FINAL은 `496670cf39b3c2b5ff5e208c01bb135fe96b3780`.
다음 재개는 S2 단독이 아니라 PR145 실제 FINAL descendant와 외부 `PHYS88_FINAL_DELIVERY_20261024.json`, `PHYS88_FINAL_DELIVERY_TERMINAL_20261024.json`의 final_HEAD·raw SHA·양쪽 readback을 맞춰 사용한다. 이 파일을 담는 commit은 자신의 SHA나 이후 remote ACK를 미리 기입하지 않는다.

Scientific identity:
`2712595494bd9d784539d470c4ad0b178314c1ca55d2b0b9a75cb5dc1e6a2774`.

| 근거 | SHA256 |
|---|---|
| CONTRACT revision3 | 8f45d6a70d7cf7ffcc556b74636f25087167a3372f781eee4078f5dd00e4154d |
| frozen implementation manifest26 | 9d2c0a45b74dc1e328f537aefa08cb930a2903091db53ff4e26321f710e10873 |
| primary RESULT421150B | 6f3f1e8d6ce07619502dee8683d8322560fe1c13e70ae27f2eb1381969500104 |
| independent reference188804B | a9f596de2a0d4a15c4bae1bf83ef74bbd9565c203b92f00fb850ad46eef257aa |
| independent C9 JSON26877B | 5ad0ccf9ebaadff19de3df531207e51b4afc4e85f02c1be0d50574517bf37198 |

## 필수 읽기와 실행 상태

FINAL_REPORT_KO.md → CONTRACT.json → SCIENTIFIC_ADMISSION.json → DAG_OVERLAY.json → EXECUTION_LEDGER.json → RESEARCH_LOOP_MAP_KO.md → source_data/SOURCE_CONTRACT.json → theory/SOURCE_CONSUMER_HANDOFF_KO.md → reviews/INDEPENDENT_REVIEW.json/.md → delivery/ → 외부 두 JSON → actual PR145 최종 본문 순서로 읽는다.

R1–R9/C1–C9=18/20은 이 commit 전 시점의 고정 관측이다. R10/C10의 actual final dualrestore·JSON readback·DAG·handoff 완료는 이후 외부 terminal에서20/20으로 닫는다. HH_R10=OFF는 workflow R10과 별도 이름공간이다. 전체 물리 목표 완료율은null이다.

Primary1=완료1+실패0,482checks(guards36포함),20integrals=16full+4FD,18relabel+36bare+32owner. 독립 reference1은 최고T에서8fields,1216quad calls/25620callbacks,612numeric source fields. 실제 resume1SKIP/callback0/rewrite0. 새ODE0/rate0/stopping0. 이전 완료 identity 재실행0.

원래 child3성공+affected saved-PDF child1실패=총4. ChildCPU7.322937s, wall7.330995100001019s; metadata-only closureCPU0.0005106s 별도. PHYS87/88 알려진 부분합CPU11.687320s는 전체역사 비용이나 잔여예산이 아니다. Symbolic lineage7calls=PHYS85/86의4+PHYS87의1+PHYS88의2. PHYS88의첫JSON report실패와 진단복구를 모두 보존했다.18scalar exactzeros와 별도 양의 branch proof이며 Wolfram all_zero=False였다. 기존·현재 소진 allowance0을 reset하지 않는다. 금액·전체비용은unknown/null이다.

## 보존해야 할 실제 artifact finding

P88-C9-01은 momentsPDF가4928B로 짧아진 문제이며 원인NOT_ESTABLISHED다. 한 번의 saved-only child는PNG memory byte일치와PDF save후metadata token gate에서exit1을 반환했다. 실패를 보존한 뒤 root가 승인한 같은 길이 timezone metadata 치환으로 최초21400B/SHA `6389368893663f161be17845fa618d8c8e9348d0a10b6eeccddf9876f18dbde7`를 복구했다. 최초FIGURE_RECEIPT와2PNG+2PDF전체bytes가 맞는다. Primary/reference/source replay는없다. recovery/와 reviews/P88_C9_01_*를 유지한다.

## 다음 구현은 물리 계약 뒤에

정식 다음 노드는 `NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT`다. 원전σ/angularlaw의 atomic→bare 적용, electron/target state, covariance/support/tail, named thermal/fast/radiation consumer를 먼저 고정한다. 기존 두 map의 numerical agreement를 실제 source equivalence로 올리지 않는다. 다음 affected identity와 성공 조건/누적 예산/원 공유lease를 root가 닫은 뒤 sandbox coding으로 간다.

같은 source사건의 relabel carrier C와 새 bare사건을 구분한다. C를 전자·heat로 쓰지 않는다. nativeEs 보간을 유지하고σ에는Jacobian을 곱하지 않는다. CommonTκ와joint moments,thermal/fast/rest/photon route,count caloric항을 함께 받는다. h=1instantbirth는stopping계산이 아니다. BASS B3C의properclock/Xonly/newbornmidpoint는설계참조이며 현재nuclear consumer는NOT_BOUND다.

각 노드 전 actualAGENTS·HEAD·병렬delta·backup·완료evidence·누적예산을 대조한다. 기존 checkout에서owned paths만 additive변경,expectedSHA/nonforcepush, Draft유지, main merge없음. 불완전historical working files를 checkout/clean하거나 globalgitadd하지 않는다. 역할은physmath-research-loop1.0.0의R1–R10/C1–C10과root승인/독립검토를 따른다. 1worker/thread·원공유lease·freshmemoryreserve1.5GiB+job.5GiB; 다른process종료금지. Runtime차이만으로 완료science를 다시 돌리지 않는다.

Non-tilted LRS BianchiI,gasπ=0/DMπ_m별도,signedmatter+radiation을 같은normalorthonormalframe에서합한후norm,Frobenius=√2×half-contraction. 동일trajectory성분은species-off인과실험아님; sampledresidual은continuumcertificate아님. HH_R10=OFF,productionNOT_ISSUED.

