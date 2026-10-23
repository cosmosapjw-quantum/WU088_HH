# PHYS84: 저장된 H I CE 결과의 보존적 순간 source

## 결과와 연구 위치

PHYS83의 source-native H I LS 1s/2s/2p 유한 연산자에서, 저장된 정확한 온도 행과 명시적인 세 준위 밀도를 받는 순간 source를 구성한다. 새 원자 rate나 population trajectory를 계산하지 않는다. 새 결과는 사건 수 → 준위 이동 → 병진열·원자 들뜸·방출광 에너지의 보존적 사상이다. 중앙 첫 노드 `WU_CE83_OWNER_COMPLETION`에는 owner PR140의 완료 identity `e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c`를 재사용한다.

정의역과 데이터는 final HEAD `6a2fc5aacb6182a916b9434c316e99e750e8273c`에 고정한다. 원 CCC 보간, finite support, Δ=10.20435 eV, A2γ=8.229/s, AM1=2.496e-6/s, AE1=6.26e8/s를 그대로 쓴다. 이들은 [PHYS83 source contract](../../hh_phys83_ce_completion_20261023/source_data/HI_CE_SOURCE_CONTRACT.json)의 원전·불확실성 경계를 따른다. source 값과 현재 공식 CCC/CHIANTI 문서를 확인한 것을 새 source accuracy 측정으로 세지 않는다.

## R1–R4: 가정과 유용한 표현

같은 normal orthonormal frame의 local proper time을 사용한다. 전자는 Maxwellian, target은 heavy stationary, H I LS 준위는 unpolarized이고 gas anisotropic stress는 0이다. 스칼라 source가 collisionless DM의 별도 π_m을 대체하지 않는다. n0, ns, np, ne는 cm^-3이고 외부에서 주어진 순간 값이다. rates q의 단위는 cm^3/s다. T는 PHYS83의 66개 저장 float64 온도 가운데 정확히 하나여야 한다. 보간·외삽 또는 다른 isotope의 온도/threshold 재해석은 하지 않는다.

필요한 분해는 ground-neutral chemical binding과 excited-state energy를 구별하는 것이다. 같은 총 H I 수를 유지하는 bound-bound 사건은 chemical ground binding을 바꾸지 않는다. 들뜸 에너지는 Uexc=Δ(ns+np)로 별도 저장한다. 이 변수를 생략하면 비정상 순간에서 열 손실과 방출광이 같다는 잘못된 식이 생긴다.

## R5: 사건과 incidence의 구성

일곱 사건 intensity를 다음 순서로 둔다.

\[
r=(u_s,u_p,d_s,d_p,r_{s,2\gamma},r_{s,M1},r_{p,E1}),
\]
\[
u_i=n_en_0q_{\uparrow i},\qquad d_i=n_en_iq_{\downarrow i},
\quad r_{s,2\gamma}=A_{2\gamma}n_s,\quad r_{s,M1}=A_{M1}n_s,
\quad r_{p,E1}=A_{E1}n_p.
\]

모든 입력과 rates가 비음수이므로 intensity도 비음수다. 전자 충돌에서는 자유 전자가 들어왔다가 다시 나가므로 ne의 사건 net source는 0이다. photon emission은 H I 준위를 바꾸며 H nuclei와 thermal H atom 수는 바꾸지 않는다.

\[
\dot n=S r,\qquad
S=\begin{pmatrix}
-1&-1&1&1&1&1&1\\
1&0&-1&0&-1&-1&0\\
0&1&0&-1&0&0&-1
\end{pmatrix}.
\]

각 column의 합이 0이므로 총 H I, nuclei, charge가 보존된다. electron source와 thermal particle-number source 역시 0이다. 각 상태가 0인 경계에서 그 상태의 outgoing intensity는 사라지고 incoming intensity만 남는다. 따라서 frozen nonnegative coefficients의 연속 rate equation은 양성 cone을 보존한다. 이번 코드는 이 순간 vector field를 계산하며 적분기를 실행하지 않는다.

병진열, 들뜸, 방출광의 사건당 에너지 row는

\[
e_{th}=\Delta(-1,-1,1,1,0,0,0),\quad
e_{exc}=\Delta(1,1,-1,-1,-1,-1,-1),\quad
e_{rad}=\Delta(0,0,0,0,1,1,1).
\]

Uexc의 정의에서 `(0,Δ,Δ)S=e_exc`가 성립한다. 각 사건에서 세 row의 합은 정확히 0이다. 따라서

\[
Q_{th}=e_{th}r=\Delta\sum_i(d_i-u_i),\qquad
\dot U_{exc}=e_{exc}r=\Delta\sum_i(u_i-d_i-r_i),\qquad
Q_{emit}=e_{rad}r=\Delta\sum_i r_i,
\]
\[
Q_{th}+\dot U_{exc}+Q_{emit}=0.
\]

Qth>0은 gas heating이다. 열 source에 incoming reaction-selected electron energy를 추가로 빼지 않는다. PHYS83의 같은 Δ를 excitation, deexcitation, storage, radiation에 사용한다. CHIANTI의 spectroscopic photon energy를 한쪽만 대입하지 않는다.

## 명시적인 radiation 소유권

`immediate_escape`는 부모의 optically thin cell boundary다. Qescaped=Qemit, Qradiation_injected=0이다. `emissivity_handoff`는 방출 source를 후속 radiation owner에게 전달하는 장부 표현이다. Qradiation_injected=Qemit, Qescaped=0으로 둔다. 후자는 transport, residence, absorption 또는 spectrum 계산을 포함하지 않는다. 두 경로 모두

\[
Q_{th}+\dot U_{exc}+Q_{radiation\_injected}+Q_{escaped}=0
\]

이며 chemical binding/source-reservoir source는 0이다. Qemit 자체는 diagnostic이므로 위 합에 다시 더하지 않는다. native radiative owner와 이 detached spontaneous owner의 동시 활성화를 거부한다. 광자는 추가 thermal particle로 세지 않는다.

2s two-photon 사건의 photon 수는 2지만 총 방출 에너지는 Δ다. 따라서 photon-number source는 `2*r_s2gamma+r_sM1+r_pE1`이고 energy source는 `Δ*(r_s2gamma+r_sM1+r_pE1)`이다. 이 정의는 각 photon이 Δ/2라는 monochromatic spectrum을 뜻하지 않는다. M1과 E1 사건도 별도 보존한다.

## 온도 source와 두 반례

외부에서 공급한 common-T ideal-gas particle density Nthermal에 대해 Uth=(3/2)kB Nthermal T다. 이 bound-bound source의 S_N=0이므로

\[
\dot T\vert_{CE}=\frac{2Q_{th}}{3k_BN_{thermal}}.
\]

사용한 kB=8.617333262145179e-5 eV/K는 부모 상수와 같다. 이 식은 local instantaneous source이다. 외부 spectral source, expansion work, ionization에 의한 Nthermal 변화, electron/ion 온도 분리 및 시간 적분은 이 adapter의 출력에서 추론하지 않는다.

1. n0>0, ns=np=0, ne>0이면 Qemit=0이지만 q_up>0인 저장 온도에서 Qth<0, Uexc_dot>0이다. 초기 충돌열 손실이 즉시 escaping luminosity와 같지 않다.
2. ne=0, ns>0이면 Qth=0이지만 Qemit=Δ A_s ns>0, Uexc_dot=-Qemit다. 이미 저장된 들뜸 에너지가 방출되는 경우다.

두 예는 해당 finite model에서 순간 `-Qth=Qemit`라는 등식을 반박한다. 과학적 novelty 또는 모든 plasma closure를 배제하는 strong no-go로 주장하지 않는다. 정상상태에서 두 excited-state source가 모두 0이면 위 보존식으로 `-Qth=Qemit`가 도출된다. 이 추가 전제 없이 coronal scalar cooling으로 축약하지 않는다.

## R6–R9: 독립 검산과 구현 수용 조건

Wolfram의 첫 evaluator는 nuclei7column, energy7column, differential energy, temperature-source, stationary reduction의 17 scalar zero를 반환했다. 같은 call의 2γ 두 항은 replacement-list 괄호 오류로 미평가였다. 원본 call과 warning을 보존하고 그 두 항만 별도 evaluator로 수정해 2zero를 받았다. 이는 새 physics identity의 기호 검산이며 PHYS83 rate나 검증 suite 재실행이 아니다.

구현은 standard-library binary64와 signed compensated sums를 사용한다. 독립 검증은 literal CSV decimal에서 만든 exact rational event/energy incidence로 비교한다. event/resolved source relative gate2e-12, signed sum 및 보존 residual/gross gate2e-13을 고정한다. G_event=일곱 event intensity 합, G_energy=Δ G_event, G_thermal=Δ×네 collision intensity 합, G_temperature=2G_thermal/(3kB Nthermal)이다. Level source는 G_event, signed energy source는 G_energy, 온도 source는 G_temperature로 오차를 정규화한다. 해당 gross가0이면 출력도 정확히0이어야 한다. 온도 계산은 Qth=0에서 정확히0을 반환하고 나머지는 (2/(3kB))×(Qth/Nthermal) 순서로 계산해 분모의 불필요한 underflow를 피한다. 무조건 residual=0을 출력하거나 음수 clipping으로 통과시키지 않는다. source SHA, 66paired T, density/Nthermal/owner/route guard와 create-only completion을 검사한다. 2γ energy2배 오류, 두 radiation destination 동시 합산, excitation reservoir 생략을 각각 구별하는 controls를 둔다.

새 제한 application은 8개의 명시적 constructed local state ×2 radiation ledger view=16행이다. 이 값들은 observed cosmological states가 아니다. parent의 실제 rates만 재사용한다. rate 계산0, population solve0, ODE0, benchmark0이다. 독립 reviewer가 실제 diff와 결과를 확인하기 전에는 새 구현 admission을 발행하지 않는다.

## 중앙 claim gate와 남은 의무

WU owner completion의 수용은 `NUMERICALLY_CHECKED_SCOPED`다. 새 local contract `WU_HI_CE_INSTANTANEOUS_SOURCE_V1`의 검증된 source preparation을 별도 노드로 기록한다. REI-L1의 excited-state/storage owner와 source/domain/clock binding은 OPEN이다. 중앙 계약의 PI/RR binding column에 Uexc를 말없이 합치지 않는다. `CONSUMER_ADMITTED`는 이 연구의 자동 결과가 아니다.

Finite-splitting2s/2p mixing, isotope/spectroscopic energy match, source uncertainty, He/Li CX, D PI/RR, nuclear finite-T event provider/stopping, recombination-to-z20 charge, Li inner-shell spectral contract 및 full geometry/spectral backreaction은 기존 OPEN 의무를 유지한다. Non-tilted LRS Bianchi I, same-frame signed tensor sum-before-norm, Frobenius=√2×half-contraction을 보존한다. sampled residual은 continuum certificate가 아니다. HH_R10=OFF; Production admission NOT_ISSUED.
