# PHYS80 R1–R10 / C1–C10 근거와 식–코드 연결

이 문서는 사용자가 선택한 embedded physmath workflow **1.0.0의 단계명**을 사용한다. 연구 대상은 고정 inventory의 PHYS79 isolated CI/CX 부분계와 별도의 일반 Maxwellian 수치 kernel이다. 세 새 ODE의 완료를 전체 원자·열·우주론적 폐쇄의 완료로 확대하지 않는다. HH_R10=OFF, production admission NOT_ISSUED이다.

아래 상대 경로는 PHYS80 unit root 기준이다. 과학 실행은 [실행 원장](EXECUTION_LEDGER.json)과 [SCIENCE_STDOUT](verification/SCIENCE_STDOUT.json), 전달 단계는 [S0 게시·checkpoint 영수증](delivery/POST_PUBLICATION_RECEIPT.json)과 외부 final-delivery JSON으로 판정한다. 이 문서는 **과학 판정·재개 조건·S0 게시/checkpoint 인계 완료**를 기록한다. 최종 S1 HEAD와 최종 ZIP restore의 마감 상태는 외부 JSON에 결합하며, 이 내부 snapshot이 아직 생성되지 않은 자기 hash를 주장하지 않는다.

## 연구 트랙 10단계

| 단계 | 실제 수행과 판정 | 핵심 증거 |
| --- | --- | --- |
| **R1 연구 위치·계약** | 부모 PR134 actual HEAD 및 고정 inventory/활성 반응을 명시. 기존 완료 identity 재실행 금지, expansion/PI/RR/source injection 제외. COMPLETE_SCOPED. | [inventory](inventory/INCREMENTAL_INVENTORY_KO.md), [physics gate](theory/PHYSICS_TO_CODE_GATE_KO.md) |
| **R2 근거·재사용** | PHYS79 source·세 저장 궤적과 기존 backup 증거를 identity로 재사용. 제한된 최신 ref/handoff 조회를 수행하고 새 sibling 결과의 범위를 분리. Exa/SciSpace primary-source 단면적 검토. COMPLETE_SCOPED. | [parent provenance](vendor/PHYS79_PROVENANCE.json), [restore reuse](inventory/PARENT_RESTORE_EVIDENCE_REUSE.json), [게시 전 갱신](inventory/PREPUBLICATION_REFRESH_KO.md), [source receipts](source/maxwellian/SEARCH_RECEIPTS.json) |
| **R3 주장·전제 정렬** | isotope electronic equality, 고정 isotope inventory, higher-charge 0, gas pi=0, 공통 thermal pool, actual ionic potential과 rate threshold 구분. 일반 kernel의 수치 검증과 species physical admission 구분. COMPLETE_SCOPED. | [계산 계약](theory/COMPUTATIONAL_CONTRACT.json), [저온 source 판단](source/maxwellian/LOW_T_SOURCE_ASSESSMENT.md) |
| **R4 가설·표현 탐색** | Q,v,h,l exact quotient 및 C02 scalar 표현을 구성. QSS의 lag/coupling 조건과 splitting 비가환 오차를 검토하고 이번 계산에는 적용하지 않음. COMPLETE_SCOPED. | [환원 유도](theory/EXACT_REDUCTION_AND_JACOBIAN_KO.md), [Radau primary evidence](theory/SCIPY_RADAU_PRIMARY_EVIDENCE.json) |
| **R5 구성적 유도** | affine isotope lift, 전자/입자 수, anchored energy, exact RHS, thermal analytic Jacobian 및 scalar equilibrium의 유일성 유도. Maxwellian number·energy moment와 E1 witness를 구성. COMPLETE_SCOPED. | [환원 유도](theory/EXACT_REDUCTION_AND_JACOBIAN_KO.md), [Maxwellian 유도](source/maxwellian/MAXWELLIAN_DERIVATION.md) |
| **R6 독립 검증** | Wolfram context 후 실제 evaluator 성공 2건으로 symbolic residual 0 확인. 1건 syntax failure 보존. 독립 full-parent event tangent와 수치 Jacobian 검토를 별도로 수행. PASS_SCOPED. | [reduction receipt](theory/WOLFRAM_REDUCTION_RECEIPT.json), [scalar/rate 성공 receipt](theory/WOLFRAM_SCALAR_RATES_FIXED_RECEIPT.json), [보존 실패](theory/WOLFRAM_SCALAR_RATES_RECEIPT.json), [독립 review](verification/independent/REVIEW_KO.md) |
| **R7 판별 검증** | 고정 gate 아래 서로 다른 numerical identity의 reduced control 2개+refinement 1개를 실행. 저장된 22-state 궤적·closed-energy extent·refinement를 비교. PASS_SCOPED. | [사전 계획](inputs/REDUCTION_PLAN.json), [science receipt](verification/SCIENCE_STDOUT.json), [case receipts](results/reduced/cases/) |
| **R8 결과 판정** | 부모 scaled-state 차이 최대 \(3.5858783426\times10^{-9}\), 새 refinement \(3.5481474703\times10^{-9}\), 모든 해당 gate PASS. 계산량 관측과 historical wall performance를 구분. kernel은 math-only admission. COMPLETE_SCOPED. | [최종 과학 보고서](FINAL_REPORT_KO.md), [science receipt](verification/SCIENCE_STDOUT.json), [kernel receipt](source/maxwellian/BELL_KERNEL_VERIFY_RECEIPT.json) |
| **R9 정식 결과·코딩 연결** | 가정→lift/RHS/Jacobian→solver state→비교 oracle를 공개 함수에 연결. 저온 source 입력의 후속 의무를 코드 기본값으로 대체하지 않음. COMPLETE_SCOPED. | 아래 식–데이터–함수 표, [core equation review](theory/CORE_EQUATION_REVIEW_KO.md), [source coefficient status](source/maxwellian/SOURCE_COEFFICIENTS.json) |
| **R10 종료·재개** | 고정 부분계 결론 및 다음 LOW_T source/energy 계약을 기록. 완료 identity 재사용, publication/backup/handoff 마감 기준을 명시. **SCOPED_SNAPSHOT_CLOSED; FINAL_DELIVERY_BOUND_EXTERNALLY**. | [과학 보고서 §8](FINAL_REPORT_KO.md), [실행 원장](EXECUTION_LEDGER.json), [S0 게시/checkpoint](delivery/POST_PUBLICATION_RECEIPT.json), 실제 외부 final-delivery 및 PR 본문 |

## 코딩 트랙 10단계

| 단계 | 실제 수행과 판정 | 핵심 증거 |
| --- | --- | --- |
| **C1 목표·baseline** | 고정 물리의 22→4/1 환원 정확도를 기존 저장 trajectory에서 확인하는 목표를 설정. 부모를 다시 적분하는 benchmark는 설정하지 않음. COMPLETE_SCOPED. | [parent provenance](vendor/PHYS79_PROVENANCE.json), [pinned parent cases](inputs/phys79_cases/), [plan](inputs/REDUCTION_PLAN.json) |
| **C2 식–데이터–코드** | ionic potential, elemental CI, DB43 CX, abundance scaling, theta clock와 exact state lift를 매핑. 실제 import 경로까지 pin. COMPLETE_SCOPED. | [reduced.py](source/reduced.py), [bridge](source/phys79_bridge.py), [계산 계약](theory/COMPUTATIONAL_CONTRACT.json), 아래 함수 표 |
| **C3 수치 설계** | Radau+analytic Jacobian, trial strict guard, accepted mesh+161 sample 검증, 대각 scaling, 사전 tolerances/gates 고정. QSS/projection/trace floor 없음. COMPLETE_SCOPED. | [사전 계획](inputs/REDUCTION_PLAN.json), [physics gate](theory/PHYSICS_TO_CODE_GATE_KO.md) |
| **C4 실행 DAG·자원** | worker/thread 각 1 및 실제 shared lease. create-only identity, 호출 전 marker, 실패/부분 차단, byte-verified complete skip. COMPLETE_SCOPED. | [runner](source/run_reduced.py), [실행 원장](EXECUTION_LEDGER.json), [attempt receipts](results/reduced/attempts/) |
| **C5 구현** | ExactReduction와 analytic rate derivatives, 4D/1D operator, pinned bridge, durable runner, 독립 generic Bell Maxwellian kernel 구현. COMPLETE_SCOPED. | [reduced.py](source/reduced.py), [runner](source/run_reduced.py), [bell_kernel.py](source/maxwellian/bell_kernel.py) |
| **C6 구현 검증** | 독립 16 논리군 최초 15 PASS+fixture 1실패 보존, 미완료 3점만 보완. kernel의 별도 unittest 6개 PASS. 원격·ODE 없는 유한 검증. PASS_SCOPED. | [초기 receipt](verification/independent/check_result_001.json), [3점 supplement](verification/independent/jacobian_supplement_001.json), [kernel receipt](source/maxwellian/BELL_KERNEL_VERIFY_RECEIPT.json) |
| **C7 과학 검증** | 새 control 2개+별도 refinement 1개 모두 완료. parent saved-state, energy/nucleus, C02 extent/root 및 refinement gate 통과. PASS_SCOPED. | [science stdout](verification/SCIENCE_STDOUT.json), [command completion](verification/SCIENCE_COMMAND_COMPLETED.json), [3 case receipts](results/reduced/cases/) |
| **C8 수치·재현성** | source/runtime/numeric identity를 고정하고 각 NPZ/receipt bytes 보존. 실제 두 번째 execute에서 완료 3개 skip, 새 ODE 0. 표본 검증을 continuum 증명과 구분. PASS_SCOPED. | [resume stdout](verification/RESUME_STDOUT.json), [resume command](verification/RESUME_COMMAND_COMPLETED.json), [case hashes](results/reduced/cases/), [runtime intake](inventory/RUNTIME_AND_PARENT_IDENTITY.json) |
| **C9 독립 검토** | 물리 식·Jacobian source review 및 별도 bounded code/finite review. boolean physical flag, actual import cache, raw signed coordinates, orphan output, claim ownership 위험을 수정한 source 확인. 재귀 검토·old suite 재실행 없음. PASS_SCOPED. | [식 review](theory/CORE_EQUATION_REVIEW_KO.md), [독립 review](verification/independent/REVIEW_KO.md) |
| **C10 판정·인계** | 과학 verdict, exact identities, no-replay 및 next DAG 기록 완료. additive actual descendant Draft PR/backup/최종 Codex·다음-thread handoff는 **SCOPED_SNAPSHOT_CLOSED; FINAL_DELIVERY_BOUND_EXTERNALLY**. | [과학 보고서](FINAL_REPORT_KO.md), [실행 원장](EXECUTION_LEDGER.json), [S0 게시/checkpoint](delivery/POST_PUBLICATION_RECEIPT.json), 최종 외부 final-delivery |

## 식–source–state–검증의 연결

| 물리·수치 객체 | 입력과 실제 함수 | 상태와 별도 검증 |
| --- | --- | --- |
| elemental neutral CI와 온도 미분 | vendor PHYS79 collisional.py의 source-domain 조건; reduced.py의 ci_value_derivative | H/D 공통 kH, He/Li 각각 공통 rate; 부모 rate 값과 독립 derivative 23점 |
| D/H ground CX \(k_f=k_r e^{-43/T}\) | cx_value_derivatives; 실제 부모 potential 차이 \(\delta_{\rm eff}\)와 rate exponent 43 K를 구분 | Q에서 CX 상쇄, v의 양방향 항; symbolic scalar 미분 및 C02 closed-energy equilibrium |
| invariant inventory와 affine isotope lift | ExactReduction.__init__, raw, state, encode | z=(Q/(H+D),v/D,h,l) 또는 scalar v/D; 초기 y/u/T 보존, 다른 isotope 초기 fraction fixture |
| anchored energy와 입자수 | state 및 _values: \(u_0-b\cdot(q-q_0)\), \(T=u/(C_VN)\) | full-state 출력 및 물리/source guards. energy residual의 construction 성격을 명시 |
| 반응 RHS와 analytic Jacobian | rhs, jacobian; physical-coordinate 미분 뒤 diagonal/time scaling | lifted_rhs를 부모 21-species event operator와 13상태 비교; 별도 Jacobian 12점/39열 |
| source/입력 identity와 실행 권한 | source_manifest, prepare, existing, execute_one, run | create-only claim, solve-call marker, runtime/source hashes, 실패 자동 replay 차단, 실제 완료 3개 skip |
| 22상태 복원과 판정 | full_states, scalar_diagnostic; pinned parent time grid | accepted endpoint 및 dense 161점; parent trajectory·refinement·extent/root 비교 |
| 명시 단면적의 Maxwellian 평균 | BellParameters, cross_section_cm2, maxwellian_at_order, evaluate_maxwellian | log-rate/underflow flag, number/incident-energy moment, negative-cross-section rejection |
| analytic pure-A witness | pure_a_oracle 및 E1/scaled asymptotic | 9 witness, 18 order profile, 별도 6 unittest. 실제 H/He/Li 단면적 admission은 없음 |
| 결과 표현 | render_figures.py가 기존 NPZ와 kernel receipt를 읽음 | 새 model evaluation/ODE 0; PNG3 시각 PASS, PDF3 같은 그림 export |

## 집계와 한계

PHYS80의 새 scientific ODE는 정확히 3회이며 실패 0이다. 독립 검토의 16은 논리 점검군, Maxwellian의 6은 unittest method 수다. 한 fixture 실패와 3점 보완을 숨기거나 이 수들을 합쳐 단일 PASS test 수로 쓰지 않는다. Wolfram의 2개 성공 algebra와 1개 syntax failure, figures의 1회 render, completed skip 3개도 각자 다른 실행 유형이다. PHYS78/79 ODE와 sibling 실행은 재사용 evidence이며 이 unit의 신규 수에 포함하지 않는다.

공간적으로 고정된 invariant manifold의 exactness, 선언된 source domain 안의 유한 궤적 gate, generic quadrature의 수치 성질이 이번에 확보한 서로 다른 결과다. 전체 source-domain forward invariance, continuum/interpolant positivity, 실제 low-T cross-section 오차, 새 isotope injection, photon energy retention, 전 우주론적 closure는 별도로 남는다. 강한 no-go 정리를 선언하지 않았고, 다음 단계를 구성적으로 지정했다.

현재 사용자의 양 트랙 승인과 embedded workflow 1.0.0을 우선한다. cloud1.3 기본 R10 종료나 과거 PHYS71 우선순위를 이유로 승인된 C1–C10을 중단하지 않았으며, 역사적 지침·receipt를 수정하지 않았다. final HEAD/backup의 자기참조를 피하기 위해 전달 identity는 root가 마감하는 외부 final-delivery와 PR body에 연결한다. S0 science 게시와 양 provider checkpoint ACK는 실제 영수증으로 확인했다. 최종 metadata HEAD/ZIP full-byte restore 상태는 외부 final-delivery를 읽어 판정한다. 늦은 HH135/REI222 event-energy component 성과는 [별도 전달 평가](delivery/LATE_HH135_REI222_ASSESSMENT_KO.md)와 S1 DAG에만 반영하며, 완료된 PHYS80 과학 payload를 수정하지 않는다.
