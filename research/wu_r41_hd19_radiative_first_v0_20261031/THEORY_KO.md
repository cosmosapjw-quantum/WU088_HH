# WU088_HH R41 | 원전 기반 방사·충돌 경쟁 및 원본 분광 외부이탈

## 모델과 원전

계산 대상: HD + H⁺의 비화학적, 외부에서 고정된 `Tgas`, `n(H+)`, 흑체 경계(`OFF`,`z=0,30,100,300`)에서 HD(v=1,J=0..6)의 **최초** HD(v=0,J=0..11) 도달. JCP 157,214302 (2022) DOI `10.1063/5.0128598`의 원본 rate 체계와 EMAA `HD.Rovibration.805a7aa5.radex` (dataset DOI `10.17178/EMAA_HD_Rovibration_805a7aa5`)의 원전 52 HD 분광준위, 368 A_ul 방사전이, H⁺ 충돌률 171×25. 원본 R36 Python code SHA256 `c982bdd3...`, RADEX SHA256 `b0db1613...`, GL inelastic tokens SHA256 `58c252a1...`; 전체 exact hashes는 `INITIAL_CHECKPOINT.json` 참조.

선행 R40 PR #179 HEAD `2d225e91040df59f45a158c7ba3d97e89741cfb1`은 충돌만의 first-v0 hitting 결과다. 이 값을 바꾸지 않고, 동일 원본 데이터로 방사 효과를 추가한 별도 연구단위다. GL-printed hybrid는 GL2022 보충자료에서 분명히 읽히는 1,548개의 rate cell만 EMAA 대응값으로 교체하는 원전 민감도 비교이지 원저자의 50개 불일치 셀 교정이 아니다.

## 이론 유도

Source original HD 19 states의 column generator를 `K=C(Tgas,n)+Rsp+Rstim+Rabs`로 놓는다. 상호전이의 비대각항은 확률 유출 비율이고 대각항은 각 열의 비대각항 합을 음수로 취한다. `U={v=1,J=0..6}` (7개 transient), `A={v=0,J=0..11}` (12개 first-hit absorbing). H⁺ 충돌 상향률은 원래 하향률로부터 상세평형으로 구축한다.

\[
k_{l\to u}(T)=k_{u\to l}(T)\frac{2J_u+1}{2J_l+1}\exp\!\left[-\frac{hc\,100(E_u-E_l)}{k_BT}\right]
\]

여기서 `E`는 cm⁻¹, `hc×100 E`는 J다. `n(H+)`는 cm⁻³, rate coefficient `k`는 cm³/s이므로 transition rate는 s⁻¹이다. 원본 A_ul는 s⁻¹, 흑체 점유수 `n_gamma=[exp(hν/k_B T_rad)-1]^-1`, `T_rad=2.7255(1+z) K`이며 `OFF`의 경우 `n_gamma=0`일 뿐 자발방출은 유지한다.

\[
R^{sp}_{l u}=A_{ul},\quad R^{stim}_{l u}=A_{ul}n_\gamma,\quad
R^{abs}_{u l}=A_{ul}\frac{g_u}{g_l}n_\gamma.
\]

열이 유출확률인 convention에서 transient fundamental matrix는 `N=(-K_UU)^{-1}`(s). 최초 도달 원인 `m∈{collision,spontaneous,stimulated}`별 도달확률은 `B^(m)=K_AU^(m) N`, 그 합 `B`의 각 열 합이 1 (closed 19-state first-hit definition). 최초 도달시간은 `tau=1ᵀ N` (s). 고정된 원본 광자전이의 기대 사건 수는 `sum_{u in U} N_ui r_(j<-u)`이며, source spectroscopy에서 유도된 각 전이의 방출과 흡수 사건을 따로 기록한다.

종료 전 기대 방사 에너지는 (방출 양/흡수 음의 부호로) `Qrad_i=Σ_{u∈U,j≠u} (E_u−E_j) R_(j u) N_(u i)`, 충돌로 전달된 내부에너지는 같은 식에서 `C`를 사용한다. 따라서

\[
Q_{{\rm rad},i}+Q_{{\rm coll},i}
=E_i-\sum_{a\in A} B_{ai} E_a.
\]

이는 모델의 경로별 HD 내부에너지 항등식이다. 단일 HD 분자에 대한 평균이며, 가스의 순가열률·광학두께·관측 스펙트럼이 아니다.

## 원전 52준위의 알려진 외부 방사 경로

R36 RADEX에는 19 상태보다 높은 52 준위까지 A_ul가 있다. `U`에서 스펙트럼으로 알려진 상위 상태 `X={indices20..52}`로 가는 흑체 흡수전이 **62개**가 있으므로, high-z에서 이를 무시한 closed-HD19 근사는 모든 first-v0 확률을 1로 만드는 구조적 과대계산을 한다. 원본에 존재하는 전이만 적용해 `S_(x u)=A_(x u)(g_x/g_u)n_gamma` (s⁻¹)를 정의하고, 바깥으로의 **최초** 방사 이탈을 별도 absorbing 사건으로 둔다. 

\[
N_\mathrm{open}=\left[-K_{UU}+\mathrm{diag}\left(\sum_{x\in X}S_{xu}\right)\right]^{-1},\quad
B_{v0}^{(m)}=K_{AU}^{(m)}N_\mathrm{open},\quad
B_\mathrm{out}=S N_\mathrm{open}.
\]

각 초기 transient에서 `Σ_a,m B_v0^(m)+Σ_x B_out=1`. outside 첫 흡수 광자 에너지를 방사 순전달 `Qrad_ext=Σ_(x,u)(E_u−E_x) S_xu N_open`에 포함하면 `Qcoll+Qrad=E_initial−Σ_A Bv0 E_A−Σ_X Bout E_X`가 성립한다. 밖으로 이탈한 뒤의 방사·충돌·재진입은 계산하지 않는다. 특히 외부 충돌률 미공급은 물리적 0을 뜻하지 않는다. **첫 이탈**은 **영구 분자 파괴**가 아니다.

## 새로운 판별 물리량

`n_(1/2)`는 **19준위 closed first-v0 diagnostic**에서 각 초기 준위마다 `P_coll(first-v0)=P_rad(first-v0)=1/2`를 만족하는 H⁺ 밀도다. 원전 그리드 온도 10개 × blackbody 경계 5개 × 초기 J 7개 × 두 source lane = 700 근을 실제 계산하였다. 브래킷 범위 10⁻⁴–10⁹ cm⁻³ 안에서 각각 수치적 근을 찾았지만, 일반적으로 모든 가능한 고정점의 유일성은 증명하지 않았다. 외부 source escape가 있는 경우 `n_(1/2)`는 폐쇄-계 조건부 진단값이며 외부 이탈과 함께 보고한다. 이 밀도를 우주론적 이온화율 또는 임계 우주론 변수로 읽지 않는다.

## 물리적 상태

이론 `DERIVED`, 결과 `NUMERICALLY_CHECKED`, 코드 `IMPLEMENTATION_VERIFIED`는 정확히 위 유효범위에 한한다. 신규 3체 산란 S-matrix, 실제 chemical Q, 관측 우주론적 냉각률, 원저자 rate 수정, 독립 저자 R6/C9은 **NOT_DONE**. Canonical DAG `34/49` 변동 없음.
