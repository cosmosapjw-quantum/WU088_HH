# WU088_HH: Bianchi 재이온화 적용을 위한 수렴 설계

작성일: 2026-10-02. 상태: DESIGN_SELECTED_BY_CURRENT_USER_SCOPE / NOT_ALL_THEORY_CLOSED.

## 1. 결정과 산출물의 경계

이 스레드의 최종 목적을 **Bianchi 재이온화가 소비할 수 있는, 출처·오차·반응 의미가 명시된 H–H 원자물리 구성요소**로 제한한다. 원 R31AO의 continuous Frozen107 → D_col/D_row → epsilon_C/R → represented model gaps → frozen Pareto 판정 경로는 유지한다. 재이온화 목적을 이유로 원 계수, 기하, 순서, 허용오차, 2,592 primitive 계약을 임의로 줄이지 않는다.

선택 경로는 ‘소비자 요구에서 역으로 닫는 두 개의 연결 경로’다.

1. HH 인증 경로: 남은 적용 정리와 exact gap/판정/assembly 구현을 이곳에서 끝내고 실제 대형 enclosure 계산과 host 인증만 NCP로 넘긴다.
2. 재이온화 연결 경로: 이미 정의된 BASS 수신기의 species/energy/source 계약에 HH의 어떤 channel이 들어갈지를 먼저 결정한다. HH 행렬 인증을 산란확률·단면적·반응률 인증으로 대신하지 않는다. 공통 H/He photoionization·recombination 경로를 HH 완료에 종속시키지 않는다.

이 설계가 승인하는 것은 작업 범위와 의존 순서다. 전체 이론 완결, 새 코드의 검증 또는 물리적 production admission을 선언하는 문서가 아니다. 본 단계에서 신규 HH 적분·trajectory·반응률 수치 계산은 0회다. 일반 코드 구현은 아래 작업 단위의 후속 산출물이다.

비선택 대안: 범용 원자/분자 산란 엔진을 먼저 완성하는 경로는 재이온화 요구를 넘으므로 제외한다. 지금 NCP 병렬 튜닝부터 반복하는 경로는 사용자의 분업과 맞지 않으므로 보류한다. 기존 미해결 사항을 ‘응용상 필요 없을 것’이라는 직관만으로 폐기하는 경로도 채택하지 않는다.

## 2. 실제 근거와 계승 상태

기준 소스 commit은 e3d68cac05f4bb389afd7cde968b0bda5a6711f7이다. 이 단계의 최초 additive 게시 commit은 d7a0b734a6dbec11a263980125a60d289ae6046a, tree는 2e511da9fbb24e236773e4b6722c7259e81cceba다. PR33은 확인 시 open/draft, 미병합이다.

기존 W3 COVERAGE ZIP·DB·보고서·receipt·handoff 다섯 파일을 원 bytes 그대로 기존 Google Drive/Dropbox에 create-only 업로드했다. 양쪽 완료 ACK/ID/name/size와 Drive parent readback을 확인했다. cloud content download는 하지 않았으므로 RESTORE_VERIFIED=false다. 과거 보고서/receipt에 적힌 당시 게시 실패는 수정하지 않으며, 새 RECOVERY_PUBLICATION.json이 후속 저장 성공을 기록한다.

현재 scientific coverage는 20/289, missing=269이고 누락 기여는 NOT_BOUNDED_OR_INCLUDED다. 고정 6셀 [275,67,288,272,16,0]은 계획만 준비되었고 실행되지 않았다. B22는 OPEN_UNDETERMINED다. 기존 40 tests PASS는 앞선 COVERAGE 단계의 증거이며 이번에 40개를 재실행했다고 하지 않는다.

| 원 단계 | 현재 확인된 범위 | 여기서 남길 실제 산출물 | NCP 또는 후속 실제 증거 |
|---|---|---|---|
| G0 | 기존31 table lineage와 원 SSOT 공백 구분 | 필요한 source/theorem/module만 crosswalk | 미복구 자료가 필요한 노드만 blocked |
| G1 | 여러 적용 정리·289셀 exact 합산 부품 | 필요한 missing lemma, all-primitive 적용·contraction 계약 | 전체 영역의 실제 수렴·비용 |
| G2 | 두 archive/12 NPY 범위의 exact decode | 실제 model 배열과 의미·index 연결 | 새로운 ABI는 별도 gate |
| G3 | norm/Gram 부품 검증, actual gap 미완료 | actual represented gaps + historical machine predicate bridge | 큰 입력이 필요할 때만 실행 분리 |
| G4–G5 | primitive0 strip·선택 endpoint의 한정 근거 | branch/domain/error ownership·endpoint 결합 검증기 | pinned backend/ABI, full interior |
| G6–G7 | 20셀과 고정6셀 adapter | 2,592-job 계약·streaming contraction·return decoder | 6셀 pilot, 전체 창/primitive, D/epsilon |
| G8 | 조건부 composition 부품 | frozen tolerance/strict comparison의 정확한 연결 | 실제 epsilon과 결합한 최종 판정 |
| G9 | strip scoped 독립 검토, 새 부품 자체 검증 | theory/implementation 검토와 실패 모드 정리 | 실제 full certificate 독립 과학 검토, B22/성능 |

모든 G0–G9를 완료로 올리지 않는다. HH 파일의 z는 source의 기하 좌표다. 이를 cosmological redshift로 해석하지 않는다. 새 인터페이스에서 geometry_z_au와 cosmological_redshift를 구별하고 D_HH, doppler_factor, epsilon_D를 별도 이름으로 둔다.

읽은 소비자 근거는 H_ATOMIC_REVISED_RESEARCH_PLAN_20260929.md와 BASS_PRESENT_R1_NONPERTURBATIVE_MULTIFREQUENCY_HHE_REIONIZATION_CONTRACT_20260917_RESULT_v1.md다. 이들은 채택된 scope/interface 근거로 사용하며, 전체 BASS의 10월2일 최신 구현 상태를 대체하지 않는다. 최신 receiver 파일 ID/commit이 필요하면 해당 연동 노드에서 정확히 회수한다.

## 3. 최소 물리 범위

최초 integration fixture는 기존 R1의 prescribed Bianchi-I, 비경사 물질 u=n, 비평형 다주파 H/He 수신기다. H-only projection은 단위/부분 시스템 검사로 사용하며, 이를 H/He production의 대체로 선언하지 않는다. 원자 module은 국소 물질 tetrad에서 값을 반환하고 기하 수송은 기존 BASS에 맡긴다. 다른 Bianchi 유형과 finite tilt의 일반 국소 API는 막지 않되, 모든 유형의 수송기를 이 저장소에서 새로 만드는 것은 제외한다.

사용할 기본 상태는 기존 수신기의 {f_gamma,x_HII,x_HeII,x_HeIII,u_th}; 원자 provider의 반환은 process별 event rate, nuclei/charge/free-electron source, threshold/internal-energy 및 heat/escaping-photon ownership이다. HH가 직접 교체할 rate의 process ID와 유효영역은 아직 확정되지 않았고 CHANNEL_MAPPING_UNRESOLVED로 둔다.

자동 확장하지 않을 것: 금속·먼지·분자화학 전체, 임의 고준위/continuum 완비성 탐구, 일반 He/H2+/H+H charge-exchange 원전의 재개발, 재결합 epoch용 HyRec 전체 재구현, 자체 Einstein backreaction, 3차원 재이온화 방사유체역학, CMB 추론/관측 fitting, 원자 입력의 학습 재훈련. 단, 이 중 한 항목이 선택된 재이온화 source의 보존법칙 또는 사전 고정 오차를 닫는 데 반드시 필요하다는 근거가 나오면 그것만 별도 최소 노드로 재등록한다.

HH electronic ion-pair channel과 free-electron ionization continuum은 같은 최종 상태가 아니다. 기존 47+2 basis의 실제 channel crosswalk와 asymptotic projectors가 확인되기 전에는 ionic 확률을 ionization rate로 바꾸지 않는다. H+ + H 공명 전하교환은 이 저장소의 neutral H–H 계산과도 별도 authority다.

## 4. 여기서 끝낼 이론과 휴대 가능한 구현

### C0. 응용 계약과 channel crosswalk

입력: 최신 HH state/basis/source registry, 위 R1 수신기, 기존 공통 H/HHe source authority.

산출물: APPLICATION_CONTRACT.json, HH_CHANNEL_CROSSWALK.json, RELEVANCE_OBLIGATIONS.json. 각 entry는 exact source ID/hash, 입·출력 상태/축퇴도/threshold/대칭계수, 물질 frame, 반환 단위, 수신기 field, 자료의 energy/temperature/density/distribution support를 가진다. 기하 z와 우주론 redshift를 강제 분리한다.

결정: channel마다 REQUIRED_FOR_SELECTED_CONSUMER / CONDITIONAL / PROVED_IRRELEVANT_IN_DOMAIN / UNRESOLVED 중 하나만 허용한다. 숫자 없는 ‘무시 가능’ 판정은 금지한다. T, redshift, 충돌 energy, source SED, tilt 허용영역과 소비자 observable error budget은 회수된 실제 수신기 계약에서 가져온다. 없는 값은 null+DOMAIN_CONTRACT_REQUIRED이며 추정한 수치로 채우지 않는다.

완료: 모든 요청 process가 기존 provider 또는 정확한 HH 산출물 경로에 하나로 연결된다. HH가 대체하지 않는 표준 rate는 source를 그대로 보존한다. 이 완료가 대형 HH 적분의 선행 성공을 요구하지 않는다.

### C1. R31AO의 실제 gap·판정 경로 완결

기존 exact decoder, exact_gram/engine.py와 composition/adapter.py를 재사용한다. R31AK/R31Z/R31AD의 실제 D_col(47×2), D_row(2×47), 독립 저장 K를 semantic identity/index까지 연결한다. H차수 비교·synthetic norm 검사를 실제 model gap으로 대체해 말하지 않는다.

제안 새 파일: exact_gap_binding.py, machine_predicate_bridge.py, ACTUAL_MODEL_GAP_INPUTS.json, PREDICATE_BRIDGE.json. 각각 source-bound 배열 import, archived binary64 predicate와 exact-real 조건의 관계, 실제 입력 ledger, 판정 경계 검증을 맡는다. 기존 모듈의 128은 radical의 절대 dyadic grid 2^-128이지 전체 norm의 상대128bit 정확도가 아님을 보존한다.

증명/검증: exact complex subtraction·conjugation·2×2 Gram·outward radical·Dmax·독립 model K·near-tie strict inequality·frozen binary64 tol token 0x3ddb7cdfd9d7bdbb·resource limit. 직접 target error gap과 represented gap±2epsilon의 교집합 계약을 보존하고 X0…X8/eta를 다시 더하지 않는다.

완료: 실제 represented gap intervals와 machine bridge는 얻되 epsilon_C/R가 없으면 final verdict=UNRESOLVED_INPUTS로 끝난다. 이 노드는 신규 HH 적분 없이 우선 실행할 수 있다. 입력 매핑 실패는 theory 오류가 아니라 provenance blocker로 기록한다.

### C2. 전체 인증 pipeline의 portable reference 구현

제안 새 파일: certificate_join.py, primitive_campaign_contract.py, result_ingest.py, certificate_return.schema.json. 기존 frozen validator/primitive join/endpoint/composition/coverage 기능을 wrapper로 연결하며 독립적인 duplicate solver를 만들지 않는다.

필수 구현: source/window/primitive/128bit별 job identity, 정확한 포함영역 partition, primitive별 coverage, endpoint 단 한 번 결합, source-prescribed normalization와 signed ordered contraction, D_col/D_row·epsilon 출력, 고정 판정기 연결. post-integral row conjugation을 callback 내부로 옮기지 않는다. 동일 window/primitive의 전체289가 아니면 endpoint+부분 합을 whole-domain enclosure라 하지 않는다.

검증: 289 완전/누락/중복 fixture, 다른 primitive의 endpoint, 잘못된 input/plan/source, double-counted endpoint, altered signs/order, invalid ball, wrong units, duplicated RETURN, interrupted delivery, final-claim 승격 시도. exact reduce는 worker 순서가 아니라 명시적 source order와 정확 산술을 따른다. 자동 retry 없음, 단일 canonical coordinator와 영구 one-shot registry. 분산 lock/64rank performance는 별도 NCP 작업이다.

완료: 소형 synthetic와 이미 있는 raw로 end-to-end ingestion/claim gate가 실제 동작한다. 전 primitive source bounds/normalized error ownership의 missing lemma는 명시적 proof obligation으로 닫는다. 실제 width/수렴/벽시계는 정리 완료 상태로 흡수하지 않는다.

### C3. 선택된 HH channel의 산란→반응 provider 계약

C0에서 필요한 channel로 확정된 경우만 시행한다. provider의 최소 경로는 O/H/D 및 독립 dotO·ionic authority → admissible evolution/asymptotic projection → transition probability 또는 S matrix → flux-normalized cross section → distribution average다. 각 화살표는 별도 식·단위·오차·경계조건을 가진다. D/epsilon만으로 임의 σ 또는 k를 발명하지 않는다.

이곳에서 끝낼 것: source가 정한 운동/ETFs/고정-Q/기저 convention의 적용 증명, norm/flux/positivity·microreversibility, 사용한 trajectory approximation의 regime, channel completeness ceiling, energy/impact-parameter/partial-wave tail 및 interpolation error 계약. full49/BR01/BR02/independent review가 요구되는 실제 propagation은 gate 이전에 실행하지 않는다.

제안 새 파일: channel_provider.py, scattering_observable_adapter.py, rate_average.py, rate_uncertainty.py. 물리적으로 승인되지 않은 채널은 SourceUnavailable/UnsupportedChannel로 반환한다. Born, straight-line trajectory, angular isotropy를 default fallback으로 숨기지 않는다. 이미 인증된 외부 σ/k를 사용할 경우 exact provider ID와 불확실성 의미를 남기고 ab-initio HH 결과라 부르지 않는다.

완료: 필요한 channel만에 대해 식과 reference 구현·analytic fixture가 완성되고, 실제 원자 수치 채움과 인증만 남는다. channel mapping 자체가 안 닫히면 consumer를 막지 않는 bounded negative result를 남긴다. 그렇다고 원 HH D/epsilon 과제까지 조용히 삭제하지 않는다.

### C4. BASS에 전달할 국소 source와 오차 조합

제안 새 파일: reionization_source_adapter.py, process_ownership.py, local_receiver_fixture.py. 기존 BASS transport를 복제하지 않고 국소 chemistry/heat/opacity insertion seam만 구현한다. 어떤 provider가 같은 process를 중복 소유하면 fail-closed한다.

반환 예: {process_id, source_id/hash, frame, rate_interval, rate_unit, stoichiometry, electron_delta, threshold_energy, heat, radiative_loss, domain, error_components, admission}.

검증: nuclei·charge left-null invariants, photo absorption=primary ionization ownership, ion-pair/CX electron count, zero-process/zero-density, threshold crossing, Maxwell limit, FLRW limit, 작은 shear 참조, invalid fractions와 heat를 silent clip하지 않는 동작. 조건부 detailed balance는 실제 reverse process·분포·축퇴도 가정 아래에만 검사한다.

R1의 첫 수신기는 u_th를 진화시키므로 조성 변화에 따른 n_part 변화를 온도 ODE에 숨기지 않는다. tilt를 켤 때는 matter-frame energy/rate와 proper-time 변환, bulk kinetic reservoir를 함께 닫아야 한다. scalar thermal k(T)를 비등방 분포의 보편적 폐쇄로 쓰지 않는다.

완료: HH provider on/off가 기존 baseline source를 보존하고, 실제 원자자료가 없어도 synthetic provider로 국소 end-to-end 조합·보존·반환계약을 검증한다. 이는 physical reionization history 검증이 아니다.

### C5. 한 번의 종결 검토와 실행 인계

산출물: THEORY_CLOSURE.json, PORTABLE_IMPLEMENTATION_MANIFEST.json, NCP_EXECUTION_CONTRACT.json, RETURN.schema.json, START_HANDOFF_KO.md.

이론 종료 조건: 선택된 응용 domain의 모든 necessary lemma가 PROVED 또는 LITERATURE_SUPPORTED_WITH_PROVED_ADAPTATION이고 physical/source mapping의 빈칸이 없다. 원자 model의 유효성에 관한 수치/실험/독립 증거가 남으면 그 항목은 별도 physical gate이며 ‘증명 완료’로 처리하지 않는다.

구현 종료 조건: actual entry points, API/schema, error paths, deterministic results, adversarial fixtures, restart/recovery, source pins, finite resource rejection이 실제 테스트된다. 소스만 작성하면 IMPLEMENTED, 테스트를 실제 통과하면 IMPLEMENTATION_VERIFIED, NCP target-host 실행을 통과해야 RUNTIME_QUALIFIED다.

최종 가능한 이곳의 종료 상태: THEORY_SPEC_FROZEN__PORTABLE_IMPLEMENTATION_VERIFIED__NCP_CERTIFICATION_PENDING. 지금은 이 상태가 아니다. 독립 reviewer가 없으면 독립 검토를 자체검토로 대체하지 않고 AWAITING_INDEPENDENT_REVIEW를 남긴다.

## 5. 직접 유도한 source 의미·rate 변환 검사

이는 이번 설계에 붙인 일반 인터페이스 lemma다. frozen HH의 실제 channel을 새로 승인하는 정리가 아니다.

species 순서를 (HI,HII,Hminus,e_free)로 놓는다. 예시 event의 변화벡터는

- HI+HI→HI+HII+e: (-1,1,0,1)
- HI+HI→HII+Hminus: (-2,1,1,0)
- HII+e→HI+photon: (1,-1,0,-1)
- HII+HI→HI+HII (aggregate resonant CX): (0,0,0,0).

nuclei row (1,1,1,0)와 charge row (0,1,-1,-1)를 곱하면 네 경우 모두 0이다. free-electron 변화는 (1,0,-1,0)이다. CX의 aggregate species source가 0이어도 입자별 velocity/energy exchange는 0이라고 할 수 없다. Hminus를 실제 state에 추가해야 한다면 downstream reaction graph와 보존 ledger를 함께 닫거나, elimination closure를 증명해야 한다. 조용히 버리거나 e_free로 치환하지 않는다.

두 입자의 상대운동이 비상대론적이고, drift 없는 등방 Maxwell 분포이며 E=mu*v_rel^2/2, theta=k_B*T_rel>0일 때

k(T_rel) = sqrt(8/(pi*mu))*theta^(-3/2) * integral[E*sigma(E)*exp(-E/theta), E=E_th..infinity].

서로 다른 Maxwell 온도 T_a,T_b이면 T_rel=mu*(T_a/m_a+T_b/m_b). drift나 비등방 분포가 있으면 scalar T_rel 식을 일반화해 쓰지 않고 상대속도 분포 자체를 적분한다. σ가 unpolarized total channel cross section이라는 가정도 명시한다. [k]=m^3/s, [sigma]=m^2, [E]=J다. 실제 event density는 서로 다른 species이면 n_a*n_b*k, 동일 입자 pair이면 채택된 unordered-event convention에서 n_a^2*k/2이고 stoichiometric source가 event multiplicity를 담당한다.

상수 σ0와 threshold E0의 fixture:
k = σ0*sqrt(8*theta/(pi*mu))*(1+E0/theta)*exp(-E0/theta).

Wolfram 실제 평가에서 v→E weight ratio=1, 위 threshold rate identity=true, 두 conservation row=0, electron deltas=(1,0,-1,0)을 확인했다. 이것은 finite symbolic check이며 HH 단면적/반응률 계산이 아니다. 코드는 SYMBOLIC_CHECKS.wl와 SYMBOLIC_RESULT.json에 있다.

## 6. 오차 예산과 수렴 기준

HH 기존 예산은 그대로다: 289*2^-57=(289/512)*2^-48<2^-48. 이 식은 계산된 모든 셀의 component radius에 관한 것이지 미계산 영역의 기여 bound가 아니다.

새 rate layer에서 positive Maxwell weight를 w_T라 하면
|delta k(T)| <= integral[w_T(E)*delta_sigma(E) dE] + delta_quadrature + delta_tail + delta_interpolation.
각 항의 owner와 포함 범위를 명시하고 이미 total source bound에 포함된 항을 다시 더하지 않는다. fit 데이터가 rigorous source-error를 제공하지 않으면 해당 항은 interval-certified로 승격하지 않고 model/data uncertainty로 남긴다.

상태벡터를 차원 없는 고정 scaling으로 비교하고 같은 prescribed geometry/초기조건을 사용한다. F가 등록 domain에서 Lipschitz constant L(t)를 가지며 source perturbation norm<=b(t)이면 Gronwall로
||delta y(t)|| <= exp(integral_0^t L)*||delta y(0)|| + integral_0^t exp(integral_s^t L)*b(s) ds.
이는 C0의 domain과 norm/scaling, L,b의 유효 bound를 실제 확보했을 때만 rigorous observable propagation으로 사용한다. sensitivity/adjoint 점 추정은 우선순위 도구일 뿐 이 bound의 대체가 아니다. HH epsilon의 단위와 ionization/temperature observable tolerance를 직접 비교하지 않는다.

R1 수신기의 기존 numerical gates는 보존한다: smooth global time order>=1.8; exact characteristic relative error<=1e-10(where precision permits); nuclei sum<=1e-10(unit)/1e-8(long); cumulative photon-primary defect<=1e-8; normalized negativity>1e-12 FAIL; weak-anisotropy derivative discrepancy<=1e-3. 이 수치를 HH certificate의 tolerance로 사용하거나 physical uncertainty allowance로 바꾸지 않는다. 구체적인 소비자 observable error allocation은 C0에서 source-authority로 고정한다.

## 7. 여기와 NCP의 분업

여기: 정리와 적용 전제·closure, exact represented gap, serialization/ABI 의미, 원 source를 보존하는 portable scalar/reference 구현, 반응/channel/rate/보존 interface, analytic·synthetic·이미 존재하는 raw를 이용한 가벼운 검증, 실행/반환 schema. 수치가 필요하면 실제 자원내 단일 bounded step으로 수행하고 환경이 막히면 해당 항목만 NCP pending으로 둔다. host gate를 만족하지 못하는 six-cell pilot을 반복 시도하지 않는다.

NCP/local Codex: pinned native build/ABI와 upstream tests, 비특권 containment/B22 synthetic 재현 및 원인 규명, 고정6셀→결과를 반영한 추가 유한 batch, 전체289·2,592 primitive·final D/epsilon, 필요한 channel의 actual propagation/cross-section/rate fixtures, end-to-end 소비자 수치 인증, OpenMPI/Fortran·SIMD/벡터화·topology/memory tuning·실측. 목표64core/128GB는 실제 quota/affinity/RAM과 topology를 확인한 뒤 적용한다.

NCP의 worker는 물리 가정·basis/order·source SED·허용오차를 새로 선택하지 않는다. 성능 최적화는 기존 scalar/interval reference와 identity/parity를 통과한 경우만 admitted candidate다. fast-math·정밀도 저하·double-counting 제거를 명분으로 source 항 삭제·허용오차 완화는 금지한다. 속도향상은 동일 작업의 직렬 benchmark와 비교해 실측한다. 그 기준이 없으면 timing만 보고한다.

한 배치 실패 후 automatic retry나 breadth expansion을 하지 않는다. 원 결과의 width/resource/analytic-domain/implementation/runtime 실패를 구분하고, finite alternative가 이론상 허용됨을 확인한 다음 별도 source-bound continuation으로 진행한다.

## 8. 실행 순서와 종결

C0→C3→C4→C5와 C1→C2→C5를 분리해 진행한다. C1/C2는 기존 HH 목표를 보존하며 C3의 relevance 판정이 대기 중이어도 진행할 수 있다. C3/C4는 actual HH data admission이 없을 때 explicit unadmitted fixture로만 검사한다. 공통 H/He baseline receiver는 기존 authority를 소비하므로 전체 HH certificate를 기다릴 필요가 없다.

다음 canonical bounded node: C0_APPLICATION_CONTRACT_AND_HH_CHANNEL_CROSSWALK. 먼저 현재 basis/channel과 실제 receiver 요청 field를 한 번 연결하고 소비자 domain/오차 예산의 source를 고정한다. 뒤따르는 현재환경 우선 구현은 C1_ACTUAL_REPRESENTED_GAP_AND_MACHINE_PREDICATE_BRIDGE다. fixed six-cell HH 실행은 NCP 대기열에 유지한다.

더 넓은 연구를 다시 여는 조건은 선택된 channel의 보존/유효영역/오차 예산을 현재 정리나 authority로 닫을 수 없다는 구체적인 counterexample 또는 missing premise뿐이다. ‘더 정밀할 수 있다’는 이유만으로 새 분야를 추가하지 않는다. 이미 닫힌 정리와 완료된 raw를 의례적으로 다시 검증하지 않는다.

## 근거

[S0] WU088_HH 원 repo AGENTS.md, README_KO.md 및 original gap-closure prompt. SOURCE_CROSSWALK.json에 exact SHA가 있다.
[S1] W3 COVERAGE report/STAGE_DELTA/composition README: 현재 구현·실행·미해결 경계를 보존.
[S2] H_ATOMIC_REVISED_RESEARCH_PLAN_20260929.md, Library file_00000000e61c81fda312020552699d59, 특히 공통 H lane 비종속성과 process relevance 기준.
[S3] BASS_PRESENT_R1_NONPERTURBATIVE_MULTIFREQUENCY_HHE_REIONIZATION_CONTRACT_20260917_RESULT_v1.md, Library file_0000000056c08206b62f4e5e92910f90, baseline/frame/state/acceptance 계약.
[S4] Friedrich, M. M., Mellema, G., Iliev, I. T., Shapiro, P. R. (2012), Radiative transfer of energetic photons: X-rays and helium ionization in C2-Ray, arXiv:1201.0602. 다주파 H/He·thermal/reference 비교 근거이며 Bianchi/HH의 증명이 아니다.
[S5] Verner, Ferland, Korista, Yakovlev (1996), ApJ 465,487, DOI:10.1086/177435; arXiv:astro-ph/9601009; 저자 data site https://www.pa.uky.edu/~verner/photo.html. 기존 photoionization provider를 재사용할 문헌 근거이며 frozen provider를 자동 교체하지 않는다.
[S6] Furlanetto & Stoever (2010), MNRAS 404,1869, arXiv:0910.4410, DOI:10.1111/j.1365-2966.2010.16401.x. Hard-photon secondary deposition은 별도 source인 이유를 확인한 근거다.

SciSpace는 discovery에만 사용했다. 반환된 C2-Ray metadata에서 first author/날짜가 불완전했으므로 arXiv 원전으로 대조했다. WolframContext의 관련 없는 quantum-well 결과는 채택하지 않았고 직접 지정한 symbolic evaluator 결과만 사용했다. 새 광범위 문헌 DB는 만들지 않았다.
