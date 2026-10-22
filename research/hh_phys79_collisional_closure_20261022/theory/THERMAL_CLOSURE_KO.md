# PHYS79 CI/CX 열·이온화 에너지 계약: 독립 유도

## 근거와 범위

**판정:** 아래 보존식과 온도 방정식은 명시된 단일 온도 이상기체·유한 반응망 가정하에서 직접 유도되었고, Wolfram의 기호식 검산과 유리수 stoichiometry 검산을 통과했다. 각 원자 반응률의 적용 온도·분기·방사 에너지 모멘트는 별도 source admission 사항이다. 이 문서는 새 우주론 trajectory를 실행하지 않았다.

읽은 원본은 `cosmosapjw-quantum/WU088_HH`의 `91d0846a940abf7817c900102dab488ff87e6a82`이다. `source/atomic_network.py`의 Git blob은 `cbc9c5bd0e2a6f9a56b4afc0fbc5ad6f5cba2de2`, `source/coupled_model.py`의 blob은 `cf19e688f1cd258a9a675737c0dcbe934855f2f8`이다. 경로 접두사는 `research/hh_phys78_sandbox_nuclide_20261021/`이다. 소스는 `binding_eV`를 중성종에서 0인 **양의 누적 이온화 에너지**로 정의한다. 음의 원자 결합에너지와 부호를 혼용하지 않는다.

대상은 non-tilted LRS Bianchi I의 같은 normal orthonormal frame이다. Metric signature는 `(-,+,+,+)`, 고유시간은 `t`, 평균 팽창률은 `H=theta/3`이다. 반응 기체는 단일 Maxwellian 온도, 비상대론적 단원자 이상기체이며 `pi_gas=0`이다. Collisionless DM의 `pi_m`과 collisionless radiation의 `pi_r`는 기존 별도 텐서이다. 이 유도에는 해당 텐서의 변경이 필요 없다. 압력의 등방성 때문에 기체 에너지식의 전단 일 `sigma:pi_gas`는 0이다.

## 1. 상태, stoichiometry, 차원

기준 H1 핵의 고유밀도를 `n_H`라 하여 `dn_H/dt=-3H n_H`로 둔다. 원자·이온·중성자 슬롯의 abundance는 `Y_i=n_i/n_H`이고, 자유전자 abundance는 전하중성으로

\[
x_e=\sum_i q_iY_i,\qquad n_e=n_Hx_e
\]

이다. 각 반응 `r`의 순 stoichiometric column을 `S_ir`, 고유부피당 사건률을 `J_r [cm^{-3}s^{-1}]`, 기준 H당 사건률을 `R_r=J_r/n_H [s^{-1}]`로 정의하면

\[
\dot{Y}_i=\sum_r S_{ir}R_r,\qquad
\dot{x}_e=\sum_{i,r}q_iS_{ir}R_r.
\]

`C_ai`가 isotope `a`의 membership 행렬이면 핵변환이 없는 원자과정은 `CS=0`이다. 따라서 각 isotope와 핵자수 `sum A_iY_i`를 보존한다. 전자 슬롯까지 확장한 행렬에서 전하행은 `(q_i,-1)`이고, 이 행과 각 반응열의 곱이 0이다. 전자수 자체는 CI와 RR에서 변하므로 핵 보존과 동일하게 취급하지 않는다.

단위는 기존 모듈과 맞춰 `n_H,n_e`는 `cm^{-3}`, `k_r`는 `cm^3 s^{-1}`, `T`는 K, 에너지는 eV, 시간은 s를 쓴다. `k_B=(1.380649e-23)/(1.602176634e-19) eV/K`를 유지한다. 방사 에너지가 `hbar omega`로 주어지면 동일한 eV 환산을 수행한다. `m c^2`로 쓰는 불변 rest-energy 기준은 원자 이온화 사건에 따라 자유전자가 하나 늘어도 바뀌지 않는다. 묶인 전자가 자유전자로 옮겨진 것이므로 전자 rest mass를 새로 추가해서는 안 된다.

## 2. 하나의 전역 이온화 에너지 벡터

각 isotope의 중성 바닥상태를 0으로 두고

\[
\epsilon_{a,0}=0,\qquad
\epsilon_{a,q}=\sum_{j=0}^{q-1}I_{a,j}
\]

로 정의한다. `I_a,j`는 `a^j -> a^(j+1)+e`의 에너지 문턱이다. 기준 H당 이온화 에너지와 반응별 변화량은

\[
b=\sum_i\epsilon_iY_i,\qquad
\Delta\epsilon_r=\sum_i\epsilon_iS_{ir},\qquad
\dot b=\sum_r\Delta\epsilon_rR_r.
\]

같은 ionic potential을 PI, RR, CI, CX 모두가 사용해야 한다. 계수 fit의 문턱은 kinetics provenance로 별도 보관하되, 열·이온화·광자 장부에는 서로 다른 문턱을 무기록으로 섞지 않는다. `Delta epsilon`을 반응마다 임의로 주입하는 방식보다 `epsilon @ S`로 생성하는 방식이 닫힌 reaction cycle의 에너지 drift를 막는다.

## 3. 전자충돌 이온화 CI

\[
A^q+e\longrightarrow A^{q+1}+2e,
\qquad R_{\rm CI}=n_Hx_eY_{A^q}k_{\rm CI}(T).
\]

원자 슬롯의 변화는 `(-1,+1)`, 자유전자 순증가는 `+1`이다. 입사 전자 에너지가 `E`이면 이온화 후 전자들의 총 운동에너지는 바닥상태 최종종·무복사 근사에서 `E-I`다. 따라서 전체 단일 온도 기체에 대한 사건당 열손실은

\[
\Delta\epsilon_{\rm CI}=I,\qquad
q_{{\rm th},\rm CI}=-I,\qquad E_{\gamma,\rm CI}=0.
\]

즉 CI 열항은 `-sum I_r R_r`이다. 입사 전자의 평균 운동에너지 전체를 빼면 최종 자유전자들의 남은 에너지를 잃는다. 동일한 이유로 `-3k_B T/2`를 `du/dt`에 추가하면 새 전자에 따른 입자수 효과를 중복 계상한다.

Maxwellian rate가 `k(T)=const T^{-3/2} integral_I^infinity sigma(E) E exp[-E/(k_B T)] dE`로 주어지면 반응으로 선택된 입사 전자의 평균 에너지는

\[
\langle E_{\rm in}\rangle_r=k_BT\left(\frac32+\frac{d\ln k_r}{d\ln T}\right).
\]

이 모멘트는 반응 전후 에너지 분할 분석에 쓰이지만, 위의 무복사 바닥상태 CI 열손실은 여전히 `I`다. Excitation-autoionization, 이차전자 비열분포, 방사 분기가 포함되는 경우에는 그 추가 에너지 disposition을 별도로 모델링한다.

원자율이 활성화되면 60 eV 광자 cutoff만으로 Li III/IV의 정확한 영을 주장할 수 없다. PHYS78의 영은 그 PI+RR 입력과 반응망에 속한 결과다. 새 CI fit의 범위와 사건률이 허용되면 Maxwellian tail을 통한 고전하 생성이 별도 채널이 된다.

## 4. 전하교환 CX와 방사 분기

수용 이온 `A^q`와 전자 공여종 `B^r` 사이의 과정은

\[
A^q+B^r\longrightarrow A^{q-1}+B^{r+1},
\quad q\ge1,\quad r<Z_B,
\quad R_{\rm CX}=n_HY_{A^q}Y_{B^r}k_{\rm CX}(T).
\]

양 isotope의 핵수와 총 이온 전하가 보존되어 자유전자 순변화는 0이다. 바닥상태 에너지 결손은

\[
\Delta\epsilon_{\rm CX}=I_{B,r}-I_{A,q-1}.
\]

무복사 바닥상태 CX이고 생성종의 recoil이 단일 온도 기체에 열화된다면

\[
q_{{\rm th},\rm CX}=I_{A,q-1}-I_{B,r}=-\Delta\epsilon_{\rm CX}.
\]

예를 들어 기존 PHYS78의 rounded potential에서 `He+ + H -> He + H+`는 `10.99 eV`를 열에 주고, 역반응은 동일 에너지를 소모한다. `Li + H+ -> Li+ + H`의 바닥상태 에너지 이득은 `8.208 eV`이다. 이는 **에너지 결손 계산**이며 해당 total rate의 최종상태 분기를 정한 것은 아니다.

일반적으로 사건당 탈출 광자 에너지 모멘트를 `E_gamma,r >= 0`라 두면

\[
q_{{\rm th},r}=-\Delta\epsilon_r-E_{\gamma,r},\qquad
\dot b_r=\Delta\epsilon_rR_r,\qquad
\dot u_{\gamma,r}=E_{\gamma,r}R_r,
\]

이므로 `q_th,r + Delta epsilon_r + E_gamma,r=0`이다. Radiative charge transfer의 광자는 에너지 결손뿐 아니라 충돌입자의 운동에너지 일부를 포함할 수 있다. 따라서 방사 total rate 하나로 `E_gamma`를 정할 수 없고, `E_gamma=-Delta epsilon`을 자동 채택하여 열항을 0으로 만드는 것도 별도 근거가 필요하다. 들뜬 최종종을 생성하는 nonradiative charge transfer도 들뜸 에너지가 내부 저장되는지 이후 광자로 빠지는지를 정해야 한다. `k(T)`가 주어진 것과 `q_th(T)`가 닫힌 것을 별도 상태로 기록한다.

### D/H 에너지 결손

Parent의 source 조사에서 선택한 Savin 계열 `D+H+ <-> D+ +H` 계약은 `I_D-I_H ~=43 k_B K`를 사용한다. PHYS78의 isotope-blind potential은 이를 정확히 0으로 만든다. 새 isolated control에서

\[
I_D=I_H+43k_B\,{\rm K},\qquad
43k_B\,{\rm K}=0.003705453302722426\ {m eV}
\]

를 명시하면 `D+H+ -> D+ +H`는 그만큼 흡열이고 역반응은 발열이다. 이는 새로운 isotope-aware potential이며 PHYS78의 역사적 파일을 바꾸지 않는다. 우주론 통합 시에는 D의 PI/RR/CI 에너지식도 같은 potential에 맞춰 연결해야 한다. CX 열항만 변경하면 기존 `binding_eV @ dY`와 불일치가 생긴다.

## 5. 입자수, 온도, 팽창

전체 열 입자수는 `N=sum_iY_i+x_e`, 기준 H당 열에너지는 `u=(3/2)k_B T N`이다. 원자 반응은 핵수를 보존하므로 `dot N=dot x_e`이다. 이상기체 에너지식으로부터

\[
\boxed{\dot u=-2Hu+q_{\rm th}},\qquad
\boxed{\dot T=-2HT+\frac{2q_{\rm th}}{3k_BN}-\frac{T}{N}\dot x_e}.
\]

CI에서 두 번째 항은 이온화 threshold를 공급하는 냉각이고, 세 번째 항은 늘어난 열 입자수에 에너지가 나뉘는 효과다. CX는 `dot x_e=0`이므로 그 방향의 열항만 온도에 반영된다. RR에서는 전자가 줄어 세 번째 항의 부호가 양이지만, 실제 최종 온도 변화는 포획 전자 운동에너지의 방사 손실과 함께 평가한다.

원본 coupled code는 `u`를 직접 진화시키고 `T=2u/(3k_BN)`로 읽으므로 입자수 항은 이미 구현 구조에 포함되어 있다. CI/CX 확장에서 `out[I_U]`에 전자수 보정항을 다시 더하지 않는다. 기존 `x=ln(a/a_initial)` 좌표에서는

\[
Y'=SR/H,\quad u'=-2u+q_{\rm th}/H,\quad b'=\epsilon\cdot Y',
\quad u_\gamma'=-u_\gamma+Q_\gamma/H.
\]

고유부피당 `U=n_Hu`, `B=n_Hb`, `p=2U/3`를 쓰면

\[
\dot U+5HU=n_Hq_{\rm th},\qquad
\dot B+3HB=n_H\dot b.
\]

무복사 원자 충돌에서 `q_th=-dot b`이므로

\[
\dot U+\dot B+3H(U+B+p)=0.
\]

탈출 방사 에너지밀도 `E_rad`를 포함하면 `dot E_rad+4H E_rad=n_H Q_gamma`를 더해 전역 교환이 닫힌다. 압력 없는 positive ionization potential에 `5H`를 적용하거나 광자 에너지에 `3H`만 적용하면 팽창 일이 잘못된다.

## 6. 다른 열과정과 통합 경계

PI는 흡수 광자 에너지에서 `Delta epsilon`을 뺀 excess를 열로 주고, Case A RR은 방사된 threshold+포획 운동에너지를 탈출 광자 reservoir에 둔다. 기존 `P_abs-q_heat-dot b-Q_RR=0` 구조에 CI/CX의 별도 항을 더하면 된다. CI를 위해 외부 UV source reservoir를 차감하지 않는다.

Collisional excitation은 이온화 상태의 `Y`를 바꾸지 않으면서 열을 들뜸·탈출 광자로 옮긴다. 이를 CX나 CI threshold에 넣지 않는다. Free-free 역시 별도 photon/thermal exchange다. Compton 항은 CMB 혹은 지정 radiation bath와의 energy exchange를 필요로 하므로 18/30/60 eV 광자 세 칸만으로 closure가 정해지지 않는다. Heat sink에만 항을 넣는다면 bath가 prescribed external reservoir임을 명시하고 총 폐쇄계 energy claim을 조정해야 한다.

코드 adapter는 최소한 `S`, 전역 `epsilon`, `rate(T,state)`와 그 온도 범위, `energy_disposition`, `E_gamma(T)`의 구현·근거 상태를 받아야 한다. Rate만 있고 에너지 모멘트가 없으면 그 항은 source inventory에는 보존하되 완결 열연산자에는 넣지 않는다. 새로운 우주론 history의 admission은 low-T까지 포함하는 CI fit, CX 최종상태/방사 모멘트, isotope-aware PI/RR potential 연결을 닫은 뒤 판단한다.

## 7. 실제 검산

`WOLFRAM_RECEIPT.json`은 Wolfram context 요청, 최초 JSON 출력 형식 실패, 동일 대수의 InputForm 재실행 성공을 보존한다. 실패 원인은 기호 `chiA`가 strict JSON 문자열이 아니었던 출력 직렬화이다. 성공 결과는 핵수·전하·사건 에너지, per-H 열식, proper-volume 열/이온화식, 총 충돌 에너지식, PI/RR 교환식에서 정확한 0을 반환했다. CI 입자수 변화는 `+1`, CX는 0이다.

`verify_stoichiometry.py`는 독립적인 Fraction 산술로 21개 원자 슬롯+전자에서 13개 CI 구조와 140개 서로 다른 isotope 사이의 CX 구조를 검사했다. 모든 isotope·핵자·전하 보존과 `Delta epsilon +q_th=0`이 정확히 성립했다. 140이라는 수는 **허용률이 채택된 과학 채널 수가 아니라 가능한 전하이동 연산자 구조의 시험 수**다. 결과는 `STOICHIOMETRY_EXACT_CHECK.json`에 있다. ODE 실행 수는 0이다.

Strong no-go를 신규 결과로 주장하지 않는다. HH_R10=OFF; production admission NOT_ISSUED.
