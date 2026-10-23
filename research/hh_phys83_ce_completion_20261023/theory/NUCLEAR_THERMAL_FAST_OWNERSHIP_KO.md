# PHYS83 연결: thermal/fast 핵 입자 소유권과 유한-T 사건 평균

## 1. 판정·부모 입력

`NUCLEAR_THERMAL_FAST_PARTICLE_OWNERSHIP`의 구성적 이론 계약을 아래처럼 정한다. PHYS81의 bare ground-state `n+p→d+γ`, `n+d→t+γ`, `p+d→h+γ`를 그대로 쓰며, 새로 태어난 daughter는 **별도 fast population**으로 먼저 소유한다. thermal bath로 들어오는 입자수는 후속 stopping/assimilation의 별도 number flux가 정한다. 이 선택은 입력 분포, microscopic nuclear rates, stopping power 또는 우주론적 ODE를 공급하지 않는다. 이번 산출물은 이들 공급자가 따라야 할 에너지·입자수·frame 및 유한-T averaging 계약이다.

직접 읽어 재사용한 PHYS81 파일은 다음과 같다. 완료된 mass/COM 계산을 호출하거나 재실행하지 않았다.

| 부모 파일 | bytes | SHA256 |
|---|---:|---|
| `theory/NUCLEAR_RECOIL_THEORY_KO.md` | 16211 | `566b5cb4f2b704e9553d5aa558372599d65ffe9dcf9dda90ab28ae1cb09eba18` |
| `source/nuclear_recoil.py` | 14385 | `e8b7ad216113932d0844e424ca6e5e17dd644e07ca883e463c0c6c325c4fcf0e` |
| `source_data/NUCLEAR_MASSES_CODATA2022.json` | 5423 | `ee87900f698e59029a1aafce3d4184870ccc6fa16a8ba50326bd13a10de60aaf` |

부모 경로는 `research/hh_phys81_atomic_nuclear_source_contract_20261023/`이며, 부모 source SHA는 코드의 `SOURCE_SHA256`과 일치한다. mass-energy column은 반올림된 CODATA 2022 추천값이다. 전체 mass covariance는 여전히 미공급이며 여기서 physical uncertainty를 생성하지 않는다.

공간은 non-tilted LRS Bianchi I, signature는 `(-,+,+,+)`다. 모든 아래 에너지는 하나의 normal orthonormal frame에서 정의한다. reacting thermal gas의 `π=0`은 유지한다. fast nuclei와 collisionless DM의 tensor는 thermal gas EOS에 합쳐 넣지 않는다. 도출 상태는 **derived**, CAS 검산은 **symbolically checked**이며 runtime production adapter는 부모의 후속 coding adoption 여부로 따로 기록한다.

## 2. COM 사건을 같은 normal frame으로 옮기는 정확한 식

질량의 rest energy를 \(A=m_ac^2\), \(B=m_bc^2\), \(C=m_cc^2\), \(C_i=A+B\), \(Q=C_i-C>0\)라 한다. \(p^{\hat0}=\epsilon/c\)이고 incoming normal-frame 에너지·운동량으로

\[
 W=\sqrt{(\epsilon_a+\epsilon_b)^2-c^2|\mathbf p_a+\mathbf p_b|^2},\quad
 \Gamma=\frac{\epsilon_a+\epsilon_b}{W},\quad
 \boldsymbol\beta=\frac{c(\mathbf p_a+\mathbf p_b)}{\epsilon_a+\epsilon_b}
\]

를 정한다. \(W\)는 에너지이며 \(\Gamma^2(1-\beta^2)=1\)이다. incoming pair의 정확한 COM kinetic energy는 \(E_*=W-C_i\ge0\)다. PHYS81의 `incident_com_kinetic_MeV`가 바로 이 변수이며, 온도에서 임의로 넣는 평균에너지가 아니다.

COM에서 \(\Delta=Q+E_*=W-C\)라 쓰면 부모와 동일한

\[
 e_\gamma^*=\Delta\left(1-\frac{\Delta}{2W}\right),\qquad
 K_c^*=\frac{\Delta^2}{2W},\qquad
 \epsilon_c^*=C+K_c^*=\frac{W^2+C^2}{2W}
\tag{1}
\]

를 얻는다. COM photon 방향을 \(\widehat{\mathbf k}_*\), \(b=\boldsymbol\beta\cdot\widehat{\mathbf k}_*\)라 할 때 inverse boost는

\[
 E_\gamma=\Gamma e_\gamma^*(1+b),\qquad
 K_c=\Gamma(\epsilon_c^*-b e_\gamma^*)-C,
\tag{2}
\]

이며 incoming kinetic debit은

\[
 K_{\rm in}=\epsilon_a+\epsilon_b-C_i
 =\Gamma W-C_i=E_*+(\Gamma-1)W.
\tag{3}
\]

따라서 각 사건에서

\[
 \boxed{E_\gamma+K_c-K_{\rm in}-Q=0.}
\tag{4}
\]

이 식은 outgoing emission을 isotropic으로 가정하지 않는다. \(\beta=0\)이면 부모 COM식으로, 이어 \(E_*=0\)이면 cold COM식으로 환원된다. 부모의 `partition_event`에 normal-frame 운동에너지를 그대로 넣는 대신 (2)–(3)의 adapter가 필요하다.

정밀 계산은 \(e_\gamma^*\)에 (1)의 factored form을 쓰고, 작은 \(K_c\)는 boost한 \(\mathbf p_c\)로
\(K_c=c^2|\mathbf p_c|^2/(\epsilon_c+C)\)를 계산할 수 있다. \(K_c\)를 에너지 closure의 나머지로 정의한 뒤 그 동일 closure를 독립 검증이라고 부르지 않는다. 실제 reference implementation은 출력 momentum의 mass shell도 따로 확인해야 한다.

[PDG Kinematics](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-kinematics.pdf), §§49.1–49.2 및 Eqs. (49.16)–(49.17)의 boost와 two-body 식을 읽고 위 식으로 단위와 signature를 옮겼다. PDG는 \(c=1\), 반대 invariant-sign 표기를 쓰므로 여기서는 \(W^2=-c^2P^2\)로 표현했다. 식 (1)–(4)의 현재 channel 연결은 직접 유도했다.

## 3. 소유권: 에너지 분율과 bath 입자수를 분리한다

두 incoming nuclei는 thermal bath에 속하며 새 daughter가 fast에 속하는 선택에서 사건당 장부는 다음과 같다.

| 장부 | capture into fast |
|---|---:|
| thermal reactant counts | \(-1_a-1_b\) |
| fast daughter count | \(+1_c\) |
| thermal particle count, electron 포함 | \(-2\) |
| total nuclear particle count | \(-1\) |
| free-electron count | \(0\) |
| thermal kinetic energy | \(-K_{\rm in}\) |
| fast kinetic energy | \(+K_c\) |
| emitted photon energy | \(+E_\gamma\) |
| total nuclear rest energy | \(-Q\) |

동일 reactant라면 같은 종에서 두 입자를 제거해야 한다. 현재 세 채널의 reactants는 서로 다르지만 generic rate API에서는 \(1/(1+\delta_{ab})\)를 유지한다. 부모의 baryon/charge stoichiometry는 thermal+fast 합에서 그대로 보존된다. nuclear charge는 pool 사이에서 이동하며 세 radiative-capture 채널의 free-electron count는 변하지 않는다.

부모 \(\zeta\)는 energy fraction이다. 이것으로 thermal daughter count를 정하지 않는다. 본 선택에서는 capture 직후 \(\zeta=0\)인 literal fast-population 소유권으로 접속하고, 이후 실제 stopping provider가 공급한 에너지 전달만 thermal source로 옮긴다. 별도 excess-energy moment model을 채택할 경우 그 EOS를 다른 계약으로 명시해야 한다.

빠른 입자가 연속적으로 감속할 때 thermal heat \(\mathcal H\)와 fast energy loss \(-\mathcal H\)를 같이 기록하며, 감속만으로 bath particle 수를 늘리지 않는다. fast→thermal assimilation number flux \(J_c\)가 발생하면

\[
 S_{n_c^{\rm th}}=+J_c,\quad S_{n_c^F}=-J_c,\qquad
 \mathcal Q_{\rm th}^{\rm match}=+J_c\langle K_{\rm match}\rangle,
 \quad\mathcal Q_F^{\rm match}=-J_c\langle K_{\rm match}\rangle.
\tag{5}
\]

마지막 residual kinetic energy는 같은 flux로 한 번만 넘긴다. cutoff까지 잃은 energy와 residual energy를 중복 계산하지 않는다. assimilation 순간에 임의의 \(3k_BT/2\)를 만들어 넣는 대신 실제 transferred energy와 새 \(n_{\rm th}\)로 EOS의 온도를 갱신한다.

비교용 prompt-thermal closure는 daughter를 즉시 bath에 넣어 \(\Delta N_{\rm th}=-1\), \(\Delta U_{\rm th}=K_c-K_{\rm in}=Q-E_\gamma\), \(\Delta N_F=\Delta U_F=0\)로 정의한다. 이것은 선택된 fast-first closure와 다른 물리적 thermalization 가정이다. 두 경로의 입자수·에너지원 열을 섞지 않는다.

## 4. 유한 온도: 반응률과 사건 평균을 같은 measure로 묶는다

일반적인 공급된 phase-space/event measure를 \(d\mathcal R\ge0\), 그 총합을 \(\mathcal R=\int d\mathcal R\)라 쓴다. \(\mathcal R>0\)에서

\[
 \langle F\rangle_{\rm rxn}=\mathcal R^{-1}\int F\,d\mathcal R
\tag{6}
\]

다. 각 event의 energies와 모든 number/energy source는 동일한 normalized weights를 쓴다. \(\mathcal R=0\)이면 모든 source는 0이고 conditional event mean은 undefined/null이다. 이를 물리적 평균 0으로 저장하지 않는다.

식 (2)의 scalar sources는 세 공급 moment

\[
 \mathsf A=\langle\Gamma W\rangle_{\rm rxn},\quad
 \mathsf B=\langle\Gamma/W\rangle_{\rm rxn},\quad
 \mathsf D=\langle\Gamma e_\gamma^* b\rangle_{\rm rxn}
\tag{7}
\]

로 정리된다. \(\mathsf A,\mathsf D\)는 에너지, \(\mathsf B\)는 inverse energy다.

\[
 \boxed{
 \begin{aligned}
 \langle E_\gamma\rangle&=\tfrac12(\mathsf A-C^2\mathsf B)+\mathsf D,\\
 \langle K_c\rangle&=\tfrac12(\mathsf A+C^2\mathsf B)-\mathsf D-C,\\
 \langle K_{\rm in}\rangle&=\mathsf A-C_i.
 \end{aligned}}
\tag{8}
\]

식 (8)의 에너지합은 어떤 허용 event measure에서도 (4)를 보존한다. 단일 thermal rate나 단일 평균 incoming energy만으로 \(\mathsf B,\mathsf D\)가 정해지지는 않는다. conditional isotropic emission이면 각 \(W,\beta\)에서 angular mean \(\mathsf D\)의 integrand가 0이다. 아래의 isotropic equal-T nonrelativistic pair 분해에서는 CM 방향과 상대운동이 독립이므로, emission kernel이 CM 방향에 독립이고 상대방향으로만 회전 공변할 때 ensemble \(\mathsf D=0\)도 얻을 수 있다. 다른 분포에는 공급한 angular kernel을 그대로 적분한다.

이 분해는 정확한 event algebra의 계산식이다. floating-point 구현은 큰 \(\mathsf A-C^2\mathsf B\)의 상쇄를 피하도록 (1)–(3)의 positive/factored event quantities를 평균해도 된다. 별도로 계산한 source들의 conservation residual을 보존한다. sampled quadrature residual은 그 sample의 검사 결과다.

### 4.1 Equal-T Maxwellian incoming moment

모든 reactant가 같은 \(T\)의 비퇴화·무편류 Maxwellian이며 nonrelativistic incoming kinetics를 채택하는 범위에서 \(M=m_a+m_b\), \(\mu=m_am_b/M\),
\(\mathbf V=(m_a\mathbf v_a+m_b\mathbf v_b)/M\), \(\mathbf g=\mathbf v_a-\mathbf v_b\)라 둔다. 그러면

\[
 \frac12m_av_a^2+\frac12m_bv_b^2
 =\frac12MV^2+\frac12\mu g^2,
\tag{9}
\]

이며 joint Maxwellian은 \(\mathbf V,\mathbf g\)에 대해 인수분해된다. \(E=\mu g^2/2\), \(\tau=k_BT\), channel-specific cross section \(\sigma(E)\)에 대해

\[
 K(T)=\langle\sigma g\rangle=
 \sqrt{\frac8{\pi\mu}}\tau^{-3/2}
 \int_0^\infty E\sigma(E)e^{-E/\tau}\,dE,\qquad
 \mathcal R=\frac{n_a^{\rm th}n_b^{\rm th}}{1+\delta_{ab}}K(T).
\tag{10}
\]

\(K\)의 차원은 volume/time이며, \(N_AK\)로 제공되는 molar rate는 \(N_A\)를 나누어야 한다. 모든 energy/mass 단위는 같은 SI 또는 cgs 체계로 변환한 뒤 prefactor를 적용한다.

반응이 선택한 relative energy는

\[
 \overline E_{\rm rxn}=
 \frac{\int E^2\sigma(E)e^{-E/\tau}\,dE}
 {\int E\sigma(E)e^{-E/\tau}\,dE}
 =k_BT\left(\frac32+\frac{d\ln K}{d\ln T}\right),
\tag{11}
\]

이며 \(\sigma\)가 \(T\)에 명시적으로 의존하지 않고 적분·미분 교환이 허용될 때 오른쪽 equality가 성립한다. screening/상태 population 등이 \(T\) 의존이면 그 explicit derivative를 분리해야 한다. CM motion은 반응선택에 바뀌지 않아 \(\langle MV^2/2\rangle=3k_BT/2\)이며

\[
 \boxed{\langle K_{\rm in}\rangle_{\rm NR,rxn}
 =\frac32 k_BT+\overline E_{\rm rxn}
 =k_BT\left(3+\frac{d\ln K}{d\ln T}\right).}
\tag{12}
\]

이는 nonrelativistic Maxwellian model에서의 식이다. 정확한 상대론적 phase-space measure와 (10)을 같은 계산으로 간주하지 않는다. exact event layer (1)–(8)와 asymptotic incoming-statistics layer (9)–(12)의 approximation tags를 별도로 유지한다. 유효범위는 \(k_BT\), 반응선택 incoming kinetic scale이 각 reactant rest energy에 비해 작아 nonrelativistic kinematics가 적절한 구간이다. 고에너지 tail의 기여는 source와 weight를 통해 확인해야 한다.

[Longland et al. (2010), Eq. (1)](https://arxiv.org/pdf/1004.4136)은 Maxwellian nuclear rate의 원전 기준으로 읽었다. [Warshaw, LLNL UCRL-ID-144510 (2001), §§2–3](https://nuclear.llnl.gov/CNP/tdf/tdf.htm)은 reaction-selected average, CM/relative 분리 및 rate slope와 relative moment의 관계를 명시한다. 이 문헌의 nonrelativistic massive-final-state 분할식을 photon에 사용하지 않고 입력 평균 논리만 재사용한다. 식 (9)–(12)는 직접 유도하고 CAS로 대조했다.

## 5. thermal number와 온도 source의 결합

thermal bath에 실제로 속한 nuclei와 electrons만 \(n_{\rm th}\)에 센다. \(u_{\rm th}=3n_{\rm th}k_BT/2\), \(p_{\rm th}=n_{\rm th}k_BT\), \(\Theta=3H\),

\[
 \dot n_{\rm th}+\Theta n_{\rm th}=S_{n_{\rm th}},\qquad
 \dot u_{\rm th}+\Theta(u_{\rm th}+p_{\rm th})=\mathcal Q_{\rm th}
\]

로부터

\[
 \boxed{\frac32 n_{\rm th}k_B\dot T
 =-n_{\rm th}k_BT\Theta+\mathcal Q_{\rm th}
 -\frac32 k_BT S_{n_{\rm th}}.}
\tag{13}
\]

이는 부모 EOS chain rule의 bath-membership을 명확히 한 것이다. fast-first capture만 있을 때 \(S_{n_{\rm th}}=-2\mathcal R\), \(\mathcal Q_{\rm th}=-\mathcal R\langle K_{\rm in}\rangle\)이므로

\[
 \left.\dot T\right|_{\rm cap\to fast}
 =\frac{\mathcal R}{n_{\rm th}}
 \left[2T-\frac{2\langle K_{\rm in}\rangle}{3k_B}\right].
\tag{14}
\]

(12)를 넣으면

\[
 \left.\dot T\right|_{\rm cap\to fast,NR}
 =-\frac{2T\mathcal R}{3n_{\rm th}}\frac{d\ln K}{d\ln T}.
\tag{15}
\]

이것은 actual nuclear rate를 계산한 결과가 아니라 명시된 sampling/ownership 하의 조건부 유도다. 예를 들어 합성 \(\sigma(E)=\sigma_0E^s\), \(s>-2\)에서

\[
 K=\sqrt{8/(\pi\mu)}\,\sigma_0\Gamma(s+2)(k_BT)^{s+1/2},\quad
 \overline E=(s+2)k_BT,
\]

따라서 \(\sigma v\)가 상수인 \(s=-1/2\)에서는 무작위 particle removal이 온도를 바꾸지 않는다. 상수 cross section \(s=0\)에서는 반응선택이 빠른 입자를 선호해 \(\dot T=-T\mathcal R/(3n_{\rm th})\)다. 핵반응 energy release의 이후 stopping heat는 별도 항으로 남는다.

## 6. fast stress와 radiation ledger의 후속 계약

fast distribution \(f_c(\mathbf p)\)를 number density per momentum volume로 정하면
\(u_F=\int(\epsilon_c-C)f_c\,d^3p\),
\(P^F_{ij}=\int c^2p_ip_j\epsilon_c^{-1}f_c\,d^3p\)다.
이 분포를 thermal bath heat capacity에도 세지 않는다. 단일 사건의 방향성·운동량과 그 후 Bianchi expansion에 의한 fast tensor evolution은 해당 공급자가 보존해야 한다. isotropic reacting gas의 \(\pi=0\)에서 fast 또는 DM의 \(\pi\)가 0이라는 결론은 나오지 않는다.

이 단원의 emitted-photon source는 emission 시점의 같은 normal-frame energy다. 실제 radiation density에는 redshift/work/transport가 추가된다. total diagnostic은 같은 normal frame의 signed matter/radiation tensors를 먼저 합하고 norm을 계산한다. 기존 `Frobenius=sqrt(2)*half-contraction` convention을 유지한다.

## 7. 실제 검산·코딩 계약·다음 의무

Wolfram context 호출 1회, evaluator 성공 2회에서 **10 symbolic residual이 모두 0**이다. 첫 호출은 event energy, product mass shell, pair factorization, power-law event mean, rate-derivative identity, EOS chain rule의 6개를 검산했다. 둘째는 3-moment energy closure, fast ledger, prompt-thermal ledger, internal transfer의 4개다. 원문 code와 tool receipt는 `ownership_checks.wl`, `wolfram_symbolic_receipt.json`, `wolfram_moment_receipt.json`에 보존했다. 이는 새 symbolic verification이며 PHYS81/82 완료 identity 실행이 아니다. nuclear rate 실행, nuclear ODE, stopping 실행은 각각 0이다.

기계 계약은 `NUCLEAR_OWNERSHIP_CONTRACT.json`에 있다. 최소 후속 구현은 parent COM kinematics를 보존하는 normal-frame event adapter, mutually exclusive pool counts, supplied positive event-weight average, rate/number/energy source assembler다. admission 검사는 같은 frame, masses/source identity, weighted normalization, number/baryon/charge closure, independent mass shell, positivity, zero-rate conditional-mean 처리와 unit consistency를 포함한다.

실제 nuclear source 활성화에 남은 입력은 channel-specific differential/total cross sections와 지원 energy/temperature 범위, event distribution와 angular measure, thermal/fast matching 및 stopping provider, radiation transport, 공통 mass covariance다. 본 단원은 **ownership/frame/finite-T averaging의 algebraic prerequisite를 닫고** 이 공급자들을 명확한 입력으로 넘긴다. rates/stopping/ODE는 미활성화 상태다. `HH_R10=OFF`, `Production admission NOT_ISSUED`를 유지한다.
