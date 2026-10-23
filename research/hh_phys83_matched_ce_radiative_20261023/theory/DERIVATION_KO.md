# PHYS83 구성적 유도: matched CE pair와 원자 내부 에너지·복사 packet

## 범위와 근거 상태

이 문서는 PhysMath Research Loop 1.3.0의 R4/R5 구성 결과다. 실제 읽은 skill context는 `c38/physmath-research-loop/SKILL.md`, `references/POLICY_INTEGRATION.md`, `references/THEORY_LOOP.md`의 R4/R5다. 선택된 단원은 PHYS82 다음 `BOUND_BOUND_CE_AND_RADIATIVE_COOLING`이며 parent가 정한 한 단원의 이론→구현 범위 안에 있다. 이 작성자는 새로운 과학 grid, ODE, benchmark, CAS 또는 독립 검증을 실행하지 않았다. 아래 수학은 **derived**이고, 원자 source 사실은 별도 source 계약에 결속한다. 문서만으로 **numerically checked** 또는 **implementation verified**라고 표시하지 않는다.

원래 보호 조건: non-tilted LRS Bianchi I; metric (-,+,+,+); reacting gas pi=0; collisionless DM pi_m 별도; 같은 normal orthonormal frame에서 signed matter/radiation tensor를 합한 뒤 norm; Frobenius=sqrt(2)×half-contraction. 이 local source 단원은 기하, 기존 PI/RR/CI source, 실제 trajectory, 초기 전하 계약을 수정하지 않는다. HH_R10=OFF. Production admission NOT_ISSUED.

선택된 physical approximation은 **고정된 T와 n_e, 고정 physical volume에서의 H I 1s/2s/2p star, matched finite-support Maxwell CE/deexcitation, recoil-free spontaneous emission, optically thin immediate escape**다. T와 n_e는 이 substep의 외부 입력이다. 원자의 여기 에너지는 동적으로 저장한다. 여기서 emitted radiation energy와 cell 밖으로 escaped energy가 같은 것은 선택한 optically thin closure 때문이다. 별도 임의 escape-time reservoir를 생산 코드에 넣지 않는다.

### 후보와 수렴

| 후보 | 실제 식과 장점 | 판정 |
|---|---|---|
| 1s/2s/2p star + optically thin spontaneous emission | 두 matched CE pair, 3-state Markov generator, 2×2 exact reduction, thermal/internal/emitted ledgers | **선택**. Source 두 쌍과 radiative branch가 확보됨 |
| 1s↔2p 두 준위만 | scalar convex exponential와 exact cumulative events | 축소 검산/degenerate limit. 2s가 확보되어 주모형으로 축소할 이유 없음 |
| 시간 지연 radiation reservoir 또는 Sobolev effective line | radiation storage, absorption/feedback 또는 quasistationary elimination이 추가됨 | 이번 구현에서 보류. Source/energy owner가 다른 별도 closure |

핵반응, He/Li CX·CE, higher levels/cascades, line trapping/absorption/stimulated emission, finite recoil, finite-splitting 2s↔2p mixing은 OPEN이다. CCC의 degenerate LS 2s↔2p cross section 발산은 이 항들을 0으로 물리적으로 증명하지 않는다. 이 단원은 해당 channel들을 제외한 명시적 finite subsystem이다.

## 1. 데이터 좌표와 하나의 matched collision kernel

Source agent가 확보한 CCC files `2S.1S`, `2P.1S`는 final.initial 이름 규칙의 ground→upper excitation이다. `1S.2S`, `1S.2P`는 reverse source 비교 자료다. Source-native common gap은

\[
\Delta=10.2043500\ \mathrm{eV}.
\]

Input energy는 incident electron energy, source cross section은 a0²다. 생산 계산은 고정된 a0 변환으로 cm²를 사용한다. LS weight는 ground1s의 g_g=2, 2s의 g_s=2, 2p의 g_p=6인 resolved-term population convention에 결속한다. 따라서 r_i=g_i/g_g는 (1,3)이다. 이 weight는 미분해 spin/magnetic substate를 합친 population의 의미와 일치해야 한다.

Upper channel i의 excitation incident energy E에 대해 excess coordinate를

\[
\epsilon=E-\Delta\ge0,
\qquad W_i(\epsilon)=(\epsilon+\Delta)\sigma_{g i}(\epsilon+\Delta)
\]

로 둔다. **W를 source knots 사이에서 piecewise linearly interpolate**한다. 이것은 sigma 자체의 PL interpolation과 다른, 이번에 명시적으로 채택한 numerical source representation이다. Raw source bytes와 raw knot values는 유지한다. 첫 threshold anchor는 W(0)=0이며, positive source points와 마지막 finite endpoint까지 이어진다. Outside support의 omitted physical source는 별도 의무다. 수학적으로 정의한 finite operator를 실제 full cross section이 support 밖에서0이라는 관측 명제로 바꾸지 않는다.

역반응을 독립 sigma interpolation으로 정의하지 않고

\[
\boxed{\epsilon\sigma_{i g}(\epsilon)=r_i^{-1}W_i(\epsilon)}
\]

로 **같은 W와 shifted support**에서 정의한다. 이는 stationary-heavy-target scattering reciprocity

\[
g_g E\sigma_{g i}(E)=g_i(E-\Delta)\sigma_{i g}(E-\Delta)
\]

를 그대로 보존한다. epsilon=0에서 sigma_down의 pointwise 값이 불안정하더라도 Maxwell flux에 들어가는 epsilon sigma_down은 W/r로 정의된다. Raw reverse source knots는 이 construction의 독립 source consistency 비교에 쓴다. Raw reverse sigma를 다시 PL interpolation해서 두 rate가 정확 detailed balance를 만족한다고 주장하면 안 된다.

## 2. 한 positive moment로 두 Maxwell rate와 도함수

\(\theta=k_BT\)를 eV 단위로 쓰고, \(\epsilon,\Delta\)도 eV 수치로 쓴다. Cross section이 cm²이면

\[
C=100\sqrt{\frac{8\,\mathrm{eV_J}}{\pi m_e}},\quad
M_{i,n}(\theta)=\int_{\epsilon_-}^{\epsilon_+}
\epsilon^n W_i(\epsilon)e^{-\epsilon/\theta}\,d\epsilon.
\]

Electron mass Maxwell convention에서

\[
\boxed{q_{g i}=C\theta^{-3/2}e^{-\Delta/\theta}M_{i,0}},\qquad
\boxed{q_{i g}=C\theta^{-3/2}r_i^{-1}M_{i,0}}.
\]

두 식 모두 cm³/s다. SI로 검산하면 prefactor는 \(\sqrt{8/(\pi m_e)}(k_BT)^{-3/2}\), integral은 \(\int E_J\sigma(E_J)e^{-E_J/(k_BT)}dE_J\)이므로 전체 단위는 m³/s다. 위의 100은 speed m/s→cm/s 변환이며 source area 변환을 대체하지 않는다.

변수 치환으로 직접 얻는 결과는

\[
\boxed{q_{g i}/q_{i g}=r_i e^{-\Delta/\theta}}.
\]

이는 같은 finite support와 같은 interpolated W에 대해 정확하다. 원자료의 반올림 일치, 실제 cross section의 정확도 또는 missing tails의 유효성을 증명하는 결과는 아니다. 계산할 때 작은 q_up에 exp(+Delta/theta)를 곱해서 q_down을 만들지 않는다. 한 M0의 log-domain 값과 서로 다른 두 Boltzmann prefactor로 두 값을 구하면 overflow/underflow의 불필요한 조합을 피한다.

Reaction-selected excess mean을

\[
\bar\epsilon_i=M_{i,1}/M_{i,0}
\]

로 정의하면 excitation incoming mean은 Delta+epsilonbar이고 deexcitation incoming mean은 epsilonbar다. 같은 고정 source와 fixed support에서

\[
\boxed{\frac{d\log q_{g i}}{dT}
=\frac{(\Delta+\bar\epsilon_i)/\theta-3/2}{T}},\qquad
\boxed{\frac{d\log q_{i g}}{dT}
=\frac{\bar\epsilon_i/\theta-3/2}{T}}.
\]

따라서 두 log derivative의 차이는 \(\Delta/(k_B T^2)\)다. 도함수 식은 source validity 밖으로 rate를 외삽하라는 허가가 아니다.

### PL W의 양의 cell 적분

Cell [epsilon_j,epsilon_j+h]에서 z=h/theta, u=(epsilon-epsilon_j)/h라 두면

\[
M_{0,j}=h e^{-\epsilon_j/\theta}
\{W_j L_0(z)+W_{j+1}L_1(z)\},
\]
\[
L_0=\int_0^1(1-u)e^{-zu}du
=\frac{z-1+e^{-z}}{z^2},\quad
L_1=\int_0^1u e^{-zu}du
=\frac{1-(1+z)e^{-z}}{z^2}.
\]

둘은 z>=0에서 nonnegative이며 z=0에서1/2다. Small z에서 subtraction 식을 그대로 쓰지 않고 convergent series/entire functions로 계산한다. 예를 들어

\[
L_0=\sum_{n\ge0}\frac{(-z)^n}{(n+2)!},\quad
L_1=\sum_{n\ge0}\frac{(-z)^n}{n!(n+2)}.
\]

작은 z에 대한 전항 양의 대안도 있다:

\[
L_0=e^{-z}\sum_{n\ge0}\frac{z^n}{n!(n+2)},\qquad
L_1=e^{-z}\sum_{n\ge0}\frac{z^n}{(n+2)!}.
\]

M1은 같은 cell에 epsilon_j+h u를 추가하여 계산한다. \(K_n=\int_0^1u^n e^{-zu}du\)라 쓰면

\[
M_{1,j}=\epsilon_j M_{0,j}
+h^2e^{-\epsilon_j/\theta}
\{W_j(K_1-K_2)+W_{j+1}K_2\},
\]

여기서 K1-K2도 positive integral이다. Production quadrature 없이 source cell moment를 전합하는 경로가 가능하다. 코드 구현의 stability gate와 독립 quadrature는 parent의 C 단계 의무다.

### 극한

Finite support에서 theta→infinity면 M0는 finite constant로 가므로 두 q는 T^(-3/2)이다. 이것을 full atomic high-energy asymptote로 부르면 안 된다. Threshold first cell의 W~s epsilon인 선택된 interpolation 아래 theta→0에서 q_up~const×theta^(1/2) exp(-Delta/theta), q_down~const×theta^(1/2)다. 이 극한도 선택한 threshold representation의 극한이다. 실제 unresolved threshold behavior에 대한 추가 claim은 아니다.

## 3. CE 사건과 열 에너지: incoming mean을 이중 차감하지 않기

하나의 excitation collision은 electron kinetic energy를 E에서 E-Delta로 바꾸고 atom internal energy를 Delta만큼 높인다. Deexcitation은 반대다. 따라서 사건당 thermal ledger는 excitation -Delta, deexcitation +Delta다. Reaction-selected incoming energy 전체를 cooling으로 빼면 outgoing kinetic energy를 빠뜨려 double counting이 된다.

고정 n_e에서

\[
a_i=n_e q_{g i},\quad b_i=n_e q_{i g},\quad d_i=b_i+A_i
\]

는 s^-1다. Parent selected source card는

\[
A_s=A_{s,2\gamma}+A_{s,M1}
=8.229+2.496\times10^{-6}
=8.229002496\ \mathrm{s^{-1}},
\]
\[
A_p=A_{p,E1}=6.260\times10^8\ \mathrm{s^{-1}}.
\]

2s two-photon과 작은 M1 branch는 분리된 event count로 남긴다. 각 radiative event의 total photon energy는 선택한 CCC LS gap Delta다. 2gamma event가 Delta짜리 photon 두 개를 만든다는 뜻은 아니다. 두 photon의 total energy가 Delta이고 number yield가2다. Spectrum이나 각 photon의 energy distribution은 이번 상태변수에 없다.

이것은 CCC-native level gap과 tabulated lifetimes를 사용하는 명시적 approximate LS source card다. 실제 fine-structure/isotope-resolved atomic card와 동일하다고 주장하지 않는다.

## 4. 세 준위 population generator와 exact reductions

Atom fraction x=(x_g,x_s,x_p)^T에서

\[
\dot x=Qx,\qquad
Q=\begin{pmatrix}
-(a_s+a_p)&d_s&d_p\\
a_s&-d_s&0\\
a_p&0&-d_p
\end{pmatrix}.
\]

Q의 off-diagonal은 nonnegative이고 column sum은0이다. 따라서 exact exp(Qt)는 column stochastic이며 nonnegative initial fraction의 positivity와 x_g+x_s+x_p=1을 보존한다. Excitation·deexcitation·bound-bound radiation은 ionic charge와 free-electron number를 바꾸지 않는다.

선택된 science initial condition은 x(0)=(1,0,0)이다. 두 upper fraction v=(x_s,x_p)^T만 쓰면

\[
\dot v=a-Bv,\quad a=(a_s,a_p)^T,\quad
B=\begin{pmatrix}d_s+a_s&a_s\\a_p&d_p+a_p\end{pmatrix}.
\]

A_i>0이므로 d_i>0이고

\[
D_B=\det B=d_s d_p+a_s d_p+a_p d_s>0.
\]

두 decay eigenvalue는 positive다. 계산식은

\[
\delta=\operatorname{hypot}(d_s+a_s-d_p-a_p,\,2\sqrt{a_s a_p}),
\]
\[
\lambda_f=\frac{d_s+d_p+a_s+a_p+\delta}{2},\qquad
\boxed{\lambda_l=D_B/\lambda_f}.
\]

lambda_l를 trace-minus-discriminant로 계산하면 큰 A_p/A_s 때문에 불필요한 cancellation이 생긴다. det/lambda_f를 쓴다. 이 수식 역시 multiplication overflow가 없는 declared floating range를 필요로 한다; 큰 n_e를 무한히 받아들이는 API가 아니다.

### 평형과 detailed balance

\[
r_i^*=a_i/d_i,\quad R_*=r_s^*+r_p^*,\quad
x_g^*=\frac1{1+R_*},\quad
x_i^*=\frac{r_i^*}{1+R_*}.
\]

Radiation A=0인 collision-only limit에서는 r_i^*=r_i exp(-Delta/theta)이므로 finite three-level Boltzmann equilibrium을 회복한다. A>0에서는 radiation으로 에너지가 나가므로 이 stationary state를 thermodynamic LTE라고 부르지 않는다. n_e=0이면 ground initial state는 그대로이며 모든 새 event count가0이다.

## 5. Ground-start exact finite step와 integrated populations

다음 entire functions를 사용한다.

\[
h(\lambda,t)=\frac{1-e^{-\lambda t}}{\lambda}
=t\,\phi_1(-\lambda t),\quad
G(\lambda,t)=\frac{t-h(\lambda,t)}{\lambda}
=t^2\phi_2(-\lambda t).
\]

h(0,t)=t, G(0,t)=t²/2다. \(\phi_1(z)=(e^z-1)/z\), \(\phi_2(z)=(e^z-1-z)/z²\)의 removable singularities를 채운다. h는 `-expm1(-lambda*t)/lambda`, G는 small-argument series를 사용한다. t-h의 naive subtraction은 lambda*t가 작을 때 금지할 구현 경로다.

\[
H_2=\frac{h(\lambda_l,t)-h(\lambda_f,t)}{\lambda_f-\lambda_l},\qquad
H_3=\frac{G(\lambda_l,t)-G(\lambda_f,t)}{\lambda_f-\lambda_l}.
\]

Exact ground-start solution과 time-integrated upper occupations는

\[
\boxed{x_s(t)=a_s\{h_f+(d_p-\lambda_l)H_2\}},\qquad
\boxed{x_p(t)=a_p\{h_f+(d_s-\lambda_l)H_2\}},
\]
\[
\boxed{J_s(t)=a_s\{G_f+(d_p-\lambda_l)H_3\}},\qquad
\boxed{J_p(t)=a_p\{G_f+(d_s-\lambda_l)H_3\}},
\]

where J_i=int_0^t x_i(u)du and x_g=1-x_s-x_p. These follow from the resolvent

\[
[(sI+B)^{-1}a]_i
=\frac{a_i(s+d_j)}{(s+\lambda_l)(s+\lambda_f)},\qquad j\ne i,
\]

and its convolution with a constant forcing. No time-stepping IVP is required for frozen coefficients.

Equivalent matrix notation is v=t phi1(-Bt)a and J=t² phi2(-Bt)a. The scalar formulas expose how to avoid feeding expm a huge norm proportional to A_p t while preserving the slow branch. An arbitrary initial vector would add exp(-Bt)v0 and t phi1(-Bt)v0 respectively, but that extension is not required by the selected ground-only production API.

### Coincident eigenvalues and stable divided differences

At lambda_l=lambda_f=lambda,

\[
H_2=\int_0^t u e^{-\lambda u}du
=\frac{1-(1+\lambda t)e^{-\lambda t}}{\lambda²},
\]
\[
H_3=\int_0^t(t-u)u e^{-\lambda u}du
=\frac{\lambda t-2+(\lambda t+2)e^{-\lambda t}}{\lambda³}.
\]

At lambda=0 these are t²/2 and t³/6. The displayed subtraction formulas are analytic definitions, not stable small-argument implementations. They need series/scaled gamma or equivalent entire-function evaluation.

For delta=lambda_f-lambda_l>=0,

\[
H_2=\int_0^t e^{-\lambda_l u}\frac{1-e^{-\delta u}}{\delta}du,\quad
H_3=\int_0^t(t-u)e^{-\lambda_l u}\frac{1-e^{-\delta u}}{\delta}du.
\]

These are positive and have a controlled near-coincidence series. With
\(J_k^e=\int_0^t u^k e^{-\lambda_l u}du\),

\[
H_2=\sum_{n\ge0}\frac{(-\delta)^n}{(n+1)!}J_{n+1}^e,
\quad
H_3=\sum_{n\ge0}\frac{(-\delta)^n}{(n+1)!}
[tJ_{n+1}^e-J_{n+2}^e].
\]

For delta*t<=1/4 the alternating terms decrease at least by the factorial ratio; a next-term bound gives a concrete truncation stopping condition. Both bracketed integrals are positive. A source-specific implementation may instead use a verified analytic divided-difference routine. Merely substituting an equal-eigenvalue limit without a declared tolerance/error bound is not an exact method for distinct eigenvalues.

A particularly stable H2 form for x=lambda_l*t<=1 and delta*t not tiny is

\[
H_2=\frac{e^{-x}}{\lambda_f}
\{t-h(\delta,t)+\lambda_l t²\phi_2(x)\}.
\]

Every displayed term is nonnegative. For x>=1 the complementary form

\[
H_2=\frac{1-e^{-x}[1+\lambda_l h(\delta,t)]}
{\lambda_l\lambda_f}
\]

avoids near cancellation; lambda_l=0 is handled by the continuous limit. This is a constructive option, not a demand to add an unnecessary abstraction if another verified implementation suffices.

### Conditioning and positivity interpretation

B reduced to upper populations is not a Metzler generator, so its off-diagonal exponential need not be positive. Positivity belongs to the full Q evolution. Individual upper populations can overshoot their stationary values due to competition for ground atoms; a monotonicity assertion for each upper level is unwarranted.

For ground initial data, full Q is reversible with its own stationary vector: pi_g a_i=pi_i d_i. Symmetrization makes the ground return probability a sum of nonnegative decaying spectral weights. Thus x_g(t)>=x_g* and total upper fraction increases monotonically. This is a Markov algebraic property, not a claim of thermodynamic equilibrium with escaping radiation.

Since a_i/d_i <= a_i/b_i=r_i exp(-Delta/theta) when b_i>0,

\[
x_g(t)\ge x_g^*\ge\frac1{1+(r_s+r_p)e^{-\Delta/\theta}}\ge\frac15.
\]

The same bound holds for integrated ground occupancy J_g=t-J_s-J_p>=t/5. Consequently subtracting J_s+J_p from t is not arbitrarily ill-conditioned in the selected matched ground-start model. Generic arbitrary-rate fixtures outside detailed balance do not inherit this bound.

## 6. Exact event counts and energy packet

Per initial H I atom, define

\[
C_i^+=a_iJ_g,\qquad C_i^-=b_iJ_i,
\]
\[
C_{s,2\gamma}=A_{s,2\gamma}J_s,\quad
C_{s,M1}=A_{s,M1}J_s,\quad
C_{p,E1}=A_pJ_p.
\]

All are nonnegative. They are cumulative event counts, not probabilities, and may exceed1 under a maintained bath. Let C_i^R be the sum of radiative branch counts for upper i. Then

\[
x_i(t)=C_i^+-C_i^--C_i^R
\]

for the selected ground initial condition. Atomic excitation energy and emitted/escaped energy per initial atom are

\[
U_{at}=\Delta(x_s+x_p),\qquad
E_\gamma=\Delta(C_{s,2\gamma}+C_{s,M1}+C_{p,E1}).
\]

The emitted photon number is

\[
N_\gamma=2C_{s,2\gamma}+C_{s,M1}+C_{p,E1}.
\]

Thermal energy withdrawal is signed in the general event definition,

\[
Q_{th}=\Delta\sum_i(C_i^+-C_i^-),
\]

and for the selected ground-start evolution satisfies the exact identity

\[
\boxed{Q_{th}=U_{at}+E_\gamma\ge0},\qquad
\boxed{\Delta u_{th}+U_{at}+E_\gamma=0},\quad
\Delta u_{th}=-Q_{th}.
\]

For numerical stability when gross upward/downward events almost cancel, the primary thermal packet can use U_at+E_gamma. The raw event difference must still be retained and compared with an independently evaluated reference at a justified gross scale; conservation by output construction alone is not an independent physical test.

An initially excited population can return kinetic heat through collisional deexcitation, so the general thermal packet is not universally a cooling-positive object. The production ground-only contract avoids silently making claims about those unimplemented initial conditions.

At frozen T the quantity Delta u_th is an energy-exchange ledger. If T is literally held by a thermostat, external work supplies Q_th and the actual bath energy stays fixed. If later used as a gas update, rates must respond to the changed T. An exact frozen-coefficient substep is not an exact coupled thermal solution. A sufficient diagnostic for a prospective short frozen step is |Q_th|/(C_V T)<<1 together with small fractional rate variation, but no physical step-size certificate is issued without a bound on the rate history. CE changes no translational particle count, so in an ideal monatomic mixture C_V excludes atomic excitation energy and counts the fixed translational species; its actual value belongs to the consumer.

## 7. Coronal and transient reductions with quantitative conditions

Set eta_i=b_i/A_i=n_e/ncrit_i, ncrit_i=A_i/q_down,i. The selected star's stationary radiative emission rate per atom is

\[
j_i^R=A_i x_i^*=
\frac{a_i}{(1+\eta_i)(1+R_*)}.
\]

The coronal ground-reservoir reference is j_i^cor=a_i. Hence

\[
\frac{j_i^{cor}}{j_i^R}-1
=\eta_i+R_*+\eta_iR_*.
\]

This supplies a concrete conditional criterion for that reduction: require the right side <=epsilon for a relative error referenced to the exact stationary star emission. It separately exposes collisional quenching and ground depletion. It says nothing about unmodeled 2s↔2p mixing, cascades or actual line trapping; ncrit is the selected channel's deexcitation/radiation competition scale, not a complete physical critical density.

For the one-upper-level limit, Gamma=a+b+A, pi=a/Gamma and

\[
x(t)=pi(1-e^{-\Gamma t}),\quad
J(t)=pi\{t-h(\Gamma,t)\}.
\]

Instantaneous emission relative to its stationary value is 1-exp(-Gamma*t), whereas time-averaged emission relative to stationary is 1-phi1(-Gamma*t). Their deficits are exp(-Gamma*t) and phi1(-Gamma*t), respectively. Thus instantaneous equilibration at Gamma*t>=log(1/epsilon) does not by itself certify the average emitted energy at the same tolerance; Gamma*t>=1/epsilon is a sufficient average criterion.

For small t from ground,

\[
x_i=a_i t+O(t²),\quad
C_i^R=A_i a_i t²/2+O(t³),\quad
Q_{th}=\Delta(a_s+a_p)t+O(t²).
\]

This explicitly shows why immediate assignment of every excitation's Delta to an escaped photon is wrong during atomic buildup even in an optically thin cell. In a stationary coronal reduction atomic storage has already been eliminated, so the same assignment becomes an approximation with its own time-scale condition.

## 8. Reuse of new REC LINE01 and exact boundary

Read pinned REC PR128 LINE01 commit `6d32330e7f45e7caa9840c558547880b7d28a069`, files FROZEN_CONTRACT.md, THEORY.md and FORMULA_CODE_MAP.md under `research/rec_line_source_20261023/`. The intake agent verifies Git blob identities and MIT provenance.

Reusable result: a recoil-free bound-bound radiative event transfers energy from atomic internal excitation to radiation, with zero direct translational thermal/ionic/free-electron yield; a source needs exclusive ownership. Our CE event adds the missing translational thermal exchange and then follows the same atomic/radiation ledger logic.

The LINE01 effective source uses HyRec E=10.198714553953742eV, statistical fine-sublevel assumptions and a quasistationary Sobolev field. Its exact W0/log-root local map eliminates that radiation and contains population-dependent opacity. The present CCC-native Delta=10.20435eV, spontaneous optically thin star and explicit atomic buildup are distinct approximations. The LINE01 numerical map, saved27 map rows and36 source rows are not replayed or relabelled as our new source result. We reuse the conservation/owner construction and its pinned explanation; we do not silently transplant its gap or exact nonlinear map into this different closure.

An active native/LINE01 owner for the same radiative transition cannot simultaneously receive another full spontaneous source from this detached module. The production module remains detached; an actual coupled owner replacement requires an explicit future handoff.

## 9. Minimal falsification targets for C6/C7/C9

1. Compare one W-cell integral and sums against independently transformed quadrature; verify source reciprocity at raw forward/reverse knots with source rounding, not an invented near-machine-precision raw-data gate.
2. Check q_up/q_down against r exp(-Delta/theta), and independently check both analytic temperature derivatives at interior temperatures. Avoid dividing by underflowed rates.
3. Compare new frozen population and integrated-event values with independent high-precision expm or quadrature at selected novel dimensionless times, especially tiny-time buildup, stiff A_p/A_s separation, and almost-coincident roots if admitted.
4. Test t=0, n_e=0, collision-only formal limit if API supports it, and the single-upper-channel reduction. An unsupported formal zero-A input should be rejected rather than quietly advertised as tested.
5. Check number/charge and two independently formed heat packets, plus photon number2 for two-photon decay and energyDelta per event.
6. Falsify the wrong replacements: use independent reverse sigma-PL and detect balance drift; assign2Delta to a two-photon event and detect energy failure; assign emitted energy=excitation heat during initial buildup and detect the missing atomic store.
7. Read actual plots: rate reciprocity, gross/net/atomic/radiation energy, transient-to-stationary differences and physical-domain labels. A high-density formal curve must not visually suggest complete n=2 closure.

These are targets, not execution receipts. Parent freezes the finite case counts and acceptance before implementation/science. No repeated historical campaign, recursive review or source-owner mutation is required for this changed subproblem.

## 10. Status and next obligation

R4 candidate construction and R5 derivations above are complete for the selected finite model. Source-domain and approximate atomic-card admission belong to the parent/source synthesis; numerical and implementation verification remain pending until actual receipts exist. The old complete PHYS82 science stays reusable and unexecuted. The larger atomic thermal closure, He/Li CX, recombination-to-z20 initial charges, Li hard-UV, full spectral/geometry coupling and nuclear thermal/fast ownership remain OPEN.
