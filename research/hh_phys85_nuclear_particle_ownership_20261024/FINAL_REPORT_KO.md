# PHYS85: thermal/fast 핵입자 소유권 — 이론·정적 구현 수용, 실행 결과 미검증

## 1. 현재 결론

PHYS85는 PHYS81의 radiative-capture photon/recoil 사건을 **같은 normal frame의 thermal/fast 입자수와 에너지 소유권**에 연결했다. 세 bare-ground capture 채널의 정확 사건 장부와, 비상대론적 공통-T Maxwellian에서 반응에 선택된 운동에너지 제거 정리를 유도했다. 독립 이론 검토는 PASS_SCOPED, 수정 후 구현의 정적 검토도 PASS_SCOPED다.

새 Wolfram exact reference의 **완전한 실행 결과는 검증하지 못했다**. 초기 호출은 namespace entrypoint 연결 실패였고, 계약에 허용된 한 번의 수정 호출은 응답 중간이 실제로 생략되어 온전한 JSON이 없었다. visible PASS/guard23/failures[]는 문자열 조각이다. 계획36event/6ensemble과 전체 assertions를 실제 완료 수로 쓰지 않는다. 유효한 완료 reference application0, completed science identity=null, 남은 추가 호출0이다.

Evidence identity는 `d78adc5c293c28d2032a8a391ee317988390f504884847e79da4d1635ad024af`다. 이는 동결 입력·코드·두 원응답·실패 기록을 결속하는 audit identity이며 완료 과학 identity가 아니다. 정확한 descriptor와 canonical JSON hash 규칙은 `results/EVIDENCE_IDENTITY.json`에 있다.

실제 물리 핵반응률, fast-product stopping, coupled thermal/xe/metric trajectory는 이번 단위에 없다. HH_R10=OFF, production admission NOT_ISSUED다.

## 2. PHYS82 이후 owner와 실제 부모

고정 중앙 인계 `rei_bianchi@0f9d9df825be1dac9ca9bdf73cdc2e8908bcba17:research/orchestration_longterm_20261023/assembly/HANDOFF_WU088_HH_KO.md`를 기준으로 최신 owner를 확인했다. 첫 노드 WU_CE83_OWNER_COMPLETION은 이미 PHYS83에서 완료됐다. 과거 PHYS82 S2만 checkout하지 않고, PHYS83/84를 포함한 실제 원격 descendant에서 진행했다.

| 근거 | 실제 identity와 처리 |
|---|---|
| PHYS82 최종 | ca9d53983459ea08f9992a8a24663e46b7180344; CSV CRLF 원본 복구가 포함된 최종 계보 유지 |
| PHYS83 owner 완료 | 6a2fc5aacb6182a916b9434c316e99e750e8273c / PR140; science e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c |
| PHYS83 저장 결과 | rate132, steady324, transient732;71cases,2111assertions; 완료1,실패0; 실제 resume1skip/0callback — 전부 재사용 |
| 실제 PHYS85 부모 | PR141 d5c2c8dbbbd77bc81526dda6e74df534fba3c4e5, tree41f951c872735c1d8d6cb5ea8162b74538bc8198 |
| PHYS84 prepared identity | dca969a27fa00a703efb4c9f341efb5e50b45b2d88f5896a66f2c4aeced0a0db; science 완료가 아님 |
| PHYS84 사전 바이트 확인 | prepared8/8, parent pins5/5 일치; 새 wrapper/child/application/resume0 |
| PHYS84 자원 | 기존 reserve1.5GiB+job0.5GiB를 유지. 최종 원시 메모리 여유0.1411361694GiB로 조건2GiB 미달; RESOURCE_WAIT_03 |

부모 PHYS84 final ZIP(7,891,881bytes, SHA256 dd68666ae61b202c21d9bff502bf9972d06926159018eb703c5518c4fff038cc)과 final JSON(307,868bytes, SHA256 5bc989c1549eb4473b99cb6d3cc3502e98dc18ca561988e8f6d23d7c409f8395)을 살아 있던 원본 bytes에서 복구·대조했다. 과거 양쪽 전체복원 CRC127/payload126/Git89/extract127 및8/5pins PASS는 과거 근거로 재사용한다. 이번에 부모 provider를 다시 다운로드했다고 주장하지 않는다.

## 3. 조사 범위와 최신 병렬 결과

이번 intake는 접근 가능한 owner repository metadata51개 pagination 완료, 관련6repo의 전체 branch refs1106개, 최근 PR metadata30개, 수정 시각 delta, 선택한 AGENTS/계약/보고서/백업 및 접근 가능한 Personal Context를 대상으로 했다. 6repo refs는 WU150, REI263, REC149, HE98, CR177, BASS269다. 과거51repo/2175branch inventory는 별도 과거 근거로 재사용했고 이번1106과 합산하지 않는다. 모든 branch의 파일 내용을 읽었다거나 접근 불가능한 비공개 대화까지 조사했다는 주장은 하지 않는다.

알려진 WU Drive527/Dropbox496 entries와 Dropbox dossier3396 entries/6pages 및 관련 폴더 범위는 terminal pagination을 확인했다. 넓은 Drive dossier 조회는1000 cap으로 전체 소진이 아니었다. 검색 필터가 오래된 결과를 반환한 Dropbox 검색은 전수성의 근거로 사용하지 않았다. 외부 과거 완료를 복원하려고 과학 실행을 다시 하지 않았다. BASS B3a 준비 문서와 VIGILODEV1Q 새 archive metadata도 실제 접근 범위대로 기록했다.

마지막 확인은 known PR6개와 최신 top1 검색6개 후, 실제 변경·신규 PR에 대해 추가28 calls(PR4, compare6, selected files18)를 수행했다. 선택18파일의 UTF-8 bytes에서 계산한 Git blob identity가 provider blob과 일치했다. 전체 원응답은 최종 ZIP의 private/intake에, 공개 가능한 요약은 intake/final_delta에 보존한다. 자세한 시각·actual HEAD는 해당 manifest가 권위다.

| 최신 owner evidence | 이번에 종합한 결과 | 닫히지 않은 의무 |
|---|---|---|
| REI PR222 6cf7c53757ce4049046a3463c57f36bece555830 | 병렬 HE·CR return과 중앙 DAG 변경을 관측. WU 고정 handoff와 AGENTS는 비교 범위에서 변경 없음 | 중앙 authority 파일은 수정하지 않고 WU 반환 overlay 제공 |
| CR C23D 중앙 return, science d04b2a56adb4a5d55b901420aa544332b41f6dbb / PR99 | prescribed Maxwellian electron bath의 low10eV EE bridge. owner의 새 trajectories4 중 admission3, 추가1은 admission basis 아님 | 전체 stopping, neutral/ion/inelastic, finite bath, nuclear fast stopping은 OPEN. Library/Dropbox R3, Drive UNKNOWN_NO_ACK 유지 |
| CR C23E PR100 8e4e06361d714939513a11f64a27f02822bde2fa | 조건부 D43K PI/RR/CX source 결속.104checks,18states,3new D quad,9band orders; old H source 재실행0 | empirical isotope-resolved D source·finite-mass/level·Milne 및 full21 coverage OPEN. WU_D_PI_RR_MATCHED의 조건부 선행 근거로 채택하며 부모 전체를 닫지 않음 |
| REC ADM01 PR131 c7cdabd871ab2ef6f722594ff063b8ce8550e6b4 | 입력 도메인 scoped admission.386primary+3independent probes라는 owner 근거 채택. U5의313/313 query coverage와 producer/target parameter 차이를 구분 | H5 INPUT_DEPENDENT_UNCALIBRATED, REC-HISTORY PARTIAL. 원1252상세rows 등 미복구; exact SUMMARY는 복구. Dropbox whole-byte/CRC/payload84 PASS, Drive ACK 없음 |
| HE HEX PR93 bf3c21a39b1111497ed77667d05b8a853ffe6646 | source catalogue intake scoped 완료와 최신 dual archive ACK 확인 | 양쪽 ACK는 전체 원격 bytes 복원 인증이 아님 |
| HE DDCS20 PR94 d8bae9f7e24ad3494e399f7ab46c4167a5623d48 | 원전20eV, outgoing3–6eV/15–120degree window의 조건부 모멘트·deterministic data box | HE-ANG SOURCE_INPUT_PENDING. 전체 joint event/recoil/spin/exchange/count/source covariance가 없음; confidence interval 아님 |
| BASS B3a PR185 c2e6f1f80417e62c95e607c80115e89de1925ca9 | detached REC LINE01의 instantaneous gross/net event-rate four-force와 pressure-rate adapter. exact23, 최종15/15; scoped source-only 수용 | finite-stock/population transaction·receiver·B3b/c coupled test OPEN. 새 capsule dual ACK, remote whole-byte readback NOT_RUN |

REI ANGTHERM01의 예전 prepared-only00303 상태는 PR221의10완료 trajectories/11charged attempts로 갱신해 재사용했다. prescribed background 범위이며 Einstein backreaction의 완료가 아니다. HE37의 stationary-heavy-target/isotropic-outgoing/infinitesimal electron Grad STF 범위, C23A의 H/He z0–15.1·finite FS2010·조건부 beta coverage, REC126 저장 C2/C3의 중복 집계 금지를 유지한다. 위 외부 결과를 WU의 새 실행으로 집계하지 않는다.

## 4. 원전과 새 물리 결과

SciSpace로 원전 후보를 찾고 LLNL Warshaw2001 TDF 및 Cardall2017을 직접 확인했다. Exa 요청1은402 credit limit로 실패했고 내용은 채택하지 않았다. HTML 수식 일부가 image인 범위를 숨기지 않고, 아래 필요한 식은 직접 유도했다. PHYS81 고정 질량표와663assertions는 재사용했다.

- Warshaw, UCRL-ID-144510 (2001), [LLNL 원문](https://nuclear.llnl.gov/CNP/tdf/tdf.htm): 공통-T Maxwellian의 COM/relative 분리와 reaction-selected energy의 배경.
- Cardall, Phys.Rev.D96,123014 (2017), [accepted paper](https://arxiv.org/abs/1802.05590): rest/binding과 thermal energy 분리의 배경.
- 수식·가정·코드 연결의 전체 유도는 `theory/FINITE_T_OWNERSHIP_KO.md`, 원전 pin은 `source_data/SOURCE_LEDGER.json`을 본다.

### 4.1 정확한 사건과 같은 frame

ε_i=m_i c², M=ε_a+ε_b, Q=M−ε_c, W=M+K로 둔다. K는 invariant COM excess다. 채널은 n+p→d+γ, n+d→t+γ, p+d→h+γ이며 h는 He3 bare nucleus다. COM photon과 daughter kinetic energy는

\[
e_*=(W-\epsilon_c)(W+\epsilon_c)/(2W),\qquad k_*=(W-\epsilon_c)^2/(2W).
\]

μ를 COM photon과 boost 방향 cosine로 두면

\[
E_\gamma=\gamma e_*(1+\beta\mu),\quad K_c=\gamma(\epsilon_c+k_*-\beta e_*\mu)-\epsilon_c,\quad K_{in}=\gamma W-M.
\]

따라서 K_c+E_γ=K_in+Q다. rational half-rapidity r로 γ=(1+r²)/(1−r²), β=2r/(1+r²)를 써 exact arithmetic을 유지한다. 이는 반올림된 표시 질량에 대한 대수 정확도이고 실제 질량·단면적 uncertainty를 없애지 않는다.

### 4.2 입자 소속과 에너지 소속

thermal-birth closure의 h=1, fast-birth의 h=0이면 ΔN_th=h−2, ΔN_fast=1−h, ΔN_e=0이다. thermal+fast 전체 핵의 A/Z를 합쳐 보존을 판단한다. 여섯 에너지 열은

\[
(\Delta U_{th},\Delta U_{fast},\Delta U_{nuc},\Delta U_{atom},\Delta U_{rad,in},\Delta U_{escape})
=(hK_c-K_{in},(1-h)K_c,-Q,0,E_\gamma\mathbf1_{handoff},E_\gamma\mathbf1_{escape}).
\]

방사 경로는 하나만 선택하며 합은0이다. emitted diagnostic이나 Q를 추가 heat로 다시 더하지 않는다. h=1은 즉시 caloric inclusion이라는 선언한 closure이고 stopping 유도가 아니다. h=0은 딸핵의 전체 수와 에너지를 fast inventory에 둔다. 실제 stopping은 별도 사건·시간·에너지/입자 이동 계약을 요구한다.

ensemble에는 mean(h K_c)가 필요하다. mean(h)mean(K_c)로 바꾸면 owner-energy covariance를 잃는다. 모든 수·에너지 열을 같은 event measure로 평균해야 보존식이 유지된다. 이번 유리수 weights는 조건부 ensemble이며 실제 Maxwellian quadrature나 rate/uncertainty 분포가 아니다.

### 4.3 반응 선택과 온도식

공통-T, 독립·등방·비상대론적 Maxwellian, COM-independent σ(K)≥0, 명시적 T 의존과 이동 cutoff가 없는 조건에서 θ=k_BT, I_j=∫K^jσ(K)e^(−K/θ)dK라 두면 κ∝θ^(−3/2)I_1, mean_R(K)=I_2/I_1이다. 따라서

\[
\langle K\rangle_R=\theta\left(\frac32+\frac{d\log\kappa}{d\log T}\right),\qquad
\langle K_{in}\rangle_R=\frac32\theta+\langle K\rangle_R.
\]

ideal thermal EOS의 수와 에너지 source를 동시에 미분하면

\[
\dot T=\frac{2R\langle\Delta U_{th}\rangle}{3k_B N_{th}}-\frac{TR\langle\Delta N_{th}\rangle}{N_{th}}.
\]

모든 daughter를 fast에 두는 closure에서는

\[
\boxed{\dot T_{capture,fast}=-\frac23\frac{RT}{N_{th}}\frac{d\log\kappa}{d\log T}.}
\]

thermal 입자가 두 개 줄었다는 사실만으로 가열을 판정할 수 없다. 반응이 높은 에너지 pair를 선택해 제거하는 효과와 수 감소를 함께 계산해야 한다. formal σ∝K^s, s>−2라면 Tdot=−(2s+1)RT/(3N_th); 상수σ는−RT/(3N_th), inverse-speedσ는0이다. 두 예는 정리의 witness이며 실제 핵 단면적으로 채택하지 않는다.

T>0,N_th>0,0<I1<∞,finite I2와 미분/적분 교환이 필요하다. R=0이면 source0이나 κ=0에서 normalized event mean/logκ는 정의하지 않는다. 이 NR 정리는 앞의 exact relativistic event kernel의 Jüttner thermal average가 아니다. Drift, 다른 온도, 명시적 T 의존 단면적 및 finite bath를 자동 포함하지 않는다.

## 5. 코드·실행·독립 검토

Astra controller가 계약과 물리 판정을 동결하고, lower-tier gpt-6.1-sol/high 요청 agent가 구현·기계적 입력 전사·허용된 실행을 맡았다. 관측 backend identity와 remote hardware/thread scheduler는 UNOBSERVED다. fresh Astra가 구현자와 별도로 theory와 code/diff/raw를 검토했다.

source/event_owner.wl, verification/verify_event_owner.wl, source/execute_reference.wl을 보존한다. verifier는 독립 직접 four-vector boost, photon null, daughter mass shell, total energy/momentum, A/Z, 입자수, 경로 이동, joint covariance와 NR theorem controls를 포함한다. 기존 PHYS81 kernel과 cold cases를 호출하지 않는다.

| 실제 호출 | 보존된 결과 | 채택 가능한 결론 |
|---|---|---|
| attempt01,02:53:30–02:53:37UTC | reference_report가 미평가 함수 문자열. raw SHA0b0b0bff4361175be326713ed828448f596bfd0989cc554a68f31273d199854a | IMPLEMENTATION_ENTRYPOINT_NAMESPACE_BINDING_FAILURE. complete event/ensemble/assertion0 |
| binding-only repair | context directives8줄 제거, wrapper prefix3곳 제거. 식·입력·guard·oracle·시간 cap 불변. 원본9파일 보존 | 독립 diff PASS 후 S1R 게시·양쪽 ACK, 한 번 실행 승인 |
| attempt02,02:59:46–02:59:56UTC | raw13,328bytes, text10,239chars의 실제 중간 생략. SHA51f4408d91e7ac6566639f3ab3c04eedb3f1e4d2f05a0abd68e7d246e1c6c9eb | TRANSPORT_TRUNCATED_REFERENCE_UNVERIFIED. full counts=null; valid scientific completion 아님 |

공식 [Wolfram context 문서](https://reference.wolfram.com/language/tutorial/ModularityAndTheNamingOfThings.html)의 complete-expression symbol 해석 순서를 첫 오류와 대조했다. 첫 static review는 이 조립 문제를 발견하지 못했다. 두 번째 raw는 평가 진입의 조각을 보이지만 전체 JSON을 검증할 수 없다. raw에 지속 retrieval handle/resource link/artifact URL이 없으므로 현재 증거에서 retrieval-only 복원 경로를 찾지 못했다. 누락 결과를 source 기대값이나 재계산으로 채우지 않았다.

독립 C9: STATIC_IMPLEMENTATION_PASS_SCOPED_REFERENCE_NOT_VERIFIED. 게시 가능한 것은 불완전한 checkpoint와 정확한 실패 이력이다. EXACT_REFERENCE_IMPLEMENTATION_VERIFIED나 physical admission은 발급하지 않았다.

바이트 대조는 prior distinct paths36개를 해시하고, expected digest38건/해당 distinct paths34개에서 불일치0이었다. 원본 implementation9, mechanical4, repair4, 두 attempt 각6의 중복 제거 primary paths28개를 포함한다. checksum 검사는 과학 assertion으로 세지 않는다.

## 6. 실행·예산·게시·백업의 분리

| 범주 | 이번 값 |
|---|---:|
| Wolfram evaluation tool calls | 2 |
| 유효한 완료 exact reference application | 0 |
| attempt01 entrypoint 실패 | 1 |
| attempt02 transport 미검증 | 1 |
| attempt02 actual complete row/assertion/guard counts | null |
| 남은 자동 repair/probe calls | 0 |
| local numerical child / PHYS84 새 wrapper | 0 / 0 |
| physical nuclear rate / fast stopping / ODE / benchmark | 0 / 0 / 0 / 0 |
| 완료 identity replay / 다른 process 종료 / cache 조작 | 0 / 0 / 0 |
| inherited spend / remaining / currency | null / null / null, reset=false |

60초 per call/내부55초는 cap이며 실제 remote CPU로 환산하지 않는다. tool-clock 간격7초·10초도 remote kernel 계측이 아니다. 외부 owner campaign의 비용·완료 수는 그 계보에 보존하고 WU의 새 실행 비용으로 중복 합산하지 않는다.

| 단계 | 내용 | 게시·백업 근거 |
|---|---|---|
| S0 | 조사·계약·유도·독립 theory PASS | 0dec9cc128b8cba8d4a7745d603a808563eb1772; 양쪽 upload ACK |
| S1 | 동결 구현·입력·검증기 | 04be89e24401966770d137b115c73f66b563ef5d; 양쪽 upload ACK |
| S1R | 첫 실패·원본 보존·binding-only repair | 1a8f98719fd3ec87d3acbfb27aeda9936b0bc613; 양쪽 upload ACK |
| S2 | 두 번째 raw·최종 독립 판정·최신 delta·DAG·handoff | 8623d650d9ef9cb918373bdfe6a3d7834bac702f; 양쪽 upload ACK. ZIP9,722,949bytes/SHA94f6f62a1029af3423adc7fb478ff433e12bb42fb1ed8e0d752422caadeca5b1 |
| FINAL | S2 ACK를 포함한 최종 전달 checkpoint | 실제 최종 HEAD/tree/ZIP SHA와 provider 전체 다운로드·복원은 외부 PHYS85_FINAL_DELIVERY_20261024.json 및 PR 최종 본문 |

모든 원격 ref 변경은 expected SHA를 사용한 additive Draft PR142이며 base/main을 merge하거나 부모 과학 파일을 수정하지 않는다. 단계별 ZIP의 ACK와 최종 ZIP의 실제 전체 복원을 구분한다. 최종 manifest는 owned Git prefixes, private intake, 원본 PHYS84 ZIP/JSON 전체 bytes를 포함한다. 최종 복원은 각 provider의 실제 전체 GET·reopen SHA·CRC·payload SHA·fresh Git blob·전체 추출을 별도 count로 기록한다. 부모 내부 ZIP의 과거 science를 실행하거나 과거 전체복원을 소급 재수행했다고 하지 않는다.

## 7. 전체 목표까지의 DAG와 다음 입력

| 노드 | 현재 완성도 | 다음 전이 조건 |
|---|---|---|
| WU_CE83_OWNER_COMPLETION | NUMERICALLY_CHECKED_SCOPED_REUSED | PHYS83 identity 재사용, 재실행0 |
| PHYS84_HI_CE_SOURCE_ADAPTER | DERIVED_STATIC_REVIEWED_NUMERICAL_WAIT | 기존 shared lease 그대로 확보될 때만 최초 수치 child |
| PHYS85 event owner·NR selection theorem | DERIVED_SCOPED_REVIEW_PASS | 유도 근거 재사용 |
| PHYS85 exact reference | STATIC_PASS / RUNTIME_NOT_VERIFIED | 완전한 output transport·검토·명시적 후속 budget/admission 계약 필요; 현재 cap0 |
| NUCLEAR_PHYSICAL_FINITE_T_EVENT_SUPPLIER | OPEN | 실제 σ/branching/angular, distribution/frame/clock, 같은 사건 수·에너지 weights, uncertainty 계약 |
| NUCLEAR_FAST_STOPPING_AND_ADMISSION | OPEN, supplier 뒤 | thermal/fast 수와 에너지 이동·시간·finite bath를 일관되게 공급 |
| WU_D_PI_RR_MATCHED | OPEN, conditional C23E child 근거 추가 | 실제 isotope PI/RR·finite mass/levels·Milne 또는 목표오차에 맞춘 근사 채택 계약 |
| HE_LI_CX_STATE_AND_PHOTON_ENERGY | OPEN | state-resolved source/branching/photon energy |
| Li 실제 source uncertainty | OPEN | instrument response/deconvolution/isotope/target-state·물리 uncertainty |
| RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT | OPEN | 동일 history/parameter/source domain과 초기 charge 계약 |
| LI_HARD_UV_INNER_SHELL_SPECTRAL_CONTRACT | OPEN | hard-UV inner-shell spectral source와 에너지/상태 귀속 |
| FULL_GEOMETRY_SPECTRAL_BACKREACTION | OPEN | 위 supplier·consumer 및 보존 coupling·별도 feedback 검증 |

전체 completion fraction은 null이다. 이질적인 열린 물리 의무에 승인된 가중치가 없어 R/C 단계 수를 전체 물리 완료율로 바꾸지 않는다. non-tilted LRS BianchiI, reacting gas pi=0, 별도 collisionless DM pi_m, 같은 normal frame의 signed tensor를 합한 뒤 norm, Frobenius=√2×half-contraction을 유지한다. 동일 trajectory 성분 분석은 species-off 인과 실험이 아니며 finite quadrature/energy residual은 continuum certificate가 아니다.

다음 thread는 `CODEX_HANDOFF_KO.md`, `NEXT_THREAD_HANDOFF_KO.md`, `POST_PUBLICATION_HANDOFF_KO.md`, `CENTRAL_RETURN.json`과 최종 외부 delivery를 먼저 읽는다. 새 실행을 시작하기 전에 현재 AGENTS·HEAD·병렬 owner·backup·누적 budget을 다시 대조한다.
