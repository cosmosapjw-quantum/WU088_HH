# PHYS88 — 원자 질량 규약에서 bare capture로의 조건부 연결

## 이번 결과와 적용 범위

같은 source 사건의 원자 등가 질량을 bare 핵 질량으로 재표기할 때 필요한 signed four-vector carrier를 구성한다. 이어서 원 ENDF kernel을 명시한 에너지 좌표에서 전송한다는 가정 아래, bare \(n+p\to d+\gamma\) 사건과 공통 온도에서의 유한 구간 반응 선택 moments를 새로 구성한다. **재표기된 기존 사건**과 **새로 생성한 bare 사건**은 서로 다른 함수와 출력으로 구분한다.

PHYS85의 입자·열/fast·photon 소유권, PHYS86의 Jüttner 사건 measure와 caloric identity, PHYS87의 원 ENDF 보간·양성성과 회전 평균 정리를 재사용한다. 기존 numerical campaign과 완료 identity는 다시 실행하지 않는다. 이번 새로운 요소는 질량 규약 분해, covariant carrier, 두 조건부 에너지 사상, 그 사상에서 bare 질량을 사용하는 새 finite-window numerical supplier다. 이는 보편적인 불가능 정리나 새 physical uncertainty certificate가 아니다.

## 1. 원전과 기호

Metric은 \((-+++)\)다. 같은 normal orthonormal frame에서
\[
q^\mu=(E,c\mathbf p)=\epsilon U^\mu,\qquad
\epsilon=mc^2,\quad U^\mu=(\gamma,\gamma\boldsymbol\beta),
\quad q^2=-\epsilon^2,\quad U^2=-1.
\]
아래 수치 energy는 eV, 단면적은 cm², \(c=29979245800\) cm/s,
\(\theta=k_BT\)이며 \(k_B/(1\,{\rm eV})\)는 exact SI 상수들의 비를 사용한다.
\(\hbar\)를 1로 놓지 않는다. 이 운동학·고전 분포 식에는 \(\hbar\)가 남지 않으며,
quantum scattering 정보는 원 평가 \(\sigma,a_\ell\)에 포함된다.

동결된 bare rest energies를 \(a=\epsilon_n,b=\epsilon_p,d=\epsilon_d\), electron을 \(e=\epsilon_e\)라 한다. PHYS81/85에서 온 표시된 CODATA2022 값을 유지한다. ENDF의 source-native 질량을
\[
h=AWR\,a,\quad AWR=0.9991673,\quad
Q_S=2224648\ {\rm eV},\quad D=a+h-Q_S,
\]
\[
M_S=a+h,\quad M_b=a+b,\quad Q_b=a+b-d=2224566.37\ {\rm eV}
\]
로 정의한다. 이는 ENDF 평가가 CODATA2022 절대 질량을 사용했다는 주장이 아니다.

ENDF-102(2023) §0.5.1.1은 AWR target의 atomic mass와 light-product AWP의 nuclear mass를 구별한다. §3.1의 incident energy는 LAB이며, §3.3.2의 Q에는 atomic convention을 사용한다. Appendix E.21의 residual mass는 입력 mass와 Q에서 구성한다. 원 MF6 photon field2223300eV와 recoil AWP1.996256은 보존된 metadata이며 독립적인 추가 deposit 또는 서로 다른 Q 제약으로 끼워 넣지 않는다. [S1,S2]

Canonical MF1은 n-p capture 및 inverse photodisintegration을 포함한 N-N R-matrix analysis를 명시한다. 이는 아래 LAB_ANCHORED 선택의 근거지만, 전자 final state의 branching 또는 atomic/bare 단면적 동일성의 오차를 제공하지 않는다. [S2]

## 2. 질량·전자 결합·규약 잔차의 분해

NIST ASD5.12의 H/D ground \(1s\,{}^2S_{1/2}\) 결합 에너지를 양수 \(B_H,B_D\)로 쓴다. 두 종류의 차이를 구별한다:
\[
\Delta_H=h-b,\qquad \Delta_D=D-d,
\]
\[
\rho_H=h-(b+e-B_H),\qquad
\rho_D=D-(d+e-B_D).
\]
그러면
\[
\Delta_H=e-B_H+\rho_H,\qquad
\Delta_D=e-B_D+\rho_D
\]
이고,
\[
\boxed{Q_S-Q_b=\Delta_H-\Delta_D
       =B_D-B_H+\rho_H-\rho_D.}\tag{1}
\]
전자 수1→1이므로 \(e\)가 상쇄된다. \(81.63\)eV는 좌변 전체이며,
전자 isotope binding shift만을 뜻하지 않는다. \(\rho\)는 선택된
표시 mass/Q 규약의 정의상 잔차다. physical error draw나 confidence interval이 아니다.

실제 수신한 ASD rendered primary rows는
\(B_H=13.598434599702\)eV,
\(B_D=13.602134636569\)eV, 각각 표시 uncertainty
\(0.000000000012\)eV, reference HDEL이다. [S3]
원 HTTP bytes는 직접 접근403으로 얻지 못했다. Exa의 실제 rendered 원전 응답과 그 SHA를 보존하며, 이를 server-byte readback이라고 쓰지 않는다.
Exact rational 계산은 이 decimal token들에 대한 항등식이다.
CODATA mass들의 상관관계나 ASD uncertainty의 독립성을 가정하지 않는다.

별도로 실제 전자 상태 \(i,j\)가 주어진 neutral bound-to-bound channel이면
\(Q_{ij}=Q_b+B_{D,j}-B_{H,i}\)다. 자유 electron을 내는
\(n+H_i\to d+e+\gamma\)라면 rest-mass Q는 \(Q_b-B_{H,i}\)이고,
electron kinetic energy와 three-body momentum이 필요하다.
현재 ENDF 입력은 이 전자 분기들을 제공하지 않으므로 그 확률을 만들지 않는다.

## 3. 같은 trajectory의 재표기와 공변 carrier

원 source 사건은
\[
q_n+hU_H=DU_D+k
\]
를 만족한다고 하자. \(q_n,k,U_H,U_D\)를 유지하면서 bare labels
\(bU_H,dU_D\)를 도입하면 bare 부문의 outgoing-minus-incoming은
\[
dU_D+k-(q_n+bU_H)
=\boxed{\Delta_H U_H-\Delta_D U_D}\equiv C^\mu.\tag{2}
\]
따라서 signed internal/convention reservoir에 \(-C^\mu\)를 기록하면
전체 네 성분의 합은0이다. 특히
\[
C^0=\Delta_H\gamma_H-\Delta_D\gamma_D,\qquad
\mathbf C=\Delta_H\gamma_H\boldsymbol\beta_H
-\Delta_D\gamma_D\boldsymbol\beta_D.\tag{3}
\]
일반적인 사건에서 \(C^0\ne Q_S-Q_b\), \(\mathbf C\ne0\)이다.
Bare로 재표기한 kinetic energies에 대해서도
\[
K_{d,b}+E_\gamma-K_{{\rm in},b}-Q_b=C^0.\tag{4}
\]

이 reservoir는 signed accounting object다. 독립적인 on-shell electron,
positive heat source, thermal bath, stopping law 또는 응력 텐서가 아니다.
실제 전자/물질 reservoir를 모델링하려면 그 분포와 소유권을 추가로 공급해야 한다.
Same-frame signed four-vector 합을 먼저 검사하며, norm으로 부호를 지우지 않는다.
Same-trajectory 재표기는 species-off 인과 실험이 아니다.

## 4. 별도의 bare 사건 생성

Bare incoming \(q_n,q_p\)를 주고
\[
P_b=q_n+q_p,\quad W_b=\sqrt{-P_b^2},\quad
K_b=W_b-M_b,\quad
E_b=-q_n\cdot(q_p/b)-a
={W_b^2-M_b^2\over2b}
\]
로 정의한다. \(E_b\)는 proton rest frame의 neutron kinetic energy다.
가까운 질량의 차를 빼지 않고
\[
K_b={2bE_b\over \sqrt{M_b^2+2bE_b}+M_b}
\]
로 계산한다.

\(q_b=Q_b+K_b\)와 COM photon direction \(\hat n\)에 대해
\[
e_*={q_b(2W_b-q_b)\over2W_b},\qquad
k_{d*}={q_b^2\over2W_b},
\]
\[
k_*^\mu=(e_*,e_*\hat n),\qquad
q_{d*}^\mu=(d+k_{d*},-e_*\hat n).
\tag{5}
\]
Bare pair의 \(P_b/W_b\)로 두 출력을 같은 normal frame에 boost한다.
그러면
\[
q_n+q_p=q_d+k,\qquad q_d^2=-d^2,\quad k^2=0,
\quad K_{\rm in}+Q_b=K_d+E_\gamma.\tag{6}
\]
이는 닫힌 새로운 bare 사건이며 식(2)의 carrier를 더하지 않는다.

## 5. 원 kernel의 두 조건부 사상

### LAB_ANCHORED

\[
E_S=E_b,\qquad
\sigma_b(E_b)=\sigma_S(E_S),\qquad
a_{\ell,b}(E_b)=a_{\ell,S}(E_S).\tag{7}
\]
원 incident LAB label과 incoming-neutron COM axis에 대한 정규화 angular law를 같이 전송한다:
\[
f(\mu|E_S)={1\over2}
[1+3a_1(E_S)\mu+5a_2(E_S)P_2(\mu)].
\]
이는 명시적인 kernel-transfer 가정이다. 식(5)의 운동학만으로 (7)을 증명하지 않는다.

### FIXED_COM_K

\[
K_b(E_b)=K_S(E_S),\qquad
E_S={K_b(2M_S+K_b)\over2h},\qquad
K_S(E_S)={2hE_S\over\sqrt{M_S^2+2hE_S}+M_S}.\tag{8}
\]
동일한 \(\sigma_S,a_{\ell,S}\)를 이 \(E_S\)에서 평가한다.
\(W_S=M_S+K_b\)일 때
\[
{dE_S\over dE_b}={bW_S\over hW_b}>0,\qquad
E_b={K_S(2M_b+K_S)\over2b}.\tag{9}
\]
따라서 native endpoints와 knots의 pullback이 잘 정의된다.
Bare LAB support는 LAB_ANCHORED의 support와 다르므로 출력 metadata에 따로 적는다.

Cross section은 energy에 대한 확률밀도가 아니다.
\(\sigma_S(E_S(E_b))\)에 \(dE_S/dE_b\)를 곱하지 않는다.
비선형 사상 뒤의 \(E_b\) knots에서 원 INT flags를 재사용해 새로 보간하면
다른 represented function이 된다. 언제나 native \(E_S\)에서 원 보간기를 호출한다.

두 모형의 차이는 선택한 전송 가정과 그 유한 구간의 민감도다.
Physical charge-state uncertainty, confidence interval 또는 두 값 사이 실제 결과의 경계가 아니다.
이번 범위에는 fixed-amplitude 등 세 번째 전송 가정을 넣지 않는다.

## 6. Bare finite-T measure와 Jacobian

공통-T, drift0, 등방 classical Maxwell-Juttner \(n,p\)를 사용한다.
Bare phase-space flux, normalization, pair mass와 boost를 모두 새 bare 값으로 쓴다.
PHYS86/87의 invariant reduction은 서로 다른 두 질량에도 적용되며,
고정 total momentum에서 incoming COM axis의 회전 평균이 normalized
angular law를 absolute photon direction의 uniform law로 바꾸는 논증을 재사용한다.
Directed conditional angular source 자체를 등방 자료로 바꾸지는 않는다.

\[
\lambda_b(K)=K(2M_b+K)(4ab+2M_bK+K^2),\qquad
\widetilde K_\nu(z)=e^z K_\nu(z).
\]
Native \(x=\log E_S\)를 적분 변수로 쓰면
\[
J_{\rm LAB}={dK_b\over dx}={bE_S\over W_b},\qquad
J_{\rm COM}={dK_b\over dx}={hE_S\over W_S}.\tag{10}
\]
정확히 같은 native153knots/152cells에서 각 사상의
\[
w(x,T)=\sigma_S(E_S)\lambda_b(K_b)
 \widetilde K_1(W_b/\theta)e^{-K_b/\theta}J_{\rm map}
\]
를 계산한다. 유한 구간 rate coefficient는
\[
\kappa_{\rm map}(T)=
{c\int w\,dx\over
 4a^2b^2\theta\,\widetilde K_2(a/\theta)\widetilde K_2(b/\theta)}.
\tag{11}
\]
단위는 cm³/s이며 실제 event rate는 별도로
\(R=n_n n_p\kappa_{\rm map}\)를 공급할 때 정의된다.
현재 density나 coupled trajectory를 만들지 않는다.
Native support 밖의 자료를0으로 연장한 full rate라고 해석하지 않는다.

Positive normalized measure \(w\,dx/\int w\,dx\)에서
\[
G={K_2(z)\over K_1(z)},\quad G_2=1+{3G\over z},\quad z=W_b/\theta,
\]
\[
m_{\rm in}=K_b+W_b(G-1),\quad
m_\gamma=e_*G,\quad
m_d=k_{d*}+(W_b-e_*)(G-1).\tag{12}
\]
각 \(K_b\)에서 \(m_{\rm in}+Q_b=m_d+m_\gamma\)이고 전체 평균에서도 보존된다.
조건부 variance는
\(v_\gamma=e_*^2(G_2-G^2+G/z)\),
\(v_{\rm in}=W_b^2(G_2-G^2)\)이며,
PHYS87의 centered variance/covariance 식을 bare values로 적용한다.
큰 raw second moment 두 개를 마지막에 빼지 않는다.

사상과 support가 T-independent이므로
\[
\theta {d\log\kappa_{\rm map}\over d\log T}
=\langle K_{\rm in}\rangle-u_n-u_p,\qquad
u_i=\epsilon_i(K_1/K_2-1)+3\theta.\tag{13}
\]
사상에 다른 source-coordinate Jacobian을 넣으면 rate와 reaction-selected moments가 달라지므로 별도 독립 구현으로 판별한다.

## 7. 입자 수·열/fast·radiation 소유권

\(h_{\rm birth}=0,1\)은 daughter의 fast/instantaneous thermal-birth 선택이다.
Bound electron을 실제로 ionize하는 과정은 여기 포함하지 않는다.
Bare 반응의 baryon number와 nuclear charge는 보존되고, free electron incidence는0이다:
\[
\Delta N_{\rm thermal}=h_{\rm birth}-2,\qquad
\Delta N_{\rm fast}=1-h_{\rm birth},\qquad\Delta N_e=0.
\]
Disjoint energy columns는
\[
(h_{\rm birth}\langle K_d\rangle-\langle K_{\rm in}\rangle,\ 
 (1-h_{\rm birth})\langle K_d\rangle,\ -Q_b,\ 0,\ 
 E_{\gamma,\rm handoff},E_{\gamma,\rm escape}).\tag{14}
\]
Photon route는 둘 중 하나만 소유한다. 합은0이며 Q를 heat로 다시 더하지 않는다.
\[
{C_V\dot T\over R}=-\langle K_{\rm in}\rangle+u_n+u_p
+h_{\rm birth}(\langle K_d\rangle-u_d).\tag{15}
\]
\(h_{\rm birth}=1\)은 모형 선택이며 fast stopping 완료 근거가 아니다.
전체 reacting gas의 \(\pi=0\), collisionless DM의 \(\pi_m\) 별도 취급을 유지한다.

## 8. 구현·판별 계획

두 사상×4T×GL16/32의16개 새 bare full integrals, 최고 T의
두 사상×logT ±\(2^{-8}\)의4개 scalar rate integrals를 한 primary child에서 수행한다.
새 cross-convention source-relabel18cases와 bare event36cases, owner32rows를 같은 동결 identity에 결속한다.
동일 T의 parent native 수치는 저장 RESULT/CSV에서 읽어 비교하며 parent integrator를 호출하지 않는다.

새 independent child는 원 ENDF를 별도 parser로 읽고 scipy kve/adaptive quadrature로
\(T=10^8\)K에서 두 사상의 rate·세 energy means를 계산한다.
Primary source/algorithm은 import하지 않는다.
별도 parent 양성성 campaign은 재실행하지 않고 고정 witness와 사상의 단조성 논증을 쓴다.

선택된 z≥\(10^5\)에서 기존6term scaled-Bessel utility를 재사용한다.
차분/variance의 cancellation은 exact coefficient 단계에서 처리한다.
한 번의 Wolfram symbolic call은 mass identity, carrier component identity,
both Jacobians, two-body shell/conservation, monotone derivative를 exact 식으로 검산한다.
모든 numerical tolerances와 resource caps는 CONTRACT.json에 동결했다.
Numerical residual은 이 유한 사례와 represented source에서의 결과이며 continuum certificate가 아니다.

## 9. 이론에서 닫는 의무와 남는 다음 입력

이 작업이 완료되면 mass/convention 회계, covariant relabel ledger,
조건부 bare constructor와 finite-window supplier child를 COMPLETE_SCOPED로 닫을 수 있다.
원래 NUCLEAR_ATOMIC_TO_BARE_CAPTURE_REMAP과 physical supplier 부모는 PARTIAL로 남긴다.
다음 첫 의무는 **NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT**다:
같은 channel/energy/angular convention의 physical bare kernel 적합성·uncertainty,
필요 support/tail, 실제 열/fast consumer와 radiation owner를 결속해야 한다.
실제 network rate와 fast-product stopping 활성화는 그 뒤다.

HH_R10=OFF, production admission NOT_ISSUED다.
R1–R10 workflow의 R10과 HH_R10 flag는 다른 이름공간이다.

## 원전

- [S1] CSEWG, ENDF-6 Formats Manual, BNL-224854-2023-INRE(2023), §0.5.1.1, §3.1/3.3.2, §6.2.4, Appendix E.21. <https://www.nndc.bnl.gov/endfdocs/ENDF-102-2023.pdf>. Parent가 받은 원 PDF SHA6da0d63d42d477eb8e832249e032112a3b4a226a9c4acffe1d7ffb4abb41e06b 재사용.
- [S2] NNDC ENDF/B-VIII.1 n-001_H_001.endf, MF1/451, MF3/102, MF6/102. <https://www.nndc.bnl.gov/endf-data/ENDF/ENDF-B-VIII.1/n-001_H_001.endf>. 원 SHA3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af.
- [S3] NIST ASD5.12(2024), H/D ground ionization energies, HDEL. <https://physics.nist.gov/asd>. 실제 full-table URL과 rendered raw response는 SOURCE_CONTRACT.json/intake receipt에서 결속.
- [S4] NIST CODATA2022 complete constants. <https://physics.nist.gov/cuu/Constants/Table/allascii.txt>. Parent bare tokens와 같은 n/p/d 및 electron displayed value를 실제 web text로 대조.
- [S5] Mohr et al., CODATA Recommended Values…2022, arXiv:2409.03787v1, §II Eq(1)–(2), neutron capture mass relation. <https://arxiv.org/html/2409.03787v1>. Atomic ionization-energy mass relation의 독립 원전; 종합 binding-energy 추정치로 parent bare mass token을 교체하지 않음.
