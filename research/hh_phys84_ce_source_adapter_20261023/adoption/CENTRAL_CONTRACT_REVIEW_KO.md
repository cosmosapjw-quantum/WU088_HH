# 중앙 인계와 PHYS83 소유자 완료 확인

검토자: `/root/central_contract_review`. 범위: 읽기 전용 원전 계약·현재 ref·PR metadata·역할·후속 연결 검토. 과학 callback, 기존 validation, IVP, benchmark, remote mutation은 모두 0이다. 관측 시각은 2026-10-23 19:16–19:19 UTC다. 사용자 지정 고정 인계를 먼저 적용했다.

## 1. 현재 확인한 identity

- 중앙 고정/현재 branch HEAD: `0f9d9df825be1dac9ca9bdf73cdc2e8908bcba17`. `git/ref/heads/research/orchestration-sandbox-20261022`의 실제 GET으로 현재 일치를 확인했다.
- `assembly/HANDOFF_WU088_HH_KO.md` Git blob: `6598d1bd4cbc149259a7f5eb8de55a320569c785`.
- `atomic/LONGTERM_CONTRACTS.json` Git blob: `f3d96c21f1f113d832507658a9cbcd5651741fa1`.
- `assembly/DAG.json`: 212367 bytes, SHA256 `c627afecab3090b732eaa3472f388c79325e694da5de1d7ee93a0c63dae3df3f`, 40 nodes. 전체 원문을 읽고 저장했다.
- 중앙 root `AGENTS.md` blob: `429a5a13ee75b1222bc50627f8d5973d01dd21c4`.
- WU root `AGENTS.md` at PR140 HEAD blob: `83e41056ef39af8183152f93a32d1285bb1a7f2c`.
- WU PR140 fresh metadata: open, draft, unmerged; head `6a2fc5aacb6182a916b9434c316e99e750e8273c`, base `09289300ec2e500806aa2cb82365f00329e41c8c`, 4 commits, added252/deleted0, updated `2026-10-23T15:45:28Z`.
- PR140 scientific identity: `e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c`. 이 검토에서는 원 실행을 재현하지 않았고 metadata의 완료 주장과 고정 계약을 대조했다. 원본 파일·외부 JSON 검증은 별도 owner-adoption 검토의 근거와 결합해야 한다.

## 2. WU_CE83_OWNER_COMPLETION 채택 범위

원 계약의 필요 출력은 finite native HI LS1s/2s/2p, Delta10.20435eV, 255–50000K, fixed T/ne, optically thin의 132 paired rates, 324 steady rows, 732 transient rows다. 현재 PR140은 이 수량과 같은 조건을 명시하고 독립 71cases/2111assertions PASS_SCOPED, 저장 결과 21 별도 점검군, 새 science1=complete1+failed0를 제공한다. 원 계약의 S0 활성 소유자 기록은 과거 스냅샷이며 현재 owner 완료로 대체 참조할 수 있다.

정확한 기존 입력·출력 identity 확인 후 `WU_CE83_OWNER_COMPLETION`의 해당 supplier 범위를 `NUMERICALLY_CHECKED_SCOPED`로 재사용해 채택하는 것이 맞다. 초기 계약의 OPEN/NOT_RUN 원문을 고치기보다 새 adoption/DAG overlay가 현재 상태와 원 근거를 가리키도록 한다. 이 채택은 새 science 실행으로 집계하지 않는다. 새 validation이 아니라 완료된 2111 assertions와 원 review를 재사용한다.

`CONSUMER_ADMITTED`는 이름 붙은 consumer, 유효한 source/domain/owner가 함께 있어야 한다. PR140 자체의 fixed-bath 완료만으로 외부 thermochemical history, full spectral geometry 또는 physical confidence를 승인할 수 없다.

## 3. 실제 후속 consumer 조사

중앙 DAG에서 `REI-L1`은 named future consumer이며 owner는 `REI adapter; BASS_CR/WU088_HH/REC physical providers`다. 상태는 `PARTIAL_DONORS_OPEN_BINDINGS`, allowed paths는 `research/rei_source_pair_binding/**`다. 입력 source identity/domain, matched number/energy/STF measure, 미지원 stopping의 명시적 nonthermal reservoir, support-zero와 missing-rate 구분, Planck/실제 monopole 구분, 한 사건의 독점적 owner, donor physical uncertainty 보존이 admission 조건이다.

그러나 선행 `REI-L0`는 현재 중앙 계획상 `READY_THEORY_CONTRACT_FUTURE_EXECUTION`, plan_status PROPOSED다. 현재 읽은 원 계약에는 실제 완성 코드가 없다. 그 source columns는 `gas_thermal,binding,uv_radiation,dynamic_escape_radiation,source_reservoir`이며 명시한 사건 벡터는 PI와 RR다. PHYS83 CE의 excited-atom state 및 excitation-storage owner를 자동으로 여기에 끼워 넣을 수 없다. `REI-L1`의 장래 수신용 WU 공급자 artifact는 가능하지만 외부 실행·admission 완료로 표시하지 않아야 한다.

`CR_N5_ATOMIC_ISOTOPE_COVERAGE`는 WU PHYS81/82/83 completion을 실제 input으로 명시한다. 출력은 source-by-species/rate/energy-domain matrix와 unique energy owners다. Missing rate=null, isotope quotient의 정확도별 별도 증명, source threshold 보존을 요구한다. PHYS83 공급자 메타데이터/유한 데이터 exporter는 이 계획된 consumer의 구체적인 입력이 될 수 있지만 isotope physical coverage나 coupled science를 닫지는 않는다.

## 4. 권고하는 가장 작은 실행 가능한 연결

Owner adoption 뒤 별도 additive Draft에서 WU 안에 **고정 source-native HI CE local source-pair adapter**를 구현할 수 있다. 이 leaf는 central handoff의 'ingest owner completion, then separate consumer PR'에 맞는 구체적인 소비자이며 외부 REI 모델을 수정할 필요가 없다. 입력은 저장된 rate_grid의 정확한 T 행, explicit n1s/n2s/n2p, electron density 및 total thermal-particle density다. Off-grid T의 interpolation 또는 rate callback은 별도 계약이 없는 동안 허용하지 않는다.

상태 i=2s,2p에서 u_i=n_e n_1s q_up_i, d_i=n_e n_i q_down_i, r_i=A_i n_i라 두면 새 adapter는 다음 순간 source를 반환한다.

- dn_1s/dt=sum(-u_i+d_i+r_i), dn_i/dt=u_i-d_i-r_i. HI nuclei와 charge는 보존된다.
- Qthermal=Delta sum(d_i-u_i), Uexc_dot=Delta sum(u_i-d_i-r_i), Qescape=Delta sum(r_i). 합이 정확히 0이다.
- CE와 bound-bound decay는 thermal-particle number를 바꾸지 않는다. fixed composition instantaneous source에서 Tdot=2 Qthermal/(3 k_B Nthermal).
- 2s의 2gamma와 M1 branching을 별도로 보유한다. 2gamma 사건의 pair energy는 Delta이며 photon number는2다. M1/2p의 photon number는1이다. 공급하지 않은 2gamma spectral shape를 만들어내지 않는다.
- unpolarized optically thin source의 normal-frame isotropy를 명시하고 signed tensor assembly의 외부 claim은 별도로 둔다.

이는 저장한 rate data를 다른 stock 상태의 새 source columns로 사용하는 작은 algebraic consumer다. 원 science callback/기존 population trajectory/old verification은 호출하지 않는다. 독립 기대값의 event columns, atom/charge/thermal-number/energy invariants, zero-stock·positive-stock·2gamma owner·missing-T 및 invalid-domain rejection으로 최소 targeted 검증을 정의할 수 있다. 원 source 불확실성·finite support·LS approximation 한계는 그대로 전달한다. 새 식/코드 결과는 이 실제 leaf에 한해 NUMERICALLY_CHECKED_SCOPED/CONSUMER_ADMITTED 여부를 판단하고, REI-L1의 future integration은 OPEN으로 둔다.

이 구체적인 local consumer를 선택하지 않는다면 central list의 다음 source node들은 서로 선행 관계가 없는 병렬 leaf다. 두 번째로 적힌 `WU_LI_SOURCE_UNCERTAINTY`는 instrument response/deconvolution/isotope/target-state의 원전 확보가 필요한 source-analysis 단계다. 현재 PHYS82 family spread만으로 새 confidence envelope를 닫을 수 없다. `WU_D_PI_RR_MATCHED`는 PR135의 보존된 event adapter에 실제 isotope-matched PI/RR source moments를 공급하는 명확한 다음 science 방향이며 원전과 Milne degeneracy/frame 계약을 먼저 닫아야 한다. 순서상 첫 노드 외에는 목록 순서 자체가 의존성을 만들지 않는다.

## 5. R/C 역할과 gate의 실제 출처

고정 WU handoff, LONGTERM_CONTRACTS, assembly DAG에는 R1–R10/C1–C10이라는 단계 이름의 별도 역할 표가 없다. 정확한 단계는 사용자 지정 `physmath-research-loop` 내장1.0.0의 THEORY_LOOP.md/CODING_LOOP.md를 따른다. 두 파일 전체를 실제 읽었다. 중앙 AGENTS는 Astra 계약/이론·수용기준/독립판정과 lower-tier 구현/targeted tests/bounded runs의 역할 분리를 요구한다. 사용자의 최신 적용 지시와 결합해 아래 매핑을 사용하는 것이 출처에 맞는다.

| 단계 | 실제 단계명 | 현재 작업의 책임/근거 |
|---|---|---|
| R1 | 연구 위치·계약 | controller: pinned central first-node, latest owner, new leaf boundary |
| R2 | 근거·재사용 | owner/source reviewers: PHYS83 frozen evidence and current ref |
| R3 | 주장·전제 정렬 | controller: finite native LS source and consumer scope |
| R4 | 가설·표현 탐색 | controller: event columns/atomic storage representation |
| R5 | 구성적 유도 | controller/theory authority: conservation and thermal-number derivation |
| R6 | 독립 검증 | independent Astra-tier reviewer: equations and assumptions |
| R7 | 판별 검증 | authorized bounded algebra; completed PHYS83 evidence reused |
| R8 | 결과 판정 | authority: scoped PASS/HOLD, no new strong no-go claim |
| R9 | 정식 결과·코딩 연결 | authority freezes input/output/domain/acceptance contract |
| R10 | 종료·재개 | controller: current result + next obligations, not full-DAG completion |
| C1 | 목표·baseline | controller + coder receives exact PHYS83 final pin |
| C2 | 식–데이터–코드 | coder traces saved-row/event-column mapping |
| C3 | 수치 설계 | authority freezes exact-row behavior and independent checks |
| C4 | 실행 DAG·자원 | controller preserves cumulative debit, shared lease, one worker/thread |
| C5 | 구현 | lower-tier coder, task-owned new paths only |
| C6 | 구현 검증 | coder, one bounded targeted command, preserve failure receipts |
| C7 | 과학 검증 | coder executes frozen invariant/reference obligations |
| C8 | 수치·재현성 | record true costs/precision and preserved source identity |
| C9 | 독립 검토 | fresh Astra-tier reviewer reads diff/raw outcomes; no self-admission |
| C10 | 판정·인계 | authority scoped decision; expected-SHA additive Draft and dual backups |

Claim sequence: OPEN → DERIVED_SCOPED → IMPLEMENTATION_VERIFIED → NUMERICALLY_CHECKED_SCOPED → CONSUMER_ADMITTED only with named consumer and valid source/domain/owner. Derivation, implementation verification, numerical/scientific execution, independent admission, publication, backup and DAG status remain separate axes.

## 6. Budget, publication, backup, coverage

All six WU central contracts record inherited_spend=null, remaining=null, currency=null and explicitly state unknown is not zero / retain campaign receipt / no new heavy launch. These fields are not replenished by owner adoption. Reuse actual PHYS83 spend/failures from its external JSON; a distinct lightweight algebra/check allowance needs a named frozen cap and true incremental cost, without representing the unknown campaign remainder as available money.

Central DELIVERY_ACK.json is a historical provider-ACK/size receipt for S0/S1 and 77 Git blob checks; it explicitly does not claim full remote ZIP bytes. PHYS83 PR140 separately asserts actual full dual ZIP restore and external JSON readback. Root is recovering those authoritative bytes. These are distinct evidence classes.

The current bounded search queried each of rei_bianchi and WU088_HH with updated>=2026-10-23, top5, sort=updated desc. REI returned PR222/221/220; WU returned PR140/139/138. Search does not expose a total/cursor. Root AGENTS and selected central contract files, two selected central subtrees and actual orchestration branch ref were read. This is not a fresh exhaustive inventory of branch contents, private conversations, external hosts or all backups.

A new WU consumer should be an additive descendant of the actual PR140 HEAD. Preserve old final files, source branches, original central author contracts and completed science. CAS/expected_sha publication, Draft=true and merge=false remain required. An additive WU overlay and central-return handoff can report adoption without overwriting the unrelated central owner branch. Any central remote mutation needs its own current-head/parallel-owner inspection.

## 7. 선택 확정 및 추가 현재 근거

Controller는 위 실행 가능한 연결을 **`WU_HI_CE_INSTANTANEOUS_SOURCE_V1`**로 선택했다. 이는 WU 안의 명시적 receiving contract이고, REI-L1 수신 준비는 아직 external consumer admission이 아니다. 중앙 저장소의 owner branch를 변경하지 않고 WU의 additive overlay/return handoff로 현재 상태를 전달한다.

추가 actual Git ref GET은 다음과 같이 기존 parent 두 브랜치가 움직이지 않았음을 확인했다.

| Branch | Actual HEAD |
|---|---|
| research/hh-phys83-ce-completion-20261023 | 6a2fc5aacb6182a916b9434c316e99e750e8273c |
| research/hh-phys83-matched-ce-radiative-20261023 | 09289300ec2e500806aa2cb82365f00329e41c8c |

Fresh Dropbox final ZIP metadata: id `id:BSpOijBcT10AAAAAAD_6kg`, 7473461 bytes, revision `65e83b602d83a0af03d47`, server_modified `2026-10-23T15:34:07Z`, downloadable=true. 이 확인은 metadata이며 새 Dropbox full-body verification이 아니다. Root의 OWNER_RECOVERY_RECEIPT는 19:17–19:18 UTC의 실제 Drive raw JSON/ZIP 다운로드와 post-close disk bytes/SHA 일치를 제공한다. 독립 owner auditor의 OWNER_ADOPTION_AUDIT는 19:20:34 UTC에 384payload/252repo/57science bytes와 저장 결과 counts, 기존 양쪽 restore receipts 재사용을 PASS_OWNER_ADOPTION_SCOPED로 확인했다. 본 중앙 reviewer는 그 원 로그를 읽었고 과학 검증을 다시 호출하지 않았다.

## 8. 새 local adapter가 그대로 재사용할 원전

완료 PHYS83 `source_data/HI_CE_SOURCE_CONTRACT.json`을 읽었다. 새로운 physical parameter supplier를 도입할 필요가 없으며, 새 leaf는 저장 q row와 아래 기존 원전의 같은 근사 정의를 보존하면 된다.

| 채택 대상 | 원전/원문 위치 | 해당 scope |
|---|---|---|
| HI LS CE rates의 입력 | https://atom.curtin.edu.au/CCC-DB/H/I/ELECTRON_IMPACT/e-H_XSEC_LS.zip | 실제 owner snapshot SHA256 57730e72656639e92c47c1b8457db0edac5a69ae93db6c357471a93759af1fc9; selected 2S.1S/2P.1S와 reciprocal source |
| CCC 이론 인용 | https://doi.org/10.1103/PhysRevA.46.6995 | Bray/Stelbovics1992. Full-paper 접근 벽이 있던 범위는 원 기록 그대로 유지 |
| 2s/2p radiative A와 branch | https://sohoftp.nascom.nasa.gov/solarsoft/packages/chianti/dbase/h/h_1/h_1.wgfa | 보존 SHA256 f16d0f5033632ce5a3104bfa4dfec9c98fc14bb2e05f682be3468419c9a90179; 2gamma8.229, M1 2.496e-6, E1 6.26e8 s^-1 |
| Metastable decay 원전 | https://doi.org/10.1103/PhysRevA.26.1142 | Parpia & Johnson1982. 정량 A는 위 official raw file에서 채택 |
| Fine-level 메타데이터 | https://sohoftp.nascom.nasa.gov/solarsoft/packages/chianti/dbase/h/h_1/h_1.elvlc | 저장 SHA256 f7286ef6837989eba038b7b055c8db9f4e1ce8a6a0b3270ccc399fd0b2f6a75b; native Delta를 일부 ledger에서 치환하지 않음 |

새로 이 원전을 다시 내려받아 완료 source identity를 바꿀 필요는 없다. 이 표는 실제 읽은 PHYS83 원전 계약의 재사용 대응이다. 2gamma row의 zero wavelength는 sentinel이고 zero photon energy 또는 autoionization으로 해석하지 않는다. 2s2p mixing, fine splitting, two-photon shape, reabsorption/stimulated terms, continuum tail와 source confidence는 계속 OPEN이다.

HH_R10 remains OFF; production admission remains NOT_ISSUED.
