# PHYS81 최종 과학 보고서

## 1. 결과와 범위

PHYS80 실제 최종 HEAD `951182dd59bbb59dba454bbaab78ad56d029355a`에서 시작해 최신 접근 가능 branch·repo·전달 기록·백업을 종합하고, 새 원자물리와 핵물리 구성요소를 구현했다. 기존 완료 identity를 반복하지 않았다. 이 단원은 **유한 source CI operator, 정확한 7→3 좌표 환원, 세 방사 포획의 photon/recoil 사건 회계**를 완성했다.

새 고정 밀도 CI parcel ODE는 **3시도=3완료+0실패**다. 원자 독립 검증15논리군, 핵 독립 검증663assertions(15운동학 입력·45에너지 분할 등), 두 Wolfram 계산, 정확 유리수 Bell 양성 증명서3개를 보존했다. 27개 species/temperature profile 각각에 finite CCC, Bell64, Bell 동일 구간 적분을 새로 평가했다. 그림은 저장 자료에서만3종 PNG/PDF를 만들었다.

완료된 PHYS78/79/80, HH1231/REI729/HH74control63 및 발견한 sibling cohort 재실행은0이다. NCP0, benchmark0, 새 cosmological ODE0, 다른 process 종료0. worker와 numerical thread는 각각1이다. HH_R10=OFF, Production admission NOT_ISSUED.

## 2. 최신 자료를 어떻게 종합했는가

접근 가능한 owner repository51개에서 branch2,175개를63페이지로 끝까지 열거했고 branch-list 오류는0이었다. 선택한 PR22개는 branch HEAD와 대조했다. 직접 관련된 source/handoff 상세 요청42개 중40개는 내용이 있었고,404하나와 빈 directory하나도 기록했다. known blob10/10을 확인했다. 전체 파일을 모두 읽었다는 뜻은 아니다.

Drive inventory는508records/501names이며 도구가 명시적 전체완료 flag를 제공하지 않았다. Dropbox는5페이지477records, has_more=false까지 확인했다. 같은 파일명만으로 서로 다른 ID/size의 객체를 합치지 않았다. PHYS80은 기존 전체 byte restore 증명과 이번 metadata/로컬 hash/전달 JSON identity를 연결해 재사용했다. 새로 다시 다운로드했다고 주장하지 않는다.

비공개 ChatGPT 대화 전체를 열람할 기능은 없었다. 접근 가능한 handoff와 ledger가 대화 유래 작업을 대조하는 자료였으며, 접근 불가 대화를 전수 확인했다는 주장은 하지 않는다. 전체 private catalog와 원전 확보 감사 자료는 S0 private backup에 보존하고 공개 단원에는 관련 identity와 요약을 담았다.

| 최신 관련 결과 | 이번 결론/재사용 |
|---|---|
| WU PR136 `951182dd59bb` | 실제 PHYS80 최종 부모;142files SHA 확인, 기존3ODE 재실행0 |
| bass_cr PR96 `ba39fc75521a` | C22D finite H CI 코드·표 그대로 재사용;4IVP 및C22E8851saved samples를 반복하지 않음 |
| REI PR221 `9620e1fcc4bd`, PR222 `b4b5d289aaad` | 국소 RR/beta thermal flow 및 기존 ledger 재사용; D matched source moments는OPEN |
| REC PR125 `407a280aff51` | 실제 THERM02 8IVP완료 확인; stale PR본문보다 실행 ledger우선 |
| REC PR124 `e6ecef7624e3` | 별도 native63Compton8cohort; PR125와 합쳐 speedup을 만들지 않음 |
| BASS_HE PR88 `fd11542ea823`, PR87 `96338b7d3c04` | 중성 transport와 finite-mass component 재사용 가능성 기록; CI/reacting gas pi에 자동 이식하지 않음 |
| toy_bbn `908c24e47838` | teaching T9범위 자료; 이번 저온 source admission으로 쓰지 않음 |

상세 head·scope·차이는 inventory/LATEST_SYNTHESIS_KO.md와 SELECTED_ACTUAL_REFS.json에 있다. Exa와 SciSpace로 원전 후보·출처를 찾고 실제 author/NIST 자료를 확인했다. Wolfram은 양성·미분·에너지/stoichiometry 항등식 검산에 사용했다. 검색 응답 자체를 physical source certificate로 취급하지 않았다.

## 3. 원전 정정과 선택한 원자 operator

### 3.1 Bell fit과 isotope chemical energy

Bell1983 원본 Table5의 H I B1은 **−0.0186**이다. 2차 자료의 −0.00186과 달라 원본 PDF 픽셀을 확인하고 coefficient transcript를 남겼다. H/He/Li neutral 계수에서

\[
x=1-I/E,\quad F(x)=-A\log(1-x)+\sum_jB_jx^j,
\quad G(x)=(1-x)F'(x)=A+(1-x)\sum_jjB_jx^{j-1}
\]

를 만든다. Wolfram은0≤x≤1에서G≤0인 점이 없다고 반환했다. 독립 exact-Fraction Bernstein 증명서는 H1구간·He2구간·Li1구간의 양수 계수로 G>0을 보인다. F(0)=0이므로 E>I에서 fit의 단면적이 양수다. 이는 분석함수에 대한 명제다. 문턱 부근 측정/fit 오차는 이 증명으로 없어지지 않는다.

Li7은 일반 NIST Li I 값의 isotope 귀속을 그대로 가정하지 않았다. NIST가 연결하는 Bushaw2007 원논문은7Li의 분광 한계를 **43487.15940(18)cm^-1**로 명시한다. exact SI h,c,e로 변환하면

\[
I_{\mathrm{Li7}}=5.39172060034581\ldots\ \mathrm{eV},
\quad \delta I=2.2317\ldots\times10^{-8}\ \mathrm{eV}.
\]

계산기록의 긴 자릿수는 입력 측정 정확도가 아니다. 이 값을 chemical defect에 사용하고, 단면적 표의 incident-energy 축은 그대로 둔다. 일반 ASD 값5.391714996eV가 자연동위원소 평균이라는 근거 없는 설명도 하지 않는다.

### 3.2 사용한 에너지 구간

| 활성 종 | finite incident E, eV | 입력/단위 | chemical defect, eV |
|---|---:|---|---:|
| H1 |13.6058–968.61|C22D CCC87rows,a0²→cm²|13.598434599702,ordinary-H/HDEL convention|
| He4 |24.6–60|CCC author ground TICS27rows,cm²|24.587389011,explicit4He|
| Li7 |6–15|CCC ground CGI13rows,cm²|5.39172060034581,7Li원전|

He+의 최저 excited residual2p1/2는40.8130309000eV다. Neutral4He 한계와 합한65.400419911eV가60eV보다 크므로 지정 finite window에서는 해당 daughter excitation이 열리지 않는다. Li+ 최저 excited residual59.020708eV에7Li defect를 더한64.41242860034581eV도15eV보다 크다. 이는 초기 ground neutral, 단일 이온화, 지정된 incoming range에서의 에너지 논증이다.

He author curve는2026년4월 자료로 unpublished accuracy가 남아 있다. Li의 chemical threshold부터6eV까지 **0.6082793996541902eV**가 비어 있다. H/He에도 physical threshold와 source floor 차이가 있다. 구간 밖 σ=0은 선택한 operator의 정의이며 실제 미측정 단면적이0이라는 결론이 아니다. He3/Li6 또는 finite-mass double-Maxwell kinetics는 새로 인정하지 않았다.

### 3.3 재사용 코드와 새 모멘트

θ=kBT(eV), σ를cm²로 두면 stationary-target Maxwell 계수는

\[
K(T)=100\sqrt{\frac{8eV_J}{\pi m_e}}\,\theta^{-3/2}
\int_a^b E\sigma(E)e^{-E/\theta}\,dE.
\]

C22D의 PL cell positive-endpoint 식과 J0,J1,J2를 그대로 재사용했다. 새 평균 incoming energy에는 J3만 추가했다. 유한 구간은T에 의존하지 않으므로

\[
\frac{dK}{dT}=\frac{K}{T}\left(\frac{\langle E\rangle}{\theta}-\frac32\right).
\]

작은 argument에서는 Taylor식을, 큰 argument에서는 scaled incomplete-gamma식을 쓴다. 로그 rate와 binary64 raw-rate underflow flag를 함께 반환한다. 실제 He4의255K와300K에서 rawK=0이지만 log10K≈−495.6983,−422.7835를 보존했다.

공통 열 저장소로 outgoing particles가 열화된다는 폐쇄에서 CI의 thermal source는 **−Ichemical×event rate**다. 평균 incoming energy를 추가 loss로 빼면 기존 열에너지를 이중 계상한다. 이 공통T EOS와 stationary-target rate는 별개의 근사 조건이다.

## 4. 물리로 줄인 계산:7→3

고정 종별 핵수B_s, 초기 중성N_s0, 초기 이온X_s0로

\[
z_s=-\log(N_s/N_{s0}),\quad N_s=N_{s0}e^{-z_s},
\quad X_s=X_{s0}+N_{s0}[-\operatorname{expm1}(-z_s)]
\]

를 쓴다. xe=ΣX_s, Ng=ΣB_s+xe,

\[
u=u_0-\sum_sI_s(X_s-X_{s0}),\quad T=\frac{u}{(3/2)k_BN_g},
\quad \dot z_s=n_{ref}x_eK_s(T).
\]

이것은 지정된 고정밀도/no-expansion/no-PI/RR/CX/CE/no-radiative-loss 모델의 정확한 연속 좌표변환이다. QSS가 아니다. 각 종의 다른K_s를 유지한다. 초기N_s0>0,0≤X_s0<B_s,xe0>0인 seeded API를 쓴다. xe0=0인 수학적 absorbing state가 불가능하다는 뜻은 아니다.

\[
\partial_{z_j}T=-\frac{N_j[I_j+(3/2)k_BT]}{(3/2)k_BN_g},
\quad J=n_{ref}\{K\otimes N+x_eK'\otimes\nabla_zT\}.
\]

따라서 Jacobian rank≤2다. 작은 이온 증가량은expm1로 보존하고 음수 trial을 clipping하지 않는다. exp의 underflow와 해석적 positivity는 분리한다. 원래7상태는 별도EOS를 사용하며 보존식으로 projection하지 않는다.

### 실제 새 대조계

B=(1,0.083,4.6e−10), X0=(2e−4,0,0), T0=25370.66308424773K, nref=1e−3cm^-3, tend=1e14s로 고정했다. B는 이 대조계를 위한 명시 입력이며 새로운 BBN abundance 추정치가 아니다. 시간s=t/tend는 RHS/Jacobian에tend를 곱하는 정확한 단위변환이다.

| 계산 | 상태/solver |rtol,atol|nfev|accepted mesh points|
|---|---|---|---:|---:|
| 기본 |3/Radau|2e−8,2e−11|386|55|
| 정련 |3/Radau|2e−10,2e−13|1156|165|
| 독립 원방정식 |7/DOP853|2e−10,2e−13|89|6|

각 계산은161개의 공통 dense 표본을 저장했다. accepted mesh226점/223steps와 dense483rows를 구별한다. 미리 고정한 상태 및 T/T0 비교 gate는각1e−7이다.

| 비교 |max normalized7-state difference|max absolute ΔT/T0|결과|
|---|---:|---:|---|
|3변수 기본 vs정련|3.266791559486393e−10|6.451973914971298e−12|PASS|
|독립7변수 vs정련3변수|7.286526937377857e−11|1.35578205058459e−12|PASS|

정련해의 최종T는 **25266.558216164776K**, xe=0.0010642158051694301이다. 최종 이온 분율Xs/Bs는 H1=0.001064059898723147, He4=1.8773392812632518e−6, Li7=0.18975204005937182이다. 이 제한된 궤적에서 전자가 증가하며 CI chemical energy가 열에너지에서 이동한다.

accepted mesh의 최대 핵수 오차는2.220446049250313e−16, 최대 상대 total-energy residual은1.2492035952546755e−16이다. Hazard energy residual은 첫 적분의 구성 결과라 독립 정확도 증명이 아니다. 원래7상태와 정련 비교가 별도의 trajectory 근거다. 모든 수치는 유한 표본 검증이며 continuum certificate가 아니다.

3변수라는 구조적 절감이 이 작은 control의 runtime 우위를 증명하지 않는다. 실제 DOP8537은Radau3보다 적은nfev를 사용했다. 방법·허용오차가 다른 wall time을 speedup benchmark로 포장하지 않는다. 다음 계통에서 solver를 선택할 때 이 control이 강한 stiffness를 요구하지 않았다는 관찰을 참고할 수 있다.

## 5. Rate 진단에서 얻은 다음 연구 방향

실제 부모Tmax에서 finite rates(cm³s⁻¹)는 H1=1.6896167676316183e−11, He4=3.7079880419624424e−14, Li7=4.077941060608214e−9다. 같은 구간 Bell와의 CCC/Bell 비는각0.9272528,0.7937276,0.7340961이다. 두 model의 차이이며 어느 쪽이 실제 정답이라는 오차막대가 아니다.

Li7의 Bell 동일 구간/전체 비는Tmax에서0.9231367126146738,255K에서는4.255644038244163e−11이다. 이는 저온에서는 빠진 threshold→6eV 구간이 결론을 좌우할 수 있음을 보여주는 **모델 비교**다. He의Bellthreshold24.6과 실제 chemical threshold도 다르므로 비가1이어도 physical coverage100%가 아니다.

Bell finite-window adaptive quadrature의 보고된 상대 오차 최대는1.1613197816350031e−12, warnings0이었다. Full Bell는64-node Gauss-Laguerre이며 물리 fit error bound가 아니다. He300K window ratio1.0000000000001137의 작은 overshoot도 수정 없이 저장했으며 부동소수점 근사로 해석한다.

## 6. 핵물리:광자·반동·열 저장소

CODATA2022의 bare p,n,d,t,helion rest energies를 사용한다. 중성 원자 질량에서 임의로Zme를 빼지 않았다. a+b→c+γ의 COM에서 Mi,Mf를rest-energy로 적고

\[
Q=M_i-M_f,\ W=M_i+K,\ \Delta=Q+K,
\quad E_\gamma=\Delta\left(1-\frac{\Delta}{2W}\right),
\quad K_R=\frac{\Delta^2}{2W}
\]

를 쓴다. 코드의Eγ,KR는 독립180digit sqrt/bisection mass-shell 해와 비교했다. K=0,1e−12,0.001,1,1000MeV의15입력,ζ3개씩45분할을 검증했다.

ζ를명시하면 저장소 변화는

\[
\Delta E_{rest}=-Q,\quad\Delta E_{th}=\zeta K_R-K,\quad
\Delta E_{nonth}=(1-\zeta)K_R,\quad\Delta E_\gamma=E_\gamma,
\]

이며 합은0이다. 모든Q를gasheat로 넣지 않는다. ζ는 thermal population membership 또는 stopping rate를 정하지 않는다.

|Cold COM channel|Q,MeV|Eγ,MeV|KR,eV|
|---|---:|---:|---:|
|n+p→d+γ|2.22456637|2.22324871192134|1317.65807866|
|n+d→t+γ|6.25723026|6.25027636127258|6953.89872742|
|p+d→helion+γ|5.49342331|5.48806102630795|5362.28369205|

숫자는 반올림된 권고질량의 산술 결과다. 원자료 covariance를 전파한 물리 정확도로 긴 자릿수를 해석하지 않는다. 핵수 A와전하 Z는보존되고nuclear particle count는사건마다−1이다. Fully stripped neutrality electron count 변화는0이다.

열 population의baryon당 입자수N이 명시됐을 때

\[
\dot T=-2HT-T\frac{\dot N}{N}+\frac{2q_{th}}{3k_BN}
\]

라는 기존 ledger 구조에 연결할 수 있다. 그러나 cold event의ζ만으로N을자동결정하지 않는다. Finite-T Maxwell source, normal-frame photon direction/energy, fast-product stopping, 실제 nuclear rates는OPEN이며 이번 코드에서활성화하지 않았다.

핵 검증의 nonblocking software 관찰도보존했다. 잘못된Decimal문자열은privatecontext밖에서parse되어 caller InvalidOperationflag를바꿀수있다. Validnumeric계산은검사한3callercontext에서동일하고context를보존한다. 모든 거부입력에flag/message동일성을주장하지 않는다.

## 7. 검증·게시·백업과 재개

원자15논리군은9species/T 독립quadrature, J3의11argument, five-point 미분,7-state pushforward, analyticJacobian,비보존manifold원상태decode, 경계T,31kernel+26parcelguard 등이다. 평균에너지 상대차최대2.8851e−16, dlogKquadrature5.3511e−16,5점미분2.6501e−12,Jacobianrow-scaled차6.1348e−11이다. 논리군·assertions·ODE·표본수는 서로다른 단위다.

실제resume은3verifiedskips,0newODE이며cohortPASS/plan/source/trajectoryhash및저장비교2개를확인했다. Profile JSON/CSV와plots는create-only다. 완료 결과를덮어쓰거나과학계산을다시실행하지 않는다.

S0는자료 대조/private감사backup, S1은유도·코드·독립검증, S2는새과학·그림, S3는최종 전달이다. STAGE_STATUS.json과delivery/가각게시/백업 상태를소유한다. StageZIPuploadACK와최종전체remote-byte/CRC/payloadSHArestore는별도다. 실제최종HEAD와최종ZIP/외부JSON의providerIDs는PR137최종본문과외부PHYS81_FINAL_DELIVERY_20261023.json으로마감한다. Git본문에자기자신의미래commit/ZIPhash를미리쓰지 않는다.

## 8. 전체 목표 DAG와 다음 일

이 단원에서 닫은 것은Bell전사/양성, finite ground-productCI 계약/코드,7→3환원과새3ODE검증, cold radiative-capture사건회계다. 전체COLLISIONAL_ATOMIC_AND_THERMAL_CLOSURE는PARTIAL이다.

다음 순서는LOW_T_CI_SOURCE_COVERAGE에서Li7threshold→6eV 자료/uncertainty를먼저확보하고, bound-boundCE/radiativecooling과He/LiCX의state/photon/energy계약을닫는것이다. 그다음연결된새identity대조계만실행한다. 핵쪽은finite-T event averaging과thermal-population/normal-frameenergy계약을먼저닫아rate/stopping에연결한다. 기존beta/RRledger를다시구현하지 않는다.

D_PI_RR_MATCHED_SOURCE_MOMENTS, RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT, LI_HARD_UV_INNER_SHELL_SPECTRAL_CONTRACT, NUCLEAR_RATES_FAST_PRODUCT_STOPPING, FULL_GEOMETRY_SPECTRAL_BACKREACTION은계속OPEN이다. 전체연구목표의고정분모가없어임의완성도%를부여하지 않는다. Non-tiltedLRSBianchiI와signedsame-frame텐서합/norm, reactinggaspi0/collisionlessDMpi_m분리는보존했다. 이번isolatedparcel은geometry/스펙트럼수송을갱신한cosmologicalevolution이아니다.

## 원전 및 재현 경로

- Bell1983: https://srd.nist.gov/jpcrdreprint/1.555700.pdf (Table5 실제픽셀 및증명서).
- CCCauthorDB: https://atom.curtin.edu.au/ccc-db/index.html (H/He/Li자료와publicationattribution).
- Bushaw2007, PRA75,052503: https://www.pnnl.gov/publications/ionization-energy-li-6li-7-determined-triple-resonance-laser-spectroscopy ; DOI10.1103/PhysRevA.75.052503.
- NISTCODATA2022: https://physics.nist.gov/cuu/Constants/Table/allascii.txt ; RMP97,025002.
- 상세원자료URL/단위/저장hash: source_data/ 및inventory/.
- 실행코드: source/finite_ci.py, parcel.py, nuclear_recoil.py, run_science.py, rate_profiles.py.
- 실제영수증: verification/, results/, figures/PLOT_MANIFEST.json.
