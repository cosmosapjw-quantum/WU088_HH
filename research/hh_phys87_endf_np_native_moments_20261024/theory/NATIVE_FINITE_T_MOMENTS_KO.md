# PHYS87 — ENDF 원래 관례의 유한 구간 사건 공급자

## 결과와 정확한 주장

입력은 NNDC ENDF/B-VIII.1의 n-001_H_001 원본이다. 원 평가의 0 K 표적-rest LAB 총 단면적, COM 비등방 광자 법칙, yield1 photon/recoil branch를 함께 보존한다. 이 문서는 common-T·zero-drift 고전 Jüttner 반응물에서 유한 원자료 구간의 반응률 계수와 같은 사건의 입자·에너지 moments를 계산하는 구성을 증명한다. 원자료 밖의 단면적, bare-nucleus 변환, 실제 불확실성 전파 및 coupled network 활성화는 별도 의무다.

이전 PHYS85의 사건 보존과 PHYS86의 reaction-selected energy/variable-composition caloric theorem은 재사용한다. 새 기여는 실제 MF3/MF6 공급자, 회전 평균에 의한 비등방 법칙의 scalar reduction, 유한 구간 1차원 계산과 source-native consumer guard다. 이것은 신규 보편 정리 또는 strong no-go 주장이 아니다.

## 1. 원전·질량·정의역

원본 SHA256은 3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af, 671232 bytes다. MF3/102는 153절점, 처음33절점까지 INT5 log-log, 나머지는 INT2 lin-lin이다. MF6/102는 LCT2, photon LAW2/LANG0/NL2와 recoil LAW4, 각각 yield1이다. 각계수는 LAB 에너지에 대해 lin-lin 보간한다. 원 MF1의 332.0mb 서술로 .0253eV knot의 .3325842b를 다시 정규화하지 않는다.

ENDF-102(2023) §0.5.1.1, §3.3.2와 Appendix E.21을 적용한다. AWR은 atomic target mass convention이고 residual mass는 QI로 도출한다. 이번 구현은 절대 질량 기준으로 부모의 표시된 neutron energy \(\epsilon_n=939565421.94\)eV를 **명시적으로 선택**한다:
\[
\epsilon_H=0.9991673\,\epsilon_n,\quad Q=2224648\ {\rm eV},\quad
M=\epsilon_n+\epsilon_H,\quad \epsilon_D=M-Q.
\]
이는 ENDF가 CODATA2022를 사용했다는 주장이 아니다. Parent bare \(n,p,d\) 질량은 바꾸지 않는다. 그 합차 \(Q_{\rm bare}=2224566.37\)eV와 차81.63eV는 원 convention 차이 기록이며 uncertainty interval이 아니다. Photon AWP=2223300eV는 primary photon metadata로 남긴다. Exact event energy는 Appendix E kinematics로 계산하며 AWP를 별도 독립 energy deposit으로 더하지 않는다. Light-product AWP를 atomic target와 혼합하여 Q를 재구성하지 않는다.

원 LAB projectile energy \(E\)와 invariant pair energy:
\[
W=\sqrt{M^2+2\epsilon_HE},\quad
K=W-M={2\epsilon_HE\over W+M},\quad
E={K(2M+K)\over2\epsilon_H}.
\]
정의역 \(10^{-5}\le E\le2\cdot10^7\)eV는 고정이며 T에 따라 움직이지 않는다. 이것은 kinematic conversion이며 arbitrary source-energy rescaling이 아니다. Source-native atomic-equivalent target/residual은 free electron pool과 다르다. Source 안의 electron은 internal이고 자유 전자 incidence는0이다. Isotope/nucleon count는 \(n+{}^1H\to{}^2H+\gamma\)로 보존한다. Bare-network request는 명시적으로 거부한다.

## 2. 실제 각분포와 conditional boost moments

ENDF §6.2.4 Eq6.8을 따라 incoming neutron COM unit vector를 \(u\), photon unit vector를 \(n\), \(\mu=u\cdot n\)라 두면
\[
f(\mu|E)={1\over2}[1+3a_1(E)\mu+5a_2(E)P_2(\mu)],
\quad {d\sigma\over d\Omega_*}={\sigma(E)\over2\pi}f(\mu|E).
\]
\(\int_{-1}^1 f\,d\mu=1\), \(\langle n\rangle=a_1u\),
\[
\langle n_i n_j\rangle={1-a_2\over3}\delta_{ij}+a_2u_i u_j.
\]
이는 Legendre 직교성과 azimuth uniformity에서 직접 따른다. Boost 방향 \(b\), \(\eta=u\cdot b\), \(\nu=n\cdot b\)에 대해
\[
\langle\nu\rangle=a_1\eta,\qquad
\langle\nu^2\rangle={1-a_2+3a_2\eta^2\over3}.
\]
원래 비등방성을 등방 source로 바꾸지 않는다.

\(q=Q+K,\ e_*=q(2W-q)/(2W),\ k_{D*}=q^2/(2W),\
E_{D*}=\epsilon_D+k_{D*}=W-e_*\)라 두면
\[
E_\gamma=\gamma e_*(1+\beta\nu),\quad
K_D=k_{D*}+(\gamma-1)E_{D*}-\gamma\beta e_*\nu,\quad
K_{\rm in}=K+W(\gamma-1).
\]
따라서
\[
\langle E_\gamma\rangle=\gamma e_*(1+\beta a_1\eta),\quad
\operatorname{Var}(E_\gamma)=(\gamma\beta e_*)^2
\left[{1-a_2+3a_2\eta^2\over3}-a_1^2\eta^2\right],
\]
\(\langle K_D\rangle=K_{\rm in}+Q-\langle E_\gamma\rangle\)다.
모든 방향에서 \(K_{\rm in}+Q=K_D+E_\gamma\)이므로 동일 measure의 평균에서도 정확히 성립한다.

각 에너지 knot의 quadratic \(f=A\mu^2+B\mu+C\) 양성성은 \(\mu=\pm1\) 및 \(A>0\)이고 \(-B/(2A)\in[-1,1]\)일 때 그 vertex에서 exact rational로 판정한다. 인접 에너지에서는 source lin-lin 계수 보간이 두 양의 다항식의 convex combination이므로 전 구간 양성성이 따른다. 이 represented-law 논증은 sampled angular residual과 구별한다.

## 3. Common-T ensemble의 회전 평균

PHYS86 식(5)-(6)의 같은 normal-frame flux를 쓴다:
\[
\bar v=c{\sqrt{D^2-\epsilon_n^2\epsilon_H^2}\over E_nE_H},
\quad D=E_nE_H-c^2p_n\cdot p_H,\quad
f_if_j\propto e^{-(E_n+E_H)/\theta},\quad\theta=k_BT.
\]
\(d^3p_n d^3p_H/(E_nE_H)\)는 invariant two-body measure다. Total four-momentum \(P\)와 W를 고정하면 pair relative COM solid angle의 Jacobian, flux와 총 \(\sigma(W)\)는 방향에 의존하지 않는다. Common-T Boltzmann factor도 \(e^{-P^0c/\theta}=e^{-\gamma W/\theta}\)뿐이다. 따라서 fixed \(W,P\)에서 incoming COM axis \(u\)는 uniform이다. 서로 다른 mass도 이 조건을 바꾸지 않는다.

모든 fixed \(n\)에 대해
\[
\int {d\Omega_u\over4\pi}\,{f(u\cdot n|E)\over2\pi}={1\over4\pi}.
\]
직교성 또는 \(\langle u_i\rangle=0,\langle u_iu_j\rangle=\delta_{ij}/3\)으로 확인한다. Hence absolute photon direction is uniform **after** the actual incoming-axis average. No drift/unequal-T/external alignment or state-dependent angular selection can be inserted into this reduction without rederiving the weight. Directed source law is still used by the conditional API.

## 4. 1차원 invariant rate와 boost 적분

\[
\lambda(W)=[W^2-M^2][W^2-(\epsilon_n-\epsilon_H)^2]
=K(2M+K)(4\epsilon_n\epsilon_H+2MK+K^2).
\]
PHYS86의 정규화 \(Z_i=4\pi\epsilon_i^2\theta K_2(\epsilon_i/\theta)\)를 energy-momentum \(cp\) 변수로 쓰면 상쇄되는 c powers가 분명해진다. 두 입자 invariant phase space를 total \(P\)와 W로 바꾸고 total spatial momentum을 적분하면
\[
\kappa_{\cal D}(T)={c\over4\epsilon_n^2\epsilon_H^2\theta
 K_2(\epsilon_n/\theta)K_2(\epsilon_H/\theta)}
\int_{K_{\min}}^{K_{\max}}\sigma(E(K))\lambda(M+K)K_1((M+K)/\theta)\,dK.
\tag{1}
\]
\(\sigma\)를 cm², c를 cm/s, energies를 eV로 통일하면 cm³/s다. n,H는 다른 species이므로 rate는 \(R=n_n n_H\kappa_{\cal D}\), symmetry factor1이다. 본 작업은 density 또는 실제 R을 정하지 않는다.

Fixed W boost law는 total phase-space radial factor
\(d^3P/P^0\propto\sqrt{\gamma^2-1}d\gamma\)와 Boltzmann factor에서
\[
dP(\gamma|W)={\sqrt{\gamma^2-1}e^{-z\gamma}\over K_1(z)/z}\,d\gamma,\quad z=W/\theta.
\]
Known Bessel integral representation을 미분하여
\[
G=\langle\gamma\rangle={K_2(z)\over K_1(z)},\quad
G_2=\langle\gamma^2\rangle=1+{3G\over z}.
\tag{2}
\]
예를 들어 \(I=K_1/z\), \(-I'=K_0/z+2K_1/z^2=K_2/z\)를 \(I\)로 나눈다. \(I''/I=1+3K_0/(zK_1)+6/z^2\)는 (2)와 동일하다. 원자료 조건부 angular 평균과 uniform incoming-axis 평균을 먼저 시행한 뒤
\[
m_K(K)=K+W(G-1),\quad m_\gamma(K)=e_*G,\quad
m_D(K)=k_{D*}+E_{D*}(G-1).
\tag{3}
\]
\[
v_\gamma(K)=e_*^2[(G_2-G^2)+G/z],\quad
v_K(K)=W^2(G_2-G^2).
\tag{4}
\]
The event average uses the same positive normalized integrand of (1) for every quantity. Total variance uses \(\langle v(K)+(m(K)-\langle m\rangle)^2\rangle\), avoiding subtraction of large nearly equal raw second moments.

## 5. 입자·에너지 owner와 온도 source

Fixed h=0/1 and one radiation route have particle columns
\(\Delta N_{\rm thermal}=h-2,\ \Delta N_{\rm fast}=1-h,\ \Delta N_e=0\).
The six disjoint energy columns are
\[
(h\langle K_D\rangle-\langle K_{\rm in}\rangle,\ 
(1-h)\langle K_D\rangle,\ -Q,\ 0,\ 
\langle E_\gamma\rangle_{\rm handoff},\
\langle E_\gamma\rangle_{\rm escape}).
\]
They sum to0. Only one radiation route owns the photon. h=1 is the stated instantaneous caloric-birth closure; h=0 keeps the residual kinetic energy fast. No Q-as-heat deposit is added.

PHYS86 gives \(u_i=\epsilon_i(K_1/K_2-1)+3\theta\), and for this T-independent fixed-domain source
\[
\theta\,{d\log\kappa_{\cal D}\over d\log T}
=\langle K_{\rm in}\rangle-u_n-u_H.
\]
Consequently the returned caloric forcing, in eV/event, is
\[
{C_V\dot T\over R}=-\langle K_{\rm in}\rangle+u_n+u_H
+h(\langle K_D\rangle-u_D).
\tag{5}
\]
C_V and R remain caller-owned and unassigned. Fixed native source-window selection is essential for this derivative identity; a T-dependent window would require boundary terms. The moment source is not a coupled T/xe history or stopping proof.

## 6. 수치 표현과 한계

Equation(1) uses scaled \(K_\nu^e=e^zK_\nu\):
\(K_1(W/\theta)/(K_{2,n}K_{2,H})=
e^{-K/\theta}K_1^e(W/\theta)/(K_{2,n}^eK_{2,H}^e)\).
Log-E integration has \(dK/d\log E=\epsilon_HE/W\).
All152 native source cells are retained. Positive Gauss-Legendre16/32 provides a frozen finite comparison, not an interval or continuum certificate. Very small exp(-K/theta) terms may underflow; count this explicitly and make no exact-tail-zero claim.

The numerical input guard is 255<=T<=101000000K, including the frozen finite-difference satellites, with finite species/pair z>=1e5. The four temperatures are primary sample points; this guard is not uniform accuracy evidence or an atomic population-equilibrium claim. For selected four temperatures z>=1e5. The large-z expansion is
\[
K_\nu^e(z)\sim\sqrt{\pi/(2z)}
\sum_{j=0}^{6}{\prod_{k=1}^j[4\nu^2-(2k-1)^2]\over j!\,8^j}\,z^{-j}.
\]
Call the polynomial \(P_\nu(t)\), t=1/z. Compute \(G-1=(P_2-P_1)/P_1\) and \(K_1/K_2-1=(P_1-P_2)/P_2\) from exact coefficient differences. Compute
\[
G_2-G^2={P_1^2+3tP_2P_1-P_2^2\over P_1^2}
\]
after cancelling coefficient terms in rational arithmetic, before evaluating in binary64. This prevents the small heat/variance signal from being lost between O(1) terms. The asymptotic truncation is explicitly tested at the frozen domain and is not a general Bessel routine or rigorous physical uncertainty bound.

Independent comparison uses actual SciPy scaled Bessels and adaptive quadrature at T1e8K, with a separate raw ENDF parser. The same new primary contains a finite-difference rate-slope control at T1e4 and1e8 and conditional angular-moment checks. No unchanged PHYS85/86 reference is replayed. Exact counts and costs belong to the execution ledger.

## 원전과 기존 근거

- [NNDC canonical ENDF](https://www.nndc.bnl.gov/endf-data/ENDF/ENDF-B-VIII.1/n-001_H_001.endf), MF1/3/6/33.
- [ENDF-102 (2023)](https://www.nndc.bnl.gov/endfdocs/ENDF-102-2023.pdf): §0.5.1.1 p24; §3.3.2 p105; §6.2.4 pp142–144; §6.3.2 pp152–153; Appendix E pp381–383.
- Cannoni, arXiv:1506.07475, invariant relative flux and unequal-mass thermal average, as pinned in PHYS86.
- PHYS85 FROZEN_INPUTS and ownership proof; PHYS86 JUTTNER_REACTION_MOMENTS_KO.md and completed identity270d5987… reused.

## 다음 gate

This child supplies finite-window source-native evaluated moments. Atomic-to-bare mass/charge-state remap, full source-support tails, covariance/angular uncertainty, density/population validity, actual thermal/fast consumer and photon escape/reabsorption remain distinct obligations. Recombination initial charge, Li source uncertainty/inner-shell, He–Li CX, D PI/RR and full spectral geometry keep their prior OPEN statuses. HH_R10=OFF; production NOT_ISSUED.

