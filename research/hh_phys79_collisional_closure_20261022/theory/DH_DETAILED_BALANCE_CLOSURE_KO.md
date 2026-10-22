# D/H ground-state charge exchange: detailed-balance 구현 계약

## 채택 모델과 문헌 식

반응 방향은 다음으로 고정한다.

\[
\mathrm{D}(1s)+\mathrm{H}^+\xrightleftharpoons[k_r]{k_f}
\mathrm{D}^++\mathrm{H}(1s).
\]

[Savin 원문](https://arxiv.org/pdf/astro-ph/0109356)의 Eq. (1)–(2), §2는 이 방향과 1s→1s 채널을 정의하며 forward threshold를 약 3.7 meV, 43 K로 준다. Eq. (6), Table 2의 두 독립 fit은, T를 K로 넣어 k를 cm³ s⁻¹로 얻는 convention에서

\[
 k_r=2.06\times10^{-10}T^{0.396}e^{-33/T}
       +2.03\times10^{-9}T^{-0.332},
\]

\[
 k_{f,\mathrm{raw}}=2.00\times10^{-10}T^{0.402}e^{-37.1/T}
       -3.31\times10^{-17}T^{1.48}.
\]

§3의 fit domain은 2.7≤T≤2×10⁵ K이며, 계산된 source data에 대한 두 fit의 정확도는 각각 forward 6%, reverse 4%보다 좋다고 기술된다. 이것은 fit 오차의 설명이며 실제 원자물리의 총 오차나 두 독립 fit의 상세평형 오차를 정한 것은 아니다. Source의 Fig. 1/Table 1 결과와 Table 2의 analytic fit도 구별한다.

이번 **구성적 thermodynamic closure**는 reverse fit을 유지하고

\[
\boxed{k_f^{\rm DB}(T)=k_r(T)e^{-43\,\mathrm{K}/T}}
\]

를 forward로 쓴다. 원문 forward fit은 `kf_forward_raw`라는 진단값으로 함께 보존한다. `kf_forward_db`는 원문의 식을 그대로 구현한 값이 아니므로 source의 forward 6% 정확도를 상속했다는 표기를 하지 않는다.

이 모델의 fixed assumptions는 다음과 같다.

- 바닥상태, 비퇴화 Maxwellian ideal gas, 같은 기체 온도.
- neutral과 ion의 translational mass를 동일한 A m_p로 둔다: H와 H⁺는 m_p, D와 D⁺는 2m_p.
- electron translational mass correction과 원자 rest-mass 결손을 translational partition prefactor에서 생략한다.
- H/D neutral electronic degeneracy는 각각 2, ion은 각각 1; nuclear spin factor는 같은 isotope의 neutral/ion에 공통이라 비율에서 상쇄된다. Hyperfine 분해는 하지 않는다.
- ionic potential 차이는 정확히 `Delta=43 k_B K`인 rounded model constant이다.

## 화학퍼텐셜에서 prefactor와 부호 유도

종 i의 de Broglie 파장은 `lambda_i=(2 pi hbar²/(m_i k_B T))^(1/2)`이고, 표준에너지 epsilon_i를 포함한 ideal-gas chemical potential은

\[
 \mu_i=\epsilon_i+k_BT\ln\left(\frac{n_i\lambda_i^3}{g_i}\right)
\]

이다. 평형조건 `mu_D+mu_H+=mu_D++mu_H`을 대입하면

\[
\frac{n_{\rm D^+}n_{\rm H}}{n_{\rm D}n_{\rm H^+}}
=
\frac{g_{\rm D^+}g_{\rm H}}{g_{\rm D}g_{\rm H^+}}
\left(\frac{m_{\rm D^+}m_{\rm H}}{m_{\rm D}m_{\rm H^+}}\right)^{3/2}
\exp\left[-\frac{I_D-I_H}{k_BT}\right].
\]

위의 declared masses와 degeneracies에서는 앞의 두 비율이 1이다. 정상 mass action flux `k_f n_D n_H+=k_r n_D+ n_H`와 결합하면 채택 비율 `k_f/k_r=e^{-43/T}`가 된다. D의 전자를 떼어 H⁺로 넘기는 forward가 흡열이므로 음의 지수가 맞다. Electron의 실제 질량을 masses에 복원하면 prefactor를 다시 계산해야 한다. 기존 `A m_p` convention에서 유도한 1을 해당 확장에 그대로 주장하지 않는다.

H의 이온화율을 x_H, D의 이온화율을 x_D라 하면, 고정 T에서

\[
 \frac{x_D}{1-x_D}=K(T)\frac{x_H}{1-x_H},\quad
 K=e^{-43/T},\quad
 \boxed{x_D=\frac{Kx_H}{1-x_H+Kx_H}}.
\]

이 식을 독립 정상점 검증에 쓸 수 있다. T→∞이면 K→1이고 x_D→x_H이다. T→0⁺의 고정 0<x_H<1에서는 K→0이므로 D가 중성으로 향한다. 실제 구현의 온도 domain은 원문 fit 범위에 제한하며 이 극한을 source 외삽 허가로 해석하지 않는다.

## 열회계와 closed isolated control

상태 순서를 `(H,H+,D,D+)`로 두면 forward stoichiometry는 `(1,-1,-1,1)`이고, 순 사건률은

\[
 R=n_H[k_fY_DY_{H^+}-k_rY_{D^+}Y_H].
\]

`epsilon=(0,I_H,0,I_H+Delta)`를 단일 전역 potential로 두면

\[
 \dot Y=(1,-1,-1,1)R,\quad \dot x_e=0,
 \quad\dot b=\Delta R,\quad q_{\rm th}=-\Delta R.
\]

따라서 fixed-volume isolated control에서는 `u+b`가 보존되고, `N=sum Y+x_e`가 상수이므로 `dot T=−2 Delta R/(3 k_B N)`이다. 우주론 팽창을 켜면 기존 `−2HT`만 추가한다. 이 에너지식에 source photon budget의 차감을 섞지 않는다.

전하 보존과 핵 보존을 이용하면 isolated control을 하나의 reaction extent xi로 줄일 수 있다. 초기값을 `H0,Hp0,D0,Dp0`라 할 때

\[
 H=H_0+\xi,\ H^+=H^+_0-\xi,\ D=D_0-\xi,\ D^+=D^+_0+\xi,
\]

\[
 u=u_0-\Delta\xi,\quad T=T_0-\frac{2\Delta\xi}{3k_BN},
\]

\[
 \dot\xi=n_H[k_f(T)(D_0-\xi)(H^+_0-\xi)
       -k_r(T)(D^+_0+\xi)(H_0+\xi)].
\]

정의역은 `max(−H0,−Dp0)≤xi≤min(Hp0,D0)`와 u>0, fit T domain의 교집합이다. 이것이 행렬 전체의 Euler 업데이트와 독립적인 reduced control이다. 어느 endpoint에서도 밖으로 향하는 rate가 사라지는지 확인할 수 있다. T가 진화하는 closed control의 최종점은 위의 평형식과 energy relation을 **함께** 풀어야 한다. 일정 T 평형을 그대로 최종 정답으로 쓰면 외부 thermostat를 숨기게 된다.

## raw fit과의 실제 비교

실제 Python float 계산으로 로그 간격 10,001점을 검사했다. 이는 표본 진단이며 구간 sup-norm certificate가 아니다.

| 구간 또는 T | `(kf_DB/kf_raw)-1` | 해석 |
|---|---:|---|
| 약 3.07160 K | −0.276941 | 전체 fit domain 표본에서 최대 절대 차이 |
| 3 K | −0.273644 | 두 독립 fit의 정확한 detailed balance가 성립하지 않는 저온 예 |
| 10 K | +0.058939 | forward replacement는 별도 모델 식 |
| 약 301.897 K | +0.0256493 | 255–25370.7 K 구간 표본에서 최대 절대 차이 |
| 25370.7 K | −0.0172376 | PHYS78 최대온도에 대응한 local 비교 |
| 200000 K | +0.0483052 | fit 상단에서의 local 비교 |

3.07160 K에서 반대 분모를 쓰는 `(kf_raw/kf_DB)-1`은 +0.383012이다. 따라서 전체 domain에 대해 수정량이 source의 6%/4% 안이라고 말할 수 없다. 이 관찰은 published underlying cross-section data의 오차를 측정한 결과가 아니다. 원문의 독립 forward fit과 이번에 정확한 detailed balance를 강제한 rounded thermodynamic model이 서로 다른 함수라는 사실과 그 차이를 보존한다. PHYS78의 actual thermal corridor에서는 표본상 차이가 약2.565% 이하였으나, 이것 역시 새 우주론 trajectory의 결과가 아니다.

## 실제 검증과 admission

Wolfram은 위 prefactor 대입으로 `exp[-Delta/(k_B T)]`를 반환했고, 고정-T equilibrium flux, binding+thermal energy residual, electron 변화, nucleus 변화가 모두 정확히 0임을 반환했다. `DH_DB_WOLFRAM_RECEIPT.json`과 `dh_db_verify.wl`에 보존했다. 수치 비교는 `DH_DETAILED_BALANCE_DIAGNOSTICS.json`에 있다.

이번 계약은 D/H 단독의 ground-state conservative operator와 source-domain 내 isolated control을 닫는다. 전체 PHYS78 PI+RR에 새 D potential을 결합하는 작업, H/He/Li 전체 CI 저온 domain, radiative CX의 energy moment, CE/Compton 등의 열 closure는 각각 별도 의무다. HH_R10=OFF, production admission NOT_ISSUED.
