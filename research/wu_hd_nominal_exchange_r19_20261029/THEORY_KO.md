# WU088_HH R19: GL2022 105 K 상태분해 단일 반응의 정확한 flow와 외부 부피 시계

**연구 범위**: R18 원본 보충표에서 인증한 `H⁺ + HD(v=0,j=2) → D⁺ + H₂(v'=0,j'=1)` SQM 반응의 **인쇄 명목 상태율**을 외부 고정 등온 bath `T=105 K`에 결속한다. 이는 상태선택 **한 방향** 4종 mass-action 모형이며, 완전한 primordial chemistry, 역반응, 실제 온도 이력, 물리 에너지 방출량, 불확실성 인증, REI/REC/CR owner의 소비자 승인을 뜻하지 않는다.

## 1. 원본과 가정

González-Lezana, Hily-Blant, Faure, *J. Chem. Phys.* **157**, 214302 (2022), DOI 10.1063/5.0128598, DIGITAL.CSIC 원본 보충자료 PDF Table 2, page 6, row `(0,2)` and product `(v'=0,j'=1)`. 원본 PDF 273554 bytes, SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. R18 검증된 모듈 `src/native_rates.py` Git blob `be2a845263b215b604f255ffe5deabe55be9dd7b`에서 `load_native_grid`를 호출해 실제 PDF를 읽고 `lookup(105, initial_j=2, product_j=1, method='SQM')`로 가져온다.

원문 `1.15(10)`의 뜻은 `1.15 × 10⁻¹⁰ cm³/s`이므로 정확한 **인쇄 소수 해독값**

\[
k_{105}^{\mathrm{print}}=\frac{23}{200000000000000000}\,\mathrm{m^3\,s^{-1}}=1.15\times10^{-16}\,\mathrm{m^3\,s^{-1}}.
\]

인쇄값의 마지막 자리 반올림 규칙, SQM 이론 불확실성, true-rate enclosure는 **미제공**이다. 이 source row는 열평균 total이 아니므로 외부 Boltzmann population이나 홀수 최종준위의 `3/4` 가중치를 **재적용하지 않는다**. 원문 보충표 initial `j=0..6`과 본문 Eq.(5)의 `j=0..8` 차이는 그대로 보존한다.

이하 `n=(n_H+,n_HD02,n_D+,n_H201)^T`는 SI 물리 **수밀도** `m⁻³`, `t`는 유체 공이동 관측자의 **proper time** `s`, `\nu=(-1,-1,1,1)^T`. 상태별 density `n_HD02`, `n_H201`는 전체 HD/H₂ abundance와 동일하지 않다. 외부 bath는 정확히 105 K로 **가정**하며 해당 bath의 실제 열역학적 구현은 수행하지 않는다.

## 2. 정의: mass-action 및 보존법칙

\[
J(t)=k_{105}^{\mathrm{print}}\,n_{H^+}(t)n_{HD02}(t),\qquad
\dot{\boldsymbol n}=\boldsymbol\nu J \quad(\Theta=0).
\]

`[J]=m⁻³ s⁻¹`, `[k]=m³ s⁻¹`. 화학적 사건은 `H⁺`와 `HD02`를 하나씩 소모하고 `D⁺`와 `H201`을 하나씩 생성한다. 아래 세 보존 공변벡터가 \(w^T\nu=0\)을 만족한다.

\[
w_H=(1,1,0,2),\quad w_D=(0,1,1,0),\quad w_q=(1,0,1,0).
\]

각각 수소 핵수, 중수소 핵수, 양전하 수의 보존이다. 세 벡터는 선형독립이고 \(\ker(\nu^T)\)를 생성한다. `w_N=(1,1,1,1)=(w_H+w_D+w_q)/2`는 추가로 독립인 불변량이 아니다. 전자/중성 수소/기타 상태가 없으므로 전체 화학계의 전하중성, detailed balance 또는 전체 baryon density의 검증으로 확대하지 않는다.

## 3. 구성적 정확 해 (고정 부피)

초기 \(a=n_{H^+}(0)\ge0,\ b=n_{HD02}(0)\ge0,\ c=n_{D^+}(0),\ d=n_{H201}(0)\)라 두고 반응 extent \(\xi\)를 도입하면

\[
\boldsymbol n(t)=(a-\xi,b-\xi,c+\xi,d+\xi),\quad
\dot\xi=k(a-\xi)(b-\xi),\quad\xi(0)=0.
\]

- `a=b=m>0`: \(\xi=m^2 kt/(1+mkt)\), 두 reactant survivor \(m/(1+mkt)\).
- `a≠b`: \(m=\min(a,b),\ M=\max(a,b),\Delta=M-m>0\), \(z=1-e^{-k\Delta t}\)이면

\[
\boxed{\xi(t)=\frac{m M z}{\Delta+m z}},\qquad
m-\xi=\frac{m\Delta e^{-k\Delta t}}{\Delta+m z},\qquad
M-\xi=\frac{M\Delta}{\Delta+m z}.
\]

- `ab=0`: \(\xi=0\).

**증명**: 두 reactant의 차는 상수 \(a-b\). \(\dot{\log}[(m-\xi)/(M-\xi)]=-k(M-m)\)를 적분하면 \((m-\xi)/(M-\xi)=(m/M)e^{-k\Delta t}\). 정리하면 위 식. 동일 초기값 극한 \(\Delta\to0\)에서 \(z\sim k\Delta t\)이므로 `a=b` 해로 수렴한다. \(0\le\xi(t)\le m\), 모든 survivor와 product는 비음수, \(\dot\xi\ge0\)이다. 비가역 forward-only 모형의 결과이지 원 반응계의 열역학적 평형 정리가 아니다.

**수치식**: `z=-expm1(-k*Δ*t)`를 사용하고 `m*M`를 직접 계산하지 않아 중간 overflow 위험을 줄인다. reactant survivor를 `m−xi` 뺄셈이 아닌 위 분수로 계산한다. `a=b` 분기는 명시적으로 처리한다. 부동소수점 유한범위 밖의 입력은 오류로 보존한다.

## 4. prescribed homogeneous volume expansion과 정확한 clock

일반상대론적 공이동 유체의 \(\Theta=\nabla_\mu u^\mu\)를 외부 지정 함수로 **가정**하고, 국소 수밀도는

\[
\dot{\boldsymbol n}+\Theta(t)\boldsymbol n=\boldsymbol\nu k n_{H^+}n_{HD02}.
\]

\(v(t)=\exp\int_0^t\Theta(s)ds=V(t)/V(0)>0\) (무차원), \(\boldsymbol N=v\boldsymbol n\) (`m⁻³` per reference volume), \(\tau(t)=\int_0^t v(s)^{-1}ds\) (`s`)로 두면

\[
\frac{d\boldsymbol N}{dt}=\boldsymbol\nu\frac{k}{v(t)}N_{H^+}N_{HD02},\qquad
\frac{d\boldsymbol N}{d\tau}=\boldsymbol\nu k N_{H^+}N_{HD02}.
\]

따라서 §3의 정확한 \(\xi(\tau)\)를 \(\boldsymbol N\)에 적용하고 최종 \(\boldsymbol n=\boldsymbol N/v\)로 돌리면 **prescribed \(\Theta(t)\)**에 대한 정확한 solution map이 된다. \(\Theta\)가 상수이면

\[
v(t)=e^{\Theta t},\qquad
\tau(t)=\begin{cases}(1-e^{-\Theta t})/\Theta,&\Theta\ne0,\\ t,&\Theta=0.\end{cases}
\]

`-expm1(-Θ*t)/Θ`로 작은 `Θt`를 안정적으로 계산한다. \(w_H^T\boldsymbol N,w_D^T\boldsymbol N,w_q^T\boldsymbol N\)은 상수지만 **물리 수밀도** \(w^T\boldsymbol n\) 자체는 `1/v`로 희석된다. 이는 동역학적으로 \(\Theta\)를 푼 것이 아니며 Bianchi shear, tilt, perturbations, full Einstein-Boltzmann source를 승인하지 않는다.

## 5. RHS Jacobian, 안정성 및 rate 민감도

임의의 증가 좌표 `s`에 대해 \(g(s)=dt/ds>0\)를 외부에서 지정하면

\[
\frac{d\boldsymbol n}{ds}=g\big[\boldsymbol\nu k n_1n_2-\Theta\boldsymbol n\big],\quad
A_{ij}=g\big[\nu_i k(n_2,n_1,0,0)_j-\Theta\delta_{ij}\big].
\]

화학 부분은 rank ≤1이며 비영 고유값 \(-gk(n_1+n_2)\le0\), 나머지 세 고유값 0이다. 희석을 포함한 전체 고유값은 \(-g\Theta\) (3중)과 \(-g[\Theta+k(n_1+n_2)]\). 이는 **4×4 isolated operator**의 국소 Jacobian이지 full chemical network/full-A의 spectrum이 아니다.

해는 `k τ`의 함수이므로 고정 초기밀도와 clock에서

\[
\boxed{\frac{\partial\xi}{\partial k}=\tau(a-\xi)(b-\xi)\ge0},\quad
\frac{\partial\xi}{\partial\tau}=k(a-\xi)(b-\xi).
\]

외부에서 독립적으로 `k_lo≤k≤k_hi`가 인증되면 \(\xi(k_{lo})\le\xi(k)\le\xi(k_{hi})\)는 sharp한 **조건부** 구간이 된다. R18 원문은 `k_lo/k_hi`를 제공하지 않으므로 이 정리에서 실제 물리 rate 불확실성을 역산하지 않는다.

## 6. 에너지 ledger의 소유권

실제 state-dependent energy defect `Q_event=E_reactants−E_products` (`J/event`)는 별도 원전·상태 에너지 및 convention이 있어야 결정된다. **오직 형식적으로** `ΔE_chem=−Q_event ξ`, `ΔE_bath=+Q_event ξ` (`J per reference m³`)를 정의하면 합은 0이다. 고정 등온 bath는 이 에너지를 외부에 전달하거나 공급한다고 **가정**할 뿐, photon/thermal-electron/gas pressure/expansion work/비평형 열역학을 계산하지 않는다. 실제 `Q_event`가 없으므로 기본 결과에는 energy number를 포함하지 않는다.

## 7. 검증, 수용 및 비수용

- 정의·부호·단위·세 핵수/전하 보존, `a=b`, `a≠b`, `ab=0`, `t=0`, `t→∞`, `Θ→0`, `Θ<0`, `Θ>0`를 검산한다.
- `Fraction`으로 **인쇄 명목** rate의 SI 값만 정확히 보존한다. 정확 해를 IEEE float64로 계산하므로 물리/수치 전체 interval certificate는 아니다.
- 독립 알고리즘 `mpmath(80 dps)` 및 SciPy `solve_ivp`와 비교하고 실제 테스트와 그림을 저장한다.
- 소스 PDF는 R18 검증 모듈에서 실제 byte SHA를 검사한다. source PDF/코드 identity가 바뀌면 재검증한다.
- R19의 scoped nominal four-state **model/solver**와 REC/CR/REI 실제 owner-consumer, source uncertainty, complete network, production readiness는 서로 다른 claim gate다.
