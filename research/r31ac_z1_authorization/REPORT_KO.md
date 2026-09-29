# R31AC: z=1 authorization envelope와 model-discrimination design closeout

기준 remote는 `91aa8a0aeb4ddd3d89f0ef295cba2ddaac255f27`, tree `d4dc56edda2a4685c3a666a4b9ea7748428052e8`이다. R31AB authorization-gate follow-up은 현재 지시에 action token이 **승인 조건 설명의 일부로만 등장**했음을 올바르게 분류하여 science producer command 0개, science-node count 0으로 종료했다. 이 결과는 실행권한 gate의 의미론을 한 단계 더 엄밀히 할 필요가 있음을 보여준다.

## 1. 연구적 상태는 이미 execution-ready다

R31AB preflight에서 다음은 hash-lock되었고 변하지 않았다.

- z=1 preregistration SHA-256 `803b0968bd7f1fab41310469578b455ef03a64aae5beac1f23c1bab8afa19ddb`
- R31Z source SHA-256 `4ba03ba2adbdc9533f6472558b33a7edf86959bfc397e5fc8e3e90f8765ba034`
- R31AA source SHA-256 `f24d2acc0506e97dbefea107c126e53891d9879311aad60b9dd3b8e9a1be05d5`
- metric/rule aggregate SHA-256 `68b0d4c4b80443f374b9c49fa4c1737a8e2f39ed6b06f7340d052aa8c7c537b6`
- producer archive SHA-256 `c10c932a6cdad817982e00920a893733b367827b116d058791bf5aacad517cd9`
- comparison tolerance `1e-10`.

z=1에서 frozen R31Z/R31AA primary prediction separation은

[
||\Delta K||_2=0.2165779475378074/t_a,
qquad
\Delta D_{\max}=0.21927766897126583/t_a.
]

따라서 direct truth와 무관하게 적어도 한 모델은 각각

[
E_K\ge0.1082889737689037/t_a,
qquad
E_{D,\max}\ge0.10963883448563291/t_a
]

오차를 갖는다. Wolfram 재계산과 일치한다.

두 primary component를 단지 **design diagnostic**으로 Euclidean 결합하면 model-separation norm은
[
0.3082023742107794/t_a,
]
squared separation은
[
0.0949887034691613/t_a^2
]
이다. 이 값은 T-optimal/model-discrimination 문헌과 연결되는 실험설계 직관을 제공할 뿐, preregistered Pareto decision rule을 대체하지 않는다.

## 2. 왜 z=1 한 점이 합리적인 다음 실험인가

SciSpace에서 model-discrimination experimental design을 추가 조사했다.

- Ucinski & Bogacka, JRSS B (2005), DOI `10.1111/J.1467-9868.2005.00485.X`: multiresponse dynamic models의 T-optimal criterion은 rival models의 response divergence가 큰 조건을 선택한다.
- Dette & Titoff, Annals of Statistics (2009), DOI `10.1214/08-AOS635`: T-optimal discrimination design의 구조와 support-point 제한을 다룬다.
- Ponce de Leon & Atkinson, Biometrika (1991), DOI `10.1093/BIOMET/78.3.601`: model-discrimination design과 prior/sequential design의 관계를 다룬다.

현재 z=1 선택은 전체 연속구간에 대해 T-optimality를 증명한 결과가 아니다. 다만 **이미 preregistered된 candidate point가 두 frozen model의 primary outputs를 매우 강하게 분리한다**는 점에서 model-discrimination design 원리와 일치한다. z=3은 R31AA tuning에 이미 사용되었으므로 holdout 역할을 할 수 없고, z=1은 parent inventory에서 equivalent direct mixed node가 발견되지 않았다.

따라서 현재 권고는 그대로 유지한다.

`RECOMMEND_AUTHORIZE_MINIMAL_Z1_MIXED_NODE`

## 3. 최소 output contract의 충분성

Preregistered primary/secondary metrics를 계산하는 데 필요한 direct source는 정확히

- mixed O,
- mixed D_col,
- mixed D_row,
- independent mixed dotO

이다.

왜냐하면
[
K=(D_{col}-D_{row}^\dagger)/2
]
이므로 E_K는 D 두 block만으로 계산되고, E_Dmax도 동일하다. E_O와 E_dotO는 O,dotO로 계산한다. Direct metric-identity residual
[
||\dot O-D_{col}-D_{row}^\dagger||_2
]
도 이 네 output만으로 닫힌다.

따라서 H, neutral47, ionic2, full49, trajectory는 z=1 model-discrimination 질문에 **정보를 추가하는 필수량이 아니다**. 해당 계산을 동시에 실행하는 것은 현재 decision problem에 비해 범위를 불필요하게 넓힌다.

## 4. authorization semantics hardening

이번 follow-up은 단순 substring/token-presence gate가 안전하지 않음을 실제로 보여줬다. 현재 사용자 메시지에는 `AUTHORIZE_Z1_MINIMAL_MIXED_NODE` 문자열이 있었지만 “승인 문장이 아니라 승인 조건 설명”으로 등장했다.

따라서 action token과 authorization act를 분리한다.

새 canonical scope는 `WU088_Z1_MINIMAL_MIXED_SCOPE_V1`이며 canonical JSON SHA-256은

`730cf09525d3b09e3b45fab7b8cec78cce631182b2c87e7008f766a10839787c`

이다.

실행 승인은 다음 structured envelope가 **현재 상위 user instruction의 affirmative directive로 제공될 때만** 성립한다.

```json
{
  "schema": "WU088_Z1_MINIMAL_MIXED_AUTHORIZATION_V1",
  "authorize": true,
  "action": "AUTHORIZE_Z1_MINIMAL_MIXED_NODE",
  "scope_sha256": "730cf09525d3b09e3b45fab7b8cec78cce631182b2c87e7008f766a10839787c",
  "one_shot": true
}
```

다음은 승인 아님:

- token이 설명/인용/예시/거부문에 나타나는 경우,
- `authorize=false`,
- scope hash mismatch,
- schema/action mismatch,
- one_shot가 true가 아닌 경우.

이 authorization-envelope 변경은 science model, prereg metric, tolerance 또는 decision rule을 수정하지 않는다. 실행 의미론만 명확하게 만든다.

## 5. one-shot semantics

승인되면 정확히 한 z=1 node만 허용한다.

- z=1.0 a0
- tau=2.2358772390338113 t_a
- B192
- required four mixed outputs only.

Successful direct output identity가 생성되는 순간 authorization은 consumed된다. 실패가 producer 실행 전이면 소비하지 않고 blocker로 반환할 수 있다. Producer가 scientific output을 생성한 뒤의 재실행은 새로운 authorization 없이는 금지한다.

Output access 직후 frozen prereg E_K/E_Dmax Pareto rule을 한 번 적용하고 stop한다. 결과를 보고 model/tolerance/rule을 바꾸거나 second validation point를 자동 실행하지 않는다.

## 6. claim ceiling

z=1 한 점이 모델 discrimination에는 높은 정보가치를 갖지만 다음은 열지 않는다.

- interval-wide interpolation accuracy,
- transition amplitude/error,
- full-cell authority,
- complete-HH physical invariant sector,
- trajectory,
- H-skip,
- production,
- BR01/BR02,
- independent review.

Fixed Q는 represented-model definition으로 확립되어 `dotQ=0`이다. Physical invariance는 별도다.

## 결론

현재 research loop의 실제 남은 변수는 과학적 설계가 아니라 **명시적 one-shot 실행 승인**이다. Authorization envelope를 받은 다음에는 추가 설계·검증을 반복하지 않고 z=1 minimal node를 실행하여 frozen comparison을 한 번 수행하는 것이 stop-condition에 맞다.
