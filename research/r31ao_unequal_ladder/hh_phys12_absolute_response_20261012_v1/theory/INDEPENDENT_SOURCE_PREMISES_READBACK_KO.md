# WU088_HH PHYS12 — 고정 family와 유한 HH ON/OFF의 이론 적용성 메모

작성 역할: `/root/family_premises`, 독립된 이론·원문 적용성 도우미. PHYS12 후보 코드·테스트·최종 판정을 생성하거나 승인하는 역할은 아니다. 원 scientific 프로그램, native provider/HH/FT03/implicit root, 수치 재계산은 실행하지 않았다. 보존된 JSON의 필요한 표시·구조와 원문을 읽었다. 이하의 새 결론은 **derived, conditional on inherited source inclusion and C²**이며 저장 PHYS09 산술은 이전 독립 판정이 채택한 증거다.

하네스는 지정된 `research_harness/PROJECT_INSTRUCTIONS.md`와 `state/RESEARCH_STATE.md`를 읽었다. 후자는 Untitled/NOT_RUN 초기 템플릿이므로 실제 WU088_HH 연구 상태의 authority로 사용하지 않았다. 호스트는 GPT-6 Astra Pro이고 canonical router에 정확한 Pro alias가 없다는 owner의 관측을 유지한다. 본 메모는 기존 Astra v4 continuation의 일부이며 새 모델 라우팅 확정을 주장하지 않는다.

## 1. 결론

각 고정 허용 coefficient tuple에서 PHYS09가 이미 조건부 채택한 균일 U를 b=1 경계에 제한하면,

\[
D_{\rm HH}O(1;\alpha)
=O(1,1;\alpha)-O(0,1;\alpha)
=\int_0^1\partial_\lambda O(\lambda,1;\alpha)\,d\lambda
\]

이다. 따라서 O=x_HII,w에는 저장 U의 해당 성분을 그대로 유한 차이의 포함으로 사용할 수 있다. 새로운 corner root, 시간 적분, Taylor remainder 또는 source 재평가는 필요하지 않다. 이 적용은 기존 uniform U의 적용범위 안에 있으며 새로운 미해결 수학 전제를 추가하지 않는다. 다만 원 source inclusion과 C² regularity의 검증 수준을 강화하지도 않는다. [C:15–25; T:208–270,274–314; D:/decision_scope,/same_family_conditions,/reviewed_mathematics]

저장 U_x의 엄밀한 양수와 U_w의 엄밀한 음수는, 동일 COMMON·동일 stage·동일 b=1에서 미래 HH source를 켰을 때 stage 후 HII fraction이 더 크고 thermal energy가 더 작다는 뜻이다. 이는 W_x<0, W_w>0인 혼합응답과 모순되지 않는다. 혼합응답은 HH 효과가 미래 photon birth를 바꿀 때 얼마나 달라지는지를 비교한다. [P:/stages/{0,1}/U/{0,3}; T:62–95,128–143,457–469]

## 2. 정리의 정확한 양화사와 최소 전제

Stage s는 full 또는 first_half다. 각 stage의 허용 coefficient set A_s는 COMMON의 저장 gas/photon/guard 값, transport·angular 계수, 밀도·원자계수·상수의 captured leaves 사이의 실제 관계를 보존한다. 단순히 모든 interval endpoint를 독립적으로 선택한 물리 family를 정의하는 것이 아니다. α_s는 Θ=[0,1]² 전체에서 하나로 고정한다. [T:81–95]

보존된 결과를 사용하는 논리 구조는

\[
\forall\alpha_s\in A_s\;\forall\theta\in\Theta:
\quad \exists!g_s(\theta;\alpha_s)\in X_s,
\qquad \partial_\lambda g_s(\theta;\alpha_s)\in[U_s]
\]

이다. 원 source 관계를 어긴 임의의 coefficient 선택까지 결과를 확대하지 않는다. 고정 α에 대한 미분이므로 α의 θ 의존성, carry derivative, 새 history normalization은 이 U에 들어 있지 않다.

| 전제 | 실제 근거와 현재 충족 범위 |
| --- | --- |
| 동일 α가 전체 parameter rectangle에 고정됨 | C:15,17 및 T:81–95가 명시한다. D:/same_family_conditions/0이 조건부 채택한다. 실제 exporter는 한 COMMON·한 PreBE 객체를 whole-box와 centre 양쪽에 재사용한다(S:85–94). |
| g_old와 stage duration은 λ,b에 독립 | T:318–325의 첫-stage 전제. COMMON_INPUT_SCOPE의 `/old_gas/{0,1,2,3}/gradient/{4,5}`에 정확한 0이 저장되어 있다. Historical primal compensation은 유지한다. |
| Θ 전체의 source·미분 포함 | T:221–226. S:87의 b=variable([0,1],5), S:92의 λ=variable([0,1],4), S:93–94의 같은 `pre.groups`를 사용한 whole-X 및 centre 호출이 직접 대응한다. D:/same_family_conditions/3이 source-inclusion 조건으로 채택한다. |
| 열린 source chart에서 C² | T:223,228 및 N:11–17. 두 C2_DOMAIN은 `/status=SOURCE_C2_EVIDENCED`, `/native_authority=false`다. 양의 w,p,T, strict simplex, 양의 photo denominator, 고정 provider threshold와 geometry가 근거다. `/parameter_open_extension`은 native gate 밖 실행과 구별되는 실수식의 열린 연장이다. |
| 같은 unique root branch | T:212–268. 실제 bit-lift Y⊂X, γ<1, strict positive margins와 nonsingular C를 PHYS09가 계산했다. D:/reviewed_mathematics의 BANACH_AND_C2_BRANCH는 PASS_CONDITIONAL이다. |
| U가 그 branch의 derivative를 포함함 | AU=−G_λ(T:274–279), 네 항 Neumann 합과 엄밀 tail(T:298–314). D:/reviewed_mathematics의 NEUMANN_INVERSE가 원 signed partials와 tail을 사용한 저장 산술을 채택한다. |
| FTC 적용의 regularity | b=1에서 C¹이면 충분하다. 상속된 C² branch는 더 강한 조건이다. 경계 regularity는 열린 source chart와 unique branch의 patching에서 온다(T:268). |

균일 포함이 Θ 전체에 유효하므로 edge b=1에서도 유효하다. 전체 폭의 U를 edge에 재사용하면 보수적인 폭이 될 수 있으나 이는 정확성의 실패가 아니다. 현재 단위 길이 [0,1] 적분이므로 `[D_HH O]=[U_O]`로 같은 endpoints를 쓸 수 있다. 일반 λ 구간이라면 길이 Δλ를 곱해야 한다. 비선형 관측량 O에 이 규칙을 그대로 적용해서는 안 되며 `[∂λO]=[O_g U+O_λ]`를 먼저 포함해야 한다.

## 3. full과 first_half의 chronology

두 stage는 각각 동일 저장 COMMON에서 시작한다. Full의 d는 저장 `dt_bits=41d2a05f20000000`, 즉 1.25×10⁹ s이며 first_half의 d는 `41c2a05f20000000`, 즉 6.25×10⁸ s다. 이는 두 개의 첫-stage family이고 first_half를 full의 앞 절반으로 계산한 뒤 그 결과를 carry한 것이 아니다. [T:62–64; D:/same_family_conditions/1; S:81–101]

같은 COMMON이라는 조건은 양 stage의 모든 stage coefficient가 같다는 뜻이 아니다. 실제 SOURCE_BOX의 `/nH_bits`는 full에서 `3f1a168039d8abcf`, first_half에서 `3f1a16a0487716e4`로 다르다. `/nHe_stored_bits`도 각각 다르다. 각 duration의 PreBE transport·density·birth coefficients를 갖는 α_full과 α_first_half를 구별해야 한다. [SOURCE_BOX stage별 해당 JSON pointers; S:88–95]

허용 비교는 “동일한 저장 COMMON에서 시작한 두 별도 첫 stage에서 각각 이런 HH 효과 포함을 얻었다”이다. 다음은 이 두 결과만으로 결론 내릴 수 없다.

- first_half 뒤의 carried second_half 결과 또는 full 대 two-half defect.
- 시간 정확도, 수렴 차수, Δt→0 계수, cosmological history 전구간의 HH 영향.
- 한 stage의 ON 값과 다른 stage의 OFF 값을 뺀 HH 효과.

실제 source 준비에서 Hubble triplet은 `h=[1e−14;3]`로 고정되어 있다(S:83). 따라서 이 witness가 임의의 Bianchi shear 또는 anisotropy scan을 대표한다는 추가 해석도 없다. 이는 현재 finite source-family의 범위 설명이지 결과를 무효화하는 사유가 아니다.

## 4. 무엇을 켜고 끄는가

Source는

\[
G=g-g_{\rm old}-dF,
\qquad F=R(g,b;\alpha)+\lambda q(g;\alpha)(1,0,0,-\chi_H),
\]

이며 incoming photons는

\[
N_j(b;\alpha)=\overline N_j(\alpha)+bM_j(\alpha)
\]

다. [C:17; T:83–95,128–143; M:34–54]

`λ=0`은 같은 COMMON 이후의 HH source를 끈다. COMMON에 이미 들어 있는 historical HH ON 효과와 primal compensation을 지우지 않는다. 두 COMMON_INPUT_SCOPE의 `/fresh_future_partial_ledger`가 이를 명시하고 `/historical_HH_and_compensation`이 보존되어 있다. 또한 `b=0`은 미래 photon birth를 끄며 기존 photon stock인 N̄는 남는다. 따라서 b를 “photo 전체 ON/OFF”라고 부르지 않는다. [T:62,83–95; N:5,19]

유한 HH contrast를

\[
D_O(b)=O(1,b)-O(0,b)
\]

라 쓰면 기존 mixed interaction은 정확히

\[
I_O=D_O(1)-D_O(0)
=O(1,1)-O(1,0)-O(0,1)+O(0,0)
=\int_0^1\!\int_0^1W_O(\lambda,b)\,db\,d\lambda
\]

이다. 새 `D_O(1)`과 기존 `I_O`는 다른 관측량이다. 둘 다 동일 stage·동일 α를 사용해야 하며 O(0,0)은 stage 후 근 값으로 g_old가 아니다. [T:385–406]

저장 U와 W의 부호를 함께 쓰면 더 구체적으로

\[
D_x(b)>0,\quad D_w(b)<0,
\qquad \partial_bD_x(b)<0,\quad\partial_bD_w(b)>0
\]

가 전체 b∈[0,1]에서 조건부로 따른다. 따라서 미래 birth를 늘리면 이 첫-stage family의 HH 추가 ionization은 줄고 HH로 인한 thermal-energy 감소의 크기도 줄어든다. 이는 온도 단조성, 절대 시간 냉각 또는 전체 radiation+gas energy 보존과는 별도의 명제다.

## 5. 저장된 U 표시와 물리 해석의 한계

다음은 PROJECTED_RESULTS에서 읽은 outward binary64 표시다. 이 메모에서 다시 계산하거나 반올림한 결과가 아니다. 산술 authority는 각 객체의 `/exact`이며 PHYS12가 이 표시를 이용할 경우 exact bound를 포함한다는 기존 보존 관계를 함께 유지해야 한다.

| Stage | U_x 표시 | U_w 표시 [eV/H] | 원 JSON pointer |
| --- | --- | --- | --- |
| full | [1.0277650809473623e−10, 3.1285543436406807e−10] | [−4.258214362203849e−09, −1.398677063976542e−09] | `/stages/0/U/0`, `/stages/0/U/3` |
| first_half | [5.142179344431992e−11, 1.5650392178060275e−10] | [−2.1291786200642545e−09, −6.995256928067862e−10] | `/stages/1/U/0`, `/stages/1/U/3` |

λ,b는 무차원이므로 U_x와 D_x는 fraction이고 U_w와 D_w는 eV/H다. HH 직접 반응벡터가 ionization을 늘리고 thermal energy를 소비한다는 구조는 M:37에 보이지만, 실제 implicit U의 부호는 A⁻¹의 피드백을 포함한 저장 계산으로 지지된다. 일반 nonlinear source에서 q>0만으로 U의 부호가 자동 보장되지는 않는다.

`D_w<0`는 HH ON 상태의 terminal thermal energy가 같은 stage의 HH OFF 상태보다 낮다는 뜻이다. 이것만으로 `w_ON−w_old<0`라거나 `∂_t w<0`라고 할 수 없다. T는 w/p이고 p에는 H·He ion fractions가 들어가므로 `D_T<0`도 별도 관측량 변환 없이 주장하지 않는다. 직접 HH 반응의 `ℓH=0`는 유지되지만 일반적으로 `ℓU=0`이나 `ℓD=0`는 아니다. 재결합·흡수·팽창 피드백이 gas-energy 효과를 낼 수 있다. [T:66–79,128–185,318–325]

## 6. 비율을 계산할 경우의 허용 해석

이 절은 추가 수치 실행의 요청이나 수행 기록이 아니며, ratio를 채택한다면 필요한 수학적 의미를 명시한다.

### 6.1 혼합 보정 대비 HH 효과

동일 stage·동일 α에서

\[
r_x=\frac{-I_x}{D_x(1)},\qquad
r_w=\frac{I_w}{-D_w(1)}
\]

를 계산하면 각각 **b=1의 유한 HH contrast를 분모로 한 미래-birth 혼합 보정 크기**다. 분모는 저장 U의 strict sign으로 0에서 떨어져 있다. 이 비율은 전체 ionization fraction이나 thermal energy에서 HH가 차지하는 비중이 아니고, HH OFF에 대한 상대 변화율도 아니다.

“미래 birth를 켜기 전에 비해 HH 효과가 몇 % 억제되었나”라는 의미의 분모는 b=0이다. 그 경우

\[
s_x=\frac{-I_x}{D_x(0)},\qquad
s_w=\frac{I_w}{-D_w(0)},\qquad
D_O(0)=D_O(1)-I_O,
\]

이며 해당 실수 ratios에는 `s=r/(1+r)`가 성립한다. 현재 strict signs 아래 0<s<1이다. r와 s를 동일 percentage로 보고하지 않는다. 분자·분모의 interval dependency를 무시한 quotient는 보수적인 포함으로 사용할 수 있지만, endpoint를 임의 pairing하여 오차막대나 통계적 신뢰구간이라고 부를 수 없다.

### 6.2 열에너지 비용 비율

\[
R_{wx}=\frac{-D_w(1)}{D_x(1)}
\]

의 단위는 eV per net extra ionized H다. 분자·분모의 H-normalization이 상쇄되기 때문이다. 이는 한 stage의 전체 coupled 반응으로 얻는 finite energy-change/ionization-change ratio다. 미시적인 HH event당 energy, 정확한 χ_H, HH event 수, total photon+gas conservation으로 해석할 수 없다. Helium 변화와 source feedback도 구별해야 한다.

만일 `[D_x]=[l_x,u_x]`에서 l_x>0, `[D_w]=[l_w,u_w]`에서 u_w<0라면 단순하지만 유효한 포함은

\[
R_{wx}\in\left[\frac{-u_w}{u_x},\frac{-l_w}{l_x}\right]
\]

이다. `R_wx/χ_H`는 무차원이다. 값이 1에 가까워도 exact identity의 증거가 아니다. ratio of integrals를 아무 근거 없이 integral of pointwise ratios로 바꾸지도 않는다.

## 7. 증거 상태와 남은 ceiling

| 항목 | 판정 수준 |
| --- | --- |
| FTC edge identity 및 저장 uniform U의 D_HH로의 전달 | derived; 동일 고정 family와 상속 전제에 조건부 |
| U_x>0, U_w<0 및 저장 exact intervals | 이전 PHYS09 실행에서 numerically checked / implementation-verified, 이전 독립 DECISION의 scoped adoption을 상속 |
| 원 source kernel의 전체 포함 정확성·provider/geometry의 물리 정확성 | inherited SOURCE_INCLUSION premise; 본 메모에서 새 증명·계산 없음 |
| 열린 fixed-leaf real-source C² | source evidence가 있고 조건부 채택됨; 전체 rounded/clipped executable의 C² 아님 |
| PHYS12 새 candidate 구현·표시·판정 | 본 도우미가 검증하지 않음; owner 및 독립 decision reviewer의 별도 의무 |
| Actual native root/U/V/W/I | 읽은 source/results에는 null; native_authority=false. 본 메모는 새 issuer 근거를 만들지 않음 |
| Carried second-half·paired defect·continuum·full49·production | 이 첫-stage FTC 결과의 범위 밖; 해결로 승격 불가 |

중대한 새 전제 누락은 발견하지 않았다. 가장 큰 해석 위험은 (i) α를 corner마다 바꾸는 것, (ii) b를 photo 전체 OFF로 바꾸는 것, (iii) historical HH를 지우는 counterfactual로 바꾸는 것, (iv) full/first_half를 연속 두 단계 또는 시간오차 추정으로 바꾸는 것이다. 현재 고정 b=1의 두 관측량 contrast에 범위를 유지하면 이 문제들은 피할 수 있다.

## 원문 포인터

아래 BASE는 `/workspace/scratch/b826cbaab54f/phys11/HH_PHYS11_20261011_v1/inputs`이다. 이 메모는 다음 문서 전체 또는 명시한 source code 구간과 JSON selections를 읽었다. 거대한 rational endpoints는 출력하거나 다시 계산하지 않았다.

- C: `BASE/phys09/SCIENTIFIC_CONTRACT.md` 전체 1–43행.
- T: `BASE/phys09/PROJECTED_ENERGY_THEOREM_KO.md` 1–536행. 핵심은 51–124, 208–314, 318–325, 385–406, 520–536행.
- D: `BASE/phys09/DECISION.json`; `/decision_scope`, `/same_family_conditions`, `/reviewed_mathematics`, `/limitations`, `/native_authority`, `/actual_native`와 key 구조를 읽었다. 결정은 `PROMOTE_SCOPED`, reviewer는 `/root/phys09_decision_review`, recorded time은 `2026-10-11T06:50:22.284875+00:00`다.
- P: `BASE/phys09/PROJECTED_RESULTS.json`; `/stages/{0,1}/stage`, `/stages/{0,1}/U/{0,3}/{lo,hi,lo_bits,hi_bits,sign}`, W의 같은 selections, `/details/{0,1}/source_inclusion_premise`, `/details/{0,1}/native_authority`, `/scope`와 key 구조.
- N: `BASE/ncp07/raw/theory/NATIVE_SOURCE_C2_KO.md` 전체 1–19행.
- S: `BASE/ncp07/raw/src/sourcebox.rs` 81–99행 및 101행, uniform mapping 관련 42–52행의 선택 검색 결과.
- M: `BASE/ncp07/raw/candidate/src/phys04_mixed.rs` 24–55행.
- `BASE/ncp07/raw/results/{full,first_half}/C2_DOMAIN.json`: `/status`, `/native_authority`, `/scope`, `/X`, `/open_witness`, `/open_particles`, `/open_temperature`, `/open_simplex_sum`, `/denominator_range`, `/physical_incoming_nonnegative`, `/geometry_basis`, `/thresholds`, `/threshold_chart`, `/parameter_open_extension`, `/nonneg_semantics`.
- `BASE/ncp07/raw/results/{full,first_half}/COMMON_INPUT_SCOPE.json`: `/old_gas/{0,1,2,3}/value`, `/old_gas/{0,1,2,3}/gradient/{4,5}`, `/historical_HH_and_compensation`, `/primal_ledger_comp`, `/primal_energy_comp`, `/fresh_future_partial_ledger`, `/stored_interval_not_point_identity`, `/theta_bits_meaning`.
- `BASE/ncp07/raw/results/{full,first_half}/SOURCE_BOX.json`: object structure, `/coordinate`, `/native_authority`, `/nH_bits`, `/nHe_stored_bits`, `/fHe_bits`, `/Hmean_bits`, `/dt_bits` 및 derivative field mapping. 원 interval derivative를 재계산하지 않았다.
