# WU R38: Velilla native Born–Oppenheimer 이원자 문턱과 R37 화학경쟁의 source-scoped 연결

## 정의와 전제
원본: Velilla et al., J. Chem. Phys. 129, 084307 (2008), DOI 10.1063/1.2973629의 EPAPS E-JCPSA6-129-612834, SHA-256은 `evidence/PROVENANCE.json`에 고정했다. 충돌률 입력은 González-Lezana, Hily-Blant & Faure, J. Chem. Phys. 157, 214302 (2022), DOI 10.1063/5.0128598의 원본 표를 계승한 R37의 첫 이탈(first-exit) 반응 분기확률이다. 두 입력을 서로 독립적인 산란 계산으로 간주하지 않는다.

원래 Fortran의 `h2(r)`는 핵 좌표 고정된 H₂ electronic Born–Oppenheimer 곡선으로 r은 Bohr, E는 Hartree이다. 핵질량 m_p, m_d로 1차원 radial operator의 고유에너지를 구한다.

\[
\left[-\frac{\hbar^2}{2\mu_{AB}}\frac{d^2}{dr^2}+\frac{\hbar^2J(J+1)}{2\mu_{AB}r^2}+V^{\rm Velilla}_{\rm H_2}(r)\right]u_{vJ}=E_{vJ}u_{vJ},
\quad u(0)=u(\infty)=0.
\]

기본 \(\mu_{\rm H_2}=m_p/2\), \(\mu_{\rm HD}=m_pm_d/(m_p+m_d)\); 핵질량은 원래 R38 보존 계산의 CODATA2022 입력을 그대로 사용한다. Spectral 경로의 출력은 분리 원자 대비 정의로 +1 Hartree 에너지 이동을 적용하고 FD 경로는 절대 전자 에너지를 사용한다. **서로 다른 에너지 0을 직접 비교하지 않고 상태별 에너지 차이만 비교한다.**

## 원본 에너지 전달식
반응 \(\mathrm{H^++HD}(v_i,J_i)\to \mathrm{D^++H_2}(v_f,J_f)\)의 이원자 BO 점근치만으로
\[
\Delta E_{if}=E^{\rm BO}_{\rm H_2}(v_f,J_f)-E^{\rm BO}_{\rm HD}(v_i,J_i),\quad
Q_{if}=-\Delta E_{if},\quad E_{\rm kin,thr}=\max(0,\Delta E_{if}).
\]
\(Q>0\)이면 발열, \(Q<0\)이면 흡열이다. 반응률 재계산이나 열전달량은 아니다. 37,170 cm⁻¹은 Velilla의 H₃⁺ 전자 PES 최소점에서 H⁺+H₂ 점근치까지의 값이고 동위원소 문턱이 아니다.

R37 원본에서 인용한 \(P^{(1)}_{if}\)를 특정 초기 상태/밀도/복사경계의 **첫 종료 사건이 화학반응이며 H₂(J_f)로 진입할 확률**이라 두면,
\[
P_{\rm chem}^{(1)}=\sum_fP^{(1)}_{if},\quad
\langle Q\rangle_{\rm initial}^{(1)}=\sum_fP^{(1)}_{if}Q_{if},\quad
\langle Q\rangle_{\rm chem}^{(1)}=\frac{\sum_fP^{(1)}_{if}Q_{if}}{P_{\rm chem}^{(1)}}.
\]
흡열 분기 조건부 확률은 \(f_{\rm endo}^{(1)}=\sum_{\Delta E>0}P^{(1)}_{if}/P_{\rm chem}^{(1)}\). 본 계산은 R37 확률을 **교체하지 않으며**, 새 이원자 BO 에너지만 이들에 전달한다.

## 출처·결과·유효범위
- Spectral (R38 2026-10-31): 247개 채널, 32개 BO 준위, 2500점 sine pseudospectral 방식. 원본 Fortran h2() 호출.
- FD (R38 2026-10-30): 190개 HD/H₂ 채널, 원본 Velilla h2(), r=0.5–16 Bohr, dr=0.005 Bohr.
- 공통 190채널의 전이 \(\Delta E\) 직접 비교. 19,200개 R37 H₂ 생성물 분기 및 1,920개 첫 이탈 조건에 더 정밀한 source-spectral BO \(Q\)를 연결했다.
- 새로운 문턱은 산란 S-matrix의 문턱 검증 또는 모든 단열/비단열 보정을 포함한 `PHYSICAL_Q_FULL`이 아니다. 질량에 따른 zero-point shift와 rotational-vibrational excitation만 반영된다.
- GL2022 열평균 반응률은 이미 원본 scattering + thermal convolution 결과이다. Boltzmann 또는 Maxwell kinetic tail을 **또 곱하면 double count**가 된다. 이 루프는 어떤 반응률도 재가중하지 않는다.
- R37 영역 밖으로 이탈한 상태의 재진입, 자발복사, 화학반응을 전체 네트워크로 추적하지 않는다. `z_boundary`는 외부 흑체 경계 매개변수이다. Q는 실제 가스 열량도, 우주론적 관측 예측도 아니다.

## 검산 상태
원본 ZIP·source hash, 별도 gfortran 컴파일 및 이등변/비등변 PES permutation check, 두 radial 방법의 대응, 생성물 확률 보존, Decimal 70자리 source-only independent summation을 확인한다. 동일 작업자의 독립 경로 검산이며 다른 저자에 의한 R6/C9은 `NOT_RUN`이다.
