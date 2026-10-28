# R14 종료 보고서 — 비정렬 quadratic forcing의 유한 조건부 인증

R14는 R13의 비정렬 affine forcing을 **셀 전체에서 비음수인 piecewise quadratic forcing**으로 확장했다. 원래 Bernstein middle coefficient가 음수인 입력도 정확한 비음수성 검사를 통과하면 받는다. Source의 꼭짓점에서 정확히 분할하고, positive cubic global-memory convolution, critical-root의 유리수 격리, whole-cell supremum의 명시적 간격, signed scalar E 전달을 하나의 유한 계약으로 구현했다.

종료 대상은 이미 진행하던 이론·코드 두 노드다. 독립 최종 C9 판정은 **PASS_SCOPED_FINAL_C9**, 열린 중대 지적은 **0**이다. 채택 delta 판정 **PASS_SCOPED_ADMISSION_METADATA_DELTA**에 따라 `WU_HD_QUADRATIC_FORCING_THEORY_R14`와 `WU_HD_QUADRATIC_FORCING_CODE_R14` 두 조건부 노드를 채택했다. 과학 DAG는 **29/44**, 상속한 42개 노드 객체의 변경은 0이다. 이론 R1–R10과 코딩 C1–C10의 종료 상태는 20/20으로 결속한다. S09/S10의 실제 identity와 영수증은 아래 종료 필드 및 `delivery/PUBLICATION_INDEX.json`이 기준이다.

이 결과는 주어진 full-A block certificate와 whole fine/coarse-domain forcing bounds에 대한 comparison 구성이다. 실제 HD reactive array 또는 named WU physical consumer/state/density/clock은 **실제로 검사한 원전 범위에서 INPUT_PENDING**이다. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`, central/physical delta=0을 유지한다. 새 후속 단위는 시작하지 않으며 future allowance는 0이다.

## 1. 실제 결과와 identity

| 항목 | 실제 결과 |
|---|---|
| Primary | **621/621 PASS**, valid 31/31, guard 46/46, 실패 0 |
| 독립 reference | **691/691 PASS**, **51,547 component comparisons**, 실패 0 |
| 비교 구성 | metadata 11,296 / exact 27,094 / coverage 8,026 / Decimal 5,131 |
| 새 과학 실행 | primary 1 / reference 1 / Wolfram CAS 1 / ODE 0 |
| Primary 전체 OS process CPU | 3.224500초 |
| Reference 전체 OS process CPU | 1.195646초 |
| 두 과학 process CPU 합계 | **4.420146초**, import·serialization 포함 |
| 동결 실행 의존 파일 | **20개**, 실행 전에 SHA-256 고정 |
| 수치 계약 | production dyadic128/Taylor96, root bisections 96, reference Decimal160 |
| Reference 사전 guard | `1e-80 * max(1, abs(reference), abs(lower), abs(upper))` |
| Guard 없는 strict Decimal containment | **false, 83건**, 예시 50개 보존 |
| 새 CAS | **32개 exact zero residual**, 이번 반환 warning 0 |
| R14 primary/reference/CAS remaining | **0/0/0** |
| 기존 완료 과학·ODE·독립 심사 재실행 | 0 |

Primary는 S05 `308a1f67e29339df4df1bcf04ae61d24f3984b33`, reference는 S06 `47c0ae15c19de624ec2838231fccf3119e6a63b4`의 동결 실행 파일에서 각각 한 번 실행했다. 각 process의 사전 한도는 CPU 90초, wall 120초, address space 1 GiB였다. 실제 한도와 사용량은 `EXECUTION_LEDGER.json` 및 process 기록에 있다.

| 저장 결과 | SHA-256 |
|---|---|
| `raw/PRIMARY_RESULTS.json` | `1e724a855cb3bca0b12c88b595ba561d4399103da65984b1b102cb04cb300907` |
| `raw/REFERENCE_RESULTS.json` | `8f39fc944e11dedda4de41250fb4ac79f142ec042ec0d61b34f0fb01de3010fc` |

Reference의 PASS는 사전에 고정한 guard 아래의 고정밀 대조 결과다. Decimal160을 interval reference로 표시하지 않으며, strict containment 83건을 숨기거나 tolerance를 사후 확대하지 않았다. Exact rational 검사와 directed-rounding의 수학적 근거는 별개로 보존한다. 이 83건은 R10/R11의 saved physical-sample readout이 아니다.

과학 S09 commit은 `dfdefe47ef0c28ae94f6e6727d3230ceed5c356d`, tree는 `a0f87622e8ac3eae235968962e704b4ad5f59c6a`이다. 과학 payload는 **105개 파일**, SHA-256 **`b68ab395e4e36ea7a6b49bb6c0b1f44fb75d10522f223d29657907179ac24e4b`**로 결속한다. S10 source commit은 `75a3bdbcba5113e4a4b94444c4ac6d6b08cc4871`, tree는 `fdf43028f7de44b7b46a7ef443708f21b6380bbe`이다. 실제 S09 remote Git tree의 blob IDs·크기는 로컬 Git blob hash·scientific manifest와 **105/105 일치**했다. 이는 content-address identity 검사이며 provider ZIP original GET 또는 모든 remote blob의 새 본문 다운로드가 아니다. **FINAL 자신의 commit/tree/ZIP/ACK는 자신의 source에 삽입하지 않고 PR150과 종료 응답에 외부 영수증으로 보존한다.**

근거: [RESULTS_KO.md](RESULTS_KO.md), [EXECUTION_LEDGER.json](EXECUTION_LEDGER.json), [FROZEN_FILES.json](verification/FROZEN_FILES.json), [SCIENTIFIC_PAYLOAD_MANIFEST.json](SCIENTIFIC_PAYLOAD_MANIFEST.json).

## 2. 최신 branch·PR·대화·백업 조사의 범위

조사는 접근 가능한 현재 목록을 terminal pagination까지 확인하고, 바뀐 구체적 의존 원전을 읽는 방식으로 닫았다. 비원자적 live metadata snapshot이며, 모든 역사 commit·PR·대화·archive의 모든 본문을 읽었다는 주장이 아니다. 비공개 자료는 집계만 공개하고, 계정 metadata와 private/shared 본문 및 저작권 원문 응답은 public source pack에서 제외했다.

| 범위 | 실제 확인 내용과 한계 |
|---|---|
| Owner repo/branch | 51 repo, 2,406 branch heads, 66 pages, 51/51 terminal, errors 0. 공개 35 repo/1,921 heads, 비공개 16 repo/485 heads는 집계만 보존 |
| Branch cutoff | **2026-10-28 09:03:58.811 UTC = 18:03:58.811 KST**. R13 대비 공개 NEW 6 / MOVED 9 / REMOVED 0 |
| 현재 open PR | **1,180 = 공개 1,126 + 비공개 집계 54**, 85 pages, 51 repo terminal, duplicate key 0 |
| 최근 closed/merged PR | R13 cutoff 06:58:58.660 UTC 이후 updated 범위, 51 pages terminal, 새 해당 행 0 |
| 바뀐 public PR | 14개. 다른 13개 현재 본문 전문 읽기; own WU PR150은 R13 closeout baseline과 현재 identity metadata 재사용 |
| 변경 원전 | 기존 immutable source 16개 전문/Git blob 16/16. 이후 구체적인 중앙·REC·CR commit만 추가 확인 |
| 추가 원전 읽기 종료 | **2026-10-28 10:03:28.930649 UTC = 19:03:28.930649 KST**. 최초 branch cutoff를 이 시각으로 바꾸지 않음 |
| 다른 대화 | PersonalContext 새 검색 1회 실제 응답 **UNAVAILABLE**. 다른 대화 또는 자료 부재를 뜻하지 않음 |
| 첨부 | 이름 있는 첨부 20개, 435,180,795 bytes의 현재 manifest/hash. 이전 전체 파일 SHA가 없어 역사 byte identity는 주장하지 않음 |

Drive에서는 발견된 folder 63개 목록을 종료하고 선택한 WU root 14개에서 167회 recursive folder list로 **1,246 items / 1,093 files / 153 nested folders**를 확인했다. Queue·capped·error는 모두 0이었다. 동일 WU scope의 R13 대비 새 11 IDs는 모두 R13 S01–S10/FINAL 백업이며 removed 0, stable metadata changed 0이다. 같은 baseline document filter 198개에서는 ID 추가/삭제가 0/0이었다. 별도 literal query의 162개 결과를 36개 삭제로 해석하지 않았다.

Dropbox root 526 entries와 dossiers recursive 5,331 rows/9 pages를 terminal까지 읽었다. 동일 WU root 13개는 **1,132 items / 1,006 files**이고 새 11 IDs는 R13 백업뿐이며 removed 0, stable metadata changed 0이다. 이전 immediate-parent 3,509개와 이번 recursive 5,331개의 차이를 신규 객체 수로 세지 않았다. 별도 BASS_BACKUPS 224개, bianchi 39개, PHYS69 1개 scope도 명시했다.

R11/R12/reconciliation/R13의 **34 ZIP pairs**는 이름·크기 34/34, 현재 R13 receipt의 provider ID/크기는 11/11 일치했다. 이는 metadata readback이며 이번 조사에서 새 upload ACK를 얻었다는 뜻이 아니다. **조사 중 archive original GET=NOT_RUN**, 새 upload ACK=0이었다. 실제 필요한 B3h anchored handoff text 1개를 읽었으며 이 text fetch를 ZIP original GET으로 바꾸지 않는다. 첨부에서는 세 ZIP의 central-directory 이름·크기를 기존 7/8/38 members 기록과 대조했고, 정책 TXT 네 개를 이번에 읽었다. 이전 PDF 첫 두 페이지 읽기 근거를 재사용했으며 모든 PDF 본문을 새로 완독했다고 하지 않는다.

근거: [intake 종합](authority/intake/SYNTHESIS_KO.md), [branch census](authority/intake/github/PUBLIC_BRANCH_CENSUS.json), [PR 추가 원전 종합](authority/intake/pr/SYNTHESIS_KO.md), [고정 원전 manifest](authority/intake/pr/POST_CUTOFF_SOURCE_MANIFEST.json). 상세 backup/첨부 scope와 실패·unavailable 분류는 `authority/intake/backups/`의 원기록을 따른다.

### 구체적으로 바뀐 의존성의 판정

| 의존 원전 | 실제 최신 내용 | WU에 적용한 한계 |
|---|---|---|
| 중앙 `66ef9a0147a0573b77e74e151dc280ba2bd4b64c` | 3 HE observation의 TANGENT13 참조 변경, central 28/88·HE delta 0. 직접 읽은 HE-EXP-NUCLEAR patch는 SOURCE_INPUT_PENDING과 WU source owner를 유지 | Full DAG byte identity=false. 3 HE 밖 104 numeric spelling 변화의 exact-value 동일성은 CR qualification을 귀속하고, 저장된 lexeme 104쌍을 Decimal로 104/104 대조. 전체 1.64 MB DAG/9 WU 객체를 독립 재검증했다고 하지 않음 |
| REC `6f4aa1a331019c957ce6748969f027160833b471` | 실제 R5_ACK **5/20**, PR146의 R1/1/20 본문은 stale. Fixed CONTRACT 전문 GET 1회. Signed incoming FULL electron source-point field, saved writers 132, query 313/endpoint 626 | physical **0/313**. Autonomous full-state field, whole-domain defect, model discrepancy, initial error, positive tube 미완. HD reactive array 또는 WU physical consumer로 전용하지 않음 |
| CR `649f8316aedc37b94eefa36eb9a8f22e175691b8` | C05 production/control/reference/plot **authored·static-reviewed freeze**. PR114 R01 본문보다 최신 | Runtime PASS가 아님. 48 small-oracle/9 conditional native-cap은 authored inventory. Conditional consumer를 WU physical binding으로 올리지 않음 |
| BASS PR225 HEAD `5e7b9e30961304870360f05c7447f66b9887ffd0` | Frozen source `4c3614006ba8408196ee83c46240f7d48a7b50a6`와 현재 본문의 **18/20**, distinct-author R6/C9 **NOT_RUN** 일치 | central delta 0, physical radii/global completion null, L4=false. Conditional bounds를 물리 13자리 정확도로 바꾸지 않음 |

BASS anchored layer의 18/20 hold, BF3-D/integration의 Python-oracle 및 upper DAG 8/15, REI의 saved-history figure route 2/7, finite-thermal 15/20과 그 안의 이전 atomic 20/20, represented-EOS의 recipient/native25/physical-radii 미결도 각각 원래 scope로 구분했다. REC native-path 20/20과 BGJET 19/20의 physical 0/313, VigilODE scoped tests와 broad-production HOLD를 구분했다. 이 원전들은 검사 범위에서 새로운 WU 물리 결속을 제공하지 않았다. **전역 자료 부재를 주장하지 않는다.**

## 3. SciSpace·Exa·Wolfram의 실제 연구 사용

SciSpace 검색 1회에서 10 paper records, Exa 검색 1회에서 8 results를 받았다. Exa fetch 1회는 primary URL 세 개를 요청하여 본문 두 개를 받았고, DOI 하나는 **HTTP406 실패**였다. 결과 개수를 본문 완독 수로 표시하지 않는다.

Leroy의 Bernstein subdivision/minimization 논문에서 coefficient hull·de Casteljau restriction·bounded subdivision 문맥을 읽었고, Farouki의 저자 호스팅 강의 슬라이드에서 positive basis·derivative differences·degree elevation 등을 대조했다. 강의 슬라이드를 관련 journal article 전문으로 표시하지 않는다. Farouki–Neff 문헌은 search highlights 및 실패한 fetch 범위로 한정했다. Exponential-integrator의 phi 정의와 polynomial forcing 문맥은 R13의 실제 읽기 기록을 재사용했다.

이 고전 도구를 WU의 staircase memory에 결합하는 source-vertex preprocessing, positive Simpson B3, critical-root 96 bisections, 명시적 gap 및 finite work 계약은 이번에 직접 유도했다. 문헌 전반의 독창성 또는 broad strong no-go를 주장하지 않는다. 원문 URL·읽은 절·응답 hash와 짧은 요약은 [LITERATURE.json](authority/literature/LITERATURE.json), 식–코드 연결은 [EQUATION_CODE_MAP.json](theory/EQUATION_CODE_MAP.json)에 있다.

Wolfram topic context를 실제 사용한 뒤, 동결한 새 CAS script를 **한 번** 실행했다. Beta 16개, Simpson/product/elevation/derivative/restriction/chain-factor 6개, reversal 4개, controls 6개가 exact zero였다. 실제 submitted code는 **3,551 bytes**, frozen script와 byte-identical, 추가 trailing LF 0이다. 이번 반환 warning은 0, tool wall은 8.877초, CPU는 null이다. 이것은 finite symbolic corroboration이며 전체 구현 검증 또는 physical closure가 아니다. R11/R13 경고 원인 NOT_ESTABLISHED를 이번 결과로 고치지 않는다.

## 4. 유지한 물리·비교 전제

고정 K, pi, destruction d와

\[
H=\pi d^T-\operatorname{diag}(d),\qquad A_w=K+wH
\]

를 유지한다. Full certified w box, 모든 시작시각, zero-mass l1 residual, 길이 tau의 full-A contraction 및 짧은 나머지의 nonexpansiveness가 전제다. Nominal K rho를 full A로 직접 이식하지 않는다. R11의

\[
q_{add}=\min(1,q_K+\tau M_w\|H\|_1),\quad b_H=\|H\|_1/2,
\]
\[
q_{minor}=1-e^{-b_HM_w\tau}(1-q_K)
\]

는 기존 채택 근거로 보존하며 이번에 다시 실행하지 않았다.

\[
h(a)=q^{\lfloor a/\tau\rfloor},\quad h(0)=1,
\qquad 0\le q\le1,
\]
\[
\mathcal R(t)=h(t-t_0)R_0+\int_{t_0}^t h(t-s)g_r(s)\,ds,
\]
\[
\mathcal E(t)=e^{d_c(t-t_0)}E_0+
\int_{t_0}^t e^{d_c(t-s)}[c\mathcal R(s)+g_e(s)]\,ds.
\]

R forcing memory는 원래 t0에서 시작해 source·observation·kernel 경계를 지나 계속 보존한다. q=0에서도 h(0)=1이고 fresh forcing을 버리지 않는다. c≥0와 signed d_c는 horizon 전체에서 고정한다. `E=abs(eta)`, coarse l1=4E이며, raw lower는 **chosen-rational-q ideal comparison의 lower**다.

Forcing은 source cell마다 quadratic polynomial이고 경계의 one-sided 값이 달라도 된다. 이 polynomial이 실제 nonlinear forcing을 whole fine/coarse domain에서 지배한다는 premise는 별도로 필요하다. Source/state/clock hash와 certificate의 검사는 그 입력 선언을 결속한다. Polynomial sample 통과만으로 실제 물리 premise를 만들지 않는다. Native v=UNSPECIFIED, MISSING_NOT_ZERO, TIQM/SQM의 구분을 보존한다.

## 5. 새 수학적 구성과 구현

원래 cell의 normalized coordinate u에서

\[
g(u)=b_0(1-u)^2+2b_1u(1-u)+b_2u^2
\]

를 받는다. Endpoint와 convex interior minimum의 exact 검사로 전체 비음수성을 판정하므로 signed b1도 허용한다. 그 뒤 gr/ge의 모든 strict interior vertices를 union하여 분할한다. Concave maximum vertex도 포함한다. 각 effective piece에서는 두 source가 monotone이어서 restricted B2 coefficients가 모두 비음수다. 원래 cell당 최대 세 조각이며 원래 source hash는 바뀌지 않는다.

비음수·비감소 cubic의 B3 coefficients가 항상 비음수라는 추론은 성립하지 않는다. 실제 반례

\[
P(x)=x^3/3-x^2/4+x/16=\int_0^x(s-1/4)^2ds,
\quad B_3=(0,1/48,-1/24,7/48)
\]

를 남겼다. 이는 한 중간 lemma의 반례이며 일반 불가능성 결론이 아니다. R14는 실제 overlap 적분에서 positive B3를 직접 만든다.

Effective knots의 k*tau translations와 observation knots를 합쳐 rational base grid를 만든다. 각 base cell에서 overlap endpoints L=max(a,t−(k+1)tau), U=min(b,t−k*tau)의 branch가 고정된다. D=U−L≥0, M=(L+U)/2에 대해

\[
I(t)=\frac{D(t)}6\{g_r(L(t))+4g_r(M(t))+g_r(U(t))\}
\]

는 결속된 quadratic의 **정확한 Simpson identity**다. Unknown forcing의 sample quadrature가 아니다. Positive B1×B2 product를 B3로 구성한 뒤 q^k를 곱해 더한다. Coefficient는 base cell마다 한 번 구축하며 endpoint·whole bound·rootbox·display가 이를 재사용한다.

Convolution F는 연속이고 initial hR0만 block 경계에서 downward jump할 수 있다. Actual right endpoint와 right left limit을 구분하고, closed-cell upper에 도달하지 않는 left-limit supremum도 포함한다.

Derivative quadratic은 degree reduction, endpoint roots, double root를 exact 처리한다. Rational derivative vertex에서 monotone branches로 나눈 뒤 strict sign-change branch의 미해결 root마다 최대 96회 exact bisection을 한다. Exact midpoint root는 조기 종료한다. 미해결 rational root가 rootbox에 남을 수도 있으므로 모든 box를 irrational이라고 부르지 않는다.

Rootbox에 de Casteljau restriction을 적용하여 midpoint lower와 hull upper를 결합하면

\[
0\le U-L\le M_B2^{-96}\le3C_{max}2^{-96},
\quad M_B=3\max_i|B_{i+1}-B_i|
\]

를 얻는다. Restriction derivative의 chain factor를 포함한다. Outward dyadic rounding이 더하는 간격은 최대 2*2^-128이다. Rootbox는 **E propagation clock에 넣지 않는다**. Irrational supremum을 exact rational 값이라고 표시하지 않는다.

E endpoint는 positive cubic coefficients Q_i와

\[
W_i(z,\Delta)=\Delta\int_0^1 e^{z(1-u)}{3\choose i}u^i(1-u)^{3-i}du
\]

를 사용한다. Positive z의 beta multipliers는 차례로 1/(n+4), 3/((n+3)(n+4)), 6/((n+2)(n+3)(n+4)), 6/((n+1)(n+2)(n+3)(n+4))이다. Negative z에는 W_i(z)=e^z W_(3−i)(−z)를 사용하고 d_c=0에서는 모두 Delta/4다. Subtractive phi cancellation 없이 dyadic128/Taylor96와 명시적 tail로 감싼다.

Whole E는 R의 whole upper와 ge의 positive hull로 만든 constant-forcing majorant 및 양 endpoint upper를 포함한다. 다음 cell에는 polynomial endpoint interval을 전달하고 느슨한 whole bound를 반복 전달하지 않는다. 독립 reference는 current production을 읽거나 import하지 않고 original-unsplit J0/J1/J2 primitives, exact power cubic, analytic rational/surd critical roots, Decimal160 monomial phi1..phi4를 사용했다. 자세한 증명과 판별 controls는 [PROOF_KO.md](theory/PROOF_KO.md), [EXACT_CONTROLS_KO.md](theory/EXACT_CONTROLS_KO.md)에 있다.

## 6. 판별 controls와 실제 자원

| Control | Exact 결과 또는 구별 |
|---|---|
| q=1, gr=s² / gr=s / gr=1, T=1 | (R,E)=(1/3,1/12) / (1/2,1/6) / (1,1/2) |
| Signed middle, gr=(s−1/4)² | b1=−3/16, vertex 1/4, R=7/48, E=1/32 |
| gr/ge vertices 1/4와 3/4 | Effective pieces 3, E=17/96 |
| One irrational maximum | sup R=1/3+sqrt(2)/6, E(2)=7/12 |
| Two critical roots | roots=(1±1/sqrt(2))/2, sup R=(95+sqrt(2))/48, E(2)=45/16 |
| Golden discriminant | sup R=(5sqrt(5)−3)/12, E(2)=2/3 |
| Double root / endpoint roots | 1/2 multiplicity 2, (R,E)=(25/12,23/8); roots 0,1, (13/6,35/12) |
| Initial q=0 jump | Actual R(1)=1/3, left-limit sup 4/3, E(1)=13/12 |
| Global memory q=1/2,T=5/4 | R=83/128, E=1249/6144 |

Signed ±d_c, near-zero d_c, shifted t0, discontinuous source, source/observation refinement, near roots, full capacity와 binding/resource/bit guards도 같은 고정 campaign에서 확인했다. 첫 세 synthetic controls의 동일한 시간구간의 source ordering s²≤s≤1 아래 quadratic endpoint의 감소율은 constant 대비 R=2/3, E=5/6, affine 대비 R=1/3, E=1/2다. **이 조건부 사례의 exact ratio**이며 보편적 raw 우위, 실제 물리 개선, speedup 또는 R11 capped 개선률이 아니다. Zero의 0/0 ratio는 null이다.

유한 입력 범위는 states 1..13, original source≤16, observation≤32, effective≤48, base≤512, full blocks≤8, input 256bits, derived 16,384bits, |d_c|*horizon≤16이다. ASCII signed integer 또는 signed p/q만 최대 2,048자로 받고 decimal/exponent/whitespace 문자열은 변환 전에 거부한다. 전용 runtime digit limit은 유한한 **6,000**, 출력 rational text는 최대 10,000자다.

Full work를 수학 계산 전에 precharge한다. 이 domain의 base 수에 대한 수동 upper는 473이고 guard 512는 보수적이다. Overlap upper는 512*48*9=221,184<250,000, root upper는 98,304다. 실제 original16/effective48/observation32/tau2/17/fullblocks8 fixture는 **base248, overlap107,136, nonempty8,916, root actual1,536/precharge47,616**이다. Direct work-helper boundary guard와 실제 domain fixture를 구분한다.

31개 사례 전체의 stored base cells는 334개, unresolved critical rootboxes는 23개였다. One/two irrational fixture의 최대 exact gaps는 각각 약 1.0958015047080374e-59와 1.3697518808850467e-60, 최대 outward dyadic whole-R widths는 각각 2^-128이다. 이 관측값으로 일반 gap bound를 바꾸지 않았다.

## 7. 독립 심사·교정·실패 이력

독립 R6는 새 증명의 18/18 의무에 `PASS_SCOPED_THEORY_R6`, 열린 중대 이론 지적 0을 기록했다. Code preflight는 14개 의무를 수동으로 검토했다. 최종 C9는 별도 저자의 실제 저장 결과·동결 identity·실행 원장·그림 심사이며 **18/18 의무, PASS_SCOPED_FINAL_C9, 중대 지적0**이다. 이후 metadata-only admission delta review는 **8/8 의무, PASS_SCOPED_ADMISSION_METADATA_DELTA, 중대 지적0**을 기록했다. 완료한 과거 심사를 반복하지 않았다.

| 교정 | 실제 발견·처리와 보존 |
|---|---|
| F01 | Reference의 primary status adapter를 실제 `PASS_SCOPED`에 맞춘 한 줄 교정 |
| F02 | 짧은 exponent text가 bit guard 전에 큰 정수를 만들 수 있는 finite-parser 결함을 static 발견. 위험 입력을 실행하지 않고 ASCII grammar를 변환 앞에 추가. 기존31 valid/source 값은 그대로, 43 guards에 lexical3개 추가해46 |
| F03 | Python default4,300 digits와 derived16,384bits의 최대4,933 digits 불일치를 교정. 유한6,000 runtime policy, 출력10,000char bound. 실제9,867-character 최대-bit serialization/parse roundtrip을 sole primary campaign 안에서 확인 |
| D01 | 더 이른 geometry-counter 의미 조율. 이전 snapshot은 기록된 patch로 **재구성**했으며 contemporaneous original 보존이라고 하지 않음 |

F02 전 production 9files, F03 전 11files와 reference의 교정 전 실제 source/author records를 보존했다. 기존31 fixtures의 수학적 값과 source SHA는 바꾸지 않았다. 과학 campaign 실제 실패는 0이다. Preflight finding을 execution failure로 바꾸어 세지 않는다.

## 8. 그림과 수치 인증의 구별

Saved-output renderer를 **1 process** 실행했다. CPU **2.567074초**, wall 약2.571720초, budget CPU10/wall30/AS1GiB, return0, timeoutfalse, rendering failure0이다. 새 과학·ODE 실행은 0이며 source results를 재계산하지 않았다. Root가 실제 두 PNG를 열어 제목·범례·겹침과 의미를 검토했고 `PASS_SCOPED_VISUAL`, 열린 중대 지적 0을 기록했다.

첫 그림은 음수 middle coefficient와 비음수 source polynomial, one/two critical roots, initial downward jump를 보여준다. 둘째 그림은 조건부 exact endpoint 비교, signed E의 저장 endpoint 연결선과 별도의 whole-cell upper bars, supremum gap/rounded width, 실제 full-capacity count를 보여준다. Root 표시점은 저장 box의 midpoint이며 96-bisection box 폭이 화면 해상도에서 보이지 않는다는 점을 명시했다. Filled actual endpoint와 open left limit을 구분한다.

저장 B2/B3의 binary64 평가는 display일 뿐이고 exact JSON이 수치 권위다. E endpoint 연결선은 전체 셀의 인증곡선이 아니다. Native9 physical plot을 재사용하지 않았고 R10 원래 sample readout을 수정하지 않았다.

| 그림 | PNG SHA-256 |
|---|---|
| `figures/R14_SOURCE_AND_EXTREMA.png` | `9e39a0b32303d6d961ae42d5c1b7beb6e101c0f48c97bc1d88fbac05fdcff49a` |
| `figures/R14_COMPARISON_AND_RESOURCE.png` | `d00caa01aebed90eff8ab7ecf1c3ed1c4bfc56e107927447380681e903459683` |

SVG 두 개, 표시 data, input identities, renderer source hash와 실제 process 기록은 [PLOT_MANIFEST.json](figures/PLOT_MANIFEST.json), [CAPTIONS_KO.md](figures/CAPTIONS_KO.md), [VISUAL_REVIEW.json](figures/VISUAL_REVIEW.json)에 있다.

## 9. 열 단계 게시·이중 백업

각 단계는 root가 expected-parent SHA를 확인하고 force=false로 연구 branch 및 draft PR150에 게시한 다음, 그 실제 source로 ZIP을 만들어 Drive와 Dropbox에 백업했다. 검증은 **로컬 ZIP CRC, 모든 member SHA-256, 양쪽 실제 upload ACK, 크기 일치**다. Provider archive original GET은 **NOT_RUN**이며 metadata/ACK를 provider 원본 byte 재다운로드 검증이라고 부르지 않는다. 자기 단계의 ACK는 다음 source와 PR150에 보존한다.

| 단계 | 이론·코드 실제 범위 | Workflow | 완료/DAG | Source commit | 게시·백업 |
|---|---|---|---|---|---|
| S01 | R1/C1 새 quadratic 계약·2 OPEN nodes | 2/20 | 27/44 | `bb960c3c293c34b4567873fb4328143b16301e59` | 실제 게시, Drive+Dropbox ACK2 |
| S02 | R2/C2 최신 원전·문헌·식–코드 종합 | 4/20 | 27/44 | `4dddf0bfc821547b7453694ba822ff10ea445d3c` | 실제 게시, ACK2 |
| S03 | R3/C3 양화·finite parser 계약 교정 | 6/20 | 27/44 | `cba31d38f97579968da7abe5a976d116227bd99d` | 실제 게시, ACK2 |
| S04 | R4/C4 구성·독립 경로·자원 고정 | 8/20 | 27/44 | `fbea4a28d68f74f1e1e561446998f50da38b0f59` | 실제 게시, ACK2 |
| S05 | R5/C5 증명·구현·교정 완료,20-file freeze | 10/20 | 27/44 | `308a1f67e29339df4df1bcf04ae61d24f3984b33` | 실제 게시, ACK2 |
| S06 | R6/C6 독립 R6·primary1회 | 12/20 | 27/44 | `47c0ae15c19de624ec2838231fccf3119e6a63b4` | 실제 게시, ACK2 |
| S07 | R7/C7 독립 reference1회·CAS1회 | 14/20 | 27/44 | `f80151577a8cfe6998ff06c594eba13f8b30ef53` | 실제 게시, ACK2 |
| S08 | R8/C8 saved-output 분석·그림·actual visual review | 16/20 | 27/44 | `17464ac63bae5840390746db855e231595d4bd9d` | 실제 게시, ACK2 |
| S09 | R9/C9 독립 최종 심사·조건부2노드 채택 | 18/20 | 29/44 | `dfdefe47ef0c28ae94f6e6727d3230ceed5c356d` | 실제 게시, Drive+Dropbox ACK 2/2 및 크기 일치 |
| S10 | R10/C10 보고서·handoff·전달 종결 | 20/20 | 29/44 | `75a3bdbcba5113e4a4b94444c4ac6d6b08cc4871` | 실제 게시, Drive+Dropbox ACK 2/2 및 크기 일치 |

S08의 actual ZIP은 `WU_MOLECULAR_R14_S08_SOURCE_20261028_17464ac63bae.zip`, **1,589,134 bytes**, SHA-256 `978b8a7af4f790267bcb0b6874cb00c21906657ffd2c658fca29739fbe9ab05a`다. Drive ID `1xUg481Ui3HqU8_jXQk-QPd8uOqQfeuRM`, Dropbox ID `id:BSpOijBcT10AAAAAAEFU4A`의 실제 ACK와 크기 일치를 확인했다. S09의 actual ZIP은 `WU_MOLECULAR_R14_S09_SOURCE_20261028_dfdefe47ef0c.zip`, **1,621,378 bytes**, SHA-256 `8120edda13336f18f1b14237729299d664cd0d1b55c3c838128ea0f4e7eb2a57`이며 Drive ID `1LnYpfqVpkT7Yuv4zA6auj2ynI4J-eMJ-`, Dropbox ID `id:BSpOijBcT10AAAAAAEFtZw`의 실제 ACK2/2와 크기 일치를 확인했다. 전 단계별 tree/ZIP identity/provider receipt는 [PUBLICATION_INDEX.json](delivery/PUBLICATION_INDEX.json)이 기준이다. FINAL 자신의 영수증은 이 source 밖의 PR150/종료 응답에 기록한다.

## 10. 보존한 이전 단위와 종료 경계

R13 FINAL `0e6282010665bc9075e073cfd144c226d29e449b` / tree `8279b6ca9716c73a1299302f77de247e9285ab36`를 출발 identity로 재사용했다. R13 S09 `37db6e1fdb915b85d7547b77e3c01fa15218b193`의 57-file payload SHA-256 `aed8a6d7e58889de248ee88f75c2a46a7418462f4e3908393d72b64e908c6563`를 변경하지 않았다.

| 단위 | 보존한 실제 결과·한계 |
|---|---|
| R13 | primary311/reference125/components8,408/CPU1.334749/frozen14. CAS25zero+Power::infy3/General::messages, QUALIFIED·원인 NOT_ESTABLISHED. F01/F02 old bytes NOT_PRESERVED, F03 최초 후처리 실패와 교정 보존 |
| R12 | primary531/reference317/components133,502/CPU4.202434/frozen30. CAS24zero+messages, QUALIFIED·원인 미확정. Display 교정 이력, provider original GET=NOT_RUN |
| R11 | primary214/reference900/components19,195/CPU1.477435/frozen18. Exact11,239/Decimal4,868/saved sample3,088. 각 과학 실행1회. CAS15zero+warnings, QUALIFIED·원인 미확정, submitted script+LF1 |
| R10 | primary175/reference469/components9,860/CPU0.511886/frozen14. 최초 후처리 ID 실패와 DOC01/META02 종결, provider original GET=NOT_RUN |
| R8 | Original reference726/727 PASS+1FAIL와 별도 exact phi24/24 PASS를 모두 보존 |

R11 capped endpoint 1,544성분은 R10 capped와 exact equality이며 추가 개선0%다. Raw endpoint worse는 192/384/384/384성분이었다. Whole-E의 작은 개선은 nonlinear166/192셀·최대0.000300669129102%, coarse defect172/192셀·최대0.000327216506710%이고 Native whole-E는 같았다. 반응 사례 첫 R whole 차이는 각각2^-128이다. Native9의 qK=0.008346121460629307, q_add=0.008455451249964609, chosen q=0.008400328633818224는 Native K+synthetic conditional reaction fixture이며 physical closure가 아니다.

R10 원래 sample readout **4.0013206434938575e-12**를 그대로 둔다. R11 최대 초과 **4.001332174731647…e-12**, 고정 tolerance **4.377656370786352e-11**, strict sample containment=false·upper 초과349성분도 그대로 둔다. R14 Decimal83과 섞지 않는다. R11 F01/F02, 첫 PNG 실패 bytes와 원인 미확정, S08 incidental temporary와 S09 실제 삭제 기록, R11 입력 복구용 Drive GET과 provider archive original GET=NOT_RUN의 구분도 유지한다.

R14 primary/reference/CAS remaining은 0/0/0이고 R13/R12/R11/R10/R9/R8/R7/R6/PHYS91 allowance 증가는 모두0이다. Global remaining과 full historical CPU는 null이다. **현재 두 노드의 종결 뒤 새 연구·코드·CAS·ODE·그림 실행을 자동으로 시작하지 않는다.** 향후 실제 새 HD array 또는 named physical consumer가 제공되면 새 사용자 지시와 별도 유한 계약 아래 입력 결속을 우선한다. 재개를 이유로 완료 과학·ODE·독립 심사를 반복하지 않는다.

허용된 게시 권한은 root의 expected-SHA/force=false 연구 branch·draft PR150, Drive+Dropbox 백업이다. Main merge와 다른 owner repo 쓰기는 포함하지 않는다. 다음 대화용 구체적 identity·읽기 순서·중지 조건은 [HANDOFF_KO.md](HANDOFF_KO.md)에 있다.

## 11. 실제 S10 영수증과 최종 source 범위

S01–S10 **10/10 단계 실제 게시·이중 백업**, 실제 provider ACK **20개**를 이 source에 결속했다. S10 ZIP `WU_MOLECULAR_R14_S10_SOURCE_20261028_75a3bdbcba51.zip`, **1,667,476 bytes**, SHA-256 `878dc1a89763bcd07797b7abd04d16395a9f1d162177279b3f03cd0c372b473d`이다. Drive ID `1nL3eLnzRpF0NGmmGtyr-xfLsrG4pcg2W`, Dropbox ID `id:BSpOijBcT10AAAAAAEF8-Q`이며 양쪽 실제 ACK와 크기가 일치했다.

FINAL ZIP은 새 R14 leaf와 현재 AGENTS, 이전 단위의 immutable 참조를 포함한다. 새 R14 과학 코드·입력·결과는 자체 포함하며, 전체 역사 repo의 모든 파일을 복원하는 archive라고 하지 않는다. FINAL 자신의 commit/tree/ZIP/ACK는 생성·업로드 뒤 PR150과 종료 응답에 외부 기록한다. 현재 source의 과학 payload105파일은 S09 이후 변경0이다.
