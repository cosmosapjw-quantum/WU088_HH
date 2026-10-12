# 다음 이론 단위 제안 — HH_DEFECT_PARAMETER_RESPONSE

**Bounded goal.** 같은 fixed α와 동일 COMMON을 유지하여 θ∈{λ,b} 각각에 대한 endpoint 결함 d=g₂−g_F와 ΔT=T₂−T_F의 1차 미분을 구성·포함하고, birth/HH의 직접 forcing과 두 경로의 상태·opacity feedback을 연결한다. PHYS16의 sector attribution을 전체 매개변수 응답에 연결하는 다음 의무다.

**재사용 가능성.** 원 C² source·root family와 보존된 1차 carry로 시작할 수 있다. 필요한 미분은 H_g, H_gg, H_θ, H_gθ 및 g₁,θ,g₂,θ다. PHYS16의 Hessian remainder 자체를 다시 미분하는 대신 원 implicit equation을 미분하면 이 C² 자료에서 닫힌다.

## 시작할 정확식

y=g₂, y_θ=∂θg₂, d_θ=∂θd, J_F=H_g(g_F;θ)라 하자. g_F=y−d이며 H(g_F;θ)=0이므로

\[
J_Fd_\theta=J_Fy_\theta+H_\theta(g_F;\theta).
\tag{P1}
\]

PHYS15의 상관 잔차 r=H(y;θ)를 같은 경로에서 미분하면

\[
r_\theta=H_g(y;\theta)y_\theta+H_\theta(y;\theta).
\]

이를 (P1)에 넣어 작은 d를 먼저 인수 분해하면

\[
\boxed{
J_Fd_\theta=r_\theta-
\int_0^1\!\left\{
H_{gg}(y-sd;\theta)[d,y_\theta]
+H_{g\theta}(y-sd;\theta)d
\right\}\,ds.
}
\tag{P2}
\]

H_g(y)−H_g(g_F)와 H_θ(y)−H_θ(g_F)에 각각 선분 적분을 적용하면 성립한다. 같은 원 C,B,q,S가 J_F의 역전달을 포함한다. r_θ의 계산은 실제 두 stage의 식을 미분하여

\[
r_\theta=h\{B_{1,g}g_{1,\theta}+B_{1,\theta}
-B_{2,g}y_\theta-B_{2,\theta}\}+V p_\theta
\tag{P3}
\]

로 시작한다. p_θ는 PHYS15 광자 일곱 항에서 같은 stage carry와 공통 λ,b를 유지하여 미분한다.

최종 관측량은 d_e=ℓ_ed, Π_F=Π₂−d_e, N=C_Td_w−T₂d_e를 사용하여

\[
\boxed{
\partial_\theta\Delta T=
\frac{C_Td_{w,\theta}-T_2d_{e,\theta}
-T_{2,\theta}d_e
-\Delta T\{\ell_e y_\theta-d_{e,\theta}\}}{\Pi_F},
\qquad T_{2,\theta}=D T(y)y_\theta.
}
\tag{P4}
\]

이는 PHYS16과 같은 양의 유한 분모를 사용한다.

## 실제 존재하는 입력과 대응

| 입력 | 실제 필드와 역할 |
|---|---|
| PHYS09 `PROJECTED_RESULTS.json` | `stages[stage=first_half/full]::{U,V}`: 첫 half 및 Full의 λ,b gas sensitivity |
| PHYS14 `ADVANCE_RESULTS.json` | `gas_response::{U,V}`: 실제 carried second-half의 y_λ,y_b |
| PHYS11 `CARRY_RESULTS.json` | `stages[stage=first_half].groups`의 incoming/outgoing/absorbed Jets: 광자 1차 carry |
| 원 Full·first-half `SOURCE_BOX.json` | `A_Gg`, `G_gg`, `G_lambda`, `G_b`, `G_g_lambda`, `G_g_b` |
| 원 source component export | `nonphoto` 및 `q`의 signed gas gradient·Hessian; (P3)의 stage별 B_g,B_θ |
| 원 Full `UNIFORM_ARITHMETIC.json` | 같은 fixed C,B,q,S 및 inverse transfer |
| PHYS16 actual application | 같은 r,d,Π_F와 sector 포함; source/root/history 재실행을 거치지 않고 시작 |

원 `src/sourcebox.rs::export`에서 `G_g_lambda[i][j]`는 `residual[i].hessian[j][4]`, `G_g_b[i][j]`는 `residual[i].hessian[j][5]`다. Gas slot은 0–3, λ=4, b=5다. 실제 파일의 두 array는 각각 4×4다. 현재 source에서

\[
H_\lambda=-2h q_2\nu_H,
\quad H_{g\lambda}=-2h\nu_H\otimes Dq_2,
\quad H_b=-2VL_FJ,
\quad H_{gb}=2\sum_j\frac{\ell_jJ_j}{D_{Fj}^2}\nu_j e_x^T,
\]

이며 ℓ_j=2ha₂,j다. 이 대응을 원 export와 함께 적용한다.

**성공 판별.** (P2)와 (P3)의 direct/feedback 분해가 동일한 d_θ를 포함하고, (P4)에 같은 매개변수·분모를 사용하며, 판정 대상 ∂λΔT·∂bΔT의 실제 구간과 부호 여유를 출력한다. 부호가 결정되지 않은 항은 남은 폭을 지배하는 shared-state 의존성을 특정한다. 첫 유도·포함은 기존 C²/1차 carry 안에서 진행하고, 새로운 source·history 실행 필요성은 그 실제 결과로 판단한다.

이 제안은 다음 단위의 시작식과 입력 대응이다. 이 문서 작성 과정에서는 새 parameter-response application을 실행하지 않았다.
