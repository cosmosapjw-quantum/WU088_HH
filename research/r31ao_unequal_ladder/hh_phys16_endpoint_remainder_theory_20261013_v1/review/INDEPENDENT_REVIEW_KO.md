# WU088_HH PHYS16 독립 심사

판정: **PROMOTE_SCOPED**. 검토한 endpoint 이론, 실제 상관 잔차 구성, 원 Hessian을 이용한 유한 adjoint 적용은 아래의 상속된 source 계열 안에서 채택할 수 있다. Blocking issue는 발견되지 않았다. 심사는 후보 작성자와 별도로 원 source 코드, 원 입력, PHYS15 항등식, PHYS16 증명을 읽고 수행했다. 계산 후보를 import하지 않는 표준 라이브러리의 정확 유리수 프로그램으로 18개 제한된 검산 묶음을 실행했다.

## 1. 심사 범위와 유지하는 전제

대상은 동일 COMMON, 고정 admissible coefficient 선택 α, 같은 전역 θ=(λ,b)∈[0,1]²를 공유하는 Full과 두 half의 차이

\[
d=g_2-g_F,\qquad r=H_F(g_2)
\]

다. λ 또는 b를 바꾼 두 해의 차이, 연속 시간의 실제 해에 대한 오차, 전체 물리 모형의 관측 검증으로 해석하지 않는다. 원 재사용 자료가 채택한 고정 실수 C² source 계열과 native binary64 coefficient의 의미가 유지되어야 한다. source 자료의 `native_authority:false`를 새 native 인증으로 바꾸지 않는다.

심사에 사용한 근거는 다음과 같다.

| 대상 | 직접 확인한 내용 | 판정 |
|---|---|---|
| PHYS15 `CORRELATED_ENDPOINT_THEORY_KO.md` | 잔차의 source 2항·photon 7항, 평균 Jacobian, 공통 sector 전달, 유한 온도식, photon anchor/secant | 동일 입력·동일 정의로 재사용 |
| 원 FT03 `ft03_interval.rs` | nonphoto의 밀도 인수, H/He 냉각항 부호, RR kinetic factor, 물리적 population·온도 조건 | 직접 확인 |
| 원 `phys04_mixed.rs`, `sourcebox.rs` | sigma=0인 nonphoto 분리 시점, λqν_H, 팽창항, `G_gg`가 RHS가 아닌 residual Hessian이라는 대응 | 직접 확인 |
| PHYS16 application 코드와 run01 | 저장 입력의 정확 비트값, source pullback, 실제 stage increment, signed photon 항, C/B/q/S 전달 | scoped 채택 |
| PHYS16 endpoint 이론과 application01 | Taylor 부호와 적분 가중치, 유한 Neumann 및 adjoint remainder, 두 birth 항의 실제 endpoint 부호 | scoped 채택 |
| Wolfram/xAct 실행 기록 | 실제 tensor 6개와 scalar 4개의 exact zero, 최종 메시지 없음 | 대수적 교차 검산으로 채택 |

핵심 source·후보·결과의 SHA256는 `INDEPENDENT_REVIEW.json`과 `INDEPENDENT_ARITHMETIC_RESULTS.json`에 기록했다. 불변 후보 이론의 SHA256는 `02f29b8e03825a1817378d9a9097228a82fd360fdd2ad9e573c6169c4aa59b48`이다.

## 2. 원 입력과 source 구성의 심사

### 2.1 정확 binary64와 공유 의존성

원 `FROZEN_SOURCE_CONTRACT.json`의 16개 단어 중 centre 4개와 radius 4개를 `UNIFORM_ARITHMETIC.json`의 native float를 다시 인코딩한 단어와 비교했다. 모두 정확히 같다. 따라서 centre의 0.915·0.3·0.6과 S의 0.015·0.01은 각각 저장된 binary64의 정확한 유리수다. 십진 유리수로 몰래 바뀌지 않는다. 원 `sourcebox.rs`는 같은 frozen 단어의 centre에서 whole Θ를 유지하여 `SOURCE_CENTRE`를 export한다.

Application에 기록된 14개 입력과 endpoint 적용에 기록된 6개 입력은 실제 파일 길이와 SHA256가 모두 일치한다. C, B, q, S는 원 자료와 같다. 정확 유리수로 모든 weighted row sum이 원 q 이하임을 확인했다. q의 상단 비트는 `3f1ec474231fbe16`이고 q<1이다.

ρ는 PHYS14의 같은 보관 구간에서 재사용하고, full remap에는 그 ρ²를 사용한다. birth amplitude M_F=2M은 실제 두 binary64 단어에서 정확히 성립한다. 원 입력상 33 group, 17 HI active group, He photo opacity=0, active group의 heat=energy−χ_H를 확인했다. 구간 계산은 공유 식을 먼저 인수분해한 뒤 외부 구간 곱을 사용한다. 남은 parameter dependency loss는 폭을 늘릴 수 있지만, 동일 계열 각 점의 포함성을 손상하지 않는다.

### 2.2 Source 시각 차이와 cooling cone

원 source는 같은 온도에서 nonphoto 값을 \(n_H e\,[k_{w,H}+f k_{w,He}]\)의 구조로 분리할 수 있다. \(f=n_{He}^{stored}/n_H\)와 실제 온도 정규화를 사용한다. 밀도비 차이

\[
\Delta f=f_1-f_2<0
\]

를 개별 구간 비율의 큰 차이로 만들지 않고 저장된 binary64의 정확 유리수 차이로 먼저 계산하는 구현이 맞다. 온도를 맞추는 pullback

\[
\delta w=-w_1\Delta f\frac{1+y_{1,1}+2y_{2,1}}{\Pi_1}
\]

과 그 선분은 원 X 내부다. 독립 유리수 계산에서 이 이동은 약 \(1.10\times10^{-16}\) eV/H이고, 관련 온도는 약 4.9×10⁴ K이며 원 [30000,110000] K domain 안에 있다.

FT03의 source 코드를 직접 확인하면 CI와 DR의 thermal 항은 양의 rate·물리적 population에 음의 부호로 들어간다. H/HeIII RR에서는 원 binary64 계수로

\[
1.5-1.503+1.923(0.470)/2>0
\]

이고, domain에서 \((\lambda/(0.522T))^{0.470}>1\)이다. HeI의 factor는 1.5−0.654>0이다. 따라서 H와 He thermal 계수가 각각 비양수라는 cooling cone을 쓸 수 있다. 이때

\[
\frac{F^{np}_{w,2}(\Psi g)}{n_2e_*(g)f_2}
\le k_{w,He}(T_1)\le0
\]

는 total cooling에서 He 성분을 제한하는 유효한 포함이다. \(\Delta f<0\)이므로 He 보정은 비음수다. 원 source 전체를 He 항으로 잘못 동일시하지 않는다. 독립 프로그램은 이 경계·pullback·nonphoto time difference·HH time difference를 다시 계산해 후보 저장 포함 안에 들어감을 확인했다.

### 2.3 실제 stage increment와 평균 source Jacobian

\(g_2-g_1=hB_2(g_2)+VP_2\)를 그대로 사용해 ΔA₁의 작은 차이를 만든 부호가 맞다. \(g_1-g_2\)를 독립 root box의 차이로 대체하지 않았다. Source movement 항의 부호는 \(-h\overline J_{12}(g_2-g_1)\)이다. 두 gas root의 hull, pullback 선분, g₂–g_F 선분은 모두 X에 엄격히 포함되고, x∈(0,1), 양의 helium population 및 y₁+y₂<1 조건을 만족한다.

전체 평균 residual Jacobian의 포함은

\[
\overline A\in I-2h[DB_2](\operatorname{hull}(g_2,g_F))
 +2h[v_F]e_x^T
\]

에서 구성한다. 마지막 항은 Q_F와 양의 Full denominator를 쓰는 HI의 한 열 구조다. 원 source jet에서 만든 gas 평균 Jacobian 및 이 photo 항을 독립 유리수로 조립하여 후보 저장값의 포함성을 확인했다.

## 3. 광자 항·guard·sector 전달의 심사

PHYS15의 일곱 광자 absorption sector는 같은 Q₁, 같은 A₂(g₂), 같은 ρ graph를 사용한다. ΔA₁, \([R,A]\), stock intermediate redshift, stock backward Euler, remap composition, birth redshift, birth backward Euler의 부호는 원 정확 항등식과 일치한다. Inactive group과 GN/GU에서 opacity가 0인 사실을 보존한다.

Below-guard의 j=1 remap은 bulk 공식을 무리하게 연장하지 않는다. \(R(\rho)^2-R(\rho^2)\)의 j=1 column은 group 0·1 및 GN·GU에서 각각

\[
-\alpha_1(\alpha_1+\rho),\quad
\alpha_1(\alpha_1+\rho-1),\quad
\alpha_1,\quad
\rho E_0\alpha_1
\]

이다. 두 개의 비퇴화 정확 유리수 witness로 direct remap composition과 이 네 계수를 대조했다. Number와 energy 차이도 정확히 0이다. 이 유한 검산은 일반 항등식의 수작업 유도를 보조한다.

각 sector는 공통 \(\overline A^{-1}\), 공통 \(T_2\), 공통 \(\Pi_F\)로 전달한다. 별개의 nonlinear endpoint를 sector마다 만들지 않으므로

\[
\sum_s d_s=d,\qquad \sum_s\Delta T_s=\Delta T
\]

라는 attribution의 의미가 유지된다. 개별 interval 합의 폭이 total interval보다 넓을 수 있다는 사실은 이 점별 항등식과 양립한다.

Photon anchor에 실제 Full의 secant 보정

\[
\delta Z_j=\delta Z_j^{anchor}
 +\frac{2ha_{2j}Q_{Fj}d_x}{D_{Fj}(g_2)D_{Fj}(g_F)}
\]

를 더한 코드도 원 PHYS15 정확식과 일치한다. Guard에는 a=0이므로 이 보정이 없다. Run01의 actual photon number 및 energy 포함은 각각 엄격히 음수다. 원 ledger의 zero inclusion은 계산 일관성 보조 검사이며, 보존 항등식의 증명 자체로 과장하지 않는다.

## 4. Endpoint 이론의 직접 심사

### 4.1 Taylor 부호·적분 가중치

y=g₂, J=DH_F(y), d=y−g_F에서

\[
0=H_F(y-d)=r-Jd+R_2(d),
\quad
K(d)v=\int_0^1(1-s)D^2H_F(y-sd)[d,v]ds
\]

이므로 \(R_2=Kd\), \(\overline A=J-K\), \(Jd=r+R_2\)가 맞다. 필요한 가정은 C²와 관련 선분 포함이다. 원 centre c에서 J(y)를 만드는 별도 적분의 가중치는 1이며, K의 1−s와 혼동하지 않았다.

HI photo 유리식의 remainder는

\[
R_{2,ph}=
\sum_j\frac{\ell_j^2Q_{Fj}d_x^2}{D_j^2(D_j+\ell_jd_x)}\nu_j
\]

이고 양의 denominator와 Q_F≥0에서 active x,w 성분은 비음수다. Nonphoto·HH remainder에는 −2h를 곱하지만, 원 `G_gg`는 이미 residual Hessian이므로 그 파일에 다시 −2h를 곱하지 않는다. 실제 readout과 endpoint 적용은 이 구별을 지킨다.

### 4.2 유한 Neumann와 공통 adjoint

원 scaled Hessian 상계 L_H와 \(a\ge\|d\|_S\)에서

\[
\|S^{-1}CKS\|_\infty\le L_Ha/2,
\qquad \|CR_2\|_S\le L_Ha^2/2
\]

를 얻는다. M=I−CJ, \(P_m=I+M+\cdots+M^m\)를 쓰면 정확한 유한 대입식

\[
d=P_mCr+P_mCR_2+M^{m+1}d
\]

에서 후보의 \(\varepsilon_m=q^{m+1}a+(L_Ha^2/2)\sum_{k=0}^m q^k\)가 나온다. Endpoint J와 평균 A는 원 q로 모두 가역이다.

온도의 유한 분자 covector \(n_T=C_Te_w^T-T_2\ell_e\)와 \(\widetilde z_m^T=n_TP_mC\)에서

\[
N_T=\widetilde z_m^Tr+\eta_m^Td+\widetilde z_m^TR_2,
\quad \eta_m^T=n_TM^{m+1}
\]

의 부호와 잔여항이 맞다. Sector에서는 \(\eta_m+\widetilde z_m^TK\)가 공통 \(d_s=\overline A^{-1}r_s\)를 작용한다. 평균 adjoint \(\overline z^T=n_T\overline A^{-1}\) 자체의 경계는

\[
\|(\overline z-\widetilde z_m)^TS\|_1
\le\kappa c_C b_T\left(q^{m+1}+\tfrac12L_Ha\sum_{k=0}^m q^k\right)
\]

이며 \(c_C=\|S^{-1}CS\|_\infty\)가 필요하다. 코드가 이 인수를 포함하며 component bound를 Θ_z/s_i로 변환하는 것도 맞다.

독립 계산에서 signed C preconditioning 뒤 exact Cramer determinant로 \((I-B)m=\operatorname{mag}(Cr)\)를 풀어 저장 majorant·remainder와 비교했다. 모든 성분이 비음수이고 정의식은 정확히 성립했다. 후보는 Gaussian elimination을 쓰므로 독립 해법을 사용한 교차 검사다. 유한 온도식의 양의 Π_F, 3회 mean-operator 교차, endpoint centre/Hessian 포함, m=2 오차와 평균 adjoint 경계를 모두 별도로 계산했다.

## 5. 채택할 수치 결론

다음 경계는 이 심사가 확인한 동일 계열의 pointwise uniform 포함이다. 표의 십진 경계는 저장된 outward 표기를 따른다.

| 수량 | 채택 포함 또는 상계 |
|---|---:|
| run01 d_x | [4.968073098724, 6.424794326491]×10⁻⁸ |
| run01 d_w (eV/H) | [−2.378772061685, −1.828215860677]×10⁻⁸ |
| run01 Δe (per H) | [4.968232944627, 6.425017521665]×10⁻⁸ |
| run01 Δn_e (cm⁻³) | [4.944257155952, 6.394011555549]×10⁻¹² |
| endpoint 교차 뒤 ΔT (K) | **[−0.001585967387181453, −0.001210819969055199]** |
| L_H | [8.27802481433761309, 8.27802481433761310]×10⁻⁵ |
| \(\|d-J^{-1}r\|_S\) | ≤7.594228219959920×10⁻¹⁶ |
| \(\|d-v_2\|_S\) | ≤7.663478331196157×10⁻¹⁶ |
| 동일 Π_F를 쓰는 온도 surrogate 오차 | ≤1.710575696736044×10⁻¹² K |

1.71×10⁻¹² K는 endpoint surrogate와 정확 평균 전달의 차이를 같은 분모에서 제한한 값이다. 전체 ΔT 포함 폭은 약 3.75×10⁻⁴ K이며, 위 오차와 다른 수량이다. 이 차이를 구별해야 한다.

### 두 birth sector

실제 평균 adjoint에서 \(\overline z_x<0\), \(\overline z_w>0\), \(\overline z^T\nu_{24}<0\)를 확인했다. \(\beta_j=\tau_j/(1+\tau_j)^2\)를 먼저 인수분해하면

\[
\beta_{23}-\beta_{24}>0,\qquad
\epsilon_{23}\beta_{23}-\epsilon_{24}\beta_{24}<0.
\]

Heat 차이의 세 다항식 계수도 원 정확 binary64 leaf에서 모두 음수다. 따라서 실제 endpoint attribution을 b로 나눈 경계는 다음과 같다.

| b>0에서의 수량 | outward 포함 (K) |
|---|---:|
| \(\Delta T_{birth\ redshift}/b\) | **[−2.193573619033929, −2.084075101148286]×10⁻⁹** |
| \(\Delta T_{birth\ BE}/b\) | **[6.795510419222985, 7.189758987952319]×10⁻⁵** |

b=0에서는 두 잔차 sector가 정확히 0이므로 attribution도 0이다. 이 부호는 이전의 birth forcing 부호를 endpoint로 무조건 승계한 결과가 아니다. 공통 평균 adjoint의 부호를 새로 포함하여 닫았다. 이 비율을 b 미분으로 부르지 않는다. 일반 sector 구간에서 아직 0을 포함하는 stock intermediate redshift·remap composition은 현재 표현의 남은 부호 문제로 둔다. 이를 물리적 불가능성이나 강한 no-go로 해석하지 않는다.

## 6. 실제 검산 실행과 문헌의 역할

`independent_arithmetic_review.py`는 후보 코드와 PHYS14 helper를 import하지 않는다. Python 표준 라이브러리 Fraction과 별도의 endpoint-pair 함수를 사용한다. 실행은 18개 묶음 PASS, exit 0, 내부 0.090991989 s, wrapper 0.133782941 s, peak RSS 27588 KiB다. 물리 source callback·root solve·history replay는 모두 0이다. 사전 기록의 19개는 예상 묶음 수였고 실제 프로그램이 등록한 묶음은 18개다. 사후 결과는 실제 수를 사용한다.

Wolfram 기록의 최종 성공 출력은 Wolfram 15.0.1, xTensor 1.3.0, xPerm 1.2.4를 명시한다. 실제 ToCanonical tensor 6개와 scalar identity 4개가 모두 exact zero이고 최종 Messages가 비어 있다. External MathLink 경로는 앞선 시도에서 실패했으며, 최종 성공은 `$xpermQ=False`를 정의 전에 적용한 Wolfram Language group algorithm 경로다. 외부 canonicalizer의 성공으로 바꾸어 서술하지 않는다. 이러한 대수 검산은 source interval validity를 새로 증명하지 않는다.

문헌 검토는 Exa와 SciSpace를 실제 사용하여 원전 다섯 개에 좁혔다. Rump의 검증 잔차·interval solve, Rannacher 및 Endtmayer–Langer–Wick의 goal-oriented residual, Alekseev–Navon의 adjoint correction과 비교했다. 관련 가정·정리 위치·URL은 `literature/LITERATURE_REVIEW_KO.md`와 `references.bib`에 있다. 조회한 Endtmayer preprint 표시식의 iteration residual 부호 문제는 exact linear witness로 별도 확인했으며, 최종 journal 본문의 오류로 확장하지 않는다. PHYS16 증명은 그 표시식에 의존하지 않는다.

표준 Neumann·adjoint 원리의 재발명을 보편적 최초성으로 주장하면 안 된다. 이번 단위에서 닫힌 내용은 WU088_HH의 실제 source 정규화·일곱 photon 항·원 Hessian·유한 온도 분모를 결합해 endpoint 평가식과 명시적인 나머지를 계산하고, 실제 두 birth sector 부호까지 판정한 구성이다. Sherman–Morrison inverse 경로는 현재 수치 적용의 필수 전제가 아니며 별도 scalar 분모를 검증했다고 주장할 필요가 없다.

## 7. 판정과 후속 의무

**PROMOTE_SCOPED**: 위 전제를 유지하는 PHYS16 이론 단위와 실제 적용을 완료로 승격할 수 있다. 수치 후보의 핵심 부호, endpoint remainder 및 birth attribution에 blocking issue는 없다. 다음 연구 단위는 현재 부호를 다시 얻기 위해 원 source를 반복 실행할 필요가 없다. 원 C²의 mixed gas–parameter derivative와 기존 response 자료를 사용하여 λ,b 반응을 구성하면 새 질문을 직접 진행할 수 있다.

현재 아직 수행하지 않은 일은 full parameter Taylor/affine 모델의 구축, 두 미판정 stock/remap sector의 엄밀한 부호 분리, 다른 source 계열·새 mesh·native 실제 실행으로의 확장이다. 이것들은 이번에 채택한 제한된 결론의 전제로 추가하지 않는다. 새 입력이나 새로운 해석 범위를 채택할 때 그에 맞는 독립 의무로 둔다.
