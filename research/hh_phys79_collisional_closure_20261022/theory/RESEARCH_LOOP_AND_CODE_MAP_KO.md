# PHYS79 연구 루프와 식–코드–근거 대응

## 1. 이번 단위의 판정과 계약

**source domain을 강제하는 CI 연산자, 명시적 D/H ground-state detailed-balance 모델, 보존적인 열·ionic-potential 회계, 두 isolated parcel과 한 정련을 구현하고 검증했다. 전체 cosmological collisional closure는 OPEN이다.** 실제 실행은 새 isolated ODE 3회 성공이며, 완료 identity 재실행은 0회다. 재개 호출은 저장 bytes를 검증한 뒤 3개를 skip하여 새 ODE를 만들지 않았다. 실행 근거는 [최초 receipt](../results/ISOLATED_COMMAND_STDOUT.json), [재개 receipt](../results/ISOLATED_RESUME_STDOUT.json)에 있다.

적용 절차는 사용자가 지정한 embedded `physmath-research-loop` 1.0.0의 R1–R10·C1–C10이다. cloud 1.3의 기본 단계 선택보다 현재 사용자 지시를 우선한 이유와 historical PHYS71 우선순위 교정은 [POLICY_OVERRIDE.json](../POLICY_OVERRIDE.json)에 보존한다. 이는 실행 순서·runtime routing의 교정이며 과학적 가정의 해제가 아니다. 본 문서는 기존 실제 근거를 연결하며 추가 ODE·시험을 실행하지 않는다.

[CONTRACT.json](../CONTRACT.json)의 `(-,+,+,+)`, non-tilted LRS Bianchi I, 같은 normal orthonormal frame, reacting gas의 `pi=0`, collisionless DM이 소유하는 비영 `pi_m`, signed tensor를 합한 뒤 norm, `Frobenius = sqrt(2) × half-contraction`을 유지한다. isolated parcel은 이 배경 계약 안에서 팽창·PI·RR·외부 열원 없이 새 충돌 연산자만 검사하는 제한된 문제다. 이는 z20→2 수정 궤적이 아니다. `HH_R10=OFF`, production admission `NOT_ISSUED`이며, 아래 절차 이름 **R10은 HH_R10 활성화를 뜻하지 않는다.**

## 2. 실제 이론 루프 R1–R10

| 단계 | 수행 내용과 확보 범위 | 근거 |
|---|---|---|
| R1 연구 위치·계약 | PHYS78의 `COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE`를 선택하고 원래 전체 의무와 이번 실행 가능한 부분을 구분했다. | [CONTRACT](../CONTRACT.json), [DAG](../DAG_OVERLAY.json) |
| R2 근거·재사용 | actual refs, 접근 가능한 sibling 결과·backup·handoff를 identity로 대조했다. PHYS78 34 ODE 및 기존 test 근거는 재사용했다. 접근할 수 없는 비공개 대화의 전수 확인은 주장하지 않는다. CI/CX 원전과 source domain을 추출했다. | [identity inventory](../inventory/IDENTITY_INVENTORY_KO.md), [source 조사](ATOMIC_SOURCES_PHYS79.md), [추출 근거](SOURCE_EVIDENCE_EXTRACTED.json) |
| R3 주장·전제 정렬 | source의 raw fit과 새 DB43K 모델을 분리했다. 전자 질량을 무시한 neutral/ion translational mass, ground-state degeneracy ratio 1, hyperfine 제외, 반올림한 `ΔI=43 k_B K` 아래의 DB를 주장한다. CI source domain, radiative-CX photon moment의 미해결 상태를 명시했다. | [D/H 모델](DH_DETAILED_BALANCE_CLOSURE_KO.md), [열 회계](THERMAL_CLOSURE_KO.md) |
| R4 가설·표현 탐색 | isotope별 ionic abundance, charge-derived electron, 양의 누적 ionic potential을 사용했다. raw 두 방향 fit을 독립 채택하는 경우와 reverse fit에 DB를 부과하는 경우를 수치적으로 구별했다. 후자를 isolated control의 명시적 closure로 선택했다. | [D/H 진단](../verification/DH_DETAILED_BALANCE_DIAGNOSTICS.json), [입력 계획](../inputs/CONTROL_PLAN.json) |
| R5 구성적 유도 | CI/CX stoichiometry, nucleus·charge 보존, event energy, 입자 수에 따른 `Tdot`, 팽창을 포함한 per-H/volume energy 식을 유도했다. radiative CX는 `Qγ`를 분리했다. D-only의 scalar extent–energy–equilibrium 연결도 구성했다. | [열 유도](THERMAL_CLOSURE_KO.md), [D/H 유도](DH_DETAILED_BALANCE_CLOSURE_KO.md) |
| R6 독립 검증 | 실제 Wolfram 대수 검산과 exact rational stoichiometry 검산을 수행했다. 13 CI 및 140 CX의 구조적 보존 검사는 rate admission 수와 구별한다. C9의 수치 conditioning 지적은 아래와 같이 교정했다. | [Wolfram](../verification/WOLFRAM_RECEIPT.json), [D/H Wolfram](../verification/DH_DB_WOLFRAM_RECEIPT.json), [exact 검사](../verification/STOICHIOMETRY_EXACT_CHECK.json) |
| R7 판별 검증 | 원래 P013/P030의 322 저장점에 순간 연산자를 평가했다. 중성 CI가 허용된 고온 구간에서 H CI와 cooling이 무시 가능한 항이라는 일괄 가정은 지지되지 않았다. 별도 isolated 2개+정련 1개의 실행으로 구현된 부분의 동역학·보존·평형 접근을 검사했다. | [저장 궤적 진단](SAVED_TRAJECTORY_FINDINGS_KO.md), [실행 receipt](../results/ISOLATED_COMMAND_STDOUT.json) |
| R8 결과 판정 | domain 안의 유한 연산자와 조건부 열역학 모델은 확보했다. low-T CI, He/Li CX의 상태·광자 에너지, D PI/RR adapter, z20 초기 charge는 미완료다. source domain 공백이나 미실행을 불가능성 정리로 바꾸지 않았다. strong no-go는 주장하지 않는다. | [DAG](../DAG_OVERLAY.json), [source 판정](ATOMIC_SOURCES_PHYS79.md) |
| R9 정식 결과·코딩 연결 | 유도식의 단위·상태·정의역·오류 처리를 `collisional.py`와 runner 계약으로 옮겼다. 아래 대응표가 source→함수→실행 상태→검증 경로를 연결한다. | 본 문서, [구현](../source/collisional.py), [control 계획](../inputs/CONTROL_PLAN.json) |
| R10 종료·재개 | 과학 실행 결과와 남은 의무는 보존했다. 최종 게시 commit·양쪽 backup·Codex/다음-thread 인계의 동일 identity 대조는 최종 delivery receipt를 기다린다. 이 행을 전체 물리 요청의 완료 판정으로 사용하지 않는다. | [execution ledger](../EXECUTION_LEDGER.json), [delivery](../delivery/), 최종 handoff에서 갱신 |

## 3. 실제 코딩 루프 C1–C10

| 단계 | 수행 내용과 확보 범위 | 근거 |
|---|---|---|
| C1 목표·baseline | parent `91d0846a940abf7817c900102dab488ff87e6a82`, 과학 기준 PR128 및 PR129 supplement를 고정했다. PHYS78 isotope inventory·charge slots·atomic tables는 byte pin으로 재사용했다. | [CONTRACT](../CONTRACT.json), [vendor provenance](../vendor/PHYS78_PROVENANCE.json) |
| C2 식–데이터–코드 | elemental CI 6개 row를 isotope transition 13개에 대응시키고, D CX의 두 방향 및 공통 ionic potential을 함수에 연결했다. charge-derived electron과 per-H 정규화를 호출 경로에 유지했다. | [collisional.py](../source/collisional.py), [bridge](../source/phys78_bridge.py) |
| C3 수치 설계 | 21 abundance와 열에너지 `u`를 별도 적분한다. isotope inventory별 고정 diagonal scaling, DOP853, 고정 161 표본, strict nonnegative RHS, domain 오류 중단, projection 없음으로 설계했다. 보존·정련·D equilibrium 및 작은 isotope heat gate는 실행 전에 고정했다. | [CONTROL_PLAN](../inputs/CONTROL_PLAN.json), [runner 검토](../verification/RUNNER_INDEPENDENT_REVIEW.json) |
| C4 실행 DAG·자원 | 두 물리 control과 한 distinct refinement를 순차 실행했다. byte-pinned PHYS78 LeasePool의 1 CPU lease를 요구하며, lease가 없으면 launch 없이 WAITING이다. 다른 process를 종료하지 않는다. | [runner](../source/run_controls.py), [request·receipt](../results/ISOLATED_COMMAND_STDOUT.json) |
| C5 구현 | rate guard, event stoichiometry, finite-state 검증, energy/temperature helper, 명시적 subnetwork, full cosmological admission 거부, create-only 실행 identity·receipt·checksum을 구현했다. | [collisional.py](../source/collisional.py), [run_controls.py](../source/run_controls.py) |
| C6 구현 검증 | 고유 unittest method 24개가 PASS했다. source domain 경계, 72-digit 원전식 reference, units·density scaling, nucleus·charge, no clipping, array ownership, finite-state, full-closure refusal을 검사했다. | [LIGHT_TEST_RECEIPT](../verification/LIGHT_TEST_RECEIPT.json) |
| C7 과학 검증 | isolated 3개에서 nucleus, independently integrated `u`와 saved `ε·Y`의 합, 비음 상태, admitted domain을 확인했다. C02는 독립 scalar equilibrium과 extent-temperature 관계도 확인했다. 저장 trajectory 진단은 species-off 인과 실험으로 해석하지 않는다. | [실행 receipt](../results/ISOLATED_COMMAND_STDOUT.json), [저장 궤적 해석](SAVED_TRAJECTORY_FINDINGS_KO.md) |
| C8 수치·재현성 | C01은 동일 물리의 더 작은 tolerance·step으로 한 번 정련했다. source·vendor·IC·solver·Python/NumPy/SciPy identity, 매 solve 호출 전 marker, NPZ bytes/SHA256을 기록했다. 재개 호출은 3개 완료 identity를 검증 후 skip했다. | [최초 receipt](../results/ISOLATED_COMMAND_STDOUT.json), [재개 receipt](../results/ISOLATED_RESUME_STDOUT.json) |
| C9 독립 검토 | kernel 작성자와 별도 검토자가 29개 초기 check 및 252 conditioning state로 실제 결함 F1/F2와 label N1을 발견했다. 수정 후 14개 targeted check로 닫았다. runner는 다른 작성자가 만들고 root가 독립 검토하여 C02 heat gate를 실행 전에 보강했다. | [초기 C9](../verification/C9_INITIAL_REVIEW.json), [targeted C9](../verification/C9_TARGETED_RECHECK.json), [runner 검토](../verification/RUNNER_INDEPENDENT_REVIEW.json) |
| C10 판정·인계 | 구현·light validation·isolated science execution은 위 범위에서 완료했다. 최종 additive draft commit, 전체 payload backup, handoff receipt 정합성은 delivery 단계에서 닫는다. 게시·백업 완료를 과학적 full closure와 동일시하지 않는다. | [ledger](../EXECUTION_LEDGER.json), [DAG](../DAG_OVERLAY.json), [delivery](../delivery/) |

24 light method, 29 초기 C9 check, 14 targeted check, 252 conditioning state는 서로 다른 검증 단위다. 이를 합쳐 고유 light test 수를 부풀리지 않는다. PHYS78의 35 light test와 34 ODE는 이번에 실행한 수가 아니다.

## 4. source → 식 → 함수 → 실행 상태

`Y_i=n_i/n_H`, `x_e=Σ_i q_iY_i`, `N=Σ_iY_i+x_e`, `u=(3/2)k_BT N`, `b=Σ_i ε_iY_i`로 둔다. `ε_i`는 neutral을 0으로 둔 **양의 누적 이온화 potential**이다. 코드 단위는 K, cm⁻³, eV, proper s, per reference H1이며 `k_B`는 eV/K로 변환되어 명시된다.

| 물리 입력·식 | 코드 연결 | 상태·검증 연결 |
|---|---|---|
| Voronov source `k_CI(T)`와 electron-temperature domain. H I/He I/Li I 하한 1 eV, He II/Li II/Li III 하한 3/4/5 eV. | `ci_domain_mask`, `ci_rate`, `CollisionNetwork.rate_coefficients` | 허용 범위 밖은 kernel에서 `RateDomainError`; 저장점 분석에서는 NaN+false mask. electron나 reactant가 0이어도 요청한 rate의 domain 검사를 생략하지 않는다. |
| CI: `A^q+e → A^(q+1)+2e`, `R=n_H k Y_A x_e`, `Δb=I`, `Δx_e=1`. | `CollisionNetwork.__init__`의 event·stoichiometry, `rhs`의 flux | 13 isotope transition 구조. C01은 중성 row `(0,1,3)`만 명시적으로 활성화한다. 추가 `3k_BT/2`를 열에너지에서 이중 차감하지 않는다. |
| Savin reverse fit과 새 `k_f=k_r exp(-43 K/T)` closure. raw independent forward fit은 별도 진단이다. | `d_cx_rates`의 closure 선택 | analytic fit domain 2.7–200000 K. source raw-fit 정확도 주장을 새 DB forward에 자동 승계하지 않는다. |
| D I + H II → D II + H I의 `Δb=43 k_B K>0`; reverse는 반대 부호. `Δx_e=0`. | `ionic_potential_eV`, D forward/reverse event | 공통 D-shifted potential을 사용한다. isolated D closure의 성공만으로 기존 isotope-blind PI/RR ledger와의 결합을 승인하지 않는다. |
| 비복사 충돌 `q_th=-Σ_r Δb_r R_r`; radiative CX는 `q_th=-Σ_r(Δb_r+Eγ_r)R_r`. | 현재 kernel의 nonradiative event sum | He/Li radiative CX의 total rate만으로 `Eγ`를 정하지 않는다. line excitation cooling, RR radiation, Compton, spectral transport는 이 kernel의 숨은 항이 아니다. |
| `u̇=-2Hu+q_th`, `Ṫ=-2HT+2q_th/(3k_BN)-T ẋ_e/N`. | `CollisionRhs.temperature_derivative_K_per_s`, `thermal_energy`, `temperature`; runner의 `rhs` | 21 abundance와 `u`를 적분하고 `T(u,Y)`로 복원한다. `u` 식에 전자수 항을 다시 넣지 않는다. isolated control은 `H=0`. |
| 일정 nH parcel: `d(Y,u)/dθ = (d(Y,u)/dt)/(n_H k_ref)`. | `prepare_task`, `execute_one`, `saved_arrays_and_checks` | 고정 diagonal scale는 좌표 변환이다. 열 bath·clipping·renormalization을 추가하지 않는다. |
| D-only `T(ξ)=T0-2ΔI ξ/(3k_BN0)`와 forward=reverse. | `d_cx_equilibrium_oracle`의 scalar `brentq`, saved extent-temperature 비교 | 별도 ODE 없이 closed-energy equilibrium을 계산한다. fixed-T bath equilibrium을 비교값으로 쓰지 않는다. |

## 5. F2 conditioning 교정과 독립성

H/D의 약 13.6 eV ionic potential을 `ε·Ydot`에서 직접 상쇄하면 0.0037054533 eV의 isotope defect를 구할 때 유효 자릿수를 잃는다. 초기 C9의 252 상태 중 85개가 해당 event-energy 상대 gate를 넘었다. 이를 소스 오차나 물리적 비보존으로 해석하지 않고 arithmetic conditioning 문제로 특정했다. [conditioning 원본](../verification/C9_ENERGY_CONDITIONING.json), [targeted 재검토](../verification/C9_TARGETED_RECHECK.json)에 입력·판정이 남아 있다.

최종 `rhs`는 `math.fsum(Δb_r R_r)`를 authoritative binding derivative로 쓰고 heat를 그 음수로 정한다. 직접 state dot product는 `binding_derivative_direct_state_eV_per_H_s`, direct−event 차이, constituent-energy scale와 함께 **진단**으로 남긴다. 따라서 event `heat+binding_dot=0`은 구성에 의한 항등식이다. 이를 독립적 동역학 보존 검사로 세지 않는다. F1은 particle aggregate·helper·RHS의 nonfinite 결과 거부로 닫았으며, N1은 rawfit/DB 선택을 model family와 별도 closure metadata로 표현해 닫았다.

더 실질적인 검사는 별도 상태변수로 적분한 `u`와 저장된 `ε·Y`의 합, 그리고 D-only scalar equilibrium이다. 또한 전체 에너지의 큰 H potential이 작은 D heat 오류를 가릴 수 있어 runner 독립 검토자가 **실행 전에** `|T_saved−T(ξ)|≤10⁻⁹ K`를 추가했다. 이 gate는 C02에서 3.410605131648481×10⁻¹³ K로 통과했다. 해당 gate의 목적·추가 시점은 [RUNNER_INDEPENDENT_REVIEW](../verification/RUNNER_INDEPENDENT_REVIEW.json)에 있다.

## 6. 실행된 control과 수용 결과

공통으로 DOP853, 161 saved samples, baseline `rtol=2×10⁻⁸`, scaled `atol=2×10⁻¹¹`이다. C01 정련은 `rtol=2×10⁻¹⁰`, `atol=2×10⁻¹³`, 최대 step 1/4이다. 입력·전체 abundance·reference rate·proper-time 변환·solver 환경은 [계획](../inputs/CONTROL_PLAN.json)과 최초 receipt가 가리키는 REQUEST 및 각 case receipt에 보존되어 있다.

| 실행 | 물리 입력 | 저장 T 범위 [K] | 최대 nucleus 상대 잔차 | 최대 `(u+b)` 상대 잔차 |
|---|---|---:|---:|---:|
| C01_BASE | 중성 CI+D CX; nH=10⁻³ cm⁻³; H ion=0.1, D는 초기 DB, 나머지 존재 isotope singly ion=0.01 | 24461.949997932665–25370.663084247735 | 9.641025415902605×10⁻¹⁶ | 8.881784197001252×10⁻¹⁶ |
| C02_BASE | D CX만; nH=1 cm⁻³; T0=300 K; H ion=0.5, D ion=10⁻⁶, 나머지 neutral | 299.99979308042737–300 | 8.881784197001252×10⁻¹⁶ | 1.1102230246251565×10⁻¹⁵ |
| C01_REFINED | C01과 동일 물리, 별도 수치 identity | 24461.94999793267–25370.663084247735 | 4.397502728453756×10⁻¹⁵ | 2.6645352591003757×10⁻¹⁵ |

세 실행 모두 saved species 최소 0, absent isotope의 절대 잔차 0, source-domain 검사 PASS, projection NONE이다. 고정 수용 기준 nucleus 10⁻¹⁰, energy 2×10⁻¹⁰을 통과했다. C02 최종 equilibrium 거리/D inventory는 3.635426294598055×10⁻⁹로 gate 10⁻⁶을 통과했다. C01의 정렬된 161점에서 최대 scaled state 차이는 4.574293383682441×10⁻¹⁵로 gate 10⁻⁶을 통과했다. 이 정련 비교와 sampled residual은 continuum certificate가 아니다. raw 정확도·physical-rate 오차를 이 작은 수치 차이로 대체하지 않는다.

## 7. 다음 실제 물리 의무와 전달 상태

1. **LOW_T_CI_SOURCE_COVERAGE:** PHYS78의 약 255–25371 K 전체 이력에 사용할 low-T cross section 또는 rate를 확보하고 Maxwellian 적분이나 source를 갖춘 연결 fit을 구성한다. 현재 neutral CI 1 eV 하한 아래를 0 또는 무제한 외삽으로 메우지 않는다. higher-stage source domain도 별도로 연결한다.
2. **HE_LI_CX_STATE_AND_PHOTON_ENERGY:** He/Li의 nonradiative final-state branching, corrected rate/domain, radiative photon-energy moment를 닫는다. total rate를 전부 gas heat로 넣는 것은 현재 유도에서 정당화되지 않는다.
3. **D_PI_RR_ENERGY_ADAPTER:** 하나의 D-shifted ionic potential을 PI threshold·RR emission·CI·CX에 일관되게 연결한다. 이 의무가 남아 있으므로 새 충돌 heat만 기존 PHYS78 방정식에 붙인 z20→2 실행을 승인하지 않는다.
4. **RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT:** 기존 `HII/H=2×10⁻⁴`, 나머지 존재 isotope neutral은 탐색 초기조건으로 보존한다. recombination에서 유도된 charge history로 승격하지 않는다. Li hard-UV inner-shell/branching·spectral energy, nuclear/molecular network, Compton·spectral transport 등의 inherited OPEN도 유지한다.

최종 게시·backup·Codex/다음-thread handoff의 완료 상태는 실제 commit/provider receipt와 payload identity를 대조하여 루트의 최종 전달 기록에서 갱신한다. 본 문서 작성 시 **R10/C10의 최종 전달 확인은 대기 중**이다. 이 대기와 별개로 위 세 isolated science execution은 receipt에 근거하여 완료되었다. 전체 physics 요청의 남은 의무는 DAG에 연결되며, strong no-go 또는 production admission은 발급하지 않았다.
