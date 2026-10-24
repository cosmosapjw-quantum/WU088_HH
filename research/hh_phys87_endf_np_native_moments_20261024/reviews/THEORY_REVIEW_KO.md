# PHYS87 독립 R6 이론 검토

## 판정

**독립 R6 이론 판정: PASS_SCOPED_THEORY. 미해결 실행 전 지적 0건.**

최종 검토 계약은 revision 2, SHA256 `464df6f83a7ac8bd64813dc9da3ca34f19398a2f970f3d69c706e3d089f6fd38`다. Revision 1에 대한 아래 두 지적은 `reviews/PREIMPLEMENTATION_CONTRACT_REPAIR.json`과 실제 수정 내용을 대조해 닫았다. 물리식·source·목표 정확도·계산 예산은 바뀌지 않았고, 교정 전 source 과학 실행은 0이다.

검토 대상은 ENDF H1 원자료의 유한 에너지 구간, 명시적으로 고른 neutron mass scale, atomic AWR/QI 규약을 사용한 source-native scalar/conditional moment 구성이다. Bare-nucleus network, source 밖 tails, covariance propagation 또는 실제 coupled physical admission은 이 판정에 포함하지 않는다. 이번 검토자는 유도 원문·동결 계약·canonical raw·전사 헤더·ENDF 매뉴얼을 직접 읽고 아래 계산을 독립적으로 전개했다. 새로운 수치 실행, Wolfram 호출, 기존 과학 재실행은 0이다. 실제 R7/C6–C9 결과 판정은 실행 원자료를 받은 뒤 별도로 한다.

## 독립 검토한 핵심 전이

### 1. 원자료와 질량/Q

Canonical ENDF SHA256은 3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af다. SOURCE_TABLE의 MF3/102와 MF6/102 헤더는 153절점, INT5→INT2, CM LAW2/LANG0/NL2 및 LAW4 recoil/yield1를 명시한다. Photon AWP는 mass가 아닌 primary energy field다.

ENDF-102(2023) §0.5.1.1은 atomic AWR와 light-product nuclear AWP를 구분하고 §6.3.2는 LAW2 primary photon과 LAW4 recoil에 Appendix E의 relativistic kinematics를 요구한다. Appendix E.21은 residual mass를 target+projectile−emitted−QI로 정의한다. Photon emitted mass=0을 사용한 \(\epsilon_D=M-Q\) 경로는 이 규약과 일치한다. Independent light-product AWP와 atomic target를 섞어 Q를 다시 만드는 경로는 쓰지 않는다.

부모 CODATA2022 neutron energy를 이번 scale로 **명시적으로 선택**하고 bare parent masses를 불변으로 둔 조건을 확인했다. 따라서 이 구성은 원 evaluation의 unknown absolute neutron mass를 알아냈다는 주장이 아니다. 81.63eV Q 차이를 오차막대나 평가 실패로 바꾸지 않고 remap gate로 남긴 처리도 맞다. AWP의 nominal primary energy와 Q-based exact event energy는 별도 값으로 유지해야 한다.

### 2. Angular normalization과 회전 평균

정규화 \(f=(1+3a_1\mu+5a_2P_2)/2\)에서는 Legendre 직교성으로 \(\langle\mu\rangle=a_1\), \(\langle P_2\rangle=a_2\), \(\langle\mu^2\rangle=(1+2a_2)/3\)이다. Azimuth 평균 후 tensor는
\[
\langle n_i n_j\rangle=(1-a_2)\delta_{ij}/3+a_2u_i u_j
\]
이므로 boost축과 입사축 사이 \(\eta\)에 대한 \(\langle\nu\rangle=a_1\eta\), \(\langle\nu^2\rangle=(1-a_2+3a_2\eta^2)/3\)가 성립한다.

고정 W와 total four-momentum에서 \(d^3p_n/E_n\,d^3p_H/E_H\)의 pair COM 방향 measure는 균일하다. Common-T product Boltzmann factor는 total energy \(\gamma W\)만 보고, scalar invariant flux와 \(\sigma(W)\)에도 그 방향이 없다. 따라서 원래 비등방 \(f(u\cdot n)\)를 uniform \(u\)에 평균하면 absolute photon 방향이 uniform이다. Unequal rest masses는 이 논증을 깨지 않는다. 반면 unequal T, drift, polarized/aligned source 또는 방향별 event selection은 이 논증의 전제를 바꾸므로 해당 추가 모델에는 재유도가 필요하다.

각 knot의 quadratic 최소값과 lin-lin coefficient convex combination에 의한 양성성 논증도 올바르다. 이 논증이 닫히려면 실행에서 실제 153개 입력의 minima가 양수라는 근거가 필요하다. 현재 정적 검토로 그 미실행 판정을 대신하지 않았다.

### 3. Rate prefactor와 차원

Natural energy-momentum 변수 \(q=cp\)를 쓰고 rest energies를 a,b라 두자. Pair phase-space convolution은
\[
\int {d^3q_a\over E_a}{d^3q_b\over E_b}\,
\delta^4(P-p_a-p_b)={2\pi\sqrt{\lambda(s)}\over s}.
\]
Flux의 \(\sqrt{\lambda}/2\), \(dP^0=ds/(2P^0)\) 및
\(\int d^3P\,e^{-P^0/\theta}/(2P^0)=2\pi\sqrt{s}\theta K_1(\sqrt{s}/\theta)\)
를 곱하면 정규화 전 적분은
\(2\pi^2c\theta\int\sigma\lambda(s)K_1(\sqrt{s}/\theta)ds/\sqrt{s}\)다.
\(Z_a Z_b=16\pi^2a^2b^2\theta^2K_2(a/\theta)K_2(b/\theta)\)로 나눈 뒤 \(s=W^2\)를 적용하면 원문 Eq.(1)의 \(c/(4a^2b^2\theta)\) prefactor를 얻는다.

\(\lambda\)는 energy^4, dK는 energy, denominator \(a^2b^2\theta\)는 energy^5이므로 결과 단위는 cσ=cm³/s다. 서로 다른 n/H에 추가 1/2를 넣지 않는 것도 맞다.

독립 NR limit에서는
\[
\kappa\to c\sqrt{8/(\pi\mu_\epsilon)}\theta^{-3/2}
\int K\sigma(K)e^{-K/\theta}dK
\]
(\(\mu_\epsilon=ab/(a+b)\))로 돌아간다. 이는 부모 상대운동 Maxwellian 식과 같으며 double-count 또는 factor2 차이가 없다.

### 4. Boost marginal과 안정한 moments

고정 W의 \(d^3P/P^0\) radial factor는 \(\sqrt{\gamma^2-1}d\gamma\)에 비례한다. \(I(z)=K_1(z)/z\)를 미분하고
\(K_2=K_0+2K_1/z\)를 적용하면
\[
-I'/I=K_2/K_1=G,\qquad I''/I=1+3G/z=G_2.
\]
원문의 gamma law와 두 moments는 맞다.

\(q=Q+K=W-\epsilon_D\)를 쓰면 \(e_*=q-q^2/(2W)\), \(k_*=q^2/(2W)\)다. 따라서 \(e_*+k_*=q\)이고, normal frame의 세 energy 공식은 점별로 \(K_{\rm in}+Q=K_D+E_\gamma\)를 만족한다. \(\langle\nu\rangle=0,\langle\nu^2\rangle=1/3\)인 회전 평균 후
\[
\operatorname{Var}(E_\gamma|W)=
e_*^2\{G_2-G^2+(G_2-1)/3\}
=e_*^2(G_2-G^2+G/z)
\]
가 된다. \(\operatorname{Var}(K_{\rm in}|W)=W^2(G_2-G^2)\)도 맞다.

총 variance를 conditional variance와 conditional mean의 centered spread 합으로 계산하는 것은 큰 raw second-moment subtraction을 피한다. 큰 z에서 \(G-1\), \(K_1/K_2-1\), \(G_2-G^2\)의 coefficient-level exact cancellation을 먼저 수행하는 수치 설계가 적절하다. 다만 6차 유한 polynomial은 asymptotic approximation이므로 actual reference와 frozen finite comparisons 전에는 수치 PASS가 아니다.

### 5. Particle/energy owner와 caloric source

Thermal/fast incidence \(h-2,1-h\), free-electron incidence0와 isotope/nuclear charge 보존은 source-native atomic-equivalent pool 안에서 일관된다. 두 radiation route는 exclusive하고, six energy columns의 합은 같은 joint measure의 closure에서 0이다.

\(U_{\rm th}=\sum n_i u_i(T)\)를 미분해 composition term을 분리하면
\[
C_V\dot T/R=-\langle K_{\rm in}\rangle+u_n+u_H+
h(\langle K_D\rangle-u_D).
\]
Q를 별도 heat로 더하지 않는 sign이 맞다. h=1은 instantaneous caloric birth model이고 stopping 결과가 아니다. R과 \(C_V\)를 지정하지 않고 forcing/event만 반환하는 API 경계도 올바르다.

Fixed source window는 T-independent kernel condition을 만족한다. 따라서
\(\theta\,d\log\kappa_{\cal D}/d\log T=\langle K_{\rm in}\rangle-u_n-u_H\)
에 moving-boundary correction이 필요 없다. 해당 식을 unprovided full thermal rate의 derivative로 승격할 수는 없다.

## 실행 전 명료화 및 교정 확인

### R6-C01 — T guard와 FD satellite 정의역

- **대상:** CONTRACT physical_model.T_K, numerical_plan.FD, acceptance.guards.
- **근거:** Primary 목록 최대값은 1e8K이나 frozen control은 \(1e8\exp(2^{-8})\)K도 요구한다. 숫자 T domain을 이 목록의 closed min/max로 읽으면 자기 검증 입력을 거부하게 된다.
- **영향:** 구현 계약의 모호성. 본 이론식을 반박하거나 목표 정확도를 바꾸는 사항은 아니다.
- **최소 교정:** 네 값은 primary sample points라고 명시하고, 숫자 API의 유효조건을 finite T>0와 모든 필요한 single-species/pair \(z\ge10^5\)로 쓰거나, primary+FD satellites를 포함한 정확한 허용집합을 명시한다. 이론의 T>0와 수치 검증된 sample 범위는 별도로 유지한다.
- **교정 확인:** revision 2는 네 온도를 `primary_T_K`로 명명하고 수치 입력 범위를 [255, 101000000]K로 명시했다. FD는 10000K와 100000000K 주위의 네 satellite에만 적용되므로 모두 이 범위 안에 있다. 모든 single-species/pair z에 finite 및 z≥1e5 guard를 추가하고, API 범위와 실제 검증 sample을 구별했다.
- **상태:** CLOSED_VERIFIED. 목표 정확도나 과학 입력 변경 없이 해소.

### R6-C02 — 유한 Bessel polynomial 표기의 등호

- **대상:** CONTRACT numerical_plan.scaled_bessel.
- **근거:** 현재 문자열의 등호는 finite terms0..6를 exact Bessel identity처럼 읽을 수 있다. 이론 원문에는 이미 \(\sim\)와 scoped approximation 설명이 있다.
- **최소 교정:** 해당 계약 문자열도 “truncated asymptotic approximation” 또는 \(\approx\)로 표시한다.
- **교정 확인:** revision 2는 “approximately”, “scoped tested asymptotic evaluation”, “no general Bessel production certificate”를 명시했다.
- **상태:** CLOSED_VERIFIED.

## Root symbolic 근거 readback

Root가 예산 안에서 수행한 단일 Wolfram 호출의 `theory/WOLFRAM_REFERENCE.wl`, `WOLFRAM_RAW.json`, `WOLFRAM_RESULT.json`을 직접 읽었다. 반환 결과는 formal residual 12개가 각각 정확한 문자열 0이고 all_zero=true다. Body wall 1.043754s, tool wall 9.957s이며 반환에 warning text는 관찰되지 않았다. 이 검사는 angular normalization/rotation, energy closure, Bessel moment identities, variance polynomial 선행 계수 및 photon second-moment algebra를 지지한다. 실제 153절점 positivity, thermal integration accuracy, 수치 API guards 또는 continuum bound는 이 호출이 검증한 것이 아니다. 검토자 자신의 Wolfram 호출과 과학 실행 수는 계속 0이다.

## 이후 C9 확인할 사항

실제 code source, 원 raw parser, bounds/guards, array interpolation, coefficient polynomial의 leading cancellation, underflow count, native interval omission 여부를 읽는다. Rate/moment/owner 결과, 16–32 비교, FD control 및 독립 kve/adaptive reference를 raw 기준으로 확인한다. Conditional large-boost algebra control의 scaled tolerance와 thermal eV absolute closure 기준을 구현에서 명료히 구분했는지도 확인한다. 새로운 수치 실행은 root가 동결한 worker/lease/budget 밖에서 수행하지 않는다.

전체 physical uncertainty, continuum quadrature/global error, bare-network admission, stopping, ODE, production 상태는 계속 OPEN/NOT_ISSUED다.

