# R31AD: five-node unit-cell structure-preserving interpolation and next-validation design

기준 parent는 `82d3d076dc229c20236747738f0ed14861a1b741`, tree `9127841194bd0f252022aac3a6acd320e84e2647`이다. R31AC one-shot z=1 science node는 정상 종료했고, frozen preregistered rule에서 `GLOBAL_SUPPORTED_AT_Z1`이 나왔다. 이 판정은 z=1 한 점에서의 **상대적 model discrimination**이며 absolute adequacy나 interval-wide admission이 아니다.

## 1. z=1 결과의 올바른 해석

Independent z=1 direct comparison:

- R31Z global:
  - E_K = 0.3650757630525158 /t_a
  - E_Dmax = 0.3846020589552572 /t_a
  - E_O = 0.1434143913780898
  - E_dotO = 0.16665577052862268 /t_a
- R31AA local:
  - E_K = 0.39755079404225363 /t_a
  - E_Dmax = 0.41595304639628755 /t_a
  - E_O = 0.16582143077497558
  - E_dotO = 0.16857337231144143 /t_a

따라서 z=1에서 global은 local보다 E_K 약 8.17%, E_Dmax 약 7.54% 낮다. 하지만 두 모델의 z=1 prediction separation은 E_K 축 0.2165779475378074/t_a, Dmax 축 0.21927766897126583/t_a였고 실제 오차는 이 separation보다 훨씬 크다.

- global E_K / model separation = 1.6857
- local E_K / model separation = 1.8356
- global E_Dmax / model separation = 1.7539
- local E_Dmax / model separation = 1.8969

따라서 `GLOBAL_SUPPORTED_AT_Z1`은 **winner selection**이지 `GLOBAL_ADEQUATE_AT_Z1`이 아니다. 현재 두 coarse interpolant 모두 z=1 mixed-connection accuracy 면에서 절대오차가 작다고 말할 근거는 없다.

z=3에서는 R31AA local이 global보다 낮은 primary errors를 보였지만, R31AA form은 그 z=3 실패를 본 뒤 설계되었으므로 z=3은 post-hoc tuning data다. 즉 현재 evidence map은:

- left coarse cell [0,2]: z=1 independent point에서 global 상대 우세
- right coarse cell [2,4]: z=3에서 local 개선 관측, 그러나 독립 validation 아님
- interval-wide winner: 미결정

## 2. 다음 연구 방향: coarse 두 모델의 승자 경쟁을 종료하고 node density를 올린다

이제 z=0,1,2,3,4의 direct mixed O,D,dotO node가 모두 존재한다. R31AD는 이 다섯 integer node를 **새 training set**으로 재분류한다.

- z=0,2,4: 기존 fit nodes
- z=1: R31Z/R31AA에 대한 independent validation을 완료한 뒤 R31AD 개발에서는 training으로 소비
- z=3: R31AA tuning/post-hoc data이며 R31AD에서는 training으로 소비

따라서 R31AD 자체에는 아직 independent validation point가 없다.

새 candidate는 각 unit cell [j,j+1], j=0,1,2,3에 대해:

1. O: endpoint O와 time derivative dotO를 맞추는 cubic Hermite
2. K=(D_col-D_row†)/2: endpoint K를 잇는 linear interpolation
3. D_col = dotO/2 + K
4. D_row† = dotO/2 - K

로 정의한다.

이 construction은 각 integer node에서 O,dotO,K,D를 정확히 재현하고, O는 전체 [0,4]에서 C1이며 K와 D는 node에서 연속이다. 또한 모든 cell 내부에서

    dotO - D_col - D_row† = 0

이 algebraic identity로 성립한다.

## 3. 왜 unit-cell refinement가 합리적인가

Cubic Hermite의 표준 scalar remainder factor는 midpoint에서

    h^4 / 384,

linear interpolation의 midpoint factor는

    h^2 / 8

이다. Wolfram exact 계산으로 두 factor와 metric identity를 재확인했다.

기존 R31AA coarse cell width는 2 a0, 새 unit-cell width는 1 a0다. underlying 4th/2nd derivative upper bound가 동일하다는 **조건부** 가정 아래 remainder coefficient만 비교하면:

- O cubic factor: 16배 감소
- K linear factor: 4배 감소

한다.

이는 actual HH error가 정확히 1/16,1/4이 된다는 뜻이 아니다. derivative bounds가 cell마다 다르고 현재 interval enclosure가 없기 때문이다. 다만 더 높은 global polynomial degree를 올리는 대신 **이미 존재하는 direct nodes로 locality를 높이는 방향**에는 명확한 수학적 근거가 있다.

## 4. R31AD validation policy

R31AD가 z=1,z=3을 training으로 사용하면 기존 validation credit은 소모된다. 따라서 새 candidate를 검증하려면 새로운 direct point가 필요하다.

Candidate validation set은 새 unit cells의 midpoints:

    {0.5, 1.5, 2.5, 3.5} a0

로 제한한다. 이 지점들은 cubic-Hermite와 linear-K remainder factor가 각 cell에서 최대가 되는 자연스러운 stress points다.

새 science node를 고르기 전에:

1. 기존 archive/provider/local runtime에서 동등 direct mixed node가 이미 존재하는지 inventory한다.
2. R31AD와 현재 independent support를 가진 R31Z global의 frozen predictions를 midpoint 네 곳에서 계산한다.
3. primary separation

    S(z)=sqrt( DeltaK(z)^2 + DeltaDmax(z)^2 )

을 사용해 가장 큰 midpoint 하나를 선택한다.
4. tie이면 작은 z를 선택한다.
5. selected z와 model/source/rule hashes를 direct-output access 전에 lock한다.

이 `S`는 **validation-point selection criterion**일 뿐 최종 model decision score가 아니다. 최종 comparison은 다시 preregistered E_K/E_Dmax Pareto rule을 써야 한다.

## 5. 문헌 맥락

SciSpace current-loop 검색에서:

- Hunter & Reiner, Technometrics (1965), DOI 10.1080/00401706.1965.10490265: sequential model discrimination에서 다음 experiment를 rival-model prediction difference가 큰 곳에 배치하는 원리.
- Ucinski & Bogacka, JRSS B (2005), DOI 10.1111/J.1467-9868.2005.00485.X: multiresponse dynamic models의 T-optimal discrimination.
- Active Discrimination Learning for Gaussian Process Models, arXiv:2211.11624: successive design points를 model-discrimination criterion으로 선택하는 sequential framework.

이 문헌들은 R31AD의 physical accuracy를 증명하지 않고, **다음 validation point를 frozen-model separation으로 고르는 methodology**의 배경만 제공한다.

## 6. claim policy

R31AD가 현재 닫는 것:

- z=1의 relative verdict와 absolute adequacy를 명확히 분리
- z=0..4 integer mixed nodes를 새 training set으로 재분류
- five-node unit-cell structure-preserving candidate 정의
- midpoint-only future validation design rule 정의

닫지 않는 것:

- R31AD predictive accuracy
- interval-wide error
- physical transition amplitude/error
- full-cell neutral/H authority
- complete-HH fixed-Q physical invariance
- BR01/BR02
- independent decision review
- H-skip / production

새 half-integer science node는 이 research node에서 실행하지 않는다.
