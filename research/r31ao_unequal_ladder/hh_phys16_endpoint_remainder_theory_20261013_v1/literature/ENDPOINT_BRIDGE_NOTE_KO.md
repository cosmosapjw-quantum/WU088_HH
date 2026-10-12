# PHYS16 문헌 분과의 직접 endpoint 연결 유도

이 문서는 원고 검토를 위한 독립 대수 노트다. PHYS15의 정의 H=H_F, r=H(g2), H(gF)=0, d=g2−gF를 사용한다. 원 convex 영역 안에서 H∈C2이고 [g2,gF]가 그 영역에 포함된다. 모든 물리 단위와 고정 α,λ,b는 PHYS15와 같다.

## 1. Endpoint Taylor와 구성적 보정

J=DH(g2). t↦H(g2−td)에 적분형 Taylor 공식을 적용하면
\[
0=r-Jd+\mathcal R(d),\qquad
\mathcal R(d)=\int_0^1(1-t)D^2H(g_2-td)[d,d]dt.
\]
따라서
\[
Jd=r+\mathcal R(d).
\]
J가 가역이면 v=J⁻¹r에 대해 d−v=J⁻¹R이다. 원 preconditioned derivative bound가 J에도 적용되므로 가역성은 PHYS15의 같은 C,B,q,S에서 따른다.

|d|≤a이고 원 경로에서
\[
|\partial_j\partial_kH_i|\le\mathsf T_{ijk}
\]
이면
\[
|\mathcal R_i(d)|\le Q_i(a):=\frac12\sum_{j,k}\mathsf T_{ijk}a_ja_k.
\]
비음수 B와 ρ(B)<1 아래 |I−CJ|≤B가 성립하면
\[
|J^{-1}|\le(I-B)^{-1}|C|,
\quad
|d-v|\le(I-B)^{-1}|C|Q(a).
\]
여기서 ρ(B)<1은 같은 양의 diagonal S에 대한 ||S⁻¹BS||∞≤q<1로 보장된다. 이 componentwise 식에서 물리 단위는 C, H, a의 대응대로 유지된다.

실제 approximate linear solve ṽ를 쓰면 η=r−Jṽ를 원 잔차 단위로 정의하고
\[
d-\widetilde v=J^{-1}(\eta+\mathcal R(d)).
\]
따라서 위 포함의 Q(a)를 |η|+Q(a)로 바꾼다. η의 실제 평가 오차까지 포함하는 directed arithmetic이 구현 계약에 필요하다.

## 2. 임의 approximate adjoint의 정확한 식

고정 row ℓ 및 임의 z̃에 대해 ζ=ℓᵀ−Jᵀz̃라 두면
\[
\ell d=\widetilde z^TJd+\zeta^Td
=\widetilde z^Tr+\widetilde z^T\mathcal R(d)+\zeta^Td.
\]
그러므로
\[
|\ell d-\widetilde z^Tr|
\le\frac12\sum_{j,k}
\sup_{\gamma}|\widetilde z^T\partial_{jk}H|a_ja_k
+|\zeta|^Ta.
\]
γ는 동일 endpoint 연결 경로를 포함하는 평가 영역이다. Hessian을 z̃에 사영한 뒤 절대값을 취하면 반응량 간 정확한 소거를 유지할 수 있다. 이는 원 source의 보존 covector를 사용할 때 유용하다. 이 식은 z̃를 exact adjoint로 간주하는 가정을 요구하지 않는다.

온도에서 PHYS15의 ℓ_T는 미지 Π_F를 포함하므로, ℓ를 “이미 평가한 고정 row”로 쓰는 위 항등식과 구별한다. 계산 방식은 두 가지다.
- 고정 g2의 DT(g2)에 대해 위 식을 사용하고 온도 Hessian 나머지를 함께 포함한다.
- PHYS15의 ΔT=(CT d_w−T2 d_e)/(Π2−d_e)에 같은 d 포함을 직접 대입한다.

첫 방식도 C2만으로 충분하고 둘째 방식은 원 유리 분모 구조를 정확히 유지한다.

## 3. HI photo 항의 정확한 유리 나머지

γ_j=2h a2j, D2j=1+γ_j(1−x2), DFj=D2j+γ_jd_x라 두면
\[
H_{\gamma,j}(g)=\nu_jQ_{F,j}/D_j(g)-\nu_jQ_{F,j}.
\]
이를 endpoint에서 Taylor 전개한 나머지는 정확히
\[
\begin{aligned}
\mathcal R_{\gamma,j}
&=\nu_jQ_{F,j}
\left[
\frac1{D_{2j}+\gamma_jd_x}-\frac1{D_{2j}}
+\frac{\gamma_jd_x}{D_{2j}^2}
\right]\\
&=\boxed{\frac{\nu_jQ_{F,j}\gamma_j^2d_x^2}
{D_{2j}^2D_{Fj}}}.
\end{aligned}
\]
물리적 Q_F≥0, D2j,DFj>0 및 원 active ν_j=(1,0,0,ε_j)ᵀ≥0에서 이 벡터는 비음수다. Guards와 inactive columns는 기체 흡수 기여가 0이다. 이 유리식은 작은 d_x의 제곱을 먼저 형성하므로 별개의 큰 survival interval을 뺄 필요를 줄인다.

Hessian은
\[
\partial_{xx}H_{\gamma}
=\sum_j\frac{2\nu_jQ_{F,j}\gamma_j^2}{D_j^3}.
\]
나머지 전체에는 −2hD²B2가 함께 들어간다. 따라서 광자 나머지의 부호와 전체 coupled remainder의 부호를 각 source 사영에 따라 판정한다.

## 4. Rank-one inverse의 적용 조건과 직접 증명

J=A0+uvᵀ라 하자. A0가 가역이고 δ=1+vᵀA0⁻¹u≠0이면
\[
K=A_0^{-1}
-\frac{A_0^{-1}uv^TA_0^{-1}}{\delta}
\]
에 대해
\[
(A_0+uv^T)K
=I+uv^TA_0^{-1}
-\frac{u(1+v^TA_0^{-1}u)v^TA_0^{-1}}{\delta}
=I.
\]
정사각 행렬이므로 K=J⁻¹이다. 역순 곱도 같은 대수로 I다.

HH에서는 A0=I−2hDB2(g2), u=2h vF(g2), v=e_x가 자연스럽다. 추가 계산 경로를 택하면 A0의 inverse 포함과 δ의 0 분리를 확인한다. 원 full preconditioner가 제공하는 것은 J의 검증이므로 A0에 관한 추가 사실은 별도 근거로 붙인다. 현재 이론은 원 C로 J를 전처리하는 경로만으로도 완결 가능하다.

## 5. 근거 상태

위 식은 유한 차원 C2 Taylor 공식, 비음수 Neumann 상계와 직접 곱셈에서 유도했다. 원 HH 결과의 새 수치 구간을 평가한 기록은 이 문서에 없다. PHYS16 본문과 독립 검토는 원 source의 실제 Hessian 정의·영역·단위에 이 식을 대응하여 진행한다.

