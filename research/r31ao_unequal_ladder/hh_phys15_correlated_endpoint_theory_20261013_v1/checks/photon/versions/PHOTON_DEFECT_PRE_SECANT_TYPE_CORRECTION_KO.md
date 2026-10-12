# WU088_HH PHYS15: 공통 입력을 보존하는 광자 결함과 기체 잔차

2026-10-12. 이론 분과 산출물. 근거 상태는 **derived + exact-arithmetic checked**이다. 적용 계열은 PHYS14의 geometric isotropic, source-aligned 계열이다. 이번 구성은 같은 COMMON의 실제 two-half와 Full 사이 광자 결함을 기체 잔차에 직접 연결한다.

## 1. 재사용 근거와 새 결과

PHYS14에서 같은 COMMON, 과거 HH ON 이력과 primal compensation, 두 half에 공통인 \((\lambda,b)\in[0,1]^2\), 정확한 39-state aggregate closure, 원 33개 energy nodes와 guards, 첫 half와 실제 둘째 half의 gas root 및 source 포함을 재사용한다. \(h=6.25\times10^8\,\mathrm s\)이고 둘째 half와 기존 Full의 종료 시각은 같다. HI 활성 group은 16–32이며 모든 HeI/HeII photo cross section은 exact zero다.

새 결과는 다음과 같다.

- 원 COMMON과 birth를 식에서 공유하는 outgoing 및 integrated absorption 결함의 정확한 분해.
- 중간 흡수·수송 순서의 비음수 absorption sector, stock과 birth 사이의 absorption 시점 판별식.
- 원 birth-redshift sector의 **이온화 absorption 증가, thermal deposition 감소**에 대한 조건부 부호 정리와 실제 captured leaf 조건 확인.
- photon number/energy 수지와 captured heat identity를 이용한 H 화학·열에너지 residual 사영.
- Full residual에서 실제 endpoint photon 차이로 이동하는 정확한 opacity secant.

재사용 원문은 PHYS14의 **theory/THEORY_CANDIDATE_KO.md** §§1–4,7과 **src/phys14_advance.py**의 transport, Source.evaluate, outgoing_carry, remap_defect다. Source capture graph는 **inputs/ncp07/candidate/src/phys04_mixed.rs**의 phys04_reduced_residual, leaf export는 **inputs/ncp07/src/sourcebox.rs**에서 읽었다. 원자료 identity는 PHOTON_EXACT_CHECKS.json과 SOURCE_READ_SCOPE.json에 기록한다.

## 2. photon·guard 공간과 비교점

광자 상태를
\[
z=(N_0,\ldots,N_{32},G_N,G_U)^{\mathsf T}\in\mathbb R^{35}
\tag{1}
\]
로 쓴다. \(N_j,G_N\)의 단위는 photons/H, \(G_U\)는 eV/H다. \(R=R(\rho)\)는 원 hat remap과 guard map을 함께 포함하고,
\[
\rho=\exp[-\operatorname{exact}(H)\operatorname{exact}(h)],\qquad
R_F=R(\rho^2)
\tag{2}
\]
로 결박한다.

각 시각의 source opacity는
\[
a_{k,j}=\operatorname{exact}(c)\operatorname{exact}(n_{H,k})
\operatorname{exact}(\sigma_j),\qquad
\kappa_{k,j}(x)=a_{k,j}(1-x)
\tag{3}
\]
이며 단위는 \(\mathrm{s}^{-1}\)이다. 두 captured density \(n_{H,1},n_{H,2}\)를 유지한다. 대각 survival 연산자를
\[
A_k(g)=\operatorname{diag}\big[(1+h\kappa_{k,j}(x))^{-1}\big],
\quad B_k=I-A_k
\tag{4}
\]
로 정의한다. 두 guard에서는 \(A_k=1,B_k=0\)이다. Full 길이에서는
\[
A_F(g)=\operatorname{diag}\big[(1+2h\kappa_{2,j}(x))^{-1}\big],
\quad B_F(g)=I-A_F(g).
\tag{5}
\]
분모는 source-aligned exact-real residual graph를 따른다.

Birth 벡터는 \(J=M e_{24}\)이며 guard 성분은 0이다. \(M\)은 저장된 fl_dt_SOURCE_bits를 exact하게 해독한 값이다. 원자료에서
\[
M=\operatorname{exact}(\mathrm{0x3eca36e2eb1c432d}),\quad
M_F=\operatorname{exact}(\mathrm{0x3eda36e2eb1c432d})=2M
\tag{6}
\]
가 정확히 성립한다. 이 identity는 두 PREBE.json의 원 bits를 비교해 확인했다.

같은 COMMON \(z_0\), 실제 gas roots \(g_1,g_2\)에서
\[
Q_1=Rz_0+bJ,\quad z_1=A_1(g_1)Q_1,\qquad
Q_2=Rz_1+bJ,\quad z_2=A_2(g_2)Q_2,
\tag{7}
\]
\[
P_1=B_1(g_1)Q_1,\qquad P_2=B_2(g_2)Q_2
\tag{8}
\]
이다. \(Q\)는 absorption 전, \(z\)는 absorption 후, \(P\)는 integrated absorbed photons/H이다.

Full input은 \(Q_F=R_Fz_0+2bJ\)다. 임의 비교점 \(g_*\)에서
\[
z_F(g_*)=A_F(g_*)Q_F,\quad P_F(g_*)=B_F(g_*)Q_F,
\]
\[
\Delta z_*=z_2-z_F(g_*),\qquad
\Delta P_*=P_1+P_2-P_F(g_*).
\tag{9}
\]
\(g_*=g_F\)는 실제 Full endpoint 비교이고, \(g_*=g_2\)는 Full residual을 실제 two-half endpoint에서 평가하는 데 필요한 비교다.

## 3. residual용 결함의 정확한 분해

이 절에서는
\[
A=A_2(g_2),\quad B=I-A,\quad A_F=A_F(g_2),\quad B_F=I-A_F,
\]
\[
\tau=h\,\operatorname{diag}(\kappa_{2,j}(x_2)),\quad
\Delta A_1=A_1(g_1)-A,\quad \Delta R=R^2-R_F
\tag{10}
\]
로 둔다. \(\tau\)의 guard 성분은 0이다. 다음 대각 연산자는 물리 영역 \(0\le x_2\le1\)에서 비음수다.
\[
C_1=\tau A^2A_F,\qquad C_2=\tau^2A^2A_F.
\tag{11}
\]
각 \(t=h\kappa\ge0\)에 대해
\[
C_1(t)=\frac{t}{(1+t)^2(1+2t)},\qquad
C_2(t)=\frac{t^2}{(1+t)^2(1+2t)},
\]
\[
A^2-A_F=-C_2,\qquad A^2+A-2A_F=C_1.
\tag{12}
\]

### 3.1 outgoing 결함

\([R,A]=RA-AR\)로 쓰면
\[
\boxed{\begin{aligned}
\Delta z_2={}&AR\Delta A_1Q_1+A[R,A]Q_1-C_2R^2z_0
+A_F\Delta Rz_0\\
&+bA^2(R-I)J+bC_1J .
\end{aligned}}
\tag{13}
\]
아래첨자 2는 비교점 \(g_*=g_2\)를 뜻한다.

| 항 | 구분되는 작용 |
|---|---|
| \(AR\Delta A_1Q_1\) | 첫 half와 endpoint 기준의 opacity 변화 |
| \(A[R,A]Q_1\) | 중간 absorption과 다음 remap의 순서 |
| \(-C_2R^2z_0\) | 같은 opacity에서 두 half BE absorption과 한 Full BE absorption의 차이 |
| \(A_F\Delta Rz_0\) | COMMON spectrum의 remap 분할 |
| \(bA^2(R-I)J\) | 먼저 생성된 광자가 겪는 추가 redshift |
| \(bC_1J\) | 두 half birth와 한 Full birth의 absorption 시점 |

**증명.** \(A_1=A+\Delta A_1\)을 (7)에 넣어
\[
z_2=AR\Delta A_1Q_1+ARAQ_1+bAJ
\]
를 얻는다. \(RA=AR+[R,A]\)와 \(Q_1=Rz_0+bJ\)에서
\[
ARAQ_1=A^2R^2z_0+bA^2RJ+A[R,A]Q_1.
\]
\(A_FR_Fz_0+2bA_FJ\)를 빼고 (12)를 쓰면 (13)이 된다. 처음부터 같은 \(z_0,b\)를 공유한다. \(\square\)

### 3.2 integrated absorption 결함

기체 residual에 직접 들어가는 식은
\[
\boxed{\begin{aligned}
\Delta P_2={}&-(I-BR)\Delta A_1Q_1+B[R,A]Q_1+B(I-R)Rz_0\\
&+C_2R^2z_0+B_F\Delta Rz_0\\
&+bBA(R-I)J-bC_1J .
\end{aligned}}
\tag{14}
\]
\(B(I-R)Rz_0\)는 첫 absorption에서 소모된 광자를 둘째 redshift 뒤의 node와 비교하는 데 필요한 항이다. 기체 에너지 증분은 각 absorption이 실제 발생한 node에서 평가된다.

**증명.** \(B_1=B-\Delta A_1\)에서
\[
\Delta P_2=-(I-BR)\Delta A_1Q_1+BQ_1+BRAQ_1+bBJ-B_FQ_F.
\]
\(BRAQ_1=BARQ_1+B[R,A]Q_1\)를 쓰면 COMMON 부분은
\[
BRz_0+BAR^2z_0-B_FR_Fz_0
=B(I-R)Rz_0+C_2R^2z_0+B_F\Delta Rz_0,
\]
birth 부분은
\[
b(2B+BAR-2B_F)J=bBA(R-I)J-bC_1J.
\]
여기서 \(B+BA=I-A^2\), \(2B+BA-2B_F=-C_1\)을 사용했다. \(\square\)

### 3.3 opacity 변화의 시간·기체 분해

각 group의 resolvent 차이를 먼저 계산하면
\[
\boxed{\Delta A_{1,j}
=h[\kappa_{2,j}(x_2)-\kappa_{1,j}(x_1)]A_{1,j}A_j,}
\tag{15}
\]
\[
\kappa_{2,j}(x_2)-\kappa_{1,j}(x_1)
=(a_{2,j}-a_{1,j})(1-x_2)+a_{1,j}(x_1-x_2).
\tag{16}
\]
첫 항은 captured source density 시각 변화, 둘째 항은 실제 기체 이동이다. 동일 \(c,\sigma_j\) leaves에서
\[
a_{2,j}-a_{1,j}
=\operatorname{exact}(c)\operatorname{exact}(\sigma_j)
[\operatorname{exact}(n_{H,2})-\operatorname{exact}(n_{H,1})]
\tag{17}
\]
를 먼저 구성해 차이의 상관관계를 유지한다.

## 4. 원 격자의 희소 구조와 새 sector 부호

### 4.1 중간 absorption·remap 순서

PHYS14가 확인한 branch에서
\[
Re_j=(1-\alpha_j)e_j+\alpha_je_{j-1},\qquad
\alpha_j=(1-\rho)\frac{E_j}{E_j-E_{j-1}},\quad j\ge1.
\tag{18}
\]
따라서 commutator의 retained 비영 성분은 한 subdiagonal에 있다.
\[
[R,A]_{j-1,j}
=\alpha_j(A_j-A_{j-1})
=\frac{h\alpha_j(\kappa_{2,j-1}-\kappa_{2,j})}
{(1+h\kappa_{2,j})(1+h\kappa_{2,j-1})}.
\tag{19}
\]
실제 guard로 나가는 group 0은 HI inactive여서 \(A_0=1\), guard의 \(A=1\)과 같으므로 그 commutator는 0이다.

**명제 1.** 원 captured HI cross section, 물리 값 \(Q_1\ge0\), \(0\le x_2\le1\)에서
\[
\boxed{B[R,A]Q_1\ge0}
\tag{20}
\]
가 성분별로 성립한다.

**증명.** 원 source에서 \(\sigma_{16}>\sigma_{17}>\cdots>\sigma_{32}>0\)이다. Active output \(i\ge16\)으로 들어가는 edge \(j=i+1\)에서는 \(\kappa_i\ge\kappa_j\), 따라서 \(A_j-A_i\ge0\)다. Threshold edge \(16\to15\), 나머지 inactive 및 guard output에서는 \(B_i=0\)이다. 모든 \(\alpha_j,Q_{1,j},B_i\)는 비음수여서 (20)이 따른다. \(\square\)

따라서 이 sector의 직접 gas forcing은 \(x,w\) 두 성분에서 비음수다. 이는 \(\epsilon_j>0\)인 active output에서 \(\nu_j=(1,0,0,\epsilon_j)^{\mathsf T}\)로 사영한 결과다.

### 4.2 stock과 birth 사이 absorption 시점의 balance

두 대각 chronology 항은
\[
\boxed{C_2R^2z_0-bC_1J
=C_1[\tau R^2z_0-bJ].}
\tag{21}
\]
따라서 각 active group의 부호는
\[
\tau_j(R^2z_0)_j-bJ_j
\tag{22}
\]
로 판별한다. Birth가 없는 group에서는 비음수이고, birth node 24에서는
\[
\tau_{24}(R^2z_0)_{24}\gtreqless bM
\tag{23}
\]
이 같은-opacity chronology sector의 absorption 증가·영·감소를 결정한다. \(\lambda,b\)와 COMMON에 대한 동일한 pointwise 식이므로, 적절한 interval 포함으로 uniform 판별도 가능하다.

### 4.3 birth-redshift sector의 이온화·열 분리

\(J=Me_{24}\)에서 (18)을 쓰면
\[
P_{\mathrm{birth},R}:=bBA(R-I)J
=bM\alpha_{24}(\beta_{23}e_{23}-\beta_{24}e_{24}),
\quad \beta_j=\frac{\tau_j}{(1+\tau_j)^2}.
\tag{24}
\]
\(\eta=hc\,n_{H,2}(1-x_2)\ge0\), \(\tau_j=\eta\sigma_j\)라 하면
\[
\beta_{23}-\beta_{24}
=\frac{\eta(\sigma_{23}-\sigma_{24})(1-\eta^2\sigma_{23}\sigma_{24})}
{(1+\eta\sigma_{23})^2(1+\eta\sigma_{24})^2}.
\tag{25}
\]
원 captured leaves와 전체 물리 범위 \(0\le x_2\le1\)에서
\[
\eta^2\sigma_{23}\sigma_{24}
\le(hc\,n_{H,2})^2\sigma_{23}\sigma_{24}<1.
\tag{26}
\]
상한의 소수 표시는 약 \(0.00013495931272495\)이고, 실제 판정은 exact Fraction 교차곱으로 한다.

또한 원 captured heat와 cross section에서
\[
\epsilon_{23}\sigma_{23}<\epsilon_{24}\sigma_{24},
\qquad \sigma_{23}>\sigma_{24}
\tag{27}
\]
이다. 따라서 \(\eta>0\)일 때
\[
\epsilon_{23}\beta_{23}
=\frac{\eta\epsilon_{23}\sigma_{23}}{(1+\eta\sigma_{23})^2}
<
\frac{\eta\epsilon_{24}\sigma_{24}}{(1+\eta\sigma_{24})^2}
=\epsilon_{24}\beta_{24}.
\tag{28}
\]

**명제 2.** \(b>0\), \(x_2<1\), 원 branch의 \(\alpha_{24}>0\)에서 이 sector는
\[
\boxed{\sum_jP_{\mathrm{birth},R,j}>0,\qquad
\sum_j\epsilon_jP_{\mathrm{birth},R,j}<0}
\tag{29}
\]
를 만족한다. 앞당겨 생성되어 redshift된 광자의 spectrum 변화는 이 sector의 이온화 absorption을 늘리고 thermal deposition을 줄인다.

동일한 현재 gas 상태 \(w>0,\Pi>0\)에서 온도 covector
\[
T_g\,\delta g=C_T\left(\frac{\delta w}{\Pi}
-\frac{w\,\delta e}{\Pi^2}\right)
\tag{30}
\]
로 이 sector의 직접 gas forcing을 사영하면 음수다. 전체 endpoint의 attribution은 §7의 동일한 implicit inverse를 통과시켜 계산한다.

## 5. 재사용 remap 차이와 guard moment

\(\Delta_j=E_j-E_{j-1}\)라 두면 PHYS14의 원 비균일 격자 식은
\[
\Delta Re_j=\alpha_j\alpha_{j-1}
\left[\frac{\Delta_{j-1}}{\Delta_j}e_j
-\left(1+\frac{\Delta_{j-1}}{\Delta_j}\right)e_{j-1}+e_{j-2}\right],
\quad j\ge2.
\tag{31}
\]
경계 column은
\[
\begin{aligned}
\Delta Re_1={}&\alpha_1(\alpha_1+\rho-1)e_1
-\alpha_1(\alpha_1+\rho)e_0\\
&+\alpha_1e_{G_N}+\rho E_0\alpha_1e_{G_U}.
\end{aligned}
\tag{32}
\]
\(j=0\) 및 기존 guard column의 차이는 0이다.

광자 수와 energy row를
\[
\mathfrak n^{\mathsf T}=(1,\ldots,1,1,0),\qquad
\mathfrak u^{\mathsf T}=(E_0,\ldots,E_{32},0,1)
\tag{33}
\]
로 두면
\[
\mathfrak n^{\mathsf T}R=\mathfrak n^{\mathsf T},\qquad
\mathfrak u^{\mathsf T}R=\rho\mathfrak u^{\mathsf T},\qquad
\mathfrak n^{\mathsf T}\Delta R
=\mathfrak u^{\mathsf T}\Delta R=0.
\tag{34}
\]
이는 (31)–(32)의 계수합과 \(E\)-가중합에서 직접 나온다. 해당 계수의 연결을 유지해 정확한 0을 구성한다.

## 6. photon ledger에서 H 화학·열에너지 residual로

이 절은 임의 비교점 \(g_*\)에 적용된다. \(\Delta\mathcal N=\mathfrak n^{\mathsf T}\Delta z_*\), \(\Delta\mathcal U=\mathfrak u^{\mathsf T}\Delta z_*\)로 두면 photon number 보존에서
\[
\boxed{\sum_j\Delta P_{*,j}=-\Delta\mathcal N.}
\tag{35}
\]
첫 absorption은 둘째 redshift 전에 발생하므로 energy ledger는
\[
\begin{aligned}
\mathfrak u^{\mathsf T}z_2
&=\rho^2\mathfrak u^{\mathsf T}z_0+b(\rho+1)ME_{24}
-\rho\sum_jE_jP_{1,j}-\sum_jE_jP_{2,j},\\
\mathfrak u^{\mathsf T}z_F(g_*)
&=\rho^2\mathfrak u^{\mathsf T}z_0+2bME_{24}
-\sum_jE_jP_{F,j}(g_*).
\end{aligned}
\tag{36}
\]
따라서
\[
\boxed{\sum_jE_j\Delta P_{*,j}
=(1-\rho)\left[\sum_jE_jP_{1,j}-bME_{24}\right]-\Delta\mathcal U.}
\tag{37}
\]
대괄호는 첫 half에서 흡수된 광자의 energy와 먼저 주입된 birth energy다. 두 경로에서 redshift work가 작용하는 시점 차이를 나타낸다.

### 6.1 captured heat identity

원 phys04_mixed.rs에서 heat는 floating subtraction '*e - CHI[a]'로 capture된다. 원 17개 active HI group 모두
\[
\boxed{\epsilon_j^{\rm captured}
=\operatorname{exact}(E_j)-\operatorname{exact}(\chi_H)}
\tag{38}
\]
가 exact Fraction 비교에서 확인되었다. Captured \(\chi_H=13.598434599702\) eV와 active \(E_j=13.6\)–20 eV는 \(\chi_H\le E_j<2\chi_H\)를 만족한다.

이 범위는 binary subtraction의 Sterbenz 조건을 충족한다. 두 양의 binary 값의 비가 2 이내이면 지수를 맞춘 정수 significand 차이가 원 precision 안에 들어간다. 같은 exponent이면 두 \(p\)-bit 정수의 차이이고, exponent가 1 차이면 \(E\le2\chi_H\)가 차의 크기를 \(p\) bits 이하로 제한한다. 해당 값과 차는 normal 범위에 있어서 subtraction은 정확히 표현된다. (38)은 이 설명과 독립적으로 원 bits에서 직접 확인했다.

Inactive group에서 모든 absorption \(P\)가 0이므로 전체 합에서
\[
\boxed{\sum_j\epsilon_j\Delta P_{*,j}
=(1-\rho)[E\cdot P_1-bME_{24}]
-\Delta\mathcal U+\chi_H\Delta\mathcal N.}
\tag{39}
\]
H 화학·열에너지 covector를
\[
\ell_H=(\chi_H,0,0,1)
\tag{40}
\]
로 정의하면 \(\ell_H\nu_j=E_j\), \(\ell_H\nu_{\rm HH}=0\)이다. \(\nu_{\rm HH}=(1,0,0,-\chi_H)^{\mathsf T}\)이며, covector의 대상은 \(\chi_Hx+w\)이다. He source는 원 nonphoto 벡터를 이 covector로 사영한 기여로 유지한다.

## 7. Full residual과 endpoint 관측량

비광자 gas source를
\[
\mathcal B_k(g,\lambda)
=F_k^{\rm np}(g)+\lambda q_k(g)\nu_{\rm HH}-2H_kwe_w
\tag{41}
\]
로 두면 실제 단계식은
\[
g_1-g_0=h\mathcal B_1(g_1,\lambda)+\sum_j\nu_jP_{1,j},\qquad
g_2-g_1=h\mathcal B_2(g_2,\lambda)+\sum_j\nu_jP_{2,j}.
\tag{42}
\]
Full residual을 실제 \(g_2\)에서
\[
r=g_2-g_0-2hF_F(g_2;Q_F,\lambda)
\tag{43}
\]
로 정의하면
\[
\boxed{r=h[\mathcal B_1(g_1,\lambda)-\mathcal B_2(g_2,\lambda)]
+\sum_j\nu_j\Delta P_{2,j}.}
\tag{44}
\]
따라서 photon forcing은
\[
r_x^{\rm ph}=-\Delta\mathcal N,\qquad
r_w^{\rm ph}=(1-\rho)[E\cdot P_1-bME_{24}]
-\Delta\mathcal U+\chi_H\Delta\mathcal N,
\tag{45}
\]
\[
\boxed{\ell_Hr
=h\ell_H[\mathcal B_1(g_1,\lambda)-\mathcal B_2(g_2,\lambda)]
+(1-\rho)[E\cdot P_1-bME_{24}]-\Delta\mathcal U.}
\tag{46}
\]
HH direct contribution은 이 covector에서 대수적으로 소거된다. HH가 이력에 미친 효과는 \(g_1,g_2,P_1,\Delta\mathcal U\)와 nonphoto 평가점에 전달된다.

Full 근 \(g_F\)와 \(g_2\)를 잇는 segment가 원 convex source domain 안에 있으면
\[
\overline J_F=\int_0^1F_{F,g}(g_F+s(g_2-g_F);Q_F,\lambda)\,ds,
\qquad
\boxed{(I-2h\overline J_F)(g_2-g_F)=r.}
\tag{47}
\]
원 Full contraction 또는 같은-domain inverse 포함을 재사용하여 4D 식을 푼다. (14), (44)의 sector를 동일한 inverse로 통과시키면 endpoint attribution이 된다.

두 endpoint의 normalization이 같으므로
\[
\delta e=\delta x+\widehat f_2(\delta y_1+2\delta y_2),\qquad
\Pi=1+\widehat f_2+e,
\]
\[
\boxed{T_2-T_F=C_T\left[\frac{\delta w}{\Pi_2}
-\frac{w_F\delta e}{\Pi_2\Pi_F}\right].}
\tag{48}
\]
두 큰 temperature interval의 차이 대신 직접 \(\delta g\)를 변환한다.

## 8. 실제 Full photon endpoint를 위한 일반 비교점

\(g_*\)에서 \(A=A_2(g_*)\), \(A_F=A_F(g_*)\)로 (13)을 구성하면 가상 둘째 half \(AQ_2\)와 \(A_FQ_F\)의 차이가 얻어진다. 실제 둘째 half로 옮기는 항은
\[
\Delta z_*=[\text{(13)의 우변, 기준 }g_*]+[A_2(g_2)-A_2(g_*)]Q_2,
\tag{49}
\]
\[
\boxed{[A_2(g_2)-A_2(g_*)]Q_2
=h\,\operatorname{diag}\left[
\frac{a_{2,j}Q_{2,j}}{D_{2,j}(g_2)D_{2,j}(g_*)}
\right](x_2-x_*).}
\tag{50}
\]
Guard 성분은 0이고, absorption 결함의 추가 항은 그 음수다. \(g_*=g_F\)이면 (47)의 \(\delta x\)를 넣어 실제 Full–two-half outgoing 결함을 구한다. Residual 구성에서는 \(g_*=g_2\)여서 추가 항이 0이다.

## 9. 극한·계산 계약·검산 상태

### 정확한 극한

1. **Transparent:** \(A_1=A=A_F=I\)이면 \(\Delta P=0\), \(\Delta z=\Delta Rz_0+b(R-I)J\).
2. **수송·opacity 변화·birth가 없는 stock:** \(R=I,A_1=A,b=0\)이면 \(\Delta z=-C_2z_0,\ \Delta P=C_2z_0\).
3. **수송·opacity 변화 없이 초기 광자가 없는 birth:** \(z_0=0,R=I,A_1=A\)이면 \(\Delta z=bC_1J,\ \Delta P=-bC_1J\).
4. **동일 opacity:** \(\Delta A_1=0\)이면 시각·gas-opacity 항이 소거되고 나머지 정확한 작용들이 남는다.

### Interval로 옮길 관계

- \(R_F=R(\rho^2),M_F=2M\), 동일 \(z_0,b\)를 먼저 결박한다.
- \(\Delta R\)는 (31)–(32), commutator는 (19), \(\Delta A_1\)는 (15)–(17), \(C_1,C_2\)는 (11)–(12)에서 직접 구성한다.
- \(Q_1=Rz_0+bJ\)와 birth sector 사이 공통 입력을 유지한 뒤 외향 연산을 한다.
- 33개 group, guards, 모든 signed \(U,V,W\)를 유지한다. 임의 \(C^2\) 매개변수 계열에서 항등식을 미분하면 같은 식의 정확한 product/quotient rule이 모든 slot에 적용된다.
- (14)와 (35)–(39)를 각각 valid inclusion으로 평가해 더 좁은 교집합을 사용할 수 있다. Exact ledger zero는 연결된 계수로 구성한다.
- 새 실제 수치 \(r,\delta g,\delta T\)는 이 식과 기존 Full source inclusion을 결합할 다음 coding 계산 대상이다.

### 실제 수행한 판별 검산

check_photon_defect_identities.py는 PHYS14 후보를 import하지 않고 원 captured leaves를 읽었다. 별도의 exact Fraction 및 \(\mathbb Q[e,f]/(e^2,f^2)\) 네 슬롯 산술로 순서가 다른 두 표현을 직접 대입했다. Spectrum과 gas 값·미분은 명시적인 manufactured rational 예제이며, \(\rho=1-1/160000\)을 사용했다.

**39개 관계, 네 슬롯 포함 3148개 scalar equality가 모두 통과**했다. Wall 약 0.48초, peak RSS 약 16 MiB였다. 실제 scientific history, root, native source 실행은 0회다. 검산은 outgoing/absorption factorization, guard 포함 number/energy/heat 수지, opacity secant, sparse commutator, 세 판별 극한, source birth/heat leaf identity를 다룬다. 새 sector 부호의 원 leaf 조건은 별도 SECTOR_SIGN_CHECKS.json에 기록한다.

이 분과에서 완결한 유도와 검산은 부모 연구 루프의 독립 검토로 전달한다. 다음 연결은 (44)–(48)을 이용한 실제 correlated endpoint inclusion이다.

