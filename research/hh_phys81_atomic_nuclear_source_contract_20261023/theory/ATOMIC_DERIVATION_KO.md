# 유한 source CI와 hazard 좌표의 물리 계약

## 1. Source 구간과 딸이온

CCC 원자료는 H1 13.6058–968.61eV(a0²), He ground TICS는 cm², Li ground CGI는 cm²이다. H source lower13.6058과 NIST physical ionization energy는 구별한다. He4는 첫 양의 표본24.6부터60eV까지, Li7은6부터15eV까지의 PL interpolation만 사용한다. 구간 밖 단면적0은 선택한 finite-support operator의 정의다. 미측정 물리 단면적0의 주장이 아니다.

He+의 가장 낮은 들뜬준위2p1/2는40.8130309000eV, He I ionization24.587389011eV이므로 excited-residual channel의 내부 threshold는65.400419911eV다. Li+ 최저1s2s triplet59.020708eV와 Li7 원논문 43487.15940(18)cm^-1의 exact-SI 변환5.39172060034581eV의 합은64.41242860034581eV다. 지정된 상한60/15eV에서 이 daughter excitation은 에너지 보존상 열리지 않는다. Recoil은 lab threshold를 낮추지 않는다. He3/Li6 isotope mapping은 이 계약에 포함하지 않는다.

CI event는 neutral−1, ion+1, free electron+1이다. 모든 outgoing electron과 recoil이 하나의 열 pool로 열화된다는 모델에서 thermal loss는 chemical defect I_s다. Incoming energy mean을 추가 loss로 쓰지 않는다. I_s와 source-window lower는 서로 다른 자료 객체이며 모든 허용 incident E가 I_s보다 크다.

## 2. 재사용할 유한 Maxwell 적분

theta=k_B T(eV), C=100 sqrt(8 eV_J/(pi m_e))일 때
K=C theta^(-3/2) int_a^b E sigma(E) exp(-E/theta)dE.
각 PL cell E=L+h t, sigma=s_l(1-t)+s_r t에서 J_n(y)=int_0^1 t^n exp(-yt)dt, y=h/theta를 쓰면 C22D의 positive endpoint 식을 그대로 재사용한다. Sigma 단위는 최종 cm²로 통일한다. E² sigma moment에는 J_3 하나가 추가된다. dK/dT=K[<E>/theta−3/2]/T이고, finite window는 T-independent다. 이 항등식은 물리 source 오차와 독립인 수학 관계다.

## 3. Neutral hazard 환원

Species s=H1,He4,Li7, 고정 nucleus abundance B_s, 초기 neutral N_s0, ion X_s0를 둔다. 각 새 source의 rate K_s(T)가 species를 공유하지 않으므로 다른 isotope까지 한 좌표로 합치지 않는다.

z_s(t)=−log[N_s(t)/N_s0], N_s=N_s0 exp(−z_s), X_s=B_s−N_s.
이벤트의 공통 전자 피드백으로 dz_s/dt=n_ref x_e K_s(T), x_e=sum_s X_s.
Thermal u=u0−sum_s I_s(X_s−X_s0), N_g=sum_s B_s+x_e,
T=u/(1.5 k_B N_g).

따라서 6 abundance+u의7상태 연속모델을3 hazard 상태로 정확히 표현한다. z=0도 허용된다. expm1을 사용해 작은 ion increment를 보존하고 saturation에서 neutral positivity를 유지한다. 이 표현은 QSS가 아니다.

dT/dz_j=−N_j(I_j+1.5 k_B T)/(1.5 k_B N_g),
J_ij=n_ref[N_j K_i+x_e K'_i dT/dz_j].

Jacobian은 두 outer product의 합이므로 rank≤2다. 부호/차원 및 이항등식을 독립 검토한 뒤 analytic Jacobian을 사용한다. 첫 적분으로 구성한 energy residual은 독립 trajectory 정확도 증거가 아니므로 원래7상태 방정식과 별도 solver/refinement로 비교한다.

## 4. Bell 분석함수 전구간 양성

x=1−I/E in[0,1), F(x)=−A log(1−x)+sum B_j x^j.
(1−x)F'(x)=G(x)=A+(1−x)sum j B_j x^(j−1).
원전 H/He/Li neutral 계수를 정확 유리수로 넣으면 Wolfram Reduce가 각각 [0,1]에서 G≤0인 x가 없다고 반환했다. F(0)=0이므로 E>I에서 F>0이다. 별도의 rational Bernstein subdivision 증명증서를 만들어 exact arithmetic으로 검토한다. 이 명제는 분석함수의 양성만 닫으며 near-threshold experimental uncertainty를 줄였다는 주장이 아니다.

## 독립 검토 후 명시한 조건

Maxwell 평균은 C22D와 같은 stationary-target/electron-mass closure다. 두 움직이는 finite-mass Maxwell 분포의 정확한 충돌계수로 주장하지 않는다. Common T는 공유 thermal pool과 EOS의 조건이다. N_s,X_s,B_s,x_e,N_g는 무차원 abundance/referenceH, n_ref는cm^-3, u는eV/referenceH다. N_s0>0, X_s0>=0, X_s0<B_s, 초기xe>0을 요구한다. Bound-bound excitation/de-excitation과 그 radiative loss도 CI-only 대조계에서 생략한다. 유한z의 분석적 중성양성과 exp(-z)의 binary64 underflow는 구별한다.

Li7 isotope energy는 독립 원전 검토에서 발견한 일반 ASD Li값의 귀속 문제를 교정했다. 바뀐것은 chemical defect와 그에 의존한 energy/Jacobian map이다. 단면적 knot/finite Maxwell rate는 바뀌지 않았다. 해당 원본intake와 교정receipt를 모두 보존했다. NeutralHe4의 새동위원소 원전도 source_data/NEUTRAL_ISOTOPE_PROVENANCE.md에 연결한다.
