# R6 최종 C9 독립 심사

## 최종 판정

**PASS_SCOPED_CERTIFIED_IMPLEMENTATION.**

일반 finite-n 증명, production core의 directed arithmetic, 실제 primary **76/76 PASS**, 별도 구현 reference **109 consistent / 0 mismatch**를 함께 검토했다. 실행 결과의 input/core/runner/reference hash는 사전에 검토한 freeze와 일치한다. 발견한 입력 guard 두 건은 첫 실행 전에 수정됐고, 실제 primary에서 두 reject control 모두 DomainError로 통과했다. 열린 material code finding은 0이다.

Wolfram은 **23개의 zero residual과 all_zero=true를 반환했지만 symbol·singularity warnings도 함께 반환했다.** 원문 경고의 원인은 확정하지 않는다. 이 호출은 경고가 붙은 보조 검산으로 유지하며, warning-free 검증이나 단독 formal proof로 취급하지 않는다. 이 제한은 core의 별도 일반 증명·정적 산술 검토·primary/reference 근거와 구별된다.

검토자는 수치 재실행·CAS 추가 호출·IVP·production import·과거 suite 실행·외부 쓰기를 수행하지 않았다.

## 1. 실제 실행과 증거 연결

| 구분 | 실제 원자료 | 판정 |
|---|---|---|
| Primary | `raw/PRIMARY_RESULTS.json` | 76/76 PASS, failure0, exit0 |
| Independent reference | `raw/INDEPENDENT_RESULTS.json` | 109consistent, mismatch0, exit0 |
| Wolfram | 원 tool response + summary | 23zero, all_zero=true, 경고 보존 |
| Execution ledger | `EXECUTION_LEDGER.json` | primary1, reference1, Wolfram1; 잔여0 |

주요 identity는 다음과 같다.

- Core: `dbc4767b31775fb6655a92fb20d299f8bea9578f8340bd7bcff4d4f677cab551`.
- 수용 runner: `38cf5268831bbd3d2b17d356817ebae4b68f08e676da1e2cbf2cb313d7c6deb5`.
- Primary input: `40c059e324783492254831ca110e8d7d9b5e644fd7565eb0c6ad1eab8f3f2f15`.
- Primary result: `1a3b55f7c14a64a10a651de2df7b7f7d2df24d0b9e809b729f32d73377c90e84`.
- Independent result: `7e7bbae7ae5285230c14ef8fbb258ef15a92635eebfb0e0ca04df6933859c5ba`.
- 정식 일반 증명: `643e9c918353c068e648e5c74290a608b9993be487d7f4773278880db1a7c51c`.

독립 reference가 실제 primary result의 위 SHA를 기록하고 있음을 확인했다. Source bytes를 별도 parser로 해석하고 Decimal250 및 SciPy 경로를 사용하며 production core를 import하지 않는다.

## 2. 수용한 코드의 내용

정적 검토에서는 다음 연결을 확인했다.

- Exact decimal/Fraction 입력을 사용하고, 인증 입력의 bool·binary float·zero denominator·비유한 표현을 거부한다.
- Odd/even Taylor bracket, dyadic floor/ceiling, 양의 반복 squaring이 바른 enclosure 방향을 유지한다.
- Normalized weight의 좌표별 extreme formula와 직접 Gibbs pair ratio를 사용한다. 실제 Gibbs 상관관계를 독립 box corner의 물리 동시 실현성으로 확대하지 않는다.
- Full \(A\)의 exit upper bound에서 \(\lambda\)를 선택하고 비음수 substochastic \(P_-\)를 만든다.
- Matrix powers·Poisson weight·weighted terms를 모두 아래로 반올림하며, 양의 생략 tail을 버리는 lower-bound 논리를 유지한다.
- Pair overlap은 lower이고 \(\rho=1-\beta\)는 upper이다. \(n=1\)은 zero-sum 공간0의 명시적 별도 convention이다.
- Common killing \(\kappa\)를 full \(A\)에서 정확히 분리하고 residual endpoint에 한 번 적용한다.
- Endpoint와 whole-block \(M,U,E\)를 구별하며 \(E\) forcing에는 \(HU+GH^2/2\)를 사용한다.
- 동일 소스·동일 clock·interval-wide bounds의 실제 유효성은 caller가 공급해야 하는 전제로 남긴다.

수정 F01은 native clock scale의 선언과 고정 \(10^{-11}\,\mathrm{cm^3/s}\) 계산을 exact equality로 연결한다. 수정 F02는 모든 switching duration을 양수로 검사한다. 둘 다 현재 고정된 유효 입력의 수치값을 변경한 수리가 아니며, 잘못된 선언을 받아들이던 실제 guard 누락을 닫은 것이다.

원 이론 명확화 N1과 N2도 정식 proof에서 확인했다. 비음수 comparison 전제와 같은 prescribed \(F\)를 명시했고, analytical \(V_n\)과 stored rational \(\widehat U_n\)을 구별했다. Equation/code table의 \(P_-\) 기호도 실제 \(P(t)=I+A(t)/\lambda\)와 \(P_-\le P(t)\) 관계로 수정됐다.

## 3. 실제 finite-source 결과의 범위

Primary는 native100K para-H2의9개 source level과9개 downward pair를 사용한다. Fixed \((\mu,N)\)는

\[
(8,64),\ (32,128),\ (128,320),\ (256,512)
\]

이며 네 경우 모두 저장된 positive overlap을 확인했다. Thermal precision256bits, source polynomial512bits다. Instantaneous lower coefficient0을 finite-block positive gap으로 잘못 바꾸지 않는다.

별도의3개 forced fixture와1개 switched family는 선언된 수학적 대조 사례다. 실제 파괴율이나 실제 consumer trajectory로 해석하지 않는다. Source 진동 표지는 UNSPECIFIED, 미제공 전이는 MISSING_NOT_ZERO, physical collider density는 UNBOUND로 남는다.

## 4. Independent reference의 정확한 읽기

Reference는 source graph 및3개 forced primary fixture와1개 switched family를 모두 읽어 scope complete를 반환했다. Scalar interval comparison35건 중34건은 strict interior가 numerical precision에서 분해됐고, 한 건은 \(e^0=1\)의 정확한 \([1,1]\) 경계다. 그 한 건의 저장된 zero-margin resolution label을 그대로 유지한다.

Forced reference의 각 fixture는33개 시각을 확인한다. 저장된 최대 양의 numerical excess에는

\[
U:\ 2.7755575615628914\times10^{-17},\qquad
E:\ 1.3322676295501878\times10^{-15}
\]

가 있으며 명시된 \(\mathrm{atol}=2\times10^{-12}\), \(\mathrm{rtol}=2\times10^{-11}\) 안이다. 따라서 모든 floating-point slack이 엄격히 비양수였다고 표현하지 않는다. 일반 continuous-time 상계는 finite samples가 아니라 증명과 directed arithmetic에서 나온다.

Noncommuting fixture의 저장된 reset commutator norm은 약0.6133333이고 common-killing propagator split error는 약 \(4.44\times10^{-16}\)이다. 이는 해당 fixture의 numerical corroboration이며 full family의 proof 자체는 별도로 검토했다.

## 5. Wolfram 경고와 반환값의 역할

다음 원자료를 모두 읽었다.

- `verification/wolfram_new_checks.wl`: 새3-state full-A/common-killing·positive-path/chain·forcing integral·zero-killing limit·constant-forcing recurrence.
- `raw/WOLFRAM_TOOL_RESPONSE.json`: 실제 경고 prefix와 Out[1] 원문.
- `raw/WOLFRAM_RESULT.json`: 추출된23zero 결과와 warning 상태.

Out[1]의 이중 JSON 문자열을 데이터로 decode한 객체가 summary의 result와 정확히 일치한다. Tool의 isError는 false지만 다음 경고가 실제로 존재한다.

- `Symbol::undefined2`
- `Power::infy`
- `Infinity::indet`
- `General::messages`

스크립트는 global symbols를 사용하며 반환된 warning stream은 각 check에 연결된 위치를 제공하지 않는다. 실행 없이 특정 경고가 어디서 생겼는지, 아무 영향이 없는지, 어떤 check에만 영향을 주는지 확정할 수 없다. 그러므로 **23zero가 반환됐다는 관측**과 **warning-free 독립 증명을 수행했다는 주장**을 분리한다.

Primary exact arithmetic, independent general-n proof 및 Decimal/SciPy crosscheck는 이 경고를 무해하다고 가정하지 않고도 수용한 범위의 근거를 제공한다. 추가 CAS 호출은 요청하지 않는다. 원 경고와 당시 결과를 함께 보존하는 것으로 이번 한정된 검산 역할을 종료한다.

## 6. 자원과 재실행

| 실행 | 실제 측정 |
|---|---|
| Primary | window CPU0.659824898s, total process CPU at finalize0.791299421s |
| Reference | window CPU0.689574078s, total process CPU at finalize0.822867308s |
| Wolfram | kernel CPU0.286018s, kernel wall0.28199s |

각 local process의 stored60s 조건은 충족됐고 Wolfram은30s tool constraint로1회 호출됐다. Final serialization tail, remote/tool/LLM 비용과 metadata 비용을0으로 바꾸거나 이 측정치를 전체 프로젝트 총비용이라고 합산하지 않는다.

첫 실행 전 guard 수정2건과 scientific runtime repair0건을 구별한다. Actual campaign은 primary1, reference1, Wolfram1이며 새 잔여 allowance는 모두0이다. PHYS91 잔여0/0/0, global historical/remaining null, 이전 budget reset 없음이 유지된다.

## 7. 출판 metadata 관찰

`EXECUTION_PLAN.json`의 contract SHA는 초기 `d5d7ec0f...`이고 현재 contract SHA는 `1a034fce...`이다. 현재 문서는 reference backend를 Decimal250으로 명확히 했으며 numerical input·횟수·유한 allowance는 보존한다. 원 계획의 hash를 historical binding으로 남기고 현재 contract identity와 변경 이유를 별도 기록하면 정확하다. 이는 scientific replay의 이유나 core admission blocker가 아니다.

## 8. 수용 경계

이 판정은 declared finite generator/source graph의 interval·block certificate 구현을 수용한다. GL2022 reactive destruction, 실제 REC/REI molecular consumer, density, 전이 누락의 물리적0, 물리적 전체 closure, production을 수용하지 않는다.

HH_R10 OFF, production NOT_ISSUED, L4 false, physical admission delta0, central completion delta0, global physical completion null을 유지한다. 새 기본정리 발견이나 strong no-go를 주장하지 않는다.

정적 준비 기록과 사전 freeze의 NOT_EXECUTED_YET 표시는 그 당시의 사실로 보존하고, 이번 원 결과와 최종 review가 실제 후속 실행을 결속한다.

