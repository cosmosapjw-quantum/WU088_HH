# PHYS79 Codex 인계: source-domain CI/D-CX와 isolated 검증

## 1. 실제 기준과 최종 전달 위치

| 항목 | 값 |
|---|---|
| Repository | https://github.com/cosmosapjw-quantum/WU088_HH |
| Additive Draft PR | https://github.com/cosmosapjw-quantum/WU088_HH/pull/134 |
| Branch | `research/hh-phys79-collisional-closure-20261022` |
| 연구 unit | `research/hh_phys79_collisional_closure_20261022` |
| PHYS79 S2 과학 commit | `338fb7728e8b41f49551200b1f1ba73c047fb90c` |
| 최종 전달 기록 위치 | `PR134 body — Final delivery / PHYS79_FINAL_DELIVERY_20261022.json` |
| 외부 전달 파일 | `PHYS79_FINAL_DELIVERY_20261022.json` |
| PHYS78 최종 부모 | `91d0846a940abf7817c900102dab488ff87e6a82` |
| PHYS78 과학·결과 commit | `b001e69668b2d2c2557b51830f5f732164b56ce0` |
| 과학 기준 PR128 | `92f5ab9dba531ebe05909dcb77d3740d2c68c580` |
| signed-attribution 보충 PR129 | `b76fd4b5d0dfe4850ebde66a8a10f78402d36c00` |

**S2 과학 commit과 최종 전달 HEAD는 역할이 다르다.** 최종 HEAD 및 최종 backup의 실제 provider ID·ZIP SHA·복원 검증 상태는 외부 `PHYS79_FINAL_DELIVERY_20261022.json`과 PR134 body에서 읽어 actual remote ref와 대조한다. commit 안에 그 commit 자신의 HEAD 또는 그 commit으로 만든 ZIP의 hash를 써 넣으면 commit/ZIP 자체가 바뀐다. 이 자기참조를 막기 위해 이 문서는 확정 가능한 과학 commit과 외부 전달 위치만 연결한다. 최종 receipt를 보지 않고 provider metadata ACK를 전체 bytes 복원 PASS로 바꾸지 않는다.

## 2. 재개 시 먼저 읽을 파일

unit 기준으로 `FINAL_REPORT_KO.md`, `CONTRACT.json`, `DAG_OVERLAY.json`, `EXECUTION_LEDGER.json`, `POLICY_OVERRIDE.json`, `theory/RESEARCH_LOOP_AND_CODE_MAP_KO.md`를 읽는다. 그다음 `results/ISOLATED_COMMAND_STDOUT.json`, `results/ISOLATED_RESUME_STDOUT.json`, `results/ISOLATED_SUMMARY.json`, `verification/LIGHT_TEST_RECEIPT.json`, `verification/C9_TARGETED_RECHECK.json`, `verification/RUNNER_INDEPENDENT_REVIEW.json`, `SCIENTIFIC_PAYLOAD_MANIFEST.json`, `delivery/`와 외부 최종 전달 JSON을 대조한다.

과학 입력을 바꾸기 전 `theory/ATOMIC_SOURCES_PHYS79.md`, `theory/THERMAL_CLOSURE_KO.md`, `theory/DH_DETAILED_BALANCE_CLOSURE_KO.md`, `theory/SAVED_TRAJECTORY_FINDINGS_KO.md`를 읽는다. PHYS78의 `FINAL_REPORT_KO.md`, `DAG_OVERLAY.json`, `EXECUTION_LEDGER.json`, `POST_PUBLICATION_HANDOFF_KO.md`, `CODEX_HANDOFF_KO.md`, `delivery/`는 inherited 의무와 과거 실행의 근거다.

역사적 파일명 alias: `verification/C9_TARGETED_RECHECK.json`의 `initial_review_preserved`에 기록된 `C9_REVIEW.json`은 개발 중 초기 검토본의 이름이다. 패키지에서 그 보존본은 **`verification/C9_INITIAL_REVIEW.json`**이다. 새 과학 결과나 누락된 추가 review를 뜻하지 않는다. 이 alias를 설명하되 역사적 receipt를 다시 쓰지 않는다.

사용자가 지정한 embedded `physmath-research-loop` **1.0.0**을 적용했다. cloud 1.3의 기본 단계 선택과 historical PHYS71 우선순위에 대한 현재 사용자 지시의 우선 적용은 `POLICY_OVERRIDE.json`에 남겼다. 원래 과학 조건을 완화한 override가 아니다. Exa·SciSpace 원전 조사, Wolfram 실제 계산 receipt, 독립 C9 review를 재사용한다.

## 3. 완료된 과학 identity — 재실행하지 말 것

실행 source-manifest SHA256은 `3ed45a27ac6688780d385f2e7833813379ceb3df9b5bc3951b9eb587222735ad`다. science ID에는 source/vendor/입력/solver 및 기록된 runtime identity가 결속된다. 출력은 `results/isolated/cases/`에 각 science ID를 파일명으로 둔 `.npz`, `.json`, `.json.sha256`이다.

| Task | science ID | NPZ bytes | NPZ SHA256 |
|---|---|---:|---|
| C01_BASE | `87b585ddcdef54dc97b13f35607d6351f8d3f8320e79942391e5813d36a00761` | 49850 | `52049245ed64711220bc4709536e6204af34b729a89b3d5482bef35035969d4b` |
| C02_BASE | `270d221e2c86815860e8c6fa37aee61effcc635ee5b9bc630b54c010c38a542f` | 18249 | `459ba3c7608df79b2853cb3d8688d4cb453b7c524ebf5a5c907af747f8c833f5` |
| C01_REFINED | `f698f70efed77439c95adbb14859c3f03c067a4eb4824571b04132200aa49d49` | 50026 | `abcb0a0f56989a96b1ee5ae14b6288f4fa0ca930db9c8e0f16c8afbc11c786a1` |

C01 baseline/refinement의 같은 물리 ID는 `a0cdd172c8325b9018e1339c357b4f517bf32cfd31848088c1a24319b12d96fc`다. 최초 실행 run ID는 `03815a51f7d3460cb658d114e0db6599`, 재개 검증 run ID는 `4dc81a560b4044cb9138400affd5aec3`다. 재개 검증은 완료된 세 case의 bytes를 확인하고 **3 skip·새 ODE 0·동일 identity replay 0**으로 끝났다. 같은 질문의 답을 얻기 위한 재실행은 필요 없다.

C01 초기조건은 T=`25370.66308424773 K`, nH=`1e-3 cm^-3`, HII/H=`0.1`, D는 선언한 DB 초기평형, 다른 존재 isotope singly ion fraction=`0.01`이다. C02는 T=`300 K`, nH=`1 cm^-3`, HII/H=`0.5`, **DII/D=`1e-6`**, 나머지 존재 isotope neutral인 D-CX-only control이다. 이 두 초기조건은 `inputs/CONTROL_PLAN.json`의 고립계 계약이며 PHYS78 z20 초기조건과 구별한다.

| 실행 의존성 | SHA256 |
|---|---|
| `source/collisional.py` | `7fca190029597888692d770f9641c6c325c921b0fb67da927f5f06db75f2f2cd` |
| `source/phys78_bridge.py` | `d86fe9a2d2749d41f9e417aaa55dd94084cde40d8e830556e0131d5edc087190` |
| `source/run_controls.py` | `08690a2c39911e9879020073214b08a1044b93bf2fa7c96b94381f8dda6d325b` |
| `inputs/CONTROL_PLAN.json` | `215a90bfe97afa482867215c1f4020fc653608cf69ccab52a91c62ae0766751f` |

전체 vendor hash 목록은 최초 실행 receipt의 `source_manifest.files`가 원본이다. handoff 문서의 metadata 수정은 과학 실행 identity 변경과 구분한다. dependency가 바뀌어 새 science ID가 생겨도, 그 사실만으로 새 ODE가 과학적으로 필요하거나 승인된 것은 아니다.

## 4. 실행·검증 회계

| 구분 | 확정된 수와 상태 |
|---|---|
| 새 isolated ODE | **3 성공 = 독립 물리 control 2 + C01 정련 1**, 실패 0 |
| 새 cosmological ODE / NCP / benchmark | 0 / 0 / 0 |
| 완료 identity ODE replay | 0 |
| 재개 호출 | 1회, 완료 3 skip, 새 ODE 0 |
| saved PHYS78 분석 | P013/P030, 고유 322 epochs; 후처리 2회; 새 ODE 0 |
| light validation | 고유 unittest method **24/24 PASS**, suite 실행 1회 |
| 별도 C9 | 초기 named check 29, targeted check 14, conditioning state 252; F1/F2/N1 닫힘 |
| 현재 새 그림 | 4종 PNG + 4종 PDF; 과거 preview는 history에 별도 보존 |
| inherited PHYS78 | ODE34 = 실패2 + pilot31 + 정련1; 고유 light35 PASS; 이번에 재실행하지 않음 |

24 light method와 C9 check·conditioning state를 합쳐 새 고유 test 수를 만들지 않는다. 후처리 dependency rebuild, 보조 QA 실패, 운영·직렬화 실패는 과학 ODE 실패와 구분하여 원장에 보존했다. HH1231, REI729, HH74control63 및 PHYS78의 완료 identity도 재실행 금지다.

최대 isotope 상대 오차는 `4.397502728453756e-15`, 최대 saved `u+ε·Y` 상대 오차는 `2.6645352591003757e-15`, C01 정련 scaled-state 차이는 `4.574293383682441e-15`다. C02의 독립 extent-temperature 최대 차이는 `3.410605131648481e-13 K`이고, 최종 평형 거리/D inventory는 `3.635426294598055e-9`다. 고정 gate는 각각 nucleus `1e-10`, energy `2e-10`, refinement `1e-6`, C02 temperature `1e-9 K`, equilibrium distance `1e-6`이다. sampled 결과를 continuum certificate로 해석하지 않는다.

## 5. 유지해야 할 과학 조건

non-tilted LRS Bianchi I, `(-,+,+,+)`, 같은 normal orthonormal frame이다. reacting gas의 `pi=0`을 유지하고 비영 `pi_m`은 collisionless DM에 속한다. matter/radiation의 signed tensor를 먼저 합한 뒤 norm을 취하며 `Frobenius=sqrt(2)×half-contraction`을 보존한다. `c`, `k_B`, `hbar` convention을 유지한다. 같은 궤적의 성분 분석은 species-off 인과 실험이 아니다.

PHYS78의 H1/D/T I–II, He3/He4 I–III, Li6/Li7 I–IV, neutron 총 21 ionic/nuclear 슬롯과 charge-derived electron을 유지한다. CI 원소 row는 6개, isotope 전이는 13개다. 그러나 실제 C01은 H/He/Li **중성 CI 7개**와 D CX 두 방향만 선택했다. T/n 초기 재고는 0이다. 기존 finite PI+RR의 18/30/60 eV source 아래 LiIII/IV가 0이었다는 관찰을 모든 CI·hard-UV·nuclear source의 금지로 확대하지 않는다.

Voronov CI source의 하한은 H I/He I/Li I가 **1 eV ≈11604.52 K**, He II/Li II/Li III가 **3/4/5 eV**다. 최고값 열은 **20 keV**이며 최저값 열의 eV와 혼동하지 않는다. PHYS78 Tmax 약 25370.7 K에서는 중성 row만 허용된다. 약255–11605 K 초기/저온 구간은 현재 fit로 닫히지 않는다. 원자료 범위 밖은 kernel 거부, 저장 분석에서는 NaN+false mask다. 0, 작은 외삽값, reactant 부재로 rate admission을 위장하지 않는다.

D CX는 Savin reverse fit과 `k_f=k_r exp(-43 K/T)`를 사용한 **새로 선언한** 상세평형 모델이다. analytic fit domain은 2.7–200000 K다. 같은 isotope의 neutral/ion 병진 질량을 `A m_p`로 같게 두고 ground-state degeneracy ratio 1, hyperfine 생략, `ΔI=43 k_B K`를 명시한다. Savin의 raw forward fit도 진단으로 남아 있으며, raw fit의 보고 정확도를 새 forward에 자동 승계하지 않는다.

양의 누적 ionic potential `ε`를 사용하여 `b=ε·Y`, `u=(3/2)k_BTN`으로 두고 비복사 event에서 `q_th=-ΣΔεR`를 쓴다. `u̇=-2Hu+q_th`, `Ṫ=-2HT+2q_th/(3k_BN)-T ẋ_e/N`이다. C01/C02는 일정 밀도, `H=0`, PI/RR·열 bath 없음의 isolated 계다. CI에서 전자수 증가를 `u` 식에 다시 추가하지 않는다.

F2 수정은 작은 D isotope defect를 큰 H/D potential의 차로 계산하는 conditioning 문제를 해소했다. authoritative binding derivative는 `math.fsum(Δε_rR_r)`이고 직접 `ε·Ydot`는 constituent-energy scale와 함께 진단으로 남는다. 구성상 `heat+binding_dot=0`을 독립 conservation test로 세지 않는다. 별도로 적분한 `u`, saved `ε·Y`, D-only scalar root와 `T(ξ)` 검증을 사용한다.

## 6. 다음 DAG — 물리 단계부터

전체 `COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE`는 `PARTIAL_WITH_EXECUTABLE_SUBSET`이다. 다음 우선 노드는 **LOW_T_CI_SOURCE_COVERAGE**다. 약255–11605 K 및 필요한 higher-stage 구간의 cross section/rate를 원전에서 확보하고, Maxwellian 적분 또는 source를 갖춘 연결 fit, 단위·정확도·중복 channel을 검증한다. 그다음 영향을 받는 R/C 단계부터 구현한다.

**HE_LI_CX_STATE_AND_PHOTON_ENERGY**는 He 비복사 최종상태, 수정된 Li nonradiative 계수·정의역, radiative photon moment를 해결해야 한다. total CX rate만으로 heat를 정하지 않는다. radiative event에서는 `q_th=-ḃ-Qγ`와 photon 쪽 `+Qγ`를 함께 쓴다. **D_PI_RR_ENERGY_ADAPTER**는 D의 PI threshold, RR emission, CI/CX에 단일 shifted potential을 연결하는 의무다. 현재 D heat를 기존 isotope-blind PI/RR 원장에 붙여 full closure를 선언하지 않는다.

**RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT**를 유지한다. PHYS78의 HII/H=`2e-4`, 다른 존재 isotope neutral은 탐색 초기조건이다. C01/C02의 인위적 control 전하 초기조건으로 이를 대체하지 않는다. Li hard-UV는 inner-shell/Auger·branching·spectral energy를 먼저 닫는다. collisional excitation, free-free, Compton, 전체 nuclear/molecular/spectral transport 의무도 OPEN이다. 현재 부분계의 성공은 전체 cosmological admission이 아니다. strong no-go는 주장하지 않는다.

## 7. 실제 CLI와 재개 동작

다음은 repository root에서 사용할 인터페이스 설명이다. **이미 완료된 control을 다시 실행하라는 지시가 아니다.** 현존 결과와 receipt를 먼저 읽는다.

```bash
cd research/hh_phys79_collisional_closure_20261022
python source/run_controls.py --help
python source/run_controls.py --preflight
```

인자를 생략해도 preflight이며 ODE를 시작하지 않는다. 실제 실행 flag는 `--execute`다. `--resume` flag는 없다.

```bash
python source/run_controls.py --execute --output results/isolated
```

같은 출력 경로·identity의 `--execute`는 COMPLETE receipt checksum, NPZ size/hash와 finite 배열을 검증하고 skip한다. 실패·부분 완료 identity는 자동 재시도하지 않는다. 완료 파일을 지우거나 출력 경로를 바꾸어 동일 물리 실행을 다시 만들지 않는다. 미래에 실제로 필요한 새 identity는 source/IC/수치 변경 이유, 판별 질문, 고정 gate와 실행 예산을 먼저 기록한다.

실행은 worker 1, thread 1이며 byte-pinned PHYS78 `LeasePool`의 공유 lease를 요구한다. 기본 lease directory는 `/tmp/rei-bianchi-cooperative-leases`다. lease가 없으면 WAITING으로 기록하고 launch하지 않는다. 매 `solve_ivp` 호출 전 durable marker를 남기고 실패도 호출 수에 포함한다. 다른 process를 종료하거나 다른 소유자의 lease를 회수하지 않는다.

## 8. 접근 범위와 과거 백업

이번 intake는 repository catalog51개, WU branch142개, 관련 최근 PR metadata74개, sibling actual ref7개 및 선택된 report/receipt를 확인했다. 모든 branch 파일·cloud backup·접근 불가 비공개 대화를 전수 확인한 것은 아니다. 새 thread는 변경된 actual refs와 접근 가능한 새 결과만 추가 대조하며, 다른 branch의 prescribed-temperature 또는 passive nuclear 결과를 자기일관 thermal closure로 자동 전용하지 않는다.

PHYS78 과거 ZIP은 `PHYS78_FINAL_20261021_91d0846a940a.zip`, SHA256 `3eca5c5f6667af5cb0acf8ac26ad7dd65e77288bb07b05df8336a027547411c4`다. Drive ZIP ID `1so8SEKteQjhW3idfuabomxJJKaQ19qNt`, 최종 전달 JSON ID `16exbIKDlkOXV4sUPCJz3GFfyMzMJnMxs`; Dropbox ZIP ID `id:BSpOijBcT10AAAAAAD_hqA`, JSON ID `id:BSpOijBcT10AAAAAAD_hqQ`다. 2026-10-21의 양쪽 전체 bytes/CRC/375 payload SHA PASS는 과거 receipt를 재사용한 것이다. PHYS79 intake의 metadata·JSON 대조를 그 ZIP의 새 전체 복원으로 표현하지 않는다.

유도, 코드, light 검증, saved 분석, 새 과학 실행, 게시, 백업, DAG 상태를 따로 보고한다. 최종 전달 receipt와 실제 remote ref 확인 뒤 additive draft descendant에서 다음 승인된 물리 작업을 이어 간다. **HH_R10=OFF. Production admission NOT_ISSUED.**
