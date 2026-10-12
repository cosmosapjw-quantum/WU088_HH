# PHYS16 — Endpoint Jacobian과 2차 remainder에 의한 관측량 포함

## 1. 대상과 재사용 범위

PHYS15에서 얻은 동일 COMMON의 정확한 잔차를 재사용하여, 알려지지 않은 평균 Jacobian 및 그 adjoint를 endpoint에서 계산 가능한 유한식과 명시적 remainder로 옮긴다. 고정 admissible coefficient 선택 α마다 같은 θ=(λ,b)∈[0,1]²를 Full과 두 half에 공유한다. 실제 two-half endpoint를 y=g₂, 기존 Full 근을 g_F, 차이를 d=y−g_F라 쓴다. 모든 식은 이 같은 α,θ에 대해 점별로 성립하며, 포함 계산은 공유 의존성을 유지한 계열 전체를 대상으로 한다.

PHYS15의 정확식과 원 수축 증명은 다음과 같다.

\[
r=H_F(y),\qquad H_F(g_F)=0,\qquad
\overline A d=r,
\tag{1.1}
\]
\[
H_F(g)=g-g_0-2hB_2(g)-V L_F(g)Q_F,
\qquad
\overline A=\int_0^1DH_F(y-sd)\,ds,
\tag{1.2}
\]
\[
|I-CDH_F(g)|\le B,\qquad
\|S^{-1}BS\|_\infty\le q<1,\qquad g\in X.
\tag{1.3}
\]

원 고정 dyadic C와 S=diag(exact64(0.015),exact64(0.01),exact64(0.01),0.5)를 그대로 사용한다. q의 원 bits는 `3f1ec474231fbe16`이며, q=exact64(0.00011736830563768177)이다. C·B·q·S의 원본은 동일한 `UNIFORM_ARITHMETIC.json`이다. 원 X는 convex이고 H_F는 그 근방의 고정 실수 source 계열에서 C²다. y와 g_F 및 필요한 연결 선분은 X에 포함된다.

이 문서의 새로운 작업은 (i) endpoint J=DH_F(y)의 보정식을 닫고, (ii) 유한 Neumann 다항식의 오차를 2차 source remainder와 함께 포함하며, (iii) 하나의 근사 adjoint로 모든 sector의 관측량 기여와 부호 여유를 판정하는 것이다. 실제 상관 잔차 [r]의 계산과 그 결과의 수치 대입은 같은 PHYS16의 residual 구성에 연결한다.

### 좌표와 단위

기체 좌표는 원 affine chart g=(x,y₁,y₂,w)이며 w의 단위는 eV/H다. h=625000000 s이고 Full 시간은 2h다. H_F의 각 성분은 해당 기체 좌표와 같은 단위를 가진다. 원 Hessian H^a_{,bc}의 단위는 [g^a]/([g^b][g^c])다. S를 사용한 모든 노름은 이 혼합 단위를 제거한 반경 척도 노름이다.

아래 tensor 표기는 이 affine 상태 공간과 상수 단위 변환을 대상으로 한다. 온도 T(g)는 이 공간 위의 관측량으로 합성한다. 배경 시공간의 metric을 상태 공간에 도입할 필요가 없다.

## 2. Endpoint Taylor 항등식

J=DH_F(y)로 두고, 선형사상 K(d)와 벡터 R₂(d)를

\[
K(d)\,v:=\int_0^1(1-s)
D^2H_F(y-sd)[d,v]\,ds,
\qquad R_2(d):=K(d)d
\tag{2.1}
\]

로 정의한다. 그러면 다음 세 식이 정확히 성립한다.

\[
\boxed{\overline A=J-K(d)},\qquad
\boxed{Jd=r+R_2(d)},\qquad
\boxed{d=Cr+(I-CJ)d+C R_2(d)}.
\tag{2.2}
\]

**증명.** s에 대해 J(y−sd)를 적분하고, 그 미분을 다시 적분하면

\[
\int_0^1J(y-sd)\,ds
=J(y)-\int_0^1(1-s)D^2H_F(y-sd)[d,\cdot]\,ds.
\]

따라서 첫 식이 나온다. 이를 PHYS15의 \(\overline A d=r\)에 대입하면 둘째 식이고, 왼쪽에 C를 곱하면 셋째 식이다. 동등하게 Taylor 적분형

\[
0=H_F(y-d)=r-Jd+R_2(d)
\]

를 직접 사용할 수 있다. y에서 g_F로 가는 변화가 −d이므로 Jd=r+R₂의 부호는 +다. □

이 정리는 C²만 사용한다. R₂가 2차로 제어되고 K가 d의 1차로 제어되는 것은 다음 절의 실제 Hessian 포함에서 정량화된다.

## 3. HI opacity의 remainder를 유리식으로 적분한다

각 group j에서

\[
\ell_j=2h a_{2j}=2hcn_{H,2}\sigma_j,
\quad D_j=1+\ell_j(1-x_2),
\quad D_{Fj}=D_j+\ell_jd_x
\tag{3.1}
\]

로 둔다. ℓ_j는 무차원이고, D_j와 D_Fj는 각각 y와 g_F에서의 Full denominator다. ν_j=(1,0,0,ε_j)ᵀ, Q_j=Q_F,j를 사용하면 잔차의 photo 부분은 상수항을 제외하고

\[
H_{\rm ph}(g)=\sum_j \frac{Q_j\nu_j}{1+\ell_j(1-x)}
+\text{g에 독립인 항}
\tag{3.2}
\]

이다. 따라서

\[
J_{\rm ph}(y)=\sum_j\frac{\ell_jQ_j}{D_j^2}\nu_j e_x^T,
\quad
\overline A_{\rm ph}=\sum_j\frac{\ell_jQ_j}{D_jD_{Fj}}\nu_j e_x^T,
\tag{3.3}
\]
\[
\boxed{
K_{\rm ph}(d)=
\left[\sum_j\frac{\ell_j^2Q_jd_x}{D_j^2D_{Fj}}\nu_j\right]e_x^T,
\qquad
R_{2,\rm ph}(d)=
\sum_j\frac{\ell_j^2Q_jd_x^2}{D_j^2D_{Fj}}\nu_j.
}
\tag{3.4}
\]

**증명.** 각 분모가 선형인 점을 이용하여

\[
\frac1{D+\ell d}-\frac1D+\frac{\ell d}{D^2}
=\frac{\ell^2d^2}{D^2(D+\ell d)},
\tag{3.5}
\]

를 적용하면 R₂ 식을 얻는다. 또한

\[
\frac{\ell Q}{D^2}-\frac{\ell Q}{D(D+\ell d)}
=\frac{\ell^2Qd}{D^2(D+\ell d)}
\]

가 K 식을 준다. 이 값은 정확한 평균 Jacobian의 적분과 일치한다. □

원 physical family의 Q_j≥0 및 양의 분모에서 R₂,ph의 x,w 성분은 비음수다. 이 구조는 d_x의 부호를 몰라도 보존되며, 구간 [d_x]가 0을 포함할 때 실제 제곱 구간을 사용하여 하한 0을 유지할 수 있다. HI inactive group과 두 guard에는 ℓ_j=0이다. 고정 33개 group과 17개 HI 활성 group을 원 정의 그대로 합산한다.

Nonphoto·HH·팽창 항의 2차 remainder는

\[
R_{2,B}(d)=-2h\int_0^1(1-s)D^2B_2(y-sd)[d,d]\,ds.
\tag{3.6}
\]

\(B_2=F^{\rm np}_2+\lambda q_2\nu_H-2H_2w e_w\)이므로

\[
D^2B_2=D^2F^{\rm np}_2+\lambda\nu_H\otimes D^2q_2.
\tag{3.7}
\]

팽창항의 Hessian은 0이다. 원 `SOURCE_BOX_COMPONENTS.json::nonphoto`와 `SOURCE_BOX.json::q`의 signed gas Hessian으로 (3.6)을 포함할 수 있다. \(\widehat H_B(d)=2\int_0^1(1-s)D^2B_2(y-sd)ds\)라 쓰면

\[
R_{2,B}=-h\widehat H_B[d,d],
\qquad K_B=-h\widehat H_B[d,\cdot],
\qquad \widehat H_B(d)\in[D^2B_2](X).
\tag{3.8}
\]

전체 R₂=R₂,B+R₂,ph이며, 전체 signed Hessian을 사용하는 포함과 교차할 수 있다. Photo 부분에는 (3.4)를 우선 사용하면 one-column 구조와 제곱의 부호가 유지된다.

## 4. 원 Hessian의 의미와 실제 얻은 상계

`SOURCE_BOX.json::G_gg`는 원 source RHS가 아니라 H_F의 gas Hessian을 저장한다. 원 코드에서의 대응은 다음과 같다.

1. `candidate/src/phys04_mixed.rs::phys04_reduced_residual`은 FT03 nonphoto를 저장한 다음 λqν_H, 각 eliminated photo rate, −2Hwe_w를 결합하여 `f`를 만든다.
2. 같은 함수의 `residual`은 각 성분에서 `gas-old-dt*f`다. 원 Full CLI의 dt는 1.25e9 s=2h다.
3. `src/sourcebox.rs::export`는 `x.residual[i].gradient[j]`를 `A_Gg`, `x.residual[i].hessian[a][b]`를 `G_gg`로 직접 저장한다.
4. 원 `source_stage`는 gas slots 0–3, λ slot 4와 b slot 5를 사용하고 두 매개변수 범위를 모두 [0,1]로 설정한다. PHYS15의 고정 α geometric family는 상속된 whole-X source 포함의 해당 부분계열이다.

따라서 G_gg에는 이미 −2h source Hessian과 HI photo Hessian이 포함돼 있다. (3.7)의 source Hessian으로 따로 구성할 때는 −2h를 곱하고, G_gg 자체를 쓸 때는 원 저장값을 그대로 사용한다.

직접 읽은 원본의 식별자는 다음과 같다.

| 원 자료 | SHA256 |
|---|---|
| NCP07 `candidate/src/phys04_mixed.rs` | `0fa10fdea11cb24aa1a191a2ea81cf4c8442299fde7278a191553b42a26585d3` |
| NCP07 `src/sourcebox.rs` | `d771968e9c12c0cce5a9e3ec5fa7311d0040ac63d1f4f4a6f54f048972f674ae` |
| Full `UNIFORM_ARITHMETIC.json` | `3cf8c86b445ba2be2889e5effbdaacbcf84d0dcedbabd60763124141dfbc09af` |

원 exact dyadic endpoint로 signed preconditioning을 먼저 수행하여

\[
\mathcal T_{ijk}:=
\frac{s_js_k}{s_i}\sum_a C_{ia}[D^2H_F]^a_{jk}(X),
\quad
L_H:=\max_i\sum_{j,k}\operatorname{mag}(\mathcal T_{ijk})
\tag{4.1}
\]

를 계산했다. 여기서 mag([l,u])=max(|l|,|u|)다. 임의 u,v에 대해

\[
\|S^{-1}C D^2H_F(g)[Su,Sv]\|_\infty
\le L_H\|u\|_\infty\|v\|_\infty.
\tag{4.2}
\]

실제 exact rational 집계 결과는

\[
L_H\in
[8.27802481433761309,8.27802481433761310]\times10^{-5}.
\tag{4.3}
\]

이 수는 원 저장된 Hessian의 포함 폭까지 포함한 상계다. 실제 endpoint 차이나 새 물리 실행을 입력으로 하지 않는다. 실제 코드와 모든 exact rational은 `checks/endpoint/read_endpoint_hessian_bounds.py`, `checks/endpoint/ENDPOINT_HESSIAN_READOUT.json`에 있다.

## 5. Endpoint 선형 전달의 2차 오차

\(\|v\|_S:=\|S^{-1}v\|_\infty\), \(\kappa=(1-q)^{-1}\)로 쓴다. 기존 PHYS15 포함에서 a≥||d||_S를 확보하면

\[
\|S^{-1}C K(d)S\|_\infty\le\tfrac12L_Ha,
\qquad
\|C R_2(d)\|_S\le\tfrac12L_Ha^2.
\tag{5.1}
\]

J 역시 (1.3)을 만족하므로 J는 가역이다. Endpoint Newton 예측값 d_*=J⁻¹r에 대해

\[
\boxed{
\|d-d_*\|_S
\le\frac{L_H}{2(1-q)}a^2.
}
\tag{5.2}
\]

**증명.** d−d_*=J⁻¹R₂이고 \(J^{-1}=(I-M)^{-1}C\), M=I−CJ다. 원 q 상계에 따른 Neumann series로 \(\|(I-M)^{-1}\|_S\le\kappa\)다. 여기에 (5.1)을 적용한다. □

원 입력으로 얻은 계수는

\[
\frac{L_H}{2(1-q)}
\in[4.13949825306495892,4.13949825306495893]\times10^{-5}.
\tag{5.3}
\]

이 정리는 PHYS15가 확보한 수축 majorant를 재사용하여 평균 Jacobian을 endpoint Jacobian으로 바꿀 때의 오차를 정량화한다. 실제 [r]에서 얻은 a를 대입하면 이 오차가 그 결함 크기의 2차임을 수치 포함으로 표현할 수 있다.

## 6. 같은 C를 쓰는 유한 Neumann 예측값

M=I−CJ와

\[
P_m(M)=I+M+\cdots+M^m,
\qquad v_m=P_m(M)Cr
\tag{6.1}
\]

를 정의한다. 행렬 역산 없이 다음의 닫힌 포함을 얻는다.

\[
\boxed{
\|d-v_m\|_S\le
\varepsilon_m(a):=
q^{m+1}a+\frac{L_Ha^2}{2}\sum_{k=0}^m q^k.
}
\tag{6.2}
\]

**증명.** (2.2)를 m+1번 대입하면 정확히

\[
d=v_m+P_m(M)C R_2(d)+M^{m+1}d.
\tag{6.3}
\]

각 항에 원 weighted norm과 (5.1)을 적용하면 (6.2)가 나온다. □

현재 q는 q²<1.378×10⁻⁸, q³<1.617×10⁻¹²를 만족한다. 따라서 m=2의 세 항 I+M+M²에서 linear tail은 1.617×10⁻¹²a보다 작다. m을 늘릴 때는 이 선형 tail이 목표 폭에 미치는 크기와 이미 남은 Hessian 항을 비교한다. 예를 들어

\[
q^{m+1}a\le\eta_{\rm lin}
\tag{6.4}
\]

를 만족하는 최소 m을 선택하고, \(\eta_{\rm lin}\)을 관측량 오차 예산이나 (6.2)의 2차 항에 맞출 수 있다. a=0이면 d=0이므로 v=0으로 즉시 닫힌다.

### 원 centre export에서 J(y)를 포함하는 식

원 gas centre c=(0.915,0.3,0.6,13.5), J_c=DH_F(c)를 사용하면

\[
J(y)=J_c+\int_0^1D^2H_F(c+t(y-c))[y-c,\cdot]\,dt.
\tag{6.5}
\]

따라서 저장된 `SOURCE_CENTRE.json::A_Gg`, whole-X G_gg와 실제 [y]로 [J(y)]를 포함할 수 있다. (6.5)의 적분 가중치는 1이며, (2.1)의 1−s와 구별된다. 이를 whole-X `A_Gg` 포함과 교차하고 동일한 C로 [M]을 만들면 (6.1)의 유한 다항식을 실제 interval arithmetic으로 평가할 수 있다.

계열 점별로 같은 M과 r를 공유하는 v_m을 정의한 후 그 포함을 계산한다. 잔차의 각 sector에는 같은 M을 사용한다. 원 centre export 자체가 whole Θ를 포함하므로 새 θ-centre source callback을 선행 조건으로 요구하지 않는다.

## 7. 유한 온도 차이의 분자와 계산 가능한 adjoint

PHYS15의 최종 시각 정규화를 재사용한다.

\[
\ell_e=(1,f_2,2f_2,0),\quad
\Pi_F=\Pi_2-\ell_e d>0,\quad
n_T=C_Te_w^T-T_2\ell_e.
\tag{7.1}
\]

n_T는 행 covector이고, N_T=n_Td의 단위는 K다. 정확한 온도 차이는

\[
\Delta T=\frac{N_T}{\Pi_F}.
\tag{7.2}
\]

임의로 계산한 열벡터 \(\widetilde z\)에 대해 endpoint adjoint 잔차를

\[
\eta^T=n_T-\widetilde z^TJ
\tag{7.3}
\]

로 두면

\[
\boxed{
N_T=\widetilde z^Tr+\eta^Td+\widetilde z^TR_2(d).
}
\tag{7.4}
\]

이는 (2.2)를 왼쪽에서 \(\widetilde z^T\)로 수축한 식이다. 근사 adjoint의 실제 선형 잔차와 source의 비선형 remainder가 모두 명시되어 있다.

특히

\[
\widetilde z_m^T=n_TP_m(M)C
\tag{7.5}
\]

를 택하면

\[
\eta_m^T=n_TM^{m+1},\quad
\|\eta_m^TS\|_1\le b_Tq^{m+1},\quad
b_T:=\|n_TS\|_1.
\tag{7.6}
\]

또한 \(\widetilde z_m^Tr=n_Tv_m\)이므로

\[
\boxed{|N_T-\widetilde z_m^Tr|\le b_T\varepsilon_m(a).}
\tag{7.7}
\]

T₂>0, f₂>0에서

\[
b_T=T_2(s_x+f_2s_{y_1}+2f_2s_{y_2})+C_Ts_w.
\tag{7.8}
\]

원 positive T₂와 f₂ 포함으로 b_T의 scalar upper bound를 바로 계산할 수 있다. N_T의 하한이 0보다 크면 ΔT>0이고, 상한이 0보다 작으면 ΔT<0이다. 이 판정은 같은 양의 Π_F에 대한 유한 관측량 판정이다.

### 예측값의 온도를 직접 사용하는 형태

v가 주어진 예측값이고 e=d−v, Π_v=Π₂−ℓ_e v>0,

\[
T_v=\frac{C_T(w_2-v_w)}{\Pi_v},
\qquad \Delta T_v=T_2-T_v
\]

라 두면 또 하나의 정확식은

\[
\boxed{
\Delta T-\Delta T_v
=\frac{(C_Te_w^T-T_v\ell_e)e}{\Pi_v-\ell_e e}.
}
\tag{7.9}
\]

따라서 v=v_m을 넣고 ε_m으로 e를 포함하면, 알려진 양의 Π_F 하한에 대해

\[
|\Delta T-\Delta T_v|
\le
\frac{\|(C_Te_w^T-T_v\ell_e)S\|_1}{\inf\Pi_F}
\,\varepsilon_m(a).
\tag{7.10}
\]

전자 수와 열에너지는 각각 ℓ_e와 e_w를 사용한 선형 readout으로 같은 e를 전달한다.

## 8. 공통 sector attribution과 부호 여유

PHYS15의 물리적 sector 분해 r=Σ_s r_s를 유지한다. 같은 평균 Jacobian으로

\[
d_s=\overline A^{-1}r_s,
\qquad N_s=n_Td_s,
\qquad \Delta T_s=N_s/\Pi_F
\tag{8.1}
\]

를 정의하면 Σ_s d_s=d, Σ_s N_s=N_T, Σ_s ΔT_s=ΔT다. 각 sector의 평균 Jacobian과 유한 온도 분모가 공통이다.

임의 \(\widetilde z\)와 (7.3)의 η에 대해

\[
\boxed{
N_s-\widetilde z^Tr_s
=\bigl[\eta^T+\widetilde z^TK(d)\bigr]d_s.
}
\tag{8.2}
\]

**증명.** n_T−\(\widetilde z^T\overline A\)=ηᵀ+\(\widetilde z^TK\)이고, \(\overline A d_s=r_s\)이므로 성립한다. □

\(c_s=\|Cr_s\|_S\)라 두면 기존 majorant에서 ||d_s||_S≤κc_s다. \(\widetilde z=\widetilde z_m\)의 경우 (4.2), (7.5)로

\[
\|\widetilde z_m^TK(d)S\|_1
\le\frac{b_TL_Ha}{2}\sum_{k=0}^m q^k.
\tag{8.3}
\]

따라서 계산 가능한 sector 오차는

\[
\boxed{
|N_s-\widetilde z_m^Tr_s|
\le E_s:=
\kappa c_s b_T\left[
q^{m+1}+\frac{L_Ha}{2}\sum_{k=0}^m q^k
\right].
}
\tag{8.4}
\]

포함 계산에서 \([\widetilde z_m^Tr_s]=[L_s,U_s]\), \(E_s\le\widehat E_s\)를 얻었다면

\[
L_s>\widehat E_s\ \Longrightarrow\ \Delta T_s>0,
\qquad
U_s<-\widehat E_s\ \Longrightarrow\ \Delta T_s<0.
\tag{8.5}
\]

이 여유는 sector forcing c_s와 전체 결함 a를 구별한다. 큰 sector들이 서로 소거하여 전체 r가 작아지는 경우에도 (8.4)는 같은 전체 endpoint를 기준으로 성립한다. 잔차별로 별도의 비선형 기체 상태를 만들지 않고, 한 번의 [M] 및 근사 adjoint 구성으로 모든 sector를 처리할 수 있다.

더 날카로운 포함은 (8.2)에 (3.4), (3.8)을 직접 대입하여 얻는다. 특히 \(\widetilde z^T\nu_j=\widetilde z_x+\epsilon_j\widetilde z_w\)를 먼저 합성하면 photo energy와 ionization의 결합을 유지할 수 있다.

### 8.1 평균 adjoint 자체의 성분 부호를 포함한다

\(\overline z^T=n_T\overline A^{-1}\),
\(c_C=\|S^{-1}CS\|_\infty\)로 두면 (8.2)의 covector 잔차에서

\[
(\overline z-\widetilde z_m)^T
=\bigl[\eta_m^T+\widetilde z_m^TK\bigr]\overline A^{-1}.
\]

\(\overline A^{-1}=(I-\overline E)^{-1}C\)와 원 q를 사용하여

\[
\boxed{
\|(\overline z-\widetilde z_m)^TS\|_1
\le \Theta_z:=\kappa c_C b_T\left[
q^{m+1}+\frac{L_Ha}{2}\sum_{k=0}^m q^k\right].
}
\tag{8.6}
\]

따라서 각 성분에서 \(|\overline z_i-\widetilde z_{m,i}|\le\Theta_z/s_i\)다. 이 작은 오차를 계산한 endpoint adjoint 포함에 더하면 실제 평균 adjoint의 부호 및 \(\overline z^T\nu_j\)의 부호를 판정할 수 있다.

### 8.2 두 birth sector의 endpoint 온도 부호

원 PHYS15 정의 \(\beta_j=\tau_j/(1+\tau_j)^2\),
\(\tau_j=hcn_{H,2}\sigma_j(1-x_2)\)를 사용한다. 고정 common endpoint의 numerator 평균 adjoint가

\[
\overline z_x<0,\qquad \overline z_w>0
\tag{8.7}
\]

를 만족하고, 원 leaf의 \(\beta_{23}-\beta_{24}>0\),
\(\epsilon_{23}\beta_{23}-\epsilon_{24}\beta_{24}<0\)를 적용하면

\[
\frac{\Delta T_{bR}}{b}
=\frac{M\alpha_{24}}{\Pi_F}
\left[(\beta_{23}-\beta_{24})\overline z_x
+(\epsilon_{23}\beta_{23}-\epsilon_{24}\beta_{24})\overline z_w\right]<0.
\tag{8.8}
\]

이는 b>0에서의 실제 endpoint 온도 attribution이다. b=0에서는 그 sector가 정확히 0이다. 또한

\[
\overline z^T\nu_{24}<0
\quad\Longrightarrow\quad
\frac{\Delta T_{bBE}}b
=-\frac{MC_{1,24}}{\Pi_F}\overline z^T\nu_{24}>0.
\tag{8.9}
\]

현재 원 root 영역에서는 x₂<1, α₂₄>0, M>0이므로 필요한 양성성이 유지된다. 매개변수 b에 대한 미분 대신 PHYS15에서 정의한 same-endpoint 잔차 두 항의 attribution을 b로 인수 분해한 식이다.

수치 포함에서도 두 가까운 양의 항을 직접 빼기 전에 작은 차이를 만든다. η=hcn₂(1−x₂), A=ε₂₃σ₂₃, B=ε₂₄σ₂₄라 두면

\[
\epsilon_{23}\beta_{23}-\epsilon_{24}\beta_{24}
=\frac{\eta\bigl[(A-B)+2\eta(A\sigma_{24}-B\sigma_{23})
+\eta^2(A\sigma_{24}^2-B\sigma_{23}^2)\bigr]}
{(1+\eta\sigma_{23})^2(1+\eta\sigma_{24})^2}.
\tag{8.10}
\]

원 leaf는 대괄호의 세 계수가 모두 음수임을 만족한다. 이 구조와 (8.7)을 사용하면 계열 b∈[0,1]의 경계 0과 내부 strict sign을 함께 보존한다.

## 9. 포함 갱신과 정지 기준

PHYS15가 확보한 초기 포함 D₀와 그 반경 a₀를 사용한다. 새 연구의 포함 절차는 다음과 같다.

1. 같은 표현 DAG에서 [r]와 sector [r_s]를 구성하고, 원 C,B,q,S로 D₀와 a₀를 얻는다. 이 전이는 PHYS15의 채택된 정리를 그대로 사용한다.
2. (6.5)와 원 whole-X A_Gg를 교차해 [J(y)] 및 [M]을 구성한다. 같은 λ,b와 원 fixed α를 각 표현에 공유한다.
3. 필요한 최소 m에서 [v_m]을 계산하고
   \[
   D_1=D_0\cap\bigl([v_m]+S[-\varepsilon_m(a_0),\varepsilon_m(a_0)]^4\bigr)
   \tag{9.1}
   \]
   로 갱신한다.
4. 폭의 원인이 source curvature라면 (3.4), (3.8)의 [R₂(D₁)]를 만들고
   \[
   D_{k+1}=D_k\cap\{C[r]+[M]D_k+C[R_2(D_k)]\}
   \tag{9.2}
   \]
   를 적용한다. 원 H_F의 전체 signed Hessian을 사용한 포함과 교차할 수 있다. 모든 평가 선분의 hull이 X 안에 있고 분모가 양수임을 포함으로 확인한다.
5. 같은 D와 근사 adjoint로 [N_T], Π_F, [ΔT] 및 (8.4)의 sector 여유를 계산한다.

각 교차는 기존의 참된 d 포함을 보존한다. 유효한 두 포함의 교차가 비면 입력 대응·연산 또는 식의 구현을 해당 전이에서 확인한다. 원 실수 함수

\[
\Phi(d)=Cr+(I-CJ)d+C R_2(d)=d+C H_F(y-d)
\tag{9.3}
\]

의 미분은 \(D\Phi(d)=I-CDH_F(y-d)\)이므로 적용 영역에서 원 q의 contraction을 만족한다. 실제 interval expression의 폭에는 평가 의존성이 더해지므로, 각 갱신에서 관측된 폭 감소를 기록한다.

**정지 기준.** 목표가 부호이면 (8.5) 또는 total N_T의 strict sign margin이 닫힐 때 종료한다. 목표가 절대 포함 폭이면 사용자가 정한 온도·전자·열에너지 목표 폭과 (7.7), (7.10)의 remainder를 비교한다. Linear tail이 이미 remainder 예산보다 작고 다음 교차가 관심 관측량의 폭을 줄이지 못하면, 실제 폭을 지배하는 입력 표현을 지정하고 해당 구간을 결과로 보존한다. m 증가·old source 재실행은 그 잔여 원인에 기여하는 경우에 선택한다.

## 10. Affine tensor 형태와 검산할 항등식

상수 affine 변환 g=c+Su에서 residual도 \(\widehat H(u)=S^{-1}H(c+Su)\)로 정의하면

\[
\widehat d=S^{-1}d,\quad
\widehat r=S^{-1}r,\quad
\widehat J=S^{-1}JS,\quad
\widehat C=S^{-1}CS,
\tag{10.1}
\]
\[
\widehat H^a{}_{,bc}=(S^{-1})^a{}_iH^i{}_{,jk}S^j{}_bS^k{}_c,
\qquad \widehat n=nS.
\tag{10.2}
\]

따라서 \(n_ad^a=\widehat n_a\widehat d^a\), \(\widehat C\widehat J=S^{-1}CJS\)이며 모든 포함 노름의 unit mapping이 일치한다. Hessian의 마지막 두 index는 원 C²와 affine chart에서 대칭이다.

Wolfram/xAct로 확인할 최소 항등식은 다음과 같다.

- Taylor 전이: \(r^a=J^a{}_bd^b-R_2^a\), \(R_2^a=K^a{}_bd^b\), \(\overline A^a{}_b=J^a{}_b-K^a{}_b\)를 대입한 \(\overline A d-r=0\).
- Adjoint: \(\eta_b=n_b-z_aJ^a{}_b\)를 대입한 \(n_bd^b-z_ar^a-\eta_bd^b-z_aR_2^a=0\).
- Sector: \(\overline A d_s=r_s\)에서 \(n_bd_s^b-z_ar_s^a-(\eta_b+z_aK^a{}_b)d_s^b=0\).
- HI rank one: \(D_{Fj}=D_j+\ell_jd_x\)에서 (3.5) 및 (3.3)–(3.4)의 resolvent 차이.
- Finite temperature: (7.9)의 양변을 원 \(T=C_Tw/\Pi\)에 대입한 차이 0.
- Affine scaling: (10.1)–(10.2)의 covector-vector contraction과 mixed-index matrix product 보존.

이 문서의 정리는 직접 유도된 결과다. 실제 원 Hessian의 exact arithmetic 집계는 별도 JSON에 기록했으며, 독립 검토와 Wolfram/xAct의 실제 결과는 PHYS16의 해당 검산 기록에 연결한다.

## 11. 실제 PHYS16 잔차 포함에 대한 적용

같은 단위의 `checks/application/run01/results/CORRELATED_DEFECT_RESULTS.json`이 계산한 D를 원 S로 정규화하면

\[
a=\max_i\frac{\operatorname{mag}([d_i])}{s_i}
\in[4.283196217660631,4.283196217660632]\times10^{-6}.
\tag{11.1}
\]

이 D는 같은 COMMON의 source 시각·기체 이동·광자 일곱 항으로 조립한 r에서 나온 실제 계열 포함이다. 해당 원 입력과 물리적 source 계열의 독립 판정은 PHYS16의 공통 검토에 연결한다. 본 절은 그 실제 D와 원 Hessian을 입력으로 새 이론의 오차를 exact rational interval arithmetic으로 계산한 결과다.

| 판별량 | 검증된 상계 |
|---|---:|
| \(\|d-J(y)^{-1}r\|_S\) | \(7.594228219959920\times10^{-16}\) |
| m=2의 \(\|d-v_2\|_S\) | \(7.663478331196157\times10^{-16}\) |
| 같은 Π_F를 사용하는 온도 오차 \(b_T\varepsilon_2/\inf\Pi_F\) | \(1.710575696736044\times10^{-12}\,\mathrm K\) |

즉, 현재의 약 mK endpoint 온도 차이를 설명하는 데 필요한 평균 Jacobian 보정은 원 포함 폭보다 훨씬 작게 제어된다. 같은 양의 분모를 쓰는 오차라는 정의는 (7.7), (7.2)와 일치한다.

실제 endpoint-Jacobian/Neumann 포함을 원 application과 교차하면

\[
\Delta T\in[-0.001585967387181453,-0.001210819969055199]\ \mathrm K.
\tag{11.2}
\]

공통 numerator 평균 adjoint의 주요 성분은

\[
\overline z_x\in[-49430.25337661141,-48867.81791954700],
\quad
\overline z_w\in[7735.849570431344,7735.908522222911],
\tag{11.3}
\]
\[
\overline z^T\nu_{24}
\in[-48644.55871834544,-48082.11727381872].
\tag{11.4}
\]

각 성분의 단위는 §7의 numerator covector와 같다. 이 실제 포함이 (8.7), (8.9)의 sign condition을 닫는다. 그 결과 b>0에서

\[
\boxed{
\frac{\Delta T_{bR}}b
\in[-2.193573619033929,-2.084075101148286]\times10^{-9}\ \mathrm K,
}
\tag{11.5}
\]
\[
\boxed{
\frac{\Delta T_{bBE}}b
\in[6.795510419222985,7.189758987952319]\times10^{-5}\ \mathrm K.
}
\tag{11.6}
\]

b=0에서 두 sector는 정확히 0이고, b∈[0,1] 전체에서는 각각 [−2.193573619033929×10⁻⁹,0] K 및 [0,7.189758987952319×10⁻⁵] K가 된다. 두 항의 합은 b>0에서 양수다. 전체 ΔT와 개별 birth attribution은 같은 평균 inverse를 사용하므로 (11.2)의 전체 냉각과 (11.6)의 birth chronology 가열이 한 비교 안에 함께 존재한다.

실제 실행은 `checks/endpoint/apply_endpoint_remainder.py`와 `checks/endpoint/application01/`에 보존한다. 코드·원 입력 SHA, exact rational 출력, 명령·시각·exit·시간·메모리는 `RUN_RECORD.json` 및 `ENDPOINT_REMAINDER_RESULTS.json`에 있다. 실제 실행에서 physical source callback, nonlinear root solve, history replay는 모두 0회였다.
