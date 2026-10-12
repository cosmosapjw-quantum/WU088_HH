# PHYS11 — 같은 소스 계열의 기체·광자·반응 ledger 전달

2026-10-11. 이 문서는 PHYS10의 첫 단계 기체·잔존 광자 결과를 **값, 두 일차 미분, 한 혼합 미분을 갖는 다음 단계 입력**으로 만드는 수학적 구성이다. 현재 확보한 33개 group의 전부를 계산 가능한 형태로 정식화하고, 실제 다음 단계에서 사라지면 안 되는 교차항을 유도한다. 실제 carried second_half, native root, 전구간 history를 실행하거나 증명한 문서가 아니다.

이 문서의 새 정리와 계산식의 근거 상태는 **derived**다. 실제 프로그램의 포함 계산과 실행 상태는 별도의 결과·실행 증거를 따른다. 정리의 전제는 PHYS09–10에서 채택한 같은 고정 계수의 실수 소스와 조건부 C² root family이며, native authority는 계속 false다.

## 1. 소스, 좌표, 보존해야 하는 구분

원 소스 기준은 PHYS10에 보존된 NCP07 source delivery `4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b`다. 아래 경로는 현재 PHYS11 core `HH_PHYS11_20261011_v1`를 기준으로 한다.

| 기호 | 실제 근거 |
|---|---|
| S1 | `inputs/ncp07/raw/candidate/src/phys04_mixed.rs::{phys04_reduced_residual,phys04_carry,phys04_mixed_at_box}` |
| S2 | `inputs/ncp07/raw/candidate/src/phys04_transport.rs::{phys04_prepare_family,phys04_distribute_after_be}` |
| S3 | `inputs/ncp07/raw/candidate/src/paired_runtime.rs::{PairedState,endpoint,accumulate}` |
| S4 | `inputs/ncp07/raw/candidate/src/coupled_primary.rs::{PrimaryState,photons,endpoint,primary_stage_step_conservative}` |
| S5 | `inputs/ncp07/raw/src/family.rs::CommonFamily` |
| S6 | `inputs/ncp07/raw/candidate/src/ft03_interval.rs::ft03_interval_rhs` |
| S7 | 각 단계의 `inputs/ncp07/raw/results/{full,first_half}/{PREBE,SOURCE_BOX,SOURCE_BOX_COMPONENTS,COMMON_INPUT_SCOPE}.json` |
| S8 | `inputs/phys09/PROJECTED_RESULTS.json` 및 `inputs/phys10/GAS_PHOTON_LEDGER_THEOREM_KO.md` |

PHYS11에서는 추가로 기존 NCP07 manifest와 byte identity가 맞는 `ft03_controlled.rs`(14,726 bytes, SHA256 `61e11471482bb49d99e5d0eb79504d3f67538fbe6361653a0462d1abb0b672db`)와 `hhe_events.rs`(9,447 bytes, SHA256 `c100b08e034089c2d67b2102769ccdd51f1d29a2f388d6bb2dfe7984af93b290`)를 읽었다. 이 두 파일의 `Ft03Model::controlled()` → `HHeModel::controlled_fixture()` 연결을 S9라고 부른다. 이는 원 source의 threshold leaf identity를 해소하는 기존 자료의 재사용이며 새 native 실행이 아니다.

상태 좌표는

\[
g=(x_{\rm HII},y_{\rm HeII},y_{\rm HeIII},w),\qquad
w\ [\mathrm{eV/H}],\qquad \theta=(\lambda,b)\in[0,1]^2.
\tag{1}
\]

λ는 미래 HH 강도, b는 미래 photon birth 강도다. COMMON에 저장된 과거 HH ON 이력과 그 compensation은 미래 λ=0에서도 유지한다. 모든 저장 구간에 허용되는 같은 고정 계수 tuple α를 한 번 선택한 뒤, parameter rectangle의 모든 점에서 그 α를 사용한다. α에는 초기조건, 배경과 시각, 단계 길이, 원자 계수, density leaves 및 실제 geometry로부터 얻은 계수 사이의 관계가 포함된다.

Full의 d=1.25×10⁹ s와 first_half의 d=6.25×10⁸ s는 모두 같은 COMMON에서 출발하는 첫 단계다. 첫 half의 결과를 두 번째 half에 전달한 실행은 아직 없다. 원자 소스의 stage helium factor f와 stored-density ratio

\[
\widehat f=\frac{\operatorname{exact}(n_{\rm He,stored})}
{\operatorname{exact}(n_H)}
\tag{2}
\]

를 구별한다. λ,b에 대해 nH와 f, fhat는 각 고정 단계에서 상수다. 단위는 원 소스대로 c [cm/s], nH [cm⁻³], σ [cm²], E [eV]를 유지한다. 광자 개수는 이미 photons/H다. 여기에 nH를 다시 나누거나 곱하지 않는다.

현재 실제 자료는 다음과 같이 나뉜다.

| 대상 | 현재 근거와 상태 |
|---|---|
| 4개 gas 값과 U,V,W | PHYS09의 같은 source-family uniform 포함을 재사용 |
| 33개 incoming group의 full Jet | PREBE.json에 실제 저장됨 |
| 99개 흡수율의 full Jet | SOURCE_BOX_COMPONENTS.json에 실제 저장됨 |
| 33개 outgoing photon의 값 구간 | SOURCE_BOX.json에 실제 저장됨 |
| q의 full Jet | SOURCE_BOX.json에 실제 저장됨 |
| source_n, source_u의 full Jet, 128개 angular source weights | PREBE.json에 실제 저장됨 |
| 4224개 ray/node와 128개 guard N/U의 실제 PreBE 배열 | 현 보존 JSON에 없음; 원 binary identity는 존재하나 별도 확보가 필요 |
| primary escape의 native derivative Jet | 현재 export에 없음 |
| primal ledger_comp[5], energy_comp, historical HH compensation | 값이 기록돼 있음. 미래 실수 미분 ledger와 별도로 보존 |

PREBE의 group b-gradient는 source affine 기울기의 **포함 구간**이다. 그것을 임의의 단일 실수 M으로 바꾸지 않는다. Born source가 들어가는 group은 24이고, 그 원 amount는 `fl_dt_SOURCE_bits`의 정확한 실수 값이다. Full의 bits는 `3eda36e2eb1c432d`, first_half는 `3eca36e2eb1c432d`다. `exact(fl(d SOURCE))`를 `exact(d) exact(SOURCE)`로 바꾸면 원 소스 계열을 바꾼다.

## 2. 전달할 미분 정보의 최소 완전성

스칼라 z(λ,b)의 carry를

\[
\mathcal J z=(z,z_\lambda,z_b,z_{\lambda b})
\tag{3}
\]

로 정의한다. 이는 ε²=η²=0인 대수에서

\[
z+z_\lambda\varepsilon+z_b\eta+z_{\lambda b}\varepsilon\eta
\tag{4}
\]

와 같다. 혼합계수에는 1/2를 붙이지 않는다. 곱은

\[
(ab)_{\lambda b}=a_{\lambda b}b+a_\lambda b_b+a_b b_\lambda+ab_{\lambda b}.
\tag{5}
\]

따라서 이 네 성분은 합·곱·양의 denominator에 대한 역수 및 C² 합성 아래 닫힌다. 혼합 미분을 다음 단계로 전달할 때 순수 λλ, bb 미분은 필요하지 않다. 그러나 `phys04_carry`가 저장하지 않는 순수 이차 slots를 0으로 채운다고 해서 실제 순수 미분이 0이라고 결론내릴 수는 없다. 이 문서의 결과는 (3)의 네 성분에 대한 것이다.

물리 값 z≥0와 signed tangent를 구분한다. 광자와 guard 값의 비음수 cone으로 value 포함을 교차하는 것은 허용되지만 zλ, zb, zλb에 같은 cone을 적용하지 않는다. value가 0이어도 zb 또는 zλb가 비영일 수 있으므로 group을 삭제할 수 없다.

## 3. 정리 A — 소스에 맞는 33-group의 완전한 carry

각 node j와 absorber a=HI,HeI,HeII에 대해

\[
L(g)=\bigl(1-x,\ f(1-y_1-y_2),\ fy_1\bigr),
\quad
\kappa_{ja}=c n_H\sigma_{ja}L_a(g),
\]
\[
D_j=1+d\sum_a\kappa_{ja},\qquad
N_j^+=\frac{N_j^{\rm in}}{D_j},\qquad
R_{ja}=\kappa_{ja}N_j^+.
\tag{6}
\]

κ의 단위는 s⁻¹, R의 단위는 photons/H/s다. 각 denominator는 원 소스의 동일한 captured leaves의 곱으로 정의하며, 물리적 값 범위에서 양수다. 다음 identity가 성립한다.

\[
\boxed{N_j^+=N_j^{\rm in}-d\sum_aR_{ja}.}
\tag{7}
\]

**증명.** dΣR=(D−1)N⁺이고 DN⁺=Nin이므로 바로 따른다. 어떤 채널도 omitted하지 않으며 thermal-w 상태에 따라 결정되는 동일 opacity를 사용한다.

스칼라 소스 J(g,λ,b)에 대하여

\[
\mathcal D_\lambda J=J_gU+J_\lambda,
\qquad \mathcal D_bJ=J_gV+J_b,
\]
\[
\mathcal D_{\lambda b}J
=J_gW+J_{gg}[U,V]+J_{g\lambda}V+J_{gb}U+J_{\lambda b},
\tag{8}
\]

여기서 U=gλ, V=gb, W=gλb다. Rj=ΣaRja로 두면

\[
\boxed{
\begin{aligned}
U_{N_j}&=(N_j^{\rm in})_\lambda-d\mathcal D_\lambda R_j,\\
V_{N_j}&=(N_j^{\rm in})_b-d\mathcal D_bR_j,\\
W_{N_j}&=(N_j^{\rm in})_{\lambda b}-d\mathcal D_{\lambda b}R_j.
\end{aligned}}
\tag{9}
\]

S1 및 S7의 saved Jets와 PHYS09의 U,V,W만으로 (9)를 계산할 수 있다. 33개 결과를 에너지 가중 합한 값은 PHYS10 관측량에 대응하지만, 이번 전달은 각 group의 spectral 정보를 남긴다. SOURCE_BOX의 photon 값 구간은 같은 소스의 값 포함이므로 (7)의 포함과 교차할 수 있다. 포함 구간이 비어 있다면 소스·표현·입력 일치 실패로 분류하고 반환한다. interval 합의 끝점이 원 실수 identity처럼 정확히 상쇄될 필요는 없다.

### 3.1 Independent quotient form

D는 g에 affine이므로 각 방향에서

\[
D_\lambda=d\kappa_gU,\quad D_b=d\kappa_gV,\quad D_{\lambda b}=d\kappa_gW,
\qquad \kappa=\sum_a\kappa_a.
\tag{10}
\]

N=Nin으로 간단히 표기하면

\[
\begin{aligned}
(N/D)_\lambda&=N_\lambda/D-ND_\lambda/D^2,\\
(N/D)_b&=N_b/D-ND_b/D^2,\\
(N/D)_{\lambda b}
&=\frac{N_{\lambda b}}D
-\frac{N_\lambda D_b+N_bD_\lambda+ND_{\lambda b}}{D^2}
+\frac{2ND_\lambda D_b}{D^3}.
\end{aligned}
\tag{11}
\]

이는 (9)와 같은 실수 함수를 주는 계산식이다. 새 source call 또는 nonlinear root를 요구하지 않는다. 식 (11)의 두 numerator–denominator 교차항 중 하나를 빼면 incoming이 양방향으로 변하는 다음 단계에서 틀린 결과를 얻는다.

### 3.2 첫 단계의 구조적 0과 저장된 signed tails

첫 단계에서는 COMMON과 geometry가 미래 θ에 독립이고 birth가 b-affine이므로

\[
(N_j^{\rm in})_\lambda=0,
\qquad (N_j^{\rm in})_{\lambda b}=0,
\qquad (N_j^{\rm in})_b=M_j.
\tag{12}
\]

M은 해당 고정 α의 source amount와 angular weight의 합이다. 저장된 PREBE Jet에는 outward 산술에서 발생한 λ 및 λb의 signed tails가 있다. 실제 저장 Jet를 그대로 소비한 포함과 (12)를 별도 증명에 따라 쓴 구조적 포함을 구별한다. 구조적 포함은 원 incoming이 (12)의 함수라는 전제에서만 적용한다. 두 계산을 교차하더라도 원 tails를 삭제한 새 소스로 기록하지 않는다.

식 (12)를 실제 다음 단계에 재사용할 수는 없다. 다음 단계의 Nin은 첫 단계의 θ-dependent outgoing photons를 전달받기 때문이다.

## 4. 정리 B — group에서 angular ray로의 lift와 실제 구현 경계

동일한 node j의 opacity는 ray r에 의존하지 않는다. 같은 원 소스 denominator Dj를 모든 ray에 쓰고,

\[
N_j^{\rm in}=\sum_r n_{rj}^{\rm in}
\]

를 만족하는 실제 ray family가 주어졌다면

\[
n_{rj}^+=n_{rj}^{\rm in}/D_j,\qquad
\sum_r\mathcal Jn_{rj}^+=\mathcal JN_j^+.
\tag{13}
\]

**증명.** denominator가 공통이므로 유한 합과 나눗셈을 교환한다. 같은 고정 계수와 C² family에서 유한 합과 모든 필요한 미분도 교환한다. (11)은 ray마다 그대로 적용된다.

이 정리는 group 결과가 실제 4224개 ray를 유일하게 복원한다는 뜻이 아니다. 초기 angular 분포와 이후 ray별 redshift가 필요하다. 특히 `n_rj/N_j`를 먼저 만드는 방법은 N_j=0에서 정의되지 않으므로 사용하지 않는다. (13)은 개별 numerator를 Dj로 직접 나누어 zero-stock의 signed forcing도 보존한다.

### 4.1 현재 distribute 함수의 계수 차이

S1의 residual은 `exact(c) exact(nH) exact(sigma)`를 각 Jet 곱에 넣는다. S2의 `phys04_distribute_after_be`는 `sigma*c*nH`를 먼저 binary64로 계산한 scalar leaf로 넣는다. 따라서 두 함수를 같은 exact-real map이라고 즉시 동일시할 수 없다. 한 채널의 차이를

\[
\delta_{ja}
=\operatorname{exact}(\operatorname{fl}(\operatorname{fl}(\sigma_{ja}c)n_H))
-\operatorname{exact}(\sigma_{ja})\operatorname{exact}(c)\operatorname{exact}(n_H)
\tag{14}
\]

로 쓰면, 실제 scalar evaluation order에 대응하는 captured coefficient에서

\[
\widetilde D_j-D_j=d\sum_aL_a\delta_{ja},
\quad
\frac{N}{\widetilde D_j}-\frac ND_j
=-\frac{N(\widetilde D_j-D_j)}{D_j\widetilde D_j}.
\tag{15}
\]

식 (15)의 같은 네 성분을 계산하면 차이를 수치적으로 감쌀 수 있다. 그 작은 크기 자체가 exact identity를 뜻하지는 않는다. 실제 ray carry를 채택하려면 (i) 소스와 동일 계수 graph로 ray lift를 하거나 (ii) 원 scalar graph를 그대로 보존하고 (15)의 차이를 명시적으로 포함해야 한다. PHYS11의 source-aligned group 결과는 이 경계를 넘지 않는다.

두 scalar 곱이 각각 정상 범위의 round-to-nearest binary64 연산이고 중간 underflow/overflow가 없으면 u=2⁻⁵³, γ₂=2u/(1−2u)에 대해 |δja|≤γ₂ c nH σja다. L≥0일 때 |D̃−D|≤γ₂(D−1)이고

\[
|N/\widetilde D-N/D|
\le\frac{N\gamma_2(D-1)}{D\{D-\gamma_2(D-1)\}}
\tag{15a}
\]

를 얻는다. N=0에서는 절대 차이가 0이며 상대 오차를 정의하지 않는다. 이 조건부 **값** 상계가 derivative equivalence, 원 native quotient의 전체 부동소수점 오차, actual native output을 인증하지는 않는다. 원 scalar leaves가 모두 있으면 δ 자체를 exact rational로 계산하는 것이 가능하다. S3의 `paired_runtime::endpoint`에는 `fl(fl(d*c)*nH)`를 먼저 capture하는 또 다른 factor graph도 있으므로 (14)의 graph와 합치지 않는다.

## 5. 정리 C — 고정 geometry의 joint transport

각 ray r의 redshift ratio ρr, hat weights H_r,kj 및 guard-export branch가 θ에 대해 고정되고, 해당 source branch에 대해 유효한 포함이 주어졌다고 하자. Source를 더하기 전 transport는

\[
\bar n_{rk}=\sum_jH_{r,kj}n^-_{rj},
\]
\[
G^N_r=G^{N,-}_r+\sum_{j\in\mathcal G_r}n^-_{rj},
\quad
G^U_r=\rho_rG^{U,-}_r+
\sum_{j\in\mathcal G_r}\rho_rE_jn^-_{rj}.
\tag{16}
\]

Birth가 k*=24에서 들어가면

\[
n^{\rm in}_{rk}=\bar n_{rk}+b s_k\omega_r\mathbf1_{k=k_*},
\quad s_k=\operatorname{exact}(\operatorname{fl}(d_k\mathrm{SOURCE})).
\tag{17}
\]

모든 미분 성분은 (16)의 같은 선형 map을 따른다. (17)의 일차 b 성분에는 s_kωr를 더하고, λ 및 λb 성분에는 새 direct birth 항이 없다. 하지만 (16)에 전달된 이전 n^-의 λ, b, λb가 일반적으로 비영이다. Guard 또한 같은 선형 map으로 전달한다. 첫 단계의 guard·redshift future derivatives가 0이어도 그 사실은 이후 단계로 자동 전파되지 않는다.

Source bookkeeping의 scalar `source_n=b s_k`와 실제 격자에 더한 양 `b s_k Σrωr`는 구별한다. 실제 normalized source family에서 Σωr=1의 관계가 유지되면 일치한다. 저장된 weight interval마다 독립 끝점을 고른 α에 대해 normalization을 증명하지 않았다면

\[
\delta S_N=b s_k(\sum_r\omega_r-1),
\quad \delta S_U=E_{k_*}\delta S_N
\tag{18}
\]

를 남겨야 한다. Scalar source_n/source_u의 actual Jet를 group sum 대신 억지로 사용하지 않는다. 첫 단계의 (18)은 b-affine이므로 mixed derivative는 0이지만, source amount와 first-b slope의 identity는 별도 문제다.

같은 ρ로 계산한 실제 piecewise-linear hat family는 내부 spectral 영역에서 ΣkH=1과 ΣkEkH=ρEj를 만족한다. 이 관계와 guard 분기를 유지하면 photon number transport identity와 redshift energy accounting이 따라온다. 서로 독립적인 weight interval의 끝점을 대입해서 이 관계가 정확하다고 선언하지 않는다. Source가 거절하는 guard/hat branch crossing을 범위를 넓혀 우회하지 않는다.

## 6. 정리 D — 실제 다음 단계 implicit composition의 누락 없는 식

다음 단계 gas를 g⁺(θ), 전달받은 입력을 r(θ), 원 residual을 G(g⁺,r,λ,b;αk)=0이라 하자. 모든 미분은 해당 같은 입력 family의 열린 C² 영역에서 존재하고 A=Gg가 가역이라고 가정한다. r에는 이전 gas와 source를 더한 incoming groups가 들어간다. Guard와 ledger가 이 local gas residual에 피드백하지 않으면 carry는 유지하되 r의 실제 의존 열은 0이다.

\[
AU^+=-\bigl(G_\lambda+G_r[r_\lambda]\bigr),\qquad
AV^+=-\bigl(G_b+G_r[r_b]\bigr),
\tag{19}
\]

대괄호는 Jacobian 또는 다중선형 미분의 방향 작용을 뜻한다.

\[
\begin{aligned}
AW^+=-\{&G_r[r_{\lambda b}]+G_{gg}[U^+,V^+]
+G_{gr}[U^+,r_b]+G_{rg}[r_\lambda,V^+]+G_{rr}[r_\lambda,r_b]\\
&+G_{g\lambda}V^++G_{gb}U^+
+G_{r\lambda}r_b+G_{rb}r_\lambda+G_{\lambda b}\}.
\end{aligned}
\tag{20}
\]

**증명.** GgU⁺+Gr rλ+Gλ=0을 b로 미분한다. Gg의 변화가 Ggg, Ggr, Ggb 항을 만들고, Gr의 변화가 Grg, Grr, Grb 항을 만든다. Gλ의 변화가 Ggλ, Grλ, Gλb를 만들며, rλ와 U⁺의 미분이 각각 rλb와 W⁺다. 총합을 A W⁺에 대해 정리하면 (20)이다.

### 6.1 HH 소스에 특화한 작은 4×4 계산식

실제 reduced RHS는

\[
F(g,\lambda,N)=F^{np}(g)+\lambda h(g)
-2H_{\rm mean}w e_4+\sum_jN_jQ_j(g),
\tag{21}
\]

\[
h=q(g)(1,0,0,-\chi_H),\quad
Q_j=\frac{C_j}{D_j},\quad
C_j=\sum_a\nu_{ja}\kappa_{ja},
\]
\[
\nu_{j0}=(1,0,0,a_{j0}),\quad
\nu_{j1}=(0,1/f,0,a_{j1}),\quad
\nu_{j2}=(0,-1/f,1/f,a_{j2}),
\tag{22}
\]

에서 a_ja=exact(captured heat_ja)다. λ 이외의 direct parameter dependence는 Nin의 carry에 흡수한다. FNN=0이며

\[
F_N\delta N=\sum_jQ_j\delta N_j,
\quad
(Q_j)_g u=\frac{(C_j)_g u}{D_j}-\frac{C_j(D_j)_g u}{D_j^2},
\]
\[
(Q_j)_{gg}[u,v]=-
\frac{(C_j)_gu(D_j)_gv+(C_j)_gv(D_j)_gu}{D_j^2}
+\frac{2C_j(D_j)_gu(D_j)_gv}{D_j^3}.
\tag{23}
\]

C,D가 g에 affine인 점을 사용했다. G=g⁺−g⁻−dF에 대해 A=I−dFg이고, incoming N의 각 derivative를 Nλ,Nb,Nλb로 표기하면

\[
\boxed{
\begin{aligned}
AU^+&=U^-+d\bigl(F_N[N_\lambda]+h\bigr),\\
AV^+&=V^-+dF_N[N_b],\\
AW^+&=W^-+d\{F_{gg}[U^+,V^+]
+F_{gN}[U^+,N_b]+F_{Ng}[N_\lambda,V^+]\\
&\hspace{39mm}+F_N[N_{\lambda b}]+h_gV^+\}.
\end{aligned}}
\tag{24}
\]

식 (24)는 photon 33개를 nonlinear unknown에 다시 넣을 필요 없이, 원 4개 gas unknown의 같은 implicit matrix를 사용한다. 각 group의 Qj와 그 derivative를 합산하면 된다. 새 단계에서 rank-one birth direction뿐 아니라 Nλ와 Nλb가 함께 들어오므로, 기존 첫 단계의 b-gradient 하나만으로 이 항들을 대체할 수 없다.

이론식이 닫혔다는 것과 실제 second_half 포함이 닫혔다는 것은 별개다. 다음 단계에는 실제 angular/guard 상태, 새 PreBE source coverage, 새 root·C²·A-inverse의 같은 family 근거가 필요하다. PHYS09의 첫 단계 A,U,V,W를 그대로 복사해서 (24)를 만족한다고 할 수 없다.

간단한 합성 반례로 첫 map의 x₁=λ, P₁=1+b를 다음 map P₂=P₁/(2−x₁)에 전달하자. 두 첫 출력의 mixed derivative는 모두 0이지만 P₂,λb=(2−λ)⁻²이고 단위 사각형의 finite interaction은 1/2이다. 이전 W가 0이라는 이유로 다음 W를 0으로 두면 일차 carry 사이의 교차항을 잃는다. 이것은 합성 법칙의 대수적 검산 사례이며 실제 HH history가 아니다.

## 7. 반응·source·열 ledger의 joint carry

미래 source-only ledger를 L이라 두고 한 단계 증가량 ΔL을 계산하면

\[
\mathcal JL^+=\mathcal JL^-+\mathcal J\Delta L.
\tag{25}
\]

다음 증가량은 현재 saved source로부터 유도된다.

| Ledger | 증가량 | 단위 |
|---|---|---|
| absorbed number | dΣjaRja | photons/H |
| source number | PREBE의 source_n; underlying 함수 b s | photons/H |
| source energy | PREBE의 source_u; underlying 함수 E* b s | eV/H |
| thermal expansion work | 2dHmean w | eV/H |
| HH events | d λ q(g) | events/H |
| HH threshold thermal contribution | −χH d λ q(g) | eV/H |

각 항의 값, U,V,W는 (8)과 곱셈식 (5)로 계산한다. 특히 HHevents를 QHH라 쓰면, 구조적으로 q=q(g)인 같은 소스에서

\[
\begin{aligned}
(Q_{HH})_\lambda&=d(q+\lambda q_gU),\\
(Q_{HH})_b&=d\lambda q_gV,\\
(Q_{HH})_{\lambda b}&=d\{q_gV+\lambda(q_gW+q_{gg}[U,V])\}.
\end{aligned}
\tag{26}
\]

저장된 q Jet의 signed parameter tails까지 소비할 때는 먼저 (8)로 `(q,Uq,Vq,Wq)`를 만들고

\[
\mathcal JQ_{HH}=d\bigl(\lambda q,\ q+\lambda U_q,
\ \lambda V_q,\ V_q+\lambda W_q\bigr)
\tag{26a}
\]

를 사용한다. 여기의 λ는 같은 parameter family의 coordinate이며 값 interval은 [0,1]이다. 식 (26a)는 raw parameter derivatives가 있는 q에 대해서도 유효하고, 실제 구조적으로 없는 미분을 수치 tails와 혼동하지 않는다. Thermal work의 carry는 단순히 `2 d Hmean (w,Uw,Vw,Ww)`다.

PHYS10의 HH gas energy cancellation은 이 반응의 ionization binding gain과 threshold thermal loss가 동일 χH를 사용해서 상쇄되는 것이었다. (26)은 이벤트 ledger 자체의 mixed response를 남긴다. 누적된 HH 이벤트를 전체 gas energy injection으로 해석하지 않는다.

S3의 `ledger_comp[5]`의 순서는 redshift work, thermal work, source number, source energy, absorbed number다. `energy_comp`는 conservative thermal point update가 사용하는 산술 compensation이다. S5는 primal compensation을 physical state에 보존하고 미래 real-family derivative ledgers를 별도의 Jet로 초기화한다. 이 분리를 계속 유지해야 한다. Kahan compensation의 binary64 rounding path를 C² 함수의 물리 derivative로 미분하지 않는다. 미래 exact-real ledger의 0 초기화는 과거 scalar ledger의 삭제가 아니다.

## 8. Source-derived escape ledger와 남는 잔여

이 절은 현재 export에 없는 native escape derivative를 대체한다고 주장하지 않는 별도 **source-derived observable**다. native endpoint는 raw FT03의 `escaped_energy_rate/(nH ev)`를 사용한다(S4). S6는 그 scalar를 직접 export하지 않지만 같은 exact-real nonphoto 함수로부터 다음 양을 정의할 수 있다.

\[
\widehat\ell=(\chi_H,\widehat f\chi_{\rm HeI},
\widehat f(\chi_{\rm HeI}+\chi_{\rm HeII}),1),
\quad
\Gamma_*=-\widehat\ell F^{np}.
\tag{27}
\]

S6에서 ci_a, rr_a, dr_m를 모두 per H per second의 반응율로 쓰고, K_a를 radiative recombination의 thermal energy loss rate, τa=exact(model.gas.threshold_ev[a])를 nonphoto collisional threshold로 쓰면

\[
j_0=ci_0-rr_0,\quad
j_1=ci_1-rr_1-\sum_mdr_m,\quad
j_2=ci_2-rr_2,
\]
\[
F^{np}=(j_0,(j_1-j_2)/\widehat f,j_2/\widehat f,w^{np}),
\quad
w^{np}=-\sum_a\tau_a ci_a-\sum_aK_a
-\sum_mdr_m\frac{k_BB_m}{\mathrm{eV}_{erg}}.
\tag{28}
\]

따라서 직접 대입하면

\[
\boxed{\Gamma_*
=\sum_a\chi_a rr_a+\sum_aK_a
+\sum_mdr_m\left(\chi_{\rm HeI}+\frac{k_BB_m}{\mathrm{eV}_{erg}}\right)
+\sum_a(\tau_a-\chi_a)ci_a.}
\tag{29}
\]

S9의 controlled fixture는 `threshold_ev=[13.598_434_599_702,24.587_389_011,54.417_76]`을 설정한다. `Ft03Model::controlled()`는 threshold를 바꾸지 않고, S4의 model(stage)도 density 두 필드만 바꾼다. 따라서 이번 원 source에서 τa=χa의 leaf identity는 확인됐다. 마지막 항이 정확히 사라져 Γ*는 S6의 exact-real RR·DR escaping losses의 합이다. 이 source leaf 확인과 아직 없는 native escape derivative export를 구별한다.

원 물리 영역에서 Γ*의 값은 비음수다. CI/RR/DR rate, threshold와 kbB/ev는 비음수다. RR kinetic factor는 `kb*T*alpha*(1.5+slope)`이고, HeI에서는 1.5−0.654>0이다. H/HeII의 `slope=−1.503+1.923*0.470*u/(1+u)`에서 T≤110,000 K와 원 λfit/(0.522T)>1로 u>1이므로 `1.5+slope>−0.003+(1.923*0.470)/2>0`이다. 따라서 K_a도 비음수다. 이 값의 positivity는 escape*의 signed U,V,W나 finite interaction의 positivity를 뜻하지 않는다.

이 source-derived escape 증가량의 네 성분은

\[
\boxed{\mathcal J\Delta E_{esc,*}
=-d\sum_{i=0}^3\widehat\ell_i
\bigl(F_i^{np},\mathcal D_\lambda F_i^{np},
\mathcal D_bF_i^{np},\mathcal D_{\lambda b}F_i^{np}\bigr).}
\tag{29a}
\]

고정 α에서 fhat와 d가 θ-independent이므로 추가 coefficient 미분은 없다. 식 (29a)는 저장된 full nonphoto Jet 네 개만 사용한다. 이때 PHYS10에서 사용한 ℓf-projection을 그대로 음수로 바꾸면 Jnorm까지 escape에 흡수하므로 (27)과 다른 관측량이 된다.

HH와 photon 항을 추가하기 전 Fnp를 사용해야 한다. f 대신 fhat가 (27)에 들어가는 이유도 (28)의 정확한 분모 때문이다. Native escaped-energy scalar와 (29)의 coefficient graph 및 원 floating evaluations를 연결하는 일은 아직 별도 의무다. 여기서 Γ*를 계산해도 native escape derivative가 실행·인증된 상태로 바뀌지 않는다.

S8의 gas energy e=ℓf g와 photon energy eγ에 대한 identity는

\[
e^++e_\gamma^+-e^--E_\gamma^{in}
=d(\ell_fF^{np}-2H_{\rm mean}w+\Psi).
\tag{30}
\]

여기에 ΔEesc,*=dΓ*와 ΔWth=2dHmeanw를 더하면

\[
\boxed{
e^++e_\gamma^++\Delta E_{esc,*}+\Delta W_{th}
-e^--E_\gamma^{in}
=d(J_{norm}+\Psi),}
\tag{31}
\]

\[
J_{norm}=(\ell_f-\widehat\ell)F^{np},\quad
\Psi=\sum_{ja}(a_{ja}+\chi_a-E_j)R_{ja}.
\tag{32}
\]

이것은 PHYS10의 잔여를 nonphoto loss와 thermal work로 분해해서 두 표현 차이까지 추적한 식이다. 왼쪽의 모든 양은 같은 source-family에서 정의한다. 각 항의 미분을 따로 큰 interval로 만든 뒤 마지막에 빼기보다, 오른쪽의 Jnorm+Ψ Jet를 먼저 합쳐 (8)을 적용하면 공통 항을 더 잘 보존할 수 있다. Jnorm을 Γ* 및 ℓfFnp 밖에 이중으로 더하지 않는다.

### 8.1 Mixed derivative와 유한 interaction

증대 ledger 잔여를

\[
T_*=e^++e_\gamma^++\Delta E_{esc,*}+\Delta W_{th}
-e^--E_\gamma^{in}
\tag{33}
\]

로 정의하면 (31)에서 곧바로

\[
\mathcal JT_*=d\bigl(J_{norm}+\Psi,
\mathcal D_\lambda[J_{norm}+\Psi],
\mathcal D_b[J_{norm}+\Psi],
\mathcal D_{\lambda b}[J_{norm}+\Psi]\bigr).
\tag{34}
\]

특히 T*,λb=d Dλb[Jnorm+Ψ]다. 각 항을 먼저 별도로 감싼 direct sum과 (34)를 source에서 먼저 투영한 포함은 같은 실수 잔여를 포함하지만 interval endpoint는 같을 필요가 없다.

같은 α와 같은 root family에서 `I_z=z(1,1)−z(1,0)−z(0,1)+z(0,0)`를 쓰면 이중 기본정리에 따라

\[
I_{T_*}=d\int_0^1\!\int_0^1
\mathcal D_{\lambda b}[J_{norm}+\Psi]\,db\,d\lambda.
\tag{35}
\]

현재 두 첫 단계에서는 이전 gas가 θ-independent이고 incoming photon energy가 b-affine이므로 Ie⁻=Iγ,in=0이다. 따라서

\[
\boxed{I_e+I_\gamma+I_{\Delta E_{esc,*}}+I_{\Delta W_{th}}
=d\int_0^1\!\int_0^1
\mathcal D_{\lambda b}[J_{norm}+\Psi]\,db\,d\lambda.}
\tag{36}
\]

단위 parameter 사각형의 면적은 1이므로 (34)의 uniform mixed 포함을 (36)의 유한 합에도 쓸 수 있다. 실제 다음 단계에서는 Ie⁻와 Iγ,in이 일반적으로 0이 아니며 (35)의 정의대로 보존해야 한다. 서로 다른 source tuple의 네 corner를 빼거나, pointwise derivative ratio를 적분해서 finite ratio라 부르는 방법은 사용하지 않는다.

조건부 실제 연속 단계에서 (31)과 transport energy accounting을 합산하면 중간 gas/photon/guard energy가 telescoping하고 source energy, redshift work, escape*, thermal work, 각 단계 d(Jnorm+Ψ)가 남는다. 이 이론적 telescoping은 현재 미확보 history에 대한 수치 보존 오차 또는 continuum remainder를 제공하지 않는다.

## 9. 검산 경계와 물리적 해석

이 구성은 기존의 총 photon energy 한 개를 넘어서, 다음 transport가 필요로 하는 spectral gas–photon 상관 응답을 보존한다. HH가 바꾼 흡수율에 대한 photon λ response, 직접 birth와 기체 응답을 합친 b response, 둘의 mixed response가 같은 root family에서 함께 전달된다. Group-wise output은 actual angular lift가 준비되었을 때 같은 denominator를 공유하는 ray map으로 이어질 수 있다.

관련 극한과 반례는 다음과 같다.

- d=0의 연속 극한에서 gas와 photon carry는 입력 carry로 돌아가고 모든 단계 ledger 증가량은 0이다. 원 실행 함수의 d>0 domain을 이 극한 때문에 바꾸지는 않는다.
- κ=0이면 N⁺=Nin이며 새로운 흡수 mixed effect는 없다. 다음 단계에는 과거의 mixed photon carry가 그대로 남을 수 있다.
- 초기 Nin=0이어도 Nb≠0이면 derivative carry가 비영이다. value-only pruning은 이 정보를 잃는다.
- 새 단계에서 Nλ≠0이면 (24)의 FNg[Nλ,V⁺]가 필요하다. 첫 단계 공식을 반복하면 이 항과 W⁻, Nλb를 잃는다.
- f=fhat, captured heat+χ=E이며 동일 source-derived escape를 포함한 이상적인 coefficient graph에서는 (31)의 오른쪽이 0이다. 실제 captured leaves는 이 등식의 전제를 그대로 만족한다고 가정하지 않는다.
- Guard/ray의 실제 입력과 그 geometry 연결이 없으면 33-group 포함만으로 actual second_half transport를 재구성할 수 없다.

이번 이론으로 닫히는 것은 source-aligned joint group carry, 필요한 ledger 증가량, 같은 mixed derivative를 보존하는 composition 법칙이다. Actual carried second_half, native authority, temporal defect, continuum remainder, full49 및 production 상태는 계속 OPEN이다.
