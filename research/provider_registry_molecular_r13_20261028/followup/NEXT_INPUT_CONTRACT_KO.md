# R13 이후 입력·이론·코드·자원 계약

**다음 우선 작업은 실제 새 HD reactive array 또는 이름이 정해진 physical consumer의 source/state/density/clock 결속이다.** 현재 조사한 입력 경로의 상태는 `INPUT_PENDING_IN_INSPECTED_SCOPE`다. 관련 백업·repo·대화 접근 범위는 `authority/intake/`의 시점과 접근 상태를 따른다. 직접 검색할 수 없었던 다른 대화까지 자료가 없다고 판정하지 않는다.

이 문서는 후속 제안 계약이다. 새로운 과학 노드를 추가하거나 완료로 표시하지 않는다. 실제 입력이 없을 때 검토할 별도 후보는 **piecewise-quadratic forcing을 위한 cubic convolution·극값 인증·양의 지수 전파**다. 후보의 증명·구현·실행·채택은 아직 수행하지 않았다.

## 1. 현재 근거와 실행 권한

작성 시점은 R13 S07, workflow 14/20이다. 이 값은 작성 당시의 snapshot이며, 재개 시 최종 `WORKFLOW_RECORD.json`, `SCIENTIFIC_ADMISSION.json`, `EXECUTION_LEDGER.json`을 읽어 현재 상태를 정한다.

현재 실행 원장에는 primary **311/311**, independent reference **125/125**, component comparisons **8,408**, component failures **0**이 기록돼 있다. Primary와 reference는 각각 실제 OS process 1회, CAS는 1회를 소비했다. CAS는 **25개 zero와 경고가 함께 있는 `QUALIFIED_SYMBOLIC_CORROBORATION`**, 경고 원인은 `NOT_ESTABLISHED`다. 이 후속 계약을 작성하며 계산을 반복하지 않았다.

| 자원 | 현재 남은 횟수 | 이 문서가 새로 배정하는 횟수 |
|---|---:|---:|
| R13 primary | 0 | 0 |
| R13 independent reference | 0 | 0 |
| R13 CAS | 0 | 0 |
| 후속 scientific/ODE campaign | 0 | 0 |

R12/R11/R10/R9/R8/R7/R6/PHYS91의 기존 allowance 증가도 0이다. Global remaining과 전체 역사적 CPU는 `null`을 유지한다. 사용자가 승인한 R13 루프와 기존 게시·백업 권한은 새로운 R14 이후 과학 실행 예산을 자동으로 만들지 않는다. 이 문서 자체의 새 CPU·wall allowance도 0이다.

## 2. 실제 입력이 도착하면 먼저 결속할 항목

### 원자료

실제 파일 바이트, 파일명, 크기, SHA-256, immutable URL 또는 provider 객체 ID, 취득 시각·방법을 기록한다. DOI·초록·논문 서술과 수치 array를 구별한다. 제공 자료가 rate인지 cross section인지, 초기·최종 채널과 반응 방향이 무엇인지, temperature 또는 collision-energy grid와 각 열의 단위가 무엇인지 확인한다.

각 state에는 가능한 실제 (v,J), spin, isotope, charge 등의 라벨과 원래 순서를 유지한다. 원자료의 TIQM/SQM 방법을 그대로 보존하고 reactive formation/destruction과 HD-preserving excitation을 구별한다. 새로운 자료에 명시된 (v)는 그 새 source에 기록한다. 기존 native fixture의 `v=UNSPECIFIED`를 소급해 채우지 않으며, 누락 값은 `MISSING_NOT_ZERO`로 관리한다.

### 실제 consumer

소비하는 repo owner·immutable commit·코드 경로·함수, state order와 정확한 사상·정규화, density의 이름·원자료·단위·정의역, clock의 이름·의미·단위·정의역을 함께 기록한다. Proper time, coordinate time, redshift 등의 변환이 있으면 변환식과 source domain을 결속한다. 실제 consumer 없이 조건부 다른 repo의 consumer만 확보한 경우에는 해당 조건부 근거를 보존한다.

다음 표의 B01–B08은 입력 수신 뒤 수행할 계약이며, 현재 상태는 모두 `NOT_RUN`이다.

| ID | 확인할 내용 | 완료 근거 |
|---|---|---|
| B01 | 실제 source bytes와 immutable/provider identity | 실제 bytes·크기·SHA·취득 기록 |
| B02 | 반응 방향, 방법, rate/cross-section 및 state 의미 | 원전·array 열과 단위의 대응 |
| B03 | source와 consumer의 state order·정규화 | 명시적 사상과 누락 상태 |
| B04 | 이름이 정해진 consumer·density·clock | immutable 코드와 단위·domain 결속 |
| B05 | 고정 K/pi/destruction과 전체 w family | 같은 full-A family의 all-starts q/tau 근거 |
| B06 | whole fine/coarse-domain forcing 함수 | source/state/clock 및 canonical forcing SHA |
| B07 | 현재 유한 코드 범위와 필요한 adapter | 모든 크기 조건의 동시 충족 또는 정확한 확장 의무 |
| B08 | 새 작업 단위와 실행 계약 | 식·코드·입력·정확도·자원·독립 검증 기준의 사전 동결 |

`source_sha256`는 실제 외부 source artifact 바이트의 identity다. R13의 `whole_forcing_source_sha256`는 `WU_R13_WHOLE_FORCING_V1` 형식으로 exact source/state/clock/source knots/g_r/g_e를 canonical serialization한 값이며 production이 다시 계산한다. 이 결속은 선언한 함수가 바뀌었는지 확인한다. `ARITHMETIC_CONTROL_PREMISE`는 arithmetic control의 지위를 유지하고, 물리적 whole-domain 부등식의 성립은 별도의 실제 근거를 요구한다.

다음 경우에는 구체적인 실패 필드와 보완 입력을 기록한다.

- Numeric array가 필요한 자리에 DOI·요약만 있거나 실제 bytes/hash가 일치하지 않는 경우.
- 반응 방향·방법·state map·matrix orientation·단위가 맞지 않거나 density/clock 결속이 없는 경우.
- 누락된 (v)나 rate를 0으로 채우거나 TIQM/SQM 및 reactive/excitation 역할을 바꾼 경우.
- Nominal K rho나 다른 K/pi/destruction/w family의 q/tau를 현재 full A에 옮긴 경우.
- Arithmetic q=0 control을 실현된 물리적 full-A certificate로 읽은 경우.
- Sample·그림 endpoint 연결선을 whole-domain forcing 또는 whole-cell 인증으로 사용한 경우.
- Forcing/state/clock을 변경하면서 이전 canonical forcing hash나 historical cap을 유지한 경우.
- Singleton state에서 (R_0>0) 또는 양의 (g_r) endpoint가 있거나, exact scalar·grid·크기 조건을 위반한 경우.

결속 실패는 해당 입력의 불일치 또는 누락을 뜻한다. 원자료와 provenance를 보존하며 정확히 필요한 보완 항목으로 이어간다.

## 3. 변경 없이 재사용할 R13 조건

계속 유지할 생성자는

\[
H=\pi d^{\mathsf T}-\operatorname{diag}(d),\qquad A=K+wH
\]

이며 certificate family 안에서 K/pi/destruction을 고정한다. 전체 인증 w box, 모든 시작시각, zero-mass residual, 짧은 구간의 nonexpansiveness가 q/tau와 함께 결속된다. 커널은

\[
h(\mathrm{age})=q^{\lfloor\mathrm{age}/\tau\rfloor},\qquad h(0)=1
\]

이다. R forcing memory는 최초 (t_0)부터 전역으로 유지한다. 관측점·source 분할·재시작·게시 checkpoint에서 reset하지 않는다. (E=|\eta|), coarse ℓ1 = (4E), 고정 (c\ge0), horizon 전체의 signed (d_c)를 유지한다.

현재 finite API는 states 1–13, source/observation cells 각각 1–64, base cells 최대 2,048, vertex-refined cells 최대 4,096, full kernel blocks 최대 8, input scalar 256 bits, derived scalar 16,384 bits, \(|d_c|(T-t_0)\le16\)을 함께 적용한다. Overlap 전 작업량 조건은

\[
(3N_{\rm base}+1)N_{\rm source}(B+1)\le200000
\]

이다. Production dyadic128/Taylor96과 independent Decimal160·사전 고정 relative guard (10^{-80})의 근거를 재사용한다. Decimal reference의 지위는 수치 corroboration이다.

Raw lower는 chosen-rational-q ideal comparison의 lower다. Whole-cell bound는 내부 극값과 actual right endpoint의 left-limit supremum까지 포함한다. R13에는 generic cap API가 없다. R10/R11 cap은 원래 source/state/clock/closed-cell identity를 유지한다. 새 물리 입력이 이 finite API나 cap contract 밖이면 실제 차이를 특정한 별도 계약을 먼저 작성한다.

## 4. 입력이 없을 때의 별도 후보: 이차 forcing

다음 후보의 목표는 exact rational source/observation partition 위에서 선언된 비음의 이차 whole-domain forcing을 처리하는 것이다. 예를 들어 각 source cell의 degree-2 Bernstein 계수와 whole-domain source premise를 입력 형식으로 검토할 수 있다. 이는 현재 R13 API에 이미 추가된 기능이 아니다.

R13은 affine forcing에서 quadratic R 조각을 구성하고 rational vertex를 삽입한다. 이차 forcing 후보에서는 cubic convolution 조각과 그 derivative-quadratic의 극값을 다뤄야 한다. 극값의 위치가 무리수일 수 있어 다음 증명·코드 의무가 먼저 필요하다.

1. 이차 forcing overlap moments와 독립 primitive를 유도하고 base-cell polynomial degree와 event topology를 정한다.
2. Derivative root의 부재·중근·순서·endpoint 일치와 identically-zero derivative를 정확히 처리한다. 무리수 root에는 exact algebraic 표현 또는 인증된 rational isolating interval을 정한다.
3. Root-isolating cell과 초기항 jump까지 gap-free whole-cell coverage를 증명한다. Isolation의 종료·폭 기준을 실행 전에 정한다.
4. Refined cell에서 사용할 Bernstein3 또는 다른 양의 표현을 증명한다. Cubic에 R13의 Bernstein2 lemma를 그대로 인용하지 않는다. Inflection 분할이나 다른 enclosure가 필요하면 해당 의무를 별도로 해결한다.
5. Signed degree-3 exponential weights와 outward argument/weight/tail bounds를 유도한다. Algebraic 또는 interval cell length를 택하면 그 길이의 불확실성도 포함한다.
6. Global R history를 유지하는 closed-cell E majorant, refinement 및 limiting controls를 마련하고 독립 proof/reference 검증을 구성한다.

후속 finite resource 계약은 source/observation 수, base/refined cell 수, algebraic degree, root-isolation 반복 수, input/derived bits, overlap/root/interval 작업량, enclosure 정확도·종료 기준, primary/reference/CAS의 CPU·wall·memory·attempt를 구체적인 값으로 먼저 동결해야 한다. 이 필드들은 현재 `null`이며 실행 allowance는 모두 0이다. R13의 범위·precision·시간 상한을 자동으로 확대하거나 새 후보에 충분하다고 간주하지 않는다.

필수 거부 사례에는 whole-domain/nonnegativity premise 누락, 이차 함수를 R13 affine 입력으로 재명명한 경우, root interval의 순서·분리·경계가 미결정인 경우, undecided sign을 root 부재로 확정한 경우, 음의 positive-basis 계수를 별도 인증 없이 허용한 경우, isolation·bit·cell·작업량 상한 초과가 포함된다. 실패 뒤 tolerance를 늘려 원래 기준의 성공으로 기록하지 않는다.

## 5. 다음 실행까지의 단계

**F0–F1:** 새로 제공된 source/consumer를 읽고 B01–B07을 결속한다. 변경되지 않은 근거를 재사용하고 실제로 바뀐 의존성만 정리한다. 이것으로 production을 발급하지 않는다.

**F2:** 실행 가능한 식·입력·출력·cap·정확도·자원·독립 검증 계약을 구체화한다. 이 문서는 그 후속 작업의 제안이며, 실행 계약의 모든 수치와 source가 동결됐다는 의미는 아니다.

**F3:** 실제 새 단위에 대한 사용자 또는 프로젝트의 유한 실행 권한을 확인하고 source/input/command/수용 기준을 동결한다. R13 및 이전 단위의 remaining 0을 보존한다.

**F4:** F3 이후에만 새로 승인된 실행과 독립 검토를 수행한다. 실제 scoped evidence로 새 노드를 채택한 뒤 scientific DAG를 갱신한다. 게시·백업은 root가 기존 expected-SHA/force=false 연구 branch·draft PR150·Drive/Dropbox 권한 안에서 수행한다. Main merge나 다른 owner repo 쓰기는 포함하지 않는다.

## 6. 재개할 때 보존할 기록

최신 AGENTS entry와 최종 REPORT/HANDOFF, SCIENTIFIC_ADMISSION, SCIENTIFIC_PAYLOAD_MANIFEST, DAG, WORKFLOW_RECORD, EXECUTION_LEDGER, 최종 C9/admission-delta review, PUBLICATION_INDEX를 읽는다. 유지된 identity와 전제 아래의 R11/R12/R13 과학·ODE·CAS·독립 심사를 통상 재개 절차로 반복하지 않는다.

R8 원래 failure와 별도 exact-phi 결과, R10 최초 ID failure와 원래 sample readout, R11 교정·첫 PNG 원인 미확정·S08/S09 삭제 기록, R12 qualified CAS와 display 교정, R13 실행 전 교정과 qualified 25-zero CAS 메시지는 원래 provenance에 남긴다. Provider original GET, upload/metadata acknowledgement, 실제 복원 바이트 검증을 계속 구별한다.

Actual HD 입력과 named physical consumer가 결속될 때까지 **HH_R10=OFF, production=NOT_ISSUED, L4=false, central/physical delta=0**을 유지한다. 이 후속 계약의 작성·게시로 증가하는 scientific DAG 노드 수와 실행 allowance는 모두 **0**이다.
