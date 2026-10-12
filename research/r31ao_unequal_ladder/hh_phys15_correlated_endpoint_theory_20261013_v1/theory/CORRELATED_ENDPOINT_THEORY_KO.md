# WU088_HH PHYS15: 동일 COMMON의 Full–two-half 결함 이론

이론 연구 시작: 2026-10-12 KST. 초안 작성: 2026-10-13 KST. 적용 규약: physmath-research-loop built-in 1.0.0, THEORY R1–R10. 본문은 PHYS14의 실제 두 번째 half를 이어받아 endpoint 결함을 구성한다. 표준 잔차·평균 Jacobian 이론 위에 이 프로젝트의 광자 chronology, 원 source 정규화, 관측량 식을 직접 유도한다.

## 1. 연구 계약과 재사용 전제

**연구 질문.** 같은 COMMON과 같은 제어변수로 시작한 길이 2h의 Full과 실제 두 번의 길이 h 단계 사이에서, 기체·광자 endpoint 차이를 공통 입력의 상관관계를 유지하여 어떤 잔차로 구성하고 T/e/w에 전달할 수 있는가?

이번 루프의 성공 조건은 (i) 실제 두 단계식에서 정확한 잔차 항등식, (ii) 시각·중간 흡수·수송·birth 작용의 분해, (iii) 기존 Full 포함을 재사용하는 유한 endpoint 전달 정리, (iv) 원 source 정규화 연결, (v) 독립 검토와 판별 대수 검산, (vi) 다음 수치 포함의 실행 계약이다. 새 물리 수치 구간은 다음 계산 단위로 지정한다.

다음 전제는 PHYS09·11·13·14의 고정 source 계열에서 상속한다.

| ID | 가정 또는 근거 | 이번 사용 |
|---|---|---|
| P1 | Full·first-half의 COMMON gas/photon/guard 및 Jet payload가 dt header를 제외하고 같다. | 동일한 g0, Z0, λ, b를 두 경로에서 공유한다. |
| P2 | PHYS14 geometric isotropic subfamily, 원 33개 node와 두 aggregate guards, 정확한 39-state closure. | R=R(ρ), RF=R(ρ²), ρ=exp(−exact(H) exact(h))를 결박한다. |
| P3 | 첫 half g1, 실제 둘째 half g2, Full gF가 같은 convex 원 source 영역 X의 내부 포함에 있다. source와 root family는 원 C² 전제를 따른다. | 연결 segment의 평균 Jacobian·source 도함수를 사용한다. |
| P4 | Full과 둘째 half는 동일 t2의 nH, stored nHe, 원자 및 열 계수와 nonphoto·HH 함수를 쓴다. | 두 endpoint에 공통 함수 B2를 쓴다. |
| P5 | 원 captured birth MF=2M이 정확하다. HI active 16–32, He photo sigma는 0이다. | 같은 J=M e24와 HI survival을 사용한다. |
| P6 | 원 Full fixed_C 및 whole-X preconditioned derivative bound가 존재한다. | 잔차를 endpoint 차이로 전달하는 정리에 재사용한다. |
| P7 | 온도는 원 source의 fhat=nHe(stored)/nH와 CT=2 eV/(3 kB)로 정의한다. | 서로 다른 normalization을 먼저 맞추고 endpoint에서는 같은 fhat2를 쓴다. |

P1·P4·P5·P7의 exact leaf 대응은 `ASSUMPTIONS_AND_BINDINGS_KO.md`, `BINDINGS.json`에 있다. P2·P3은 PHYS14의 승인 결과와 geometry/root 검토를 재사용한다. P6은 원 NCP07 Full `UNIFORM_ARITHMETIC.json`의 fixed_C 및 q를 함께 사용한다. 수치 입력의 IEEE leaves는 정확한 유리수로 해독하고, 원자 fit을 변경하지 않는다.

고정된 admissible 계수 선택 α마다 θ=(λ,b)∈[0,1]²를 두 half와 Full에 동일하게 적용한다. 과거 HH ON과 primal compensation은 공통 초기 자료에 포함된다. 이후 모든 정리는 이 같은 α, θ에 대한 pointwise 식이며, 공유 변수를 유지한 포함식은 해당 전체 계열에도 적용된다.

## 2. 상태, 단위와 단계식

기체는 g=(x,y1,y2,w)ᵀ이며 x는 HII 분율, y1,y2는 HeII·HeIII 분율, w는 eV/H다. h=625000000 s, t0=160000000000 s, t1=t0+h, t2=t0+2h다. 광자와 guard 상태는

\[
Z=(N_0,\ldots,N_{32},G_N,G_U)^T\in\mathbb R^{35}.
\]

N와 GN은 photons/H, GU는 eV/H다. R은 아래 경계로 나간 number/energy를 guards로 옮기고, 기존 guard energy에 ρ를 곱하는 원 remap이다. number와 energy row를

\[
\mathfrak n=(1,\ldots,1,1,0),\quad
\mathfrak u=(E_0,\ldots,E_{32},0,1)
\]

로 두면 nR=n, uR=ρu다. 이 공간의 서로 다른 단위를 섞은 무척도 operator norm은 사용하지 않는다.

Source 시각 k=1,2에서 a_kj=exact(c) exact(n_k) exact(σ_j), κ_kj(g)=a_kj(1−x)라 둔다. 반 단계의 survival은

\[
A_k(g)=\operatorname{diag}(1+h\kappa_{kj}(g))^{-1},\quad
L_k=I-A_k,
\]

Full에서는 AF(g)=diag(1+2hκ_2j(g))⁻¹, LF=I−AF다. Guard에서 A=1, L=0이다. 흡수 한 개의 기체 변화는 ν_j=(1,0,0,ε_j)ᵀ이며, V의 active j열은 ν_j, inactive 및 guard 열은 0이다. ε_j는 원 captured heat leaf다. 비광자 source는

\[
\mathcal B_k(g,\lambda)=F_k^{np}(g)+\lambda q_k(g)\nu_H-2H_kwe_w,
\quad\nu_H=(1,0,0,-\chi_H)^T.
\tag{2.1}
\]

M=exact(0x3eca36e2eb1c432d)=7378697629483821/2361183241434822606848, J=M e24다. MF=exact(0x3eda36e2eb1c432d)=2M. 따라서

\[
Q_1=RZ_0+bJ,\quad Z_1=A_1(g_1)Q_1,\quad P_1=L_1(g_1)Q_1,
\]
\[
Q_2=RZ_1+bJ,\quad Z_2=A_2(g_2)Q_2,\quad P_2=L_2(g_2)Q_2,
\tag{2.2}
\]
\[
Q_F=R_FZ_0+2bJ.
\tag{2.3}
\]

P는 integrated absorbed photons/H다. 실제 기체 단계는

\[
g_1-g_0=h\mathcal B_1(g_1)+VP_1,\qquad
g_2-g_1=h\mathcal B_2(g_2)+VP_2.
\tag{2.4}
\]

Full 잔차를

\[
\mathcal H_F(g)=g-g_0-2h\mathcal B_2(g)-VL_F(g)Q_F,
\quad\mathcal H_F(g_F)=0
\tag{2.5}
\]

로 고정한다. Full 잔차의 평가점 g2에서 정의한 광자는 ZhatF=AF(g2)QF, PhatF=LF(g2)QF다. 실제 Full 광자는 ZF=AF(gF)QF다. 이 두 비교점은 각각 잔차 구성과 최종 photon 차이에 사용한다.

## 3. 정리 1 — 상관된 기체 결함의 정확한 잔차

\[
p=P_1+P_2-\widehat P_F,\qquad r=\mathcal H_F(g_2)
\]

라 두면

\[
\boxed{r=h[\mathcal B_1(g_1)-\mathcal B_2(g_2)]+Vp.}
\tag{3.1}
\]

**증명.** (2.4)를 더하면 g2−g0=hB1(g1)+hB2(g2)+V(P1+P2)다. 같은 g0, QF, λ, b를 사용한 (2.5)에 대입하면 (3.1)을 얻는다. COMMON이 항등식 단계에서 소거된다. □

기체의 중간 이동도 같은 source로 묶을 수 있다. δg21=g2−g1,

\[
\delta\mathcal B_t(g)=\mathcal B_1(g)-\mathcal B_2(g),\qquad
\overline J_{12}=\int_0^1D_g\mathcal B_2(g_1+s\delta g_{21})\,ds
\]

로 두면

\[
\mathcal B_1(g_1)-\mathcal B_2(g_2)
=\delta\mathcal B_t(g_1)-\overline J_{12}\delta g_{21},
\tag{3.2}
\]
\[
\boxed{r_g=h\delta\mathcal B_t(g_1)-h\overline J_{12}
[h\mathcal B_2(g_2)+VP_2].}
\tag{3.3}
\]

이 식은 첫 시각의 source 계수 변화와 실제 기체 이동을 구분한다. δBt의 직접 구성은 §5에 있다.

## 4. 정리 2 — 광자 absorption 결함의 일곱 항

이 절의 기준점은 g2다. A=A2(g2), L=I−A, AF=AF(g2), LF=I−AF,

\[
\tau=h\operatorname{diag}\kappa_2(g_2),\quad
C_1=\tau A^2A_F,\quad C_2=\tau^2A^2A_F,
\quad\Delta A_1=A_1(g_1)-A,\quad\Delta R=R^2-R_F.
\tag{4.1}
\]

광자 C1,C2는 §6의 기체 전처리 행렬 C와 별개다. [R,A]=RA−AR로 두면

\[
\boxed{\begin{aligned}
p={}&-(I-LR)\Delta A_1Q_1
+L[R,A]Q_1+L(I-R)RZ_0\\
&+C_2R^2Z_0+L_F\Delta RZ_0
+bLA(R-I)J-bC_1J.
\end{aligned}}
\tag{4.2}
\]

| 항 | 실제로 분리한 작용 |
|---|---|
| −(I−LR)ΔA1 Q1 | 첫 stage와 endpoint 기준 opacity의 변화 |
| L[R,A]Q1 | 중간 흡수와 다음 수송의 순서 |
| L(I−R)RZ0 | 서로 다른 시점의 흡수를 해당 원 node에서 평가하는 보정 |
| C2 R²Z0 | 기존 광자의 두 half BE 흡수와 Full BE 흡수 |
| LF ΔR Z0 | 같은 COMMON spectrum의 수송 분할 |
| bLA(R−I)J | 먼저 생성된 광자의 추가 redshift |
| −bC1J | 총량이 같은 두 birth의 흡수 시점 |

**증명.** L1=L−ΔA1를 (2.2)에 넣어

\[
p=-(I-LR)\Delta A_1Q_1+LQ_1+LRAQ_1+bLJ-L_FQ_F
\]

를 얻는다. RA=AR+[R,A], Q1=RZ0+bJ를 대입하고, 각 τ≥0에 대해

\[
A^2-A_F=-C_2,\qquad A^2+A-2A_F=C_1
\tag{4.3}
\]

를 쓰면 (4.2)가 나온다. 동일 변수의 연결을 유지한 순수 대수 항등식이다. □

Opacity 변화도 작은 차이를 먼저 묶는다.

\[
\Delta A_{1,j}=h[\kappa_{2,j}(g_2)-\kappa_{1,j}(g_1)]A_{1,j}A_j,
\]
\[
\kappa_{2,j}-\kappa_{1,j}
=c\sigma_j(n_2-n_1)(1-x_2)+a_{1,j}(x_1-x_2).
\tag{4.4}
\]

### 4.1 원 격자에서의 부호 정리

PHYS14에서 확인한 원 branch는 Rej=(1−αj)ej+αj e(j−1), αj=(1−ρ)Ej/(Ej−E(j−1))다. 따라서

\[
[R,A]_{j-1,j}=\alpha_j(A_j-A_{j-1}).
\tag{4.5}
\]

원 HI σ16>σ17>⋯>σ32>0에서 active output으로 내려오는 edge는 Aj−A(j−1)≥0다. Inactive output에서는 Li=0이다. 따라서 물리적 Q1≥0, 0≤x2≤1에서

\[
\boxed{L[R,A]Q_1\ge0}
\tag{4.6}
\]

가 성분별로 성립한다. 이 항의 직접 x,w forcing은 비음수다.

두 chronology 대각 항은

\[
C_2R^2Z_0-bC_1J=C_1[\tau R^2Z_0-bJ].
\tag{4.7}
\]

Birth node 24에서 τ24(R²Z0)24와 bM의 대소가 이 항의 흡수 증가·영·감소를 판별한다. R=I, A1=A의 정확한 특수 경우에는

\[
p_j=\frac{\tau_j}{(1+\tau_j)^2(1+2\tau_j)}
(\tau_jN_{0,j}-bJ_j).
\tag{4.8}
\]

### 4.2 먼저 생성된 광자의 redshift가 이온화와 열에 주는 방향

βj=τj/(1+τj)², η=hcn2(1−x2)라 두면

\[
p_{bR}=bLA(R-I)J=bM\alpha_{24}
(\beta_{23}e_{23}-\beta_{24}e_{24}),
\tag{4.9}
\]
\[
\beta_{23}-\beta_{24}
=\frac{\eta(\sigma_{23}-\sigma_{24})(1-\eta^2\sigma_{23}\sigma_{24})}
{(1+\eta\sigma_{23})^2(1+\eta\sigma_{24})^2}.
\tag{4.10}
\]

원 captured leaves에서 (hcn2)²σ23σ24≈0.00013495931272495<1,
ε23σ23<ε24σ24와 σ23>σ24가 exact 유리수 비교로 성립한다. 따라서 b>0, x2<1, α24>0에서

\[
\boxed{\mathbf1^Tp_{bR}>0,\qquad\epsilon^Tp_{bR}<0.}
\tag{4.11}
\]

두 번째 부호는 ε23σ23의 작은 분자와 (1+ησ23)²의 큰 분모에서 나온다. 현재 g의 양의 w,Π에 대한 Tg V p_bR도 음수다. 이 직접 forcing을 endpoint로 전달한 기여는 §7의 같은 평균 inverse와 온도 covector로 정의한다.

## 5. 정리 3 — 원 source의 밀도·온도 정규화 연결

여기서 fk=exact(nHe,k stored)/exact(nk), s=y1+2y2,
ek=x+fk s, Πk=1+fk+ek, Tk=CTw/Πk다. 원 FT03 반응 graph의 인수 분해는

\[
F^{np}_{k,frac}=n_ke_k k_{frac}(x,y_1,y_2,T_k),
\]
\[
F^{np}_{k,w}=n_ke_k[k_{wH}(x,T_k)+f_k k_{wHe}(y_1,y_2,T_k)].
\tag{5.1}
\]

kfrac와 kwH,kwHe는 원 CI·RR·DR의 조합이며 완전한 정의는 근거 문서 §3.1에 있다. Photo·HH·팽창을 넣기 직전 저장한 nonphoto 함수를 대상으로 한다. HH source는 qk=nk(1−x)²kHH(Tk)다.

온도 정렬 사상을

\[
\Psi g=(x,y_1,y_2,w\Pi_2/\Pi_1),\quad
r_n=n_1/n_2,\quad r_e=r_n e_1/e_2,\quad\Delta f=f_1-f_2
\tag{5.2}
\]

로 두면 T2(Ψg)=T1(g)다. 따라서 정확히

\[
F^{np}_1(g)=r_eF^{np}_2(\Psi g)
+n_1e_1\Delta f\,k_{wHe}(T_1)e_w,
\quad q_1(g)=r_nq_2(\Psi g).
\tag{5.3}
\]

작은 차이는 다음 두 식으로 먼저 만든다.

\[
r_e-1=(r_n-1)+r_n\Delta f\,s/e_2,
\quad\delta w=\Psi_w(g)-w=-w\Delta f(1+s)/\Pi_1.
\tag{5.4}
\]

g→Ψg의 w선분 평균 도함수를 overline{Fnp_2,w}, overline{q2,w}라 두면

\[
\boxed{\begin{aligned}
F^{np}_1(g)-F^{np}_2(g)
={}&(r_e-1)F^{np}_2(g)+r_e\overline{F^{np}_{2,w}}\,\delta w\\
&+n_1e_1\Delta f\,k_{wHe}(T_1)e_w,\\
q_1(g)-q_2(g)
={}&(r_n-1)q_2(g)+r_n\overline{q_{2,w}}\,\delta w.
\end{aligned}}
\tag{5.5}
\]

원 H1=H2여서 같은 g의 팽창항은 δBt에서 소거된다. (5.5)와 λνH를 조합하면 (3.3)의 source 시각항을 얻는다. 원 실제 ratio는 Δf∈[−6.94524945677013820,−6.94524945677013819]×10⁻¹⁸다. Full·first-half·second-half의 공동 root hull에서 δw∈[1.09800931589085210,1.11069895932571596]×10⁻¹⁶ eV/H다. 이 hull, Ψ(hull) 및 연결 선분은 원 X 내부에 있다. 따라서 기존 whole-X source 도함수 포함을 적용할 수 있다.

## 6. 정리 4 — 기존 Full 검증으로 닫히는 endpoint 차이

d=g2−gF와

\[
\overline{\mathcal A}=\int_0^1D_g\mathcal H_F(g_F+s d)\,ds
\]

를 정의한다. 원 convex X 안의 선분에 대해 미적분학의 기본정리가 주는 정확한 식은

\[
\boxed{\overline{\mathcal A}d=r.}
\tag{6.1}
\]

부호는 H_F(g2)−H_F(gF)=r와 일치한다. HI photo 구조를 직접 미분하면

\[
D\mathcal H_F(g)=I-2hD\mathcal B_2(g)+2h\,v_F(g)e_x^T,
\]
\[
v_F(g)=\sum_j\frac{a_{2,j}Q_{F,j}}{[1+2h\kappa_{2,j}(g)]^2}\nu_j.
\tag{6.2}
\]

Photo 미분은 x 한 열만 가진다. 원 Full source 포함은 같은 QF·계수 계열의 (6.2)를 포함한다.

원 고정 binary64 행렬 C를 exact dyadic 행렬로 해석한다. 이것은 centre Jacobian의 실제 수치 전처리 결과이며 정확한 역행렬로 재정의하지 않는다. 원 `UNIFORM_ARITHMETIC.json`에서

\[
|I-CD\mathcal H_F(g)|\le B\quad(g\in X),\quad
S=\operatorname{diag}(\operatorname{exact}(0.015),
\operatorname{exact}(0.01),\operatorname{exact}(0.01),\operatorname{exact}(0.5)),
\]
\[
\|S^{-1}BS\|_\infty\le q,
\quad q=\operatorname{exact}(0.00011736830563768177)<1.
\tag{6.3}
\]

S는 Full 증명에 쓰인 원 radius다. PHYS14 두 번째 half의 별도 수축 척도와 구분한다. 평균 Ebar=I−C Abar도 |Ebar|≤B를 만족한다. 그러므로

\[
d=Cr+\overline E d,
\quad\widetilde B=S^{-1}BS,
\]
\[
\boxed{|S^{-1}d|\le(I-\widetilde B)^{-1}|S^{-1}Cr|,\qquad
\|S^{-1}d\|_\infty\le\frac{\|S^{-1}Cr\|_\infty}{1-q}.}
\tag{6.4}
\]

**증명.** 평균과 적분에서 B를 그대로 적분하면 Ebar의 포함이 따른다. ||S⁻¹ Ebar S||∞≤q<1이므로 I−Ebar=C Abar는 가역이다. 유한 정사각 행렬의 곱이 가역이므로 C와 Abar 모두 가역이다. Neumann 전개의 항별 절대값을 비음수 Btilde로 지배하면 두 포함을 얻는다. □

기존 q가 주는 scalar amplification은 1/(1−q)<1.000118이다. 이는 **전처리된 잔차 Cr**의 반경 척도 노름에 대한 결과다. 실제 잔차의 크기는 (3.1)–(5.5)를 평가하여 정한다.

### 포함 계산의 닫힌 절차

1. 같은 α,θ를 공유한 expression DAG에서 [r]를 구성한다. 두 광자 표현과 ledger의 공통 연결을 보존한다.
2. 원 [E]=I−C[DHF](X)와 exact S,C를 회수한다. (6.4)로 반드시 포함하는 초기 [d]를 만든다.
3. [d]←[d]∩(C[r]+[E][d])를 적용한다. 기존 [g2]−[gF]는 독립적인 유효 cap으로만 교차할 수 있다.
4. [g2]−[d]가 만든 더 좁은 Full 구간과 source Hessian을 필요할 때 사용한다. 개선은 실제로 남은 폭에 따라 선택한다.
5. 검증된 [d]를 §7에 대입해 [Δe],[Δw],[ΔT],[Δne]를 구성한다.

이 절차의 존재·가역성은 원 근 전제와 (6.3)으로 닫힌다. 다음 계산은 새 물리 root를 찾는 작업 없이 이 작은 결함의 포함을 평가할 수 있다.

## 7. 정리 5 — 유한 온도 차이와 같은 inverse의 관측량 기여

같은 endpoint f2에 대해

\[
\ell_e=(1,f_2,2f_2,0),\quad d_e=\ell_e d,\quad d_w=e_w^Td,
\quad\Delta n_e=n_2d_e,
\]
\[
\Pi_F=\Pi_2-d_e>0,\quad T_2=C_Tw_2/\Pi_2.
\]

정확한 유한 온도 차이는

\[
\boxed{T_2-T_F=\frac{C_Td_w-T_2d_e}{\Pi_2-d_e}.}
\tag{7.1}
\]

**증명.** TF=CT(w2−dw)/(Π2−de)를 T2에서 빼고 공통 분모를 취한다. □

endpoint covector를

\[
\ell_T=(C_Te_w^T-T_2\ell_e)/\Pi_F
\tag{7.2}
\]

로 두면 ΔT=ℓT d다. 같은 평균 Jacobian의 adjoint

\[
\overline{\mathcal A}^{T}z_T=\ell_T^{T}
\]

는 정확한

\[
\boxed{\Delta T=z_T^Tr,\qquad
r=\sum_sr_s\ \Longrightarrow\ \Delta T=\sum_sz_T^Tr_s}
\tag{7.3}
\]

를 준다. 각 rs는 (3.3)의 source 시각·기체 이동과 (4.2)의 광자 sector다. 모든 항에 같은 원 endpoint와 같은 inverse가 적용된다. 따라서 각 항의 endpoint 온도 기여가 하나의 전체 차이를 정확히 분할한다. 전자·열에너지·ne도 같은 방식의 covector를 쓴다. Direct gas forcing의 부호와 endpoint 기여의 부호 사이의 변환은 이 식이 담당한다.

온도 분자 CT dw−T2 de의 두 항을 같은 d와 묶어 평가한다. 두 큰 온도 포함을 독립적으로 빼는 연산에서 발생하는 입력 반복을 줄이는 구성이다. Standard residual preconditioning과 goal covector의 원리는 알려져 있으며, 여기서는 이 고정 source의 유한 차이·정확한 분모·공유 sector를 연결했다 [L1].

## 8. 정리 6 — guard ledger와 H 화학·열에너지 잔차

ΔZhat=Z2−ZhatF, ΔN=nΔZhat, ΔU=uΔZhat라 둔다. 총 birth가 같고 nR=n이므로

\[
\mathbf1^Tp=-\Delta N.
\tag{8.1}
\]

uR=ρu를 두 실제 단계에 적용하면

\[
uZ_2=\rho^2uZ_0+b(\rho+1)ME_{24}
-\rho E\cdot P_1-E\cdot P_2,
\]
\[
u\widehat Z_F=\rho^2uZ_0+2bME_{24}-E\cdot\widehat P_F.
\]

따라서

\[
\boxed{E\cdot p=(1-\rho)(E\cdot P_1-bME_{24})-\Delta U.}
\tag{8.2}
\]

원 active 17개 group의 stored heat는 εj=exact(Ej)−exact(χH)와 정확히 같다. 이번에 원 bits에서 직접 확인했고, χH≤Ej<2χH인 normal binary subtraction의 Sterbenz 조건과도 일치한다. 원 captured leaf를 유지한 상태에서 사용할 수 있는 새 항등식이다. 따라서

\[
\epsilon\cdot p=(1-\rho)(E\cdot P_1-bME_{24})-\Delta U+\chi_H\Delta N.
\tag{8.3}
\]

H 화학·열에너지 covector ℓH=(χH,0,0,1)에 대해 ℓHνj=Ej, ℓHνH=0이다. 따라서

\[
\boxed{\ell_Hr=h\ell_H[\mathcal B_1(g_1)-\mathcal B_2(g_2)]
+(1-\rho)(E\cdot P_1-bME_{24})-\Delta U.}
\tag{8.4}
\]

이 사영은 χHx+w의 잔차다. HH의 직접 qνH는 소거되고, HH가 실제 상태·opacity·흡수·nonphoto source에 전달한 변화가 나머지 항에 유지된다. Helium의 nonphoto 열 기여도 원 벡터에 포함된다. 첫 absorption을 둘째 redshift 이후에 놓으면 (8.2)의 (1−ρ)E·P1 항이 달라지므로, ledger는 시간 순서를 판별하는 별도의 정확한 관계다.

## 9. 실제 photon endpoint 차이의 회수

잔차 기준 photon 차이는

\[
\begin{aligned}
\Delta\widehat Z={}&AR\Delta A_1Q_1+A[R,A]Q_1-C_2R^2Z_0
+A_F\Delta RZ_0\\
&+bA^2(R-I)J+bC_1J.
\end{aligned}
\tag{9.1}
\]

실제 Full과의 차이 ΔZ=Z2−ZF는

\[
\boxed{\Delta Z_j=\Delta\widehat Z_j+
\frac{2h a_{2,j}Q_{F,j}}{D_{F,j}(g_2)D_{F,j}(g_F)}d_x,
\quad 0\le j\le32.}
\tag{9.2}
\]

여기서 DF,j(g)=1+2hκ2j(g), 두 guard의 차이는 ΔZhat와 같다. 실제 AF(g2)−AF(gF)의 resolvent identity에서 부호 +가 나온다. 식 (9.2)는 §6에서 얻은 같은 dx를 사용한다. 임의 비교점의 대안 전개는 광자 분과 원고 §8에 있다.

## 10. 판별 사례와 실제 수행 범위

광자 exact Fraction 및 네-slot 산술의 독립 구현은 39개 관계·3148개 scalar equality를 통과했다. Transparent limit, stock만 있는 경우, birth만 있는 경우, 첫 opacity 변화, 순서가 다른 remap/absorption, 두 guards의 number/energy chronology를 포함한다. Manufactured spectrum과 parameter Jet에 대한 대수 검산이며, 원 captured leaves의 역할과 시험용 rational 상태를 결과 JSON에서 구분한다.

원 leaf 검사는 HI cross section의 strict monotonicity, active 17개 captured heat identity, birth-redshift 부호 조건을 exact 정수비 비교로 확인했다. 추가 gas·source bridge 검산과 독립 심사의 결과는 `checks/`와 `review/`에 붙인다. 새로운 physical source callback·root·history 실행은 이 이론 단위에서 0회다.

## 11. 결정과 다음 열린 계산

이번 이론의 새 내용은 (3.1)–(9.2)다. 특히 같은 COMMON의 잔차에서 시작하여 (6.4)의 포함과 (7.1)의 유한 온도 차이까지 하나의 계산 가능한 사슬을 구성했다. 원 source의 미소 fhat 차이를 δBt에 유지했고, 광자 분할의 개별 작용에 대해 부호와 ledger 관계를 얻었다.

후속 계산의 이름은 **HH_CORRELATED_ENDPOINT_ENCLOSURE**다. 입력은 이 원고의 expression DAG, 원 근/carry/source 포함, 정확한 C·S와 같은 COMMON이다. 출력은 r, d, ΔT/e/w/ne, 같은 inverse로 전달된 sector별 기여, 실제 ΔZ의 검증 구간이다. 먼저 재사용된 자료로 실제 폭을 측정하고, 유의미한 폭의 원인이 되는 관계만 추가로 다듬는다. 독립 심사 이후 이론 node를 derived로 승격하고, 수치 node는 이 계산 계약에 연결한다.

## 참고 근거

[L1] S. M. Rump, *Verification methods: Rigorous results using floating-point arithmetic*, Acta Numerica 19 (2010), 287–449. https://www.tuhh.de/ti3/paper/rump/Ru10.pdf. 표준 interval dependency, preconditioning, slopes/nonlinear verification의 배경. 프로젝트의 단계식·source 인수 분해·광자 sector는 본문의 직접 유도다.

[I1] PHYS14 승인 Git head 087a16f28d0ee4fc7ae74ae50bfcafe578716e85, PR49; source-aligned 39-state theory, 실제 두 번째 half 결과, geometry 및 decision.

[I2] NCP07 원 archive SHA256 4ea6b7dbbc714493ac85f944a65a353a1ee75abf5742c3e7ce65a7df56cc3465; Full/first-half source, COMMON, birth, 원 fixed_C. Drive 및 Dropbox의 원 이력 식별자는 evidence manifest에 기록한다.

[I3] PHYS09 projected source/root sensitivity, PHYS11 joint first-half carry, PHYS13 thermodynamic readout 및 원 root images. 각 원 bytes 및 적용범위는 BINDINGS와 PHYS14 입력 manifest를 재사용한다.
