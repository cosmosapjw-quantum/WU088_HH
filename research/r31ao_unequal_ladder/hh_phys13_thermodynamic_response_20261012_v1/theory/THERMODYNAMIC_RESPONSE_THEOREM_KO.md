# WU088_HH PHYS13 — 유한 전자·온도 응답과 냉각 성분의 분해

2026-10-12. 이 문서는 PHYS13의 **이론 후보**다. 정리·항등식의 근거 상태는 `derived`, PHYS09–12 root/source 조건은 `inherited`다. 이 작성자는 새 수치 포함 프로그램을 실행하지 않았으며 최종 독립 판정자가 아니다. 실제 수치 결과와 최종 채택은 owner의 계산 및 별도 decision reviewer의 결정을 따른다.

이번 새 질문은 동일 first-stage HH ON/OFF family에서 추가 자유전자의 양, 온도의 절대 유한 응답, 온도 감소를 만드는 열에너지 변화와 입자수 변화의 상대 기여를 닫는 것이다. **PHYS09가 이미 계산한 양의 mixed temperature 포함을 새 발견으로 세지 않는다.** 그 기존 포함을 새로운 absolute response와 연결하면 photon birth가 HH 냉각을 억제하는 유한 비율을 얻을 수 있다.

## 1. 고정 family, 관측량, 원 source의 온도 규약

각 stage에서 원 PHYS09–12의 고정 coefficient tuple을 α라 하고

\[
g=(x,y_1,y_2,w),\qquad
\theta=(\lambda,b)\in[0,1]^2,\qquad
G=g-g^- -dF(g,\lambda,b;\alpha)=0
\tag{1}
\]

를 유지한다. λ는 선택한 미래 HH 소스의 강도, b는 선택한 미래 photon birth의 강도다. 과거 COMMON, 저장 광자와 보정은 λ=0 또는 b=0에서도 유지한다. d, density, atomic leaves 및 α의 실제 관계는 θ에 대해 고정한다. 각 θ에서 다른 허용 계수를 고르는 차이는 이 family의 응답이 아니다.

이전 source-inclusion, 열린 C² real-lift, strict Banach self-map, 가역 Jacobian 조건을 상속한다. 같은 근 branch의 미분을

\[
U=g_\lambda,\qquad V=g_b,\qquad W=g_{\lambda b}
\tag{2}
\]

라 한다. Full과 first_half는 동일 COMMON에서 각각 출발하는 서로 다른 첫 stage다. 이번 관측량 변환에 실제 carried second_half가 들어가지는 않는다.

원 source가 사용하는 상수는

\[
f=\operatorname{exact}(f_{\rm He}^{\rm stage}),\qquad
\widehat f=\frac{\operatorname{exact}(n_{\rm He,stored})}
{\operatorname{exact}(n_H)},\qquad
C_T=\frac{2\operatorname{exact}(\epsilon_{\rm eV})}
{3\operatorname{exact}(k_B)}>0.
\tag{3}
\]

`coupled_primary.rs::model`은 nHe를 binary64 곱 `stage.n_h_cm3 * stage.f_he`로 저장한다. `ft03_interval.rs::ft03_interval_rhs`는 그 **저장된 nHe와 nH를 각각 constant Jet로 올린 뒤 나눈다**. 따라서 fhat는 f나 `exact(fl(nHe/nH))`와 일반적으로 다르다. kB와 eV 변환도 각각 원 captured leaf를 실수로 올린 뒤 (3)에서 나눈다. 임의의 kB_eV decimal 또는 먼저 반올림한 quotient로 바꾸지 않는다.

주 관측량은 source와 일치하는

\[
e_{\rm el}=x+\widehat f(y_1+2y_2),\qquad
\Pi=1+\widehat f+e_{\rm el},\qquad
n_e=\operatorname{exact}(n_H)e_{\rm el},\qquad
T=C_T\frac{w}{\Pi}.
\tag{4}
\]

이다. e_el의 단위는 H핵당 전자 수, n_e는 proper cm⁻³, w는 eV/H, T는 K다. e_el은 이전 문서가 e로 쓴 열·이온화 **에너지**와 다르다. 아래에서는 그 에너지에 별도 기호 E_gas를 쓴다. 단위 c, kB, eV 변환을 유지하며 자연단위를 도입하지 않는다.

`ft03_interval.rs`의 전자 밀도는 `nh*x + nhe*(y1+2*y2)`이므로 (4)의 n_e와 exact-real 수준에서 같은 식이다. Native floating execution의 값·미분과 동등하다는 인증은 이 대수적 대응과 구별한다. Source domain에서 w>0, Π>0를 사용한다.

f를 사용하는 별도 stage 관측량이 필요하면 모든 식에서 fhat를 **고정 β=f**로 바꿀 수 있다. 다만 그 결과에는 e_el,f, T_f라는 다른 이름을 붙여야 한다. β-parametric 항등식이 성립한다고 해서 실제 source의 fhat를 f로 교체해도 된다는 뜻은 아니다. 두 온도의 정확한 차이는

\[
T_f-T_{\widehat f}
=-C_T(f-\widehat f)
\frac{w(1+y_1+2y_2)}{\Pi_f\Pi_{\widehat f}}.
\tag{5}
\]

식 (5)는 coefficient readout 차이를 포함하는 데 쓸 수 있으며, 차이가 작다는 이유로 원 규약을 지우지 않는다.

근거: 보존 원문 LG062 §2.1 식 (5), LG064 §2, LG066 §1; 실제 `ft03_interval.rs::ft03_interval_rhs`의 particles·t·ne 구성 및 `coupled_primary.rs::model,valid`.

### 1.1 동일 근에서 normalization 관측량만 바꾼 bridge

δ=f−fhat, s=1+y1+2y2, U_s=U_y1+2U_y2로 놓는다. Π_f=Π_fhat+δs이고
U_e,f=U_e,fhat+δU_s다. 식 (5)를 **같은 g(λ,b;α)**에서 미분하면

\[
\boxed{\partial_\lambda(T_f-T_{\widehat f})
=-\frac{C_T\delta}{\Pi_f\Pi_{\widehat f}}
\left[
U_ws+wU_s
-ws\left(\frac{U_{e,f}}{\Pi_f}
+\frac{U_{e,\widehat f}}{\Pi_{\widehat f}}\right)
\right].}
\tag{5a}
\]

이 factorized 식은 두 거의 같은 큰 온도 미분 포함을 마지막에 빼지 않고, 원 차이의 δ 인자를 유지한다. 고정 b에서

\[
D_{\rm HH}T_f-D_{\rm HH}T_{\widehat f}
=\int_0^1\partial_\lambda(T_f-T_{\widehat f})\,d\lambda
\tag{5b}
\]

이므로 (5a)의 uniform 포함은 곧 finite readout 차이를 포함한다. 실제 source에 f를 넣어 다시 구한 근과 원 근의 차이를 (5b)가 포함하는 것은 아니다. 여기에서는 root family를 고정하고 출력 정의만 비교한다. δ=0이면 모든 bridge가 정확히 0이며, Δλ=0에서도 finite bridge는 0이다.

## 2. 전자 응답과 정확한 온도 미분

\[
a=(1,\widehat f,2\widehat f,0),\qquad
e_w=(0,0,0,1)
\]

로 놓으면 e_el=a·g이므로

\[
U_e=a\cdot U,\qquad V_e=a\cdot V,\qquad W_e=a\cdot W.
\tag{6}
\]

첨자 e는 이 문서에서 e_el의 미분을 뜻한다. n_e의 세 미분은 각각 exact(nH)를 곱하면 된다. 현재 stage에서 nH가 θ-independent라는 사실이 필요하다.

온도의 gradient와 Hessian은

\[
T_g=C_T\left(\frac{e_w}{\Pi}-\frac{wa}{\Pi^2}\right),\qquad
T_{gg}=C_T\left[-\frac{e_wa^{\mathsf T}+ae_w^{\mathsf T}}{\Pi^2}
+\frac{2waa^{\mathsf T}}{\Pi^3}\right].
\tag{7}
\]

따라서

\[
\boxed{U_T=C_T\left(\frac{U_w}{\Pi}-\frac{wU_e}{\Pi^2}\right)},\qquad
V_T=C_T\left(\frac{V_w}{\Pi}-\frac{wV_e}{\Pi^2}\right),
\tag{8}
\]

\[
\boxed{W_T=C_T\left[
\frac{W_w}{\Pi}-\frac{wW_e}{\Pi^2}
-\frac{U_wV_e+V_wU_e}{\Pi^2}
+\frac{2wU_eV_e}{\Pi^3}\right].}
\tag{9}
\]

식 (9)는 (7)의 T_gW+T_gg[U,V]다. 이전 PHYS09의 mixed-temperature 계산도 이 두 항을 사용했다. W_w의 부호만 온도로 환산하거나 첫 두 항만 남기면 다른 관측량을 계산한다.

ΠT=C_Tw를 직접 미분한 동치식은

\[
\Pi U_T=C_TU_w-TU_e,\qquad
\Pi W_T=C_TW_w-TW_e-U_TV_e-V_TU_e.
\tag{10}
\]

서로 유효한 포함으로 (9)와 (10)을 계산했다면 교집합을 사용할 수 있다. 이 교집합이 비어 있으면 실패를 보고해야 하며, 비어 있지 않다는 사실은 source inclusion의 독립 인증이 아니다.

## 3. 유한 HH ON/OFF 차이와 두 냉각 성분

고정 b에서 Δλ=λ1−λ0≥0인 유한 응답을

\[
D z(b)=z(\lambda_1,b)-z(\lambda_0,b)
\]

라 한다. 동일 C¹ branch에 기본정리를 적용하면

\[
D e_{\rm el}=\int_{\lambda_0}^{\lambda_1}U_e\,d\lambda,
\qquad Dn_e=n_HDe_{\rm el},\qquad
DT=\int_{\lambda_0}^{\lambda_1}U_T\,d\lambda.
\tag{11}
\]

uniform U_e 및 U_T 포함에 Δλ를 곱하면 (11)의 유한 포함을 얻는다. Δλ=1에서는 별도 인자가 없다. Δλ=0에서는 차이가 정확히 0이다. Unit ON/OFF의 기본 관측 조건은 b=1이지만, 전 사각형에서 uniform하면 같은 부등식이 모든 고정 b에 적용된다.

온도 차이를 열에너지 변화와 입자수 변화로 나누는 자연스러운 **같은 λ 경로의 정확한 분해**는

\[
DT=C_w+C_e,
\quad C_w=\int C_T\frac{U_w}{\Pi}\,d\lambda,
\quad C_e=-\int C_T\frac{wU_e}{\Pi^2}\,d\lambda.
\tag{12}
\]

U_w<0, U_e>0 및 w,Π>0가 실제 uniform 포함에서 확인되면 C_w<0, C_e<0이고 DT<0다. 열에너지가 감소하는 효과와, 그 에너지를 나누어 갖는 자유입자 수가 증가하는 효과가 함께 작동한다. 이 성분들은 별도의 물리 소스를 따로 켜서 만든 counterfactual이 아니다. 둘 다 같은 HH perturbation에 대한 chain rule 성분이다.

U_x>0만으로 U_e>0가 되지는 않는다. He 반응이 U_e에 들어간다. 또한 U_w<0만으로 U_T<0가 되지는 않는다. 현재 숫자가 He 성분의 음의 가능성을 압도하는지 (6)으로 확인해야 한다.

Endpoint의 정확한 검산 관계도 있다. 아래에서 0,1은 λ0,λ1 endpoint이고 동일 b,α다.

\[
\boxed{DT=\frac{C_TDw-T_0De_{\rm el}}{\Pi_1}
=\frac{C_TDw-T_1De_{\rm el}}{\Pi_0}.}
\tag{13}
\]

이는 T1Π1−T0Π0=C_TDw에서 얻는다. 특히 Π,T>0에서 Dw<0, De_el>0면 유한 차이도 음수다. 식 (13)은 실제 corner roots를 계산했다는 진술이 아니다. Endpoint 표기 없이 uniform root box와 미분을 사용하는 (11)–(12)만으로 새 포함을 계산할 수 있다.

열·입자 분해는 finite algebraic convention에 따라 달라질 수 있다. 예를 들어 endpoint 대칭 분해

\[
DT=\frac{C_T}{2}\left(\frac1{\Pi_0}+\frac1{\Pi_1}\right)Dw
-\frac{C_T(w_0+w_1)}{2\Pi_0\Pi_1}De_{\rm el}
\tag{14}
\]

도 정확하지만 각 항은 (12)의 적분 성분과 일반적으로 같지 않다. PHYS13의 ‘냉각 기여 비중’은 (12)의 λ 경로 분해로 정의해야 한다.

### 3.1 Photon birth의 양의 열에너지 응답과 음의 온도 응답

같은 family에서 추가 photon birth에 대한 V_w>0와 V_e>0가 실제로 확인됐다고 하자. 전자 증가당 순 열에너지 증가를

\[
\epsilon_b=\frac{V_w}{V_e}>0,\qquad z=\frac{w}{\Pi}>0
\tag{14a}
\]

로 정의하면 (8)은

\[
\boxed{V_T=C_T\frac{V_e}{\Pi}(\epsilon_b-z).}
\tag{14b}
\]

가 된다. 따라서 **uniform ε_b의 상계가 uniform z의 하계보다 작으면 V_T<0**다. 열에너지가 증가해도, 추가 입자가 가져오는 열에너지가 현재 입자당 평균 열에너지보다 작으면 온도는 내려간다. 동치 조건은 V_w/w<V_e/Π다. 고정 λ에서 b를 0에서 1로 바꾸는 유한 온도 차이도 ∫V_T db<0이며, 같은 변화에 대한 Dw,De_el은 모두 양수다.

현재 13.7 eV birth node는 H photoionization의 작은 excess heat를 제공하는 source다. 이 구조는 ε_b가 w/Π보다 작다는 실제 포함의 물리적 해석을 돕는다. 다만 ε_b는 전체 implicit gas feedback을 포함하는 비율이다. 그것을 한 번의 photon absorption당 `13.7−χH`와 정확히 같다고 놓거나, old photons·HH·nonphoto feedback을 없애지는 않는다. 원 source heat는 captured leaf를 유지한다.

온도와 압력의 차이도 명확해진다. 이 source의 이상기체 readout에 대해

\[
\frac{p}{n_H}=\Pi\frac{k_B}{\epsilon_{\rm eV}}T=\frac23w
\quad[\mathrm{eV}].
\tag{14c}
\]

그러므로 V_w>0이면 이 열압력은 증가하고 V_T<0와 양립한다. 입자수가 더 많이 증가하기 때문이다. HH의 U_w<0는 같은 thermal pressure readout의 감소를 뜻한다. 이 p는 전체 radiation pressure나 cosmological stress tensor의 합이 아니다.

## 4. 기존 Banach 자료로 관측량에 쓸 root box를 축소

PHYS09의 gc,r와

\[
\beta_i\ge |(CG(g_c,\theta))_i|,\qquad
B_{ij}\ge |(I-CG_g)_{ij}|
\]

가 전 영역에서 유효하고, 근 g가 Y=gc+[-r,r]에 속한다. 근은 fixed point이므로

\[
|g_i-g_{c,i}|\le\beta_i+\sum_jB_{ij}r_j=:z_i.
\tag{15}
\]

따라서

\[
Z=Y\cap\prod_i[g_{c,i}-z_i,g_{c,i}+z_i]\subseteq X
\tag{16}
\]

도 uniform root enclosure다. 저장 `banach_beta`, `banach_absK_radius`의 상계를 사용해 z를 외향으로 만들 수 있다. 관측량의 w,Π를 Z에서 평가하는 것은 원 source domain X를 임의로 줄여 source를 다시 정의하는 일이 아니다. U,V,W 및 source derivative의 기존 whole-X 포함은 그대로 유효하다. Root 포함 (15)은 기존 self-map 증명의 직접적인 귀결이며 새 nonlinear solver를 요구하지 않는다.

수치가 넓더라도 근거 없는 root point 또는 centre를 실제 온도라고 대입하지 않는다. 보존된 Z가 아니라 Y 또는 X를 사용하면 일반적으로 더 넓은 포함도 유효하다.

## 5. 에너지 행의 일차 투영과 유효 열손실 에너지

새로 유용한 correlated 포함은 Uw와 Ue를 큰 독립 구간으로 나눈 값보다 정밀한 **동일 source의 열·입자 관계**다. 원 stage-f 에너지 covector를

\[
\ell_f=(\chi_H,f\chi_{\rm HeI},f(\chi_{\rm HeI}+\chi_{\rm HeII}),1),
\quad E_{\rm gas}=\ell_fg,\quad\mathcal E=\ell_fF
\tag{17}
\]

라 한다. PHYS09의 `details[].energy_source_Jet`은 이 ℰ의 실제 source 표현이다. 같은 old state·d·α에서 에너지 residual을 한 번 미분하면

\[
\boxed{U_{E_{\rm gas}}=\ell_fU=d(\mathcal E_gU+\mathcal E_\lambda).}
\tag{18}
\]

이 식은 새 일차 투영 계산에 해당한다. 원 source의 HH direct 항 ℓ_fH=0이 ℰ를 만들 때 이미 보존돼 있어, independent [Uw]+χH[Ux]를 뒤늦게 더할 때 생기는 dependency 폭을 줄일 수 있다. 저장 ℰ의 gradient 및 direct λ slot을 모두 사용하며 원 numerical tail을 임의로 삭제하지 않는다. 새 초월함수 source 호출은 필요하지 않다.

총 자유전자 응답과 열 응답의 residual을

\[
\mathcal R=U_w+\chi_HU_e
\]

라 쓰면

\[
\boxed{\mathcal R=U_{E_{\rm gas}}
+(\chi_H\widehat f-f\chi_{\rm HeI})U_{y_1}
+\{2\chi_H\widehat f-f(\chi_{\rm HeI}+\chi_{\rm HeII})\}U_{y_2}.}
\tag{19}
\]

이는 (6), (17)을 대입한 정확한 항등식이다. f와 fhat를 같다고 놓지 않는다. ℛ에는 coupled photo·nonphoto·He·expansion feedback이 남는다. ℓ_fH=0만으로 ℛ=0 또는 Uw=−χHUe를 결론내리지 않는다.

U_e>0가 증명됐으면

\[
\boxed{\chi_{\rm eff}:=\frac{-U_w}{U_e}
=\chi_H-\frac{\mathcal R}{U_e}.}
\tag{20}
\]

따라서 direct ratio 포함과 (18)–(20)의 correlated 포함을 교차할 수 있다. χeff는 **HH amplitude를 바꿀 때 추가 전자 하나당 줄어드는 열에너지의 국소 비율**이며 단위는 eV다. 새로운 microscopic ionization threshold나 HH event당 에너지의 독립 측정이 아니다. Source의 threshold χH와 얼마나 가까운지는 (19)의 실제 포함이 판정한다.

유한 ratio도 같은 구간에 속한다. U_e>0에서

\[
\frac{-Dw}{De_{\rm el}}
=\frac{\int\chi_{\rm eff}U_e\,d\lambda}
{\int U_e\,d\lambda}
\in[\chi_{\rm eff}^-,\chi_{\rm eff}^+].
\tag{21}
\]

이는 양의 가중평균 정리다. 점별 비율을 그대로 적분한 양과 finite ratio를 동일시하지 않는다. (21)은 Δλ>0에서 적용하고 영길이 경로의 0/0은 정의하지 않는다.

## 6. 입자수에 따른 냉각 기여의 보수적이면서 좁은 비중

U_w<0,U_e>0에서 두 양의 냉각 크기를

\[
A=-C_T\frac{U_w}{\Pi},\qquad
B=C_T\frac{wU_e}{\Pi^2},\qquad
-U_T=A+B>0
\tag{22}
\]

로 정의한다. 점별 입자 기여 비중은

\[
\boxed{r_{\rm part}=\frac{B}{A+B}
=\frac{w}{\chi_{\rm eff}\Pi+w}
=\frac{w/\Pi}{\chi_{\rm eff}+w/\Pi}.}
\tag{23}
\]

χeff>0, w>0,Π>0에서 r_part는 w에 대해 증가하고 χeff,Π에 대해 감소한다. 독립 포함으로도

\[
\frac{w^-}{\chi_{\rm eff}^+\Pi^++w^-}
\le r_{\rm part}\le
\frac{w^+}{\chi_{\rm eff}^-\Pi^-+w^+}
\tag{24}
\]

를 얻는다. w/Π를 직접 포함하는 방식과 (24)를 교차해도 된다. 같은 root box와 (20)의 좁은 χeff 포함을 사용하면, Ue와 Uw의 공통 source amplitude가 넓다는 이유로 비중이 함께 넓어지는 것을 줄일 수 있다.

실제 유한 냉각에서의 입자 기여 비중은 (12)에 따라

\[
\rho_{\rm part}:=\frac{-C_e}{-DT}
=\frac{\int B\,d\lambda}{\int(A+B)\,d\lambda}
=\frac{\int r_{\rm part}(A+B)\,d\lambda}
{\int(A+B)\,d\lambda}.
\tag{25}
\]

그러므로 uniform r_part∈[r−,r+]이면 **finite ρ_part에도 같은 구간**이 적용된다. Energy 기여 비중은 1−ρ_part다. 둘은 합이 정확히 1인 같은 경로 분해이므로 별도의 비율 두 개를 독립적으로 fit하지 않는다. χeff와 r_part의 구간은 수치 결과이며 전체 우주론적 중요도 또는 HH 생략 예산이 아니다.

## 7. 기존 mixed temperature와 새로운 절대 냉각의 결합

동일 α에서 unit rectangle의 finite interaction은

\[
I_z=z(1,1)-z(1,0)-z(0,1)+z(0,0)
=D_{\rm HH}z(1)-D_{\rm HH}z(0)
=\int_0^1\!\int_0^1 W_z\,d\lambda\,db.
\tag{26}
\]

PHYS09 `details[].temperature_mixed_K`의 기존 포함은 Full에서
[2.589911457894497e−12, 8.84851227942642e−12] K,
first_half에서 [3.245291906525611e−13, 1.107858848529048e−12] K다.
이 값은 기존 저장 결과의 표시이며 신규 계산 횟수에 포함하지 않는다.

PHYS13에서 U_T<0를 새로 확인하고 기존 W_T>0를 유지하면

\[
\boxed{D_{\rm HH}T(0)<D_{\rm HH}T(1)<0.}
\tag{27}
\]

즉 같은 고정 stage에서 HH가 추가하는 온도 감소는 두 b 값에서 모두 존재하고, 미래 photon birth를 켜면 그 감소의 크기가 작아진다. 온도의 원래 시간 변화, photon birth 자체의 온도 기여, 전체 history의 cooling rate를 (27)로 정하지 않는다.

§3.1에서 별도로 V_T<0도 확인됐다면 U_T<0, V_T<0, W_T>0는 함께 성립할 수 있다. HH와 photon birth는 각각 현재 family의 온도를 낮추고, 하나를 켜면 다른 하나가 만드는 추가 감소의 크기는 줄어든다. 동일한 positive interaction은
`D_birth T(λ=1)−D_birth T(λ=0)=I_T>0`로도 읽힌다. 간단히 T=T0−aλ−cb+dλb, a>d>0, c>d>0인 함수가 이 세 부호의 양립성을 보여 준다. 이 관계를 ‘birth가 가스를 가열한다’라는 한 문장으로 바꾸면 V_T의 실제 부호를 잃는다.

새 absolute response와 기존 mixed result의 유한 비율을

\[
r_T=\frac{I_T}{-D_{\rm HH}T(1)},\qquad
\eta_T=\frac{I_T}{-D_{\rm HH}T(0)}=\frac{r_T}{1+r_T}
\tag{28}
\]

로 구별한다. r_T는 b=1 응답 크기를 분모로 한 보정, η_T는 b=0 응답 크기에 대한 억제 분율이다. 두 분모는 (27)에서 엄밀히 양수다. U_e>0,W_e<0가 실제 포함에서 확인되면 전자에 대해서도

\[
0<D_{\rm HH}e_{\rm el}(1)<D_{\rm HH}e_{\rm el}(0),\qquad
r_e=\frac{-I_e}{D_{\rm HH}e_{\rm el}(1)},\qquad
\eta_e=\frac{r_e}{1+r_e}
\tag{29}
\]

가 성립한다. nH가 같은 고정 상수이므로 n_e의 대응 비율은 e_el의 비율과 같다.

## 8. 구별력이 있는 exact consistency 사례

다음은 실제 NCP source 대신 쓰는 모델이 아니라, 유도·관측량 변환의 오류를 검출하는 별도 작은 사례다. 필요한 사례를 owner가 exact rational arithmetic으로 실제 실행한 경우에만 수치 검증 상태를 붙인다.

### 8.1 열에너지 감소와 H 이온화 증가만으로 온도 감소를 추론할 수 없음

β=1/10인 양의 particle chart에서

\[
x=1/10+\lambda/100,\quad
y_1=4/5-\lambda/2,\quad y_2=0,\quad
w=1-\lambda/1000
\]

를 생각한다. λ∈[0,1]에서 물리적 fraction 범위와 w>0를 만족한다. U_x=1/100>0, U_w=−1/1000<0지만 U_e=−1/25<0다. Π=(32−λ)/25이므로

\[
\frac{U_T}{C_T}=\frac{121/3125}{\Pi^2}>0,\qquad
\frac{D_{0\to1}T}{C_T}
=\frac{999}{1240}-\frac{25}{32}
=\frac{121}{4960}>0.
\tag{30}
\]

이 사례는 실제 HH source family 또는 현재 root box의 반례가 아니다. U_w<0,U_x>0라는 두 부호만으로 일반 온도 정리를 만드는 추론의 반례다.

### 8.2 원 state의 mixed derivative가 0이어도 온도 interaction은 비영

Π=P+uλ, w=w0−aλ+v b, P,u,a,v>0이며 w>0라고 하자. 모든 gas component의 mixed derivative가 0이어도

\[
W_T=-C_T\frac{uv}{(P+u\lambda)^2}<0,\qquad
I_T=-C_T\frac{uv}{P(P+u)}<0.
\tag{31}
\]

이는 (9)의 Hessian 교차항을 빠뜨린 구현을 검출한다. 반대로 w=τΠ인 정확한 isothermal family에서는 임의의 C² Π에 대해 U_T=V_T=W_T=DT=0이다. (8)–(10)의 분자와 분모 항들이 함께 상쇄되어야 한다.

### 8.3 PHYS12의 네 gas 부호만으로 mixed temperature의 부호를 정할 수 없음

β=1/10, y1=y2=0에서

\[
x=\lambda/2+b/100-\lambda b/200,\qquad
w=2-\lambda/4+b+\lambda b/100
\]

를 쓰면 전 사각형에서 U_x>0,U_w<0,W_x<0,W_w>0다. V_x>0,V_w>0도 만족한다. 그런데

\[
\frac{I_T}{C_T}
=\frac{184}{107}-\frac{35}{32}-\frac{100}{37}+\frac{20}{11}
=-\frac{360439}{1393568}<0.
\tag{32}
\]

따라서 실제 PHYS09 W_T>0는 실제 전체 Hessian 계산의 결과여야 하며 PHYS12의 gas 부호를 말로 번역해 얻을 수 없다. 이 사례 역시 원 NCP source 실행이 아니다.

### 8.4 유한 비중은 양의 가중평균

χeff 또는 w/Π가 λ에 따라 변하는 경우에도 (25)의 양의 가중평균은 pointwise bounds 사이에 들어간다. 따라서 단순 ∫r_part dλ와 실제 finite ρ_part가 일반적으로 다를 수 있다는 것을 유지한다. 상수 r_part일 때는 둘이 같다. 양의 P,u,K에 대해 Π=P+uλ, w=K/Π인 family는 U_e=u>0, U_w=−Ku/Π²<0이며 χeff=w/Π다. 이때 A=B이고 점별 r_part와 유한 ρ_part가 모두 정확히 1/2이다. 이는 w와 χeff가 모두 변하는 비자명한 사례다. 앞 절의 isothermal family에서는 -U_T=0이므로 냉각 비중을 정의하지 않는다.

## 9. 이번 후보에서 실제로 닫을 질문과 다음 구간

owner의 `results/thermo_v2/THERMO_RESULTS.json`에서 실제 계산한 새 결과는 다음과 같다. 이론 작성자가 그 실행을 수행한 것은 아니다.

1. 같은 source의 fhat, nH, kB, eV leaves에 결박한 U_e, D_e, D_ne 및 absolute DT 포함과 엄밀한 부호.
2. 같은 λ 경로의 열·입자 냉각 성분 (12)과 총합, 원 Banach 자료에 따른 관측량 root enclosure.
3. 저장 ℰ Jet의 일차 투영 (18), ℛ와 χeff, 그로부터 얻은 finite energy-per-electron 및 냉각 비중의 좁은 포함.
4. **재사용한** 기존 mixed-temperature 결과와 결합한 finite HH cooling suppression ratio, 그리고 새 선형 전자 관측량의 mixed response와 엄밀한 음수 부호. Electron suppression ratio는 식 (29)에서 유도 가능한 비율로 제시했으며, 이번 JSON의 별도 수치 산출 항목으로 계산하지 않았다.
5. 같은 source에서 V_w>0,V_e>0인데 V_T<0가 되는 ε_b< w/Π의 실제 포함, 그리고 이 진술과 positive mixed-temperature interaction의 양립성.
6. 같은 root family에서 f/fhat 출력 정의만 바꾼 factorized normalization bridge (5a)–(5b).

이 계산은 보존된 exact endpoints와 유리함수 관측량의 후처리다. 실제 native roots, actual carried second_half, 시간·continuum 오차, anisotropic scan, full49, production을 닫는다고 주장하지 않는다. Root box width와 derivative interval width를 통계적 신뢰구간이나 시간적분 오차로 해석하지 않는다.

이 결과 다음에는 두 독립 경로가 있다. 구체적인 consumer 관측량과 허용 예산이 들어오면 새 absolute T/e/n_e 응답을 기존 domain screen과 materiality 행에 적용한다. 실제 연속 두 stage를 진행할 때는 PHYS11이 정의한 gas·photon·guard carry와 새 stage의 source/root 포함을 사용해야 하며, 여기의 두 first-stage 표를 더해서 두 half history를 만들지 않는다.

## 10. 근거와 읽은 범위

| 근거 | 읽은 범위와 용도 |
|---|---|
| `sources/ROOT12THEORY.md` | 전체: fixed α, uniform FTC, absolute U_x/U_w와 기존 scope |
| `sources/LG062.md` | §§2.1, 5, 7의 온도 관측량 및 관련 결과: exact temperature convention, Banach bounds, 기존 W_T |
| `sources/LG064.md` | §2: f/fhat, source temperature normalization |
| `sources/LG065.md` | §§1–4: joint first-stage/next-stage 구분과 physical carry |
| `sources/LG066.md` | §1, §§6–9 관련 부분: same-family/carry, source-derived energy, 기존 열린 항목 |
| `inputs/phys09/PROJECTED_RESULTS.json` | schema, stages U/V/W, details root metadata·기존 temperature_mixed_K; 원 exact fractions은 owner의 산술 소비 대상 |
| `inputs/ncp07/candidate/src/ft03_interval.rs` | `ft03_interval_rhs`의 density·particles·t·ne graph |
| `inputs/ncp07/candidate/src/coupled_primary.rs` | `model`, `valid` 및 관련 normalization call sites |
| `inputs/ncp07/results/full/NATIVE_CONSTANT_LEAVES.json` | 전체: kb/ev/c/CHI binary words |

확인한 실제 파일 identity:

- `PROJECTED_RESULTS.json`: `c6329fed8c411e1592bd1a0c63ebd9ca6151e81500ed1f46fb6b40f4b7758444`
- `ft03_interval.rs`: `886580a810b8ec29c8f0b6199c0e35d82fde1f46d984a5f8f1da304326a42a42`
- `coupled_primary.rs`: `2c528f1e7dcf44622374f8421a192f75ce8cff8b1c311bbff508f9ed863d7dcc`
- `NATIVE_CONSTANT_LEAVES.json`: `9fac898db23a8556267c976aacd6f810583d608abb8c6f49afa67a690ddc7d3e`

이 hash들은 입력 identity 근거다. Source inclusion, root validity 또는 native authority를 자체적으로 증명하지 않는다. 적용한 harness는 GPT-6 Astra v4.0.0이며 core, state template, integrated-run prompt를 읽었다. 최종 PROMOTE는 이 후보 생성에 참여하지 않은 decision reviewer가 수행한다.
