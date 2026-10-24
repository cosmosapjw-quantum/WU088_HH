# PHYS89: nuclear source covariance와 공통 사건 소비자 계약

## 결과와 확보 범위

이 문서는 PHYS88 FINAL의 조건부 질량 사상을 그대로 재사용한다. 현재 단일 선택 노드는 `NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT`이며 상태는 `PARTIAL_INPUT_DEPENDENCIES`이다. 이번에 실행할 유한한 자식 의무는 원 MF33 fractional covariance의 정확한 구조 복원, 조건부 pullback, 정규화된 유한 함수의 상관, 같은 사건의 thermal/fast/radiation energy와 clock/density 인터페이스이다. 실제 finite-T rate 적분, history, nuclear rate 활성화, fast stopping은 없다.

이 파일은 중단 전 유도와 검토 교정을 남은 인계 기록에서 복원한 revision3이다. 이전 revision2 원bytes는 현 호스트에서 확보되지 않았다. 이전 이론·Wolfram의 지식은 재사용하되 새 파일에 과거 SHA를 붙이지 않는다. 이전 Wolfram evaluator1회는 성공한7개0이라는 transcript 기록으로 보존하고 다시 호출하지 않는다. 현재 독립 검토와 이후 새 source/fixture 검증은 새 파일identity에 묶는다.

## 1. 원 평가와 atomic/bare 구별

원 자료는 고정 SHA256 `3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af`의 ENDF H1이다. Brown et al. ENDF/B-VIII.0 §III.A.2/TableII는 n-p capture와 gamma-d inverse channel의 R-matrix 평가를 기술한다. AWR의 atomic mass 관례만으로 electron-resolved neutral-atom kernel을 추론할 수 없다. Nominal unpolarized nuclear cross section은 rho_n=I2/2, rho_p=I2/2의 평균으로 사용하며 추가 singlet/triplet 확률을 곱하지 않는다. 정확한 evaluator masses/deck와 invariant-s 이전, electron·target-state 영향과 그 오차는 아직 공급되지 않았다.

PHYS88의 LAB_ANCHORED, FIXED_COM_K 두 조건부 사상과153 native knots/152 cells, native Es 보간을 유지한다. 81.63eV는 binding차0.003700036867eV와 convention-residual차81.626299963133eV로 분해된다. Signed same-event carrier는 heat나 실제 electron이 아니며 fresh bare two-body 사건과 구별한다. 이전 네 T의136.189–168.788ppm은 두조건부 모형 차이이다.

## 2. MF33의 독립 격자와 pullback

원 MF33/MT102는 MAT125, NL1, MAT1=0, MT1=102, NC0, NI1, LS1, LB5, NT11935, NE154를 갖는다. Boundary154개와153group의 upper-triangle diagonal-first row-major11781값이 있다. Covariance boundary의 [5e-6,2.025e7]eV와 cross-section native support [1e-5,2e7]eV는 다르다. Wider covariance grid가 sigma의 support를 늘리지 않는다.

LB5의 F는 fractional group covariance이다. E가 native bin g에 속하고 E'가 h에 속하면

Cov[sigma(E),sigma(E')]=sigma(E)sigma(E')F_gh.

Monotone conditional map Es=phi(Eb)에서 sigma_b(Eb)=sigma_s(phi(Eb))로 정의하면 F는 두 native bin index로 pullback된다. sigma나F에 Jacobian을 추가하지 않는다. Jacobian은 dEs=phi'(Eb)dEb라는 적분 measure 변환에만 들어간다. 적분이 후속 단계에 허용되면 native sigma knots와 MF33 boundaries의 공통 세분을 써야 한다. F를153개의 sigma knots 위로 보간하는 것은 다른 객체이다.

Bins는 왼쪽 닫힘·오른쪽 열림이고 마지막 support endpoint만 마지막 bin에 둔다. 단차가 있는 F에서 Es→Eb→Es 부동소수 roundtrip으로 bin을 결정하면 경계가 잘못 바뀔 수 있다. Canonical Es/bin을 운반하거나 forward-mapped boundary를 직접 비교한다. Epsilon clipping은 없다.

## 3. 유한 함수의 공통 source 상관

실제 새 열 적분을 수행하지 않고 유한 group coefficient r_g>=0, Z=sum_g r_g>0와 reward a_ag를 입력받는다. Z는 정규화, A_a=sum_g a_ag, M_a=A_a/Z이다. Group nuisance eta에 대하여

delta Z=r dot eta, delta A_a=a_a dot eta,
Cov[(Z,A)]=L F L^T.

정규화 미분은 b_a=(a_a-M_a*r)/Z이며 delta M_a=b_a dot eta, Cov_delta(M)=B F B^T이다. 이는 일차 source covariance 전파이다. 분모가 양수인 유한 변화는 정확히

M'_a-M_a=(delta A_a-M_a delta Z)/(Z+delta Z).

abs(delta Z)<=rho Z, 0<=rho<1이면 일차식과의 차이는 rho/(1-rho)*abs(b_a dot eta) 이하이다. 여러 map/T/consumer가 같은 평가 F를 사용하면 교차 상관을 유지해야 한다. 기존 scalar thermal totals로 미지의 group coefficient를 복원할 수 없다. Event kinetic variance, source epistemic covariance, counting shot noise는 서로 다른 객체이다.

원F의 PSD 여부는 직접 source 진단 대상으로 남긴다. 출력된 decimal matrix에 exact negative principal minor 또는 rational v^T F v<0가 있으면 그 displayed matrix를 확률 covariance로 채택하지 않는다. F를 projection/jitter/clipping하지 않는다. Binary64 eigenvalue는 진단이고 exact Fraction witness가 대수적 반례 근거이다. 토큰 ULP 및 반ULP는 nearest-rounding을 가정한 조건부 bound이며 formatter 또는 물리 오차의 보증이 아니다. 이 국소 반례는 evaluator 자체나 물리 모델에 대한 strong no-go가 아니다.

## 4. 같은 사건의 measure와 소유권

Normal orthonormal frame에서 q=(E,c p), metric(-+++)를 쓴다. a=m_n c^2,b=m_p c^2이면 Moller flux 속도는

vM=c sqrt((q_n dot q_p)^2-a^2 b^2)/(E_n E_p).

분포는 physical volume의 momentum number density이고 dnu=f_n f_p vM (d sigma/dOmega) d^3p_n d^3p_p dOmega는 proper time당 physical volume당 사건 강도이다. n,p는 다른 입자이므로 identical-pair1/2를 넣지 않는다. Differential kernel, 분포와 state contract가 실제 주어져야 이 measure를 물리적으로 평가할 수 있다.

K_in+Q_b=K_d+E_gamma인 사건에서 h와r_gamma를[0,1]의 event-dependent 분할로 정의한다.

| 소유권 | signed energy eV |
|---|---|
| thermal | h K_d-K_in |
| fast | (1-h)K_d |
| rest | -Q_b |
| atomic | 0 |
| photon handoff | r_gamma E_gamma |
| escape | (1-r_gamma)E_gamma |

여섯 열의 합은 사건마다0이다. 따라서 group coefficient의 열합도0이고 같은 F로 전파한 covariance의 합계 행도0이다. h가 사건에 의존하면 <hK_d>를 사용하며 <h><K_d>로 대체하지 않는다. Thermal count는h-2, fast count는1-h, electron count는0이다. h=1은 instant birth caloric bookkeeping이고 stopping 계산이 아니다.

이 caloric 인터페이스는 입사 neutron과 proton을 모두 thermal reservoir가 소유하고, outgoing deuteron의 h 부분만 그 reservoir에 넣는 경우에 한정한다. C_V=sum_s n_s partial_T u_s(T)>0를 가정한다. 다음 dotT|capture는 반응 기여이며 expansion/work/다른 과정은 각각의 소유자가 더한다. Thermal internal energy를 각 species의 u_s(T)로 쓰면, physical number sources를 함께 넣은 온도분자는

C_V dotT|capture=integral[-K_in+u_n+u_p+h(K_d-u_d)]dnu.

이는 에너지 항만으로 온도 변화를 잘못 결정하지 않도록 수변화 항을 포함한 식이다. Photon/fast spectrum은 동일 joint event measure의 pushforward로 공급한다. Scalar mean만으로 spectrum을 공급했다고 할 수 없다.

Signed tensor source integral q^mu q^nu/q0 dnu는 tensor birth rate이며 저장된 stress state가 아니다. 사건 four-momentum 합이0이어도 spatial stress 합은 일반적으로0이 아니다. Reacting gas pi=0와 collisionless DM pi_m을 분리하고, 같은 frame의 signed matter/radiation tensors를 먼저 더한 뒤 norm을 계산한다. Frobenius=sqrt(2)*half-contraction을 유지한다.

## 5. clock, density, tail

Conserved Href는 dot nHref+Theta nHref=0을 만족한다. Y=n/nHref이면 dotY=S/nHref이다. Reference가 보존되지 않으면 -Y(Theta+dotnHref/nHref)가 추가된다. Coordinate time t에는 d tau/dt=alpha를 정확히 한 번 곱한다. 한 packet의 yield는 R Delta_tau/nHref이다. eV/Href에서SI energy density로 바꾸려면 nHref[m^-3]와1.602176634e-19J/eV를 곱한다. cm^-3 입력은 먼저1e6을 곱한다.

유한 supportI 안의 Z_I>0와 M_I=A_I/Z_I를 알고, 비음수 event measure의 tail mass 0<=Z_tail<=B0 및 절대 reward moment |A_tail|<=BA가 별도로 확보되면

|M_full-M_I| <= (BA+|M_I|B0)/Z_I.

Boltzmann 억제만으로 sigma·reward의 tail 상계를 얻을 수 없다. 실제 B0/BA와 outside-support kernel은 미공급이므로 full-support physical bound는 발행하지 않는다.

## 6. 이름 있는 소비자 요청과 독립 검토 교정

기존 중앙 REI-L2는 n/T beta daughter, electron/neutrino/recoil/nonthermal energy의 계약이다. Capture deuteron reservoir의 기존 구현으로 호출할 수 없다. `WU89_REI_L2_NP_CAPTURE_REQUEST_V1`는 그 bookkeeping의 **capture 확장 제안**이며 scope_extension_required=true, actual_owner_id/ACK=null이다. Thermal/fast 소비자는 PROPOSED_UNIMPLEMENTED이다. `WU89_BASS_NUCLEAR_PHOTON_REQUEST_V1`도 actual owner/ACK=null, NOT_BOUND이다. BASS B3C의 cold H-Lyalpha14cohort manufactured 예제는 설계 참고만 제공한다.

중단 전 독립 R6의 P89-R6-01은 이 scope 혼동을 찾아 교정했다. 부수적인 이전 repair metadata shallow-copy alias(P89-R6-META-01)도 수정됐다고 인계되었으나 그 원bytes는 현 호스트에 없다. 현재 문서는 수정된 의미를 명시하고 독립 재검토한다.

## 7. 코딩 연결과 판정 한계

CONTRACT.json이 parser, grid, support, exact rational fixtures, source PSD 진단, typed owner/clock guards,1primary+1independent reference의 범위를 동결한다. 이론 조건부 식의 검증과 실제 source 표의 구조 진단이 이번 실행 대상이다. Source CI/physical finite-T supplier/named consumer ACK는 미해결 물리 의존성으로 남는다. 새 ODE0, 적분0, benchmark0, nuclear activation0, stopping0, HH_R10 OFF, production NOT_ISSUED이며 전체 물리 완료율은null이다.

## 1차 출처

- ENDF-102, 2023 manual: https://www.nndc.bnl.gov/endfdocs/ENDF-102-2023.pdf , §0.5.1.1 atomic weight conventions; §33.2.2.2 LB5 covariance.
- Brown et al., Nuclear Data Sheets148 (2018), ENDF/B-VIII.0: https://escholarship.org/content/qt2dj9p3h4/qt2dj9p3h4_noSplash_7d55137415e7004203a27c552b02b984.pdf , §III.A.2 and TableII.
- PHYS88 FINAL source and completed evidence: https://github.com/cosmosapjw-quantum/WU088_HH/tree/92dec7cdc1cf5afeff5bdff8d6234f7f1e3dbbd8/research/hh_phys88_atomic_bare_remap_20261024
