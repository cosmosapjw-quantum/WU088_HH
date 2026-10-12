# WU088_HH PHYS14 — 등방 공동 carry의 정확한 축약과 다음 half의 관측량 응답

2026-10-12. 작성 역할은 이론 후보 생성이다. 아래 새 정리의 근거 상태는 **derived**다. 원 PHYS09–13의 소스 포함과 첫 단계 근 계열은 상속하며, PHYS14의 실제 다음 단계 포함 계산·최종 독립 판정은 owner와 별도 reviewer의 결과를 따른다.

이번 목적은 PHYS11이 이미 유도한 일반 공동 carry 공식을 실제 다음 시간 단계에 적용하는 것이다. 새 기여는 현재 등방 배경에서의 **정확한 39개 상태 축약**, 기존 Full 소스 중 **다음 half에서도 동일한 부분의 재사용 정리**, HI 단일 광흡수 채널의 **rank-one Jacobian과 광자 기억의 부호 구조**, 그리고 **두 half와 Full 사이의 spectral-remap 차이를 분리하는 정확한 식**이다. 일반 implicit chain rule과 PHYS13의 온도 체인룰은 기존 결과로 재사용한다.

## 1. 입력 계열, 시각 및 관측량

원 COMMON의 시각을 \(t_0=1.6\times10^{11}\,\mathrm s\), half 길이를 \(h=6.25\times10^8\,\mathrm s\)라 한다. 이번에 이어갈 시각은

\[
t_1=t_0+h=1.60625\times10^{11}\,\mathrm s,
\qquad t_2=t_0+2h=1.6125\times10^{11}\,\mathrm s.
\tag{1}
\]

\(t_1\)의 입력은 PHYS09–13의 `first_half`에 해당하는 같은 COMMON 첫 단계의 출력이다. \(t_2\)는 기존 `Full`의 종료 시각과 같다. 미래 parameter \(\theta=(\lambda,b)\in[0,1]^2\)는 두 half에서 공통으로 유지한다. 따라서 \(\lambda\) 미분에는 첫 half가 남긴 기체·광자 변화와 둘째 half의 직접 HH forcing이 모두 들어간다. COMMON의 과거 HH ON 이력·원 광자·보상 상태는 초기 입력으로 보존된다.

기체 좌표와 온도는

\[
g_k=(x_k,y_{1,k},y_{2,k},w_k),\qquad
e_k=x_k+\widehat f_k(y_{1,k}+2y_{2,k}),
\]
\[
\Pi_k=1+\widehat f_k+e_k,
\qquad T_k=C_Tw_k/\Pi_k,
\quad C_T=\frac{2\operatorname{exact}(\epsilon_{\rm eV})}
{3\operatorname{exact}(k_B)}.
\tag{2}
\]

\(w\)는 eV/H, \(N_j\)는 photons/H, \(e\)는 electrons/H, \(T\)는 K다. 각 단계의

\[
f_k=\operatorname{exact}(f_{\rm He,stage}),\qquad
\widehat f_k=\frac{\operatorname{exact}(n_{\rm He,stored,k})}
{\operatorname{exact}(n_{H,k})}
\tag{3}
\]

를 구별한다. \(f_k\)는 photo source, \(\widehat f_k\)는 FT03 nonphoto·HH 온도·전자 정의에 쓰인다. 모두 \(\lambda,b\)에 대해 고정이며, 같은 단계의 parameter rectangle에서 같은 coefficient tuple을 사용한다. 기하학은 원 선택값 \(H_1=H_2=H_3=H=10^{-14}\,\mathrm{s}^{-1}\)다. 이 문서에서 source에 결박한 \(H,h,E,c\) 등의 계산용 상수는 해당 captured binary leaf의 정확한 실수 값을 뜻한다. 비등방 성분을 이 새 특수화의 입력으로 추가하지 않는다.

## 2. 새 정리 A: 등방 배경의 정확한 group closure

### 2.1 원 ray 기하학에서 공통 redshift 비율을 얻는다

원 `paired_runtime.rs::g_box`의 실수 함수는 captured ray 벡터 \(q_r\ne0\)에 대해

\[
G_r(t)=\left[\sum_{i=1}^3q_{ri}^2e^{-2H_it}\right]^{1/2}.
\]

등방 조건 아래

\[
G_r(t)=e^{-Ht}\|q_r\|,
\qquad
\boxed{\rho_k=G_r(t_k)/G_r(t_{k-1})=e^{-Hh_k}}.
\tag{4}
\]

captured \(q_r\)의 길이가 정확히 1이라는 추가 조건도 필요 없다. 같은 captured 벡터의 norm이 분자·분모에서 상쇄된다. 원 source의 exact-real geometry에 대한 결과이므로 outward ray별 ratio interval들이 조금씩 달라도 공통 값 (4)을 포함할 수 있다.

원 source weight의 실수 기하학도 \(\mathrm{volume}/G_r(t)^3=\|q_r\|^{-3}\)이므로 등방 배경에서는 시각에 독립이다. 그 값들을 합으로 정상화한 실제 계열은

\[
\omega_r=\|q_r\|^{-3}/\sum_s\|q_s\|^{-3},\qquad
\omega_r\ge0,\quad\sum_r\omega_r=1.
\tag{5}
\]

따라서 128개 weight가 각각 정확히 \(1/128\)이라고 가정할 필요가 없다. 저장된 weight interval을 소비할 경우에는 (5)의 관계를 만족하는 기하학 계열을 선택한다. 독립 interval 끝점을 각각 실제 계수로 선택하는 box family보다 이 조건을 포함한 family가 더 구체적이다.

### 2.2 선형 수송·guard map의 축약

원 captured energy node \(E_0<\cdots<E_{32}\)와 piecewise-linear hat \(H_i(E)\)로

\[
\mathsf R_{ij}(\rho)=H_i(\rho E_j)
\tag{6}
\]

를 정의한다. \(\rho E_j<E_0\)인 column은 retained grid에서 0이며 lower guard로 보낸다. 원 guard·hat branch가 고정되는 coefficient domain을 사용한다. 그러면 각 ray의 transport와 다음 incoming은

\[
\bar n_{r,i}=\sum_j\mathsf R_{ij}(\rho)n^-_{r,j},
\qquad n^{\rm in}_{r,i}=\bar n_{r,i}+b\widehat{hS}\,\omega_r\delta_{i,24}.
\tag{7}
\]

\(\widehat{hS}=\operatorname{exact}(\operatorname{fl}(h\,\mathrm{SOURCE}))\)는 source가 capture한 leaf다. 원 \(h,S\)를 새로 실수 곱해 이 leaf를 교체하지 않는다.

다음 aggregate를 취한다.

\[
N_j=\sum_r n_{r,j},\qquad G_N=\sum_rG_{N,r},\qquad G_U=\sum_rG_{U,r}.
\]

유한합과 (7)을 교환하면

\[
\boxed{N^{\rm in}=\mathsf R(\rho)N^-+b\widehat{hS}e_{24}},
\tag{8}
\]

\[
G_N^+=G_N^-+\sum_{j\in\mathcal G}N^-_j,
\qquad
G_U^+=\rho G_U^-+\sum_{j\in\mathcal G}\rho E_jN^-_j.
\tag{9}
\]

여기서 \(\mathcal G=\{j:\rho E_j<E_0\}\)다. 기체는 transport 동안 그대로이고, local absorption에서 denominator는 ray에 독립이므로 PHYS11의

\[
n^+_{r,j}=n^{\rm in}_{r,j}/D_j(g^+),
\qquad N^+_j=N^{\rm in}_j/D_j(g^+)
\tag{10}
\]

가 적용된다.

### 2.3 정확한 축약의 증명과 계산적 효과

full state에서 \((g,N,G_N,G_U)\)를 취하는 선형 사상을 \(\mathsf C\), residual denominator를 각 ray에도 동일하게 쓰는 **source-aligned exact-real full ray stage**를 \(\Phi_k\), (8)–(10)과 같은 4D implicit gas residual로 구성한 축약 stage를 \(\bar\Phi_k\)라 하자. 이 denominator 선택은 PHYS11의 source-aligned carry를 따른다. 원 `phys04_distribute_after_be`의 선행 scalar 곱 leaf와 residual의 개별 leaf 곱 차이는 원본 provenance에 따로 남긴다. 동일한 입력 계열에서 해당 gas root가 유일하면

\[
\boxed{\mathsf C\Phi_k=\bar\Phi_k\mathsf C},
\qquad
\mathsf C\Phi_m\cdots\Phi_1
=\bar\Phi_m\cdots\bar\Phi_1\mathsf C.
\tag{11}
\]

증명은 transport의 (8)–(9), ray 공통 absorption (10), gas residual이 aggregate \(N^{\rm in}\)에만 의존한다는 원 소스식에 따른다. 양쪽 gas residual이 동일하므로 유일 근도 동일하다. 다음 단계에 같은 논리를 귀납적으로 적용하면 두 번째 식을 얻는다. \(\mathsf C\)는 선형이고 각 stage family가 \(C^2\)이면 값·\(\lambda\)·\(b\)·\(\lambda b\)의 네 carry 성분에도 (11)이 적용된다.

따라서 **현재 등방 family의 기체·spectral group·총 guard 관측량**은 gas 4개+photon group 33개+guard 합 2개, 총 **39개 실수 상태**로 정확히 닫힌다. 각 상태의 네 carry 성분을 유지하면 156개 scalar slots다. 원 full 구조의 gas4+ray4224+guard256=4484개 상태와 비교한 대수적 축약이다. Ledger는 필요한 누적 관측량을 별도 scalar로 더한다. 이 숫자는 wall-time 가속비의 측정값이 아니다.

실제 ray 배열이 확보되면 초기 aggregate와 guard 합을 직접 구성해 (11)의 입력을 연결한다. 이미 유효한 aggregate carry가 있는 첫 단계의 기체·총 spectral 후속 계산은 그 aggregate도 사용할 수 있다. 향후 ray별 관측량은 원 ray 배열을 별도로 유지한다. 원 native scalar coefficient capture graph 및 compensation 값은 해당 원본 상태의 provenance로 보존한다.

### 2.4 광자수·에너지 수송 수지

실제 hat 계수 관계를 보존하면 각 column에서

\[
\sum_i\mathsf R_{ij}+\mathbf1_{j\in\mathcal G}=1,
\quad
\sum_iE_i\mathsf R_{ij}+\rho E_j\mathbf1_{j\in\mathcal G}=\rho E_j.
\tag{12}
\]

따라서 transport+guard는 photon number를 보존하고 총 photon/guard energy를 \(\rho\)배 한다. Redshift work 증분은 \((1-\rho)(\sum_jE_jN_j^-+G_U^-)\)이다. (12)를 구성 단계에서 사용하면 큰 independent energy intervals를 빼는 cancellation 손실도 줄일 수 있다. 모든 \(\theta\) 미분은 같은 선형 항등식을 따른다.

## 3. 새 정리 B: 기존 Full의 nonphoto·HH source는 둘째 half에서 그대로 쓸 수 있다

`phys04_reduced_residual`과 `hh_rate_jet`을 실제로 읽으면 nonphoto 4-vector \(F^{\rm np}\)와 HH event rate \(q\)는

\[
F^{\rm np}=F^{\rm np}(g;n_H,n_{\rm He,stored},k_B,\epsilon_{\rm eV},\text{atomic leaves}),
\qquad q=q(g;\text{same stage leaves})
\tag{13}
\]

이다. old gas, incoming photons, \(d\), \(b\), \(\lambda\)에 대한 직접 의존성은 없다. HH contribution은 나중에 \(\lambda q(1,0,0,-\chi_H)\)로 들어간다. Thermal expansion contribution도 별도 \(-2H_{\rm mean}w e_w\)다.

현재 둘째 half 종료 시각 \(t_2\)는 기존 Full 종료 시각과 같다. 원 source의 \(n_H=\operatorname{fl}(10^{-4}\exp[-\operatorname{fl}(\sum H_i)\,t_2])\), \(n_{\rm He,stored}=\operatorname{fl}(n_Hf)\), \(H_{\rm mean}\)와 원자 leaf identity가 같다는 실제 비교를 전제로, \(F^{\rm np}_2\)와 \(q_2\)는 **같은 실수 함수**다. 그러므로 기존 Full `SOURCE_BOX_COMPONENTS.json::nonphoto`와 `SOURCE_BOX.json::q`의 값·gas gradient·gas Hessian 포함은 원 전체 domain \(X\)에서 다음 half에도 유효하다.

시간 길이 \(d\)는 (13)에 없으므로 Full의 \(2h\)를 half의 \(h\)로 바꾸어도 이 재사용은 성립한다. 다음 half의 새 source는

\[
F_2(g,\lambda,N^{\rm in}_2)
=F^{\rm np}_{\rm Full}(g)+\lambda q_{\rm Full}(g)\nu_H
-2H_{\rm mean}w e_w+F^{\rm ph}_2(g,N^{\rm in}_2;h),
\quad\nu_H=(1,0,0,-\chi_H).
\tag{14}
\]

이 식에서는 새 incoming carry를 사용해 photo denominators와 photo sum을 다시 계산한다. Full의 완성 residual·Jacobian·outgoing photons는 다른 \(d,N^{\rm in}\)에 대응하므로 (14)의 새 계산 대상으로 구분한다. 저장 Jet의 gas slots 0–3은 (13)의 도함수로 소비한다. \(q,F^{\rm np}\)의 raw forcing slots에 남은 signed rounding tail은 export 원본에 보존하되, (13)으로 구조적으로 증명된 직접 parameter independence와 구별한다.

### 3.1 Uniform root와 \(C^2\) continuation을 닫는 계산형

실제 carry에 따른 \(g_1(\theta)\in Y_1\), \(N^{\rm in}_2(\theta)\in P_2\)가 주어졌다고 하자. 같은 convex box \(X\)에서 다음 두 가지 포함을 실제로 확인한다.

\[
\boxed{Y_1+h[F_2](X,[0,1],P_2)\subset\operatorname{int}X},
\qquad
\|S^{-1}h[F_{2,g}]S\|_\infty\le\kappa<1.
\tag{15}
\]

\(S\)는 양의 diagonal scale이고 \(g\)의 분율·eV/H 단위를 맞추는 데 사용한다. 그러면 \(g\mapsto g_1(\theta)+hF_2(g,\lambda,N^{\rm in}_2(\theta))\)는 모든 동일 계열 parameter에서 strict self-map이자 contraction이다. Banach 정리에 따라 \(X\) 안에 유일한 다음 근 \(g_2(\theta)\)가 있다. Open source domain, 양의 denominators, \(C^2\) incoming carry와 uniform invertibility \(I-hF_{2,g}\)에 의해 implicit function theorem을 적용하면 그 근들은 같은 \(C^2\) 계열을 이룬다.

이때 새 과학적 계산은 **다음 단계의 새 residual 포함·root 존재/유일성·응답 전달**이다. FT03/HH 초월 source kernel을 새로 평가할 필요는 없다. 포함이 넓을 때에는 원 source centre 값과 원 \(X\) gradient/Hessian을 사용한 mean-value/Taylor 포함으로 새 \(Y\subset X\)를 좁힐 수 있다. 이때도 root domain 및 평가 domain을 명시적으로 구별한다.

## 4. 새 정리 C: HI 단일 photo 채널의 작은 전달 구조

원 Full `sigma_bits`를 읽은 결과 HI의 활성 node는 17개이고 HeI, HeII는 각 33개 node에서 모두 exact zero다. 이 source identity 아래

\[
a_j=c\,n_H\sigma_{j,\rm HI},\quad
\kappa_j=a_j(1-x),\quad
D_j=1+h a_j(1-x),\quad
p_j(x)=\frac{a_j(1-x)}{D_j},
\]
\[
\epsilon_j=\operatorname{exact}(\text{captured heat}_{j,\rm HI}),
\qquad \nu_j=(1,0,0,\epsilon_j),
\qquad F^{\rm ph}=\sum_jN_j^{\rm in}p_j\nu_j.
\tag{16}
\]

\(a_j\)의 단위는 \(\mathrm{s}^{-1}\), \(p_j\)는 \(\mathrm{s}^{-1}\)이며 \(\epsilon_j\)는 eV다. \(a_j\)는 residual graph의 captured leaves를 실수로 곱한 값이다.

직접 미분하면

\[
p'_j=-\frac{a_j}{D_j^2},\qquad
p''_j=-\frac{2h a_j^2}{D_j^3}.
\tag{17}
\]

따라서 photo source의 gas Jacobian은

\[
F^{\rm ph}_g=-v e_x^{\mathsf T},\qquad
v=\sum_j\frac{a_jN_j^{\rm in}}{D_j^2}\nu_j,
\tag{18}
\]

처럼 **한 열만 가진 rank-one 행렬**이다. Photo Hessian도 \(xx\) entry만 필요하다. Photon-memory forcing은 \(x,w\) 두 행에만 직접 들어간다. 이 특수화는 He nonphoto와 HH의 전체 gas coupling을 그대로 유지한다.

\(A_0=I-h\{F^{\rm np}_g+\lambda(\nu_Hq_g)-2H_{
\rm mean}e_we_w^{\mathsf T}\}\)라 두면

\[
A=I-hF_g=A_0+hve_x^{\mathsf T}.
\]

\(A_0\)가 가역이고 \(1+h e_x^{\mathsf T}A_0^{-1}v\ne0\)이면 Sherman–Morrison 항등식으로

\[
\boxed{A^{-1}=A_0^{-1}-
\frac{hA_0^{-1}ve_x^{\mathsf T}A_0^{-1}}
{1+h e_x^{\mathsf T}A_0^{-1}v}.}
\tag{19}
\]

이는 선택 가능한 계산형이다. (15)의 간단한 4×4 Neumann/Picard 포함이 충분히 좁으면 새 inverse 구현을 추가할 필요는 없다. (18)은 photo derivative 비용과 cancellation을 줄이면서 새 next-stage 소스를 정확히 구성하는 데 바로 사용할 수 있다.

## 5. 새로운 물리적 전달 구조: 광자 기억과 온도 forcing

### 5.1 HH가 남긴 잔존 광자의 첫 미분

HI-only opacity에 대해 outgoing photon의 parameter derivative는

\[
\boxed{U_{N_j}^+=\frac{U_{N_j}^{\rm in}}{D_j}
+\frac{h a_jN_j^{\rm in}}{D_j^2}U_x^+,}
\qquad
\boxed{V_{N_j}^+=\frac{V_{N_j}^{\rm in}}{D_j}
+\frac{h a_jN_j^{\rm in}}{D_j^2}V_x^+.}
\tag{20}
\]

첫 half에서는 \(U_N^{\rm in}=0\), \(V_N^{\rm in}=\widehat{hS}e_{24}\)가 구조적으로 성립한다. PHYS12–13의 \(U_x>0,V_x>0\), \(N^{\rm in}\ge0\), \(D>0\)를 사용하면 **HH 또는 birth의 증가가 남기는 outgoing photon의 첫 미분은 모든 group에서 비음수**다. 활성 opacity와 양의 incoming stock을 갖는 group에서는 HH 미분이 엄밀히 양수다. Exact source의 구조적 영과 저장된 아주 작은 signed arithmetic tail은 원본에서 함께 추적할 수 있다.

\(\mathsf R\ge0\)이므로 다음 transport에서도

\[
U_{N,2}^{\rm in}=\mathsf R U_{N,1}^{+}\ge0,
\quad
V_{N,2}^{\rm in}=\mathsf R V_{N,1}^{+}+\widehat{hS}e_{24}\ge0.
\tag{21}
\]

즉 첫 half의 HH가 줄인 흡수는 다음 half에 **추가 양의 광자 reservoir**로 전달된다. 다음 단계의 \(U_x^+>0,V_x^+>0\)까지 포함되면 이 비음수 photon-memory 성질은 후속 동일 구조 단계로 귀납적으로 이어진다. Mixed derivative는 (20)의 두 방향 사이 교차항을 포함하므로 이 첫 미분 부호 정리를 그대로 적용하는 항목이 아니다.

### 5.2 Next-stage gas response의 source/carry 분해

PHYS11의 일반식에 (16)–(17)을 넣으면 \(U_2,V_2,W_2\)의 실제 계산은

\[
AU_2=U_1+h\left[q\nu_H+\sum_jp_j\nu_j U_{N,j}^{\rm in}\right],
\]
\[
AV_2=V_1+h\sum_jp_j\nu_j V_{N,j}^{\rm in},
\tag{22}
\]

\[
\begin{aligned}
AW_2=W_1+h\{&F^{\rm np}_{gg}[U_2,V_2]
+\lambda\nu_H q_{gg}[U_2,V_2]+\nu_H q_gV_2\\
&+\sum_j\nu_j[,p''_jN_j^{\rm in}U_{2,x}V_{2,x}
+p'_j(U_{2,x}V_{N,j}^{\rm in}+V_{2,x}U_{N,j}^{\rm in})
+p_jW_{N,j}^{\rm in},]\}.
\end{aligned}
\tag{23}
\]

Thermal expansion은 linear이므로 Hessian forcing에는 새 항이 없다. 필요한 Hessian은 FT03 4개의 gas 4×4, HH의 gas 4×4 및 photo scalar \(p''_j\)다. \(F_{NN}=0\)이며 33×33 photon Hessian을 만들 필요가 없다.

다음 root를 푸는 동안 incoming \(N_2^{\rm in}(\theta)\)는 **현재 gas unknown에 독립인 전달 입력**이다. 따라서 그 current-gas columns는 0이고 이전 gas dependence는 이미 \(U_N,V_N,W_N\)에 들어가 있다. 이 입력 구분을 유지하면 (22)–(23)이 정확히 PHYS11의 chain rule을 구현한다.

### 5.3 광자 하나의 직접 온도 forcing과 완전한 implicit response

PHYS13의 \(T_g\)를 (16)의 source direction에 적용하면

\[
\boxed{T_gQ_j=C_T\frac{p_j}{\Pi}
\left(\epsilon_j-\frac{w}{\Pi}\right).}
\tag{24}
\]

따라서 실제 support에 대해 \(\epsilon_j<w/\Pi\)가 성립하면 추가 incoming photon은 직접 온도 source에서 냉각 방향이다. 원 source history가 \(E\le13.7\,\mathrm{eV}\) support를 유지하고 현재 \(w/\Pi\simeq6.3\,\mathrm{eV}\) 영역이라면 captured heat는 최대 약 \(0.102\,\mathrm{eV}\)여서 큰 간격으로 이 조건을 만족한다. 이 support는 원 COMMON 또는 실제 carry에서 별도로 확인하고, 전체 20 eV grid를 13.7 eV support로 바꿔 읽지 않는다.

완전한 implicit 온도 response는 \(z_T=A^{-\mathsf T}T_g^{\mathsf T}\)로

\[
\boxed{U_{T,2}=z_T^{\mathsf T}U_1
+h z_T^{\mathsf T}q\nu_H
+h\sum_j(z_T^{\mathsf T}Q_j)U_{N,j}^{\rm in}.}
\tag{25}
\]

이 식은 같은 미분에서 gas memory·직접 HH·photon memory를 정확히 분해한다. 각 항에 gas feedback이 같은 \(A^{-1}\)로 적용된다. 실제 \(z_T^{\mathsf T}Q_j<0\)를 포함하고 (21)을 확인하면 마지막 항은 비양수이므로 **HH가 남긴 광자 기억이 다음 단계의 온도 응답에 추가 냉각으로 기여한다**. 이 부호는 (24)의 직접 forcing과 구별해 실제 inverse 포함으로 판정한다. 독립적인 source switch 실험으로 세 항을 정의할 필요 없이, 동일 global \(\lambda\) 응답의 전달 기여로 읽을 수 있다.

## 6. PHYS13 관측량을 실제 두-half endpoint에 적용

새 \(U_2,V_2,W_2\)와 root 포함 \(Y_2\)가 얻어지면 현재 stage의 \(\widehat f_2\)로

\[
U_{e,2}=U_{2,x}+\widehat f_2(U_{2,y_1}+2U_{2,y_2}),
\]
\[
U_{T,2}=C_T\left(\frac{U_{2,w}}{\Pi_2}-\frac{w_2U_{e,2}}{\Pi_2^2}\right)
\tag{26}
\]

를 계산한다. \(V,W\)의 공식은 PHYS13의 Hessian 포함식을 그대로 사용한다. 같은 \(C^2\) rectangle에서

\[
\Delta_{\rm HH}T_2(b)=\int_0^1U_{T,2}(\lambda,b)\,d\lambda,
\quad
\Delta_{\rm HH}e_2(b)=\int_0^1U_{e,2}(\lambda,b)\,d\lambda,
\]
\[
I_{T,2}=\int_0^1\!\int_0^1W_{T,2}(\lambda,b)\,d\lambda\,db.
\tag{27}
\]

따라서 uniform derivative 포함은 실제 **COMMON→first half→second half**를 따른 유한 endpoint response를 포함한다. (27)의 의미는 과거 두 개의 별도 first-stage 표를 더한 값과 구별된다. \(U_{e,1}\)과 차이를 낼 때는 \(\widehat f_1,\widehat f_2\)가 각 stage에 맞는지도 유지한다.

## 7. 새 정리 D: 두 half와 Full의 spectral-remap 차이를 정확히 분리한다

등방 redshift에서는 \(\rho(2h)=\rho(h)^2\)다. 고정-node hat projection이 들어간 이산 map은 두 가지 서로 다른 projection 순서를 갖는다. 이를 원 captured nonuniform energy nodes에서 정확히 비교할 수 있다.

\(\Delta_j=E_j-E_{j-1}>0\), \(\varepsilon=1-\rho\), \(a_j=\varepsilon E_j/\Delta_j\)라 하자. \(j\ge2\)이고 \(\rho E_j,\rho^2E_j\)가 모두 \([E_{j-1},E_j]\), \(\rho E_{j-1}\in[E_{j-2},E_{j-1}]\)에 속한다고 가정한다. 해당 columns에 대해

\[
\mathsf R(\rho)e_j=(1-a_j)e_j+a_je_{j-1}.
\tag{28}
\]

\(\mathsf R(\rho)^2e_j\)의 세 성분은

\[
(1-a_j)^2e_j+a_j(2-a_j-a_{j-1})e_{j-1}
+a_ja_{j-1}e_{j-2}.
\]

한 번의 Full remap은 \((1-(1+\rho)a_j)e_j+(1+\rho)a_je_{j-1}\)다. 두 식을 빼고
\(\Delta_j(a_j-\varepsilon)=\Delta_{j-1}a_{j-1}\)를 쓰면

\[
\boxed{[\mathsf R(\rho)^2-\mathsf R(\rho^2)]e_j
=a_ja_{j-1}\left[
\frac{\Delta_{j-1}}{\Delta_j}e_j
-\left(1+\frac{\Delta_{j-1}}{\Delta_j}\right)e_{j-1}
+e_{j-2}\right].}
\tag{29}
\]

원 captured nodes의 미세한 비균일성까지 포함한 exact identity다. 계수의 합과 \(E\)-가중 합은 각각 0이다. 따라서 두 방법은 이 branch에서 광자수와 redshifted energy를 같게 보존하면서 spectral shape에서 차이가 난다. 균일 간격에서는 \(a_ja_{j-1}(e_j-2e_{j-1}+e_{j-2})\)로 줄어든다.

현재 HI threshold 근방의 좁은 node 간격에서는 \(a_j\)가 작지 않을 수 있으므로, 이 항은 실제 Full-vs-two-half 비교를 해석할 때 남길 가치가 있다. (29)의 branch 가정을 벗어나는 columns는 같은 33×33 sparse matrices를 직접 곱해 차이를 계산하면 된다. 이 차이를 gas source·birth injection·backward-Euler 길이의 변화와 분리하면 어떤 시간 세분 효과가 온도·이온화 관측량에 전달되는지 추적할 수 있다. 실제 endpoint 차이를 아직 계산하지 않은 경우 (29)는 operator-level derived 결과로 보고한다.

## 8. 구현에 필요한 최소 데이터와 연산

| 대상 | 필요한 원 데이터·연산 | 상태/역할 |
|---|---|---|
| 첫 half 입력 | 같은 COMMON의 PHYS09 gas \(g,U,V,W\), PHYS11 spectral carry 또는 원 first_half PREBE와 source quotient | 상속된 포함을 실제 연속 입력으로 사용 |
| 둘째 half 기하학 | \(H,h\), 공통 \(\rho=e^{-Hh}\)의 유효 포함, 원 33 energy leaves, source amount와 정상화 관계 | 등방 closure의 새 specialization |
| FT03·HH | 기존 Full의 nonphoto4, q, gas gradient/Hessian; 동일 endpoint stage bits; 원 \(X\) | 새 source 호출 없는 재사용 |
| Photo 값·미분 | HI sigma·heat leaves, 새 incoming 값과 \(U,V,W\), (16)–(17) | scalar 33-group 합, 실제 active는 17개 |
| 새 gas root | (15)의 strict self-map 및 scaled Jacobian contraction 또는 동등한 fixed-C 포함 | PHYS14 실제 실행으로 닫을 gate |
| 새 gas 응답 | 같은 \(A\)에 (22)–(23), 정확/외향 matrix-vector 연산 | 3개 4-vector solve; photon 33D nonlinear solve 불필요 |
| 관측량 | \(\widehat f_2,C_T\), 새 root box 및 \(U,V,W\) | PHYS13 readout을 실제 carried endpoint에 적용 |
| 추가 물리 분해 | (25)의 scalar adjoint contraction, (29)의 sparse remap difference | 가용 계산 결과만 새 수치 주장으로 보고 |

## 9. 작은 유리수 검산과 읽은 원문

`check_theory_identities.py`를 실제 실행해 다음 4개 의미 사례를 exact `Fraction` 산술로 확인했다. 결과는 `THEORY_EXACT_CHECKS.json`이며 실행 시간은 약 0.0079초다. 이는 후보 작성자의 검산으로 분류한다.

1. 서로 다른 세 ray가 signed \(U,V,W\)를 가진 경우, 공통 denominator quotient와 네 carry 성분의 합이 정확히 교환된다.
2. Inherited photon forcing과 opacity response가 동시에 존재하는 유리수 사례에서 (20)이 정확하며, 양의 photon heat source와 음의 직접 온도 source가 (24)에 따라 양립한다.
3. 비대각 baseline 행렬에 대해 (19)의 후보 inverse를 원 rank-one 갱신 행렬과 곱해 정확히 단위행렬을 얻는다.
4. 원 captured energy nodes의 \(j=10,16,24\)에 대해 (29)가 정확하고, 비영 spectral shape 차이의 number·energy moment는 정확히 0이다. 이 의미 사례의 \(\rho=1-1/160000\)은 명시적인 유리수 선택으로, 물리적 exponential을 새로 평가했다고 보고하지 않는다.

따라서 이들 항등식에는 `derived + exact-arithmetic checked`를 병기할 수 있다. 실제 다음 단계 root·온도·전자 응답은 owner 실행 결과를 별도로 따른다.

### 읽은 범위와 attribution

- Astra v4.0.0 `START_HERE.md`, `PROJECT_INSTRUCTIONS.md`, `state/RESEARCH_STATE.md` template, `docs/MODEL_ROUTING.md`, `prompts/00_integrated_work_run.md`, `policies/STOP_RULES.md`를 읽고 적용했다. Host model label은 부모가 제공한 GPT-6 Astra Pro다.
- PHYS13 `HANDOFF_KO.md` 전체와 `THERMODYNAMIC_RESPONSE_THEOREM_KO.md` §§1–3,5–10을 읽었다. 온도·전자·에너지 정의와 FTC readout은 PHYS13을 재사용한다.
- 이전 보고서 회수본 `sources/LG065.md` 전체, `LG066.md` §§1–6 및 관련 carry/ledger 부분, `LG115.md` 전체를 읽었다. 일반 carry 대수, group absorption quotient, general geometry transport, 다음 4×4 implicit chain rule은 PHYS11의 기존 결과다.
- 실제 NCP07 source `candidate/src/phys04_transport.rs`, `phys04_mixed.rs` 전체, `paired_runtime.rs`의 energy node·qhat·g_box·source_weights·hat map, `hh_primary_extension.rs::hh_rate_jet`, `coupled_primary.rs::{model,valid,interval_rhs}`, `ft03_interval.rs` 전체를 읽었다.
- 실제 `results/full/SOURCE_BOX.json`의 energy/sigma/stage leaves와 `SOURCE_BOX_COMPONENTS.json`의 nonphoto schema를 확인했다. Full HI active17, HeI/HeII exact-zero 전체33은 원 bits를 직접 해독한 결과다.
- 자료 읽기 중 PHYS13 복사본의 `first_half/NATIVE_CONSTANT_LEAVES.json` 경로가 없다는 `FileNotFoundError` 한 건을 확인했다. NCP07 원본 및 PHYS13의 Full constant leaves로 필요한 source를 읽었다. 과학 실행 실패가 아니라 자료 경로 확인 사건이다.

이 문서는 최종 독립 PROMOTE 판정을 하지 않는다. 실제 owner의 next-stage 실행이 닫은 root·response와 여기의 일반 유도만 있는 항목을 최종 보고서에서 구분한다.
