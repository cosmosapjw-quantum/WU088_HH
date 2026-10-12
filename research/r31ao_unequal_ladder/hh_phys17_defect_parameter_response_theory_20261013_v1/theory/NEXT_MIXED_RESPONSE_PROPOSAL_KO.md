# 다음 이론 단위 — HH_DEFECT_MIXED_RESPONSE

**상태:** 다음 연구 시작식과 재사용 입력을 정했다. 이 파일 작성 중 새 mixed-response application은 실행하지 않았다(`not_run`).

## 1. 물리 질문과 현재 출발점

PHYS17은 같은 α, COMMON, λ,b∈[0,1]²에서 endpoint 온도 결함 F(λ,b)=ΔT(λ,b)의 전역 1차 방향을 얻었다. 다음 질문은 **HH와 birth의 공존이 시간 분할 온도 차이에 주는 혼합 작용의 부호와 크기**다. 대상은

\[
W_d=\partial_{\lambda b}(g_2-g_F),\qquad
F_{\lambda b}=\partial_{\lambda b}\Delta T,
\]

\[
\boxed{\mathcal I=F(1,1)-F(1,0)-F(0,1)+F(0,0)
=\int_0^1\!\int_0^1 F_{\lambda b}(\lambda,b)\,db\,d\lambda.}
\tag{M1}
\]

이미 얻은 원 λ-도함수 범위에서 |I|≤1.958485175177039×10⁻⁹ K가 성립한다. 이는 다음 판별의 비교 기준이며, 이 범위 안에서 실제 interaction의 방향을 결정하고 source forcing·absorption feedback·온도 분모의 역할을 분리한다.

정칙성은 현재 C² source/root family를 유지한다. 두 implicit 경로를 직접 두 번 미분하면 필요한 gas Hessian과 mixed gas/parameter Hessian이 원 자료에 모두 있다. 원 C² 자료로 시작하고, 추가 정칙성이 필요한 표현은 그 필요성과 얻을 개선을 구분한다.

## 2. 원 mixed carry와 표기

\[
g=g_2,\quad g_F=g-d,
\quad U=g_{2,\lambda},\quad V=g_{2,b},\quad W=g_{2,\lambda b},
\]

\[
U_F=U-d_\lambda,\quad V_F=V-d_b,\quad
W_F=W-W_d.
\]

원 첫 half의 carry는 U₁,V₁,W₁이고, stage 차이는

\[
s=g_2-g_1,\quad s_\lambda=U-U_1,\quad s_b=V-V_1,\quad
s_{\lambda b}=W-W_1.
\]

| 재사용 입력 | 실제 역할 |
|---|---|
| PHYS09 `PROJECTED_RESULTS.json` first_half/full의 U,V,W | 첫 half 및 Full의 원 1차·혼합 carry |
| PHYS14 `ADVANCE_RESULTS.json/gas_response`의 U,V,W | 실제 carried second-half의 mixed endpoint |
| PHYS11 first-half와 PHYS14 second-half photon signed Jets | incoming·absorbed·outgoing의 mixed carry |
| 원 first_half/full nonphoto/q value·gradient·signed Hessian | 단계별 C² source composition |
| 원 Full A_Gg,G_gg,G_g_lambda,G_g_b,G_lambdab | 실제 Full mixed implicit forcing |
| PHYS16 d 및 PHYS17 dλ,db,sλ,sb | 작은 결함과 stage carry를 먼저 인수 분해하는 기준 |
| 원 Full C,B,q,S | Wd의 동일 전처리 포함 |

원 PHYS14의 `gas_response`에서 `coordinates,U,V,W`, PHYS09의 full/first_half stage에서 `U,V,W` 필드를 실제 읽어 존재를 확인했다. Parameter slot과 byte identity는 next application에서 원 계약에 결박한다. 새 source/root/history 재실행을 요구하는 계약은 아직 없다.

## 3. C²에서 정확히 닫히는 mixed implicit 식

H=H_F, J_F=H_g(gF), J_y=H_g(g₂)라 두고

\[
\mathcal B(g_0;p,q)=H_{gg}(g_0)[p,q]
+H_{g\lambda}(g_0)q+H_{gb}(g_0)p+H_{\lambda b}(g_0)
\tag{M2}
\]

를 정의한다. H(gF;λ,b)=0을 두 번 미분하면

\[
\boxed{J_FW_F=-\mathcal B(g_F;U_F,V_F).}
\]

따라서 새 mixed defect는

\[
\boxed{J_FW_d=J_FW+\mathcal B(g_F;U_F,V_F).}
\tag{M3}
\]

이 식은 원 W₂와 Full mixed forcing을 결합하는 직접 계산의 출발점이다. 현재 Full에서 Hλb는 고정 gas의 원 future partial로 0이며, 실제 export의 signed enclosure와 정확한 source 구조를 함께 사용한다.

### 3.1 작은 1차 defect를 보존하는 상관식

r=H(g₂), L=J_y−JF=∫Hgg(g₂−td)[d,·]dt,
ΔHgg=Hgg(g₂)−Hgg(gF), ΔHgθ=Hgθ(g₂)−Hgθ(gF)라 두면

\[
\boxed{\begin{aligned}
J_FW_d={}&r_{\lambda b}-LW\\
&-\Delta H_{gg}[U,V]
-H_{gg}(g_F)[d_\lambda,V]
-H_{gg}(g_F)[U_F,d_b]\\
&-\Delta H_{g\lambda}V-H_{g\lambda}(g_F)d_b\\
&-\Delta H_{gb}U-H_{gb}(g_F)d_\lambda
-\Delta H_{\lambda b}.
\end{aligned}}
\tag{M4}
\]

**증명.** rλb=JyW+B(g₂;U,V)와 (M3)를 빼고
`Hgg(gF)[U,V]−Hgg(gF)[UF,VF]
=Hgg(gF)[dλ,V]+Hgg(gF)[UF,db]`
를 대입한다. Hgλ,Hgb의 항도 같은 선형 차이로 분해한다. □

(M4)의 Hessian 공간차 ΔHgg에는 원 signed Hessian 범위의 차를 사용할 수 있다. 하나의 공통 범위 [l,u]에 속하는 두 Hessian 값의 차는 [l−u,u−l]에 들어가며, 이 항은 U,V의 곱에만 곱해진다. 첫 판별에서는 이 실제 크기를 다른 항과 비교한다.

### 3.2 HI와 HH 구조로 정확히 인수 분해하는 부분

Dj=1+ℓj(1−x₂), DFj=Dj+ℓj d_x, ℓj=2ha₂j라 두면

\[
\boxed{\Delta H_{gg,\rm ph}=
2\sum_j\frac{\ell_j^3Q_{Fj}d_x
(D_{Fj}^2+D_{Fj}D_j+D_j^2)}{D_j^3D_{Fj}^3}
\,\nu_j e_x^T\otimes e_x^T,}
\tag{M5}
\]

\[
\boxed{\Delta H_{gb}=
2\sum_j\frac{\ell_j^2J_{\gamma j}d_x(D_{Fj}+D_j)}{D_j^2D_{Fj}^2}
\,\nu_j e_x^T,}
\tag{M6}
\]

\[
\boxed{\Delta H_{g\lambda}=-2h\nu_H\otimes
\int_0^1 D^2q_2(g_2-td)[d,\cdot]dt.}
\tag{M7}
\]

이 세 항은 같은 d를 명시적으로 유지한다. Nonphoto와 λq의 Hessian **값의 차이**는 원 C² signed 포함을 그대로 사용하여 별도로 크기를 기록한다. (M5)는 `a⁻³−b⁻³=(b−a)(a²+ab+b²)/(a³b³)`, (M6)는 같은 2차 분모 차에서 나온다.

## 4. 실제 stage 식에서 rλb를 구성하는 첫 경로

B_k=F_k+λq_kνH−2Hkw e_w이므로

\[
\boxed{\begin{aligned}
r_{g,\lambda b}=h\{&B_{1,g}W_1-B_{2,g}W
+B_{1,gg}[U_1,V_1]-B_{2,gg}[U,V]\\
&+[Dq_1V_1-Dq_2V]\nu_H\}.
\end{aligned}}
\tag{M8}
\]

각 source는 자기 stage endpoint에서 평가한다. 첫 두 linear term의 차이는 현재 PHYS17의 C² bridge를 그대로 이용해

\[
B_{1,g}(g_1)W_1-B_{2,g}(g_2)W
=D\delta B_t(g_1)W_1-B_{2,g}(g_2)s_{\lambda b}
-\int_0^1B_{2,gg}(g_1+ts)[s,W_1]dt
\tag{M9}
\]

로 만든다. Hessian contraction도

\[
\boxed{\begin{aligned}
B_{1,gg}[U_1,V_1]-B_{2,gg}[U,V]
={}&(B_{1,gg}-B_{2,gg})[U_1,V_1]\\
&-B_{2,gg}[s_\lambda,V_1]-B_{2,gg}[U,s_b]
\end{aligned}}
\tag{M10}
\]

로 작은 stage 1차 차이를 유지한다. 마지막 HH gradient 차이는

\[
Dq_1(g_1)V_1-Dq_2(g_2)V
=D\delta q_t(g_1)V_1-Dq_2(g_2)s_b
-\int_0^1D^2q_2(g_1+ts)[s,V_1]dt
\tag{M11}
\]

로 연결한다. (M9),(M11)의 density derivative는 이번 PHYS17에서 완결한 closure를 그대로 쓴다.

Photon rph,λb=V pλb는 원 동일 일곱 sector graph에 mixed 2-jet을 적용한다. 필요한 primitive는

\[
A_{k,\lambda b}=ha_k A_k^2 W_{k,x}
+2(ha_k)^2A_k^3U_{k,x}V_{k,x},
\quad Q_{1,\lambda}=0,\quad Q_{1,b}=J_\gamma,\quad Q_{1,\lambda b}=0.
\tag{M12}
\]

ζ= h[cσ(n₂−n₁)(1−x₂)−a₁s_x]에 대해

\[
\zeta_{\lambda b}=-h[c\sigma(n_2-n_1)W_x+a_1s_{\lambda b,x}]
\]

를 먼저 구성하고 ΔA₁=ζA₁A₂의 mixed product rule에 사용한다. 두 번째 stage의 sλb는

\[
s_{\lambda b}=h\{B_{2,g}W+B_{2,gg}[U,V]+Dq_2[V]\nu_H\}+VP_{2,\lambda b}
\tag{M13}
\]

와 원 W−W₁의 포함을 교차한다. 식 (M8)–(M13)은 원 second-order Jets를 이용하는 유한 연산이며, 원 source의 3차 미분을 요구하지 않는다.

## 5. 유한 온도 분수의 mixed derivative

P=ΠF=Π₂−de, N=CT dw−T₂de, F=N/P라 두자. 

\[
P_\theta=\ell_e(g_{2,\theta}-d_\theta),\quad
P_{\lambda b}=\ell_e(W-W_d).
\]

N=FP를 두 번 미분하면

\[
\boxed{F_{\lambda b}=
\frac{N_{\lambda b}-F_\lambda P_b-F_bP_\lambda-FP_{\lambda b}}P,}
\tag{M14}
\]

\[
N_{\lambda b}=C_TW_{d,w}-T_2\ell_eW_d
-T_{2,\lambda b}d_e-T_{2,\lambda}d_{e,b}-T_{2,b}d_{e,\lambda}.
\]

같은 nF=CTe_wᵀ−TFℓe를 사용하면

\[
\boxed{\begin{aligned}
F_{\lambda b}=\frac1{\Pi_F}\{&n_FW_d
-T_{2,\lambda b}d_e-T_{2,\lambda}d_{e,b}-T_{2,b}d_{e,\lambda}\\
&-F_\lambda P_b-F_bP_\lambda-F\ell_eW\}.
\end{aligned}}
\tag{M15}
\]

두 번째 endpoint의 mixed 온도는

\[
\boxed{T_{2,\lambda b}=
\frac{C_TW_w-T_2\ell_eW-T_{2,\lambda}\ell_eV-T_{2,b}\ell_eU}{\Pi_2}.}
\tag{M16}
\]

(M14)–(M16)은 정확한 quotient identity다. 같은 양의 ΠF를 사용하고, mixed forcing을 원 C,B,q,S와 같은 JF adjoint로 전달할 수 있다.

## 6. 다음 판별과 완료 기준

1. 원 W1,W2,WF 및 photon mixed carry의 identity·slot을 결박한다.
2. (M3)의 직접 포함과 (M4),(M8)–(M13)의 상관 포함을 실제로 구성한다. H의 양 끝 Hessian 차이는 원 C² 범위 안에서 평가한다.
3. 원 preconditioner로 Wd를 포함하고 (M15)의 같은 분모로 Fλb에 전달한다.
4. Fλb 및 I의 실제 구간·부호 margin을 출력하고, 이미 확보한 |I|≤1.95849×10⁻⁹ K와 비교한다. 폭을 지배하는 항을 실제 분해값으로 특정한다.
5. source forcing, photon competition, thermal normalization의 혼합 기여를 하나의 공통 inverse와 covector로 연결한다. Wolfram/xAct 및 독립 검토 후 해당 범위의 결과를 채택한다.

새 실행은 `not_run`, heavy_queue=[], launch=false로 둔다. 첫 실행은 보존된 source·carry의 exact interval 연산이다. 별도 source 평가나 고차 정칙성 보강의 필요성은 위 판별 결과에서 결정한다.
