# PHYS85: 반응에 선택된 운동에너지와 thermal/fast 입자 소유권

## R1–R3: 기존 완료 근거와 새 질문

실제 부모는 PR141 HEAD `d5c2c8dbbbd77bc81526dda6e74df534fba3c4e5`다. PHYS83 완료 identity와 PHYS84 동결 source adapter를 재사용한다. PHYS84 첫 수치 검증은 기존 1.5GiB reserve+0.5GiB job lease에 대기 중이며 코드나 기준을 바꾸지 않는다. 중앙 `WU_CE83_OWNER_COMPLETION`의 역사적 OPEN은 owner 완료를 읽은 overlay에서만 갱신한다.

별도 선행 없는 `WU_NUCLEAR_PARTICLE_OWNERSHIP`의 이번 질문은 세 bare capture 채널 n+p→d+γ, n+d→t+γ, p+d→h+γ에서 **초기 thermal 입자의 소모, 최종 딸핵의 유일한 집단 소속, 같은 normal frame의 에너지**를 어떻게 한 사건으로 결속하는가다. 실제 단면적·율·stopping·ODE 활성화는 후속 의무다. CR의 새 finite-T photoelectron bridge 예약을 구현하지 않는다.

PHYS81 `b3ec271a96cb67e583bffa9b61533802838236f9`의 COM photon/recoil 식과 CODATA2022 질량 원문, 완료663 assertions를 그대로 채택한다. 기존 kernel/검증/cold cases를 호출하지 않는다. 아래 일반 Maxwellian 평균법과 EOS chain rule은 문헌에 존재하는 구조다. 새 프로젝트 기여는 이 구조를 PHYS81 사건과 thermal/fast 입자 소유권에 연결하고 실행 가능한 exact reference로 제공하는 것이다.

### 원전 범위

- S. I. Warshaw, *The TDF System for Thermonuclear Plasma Reaction Rates, Mean Energies and Two-Body Final State Particle Spectra*, UCRL-ID-144510 (2001), [LLNL 원문](https://nuclear.llnl.gov/CNP/tdf/tdf.htm), §§2–3: 공통-T Maxwellian의 COM/relative 분리, 반응률로 가중한 선택 평균, 두 동일 반응물의 pair factor, 선택 상대에너지와 rate slope. 원문의 massive final-state 비상대론적 식을 광자에 그대로 적용하지 않는다.
- C. Y. Cardall, *Relativistic Analogue of the Newtonian Fluid Energy Equation with Nucleosynthesis*, Phys. Rev. D96,123014 (2017), [accepted version](https://arxiv.org/abs/1802.05590): rest/binding과 thermal energy의 일관된 분리 배경. 이번 외부 reaction supplier나 새로운 cosmological completion을 제공하는 자료는 아니다.
- PHYS81 고정 [CODATA2022 source](https://physics.nist.gov/cuu/Constants/Table/allascii.txt)와 당시 원전 검토를 재사용한다. 표시 질량은 반올림 추천값이며 joint covariance를 새로 확보하지 않았다. exact rational 결과는 입력 소수에 대한 대수 정확도다.

SciSpace는 후보 원전을 찾는 데 사용했다. 무관한 첫 검색 결과는 채택하지 않았다. Exa402 credit-limit는 보존하며 다른 원전 경로로 진행했다. 웹 HTML에서 식 일부가 image로 표시되는 한계는 아래 직접 유도로 보완한다. 문헌 내용을 확인하지 않은 식까지 읽었다고 주장하지 않는다.

## R4–R5: 같은 normal frame의 정확한 한 사건

질량의 에너지 등가를 ε_a=m_a c², ε_b=m_b c², ε_c=m_c c²로 쓰고 M=ε_a+ε_b, Q=M−ε_c, K≥0, W=M+K라 하자. K는 **정확한 invariant COM excess energy**이며 normal-frame pair kinetic energy가 아니다. 부모 식은

\[
e_*=\frac{(W-\epsilon_c)(W+\epsilon_c)}{2W},\quad
k_*=\frac{(W-\epsilon_c)^2}{2W},\quad E_{c*}=\epsilon_c+k_*,\quad e_*+E_{c*}=W.
\]

새 구현은 유리수 half-rapidity r∈[0,1)로 γ=(1+r²)/(1−r²), β=2r/(1+r²)를 표현한다. 이는 γ²(1−β²)=1을 정확히 만족한다. μ∈[−1,1]는 COM photon과 boost 방향의 cosine다. 같은 normal orthonormal observer가 보는 에너지는

\[
E_γ=γe_*(1+βμ),\quad
K_c=γ(E_{c*}−βe_*μ)−\epsilon_c,\quad
K_{in}=γW−M.
\]

따라서 **K_c+E_γ=K_in+Q**다. 이는 warm input과 COM motion을 포함한 개별 사건의 상대론적 운동학이다. β=0에서 부모 식으로 돌아가는 대수 극한을 재사용하며 이전 cold numerical result를 재계산하지 않는다.

독립 검증은 저장소 에너지 합만 다시 보는 것에 그치지 않는다. z축 boost에서 c p_{c,z}=γ(βE_{c*}−e_*μ), c²p_{c,⊥}²=e_*²(1−μ²)로 직접 구성하고 E_c²−c²p_c²=ε_c²를 확인한다. 코드에는 `mc_energy` 등 명시적 이름을 쓴다. 총 z momentum은 γβW/c이고 photon은 null이다. energy residual을 0으로 덮어쓰지 않는다. 일반 domain에서 E_γ>0, K_in≥0, K_c≥0이며, 경계에서 kinetic energy가0인 사건도 유효하다. 계획한 비퇴화 fixtures의 strict positivity는 그 사례에 한정한다.

## R5–R6: 집단 소속과 에너지 소속을 동시에 고정

두 incoming nuclei는 thermal이다. 딸핵의 사건별 소속 h는 thermal-birth model이면1, fast-birth면0이다. 전자는 생성되지 않는다. h는 에너지 분율 ζ가 아니다. thermal-birth는 입자 하나와 전체 K_c를 즉시 ideal thermal moment에 넣는 **명시한 closure**이며 물리 stopping을 유도한 결과가 아니다.

\[
\Delta N_{th}=h-2,\quad\Delta N_{fast}=1-h,\quad
\Delta N_{nuc,total}=-1,\quad\Delta N_e=0.
\]

질량수와 전하 incidence는 thermal+fast 모든 핵을 합쳐야 보존된다. fast charged daughter를 제외한 thermal 핵 전하만으로 free-electron 수를 다시 계산하지 않는다. 기존 bare-mass 기준에는 atomic binding 변화가0이다.

| energy owner | 사건별 변화 |
|---|---:|
| thermal | h K_c−K_in |
| fast | (1−h) K_c |
| nuclear rest | −Q |
| atomic binding | 0 |
| radiation injected | handoff일 때 E_γ, 나머지0 |
| escaped radiation | escape일 때 E_γ, 나머지0 |

여섯 열의 합은 정확히0이다. `emitted`는 진단량이고 별도 일곱째 에너지가 아니다. 방출 Q를 다시 heat로 더하지 않는다. 향후 stopping은 capture와 다른 사건으로 ΔN_th=+1, ΔN_fast=−1 및 같은 fast-to-thermal 에너지 이동을 제공해야 한다. 입자 편입과 에너지 전달 시간이 다르면 그 모델은 별도 moment contract를 요구한다.

가중 사건 평균에서 `mean(h*K_c)`를 유지해야 한다. `mean(h)*mean(K_c)`로 대체한 오차는 covariance이며, 서로 다른 에너지 사건에 서로 다른 소속을 부여하면 일반적으로 0이 아니다. 동일 event weights로 모든 incidence와 에너지 열을 평균해야 선형 보존식이 유지된다.

율 R[volume⁻¹ time⁻¹]이 별도로 주어질 때만 위 사건당 평균에 R을 곱한다. 이번 reference weights는 합1의 유리수 **조건부 사건 ensemble**이며 측정 율, 실제 Maxwellian quadrature 또는 불확도 분포가 아니다.

## R5–R7: 반응에 선택된 유한-T 운동에너지

이 절은 **비상대론적 공통-T Maxwellian** 모델에서 정확하다. 앞 절의 상대론적 kernel을 정확한 Maxwellian/Jüttner 평균으로 계산했다고 합치지 않는다.

\[
\mathbf V=(m_a\mathbf v_a+m_b\mathbf v_b)/M_m,\quad
\mathbf g=\mathbf v_a-\mathbf v_b,\quad
K=\tfrac12\mu_m g^2,\quad K_V=\tfrac12M_mV^2,
\]

여기서 M_m=m_a+m_b, μ_m=m_a m_b/M_m는 질량이다. 독립 Maxwellian의 곱에서 exponent는 (K_V+K)/θ, θ=k_BT이고 Jacobian은1이다. σ(K)g가 COM에 의존하지 않으므로 반응으로 선택해도 mean(K_V)=3θ/2다. 방향 cross term 평균은0이다. 다만 relative K는 반응률로 선택된다.

\[
\kappa(T)=\sqrt{\frac8{\pi\mu_m}}\theta^{-3/2}I_1,
\quad I_j=\int_0^\infty K^j\sigma(K)e^{-K/\theta}\,dK,
\quad\langle K\rangle_R=I_2/I_1.
\]

이때 총 incoming pair kinetic mean은 3θ/2+mean_R(K)다. 개별 reactant의 평균은

\[
\langle E_a\rangle_R=\frac{m_a}{M_m}\frac{3θ}{2}
 +\frac{m_b}{M_m}\langle K\rangle_R,
\quad
\langle E_b\rangle_R=\frac{m_b}{M_m}\frac{3θ}{2}
 +\frac{m_a}{M_m}\langle K\rangle_R.
\]

T>0, N_th>0, σ≥0, 0<I₁<∞와 finite I₂를 가정한다. σ와 적분영역이 T와 독립이고 미분/적분 교환을 허용하는 finite moment 조건에서

\[
T\frac{d\log\kappa}{dT}=-\frac32+\frac{\langle K\rangle_R}{θ}.
\]

σ의 명시적 T 의존, 이동하는 cutoff, drift, 서로 다른 온도, 비-Maxwellian tail에는 이 식을 그대로 적용하지 않는다. R=0이면 source는0이지만 κ=0에서 normalized event mean과 log κ는 정의하지 않는다. 위 식 자체가 missing source를 공급하지 않으며 total-rate table만으로 differentiation noise/domain 문제도 자동 해결하지 않는다.

## R6–R8: 온도식의 구성적 귀결

fixed-volume instantaneous source에서 U_th=3 k_B N_th T/2이므로

\[
\dot T=\frac{2R\langle\Delta U_{th}\rangle}{3k_BN_{th}}
 -\frac{TR\langle\Delta N_{th}\rangle}{N_{th}}.
\]

capture daughter를 모두 fast에 두는 h=0 closure에서는 ΔN_th=−2이고 thermal energy source는 −R(3θ/2+mean_R(K))다. 합치면

\[
\boxed{\dot T_{capture,fast}
=-\frac{2R}{3k_BN_{th}}(\langle K\rangle_R-3θ/2)
=-\frac23\frac{RT}{N_{th}}\frac{d\log\kappa}{d\log T}.}
\]

따라서 입자수 감소만으로 가열을 선언할 수 없다. σ∝K^s, s>−2라는 formal witness에서 I_2/I_1=(s+2)θ이고 Tdot=−(2s+1)RT/(3N_th)다. 상수 σ(s=0)는 −RT/(3N_th), inverse-speed σ∝K^−1/2는0을 준다. 두 예는 source-selection/number-term 검증용이며 실제 capture cross section으로 채택하지 않는다.

우주론적 적용은 별도 local source에 기존 −2HT, 보존 baryon density 정규화, 모든 필요한 work/transport를 더한다. 이번 finite algebra를 coupled history bound로 해석하지 않는다. non-tilted LRS BianchiI, reacting gas π=0, 별도 collisionless DM π_m, 같은 frame의 signed tensor 합 뒤 norm, Frobenius=√2×half-contraction 규약은 그대로다. 이 scalar interface는 fast/radiation angular tensor closure를 공급하지 않는다.

## R9–R10: 실행 가능한 다음 단계와 주장 경계

새 exact reference는 non-cold9events의 owner/route36행과 correlated-owner6ensemble을 만든다. 직접 four-momentum oracle, incidence, route, covariance, formal power-law witnesses를 독립 검토한다. 유도·CAS·code verification·application·게시·백업을 별도 ledger에 기록한다. 원본 663 assertions나 PHYS83/84 numerical results의 중복 실행은0이다.

이 작업으로 사건당 소유권의 scalar contract와 선택 kinetic debit 의무를 구성적으로 닫는다. **실제 finite-T nuclear source supplier는 OPEN**이다. evaluated σ/branching/angular data, distribution/frame/clock, same-event weights, thermalization/fast evolution, uncertainty/covariance와 consumer domain을 공급한 후에만 물리적 rates/fast stopping 활성화를 검토한다. HH_R10=OFF; production admission NOT_ISSUED.
