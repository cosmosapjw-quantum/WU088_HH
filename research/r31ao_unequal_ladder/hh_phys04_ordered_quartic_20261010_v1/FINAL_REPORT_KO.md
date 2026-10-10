# WU088_HH PHYS04 — Source 순서, 혼합 quartic, NCP 이식 계약

2026-10-10 · PHYS03 다음 물리 연구 루프

## 1. 이번 루프의 결과

PHYS04는 source 순서를 보존한 mixed quartic 유도, 선택 spectrum의 엄밀한
remap opacity 계산, reduced-BE 혼합 감도 reference 구현을 완료했다.
새 결과는 다음과 같다.

1. 선택된 25-group spectrum 전체에서는 two-half minus full remap의 HI opacity
   결함이 **음수**다. Full에 대한 상대 변화는 **−0.2319265616 ppm**이다.
   문턱 node 하나의 양의 결함을 전체 spectrum의 부호로 확장할 수 없다.
2. Old photon과 incoming U,V,W가 있어도 사용할 수 있는 source-ordered
   mixed h⁴ 재귀를 유도했다. Endpoint density drift, birth clock,
   nonphoto H/He 및 thermal feedback을 일반 식에 보존했다.
3. 별도의 zero-old-photon 특수화에서는 첫 birth의 remap이 음의 HH 혼합
   반응을 강화하는 quartic 항을 얻었다. 지정 h에서 그 고립된 항은
   inherited two-half cubic의 **+5.304951111 ppm**이다.
4. Photon 제거의 분모 Hessian까지 포함하는 implicit U,V,W 산술을 구현했다.
   이는 주어진 root candidate에서의 reference 계산이며 actual native
   root producer, FT03/LCS callback 연결 또는 finite gas 인증은 아니다.
5. NCP handoff를 실제 owner source에 연결했다. 첫 수정은 receipt 발급의
   추가 endpoint 호출을 없애는 것이고, 다음은 archived physical seed와
   새 구간의 parameter-family identity를 올바르게 분리하는 것이다.

최종 독립 판정은 **PROMOTE_SCOPED**다. /root/phys04_decision이 후보 작성과
검증 설계에 참여하지 않은 별도 검토자로서 C01–C06을 명시된 범위에 한해
승격했다. Blocking finding은 없었다. **C07의 actual finite mixed sign,
finite gas remainder, continuous error와 physical/production admission은 HOLD**다.
원 판정은 review/DECISION.json, 상세 검토는 review/REVIEW_KO.md에 있다.
이 전달본의 물리 본문은 고정된 REPORT_KO.md와 같고 이 최종 상태 문단만 반영했다.

## 2. 출발점과 물리 정의

연구 parent는 93e04c51c682216d9cb662b77a52a5783b15c71f,
actual owner는 569b04cd71e45756e0fd476aef6643bd9434f4fa다.
PHYS03 이후 두 ref의 intake delta는 0이었다. PHYS03의 봉인된 110개 payload를
hash로 확인하여 이어받았고, 완료된 PHYS01/02/03 과학 검사는 다시 실행하지 않았다.
Source bindings와 원문은 inputs/source_survey/에 있다.

상태는 z=(x_HII,x_HeII,x_HeIII,w,P)이며 w는 eV/H, P는 photons/H다.
시간은 proper seconds, 밀도는 cm⁻³다. λ는 HH ionization과 연결된
binding-energy sink를 함께 곱하고, b는 지정한 **미래 birth**만 곱한다.
b=0에서 기존 photon stock을 지우면 같은 초기상태의 혼합 family가 아니다.
Geometry, θ, grid, source shape, step clock, rates, closure와 tolerance는
네 corner에서 같아야 한다. 재시작 구간에서는 이미 생긴 U,V,W를 운반한다.

원 owner의 순서는 transport/redshift → fixed-grid hat remap 및 guards →
endpoint source weights와 birth → compensated direction sum →
endpoint density를 사용한 coupled BE → root/carry →
fixed-node absorption의 방향별 복원 → ledger/compensation이다.
Full은 비교 경로, sequential two-half가 owner 설계의 accepted 경로다.
Source 조사 SS10–SS15가 각 구현 지점을 고정한다.

HH rate와 온도는

\[
q=n_H(1-x)^2k(T),\qquad
k(T)=1.2\times10^{-17}T^{1.2}e^{-157800/T},
\]
\[
\Pi=1+f_{\rm He}+x+f_{\rm He}(y_1+2y_2),\qquad
T=\frac{2E_{\rm eV}w}{3k_B\Pi}
\]

다. q에 1/2를 넣지 않는다. He와 electron의 particle-number feedback을
온도 미분에 남긴다. Native HH rate의 35000–60000 K domain guard도 유지한다.
HI provider cutoff 13.60 eV와 binding energy 13.598434599702 eV는 다르다.
Photon excess energy의 온도를 쓰는 경우 그것은 CMB 온도가 아니다.

## 3. Fixed-grid remap의 정확한 구조

이번 수치 진단은 inputs/SELECTED_SOURCE.json의 binary64 leaf를 정확한
실수로 해석한다. 입력 SHA-256은
26a340065a9a99d02903bf0cc008baaf6ade00d2e845beb9d2b0b7d801316494다.
이 spectrum은 과거 half1 preBE 조립값이다. 실제 macro의 raw predecessor나
이번에 진화시킨 native trajectory라는 뜻은 아니다.

FLRW에서 H=10⁻¹⁴ s⁻¹, h=1.25×10⁹ s를 사용한다.
Node j가 바로 아래 cell 안에 남는 한

\[
\alpha_j=\frac{HE_j}{E_j-E_{j-1}},\qquad
L_Ae_j=\alpha_j(e_{j-1}-e_j),\qquad
s(h)=\frac{1-e^{-Hh}}H
\]

로 두면 active remap은 정확히

\[
\boxed{R_A(h)=I+s(h)L_A}
\]

다. 가장 아래 active node의 inactive 방향 유출은 active block 밖에
기록한다. 현재 inactive 0..15는 H/He 모든 photo cross section이 0이고
redshift가 이를 active sector로 되돌리지 않는다. 따라서 opacity와
photo heating을 이 quotient에서 계산하는 것이 정확하다.

전체 원 photon 배열에는 같은 매끄러운 chart를 가정할 수 없다.
원 owner에서 최저 node 10 eV의 packet은 임의의 h>0에 lower guard로
옮겨지므로 전체 원 배열에서는 R(0⁺)≠I다. Guard의 number/energy ledger를
별도로 보존해야 한다. Independent direct-hat witness에는 이 경계 규칙을
포함했다. R_A(h)를 exp(hL_A)로 바꾸는 것도 잘못이다.

δ=h/2라 하면 cell 조건 안에서

\[
\boxed{
R_A(\delta)^2-R_A(h)=s(\delta)^2(L_A^2+HL_A)
}
\]
\[
s(h/2)^2=\frac{h^2}{4}-\frac{Hh^3}{8}
+\frac{7H^2h^4}{192}+O(H^3h^5)
\]

이다. 즉 수송과 fixed-node opacity의 결합은 photon number만으로
결정되지 않는다. Commutator의 성분도
([diag σ,L_A])_ij=(σ_i−σ_j)(L_A)_ij여서 단면적 경사와 cutoff를 직접 본다.
자세한 유도는 REMAP_OPACITY_THEORY_KO.md에 있다.

## 4. 전체 spectrum에서 결함 부호가 바뀌는 이유

두 observable은
\(\mathcal O_\sigma=\sum_j\sigma_{{\rm HI},j}P_j\)와
\(\mathcal O_E=\sum_j\sigma_{{\rm HI},j}(E_j-\chi_H)P_j\)다.
아래는 엄밀한 interval의 midpoint를 반올림한 표시다.

| Observable | Full remap | Two-half remap | Two-half − full | Full 대비 |
|---|---:|---:|---:|---:|
| HI opacity, cm² photons/H | 2.4108813685103331e−19 | 2.4108808093629068e−19 | −5.5914742628126907e−26 | −0.2319265616 ppm |
| HI excess-energy weight, eV cm² photons/H | 1.9191991429028059e−20 | 1.9191990889708504e−20 | −5.3931955506219376e−28 | −0.02810128157 ppm |

Node16의 기여는 +1.1492751245328895e−24이고, 바로 위 node17의 기여는
−1.2052810061249352e−24다. Node18..24를 모두 합친 양의 기여는
약 9.1138963919e−29다. 따라서 전체 합은 음수다.
PHYS03의 단위 문턱 column 결과와 이번 aggregate 결과는 입력이 다르며
서로 모순되지 않는다. 그림은 figures/remap_opacity_contributions.svg다.

모든 exact rational endpoint 및 48자리 outward decimal은
results/REMAP_OPACITY_EXACT_V1.json에 있다. Exp(−x)의 16차 짝수 partial sum과
17차 홀수 partial sum을 각각 상·하계로 사용했다. Binary64 native operation의
rounding path를 재현한 것이 아니라, source leaf로 정의한 실수식을 감싼다.

별도 Decimal150 구현은 L_A 또는 위 결함식을 쓰지 않고 원 hat+guard map을
직접 두 번 적용했다. Full/two-half/defect의 6개 witness가 해당 interval에
들어갔다. Hat의 affine identity로 number 및 redshifted energy 보존을
증명했고, direct 계산의 4개 moment residual은 사전 기준 1e−135 이하였다.

Scalar remap 결함의 h⁴ 절단에 대한 상대 remainder는 지정 h에서
약 −6.1035406325e−17이다. 이 작은 값은 s(h/2)²의 특별한 구조에서 나온다.
Gas의 mixed h⁵ remainder나 continuous source-law error로 전용할 수 없다.

## 5. Source 순서를 보존한 일반 혼합 quartic

Endpoint birth를 B에 포함하고 F에서 제외한 한 step은

\[
z^+=R_\delta(t)z+b\delta B(t+\delta)
       +\delta F(t+\delta,z^+;\lambda),\qquad F=F_0+\lambda H_{\rm HH}.
\]

여기서 H_HH는 HH vector field다. 앞 절의 H는 expansion rate이므로
두 기호를 문맥 없이 섞지 않는다. 한쪽 remap을
R_δ=I+δL+δ²M/2+δ³N/6+δ⁴P₄/24+…로 전개하고, preBE의 raw δᵏ
increment coefficient를 d_k라 하면
d₁=Lz+bB, d₂=Mz/2+bB_t, d₃=Nz/6+bB_tt/2,
d₄=P₄z/24+bB_ttt/6이다.

\[
a_1=d_1+F,\qquad a_2=d_2+Ja_1+F_t,
\]
\[
a_3=d_3+Ja_2+\tfrac12Q(a_1,a_1)+F_{tz}a_1+\tfrac12F_{tt},
\]
\[
\boxed{
\begin{aligned}
a_4={}&d_4+Ja_3+Q(a_1,a_2)+F_{tz}a_2\\
&+\tfrac16C(a_1,a_1,a_1)
+\tfrac12F_{tzz}(a_1,a_1)
+\tfrac12F_{ttz}a_1+\tfrac16F_{ttt}
\end{aligned}}
\]

이며 J=F_z,Q=F_zz,C=F_zzz다. a_k는 raw coefficient여서 k차 도함수와
factorial이 다르다. n_H(t)의 drift는 F_t와 모든 필요한 cross derivative에
들어간다. H/He nonphoto, heating/cooling 및 HH temperature feedback은
F tensor 안에 남는다.

시간을 포함한 X=(t,z), G₁=(1,a₁), G_r=(0,a_r), D=D_X를 사용하면
two-half의 raw h⁴ coefficient는

\[
\begin{aligned}
C_4=\frac1{16}\{&
2G_4+DG_1[G_3]+DG_2[G_2]+DG_3[G_1]\\
&+D^2G_1[G_1,G_2]+\tfrac12D^2G_2[G_1,G_1]
+\tfrac16D^3G_1[G_1,G_1,G_1]\}.
\end{aligned}
\]

Incoming U=∂λz,V=∂bz,W=∂λ∂bz에 대해

\[
\mathcal M a=a_zW+a_{zz}(U,V)+a_{z\lambda}V+a_{zb}U+a_{\lambda b}
\]

를 적용한다. One-full mixed coefficient는 M a₄, two-half는
M pr_z C₄다. pr_z는 state projection이며 미분 기호가 아니다.
Derivation, assumptions와 exact 검사는 quartic/PHYS04_ORDERED_QUARTIC_KO.md 및
quartic/run_02/EXACT_CHECK.json에 있다.

이 유도는 formal local series로 성립한다. Actual finite h의 root,
uniform derivative bound와 parameter tube가 확보되어야 finite remainder를
정량화할 수 있다. Joint C⁶와 bounded compact neighborhood는 충분한
smoothness 조건이지만 이번에 그 상수를 계산하지 않았다.

## 6. Zero-old-photon 특수화의 새 물리 항

이 절만 P₀=0, U₀=V₀=W₀=0, frozen external coefficients, constant birth,
transported photon의 내부 생성 없음, photon-only L을 가정한다.
앞 절의 실제 nonzero spectrum과 다른 실험이다.

\[
\nu=1.2+\frac{157800\ {\rm K}}{T},\qquad
\Xi_j=\frac{1-x}{\Pi}\nu
\left[1-\frac{\Pi(E_j-\chi_H)}w\right],\qquad
A_j=cn_H\sigma_{{\rm HI},j}
\]

라 두면 two-half mixed quartic의 L 의존 gas x 항은

\[
\boxed{
\Delta_L[h^4]\partial_\lambda\partial_b x_{\rm two}
=-\frac q{16}\sum_j A_j(4+\Xi_j)(LB)_j .
}
\]

B는 S_*를 포함한다. 13.7 eV first birth의 다음-half remap은
LB=S_*α₂₄(e₂₃−e₂₄)다. 현재 leaf에서는
σ₂₃(4+Ξ₂₃)−σ₂₄(4+Ξ₂₄)>0이므로 이 항은 음수다.
더 낮은 에너지에서 HI opacity가 커지는 효과와 photon당 excess heat가
작아지는 효과가 해당 혼합 반응에 함께 들어간다.

지정 h에서 이 고립된 h⁴ 항을 inherited negative two-half cubic으로
나눈 비는 +5.304951110809629 ppm이다. 두 항이 모두 음수라 비는 양수다.
이를 total quartic, finite full/two-half mixed error, total HH response의
상대 오차라고 해석하지 않는다. Nonzero stock 및 old U,V,W에는 일반 재귀를 쓴다.

## 7. NCP 이식에 제공하는 혼합 감도 코드

NCP는 이 저장소의 c64-g3 cloud/local Codex lane이다. 현재 미분 대상은
smooth coupled BE equality residual이며 새 complementarity 방정식은 도입하지 않는다.

\[
P_j=\frac{N_j}{D_j},\qquad
D_j=1+d\,cn_H[(1-x)\sigma_{{\rm HI},j}
+f_{\rm He}(1-y_1-y_2)\sigma_{{\rm HeI},j}
+f_{\rm He}y_1\sigma_{{\rm HeII},j}]
\]
\[
\boxed{
P_{ab}=\frac{N_{ab}-P D_{ab}-P_aD_b-P_bD_a}{D}.
}
\]

N=0에서도 D>0이면 사용할 수 있으며 N으로 나누지 않는다.
Signed tangent는 positivity clip 대상이 아니다.
Gas residual G=y−y₀−d F̄(y,N;λ), A=G_y에서 AU=−G_a, AV=−G_b를 푼 뒤,
(y,U,V,0)을 넣은 mixed residual r_ab에 대해 AW=−r_ab를 푼다.
이는 gas Hessian, gas–photon cross derivative, inherited N_ab와 HH H_yV를 포함한다.

src/implicit_mixed.py는 이 산술, H/He photo stoichiometry와 HH의
(+q,−χ_Hq) 연결을 구현한다. 실제 rate는 callback으로 전달한다.
현재 테스트의 nonphoto/HH callback은 polynomial fixture이므로 actual
FT03/LCS provider 검증이나 native interval inverse로 승격할 수 없다.
상세 계약은 IMPLICIT_MIXED_THEORY_KO.md에 있다.

## 8. NCP local Codex의 구체적인 다음 작업

전체 복사·붙여넣기 지시는 NCP_LOCAL_CODEX_HANDOFF_KO.md,
작업 DAG는 NCP_TASKS.json, 반환 형식은 NCP_RETURN_TEMPLATE.json에 있다.
현재 owner에서 확인한 우선순위는 다음과 같다.

| 작업 | 실제 source 근거 | 완료 기준 |
|---|---|---|
| Receipt의 추가 endpoint 제거 | ENERGY06E accepted_half1_receipt의 actual_full 재호출, SS16 | 같은 실행의 private typed result로 receipt 발급; receipt/half2 resolution의 추가 endpoint/root 0 |
| 공통 physical seed로 family 초기화 | archived member1, HhRunIdentity, OFF ledger 검사, SS08–SS09/20–21 | 과거 history·physical payload 보존, future increment ledger 분리, ON→OFF retag 금지 |
| λ,b와 U,V,W의 전체 연결 | owner_birth, hh_source_endpoint, reduced photon residual, SS10–SS14 | 원 source 순서, half1→half2 carry, denominator Hessian 및 endpoint density 보존 |
| 실제 interval callback과 tube | hh_rate_jet, hh_interval_source, interval_rhs, SS12–SS15 | source-bound G_y/Hessian, fixed C, parameter rectangle, strict inclusion/contraction의 실제 증거 |
| 현재 checkout의 build/선택 검증 | receipt_contract/absolute wrappers, SS04–SS06/22–25 | wrapper relocation 기록, 실제 존재하는 대상만 실행, 미승인 dispatch refusal 유지 |

Receipt 문제는 정적 소스에서 발견한 잠재적 호출예산 결함이다.
현재 private permit issuer가 없으므로 관찰된 production runtime 실패라고
보고하지 않는다. hh_stage_root 내부에도 point solve가 있어 top-level endpoint,
conservative point solve, certificate 내부 point solve와 root producer 수를 분리한다.

Archived seed의 SHA-256은
678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b,
108416 bytes, clock 1.6e11 s, 128 directions×33 energies다.
현재 NCP host에 그 bytes가 있는지는 아직 확인하지 않았다.
Exact cache/backup에서 찾아야 하며 과거 trajectory를 재계산하지 않는다.

원 ON member1에는 과거 HH ledger가 있다. 원 OFF invariant를 완화하거나
mode byte만 바꿔 새로운 family를 만드는 것은 물리적으로 같은 초기상태와
run identity를 혼동한다. 새 family initializer는 과거 baseline과 앞으로의
HH increment를 분리하면서 원 provenance·guards·compensations를 보존해야 한다.

현재 receipt_contract main은 exit77의 과학 dispatch refusal이다.
실제 --lambda/--source-amplitude CLI가 아직 있다고 가정하지 않는다.
코드·build·새 synthetic checks까지 완료한 뒤 live source/ABI/binary/seed/tube,
정확한 호출 수·wall·memory·cgroup을 채워 미래 실행 제안을 완성한다.
현재 native authorization=null, budget=0이다. 과거의
1 macro/4 corners/12 endpoints 제안은 승인이 아니며 이번 handoff도 실행권을 새로 만들지 않는다.

## 9. 검산 결과와 보존한 수정 이력

| 새 검산 | 실제 결과 | 검증 범위 |
|---|---|---|
| Source-ordered quartic final run_02 | 6 cases, 1152 rational slots 일치; formal residuals 0 | tensor/chain-rule 재귀와 별도 time-series convolution/finite formal substitution 비교 |
| Remap operator | exact interval 및 6 independent Decimal150 witness 일치 | 25-group spectrum의 fixed-grid hat+guard observable |
| Implicit mixed arithmetic | 6 cases, 72 derivative slots 일치, 96 residual slots 0 | prescribed rational gas family와 D2+linear solve 비교 |
| Implicit domain rejection | 4 cases 거절 | singular Jacobian, 0/negative denominator, invalid threshold |

Quartic 두 계산 경로는 Fraction과 fixture RHS를 공유한다. Implicit 두 경로도
물리 algebra와 fixture를 공유한다. 각각 다른 계산 경로를 비교했지만
실제 native provider의 독립 재구현 검증이라는 뜻은 아니다.

최초 environment probe에서 Sympy가 없어 Fraction으로 진행했다.
Quartic run_01은 algebra가 통과했으나 frozen fixture에 t/47 nonphoto drift가
남은 scope-label mismatch가 발견되었다. 원 script/result를 보존한 뒤,
그 drift를 이미 선언된 switch에 연결하여 영향 범위 6 cases만 run_02로
확인했다. 일반 유도는 바뀌지 않았다. Frozen 특수화의 최종 근거는 run_02다.
세부 원본은 FIRST_ENVIRONMENT_PROBE_FAILURE.json 및
FIRST_FIXTURE_SCOPE_CORRECTION.json에 있다.

이번 실제 native dispatch, nonlinear BE root, IVP, NCP science,
legacy atomic integral, 완료된 PHYS01/02/03 suite 재실행은 모두 0이다.
그림은 저장된 결과만 표시하며 과학 계산을 다시 수행하지 않았다.

## 10. 현재 판정 상한과 다음 연구

이번 결과의 범위는 local coefficient의 유도, 지정한 실수식의 엄밀 interval,
reference arithmetic 검증, 실제 source에 연결된 구현 계약이다.
Actual common-state 네 corner와 typed accepted half1 producer가 없으므로
유한 h의 I, true continuous source-law error와 gas remainder는 null이다.
Legacy 24/289, unbounded 265, ε_C/ε_R=null, B22 OPEN은 유지한다.
Canonical S0 HH OFF, consumed ON06G 256 macros through 3.2e11 s도 그대로다.

다음 PHYS05의 물리 질문은 **기존 photon stock과 incoming mixed sensitivity가
있는 실제 source family에서 opacity-weighted defect가 gas 혼합 반응과
finite-step bound로 어떻게 전달되는가**다. PHYS04의 zero-stock 5.305 ppm을
확장하여 답하지 않는다.

NCP 구현 결과가 준비되면 source-bound reduced-BE Jacobian/Hessian 및
parameter rectangle을 PHYS04의 일반 recurrence와 대조하고, 실제 endpoint
및 half1 carry의 독립 certificate로 finite response를 판단한다.
그 producer가 여전히 없으면 endpoint-free 범위에서 nonzero-stock
quartic의 항별 부호·크기와 한쪽 geometry/remap 조건을 먼저 분석한다.
완료된 gate 목록만 반복하는 루프로 돌아가지 않는다.

최종 게시 commit, archive hash와 두 backup acknowledgement는 봉인 archive
바깥의 WU088_HH_PHYS04_DELIVERY_RECEIPT.json에 기록한다.
Archive 내부에 자기 hash 또는 아직 생성되지 않은 commit을 미리 넣지 않는다.
