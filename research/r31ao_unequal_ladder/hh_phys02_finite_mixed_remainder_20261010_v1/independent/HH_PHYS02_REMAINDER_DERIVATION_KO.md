# HH-PHYS02 독립 유도: 작은 HH 규모를 보존하는 유한시간 나머지

작성일 2026-10-10. 역할은 독립 유도 참여자이며 최종 decision reviewer가 아니다.

호스트가 이 실행 문맥에 제공한 모델 라벨은 GPT-6 Astra Pro이다. 이를 부모의 모델명으로부터 추정하지 않았다. 별도의 runtime model ID/attestation은 노출되지 않았으므로 그 의미의 신원 검증은 주장하지 않는다. 지정된 Astra 연구 하네스의 START_HERE, PROJECT_INSTRUCTIONS, MODEL_ROUTING 및 템플릿 RESEARCH_STATE를 읽었다. 템플릿 상태를 이전 연구 증거로 취급하지 않았다.

## 결론과 근거 상태

다음 결과는 직접 유도(derived)이다.

1. 네 번의 큰 해를 빼지 않고 혼합 감도 자체를 적분하면 정확한 \(\lambda S\) 인수를 얻는다. HH 감도와 혼합 감도를 \(q_0=q(z_0)>0\)로 정규화하면 나머지 계산에도 \(q_0\) 규모를 보존할 수 있다.
2. 전체 매개변수 직사각형에 공통인 augmented-state tube와 그 위의 혼합 감도 4차 시간도함수 상계를 확보하면, 실제 궤적을 수치 적분하지 않고도 \(t^3\) 항 뒤의 모든 고차항을 포함하는 유한시간 부호 인증을 얻는다.
3. 초기점의 4차 혼합 계수는 \(S\)에 무관하고 \(\lambda\)에 대해 affine이다. 따라서 네 모서리 차이의 \(t^4\) 항에는 \(\lambda^2S\)가 생기지만 \(\lambda S^2\)는 없다.
4. 현재 frozen HI-only source에서 \(t^4\)의 \(x\) 계수는 기존 광자들을 정확히 두 순간 \(\sum a_jP_j\), \(\sum a_jg_jP_j\)를 통해 참조한다. 유한시간 나머지의 enclosure에는 모든 활성 광자 bin의 개별 동역학을 보존해야 한다.

3번의 tensor 식과 매개변수 의존성은 별도의 비물리 polynomial fixture에서 유리수 exact arithmetic으로 확인했다. 이는 실제 FT03 수치점이나 native source의 검증을 대체하지 않는다.

## 1. 정의와 적용 범위

전체 상태는

\[
 z=(x,y_1,y_2,w,P_0,\ldots,P_{24}),\qquad
 w\ {\rm in\ eV/H},\quad P_j\ {\rm in\ photons/H}
\]

이며 시간은 proper seconds이다. 고정 stage 안에서 \(n_{\rm H},n_{\rm He}\), 광자 에너지, 단면적, 평균 팽창률은 고정한다. 기본 metric signature는 \((-+++)\)이나 이번 국소 반응식에 계량의 추가 사용은 없다.

\[
 \dot z=F(z;\lambda,S)=F_0(z)+\lambda H(z)+SB,\qquad
 H(z)=q(z)\eta,\quad
 \eta=(1,0,0,-\chi_{\rm H},0_{\rm photon}),
\]

\[
 B=e_{P_*},\qquad
 q=n_{\rm H}(1-x)^2k(T),\qquad
 T=\frac{2E_{\rm eV}}{3k_{\rm B}}
       \frac{w}{1+r+x+r(y_1+2y_2)}.
\]

\(r=n_{\rm He}/n_{\rm H}\), \(E_{\rm eV}\)는 eV→erg 변환상수이다. \(c,k_{\rm B}\)를 없애지 않는다. HH의 \(k(T)\)는 원 source의 LCS91 식이고, 쌍계수 \(1/2\)를 추가하지 않는다. \(\lambda\in[0,1]\), \(S\in[0,S_*]\), \(S_*=5\times10^{-15}\ {\rm H^{-1}s^{-1}}\)는 모형의 수학적 연속매개변수이다.

\(F_0\)에는 원 H/He CI, RR, DR, 그 열항, \(-2H_{\rm mean}w\), 그리고 기존 광자 25개 bin의 photo 항이 전부 들어 있다. 기존 photon source를 진공으로 바꾸지 않는다. 모든 \((\lambda,S)\)는 동일한 초기 전체 상태 \(z_0\)를 갖는다.

읽은 초기 입력은 PHYS01의 inputs/SELECTED_SOURCE.json이다. 초기 기체는 old_gas, 초기 광자는 old_point_photons이다. point_gas/point_photons, carry_gas, parent root box를 초기 시간 이력으로 대체하지 않는다. 선택 입력의 기록된 SHA-256은

    26a340065a9a99d02903bf0cc008baaf6ade00d2e845beb9d2b0b7d801316494

이다. 이 문서는 parent identity ledger를 인용하며 새 root/실제 이력의 인증을 하지 않는다.

고정된 물리 영역 \(D\)에 대해 \(F_0,H\in C^5(D)\)이고, 고려할 모든 궤적이 \(0\le t\le\Delta\) 동안 \(D\)에 남는다고 가정한다. 이 가정은 아래 tube 검사로 닫을 수 있다. HH source guard인 \(35000<T<60000\) K가 FT03 guard보다 엄격하다. 분율, 양의 열에너지, 양의 \(\Pi=1+r+x+r(y_1+2y_2)\)도 지켜야 한다.

현재 미분은 상태 및 \(\lambda,S\)에 대한 것이다. 고정 에너지가 cutoff 값에 놓이는 것과 에너지 자체가 시간에 따라 cutoff를 통과하는 것은 다르다. 고정된 zero-sigma branch는 상태에 대해 매끄럽다. redshift/hat-cell crossing, birth/reset, floor 전환을 포함하는 stage로 이 결과를 연장하지 않는다.

## 2. 정확한 혼합 감도와 Volterra 표현

\[
 a=\partial_\lambda z,\qquad b=\partial_S z,\qquad
 c=\partial_\lambda\partial_S z,
\quad J=F_z,\quad Q=F_{zz}.
\]

매개변수는 시간에 대해 상수이고 \(B\)가 상태에 무관하므로

\[
\begin{aligned}
 \dot a&=Ja+H,&a(0)&=0,\\
 \dot b&=Jb+B,&b(0)&=0,\\
 \dot c&=Jc+Q[a,b]+H'b,&c(0)&=0.
\end{aligned}
\tag{2.1}
\]

\(H'b\)는 \(\partial_\lambda F_z=H'\)에서 나온다. 대칭인 \(H'a\) 항을 추가하면 안 된다. \(S\)의 직접 forcing은 \(B\)로 상수이다.

\(\Phi(t,s)\)를 해당 \((\lambda,S)\) 궤적의 변분 전파자,
\(\partial_t\Phi=J(t)\Phi,\ \Phi(s,s)=I\)로 정의하면

\[
\begin{aligned}
 a(t)&=\int_0^t\Phi(t,s)H(z(s))\,ds,\\
 b(t)&=\int_0^t\Phi(t,s)B\,ds,\\
 c(t)&=\int_0^t\Phi(t,s)
    \{Q(z(s))[a(s),b(s)]+H'(z(s))b(s)\}\,ds.
\end{aligned}
\tag{2.2}
\]

이는 정확한 Volterra 표현이다. \(F_0\)의 다른 반응들은 \(J,Q,z(s),\Phi\)에 남는다.

유한한 네 모서리 차이는 기본정리 두 번으로

\[
 I_z(t;\lambda,S)
 =\int_0^\lambda d\alpha\int_0^S d\beta\ c(t;\alpha,\beta)
 =\lambda S\int_0^1 da\int_0^1 db\
       c(t;a\lambda,bS).
\tag{2.3}
\]

따라서 감도에 대한 uniform enclosure를 쓰면 \(\lambda S\)를 빼앗기지 않는다. 원래 상태 \(x\simeq0.9\)의 네 float 값을 독립적으로 계산한 뒤 \(10^{-17}\) 수준의 차이를 취하는 방식은 이 규모를 보존하지 못할 수 있다.

### \(q_0\)까지 보존하는 선택적 정규화

이번 초기점은 \(q_0=q(z_0)>0\)이다. \(\widehat a=a/q_0\), \(\widehat c=c/q_0\), \(\widehat H=H/q_0\)로 두면

\[
\begin{aligned}
 \dot{\widehat a}&=J\widehat a+\widehat H,\\
 \dot b&=Jb+B,\\
 \dot{\widehat c}&=J\widehat c+Q[\widehat a,b]+\widehat H'b.
\end{aligned}
\tag{2.4}
\]

그리고 \(I_z=\lambda S q_0\langle\widehat c\rangle\)이다. \(q_0\)는 매개변수에 독립인 고정 초기값이므로 이 정규화는 exact이다.

소스 매개변수를 \(s=S/S_*\)로 구현한다면 \(\partial_s z=S_*b\), \(\partial_\lambda\partial_s z=S_*c\)이다. 동시에 \(b=(\partial_s z)/S_*\), \(\widehat c=(\partial_\lambda\partial_s z)/(q_0S_*)\)를 쓰면 식 (2.4)가 그대로 된다. \(S_*\)가 두 번 곱해지거나 나눠지지 않도록 계약에 명시한다.

이 정규화는 필수는 아니다. 작은 실제 감도 폭을 유지하는 interval arithmetic으로도 같은 bound를 얻을 수 있다. 다만 정규화는 초소형 HH 신호가 큰 일반 상태오차에 묻히는 것을 막는 유용한 수치 선택이다.

## 3. 유한시간 remainder 정리

PHYS01에서 이미 유도한 초기 혼합계수

\[
 K_3=c^{(3)}(0),\qquad
 (K_3)_x=-Aq_0(4+\Xi_0),\qquad
 A=cn_{\rm H}\sigma_{\rm H}(E_*)
\]

를 상속한다. 또한 \(c(0)=c'(0)=c''(0)=0\)이다. 이 \(K_3\)는 초기점의 \(\lambda,S\)에 무관하다.

모든 \(0\le t\le\Delta\), \(0\le\lambda\le1\), \(0\le S\le S_*\)에 대해

\[
 m_4\le\widehat c_x^{(4)}(t;\lambda,S)\le M_4
\]

를 확보했다고 하자. Taylor의 적분형 나머지는 정확히

\[
 \widehat c_x(t)
  =-\frac{A(4+\Xi_0)t^3}{6}
   +\frac{1}{6}\int_0^t(t-s)^3\widehat c_x^{(4)}(s)\,ds
\]

이고, 시간 가중치가 음수가 아니므로

\[
 \boxed{\frac{I_x(t;\lambda,S)}{\lambda S q_0}
   \in-\frac{A(4+\Xi_0)t^3}{6}
      +\frac{t^4}{24}[m_4,M_4].}
\tag{3.1}
\]

\(\lambda S=0\)이면 분모를 계산하지 않고 \(I_x=0\)를 exact하게 반환한다. 양의 매개변수에서 위 식을 사용한다.

절댓값 상계 \(\mathcal M_4\ge\max(|m_4|,|M_4|)\)만 있다면

\[
 \left|I_x+\frac{\lambda S A q_0(4+\Xi_0)t^3}{6}\right|
 \le\frac{\lambda S q_0\mathcal M_4t^4}{24}.
\tag{3.2}
\]

따라서 \(A>0\), \(q_0>0\), \(4+\Xi_0>0\)와

\[
 \Delta\mathcal M_4<4A(4+\Xi_0)
\tag{3.3}
\]

가 함께 확인되면 \(0<t\le\Delta\), 양의 \(\lambda,S\)에서 \(I_x<0\)이다. signed upper bound \(M_4\)를 쓰는 판정이 절댓값 bound보다 더 날카로울 수 있다.

식 (3.1)은 4차 항 하나의 추정이 아니다. 그 뒤의 모든 시간 차수가 적분 나머지 안에 포함된다. 큰 시각의 점별 상태들을 차분한 결과도 아니다.

### 정규화 시간 \(\tau=t/\Delta\)를 쓸 때

실제 변수 \(W=\partial_\lambda\partial_s z\)에 대해

\[
 W_x(\tau)=C_3\tau^3+R_4(\tau),\qquad
 C_3=-\frac{S_*Aq_0(4+\Xi_0)\Delta^3}{6}.
\]

전체 augmented tube의 arbitrary point에서 계산한 ordinary time-jet의 4차 계수가 \([L_4,U_4]\)에 들면

\[
 W_x(1)\in C_3+[L_4,U_4],
\quad I_x(\Delta;\lambda,S)\in
  \lambda(S/S_*)\{C_3+[L_4,U_4]\}.
\tag{3.4}
\]

ordinary Taylor jet은 이미 \(W_\tau^{(4)}/4!\)를 저장한다. \([L_4,U_4]\)를 다시 24로 나누면 안 된다. \(\tau=1\)이므로 추가 \(\Delta^4\)도 다시 곱하지 않는다. 시간 scaling을 하지 않은 코드에는 식 (3.1)을 사용한다.

## 4. 계산 가능한 enclosure 절차

정규화 여부를 고정하고 \(Y=(z,a,b,c)\) 또는 그 정규화 변수의 RHS를 식 (2.1)/(2.4)로 정의한다. 원 source의 계산 그래프를 hyperdual parameter algebra와 time jets에 평가해도 동일하다.

1. 전체 \((\lambda,S)\) 직사각형에 대해 공통인 compact box \(\mathcal Y\)를 제안한다. \(Y_0=(z_0,0,0,0)\)를 포함한다.
2. 모든 기체 상태가 물리 분율, 양의 \(w,\Pi\), HH 온도 guard 안에 있음을 interval로 확인한다.
3. outward interval로

   \[
    Y_0+[0,\Delta]\,G(\mathcal Y,[0,1],[0,S_*])
       \subset\operatorname{int}\mathcal Y
   \tag{4.1}
   \]

   를 확인한다. \(\tau\)를 쓰면 \([0,\Delta]G\)를 \([0,1]G_\tau\)로 바꾼다.

4. inclusion이 닫힌 뒤 전체 \(\mathcal Y\)를 arbitrary initial point로 놓고 time-jet recurrence를 4차까지 평가하여 혼합 감도 성분의 fourth derivative 또는 fourth coefficient를 구한다.
5. 전체 매개변수 직사각형의 signed bound로 식 (3.1) 또는 (3.4)를 평가한다. leading cubic은 정확한 초기 계수를 사용한다.

식 (4.1)이 참이고 RHS가 국소 Lipschitz이면 해가 box 경계에 최초로 도달할 수 없다는 first-exit 논증으로 전체 시간구간의 잔류가 따른다. compact 영역에서 존재시간도 연장된다. 따라서 수치 trajectory를 먼저 생산할 필요가 없다. contraction factor \(<1\)은 이 sufficient no-exit criterion에 추가로 필요한 조건이 아니다.

실제로 일정한 좌표에 대해 singleton interval을 유지한다면 strict inclusion은 그 불변 affine subspace의 relative interior에서 적용한다. 현재 \(a_j=0\)이고 source가 들어오지 않는 16개 광자 bin은 정확히 \(P'_j=0\)이다. 그 좌표를 기록한 채 exact elimination해도 원 25-bin 초기상태와 물리적 의미를 보존한다.

augmented RHS는 \(F_{zz}\)를 포함한다. 그 RHS의 세 번의 시간미분으로 혼합 감도의 4차 시간도함수를 얻으므로 \(F_0,H\in C^5\)면 충분하다. 전체 box 위의 높은 derivative가 필요한 점을 초기점의 낮은-order coefficient 계산과 혼동하지 않는다.

임의 폭의 box를 매번 키워도 inclusion이 실패하거나 나머지 bound가 부호를 닫지 못하면 실패를 보존한다. 더 작은 \(\Delta\), state scaling, parameter subdivision, 구조를 보존하는 jet 표현은 가능한 대응이다. uniform coarse bound의 실패를 물리적 부호 반전으로 판정하지 않는다.

## 5. 4차 초기 혼합계수의 tensor 식

이 절의 모든 값은 \(z_0\)에서 해당 \((\lambda,S)\)를 고정해 평가한다.

\[
 F=F_0+\lambda H+SB,\quad J=F_z,\quad Q=F_{zz},\quad
 C=JB=Au\,d,\quad d=(1,0,0,g, -e_{P_*}),
\]

여기서 \(u=1-x\), \(g=E_*-\chi_{\rm H}\)이다.

현재 photo RHS는 gas와 photon 사이에 bilinear이고 \(H\)는 photon-independent이다. 따라서

\[
 H'B=0,\quad H''(B,\cdot)=0,\quad Q(B,B)=0,\quad
 F'''(B,\cdot,\cdot)=0.
\tag{5.1}
\]

세 번째 조건은 photon에 선형이라는 데서, 네 번째 조건은 photo의 gas 의존성도 affine이라는 데서 나온다. 단순히 photon 선형이라는 조건만으로 네 번째 조건을 주장하면 안 된다.

식 (2.1)을 초기점에서 시간미분하면

\[
\begin{aligned}
 a'(0)&=H,&a''(0)&=JH+H'F,\\
 b'(0)&=B,&b''(0)&=C,\\
 b'''(0)&=JC+2Q(F,B).
\end{aligned}
\]

이를 혼합 감도식에 대입하면

\[
 K_3=H'C+2Q(H,B)
\]

와

\[
\boxed{
\begin{aligned}
 K_4:=c^{(4)}(0)
  ={}&JK_3+3Q(B,JH+H'F)+3Q(H,C)\\
    &+H'[JC+2Q(F,B)]+3H''(F,C).
\end{aligned}}
\tag{5.2}
\]

를 얻는다. 예를 들어 \(Q[a,b]\)의 세 번의 시간미분은 초기점에서

\[
 3Q(a''(0),B)+3Q(H,C)+6F'''(F,H,B)
\]

이고 마지막 항은 식 (5.1)로 0이다. \(H'b\)의 세 번의 시간미분에서 \(H'b'''(0)+3H''(F,C)\)가 남는다. \(Jc\)에서는 \(JK_3\)만 남는다.

독립적인 확인은 \(z^{(4)}=J^3F+JQ(F,F)+3Q(F,JF)+F'''(F,F,F)\)를 \(\lambda,S\)로 미분하는 것이다. 같은 식 (5.2)를 얻는다.

### 매개변수 의존성

\(C=F_0'B\)와 \(K_3\)는 \(\lambda,S\)에 무관하다. 식 (5.2)의 \(S\)는 \(F=F_0+\lambda H+SB\)의 위치에서만 나타나며 식 (5.1)로 소거된다. \(\lambda\)의 차수는 최대 1이다.

\[
 K_4(\lambda,S)=K_{40}+\lambda K_{41},
\tag{5.3}
\]

\[
\boxed{
 K_{41}
 =2H'^2C+4H'Q_0(H,B)
   +6Q_0(H'H,B)+6H''(H,C).
}
\tag{5.4}
\]

여기서 \(J_0=F_0'\), \(Q_0=F_0''\)이며 \(K_{40}\)는 식 (5.2)에 \(\lambda=S=0\)를 넣은 것이다.

따라서 유한한 네 모서리 차이는 국소적으로

\[
 I_z=\lambda S\left\{
  \frac{K_3t^3}{6}
  +\frac{[K_{40}+(\lambda/2)K_{41}]t^4}{24}
 \right\}+O(\lambda S t^5).
\tag{5.5}
\]

여기서 \(O(t^5)\)는 추가 매끄러움에서의 국소 확장 표기이다. 실제 유한시간 인증에는 5차 bound를 새로 요구하지 말고 식 (3.1)의 4차 적분 remainder를 사용하면 된다. 원 source의 guard 내부 analytic 식은 충분히 매끄럽지만 native 분기 전체의 매끄러움을 뜻하지 않는다.

## 6. source 구조를 드러내는 4차 식

\(q_v=Dq[v]\), \(q_{v,w}=D^2q[v,w]\), \(\eta=(1,0,0,-\chi,0)\), \(d=(1,0,0,g,-e_{P_*})\)로 표기한다. 두 방향의 gas \(x\) 성분은 1이다.

\[
 Q(B,v)=-A v_xd,\qquad H=q\eta,\quad H'v=q_v\eta.
\]

식 (5.2)를 전개하면

\[
\boxed{
\begin{aligned}
 K_4=A\{&
   u q_d\,J\eta-2q\,Jd
   -3[q(J\eta)_x+q_F]d
   +3uq\,Q(\eta,d)\\
   &+\eta[uq_{Jd}-2F_xq_d+3u q_{F,d}]
  \}.
\end{aligned}}
\tag{6.1}
\]

\[
\boxed{
 K_{41}=A\eta\{2u q_dq_\eta-4q q_d+6u q q_{\eta,d}\}
          -6Aq q_\eta d.
}
\tag{6.2}
\]

특히 \(x\)에서는 두 벡터 \(\eta,d\)의 \(x\) 성분이 1임을 사용하면 된다. \(K_{40}\)에는 비광자 H/He 반응과 thermal/expansion drift의 첫째·둘째 도함수가 명시적으로 남는다. 네 번째 시간차수의 부호가 세 번째 계수와 같아야 한다는 정리는 없다.

### 기존 25개 bin이 4차 \(x\) 계수에 들어오는 방식

현재 선택 입력의 He photo 단면적은 모두 0이다. \(a_j=cn_{\rm H}\sigma_{{\rm H},j}\), \(g_j=E_j-\chi_{\rm H}\)로 놓고 기체의 비광자 RHS를 \(N(y)\), \(y=(x,y_1,y_2,w)\)로 정의하면 원 frozen source는

\[
\begin{aligned}
 \dot y &=N(y)+u\sum_j a_jP_j e_j+\lambda qh,\\
 \dot P_j &=-a_juP_j+S\delta_{j*},\\
 e_j&=(1,0,0,g_j),\qquad h=(1,0,0,-\chi_{\rm H}).
\end{aligned}
\tag{6.3}
\]

\(N\)에는 H/He의 모든 nonphoto 및 열·팽창항이 포함된다. 즉 \(N\)을 물리적으로 작은 근사함수로 바꾸는 것이 아니다.

초기점에서

\[
 m=\left(\sum_j a_jP_j,\ 0,\ 0,\ \sum_j a_jg_jP_j\right)
      =(\Gamma_0,0,0,G_0),\qquad e=e_*,
\]

\[
\begin{aligned}
 f&=N+u m+\lambda qh,\\
 a&=N'h-m+\lambda hq_h,\\
 b&=N'e-m-Au e+\lambda hq_e,\\
 d_2&=N''(h,e)+A e+\lambda hq_{h,e}.
\end{aligned}
\]

이때 \(a=(J\eta)_{\rm gas}\), \(b=(Jd)_{\rm gas}\), \(d_2=Q(\eta,d)_{\rm gas}\)이고

\[
\boxed{
 (K_4)_{\rm gas}=A\{
  u q_e a-2q b-3(q a_x+q_f)e
  +3uqd_2
  +h[uq_b-2f_xq_e+3u q_{f,e}]
 \}.}
\tag{6.4}
\]

따라서 초기 \(K_4{}_x\)의 기존 photon 의존성은 \(\Gamma_0,G_0\) 두 순간으로 정확히 표현된다. bin마다 \(a_j\)가 다르므로 그 두 순간만으로 전체 시간진화를 닫을 수는 없다. 예를 들어

\[
 \dot\Gamma=-u\sum_j a_j^2P_j+AS
\]

에서 이미 새 순간이 필요하다. 유한시간 enclosure에 spectrum 전체를 유지해야 하는 구체적 이유다.

## 7. 경계, 실패 모드, claim ceiling

- 초기 전체 상태를 공유하지 않으면 \(a(0),b(0),c(0)\)가 0일 이유가 없다. 혼합 응답의 \(t^0,t^1,t^2\) 항이 생길 수 있으므로 실제 ON/OFF history 차이를 여기의 same-IC 차이로 재해석하지 않는다.
- \(q_0>0\) 정규화는 이번 내부 초기점에 대한 것이다. \(x_0=1\)이면 \(q_0=0\)이나 이후 RR이 중성수소를 만들 수 있다. 이때 실제 혼합 응답 전체가 \(q_0\)에 비례한다고 주장할 수 없다. 그런 경계에는 \(q\)의 전체 polynomial \(n_{\rm H}u^2k(T)\)를 유지하고 별도의 supremum 또는 다른 초기차수 분석을 써야 한다.
- \(1/u\) 표현은 내부점의 해석용이다. rate/Hessian 구현에서 원 \(u^2\) 식을 유지하면 \(u=0\)에서 \(q=dq=0\), \(q_{xx}=2n_{\rm H}k\)가 유한하다.
- fixed-energy zero-sigma bin의 exact elimination은 가능하다. 활성 bin을 평균 opacity 하나로 바꿔 finite-time bound를 계산하면 식 (6.3)을 바꾸게 된다.
- interval width, roundoff, large-state subtraction으로 생긴 음수/양수는 물리적 상호작용의 부호 증거가 아니다. 실패한 enclosure는 numerical enclosure failure로 분류한다.
- rate floor, source-law reset, photon birth, energy cutoff crossing에는 piecewise sensitivity 및 event map이 필요하다. smooth tube theorem은 그 event를 가로지르지 않는다.
- HH/source strength를 고정 LCS와 연속 source의 수학적 매개변수로 보는 계약을 유지한다. \(\lambda\)를 physical fit uncertainty, KS/LCS mixing, 혹은 full-history ON/OFF probability로 바꾸지 않는다.
- 이 결과는 지정된 ideal-real frozen ODE의 derived/numerically checked 주장에 한정된다. native binary64 중간연산 rounding, BE root existence/uniqueness, actual owner chronology, NCP나 전체 cosmological transport의 인증이 아니다.
- source 상수를 binary64 leaf의 exact real로 해석하는 것과 native가 예컨대 DR prefactor의 중간 곱셈을 binary64로 계산한 결과를 exact real로 해석하는 것은 서로 다른 모형이다. 구현 계약에서 어느 쪽인지 명시해야 한다.

## 8. 수행한 검증과 권장 acceptance checks

실행한 경량 검증:

    python theory_independent/check_k4.py

결과 파일은 K4_EXACT_CHECK.json이다. 정확한 유리수 \(3\) gas+\(2\) photon 다항식 모형에서 독립적인 시간/매개변수 series recurrence와 식 (5.2)를 비교했다. 6개 매개변수 조합에서 모든 상태성분이 exact 일치했고, \(S\) 독립성과 \(\lambda\) affine 관계 및 식 (6.2)가 exact 일치했다. 과학 rate를 사용하지 않은 대수 검증이며 물리적 수치 certificate가 아니다. IVP 적분, native dispatch, BE/NCP root 계산은 실행하지 않았다.

실제 enclosure의 의미 있는 확인 항목은 다음과 같다.

1. 선택 old_gas+old_point_photons와 source index 24, 정확한 상수 의미를 고정한다.
2. time0에서 \(a=b=c=0\), \(c'=c''=0\)를 확인하고 상속된 cubic coefficient를 재사용한다.
3. 16 inactive bins가 정확히 zero derivative이고 남은 9개 bin이 별도로 전파됨을 확인한다.
4. augmented tube inclusion, 온도·분율 guard, 전체 \(\lambda,s\) rectangle을 검사한다.
5. ordinary jet의 factorial convention과 \(\tau=t/\Delta\) 변환을 교차 확인한다.
6. \(S=0\) 또는 \(\lambda=0\)이면 혼합 응답을 exact zero로 처리한다.
7. fourth initial coefficient의 \(S\) 독립·\(\lambda\) affine 관계를 실제 source에서도 점검하면 sparse algebra의 누락을 찾는 데 유용하다. 이것은 전체 time bound와 별도 검사다.

## 9. 읽은 source의 범위

PHYS01의 THEORY_KO.md와 INPUT_IDENTITY.json 및 SELECTED_SOURCE.json을 읽었다. Rust 원문 중 HH rate와 gas jet, FT03의 analytic rate 전체, ft03_rhs와 초기 model, coupled primary의 model/valid/raw/lower/photo/endpoint 정의, HHe 기본 상수를 읽었다. root solver 및 native integration 경로를 실행하거나 재감사하지 않았다. 사용한 하네스 state는 NOT_RUN 템플릿임을 확인했다.

이 문서의 새로운 정리·4차 tensor식·moment reduction은 직접 유도이다. 기존 PHYS01의 cubic coefficient와 초기 물리설정은 상속된 결과로 명시적으로 분리했다.
