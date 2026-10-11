# WU088_HH PHYS07 — NCP local Codex 실행 인계

이 문서 전체를 NCP local Codex의 작업 지시로 사용한다. **PHYS06에서 이미 구현한 energy/uniform/mixed/finite/paired adapter를 재사용하고, 실제 `phys04_prepare_family`와 `phys04_reduced_residual`이 만든 입력·leaf·값·미분을 전체 source box와 C² 근거에 연결하라.** 별도 사용자 첨부파일 없이 Git 또는 기존 두 백업에서 시작할 수 있다.

이번 목표는 실제 소스에 묶인 first-stage 산술 producer다. Native endpoint, conservative/BE point, certificate-internal point, native nonlinear root/certificate producer, IVP, heavy atomic 및 과거 과학 suite의 실행 ceiling은 각각 **0**이다. 새로 허용한 native source 산술 호출은 아래 두 이름의 첫 실행에만 한정된다. Public source 함수 호출과 실제 endpoint/root 실행을 같은 종류로 세지 않는다.

이 파일의 새 target 이름과 command는 **구현할 실행 계약**이며, 이미 실행된 프로그램이나 검사 결과가 아니다. `NCP_TASKS.json`의 수치 ceiling과 `NCP_RETURN_TEMPLATE.json`의 미측정 null을 그대로 적용한다.

## 1. 첨부 없이 정확한 입력을 복구한다

Repository는 `cosmosapjw-quantum/WU088_HH`다. 현재 PHYS07 자료의 복구 위치는 다음과 같다.

| 항목 | 위치 |
|---|---|
| 연구 branch | `research/hh-phys07-source-domain-20261011` |
| 연구 package directory | `research/r31ao_unequal_ladder/hh_phys07_source_domain_20261011_v1/` |
| Delivery directory | `research/r31ao_unequal_ladder/hh_phys07_source_domain_20261011_v1_delivery/` |
| Detached receipt | `WU088_HH_PHYS07_DELIVERY_RECEIPT_20261011_v1.json` |
| Google Drive folder ID | `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM` |
| Dropbox folder | `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928` |

먼저 Git delivery directory 또는 기존 백업의 START 안내에서 위 receipt를 읽고, **실제 읽은 receipt bytes의 SHA256**를 기록한다. Receipt의 `publication.commit`, `publication.tree`, `archive.name`, `archive.bytes`, `archive.sha256`, `archive.manifest_sha256`, `backups.drive.object_id`, `backups.dropbox.path`를 실제 값으로 해석한다. 이 문자열들은 **receipt field reference**이며 SHA의 대체값이 아니다. Core 안에 나중의 publication SHA를 넣는 hash cycle을 만들지 않는다. Branch가 이동해도 receipt에 고정된 commit의 package를 사용한다.

Git source가 이미 같은 identity로 있으면 전체 ZIP을 다시 받지 않는다. ZIP이 필요하면 동일 SHA cache 또는 두 백업 중 접근 가능한 하나에서 한 번 복구하고 bytes/SHA/MANIFEST를 확인한다. 다른 백업의 upload ACK, metadata identity, 실제 restore는 서로 다른 증거다. 사용하지 않은 경로를 이번 실행에서 restore했다고 기록하지 않는다. 하나가 막히면 다른 동일 identity 경로로 계속한다. 모두 막히면 구체적인 누락 identity와 실패를 남기고 가능한 구현을 계속하되, 없는 source나 결과를 추정하지 않는다.

별도 표시가 없으면 아래 읽기 경로는 **복구한 PHYS07 package root에 상대적**이고, 새 산출물 경로는 **새 NCP package root에 상대적**이다.

읽기 순서:

1. `SCIENTIFIC_CONTRACT.md`, `REPORT_KO.md`, `review/DECISION.json`, 현재 claim/blocker ledger, 이 인계의 JSON 두 개.
2. `theory/SOURCE_C2_DOMAIN_KO.md`, `theory/REFERENCE_ROOT_THEOREM_KO.md`, `results/SOURCE_ANALYSIS.json`, 두 `results/{full,first_half}/run_summary.json` 및 필요한 원 export.
3. `inputs/SOURCE_PORT_LEAF_MAPPING.json`, `inputs/ARCHIVED_COMMON_SEED_POINT_INPUT.json`, `inputs/ncp_phys06/SOURCE_INTAKE_KO.md`, `inputs/ncp_phys06/SOURCE_BOUNDARY_AND_CHART_KO.md`, `inputs/ncp_phys06/SOURCE_INTAKE_MANIFEST.json`.
4. `inputs/ncp_phys06/delivery/NCP_RETURN_FINAL.json`, `inputs/ncp_phys06/review/DECISION.json`, `inputs/ncp_phys06/evidence/BUILD_PINS.json`, `inputs/ncp_phys06/evidence/FAILURES_AND_CORRECTIONS.json`, `inputs/ncp_phys06/evidence/RUN_LEDGER.jsonl`과 아래 지정한 실제 코드. 이 inherited NCP 판정은 1번의 현재 PHYS07 `review/DECISION.json`과 다른 기록이다.
5. 현재 repository의 `AGENTS.md` 및 두 Astra v4 하네스의 `START_HERE.md`, coding `AGENTS.md`, research `PROJECT_INSTRUCTIONS.md`, 관련 `docs/MODEL_ROUTING.md`와 현재 task contract. 이미 검사된 하네스 패키지 검사를 다시 실행하지 않는다.

`harness/physmath-research-harness-gpt6-astra-v4.0.0-20260908.zip`과 `harness/physmath-coding-harness-gpt6-astra-v4.0.0-20260908.zip`가 포함되어 있다. 현재 인계를 작성한 host raw label은 `GPT-6 Astra Pro`다. NCP에서는 **실제 표시된 raw model label**, 사용한 family/harness/version, routing 판단 근거와 지침 읽기 receipt를 따로 기록한다. Raw `Pro` suffix가 프로그램의 등록 alias와 자동 일치한다고 주장하거나 모델을 바꾸지 않는다. 하네스 이름은 runtime attestation이 아니며, 실제 관측하지 못한 runtime model ID는 null이다.

## 2. 최신 NCP 기준선과 보호할 상태

| 항목 | 고정 identity |
|---|---|
| 최신 NCP branch | `codex/hh-phys06-ncp-20261011` |
| 시작 head | `65a36e255aa6d9911e23a9b5ced18d8a9f507606` |
| 시작 tree | `f823df8c95defcaba737139859cd9eeeda4ef133` |
| 구현 core | `927019cff541e8a4a1f0d2c8846f1466d6b70533` |
| 구현 core tree | `f156e72d5e58d4c6efa840606af28e43aa014e6f` |
| 이전 NCP dossier | `research/r31ao_unequal_ladder/ncp_phys06_local_20261011_v1/` |
| 이전 전체 source SHA256 | `26a7136322696aaf1dd65a13987d437ee8dfd86ed8967e6db1a224d828fb01f6` |
| 이전 candidate source SHA256 | `14b1d1e76f54175069020fb49568f8a3c16571620fd69a532afaed73bb34a207` |
| 이전 ABI SHA256 | `149b59c50ceec2a7d6c1beef54490181dd4aeefaa473e356810abd02133f2ea9` |
| 이전 최종 build binary SHA256 | `36bc9ad2f95d214d1a0b1abe4fd44623c5dd1aea6e1e67cbc3eb28c9bd12363d` |
| COMMON seed SHA256 / bytes | `678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b` / `108416` |

이전 binary pin은 마지막 build에서만 관측됐다. 이전의 모든 target이 그 binary에서 통과했다고 소급하지 않는다. 최종 observable-gradient 수정 뒤의 과거 target 재실행은 미측정으로 남아 있다. 이번에 새 소스를 변경하면 새 source/candidate/ABI/compiler/flags/binary identity를 실제로 기록하고, 각 첫 target 직전에 해당 binary를 pin한다. 나중의 build hash로 앞선 실행을 덮지 않는다.

이전 NCP fallback ZIP은 `WU088_HH_PHYS06_NCP_LOCAL_20261011_v1_sha_f4ca1d216962.zip`, SHA256 `f4ca1d2169628dfdb4966de27435f8f32d804193dada62468a1611cc6bef12ad`, 4,005,923 bytes다. Drive object ID는 `1AcrHu25VfLsxIoeIsRZgyq8wl-8vMP8t`, Dropbox ID는 `id:BSpOijBcT10AAAAAAD3_Rw`다. 이 복구 정보는 현재 PHYS07 ZIP identity와 다르다.

시작 head에서 사용자 작업을 보호하는 isolated worktree를 만들고 새 branch `codex/hh-phys07-ncp-20261011`, 새 directory `research/r31ao_unequal_ladder/ncp_phys07_local_20261011_v1/`에만 additive 작업을 한다. 동명 branch가 이미 있으면 지우거나 reset하지 말고 실제 head와 task identity를 비교한 뒤 같은 실행을 이어가거나 충돌을 기록한다. 기존 dossier, archive, receipts, 원 scientific arrays는 수정하지 않는다. 최신 PHYS06 구현을 버리고 v2/원 owner로 돌아가지 않는다.

완료된 PHYS06 adapter와 여섯 target/한 fixture recheck, v2 receipt와 189-slot oracle, PHYS04 remap/quartic, PHYS05 18,817 checks, FD1/FD2/6-cell/G256, seed/receipt/하네스 진단 및 이번 PHYS07 Python reference는 **증거를 읽어 상속**한다. 새 source producer를 만드는 데 필요한 COMMON 입력 준비는 허용되지만, decode/encode 자체를 새 연구 target으로 반복하지 않는다. `CommonFamily::initialize`에 내장된 1회 decode/roundtrip 검사는 실제 필요한 입력 준비로 기록한다.

COMMON에는 과거 HH ON 이력이 남아 있다. 미래 `lambda=0`, `b=0`은 그 이력, old gas/photon/guard, 보상합 또는 과거 HH ledger를 지우지 않는다. 기존 admission `24/289`, unbounded `265`, epsilon_C/R=null, B22 OPEN, canonical S0 OFF, ON06G 256-macro prefix `t=3.2e11 s`, physical/production HOLD는 이번 source 산술의 PASS로 바뀌지 않는다.

## 3. 이번 PHYS07 연구 결과를 비교 근거로 사용한다

PHYS07은 고정 reference scalar leaves와 **isotropic analytic transport reference family**에 대해 whole gas box와 whole `Theta=[0,1]^2`를 계산했다. 최종 독립 판정이 허용한 범위는 package의 `review/DECISION.json`을 따른다. 저장된 `results/SOURCE_ANALYSIS.json`은 두 stage에서 엄격한 Banach 포함과 reference root derivative/rectangle interaction을 기록한다. 표시용 수축 상한은 full 약 `0.0011531881192975576`, first-half 약 `0.0005772958701028138`이다. Reference의 HII mixed response는 음수, thermal w 및 temperature mixed response는 양수인 포함이 얻어졌고 energy projection의 부호는 0을 가로질러 OPEN이다. 이 숫자의 인증 endpoint는 JSON의 rational endpoint이며 `display_float`가 아니다.

그 결과는 **고정된 reference residual의 첫 단계 root**에 대한 수학적 결과다. NCP native libm, 실제 방향 leaf, widened source weights, PreBE tuple, rounded point execution, carried second-half와의 동일성은 아직 확인 대상이다. 연구자가 사용한 gas point/방향별 point-stock exact sum을 `CommonFamily::initialize`의 **stored interval boxes**와 같은 입력이라고 쓰지 않는다. NCP의 source bound는 실제로 전달한 frozen interval inputs와 native leaves에 대해 명시한다. Archived point가 그 interval에 들어가는지 확인하면 그 포함 관계를 기록할 수 있지만, 이것은 tuple의 bitwise equality가 아니다.

NCP에서 reference를 다시 계산하거나 Python 결과로 native field를 채우지 않는다. 같은 변수·단위·leaf·input scope가 확인된 항목만 비교한다. Native scalar leaf의 bit equality, native interval이 reference interval 전체를 포함하는지, 두 결과가 단순히 overlap하는지, 서로 다른 coefficient-family를 bound하는지를 별도 필드로 남긴다. Overlap만으로 정확한 enclosure나 동일성을 확정하지 않는다.

## 4. source producer의 정확한 입력과 호출 흐름

### 4.1 고정 입력

| 항목 | 계약 |
|---|---|
| Gas coordinate | `g=(x_HII,y_HeII,y_HeIII,w_eV_per_H)` |
| Exact decimal gas box | `[.90,.93] × [.29,.31] × [.59,.61] × [13,14]` |
| Parameter rectangle | `lambda,b ∈ [0,1]`, 전체 영역 |
| COMMON clock | `t0=1.6e11 s`, archived clock bits와 일치 |
| Hubble triplet | `(1e-14,1e-14,1e-14) s^-1`, source binary64 leaves |
| Full first stage | `dt=1.25e9 s`, COMMON에서 출발 |
| First-half stage | `dt=6.25e8 s`, 같은 COMMON에서 출발 |
| Grid | 33 energy nodes, 128 directions, 4,224 directional photons, guard N/U 각각 128 |
| Jet slots | 0–3 gas, 4 lambda, 5 b, 6 unused; 7-vector gradient와 7×7 Hessian 보존 |

Exact decimal endpoint는 유리수다. 예를 들어 `.90`을 nearest f64 하나로 저장한 뒤 exact lower라고 간주하지 않는다. 각 rational lower/upper를 outward binary64로 변환하고 numerator/denominator, hex/bits와 포함 근거를 기록한다. Fixed gas center와 양의 radius는 실행 전에 고정한다. Existing `UniformData`가 검사하는 outward `center±radius`가 source의 frozen X 안에 들어가도록 한다. 몇 ulp의 추가 enclosure가 필요하면 **첫 source 호출 전에** 확장된 X와 rational reference X의 포함 관계를 기록한다. 결과를 본 뒤 X/radius/Theta를 바꿔 같은 첫 실행으로 재분류하지 않는다.

### 4.2 두 stage에서 각각 한 번의 PreBE와 두 번의 residual

새 CLI target `phys07_sourcebox_full_first`, `phys07_sourcebox_first_half_first`를 만들고 순차 실행한다. 각 target의 내부 순서는 다음과 같다.

1. Frozen COMMON, config, source/build identity, X/Theta, 좌표 tag와 runtime resource preflight를 검사한다. 기존 initializer의 stored interval gas/photon/guard Jets를 사용하고 historical/primal compensation을 보존한다. 초기 미래 미분이 0이라는 근거를 old history=0으로 혼동하지 않는다.
2. `candidate/src/phys04_transport.rs::phys04_prepare_family`를 **1회** 호출한다. `b`는 slot 5의 `Jet::variable([0,1],5)`다. Clock/Hubble/config는 고정한다. 반환한 `Phys04PreBE`에 `validate_family_input`을 호출하여 동일 call-frame, output words와 source bytes를 확인한다. 별도 가짜 PreBE나 public issuer를 만들지 않는다.
3. `candidate/src/phys04_mixed.rs::phys04_reduced_residual`을 **whole X×Theta에서 1회** 호출한다. Old gas는 위 고정 COMMON Jet, trial gas는 slot 0–3 변수, lambda는 slot 4 변수, incoming은 **방금 PreBE의 `groups` Jets**, energies/stage/dt도 같은 PreBE의 값이다. 4,224 directional photons를 그대로 33개 group 대신 넣거나 archived primary packets로 치환하지 않는다.
4. 같은 source·old input·PreBE를 사용해 **fixed gas center×whole Theta에서 1회** 더 호출한다. Gas center Jets도 gas 미분 슬롯은 유지하며 value만 고정한다. Lambda와 incoming Jets를 parameter center로 줄이지 않는다. 이 결과가 `[G(g_c,Theta)]`이며 같은 export의 gas-gradient interval midpoint를 고정 preconditioner용 대표행렬로 사용할 수 있다. 그 midpoint는 실제 theta-center Jacobian을 별도로 계산했다는 뜻이 아니다.
5. 이 두 export를 재사용해 C² 근거, native leaf 비교, energy projection, `UniformData` 및 source-directional witness를 만든다. 추가 source/provider/rate callback을 호출하지 않는다. Source/PreBE 실패 시 이미 쓴 호출량과 첫 오류를 저장하고 해당 stage를 OPEN으로 반환한다.

`phys04_mixed_at_box` 또는 기존 `certificate::export_derivatives` 경로는 이 producer의 shortcut으로 쓰지 않는다. 그 경로는 residual을 네 번 호출하고 U/V/W 후보 선행 문제를 만들기 때문이다. New source-box type은 실제 PreBE/직접 residual 결과에서만 생성하고, 기존 generic uniform arithmetic에 넘길 데이터 생성 권한만 가진다. Private `Phys04ExactPermit`, `NativePointCertificate`, `NativeFamilyTube`, `NativeUniformCertificate`를 발행하는 기능을 추가하지 않는다. 기존 `phys04_native_dispatch_requested()`의 거부를 우회하여 다른 public endpoint를 호출해서도 안 된다.

## 5. 여섯 작업의 구현·완료 기준

### T01 — Intake와 isolated additive 작업

실제 PHYS07 receipt/commit/tree/manifest, 위 NCP base, COMMON, inherited completion/failure를 읽고 `evidence/INTAKE.json`과 source diff 기준선을 만든다. 새 repository/source/build identity를 historical pin과 구분한다. `NCP_TASKS.json`의 계획과 실제 실행 ledger를 연결한다. 시작 전 model/routing receipt와 resource preflight를 저장한다.

### T02 — Native leaf·source tuple·기존 history 연결

Public source call에서 실제 사용한 nH, stored nHe, fHe, Hmean, source time/dt, c/kB/eV, CHI, 33 energy nodes와 99 sigma leaves, heat leaf `fl(E-CHI)`, source `fl(dt*SOURCE)`, 방향별 geometry/hat/guard branch와 birth weights를 기록한다. Provider/HH-rate를 다시 호출해 기록용 값을 만들지 않는다. 현재 `Phys04DerivativeExport`는 sigma와 별도 q Jet을 노출하지 않으므로 **새 candidate copy에서 이미 계산한 sigma/q를 metadata로 복사하는 최소 변경**이 가능하다. 원 수식·연산 순서·leaf 생성은 보존하고 ABI/source 변경을 pin한다. Transport trace도 기존 call-site에서 수집하며, trace를 위해 두 번째 PreBE/geometry pass를 만들지 않는다.

PreBE의 input/output 전 word와 signed value/gradient/Hessian을 손실 없이 저장한다. Compact binary/형태가 명시된 배열을 써서 출력 budget을 지킬 수 있다. 숨겨진 private seal을 외부에서 재구성하는 대신 기존 validator가 성공한 그 객체와 실행 identity를 묶는다. 생성 경로를 증명하는 evidence와 bytes hash를 구별한다. Scalar libm leaves와 interval exp/log의 finite-remainder path도 따로 기록한다. Native `powf/exp/sqrt` 값이 correctly rounded reference leaf와 다르면 차이를 그대로 보존하고 native leaf 기준의 범위를 명시한다.

`CommonFamily.physical`의 archived point와 stored box 입력, old HH/primal compensation, 새 미분 ledger의 대응표를 작성한다. `FamilyIdentity.theta_bits:[u64;3]`는 Hubble triplet이며 lambda/b rectangle이 아니다. Zero stock의 signed b derivative를 제거하지 않고, 미래 amplitude 0을 과거 OFF 상태로 바꾸지 않는다.

### T03 — 실제 C² 영역 predicate와 branch 근거

다음을 검증한 **source-specific domain evidence**를 생성한다. `Domain::Regularity`의 문자열이나 true flag 자체는 이 evidence를 대신하지 않는다.

\[
\widehat f=\operatorname{exact}(n_{He}^{stored})/\operatorname{exact}(n_H^{stored}),\quad
p=1+\widehat f+x+\widehat f(y_1+2y_2),\quad
T=\frac{2\epsilon_{eV}}{3k_B}\frac{w}{p}.
\]

전체 X에서 strict FT03 simplex, `w>0`, `p>0`, HH `35000≤T≤60000 K`와 FT03 `30000≤T≤110000 K`, 모든 `D_j=1+dt*kappa_j>0`, nonnegative physical incoming을 확인한다. Source는 lambda=0에서도 HH Jet을 평가하므로 그때도 HH temperature guard가 필요하다. Paired temperature guard의 blanket은 `FHE*(1-8*EPSILON)`과 `FHE*(1+8*EPSILON)`을 source 순서로 계산한 **각 binary64 rounded endpoint**다. 이 실제 interval이 stored density ratio를 포함하는지도 기록한다.

예비 open gas witness는 `(0.899,0.931)×(0.289,0.311)×(0.589,0.611)×(12.9,14.1)`다. Actual native leaves로 이웃 영역의 단조 corner temperature/particle/simplex 여유를 source 재호출 없이 확인한다. Parameter rectangle 경계에는 affine/rational source의 작은 열린 연장을 수학적으로 설명한다. 그 연장을 음수 photon이나 `[0,1]` 밖의 amplitude를 native 함수에 넣는 실행 절차로 사용하지 않는다.

Fixed energy와 fixed geometry의 threshold/hat 분기, `min/max`, `widened`, physical-value `nonneg`의 역할을 분리한다. Interval endpoint를 clip하는 프로그램 전체가 C²라고 하지 않는다. 미분 대상은 고정된 coefficient chart의 real source이며 positivity intersection은 물리값 enclosure를 좁히는 단계다. Tangent/Hessian에는 clamp를 적용하지 않는다. Guard/hat crossing을 발견하면 실제 node/ray/coefficient interval을 남긴다. Lambda/b subdivision은 geometry coefficient를 바꾸지 않으므로 그 실패의 일반적 해결책으로 사용하지 않는다.

`w`와 `e=w+chiH*x+f*chiI*y1+f*(chiI+chiII)*y2`를 다른 coordinate tag로 관리한다. Existing `Domain.x[3]`은 thermal w다. Energy-box를 쓰려면 `w=e-beta·z`의 pullback과 연관된 domain을 따로 증명한다. 이번 기본 producer는 gas X를 유지한다.

### T04 — Whole-source export와 기존 uniform adapter 연결

한 실행에 묶인 export에 다음을 담는다: `Gc`, `A=G_g`, `G_lambda`, `G_b`, `G_lambdab`, `G_g,lambda`, `G_g,b`, 네 residual component의 `G_gg`, whole-domain photons/denominators, old/preBE signed Jets, source/leaf/clock/seed/carry identity, C² evidence. 전체 7-slot Jet을 원형으로 보존하고 adapter가 쓰는 4+2 슬롯 mapping을 별도로 명시한다.

Existing PHYS06 `energy.rs`로 `ell*G`, S/Q pullback 및 Jnorm/Psi를 계산한다. Source의 `f`와 `widehat f`를 동일하게 치환하거나 heat leaf를 exact subtraction으로 바꾸지 않는다. Energy row의 algebraic cancellation과 실제 interval width는 다르다.

Existing `uniform::{Domain,Partials,UniformData,FixedC,root_arithmetic}`를 재사용한다. Fixed C는 위 center export에서 고정한 대표 Jacobian으로 한 번 만든다. 새 source-bound factory가 actual source/domain evidence를 검증한 뒤에만 `UniformData`를 제공한다. 기존 adapter의 `WholeSourceEnclosure::Unresolved`를 boolean 또는 JSON import만으로 resolved로 바꾸지 않는다. Serialization은 evidence를 보관하며 native 권한을 발급하지 않는다.

각 stage에서 `root_arithmetic`을 **최대 1회** 호출하여 `B`, `beta`, radius, q, strict margins를 보관할 수 있다. 이는 supplied interval에 대한 source-bound **조건부 포함 산술**이며 native solver/certificate producer가 아니다. 실제 source enclosure·C² 연결에 미해결 전제가 있으면 판정에도 남긴다. Root inclusion이 실패해도 source export는 보존하고 margin 실패를 있는 그대로 반환한다. U/V/W를 얻기 위한 새로운 nonlinear solve, tangent candidate search, Neumann iteration 또는 finite/paired target을 추가하지 않는다. 이번 두 first stages의 native U/V/W/I 및 carried second-half는 계속 null이다.

### T05 — Native leaves를 사용한 HH–광자 방향미분 witness

각 stage의 실제 PreBE birth derivative를 photon amount로 `M_j=partial_b N_j`라 정의한다. Reference에서는 `M=exact(fl(dt*SOURCE))`가 node 24에 들어갔지만 native widened weights의 group 합이 그 값과 bitwise 같다고 가정하지 않는다. Effective rate를 원하면 `B_dt=M/dt`로 별도 정의한다. Source의 finite birth leaf를 exact `dt*5e-15`로 바꾸거나 dt를 두 번 곱하지 않는다.

Whole-X export의 q와 `H=(q,0,0,-chiH*q)`, photo b derivative `P_M=Σ M_j K_j/D_j`를 재사용하면 first-COMMON source에는

\[
G_\lambda=-dt\,H,\quad G_b=-dt\,P_M,\quad
G_{\lambda b}=0,\quad G_{g\lambda}=-dt\,H_g,\quad G_{gb}=-dt\,(P_M)_g
\]

라는 source identity가 있다. Algebraic exact zero와 outward interval이 0을 포함한다는 결과를 따로 저장한다. Jet을 고치거나 작은 항을 지워 zero-width equality를 만들지 않는다.

Source directional outputs는 `H_g P_M`와 `(P_M)_g H`다. 필요하면 이들을 dt로 나눈 rate convention도 단위를 붙여 기록한다. 캡처된 q, sigma, T, p, heat leaves와 denominator로 직접 해석식과 Jet contraction을 비교한다. Source callback이나 finite difference를 추가하지 않는다. HI-only birth에서 `a=fl(E-chiH)`, `A_j=c*nH*sigma_Hj`, `u=1-x`, `nu=1.2+157800/T`, `Xi=u*nu/p*(1-a*p/w)`이면

\[
(H_gP_M)_x=-q\sum_j A_jM_j(2+\Xi_j)/D_j,\quad
((P_M)_gH)_x=-q\sum_j A_jM_j/D_j^2.
\]

Active support와 `a*p<w`를 native export에서 확인한 범위에만 부호를 붙인다. HH는 thermal w와 T를 내리고, 낮은 excess-energy photo event는 w를 올리면서 입자 수 증가로 T를 내릴 수 있다. 이것은 source directional mechanism이다. 실제 implicit mixed W와 동일하지 않으며, reference W_T>0와도 모순되지 않는다. Energy projection은 `ell H_gP_M=0` 및 `ell(P_M)_gH=-q Σ(chiH+a) A_j M_j/D_j²`를 사용하고, 일반 leaf의 `chiH+a=E+epsilon`을 보존한다. Energy W의 음수나 finite full/two-half defect를 이 witness에서 추정하지 않는다.

### T06 — 독립 판정·실제 return·두 백업

후보 코드/이론/테스트를 만든 사람이 아닌 reviewer 한 명이 실제 diff, first logs, identity, domain proof, source interval 의미, 출력과 claim ceiling을 읽어 판정한다. Self-review나 agent 호출 횟수를 독립성으로 표시하지 않는다. Reviewer는 이번 source callback budget을 자동으로 늘리지 않고 과거 suite를 재실행하지 않는다. 실제 결함은 승인된 범위와 남은 예산 안에서 고친다. Source execution 뒤 수정한 파일이 결과에 영향을 주면 해당 결과를 새 코드의 검증으로 소급하지 않는다. Source 재호출 예산이 없으면 그 항목을 `NOT_EVALUATED_AFTER_CHANGE`/OPEN으로 정직하게 반환한다.

`NCP_RETURN.json`, `RETURN_KO.md`, `NEXT_HANDOFF_KO.md`, `CLAIM_LEDGER.json`, `BLOCKERS.json`, `MANIFEST.json`, source/build/input manifests, ordered `evidence/RUN_LEDGER.jsonl`, 모든 first stdout/stderr/exit/resource record, review decision을 새 NCP package에 저장한다. 원 파일을 보존하며 additive commit하고 새 ZIP 및 detached delivery receipt를 만든다. 기존 두 백업 폴더에 package뿐 아니라 START·handoff·tasks·return·receipt 등 다음 사람이 필요한 전달파일도 새 이름으로 올린다. 사용자에게 추가 첨부를 요구하지 않는 START를 제공한다.

Upload ACK, 서버가 보고한 bytes/hash/ID, 다운로드한 bytes의 검증, 전체 restore 실행을 각각 기록한다. 이전 NCP가 수행한 dual restore를 이번 PHYS07 NCP restore라고 쓰지 않는다. Git core/package와 delivery receipt의 self-hash cycle을 피한다. 나중에 완성된 publication/backup 상태는 detached receipt와 delivery return에 실제 값으로 기록한다. 자동 승인 검토가 특정 쓰기를 거부하면 그 action/reason을 보존하고 사용 가능한 승인된 다른 경로를 완료한다.

## 6. 실행 ceiling과 사전 고정할 run ledger

| 종류 | 이번 NCP 계약 |
|---|---|
| 새 stage first targets | `phys07_sourcebox_full_first`, `phys07_sourcebox_first_half_first`, 각 1회, 순차 |
| `phys04_prepare_family` | stage당 1회, 전체 2회 이하 |
| `phys04_reduced_residual` | stage당 2회, 전체 4회 이하; 실패한 진입도 센다 |
| Transitive FT03 RHS / HH Jet | 각각 전체 4회 이하, 위 direct residual 안에서만 |
| AtomicProvider channel evaluation | 33×3×4 = 전체 396회 이하, 위 residual 안에서만; 별도 provider/atomic diagnostic 0 |
| `uniform::root_arithmetic` | stage당 최대 1회, 전체 2회 이하; 조건부 산술이며 native authority=false |
| `phys04_mixed_at_box`, uniform linear/mixed/finite/paired 새 실행 | 0 |
| Native endpoint / conservative point / internal point / nonlinear root or native certificate producer / IVP / heavy atomic / old suite | 각각 0 |
| Stage invocation 자원 | wall 60 s, address space 512 MiB, output/artifacts 합계 32 MiB, CPU 1 core, 동시 1, swap 0 |
| 변경 코드 build | 최대 3회: 최초 1회와 구체적인 compile 결함 수정 최대 2회; 각 wall 300 s, memory 512 MiB, output 32 MiB, CPU 1 core, 동시 1, swap 0 |
| Build mode | 기존 toolchain, offline/locked, `CARGO_BUILD_JOBS=1`; toolchain/dependency 설치 또는 broad workspace build 0 |
| Source 재실행 | 추가 allowance 0. 첫 실패를 보존하고 남아 있는 미실행 target만 진행한다. 새 input/box/parameter sweep 0 |

새 source CLI와 실행 wrapper를 먼저 구현하고 preflight를 완료한다. NCP wrapper는 exact command vector, cwd, run ID, child/process group, 시간/주소공간/출력 제한, 전후 source/input/binary hash, counters를 기록하고 초과 시 해당 process group을 종료해야 한다. 연구 package의 Python 전용 `tools/run_bounded.py`를 Rust 실행기로 잘못 호출하거나 기존 hard ceiling을 수정해서 권한을 늘리지 않는다. Address-space limit과 cgroup RSS/memory/swap/CPU enforcement를 구분하고, 실제 호스트에서 적용된 제한만 attested로 기록한다. 필요한 cap을 적용할 수 없으면 source dispatch 전에 그 target을 BLOCKED로 둔다.

Build의 prospective command는 새 NCP package에서 `cargo build --offline --locked --jobs 1 --bin hh_phys07_sourcebox`다. 새 CLI는 full/first-half 중 하나의 고정 task ID와 frozen contract를 받아 위 호출 순서만 실행하도록 만든다. 실제로 만든 path/arguments/executable SHA를 preflight와 run ledger에 적는다. 이미 실행 중인 legacy runner, default `cargo test`, 기존 suite를 wrapper의 preflight로 호출하지 않는다.

기존 `phys04_native_counts()`의 `[endpoint,conservative,internal_point,root]`, `phys04_arithmetic_counts()`의 `[derivative,source_rhs,linear]`, uniform arithmetic counts를 target 직전/직후 읽어 delta를 남긴다. 계측이 없는 항목은 dispatch log와 정적 callgraph 근거를 따로 기록하고 measured counter는 null로 둔다. Ceiling 0을 관측값 0의 근거로 사용하지 않는다. PreBE/HH/provider의 진입 수는 새 wrapper 또는 기존 호출 지점에 최소 계측을 추가해 보존한다. 모든 first failure/timeout/출력 제한 실패는 원 stdout/stderr와 함께 남기며 PASS로 덮지 않는다.

## 7. 완료와 남는 claim ceiling

완료는 실제 source-specific producer, C² evidence, 두 stage의 가능한 범위 내 최초 source exports, 기존 adapter 연결, native-leaf source witness, 독립 판정과 완전한 복구 가능한 전달물이다. 조건부 산술의 엄격한 margin이 안 닫혀도 source export와 실패 근거는 반환하고 task별 scope를 구분한다. Source/leaf/derivative enclosure의 참됨이 확인되지 않은 경우에는 object가 생성됐다는 사실만으로 whole-source certification을 채택하지 않는다.

Actual native root/tube/U/V/W/I, full-versus-two-half defect, second-half carried family, gas/time/continuous-source remainder는 이번 반환에서 null이다. PHYS07 reference theorem은 그 이름과 residual/input scope로만 상속한다. 기존 `NCP_RETURN_FINAL.json`의 `next_proposal_not_executed`는 미실행 proposal로 보존하고 `request_ready=false`, authorization=null을 유지한다. 이번 source 산술 허용량은 그 endpoint 제안을 실행할 권한이 아니다.

새 local Codex는 계획만 답하지 말고 T01–T06을 가능한 acceptance까지 수행하고, concrete limitation·actual evidence·delivery identities가 들어 있는 `NCP_RETURN.json`과 한국어 반환문을 완성하라. 이미 승인된 Git/Drive/Dropbox 전달과 가역적 코드 작업에는 단계별 재확인을 끼워 넣지 않는다. 별도 권한이 실제로 필요한 경계에 이르면 그 전까지의 산출물을 완성하고 정확히 어떤 action과 어떤 규칙이 막았는지 반환한다.
