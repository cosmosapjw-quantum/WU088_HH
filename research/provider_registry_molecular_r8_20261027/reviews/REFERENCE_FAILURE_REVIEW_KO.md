# R8 최초 reference 실패의 독립 검토

**판정: REF01 — parameter-dependent accuracy contract mismatch. 최종 C9는 PENDING이다.**

최초 reference의 FAIL은 그대로 보존한다. 실제 실패는 native9 사례의 `phi factor` 한 scalar다. 727개 check 중 1개, 22,659개 성분 비교 중 1개가 실패했다. Primary는 실제 237/237 PASS이며, 최초 reference의 나머지 726개 check·22,658개 성분은 PASS다. 이 수를 물리적으로 독립된 사례 수로 해석하지 않는다.

## 관측값과 원인

저장된 생산값과 독립 Decimal80 값의 차이는 양수

`2.91082879488003260494168072896889699597324659550784e-30`

이다. 두 값이 모두 1보다 작기 때문에 기존 `1e-30 * max(1, |P|, |reference|)` 허용치가 정확히 `1e-30`이 되어 실패했다. 과소상계를 발견한 항목은 아니다.

현재 생산 코드는 음의 d에서

`phi = (1 - exp(d*delta))/(-d)`

를 exp의 인증된 하한으로부터 위로 계산한다. 따라서 exp 구간의 절대 폭은 `1/|d|`만큼 증폭된다. Native9의 `d=-1/20000000`에서는 이 인자가 20,000,000이다. 고정된 근접성 허용치는 이 변환을 반영하지 못했다.

저장된 exp 구간을 공통분모 `S=2^128`로 쓰면 하한·상한의 분자는 각각

- `340282358847370961587573751651638012542`
- `340282358847370961587573751651638012593`

이므로 폭은 정확히 `51/S`다. `ell <= z=exp(d*delta) <= u`와 생산 규칙 `P=ceil_S((1-ell)/|d|)`에서

`0 <= P-phi <= (u-ell)/|d| + 1/S = 1020000001/S`

를 얻는다. 이는 관측된 gap의 원인을 설명하는 매개변수 의존 산술 경계다. 기존 FAIL을 이 공식만으로 PASS로 고쳐 쓰는 것은 아니다.

이전 preflight는 일반적인 상방 산술의 유효성을 검토했지만, reference의 고정 accuracy threshold에 필요한 이 작은 `|d|`의 증폭 인자를 지적하지 못했다. 그 제한을 이번 발견으로 명시한다.

## 최소 수정 제안

전체 primary·reference를 다시 실행하거나 다른 비교의 blanket tolerance를 완화할 필요는 없다. 원본 결과와 소스를 유지하고, 별도의 제한된 productive-repair 계약 아래 이 scalar만 독립 exact rational 방식으로 재판정하는 것이 타당하다.

`kappa=-d>0, x=kappa*delta`라 두고 `0<x<=1`을 정확히 확인한다. 적분의 급수는

`phi = delta * sum(k=0..infinity, (-x)^k/(k+1)!)`

다. 항의 크기 비가 `x/(k+2)<=1`이므로 교대급수의 고정 부분합으로 엄밀한 상하한을 얻는다. 예를 들어 degree를 실행 전에 고정하여

`U = delta * sum(k=0..8, (-x)^k/(k+1)!)`

`L = delta * sum(k=0..9, (-x)^k/(k+1)!)`

로 두면 `L<=phi<=U`, `U-L=delta*x^9/10!`다. 새 체크는 저장된 생산값 P에 대해 다음을 exact Fraction으로 확인한다.

1. `P>=U`: 실제 생산값이 엄밀한 상계임을 직접 인증한다.
2. `P-L <= ((u-ell)/kappa+1/S)+(U-L)`: 관측 gap에 맞춘 임의 허용치 없이, 유도된 산술 경계 안에 있음을 확인한다.

새 solver, exp 평가, production import, ODE, generator 또는 과거 R6/R7 실행이 필요하지 않다. Source hash·degree·assertion·새 실행 허용량은 먼저 고정하고, 실패하면 보존 후 중단한다. 최초 `REFERENCE_RESULTS.json`은 FAIL과 기존 hash 그대로 남기고 별도 scalar 결과·process receipt로 재판정을 기록해야 한다.

## 근거와 남은 범위

- Primary 원본 SHA256: `520110d1cae1677491aecd7216621c25f1098470c939ee027d5df3bde183686b`
- 최초 reference 원본 SHA256: `da699b9a8b53389e3d222f34a5a421cd88ce17787bde69cc2e9bed5fb15409df`
- Reference source commit: `b87ea61ab2d5e17221a6cf3b710aec074eb1a28e`
- 실제 OS CPU: primary 3.807278초, reference 0.440898초. 외부 영수증은 imports·serialization을 포함한다.

현재 증거는 core·primary input·family 결속의 수정을 요구하지 않는다. 실제 물리 consumer·reactive source·density/clock 결속은 여전히 미결이며 CAS의 qualified 상태도 달라지지 않는다. 원 primary/reference 예산은 소진된 상태다.

심사자는 실패 항목과 관련 source·원본 factor·contract·receipt만 읽고 수학적으로 진단했다. **과학 실행·runner/import·AST·코드 수정·외부 쓰기는 0**이다. 위 제안은 아직 실행되지 않았으며, 최종 C9 PASS를 선언하지 않는다.

