# WU088_HH R15 종합 연구 보고서

이론 **R1–R10**, 코딩 **C1–C10**의 요청된 한 단위를 완료했다. 과학 DAG는 **31/46**이며, 이번에는 조건부 이론·구현 노드 두 개가 추가 완료됐다. 기존44개 node object, 중앙/물리 채택 증분0을 보존했다.

- 과학 채택 소스: [`1ba1b0727cf3d5ba21931b0f3f14a2beae664f67`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/1ba1b0727cf3d5ba21931b0f3f14a2beae664f67)
- 과학 소스 tree: `0ce9b0de3546bf7ec06782bd70160879fa654827`
- Scientific payload: **70 files**, SHA256 `828888e952c15bd94d37d7dd30c0676df9470ca316bb1dbb8334c6c218b0e909`
- 현재 문서 생성 시점의 실제 paired checkpoint 백업: **10/10**, provider ACK **20**
- 문서 생성: 2026-10-28T12:04:18.838411+00:00; phase `FINAL`. 자체 commit·archive·provider receipt는 게시 후 다음 source 또는 PR150/최종 응답에 기록한다.
- [Draft PR150](https://github.com/cosmosapjw-quantum/WU088_HH/pull/150), branch `research/provider-registry-20261025`; expected-SHA와 force=false로 게시했다.

현재 상태는 위 과학 채택과 `WORKFLOW_RECORD.json`, `SCIENTIFIC_ADMISSION.json`, `delivery/PUBLICATION_INDEX.json`이 권위다. R1–R8 설계·증명·결과 파일의 당시 OPEN/NOT_RUN 표기는 작성 시점의 증거로 유지한다.

## 1. 이번에 완성한 연구

R14의 정확한 이차 forcing 결과를 재사용하고, 원래 Bernstein-B3 계수가 모두 비음수인 cubic forcing에 대해 **positive Bernstein-B4 global memory, 유한 작업량을 갖는 whole-cell supremum certificate, signed scalar 오차 전파**를 직접 유도·구현했다. 독립 원식 reference와 Wolfram 검증을 실제 실행하고 독립 C9를 마친 뒤 다음 두 노드를 `COMPLETE_SCOPED_CONDITIONAL`로 채택했다.

- `WU_HD_CUBIC_BERNSTEIN_FORCING_THEORY_R15`
- `WU_HD_CUBIC_BERNSTEIN_FORCING_CODE_R15`

R14 종료 시점은 **29/44**였다. 이번 두 노드를 OPEN으로 등록한 뒤 **29/46**으로 시작했고, C9 후 **31/46**으로 완료했다. 기존44개 node object는 R14 입력과 완전히 동일하다. 중앙 DAG의 완료 증분과 물리 채택 증분은 각각0이다. 이론·코드의 조건부 수용 근거는 `SCIENTIFIC_ADMISSION.json`, 실제 단계별 근거는 `WORKFLOW_RECORD.json`에 있다.

현재 사용자의 예산 증액 및 다음 전체 루프 지시를 `POLICY_DELTA.json`에 반영했다. 그 지시가 이전 R14의 미래 단위 허용량0을 이번 한정된 R15 단위에 대해 대체한다. 과거 소진된 실행량이나 다른 프로젝트의 잔여 예산을 복구·이전하지 않았다. 사용자 제공 workflow1.0.0에 설치된 정책1.3.0의 근거 재사용·구성적 서술·유한 독립 검토·분업 원칙을 통합했다.

## 2. 최신 저장소·대화·PR·백업 조사

조사는 접근 가능한 범위를 종료 페이지까지 확인하고, 실제로 읽은 원전과 재사용한 근거를 구분했다. 여러 서비스의 조회는 비원자적 snapshot이며, 아래 cutoff 이후 모든 외부 변경까지 고정됐다는 뜻은 아니다.

| 조사 대상 | 실제 완료 범위 | 해석 범위 |
|---|---|---|
| Owner 저장소·branch | 51 repos, 2,418 heads, 66 branch pages, 51/51 terminal, API error0 | 공개35repos/1,929heads, 비공개16repos/489heads는 집계만 공개 |
| 공개 branch delta | NEW8, MOVED8, REMOVED0, UNCHANGED1,913 | R14 공개 baseline09:03:58.811 UTC와 비교 |
| 변경 head의 최근 commit | 16 histories, 176 branch-relative records, 159 distinct(repo,SHA), terminal16/16 | 고정 head 및 cutoff 이후 metadata 범위; 전 역사 diff 완독 아님 |
| Open PR | 51 repos, 85 pages, 1,184개=public1,130+private54 | 모든 목록 terminal, duplicate/error0 |
| Recent closed/merged | 51 pages, cutoff 이후0 | updated 내림차순의 정의된 cutoff 범위 |
| 공개 PR delta | NEW4, CHANGED5, REMOVED0, UNCHANGED1,121 | 타 repo의 변경 PR body8개 전문, WU 현재 section 및 동일 과거 이력 재사용 |
| 선택 불변 원전 | branch lane21개 Git blob21/21, PR lane6개 Git blob6/6 | 서로 겹칠 수 있는 읽기 기록이므로27개 고유 문서라고 합산하지 않음 |
| Drive WU | 14 roots, 167 folder lists, 1,257items/1,104files/153folders | queue/cap/error0, 같은167 folder IDs 확인 |
| Drive 추가 범위 | general parent 최신1,000, folder-only27roots, 추가15roots/17lists/547items | general parent의 전 역사 목록에는1,000cap이 있음 |
| Dropbox | root530, dossiers5,381rows/9pages terminal | 같은 WU13roots에1,143items/1,017files |
| 기존 WU archive | 45쌍 name/ID/size45/45, R14 영수증11/11 일치 | metadata 대조; 모든 과거 ZIP을 새로 내려받은 것은 아님 |
| 대화 검색 | PersonalContext2회, WU4labels와 관련7labels 및 반환 pointers | label 중복 가능; 모든 대화 목록/전체 본문 API가 없어 전수 본문 완독 주장은 하지 않음 |
| 첨부 자료 | 20개, 총435,180,795bytes, R14 manifest와SHA/size20/20 일치 | 기존 PDF/ZIP 검토 재사용, 관련 정책 TXT 재확인 |

Branch 조회는 **2026-10-28 10:44:06.934–10:44:35.010 UTC**, PR 목록은 **10:45:18.741–10:45:34.190 UTC**, 백업 목록은 **10:45:01.661–10:49:12.998 UTC**다. 선택 원전 읽기는 branch lane10:47:58.501, PR lane10:49:20.441 UTC까지 진행했고, 구체적인 REI/CR 후속 commit은 별도 post-cutoff delta로 보존했다. 이 후속 읽기를 전체 census cutoff로 소급하지 않았다.

Drive의 같은 folder count와 현재 ID 대조는 모든 역사 파일 identity 불변을 의미하지 않는다. Private repo 이름·본문·개별 hash 및 대화 원응답은 공개 소스팩에서 제외했다. 구체적 목록, 읽기 범위와 변경점은 `authority/intake/{github,pr,backups}/` 및 통합 `authority/intake/SYNTHESIS_KO.md`에 있다.

### 서로 다른 프로젝트 결과의 통합

| 새 원전 | 실제 닫힌 결과 | 이번 WU 연구에 반영한 판단 |
|---|---|---|
| BASS_HE endpoint14 `ea497efe2dca…` | 같은 endpoint-zero 조건에서 비음수 even sextic의 feasible witness, local14/18 | 이전 quartic 배제의 차수 범위를 유지하고 고차 forcing의 양성성을 직접 구성 |
| BF3E 문서 `90b600519712…`, 코드 `60c1ebbb5ef6…` | 같은 finite collocation에서 retarded source memory9/15, targeted13tests/wheel PASS | 원래 초기 carrier와 global memory를 보존하고, 다른 operator의 인증 상수는 이전하지 않음 |
| REC `bc9fd57d41dc…` | HyRec FULL/H_STEADY의 source-point Fe=FH,132FH/264real/41,052virtual bitwise 일치, C9 완료 | Point 성분 검증과 whole-domain forcing/전체 trajectory를 구분; 실제 HD 입력으로 채택하지 않음 |
| CR energy-sum `3d9818b4b91d…` | E_i+E_j≤K 아래 double mass 최대화, primary123/control80/reference223 PASS | d 최대화와 witness의 cross C를 구분; 타 repo의 실패 및 예산 상태 보존 |
| CR cross `9ec654379074…`, closeout `9c0cc44c87ed…` | 다른 birth bin의 fractional matching, 3,201atoms/12,804source fields, native dual9/explicit primal3 | 목적량·source marginal·threshold identity를 명시하고 K20 실패/회복 이력을 보존 |
| REI directional `207491c2caa2…` | C8 저장 그림과 방향미분 검증,18/20 | stale PR 본문 대신 실제 불변 source 상태 사용; physical recipient/radius의 null 유지 |
| REI external/fast-selected | 201epochs QSS와 별도257epoch n/T 결과 | 서로 다른 clock/background 이력을 하나의 물리해로 합치지 않음 |
| VigilODE `64004e23042f…` | 원래 residual의 direct Bernstein 경계와 cyclic closure/trace 이론 | 독립 원식 power-basis reference를 채택; 모델 고유3/4,25/32 상수를 WU로 이식하지 않음 |
| HTT `679f2c5e434a…` | SYNTHETIC_UNIT_FIXTURE 기반 준비, source qualification 대기 | 실행 준비·수치 결과·물리 채택을 각각 구분 |

예를 들어 HE의 새 증인은 \(f(\mu)=(1-\mu^2)r(\mu^2)\), \(r(z)=1411/10000-z/4+33z^2/25>0\)다. 더 높은 차수의 실제 구성이 이전 낮은 차수의 제한을 그대로 일반화할 수 없음을 보여 준다. BF3E의 panel8/16/32/64 차이 약2.62e-9,1.64e-10,1.02e-11,6.39e-13은 같은 finite-collocation 문제에서의 관측이다. 그 targeted 성공과 별도 portable/native CI 실패를 함께 보존했다. REC의 small residual도 physical0/313 및 full-state/whole-domain 미공급 상태를 바꾸지 않았다. 이 구체적인 범위 구분이 R15의 입력 원뿔·full-A·clock 계약에 반영됐다.

백업 조사에서는 신규 BF3E ZIP217,005bytes를 실제 original GET하여 content-hash, ZIP CRC 및48개 manifest member를 확인하고 핵심 텍스트7개를 읽었다. WU의 이번 S09 복원 검증은 아래 전달 절에 별도 기록한다. 두 작업의 주체·시점·대상을 섞지 않았다.

## 3. 문헌과 요청 도구의 사용

**SciSpace** 검색1회에서10records, **Exa** 검색3회에서10+10+8=28records를 얻었고 primary URL3개를 실제 취득했다. 이는 중복 제거한 논문 수나 모든 검색 결과의 전문 완독 수가 아니다. **Wolfram**에는 동결된8,361byte source를 실제1회 제출하여 아래72개 항등식을 확인했다. Context 검색의 관련성이 낮은 QuantumFramework 문서는 근거에 사용하지 않았다.

Classical Bernstein/Descartes 도구는 [Mourrain–Rouillier–Roy의 원전](https://library.slmath.org/books/Book52/files/24roy.pdf) §2의 명제2.3/2.4/2.8과 Algorithm2.9, [Sagraloff의 원전](https://arxiv.org/pdf/1109.6279) Theorem2(P4)를 확인했다. [Sharma 강의노트](https://www.imsc.res.in/~vikram/poly-2012/descartes.pdf)의 해당 인쇄 페이지도 실제 열어 읽었다. Midpoint가 근인 경우의 parity 문구를 이번 zero-aware 규약으로 그대로 전용하지 않고, \(2u-1\)의 parent variation1/두 child variation0 사례를 남긴 뒤 필요한 부등식을 직접 증명했다. 이것은 특정 규약의 적용 범위 교정이며 분야 전체의 no-go나 오류 일반화를 뜻하지 않는다.

HD 원전은 [GL2022, J. Chem. Phys.157,214302, DOI10.1063/5.0128598](https://doi.org/10.1063/5.0128598)이다. Publisher 본문이 가리키는 실제 supplementary native array bytes를 이번에는 확보하지 못했다. Neutral H+HD QCT와 charged H⁺+HD SQM/TIQM을 구분한다. Figshare API의 off-target 결과도 전체 자료 부재의 증거로 사용하지 않았다. 문헌 위치·실제 취득 범위는 `theory/R2_LITERATURE_AND_REUSE_KO.md`, `authority/literature/`에 보존했다.

## 4. 재사용 가능한 이론 결과

고정 column-conservative Metzler \(K\), \(\pi\ge0\), \(\mathbf1^\top\pi=1\), destruction vector \(d\ge0\), 비음수 w box에서

\[
H=\pi d^\top-\operatorname{diag}(d),\qquad A_w=K+wH
\]

를 둔다. 실제 full-A evolution operator가 허용된 **모든 시작시각과 이력**에서 zero-mass norm의 길이\(\tau\) block을 q 이하, 짧은 remainder를1 이하로 보내는 certificate가 있어야 한다. Constant-w certificate의 범위를 switching histories로 자동 확대하지 않는다. 같은 source/state/norm/clock 및 whole fine/coarse-domain forcing bound를 사용한다.

원래 초기시각에서

\[
h(a)=q^{\lfloor a/\tau\rfloor},\quad h(0)=1,
\qquad
\mathcal R(t)=h(t-t_0)R_0+\int_{t_0}^{t}h(t-s)g_r(s)\,ds,
\]
\[
\mathcal E(t)=e^{d_c(t-t_0)}E_0+\int_{t_0}^{t}e^{d_c(t-s)}[c\mathcal R(s)+g_e(s)]\,ds
\]

를 계산한다. \(c\ge0\)는 비교 결합계수, \(d_c\)는 부호를 보존하는 scalar 계수다. \(E=|\eta|\), coarse \(l^1=4E\)를 유지한다. Source/observation refinement에서 적분 하한과 kernel의 나이를 재설정하지 않는다.

각 원래 source cell에 주어진 비음수 rational B3 계수와 exact event grid에서 cubic Simpson 항등식

\[
\int_L^U g_r(s)\,ds=\frac{U-L}{6}\left[g_r(L)+4g_r\!\left(\frac{L+U}{2}\right)+g_r(U)\right]
\]

을 쓰면 positive B1×B3 곱으로 비음수 B4 convolution이 된다. \(q^k\) 가중합과 초기 memory를 더해 한 번 조립한 \(P(u)=\sum_{i=0}^4B_i\mathsf B_i^4(u)\)에서 도함수 B3 계수는 \(4(B_{i+1}-B_i)\)다.

Exact zero를 제거한 sign variation에 대해 인접 평균 삽입과 삭제의 직접 논증으로 \(V_L+V_R\le V\)를 얻었다. 한 깊이의 mixed nodes는 최대3이므로 깊이D에서

\[
\mathrm{splits}\le3D,\qquad\mathrm{visits}\le6D+1.
\]

Mixed leaf를 단일근 분리구간으로 가정하지 않으므로 repeated root, split-point zero, rootless mixed coefficients를 함께 다룬다. Root-separation 가정 없이 D=96에서 **셀당288분할/577방문**으로 종료한다. Restricted derivative의 coefficient 관계로

\[
0\le U_{\rm exact}-L_{\rm exact}\le M_B2^{-96}\le4C_{\max}2^{-96},
\quad M_B=4\max_i|B_{i+1}-B_i|,
\quad C_{\max}=\max_iB_i
\]

를 얻었다. Dyadic128 outward 변환은 구간 폭을 최대\(2\cdot2^{-128}\)만큼 더한다. 이 식의 L은 whole-cell supremum의 하한이며, 모든 시각에 공통인 pointwise lower를 뜻하지 않는다.

Scalar 전달에는

\[
W_i(z,\Delta)=\Delta\int_0^1e^{z(1-u)}\mathsf B_i^4(u)\,du,
\qquad z=d_c\Delta
\]

를 사용한다. \(|d_c|(T-t_0)\le16\)에서 positive Taylor0..96, 첫 누락항97 이후의 ratio≤16/98 꼬리 상계와 \(W_i(z)=e^zW_{4-i}(-z)\) reflection으로 양·음·0을 처리한다. Whole-cell E는 상수 forcing majorant로 감싸고, 다음 셀에는 별도 polynomial endpoint interval을 전달한다. 초기 staircase memory의 실제 오른쪽 값과 왼쪽 극한도 구분한다.

**입력 범위는 원래 B3 계수가 비음수인 원뿔이다.** \((u-1/2)^2\)는 비음수 함수지만 그 B3 계수는 \((1/4,-1/12,-1/12,1/4)\)라서 이 입력 조건에 속하지 않는다. R14의 더 넓은 quadratic 전처리 결과를 별도 보존한다. 산출물의 R/E lower는 제공된 forcing bound로 정의한 이상 비교함수의 lower다. 실제 물리 오차에 대한 lower로 해석하지 않는다.

전체 증명은 `theory/PROOF_KO.md`, 간결한 재사용 정리는 `theory/REUSABLE_STATEMENT_KO.md`, 변수·단위·초기 조건·입출력·정밀도·실행 경계는 `design/R9_COMPUTATIONAL_CONTRACT_KO.md`에 있다. 학술적 최초성이나 새로운 strong no-go를 채택하지 않았다.

## 5. 실제 구현·검증·그림

Production은 exact rational positive Bernstein 경로를 사용한다. 독립 reference 저자는 production 구현을 읽거나 import하지 않고 공개 식과 입력 계약에서 원래 unsplit source primitive J0..J3, 다섯 내부 유리수 값의 power quartic 재구성 및 네 off-stencil 확인, exact squarefree/Sturm 비음수 판정을 구현했다. Signed scalar는 별도 Decimal160/512항 monomial-phi 경로로 계산했다.

| 검증 | 실제 결과 | 근거 |
|---|---|---|
| R6 정적 심사 | 24/24, material0 | `reviews/R6_STATIC_REVIEW.json` |
| Primary | 302/302,21models,75base cells,68guards,14depth rows | `raw/PRIMARY_RESULTS.json` |
| Reference | 302/302records,21models,오류0 | `raw/REFERENCE_RESULTS.json` |
| Reference 분류 | pure exact238,mixed exact/guarded21,guarded42,metadata-only1 | `reviews/C9_FINAL_REVIEW.json` |
| Decimal 비교 | guarded784/784; strict 포함 miss59, 예시50개 보존 | `verification/REFERENCE_ASSESSMENT.json` |
| Wolfram | 72고유 target의 exact residual0, 관측 warning0 | `raw/CAS_RAW_RESPONSE.json` |
| 동결 소스 | 30/30 유지 | `verification/FROZEN_FILES.json` |
| Scientific payload | 70파일 size/SHA256/Git blob 일치 | `SCIENTIFIC_PAYLOAD_MANIFEST.json` |
| 저장 그림 | PNG2/SVG2, root와 독립 C9 reviewer가 각각 실제 PNG2개 열람 | `figures/VISUAL_REVIEW.json`, C9 기록 |
| C9 최종 심사 | 20/20, material0 | `reviews/C9_FINAL_REVIEW.json` |

Pure exact238 records에는 exact 진단·integer·metadata 범주가 포함된다. 이를238개의 별도 수학 정리로 세지 않는다. 모든21 model은 `ARITHMETIC_CONTROL_PREMISE`이며 q=0도 산술 경계 대조군이다.

### Strict Decimal miss59건의 의미

Reference Decimal 값을 exact Fraction으로 바꾸어 원래 rational 구간과 비교하면59건이 구간 밖이다. 실행 전에 동결한

\[
10^{-80}\max(1,|\mathrm{reference}|,|\mathrm{lower}|,|\mathrm{upper}|)
\]

를 적용한784비교는 모두 통과했다. 첫 보관 예시는 z=0의 W1이다. Production은 exact singleton \([1/5,1/5]\)를 주었고, Decimal monomial-phi 조합은 유한 자리 연산으로0.1999…9990을 주었다. 해당 값의 strict miss와 fixed-guard 통과를 각각 남겼다. 이 예시의 원인을 모든59건의 개별 진단으로 확대하지 않았다. Decimal 부분은 `GUARDED_CORROBORATION_NOT_INTERVAL_REFERENCE`이며, exact rational·Sturm 판정과 구분한다.

### 대표 대조군과 관측 수렴

| 대조군 | 매개변수·결과 |
|---|---|
| 순수 cubic | g_r=t³,q=1,t0=0,T=1,R0=E0=0,c=1,d_c=0,g_e=0 → R(1)=1/4,E(1)=1/20 |
| 초기 memory jump | 위 cubic에 q=0,tau=1,R0=1 → 실제 R(1)=1/4, 왼쪽 극한/whole supremum=5/4,E(1)=21/20 |
| Canonical GLOBAL_MEMORY | q=1/2,tau=1/2,T=5/4 → R=2337/4096,E=12013/81920 |
| Signed/clock/domain | d_c=±16, nonaligned clocks, singleton, states13/source16/observation32/blocks8 등 |
| Derivative 구조 | simple/double/triple/endpoint/rootless/constant 진단 |

Canonical tau=1/2의 GLOBAL_MEMORY와 R4에 수록된 별도 tau=1 수동 예제를 혼용하지 않았다.

전체75base cells에서 splits677,visits1,429이며 셀당 최대는191/383이다. 고정 D=96 진단의 유리 임계점 예는 exact gap0,3splits/7visits, 증명 상계 약1.70920e-30이다. 비유리 임계점 예는 exact rational gap의 표시값 **3.8938557722194933e-60**, 증명 상계 **2.4980595331998706e-30**,191splits/383visits다. 실제 수용은 소수 표시가 아니라 저장된 rational 비교로 수행했다. 이 관측값을 모든 입력의 수렴률·CPU 보증으로 확대하지 않는다.

`figures/R15_comparison_envelopes.png`는 실제 endpoint/left-limit/whole-cell 경계를, `figures/R15_subdivision_convergence.png`는 저장된14depth rows의 gap과 작업량을 보여 준다. 두 SVG도 함께 제공한다. 그림 생성은 기존 결과만 읽었고 과학 계산을 반복하지 않았다.

## 6. 자원·실패 이력·남은 입력

실제 primary1/reference1/CAS1/renderer1회, 수정 재실행0, 새 ODE0회다. Primary OS CPU0.568891초, reference 약2.060271초, 합계 약2.629162초이며 imports·serialization을 포함한다. Renderer 약3.270585초는 별도다. Python3.12.14/Linux6.18.55에서 측정했다. Primary120초/reference180초 CPU 제한과 각각1GiB 제한 안에 종료했다. CAS CPU 및 실제 remote wall time, 전체 과거 CPU·전역 잔여 예산은 null을 유지한다. 현재 환경의 Fraction/C++ probe는 행정적 실행 가능성 확인이며 새 C++ 과학 campaign에 합산하지 않았다.

계약의 입력 cap은 states13/source16/observation32/base512/full blocks8, input256bits, production 및 저장 derived16384bits다. Reference의 미직렬화 Euclid/Sturm 내부에는 별도1,048,576bit guard를 미리 두었다. 실제 최대 내부 numerator/denominator1313/1302bits는 그 안에 있다. 최대 크기의 모든 입력이 이번 fixture의 비용으로 끝난다는 성능 보증은 하지 않는다. 두 미사용 repair reserve는 C10에서 소멸시키고 모든 base/repair/future allowance를0으로 닫는다.

실제 **GL2022 HD reactive array와 named physical consumer/state/density/clock는 INPUT_PENDING_IN_INSPECTED_SCOPE**다. Native v UNSPECIFIED, MISSING_NOT_ZERO, TIQM/SQM DISTINCT, HH_R10 OFF, production NOT_ISSUED, L4 false, central/physical delta0을 유지한다. 이는 검사한 입력 범위의 상태다.

다음 유용한 연구는 실제 native array와 단위·state order·support를 확보하여 명명된 consumer의 density/clock 및 full-A/whole-forcing certificate와 결속하는 일이다. 별도의 방법론 후속 후보로 더 넓은 pointwise-nonnegative cubic의 exact preprocessing을 제안했다. `NEXT_INPUT_CONTRACT.json`은 제안이며 새 노드·실행·예산을 만들지 않는다. 기존 원전의 identity와 전제가 유지되면 완료 검증을 재사용하고 실제로 달라진 의존 부분을 진행한다.

## 7. 실제 단계별 게시·이중 백업

이론/코딩의 같은 번호 두 단계를 S01–S10 체크포인트로 묶었다. 각 체크포인트는 실제 commit/ref 갱신과 Drive·Dropbox 완료 응답을 확인한 뒤 다음 체크포인트로 진행했다. 아래는 실제 받은 영수증이다.

| 체크포인트 | 완료 단계 | DAG | 불변 commit | Drive / Dropbox | ZIP bytes |
|---|---:|---:|---|---|---:|
| S01 | 2/20 | 29/46 | [`9003d45d710a`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/9003d45d710ac56497152055d31e2bef55f3f7fa) | [Drive](https://drive.google.com/file/d/1T54VMO2puvYnTfUzJ_BgbeUdZnM-Pj4q/view?usp=drivesdk) / completed ACK | 711,071 |
| S02 | 4/20 | 29/46 | [`e913e74867f8`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/e913e74867f8a3a5a69052e36e8bb6a2190b177c) | [Drive](https://drive.google.com/file/d/1wwvH427jVQ3JstuGIDgKFrlEOnsT5r4-/view?usp=drivesdk) / completed ACK | 732,605 |
| S03 | 6/20 | 29/46 | [`111d1d41ae2b`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/111d1d41ae2b9e2e3361708ac640fd25f60039c4) | [Drive](https://drive.google.com/file/d/1_VIJKjGX8IgxF6iZOKty3cApm_sCExiM/view?usp=drivesdk) / completed ACK | 761,523 |
| S04 | 8/20 | 29/46 | [`3dae38e813f0`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/3dae38e813f0ef952990698910d1481eee78357f) | [Drive](https://drive.google.com/file/d/1ljwA_z9ukiNBD8yfD1qFvL9NgbdSY5W3/view?usp=drivesdk) / completed ACK | 788,182 |
| S05 | 10/20 | 29/46 | [`050d4d870338`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/050d4d870338f8b6f639c36eaf22d4b62ef3aee9) | [Drive](https://drive.google.com/file/d/1GDebUrgSlmiPgbbm7r1t-8K8hYItoKFu/view?usp=drivesdk) / completed ACK | 910,789 |
| S06 | 12/20 | 29/46 | [`e868564bdfd4`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/e868564bdfd42df4ecbcf4e020eba700500c0031) | [Drive](https://drive.google.com/file/d/1FmlJtbSQbjv9rvczrVUUSvYTPtRXsw5O/view?usp=drivesdk) / completed ACK | 1,053,998 |
| S07 | 14/20 | 29/46 | [`2fd67bbcf51a`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/2fd67bbcf51a86d7f45a21da81f6b06572ba5b63) | [Drive](https://drive.google.com/file/d/1J1wRmp16meNhA0u13ihikzNld9uPA7H-/view?usp=drivesdk) / completed ACK | 1,087,482 |
| S08 | 16/20 | 29/46 | [`93355d9df88c`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/93355d9df88cb44c1c70778f4bf69ff1d2a2658c) | [Drive](https://drive.google.com/file/d/1PdKEn9aQotvxxMRO0HOv_umsv2Upernh/view?usp=drivesdk) / completed ACK | 1,584,994 |
| S09 | 18/20 | 31/46 | [`1ba1b0727cf3`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/1ba1b0727cf3d5ba21931b0f3f14a2beae664f67) | [Drive](https://drive.google.com/file/d/1HZY7hb1rNQGwkubSp8kROVKrtJoWYoqw/view?usp=drivesdk) / completed ACK | 1,623,172 |
| S10 | 20/20 | 31/46 | [`3331e8dcecc2`](https://github.com/cosmosapjw-quantum/WU088_HH/commit/3331e8dcecc250505b642b5c430a63045fa74d81) | [Drive](https://drive.google.com/file/d/1qXaIj8sbRu5GJlF8-2hEo-G3V8Kh3j2_/view?usp=drivesdk) / completed ACK | 1,642,976 |

S01–S10의10개 소스 ZIP과20개 provider ACK를 실제 확인했다. FINAL은 동일한 과학 결과에 마지막 전달 metadata를 보존하는 추가 소스팩이다. FINAL 자신의 영수증은 그 내부에 넣을 수 없으므로 PR150과 최종 응답을 따른다.

### 실제 복원 검증

S09 archive **1,623,172bytes**, SHA256 `9c9af8993a8783fd98b564941f713eb8d753fa5423ce3bb34510552bff5dd5ef`를 Dropbox original GET **1회**, HTTP200으로 직접 내려받았다. ZIP CRC PASS, source **243개**와 manifest를 포함한 **244members**의 크기·SHA256·Git blob이 모두 일치했다. Dropbox content-hash도 일치했다. 원격 GitHub의 S09 immutable tree에서 과학 payload70개 및 admission/DAG/C9/manifest의 blob·size를 다시 대조했다.

이는 S09 한 개의 실제 원본 복원 검증이다. 나머지 archive의 upload ACK, provider size readback, 생성 시 ZIP CRC/멤버 hash 확인과 구분한다. S09 복원은 과학 재실행0이다. 전체 역사 repository를 ZIP 하나에 넣은 것은 아니며, 각 R15 소스 ZIP의 범위는 현재 AGENTS와 자기완결적인 R15 leaf다.

실제 복원 근거는 `delivery/S09_RESTORE_VERIFICATION.json`, 원격 소스 대조는 `verification/REMOTE_SOURCE_IDENTITY_CHECK.json`, 모든 영수증은 `delivery/PUBLICATION_INDEX.json`에 있다. 짧은 수명의 원본 download URL과 private 응답은 공개팩에 없다.

## 8. 재개 지점

`HANDOFF_KO.md`의 복사 가능한 블록과 `NEXT_INPUT_CONTRACT.json`을 사용한다. 과학 채택 source S09와70파일 payload를 고정하고, 전달용 FINAL의 실제 head/archive/provider 영수증은 PR150 또는 이번 최종 응답에서 확인한다. 현재 완료 결과를 자동으로 재실행하지 않는다. 입력 identity나 전제가 달라질 때 영향받는 범위와 유한 계약을 먼저 정하고 실제 작업을 이어간다.
