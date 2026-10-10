# PHYS03: 명시적 시간변화와 photon birth의 혼합 응답

2026-10-10. 독립 후보 유도와 bounded algebra 검산. 최종 decision reviewer의 판정 문서가 아니다.

## 1. 범위와 계승

PHYS02의 frozen finite-remainder 인증을 다시 수행하지 않는다. 이번 목표는 smooth nonautonomous source의 새 항, 임의의 smooth birth profile에 대한 leading causal kernel, 그리고 birth 후 BE 노출의 형식적 계수를 도출하는 것이다. 모든 source·원자물리·우주론 수치 이력을 새로 생성하지 않는다.

부모 실행자의 source 조사에서 실제 owner 배경과 연산 순서는 식별되어 있다. 그 owner는 endpoint remap, birth, frozen BE를 합성한다. 이를 단일한 smooth nonautonomous ODE로 바꾸는 것은 별도의 모형 선택이다. 이 문서는 그 smooth reference family를 실제 native family라고 간주하지 않는다. PHYS02의 선택 초기점은 추출된 source-cell 입력이고, macro 전체 연산 이전의 공통 초기상태라고 주장하지 않는다.

아래 정의는 실제 source에 연결할 수 있는 일반 smooth-cell 계약이다.

\[
 \dot z=F(t,z;\lambda,S)=F_0(t,z)+\lambda H(t,z)+SB(t),
 \qquad S=bS_*,\quad S_*={\rm binary64}(5\times10^{-15}).
\tag{1.1}
\]

계산식에서는 차원 있는 \(S\)를 독립 매개변수로 사용한다. 원 요청의 \(b\)에 대한 혼합 감도는 아래 \(S\) 감도에 \(S_*\)를 곱하면 된다. \(\lambda,b\in[0,1]\)이다.

상태 \(z\)는 기체와 모든 광자 성분을 포함하고, 모든 \((\lambda,S)\)가 같은 초기 전체상태 \(z(t_0)=z_0\)를 갖는다. \(H\)는 photon-independent이며 photon 성분이 0이다. \(B(t)\)는 상태와 매개변수에 무관하고 고정된 photon 좌표부분공간에 놓인다. 따라서 \(B_t,B_{tt}\)도 그 부분공간에 놓인다. 고정 chart 안에서 photo RHS는 gas–photon에 bilinear이며, 그 밖의 nonphoto H/He·열·팽창항은 제거하지 않는다.

시간은 proper seconds, \(w\)는 eV/H, \(P_j\)는 photons/H이다. 기본 metric signature는 \((-+++)\)이고 \(c,k_{\rm B},E_{\rm eV}\)를 유지한다. \(t\)-미분은 따로 표시하지 않으면 상태 \(z\)를 고정한 편미분이다. \(\delta=t-t_0\)는 전개에 쓰는 경과시간이다.

## 2. 정확한 비자율 감도식

\[
 U=\partial_\lambda z,\quad V=\partial_Sz,\quad
 W=\partial_\lambda\partial_Sz,\quad J=F_z,\quad Q=F_{zz}.
\]

시간이 매개변수에 독립인 공통 clock이면

\[
\begin{aligned}
 \dot U&=JU+H,&U(t_0)&=0,\\
 \dot V&=JV+B(t),&V(t_0)&=0,\\
 \dot W&=JW+Q[U,V]+H_zV,&W(t_0)&=0.
\end{aligned}
\tag{2.1}
\]

\(F_t\)가 별도의 항으로 이 감도식에 추가되지는 않는다. 매개변수 미분에서 clock을 고정했기 때문이다. 반면 이 식을 시간으로 미분할 때에는 모든 계수의 explicit-time derivative가 필요하다.

\[
 I_z(t;\lambda,S)
 =\lambda S\int_0^1\!\!\int_0^1
 W(t;a\lambda,cS)\,da\,dc.
\tag{2.2}
\]

따라서 nonautonomous 경우에도 \(\lambda S\) 인수는 정확히 보존된다. 초기 \(q_0>0\)이면 \(U/q_0,W/q_0\) 정규화도 PHYS02와 똑같이 가능하다.

## 3. 자동화 가능한 total-derivative 형식

매개변수를 고정하고

\[
 D=\partial_t+F\cdot\nabla_z
\]

를 계수장에 작용시키자. 아래 도함수는 인자 벡터를 고정한 tensor의 미분이다.

\[
\begin{aligned}
 DJ&=J_t+Q(F,\cdot),\\
 DQ&=Q_t+F_{zzz}(F,\cdot,\cdot),\\
 D H_z&=H_{tz}+H_{zz}(F,\cdot),\\
 D^2 H_z&=H_{ttz}+2H_{tzz}(F,\cdot)
       +H_{zzz}(F,F,\cdot)
       +H_{zz}(F_t+JF,\cdot).
\end{aligned}
\tag{3.1}
\]

초기점 \((t_0,z_0)\)에서

\[
\begin{aligned}
 U_1&=H,\\
 U_2&=JH+H_t+H_zF,\\
 V_1&=B,\\
 V_2&=JB+B_t,\\
 V_3&=J(JB+B_t)+2(DJ)B+B_{tt}.
\end{aligned}
\tag{3.2}
\]

현재의 photon-only 가정을 잠시 사용하지 않아도, \(B=B(t)\)이며 상태에는 무관하면

\[
\begin{aligned}
 K_2&:=W^{(2)}(t_0)=H_zB,\\
 K_3&:=W^{(3)}(t_0)
 =JK_2+2Q(H,B)+H_zV_2+2(DH_z)B,\\
 K_4&:=W^{(4)}(t_0)\\
 &=JK_3+3(DJ)K_2
   +3Q(U_2,B)+3Q(H,V_2)+6(DQ)(H,B)\\
 &\quad+H_zV_3+3(DH_z)V_2+3(D^2H_z)B.
\end{aligned}
\tag{3.3}
\]

이 형식은 time/state AD 또는 clock augmentation으로 자동화하기 좋다. \(B_z\ne0\)인 state-dependent injection에는 식 (2.1)부터 추가항이 필요하므로 식 (3.3)을 적용하지 않는다.

clock \(t'=1\)을 넣어 자율화할 때도 주의가 있다. 확장된 birth 장은 \(\bar B=(0,B(t))\)이고 \(\partial_t\bar B\ne0\)일 수 있다. 예전의 “autonomous이고 \(B\)가 상수”라는 tensor식을 그대로 적용하면 \(B_t\) 항을 누락한다. 안전한 방법은 식 (2.1) 전체에 clock 좌표를 추가한 뒤 time jet을 계산하는 것이다.

## 4. 현재 source 구조에서의 cubic과 quartic

고정된 photon 부분공간을 \(\mathcal P\)라 하면

\[
 H_zp=H_{tz}p=H_{zz}(p,v)=0\qquad(p\in\mathcal P).
\]

photo bilinearity는

\[
 Q(B,B)=0,\qquad F_{zzz}(B,v,w)=0
\tag{4.1}
\]

를 준다. \(F_{zzz}\)가 photon slot에서 0이라는 결론에는 gas 쪽 affine 의존성도 필요하다. 단순히 photon에 선형이라는 조건만으로는 충분하지 않다.

식 (3.3)에 이를 대입하면

\[
 K_2=0,\qquad
 \boxed{K_3=H_zJB+2Q(H,B).}
\tag{4.2}
\]

즉 **explicit-time derivative는 cubic에 들어오지 않는다.** 모든 계수를 \(t_0\)에서 평가한 PHYS02의 계수와 같다. 밀도·온도·에너지의 초기값 자체는 물론 이 초기 계수를 결정한다.

\(C=JB\)로 쓰고 PHYS02의 instantaneous frozen 식을

\[
\begin{aligned}
 K_4^{\rm fr}={}&JK_3+3Q(B,JH+H_zF)+3Q(H,C)\\
 &+H_z[JC+2Q(F,B)]+3H_{zz}(F,C)
\end{aligned}
\tag{4.3}
\]

로 정의하면, 정확한 새 항은

\[
\boxed{
\begin{aligned}
 K_4 &=K_4^{\rm fr}+\Delta_tK_4,\\
 \Delta_tK_4={}&
     3Q(H_t,B)
    +3Q(H,B_t)
    +6Q_t(H,B)\\
    &+H_z[JB_t+2J_tB]
    +3H_{tz}(JB).
\end{aligned}}
\tag{4.4}
\]

여기서 \(J_t=\partial_tF_z\), \(Q_t=\partial_tF_{zz}\)이다. \(F_t\) 벡터 자체, \(B_{tt}\), \(H_{tt}\)는 이 차수의 최종 식에 남지 않는다. 그 항들은 식 (3.3)에 존재하지만 photon slots와 zero initial sensitivities로 소거된다.

따라서

\[
 I_z=\lambda S\left[
   \frac{K_3\delta^3}{6}
  +\frac{\{K_{40}^{\rm fr}+\Delta_tK_4
          +(\lambda/2)K_{41}\}\delta^4}{24}
 \right]+O(\lambda S\delta^5).
\tag{4.5}
\]

\(\Delta_tK_4\)는 \(\lambda,S\) 모두에 무관하다. 예를 들어 \(Q_t(H,B)\)의 \(\lambda H_{tzz}\) 부분은 photon slot 때문에 0이고, \(J_tB\)의 \(\lambda H_{tz}B\)도 0이다. 따라서 \(K_4\)는 여전히 \(S\)에 무관하고 \(\lambda\)에 affine이며, \(\lambda^2S\) 계수 \(K_{41}\)는 기존 PHYS02의 instantaneous 식과 같다.

### 더 강한 구조적 소거

explicit-time variation이 photon-independent nonphoto 장 \(N(t,y)\)에만 있다면

\[
 (J_t^{N})B=0,\qquad (Q_t^{N})(H,B)=0.
\]

\(H_t=B_t=0\)인 한 \(\Delta_tK_4=0\)이다. \(N,N_y,N_{yy}\)의 instantaneous 값은 식 (4.3)에 남지만 **그 nonphoto 장의 명시적 시간변화 자체는 mixed quartic에 들어오지 않는다.** 이 영향은 최소 5차부터 가능하다. \(-2H_{\rm mean}(t)w\)의 explicit \(H_{\rm mean,t}\)만 변화시키는 경우도 여기에 해당한다.

반면 밀도 변화는 일반적으로 HH amplitude와 photon opacity도 바꾸므로 \(H_t,J_tB,Q_t(H,B)\)를 통해 quartic에 들어온다.

## 5. 물리 source에 입력해야 하는 derivative

예를 들어 동일한 H/He gas 좌표에서 \(r(t)=n_{\rm He}/n_{\rm H}\)이고

\[
 \Pi=1+r+x+r(y_1+2y_2),\qquad
 T=\frac{2E_{\rm eV}}{3k_{\rm B}}\frac{w}{\Pi}
\]

이면, 상태를 고정한 편미분은

\[
 \Pi_t=r_t(1+y_1+2y_2),\qquad
 T_t|_z=-T\frac{\Pi_t}{\Pi},
\]

\[
 q_t|_z=n_{{\rm H},t}u^2 k(T)
        +n_{\rm H}u^2 k_T(T)\,T_t|_z.
\tag{5.1}
\]

\(H_{tz}\)는 이 식의 상태 Jacobian으로 구할 수 있다. \(q\) 또는 \(u\)로 나눌 필요가 없다.

단일 photo 계수 \(a_j(t)=cn_{\rm H}(t)\sigma_{\rm H}(E_j(t))\)를 실제로 smooth cell에서 사용하는 경우

\[
 a_{j,t}=c\{n_{{\rm H},t}\sigma_{\rm H}
          +n_{\rm H}\sigma_{{\rm H},E}E_{j,t}\},\qquad
 g_{j,t}=E_{j,t}.
\tag{5.2}
\]

이것은 해당 에너지와 단면적이 smooth branch 안에서 움직이는 모델에 대한 식이다. 실제 fixed-grid remap owner가 단면적을 고정 node에서 평가한다면 transported energy에 식 (5.2)를 적용해 그 연산을 대체하면 안 된다. remap과 고정-node absorption은 각자 정의한 map/flow의 derivative로 처리해야 한다.

식 (4.4)의 실제 숫자를 평가하려면 어떤 연속 reference family에 어떤 provider 값과 derivative를 bind하는지 먼저 고정해야 한다. 실제 owner background가 식별되어 있다는 사실만으로 그 reference family 또는 full/two-half family의 상태·감도가 인증되는 것은 아니다.

## 6. prescribed birth time에 대한 정확한 causal Volterra 식

이 절에서는 시작시각을 0으로 옮겨 표기한다. 필요하면 모든 coefficient의 \(t\)에 실제 \(t_0+t\)를 대입한다.

새 광원이 없는 기준 \((\lambda,S)=(0,0)\) 궤적을 \(z_*(t)\), 그 Jacobian과 Hessian을 \(J_0(t),Q_0(t)\)라 하자. 이 궤적과 계수는 이론상의 기호이며 여기서 수치 적분하지 않는다. \(\Phi(t,r)\)는

\[
 \partial_t\Phi(t,r)=J_0(t)\Phi(t,r),\qquad \Phi(r,r)=I
\]

이다. HH 감도는

\[
 U(t)=\int_0^t\Phi(t,r)H(r,z_*(r))\,dr.
\tag{6.1}
\]

정해진 birth시각 \(\sigma\)에 작은 질량 \(m\)의 photon을 additive map
\(z^+=z^-+mB(\sigma)\)로 넣는다. birth시각은 상태나 매개변수에 의존하지 않는다고 가정한다. 그 first birth sensitivity는

\[
 V_\sigma(t)=
 \begin{cases}
 0,&t<\sigma,\\
 \Phi(t,\sigma)B(\sigma),&t\ge\sigma.
 \end{cases}
\]

혼합 jump는 0이지만 \(U(\sigma^-)\)를 0으로 reset하지 않는다. 종료상태의 정확한 mixed functional kernel은

\[
\boxed{
 \mathcal K_z(t,\sigma)=
 \int_\sigma^t\Phi(t,r)
 \left[
 Q_0(r)\{U(r),\Phi(r,\sigma)B(\sigma)\}
 +H_z(r)\Phi(r,\sigma)B(\sigma)
 \right]dr.}
\tag{6.2}
\]

즉 \(\partial_\lambda\partial_m z(t)|_{\lambda=m=0}
=\mathcal K_z(t,\sigma)\)이다. 누적 HH sensitivity \(U(r)\)의 적분 하한은 0이며 \(\sigma\)가 아니다.

임의의 prescribed smooth birth rate \(j(\sigma)\)에 대한 mixed functional derivative는

\[
 \delta_\lambda\delta_j z(t)
 =\lambda\int_0^t j(\sigma)\mathcal K_z(t,\sigma)\,d\sigma.
\tag{6.3}
\]

이는 HH와 새 source의 first functional response이다. 유한한 strength의 전체 nonlinear response와 같다고 주장하지 않는다. 유한 매개변수의 차이는 식 (2.2)의 parameter average를 사용해야 한다.

## 7. frozen leading kernel과 prebirth memory

이제 고정 외부계수와 초기 \(z_0\)의 국소 Taylor 계수를 사용한다. \(q(T,x)\)의 상태 derivative를 없애는 것이 아니다. 특히 thermal suppression에 필요한 \(q_T\)를 보존한다.

\[
 X=H_zJ_0B,\qquad Y=Q_0(H,B)
\]

라 두면 \(U(r)=rH+O(t^2)\), \(V_\sigma(r)=B+(r-\sigma)J_0B+O(t^2)\)이고 \(H_zB=0\)이므로

\[
\boxed{
 \mathcal K_z(t,\sigma)
 =\frac{(t-\sigma)^2}{2}\,X
  +\frac{t^2-\sigma^2}{2}\,Y
  +O(t^3),\quad 0\le\sigma\le t.
}
\tag{7.1}
\]

매끄러움과 uniform bounded derivatives에서 remainder는 이 삼각형 전체에 uniform하게 잡을 수 있다. bounded continuous rate에 적분하면 \(O(t^4)\), 고정 질량 impulse에는 \(O(mt^3)\)가 된다.

단색 HI-only birth에 대해 \(A=cn_{\rm H}\sigma_{\rm H}(E_*)\),
\(X_x=-Aq(2+\Xi)\), \(Y_x=-Aq\)이므로

\[
\boxed{
 \mathcal K_x(t,\sigma)=
 -\frac{Aq}{2}\{(2+\Xi)(t-\sigma)^2+t^2-\sigma^2\}
 +O(t^3).}
\tag{7.2}
\]

이는 PHYS01의 chronology를 일반 감도식에서 재도출한 것이다. HH를 birth 이후에만 축적시키는 잘못된 reset은 \(t^2-\sigma^2\)를 \((t-\sigma)^2\)로 바꿔

\[
 \Delta\mathcal K_z
   =\sigma(t-\sigma)Y,\qquad
 \Delta\mathcal K_x=-Aq\,\sigma(t-\sigma)
\tag{7.3}
\]

를 누락한다. birth 전에 이미 달라진 중성수소를 새 photon이 만나는 효과다.

\(\Xi\ge0,Aq>0\)이면 leading kernel은 \(\sigma<t\)에서 음수이고

\[
 \partial_\sigma\mathcal K_x
 =Aq\{(2+\Xi)(t-\sigma)+\sigma\}>0
\tag{7.4}
\]

이다. 같은 photon mass라면 먼저 들어올수록 leading 비가산 억제가 크다. 이 statement는 local leading kernel의 부호이며 arbitrary all-time kernel의 부호 정리는 아니다.

### smooth profile의 첫 derivative와 quartic 교차검사

\(B(t)=\rho(t)B_*\), \(\rho(t)=\rho_0+\rho_1t+O(t^2)\)이고 다른 explicit coefficients가 고정이면

\[
 \Delta_tK_4^{\rm profile}=\rho_1(X+3Y).
\tag{7.5}
\]

이 식에서 \(X,Y\)는 \(B_*\)로 계산한다. 직접 kernel 적분에서도

\[
 \int_0^t\sigma\,\mathcal K_z^{(2)}(t,\sigma)d\sigma
   =\frac{t^4}{24}(X+3Y)
\]

이므로 식 (4.4)의 \(B_t\) 항과 독립적으로 일치한다.

## 8. 같은 photon 질량으로 profile을 비교할 때

관측 종료 \(\Delta\), 총 추가 질량 \(M\), 동일한 초기 HH 및 기체 조건을 두고 \(I_x/(\lambda MAq\Delta^2)\)의 leading factor를 비교하면 다음과 같다.

| 광원 또는 형식적 연산 | leading factor |
| --- | ---: |
| 0에서 \(\Delta\)까지 uniform continuous rate \(M/\Delta\) | \(-(4+\Xi)/6\) |
| \(t=0\)의 initial impulse 후 연속 진화 | \(-(3+\Xi)/2\) |
| \(t=\Delta\)의 terminal impulse, 추가 노출시간 0 | \(0\), 상태 \(z\)의 mixed jump는 exact zero |
| birth를 넣고 길이 \(\Delta\)의 한 frozen BE map | \(-(3+\Xi)\) |

마지막 행은 \(z^+=z_0+MB+\Delta\{F_0(z^+)+\lambda H(z^+)\}\)의 형식적 계수이다. “끝점에 birth를 추가한 뒤 BE”라는 이름이 붙어도 연속시간 terminal impulse와 같지 않다. 유한 BE 근이나 owner의 actual history를 계산한 결과가 아니다.

PHYS01에서 상속한 \(\Xi_0\simeq0.1769024684\)를 쓰면 initial impulse/uniform의 leading 크기 비는 약 \(2.2817644121\), 한 BE map/uniform은 약 \(4.5635288242\)이다. 한 BE map은 initial continuous impulse의 정확히 두 배인 leading coefficient를 갖는다.

상속된 \(S_*,\Delta=1.25\times10^9\) s로 \(M=S_*\Delta\)를 맞춘 point-coefficient 진단은 uniform \(-2.0159064163\times10^{-17}\), initial impulse \(-4.5998235188\times10^{-17}\), 한 BE map \(-9.1996470376\times10^{-17}\)이다. **새 source profile/BE에 PHYS02의 finite-remainder 인증을 전용하지 않는다.** 이 숫자들은 leading coefficient를 비교하는 동일한 정규화의 진단이다.

초기 impulse를 비교할 때의 common initial state는 impulse 직전이다. impulse 직후에는 control에 의해 photon 초기값이 달라지므로 continuous source의 zero initial \(V\) 조건 및 cubic law와 혼동하지 않는다.

## 9. 반복 endpoint-birth + BE의 형식적 cubic coefficient

원래 공통 초기상태로부터 \(m\)개의 step을 취하고 \(\delta=\Delta/m\), 각 step에 \(S\delta B\)를 넣는 frozen formal map을 생각하자. 실제 nonlinear BE 근을 계산하지 않고 time series만 비교한다.

\[
 I_{z,m}
 =\lambda S\Delta^3
 \{\alpha_mX+\beta_mY\}
 +O(\lambda S\Delta^4),
\]

\[
 \alpha_m=\frac{(m+1)(m+2)}{6m^2},\qquad
 \beta_m=\frac{(m+1)(2m+1)}{6m^2}.
\tag{9.1}
\]

각 step의 leading HH 감도는 \(U_k=k\delta H\), photon sensitivity는 \(V_{P,k}=k\delta B\), gas birth 감도는 \(V_{{\rm gas},k}=\delta^2k(k+1)C_{\rm gas}/2\), \(C_{\rm gas}=(J_0B)_{\rm gas}\)이다. mixed recurrence에 대입해

\[
 W_m=\delta^3\sum_{k=1}^m
 \{k^2Y+k(k+1)X/2\}+O(\Delta^4)
\]

를 얻고 정수 합을 수행하면 식 (9.1)이 나온다.

따라서

\[
\boxed{
 I_{x,m}=-\lambda SAq\Delta^3 C_m+O(\lambda S\Delta^4),\qquad
 C_m=\frac{4+\Xi}{6}
    +\frac{3+\Xi}{2m}
    +\frac{5+2\Xi}{6m^2}.}
\tag{9.2}
\]

\(m=1\)은 \(3+\Xi\), \(m=2\)는 \(13/8+\Xi/2\), \(m\to\infty\)는 continuous coefficient \((4+\Xi)/6\)이다. \(\Xi\ge0\)이면 이 leading coefficient는 \(m\)에 따라 단조 감소한다.

이 식의 비교조건은 동일 raw initial state, 동일 총 시간과 photon mass, 정해진 frozen source 순서이다. 실제 owner의 remap, fixed-grid cutoff, density sampling이 이 가정을 만족하는지 별도로 판단해야 한다. smooth \(O(\Delta)\) coefficient drift가 cubic에 들어오지 않는다는 결과는 branch crossing이나 비매끄러운 remap을 자동으로 포괄하지 않는다.

만약 birth 전에 이미 누적된 HH 감도 \(U_{\rm old}\ne0\)가 있으면, additive birth 후 BE의 exact sensitivity identity는

\[
 (I-\delta J_+)W_+
 =W_{\rm old}
   +\delta\{Q_+(U_+,V_+)+H_{z,+}V_+\}.
\tag{9.3}
\]

그 \(U_{\rm old}\)를 버리면 \(\delta Q(U_{\rm old},B)\) 등 더 낮은 차수 항을 누락할 수 있다. 식 (9.2)를 actual owner ladder의 임의 중간상태에 그대로 대입하지 않는다.

## 10. 유한시간 remainder의 nonautonomous 확장

새 augmented 상태를

\[
 \mathcal Y=(t,z,U,V,W),\qquad t'=1
\]

로 두고 식 (2.1)을 함께 사용한다. source의 explicit-time 함수와 그 derivative가 정의된 clock 구간 전체 및 전체 parameter rectangle을 tube에 포함해야 한다.

joint \((t,z)\)의 \(C^5\), guard 유지, 전체 augmented tube inclusion이 확보되면 PHYS02의 Taylor 적분 remainder가 그대로 성립한다. 예를 들어

\[
 m_4\le W_x^{(4)}(t;\lambda,S)\le M_4
\]

가 전체 extended tube에서 확인되면

\[
 \frac{I_x}{\lambda S}
 \in \frac{(K_3)_x\delta^3}{6}
       +\frac{\delta^4}{24}[m_4,M_4].
\tag{10.1}
\]

단, PHYS02의 frozen \([L_4,U_4]\)는 이 extended tube의 bound가 아니다. 새 coefficient functions, endpoint/freezing semantics, 공통 source family 및 guard를 bind하지 않고 PHYS02의 \(0.268818\%\) 수치를 재사용하지 않는다.

cell을 실제 이전 이력에서 이어 시작하면 \(U,V,W\)의 초기값이 일반적으로 0이 아니다. 그 경우 식 (2.1)은 여전히 맞지만 zero-initial cubic expansion 대신 해당 초기 감도를 보존한 Taylor polynomial과 remainder를 사용해야 한다.

## 11. 검산, source provenance와 실행 상태

check_nonautonomous.py는 표준 라이브러리 fractions.Fraction으로 실행된다. 독립적인 sparse multivariate polynomial differentiation과 time/parameter series recurrence를 비교한다. 실제 물리 이력을 생성하지 않는 대수 fixture이다.

수행한 확인은 다음과 같다.

- time-dependent photo coefficient/energy, HH amplitude, birth profile/direction, nonphoto coefficient, additive drift의 6 family와 6 parameter point, 총 36개에서 모든 5개 상태의 cubic/quartic 식이 exact 일치했다.
- 모든 case에서 cubic의 explicit-time derivative 소거, quartic의 \(S\) 독립성과 \(\lambda\) affine 성질을 확인했다.
- photon-independent nonphoto drift는 quartic까지 차이를 만들지 않았다. 별도 additive-drift fixture에서는 mixed \(x\)의 최초 차이가 5차임을 확인했다.
- leading Volterra kernel의 uniform/linear profile 적분, initial/terminal impulse, prebirth HH memory 항을 exact rational로 확인했다.
- 반복 birth+BE의 \(m=1,2,3,5,8\), \(\lambda_{\rm base}=0,1/3\) 10개 case에서 각 BE equation의 formal time series를 세 번의 polynomial substitution으로 전개했다. 모든 상태의 cubic coefficient가 식 (9.1)과 exact 일치했다. BE 근이나 유한 step 상태는 구하지 않았다.
- PHYS01 point coefficient의 \(\Xi_0,AqS_*\Delta^3\)만 provenance-bound로 읽어 70자리 Decimal profile/ladder 진단을 계산했다. interval certificate로 표기하지 않았다.

관련 evidence는 NONAUTONOMOUS_EXACT_CHECK.json, SOURCE_PROFILE_INPUT.json, COMMAND_STATUS.json, checker.stdout, checker.stderr이다. 실행한 scientific IVP/native/BE-root/NCP 횟수는 모두 0이다. 대수 checker의 최초 실패가 발생하면 FIRST_FAILURE.json을 create-only로 남기도록 구현했고, 현재 checker 실행에서는 실패가 발생하지 않았다. 문서의 첫 apply_patch는 LaTeX 줄의 patch prefix 누락으로 실패했으며 FIRST_ARTIFACT_WRITE_FAILURE.json에 별도 보존했다. 이 도구 형식 오류는 과학 검사 실패가 아니고 원 실패 때 문서는 생성되지 않았다.

상속 point-coefficient 파일의 SHA-256:

    c3d2f5404e01ea846f8faa3c60e824319eb04fb76c265e60ed821dc0a5411ada

원 선택 source JSON의 SHA-256:

    26a340065a9a99d02903bf0cc008baaf6ade00d2e845beb9d2b0b7d801316494

## 12. 근거 상태와 다음 연결

식 (2.1)–(10.1)은 명시된 smooth-cell 가정 아래 직접 유도(derived)이다. 새 coefficient 및 formal-map 관계는 exact nonphysical algebra fixtures로 검산했다. 실제 time-dependent 물리 family의 finite numerical certificate는 이 문서에서 생성하지 않았으며 actual-owner 연결은 unresolved이다.

호스트가 이 실행 문맥에 제공한 모델 라벨은 GPT-6 Astra Pro이다. 부모의 라벨로부터 자식 runtime을 추정하지 않았다. 별도 runtime attestation은 노출되지 않았다. 이전 독립 작업에서 읽은 지정 Astra v4.0.0 연구 하네스 및 이번 PHYS02 NEXT_HANDOFF를 적용했다. 이 산출물은 후보 생성과 검증설계에 참여한 독립 유도 담당자의 결과이며 최종 PROMOTE reviewer의 독립 판단으로 표기하지 않는다.

