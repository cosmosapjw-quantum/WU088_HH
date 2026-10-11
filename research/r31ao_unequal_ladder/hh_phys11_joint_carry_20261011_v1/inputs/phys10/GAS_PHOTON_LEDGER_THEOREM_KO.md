# PHYS10 — gas와 잔류 광자의 유한 혼합 에너지 ledger

2026-10-11. PHYS10의 새 최초 계산 `ledger_first`는 PHYS09와 같은 고정 실수 source 계열에서 **잔류 광자의 유한 에너지 상호작용이 엄격히 양수**임을 확인했다. Gas의 음의 유한 에너지 상호작용과 더한 잔여는 작지만 0을 포함한다. 그 상대 크기의 엄밀한 상계는 Full에서 0.155612%, 같은 COMMON의 first_half에서 0.077316%보다 작다.

정확한 source 항등식과 그 조건부 수학적 귀결은 **derived**, 새 rational 포함과 그 부등식은 **numerically checked / implementation-verified**다. 원 source inclusion과 열린 C² 전제는 상속하며, native root 실행·권한의 새 증거로 해석하지 않는다. 이론 작성자는 새 과학 코드를 실행하거나 고치지 않고 봉인할 source·code·실제 결과·로그를 읽었다. 최종 과학 채택은 비생성 독립 reviewer의 `review/DECISION.json`을 따른다.

## 1. 문제와 PHYS09로부터 재사용하는 것

PHYS09는 HH와 미래 photon birth를 함께 켰을 때의 gas energy

\[
e(g)=\ell g,
\quad
\ell=(\chi_H,f\chi_{\mathrm{HeI}},f(\chi_{\mathrm{HeI}}+\chi_{\mathrm{HeII}}),1)
\tag{1}
\]

의 유한 상호작용이 음수임을 보였다. 이번 질문은 그 음의 mixed departure가 같은 stage의 광자 응답과 어떤 관계를 갖는가다. Gas와 광자의 큰 interval을 마지막에 더해 작은 차이를 관측하는 대신, 원 eliminated source의 흡수 identity를 먼저 사용한다.

좌표와 parameter는

\[
g=(x_{\mathrm{HII}},y_{\mathrm{HeII}},y_{\mathrm{HeIII}},w),
\quad w[\mathrm{eV/H}],\qquad
\theta=(\lambda,b)\in\Theta=[0,1]^2,
\tag{2}
\]

이며 implicit 방정식은

\[
G(g,\theta;\alpha)=g-g_0(\alpha)-dF(g,\theta;\alpha)=0.
\tag{3}
\]

λ는 미래 HH source의 강도, b는 미래 photon birth의 강도다. α는 COMMON gas/photon/guard, fixed geometry, atomic coefficient, density와 모든 captured scalar leaves를 묶은 **한 고정 coefficient tuple**이다. 각 정리의 양화사는 원 포함에 허용되는 모든 고정 α다. 한 parameter rectangle 안에서 α는 바뀌지 않으며, 네 corner에 서로 다른 source tuple을 선택하지 않는다.

PHYS09의 조건부 uniform root theorem, C² 연결 및 exact intervals

\[
U=\partial_\lambda g,\qquad V=\partial_b g,
\qquad W=\partial_{\lambda b}g,
\quad W_e=\ell W
\tag{4}
\]

를 그대로 재사용한다. Inverse, Banach margin, Neumann tail 또는 gas energy proof를 새로 실행하지 않았다. 재사용 원본은 `inputs/phys09/PROJECTED_RESULTS.json`이며 SHA256은 `c6329fed8c411e1592bd1a0c63ebd9ca6151e81500ed1f46fb6b40f4b7758444`다.

두 duration은 원 captured bit leaves의 정확한 실수 값으로 Full d=1.25×10⁹ s, first_half d=6.25×10⁸ s다. 둘 다 같은 COMMON에서 독립적으로 시작하는 첫 stage다. First_half는 실제 첫 half의 terminal 상태를 전달받은 second_half가 아니며, 두 결과의 비율로 시간 수렴 차수를 정하지 않는다.

## 2. Photon 정규화와 source 구조

원 source에서 j=0,…,32는 photon energy node이고 a=0,1,2는 각각 HI, HeI, HeII absorber다. 다음 coefficient는 한 stage의 θ 전역에서 고정이다.

\[
L_0(g)=1-x,\quad
L_1(g)=f(1-y_1-y_2),\quad
L_2(g)=fy_1,
\]
\[
\kappa_{ja}(g)=c\,n_H L_a(g)\sigma_{ja},\qquad
D_j(g)=1+d\sum_a\kappa_{ja}(g).
\tag{5}
\]

PreBE 이후의 incoming은

\[
N_j^{\mathrm{in}}(b;\alpha)=\bar N_j(\alpha)+bM_j(\alpha),
\qquad
N_j(g,b;\alpha)=\frac{N_j^{\mathrm{in}}(b;\alpha)}{D_j(g)},
\qquad
R_{ja}(g,b;\alpha)=\kappa_{ja}(g)N_j(g,b;\alpha).
\tag{6}
\]

N_j 및 M_j의 단위는 photons/H, κ는 s⁻¹, R은 photons/H/s다. 이는 `coupled_primary.rs::PrimaryPacket { energy_ev, per_h }`와 `photons()`의 `p.per_h / (1+dt*opacity)`, `paired_runtime.rs`의 angular group를 `PrimaryPacket::per_h`로 넘기는 원 코드에 대응한다. `phys04_transport.rs`는 동일 angular photon amounts를 group 합으로 만들고 그 sum을 source에 전달한다. 따라서 광자 energy에 n_H를 다시 곱하거나 나누지 않는다.

Birth amount M_j는 원 finite source leaf와 고정 angular weights의 계열이다. Source rate로 바꾸어 d를 추가하거나, rounded `fl(d SOURCE)`를 unrounded d×SOURCE로 바꾸지 않는다. 고정 gas에서 incoming은 g와 λ에 독립이고 b에 affine하다. Geometry, energy ratio, atomic thresholds와 photon cross-section leaves도 θ에 독립이다. 실제 physical chart에서 D_j>0이고 원 C² 증거가 작은 열린 연장을 제공한다.

Retained photon energy는

\[
e_\gamma(g,b)=\sum_{j=0}^{32}E_jN_j(g,b)
\quad [\mathrm{eV/H}],
\tag{7}
\]

로 정의한다. E_j=exact(captured node energy)는 eV이며 local absorption-elimination stage에 고정된다. 이 관측량은 이 단계에서 남은 photon energy다. PreBE 단계의 guard·escape·redshift 및 전체 history의 radiation energy ledger를 모두 포함하는 관측량으로 확장하지 않는다.

Stage helium factor f는 gas energy의 (1), absorber amount의 (5)에 들어간다. Nonphoto와 temperature source의 stored density ratio fhat=exact(nHe_stored)/exact(nH)는 원 그래프대로 별도로 유지한다. f=fhat라는 추가 등식을 사용하지 않는다. 자연단위를 도입하지 않았으며 c와 에너지 변환의 원 단위가 보존된다. Metric 연산이 없는 이 source 계산은 기본 signature (−,+,+,+)와 독립적이다.

## 3. 정리 1 — absorbed와 retained photon의 정확한 관계

**정리.** (5)–(6)의 같은 고정 coefficient source에서 각 node에 대해

\[
d\sum_aR_{ja}=(D_j-1)N_j=N_j^{\mathrm{in}}-N_j.
\tag{8}
\]

따라서

\[
d\mathcal A=\sum_jE_jN_j^{\mathrm{in}}-e_\gamma,
\qquad
\mathcal A(g,b)=\sum_{j,a}E_jR_{ja}(g,b)
\tag{9}
\]

가 정확하다.

**증명.** R_ja=κ_jaN_j를 합하면 dΣR=(D−1)N이다. D_jN_j=N_j^in을 대입하면 (8)을 얻는다. 각 node의 E_j를 곱하고 모든 node를 합하면 (9)다. Fraction denominator에 포함된 모든 absorber를 같은 합에 넣었으므로 He를 생략하거나 σ의 작은 값을 0으로 치환한 관계가 아니다. 이는 discrete elimination의 대수적 identity이며 continuum photon conservation을 따로 가정하지 않는다.

임의의 scalar source J(g,λ,b)에 대해 같은 implicit family의 전체 mixed derivative를

\[
\mathscr L[J]
=J_gW+J_{gg}[U,V]+J_{g\lambda}V+J_{gb}U+J_{\lambda b}
\tag{10}
\]

로 표기한다. 이를 확인하려면 먼저 ∂λJ=J_gU+J_λ를 쓰고 b에 대해 미분한다. 첫 항에서 J_gW, J_gg[U,V], J_gbU가 나오고 두 번째 항에서 J_gλV와 J_λb가 나온다. Gas index i,j는 0,…,3, λ slot은 4, b slot은 5다. Hessian을 대각항만으로 근사하거나 parameter cross terms를 생략하지 않는다.

N_j^in은 λ에 독립이므로 ∂λbN_j^in=0이다. 따라서 (9)의 전체 derivative는

\[
\boxed{W_\gamma=-d\mathscr L[\mathcal A].}
\tag{11}
\]

원 JSON `SOURCE_BOX.photons`는 값 interval만 갖는다. PHYS10은 없는 full photon Jet를 복원했다고 주장하지 않고, 이미 보존된 `SOURCE_BOX_COMPONENTS.photo_rates[33][3]`의 full Jets를 (11)로 소비한다. 이는 (8)에 의한 동일 observable의 정확한 재표현이다.

## 4. 정리 2 — captured heat를 유지한 gas+photon ledger

Captured heat와 threshold를

\[
a_{ja}=\operatorname{exact}(\mathrm{heat}_{ja}),\quad
\chi_a=\operatorname{exact}(\mathrm{CHI}_a),\quad
\epsilon_{ja}=a_{ja}+\chi_a-E_j,
\qquad
\Psi=\sum_{j,a}\epsilon_{ja}R_{ja}
\tag{12}
\]

로 정의한다. 식 (12)의 덧셈·뺄셈은 각각의 captured leaf를 exact real로 올린 뒤 수행한다. ε는 `energy.rs::heat_epsilon`의 a−(E−χ)와 같은 부호 convention이다. a+χ=E라는 근사 등식을 도입하지 않는다.

원 HH reaction vector는 H=q(1,0,0,−χ_H)이고 같은 χ_H를 사용하는 (1)에 대해 ℓH=0이다. 원 nonphoto clone을 F^np라 쓰면 PHYS09의 정확한 source identity는

\[
\mathcal E=\ell F
=\ell F^{np}-2H_{\mathrm{mean}}w
+\sum_{j,a}(a_{ja}+\chi_a)R_{ja}
=\mathcal B+\mathcal A,
\]
\[
\mathcal B=\ell F^{np}-2H_{\mathrm{mean}}w+\Psi.
\tag{13}
\]

F^np는 HH, photo, expansion을 더하기 전의 실제 clone이다. Nonphoto projection은 stage f와 원 FT03 normalization을 그대로 사용하므로 이미 Jnorm=(f−fhat)×He nonphoto의 효과를 포함한다. Jnorm을 별도 항으로 다시 더하지 않는다. 팽창도 (13)에 정확히 한 번만 들어간다.

Gas energy residual e−e_0=dℰ와 (9)를 합하면 다음 정리를 얻는다.

**정리.** 원 source inclusion 및 PHYS09의 같은 C² root family를 전제로

\[
\boxed{e+e_\gamma=e_0+\sum_jE_jN_j^{\mathrm{in}}+d\mathcal B.}
\tag{14}
\]

고정 future-parameter initial ledger에서 e_0는 λ,b에 독립이고 N^in은 b에 affine이다. 그러므로

\[
\boxed{
W_e+W_\gamma=d\mathscr L[\mathcal B]
=d\mathscr L[\ell F^{np}]-2dH_{\mathrm{mean}}W_w+d\mathscr L[\Psi].
}
\tag{15}
\]

모든 소스는 원 thermal-w 상자에서 평가한다. 독립 energy-coordinate domain을 새로 가정하지 않는다. B의 Jet 계수를 먼저 합한 뒤 L을 적용하면 공통 W 및 U,V와의 dependence를 더 오래 보존할 수 있다. 각 source part를 따로 contraction한 포함과 B를 먼저 조립한 포함은 모두 (15)의 오른쪽을 포함하지만, interval 끝점이 정확히 같은 방식으로 합쳐질 필요는 없다.

원 실수 B는 고정 gas에서 future λ,b에 직접 의존하지 않는 부분이 많다. 그 구조적 사실과 source extension의 signed numerical tails를 구별한다. PHYS10 실제 산술은 nonphoto/rate에 저장된 모든 gradient·Hessian tails를 그대로 넣어 (10)의 다섯 항을 모두 계산했다.

## 5. 정리 3 — 유한 interaction와 같은 family의 비율

관측량 z에 대해

\[
I_z=z(1,1)-z(1,0)-z(0,1)+z(0,0)
\tag{16}
\]

로 정의한다. 네 corner는 같은 α와 같은 C² implicit branch에 속한다. 첫 parameter에 한 번, 두 번째 parameter에 한 번 기본정리를 적용하면

\[
I_z=\int_0^1\!\int_0^1W_z(\lambda,b)\,db\,d\lambda.
\tag{17}
\]

**정리.** [Γ]가 (11)의 uniform enclosure이고 [B]가 (15)의 uniform enclosure라면, 단위 parameter rectangle의 넓이가 1이므로

\[
I_\gamma\in[\Gamma],\qquad I_e+I_\gamma\in[B].
\tag{18}
\]

이 결과를 위해 corner nonlinear solver나 photon endpoint 실행을 할 필요는 없다. PHYS10에서 실제 corner roots를 구하지 않았다. 서로 다른 α의 endpoint를 빼거나 local point Hessian을 rectangle 전체의 derivative로 바꾸면 (18)은 정당화되지 않는다.

PHYS09의 uniform gas enclosure를 [e_−,e_+]라고 하고 e_+<0라 하자. A=−I_e>0이며 A∈−[W_e]다. T=I_e+Iγ∈[B]라 놓으면 같은 finite quantities에서

\[
\frac{I_\gamma}{-I_e}=1+\frac{T}{A}.
\tag{19}
\]

따라서 sound ratio enclosure는

\[
\left(\frac{[\Gamma]}{-[W_e]}\right)
\cap
\left(1+\frac{[B]}{-[W_e]}\right).
\tag{20}
\]

이 교집합은 ratio를 정확한 점값으로 취급하지 않는다. 또한 pointwise derivative ratio를 적분해서 finite ratio라고 주장하지 않는다. (18)을 통해 실제 유한 A,T가 각각 같은 구간에 들어간 다음, 같은 finite identity (19)를 적용하는 것이다.

더 간단한 대칭 보상 상계는

\[
\eta=\frac{\max(|B_-|,|B_+|)}{-e_+},\qquad
\left|\frac{I_\gamma}{-I_e}-1\right|\le\eta.
\tag{21}
\]

η<1이면 Iγ>0도 따른다. 아래 실제 결과는 직접 (11)의 엄격한 양수와 (21)을 모두 만족한다. [Γ]∩([B]−[W_e])로 photon 포함을 refinement할 수 있으나, 이번 두 stage에서는 이 교집합이 원 [Γ]를 더 줄이지 않았다. 수치적으로 같은 폭이어도 identity의 의미와 direct sum은 보존했다.

## 6. 실제 새 포함 결과

모든 표의 끝점은 exact-rational 연산 결과의 바깥쪽 binary64 표시다. 정확한 분자·분모는 `results/ledger_first/LEDGER_RESULTS.json`에 저장되어 있다. Mixed derivatives와 같은 단위 사각형의 finite interactions에 공통으로 적용된다.

| 양 | Full | 같은 COMMON의 first_half |
|---|---:|---:|
| PHYS09에서 재사용한 I_e, eV/H | [−6.192852956727484e−16, −2.012354998700877e−16] | [−7.75969827499494e−17, −2.5357316013204017e−17] |
| **새 Iγ, eV/H** | **[2.0147819024003132e−16, 6.190685965150866e−16]** | **[2.5372573637033666e−17, 7.758341579441771e−17]** |
| 보존한 direct sum [I_e]+[Iγ], eV/H | [−4.17807105432717e−16, 4.178330966449989e−16] | [−5.2224409112915727e−17, 5.222609978121369e−17] |
| **Source부터 투영한 I_e+Iγ, eV/H** | **[−3.1314477547412323e−19, 2.4467453520579934e−19]** | **[−1.9605021839988345e−20, 1.5319948343632613e−20]** |
| Iγ/(−I_e) | **[0.9984438889973375, 1.0012158616912215]** | **[0.9992268494887321, 1.0006041628512914]** |
| η의 바깥쪽 상계 | 0.0015561110026624584 | 0.0007731505112678191 |

따라서 gas energy의 음의 mixed departure는 retained photon energy의 양의 mixed departure로 거의 상쇄된다. η는 Full에서 0.155612%, first_half에서 0.077316%보다 작다. Ratio 구간은 양쪽 모두 1을 포함한다. 정확히 1이라는 판정이나 total interaction의 정확한 0은 얻지 않았다.

### 6.1 Retained photon response의 다섯 항

여기서는 (11)의 −dL(A)에 이미 photon sign을 적용한 항들을 표시한다.

| Photon 항, eV/H | Full | first_half |
|---|---:|---:|
| Feedback | [−1.7947160830811816e−18, −5.661584590209481e−19] | [−1.1257452587192628e−19, −3.556823974812458e−20] |
| Hessian | [5.919274332827627e−22, 2.5819296728808077e−21] | [1.8606486181612964e−23, 8.102254144434713e−23] |
| Gas–λ signed tail | [−9.567e−319, 9.567e−319] | [−1.19653e−319, 1.19653e−319] |
| **Gas–birth term** | **[2.032723143956792e−16, 6.196321730444347e−16]** | **[2.548512955641941e−17, 7.76189030116244e−17]** |
| λ–birth signed tail | [−5.9942125483737e−311, 5.9942125483737e−311] | [−2.997106274187e−311, 2.997106274187e−311] |

양의 gas–birth 항이 음의 feedback을 이긴다. 이는 PHYS09에서 음의 gas birth-gradient가 지배했던 사실과 같은 source transfer의 양면이다. 독립적인 physical source를 하나 더 fit한 결과가 아니다.

### 6.2 Gas+photon 잔여의 source 분해

(15)의 nonphoto, expansion, captured heat defect는 다음과 같다.

| Source part, eV/H | Full | first_half |
|---|---:|---:|
| dL(ℓF^np) | [−2.787417411584523e−19, 2.7907756952147026e−19] | [−1.7451970205780317e−20, 1.7472999977840642e−20] |
| **−2dHmean W_w** | **[−3.440303431567093e−20, −1.0578055231115218e−20]** | **[−2.1530516342080285e−21, −6.625765892416593e−22]** |
| dL(Ψ), 바깥 binary64 표시 | [−2⁻¹⁰⁷⁴, 2⁻¹⁰⁷⁴] | [−2⁻¹⁰⁷⁴, 2⁻¹⁰⁷⁴] |

Expansion mixed term은 엄격히 음수다. Hmean>0와 PHYS09의 W_w>0에 부합한다. Nonphoto 및 total에는 0이 들어가므로 그 두 항의 실제 부호를 정하지 않는다. 이 표의 개별 구간을 더한 것은 B의 source Jet를 먼저 합친 뒤 contraction한 포함보다 넓을 수 있다. 양자의 끝점이 같은 수치로 더해져야 한다고 요구하지 않는다.

Captured ε는 stage마다 99개 중 19개가 정확히 0이 아니다. 실제 nonzero 값은 ±1.7763568394002505×10⁻¹⁵ eV 또는 ±3.552713678800501×10⁻¹⁵ eV이고, 이번 자료에서는 모두 absorber index 2의 leaves다. 나머지 80개가 정확히 0이라는 것과 19개에 nonzero coefficient가 있다는 것을 모두 기록했다.

그러나 ε≠0인 coefficient가 있다는 사실은 실제 Ψ mixed contribution≠0라는 증거가 아니다. 그 기여는 original rate Jets와의 곱이며 현재 포함은 0을 감싼다. 표의 2⁻¹⁰⁷⁴는 binary64 최소 양의 subnormal이다. 정확한 rational tail을 바깥쪽으로 표시한 것으로, 실제 exact endpoint가 그 binary64 수와 같다는 뜻이 아니다. Underflow 이하의 rational 항을 0으로 버리지 않았다.

## 7. 물리적 해석과 반례 경계

I_e<0는 두 미래 효과를 함께 켠 gas energy가 각 단독 효과를 더한 가산 예측보다 작다는 뜻이다. Iγ>0는 같은 조합에서 남는 photon energy가 가산 예측보다 크다는 뜻이다. 동일 stage의 흡수 감소가 양쪽에 반대 부호로 나타나며, nonphoto·팽창·captured heat 표현의 차이가 작은 잔여를 만든다.

이 서술의 대상은 미래 λ,b의 mixed departure다. Gas가 가진 절대 에너지가 광자로 방출되어 보존된 비율, HH energy injection의 absolute radiative efficiency, 장시간의 heating/cooling, 전체 photons의 escape probability를 측정한 것으로 해석하지 않는다. 특히 retained photons가 더 많다는 혼합 효과와 전체 시스템의 escaping radiation은 다른 관측량이다.

수학적 한계를 확인하는 특수 경우는 다음과 같다.

- 모든 κ가 0이면 N=Nin이므로 eγ의 λ–b interaction은 0이다. 실제 양수 결과는 비영 흡수와 gas의 HH 반응이 결합한 source 범위에 제한된다.
- F^np=0, Hmean=0, ε=0인 ideal source에서는 (14)로 total mixed interaction이 정확히 0이다. 이번 실제 source에는 이 세 항을 없애지 않았으므로 그 특수 경우의 정확한 0을 주장하지 않는다.
- λ 또는 b increment가 0이면 유한 interaction은 0이다. 일반 rectangle에는 mixed derivative의 적분 범위와 면적이 따라온다.
- 실제 physical incoming은 nonnegative이지만 signed tangent와 Hessian에는 같은 positivity cone을 적용하지 않는다. 음의 tail을 제거하면 여기서 사용한 inclusion의 의미를 바꾼다.
- 서로 다른 COMMON, 서로 다른 captured coefficient tuple 또는 carried stage를 corner마다 사용하면 (17)로 동일 interaction을 연결할 수 없다.

## 8. 실제 실행과 검증 증거

새 프로그램은 `diagnostics/analyze_photon_ledger.py`다. PHYS09의 exact rational endpoints를 재사용하고 두 stage에서 각각 99 full photo-rate Jets와 4 nonphoto Jets를 읽었다. 각 Jet의 value, 7 gradient, 7×7 Hessian을 보존하므로 사용한 source interval 표현은 stage당 103×57=5,871개다. Scalar coefficients와 재사용 U,V,W의 rational input도 원 파일 identity에 결박했다.

| 기록 | 실제 결과 |
|---|---|
| Run ID | ledger_first |
| 실행 구간 UTC | 2026-10-11 08:44:01.943572–08:44:02.669802 |
| 실행 구간 KST | 2026-10-11 17:44:01.943572–17:44:02.669802 |
| Wrapper elapsed | 0.7208253940043505 s |
| 최대 RSS | 23,924 KiB |
| 종료 | exit 0, timeout false, stderr 0 bytes |
| 제한 | Wall/CPU 45 s, address space 384 MiB, 각 log/output 16 MiB |
| Assertion | 35개; 독립 test 개수로 부르지 않음 |
| 의미 사례 | 7개 |
| 입력·코드 before/after bindings | 19개 전부 unchanged |
| 과학 시도 | 최초 1회, 수정 재시도 없음 |
| 새 source / inverse / native root / 역사적 suite | 모두 0 |

의미 사례는 exact eliminated photon number, 닫힌 rational photon finite FTC, 전체 다섯 항 chain rule, nonzero captured heat defect, signed subnormal 보존, dependency가 있는 interval 합과 early identity의 차이, 잘못된 exact endpoint·교집합·divisor·tangent domain 거절이다. 세 photon-number samples 또는 네 invalid-domain rejection을 독립 physics tests 네 개로 과장하지 않는다.

실제 run은 작은 saved-source 후처리이며 NCP 64-core의 heavy job을 필요로 하지 않았다. 새로운 Rust duplicate implementation, 원 소스 callback, photon point endpoint, nonlinear root, IVP, 수치 미분, complete inverse replay를 수행하지 않았다. PHYS08/09의 완료 NCP 반환 재사용 여부는 이번 별도 intake에서 확인하며 이 문서의 source proof를 대신하지 않는다.

| 산출물 | SHA256 |
|---|---|
| results/ledger_first/LEDGER_RESULTS.json | 5c80682180650f4c98bff6a0cec699cb04b9a52c680a019b1e522f0bb598a7cc |
| results/ledger_first/SUMMARY.json | 73c6ddabd0d8fc2047405378be253d0a7f58fc0ef82f3e91f98f52c7d85c1cbe |
| diagnostics/analyze_photon_ledger.py | f4de621ae1bf82d7097f11b87847d05fcd563256cb0249650b55a239accfe636 |
| src/exact_weighted.py | 30886477bcd095a7324c169959f7adee8912a478174a82857408317c3e356390 |
| SCIENTIFIC_CONTRACT.md | 7860dc05d3118267a06efada060a4ffdb1ef99e6aad881fb58334863334cb1ba |

## 9. Source·정리·코드의 대응

| 주장 | 원 근거 | 계산 위치 |
|---|---|---|
| Packet당 photons/H 및 고정 E | candidate/src/coupled_primary.rs::PrimaryPacket, photons; candidate/src/paired_runtime.rs의 group→packet 전달 | (5)–(7), stage() dimensional leaves |
| Affine incoming, 고정 θ geometry | candidate/src/phys04_transport.rs::phys04_prepare_family; C2_DOMAIN.json | (6), (11), finite theorem의 전제 |
| Eliminated N, full absorption rates | candidate/src/phys04_mixed.rs::phys04_reduced_residual | stage()의 absorption Jet, contract() |
| HH exact energy cancellation와 nonphoto clone | 같은 residual; PHYS09 PROJECTED_ENERGY_THEOREM_KO.md | B의 nonphoto/expansion/Ψ 조립 |
| ε와 f/fhat의 원 의미 | src/energy.rs::{export,heat_epsilon} | capture_epsilon 전 99개; Jnorm 추가 없음 |
| 동일 implicit U,V,W 및 negative W_e | inputs/phys09/PROJECTED_RESULTS.json, DECISION.json | exact_input(), 별도 inverse 없음 |
| Full chain rule과 finite ratio | 이 문서 (10), (17)–(21) | contract(), intersect(), same-family ratio intersection |

표의 candidate/src 및 src 경로는 `inputs/ncp07/raw/` 아래다. 원 NCP07 source delivery는 `4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b`, PHYS09 science core는 `3e409503c40a7899033126a458b1cb06b227978a`, core subtree는 `afdef4725df9fdb084038d291343ac371ef96196`다. Commit·hash는 identity 근거이며 물리적 모델 타당성이나 native authority를 그 자체로 보장하지 않는다.

## 10. 판정 범위

새 수학 결과는 같은 captured-source family의 두 first-stage 문제에서 Iγ>0, I_e+Iγ의 작은 uniform/finite 포함, 같은 family의 보상 비율이다. Total의 부호는 `ZERO_CONTAINING`이며 exact zero 또는 부호 승격은 `UNRESOLVED`다. Native root/U/V/W/I는 null, native authority는 false를 유지한다.

Carried second_half, full/two-half paired defect, time/continuum remainder, full49, production 및 전체 transport/guard/escape/redshift conservation은 이 문서의 채택 대상이 아니다. PHYS07 analytic-reference energy OPEN 및 원 NCP07 node32 per-node predicate의 OPEN도 소급 변경하지 않는다. 이론·수치 creator의 주장은 `theory/CLAIMS_GAS_PHOTON_LEDGER.json`에 정리했고, 최종 독립 결정은 `review/DECISION.json`을 따른다.
