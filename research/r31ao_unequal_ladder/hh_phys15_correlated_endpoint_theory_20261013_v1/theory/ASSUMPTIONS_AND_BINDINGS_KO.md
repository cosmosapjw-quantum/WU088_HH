# PHYS15 — 동일 COMMON endpoint 비교의 전제와 정확한 source 연결

## 결론

PHYS14의 실제 two-half endpoint와 기존 Full을 같은 계수 선택에 결박할 자료가 있다. 양쪽은 같은 COMMON Jet payload에서 시작하고, Full과 둘째 half는 같은 종료 시각의 기체 source 함수를 쓴다. 총 광자 생성량은 정확히 같다. 시간 분할의 차이는 중간 기체 진화, 광자 수송·흡수, 첫 주입 광자의 경과 시간, 첫 stage와 끝 stage의 source 계수 차이로 구성할 수 있다.

현재 Git PR49는 `open`, `merged=false`이며 head는 `087a16f28d0ee4fc7ae74ae50bfcafe578716e85`다. 실제 읽은 AGENTS, CURRENT_DEVELOPMENT_PLAN, IMPLEMENTATION_PLAN은 동일 COMMON의 상관된 endpoint 결함을 다음 과제로 지정한다. 정확한 원격 식별자와 기존 overlay의 동일성은 `GIT_HEAD_AND_ROOT_READ.json`에 있다.

## 1. 재사용할 전제와 데이터

이 비교의 계수 선택은 \(\alpha=(g_0,N_0,\mathrm{guard}_0,\text{고정 source leaves},\rho,\{w_r\})\)로 공동 정의한다. \(\lambda,b\in[0,1]\)를 두 half와 Full에 동일하게 적용한다. \(\alpha\)는 rectangle 전체에서 고정한다. 과거 HH ON과 primal compensation은 동일 COMMON에 포함된다.

PHYS09·11·13의 고정 source 계열, 원 \(X\)의 \(C^2\)·근 포함, PHYS14의 새 두 번째 근·carry 포함을 재사용한다. Geometric isotropic 선택은 \(\rho=e^{-Hh}\), Full에서는 \(\rho^2\)이며, 실제 normalized angular weight의 합은 1이다. 이 연결된 선택의 원 ray interval 포함은 PHYS14의 독립 `GEOMETRY_REVIEW.json`에 이미 검토되어 있다.

| 결박 대상 | 실제 확인 |
|---|---|
| COMMON | 두 `COMMON_INPUT_SCOPE.json` 전체가 같다. Full·half input binary는 5-word header의 dt를 제외한 payload가 byte-identical이다. |
| 시간 | \(t_0=1.6\times10^{11}\) s, \(h=625000000\) s, \(t_1=160625000000\) s, \(t_2=161250000000\) s. |
| 원 영역 | 두 stage의 \(X\), gas centre \((0.915,0.3,0.6,13.5)\), radius \((0.015,0.01,0.01,0.5)\)가 같다. |
| 끝 stage | PHYS14 둘째 half의 \(n_H,n_{He}^{stored},f,H\), energy/sigma/heat, \(k_B\), eV leaves는 기존 Full의 값이다. |
| source | Full의 `nonphoto`와 \(q\)의 값·gradient·Hessian을 둘째 half가 그대로 사용한다. 새 half에서는 \(d=h\), 새 photon incoming을 쓴다. |
| 격자 | 원 33개 node 유지. HI 활성 node는 16–32, HeI/HeII photo sigma는 모든 node에서 정확히 0이다. Birth는 node 24에 들어간다. |
| thermal 좌표 | \(w\)는 eV/H, 광자는 photons/H. readout은 \(\widehat f=\operatorname{exact}(n_{He}^{stored})/\operatorname{exact}(n_H)\)를 사용한다. |

기존 근 포함의 유효성은 상속된 과학 전제다. 이번 파일 조사에서는 이를 변경하거나 과거 source·근·history 실행을 반복하지 않았다. `BINDINGS.json`은 실제 사용한 33개 파일의 크기·SHA256, exact bits, 원 영역과 근 hull을 기록한다.

## 2. 총 birth 양과 시간 순서를 분리하는 정확한 식

원 `fl_dt_SOURCE_bits`는 half에서 `3eca36e2eb1c432d`, Full에서 `3eda36e2eb1c432d`다. 따라서

\[
M_h=\frac{7378697629483821}{2361183241434822606848},\qquad
M_F=2M_h
\]

가 정확히 성립한다. 총 생성량 capture의 차이는 0이다. 첫 half에 생성된 광자는 둘째 half 전에 흡수와 추가 수송을 거친다.

\(R=R(\rho)\), \(R_F=R(\rho^2)\), \(e_B=e_{24}\),
\(A_1=\operatorname{diag}[1+h c n_1\sigma_j(1-x_1)]^{-1}\)라 두면

\[
N_1^-=RN_0+bM_h e_B,\qquad
N_2^-=R A_1N_1^-+bM_h e_B,\qquad
N_F^-=R_FN_0+2bM_he_B.
\]

같은 \(N_0,b,M_h\)를 먼저 묶으면

\[
N_2^--N_F^-=(R^2-R_F)N_0
+R(A_1-I)(RN_0+bM_he_B)+bM_h(R-I)e_B.
\]

이는 기존 remap 차이, 중간 흡수, 첫 birth의 추가 redshift를 각각 남긴다. 실제 interval 계산에서는 동일 \(N_0\)와 \(A_1(x_1)\)를 보존한다. 원 fixed-node 수송은 하단 guard를 포함해 다룬다.

## 3. 첫 stage와 끝 stage 사이의 source-normalization bridge

여기서는 \(f_i=\widehat f_i\), \(i=1,2\)이며, 2는 Full과 둘째 half의 공통 source stage다. 편의를 위해 기체 분율을 \((x,y,z)=(x_{HII},y_{HeII},y_{HeIII})\)로 쓴다.

\[
e_i=x+f_i(y+2z),\qquad
\Pi_i=1+f_i+e_i,\qquad T_i=C_Tw/\Pi_i.
\]

실제 leaf에서

\[
n_1\simeq9.951928415493808\times10^{-5},\quad
n_2\simeq9.951741818585369\times10^{-5}\quad[\mathrm{cm}^{-3}],
\]
\[
f_1-f_2\in[-6.94524945677013820,-6.94524945677013819]\times10^{-18}.
\]

이 미소 차이는 scalar \(n_H f_{stage}\)를 저장한 뒤 나눈 원 coefficient graph에서 생긴다. 정확한 비교에서는 두 ratio를 유지한다.

### 3.1 원 FT03 graph의 인수 분해

\(\beta_a(T)\)는 collisional-ionization coefficient, \(\alpha_a(T)\)는 radiative recombination coefficient, \(s_a=d\log\alpha_a/d\log T\)를 뜻한다. 이들은 원 `ft03_interval.rs`의 고정 fit 함수다. HeI dielectronic term은

\[
d_{DR}(T)=\sum_{r=1}^2 d_r(T),\qquad
d_r(T)=c_r A_{DR}T^{-3/2}e^{-B_r/T},\quad(c_1,c_2)=(1,0.3).
\]

\[
\begin{aligned}
k_x&=(1-x)\beta_H-x\alpha_H,\\
k_y&=(1-y-z)\beta_I-y(\alpha_I+d_{DR})-y\beta_{II}+z\alpha_{II},\\
k_z&=y\beta_{II}-z\alpha_{II}.
\end{aligned}
\]

Photo-off 원 source에서 모든 collisional·RR·DR 항은 반응 전 population과 electron density의 곱으로 구성된다. H당 정상화와 He 분율 정상화를 적용하면

\[
\boxed{F^{np}_{\rm frac}(n,f,g)=n e\,(k_x,k_y,k_z)(x,y,z,T).}
\]

\(\epsilon_{\rm eV}\)를 captured eV-to-erg leaf, \(\chi_a\)를 FT03 controlled model의 captured threshold leaf라 두고
\(\kappa_a(T)=k_BT\alpha_a(T)(3/2+s_a(T))/\epsilon_{\rm eV}\)라 쓰면,

\[
k_{wH}=-\chi_H(1-x)\beta_H-x\kappa_H,
\]
\[
\begin{aligned}
k_{wHe}={}&-\chi_I(1-y-z)\beta_I-\chi_{II}y\beta_{II}
-y\kappa_I-z\kappa_{II}\\
&-y\sum_{r=1}^2d_r(T)\frac{k_B B_r}{\epsilon_{\rm eV}}.
\end{aligned}
\]

따라서

\[
\boxed{F^{np}_w(n,f,g)=n e\,[k_{wH}(x,T)+f k_{wHe}(y,z,T)].}
\]

위 `nonphoto`는 export가 HH·photo·팽창 항을 넣기 직전에 저장한 네 성분이다. \(-2Hw\)는 다음 결합 단계에서 따로 더한다. 이 분해는 원 graph의 반응 항을 인수 분해한 결과이므로 fit·source를 새로 평가할 필요가 없다.

### 3.2 온도를 맞춘 가스 pullback

\[
g_*=(x,y,z,w\Pi_2/\Pi_1),\qquad
r_e=\frac{n_1e_1}{n_2e_2}.
\]

같은 분율에서 \(T_2(g_*)=T_1(g)\)이므로

\[
\boxed{F^{np}_{1,\rm frac}(g)=r_eF^{np}_{2,\rm frac}(g_*),}
\]
\[
\boxed{F^{np}_{1,w}(g)=r_eF^{np}_{2,w}(g_*)
+n_1e_1(f_1-f_2)k_{wHe}(y,z,T_1).}
\]

원 HH source의 \(q=n(1-x)^2k_{HH}(T)\)에서 또한

\[
\boxed{q_1(g)=\frac{n_1}{n_2}q_2(g_*).}
\]

따라서 첫 source와 끝 source의 차이는 밀도·electron factor, 미소 thermal-coordinate 이동, 명시적 He thermal 보정으로 전달된다. \(f_1=f_2\)를 가정할 때의 단순 밀도 scaling도 이 식의 정확한 특수 경우다.

### 3.3 원 source domain에서의 사용 조건

\[
w_*-w=w\frac{(f_2-f_1)(1+y+2z)}{\Pi_1}>0.
\]

기존 Full·first-half·second-half root image의 공동 convex hull에서 이 이동의 외향 포함은

\[
w_*-w\in[1.09800931589085210,1.11069895932571596]\times10^{-16}
\quad[\mathrm{eV/H}].
\]

실제 exact endpoint로 확인한 hull과 그 pullback은 원 \(X\) 내부에 있으며, \(g\)에서 \(g_*\)로 가는 segment도 \(X\) 안이다. 전체 닫힌 \(X\)의 경계까지 pullback을 확장하려면 \(w\Pi_2/\Pi_1\le X_w^+\) 조건을 별도로 적용한다. 현재 사용점은 엄격한 내부 root hull이므로 기존 source gradient·Hessian 포함을 그대로 재사용한다.

## 4. endpoint source와 관측량에서 보존할 상관관계

Full과 둘째 half의 공통 nonphoto·HH·팽창 함수를 \(B_2(g,\lambda)\)라 두면, 같은 \(\lambda\)에서

\[
B_2(g_2,\lambda)-B_2(g_F,\lambda)
=\left[\int_0^1 D_gB_2(g_F+s(g_2-g_F),\lambda)\,ds\right](g_2-g_F).
\]

원 source interval 두 개를 각각 빼기 전에 이 동일 함수를 묶는다. 첫 stage의 시간 차이는 위 bridge 또는 같은 centre에서의 source 차이를 기준으로 유지한다. Full photo denominator는 \(1+2ha_{2j}(1-x_F)\), 둘째 half는 \(1+ha_{2j}(1-x_2)\), 첫 half는 \(1+ha_{1j}(1-x_1)\)이며 \(a_{ij}=c n_i\sigma_j\)다.

끝점 두 개는 같은 \(f_2,C_T,n_2\)를 쓰므로 \(\delta g=g_2-g_F\)에서

\[
\delta e=\delta x+f_2(\delta y+2\delta z),\qquad
\delta n_e=n_2\delta e,
\]
\[
\boxed{\delta T=C_T\frac{\Pi_F\delta w-w_F\delta e}{\Pi_F\Pi_2}.}
\]

이 식을 사용하면 두 온도 구간을 독립적으로 빼면서 생기는 COMMON 상관 손실을 줄일 수 있다.

## 5. 실제 자료 보충과 남은 연구

다음 두 파일을 SHA256 `4ea6b7dbbc714493ac85f944a65a353a1ee75abf5742c3e7ce65a7df56cc3465`의 원 NCP07 ZIP에서 직접 읽었다. 각 member의 크기·SHA256를 원 MANIFEST 및 기존 회수본과 대조한 뒤 `extra_inputs/`에 create-only로 복사했다.

| 파일 | bytes | SHA256 |
|---|---:|---|
| `results/first_half/SOURCE_CENTRE.json` | 57,834 | `fe63465b6a457cb9dd6c88f37a7161ce75d7761b7296608ec8eb3bde8bb629a9` |
| `candidate/src/hh_primary_extension.rs` | 26,293 | `f47d910abb096f96b829e3392fdfbf55d079ba2fbb09a45416c97c76a4f4a647` |

현재 이론 비교에 필요한 입력 결손은 없다. 남은 계산은 공동 \(\alpha\)에 대한 gas·photon 결함을 조립하고, 원 convex hull의 source·Jacobian 포함으로 \(T,e,w\)에 전달하는 일이다. source-time bridge와 endpoint defect의 새 명제는 별도 독립 검토에서 판정한다.

이번 담당 작업의 새 source/native 호출, 근·history 재실행, cloud write는 모두 0회다. `inspect_bindings.py`는 targeted file identity, 정확한 유리수 leaf·영역 계산과 두 archive member 복사만 수행했다. 새로운 물리 경로를 수치 실행한 횟수로 세지 않는다.
