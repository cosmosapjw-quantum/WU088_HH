# PHYS86: 같은 normal frame의 반응 선택 에너지와 열용량

## 결과와 적용 범위

PHYS85의 정확한 capture 사건 회계에 온도 의존 사건 measure를 연결한다. 핵반응 단면적의 실제 공급, daughter stopping, photon 재흡수, ODE 활성화는 이 단위의 입력이 아니다. 이번 구성은 그 공급자가 만족할 식과 검증 가능한 참조 구현이다. 기존 PHYS85의 완료된 유도는 재사용하며, 미완료 참조 실행은 별도의 출력 전송 계약으로 첫 완전 검증을 시도한다.

같은 normal orthonormal frame에서 두 열적 반응물의 분포가 공통 온도 T의 독립적인 고전 Maxwell–Jüttner 분포이고, 미시 반응 kernel이 T에 명시적으로 의존하지 않으면

\[
\langle K_{\rm in}\rangle_R=u_a(T)+u_b(T)+k_B T^2\partial_T\log\kappa(T).
\tag{1}
\]

\(u_i\)는 species i의 열적 입자 한 개당 평균 운동에너지다. 같은 조건에서 빠른 daughter가 모두 thermal inventory 밖에 태어나면 반응에 의한 온도 source는

\[
C_V\dot T\big|_R=-R k_B T^2\partial_T\log\kappa(T),\qquad
C_V=\sum_i n_i u_i'(T)>0.
\tag{2}
\]

열적 daughter membership \(h\in\{0,1\}\)를 명시적으로 선택하는 경우에는

\[
C_V\dot T\big|_R=-Rk_BT^2\partial_T\log\kappa
+R\langle h[K_c-u_c(T)]\rangle_R.
\tag{3}
\]

이 식은 단일 reaction source의 국소 열적 moment closure다. 순간적으로 Maxwell–Jüttner 모양을 유지하는 재열평형 가정을 쓴다. expansion/shear work와 transport는 전체 fluid 방정식에 별도로 결합한다. 고전 희박 기체, 고정 species/rest masses/internal states, 양의 T와 C_V, 유한한 0차–2차 사건 에너지 moments, 적분 미분 교환을 보장하는 국소 지배함수를 가정한다. 양자 점유, stimulated emission, plasma screening의 명시적 T 의존성, drift와 thermal shape distortion은 아래 보정식 또는 별도 공급자 계약의 대상이다. 수학적 고온 극한은 종수 고정 이상기체의 극한이며 실제 bare-nucleus plasma의 물리적 유효영역을 발급하지 않는다.

## 1. Frame, flux, 분포

Metric은 (-,+,+,+), \(p_i^\mu=(E_i/c,\mathbf p_i)\), \(\epsilon_i=m_i c^2\), \(E_i=\sqrt{\epsilon_i^2+c^2|\mathbf p_i|^2}\). Normal frame의 bulk velocity는 0이다. \(c,\hbar,k_B\)를 자연단위로 놓지 않는다. 여기서 \(\beta_T=1/(k_BT)\)는 역에너지이며 PHYS85 boost의 \(v/c\)와 다르다.

\[
f_i(\mathbf p;T)=Z_i^{-1}e^{-\beta_T E_i},\quad
Z_i=\int d^3p\,e^{-\beta_TE_i}
=4\pi m_i^2 c k_BT K_2(z_i),\quad z_i=\epsilon_i/(k_BT).
\tag{4}
\]

이 f는 \(d^3p\)에 대해 1로 정규화한다. 고정 spin degeneracy와 \((2\pi\hbar)^{-3}\)를 상태밀도에 함께 넣어도 정규화에서 상쇄되므로 생략한 상수는 물리적 단위설정이 아니다. \(n_i f_i\)가 이 frame의 particle momentum density다.

정규화는 \(p=mc\sinh\chi\)로 직접 확인할 수 있다. \(\sinh^2\chi\cosh\chi=(\cosh3\chi-\cosh\chi)/4\)와 \(K_3-K_1=4K_2/z\)를 쓰면 \(Z=\pi m^3c^3(K_3-K_1)=4\pi m^3c^3K_2/z\)가 되어 (4)와 일치한다.

\(D=-c^2 p_a\cdot p_b=E_aE_b-c^2\mathbf p_a\cdot\mathbf p_b>0\)를 쓰면 실제 상대속도와 normal-frame rate의 flux factor는

\[
v_{\rm rel}=c\frac{\sqrt{D^2-\epsilon_a^2\epsilon_b^2}}D,\qquad
\bar v=\frac{D}{E_aE_b}v_{\rm rel}.
\tag{5}
\]

\(\bar v\)는 흔히 Møller velocity라고 부르는 flux factor다. 독립적인 invariant relative speed로 취급하지 않는다. 실제 frame의 \(d^3p_a d^3p_b\) 평균에서는 \(\sigma\bar v\)가 정확한 kernel이다. Cannoni의 invariant 식 (74)의 \(D/(E_aE_b)\)를 보존한 표현이며, \(\sigma v_{\rm rel}\)만을 정규화된 두 f에 평균하는 표현과 구별한다. Source는 differential cross section과 최종 branch/angle measure를 같은 사건으로 제공해야 한다.

사건 변수 \(x=(\mathbf p_a,\mathbf p_b,\omega)\), 고정 measure \(d\lambda\), 총 incoming energy \(S=E_a+E_b\), T-independent kernel \(B(x)\ge0\)를 정의한다. \(B\)에는 위 flux와 미시 단면적/정규화 branch measure가 들어간다. 물리 supplier가 없는 참조 모델에서는 B가 명시적으로 constructed kernel임을 기록한다.

\[
N(\beta_T)=\int B e^{-\beta_TS}d\lambda>0,
\quad\kappa=\frac{N}{Z_aZ_b},\quad
dP_R=\frac{B e^{-\beta_TS}}N d\lambda,
\quad R=\frac{n_an_b}{1+\delta_{ab}}\kappa.
\tag{6}
\]

\(R\)은 사건 수/(proper volume·normal proper time), \(\kappa\)는 volume/time이다. 본 capture 세 채널은 a≠b다. 동일 입자를 확장할 때 대칭계수 1/2와 두 반응물의 stoichiometric debit을 함께 적용한다.

## 2. 선택 평균과 rate 기울기: 직접 유도

정의 (6)를 미분하면 \(-\partial_{\beta_T}\log N=\langle S\rangle_R\), \(-\partial_{\beta_T}\log Z_i=\bar E_i\)다. 따라서

\[
-\partial_{\beta_T}\log\kappa
=\langle S\rangle_R-\bar E_a-\bar E_b.
\tag{7}
\]

\(d\beta_T/dT=-1/(k_BT^2)\), \(K_{\rm in}=S-\epsilon_a-\epsilon_b\), \(u_i=\bar E_i-\epsilon_i\)를 대입하면 (1)을 얻는다. 이 유도는 COM/relative motion의 비상대론적 독립 분해를 요구하지 않는다. Exact normal-frame event kinematics와 동일한 energy variable을 쓴다.

평형 분포를 따르는 고정 species의 thermal kinetic energy density가 \(U_{\rm th}=\sum_i n_i u_i(T)\)이면

\[
\dot U_{\rm th}\big|_R=C_V\dot T\big|_R+\sum_i u_i\dot n_i\big|_R.
\tag{8}
\]

PHYS85 사건 소유권을 같은 \(P_R\)에 평균하여 \(\dot U_{\rm th}|_R=R[-\langle K_{\rm in}\rangle_R+\langle hK_c\rangle_R]\), \(\sum_i u_i\dot n_i|_R=R[-u_a-u_b+\langle h\rangle_Ru_c]\)를 얻는다. (1)을 (8)에 넣으면 (3)이 성립한다. h=0인 (2)는 이 식의 정확한 특수 경우다. h=1은 명시적 instantaneous caloric birth model이며 stopping 유도가 아니다. 모든 핵 수·전하 및 nuclear rest, thermal, fast, radiation/escape 소유권은 PHYS85 사건 회계를 유지한다.

## 3. Covariance, 곡률, 온도에 의존하는 kernel

T-independent 관측량 \(\phi(x)\)에 대해 \(\langle|\phi|\rangle_R\), \(\langle|\phi S|\rangle_R\)가 유한하고 해당 미분·적분 교환이 지배가능하다고 가정하자. 정규화된 평균을 직접 미분하면

\[
\partial_T\langle\phi\rangle_R
=\frac{\operatorname{Cov}_R(\phi,S)}{k_BT^2}.
\tag{9}
\]

이를 \(\phi=S\)에 적용하거나 (7)을 다시 미분하여

\[
\partial_{\beta_T}^2\log\kappa
=\operatorname{Var}_R(S)-\operatorname{Var}_a(E_a)-\operatorname{Var}_b(E_b)
\tag{10}
\]

를 얻는다. 따라서 variance 공급자와 fitted rate curvature의 일관성을 검사할 수 있다. 양의 event measure에서 (10)의 우변에 thermal variance를 다시 더한 값은 음수가 될 수 없다. 이는 같은 고정 measure·T-independent kernel에 대한 consistency test이고 새로운 보편적 strong no-go/문헌 신규성 주장은 하지 않는다.

\(B=B_T\)이면 \(A_T=N^{-1}\int(\partial_TB_T)e^{-\beta_TS}d\lambda\)를 정의한다. 이 정의는 B=0에서 log를 나누지 않는다. 국소 지배가능 미분을 가정하면

\[
\langle K_{\rm in}\rangle_R=u_a+u_b+k_BT^2[\partial_T\log\kappa-A_T],
\tag{11}
\]

이고 (3)의 rate-slope에도 같은 차이를 쓴다. Screening/branch population/stimulated source를 넣을 때 이 보정을 생략하면 rate 변화가 kinetic selection으로 잘못 배정된다. \(\phi_T\) 및 \(B_T\)의 일반 평균 미분에는 각각 \(\langle\partial_T\phi\rangle_R\)와 \(N^{-1}\int(\phi-\langle\phi\rangle_R)(\partial_TB_T)e^{-\beta_TS}d\lambda\)가 추가된다. 후자는 B>0인 곳에서의 score 표현 \(\operatorname{Cov}_R(\phi,\partial_T\log B)\)을 B=0에서 나눗셈 없이 확장한다. 본 새 구현의 기본 경로는 고정 kernel이고 T-dependent fixture는 (11)의 판별 검사다.

## 4. 정확한 열용량과 PHYS85 극한

\(r(z)=K_1(z)/K_2(z)\)와 Bessel recurrence를 쓰면 \(r'=r^2+3r/z-1\). (4)의 미분으로

\[
u_i=\epsilon_i[r(z_i)-1]+3k_BT,
\qquad
\frac{u_i'(T)}{k_B}=3+z_i^2-z_i^2r(z_i)^2-3z_ir(z_i).
\tag{12}
\]

양성성은 \(u_i'(T)=\operatorname{Var}_i(E_i)/(k_BT^2)>0\)에서도 직접 따른다. 식 (12)의 큰 z에서 큰 항의 소거가 있으므로 부동소수점 production 구현에는 안정한 Bessel ratio/asymptotic 경로가 별도로 필요하다. 이번 참조는 기호 미분 및 고정 finite algebraic witnesses이고 그 production 수치 구현을 채택하지 않는다.

비상대론적 \(z_i\to\infty\)에서 \(u_i\to3k_BT/2\), \(C_V\to3N_{\rm th}k_B/2\). (2)는 PHYS85의

\[
\dot T|_R=-\frac{2RT}{3N_{\rm th}}\frac{d\log\kappa}{d\log T}
\tag{13}
\]

로 돌아간다. 형식적 \(\sigma\propto K^s\), s>−2의 비상대론적 witness에서 slope=s+1/2, constant σ의 source는 −RT/(3N_th), inverse-speed의 source는 0이다. 기존 PHYS85 witness 유도와 검증 입력을 재사용한다. 초상대론적 고정종수 이상기체의 형식적 \(u_i'\to3k_B\) 극한도 (12)의 식 자체로 얻는다.

## 5. 코딩 계약과 판별 입력

새 supplier interface는 event energy에서 얻은 moments와 thermal partition moments를 분리해 받는다. \(\bar S_R,\operatorname{Var}_R(S),\bar E_a,\bar E_b,\operatorname{Var}_a(E_a),\operatorname{Var}_b(E_b)\)로 (7),(10)을 계산하고, 같은 사건의 \(\langle hK_c\rangle_R,\langle h\rangle_R\)로 (3)을 계산한다. Rate의 실제 값이나 T derivative를 임의로 채우지 않는다. \(N=\kappa=0\)에서는 정규화된 event measure와 log rate가 정의되지 않으며 source는 0이다. 반면 \(\kappa>0\)이고 반응물 density가 0이어서 \(R=0\)이면 event measure와 log rate는 여전히 정의된다. Source API는 R=0에서 event mean 평가 없이 0을 반환할 수 있다.

최소 reference는 2×2 finite positive exponential-family witness를 쓴다. 이는 Maxwell–Jüttner continuum quadrature가 아니며 공식 supplier data도 아니다. 무차원 inverse-temperature \(b=\epsilon_0/(k_BT)\), one-particle energies \(e_a=(2,3),e_b=(4,6)\), base weights \(a=(1,2),b_w=(2,1)\), reaction kernel matrix \(G=((1,3),(2,4))\)를 고정한다. h matrix \(((0,1),(1,0))\), daughter kinetic observable \(K_c/\epsilon_0=((1,2),(3,5))\)는 covariance와 thermal membership 분리를 판별하는 구성 입력이며 실제 capture 사건 운동학으로 주장하지 않는다. 실제 capture 운동학은 별도 PHYS85 36/6 사건으로 검증한다.

\(q=e^{-b}\)를 변수로 잡으면 \(Z_a=q^2+2q^3\), \(Z_b=2q^4+q^6\), \(N=2q^6+8q^7+3q^8+8q^9\). \(\partial_b=-q\partial_q\)를 쓰면 모든 선택·variance·covariance·kernel 보정 검사는 q=1/2,2/3,3/4에서 정확 유리수다. T-dependent 판별에는 \(G_b=e^{-b}G=qG\)를 써서 정규화 event measure는 유지되고 log rate 미분만 바뀌는 사례를 구성한다. 보정항을 생략한 식은 이 구성 입력에서 실패하고 (11)은 정확히 통과해야 한다.

검증기는 source moment function과 다른 경로에서 partition polynomial을 직접 미분한다. 검증 집계·행 순서·exact rational 원자료와 finite counts를 완전히 수신한 뒤에만 참조 구현을 채택한다. 전체 결과의 어느 단계도 finite-T nuclear cross-section supplier 또는 continuum integration certificate를 발급하지 않는다.

## 원전과 직접 기여

- Chacón-Acosta, Dagdug, Morales-Técotl, arXiv:0910.1625 / Phys. Rev. E 81,021126: 정규화 Jüttner 분포와 covariant/comoving thermodynamic moments. 식(4)의 출처와 frame 연결. https://arxiv.org/html/0910.1625v1
- Cannoni, arXiv:1506.07475v3, Appendix B 식(64),(74)–(81): true relative velocity, flux, 동일입자 계수와 normalized thermal average의 구별. https://arxiv.org/html/1506.07475v3
- Weaver, Phys. Rev. A13,1563 (1976), DOI10.1103/PhysRevA.13.1563: relativistic plasma binary reaction-rate 원전; 이번 직접 fulltext 채택은 Cannoni의 대응식에 한정한다.
- Warshaw, LLNL TDF (2001), DOI10.2172/15006194: 반응률과 product energy moments를 함께 공급하는 맥락; 그 비상대론적 spectra를 본 상대론적 supplier로 대체 채택하지 않는다.
- Wolfram BesselK 공식문서 Applications: relativistic ideal-gas heat capacity 식의 독립 대응. https://reference.wolfram.com/language/ref/BesselK.html

이번 프로젝트의 직접 기여는 표준 정규화·미분 identity를 PHYS85의 같은-frame thermal/fast 사건 소유권, 가변 thermal 입자수, joint retention moment와 연결한 식(1)–(3),(11) 및 그 실행 계약이다. 새로운 보편적 통계역학 정리라는 문헌 신규성을 주장하지 않는다. 모든 NG1–NG7은 새 strong no-go 채택 대상 없음으로 기록한다.
