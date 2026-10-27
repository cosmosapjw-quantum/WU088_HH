# WU088_HH R5 연구 결과: 분자 상태 축약의 동적 오차 보증

작성일: 2026-10-27 UTC. 대상 PR150 / research/provider-registry-20261025.
이론 R1–R10 및 코딩 C1–C10의 새 과학 단위는 WU_MOLECULAR_DYNAMIC_LIFT_R5다.

## 1. 판정과 완료 범위

이론과 코드는 각각 독립 검토를 통과하여 새 scoped 노드 2개를 채택했다.
현재 로컬 DAG는 **11/26**이다. 기존 R4의 24개 노드 객체와 9개 완료 판정은 그대로이며,
새 이론 1개와 구현 1개만 분모·분자에 추가했다. 중앙 DAG 완료 증가와 물리적 admission 증가는 모두 0이다.

새 성과는 명시된 유한 상태 모델에서 population 총량, 상태 분포 잔차, 축약 총량 오차를 동시에
제어하는 일반 n 정리와 exact BigInt rational 구현이다. 실제 HD 원자료의 제한된 전이 그래프에는
별도의 finite-block 수축 보증을 적용했다. GL2022 상태별 destruction 배열과 실제 소비자는 여전히 입력 의존성이다.

연구 내용 20단계와 Git/Drive 텍스트 checkpoint 10개를 별도로 기록한다.
원본 ZIP의 Dropbox·Drive 이중 게시 및 양쪽 원본 바이트 readback은 실행 호스트 장애로 미완료다.
R10/C10의 완전한 전달 종료는 이 조건이 충족된 뒤에만 표시한다.
기존 R4의 DAG9/24, workflow18/20, S10 ZIP 미완료도 유지한다.

근거: [SCIENTIFIC_ADMISSION.json](SCIENTIFIC_ADMISSION.json),
[THEORY_ADMISSION.json](theory/THEORY_ADMISSION.json),
[DAG.json](DAG.json), [WORKFLOW_RECORD.json](WORKFLOW_RECORD.json).

## 2. 실제 조사 범위와 재사용 결정

최초 조사에서는 접근 가능한 owner 저장소51개, branch ref2,349개,65페이지를 확인했다.
최종 root 재조회(10:34:41–10:35:32 UTC)는 **51개/2,352refs/65페이지**이며 모든 저장소의 마지막 페이지를 확인했다.
공개35개/1,869refs/47페이지와 비공개16개/483refs/18페이지다.
공개 조사 파일에는 비공개 저장소의 이름·브랜치·SHA를 게시하지 않는다.
WU 자체는 159개 refs(100+59)를 확인했다.

이것은 branch 목록 전수 조사이며 2,352개 tip의 모든 파일을 읽었다는 뜻은 아니다.
WU 최근 PR8개, 관련6repo 최근PR 각5개와 관련 분기, 최신 계약·admission·handoff를 실제 읽어
이번 변경의 근거와 중복 계산 여부를 판정했다. 현재 대화에서 Personal Context는 사용할 수 없었다.
접근 불가능한 대화 이력, 노출되지 않은 로컬 초안, 일반 이름으로만 저장된 미색인 파일의 보편적 부재를 주장하지 않는다.

백업 조사에서는 WU Dropbox 직접 목록555개를 terminal까지, Drive 직접 목록586개를 확인했다.
Drive 도구는 terminal flag를 노출하지 않았다. 관련 Library 최근 metadata1,231개/7페이지는 terminal까지
확인했지만 metadata 기반 이름 검색으로 모든 본문이 조사됐다고 보지 않는다.
이 조사 시점의 최신 WU 원본 보관물은 R4 S09이며, 새 R5 native text document는 조사 이후 생성됐다.

### 최신 관련 결과를 종합한 결정

| 대상 | 실제 확인한 pin/범위 | WU에서의 처리 |
|---|---|---|
| REC | d6dbe39a4923439547c01695d9020ba39367ea90, HD parser/source와 완료된54DB/24LTE | 원본 바이트·결과 재사용, 재실행0 |
| REI | 157a41919e5503ef8def183769a61167b2bd15b3,20단계 내용,3189검사PASS | overall RESOURCE HOLD 유지; provider C9 pending, physical state update false |
| BASS | 29dcf5ab94ae8b84bf8e3f31dddb31ce719929b1, B3h native incoming-photon tube/uncollided transport | scoped 결과 인정, molecular destruction 공급으로 해석하지 않음 |
| CR | 2776752de6952f60d8d690a128f33fec4df2c57b | 기존 finite causal-clock provider 범위, 후속 C9/C10 의존성 유지 |
| HE | ac6042a6b0610b09d0576538767ee0299389a5eb | 기존 조건부 provider 범위 유지 |
| VigilODE | 3064d453091af1dec7f99f0c8afabd98b447ea34 | adapter/profile audit; physical tube 또는 HD rate admission 아님 |

REI의 최신 admission은 3189/3189 수치 PASS와 자원 HOLD를 동시에 기록한다.
그 작업의 planning known15.077490885가 cap14.99를 넘었으므로 WU의 새 예산으로 이전하거나
HOLD를 PASS로 바꾸지 않았다. 중앙 working32/88, declared27/88, 이번 WU delta0의 분모는 로컬26과 다르다.

최종 재조회에서 BASS DV2-B frozen 및 DV2-C expanding Bianchi-II 브랜치2개와 CR proper-injection 브랜치1개가 새로 발견됐다. 각 고정 commit의 OPERATOR_CONTRACT 또는 THEORY_KO.md를 실제 읽었다. BASS 두 계약의 independent model review는 NOT_RUN, production은false이며, CR은 R05 proper-time source/return 유도 단계에서 donor100K와 recipient10000K 불일치를 유지한다. 이 결과들은 WU HD destruction 배열을 공급하지 않는다. [추가 브랜치 근거](authority/NEW_BRANCHES_FINAL_ADDENDUM.json).

원 조사 파일은 보존 도구가 ACK 없이 중단되어 byte-identical 회수에 실패했다. 그 예상 hash와 실패를 유지하고, root가 새로 읽은 완전한 공개목록을 [OWNER_BRANCH_INVENTORY_PUBLIC.json](authority/OWNER_BRANCH_INVENTORY_PUBLIC.json)에 게시했다. 최초2,349개와 최종2,352개 snapshot을 합쳐 하나의 원자적 시점으로 주장하지 않는다.

조사 당시 pin과 후속 변화는 [SURVEY_SCOPE.json](authority/SURVEY_SCOPE.json),
[LATE_PARALLEL_DELTA.json](authority/LATE_PARALLEL_DELTA.json),
[FINAL_PARALLEL_SNAPSHOT.json](authority/FINAL_PARALLEL_SNAPSHOT.json)에 구분했다.

## 3. 새 이론: exact projection에서 동적 상계까지

column-conservative Metzler K, 비음수 h,d,f,x(0), 확률벡터 pi를 가정한다.
f는 full/coarse 모델이 공유하는 prescribed source다.

\[
x'=Kx-hDx+f,\quad D=\operatorname{diag}(d),\quad
X=\mathbf1^Tx,\quad r=x-\pi X,\quad Q=I-\pi\mathbf1^T.
\]

\[
\bar d=d^T\pi,\quad b=D\pi-\pi\bar d,\quad
B=\pi d^T-D,\quad L=K+hB,\quad
c=K\pi-\dot\pi-hb.
\]

그러면 정확히

\[
X'=-h\bar dX-hd^Tr+F,\qquad
r'=Lr+cX+Qf,\qquad F=\mathbf1^Tf.
\]

움직이는 pi의 -piDot X와 nonstationary Kpi X를 모두 보존했다.
B는 off-diagonal이 비음수이고 column sum이0인 generator다.
원래 population 방정식에 새로운 물리적 reset event를 추가한 것은 아니다.

일반 column generator A에 대해

\[
\delta(A)=\min_{i<j}
\left(A_{ij}+A_{ji}+\sum_{k\ne i,j}\min(A_{ki},A_{kj})\right)
\]

이면 zero-sum z에서

\[
\|e^{At}z\|_1\le e^{-\delta(A)t}\|z\|_1.
\]

기존 stochastic Dobrushin overlap 공식을 column convention으로 옮기고
작은 시간 step 및 semigroup 극한을 사용했다. 이 부분은 문헌 재사용이며 보편적 신규성을 주장하지 않는다.
단순 spectral gap이나 prefactor C>1인 다른 norm 상계를 이 delta에 그대로 넣으면 안 된다.

\[
k=h d_{\min},\quad a=\delta(L),\quad q=\|c\|_1,\quad
g=\|Qf\|_1,\quad b_0=h\bar d,\quad s=\tfrac12h\,\operatorname{osc}(d).
\]

비교계를

\[
M'=-kM+F,\quad U'=-aU+qM+g,\quad E'=-b_0E+sU
\]

로 두고 초기 상계를 맞추면

\[
0\le X\le M,\qquad \|r\|_1\le U,\qquad |X-\bar X|\le E,
\quad \bar X'=-h\bar d\,\bar X+F
\]

가 성립한다. 공통 파괴율 d+c0를 더할 때 q와 oscillation은 변하지 않고
delta(L)는 h c0만큼 증가한다. 따라서 공통 파괴 damping을 잃지 않는다.
h=0 또는 d가 모든 상태에서 같으면 같은 초기 총량에 대한 aggregate closure는 정확하다.

일반 n 증명은 구현에 참여하지 않은 별도 검토자가 실제 두 파일을 읽고 승인했다.
[증명](theory/DYNAMIC_LIFT.md), [R6 검토](reviews/R6_FINAL.json).
문헌: Gaubert–Qu, Dobrushin's ergodicity coefficient for Markov operators on cones,
[저자 제공 원문](https://www.cmap.polytechnique.fr/~gaubert/PAPERS/GaubertQuIEOTD14QuFinal.pdf).

## 4. 구현: 끝점과 구간 전체의 exact rational 보증

유한한 비음수 상수 계수와 Delta>=0에서

\[
M_*=M+F\Delta,\quad C=qM_*+g,\quad
U_*=U+C\Delta,\quad E_*=E+sU_*\Delta
\]

를 구간 전체 상계로 사용한다. 끝점에는

\[
M_+=\frac M{1+k\Delta}+F\Delta,\quad
U_+=\frac U{1+a\Delta}+C\Delta,\quad
E_+=\frac E{1+b_0\Delta}+sU_*\Delta
\]

를 사용한다. exp(-z)<=1/(1+z), 비음수 forcing 적분의 상계 및 단조 비교가 근거다.
시작 상계보다 작은 끝점 상계를 전체 구간 상계로 사용하는 오류를 피한다.
고정된 유한 계수에서 local O(Delta^2), 고정 시간 구간에서 1차 수렴이다.

시간 의존 계수를 적용할 때에는 k,a,b0의 유효한 구간 하계와 F,q,g,s의 구간 상계가 필요하다.
순간 표본으로 계산한 계수를 시간 구간의 보증으로 사용할 수 없다.

src/dynamic_lift.mjs는 decimal/fraction 문자열을 BigInt rational로 처리한다.
coefficients, projectedState, initialBounds, envelopeStep, envelope, contractionRate,
generatorFromEdges를 제공한다. 구현 검증 범위는1..9states, 반복 상한256steps다.
JSON은 정확한 유리수 문자열을 보존하며 approximate()는 표시용이다.
입력이 exact decimal이라는 사실은 원자료의 측정 불확실성이0이라는 뜻이 아니다.

현재 core SHA256:
8c86303793baa1fd01dcdbae93c521c13713c74d6658101f0d77b4ebe4538273

[API](coding/API.md), [이론–코드 연결](theory/THEORY_CODE_MAP.md),
[코드](src/dynamic_lift.mjs), [코드 동일성 및 수정 범위](verification/CURRENT_CODE_EQUIVALENCE.json).

## 5. 저장된 수치 결과와 오차의 분리

무차원 두 상태 fixture:
K=[[-1,2],[1,-2]], pi=(2/3,1/3), d=(1,4), h=1, x0=pi, t=1.
실제 HD destruction 계수를 넣은 population simulation이 아니다.

| Formation | 실제 residual L1 | 연속 U 상계 | 실제 aggregate 오차 | 연속 E 상계 | 256step 유리수 E 표시 |
|---|---:|---:|---:|---:|---:|
| f=0 | 0.05730673015 | 0.09744018373 | 0.05748532661 | 0.07973201007 | 0.08421485557 |
| f=(1,0) | 0.27828524054 | 0.33250708261 | 0.17298652229 | 0.19955911281 | 0.21090751373 |

f=0의 저장된 refinement:

| steps | 유리수 E 상계의 표시값 |
|---:|---:|
|8|0.25649642609|
|16|0.15969202577|
|32|0.11753301630|
|64|0.09808033326|
|128|0.08876731612|
|256|0.08421485557|

256step에서 연속 E와의 차이는0.0044828455040225035다.
마지막 두 격자의 초과 차이 비율은2.0155292084083016이며 f=(1,0)은2.014371808486894다.
이 값은 유리수 시간 이산화의 보수성과 수렴을 보는 지표다.
full/coarse 모델 차이, 연속 comparison의 느슨함, 이산화 초과분, 물리 입력 불확실성은 서로 다르다.
표의 소수는 outward rounding 결과가 아니며 exact endpoint는 results/PRIMARY.json에 있다.
이 분석을 위해 과학 계산을 다시 실행하지 않았다.

[저장 결과](results/PRIMARY.json), [분석](results/NUMERICAL_ANALYSIS.json),
[Wolfram 대조](verification/CAS_COMPARISON.json).

## 6. 실제 HD 자료에 조건부로 연결한 sparse graph

REC가 이미 확인한 LAMDA 원문2289bytes를 그대로 재사용했다.
source SHA256:
0c99fe168235d6d6dac3063093bbbe8b4a2ea15cca53c7e2987763c801fdaefb

이번 적용은 J0..8의9states, T100K, para-H2의9개 하향 전이에 한정한다.
pi는 Boltzmann weight의17자리 근삿값을 exact rational로 정규화한 선언 입력이다.
그 pi에 대해 inverse edge를 구성하여 Kpi=0을 정확히 맞춘다.
이것은 실제 thermal weight의 outward interval certificate가 아니다.
누락 전이는 MISSING_NOT_ZERO, vibrational state는 UNSPECIFIED로 남긴다.
기존 REC의 radiative frequency35Hz gate7/8FAIL도 물리적으로 해결됐다고 바꾸지 않았다.

이 공급된 그래프에서는 instantaneous delta(K)=0이다.
그러나 lambda=2max(exit rate), P=I+K/lambda의 P^8에 양의 공통 row 질량 eta가 있다.
단조 하향 경로와 상태0의 self-loop를 사용하여 exact rational eta를 구했고,
uniformization 및 e<3으로

\[
t_0=8/\lambda,\qquad
\rho=1-\eta\frac{8^8}{3^8\,8!}<1
\]

을 얻는다. 이는 homogeneous evolution에 대한 block 수축이다.
rho^(floor(t/t0))를 사용할 수 있지만 instantaneous a로 바꾸면 안 된다.
forcing이 있을 때에는 별도 convolution이 필요하다.

| 조건부 그래프 값 | 표시값 |
|---|---:|
|lambda|8.429541533035898|
|eta|3.073843341040988e-7|
|block time tau0|0.949043310202281|
|1-rho|1.949445348763252e-8|

tau=n_coll kappa_ref t, kappa_ref=1e-11cm^3/s를 사용했다.
실제 collider density가 결속되지 않았으므로 물리적 relaxation time을 산출하지 않았다.
이 보증은 작지만 엄밀한 양의 block 수축을 주며 최적 수축률을 주장하지 않는다.

[조건부 graph 증명](theory/HD_GRAPH_BLOCK.md), [정확한 graph 결과](results/HD_GRAPH.json),
[재사용 원본](authority/reused/lamda_hd_20261025.dat),
[공식 LAMDA 데이터](https://home.strw.leidenuniv.nl/~moldata/datafiles/hd.dat),
[공식 설명](https://home.strw.leidenuniv.nl/~moldata/HD.html).

## 7. 검증, 실제 발견한 오류, 수정 범위

| 근거 | 실제 결과 | 해석 |
|---|---|---|
|Primary V8 BigInt|188 assertions /8groups PASS|원래 core06d13f...의 실행 기록 유지|
|Source geometry|41 exact checks PASS|현재 선언한 source graph만 검증|
|독립 analytic prototype|56/56 PASS,14rows|저장된 원 결과 회수; 재실행0|
|Wolfram|21exact zeros,80자리 기준값|일반 증명의 보조 검산|
|Parser 수정 검증|20/20 PASS|기존 실행 전체를 반복하지 않은 targeted 검증|
|독립 재입력 확인|저장 endpoint3값 byte-exact|수정 전 실제 실패하던 경계 확인|
|독립 R6 수학 검토|PASS_SCOPED_GENERAL_N_THEORY|일반 n 증명; blocking0|
|독립 C9 코드 검토|PASS_SCOPED_AFTER_TARGETED_REPAIR|blocking0|

실제 발견한 구현 오류는2048자 문자열 제한이 프로그램 자신의256step 유리수 U/E 출력을
거부한 것이다. zero-formation 결과 길이는 M1235,U2310,E3382였다.
canonical integer/fraction을 먼저 파싱하도록 수정하고 decimal/exponent 제한은 유지했다.
연산·projection·coefficient·enclosure 본문은 byte-identical하다.
기존188 및41검사의 실행 코드를 새 코드로 바꿔 기록하지 않았으며,
동일한 numeric semantics에 대한 재사용 논리와20개 targeted 검사, 독립3값 확인을 연결했다.

Wolfram 첫 시도는 AssociationMap을 사용하는 결과 직렬화에서 실패했다.
실패 코드/응답을 보존하고 AssociationThread로 직렬화만 고친 두 번째 호출이 성공했다.
성공한 80자리 기준값과 binary64 closed-form 표시의 최대 상대 차이는1.740554113208687e-16이었다.
이것은 source의 물리적 불확실성 경계가 아니다.

Git create_blob 보존 호출3개는 성공 ACK 없이 지연되어 중단했다.
실제 승인된 create_tree(content) 경로로 증거를 회수했고 원본 내용의 blob/SHA256 readback을 확인했다.
처음 지연된 호출을 성공으로 처리하지 않았다.
상세: [실행 장부](EXECUTION_LEDGER.json), [C9 검토](reviews/C9_FINAL.json),
[원형 코드와 원 결과](verification/independent_two_state_provenance.json).

## 8. 자원 장부와 재실행 정책

Primary1회, source graph1회, 독립 analytic prototype1회, Wolfram 최초실패1회+직렬화수정1회,
관측된 parser오류에 대한 targeted20개 및 독립3값 확인을 기록했다.
과거54DB/24LTE/249compiler 검사를 재실행하지 않았고 물리 IVP, 새Q, activation도0이다.

계측된 V8 wall은 primary70444ms, source7ms, targetedrepair623ms, 독립saved3값257ms다.
비계측 prototype과 tool/transport/LLM 비용은 이 합계에 포함되지 않는다.
전체 CPU는 null이며0으로 간주하지 않는다.
성공 Wolfram selfCPU0.038076999999999916s, selfwall0.038211s는 알려진 부분만이다.
PHYS91 remaining[0,0,0], global remainingnull을 유지하고 과거 예산을 reset/transfer하지 않았다.
HH_R10=OFF, production=NOT_ISSUED, L4_ready=false다.

## 9. 단계별 게시와 백업

| 단계 | 수행 내용 | 완료 DAG | 실제 source commit | Git / Drive text |
|---|---|---:|---|---|
|R1/C1|계약·현재 위치|9/26|34ffc4554cbd847bcfec21459e5a5d01f37ec002|PASS / exact readback PASS|
|R2/C2|근거·재사용과 수식 연결|9/26|2ffb88562ea808413de9332cb2e116036a799d17|PASS / exact readback PASS|
|R3/C3|주장·수치 설계|9/26|998fa1adbc4078d81a8c49424898570a24b900a0|PASS / exact readback PASS|
|R4/C4|표현 탐색·실행 계획|9/26|dde0806dc6b22d20a93e8b904c4104e315a8b653|PASS / exact readback PASS|
|R5/C5|증명·구현|9/26|a49104da1491f20d087ddfafcdf60347aaeca16a|PASS / exact readback PASS|
|R6/C6|검증·관측된 오류 수정|9/26|eb59de011f7cc67d465cda8e84b598a5d17251d6|PASS / exact readback PASS|
|R7/C7|과학 해석|9/26|5293371425f383c2d329d0ef85472c5820bc5361|PASS / exact readback PASS|
|R8/C8|이론 채택·수치 분석|10/26|06d3acf39acdc385601e4d8e5811c545fb3b934f|PASS / exact readback PASS|
|R9/C9|최종 함의·독립 코드 검토|11/26|c9d902f9357cff67b218a1ad967e4a3b3402d854|PASS / exact readback PASS|
|R10/C10|최종 보고·handoff·전달 재개 계약|11/26|실제 S10 source는 후속 delivery/S10.json 및 PUBLICATION_INDEX.json|해당 영수증에 실제 결과 기록|


각 pair는 실제 expected-SHA, force=false Git 업데이트 후 HEAD readback을 했고,
변경된 파일의 정확한 UTF-8 본문과 byte count/SHA256/Git blob manifest를 native Drive 문서에
append한 뒤 텍스트를 다시 읽어 일치시켰다. 각 단계의 source commit과 후속 receipt commit을 구별한다.

백업 문서:
https://docs.google.com/document/d/1PaWDrK9J9kL28pFItRihuU8YrwSKhWRT7vEm_pIX4ic

텍스트 캡슐은 pinned R4 parent 위에 적용할 수 있는 exact overlay다.
전체 repo ZIP, Dropbox 업로드, 양쪽 원본 archive 다운로드 검증을 대체하지 않는다.
실제 Python/C++ service probe는 실행 환경 불가 오류로 process launch 전에 끝났고
desktop device도 Offline이었다. 호스트 복구 전 미완료 산출물은 원본 ZIP과 이중 byte-readback이다.

[최종 게시 인덱스](delivery/PUBLICATION_INDEX.json),
[전달 재개 절차](delivery/RECOVERY_PROTOCOL.md),
[준비한 packager](delivery/package_checkpoint.py),
[준비한 text recovery](delivery/recover_doc_capsules.py).
두 Python 스크립트는 호스트에서 실행하지 않았으며 실행 완료를 주장하지 않는다.
초기 단계의 ZIP을 나중에 생성할 때 실제 생성·업로드 시각을 기록하고 소급 완료로 쓰지 않는다.

## 10. 다음 연구의 정확한 입력과 handoff

우선 현재 R4/R5 archive delivery를 기존 과학 재실행 없이 마무리한다.
그 뒤 실제 GL2022 state-to-state destruction 원문 숫자와 source spin/support/energy convention,
실제 소비자의 x/pi, density, clock, formation, 상태별 destruction을 결속해야 물리 적용으로 나아갈 수 있다.

SciSpace와 Exa 조사에서는 GL2022 DOI10.1063/5.0128598,
EMAA DOI10.17178/emaa_hd_rovibration_805a7aa5, Desrousseaux2021 DOI10.1039/D1CP02564C를 확인했다.
EMAA metadata는 원 숫자 payload를 제공한 것이 아니며 excitation을 destruction으로 교체하지 않는다.
다른 논문의 spin factor를 GL2022에 자동 이식하지 않는다.
관련 실제 도구 호출 및 읽기 수준은 [primary-source 조사](reviews/INDEPENDENT_SOURCE_REVIEW_KO.md)에 있다.

숫자 입력이 계속 미확보이고 다음 작업이 별도 bounded unit을 허용한다면,
현재 근사 thermal pi를 엄밀한 interval weight로 교체하고 forced finite-block convolution을
구성하는 것이 구체적인 수학 후속 후보다. 이 후보는 이번26개 DAG에 추가하지 않았다.

[다음 입력 계약](followup/NEXT_INPUT_CONTRACT.json)과
[복사 가능한 handoff](HANDOFF_KO.md)에 정확한 pin, 재사용, 예산, 미완료 전달 조건을 기록했다.
