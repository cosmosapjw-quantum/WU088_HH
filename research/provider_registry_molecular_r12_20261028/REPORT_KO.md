# R12 최종 연구 보고서 — 비정렬 forcing convolution과 닫힌 셀 인증

R12는 기존 R11의 모든 시작시각에 유효한 full-A block certificate를 보존하면서, 서로 정렬되지 않은 정확한 유리수 source·observation 격자의 forcing convolution과 닫힌 셀 cap의 세분화를 구성·구현했다. 실제 최종 C9는 **PASS_SCOPED_FINAL_C9**, 열린 중대 지적은 **0건**이다. 등록되어 있던 이론·코드 두 노드를 조건부 방법으로 채택하여 과학 DAG는 **25/40**이 되었고, 앞선 38개 노드 객체는 그대로 보존했다. [과학 채택](SCIENTIFIC_ADMISSION.json), [최종 C9](reviews/C9_FINAL_REVIEW.json), [DAG](DAG.json).

이번 네 저장 사례에서 R11 대비 추가 capped 개선은 **0%**다. 두 격자를 같은 기존 193점과 192개 닫힌 셀에 맞추면 capped R/E가 모두 기존 값과 정확히 같다. 새 성과는 비정렬 source의 실제 위치, 이동한 불연속 경계, 같은 시계의 cap 포함 관계를 보존하는 유한 구현과 그 검증이다. 이 관찰을 모든 입력에서 cap이 같다는 정리로 확대하지 않는다. [저장 출력 분석](RESULTS_KO.md).

이 문서가 읽은 workflow는 **20/20**이며, 실제 게시·이중 백업은 **S01–S10, 10/10단계**다. 과학 채택과 workflow, 실제 전달 완료 수는 각각의 기록으로 구분한다. 현재 문서는 `FINAL`용 패키징이며 새 연구 단위나 실행 허용량을 선택하지 않는다.

## 1. 채택 근거와 불변 식별값

| 항목 | 실제 기록 |
| --- | --- |
| 연구 단위 | `WU_NONALIGNED_CONVOLUTION_R12` |
| 연구 branch | `research/provider-registry-20261025` |
| draft PR | [PR150](https://github.com/cosmosapjw-quantum/WU088_HH/pull/150) |
| 과학 채택 S09 commit | `eb431411f6f0c4c9065edb0a5a11ce2c4bccf2fe` |
| 과학 채택 S09 tree | `55e7edd4daa438fb0838ad5141df0db4ff9464a2` |
| 과학 payload 파일 수 | 64 |
| 과학 payload SHA-256 | `dd66d34c0171ec215fa0e39525cc59f4c23f090b4a7deaa93b397c1f4a4417ba` |
| 실행 전 동결 파일 수 | 30 |
| 현재 포함한 마지막 완료 단계 | S10 |
| 그 단계의 실제 commit | `cf76cb0c7f7975327bca9801b5a5ded221b85b99` |
| 그 단계의 실제 tree | `5007997b05bcfd8a70cc1deaf72b80e2b02f389c` |

과학 payload의 범위와 제외 항목은 [SCIENTIFIC_PAYLOAD_MANIFEST.json](SCIENTIFIC_PAYLOAD_MANIFEST.json)에 있다. 이 보고서와 handoff는 이미 확정한 과학 근거를 설명하는 종료 문서다. FINAL의 자기 commit·tree·ZIP·provider ACK는 그 source 밖인 [PR150](https://github.com/cosmosapjw-quantum/WU088_HH/pull/150)과 최종 대화 응답에 둔다. 완료 뒤 그 영수증을 FINAL source에 소급 삽입하지 않는다.

## 2. 적용 전제와 새 수학적 구성

Column-conservative Markov 생성자 \(K\), 확률벡터 \(\pi\), 비음수 destruction 벡터를 고정하고 \(H=\pi d_{\rm dest}^{T}-\operatorname{diag}(d_{\rm dest})\), \(A(t)=K+w(t)H\)를 유지한다. R11에서 저장한 선택 유리수 \(q\)와 block 길이 \(\tau\)는 전체 인증된 \(w\) box 안의 모든 admissible measurable 경로와 모든 시작시각에서 유효해야 한다. 같은 source family, 상태와 순서, 정확한 시계, 초기 불변량, whole-fine/coarse forcing이 적용 범위다. Nominal \(K\)의 contraction 값을 full \(A\)에 직접 이식하지 않는다. [전체 전제](theory/PREMISES_AND_MAP_KO.md), [증명](theory/PROOF_KO.md).

남은 구간의 \(\ell^1\) 비팽창성과 동일 family에서의 합성을 이용하면 나이 \(u\)에 대한 kernel은 다음과 같다. \(h(0)=1\)이며 \(q=0\)에서도 \(0^0=1\)을 사용한다. 따라서 마지막 block 안에 새로 들어온 forcing이 사라지지 않는다.

$$h(u)=q^{\lfloor u/\tau\rfloor},\qquad u\ge0,\qquad h(0)=1.$$

Source cell \([a_j,b_j]\)에서 상수 upper \(g_{r,j}\)가 주어졌을 때 convolution은 interval overlap 길이로 정확히 계산한다. 관측 시각을 격자에 반올림하거나 forcing을 block 시작점으로 옮기지 않는다.

$$F(t)=\sum_j g_{r,j}\sum_{k\ge0}q^k\left|[a_j,b_j]\cap[t-(k+1)\tau,t-k\tau]\right|,\qquad \overline R(t)=h(t-t_0)R_0+F(t).$$

독립 reference는 같은 overlap 반복문을 사용하지 않고 원시함수 \(J\)를 직접 구성한다. \(x=\max(v,0)\), \(n=\lfloor x/\tau\rfloor\)라 하면, \(q=0,1\)도 아래 유한 합에 포함된다.

$$J(v)=\tau\sum_{k=0}^{n-1}q^k+q^n(x-n\tau),\qquad F(t)=\sum_j g_{r,j}\{J(t-a_j)-J(t-b_j)\}.$$

Refinement는 source·observation·기존 cap 경계와 모든 필요한 source 경계의 \(k\tau\) 평행이동을 합쳐 만든다. 각 열린 세분 셀에서 \(F\)와 \(\overline R\)은 affine이다. Kernel jump에서는 셀 오른쪽 끝점으로 왼쪽에서 접근한 극한과 끝점의 실제 값을 구별한다. Whole-cell \(R\) upper에는 양쪽의 필요한 값을 모두 포함한다. 원래 global convolution의 이력을 cap 시점에서 초기화하지 않는다. [정리와 API](theory/THEOREM_AND_API_KO.md), [구현 설계](CODE_DESIGN_KO.md).

삼각 비교계의 두 번째 성분은 \(E=|\eta|\), coarse \(\ell^1=4E\)를 유지하며 \(E'\le cR+d_cE+g_e\)로 전파한다. 길이 \(\Delta\)인 세분 셀에서 \(R\)의 왼쪽 값과 오른쪽 왼극한을 각각 \(L,V\)라 하면 ideal affine forcing의 scalar 전파는 다음과 같다.

$$E_+=e^{d_c\Delta}E_-+(cL+g_e)\Delta\varphi_1(d_c\Delta)+c(V-L)\Delta\varphi_2(d_c\Delta),$$

$$\varphi_1(z)=\frac{e^z-1}{z},\qquad \varphi_2(z)=\frac{e^z-1-z}{z^2},\qquad \varphi_1(0)=1,\quad\varphi_2(0)=\tfrac12.$$

생산 구현은 양의 Bernstein moment와 dyadic128/Taylor96 바깥쪽 반올림을 사용한다. 독립 reference는 정확한 Fraction과 Decimal160 닫힌식을 사용하며 양수·음수·0 및 0 근처 \(d_c\)를 다룬다. 닫힌 셀 upper는 점을 연결한 선으로 대체하지 않는다. 기존 cap은 같은 source·상태·시계에서 해당 세분 셀 전체를 포함하는 old closed cell에만 적용하고, old point cap은 정확히 같은 유리수 시각에만 적용한다.

Refinement에 대한 불변성은 같은 ideal raw convolution과 그 비교 해에 관한 것이다. 유한 정밀도의 E 출력은 rounding 누적으로 비트 단위로 같을 필요가 없으며, capped E는 세분화된 전파를 통해 더 작아질 수 있다. 이번 저장 사례의 cap 동등성은 아래 실제 결과이며 일반적 cap 불변성 주장이 아니다. Raw lower는 선택한 rational-q ideal comparison의 lower로만 해석한다. 실제 물리 오차의 lower라는 뜻은 없다.

## 3. 유한 실행과 독립 검증

| 구분 | 실제 결과 | 과학 실행 수 | 전체 OS CPU |
| --- | --- | --- | --- |
| Primary | 531/531 PASS | 1 | 1.103768 s |
| 독립 reference | 317/317 PASS | 1 | 3.098666 s |
| 합계 | component comparisons 133,502, 실패 0 | 2 | 4.202434 s |

| Reference 비교 종류 | 실제 component 수 |
| --- | --- |
| Exact Fraction | 68,870 |
| Decimal160 | 19,019 |
| source·clock·closed-cell coverage | 44,719 |
| metadata | 894 |

CPU 합계 `4.202434`초는 두 Python 과학 프로세스의 import와 serialization을 포함한다. 저장 출력 분석·그림 생성과 원격 CAS의 CPU는 이 합계에 넣지 않았다. 전체 과거 CPU와 global remaining은 계속 null이다. [실행 원장](EXECUTION_LEDGER.json), [Primary process](raw/PRIMARY_PROCESS.json), [Reference process](raw/REFERENCE_PROCESS.json).

Decimal 검증의 guard는 실행 전에 고정한 `1e-80*max(1,abs(reference),abs(lower),abs(upper))`이며 판정은 `GUARDED_CORROBORATION_NOT_INTERVAL_REFERENCE`이다. Exact Fraction 비교에는 이 guard를 적용하지 않았다. Decimal reference 자체를 interval arithmetic으로 부르지 않는다. 비교 component 수는 물리 scenario 수와 다르다. [독립 reference 설계](verification/REFERENCE_DESIGN_KO.md), [실제 reference 결과](raw/REFERENCE_RESULTS.json).

유한 구현 계약은 상태 수 1–13, source·observation·old-cap cell 각각 최대 192, refined cell 최대 2,048, full block 최대 8, overlap 항 최대 200,000, 정확한 scalar 입력 최대 1024 bits, |d_c|×horizon 최대 16이다. 각 primary/reference의 사전 자원 한도는 60 CPU초·90 wall초였고, 허용된 각 1회만 사용했다. 네 저장 사례와 11개 control의 실제 검사는 이 고정 범위에 대한 근거이며 전체 family 정리의 근거는 해석적 증명이다. [계약](CONTRACT.json), [동결 기록](raw/PREEXECUTION_FREEZE.json).

Wolfram은 실제 1회 호출에서 **24개 zero residual**을 반환했다. 동시에 다음 경고를 반환했고 원인은 `NOT_ESTABLISHED`이다. 판정은 `QUALIFIED_SYMBOLIC_CORROBORATION`로 유지한다.

- `Symbol::undefined2: Warning: Global symbols "L, V, L, V, L, V, L, V, L, V, L, V" are undefined.`
- `General::messages: Messages were generated which may indicate errors.`

Zero residual은 동결된 유한 항등식의 보조 근거다. 전체 정리나 물리 closure의 독립 채택을 뜻하지 않는다. SciSpace와 Exa는 실제 문헌·HD 배포 경로 조사에, Wolfram은 새 유한 항등식 확인에 사용했다. 도구별 실제 요청과 근거는 [문헌 기록](authority/literature/LITERATURE.json), [HD 경로 조사](authority/intake/hd_public_data/HD_ROUTE_REPORT_KO.md), [CAS 판정](raw/CAS_ASSESSMENT.json)에 있다.

## 4. 저장 사례의 실제 결과

Source forcing의 192개 저장 원소가 모두 정확히 같음을 확인한 경우에만 source cell 하나로 압축했다. 이는 함수의 값을 바꾸지 않는 표현 변환이다. 두 격자는 같은 시작·종료 시각을 사용하며, nonaligned의 새 내부 요청점에 old point cap을 잘못 적용하지 않았다.

| 사례 | 격자 | source / observation / refined cells | full blocks | overlap 항 | scalar 길이 종류 |
| --- | --- | --- | --- | --- | --- |
| 2상태 무반응 | aligned | 1 / 192 / 192 | 3 | 772 | 1 |
| 2상태 무반응 | nonaligned | 1 / 192 / 383 | 3 | 1536 | 5 |
| 2상태 비선형 | aligned | 1 / 192 / 192 | 3 | 772 | 1 |
| 2상태 비선형 | nonaligned | 1 / 192 / 383 | 3 | 1536 | 5 |
| 2상태 coarse-source defect | aligned | 1 / 192 / 192 | 3 | 772 | 1 |
| 2상태 coarse-source defect | nonaligned | 1 / 192 / 383 | 3 | 1536 | 5 |
| Native9 조건부 fixture | aligned | 1 / 192 / 192 | 3 | 772 | 1 |
| Native9 조건부 fixture | nonaligned | 1 / 192 / 383 | 3 | 1536 | 5 |

다음 수치는 저장한 exact rational 값을 표시용 15자리로 바꾼 것이다. 원본 유리수는 [전체 분석 JSON](analysis/SAVED_OUTPUT_SUMMARY.json)에 있다.

| 사례 | 격자 | raw R(T) | raw E(T) | capped R(T) | capped E(T) |
| --- | --- | --- | --- | --- | --- |
| 2상태 무반응 | aligned | 0.06103515625 | 0 | 0.0557825400371075 | 0 |
| 2상태 무반응 | nonaligned | 0.06103515625 | 0 | 0.0557825400371075 | 0 |
| 2상태 비선형 | aligned | 0.0670615623147999 | 0.000514553889690015 | 0.0602119158660167 | 0.000396434054402575 |
| 2상태 비선형 | nonaligned | 0.0670615623147999 | 0.000514553889690015 | 0.0602119158660167 | 0.000396434054402575 |
| 2상태 coarse-source defect | aligned | 0.0670615623147999 | 0.000683240624257362 | 0.0602119158660167 | 0.000565120788969921 |
| 2상태 coarse-source defect | nonaligned | 0.0670615623147999 | 0.000683240624257362 | 0.0602119158660167 | 0.000565120788969921 |
| Native9 조건부 fixture | aligned | 0.0000701971878504450 | 0.00000119238424255714 | 0.0000364476161178182 | 6.19079240657234e-7 |
| Native9 조건부 fixture | nonaligned | 0.0000701971878504450 | 0.00000119238424255714 | 0.0000364476161178182 | 6.19079240657234e-7 |

### 같은 시각과 같은 닫힌 셀의 비교

Aligned는 기존 193점을 그대로 사용했다. Nonaligned는 refined grid에서 그와 정확히 같은 193개 old knot를 선택하고, 각 기존 닫힌 셀에 포함되는 refined whole upper들의 최댓값을 취했다. 서로 다른 요청 시각의 endpoint를 직접 비교하지 않았다.

| 두 격자·네 사례 합계 | R11보다 작음 | 정확히 같음 | R11보다 큼 |
| --- | --- | --- | --- |
| capped 점 성분 | 0 | 3088 | 0 |
| capped 닫힌 셀 성분 | 0 | 3072 | 0 |
| raw 점 성분 | 0 | 400 | 2688 |
| raw 닫힌 셀 성분 | 0 | 392 | 2680 |

양의 baseline에서 추가 capped 개선은 0%다. 무반응 E의 baseline은 0이므로 0/0 상대비를 0%로 바꾸지 않고 null로 둔다. Raw의 보편적 우위를 주장하지 않는다. 같은 old knot의 kernel/F/R exact 값은 두 격자에서 일치하고, 같은 ideal E를 감싸는 outward 구간들은 겹친다. 세분화가 rounding 폭을 줄인다는 보장은 없다.

## 5. 그림의 의미와 표시 범위

### 그림 1 — 비정렬 source 경계와 fresh forcing

![Nonaligned control geometry](figures/NONALIGNED_CONTROL_GEOMETRY.png)

`NONALIGNED_CONTROL_GEOMETRY`는 translated-source control의 source knots, source에서 이동한 경계8/15·13/15, step kernel, exact F 및 R affine segment를 표시한다. R의 open circle은 **셀의 오른쪽 끝점에 왼쪽에서 접근한 극한**이고 filled point는 해당 끝점의 실제 비교값이다. E의 dashed endpoint 연결선은 시각적 안내이며 orange whole-cell steps가 각 닫힌 셀의 upper를 나타낸다. 별도 q=0 control은 마지막 [3/4,1]에 들어오는 새 forcing이 h0=1을 가지므로 최종 R=1/4, E=1/32임을 보여 준다.

### 그림 2 — 동일한 R11 clock과 cap으로 비교

![Matched R11 cap comparison](figures/MATCHED_R11_CAP_COMPARISON.png)

`MATCHED_R11_CAP_COMPARISON`의 왼쪽 열은 같은193점, 오른쪽 열은 같은192 old closed cell이다. 오른쪽 nonaligned 값은 해당 old cell 안의 refined upper 최댓값으로 집계했다. 파란색은 raw R, 주황색은 raw E이며 실선/파선은 aligned/nonaligned를 구별한다. 초록색 ratio1은 두 격자의 capped 출력이 R11과 정확히 같음을 뜻한다. Positive baseline만 ratio를 표시하며, no-reaction E는 모두0이므로 0/0 ratio를 생략하고 null로 기록했다. Point plot의 연결선은 whole-cell 인증으로 읽지 않는다.

PNG와 SVG를 함께 제공한다. 모든 PNG chunk CRC·정확한 IEND 끝·Pillow full decode 및 SVG XML을 확인한 뒤 atomic replace로 저장한다. 최종 bytes/SHA는 `figures/FIGURE_MANIFEST.json`에 있다.

최종 파일의 실제 크기·SHA-256·원본 결과 식별값은 [FIGURE_MANIFEST.json](figures/FIGURE_MANIFEST.json)에 있다. 그림은 저장 결과의 후처리이며 새로운 과학 실행으로 집계하지 않는다.

## 6. 최신 입력 조사와 접근 범위

이번 GitHub census는 접근 가능한 51개 repository와 2,385개 head를 실제 열거했다. Repository 목록은 2페이지, branch 목록은 66페이지였으며 모든 대상 목록을 terminal까지 읽었다. 공개 범위는 35개 repo/1,902개 head, 비공개 범위는 16개 repo/483개 head다. 비공개 식별자는 공개 문서에서 제외하고 집계만 남겼다.

공개 head의 이전 기준 대비 변화는 신규 10, 이동 6, 삭제 0, 불변 1,886개다. 새 material branch 12개를 대상으로 27회 원문 요청을 했고, 25회 성공 중 23개는 full blob byte 확인, 2개는 부분 범위 읽기다. 경로별 오류 2건도 기록했다. Head census 종료는 2026-10-28T13:39:41.723 KST, 선택 immutable source 읽기 종료는 2026-10-28T13:48:01.266 KST다. 이것은 읽기 시각의 조사이며 모든 branch의 모든 파일을 읽었다는 뜻이나 원자적 snapshot이라는 뜻이 아니다. [GitHub 조사](authority/intake/github/SYNTHESIS_KO.md).

Dropbox의 지정 main hierarchy는 5,249항목/9페이지를 terminal까지 읽었다. Root 직접 목록 511항목과 추가 관련 326항목도 실제 terminal이며, 고유 열거 합집합은 6,086항목이다. 관련 없는 모든 하위 폴더의 내용까지 조사했다는 뜻은 아니다.

Drive folder discovery는 553개/4페이지에서 실제 token terminal이었다. 관련 270개 folder의 고유 항목은 3,933개이고, root의 관련 항목을 포함한 합집합은 4,142개다. 상위 BASS folder 파일목록은 1,000개 cap에 걸려 부분적이다. 사용 가능한 file-list API에 cursor가 없고, 실제 존재하는 ZIP의 이름 검색과 q/시간 분할 검색도 0건을 반환하여 그 검색으로 binary ZIP의 완전 열거를 복구할 수 없었다. 이 한계를 자료 부재로 해석하지 않는다. [백업 조사](authority/intake/backups/SYNTHESIS_KO.md), [실제 cap·검색 probe](authority/intake/backups/DRIVE_CAP_AND_SEARCH_PROBES.json).

다른 대화 원문은 0건이다. Personal-context 도구가 실제 unavailable을 반환했고, 현재 대화에 이미 제공된 handoff만 재사용했다. 다른 전체 대화에 접근했다거나 모든 대화에 관련 자료가 없다는 주장은 하지 않는다. 첨부 20개의 SHA·크기가 이전과 동일하여 기존 조사 근거를 재사용했다. [대화 접근 기록](authority/intake/backups/CONVERSATION_ACCESS.json), [첨부 식별값](authority/intake/attachments/ATTACHMENT_IDENTITY.json).

변경된 의존성에서는 REC의 실제 원본 복구, REI C7의 새 검증, BASS의 별도 조건부 source-memory 구성과 추가 연구 branch를 확인했다. Git HEAD의 불변 여부와 별개로 R11 FINAL 뒤에 생성된 VigilODE V8 matrix B 원본도 읽었다. 그 원본은 9,285,519 bytes·299 members이며 선택 자료의 당시 상태는 15/20, C9와 final admission pending이었다. Supplied interval matrix의 고정 metric 결과를 WU의 column-Markov l1 theorem이나 실제 HD·WU physical binding으로 옮기지 않았다. 이 최신 근거와 과거의 미복구 기록을 구별했다. [조사 종합](authority/intake/SYNTHESIS_KO.md), [V8 원본 기록](authority/intake/backups/MATRIX_B_SELECTED_MANIFEST.json).

실제 새 HD reactive array와 named WU physical consumer/state/density/clock의 결속은 이번에 읽은 범위에서 확보되지 않았다. 공식 HD 배포 경로에서는 reactive supplementary의 존재 진술과 비반응 excitation 자료를 구별했고, 실제 reactive array bytes를 확보한 것으로 기록하지 않았다. 이는 현재 입력의 INPUT_PENDING 상태이며 전역적인 자료 부재 결론이 아니다.

## 7. 단계별 실제 게시와 이중 백업

| 단계 | 완료 내용 | 실제 source commit | ZIP bytes | ZIP SHA-256 | Drive ACK | Dropbox ACK ID | workflow | 과학 DAG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S01 · R1/C1 | 연구 범위·재사용 기준 | [560fcab19e97c09035d0f15234781001b8871806](https://github.com/cosmosapjw-quantum/WU088_HH/commit/560fcab19e97c09035d0f15234781001b8871806) | 3,783,154 | `0e4dbc6e2e8e64168a7a96fa3cdcc07050383e9d413bd56829163941301669a7` | [Drive](https://drive.google.com/file/d/1Vsxp3Exdj5xPJVkcamnMSY6O8sBjLS_r/view?usp=drivesdk) | `id:BSpOijBcT10AAAAAAEDJgw` | 2/20 | 23/40 |
| S02 · R2/C2 | 조사·문헌·구현 설계 | [73bd3c662d422a6e14a4df55f10ef1c212cdc1d6](https://github.com/cosmosapjw-quantum/WU088_HH/commit/73bd3c662d422a6e14a4df55f10ef1c212cdc1d6) | 4,096,173 | `eb3c61a03eb661d3edfd0cd94be6166bbe6ca04245e240fd4e07fac9b4f46ad4` | [Drive](https://drive.google.com/file/d/1qvoH6HoIu7c1A9DbWAKlTnpu4JLl9QuV/view?usp=drivesdk) | `id:BSpOijBcT10AAAAAAEDJiQ` | 4/20 | 23/40 |
| S03 · R3/C3 | 전제·정리·API | [22e4d4f0555d34e5cdf662f02f976d9b55c4a4f2](https://github.com/cosmosapjw-quantum/WU088_HH/commit/22e4d4f0555d34e5cdf662f02f976d9b55c4a4f2) | 4,102,514 | `88a52444a2beb4dd08c4d9df124c66997fed6a19810596bffbe4e44a04f2424a` | [Drive](https://drive.google.com/file/d/1h5ypJs1n_zQD-G_OZ9d9HQWJzjVghici/view?usp=drivesdk) | `id:BSpOijBcT10AAAAAAEDJjg` | 6/20 | 23/40 |
| S04 · R4/C4 | 구성·유한 자원 계약 | [8b01fd27bdde6e6f87b2ef12dbc0c52169f03f11](https://github.com/cosmosapjw-quantum/WU088_HH/commit/8b01fd27bdde6e6f87b2ef12dbc0c52169f03f11) | 4,105,190 | `09c02fd7f636ddde3651f70a213dc5ad43bd4f6d10c21d13510d5ed0aa92f445` | [Drive](https://drive.google.com/file/d/12p6LnRJ860F75C-E1t0H2HeiSguveIpm/view?usp=drivesdk) | `id:BSpOijBcT10AAAAAAEDJkA` | 8/20 | 23/40 |
| S05 · R5/C5 | 증명·코드·실행 전 동결 | [9e4ff95efff61278536d4401f307523dd207c260](https://github.com/cosmosapjw-quantum/WU088_HH/commit/9e4ff95efff61278536d4401f307523dd207c260) | 4,154,032 | `51b68db36cdb89bee425f4a2efa4769238981af38ca53465237e5d829cf4e7c6` | [Drive](https://drive.google.com/file/d/1qZcqukP3jbfa2WEL1ymDJ0_W8ay2tuYz/view?usp=drivesdk) | `id:BSpOijBcT10AAAAAAEDJkw` | 10/20 | 23/40 |
| S06 · R6/C6 | 독립 사전 심사·primary·CAS | [85fb1d5224a8ab0abd65880923ed209b691afb47](https://github.com/cosmosapjw-quantum/WU088_HH/commit/85fb1d5224a8ab0abd65880923ed209b691afb47) | 5,556,943 | `bd2a149edfdbb132ef09ae10fa6aabf30e1e48f3b9a4d89decddc1fc2ca14436` | [Drive](https://drive.google.com/file/d/1eQLnjCOMUIq3D3r5t7ovm0VzP9ABet3p/view?usp=drivesdk) | `id:BSpOijBcT10AAAAAAEDJmQ` | 12/20 | 23/40 |
| S07 · R7/C7 | 독립 reference·실제 실행 기록 | [ea50fe9b044af4e9f86de031cd3370100da8633d](https://github.com/cosmosapjw-quantum/WU088_HH/commit/ea50fe9b044af4e9f86de031cd3370100da8633d) | 5,872,085 | `4371cf13e0efeb70ffe373fd9348d7131a15481f43b937a457acc32aa1b3015b` | [Drive](https://drive.google.com/file/d/1WUfR-7tL7xDCfs_a8LXQhm21WqvtTVD5/view?usp=drivesdk) | `id:BSpOijBcT10AAAAAAEDJmw` | 14/20 | 23/40 |
| S08 · R8/C8 | 저장 출력 분석·그림 | [f14f2c5588206ba01fb4690971cfa0bd4a4d4ca3](https://github.com/cosmosapjw-quantum/WU088_HH/commit/f14f2c5588206ba01fb4690971cfa0bd4a4d4ca3) | 7,937,576 | `440759d5a95ccfbbcea71402a80f8deffee87c45b2b2c62f38e769eb9a450104` | [Drive](https://drive.google.com/file/d/1fXFkF3ei0kn6ELtgn4HT7-RdwpKdQLix/view?usp=drivesdk) | `id:BSpOijBcT10AAAAAAEDJrQ` | 16/20 | 23/40 |
| S09 · R9/C9 | 최종 C9·두 노드 과학 채택 | [eb431411f6f0c4c9065edb0a5a11ce2c4bccf2fe](https://github.com/cosmosapjw-quantum/WU088_HH/commit/eb431411f6f0c4c9065edb0a5a11ce2c4bccf2fe) | 7,960,113 | `581846273f4e8e8bee86565138cbf972ff5cd5ca1a70cfa3211481cab99e3290` | [Drive](https://drive.google.com/file/d/1pYhgLrq-KOjqviut-shv5mcFhlRWfEbW/view?usp=drivesdk) | `id:BSpOijBcT10AAAAAAEDJsw` | 18/20 | 25/40 |
| S10 · R10/C10 | 최종 보고·인수인계 | [cf76cb0c7f7975327bca9801b5a5ded221b85b99](https://github.com/cosmosapjw-quantum/WU088_HH/commit/cf76cb0c7f7975327bca9801b5a5ded221b85b99) | 8,003,184 | `afce08815bcc9f0d80500a1e1a61480de5d41dda950cb9831b6bddb44e079e06` | [Drive](https://drive.google.com/file/d/1YKBDQNZ7vjqzavdjXq0o9-Vd27nqSJsY/view?usp=drivesdk) | `id:BSpOijBcT10AAAAAAEDJvQ` | 20/20 | 25/40 |

위 표의 완료 행은 10개 ZIP과 두 provider의 실제 ACK 20개에 대응한다. 검증 수준은 로컬 ZIP CRC·모든 member SHA-256 일치, Drive·Dropbox의 실제 ACK 및 양쪽 크기 일치다. 이번 R12 단계 백업의 provider original GET은 NOT_RUN이다. 최신 조사에서 새 V8 원본을 GET한 사실은 R12 단계 ZIP을 provider에서 다시 내려받았다는 뜻이 아니다. 각 source tree·archive 이름과 완전한 영수증은 [PUBLICATION_INDEX.json](delivery/PUBLICATION_INDEX.json)에 있다.

이 문서에 포함한 마지막 완료 단계는 S10이다. ZIP 이름은 `WU_MOLECULAR_R12_S10_SOURCE_20261028_cf76cb0c7f79.zip`, 크기는 8,003,184 bytes, SHA-256은 `afce08815bcc9f0d80500a1e1a61480de5d41dda950cb9831b6bddb44e079e06`이다. 실제 저장 위치는 [Drive](https://drive.google.com/file/d/1YKBDQNZ7vjqzavdjXq0o9-Vd27nqSJsY/view?usp=drivesdk)와 Dropbox ID `id:BSpOijBcT10AAAAAAEDJvQ`다. FINAL 자신의 발행 결과는 자기 source 밖의 PR150과 최종 응답에서 확인한다.

## 8. 범위, 보존 상태와 종료 경계

Native9은 **native K + synthetic conditional reaction fixture**다. Actual HD reactive array와 named physical consumer/density/clock은 INPUT_PENDING, HH_R10=OFF, production=NOT_ISSUED, L4=false, central/physical delta=0을 유지한다. Native v=UNSPECIFIED, MISSING_NOT_ZERO, TIQM/SQM의 구별도 보존한다. 물리 closure나 생산 적용 허가를 새로 발급하지 않았다.

R12 primary/reference/CAS의 잔여는 **0/0/0**이다. R11/R10/R9/R8/R7/R6/PHYS91의 기존 실행 허용량도 증가시키지 않았다. 이번 단위를 재개할 때 완료한 과학 실행·ODE·독립 심사나 전체 census를 통상 복구 절차로 반복하지 않는다. 기존 입력·증명·출력의 식별값과 적용 전제가 유효하면 그 근거를 재사용한다.

R8 원래 reference 726/727 PASS + 1 FAIL과 별도 exact phi 24/24 PASS는 서로 다른 기록으로 남는다. R10의 최초 후처리 ID 실패와 DOC01/META02, R10·R11의 CAS 경고 및 원인 미확정 상태도 유지한다. 기존 sample 허용오차 atol=2e-12, rtol=2e-10에 대한 결과를 strict containment로 바꾸지 않았다. R10의 저장 sample 최대 초과 4.0013206434938575e-12는 고정 tolerance 4.377656370786352e-11 이내였으며, R12에서 새 sample campaign을 실행하지 않았다.

이번 R12의 사전 포인터 수정, 게시 호출 거부·orchestration 문법 오류, 저장 그림의 표시 수정과 해당 보존 경로는 [실행 원장](EXECUTION_LEDGER.json), [지적 기록](reviews/FINDINGS.json), [최종 C9](reviews/C9_FINAL_REVIEW.json)에 따른다. 완료된 과학 결과를 다시 실행하여 그 기록을 지우지 않았다.

현재 사용자 범위는 이미 등록되어 있던 R12 두 노드의 종료까지다. 다음 연구 단위·DAG 노드·새 계산 허용량은 정하지 않았다. 실제 새 HD array 또는 명명된 WU physical consumer가 구체적인 bytes와 결속 자료로 제공되는 경우 그 source/state/density/clock·whole-domain 전제를 우선 확인한다. 이후 작업은 새로운 명시적 범위에 따라 선택한다. [다음 입력 계약](followup/NEXT_INPUT_CONTRACT.json), [복사용 handoff](HANDOFF_KO.md).
