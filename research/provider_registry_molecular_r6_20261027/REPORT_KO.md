# WU088_HH R6 — literal Gibbs 구간과 강제 유한 블록 경계

**R6 이론·코드 과학 채택 완료, local DAG13/28. S10최종source와전달영수증을마감중이다.**

S09 뒤 다시 읽은 `DAG.json`은 **13/28**이다. 새 이론·코드 노드는 각각 `COMPLETE_SCOPED_INTERVAL_BLOCK_THEORY`, `COMPLETE_SCOPED_OUTWARD_INTERVAL_BLOCK_CERTIFICATE`로 채택되었다. S09 commit은 `7168ad4807dd1e02aef852bcf428df75b222f0de`, scientific payload SHA-256은 `796f399586916847844c7040082a1dce308035d1bce74bf805246574f98b94b4`이다. 선행 R5의 11/26에서 원 26개 객체를 그대로 계승하고 두 scoped 노드를 추가했다. 중앙 DAG 완료 증가량과 물리적 admission 증가량은 모두 0이다. 최종 S10 source HEAD는 이 S09 commit과 구별하여 실제 receipt에서 확정해야 한다.

## 1. 결과와 연구 기여

이번 단위는 두 가지 남은 수학 의무를 실제 코드와 연결했다. 첫째, R5의 17자리 근사 열확률을 원천 에너지의 decimal literal 및 정확한 SI 정의상수에서 출발하는 외측 구간으로 대체했다. 둘째, 순간 수축 계수가 0인 희소 생성자에도 적용할 수 있도록, 비음수 uniformization 부분합에서 유한 시간 블록의 수축을 인증하고 형성·파괴 강제항을 포함한 잔차와 총량 오차의 경계를 구현했다.

실제 저장된 실행 결과는 primary **76/76**, independent reference **109개 검사·불일치 0개**이다. Wolfram은 **23개의 영 잔차와 경고**를 함께 반환했다. Native 100 K 열확률의 최대 구간 폭은 약 **2.1536847338733093e-76**이다. 고정한 네 블록 중 가장 긴 블록에서는 수축 상계가 **rho = 0.008346121460629307**이다. 이 값들은 선언된 9상태 HD–para-H2 여기 그래프에 대한 결과이다. 실제 반응성 파괴율이나 physical consumer를 새로 확보했다는 뜻은 아니다. 근거 파일은 `raw/PRIMARY_RESULTS.json`, `raw/INDEPENDENT_RESULTS.json`, `raw/WOLFRAM_RESULT.json`이다.

기여의 범위는 표준 정규화 단조성, uniformization, Dobrushin 공통 질량 성질을 WU의 명시된 그래프·원천·비교계에 맞게 증명하고 구현한 것이다. 새로운 기본 정리의 발견이나 strong no-go를 주장하지 않는다. 일반 증명과 exact directed arithmetic이 주 근거이고, 독립 수치와 CAS는 서로 다른 수준의 보조 검증이다.

## 2. 최신 자료 조사와 source 선택

### 2.1 접근 가능한 조사 범위

`authority/survey/R6_SYNTHESIS_KO.md`의 실제 관측은 **51개 저장소, 2,354 refs, 65페이지**이며 51개 저장소 모두 목록 끝까지 열거했다. 공개 부분은 35개 저장소·1,871 refs이고, 비공개 부분은 식별자를 공개하지 않은 16개 저장소·483 refs의 집계이다. WU 최신 PR 8개와 관련 6개 owner의 최신 PR 5개씩, 총 38개 PR 본문을 확인했고 판단에 필요한 10개 파일을 commit과 blob에 고정해 읽었다. 이는 순차 관측이며 모든 branch의 모든 파일과 모든 과거 commit을 동시에 읽은 snapshot은 아니다.

다른 대화 원문은 이번 호출에서 접근할 수 없었다. PersonalContext가 unavailable을 반환했으며, 전달받은 프로젝트 대화 발췌는 사용자 제공 요약으로 구별했다. 이 제한을 과거 대화 전체 조사 완료로 바꾸어 표기하지 않는다.

WU의 선행 pin은 `35bb7f296abc8ff6c8b38c2c08cc14dd498d4c99`, PR150, `research/provider-registry-20261025`이다. 초기 목록 관측은 10:58–10:59 UTC였고, 12:37:04.540 UTC의 마지막 owner refresh에서 REI/BASS/CR의 변경 HEAD와 세 PR 및 10개 파일을 추가로 읽었다. 이 refresh의 `authority/final_owner_delta/FILE_MANIFEST.json`과 세 최신 HANDOFF 원문을 실제로 확인했다. 여섯 owner의 최종 관측 pin은 다음과 같으며, 전체 51개 목록을 그 후 다시 동시 snapshot으로 만들었다는 주장은 하지 않는다.

| owner | 관측 pin | WU에 전달되는 의미 |
|---|---|---|
| rec_bianchi | [d6dbe39a4923439547c01695d9020ba39367ea90](https://github.com/cosmosapjw-quantum/rec_bianchi/commit/d6dbe39a4923439547c01695d9020ba39367ea90), PR139 | 기존 HD54DB/24LTE·thermal/history 근거 재사용. 실제 H5 outgoing bound와 HD reactive destruction 입력은 없음 |
| rei_bianchi | [fbb55bcd0c77990b62470862a9f4a70647d0c5c9](https://github.com/cosmosapjw-quantum/rei_bianchi/commit/fbb55bcd0c77990b62470862a9f4a70647d0c5c9), PR240 | 새 affine-history 정리와 Fraction 코드·16 test methods를 작성. 새 tests/import/science는 NOT_RUN_BUDGET_HOLD이며 실제 recipient binding은 미완료 |
| bass | [6bf4a5d90b05f7e583be698854e521d259287837](https://github.com/cosmosapjw-quantum/bass/commit/6bf4a5d90b05f7e583be698854e521d259287837), PR203 | REC knots 5126–5127의 native atomic stocks와 finite Ly-alpha return을 복원·채택. fullphysicaltransaction=false이며 WU HD reactive 입력은 아님 |
| bass_cr | [8482ed83b14517b709ba6e801f6714cc333e720f](https://github.com/cosmosapjw-quantum/bass_cr/commit/8482ed83b14517b709ba6e801f6714cc333e720f), PR109 | 실제 PHYS02 electron 18 rows와 256 checks. actual nb/native25/RR/retained-photon은 null이고 WU 분자 consumer가 공급된 것은 아님 |
| BASS_HE | [ac6042a6b0610b09d0576538767ee0299389a5eb](https://github.com/cosmosapjw-quantum/BASS_HE/commit/ac6042a6b0610b09d0576538767ee0299389a5eb), PR102 | 원 게시 branch는 그대로. STATE04 후속은 BASS의 외부 closeout 사본에서 발견했으며 원 저장소·중앙 publication blocked 상태 |
| vigilode | [68a28357d960c4c2743c299770f0a33ef63245b2](https://github.com/cosmosapjw-quantum/vigilode/commit/68a28357d960c4c2743c299770f0a33ef63245b2) | 새 rigorous performance audit. 잔차 실패 2건과 안정적 wall speedup 미확립을 보존하며 WU 분자 물리 입력을 공급하지 않음 |

BASS_HE의 외부 STATE04 사본은 source identity `2addfab8c8975febd69d2c88eecc09afea508fbe`, delivery identity `30924d902187777fbff02687639c91d65cf53191`을 기록한다. 이 자료는 native HD–H+ 여기 한 edge와 명시된 reciprocity의 scoped 결과이며, global physical consumer admission은 false이다. 이번 조사에서는 그 owner receipt를 읽었고 그 원격 ZIP 전체를 다시 다운로드하여 검증한 것은 아니다. 자세한 read level과 상태는 위 조사 종합에 보존되어 있다.

마지막 refresh는 선행 판단을 그대로 반복한 것이 아니다. REI의 affine-history 결과는 새 수학·코드가 있으나 실행 보류라는 구분을 보존한다. BASS는 초기 S0에서 실제 native atomic-state 복원으로 진전했으며, 이미 확보한 endpoint stock을 다시 미입력으로 되돌리지 않는다. CR 최신 원문은 PHYS02 100 K와 기존 RR 10000 K의 **thermal-state mismatch**를 명시하며 gas-rest scalar frame 자체의 mismatch를 주장하지 않는다. 초기 관측의 포괄적인 frame mismatch 표현을 최종 물리 판정으로 유지하지 않는다. 이 세 변화 중 어느 것도 GL2022 파괴 수치 배열이나 실제 WU molecular consumer를 새로 제공하지 않았다.

직접 읽은 마지막 근거는 [REI affine-history HANDOFF](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/fbb55bcd0c77990b62470862a9f4a70647d0c5c9/research/rei_expanded_event_consumer/affine_history_enclosure_20261027/HANDOFF_KO.md), [BASS native-history HANDOFF](https://github.com/cosmosapjw-quantum/bass/blob/6bf4a5d90b05f7e583be698854e521d259287837/research/bass_b3h_native_history_inversion_20261027/HANDOFF_KO.md), [CR proper-injection HANDOFF](https://github.com/cosmosapjw-quantum/bass_cr/blob/8482ed83b14517b709ba6e801f6714cc333e720f/research/cr_proper_injection_20261027/HANDOFF_KO.md)이다.

### 2.2 GL2022와 이번 단위의 경계

GL2022 DOI [10.1063/5.0128598](https://doi.org/10.1063/5.0128598)에 대해 기존 실패 supplement URL을 반복하지 않고 새 [IFF-CSIC 기관 publication page](https://www.iff.csic.es/a-statistical-investigation-of-the-rate-constants-for-the-h-hd-reaction-at-temperatures-of-astrophysical-interest/)를 확인했다. 반환된 본문에서는 원 numerical state-to-state destruction array 또는 그 다운로드 manifest를 확보하지 못했다. 상태는 **INPUT_PENDING**이다. 이 관측이 데이터의 전 세계 부재를 입증하는 것은 아니다.

EMAA의 반응 2 여기, LAMDA의 회전 여기, 405 K라는 단일 에너지, 다른 source의 spin weight를 반응성 파괴 입력 대신 사용하지 않았다. 기존 REC54DB/24LTE와 R5 결과를 새 과학 실행으로 재계수하지 않았다.

## 3. 일반 정리와 적용 조건

### 3.1 유한 상태 모델과 단위

열벡터 convention을 사용한다. 상태별 개체 수밀도 x, 총량 X, 확률분포 pi에 대해

\[
x'=Kx-hDx+f,\quad D=\operatorname{diag}(d),\quad
X=\mathbf1^Tx,\quad r=x-\pi X,\quad Q=I-\pi\mathbf1^T.
\]

K는 Metzler이며 column sum이 0이다. 초기값 x0, h, d, prescribed formation f는 음이 아니다. pi는 simplex 값의 국소 절대연속 함수이고 나머지 계수는 국소 유계 가측, f는 국소 적분가능하다고 둔다. 물리적 cgs convention에서는 x가 cm^-3, K가 s^-1, h가 cm^-3, d가 cm^3 s^-1, f가 cm^-3 s^-1, t가 proper seconds이다. 실제 다른 단위계의 consumer를 붙일 때는 그 변환을 명시해야 한다.

\[
\bar d=d^T\pi,\quad
L=K+h(\pi d^T-D),\quad
c=K\pi-\dot\pi-h(D\pi-\pi\bar d)
\]

로 정의하면 R5에서 유도한 정확한 잔차 식은

\[
r'=Lr+cX+Qf,\qquad \mathbf1^Tr=\mathbf1^Tc=\mathbf1^TQf=0
\]

이다. 비정상 pi, 불완전한 상세균형 또는 moving thermal state에서는 Kpi나 piDot을 자동으로 0으로 두지 않는다. 이번 native 100 K source closure에서는 같은 literal Gibbs pair ratio로 역방향 전이를 구성했으므로 그 선언된 그래프에 대한 Kpi=0을 구조적으로 보장한다.

### 3.2 유한 블록 전파자 정리

Z를 합이 0인 벡터 공간이라 하자. Column Markov generator family A(t)에 대해 모든 관심 시간에서 유효한 entrywise off-diagonal 하한과 exit 상한을 주고, 양의 lambda를 exit 상한 이상으로 잡는다. 그러면

\[
P(t)=I+A(t)/\lambda\ge P_-\ge0
\]

인 공통 substochastic 하한을 만들 수 있다. H>0, N>=0와 정확한 지수함수 하한 e_-<=exp(-lambda H)로

\[
R_N(H)=e_-\sum_{m=0}^N\frac{(\lambda H)^m}{m!}P_-^m
\]

를 정의하면 모든 시작 시각 s에 대해 R_N(H)<=Phi_A(s+H,s)가 성분별로 성립한다. 저장된 dyadic 하한을 Rhat_N이라 할 때도 Rhat_N<=R_N이면 같은 결론을 쓴다.

n>=2에서

\[
\beta=\min_{j<k}\sum_i\min\{(\widehat R_N)_{ij},(\widehat R_N)_{ik}\},
\quad\rho=1-\beta
\]

라 두면

\[
\|\Phi_A(t,s)z\|_1\le
\rho^{\lfloor(t-s)/H\rfloor}\|z\|_1,\qquad z\in Z.
\]

여기에는 공통 계수 경계가 모든 해당 이동 창에 유효하다는 조건이 필요하다. 단일 시점의 계수 표본은 그 조건을 대신하지 않는다. n=1은 Z={0}인 별도 자명한 경우이다. beta=0은 선택한 certificate가 양의 수축을 보이지 못했다는 뜻이며 no-go 결론이 아니다.

### 3.3 Common killing과 강제항

v=hd라 쓰고 0<=kappa<=min_j v_j를 만족하는 상수 하한을 분리한다.

\[
A=K+\pi(v-\kappa\mathbf1)^T-\operatorname{diag}(v-\kappa\mathbf1).
\]

A는 Markov generator이고, Z에서 L=A-kappa I이다. 따라서

\[
\|\Phi_L(t,s)z\|_1\le
e^{-\kappa(t-s)}\rho^{\lfloor(t-s)/H\rfloor}\|z\|_1.
\]

rho는 **전체 A**의 경계에서 계산해야 한다. K 단독 rho를 추가 reset generator가 있는 L에 그대로 붙이지 않는다. 분리한 kappa를 같은 잔차 전파자에 다시 더하지 않는다. 현재 native source의 실제 계산에는 파괴 입력이 없으므로 A=K, kappa=0이다. 파괴를 포함한 세 fixture는 명시적으로 synthetic mathematical controls이다.

각 블록에서 ||cX+Qf||_1<=G_n을 보장하면 Duhamel 적분으로 해석적 비교 수열 V를

\[
V_{n+1}=\rho e^{-\kappa H}V_n+G_n\Psi_\kappa(H),
\quad\Psi_\kappa(H)=\int_0^H e^{-\kappa a}da
\]

로 정의할 수 있다. 반면 코드가 저장하는 보수적인 유리수 수열은 별도로

\[
\widehat U_{n+1}=\frac{\rho}{1+\kappa H}\widehat U_n+G_nH,
\qquad \widehat U_n^*=\widehat U_n+G_nH
\]

이다. 같은 초기값과 G_n에서 실제 endpoint 잔차<=V_n<=Uhat_n이다. Uhat_n의 상수 강제항 닫힌 식에는 자신의 계수 qhat=rho/(1+kappa H)를 사용해야 한다. 더 작은 V_n의 식으로 Uhat_n 자체를 상계한다고 해석하지 않는다. Uhat endpoint와 Uhat whole-block은 다른 시간 범위를 인증한다.

## 4. 증명과 구간 전파의 핵심

### 4.1 Literal 열확률

Native 에너지는 파수의 decimal literal로 읽는다. 정확한 SI 정의상수 h_P=6.62607015e-34 J s, c_light=299792458 m/s, k_B=1.380649e-23 J/K를 써서

\[
z_i=\frac{100h_Pc_{\rm light}(\widetilde\nu_i-\widetilde\nu_0)}{k_BT},
\qquad w_i=g_i e^{-z_i}
\]

를 구성한다. 100은 cm^-1에서 m^-1로의 변환이다. SI 정의값의 정확성은 [BIPM defining constants](https://www.bipm.org/en/measurement-units/si-defining-constants)에서 확인했다. 원천 decimal literal을 수학 입력으로 정확히 취급하는 것과 실제 spectroscopy의 불확실성이 0이라는 주장은 구분한다. 물리적 원천 불확실성·공분산은 주어지지 않았다.

지수함수는 y=z/2^s<=1/2로 줄인 뒤 교대 Taylor odd/even 부분합을 정확한 유리수로 계산한다. 하한은 아래로, 상한은 위로 반올림하며 반복 제곱한다. 최종 endpoint 자체가 enclosure이고 초기 Taylor threshold를 최종 오차로 재사용하지 않는다.

0<l_i<=w_i<=u_i이면 좌표별 단조성으로

\[
\frac{l_i}{l_i+\sum_{j\ne i}u_j}
\le\pi_i\le
\frac{u_i}{u_i+\sum_{j\ne i}l_j}.
\]

pi는 여전히 simplex에 속한다. 좌표별 상·하한이 동시에 달성된다고 가정하지 않는다. 이 기본 성질은 [Wei et al. 2023, section 2.1](https://proceedings.mlr.press/v206/wei23c/wei23c.pdf)의 constant softmax bounds와 같은 원리다. 상향률에는 normalized box끼리의 나눗셈 대신 (g_u/g_l) exp[-(E_u-E_l)/(k_BT)]의 직접 구간을 사용한다.

### 4.2 시간순 uniformization과 비음수 부분합

유한 차원에서 integrating factor와 Peano–Baker 급수는 전파자를 시간순 P(t_m)...P(t_1)의 적분 합으로 표현한다. 공통 P_- 하한과 비음수 곱의 단조성 때문에 각 곱이 P_-^m 이상이다. 적분 simplex의 부피는 H^m/m!이고 생략한 급수 꼬리는 비음수이다. 따라서 lower bound를 위해 꼬리의 상한을 구할 필요가 없다. [van Dijk 1991의 primary VU 원문](https://research.vu.nl/ws/portalfiles/portal/73611171/Scanjob%20199100006)은 시간가변 uniformization의 선행 근거이며, 본 유한 차원 가측 계수 버전은 일반 증명에서 직접 유도한다.

생산 코어는 S=2^p에서 P_-를 아래로 반올림한 Ptilde, M_0=I, M_{m+1}=floor_S(M_m Ptilde), w_0=floor_S(e_-), w_{m+1}=floor_S(w_m mu/(m+1))를 사용한다. 마지막으로 sum_m floor_S(w_m M_m)을 저장한다. 비음수 성분의 곱과 합만 쓰므로 각 단계가 실제 항 아래에 남는다. 작은 양의 항이 0으로 내려가더라도 certificate가 덜 강해질 뿐 하한 방향은 유지된다.

확률행렬의 column-pair 공통 질량이 beta 이상이면 zero-sum induced l1 norm이 1-beta 이하라는 Dobrushin 성질을 쓴다. [Gaubert–Qu의 저자 PDF](https://www.cmap.polytechnique.fr/~gaubert/PAPERS/GaubertQuIEOTD14QuFinal.pdf)는 이 표준 성질의 primary 근거이며 row convention을 transpose하여 적용했다. 블록보다 짧은 나머지에는 nonexpansiveness만 사용한다. rho<1을 즉시 prefactor 1의 순간 지수율로 바꾸지 않는 이유가 여기에 있다.

### 4.3 총량과 coarse discrepancy

전체계와 coarse equation에는 같은 prescribed F(t)=1^T f(t)를 사용해야 한다. 한 블록 전체에서 비음수 k,b와 상한 q_c,g,F_+,s_+가

\[
k\le h\min d,\quad b\le h\bar d,\quad
\|c\|_1\le q_c,\quad \|Qf\|_1\le g,\quad
F\le F_+,\ h\operatorname{osc}(d)/2\le s_+
\]

를 만족하고 초기 M,Uhat,E가 각각 X,||r||_1,|X-Xbar|를 덮는다고 하자. 그러면

\[
M_n^*=M_n+F_+H,\quad G_n=q_cM_n^*+g,\quad
M_{n+1}=M_n/(1+kH)+F_+H
\]

와 앞의 Uhat 수열을 사용할 수 있다. Whole-block 잔차 적분을 H Uhat_n + G_n H^2/2로 상계하면

\[
E_{n+1}=\frac{E_n}{1+bH}
+s_+(H\widehat U_n+G_nH^2/2),\qquad
E_n^*=E_n+s_+(H\widehat U_n+G_nH^2/2)
\]

를 얻는다. 오른쪽 endpoint의 작은 Uhat_{n+1}로 전체 블록의 적분을 대체하지 않는다. f가 실제 상태에 의존하거나 coarse source가 다른 경우에는 추가 coupling/source-difference 경계가 필요하다.

## 5. 구현과 원시 실행

실행 가능한 주 모듈은 `src/interval_block.py`이다. `native_hd_source`, `thermal_from_levels`, `pair_ratio`, `GeneratorBox`, `uniformization_lower`, `finite_block`, `reset_generator_bounds`, `forced_step`이 원천에서 비교계까지의 경로를 제공한다. 생산 경로는 고정된 REC parser의 원문 decimal literal을 사용하며, 그 parser의 binary64 upward-rate 계산을 호출하지 않는다. 일반 정리와 코드 correspondence는 `theory/INTERVAL_BLOCK_PROOF_KO.md`에 정리되어 있다.

`verification/PRIMARY_INPUT.json`은 native 100 K, collider 2, J=0..8, v=UNSPECIFIED, 9 downward rows와 mu=[8,32,128,256], N=[64,128,320,512]를 사전에 고정한다. Thermal bits=256, polynomial bits=512이다. Native rate coefficient를 1e-11 cm^3/s로 나누어 무차원 생성자를 만들며, 누락 채널은 MISSING_NOT_ZERO로 유지한다.

Primary는 `verification/run_primary.py`, 별도 reference는 `verification/reference_r6.py`이다. Reference는 생산 코어를 import하지 않고 원천 파일을 독립 파싱하며 Decimal 250자리 지수함수와 SciPy expm/expm_multiply를 사용한다. Primary의 exact rational certificate, reference의 Decimal 수치 비교, SciPy tolerance를 섞어 하나의 엄밀성 주장으로 합치지 않는다.

| 실행 | 실제 결과 | 실행 구간 CPU | 전체 process CPU | 내부 wall |
|---|---|---:|---:|---:|
| Primary 1회 | 76/76, failure 0 | 0.659824898 s | 0.791299421 s | 0.662826006 s |
| Reference 1회 | 109 checks, mismatch 0 | 0.689574078 s | 0.822867308 s | 0.763363920 s |
| Wolfram 1회 | 23 zero residuals, warnings 보존 | kernel 0.286018 s | 원격 전체 process 값 미제공 | kernel 0.28199 s |

Primary와 reference의 CPU 상한은 각각 60초, Wolfram의 time limit은 30초였다. 새 finite allowance의 primary/reference/Wolfram 잔여는 모두 0이다. 옛 PHYS91 잔여 0/0/0, global 잔여 null, 옛 과학 재실행 0, physical IVP 0, new Q 0을 유지한다. 서로 다른 프로세스 및 원격 kernel의 측정 범위를 혼합해 미측정 전체 CPU를 발명하지 않는다.

## 6. 실제 수치와 해석

### 6.1 열확률과 native finite blocks

`raw/PRIMARY_RESULTS.json`의 source case `strict_thermal_precision_width`가 저장한 최대 pi 구간 폭은 약 2.1536847338733093e-76이다. 이 수치는 원천 literal의 mathematical enclosure 폭이며 spectroscopy의 측정 불확실성은 아니다.

| mu | N | H, 무차원 tau (표시값) | beta 하한, 아래 반올림 | rho 상한, 위 반올림 |
|---:|---:|---:|---:|---:|
| 8 | 64 | 0.949043310202281 | 0.000642505600817 | 0.999357494399183 |
| 32 | 128 | 3.79617324080912 | 0.076003940433656 | 0.923996059566344 |
| 128 | 320 | 15.1846929632365 | 0.834704269037226 | 0.165295730962774 |
| 256 | 512 | 30.369385926473 | 0.991653878539370 | 0.008346121460630 |

물리 시간과의 관계는 tau=n_coll*(1e-11 cm^3/s)*t이다. n_coll이 미입력이므로 위 H는 seconds가 아니다. 네 개 선택 블록 밖의 최적성을 주장하지 않는다.

마지막 블록의 독립 SciPy Dobrushin 계수는 0.008346121460628762였다. Source R_lower와 전파자의 성분별 비교에서 최소 표시 slack은 -2.7755575615628914e-15였고, 명시된 tolerance 2.2e-11 안이었다. 이는 binary64 corroboration의 수치 오차 수준이며 exact outward proof의 대체물이 아니다. 별도 Fraction 경로가 pair overlap, dyadic 성분, column-substochastic 조건을 확인했다.

35개 Decimal 구간 비교 중 34개는 strict interior로 판별되었다. 나머지 하나는 ground-state z=0에서 reference=lower=upper=1인 정확한 [1,1] 구간이다. 원시 generic classifier는 strict margin=0 때문에 `NUMERICALLY_COMPATIBLE_BUT_NOT_RESOLVED_AT_250_DPS`라고 표시했다. 실제 내용은 exp(0)=1의 정확한 경계 일치이다. 이를 정밀도 부족으로 해석하지 않으며 원시 코드·결과를 수정하거나 재실행하지 않았다.

### 6.2 강제항·비가환·switched controls

세 강제 fixture는 각각 8블록, 33개 시간 표본을 사용했다. Endpoint M/U/E와 whole-block의 양 끝 및 내부 1/4,1/2,3/4 지점에서 허용오차 초과가 없었다. Zero-killing 및 uniform-killing 2상태의 H는 1/4이고, state-dependent killing의 비가환 3상태 H는 1/2이다.

비가환 fixture의 K와 reset generator commutator 1-norm은 약 0.6133333333333331이었다. 전체 A에 대한 common-killing 전파자 분리의 표시 오차는 4.440892098500626e-16이었다. 실제 형성항 총합 F와 F_upper 조건도 확인했다. 이러한 수학 fixture를 원천에서 회수한 물리적 d,h,f로 표기하지 않는다.

두 조각 3상태 switched control 한 개에서는 각 1/4 길이의 전파자를 실제 시간순으로 곱했다. 공통 P_lower는 rational 생성자 모두를 감쌌고, 하한 행렬과 시간순 전파자 사이의 최소 성분별 여유는 0.038973345032464315였다. 별도 두 상태 닫힌 형식 해와 세 clock scaling을 이용한 6개 analytic controls도 일치했다. 연속 시간 전체의 보장은 표본의 개수가 아니라 앞의 일반 증명에 의존한다.

### 6.3 Wolfram 결과와 경고

`raw/WOLFRAM_RESULT.json`은 column sums, common killing, positive path power, analytic chain propagator, block error integral, zero-killing limit, constant-forcing recurrence에 대해 합계 23개의 영 잔차를 기록한다. 함께 반환된 경고는 다음과 같다.

```text
Symbol::undefined2: Warning: Global symbols "L, A, P, S, R2, P, P, P, R2, R2, A, L, A, P, P, S, S, HH, HH, HH, HH, HH" are undefined.
Power::infy: -- Message text not found -- (1/0)
Infinity::indet: -- Message text not found -- (0*Infinity)
Infinity::indet: -- Message text not found -- (0*Infinity)
General::messages: Messages were generated which may indicate errors.
```

경고 없는 실행이라고 주장하지 않는다. 경고의 정확한 원인을 이 보고서에서 추측하여 확정하지 않는다. 원시 응답과 경고를 보존했고 CAS 재실행은 0회다. 반환된 영 잔차는 보조 근거로 취급하며 일반 증명, exact arithmetic, 독립 numerical reference를 별도로 판단한다.

## 7. 물리적 연결에 필요한 실제 다음 입력

현재 결과는 density와 reactive input을 실제로 받았을 때 잔차와 coarse total discrepancy를 감쌀 수 있는 조건부 계산 도구다. 다음 단위는 다음 두 갈래 중 실제로 달라진 입력이 생긴 쪽을 우선한다.

**A. Native reactive payload.** GL2022의 원 state-to-state 수치 배열과 immutable bytes/hash, 초기 HD(v,j) 및 최종 H2(v',j')의 charge/isotope/channel identity, temperature 또는 collision-energy grid, 단위·threshold·support·interpolation convention, 원 nuclear-spin normalization 및 source symmetrization을 확보한다. 불확실성이 없으면 없다고 쓰는 대신 미제공 또는 unknown으로 기록한다. 실제 원천 에너지가 필요할 경우 source-matched state energies와 recoil/energy bookkeeping까지 별도로 결합한다.

**B. Named physical consumer.** 실제 owner/repo/commit, 입력 파일과 호출 함수를 고정하고 x0, pi(t), piDot 또는 검증된 경계, Kpi의 비정상 잔차, 모든 collider의 identity/density/ortho–para weighting, state-dependent d_j와 h(t), prescribed f(t), 같은 total F를 쓰는 coarse equation을 제공한다. 각 block 전체의 coefficient bounds와 physical clock/단위 변환을 함께 제공해야 한다. 지금의 source K-only certificate는 전체 A가 달라진 consumer의 rho를 자동으로 대신하지 않는다.

현재 실제 density, h, destruction d, formation f, physical x0, moving pi/piDot와 named consumer는 미입력이다. 고정 synthetic fixture의 값으로 이 칸을 채우지 않는다. 그래프에 없는 전이·상태, source 밖 온도, 다른 spin convention을 추가한다면 그 실제 changed-input 범위의 generator/closure와 error bound를 새로 정당화해야 한다.

입력이 붙으면 기존 R6 구현과 저장된 증명을 재사용하여 영향받는 bound 및 adapter만 작성한다. 보관된 archive 전체의 반복 재검증, 옛 76/109 또는 REC54DB/24LTE의 자동 재실행을 선행 작업으로 삼지 않는다. 식별 불일치나 실제 손상 증거가 있을 때만 해당 artifact의 integrity 복구를 좁혀 수행한다. 다른 수학 질문을 여는 일은 현재 physical pending packet을 자동 대체하거나 완료시키지 않는다. 별도의 변경 의무·수용 기준·유한 allowance가 필요하다.

## 8. 단계별 게시와 원본 백업

R_i/C_i를같은순번체크포인트로묶었다. 각루프는10단계이며연구DAG와별도다. 아래의완료는실제Gitref확인및Dropbox/Drive원본GET의전체SHA256·CRC·파일검증에묶인다.

| 단계 | 연구 DAG | 실제 source commit | 양쪽 원본 검증 |
|---|---:|---|---|
| R1/C1 | 11/28 | [95b836cb31d3](https://github.com/cosmosapjw-quantum/WU088_HH/commit/95b836cb31d3edeb4032e7c3ee5d2418c4f6b697) | PASS |
| R2/C2 | 11/28 | [9980d4c2b1d4](https://github.com/cosmosapjw-quantum/WU088_HH/commit/9980d4c2b1d46e6c6d60c77e5bdbc1d3a0cf6aa2) | PASS |
| R3/C3 | 11/28 | [b81c668abd90](https://github.com/cosmosapjw-quantum/WU088_HH/commit/b81c668abd903faecaf913213937c378970f3458) | PASS |
| R4/C4 | 11/28 | [05e557ee7bbb](https://github.com/cosmosapjw-quantum/WU088_HH/commit/05e557ee7bbbe125a495a669e9c64ac916d6ceed) | PASS |
| R5/C5 | 11/28 | [95c642795697](https://github.com/cosmosapjw-quantum/WU088_HH/commit/95c64279569725b429210dd47f2b0b84048f48c1) | PASS |
| R6/C6 | 11/28 | [b71a3c0a05ef](https://github.com/cosmosapjw-quantum/WU088_HH/commit/b71a3c0a05ef46351d83d092cf19742d18a07c68) | PASS |
| R7/C7 | 11/28 | [8582df66ea3d](https://github.com/cosmosapjw-quantum/WU088_HH/commit/8582df66ea3d6d7abee9fead272d2d8bea93bb8d) | PASS |
| R8/C8 | 12/28 | [3aef8b9efb85](https://github.com/cosmosapjw-quantum/WU088_HH/commit/3aef8b9efb85a19a3d0ea3e86f374069a2599f29) | PASS |
| R9/C9 | 13/28 | [7168ad4807dd](https://github.com/cosmosapjw-quantum/WU088_HH/commit/7168ad4807dd1e02aef852bcf428df75b222f0de) | PASS |
| R10/C10 | 13/28 | source publication pending | pending actual receipt |

선행R4S10및R5S01–S10도원래sourcecommit으로복구하여 **11/11ZIP,22/22원본사본** 검증을완료했다. 실제복구ZIP합계는27,866,026bytes,양쪽수신은55,732,052bytes이다. `delivery/LEGACY_RECOVERY_CLOSURE.json`이원본commit/tree·hash·providerID·개별영수증을결속한다. R4의R10/C10전달의무와R5의10단계ZIP전달대기를이기록으로닫으며,고정된과거commit과그당시pending기록은그대로보존한다. 과학재실행은0이다.

최종source는 `PENDING_S10_ACTUAL_PUBLICATION`이며그ZIP SHA256은 `PENDING_S10_ACTUAL_ARCHIVE`이다. 실제metadataHEAD는이source뒤의branchHEAD이며 `delivery/PUBLICATION_INDEX.json`과최종전달영수증에서구별한다. 보관범위는AGENTS와8개provider/program/ledger연구디렉터리이며전체역사저장소의clone이라고주장하지않는다.

현재scientificpayload SHA256은`796f399586916847844c7040082a1dce308035d1bce74bf805246574f98b94b4`이고,17개고정파일의metadata검증과상속26개DAG객체불변검사를통과했다. 이무결성확인은새수치실행이아니다. main merge=false,HH_R10=OFF,production=NOT_ISSUED,L4_ready=false,중앙·물리완료delta0을유지한다.

## 9. 재개

완성된복사문은[HANDOFF_KO.md](HANDOFF_KO.md)에있다. 다음실제입력과최소변경의무는[followup/NEXT_INPUT_CONTRACT.json](followup/NEXT_INPUT_CONTRACT.json)을따른다. 기존성과와원본backups를기본적으로재사용하며,실제identity불일치나새입력이있는부분만검토한다.
