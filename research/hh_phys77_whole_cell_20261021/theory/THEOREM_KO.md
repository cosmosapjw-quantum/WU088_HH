# PHYS77: finite-owner whole-cell source enclosure의 구성적 정리

2026-10-21. 대상 DAG 의무: `FINITE_OWNER_WHOLE_CELL_SOURCE_OR_RESIDUAL_ENCLOSURE`.

이 문서는 PHYS76의 조건부 Green/response 정리에 필요한 cell 전체의 `A, P_m, P_r`를 만드는 최소 구성이다. 원본 `ComponentReduced`의 finite L8, collisionless 모델과 저장된 시작 상태를 고정한다. 새 ODE 적분, benchmark, NCP 실행은 이 유도에 없다. 실제 interval 검사와 게시·백업 결과는 별도 receipt가 담당한다.

## 1. 인증할 수학적 대상과 원본 대응

원본은 REI198 verified payload의 `pilot.py`, `matter_radiation_20261021/component_pilot.py`, `vendor/canonical_fv.py`, `vendor/lrs_boltzmann.py`다. 모든 source SHA와 초기 raw NPZ SHA, case amplitude 및 아래 배열의 실제 bytes를 함께 묶는다.

원본 Python/NumPy 프로그램의 binary64 계산은 그 자체로 매끄러운 ODE가 아니다. 인증 대상은 **captured finite owner의 실수화(real lift)** `y'=F#(x,y)`다. 입력·이미 계산된 model coefficient와 배열의 binary64 값을 정확한 유리수로 읽고, 아래 함수식의 산술·exp·sqrt를 실수 연산으로 해석한다. 이 실수화와 원래 solver 실행의 관계는 source/formula mapping 및 저장값 대비 검산으로 별도 기록한다. literal floating-point 실행의 모든 중간 반올림을 원래 continuum 방정식으로 동일시하지 않는다.

최소 capture 항목은 `h0, href, aref, omega_m, omega_r, omega_lambda, FM, mpref, mass, reference_energy_norm, q_nodes, mu2, packet_numbers, M`와 case의 `A_m`, 초기 `x,y`다. 원본 생성 후 저장된 `mpref`, `href`, normalization, Gauss nodes·weights와 `M`은 다시 이상적인 값으로 계산하지 않는다. 검증용 capture schema는 실수화에서 고정되는 상수와 실수 연산으로 남는 식을 명시해야 한다. 예를 들어 이미 계산해 capture한 `h0_sq`를 쓰려면 RHS와 source 식 모두에 그 같은 상수를 써야 한다.

`M = legendre_matrix(8, power=4)[::2,::2]`는 Gauss64와 binary64 연산으로 생성된 실제 5×5 배열이다. 분석적 monopole row `(0,-2,0,0,0)`로 치환하면 다른 owner가 된다. 모든 25개 captured entry를 보존한다. 쓸모없는 듯한 작은 nonzero entry도 제거하지 않는다.

상태와 독립 변수는

\[
y=(\tau,b,q,E_0,E_2,E_4,E_6,E_8),\qquad
x=\log(a/a_{\rm ref}),\qquad q=s/h_{\rm ref}.
\]

여기서 state `q`는 deceleration parameter가 아니다. `tau=href × elapsed proper seconds`이며 feedback에는 나타나지 않는다. 전체 8-state tube를 검증해도 되고, 먼저 7-state feedback block을 검증한 뒤 양의 `tau'=href/H`를 적분하여 passive clock을 포함해도 된다. 후자는 원본 RHS의 변경이 아니라 삼각 구조를 사용한 증명 분해다.

## 2. 양의 canonical packet에서의 정확한 moment 식

packet index를 k라 하고, capture한 `n_k>=0`, `Q_k>=0`, `0<=muk2<=1`, `m>0`, `N>0`를 사용한다. `N`은 원본 `reference_energy_norm`이다.

\[
u_k=Q_k^2e^{-2x+2b}(1-\mu_k^2),\quad
v_k=Q_k^2e^{-2x-4b}\mu_k^2,\quad
\epsilon_k=\sqrt{m^2+u_k+v_k},\quad
c_k={e^{-3x}n_k\over N}.
\]

\[
\rho=\sum_k c_k\epsilon_k,\quad
p_\perp=\sum_k c_k{u_k\over2\epsilon_k},\quad
p_\parallel=\sum_k c_k{v_k\over\epsilon_k},\quad
\bar p={2p_\perp+p_\parallel\over3},\quad
\pi={p_\parallel-p_\perp\over3}.
\]

이 값은 원본 finite momentum rule의 dimensionless normalized moments다. momentum quadrature 오차를 감싸거나 무한 momentum continuum을 인증한 것은 아니다. 정확한 고정 packet들의 유한합이므로 각 term의 interval 포함성과 outward sum만으로 전체 moment 포함성이 따른다.

signed stress는 동치인 다음 유한합으로 계산할 수 있다.

\[
\pi=\sum_k {c_k\over3\epsilon_k}(v_k-u_k/2).
\]

이는 real lift 안에서의 대수적 동치이며, binary64 reduction의 bitwise 재현을 주장하지 않는다. 큰 두 양의 pressure 합을 마지막에 빼는 것보다 interval 폭을 줄이는 선택이 될 수 있지만, 실제 폭·속도 개선은 별도 결과가 있어야 주장한다.

양의 형태

\[
\rho-\bar p
=\sum_k c_k{3m^2+2(u_k+v_k)\over3\epsilon_k}>0
\]

도 직접 사용할 수 있다. 적어도 한 `n_k>0`이면 strict positivity가 성립한다.

미분하면 `partial_x u=-2u`, `partial_x v=-2v`, `partial_b u=2u`, `partial_b v=-4v`이므로

\[
\partial_x\rho=-3\rho-(2p_\perp+p_\parallel)
=-3(\rho+\bar p),\qquad
\partial_b\rho=2p_\perp-2p_\parallel=-6\pi.
\]

따라서 임의의 실제 `b'=w`를 따라

\[
\rho'=-3(\rho+\bar p)-6w\pi.
\]

이 항등식은 captured nonnegative packet과 고정 normalization에 대해 정확하다. Gauss rule이 연속 Vlasov 적분을 정확히 근사한다는 추가 가정을 사용하지 않는다. Wolfram의 packet 단위 symbolic 결과 `{0,0}`는 별도 evidence에 보존하며 증명은 위 미분이다.

## 3. 고정 finite-owner RHS와 signed source

표기를

\[
a=a_{\rm ref}e^x,\quad d={(1-f_m)\Omega_m\over a^3},\quad
r={\Omega_r\over a^4},\quad \mu=\texttt{mpref},\quad s=h_{\rm ref}q,
\]

\[
T=H^2=h_0^2(d+\mu\rho+rE_0+\Omega_\Lambda)+s^2,\qquad
w=s/H,\quad Q=\mu\pi+rE_2/3
\]

로 둔다. 모든 표현은 capture contract가 정한 동일한 상수를 사용한다. `T>0`인 domain에서 원본 RHS의 실수화는

\[
\tau'=h_{\rm ref}/H,\quad b'=w,\quad
q'=-3q+{3h_0^2Q\over h_{\rm ref}H},\qquad
\mathbf E'=wM\mathbf E.
\]

공통 정규직교 normal frame에서 `sigma=diag(-s,-s,2s)`, `pi_A=diag(-p_A,-p_A,2p_A)`다. `kappa=8 pi G/c^2`와 원본 `kappa rho_crit,0=3h0^2`를 같은 convention으로 사용하면 signed half-contraction 좌표는

\[
S={\sqrt3s\over H},\quad
P_m={\sqrt3\,3h_0^2\mu\pi\over T},\quad
P_r={\sqrt3\,h_0^2rE_2\over T}.
\]

두 sector를 별도로 감싼다. total stress는 `Pm+Pr`를 먼저 만든다. Frobenius 양은 `Sigma_F=sqrt(2)|S|`, `Pi_A,F=sqrt(2)|P_A|`, `Pi_total,F=sqrt(2)|Pm+Pr|`다. `|Pm|+|Pr|`는 total norm이 아니다.

## 4. 전체 captured monopole row를 보존한 A

`g0=(M E)_0`, `delta0=g0+2E2`라 하자. `delta0`는 행렬의 분석적 monopole identity와 captured row 사이의 실제 차이를 포함한다. `delta0=0`을 가정하지 않는다.

`d'=-3d`, `r'=-4r`, `E0'=w g0` 및 위 moment 항등식과 q 방정식을 대입하면

\[
T'=h_0^2\left[-3d-3\mu(\rho+\bar p)-4rE_0
+rw\delta_0\right]-6s^2.
\]

검산용으로는 이 식을 원래 chain rule

\[
T'=\partial_xT+\nabla_yT\cdot F^\#
\]

와 비교할 수 있다. matter work의 `-6mu w pi`와 shear-energy source의 `+6mu w pi`는 정확히 상쇄된다. radiation work에는 captured row에서 온 `r w delta0`가 남는다.

따라서 필요한 coefficient는

\[
\boxed{A=3+{T'\over2T}
={h_0^2\over T}
\left[{3\over2}d+{3\over2}\mu(\rho-\bar p)
+rE_0+3\Omega_\Lambda+{rw\over2}\delta_0\right].}
\]

대괄호에서 양의 kinetic 표현을 사용하면 `3+T'/(2T)`의 큰 항 사이 상쇄를 피할 수 있다. 마지막 row-defect term의 부호와 interval은 유지한다. 이 식으로 얻은 `A`는 해당 실수화의 실제 `3+H'/H`이며, deceleration convention `A=2-q_dec`와 일치한다.

원본 shear 방정식을 직접 미분하면

\[
S'=-A S+P_m+P_r.
\]

이 항등식에는 ideal monopole row를 대입할 필요가 없다. 그러므로 아래 tube가 확보되면 PHYS76 interval transport에 필요한 세 coefficient를 동일한 실제 trajectory에서 얻을 수 있다.

## 5. Jacobian 없는 whole-cell defect tube 정리

`X=[x0,x1]`, `h=x1-x0>0`이고 `p:X→R^n`은 명시적인 C1 predictor라 하자. 실제 구현에서는 저장된 두 node로부터 nearest Decimal slope를 계산한 뒤, 그 유한 Decimal 값 자체를 정확한 affine 계수로 고정한다. 따라서 실제 `p(x1)`는 저장 endpoint와 약간 다를 수 있으며, `p0+h*slope`를 outward 평가한다. `p0+[0,h]*slope`는 **이 명시적 polynomial의 range**를 감싼다. 미지의 실제 solution의 range로 가정하지 않는다.

`R=product_i [r_i^-,r_i^+]`는 후보 error box, `E_init`은 실제 `y(x0)-p(x0)`를 포함하는 초기 error box다. `P(X)`가 모든 `p(x)`를, `Pprime(X)`가 모든 `p'(x)`를 포함한다고 하자. 후보 state box `Y=P(X)+R`에서 다음을 확인한다.

1. 원본 capture 및 case identity가 맞고 모든 입력이 유한하다.
2. `Y`에서 source domain이 성립한다. 특히 `H²` interval의 하한이 양수이고, chart와 positive packet 가정이 유지된다.
3. `F#`가 닫힌 시간 구간 X에서 연속이고, 이 compact tube를 포함하는 state의 열린 근방에서 locally Lipschitz이다. 위 finite sums·exp·positive sqrt·나눗셈으로 이 조건이 성립한다. 초기 x=0에서는 시간 방향의 one-sided IVP를 사용하며 음의 x에서 원본을 실행할 필요가 없다.
4. outward interval 평가로 전체 box에 대해

\[
D\supseteq\{F^\#(x,p(x)+e)-p'(x):x\in X,e\in R\}
\]

를 얻는다. 자연 interval extension `D=F#(X,P(X)+R)-Pprime(X)`면 충분하다.
5. 다음 strict inclusion을 각 성분에서 exact endpoint 비교로 확인한다.

\[
\boxed{B=E_{\rm init}+[0,h]D\ \subset\ \operatorname{int}(R).}
\]

그러면 초기 조건 `y(x0) in p(x0)+E_init`를 갖는 각 IVP의 유일한 solution이 X 전체에 존재하고, 모든 x에서

\[
y(x)\in p(x)+R,
\qquad
y(x_1)\in p(x_1)+E_{\rm init}+hD.
\]

마지막 endpoint 식의 계수는 `[0,h]`가 아니라 정확한 `h`다. 전체 cell의 시간 변수를 제거한 bound와 endpoint bound를 구분해야 한다.

### 증명

가정 3으로 초기 주변의 유일한 local solution이 존재한다. `e=y-p`라 두면

\[
e(x)=e(x_0)+\int_{x_0}^x
[F^\#(t,p(t)+e(t))-p'(t)]\,dt.
\]

실제 해가 아직 R 안에 있는 시간까지 integrand는 D에 들어간다. 각 성분의 integral은 `[0,h]D`에 들어가므로 `e(x)`는 B에 들어간다. B는 R의 내부에 놓이며 두 집합 사이의 각 성분 거리에는 양의 여유가 있다.

처음으로 R의 경계에 도달하는 시간이 존재한다고 가정하면, 그 시간까지의 integral 식과 연속성으로 그 시점의 e도 B에 들어가야 한다. 이는 경계에 있다는 가정과 모순이다. 또한 compact tube가 smooth domain 안에 있어 유한 시각에 solution이 그 내부에서 연장 불가능해질 수 없다. 그러므로 solution은 x1까지 존재하고 tube를 벗어나지 않는다. x=x1에서 integral 길이는 h이므로 endpoint bound가 따른다. 유일성은 원래 locally Lipschitz IVP의 유일성이다. QED.

이 증명은 전체 cell에서 Picard operator가 contraction임을 별도로 요구하지 않는다. Strict inclusion이 실패해도 해의 부재·불안정성·물리 부적합을 뜻하지 않는다. 해당 predictor, box와 interval extension으로 증명이 아직 닫히지 않았다는 뜻이다.

## 6. 검사 결과를 PHYS76 source enclosure로 연결

정리의 성공 receipt가 있으면 실제 solution을 포함하는 `X,Y`에 위 finite formulas를 outward 평가한다.

\[
[A]\supseteq A(x,y(x)),\qquad
[P_m]\supseteq P_m(x,y(x)),\qquad
[P_r]\supseteq P_r(x,y(x))\quad(x\in X).
\]

이제 `source/method/locator`가 확인되는 whole-cell witness를 PHYS76 `interval_transport.py`에 제공할 수 있다. 그 Green factor와 response bounds는 이 cell에서 연속 시간에 유효한 finite-owner statement가 된다. Initial S 역시 `p(x0)+E_init`에서 outward 계산한다.

동일 trajectory에서 `S=D+Jm+Jr`를 감싸는 결과다. species-off 인과 실험은 아니다. Coupling이 Pm, Pr, H 모두에 들어간다. 별개 moment continuum이나 angular L→∞의 해를 포함한다고 주장하지 않는다.

초기 상태가 저장된 **전체 구간 시작점**이며 그 binary64 vector를 정확한 IVP 초기 조건으로 정의한 경우 `E_init={0}`를 사용할 수 있다. 이는 nominal target parameter가 정확히 구현됐다는 주장이 아니라 원래 실행이 실제로 시작한 float vector를 고정하는 것이다.

중간 saved endpoint에서 시작할 때는 이전 cell의 인증된 endpoint box를 운반해야 한다. 그것이 없으면 `E_init=0`은 다른 restart IVP의 조건부 statement이며 원래 prefix trajectory의 인증이 아니다. 이후 각 cell에서 새 saved node를 중심으로 재중심화할 수 있지만, `E_next=Y_end-p_next(x_start)`를 유지해야 한다. 그 폭을 0으로 리셋하지 않는다.

## 7. 최소 kernel과 실제적인 범위

필요한 kernel은 다음과 같다.

- finite Decimal interval의 `+,-,*,/,square,exp,sqrt,sum,hull`와 strict-inclusion 비교;
- exact binary64 capture를 읽는 함수와 source/array/state hash 검사;
- 양의 packet moments, captured M의 5×5 곱, 위 RHS·A·Pm·Pr 평가;
- affine predictor의 exact 정의, 후보 R, `D,B,Y_end` 및 inclusion margin receipt;
- 성공한 cell에서 PHYS76 witness를 내보내는 adapter.

`Decimal.from_float` 또는 `as_integer_ratio`로 captured binary64를 정확히 변환한다. `Decimal(str(float))`는 bit identity를 보존하지 않는다. Exact interpolation을 원하면 slope를 outward enclosure 또는 exact rational coefficient로 처리한다. 현재 구현은 앞 절처럼 반올림된 point slope 자체를 predictor 정의로 선택한다. `p(x0)=y0,p(x1)=y1`를 동시에 정의하면서 반올림한 slope를 exact interpolation slope처럼 쓰면 안 된다.

Exp/sqrt는 correctly-rounded candidate를 outward 이웃으로 감싸거나 독립 endpoint inequality로 검증한다. sqrt의 경우 하한 L에 `round_up(L²)<=input_lower`, 상한 U에 `round_down(U²)>=input_upper`를 확인하는 방식도 가능하다. 모든 division denominator의 interval이 0을 피해야 한다. Nearest 함수나 이웃 연산이 만드는 overflow/subnormal은 PHYS76의 엄격한 representability 정책에 맞춰 거부한다. 전체 Decimal context를 바꾸지 않는다.

Affine predictor는 원래 saved data를 재사용하므로 새 ODE는 필요 없다. 처음에는 1개 또는 소수의 case에서 전체 구간 첫 cell만 검증하는 것이 수학·source mapping 의무를 작게 닫는 방법이다. 이 유도만으로 실제 inclusion 성공이나 1231개 전체 history 인증을 선언하지 않는다.

자연 interval extension은 x와 state의 상관관계를 버리므로 box가 넓어질 수 있다. 구체적인 실패가 나면 그 cell을 같은 predictor의 정확한 subinterval로 나누거나, 검증 가능한 Hermite/Taylor polynomial을 사용하거나, Jacobian-centered defect bound를 추가할 수 있다. Subdivision은 node extrema를 증명으로 바꾸지 않는다. 각 subcell을 다시 엄격히 검사하고 초기 endpoint enclosure를 순서대로 운반해야 한다.

## 8. 이 kernel에 직접 필요한 표적 검산

1. 정확한 해가 알려진 scalar linear IVP에서 tube·endpoint 포함성과 충분히 작은/큰 candidate의 pass/fail 분리.
2. interior에 peak가 있으나 양 끝에서 작거나 0인 nonautonomous forcing으로 endpoint extrema만 사용하는 잘못된 구현 검출.
3. 부호가 섞인 D에서 `[0,h]D`와 endpoint `hD`가 다름을 확인.
4. captured M의 작은 첫-row 성분을 의도적으로 남겨 `delta0`가 A에 나타나는지 확인.
5. 단일 양의 kinetic packet의 두 derivative identity 및 `rho-pbar`의 동치식 검산.
6. `H²` lower<=0, negative packet, 0 denominator, capture/hash mismatch 및 chart 위반 거부.
7. endpoint enclosure를 다음 cell로 운반하고 stored node 중심으로 재중심화할 때 error 폭이 사라지지 않는지 확인.
8. Matter/radiation signed sum, half/Frobenius sqrt2 및 cancellation case의 tensor mapping 확인.

이는 최적화 benchmark가 아니라 선택된 finite-cell certificate의 논리와 구현을 검증하는 최소 표적군이다. 테스트 수나 actual PASS 상태는 실제 실행 receipt에서만 기록한다.

## 9. 문헌·코드에서 재사용한 것

기존 validated ODE 문헌은 존재·유일성과 whole-step enclosure를 먼저 확인한 뒤 endpoint를 정밀하게 감싸는 구조를 사용한다. 이번 first-exit proof와 finite-owner source 연결은 그 구조에 맞춘 작은 self-contained specialization이다. 새로운 no-go 정리나 범용 solver의 novelty 주장은 없다.

- Nedialkov, Jackson, Pryce, *An Effective High-Order Interval Method for Validating Existence and Uniqueness of the Solution of an IVP for an ODE* (2001), [DOI](https://doi.org/10.1023/A:1014798618404). Primary publisher abstract와 bibliography를 읽었다. 유료 본문의 세부 정리를 읽었다고 주장하지 않는다.
- Bréhard, *A Symbolic-Numeric Validation Algorithm for Linear ODEs with Newton-Picard Method*, [author-deposited HAL manuscript](https://hal.science/hal-03161118). Approximation 생성과 rigorous a posteriori validation을 분리하는 근거다. 이 논문의 linear resolvent machinery를 nonlinear owner에 그대로 적용하지 않는다.
- [TaylorModels.jl 공식 문서](https://juliaintervals.github.io/TaylorModels.jl/dev/api/)의 polynomial+remainder Picard pass가 가까운 구현 참고다. 실제 repository LICENSE는 MIT Expat이며, search metadata의 `NOASSERTION` 대신 실제 license blob을 확인했다. Julia 코드를 현재 Python kernel에 그대로 복사하지 않는다. 향후 번역·코드 재사용 시 해당 copyright/permission notice를 함께 보존한다.
- [CAPD 공식 validated ODE 문서](http://capd.ii.uj.edu.pl/html/odes_rigorous.html)는 interval initial set, Taylor/Hermite–Obreshkov, doubleton/tripleton 및 solution-curve 전략을 제공한다. 공식 repository `COPYING`은 GPLv3다. 현재 최소 Python kernel의 의존성이나 vendored code로 도입하지 않았다.
- [Python Decimal 공식 문서](https://docs.python.org/3/library/decimal.html)는 기본 arithmetic·context·rounding semantics의 근거다. 기존 PHYS76 outward engine의 구체적인 경계 수정과 receipt를 재사용할 수 있다.

SciSpace는 위 관련 연구를 찾는 데 사용했다. Neumaier의 dissipative enclosure 논문과 Ernsthausen의 rigorous defect-control thesis도 후보로 찾았으나 이번 fetch에서 원문이 열리지 않아 세부 정리를 근거로 채택하지 않았다. Tool warning·fetch 실패와 source pins는 별도 `evidence/RESEARCH_EVIDENCE.json`에 남긴다.

## 10. 종료 판정

이 유도는 조건부 transport 앞단의 **유한 owner cell 한 개를 실제로 인증할 수 있는 구성**을 제공한다. 실제 cell inclusion을 수행하면 그 범위만 새 근거로 추가한다. 전체 z20→2 history, finite-momentum discretization 오차, angular continuum positivity, L→∞, full cold EoR, non-LRS 및 production admission은 자동으로 따라오지 않는다.

`HH_R10=OFF`. 새 ODE 0, benchmark 0, NCP 0. 실제 실행·게시·백업·DAG 갱신은 각각 별도 receipt로 기록한다.
