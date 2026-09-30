# R31AG: z=3.5 fresh validation authorization gate

기준 parent는 `e62c5093b67fa0269069c4e64e6eb17a06c9a37e`, tree `b52b792d1e59dea0de662f4ddf2b5d0dbc3980da`이다. R31AF NCP follow-up은 science node 0개로 six-node adaptive model을 재현했고, z=3.5를 다음 fresh validation point로 preregister했다.

## 1. 현재 상태

R31AF model:

- training z = {0,0.5,1,2,3,4}
- cells = [0,.5],[.5,1],[1,2],[2,3],[3,4]
- node reproduction / continuity / metric identity = binary64 roundoff 수준
- independent validation points = [].

z=0.5는 R31AD에 대한 독립 validation을 완료한 뒤 R31AF training으로 소비되었다. 따라서 R31AF 자체는 아직 독립 validation을 갖지 않는다.

Parent preregistration은

- selected z = 3.5 a0
- time = 7.825570336618339 t_a
- B192
- execution_authorized=false
- direct_z35_output_accessed=false

로 잠겨 있다.

Current-loop provider title search에서도 Dropbox/Drive에서 `B192_z3.5` direct object는 발견되지 않았다. 이 검색은 exhaustive absence proof가 아니므로, independence의 authoritative 근거는 parent prereg + actual pre-execution source inventory다.

## 2. z=3.5 information value

Frozen R31AF/R31Z model-only separation은

[
Delta K=0.19122378403347964/t_a,
]

[
Delta D_{max}=0.2095387347094023/t_a,
]

[
S=sqrt{Delta K^2+Delta D_{max}^2}
=0.2836776637729875/t_a.
]

임의 direct truth X에 대해

[
||G-L||le ||G-X||+||L-X||
]

이므로 적어도 한 model은

[
E_Kge0.09561189201673982/t_a,
]

[
E_{D,max}ge0.10476936735470115/t_a
]

오차를 갖는다.

Wolfram 재계산에서 primary separation은 tolerance (10^{-10})보다 각각 약 (1.912	imes10^9), (2.095	imes10^9) 배 크다.

z=3.5의 design score는 남은 fresh z=2.5보다

[
0.002888151356970459
]

크고 상대 margin은 약 1.029%다. 따라서 선택은 roundoff 수준의 tie는 아니지만 두 후보 중 압도적인 optimum이라고 부르지는 않는다. 이미 output access 전에 selection rule로 z=3.5가 잠겼으므로 그대로 따른다.

## 3. 왜 z=3.5가 다음 독립 검증으로 적절한가

R31AF의 adaptive modification은 [0,1]에만 있다. z=3.5는 [3,4] cell에 있으므로 z=0.5 residual을 이용한 left-cell refinement의 직접 영향권 밖이다. 따라서 다음 direct point는

1. R31AF의 regional generalization,
2. 기존 right-cell interpolation,
3. R31Z와의 frozen discrimination

을 동시에 검사한다.

SciSpace에서 local a posteriori refinement와 model-discrimination/holdout methodology를 검토했다. Jakeman–Roberts는 local error indicator가 큰 region에만 refinement를 집중하는 원리를, Buffa–Giannelli는 local residual indicator 기반 adaptive refinement를 제공한다. 이 문헌은 WU088_HH accuracy를 대신 증명하지 않는다.

## 4. 실행 범위의 최소성

Preregistered primary metrics:

[
E_K=||K_{pred}-K_{direct}||_2,
quad K=(D_{col}-D_{row}^dagger)/2,
]

[
E_{D,max}=max(E_{Dcol},E_{Drow}).
]

Mandatory secondary는 E_O, E_dotO, E_Dcol, E_Drow 및 metric identity residual이다.

따라서 direct source로 필요한 것은 정확히:

- mixed O 47x2
- mixed D_col 47x2
- mixed D_row 2x47
- independent mixed dotO 47x2

뿐이다.

H, neutral47, ionic2, full49, trajectory는 이 validation question에 필요하지 않는다.

## 5. canonical authorization scope

Canonical JSON algorithm:

- UTF-8
- recursive lexicographic key sort
- separators exactly `,` and `:`
- no whitespace
- finite JSON numbers only
- SHA-256 over exact canonical bytes.

Scope SHA-256:

`f43faaf5746a5fda5cd26593ee69e97c0f2be8239727a62081d49357e3c2a9b4`.

Future authorization은 current upper-level user instruction이 다음 envelope를 affirmative directive로 제공할 때만 성립한다.

```json
{
  "schema": "WU088_R31AF_Z35_MINIMAL_MIXED_AUTHORIZATION_V1",
  "authorize": true,
  "action": "AUTHORIZE_R31AF_Z35_MINIMAL_MIXED_NODE",
  "scope_sha256": "f43faaf5746a5fda5cd26593ee69e97c0f2be8239727a62081d49357e3c2a9b4",
  "one_shot": true
}
```

Action string이 설명/예시/조건/부정문에 존재하는 것만으로는 승인하지 않는다.

## 6. future one-shot comparison

승인되면 exactly one z=3.5 node를 실행한 뒤 frozen

- R31AF_ADAPTIVE_SIX_NODE_CUBIC_O_LINEAR_K
- R31Z_GLOBAL_QUINTIC_O_QUADRATIC_K

를 prelocked E_K/E_Dmax Pareto rule로 한 번 비교한다.

Verdict:

- `PARETO_SUPPORTED_AT_Z35`
- `GLOBAL_SUPPORTED_AT_Z35`
- `TRADEOFF_UNRESOLVED`.

Design score S는 final decision score가 아니다.

Scientific output identity가 생성되면 authorization은 consumed된다. 결과를 보고 retune하거나 z=2.5를 자동 실행하지 않는다.

## 7. claim ceiling

z=3.5 single point도 다음을 자동 승인하지 않는다.

- interval-wide interpolation accuracy
- transition amplitude/error
- full-cell authority
- complete-HH fixed-Q physical invariance
- trajectory
- H-skip
- production
- BR01/BR02
- independent project review.

## 결론

R31AF의 첫 독립 validation으로 **z=3.5 minimal mixed OD + independent JVP node를 실행하는 것을 과학적으로 권고**한다.

`RECOMMEND_AUTHORIZE_R31AF_Z35_MINIMAL_MIXED_NODE`

R31AG 자체에서는 실행하지 않는다.
