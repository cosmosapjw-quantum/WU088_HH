# R31AO: source-authority-compliant unequal reference-order ladder

기준 R31AN remote는 commit `5f2fb0e87d6cf42cd1dd7e9f26b902e06c04b1cf`, tree `4f53b7220c453aaf3a93efb772316bec8c925109`이다. R31AN의 `REFERENCE_ORDER_INPUT_BLOCKED`는 B144/B192/B256 등비 ladder의 producer contract가 닫히지 않았다는 뜻이며, reference-certification 질문 전체가 막혔다는 뜻은 아니다.

## 1. recovered authority가 허용하는 ladder

R31AN source audit에서 확인된 사실:

- OD Python/native path는 n<=192를 허용하고 n>192를 거부한다.
- JVP는 `frozen_grid_n{n}.npz`가 미리 존재해야 한다.
- recovered frozen grids는 B128, B160, B192가 존재한다.
- exact-weight source는 frozen B96--B192 intended range를 선언한다.
- B256은 unchanged OD authority 밖이다.
- B144는 OD size guard 안이지만 frozen JVP grid가 없다.

따라서 현재 source를 변경하지 않고 양쪽 OD+independent-JVP contract를 동시에 만족하는 자연스러운 3-order ladder는

    B128 -> B160 -> B192

이다.

ratio는 5/4와 6/5로 같지 않다. Equal-ratio convenience는 잃지만 source authority는 보존한다.

Current-turn Drive/Dropbox title search에서 z=0.75 B128/B160 complete output을 찾지 못했지만 이는 absence proof가 아니다. NCP follow-up에서 bounded local/archive/member metadata inventory를 다시 수행한다.

## 2. unequal-ratio conditional observed order

조건부 scalar/fixed matrix-error-direction model

    Q_n = Q_inf + C n^{-p}, p>0

에서

    rho = d128160/d160192

는

    rho=((5/4)^p-1)/(1-(5/6)^p)

를 만족한다.

Wolfram exact analysis에서 이 함수는 p>0에서 strictly increasing이고 range는

    rho > log(5/4)/log(6/5)
        = 1.2239010857415446077...

이다.

따라서:

- rho <= 1.2239010857415446이면 positive-p power model과 normwise로 양립하지 않는다.
- rho가 threshold보다 크면 p>0 solution은 유일하다.

## 3. conditional error formulas

Power model이 실제로 유효한 scalar/fixed-direction mode에서

    E192_cond = d160192 / ((6/5)^p - 1)

    E160_cond = d160192 / (1 - (5/6)^p)

이다.

spectral 2-norm increments만으로 matrix error direction stability가 보장되지 않는다. Future comparator는 raw complex difference arrays, spectral/Frobenius norm, max abs, normalized Frobenius alignment 및 scalar-fit residual을 기록한다. Threshold를 새 certification rule로 발명하지 않는다.

상태는

    CONDITIONAL_UNEQUAL_RATIO_ASYMPTOTIC_DIAGNOSTIC

이고 rigorous=false다.

## 4. finite-order verdict-stability replay

Future B128/B160 direct mixed outputs가 확보되면 같은 z=0.75에서 frozen primary/secondary comparisons를 finite-order reference별로 replay한다.

- B128
- B160
- B192

세 reference에서 primary와 secondary verdict가 모두 동일하면

    B_ORDER_VERDICT_STABLE_OVER_128_160_192

라고 기록할 수 있다.

이는 continuum/source certification이 아니다.

## 5. rigorous certification은 여전히 별도 blocker

R31AN rigorous audit의 결론은 유지한다.

Missing:
- quadrature remainder/derivative bound
- special-function enclosure
- certified roundoff/transcendental bound
- outward-rounded assembly bound.

따라서 order study가 성공해도 SOURCE_ACCURACY_BOUND_UNAVAILABLE과 rigorous-reference blocker를 자동으로 닫지 않는다.

SciSpace 문헌도 같은 claim ceiling을 지지한다. Roy는 reliable Richardson-type estimate에 asymptotic range와 최소 세 systematically refined solutions가 필요함을 강조한다. Baker는 nonuniform refinement에서 observed exponent가 formal order와 달라질 수 있음을 보인다. Phillips & Roy는 non-asymptotic/oscillatory convergence를 별도 uncertainty regime으로 다룬다.

## 6. bounded next action

이번 node에서는 B128/B160 science computation을 실행하지 않는다.

NCP follow-up은:

1. source/hash/grid authority 재확인,
2. z=0.75 B128/B160 complete output inventory,
3. unchanged producer의 transaction scope dry audit,
4. unequal-ratio raw-array comparator/p-solver prelock,
5. finite-order primary+secondary replay contract prelock,
6. outputs가 없고 authority가 닫히면 B128+B160 one-shot authorization scope 생성,
7. science_node_count=0으로 종료.

B192 existing output은 재사용한다.

## 결론

B256 blocker 때문에 producer를 확장할 이유는 없다. 현재 authority 안에 이미 B128/B160/B192 ladder가 있고 unequal refinement ratio는 수학적으로 처리 가능하다. 다음 질문은 “새 order를 지원하도록 코드를 바꿀 것인가”가 아니라 “기존 authority로 B128/B160/B192 finite-order stability가 성립하는가”다.
