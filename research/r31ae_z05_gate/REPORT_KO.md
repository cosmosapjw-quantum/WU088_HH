# R31AE: selected z=0.5 validation authorization decision

기준 parent는 `0383a3b3c66a3b3e820c7deb228f7cd90b249995`, tree `94de041166451db62e0cc653a745933daffcddda`이다. R31AD NCP follow-up은 새 science node 없이 z=0,1,2,3,4 five-node model을 재현했고, fresh midpoint 후보 가운데 prediction-only design score가 가장 큰 `z=0.5 a0`를 선택해 preregistration을 잠갔다.

## 1. 현재 판정

과학적 권고는

`RECOMMEND_AUTHORIZE_R31AD_Z05_MINIMAL_MIXED_NODE`

이다.

이 권고는 R31AD가 R31Z보다 우수할 것이라는 예측이 아니다. Frozen model predictions만으로 선택된 z=0.5가 두 모델을 강하게 구별할 수 있다는 information-value 판정이다.

z=0.5에서 model-only separation:

- `DeltaK_model = 0.19753269207305832 /t_a`
- `DeltaDmax_model = 0.2140818408032047 /t_a`
- `S = sqrt(DeltaK^2+DeltaDmax^2) = 0.29129057485493476 /t_a`.

임의의 direct truth X에 대해 triangle inequality로

[
||G-L|| le ||G-X||+||L-X||
]

이므로 적어도 한 모델은

[
E_K ge 0.09876634603652916/t_a,
]

[
E_{D,max} ge 0.10704092040160235/t_a
]

오차를 갖는다. Wolfram exact/numeric evaluation으로 이 half-gap을 재검산했다. Primary separation은 preregistered tolerance (10^{-10})보다 각각 약 (1.98	imes10^9), (2.14	imes10^9) 배 크다.

## 2. midpoint selection의 robustness와 한계

Fresh candidates의 design score는:

- z=0.5: 0.29129057485493476
- z=2.5: 0.280789512416017
- z=3.5: 0.2836776637729875

이다. 두 번째로 큰 z=3.5와의 차이는

[
0.007612911081947282
]

이고 상대 margin은 약 2.684%다.

따라서 z=0.5 selection은 binary64 roundoff 때문에 우연히 뒤집힐 수준은 아니지만, 다른 fresh midpoint들보다 압도적으로 유일한 optimum이라고 부를 정도의 큰 gap도 아니다. Selection rule이 output access 전에 이미 고정되었으므로 z=0.5를 그대로 사용한다. 다른 midpoint를 결과를 보고 선택하는 것은 금지한다.

z=1.5는 preexisting direct OD-only output이 있었고 independent JVP가 없으므로 fresh full validation candidate에서 제외되었다.

## 3. holdout / sequential-design 의미

R31AD development에서는 z=0,1,2,3,4를 모두 training으로 소비했으므로 independent validation point가 0개다. z=0.5 selection에는 direct truth가 사용되지 않고 두 frozen model prediction만 사용되었다.

SciSpace current-loop 검색에서:

- Nakkiran & Blasiok, arXiv:1809.05596: adaptive exploration과 holdout exposure를 분리해 false discovery를 줄이는 Generic Holdout 원리.
- Arnold et al., arXiv:2404.18678: sequential model evaluation에서 selection uncertainty를 보존하는 framework.
- Rabinowicz & Rosset, arXiv:1802.00996: interpolation/extrapolation point의 prediction error는 in-sample fit와 별도로 평가해야 함.

이 문헌들은 WU088_HH의 interpolation accuracy를 증명하지 않는다. 현재 적용하는 핵심 원칙은 **selected holdout의 direct output을 model retuning 전에 한 번만 사용하고, single-point verdict를 interval-wide accuracy로 확대하지 않는 것**이다.

## 4. 최소 output의 충분성

Future primary metrics:

[
E_K=||K_{pred}-K_{direct}||_2,
quad
K=(D_{col}-D_{row}^dagger)/2,
]

[
E_{D,max}=max(E_{Dcol},E_{Drow}).
]

Mandatory secondary metrics는 E_O, E_dotO, E_Dcol, E_Drow 및 metric-identity residual이다.

따라서 direct source로 필요한 것은 정확히:

- mixed O 47x2,
- mixed D_col 47x2,
- mixed D_row 2x47,
- independent mixed dotO 47x2

이다.

H, neutral47, ionic2, full49, trajectory는 이 validation question을 닫는 데 필요하지 않다.

## 5. canonical authorization scope

R31AC one-shot return에서는 scope JSON의 canonical serialization이 명시되지 않아 independent digest rederivation이 UNVERIFIED로 남았다. R31AE에서는 이를 수정한다.

Canonicalization:

- UTF-8 JSON
- object keys recursively sorted lexicographically
- no whitespace: separators `,` and `:`
- JSON booleans/lists/numbers as stored
- NaN/Infinity forbidden
- SHA-256 of those exact bytes.

R31AE scope digest:

`f9872cb045fef146987829620c669fb99f2417a787d74cde26dfee107153a567`

이다.

Future authorization은 현재 상위 user instruction이 affirmative directive로 다음 envelope를 제공할 때만 유효하다.

```json
{
  "schema": "WU088_R31AD_Z05_MINIMAL_MIXED_AUTHORIZATION_V1",
  "authorize": true,
  "action": "AUTHORIZE_R31AD_Z05_MINIMAL_MIXED_NODE",
  "scope_sha256": "f9872cb045fef146987829620c669fb99f2417a787d74cde26dfee107153a567",
  "one_shot": true
}
```

Token mention, quote, example, condition, negation, hash/schema/action mismatch는 승인으로 취급하지 않는다.

## 6. one-shot future execution contract

승인되면 exactly one node:

- z = 0.5 a0
- tau = 1.1179386195169057 t_a
- B192
- four mixed outputs only.

Direct output identity가 생성되면 authorization은 consumed된다. Frozen model/prereg/selection hashes를 output access 전에 확인한다.

Future verdict:

- `PARETO_SUPPORTED_AT_SELECTED_MIDPOINT`
- `GLOBAL_SUPPORTED_AT_SELECTED_MIDPOINT`
- `TRADEOFF_UNRESOLVED`.

Decision은 E_K/E_Dmax의 prelocked Pareto rule만 사용한다. Design score S는 final model-selection score가 아니다.

## 7. claim ceiling

한 z=0.5 결과로 다음을 승인하지 않는다.

- interval-wide R31AD accuracy
- transition-amplitude/error bound
- trajectory
- full-cell
- complete-HH fixed-Q physical invariance
- H-skip
- production
- BR01/BR02
- independent project review.

결과를 본 뒤 R31AD/R31Z를 retune하거나 z=2.5/3.5를 자동 실행하지 않는다.

## 결론

R31AD five-node model의 첫 independent validation으로 z=0.5 minimal mixed OD+independent-JVP node를 실행하는 것이 현재 가장 직접적인 다음 과학 실험이다. 이 R31AE node 자체는 실행을 승인하지 않으며 science-node count는 0이다.
