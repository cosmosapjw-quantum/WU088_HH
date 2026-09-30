# R31AN: R31AK freeze 후 B192 reference-certification 전환

기준 parent는 commit `34eaa2ab52fc782825235629dade382b2322d2a4`, tree `f2a43200e79f45b5cfd57b81afd4da99c7d402c3`이다. z=0.75 one-shot은 PRIMARY=`PARETO_SUPPORTED_AT_Z075`, SECONDARY=`REFINED_PARETO_SUPPORTED_AT_Z075`로 종료했고, R31AM의 frozen action은 `FREEZE_R31AK_LOCALLY_SUPPORTED__PIVOT_TO_REFERENCE_CERTIFICATION`이다.

## 1. interpolation 연구의 stop condition

R31AK model freeze receipt:

- model aggregate SHA256 `50a5f0eeda63d6e04795e301f6b07a41fd11a4b145e267cfc608261356d49b30`
- eight-node manifest `d978792bef0c3bf2b670d4e73d70dcea391645f38555f1070323037610162ece`
- z0.75 selected prediction arrays `66ff922f687a796417e23147e5720af9a467ef7d988b490a2709e0a2967c4010`
- z0.75은 fresh single-geometry validation으로 보존하며 training으로 자동 소비하지 않음
- automatic knot / next science node = false.

따라서 R31AN은 interpolation degree, knot, validation geometry를 추가하지 않는다.

## 2. 무엇이 아직 미인증인가

현재 direct mixed reference는 B192다. z=0.75에서 R31AK-vs-R31Z 및 refined-vs-coarse 결과는 모두 강하지만, RETURN은 `SOURCE_ACCURACY_BOUND_UNAVAILABLE`, `B_order_reference_certification=NOT_ADMITTED`를 유지한다.

Repo의 과거 H anchor에는 B160/B192 총 470/470 element order-comparison이 있다. 최대 |H192-H160|은 z=0에서 약 1.61e-9 Eh까지 작았지만, 기존 보고서 자체가 이를 **finite two-order increment**로만 분류하고 continuum integral error의 rigorous upper bound로 보지 않는다. 또한 이 자료는 H block이고 현재 primary reference는 mixed O,D,dotO이므로 그대로 전이할 수 없다.

MATHEMATICS.md는 wide scalar special-function implementation에 asymptotic approximations가 존재함도 명시한다. 따라서 reference error는 최소한 다음을 구분해야 한다.

    epsilon_ref <= epsilon_order
                 + epsilon_special_function
                 + epsilon_roundoff
                 + epsilon_assembly

B-order sweep는 주로 epsilon_order의 empirical behavior를 본다. 모든 order에 공통인 special-function bias를 자동 검출하지 못한다.

## 3. 첫 단계: 동일 z=0.75의 등비 3-order ladder

최소 empirical convergence ladder를

    B144, B192, B256

으로 고정한다. 이유는

    192/144 = 256/192 = 4/3

으로 동일 refinement ratio를 갖고, B192 existing output을 재사용해 새 order는 두 개만 필요하기 때문이다.

Future required direct blocks at each new order:

- O 47x2
- D_col 47x2
- D_row 2x47
- independent dotO 47x2.

H, neutral47, ionic2, full49, trajectory는 reference-order question에 불필요하다.

현재 Drive/Dropbox title search에서는 z=0.75 B144/B256 결과를 찾지 못했지만 absence proof로 사용하지 않는다. NCP source/archive inventory가 authority다.

## 4. 3-order analysis의 claim ceiling

Scalar 또는 fixed-direction matrix power model

    Q_n = Q_inf + C n^{-p}

을 **조건부로** 가정하면 equal ratio r=4/3에서

    p_obs = log(d_144,192 / d_192,256) / log(4/3),

    E_192,cond = d_192,256 / (1-(3/4)^p_obs),

    E_256,cond = d_192,256 / ((4/3)^p_obs-1).

그러나 spectral-norm increments에서 이 식은 error matrices의 방향이 order와 함께 바뀌면 정확한 model identity가 아니다. 따라서 p_obs와 extrapolated errors는 `CONDITIONAL_ASYMPTOTIC_DIAGNOSTIC`이지 rigorous bound가 아니다.

더 일반적으로 future increments에 대해

    ||Delta_(k+1)|| <= q ||Delta_k||, 0<=q<1

이라는 contraction을 **증명할 수 있다면**

    ||Q_inf-Q_latest|| <= q/(1-q) ||Delta_last||

의 geometric tail bound를 얻을 수 있다. 두 개의 observed ratios만으로 future contraction을 증명할 수는 없다.

Wolfram exact/numeric check에서 위 식과 equal-ratio 구조를 검산했다.

## 5. 현재 verdict가 exact reference perturbation에 견디는 budget

z=0.75 PRIMARY observed margins:

- K: 0.31982343565606725 /t_a
- Dmax: 0.33345694057636704 /t_a.

SECONDARY refined-vs-coarse margins:

- K: 0.05713242012648218 /t_a
- Dmax: 0.08782058637980173 /t_a.

Reference perturbation norm upper bound epsilon_i가 실제로 확보되었다면 margin 변화는 최대 2 epsilon_i다. tolerance 1e-10/t_a를 보존하는 strict sufficient radii:

PRIMARY:
- epsilon_K < 0.15991171777803362 /t_a
- epsilon_Dmax < 0.16672847023818352 /t_a.

SECONDARY:
- epsilon_K < 0.028566210013241087 /t_a
- epsilon_Dmax < 0.04391029313990087 /t_a.

두 verdict를 동시에 robust하게 만들기 위한 common target은 0.028566210013241087/t_a보다 작은 actual normwise reference bound다.

이 값은 **목표 budget**이지 현재 B192 error estimate가 아니다.

## 6. 문헌 결론

SciSpace에서 두 부류를 분리했다.

1. Gonnet, ACM Computing Surveys 2012, DOI 10.1145/2333112.2333117:
adaptive quadrature error estimator에는 공통 failure mode가 있으며 estimator 자체의 가정과 구조를 분리해야 한다.

2. Fousse, ARITH 2007, DOI 10.1109/ARITH.2007.8:
실제 certified quadrature는 derivative bound와 multiple-precision/roundoff control을 이용해 true integral을 포함하는 interval을 만든다.

3. Phillips & Roy, Journal of Fluids Engineering 2014, DOI 10.1115/1.4027353:
Richardson-type discretization estimates는 asymptotic range에서만 신뢰 가능하며 non-asymptotic/oscillatory convergence를 별도로 다뤄야 한다.

4. Oates et al., JRSS B, DOI 10.1093/jrsssb/qkae098:
unknown convergence order를 probabilistic Richardson framework로 다룰 수 있으나 이는 probabilistic uncertainty model이며 rigorous enclosure와 동일하지 않다.

따라서 R31AN은 empirical order stability와 rigorous certification을 같은 gate로 합치지 않는다.

## 7. R31AN의 다음 bounded action

이번 node에서는 B144/B256를 실행하지 않는다.

NCP handoff는:

1. existing source/archive에서 mixed OD/JVP producer가 n=144,256을 source 변경 없이 허용하는지 확인,
2. B144/B256 existing output inventory,
3. future comparator와 3-order diagnostics를 direct output 이전에 lock,
4. B144+B256 두 order의 same-z transaction에 대한 별도 one-shot authorization scope 생성,
5. rigorous source-bound feasibility audit를 병렬 read-only로 수행,
6. science execution 없이 return.

Future authorized order study가 수행되더라도 결과는 우선
`B_ORDER_STABILITY_EMPIRICAL` 또는 `B_ORDER_NONCONTRACTING`으로 분류한다. Rigorous derivative/interval/special-function bound가 별도로 없으면 `SOURCE_ACCURACY_BOUND_UNAVAILABLE`을 유지한다.

## 결론

Interpolation axis는 stop condition을 충족했다. 다음 scientific question은 “R31AK를 더 refine할 것인가”가 아니라 “B192 reference와 underlying source evaluation을 어느 norm에서 얼마까지 신뢰할 수 있는가”다. R31AN은 그 certification DAG의 입구를 고정한다.
