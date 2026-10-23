# PHYS83 continuation — Codex 인수인계

## 1. 시작할 identity와 최종 권한 기록

저장소는 https://github.com/cosmosapjw-quantum/WU088_HH, 현재 Draft는 [PR140](https://github.com/cosmosapjw-quantum/WU088_HH/pull/140), branch는 `research/hh-phys83-ce-completion-20261023`다. 선택한 유한 H I CE 연구와 detached nuclear ownership 구현은 완료했다. 전체 원자·핵·우주론 모형의 완료 또는 production 승인은 아니다.

| 항목 | 고정 identity |
|---|---|
| PHYS82 최종 HEAD | `ca9d53983459ea08f9992a8a24663e46b7180344` |
| 실제 직접 부모 PHYS83 S0 / PR139 | `09289300ec2e500806aa2cb82365f00329e41c8c` |
| 현재 continuation S0 | `65c6751d363363cfc15eba0c7debf50eb493c1c9` |
| 검증된 코드 checkpoint S1 | `cedf70d886e61fabe4e4f10f5d9cddc1b15ba3dd` |
| 과학 결과 checkpoint S2 | `1f5b11524abc351027d0f88cea009f0015dd088f` |
| 완료 과학 identity | `e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c` |
| 동결 과학 집합 | `delivery/SCIENTIFIC_FREEZE.json`, 57 files |

**S2는 최종 전달 HEAD를 대신하지 않는다.** 이 문서를 포함할 final commit의 자기 SHA와 최종 ZIP의 자기 hash·provider IDs는 문서 작성 시점에 정해지지 않았다. 게시 후에는 외부 **`PHYS83_CONT_FINAL_DELIVERY_20261023.json`과 PR140 최종 본문**에서 실제 final HEAD, ZIP size/SHA256, Drive/Dropbox IDs, 전체 복원 및 외부 JSON readback 결과를 읽는다. 최종 authority가 아직 없으면 알려진 S2를 과학 완료 checkpoint로만 사용하고 전달 단계는 미확정으로 남긴다. 해당 값을 추정하지 않는다.

## 2. 필수 읽기와 단계 구별

Unit은 `research/hh_phys83_ce_completion_20261023/`다. 먼저 다음을 읽는다.

- `FINAL_REPORT_KO.md`, `CONTRACT.json`, `DAG_OVERLAY.json`, `EXECUTION_LEDGER.json`, `RESEARCH_LOOP_MAP_KO.md`.
- `source_data/HI_CE_SOURCE_CONTRACT.json`, `theory/MATCHED_CE_IMPLEMENTATION_MAP_KO.md`, `theory/PARENT_MATCHED_KERNEL_CORE_KO.md`.
- `theory/NUCLEAR_THERMAL_FAST_OWNERSHIP_KO.md`, `theory/NUCLEAR_OWNERSHIP_CONTRACT.json`, `theory/NUCLEAR_CODING_ADOPTION_MAP_KO.md`.
- `verification/INDEPENDENT_REVIEW_KO.md`, `verification/INDEPENDENT_VERIFICATION_AGGREGATE.json`, `verification/SAVED_RESULTS_REVIEW.json`, `verification/PLOT_VISUAL_REVIEW.json`.
- `results/SCIENCE_IDENTITY.json`, `results/COMPLETE.json`, `results/SCIENCE_SUMMARY.json`, `delivery/SCIENTIFIC_FREEZE.json`.
- `inventory/PRE_SCIENCE_CURRENT_DELTA_REFRESH.json`, 그 Markdown 설명, `POST_PUBLICATION_HANDOFF_KO.md`, `delivery/`와 외부 최종 authority.

`CONTRACT.json`의 초기 status, S1 독립 검토 문서의 “science grid 미실행”, 단계별 receipt의 pending은 각 작성 시점의 기록이다. 완료 과학은 실제 S2 결과·장부가, 이후 게시·백업은 외부 최종 authority가 설명한다. 초기 snapshot을 덮어써 과거에 완료됐던 것처럼 바꾸지 않는다.

## 3. 이미 완료된 일

새 과학 실행은 **1시도 = 1완료 + 0실패**다. 66개 온도에서 두 channel의 paired up/down rate **132회**, 저장 rate를 재사용한 steady **324행**, 여섯 transient profile **732행**이다. Full coupled/cosmological ODE, benchmark, empirical nuclear rate 및 fast-product stopping 실행은 각각 0이다. 부모 902 reciprocity checks와 Wolfram 7 residual은 재사용했고, 새 핵 소유권 유도는 Wolfram 10 residual=0으로 검산했다.

독립 검증은 **71 named cases / 2,111 assertions PASS_SCOPED**다. CE/population 1,885, nuclear scalar ownership 171, mock runner 55로 구분한다. 최초 CE 시도의 mpmath import 실패는 수치·과학 호출 전 환경 실패 1건이며 과학 실패가 아니다. Mock의 의도한 실패 callback도 과학 실패에 합하지 않는다. 완료된 검증 matrix를 다시 실행하지 않는다.

실제 completed resume는 **1회 skip, scientific callback 0**이며 `verification/science_resume_01.json`과 대응 lease receipt에 보존됐다. 그림은 저장 CSV만 읽어 **3 PNG + 3 PDF**를 생성했고 root의 PNG 육안 검토는 PASS_SCOPED다. 저장 과학의 최대 normalized raw energy residual은 `2.433784209198325e-16`, nuclei residual은 `1.1102230246251565e-16`이다. 이는 sampled 진단이며 continuum certificate가 아니다. 근거는 `EXECUTION_LEDGER.json`과 `results/SCIENCE_SUMMARY.json`이다.

## 4. 유지할 물리 계약

현재 문제는 stationary-heavy-target, unpolarized H I LS 1s/2s/2p의 유한 CCC subset이다. T=255–50000 K, source-native Δ=10.20435 eV, g=(2,2,6), excess support=[0,958.40145] eV다.

`W(ε)=(ε+Δ)σ_up(ε+Δ)`를 piecewise linear로 두고 같은 W와 같은 support로 deexcitation을 정의한다. Reverse source는 provenance/printed-precision 검산 자료이며 별도 interpolation provider가 아니다. 저장 rate는 full physical rate, tail enclosure 또는 source confidence interval이 아니다.

고정 T/ne, ground-start, local proper time, optically thin immediate escape를 유지한다. Signed `thermal_change_eV`와 positive `heat_withdrawal_eV`는 서로 음수 관계다. Collisional event의 열 인출은 준위 gap이며 reaction-selected incoming energy 전체를 추가 cooling으로 빼지 않는다. 2s two-photon 사건은 총 에너지 Δ와 광자 두 개를 가지며, Δ/2 monochromatic spectrum을 가정하지 않는다. 별도 작은 M1 branch도 보존한다. Detached own-spontaneous와 native radiative owner를 동시에 켜지 않는다.

고밀도 행은 제한된 star의 formal quenching 진단이다. 이를 mixing·higher levels·opacity가 닫힌 실제 고밀도 H I 해 또는 coupled thermal/charge history의 경계로 쓰지 않는다.

Nuclear module은 공급된 같은 normal-frame scalar event energies와 positive weights의 소유권·평균·thermal particle-number EOS를 검증했다. 실제 on-shell event 생성, frame transformation, finite-T measure, isotope stoichiometry를 공급한 것이 아니다. Physical nuclear rates와 stopping 활성화는 그 source contract 이후다.

## 5. 완료 결과와 기존 resume 영수증의 읽기 검증

기본 행동은 기존 완료 bytes와 **이미 실행된 resume 1 SKIP / scientific callbacks 0** 영수증을 읽어 재사용하는 것이다. 추가 resume invocation이나 새 receipt를 만들 필요가 없다. Runtime 버전 차이는 replay 사유가 아니다. `results/`, claim, COMPLETE, 기존 verification/figure outputs를 지우거나 새 결과로 덮지 않는다. 과학 입력·코드를 바꾼 후 기존 완료 identity를 재사용하지 않는다.

필요하면 아래 명령을 **unit 디렉터리에서** 사용해 복원된 파일과 기존 영수증만 읽는다. Runner·과학 모듈을 import하거나 실행하지 않으며 새 invocation/receipt를 만들지 않는다. 먼저 외부 final authority와 archive/member bytes의 identity를 확인한다. 이 예시는 문서 작성 중 실행하지 않았다.

```bash
python3 - <<'PYREAD'
import hashlib
import json
from pathlib import Path

expected = "e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c"
freeze = json.loads(Path("delivery/SCIENTIFIC_FREEZE.json").read_text())
assert freeze["scientific_identity"] == expected
assert freeze["file_count"] == len(freeze["files"]) == 57
for name, meta in freeze["files"].items():
    raw = Path(name).read_bytes()
    assert len(raw) == meta["bytes"], name
    assert hashlib.sha256(raw).hexdigest() == meta["SHA256"], name
complete_bytes = Path("results/COMPLETE.json").read_bytes()
complete = json.loads(complete_bytes)
claim = json.loads(Path("delivery/scientific_claims", expected + ".json").read_text())
assert complete["status"] == claim["status"] == "COMPLETED"
assert complete["scientific_identity"] == claim["scientific_identity"] == expected
assert hashlib.sha256(complete_bytes).hexdigest() == claim["completion_SHA256"]
assert len(complete["files"]) == 7
for name, meta in complete["files"].items():
    raw = Path("results", name).read_bytes()
    assert len(raw) == meta["bytes"], name
    assert hashlib.sha256(raw).hexdigest() == meta["SHA256"], name
resume = json.loads(Path("verification/science_resume_01.json").read_text())
lease = json.loads(Path("verification/lease_science_resume_01.json").read_text())
assert resume["status"] == "SKIP_COMPLETED_IDENTITY"
assert resume["scientific_identity"] == expected
assert resume["science_callbacks"] == 0 and resume["verified_payload_files"] == 7
assert lease["status"] == "COMMAND_COMPLETED" and lease["exit_code"] == 0
assert lease["workers"] == lease["threads"] == 1
assert lease["other_processes_terminated"] == 0
assert lease["old_science_runner_called"] is False
stored_stdout = json.loads(lease["stdout"])
assert stored_stdout["status"] == resume["status"]
assert stored_stdout["scientific_identity"] == expected
assert stored_stdout["science_callbacks"] == 0
print("Stored completion and prior resume receipts agree; new invocations=0.")
PYREAD
```

무결성 검사 실패는 복원·identity 불일치로 조사한다. 실패를 지우거나 completed claim을 제거해서 계산을 다시 시작하지 않는다. 완료 검증 suite나 과학을 다시 호출하여 복원 문제를 덮지 않는다. **새 물리 문제·source·구현 identity가 필요한 경우에만** 별도 연구 계약, 유도, 제한된 구현·독립 검토와 admission 뒤 새 수치 단위를 실행한다. 가용 CPU/RAM과 공유 lease를 읽고 1 worker/1 thread를 유지하며 다른 process를 종료하지 않는다.

## 6. 다음 물리→코딩 단위

다음 원자 leaf는 **HI_2S_2P_MIXING_AND_SPECTROSCOPIC_ENERGY_MATCH**다. 원전에서 projectile/target state, finite splitting, fine-structure·isotope convention, cross section/rate의 units·range·degeneracies, detailed balance, branching 및 photon/recoil energy를 먼저 닫는다. 현재 degenerate LS CCC의 2s↔2p 발산을 임의 cutoff로 실제 mixing source처럼 사용하지 않는다. 분광 에너지를 채택하면 collision threshold, atomic storage, radiation energy가 하나의 계약으로 함께 바뀌어야 한다. 현재 Δ-native 완료 자료를 수정하지 않고 별도 descendant unit에 새 identity를 부여한다.

병렬 핵 leaf는 **NUCLEAR_FINITE_T_EVENT_PROVIDER_AND_STOICHIOMETRY**다. 같은 normal orthonormal frame의 on-shell event, finite-T 반응·각도 measure, isotope별 thermal/fast 입자 수, 전자·광자·recoil 소유권을 source와 연결한다. 같은 event measure로 rate와 energy moments를 평균하고, 근거 없이 평균 rate×평균 energy로 분리하지 않는다. Thermal EOS의 입자 수 항을 보존한다. 이 계약이 닫힌 뒤 필요한 최소 새 검증을 설계하고, empirical rates/stopping은 별도 admission한다.

연구 시작 전 actual refs와 접근 가능한 최신 결과를 identity로 다시 대조한다. 2026-10-23 15:00–15:02 UTC refresh는 여섯 repo×최근 5 PR와 12 actual refs의 제한된 관측이었다. REI ANGTHERM02 review-pending 결과, REI moment-cone, REC LINE02, BASS G1B는 각 범위로 구별했다. 오래된 51/2175 inventory를 재사용하되 접근 불가능한 비공개 대화를 전수 확인했다고 주장하지 않는다.

## 7. 유지할 OPEN과 보호 조건

다음 의무를 유지한다.

- `BOUND_BOUND_CE_AND_RADIATIVE_COOLING_FULL_SOURCE`: finite-mass/isotope spectroscopy, 실제 interpolation/tail uncertainty, finite-splitting mixing, higher levels/cascades, CI/RR, photoabsorption/stimulated emission, opacity/trapping, two-photon spectrum, He/Li CE.
- `HE_LI_CX_STATE_AND_PHOTON_ENERGY`.
- Li instrument response/deconvolution/isotope/target-state 및 실제 physical uncertainty.
- `RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT`, `D_PI_RR_MATCHED_SOURCE_MOMENTS`, `LI_HARD_UV_INNER_SHELL_SPECTRAL_CONTRACT`.
- Nuclear finite-T provider/isotope stoichiometry, empirical nuclear rates 및 fast-product stopping.
- `FULL_GEOMETRY_SPECTRAL_BACKREACTION`와 coupled thermal/charge/spectral transport.

PHYS78/79/80/81/82 및 이번 PHYS83, HH1231/REI729/HH74control63, C22D/E, HE34/35/36/37, ANGULAR01, C23A, 완료된 REI·REC identity를 재실행하지 않는다. Non-tilted LRS Bianchi I, reacting gas pi=0, 별도 collisionless DM pi_m을 유지한다. 같은 normal frame의 signed matter/radiation tensor를 먼저 합한 뒤 norm을 취하며 Frobenius=sqrt(2)×half-contraction이다. 같은 trajectory의 성분 분석은 species-off 인과 실험이 아니다.

새 단원도 실제 remote descendant의 additive Draft PR로 게시한다. 유도·코드·검증·과학 실행·게시·단계별 ACK·최종 전체 복원·DAG를 따로 기록한다. **HH_R10=OFF. Production admission NOT_ISSUED.**

## 8. Codex에 붙여 넣을 짧은 지시

```text
WU088_HH PHYS83 continuation 이후 연구를 이어가라. 먼저 PR140 최종 본문과 외부
PHYS83_CONT_FINAL_DELIVERY_20261023.json에서 actual final HEAD/ZIP/복원 identity를
확인하고 그 최종 descendant를 사용하라. UNIT의 CODEX_HANDOFF_KO.md와 필독 자료를
읽어 완료 science e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c,
S2 1f5b11524abc351027d0f88cea009f0015dd088f, frozen57을 재사용하라.
완료 검증·science를 재실행하지 말고 runtime 차이로 replay하지 마라.
$physmath-research-loop와 Exa/SciSpace/Wolfram으로 다음 원자 source contract
HI_2S_2P_MIXING_AND_SPECTROSCOPIC_ENERGY_MATCH를 물리 단계에서 먼저 닫아라.
NUCLEAR_FINITE_T_EVENT_PROVIDER_AND_STOICHIOMETRY는 병렬 OPEN으로 조사하되
physical nuclear rates/stopping은 아직 활성화하지 마라.
actual refs와 최신 접근 가능한 결과를 제한된 범위로 대조하고, 최소 새 unit만
1 worker/thread와 공유 lease 안에서 구현·독립 검증하라. 기존 파일을 보존하고
additive Draft PR, 단계별 백업 및 최종 양쪽 전체 복원·handoff를 따로 마감하라.
HH_R10=OFF, Production admission NOT_ISSUED 및 모든 OPEN 의무를 유지하라.
```

