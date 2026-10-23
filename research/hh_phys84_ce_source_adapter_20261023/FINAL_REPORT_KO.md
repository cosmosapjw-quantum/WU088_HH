# PHYS84: PHYS83 완료 채택과 H I 보존적 순간 source 준비

## 현재 판정

중앙 인계의 첫 노드 `WU_CE83_OWNER_COMPLETION`을 실제 PHYS83 owner의 완료 근거로 채택했다. 새 `WU_HI_CE_INSTANTANEOUS_SOURCE_V1`은 물리 계약과 유도를 닫고 코드를 작성·동결했으며, 독립 정적 검토를 통과했다. **새 수치 검증은 공유 lease가 child 시작 전에 거부하여 대기 중이다. 실제 16행 source application은 시작하지 않았다.** 새 adapter의 claim은 `DERIVED_SCOPED`에 유지한다.

별도 additive Draft는 [PR141](https://github.com/cosmosapjw-quantum/WU088_HH/pull/141)이다. 실제 PHYS83 final을 부모로 사용했고 main을 병합하지 않았다. S0는 `ce14c0bfc0318662673b021a08f4029d6a36c7a7`, 준비 코드·검토·자원 대기 S1은 `3c04b6eecd6d1f425e8b6aa5d54b81ec56ffe173`이다. 최종 metadata HEAD와 최종 양쪽 복원 결과는 순환 자기참조를 피하기 위해 **외부 `PHYS84_FINAL_DELIVERY_20261023.json` 및 PR141 최종 본문**을 권위로 삼는다. 이 보고서의 파일명은 전달 문서의 종결을 뜻하며 미실행 과학 계산의 완료를 뜻하지 않는다.

| 단계 | 실제 상태 |
|---|---|
| PHYS83 owner 채택 | 기존 완료 evidence를 `NUMERICALLY_CHECKED_SCOPED`로 재사용 |
| PHYS84 물리·source 소유권 | 고정 계약, 유도, 독립 검토 완료 |
| 새 기호 검산 | Wolfram 두 evaluator call, 채택된 scalar zero 19 |
| 구현 | v5 동결, 독립 정적 검토의 차단 지적 0 |
| 새 수치 검증 | lease 요청 1, 거부 1, child 0, assertion 0 |
| 새 실제 application | 0회, 결과 0행; 예정은 8상태 × 2경로 = 16행 |
| 실제 완료 resume | 미실행; 완료 결과가 아직 없음 |
| S2 과학 checkpoint | 생성하지 않음 |
| REI-L1 consumer admission | `NOT_ISSUED`; state/storage/source/clock binding OPEN |
| HH_R10 / production | `OFF` / `NOT_ISSUED` |

준비 artifact identity는 `dca969a27fa00a703efb4c9f341efb5e50b45b2d88f5896a66f2c4aeced0a0db`다. 이는 7개 계약·유도·코드·oracle 파일의 metadata identity이며 새로운 완료 science identity가 아니다. 해당 identity 문서까지 포함한 8개 파일을 [준비 파일 manifest](delivery/PREPARED_FREEZE_MANIFEST.json)로 동결했다.

## 1. 시작점과 기존 근거의 재사용

먼저 [고정 중앙 인계](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/0f9d9df825be1dac9ca9bdf73cdc2e8908bcba17/research/orchestration_longterm_20261023/assembly/HANDOFF_WU088_HH_KO.md), 실제 owner PR140, AGENTS, 관련 최근 변경과 백업을 대조했다. 인계의 PR139 S0는 owner가 진행 중이던 시점의 기록이었다. 실제 완료는 [PR140](https://github.com/cosmosapjw-quantum/WU088_HH/pull/140), final HEAD `6a2fc5aacb6182a916b9434c316e99e750e8273c`, science identity `e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c`이다.

저장된 rate 132행, steady 324행, transient 732행과 57개 동결 과학 파일을 채택했다. 기존 71 cases / 2111 assertions, 과학 실행 1=완료1+실패0, 기존 resume skip1/callback0은 원 소유자의 완료 기록이다. 이번 단원에서 그 수치 검증, rate 계산, population solve, resume를 반복하지 않았다. 독립 byte/metadata adoption audit의 29개 그룹이 통과했다. 첫 audit의 `science_callbacks` 키 이름 진단은 audit 전용 실패 1로 남겼다. [채택 검토](adoption/OWNER_ADOPTION_REVIEW_KO.md), [raw audit](adoption/OWNER_ADOPTION_AUDIT.json) 참조.

기존 51 repository / 2175 branch inventory와 앞선 bounded delta 기록을 재사용했고, 이번 관련 WU/REI 최근 PR·선택 refs·계약·backup metadata만 현재성 대조했다. 전체 branch 내용이나 접근 불가능한 비공개 대화를 전수 확인했다는 주장은 하지 않는다. 외부 실행 호스트의 상태와 금전 누적·잔여 예산은 확인되지 않은 값으로 유지했다.

최종 게시 전 중앙 branch의 실제 HEAD는 `68420637a9ab54ada92afd786c5733bc0764b8c9`로 전진했다. 그 HEAD의 AGENTS, WU 고정 인계, atomic contracts 세 Git blob은 최초 pin과 동일했다. 현재 중앙 DAG의 관련 계약도 읽어 새 WU 완료를 덮어쓰는 근거가 없음을 확인했다. 따라서 동결 물리 계약은 원 pin을 유지하고, 새 현재성 관측은 [FINAL_CURRENT_DELTA.json](adoption/FINAL_CURRENT_DELTA.json)에 별도로 기록했다.

## 2. 물리 계약: 사건에서 에너지 source까지

PHYS83의 source-native H I LS `1S/2S/2P`, heavy stationary target, Maxwellian electron, unpolarized 상태를 유지한다. 입력은 저장된 66개 **정확한 float64 온도** 중 하나와 `n1s,n2s,n2p,ne,Nthermal`이다. 온도 범위는 255–50000 K지만 연속 보간·외삽을 제공하지 않는다. 입력 밀도 범위, Nthermal의 양성·상한·입자수 조건, native/detached radiation owner와 명시적 excited-state owner를 검사한다. 모든 시간 source는 같은 normal orthonormal frame의 local proper seconds를 사용한다.

native Δ=10.20435 eV를 collisional excitation, deexcitation, excited-atom storage와 방출광에 공통으로 사용한다. 부모의 `A2γ=8.229/s`, `AM1=2.496e-6/s`, `AE1=6.26e8/s`를 유지한다. CHIANTI의 다른 spectroscopic 에너지를 한 장부에만 끼워 넣지 않는다. source provenance와 불확실성 경계는 [PHYS83 source contract](../hh_phys83_ce_completion_20261023/source_data/HI_CE_SOURCE_CONTRACT.json)에 있다.

각 upper state i에 대해 `u_i=ne*n1s*q_up_i`, `d_i=ne*n_i*q_down_i`다. 사건 벡터는

\[
r=(u_s,u_p,d_s,d_p,A_{2\gamma}n_s,A_{M1}n_s,A_{E1}n_p).
\]

준위 source는 고정 incidence `dn/dt=S r`다. 각 column의 합은 0이고 자유 electron, thermal particle 수와 charge의 net source도 0이다. Ground chemical binding과 excited-atom storage를 분리해 `Uexc=Δ(ns+np)`를 둔다.

| 사건 | 병진열 변화 / Δ | 들뜸 저장 변화 / Δ | 방출광 에너지 / Δ | photon 수 |
|---|---:|---:|---:|---:|
| 1s → 2s 또는 2p 충돌 들뜸 | −1 | +1 | 0 | 0 |
| 2s 또는 2p → 1s 충돌 탈들뜸 | +1 | −1 | 0 | 0 |
| 2s → 1s two-photon decay | 0 | −1 | +1 | 2 |
| 2s → 1s M1 decay | 0 | −1 | +1 | 1 |
| 2p → 1s E1 decay | 0 | −1 | +1 | 1 |

따라서 사건별로, 그리고 합한 source에서

\[
Q_{th}=\Delta(d_s+d_p-u_s-u_p),\qquad
\dot U_{exc}=\Delta(u_s+u_p-d_s-d_p-r_{s,2\gamma}-r_{s,M1}-r_{p,E1}),
\]
\[
Q_{emit}=\Delta(r_{s,2\gamma}+r_{s,M1}+r_{p,E1}),\qquad
Q_{th}+\dot U_{exc}+Q_{emit}=0.
\]

`Qth>0`은 gas heating이다. 반응에 선택된 incoming electron의 전체 운동에너지를 추가로 차감하지 않는다. Two-photon 사건은 photon 2개에 총 Δ를 나누어 전달한다. 단색 Δ/2 spectrum을 가정하지 않는다.

에너지 열은 `gas_thermal, chemical_binding, atomic_excitation, radiation_injected, escaped_radiation, source_reservoir`의 6개다. `immediate_escape`는 emitted energy 전부를 escaped 열에, `emissivity_handoff`는 radiation_injected 열에 둔다. 두 owner 경로는 배타적이다. emitted diagnostic을 다시 더하지 않으며 chemical ground binding/source reservoir 열은 이 bound-bound 계약에서 0이다. 후자의 handoff는 spectrum·transport·residence 계산을 포함하지 않는다.

Common-T ideal bath의 Nthermal에 대해 이 채널의 입자수 source가 0이므로

\[
\dot T\vert_{CE}=\frac{2Q_{th}}{3k_BN_{thermal}},\qquad
k_B=8.617333262145179\times10^{-5}\ {\rm eV/K}.
\]

이것은 순간 source다. 들뜬 상태가 비어 있는 ground-only 상태에서는 충돌 냉각이 들뜸 저장으로 들어가며 순간 emission은 0이다. 반대로 ne=0인 이미 들뜬 2s 상태는 병진열 source 0으로 방출할 수 있다. 따라서 `-Qth=Qemit`는 정상상태 등 추가 전제가 있을 때 도출한다. 두 경우는 고정 모형의 대수적 귀결이며 이번에 실제 16행 계산을 실행했다는 증거로 세지 않는다. [전체 유도](theory/INSTANTANEOUS_SOURCE_DERIVATION_KO.md) 참조.

## 3. 문헌·기호·구현 검토의 실제 범위

현재 공식 [CCC](https://atom.curtin.edu.au/ccc-db/index.html), [CHIANTI H I](https://db.chiantidatabase.org/h/h_1.html) 및 관련 원전을 읽고 부모 source pins를 재사용했다. Exa 검색은 credits limit HTTP402로 1회 실패해 새 성공 검색은 0이다. SciSpace 검색 1회는 문헌 discovery에 사용했으며 새로운 수치 상수를 그 결과에서 대입하지 않았다.

Wolfram context 요청은 internal tool error였다. 첫 evaluator는 nuclei 7column, energy 7column, differential energy, thermal temperature, steady reduction의 17 scalar zero를 반환했다. 같은 call의 two-photon 두 항은 replacement-list 괄호/precedence 문제로 미평가였다. 그 두 항만 고친 두 번째 evaluator에서 2zero를 얻었다. 합계 19zero, 미해결 0이다. 첫 warning과 실패 범위는 [기호 ledger](symbolic/SYMBOLIC_LEDGER.json)에 보존했다. PHYS83의 기호 계산을 반복하지 않았다.

코드는 standard-library binary64, `math.fsum`, source bytes/hash pin, 정확한 저장 온도 matching을 사용한다. 독립 검증 프로그램은 literal CSV decimal로 만든 Fraction 산술에서 사건·준위·에너지 source를 별도로 구성한다. 양의 event/radiation/photon relative gate 2e-12, signed/gross 및 보존 residual gate 2e-13을 고정했다. clipping 또는 residual 강제 0은 없다. 수치 oracle은 작성되었으나 이번 child가 시작하지 못해 assertion 결과는 아직 없다.

정적 검토에서 완료 파일의 canonical bytes, 실제 callback sentinel, bytecode 억제, runtime version과 science identity의 분리, 실제 interface 호출 계수와 JSON 숫자형 변조가 교정되었다. 마지막 보정은 COMPLETE 원문을 `encoded(expected)`와 직접 비교해 `row_count:16.0`도 거부하는 변경과 mock control 하나다. 물리식, 입력과 tolerance는 바뀌지 않았다. [독립 검토](reviews/INDEPENDENT_REVIEW_KO.md)의 현재 판정은 `STATIC_REVIEW_PASS_NUMERICAL_ADMISSION_WAIT`다.

## 4. 자원 대기와 회계

검증 진입 요청은 고정 cooperative lease를 그대로 사용했다. 실제 관측은 capacity8 GiB, available1.0545654296875 GiB, reserve1.5 GiB, job0.5 GiB, admissible_slots0, live_leases0이었다. Outer exit75, lease=null이며 검증 child를 만들지 않았다. [원 영수증](verification/ATTEMPT_01.json)과 [outer 관측](verification/ATTEMPT_01_EXTERNAL_RECEIPT.json)을 분리했다.

후속 읽기에서 사용량 대부분이 file cache로 관측되었다. 하지만 active file cache에 credit을 주는 변경은 동결 admission 의미를 바꾸므로 채택하지 않았다. sysfs reclaim은 쓰기 불가였고 이를 변경하지 않았다. 연결된 대체 장치의 read-only config 조회도 도구 월 사용 한도로 중지되어 외부 자원은 확인하지 못했다. 재연결·재시도·외부 실행은 없었다. [자원 독립 검토](reviews/RESOURCE_GATE_REVIEW_KO.md) 참조.

| 이번 단원의 실행 구분 | 실제 값 |
|---|---:|
| 새 verification lease 요청 / grant | 1 / 0 |
| 검증 child / cases / assertions | 0 / 0 / 0 |
| interface fixture 평가 / mock callback | 0 / 0 |
| 실제 새 16행 application / 완료 / 실패 | 0 / 0 / 0 |
| 실제 완료 resume skip / callback | 0 / 0 |
| 새 rate / population solve / ODE / benchmark | 모두 0 |
| 완료 science identity 재실행 | 0 |
| 다른 process 종료 | 0 |

이 자원 거부는 수치 알고리즘 실패나 과학 실행 실패로 집계하지 않는다. 금전 inherited_spend/remaining/currency는 null로 유지하며 비용0 또는 예산 재충전으로 해석하지 않는다. [누적 ledger](EXECUTION_LEDGER.json)는 부모 완료 기록, 새 기호 검산, 환경·게시·백업을 분리한다.

## 5. 작업 공간 초기화와 복구

S0 게시 뒤 도구 catalog가 바뀌면서 로컬 작업 공간이 초기화되었다. Drive 첫 upload는 catalog rejection, Dropbox 첫 upload는 local source path not found로 실패했다. 당시 미업로드 S0 ZIP 8,496,264B / SHA `b655b5bc5b6d7f2fb0032d138f3e81e5329ec0df4b15f4c4a1818e69526df255`의 bytes는 잃었으며 성공 backup으로 세지 않는다.

S0 Git 14파일은 원 SHA와 전부 일치하게 복구했다. 미게시 v4 코드 5파일은 도구 대화의 literal source/patch에서 복구했고 reviewer가 보존한 초기화 전 5개 SHA와 모두 일치했다. v1–v3 기록은 literal transcript 재구성이며 별도로 남은 초기화 전 hash와의 비교를 주장하지 않는다. 원 검토 문서는 authored text를 복구했으나 초기화 전 document digest가 없어 현재 관측 digest로 구분했다. 원래 private intake51개 전체의 exact 복구도 주장하지 않는다.

새 S0_RECOVERY ZIP은 7,670,634B, SHA `9e16907f94fd7cf098adc03b3e0928fa9bd82196599024358d9897ecdde9d2ae`이며 양쪽 upload ACK를 받았다. 새 archive identity이며 잃은 원 S0와 동일한 ZIP이 아니다. 부모 PHYS83 ZIP과 delivery JSON은 원 bytes가 남아 해시를 유지했다. [복구 기록](recovery/WORKSPACE_RESET_01.json), [코드 복구 영수증](implementation/RECOVERY_RECEIPT.json), [S0 ACK](delivery/S0_RECOVERY_BACKUP_ACK.json) 참조.

## 6. 게시·복원·다음 행동

원격 실제 descendant에서 expected SHA로 S0, S1, 최종 metadata를 게시한다. parent 파일 수정은 0이며 중앙 frozen DAG는 직접 바꾸지 않는다. [DAG_OVERLAY](DAG_OVERLAY.json)와 [중앙 반환 인계](CENTRAL_RETURN_HANDOFF_KO.md)가 원 상태와 새 채택 근거를 연결한다. S0/S1의 stage upload ACK와 최종 전체 다운로드·복원은 서로 다른 검증이다. 미실행 S2는 archive나 완료 영수증을 만들지 않는다.

최종 ZIP은 최종 Git unit, 현재 보존된 private evidence, 원 PHYS83 ZIP/JSON을 포함한다. 양 provider의 실제 전체 GET 뒤 close/reopen size/SHA/원본 bytes, 모든 outer member CRC, payload SHA, fresh Git blob, 실제 추출·재해시와 8 prepared frozen files를 검증한다. 각 provider에서 내려받아 추출한 nested PHYS83 ZIP에서 필수 입력4개+lease1개를 별도로 실제 복원한다. 이는 historical PHYS83 전체385 member 복원·57science freeze를 새로 수행했다는 주장이 아니다. 최종 영수증은 외부 delivery JSON과 PR 본문에 기록한다.

다음 실행자는 실제 refs/AGENTS/병렬 변경/백업과 budget을 다시 읽고 unchanged pinned lease가 실제 허용할 때만 새 `ATTEMPT_02`로 검증을 시작한다. 수치 raw outcome의 fresh independent review가 통과한 뒤에만 원래 예정한 16행 application을 한 번 수행하고, 이후 실제 resume1skip/callback0을 확인한다. [Codex 인계](CODEX_HANDOFF_KO.md), [다음-thread 인계](NEXT_THREAD_HANDOFF_KO.md), [게시 후 권위](POST_PUBLICATION_HANDOFF_KO.md)에 정확한 재개 순서가 있다.

Li instrument response/deconvolution/isotope/target-state 및 실제 source uncertainty, He/Li CX state/photon energy, D PI/RR matched source moments, recombination-to-z20 initial charge, Li inner-shell spectral contract와 full geometry backreaction은 OPEN이다. Nuclear는 기존 scalar thermal/fast ownership을 재사용하지만 physical finite-T event supplier와 correlated rate×energy averaging을 닫기 전 rates/stopping을 활성화하지 않는다. Non-tilted LRS Bianchi I, reacting gas π=0, 별도 collisionless DM π_m, 같은 frame의 signed tensor 합 뒤 norm, Frobenius=√2×half-contraction을 유지한다. 조건부 모형 범위·고정 T/ne 결과·동일 trajectory 성분 분해·sampled residual의 기존 해석 경계를 유지한다.
