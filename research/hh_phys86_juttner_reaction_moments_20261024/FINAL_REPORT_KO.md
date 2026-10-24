# PHYS86 최종 과학 보고 — Jüttner 반응 선택 moments

## 1. 판정

**과학 판정은 PASS_SCOPED다.** PHYS85의 같은 normal frame capture 사건 소유권 코드에서 첫 완전한 참조 certificate를 확보했고, 공통 온도 Maxwell–Jüttner 분포의 반응 선택 에너지와 가변 thermal 입자수의 온도 source를 유도·구현했다. 고정된 두 Wolfram 요청을 각각 한 번 실행한 뒤 별도 Astra 검토자가 실제 원문을 읽었다.

새 참조 평가 **2회 = 완료2 + 실패0**, 이전 PHYS85 호출2회를 포함한 누적 evaluator 호출 **4회**다. 현재 허용된 추가 호출은0이다. 이전 entrypoint 실패와 잘린 출력은 원본대로 보존한다. 완료된 PHYS78–83 및 외부 owner 과학 identity를 재실행하지 않았다.

과학 완료와 전달 완료는 다르다. S0/S1 Git과 Dropbox ACK는 확보했다. S0 Drive는 장시간 응답 대기 후 **UNKNOWN_NO_ACK**이며, 이후 실제 상태는 delivery/와 외부 final-delivery receipt를 따른다. 이 과학 보고가 양쪽 최종 백업 복원이나 production admission을 발급하지 않는다.

| 축 | 실제 판정 |
|---|---|
| 원전·가정·유도 | DERIVED_SCOPED_REVIEW_PASS |
| 동결 구현·정적 검토 | PASS_STATIC_SCOPED |
| PHYS85 complete projected reference | PASS_SCOPED |
| 새 finite-family moment 및 symbolic reference | PASS_SCOPED |
| 독립 actual-raw C9 | PASS_SCOPED, repair finding0 |
| 실제 nuclear rate / stopping / ODE | 새 실행0, 공급·활성화 OPEN |
| WU_NUCLEAR_PARTICLE_OWNERSHIP 부모 | PARTIAL |
| HH_R10 / production | OFF / NOT_ISSUED |

## 2. 접근 가능한 최신 결과의 종합

이번에는 기존 inventory를 이름만 재인용하지 않고 접근 가능한51repo의 조사 시점 branch refs snapshot를 다시 수집했다. 공개35repo는 native refs, 비공개16repo는 인증 connector pagination으로 보완하여 **2226refs**를 관찰했다. 관련6repo의1114refs는 이전1106refs snapshot에 대해 신규8·변경4·삭제0이었다. 과거2175refs의 전체 대응 지도가 없어 단순 차이51을 identity delta라고 주장하지 않는다.

관련 최신 PR35개, 별도 owner updated 검색16결과, 선택 source 읽기30건 중 실제 반환27blob의 Git SHA를 확인했다. REC/BASS/Vigil의 root AGENTS404 세 건도 보존했다. 이는 모든 branch의 전체 source, 모든 PR 본문 또는 비공개 대화 전수 열람을 뜻하지 않는다. PersonalContext는 실제로 이 대화에서 사용 불가였다.

WU 알려진 백업 폴더의 Drive534개·Dropbox503개와 관련 owner의 백업 metadata를 확인했다. broad Dropbox3401개 직접 항목의 pagination은 끝까지 읽었지만 HE Drive1000 상한은 소진 여부를 증명하지 않는다. 겹치는 폴더 개수를 전체 고유 파일 수로 합산하지 않았다. 부모 PHYS85의 기존 실제 provider 다운로드 네 파일을 다시 바이트 대조하여 원본과4/4 일치했다. 새 부모 다운로드·중첩 복원·과학 재실행은0이다.

게시 직전 중앙 PR222는 조사 시작 pin5182d82c에서 d5aa6c94로 추가2commit/5file 변경됐다. AGENTS blob429a5a13과 WU handoff blob6598d1bd,7authority와6WU nodes는 그대로였다. 40중38개 중앙 노드가 같았고 차이는 HE/CR producer return이었다.

| 결과 | 이번 채택 범위와 남은 의무 |
|---|---|
| PHYS83 PR140, science e09e6484… | 첫 노드 WU_CE83_OWNER_COMPLETION을 완료 근거로 재사용. 132rates/324steady/732transient/2111assertions 재실행0 |
| PHYS84 prepared dca969a2… | 8prepared+5parent pins 유지. local lease 수치 실행 WAIT, 새 child0 |
| REC PR132 ae189694…, science4224a7be… | retarded constant-shear characteristic/native Wien adapter의 저장 결과 재사용. physical source history uncertainty와 initial-charge 공급은 OPEN. CI formatting 실패와 scoped science를 분리 |
| CR N5 b8882d02…, 문서b65befa5… | PHYS83와 저장 C23D를 연결한 조건부 first-event/CE 결과. thermal ne·k와 fast-target n·vσ hazard를 혼용하지 않음. Drive UNKNOWN 보존 |
| HE37 d6183444… | stationary-heavy-target / isotropic-outgoing / infinitesimal electron Grad STF. gas STF가 아님 |
| HE DDCS20 d8bae9f7… | 고정된 측정 window20의 조건부 근거. full joint event law와 recoil 공급은 OPEN |
| HE CCC exchange PR95, science63706d60… | 새로 관찰한 equal-sharing amplitude/phase/spin 정규화와 TP TableI8값. parent HE-ANG SOURCE_INPUT_PENDING, physical provider 미채택 |
| BASS PR185 c2e6f1f8… | detached photon event source. finite-stock B3b/c와 coupling OPEN; 다른 담당자의 B3B 준비를 중복 구현하지 않음 |
| VigilODE PR85 1c829f20… | staged domain guard와 제한된 scalar-linear positivity certificate. 일반 coupled integrator/compiled-roundoff certificate로 승격하지 않음 |
| REI L0 TRACE 백업 | producer targeted numerics 근거만 재사용. 자체 increment CPU cap 초과와 fresh-review HOLD를 보존하고 WU 예산으로 이전하지 않음 |
| C23A/C23D/C23E 및 REC126 | 각 완료 identity·조건부 범위와 기존 실패·비용을 보존. empirical D PI/RR source를 얻었다고 주장하지 않음 |

SciSpace 검색1회와 Wolfram context1회를 원전 탐색에 사용했다. Exa는1회 시도에서402 credit limit으로 내용이 반환되지 않아 결과에 사용하지 않았다. 아래 유도는 실제 읽은 primary papers와 독립 직접 계산으로 닫았다.

## 3. 새로 연결한 물리

### 3.1 같은 normal frame의 event measure

Metric은 (-,+,+,+), \(\epsilon_i=m_i c^2\), \(E_i=\sqrt{\epsilon_i^2+c^2p_i^2}\), \(\beta_T=(k_BT)^{-1}\)다. \(\beta_T\)는 boost의 v/c가 아니다. 고전 희박 기체, 고정 species/rest masses/internal states, 공통 온도와 즉시 재열평형 closure를 가정한다.

\[
f_i(\mathbf p;T)=Z_i^{-1}e^{-\beta_TE_i},\qquad
Z_i=4\pi m_i^2 c k_BT K_2(\epsilon_i/k_BT).
\]

분포는 d³p에 대해 정규화한다. 같은 frame에서 \(D=E_aE_b-c^2\mathbf p_a\cdot\mathbf p_b\)라면
\[
v_{\rm rel}=c\sqrt{D^2-\epsilon_a^2\epsilon_b^2}/D,\qquad
v_{\rm flux}=\frac{D}{E_aE_b}v_{\rm rel}.
\]
실제 rate kernel은 이 frame의 정규화된 두 분포에 대해 \(\sigma v_{\rm flux}\)를 포함한다. Møller flux factor를 별도의 invariant relative speed로 바꾸지 않는다.

고정 measure에서 \(S=E_a+E_b\), 비음수 T-independent kernel B를 두면
\[
N=\int B e^{-\beta_TS}d\lambda,\quad
\kappa=N/(Z_aZ_b),\quad
dP_R=B e^{-\beta_TS}d\lambda/N,\quad
R=n_an_b\kappa/(1+\delta_{ab}).
\]
N>0인 경우 정규화된 사건 평균을 정의한다. 동일 입자 쌍은 대칭계수와 두 반응물의 stoichiometric debit을 함께 적용해야 한다.

### 3.2 선택 에너지와 가변 입자수

정규화 partition을 직접 미분하면
\[
-\partial_{\beta_T}\log\kappa
=\langle S\rangle_R-\bar E_a-\bar E_b.
\]
따라서 thermal 입자 하나의 평균 운동에너지를 \(u_i=\bar E_i-\epsilon_i\)라 할 때
\[
\boxed{\langle K_{\rm in}\rangle_R
=u_a+u_b+k_BT^2\partial_T\log\kappa.}
\]

온도 변화에는 thermal energy source와 thermal 입자수 source가 모두 필요하다.
\[
U_{\rm th}=\sum_i n_i u_i(T),\qquad
\dot U_{\rm th}|_R=C_V\dot T|_R+\sum_i u_i\dot n_i|_R,\quad
C_V=\sum_i n_i u_i'(T)>0.
\]
Daughter의 사건별 thermal membership \(h\in\{0,1\}\)를 유지하면
\[
\boxed{C_V\dot T|_R
=-Rk_BT^2\partial_T\log\kappa
+R\langle h(K_c-u_c)\rangle_R.}
\]

h=0은 모든 daughter가 fast inventory에 태어나는 경우다. h=1은 명시적인 instantaneous caloric birth model이며 실제 stopping 유도가 아니다. \(\langle hK_c\rangle\)를 \(\langle h\rangle\langle K_c\rangle\)로 바꾸지 않는다. Photon/recoil/rest energy와 thermal/fast 개수는 같은 사건의 같은 normal frame에서 회계한다.

### 3.3 변화율, 명시적 kernel 의존성, 열용량

유한한 필요한 moments와 적분 미분 교환을 보장하는 조건에서
\[
\partial_T\langle\phi\rangle_R=\operatorname{Cov}_R(\phi,S)/(k_BT^2),\qquad
\partial_{\beta_T}^2\log\kappa
=\operatorname{Var}_R(S)-\operatorname{Var}_a(E_a)-\operatorname{Var}_b(E_b).
\]
관측량 \(\phi\)와 B가 T에 직접 의존하면 별도 미분항이 필요하다. 특히
\[
A_T=N^{-1}\int(\partial_TB_T)e^{-\beta_TS}d\lambda
\]
를 정의하면 앞선 선택·온도 식에서 \(\partial_T\log\kappa\)를 \(\partial_T\log\kappa-A_T\)로 교체한다. 이 적분 정의는 B=0인 지점에서 log B로 나누지 않는다.

\(r=K_1(z)/K_2(z)\), \(z=\epsilon/(k_BT)\)이면
\[
u=\epsilon(r-1)+3k_BT,\qquad
u'/k_B=3+z^2-z^2r^2-3zr
=\operatorname{Var}(E)/(k_BT)^2>0.
\]
NR 극한에서는 \(C_V\to3N_{\rm th}k_B/2\)여서 PHYS85의
\[
\dot T|_R=-\frac{2RT}{3N_{\rm th}}\frac{d\log\kappa}{d\log T}
\]
로 돌아간다. 큰 z의 부동소수점 소거를 안정하게 다루는 production Bessel 구현은 이번에 채택하지 않았다. expansion/shear/transport 및 quantum, screening, time-dependent domain 등은 조건에 맞는 별도 공급이 필요하다.

## 4. 실제 코드와 실행 결과

실행 source는 S1 commit280ef5094dd56b76ce4f5dc8f8aad7bc36172728, tree435ef54285fe1a2690cc75a9791e77e553cbe4ea다. 요청 arguments와 실행 code의 바이트가 동결본과 일치함을 확인했다.

| 항목 | PHYS85 complete projection | 새 moment reference |
|---|---:|---:|
| 실제 새 evaluator 호출 | 1 | 1 |
| 실제 사례 | 36events +6ensembles | q=1/2,2/3,3/4 |
| Guards | 23 | 10 |
| 실제 검사 PASS | 1017/1017 | 82/82 |
| 보존 원문 파일 | 5698bytes | 6179bytes |
| 완전 payload | 3791bytes | 2703bytes |
| 실제 escaped output | 4512bytes | 4047bytes |
| fresh actual-raw 검토 | PASS_SCOPED | PASS_SCOPED |

첫 요청은 PHYS85의25893byte repaired core를 그대로 실행했다. n+p→d+γ, n+d→t+γ, p+d→³He+γ의 noncold 구성 사건, 두 daughter ownership, 두 radiation route에 대해9개 서로 다른 정확 에너지 triple,3개 ownership-energy covariance,36+6개의 정확 잔차 norm0과23개 guard tag를 완전히 받았다. 옛 잘린 verbose report를 복구한 것은 아니며, 새로 규정한 projected certificate의 첫 완전 검증이다. 반올림된 CODATA 표시값을 exact rational로 읽은 결과를 물리 질량의 정확값이나 confidence interval로 바꾸지 않는다.

둘째 요청은 물리 단면적이 아닌2×2 양의 finite exponential-family witness다. 독립 checker는 source 함수와 다른 경로에서 partition polynomial을 직접 미분했다. Daughter \(u_c\), R, C_V는 formal symbol로 유지하여 가짜 EOS나 핵반응률을 채워 넣지 않았다.

| q | 구성 rate κ | 선택 차 \(\langle S\rangle-\bar E_a-\bar E_b\) | \(\operatorname{Cov}(hK_c,S)\) | 보정을 뺀 잔차 |
|---|---|---|---|---:|
| 1/2 | 31/18 | 209/558 | 24/961 | -1 |
| 2/3 | 149/77 | 4980/11473 | -8496/22201 | -1 |
| 3/4 | 418/205 | 19443/42845 | -1260/2299 | -1 |

에너지는 구성 scale ε₀로 나눈 값이며 covariance는 ε₀² 단위의 무차원 값이다. 이 표는 실제 온도별 nuclear-rate 표가 아니다. Kernel을 q배한 대조에서 event measure는 유지되고 log-rate 기울기만1만큼 달라졌다. 명시적 보정1을 넣은 식은 세 점 모두 정확히 통과했다. Moment 잔차45개, formal source 잔차3개, symbolic residual8개가 모두0이다. Covariance 부호가 바뀌는 실제 예는 임의 관측량의 covariance를 항상 양수라고 둘 수 없음을 보여 준다.

κ=N=0이면 normalized means와 logκ는 정의되지 않지만 source는0이다. κ>0인 채 density가0이어서 R=0인 경우에는 event measure가 유효하며 source API는 mean 평가 없이0을 반환할 수 있다. C_V≤0은 그 전에 거부한다.

### 원문 경고와 판정 범위

두 원문에 Symbol::undefined2 및 General::messages가 있다. 둘째 원문에는 Infinity::indet (0*Infinity) 경고 두 건도 있다. 내부 발생 지점은 보존된 출력만으로 특정하지 못했다. 이를 삭제하거나 warning-free run으로 보고하지 않았다. 채택한 값에는 Indeterminate/Infinity가 없고 엄격한 exact-zero 검사와 독립 원식 검토가 일치하여 위의 한정된 reference PASS를 채택했다. 일반 Bessel 수치 안정성이나 production 실행을 이 로그로 보증하지 않는다. 경고 제거만을 위한 재실행은 하지 않았다.

## 5. 예산·자원·절차

- 이전 PHYS85 evaluator2회와 old remaining allowance0을 그대로 보존했다.
- 새 계약의 recovery1 + moment1을 사용했다. 추가 probe/retry/repair0, 현재 남은 호출0이다.
- 각 요청 outer60s/inner55s, 순차 단일 kernel 경로다. Cloud hardware/scheduler는 UNOBSERVED다.
- Local scientific child0, PHYS84 새 application0, physical rates0, stopping0, ODE0, benchmark0, completed identity replay0이다.
- local reserve1.5GiB+job0.5GiB 조건을 변경하지 않았다. 다른 process 종료0, cache 정책 변경0이다.
- 알려지지 않은 과거 금전 비용·잔여 예산은 null이며0으로 재설정하지 않았다.

S0 Drive 호출이1206s 뒤 root의 대기 중단으로 끝났을 때 tool은 “aborted by user”라고 표시했다. 실제 사용자의 작업 취소나 원격 업로드 취소로 해석하지 않는다. 원격 성공/실패는 UNKNOWN_NO_ACK다. 새 dual ACK가 과학 실행의 선행 허가여야 한다는 추가 규칙은 controller의 절차적 조건이었다. 실제 중앙 AGENTS 실행 전환 정책과 별도 독립 검토에 따라, 검토된 S1 Git·정확한 local packs·검증된 부모 백업을 근거로 두 요청 실행을 허가했다. 그 조정은 입력/검사/예산/lease를 변경하지 않았으며 양쪽 최종 백업 의무도 해제하지 않았다. 관련 원래 gate, 보정 검토와 root GO를 모두 보존한다.

## 6. DAG와 다음 연구

이번에 닫은 것은 nuclear parent 전체가 아니라 **같은-frame supplied-event reference와 Jüttner moment/caloric-source 연결**이다.

| 순서 | 노드 | 현재 상태 |
|---|---|---|
| 선행 | WU_CE83_OWNER_COMPLETION | 완료 근거 재사용 |
| 조건부 병렬 | PHYS84_HI_CE_SOURCE_ADAPTER | 유도·정적검토 완료, local numerical WAIT |
| 완료 child | PHYS85 supplied-event reference → PHYS86 complete projection | EXACT_REFERENCE_PASS_SCOPED |
| 완료 child | PHYS86_JUTTNER_REACTION_SELECTED_MOMENTS | DERIVED_AND_EXACT_REFERENCE_PASS_SCOPED |
| 다음 핵물리 | NUCLEAR_PHYSICAL_FINITE_T_EVENT_SUPPLIER | OPEN |
| 그 이후 | NUCLEAR_FAST_STOPPING_AND_ADMISSION | OPEN |
| 병렬 원전 | HE_LI_CX_STATE_AND_PHOTON_ENERGY | OPEN |
| 병렬 원전 | D_PI_RR_MATCHED_SOURCE_MOMENTS | empirical source OPEN |
| 병렬 원전 | Li instrument/deconvolution/isotope/target/physical uncertainty | OPEN |
| 연결 선행 | RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT | OPEN |
| 연결 선행 | LI_HARD_UV_INNER_SHELL_SPECTRAL_CONTRACT | OPEN |
| 전체 결합 | FULL_GEOMETRY_SPECTRAL_BACKREACTION | OPEN |

다음 핵물리 의무는 실제 원전의 isotope/target state/energy domain을 고정하고, 같은 사건의 differential capture kernel·angular branching·normal-frame photon/recoil·thermal/fast membership을 제공하는 것이다. 그 event measure가 κ, 선택 평균, joint retention, variance와 미분 관계를 함께 만족하는지 먼저 닫아야 한다. 총 rate fit만으로 angular joint law나 fast stopping을 임의로 채우지 않는다. 그 공급 이후에만 physical rate와 stopping 활성화를 판단한다.

Non-tilted LRS Bianchi I, reacting gas π=0, collisionless DM π_m 별도 조건을 유지한다. Signed matter/radiation tensors를 같은 normal frame에서 합한 뒤 norm을 취한다. Frobenius는 half-contraction norm의√2배다. 동일 trajectory의 성분 분해는 species-off 인과실험이 아니고 sampled residual은 continuum certificate가 아니다.

단계별 R/C 완료 표는 RESEARCH_LOOP_MAP_KO.md다. 전체 목표의 가중 분모가 정해져 있지 않아 완료율은 null이며, 절차20단계의 진척을 전체 물리 완료율로 해석하지 않는다.

## 게시 직전 추가 source와 전달 방식

최종 과학 게시 전 중앙 PR222의98ca692b200227c51011bfbbe037daaccfc6f3eb까지 추가3commit/29file delta를 확인했다. AGENTS·WU 인계·7authority·6WU nodes는 그대로다. HE CCC child의 dual upload/metadata readback과 REI-L0의 finite source-exchange/signed-STF algebra admission이 추가됐지만, HE physical provider와 REI full L1은 미채택이다. REI 문서가 인용한 PHYS86 S0는 그 producer의 과거 조사 snapshot이며 현재 owner 결과를 덮어쓰지 않는다.

두 Drive whole-archive 호출은 ACK가 없는 상태로 보존했다. Root는 과학 입력을 바꾸지 않고 원본 ZIP의 연속된 byte parts를 전송하는 방식을 별도 TRANSPORT_AMENDMENT.json으로 선택했다. 원인이나 API size limit을 확정한 것은 아니다. 성공한 경우 Drive는 각 part의 전체 raw GET과 SHA를 확인한 뒤 정확한 순서로 원본 ZIP을 재조립하고 전체 SHA/CRC/payload/Git/추출 검증을 수행한다. 이를 단일 ZIP object의 GET이나 원래 whole-upload ACK라고 보고하지 않는다. 실제 성공 여부는 이후 receipt에만 기록한다.

PHYS82의 conditional matched-model 범위는 실제 source confidence interval이 아니며 고정 T/ne 노출을 coupled thermal/xe history의 경계로 쓰지 않는 조건도 유지한다.

## 7. 원전·검증·복구 위치

원전:
- Chacón-Acosta, Dagdug, Morales-Técotl, arXiv:0910.1625v1: https://arxiv.org/html/0910.1625v1
- Cannoni, arXiv:1506.07475v3, Appendix B: https://arxiv.org/html/1506.07475v3
- Wolfram BesselK 공식 문서: https://reference.wolfram.com/language/ref/BesselK.html

표준 Jüttner 정규화·partition 미분 identity를 재사용하고, 이번 프로젝트의 기여는 이를 기존 사건 소유권/가변 thermal 수/joint retention source와 연결해 실행한 것이다. 새로운 보편적 통계역학 정리나 strong no-go의 문헌 신규성은 주장하지 않는다.

필수 근거는 CONTRACT.json, theory/, implementation/의 두 frozen request, source_data/PHYS85_EXPECTED_ORDER.json, results/의 두 whole raw/certificate, reviews/ACTUAL_RAW_REVIEW*, results/ROOT_SCIENTIFIC_DECISION.json이다. 완성된 scientific identity와 최종 evidence identity는 results/의 별도 문서에 결속한다. 최종 containing HEAD·ZIP·provider ID·raw JSON readback은 실제 PR143 본문과 외부 PHYS86_FINAL_DELIVERY_20261024.json의 관찰 상태를 따른다. 존재하지 않는 future ACK나 자기 commit SHA를 이 문서 안에 추정해 넣지 않는다.
