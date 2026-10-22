# PHYS81: 세 cold-COM 방사포획의 광자·반동 분할과 핵 입자수 온도항

## 0. 판정과 실제 수행 범위

**원전 질량 입력과 cold-COM 단일 광자 사건의 에너지 분할은 이론적으로 닫혔다.**
반응률, 유한 온도 반응물의 선택 운동에너지, 반동 stopping과 bath 편입, 방사 수송 및 우주론적 활성화는 이번 결과에 포함되지 않는다.

대상은 fully stripped ground-state 채널

\[
 n+p\to d+\gamma,\qquad n+d\to t+\gamma,\qquad p+d\to h+\gamma,
\]

이며 \(h\)는 \(^3\mathrm{He}^{2+}\) helion이다. 상대속도 0의 COM 한계에서 하나의 광자와 하나의 최종 핵만 존재하는 사건을 조건부로 다룬다. 이 조건부 운동학은 정확히 상대속도 0인 물질에서 유한 반응률이 있다는 주장이 아니다.

사용한 workflow는 physmath-research-loop **1.3.0**이다. 부모가 위임한 R2 원전·중복 조사, R5 독립 유도, R6 부호·단위·범위 검토에 한정했다. 부모와 별도 native child에서 수행했지만 같은 모델 계열의 별도 문맥 검토다. 추가 reviewer tree를 만들지 않았다. 계산 코드·CAS·수치 대입·ODE·반응률 실행·원격 쓰기는 하지 않았다. 도구로 수행한 것은 문헌/기존 파일 읽기와 증거 문서의 저장·해시뿐이다.

## 1. 원전과 고정할 질량 표

2022 CODATA의 [NIST 공식 complete listing](https://physics.nist.gov/cuu/Constants/Table/allascii.txt)을 실제 읽었다. 아래는 그 표의 값과 standard uncertainty를 그대로 옮긴 것이다. 괄호 없는 uncertainty 열을 별도로 보존했다. 모두 중성 원자가 아닌 **bare nuclear masses**다.

| 핵 | 질량 kg | 표준불확도 kg | \(mc^2\), MeV | 표준불확도 MeV |
|---|---:|---:|---:|---:|
| proton | 1.67262192595e−27 | 0.00000000052e−27 | 938.27208943 | 0.00000029 |
| neutron | 1.67492750056e−27 | 0.00000000085e−27 | 939.56542194 | 0.00000048 |
| deuteron | 3.3435837768e−27 | 0.0000000010e−27 | 1875.61294500 | 0.00000058 |
| triton | 5.0073567512e−27 | 0.0000000016e−27 | 2808.92113668 | 0.00000088 |
| helion | 5.0064127862e−27 | 0.0000000016e−27 | 2808.39161112 | 0.00000088 |

기계 판독 원전 표와 URL은 `SOURCE_PINNED_MASSES.json`이다. 유도 상수는
\(c=299792458\ \mathrm{m\,s^{-1}}\),
\(k_B=1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}\),
\(1\,\mathrm{eV}=1.602176634\times10^{-19}\,\mathrm J\)이며 SI에서 exact다.

[Mohr et al., Rev. Mod. Phys. 97, 025002 (2025), DOI 10.1103/RevModPhys.97.025002](https://physics.nist.gov/cuu/pdf/RevModPhys.97.025002.pdf)의 Sec. II.B, 인쇄 페이지 6은 거의 정지한 n+p 포획에서 deuteron recoil을 포함한 상대론적 에너지·운동량 보존을 직접 설명한다. Eq. (6)은 이를 CODATA 조정상수로 표현한 식이다. Sec. II.C는 p,d,t,h 질량의 cyclotron-frequency ratio 근거를 설명한다. 이 자료는 운동학의 원전 대조에 사용한다. neutron mass 자체가 포획 광자 측정에 연결되므로 이 질량 표에서 다시 만든 n+p 광자 에너지를 **독립된 새 실험 검증**으로 부르지 않는다.

입력 오차에는 상관이 있다. 다섯 질량의 전체 covariance는 이번 범위에서 받지 않았다. 질량 벡터 \(\boldsymbol m\)와 반응 질량차 계수 \(v_r\)에 대해

\[
 Q_r=c^2v_r^T\boldsymbol m,\qquad
 u^2(Q_r)=c^4v_r^T C_m v_r
\]

가 필요한 전파식이다. 오차를 독립이라고 가정한 숫자나 임의의 신뢰구간은 제시하지 않는다. 표시된 소수는 반올림된 추천값이다.

## 2. 질량 차이와 에너지 Q의 단위 교정

한 채널에 대해

\[
 M_i=m_a+m_b,\quad M_f=m_c,\quad
 \Delta m=M_i-M_f\ [\mathrm{kg}],\quad
 Q=(M_i-M_f)c^2\ [\mathrm J]
\]

로 고정한다. 따라서 아래의 \(Q^2/(2M_i c^2)\)에서 **Q는 에너지**다. 만일 Q라는 기호를 질량차에 쓰면 동일한 반동 에너지는 \(Q^2c^2/(2M_i)\)로 바뀐다. 이 단위 구분을 코드 입력 이름에서도 보존해야 한다.

\(M_i\)는 incoming system의 invariant mass이며 상대운동에너지가 0인 지금의 한계에서만 \(m_a+m_b\)다. 포획 뒤 핵의 rest mass와 혼동하지 않는다.

## 3. 정확한 두 가지 독립 대수 경로

### 3.1 에너지와 운동량으로 직접 푼다

COM에서 \(\boldsymbol p_c=-\boldsymbol p_\gamma\),
\(|\boldsymbol p_\gamma|=E_\gamma/c\)다. 최종 massive nucleus에 상대론적 분산관계를 적용하면

\[
 M_ic^2=E_\gamma+
 \sqrt{M_f^2c^4+E_\gamma^2}.
\]

양변에서 \(E_\gamma\)를 빼고 제곱하면

\[
 M_i^2c^4-2M_ic^2 E_\gamma=M_f^2c^4,
\]

따라서

\[
 \boxed{E_\gamma=\frac{(M_i^2-M_f^2)c^2}{2M_i}
 =Q\left(1-\frac{Q}{2M_ic^2}\right).}
 \tag{1}
\]

핵의 recoil kinetic energy는

\[
 \boxed{K_R=M_ic^2-E_\gamma-M_fc^2
 =\frac{(M_i-M_f)^2c^2}{2M_i}
 =\frac{Q^2}{2M_ic^2}.}
 \tag{2}
\]

이는 비상대론적 \(p^2/(2M_f)\) 근사가 아니라 **single-photon two-body cold-COM 사건의 정확한 식**이다. 분모의 \(M_i\)를 \(M_f\)로 교체하면 다른 근사식이다.

### 3.2 불변량으로 확인한다

signature \((-+++ )\)를 쓴다. \(P_i^\mu=(M_ic,\boldsymbol0)\),
\(k^\mu=(E_\gamma/c,E_\gamma\widehat{\boldsymbol n}/c)\),
\(P_f=P_i-k\)이고 \(k^2=0\)이다. 따라서

\[
 -M_f^2c^2=P_f^2=-M_i^2c^2+2M_iE_\gamma,
\]

로부터 (1)을 다시 얻는다. 이 두 경로는 같은 물리 가정 아래 서로 다른 대수 검토이며 독립 실험이나 CAS 결과가 아니다.

### 3.3 검토한 부호·단위·극한

\(0<M_f<M_i\)에서 \(E_\gamma>0\), \(K_R>0\)이며

\[
 \boxed{E_\gamma+K_R=Q.}\tag{3}
\]

\(Q\to0^+\)에서 광자 에너지는 1차, recoil은 2차로 사라진다.
\(\epsilon=Q/(M_ic^2)\)라 쓰면 \(K_R/Q=\epsilon/2\),
\(E_\gamma/Q=1-\epsilon/2\)다. 모든 항은 에너지 차원이다.

실제 수치 구현은 \(M_i^2-M_f^2\)의 직접 차보다 \(Q(1-Q/(2M_ic^2))\)를 쓰는 것이 표현상 간단하다. 그래도 작은 Q를 rounded mass에서 얻는 cancellation 및 입력 불확도가 사라지는 것은 아니다. 이번 문서는 부동소수점 정확도를 측정하지 않았다.

## 4. 세 채널의 stoichiometry, charge, 입자수

\[
 (M_i,M_f)=
 \begin{cases}
 (m_n+m_p,m_d),&r=1,\\
 (m_n+m_d,m_t),&r=2,\\
 (m_p+m_d,m_h),&r=3.
 \end{cases}
\]

핵 입자 배열을 \((n,p,d,t,h)\)로 정하면 생성−소멸의 column은

\[
 S_1=(-1,-1,+1,0,0)^T,\quad
 S_2=(-1,0,-1,+1,0)^T,\quad
 S_3=(0,-1,-1,0,+1)^T.
\]

\(A=(1,1,2,3,3)\), \(Z=(0,1,1,1,2)\)이므로 각 채널에서

\[
 A^TS_r=0,\qquad Z^TS_r=0,\qquad\boldsymbol1^TS_r=-1.
 \tag{4}
\]

따라서 baryon number와 nuclear charge는 보존되지만 자유 neutron까지 세는 핵 입자수는 포획마다 하나 줄어든다. 모든 charged nucleus가 fully stripped이며 별도 leptonic/atomic event가 없으면 neutrality로 유도한 free electron 수는
\(\Delta N_e=0\)이다. 여기에 독립 전자 생성 계수를 더하지 않는다.

중성 원자 질량을 대신 쓸 때는 전자 결합에너지 차이를 함께 바꿔야 한다. NIST 논문 Eqs. (1)–(2)의 \(m_{\rm atom}=m_{\rm nuc}+Zm_e-B_e/c^2\)와 charge 보존으로

\[
 Q_{\rm neutral}=Q_{\rm bare}+B_{e,f}-B_{e,a}-B_{e,b}.
\]

이번 bare-mass 사건 장부에 atomic binding energy를 다시 더하면 이중 계산이다.

## 5. ζ를 공급받은 cold-event 에너지 장부

채널별 \(0\le\zeta_r\le1\)를 recoil kinetic energy 중 선택한 thermal reservoir로 넘기는 **공급된 에너지 분율**로 정의한다. 직접 escaping photon과 남은 nonthermal recoil을 별도로 보유하면 사건당

| 저장소 | 변화 |
|---|---:|
| nuclear rest energy | \(-Q_r\) |
| escaped gamma ledger | \(+E_{\gamma r}\) |
| thermal energy reservoir | \(+\zeta_r K_{Rr}\) |
| retained nonthermal recoil reservoir | \(+(1-\zeta_r)K_{Rr}\) |

이며 합은 (3)에 의해 0이다. \(\zeta=0,1\)의 경계에서도 장부가 닫힌다. 전체 Q를 heat로 지정하거나, \(E_\gamma=Q\)와 양의 recoil을 동시에 더하면 이 장부가 깨진다.

이 결과는 stopping/thermalization provider를 만들지 않는다. \(\zeta\)가 에너지 분율만 정하면 nonthermal daughter의 **bath 입자수 편입**은 아직 정해지지 않는다. 다음 두 해석을 구별해야 한다.

1. 모든 nuclear species가 common thermal bath의 heat capacity에 들어가고 nonthermal energy는 별도 excess-energy bookkeeping으로 정의된 phenomenological moment model. 이 경우 그 EOS/pressure 소유권을 명시해야 한다.
2. fast daughter를 실제 별도 kinetic population으로 분리. 이 경우 총 핵수 \(\Delta N_{\rm nuc}=-1\)은 여전히 맞지만 thermal particle 수는 daughter 편입·stopping 식을 따라야 한다. \(\zeta\) 하나만으로 \(\Delta N_{\rm th}=-1\)을 추론할 수 없다.

현재 cold-event 장부는 두 해석 모두의 에너지 입력으로 사용할 수 있으나 특정 physical thermalization model의 완성 판정은 하지 않는다.

## 6. nuclei+electron 온도식에 필요한 항

### 6.1 일반 chain rule

\(n_B\)를 보존되는 baryon density로 정하고 \(Y_s=n_s/n_B\)라 한다. 핵반응으로 달라지는 hydrogen nucleus density를 보존 정규화로 쓰지 않는다. 모든 집계된 종이 common nonrelativistic monatomic thermal bath에 속한다는 EOS 가정에서

\[
 N=\sum_sY_s+x_e,\qquad n_{\rm th}=n_BN,
 \quad u_{\rm th}=\frac32 n_BNk_BT,\quad p=n_BNk_BT.
\]

\(\theta=3H\), \(\dot n_B+3Hn_B=0\)이고 thermal energy 방정식이

\[
 \dot u_{\rm th}+3H(u_{\rm th}+p)+\sigma:\pi_{\rm th}
 =\mathcal Q_{\rm th}
\]

이면 직접 미분하여

\[
 \boxed{\dot T=-2HT-\frac{T\dot N}{N}
 +\frac{2(\mathcal Q_{\rm th}-\sigma:\pi_{\rm th})}
 {3k_B n_B N}.}\tag{5}
\]

기존 reacting gas \(\pi=0\)의 범위를 유지하면 해당 contraction은 0이다. 다른 collisionless matter stress를 이 기체 식에 끼워 넣지 않는다.

포획 event rate per baryon을 \(r_j\ [\mathrm{s^{-1}}]\)라 쓰면

\[
 \dot Y=Sr,\quad\dot x_e=0,\quad
 \dot N=-\sum_jr_j,
\]

따라서 핵 입자수 변화가 만드는 항은

\[
 \boxed{\left.\dot T\right|_{\rm particle\ count}
 =+\frac{T}{N}\sum_jr_j.}\tag{6}
\]

원자 PI/RR에서는 핵 수가 고정되어 \(\dot N=\dot x_e\)로 줄일 수 있었다. 그 축약을 핵융합에 그대로 쓰는 것이 여기서 찾아낸 누락 위험이다. **일반 chain rule은 이미 REI221에서 사용된 구조이며 새 법칙으로 주장하지 않는다.** 새 부분은 세 capture column의 \(\dot N_{\rm nuc}\ne0\)를 명시적으로 연결한 것이다.

### 6.2 (6)만으로 실제 가열을 선언할 수 없는 이유

유한 온도의 반응물은 보통 0이 아닌 운동에너지를 갖고, 반응별로 선택되는 상대 운동에너지는 단순한 \(k_BT\) 대입이 아니다. COM의 상대 운동에너지를 \(K\ge0\), 총 incoming energy를 \(W=M_ic^2+K\)라 놓으면 exact two-body 식은

\[
 E_\gamma(K)=\frac{W^2-M_f^2c^4}{2W},\qquad
 K_R(K)=\frac{(Q+K)^2}{2W}.
\]

초기 운동에너지 K를 동일한 reservoir에서 제거하고 최종 recoil을 모두 그곳에 되돌리는 COM 사건의 net kinetic source는

\[
 \Delta U_{\rm kin}=K_R(K)-K.
 \tag{7}
\]

그러므로 유한-T 계산에 cold \(\zeta K_R(0)\)만 넣으면 반응물의 kinetic moment가 광자로 빠지는 항을 놓칠 수 있다. gas frame의 COM motion, emission angular distribution와 partial thermalization까지 있으면 그 에너지·입자수 소유권도 추가로 정해야 한다. (5)는 그러한 source가 공급되면 바로 쓸 수 있는 정확한 EOS chain rule이며, (7)은 이번 cold kernel을 warm plasma model로 확대할 때 필요한 의무를 드러낸다.

## 7. 공급된 extent를 통한 계산 단순화

반응률을 새로 만들지 않고 event extent per baryon \(\xi_j\)를 공급받으면

\[
 Y=Y_0+S\xi,
\]

즉

\[
\begin{aligned}
Y_n&=Y_{n0}-\xi_1-\xi_2,&Y_p&=Y_{p0}-\xi_1-\xi_3,\\
Y_d&=Y_{d0}+\xi_1-\xi_2-\xi_3,&Y_t&=Y_{t0}+\xi_2,\\
Y_h&=Y_{h0}+\xi_3.
\end{aligned}
\]

허용 영역은 \(\xi\ge0\) 및 \(Y_0+S\xi\ge0\)인 compatibility polytope다. 세 채널이 n,p,d를 공유하므로 각 채널의 개별 extent cap만 검사해도 전체 양성이 보장된다고 가정하지 않는다.

constant event energies와 supplied \(\zeta_j\)를 쓰는 fixed-volume, no-other-source **조건부 에너지 장부**에서는

\[
 E_{\gamma,\rm esc}=E_{\gamma,0}+\sum_jE_{\gamma j}\xi_j,\qquad
 E_{\rm nt}=E_{\rm nt,0}+\sum_j(1-\zeta_j)K_{Rj}\xi_j,
\]

\[
 U_{\rm th}=U_{\rm th,0}+\sum_j\zeta_jK_{Rj}\xi_j,
 \quad N=N_0-\sum_j\xi_j.
\]

그 EOS 가정까지 채택한 경우에만

\[
 \boxed{T(\xi)=
 \frac{N_0T_0+\frac{2}{3k_B}\sum_j\zeta_jK_{Rj}\xi_j}
 {N_0-\sum_j\xi_j}},\qquad N>0.\tag{8}
\]

이 식은 장부·온도 상태의 조건부 대수적 제거를 제공한다. 물리적으로 누락된 유한-T incoming kinetic moment나 bath 편입을 채워 주지는 않는다. \(\zeta\) 또는 event moment가 상태 의존적이면 해당 source를 extent에 대해 적분해야 하며 상수 곱으로 치환하지 않는다. 이 재구성으로 에너지를 만든 뒤 같은 에너지 보존식만 검사하는 것은 독립 검증이 아니다.

Local fixed-volume escaped-energy counter는 방출 시 에너지의 누적 장부다. 우주론적 radiation energy density로 해석하려면 redshift/work/방향 수송이 필요하다. 이 노트는 그런 radiation tensor closure를 제공하지 않는다.

## 8. 중복 조사와 신규성의 정확한 범위

실제 읽은 REI221 `research/rei_coupled_local_flow_20261022/THEORY.md`는 commit
`9620e1fcc4bdda76e0311206f614234926600381`, Git blob
`dfbc812088e1d9a9b4de8b80e16d30b09f41f5a4`다.
그 Sec. 2는 pure-H Case-A RR, \(U=3k_B(1+x)T/2\), particle-number chain rule과 escaped RR energy를 이미 다룬다. Sec. 3은 prescribed-T neutron beta+RR와 exact population subflows이며, Sec. 3.5는 beta electron/neutrino/recoil partition 미공급을 명시한다.

따라서 일반 열역학 chain rule, cumulative escaped-energy 장부, extent 좌표와 기존 beta/RR 실행을 반복하지 않는다. 세 capture 채널의 bare-mass cold-COM 분할, total nuclear particle count의 −1, unchanged derived electron, photon/recoil/bath 경계가 이 후보의 구체적인 추가 입력이다.

REI219 `NUCLEAR_PROVIDER_INVENTORY.md`에는 p(n,γ)D, D(n,γ)T, D(p,γ)He3 rate anchors가 이미 존재한다. 이들의 존재와 원전 범위를 재사용하되 이번 mass/kinematics 자료가 해당 low-T rate validity까지 입증한다고 쓰지 않는다. 기존 β 에너지 partition 의무도 이 세 radiative-capture 결과로 닫히지 않는다.

이는 **읽은 exact REI221 local-flow 단원과 전달 기록에 대한 비중복 판정**이다. 전 저장소의 모든 과거 코드에서 동일 식이 없었다거나 문헌상 새로운 법칙이라는 주장이 아니다. 추정한 sandbox/THEORY 경로는 404였고, 그 파일 전체를 읽었다고 기록하지 않았다.

## 9. 실제 검토와 다음 단계

실제 검토: NIST primary table의 질량/standard uncertainty 전사, NIST Sec. II.B의 포획 recoil 식 읽기, 직접 energy–momentum과 four-vector invariant 두 대수 경로, 차원/부호/zero-release/ζ endpoint, 세 stoichiometric column의 A/Z/particle-count 수동 대조, EOS chain rule와 finite-K 반례 검토, exact REI221 문서 대비다. CAS나 수치잔차 검사를 수행했다고 주장하지 않는다.

다음 coding admission에서 고정할 것은 (a) 공급된 extent 장부 또는 실제 rate-driven scenario 중 무엇인지, (b) common thermal bath의 species membership, (c) cold-event 근사를 유지할지 supplied incoming kinetic moment를 추가할지, (d) ζ와 escaped/nonthermal reservoir pressure·number 소유권이다. 이 선택 뒤 바뀐 부분만 구현·검증하면 된다.

아직 열려 있는 항목은 rate/source domain, finite-T weighting, stopping/thermalization, covariance 기반 derived uncertainty, spectral/방향 수송, cosmological background coupling이다. HH_R10=OFF와 production admission=NOT_ISSUED를 변경하지 않는다.
