# R8 최종 독립 C9 심사

**판정: PASS_SCOPED_CONDITIONAL_CAUSAL_LAG_KERNEL_CODE. 미해결 실질적 발견 사항은 0개다.**

고정된 일반 증명, production core와 caller, 실제 primary, 최초 reference의 나머지 통과 항목, 별도로 승인·실행한 exact scalar 재판정을 함께 근거로 R8의 조건부 방법·구현 채택을 지지한다. 이 문서는 같은 제한된 심사의 최종 판정이다. Reviewer가 DAG를 변경하지 않았으며, 심사 시점 상태는 **15/32**다. 실제 S09 채택·게시는 root가 결정한다.

## 1. 실제 실행 결과와 비용

|구분|실제 결과|전체 프로세스 CPU|판정 역할|
|---|---|---:|---|
|S06 primary|237/237 PASS|3.807278초|고정 네 HD fixture·다섯 analytic control 및 source/guard 검사|
|S07 최초 reference|726/727 PASS, 1 FAIL 보존; 성분 22,658/22,659 PASS|0.440898초|독립 Decimal80 합산·닫힌식·저장 궤적과의 비교|
|S08 targeted scalar|24/24 PASS|0.072788초|최초 reference의 유일한 φ 항목을 exact rational로 재판정|

세 Python 프로세스의 전체 CPU 합은 **4.320964초**이며 imports와 serialization, 최초 실패한 reference의 비용을 포함한다. CAS CPU는 제공되지 않아 별도 미상으로 남긴다. 백업 전송과 metadata 비용 및 전체 과거 CPU를 이 합에 포함했다고 주장하지 않는다. 검사 수는 서로 독립된 물리 시나리오 수가 아니다.

Primary source는 `72931db38a5dbfc7b12720455c44109039a8f711`, 최초 reference source는 `b87ea61ab2d5e17221a6cf3b710aec074eb1a28e`, 실제 scalar source는 `ade11fe31248d5417902827e5a563ee9a71a065e`다. S08 결과는 reviewed runner·계약 해시와 실제 GitHub run `40536762714`에 결속된다.

## 2. 증명과 코드의 수용 범위

기존 독립 이론 판정 `PASS_SCOPED_CONDITIONAL_LAG_KERNEL_THEORY`를 유지한다. 같은 명목 Markov family·ordered state·clock·norm에 속하고 모든 시작 시각에 유효한 H/ρ 인증과 부분 구간 비팽창성을 사용한다. Reaction/reset feedback은 a,b,g에 남아 있으며 nominal K 수축을 full reactive operator에 옮기지 않는다.

Whole-cell과 endpoint의 지연 index, current-cell forcing의 계수1, d<0·d=0·d>0의 적분 상방 방향을 확인했다. 두 pass는 이전 전체 cell 배열만 읽는다. 마지막 exact min 뒤에 재반올림하지 않으므로 원래 whole baseline과 공통 시각의 point cap보다 커지지 않는다는 뜻이 유지된다.

Caller는 실제 frozen R6/R7 자료의 해시, native K midpoint, 공통 λ/P_lower, H/ρ, 상태 순서, 세 블록의 동일 B/g·clock과 초기/종료 연결을 검증한다. 192개 cell baseline 및 사례별 18개 저장 cap은 실제 원본 pointer·값·시각에 결속된다. Boolean metadata만으로 과학적 유효성을 선언하지 않는다.

독립 reference는 production core를 import하지 않고 Decimal80 직접 합산과 별도 analytic-control 닫힌식을 사용했다. 네 사례의 저장된 193 endpoint와 각 closed cell의 양 경계 비교도 실제 통과했다. 저장된 binary64 표본은 corroboration이며 cap이나 새 연속 ODE 인증의 근거가 아니다.

실행한 fixture 이외의 모든 유한 입력을 전수 시험했다는 주장은 없다. Core의 일반 조건과 유한 domain에 대한 근거는 증명·정적 산술 검토이며, actual reference는 사전에 고정된 좁은 입력을 확인했다.

## 3. PRE01과 REF01의 종료

**PRE01은 종료한다.** 원 cap을 Decimal80로 반올림한 뒤 exact no-worse 비교에 사용하던 문제가 첫 실행 전에 수정되었다. 실제 reference에서 원본 Fraction cap과 직접 비교한 144개 cap group이 모두 PASS다.

**REF01은 RESOLVED_BY_EXACT_SCALAR_RE_ADJUDICATION으로 종료한다.** 최초 reference의 native9 φ 비교는 생산값이 reference보다 약 `2.9108287948800326e-30` 큰데 원 근접성 기준이 `1e-30`이어서 실패했다. 저장된 exponential enclosure 폭 `51/2^128`이 `1/|d|=20000000`으로 증폭되므로 이 작은 d에서는 안전한 산술 여유가 `1020000001/2^128`다.

별도 scalar verifier는 production 함수와 exp evaluator를 호출하지 않고, `x=(-d)*delta∈(0,1)`에서 직접 적분 급수의 고정된 S9 하한과 S8 상한을 Fraction으로 계산했다. 교대급수 정리에 따라 `S9<=phi<=S8`이고 gap은 `delta*x^9/10!`다. 실제 S08에서 다음 조건이 모두 통과했다.

- `P>=S8`: 저장된 생산값이 엄밀한 φ 상계다.
- `P-S9<=A+(S8-S9)`, `A=1020000001/2^128`: 상계 여유가 원자료 구간으로부터 유도한 산술 예산과 일치한다.
- `P-S8>1e-30`: 최초 근접성 기준을 초과한 보수적 여유가 exact arithmetic에서도 실제임을 확인한다.
- 계산 전후 원 primary·reference 해시가 변하지 않았다.

따라서 전체 reference를 재실행하거나 blanket tolerance를 완화하지 않고 유일한 관측 의무를 닫았다. **최초 REFERENCE_RESULTS.json의 status는 계속 FAIL이다.** 이를 원래부터 727/727 PASS였던 실행으로 표현하지 않는다. 이전 static preflight가 이 작은 |d|의 근접성 증폭을 지적하지 못한 점도 실패 검토에 보존한다.

## 4. 실제 개선의 범위

Primary가 기록한 세 번째 macro endpoint의 exact 비교에서는 nonlinear, coarse-source-defect, native9 세 fixture 모두 R·E 두 성분이 저장된 R7 상계보다 엄격히 작다. No-reaction fixture는 두 성분 모두 동일하다.

|Fixture|1차 pass에서 이전 배열보다 작아진 whole-cell 성분|2차 pass에서 이전 배열보다 작아진 성분|
|---|---:|---:|
|two_state_no_reaction|0/384|0/384|
|two_state_nonlinear|376/384|382/384|
|two_state_coarse_source_defect|379/384|383/384|
|saved_native_nine_state_K_conditional_feedback|326/384|384/384|

이는 실제 저장 결과의 count와 boolean을 읽은 것이며 새 계산이 아니다. Strict improvement를 모든 입력에 보편적으로 주장하지 않는다.

## 5. CAS의 제한

CAS 최초 호출은 실제 JSON export 실패와 `$Failed`를 반환했다. 승인된 export-only repair 한 번에서 scalar residual 7/7과 kernel control 9/9의 0, 부호식 4/6의 True가 반환되었고 두 부호식은 symbolic 상태다. 그 두 식의 수동 근거는 독립 검토한 R8.14의 적분 양수성과 R8.12의 cell lag 부등식이다.

실제 `Power::infy`, `Infinity::indet` 경고를 보존하며 원인은 `NOT_ESTABLISHED`다. CAS 상태는 **QUALIFIED_PARTIAL_SYMBOLIC_CORROBORATION**이다. 일반 증명을 CAS로 대체하지 않으며, 전체 CAS PASS·warning-free라고 표현하지 않는다.

## 6. 핵심 원본 식별자

|파일|SHA256|
|---|---|
|src/volterra_feedback.py|3a415e8ccc76669a95bec30aa52fc1f1ad867cff1fd9fcca66734fb71872fba3|
|verification/run_primary.py|19aa784543bf75343e70ba76f9696cca0ecce7396e03d2c5c4206827dcf8250a|
|verification/run_reference.py|e0d4d88e367413b1e72a88c2d25b223f69ea0c37a916b7b40c610df78e0c4c2f|
|verification/run_phi_scalar_repair.py|219825e3786085951e456cb7408044598bc30166f5decee5669bc27c4147998d|
|raw/PRIMARY_RESULTS.json|520110d1cae1677491aecd7216621c25f1098470c939ee027d5df3bde183686b|
|raw/REFERENCE_RESULTS.json|da699b9a8b53389e3d222f34a5a421cd88ce17787bde69cc2e9bed5fb15409df|
|raw/PHI_SCALAR_REPAIR_RESULTS.json|0ea2399efd86657703a826e01b2c71528e994b990ae6ab9ffdab8c84653f2dcc|
|raw/PHI_SCALAR_REPAIR_PROCESS.json|262cec601e172056eb3b7d996d4c9ff3f434186a7887b207a9c14d62c3cb1f13|

나머지 proof·map·계약·과거 재사용 근거·process·CAS 원본의 실제 해시는 동반 C9_FINAL_REVIEW.json에 기록했다.

## 7. 유지되는 조건과 최종 권고

실제 named HD consumer, GL2022 reactive state array, collider density 및 physical-clock 결속은 여전히 입력 미결이다. Native HD 진동 표지는 v=UNSPECIFIED로 유지하며, 명목 excitation generator와 합성 reaction feedback을 구분한다. 이번 판정은 조건부 estimator·구현에 한정되고 물리 완료·중앙 완료 증가는 0이다.

다른 family·clock·state order, all-starts 가정이 없는 인증, 전체 구간에 유효하지 않은 B/g 또는 입증되지 않은 초기 envelope에는 자동 적용할 수 없다. 새로운 기본 정리 발견, strong no-go, 실제 생산 물리 준비 또는 새로운 연속 ODE 인증을 주장하지 않는다.

원 R8 primary/reference/CAS와 두 개의 제한된 보완 allowance는 모두 소진되었다. 과거 R6/R7/PHYS91 예산도 0으로 유지하며 추가 실행을 요청하지 않는다. **심사자의 과학 실행·import·AST·CAS·과거 과학 재실행·외부 쓰기는 모두 0**이다. 최초 proof/core/primary/reference를 작성하지 않았으며, 관측된 REF01 뒤에 보완 수학을 제안하고 별도 작성자의 scalar code와 실제 결과를 검토했다.

이 조건과 기록 보존 아래 R8의 scoped theory/code 채택을 권고한다.

