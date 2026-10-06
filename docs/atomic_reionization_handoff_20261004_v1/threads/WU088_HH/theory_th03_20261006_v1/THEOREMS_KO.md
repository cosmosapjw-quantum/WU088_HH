# HH-TH03 핵심 정리와 적용 범위

전체 증명은 START의 ZIP/THEORY_KO.md에 있다. 아래는 직접 유도의 검색용 요약이다.

## 1. 같은 photon cohort의 생존비

서명(-+++),proper seconds, prescribed H_i=H(1+epsilon,1-epsilon,1), nH=nH0 exp(-3Ht), 공통온도 zero-tilt S0-derived model을 유지한다. 한 geometry와 HH provider를 고정하고 1=ON,0=OFF,u_l=1-h_l,delta=h1-h0라 쓴다. 같은 birth(t_b,E_b,n_b,p_b)와 characteristic을 갖는 HI-only 흡수 cohort를 다룬다. source/산란/재분배로 같은 cohort를 중간에 채우지 않는다. per-H photon에는 추가 -3H 항이 없다.

a(t)=c*nH(t)*sigma_H(E(t)), p_l'=-a*u_l*p_l,
U_l=int_birth^t a*u_l, S=U0-U1=int_birth^t a*delta.

p_b>0와 유한 U_l에서 integrating factor로 p_l=p_b exp(-U_l)이므로

p1/p0=exp(S), Delta p=p0*expm1(S).

이것은 gas를 동결한 근사가 아니다. 실제 h_l(t)를 그대로 사용한 항등식이다. p_b=0이면 두 p가0이고 log ratio 대신 아래 식을 쓴다:

Delta p'=-a*u1*Delta p+a*p0*delta.

따라서 이전 Delta p와 적분 source를 variation-of-constants로 전파한다. 새 slab/event에서 S나 incoming error를0으로 reset하지 않는다. 진짜 동일 birth에서만 S=0이다.

두 a가 달라 a1=a0+Delta a이면 S'=a0*delta-u1*Delta a다. 같은 macro-grid만으로 Delta a=0이라 할 수 없다. fixed-energy bin 사이에 수송 유입이 있는 전체 F08에는 단일-cohort 생존비를 직접 대입하지 않는다.

## 2. Terminal 흡수 차이와 부호

R_l=a*u_l*p_l이면

Delta R=a*p0*[u1*expm1(S)-delta].

TH02 terminal 조건(매끄러운 prehistory,횡단,identity reset,해당 group 분류) 아래

K_Dh=-|tau'|*Delta R.

u0,u1>0이면 Delta R>0 iff S>log(u0/u1). 중성수소 감소와 누적 photon 생존이 경쟁하므로 endpoint delta의 부호만으로 순간 흡수 차이를 정하지 않는다. 실제 S0에서 부호반전을 관측했다는 뜻은 아니다. 경계에서는 log 대신 division-free 식을 쓴다.

같은 birth에서 누적 photo사건 차이는 Delta J_photo=-Delta p다. H photo만이 photon sink인 원 S0에서 초기 차이가0이면
Delta h+sum Delta p=J_HH+Delta J_eCI-Delta J_HRR.
따라서 J_HH와 최종 Delta h를 동일시하지 않는다. 추가 H반응은 해당 장부항을 더한다.

## 3. 포화하는 상계

B_h=sup_birth..t*|delta|,b_h=|delta(t*)|,Lambda_bar>=int a를 둔다. U0,U1>=0이므로

|exp(-U1)-exp(-U0)|=exp(-min U)*(1-exp(-|U1-U0|))
<=1-exp(-Lambda_bar*B_h).

따라서 |Delta p|<=p_b*(1-exp(-Lambda_bar*B_h)). 이 식은 큰 구간에서 exp(+Lambda B)로 발산하지 않는다. P=|tau'|*a_cut*p_b라 하면

|K_Dh|<=P*min{1,b_h+1-exp(-Lambda_bar*B_h)}
       <=P*min{1,(1+Lambda_bar)*B_h}.

B_h=0이면 K_Dh도0이다. B_h가 아직 없을 때의 P는 물리적 분율 범위만 사용한 넓은 a-priori source contribution envelope다. 실제 signed kink, 동시group 전체, 전구간A를 인증한 것이 아니다.

w=eV/H,Pi=1+h+r(1+y1+2y2),T=Cw/Pi,C=2eV_erg/(3kB),Theta=C(Ec-chi)라 두면 B_l=(Theta-T_l)/Pi_l,
K_DT=-|tau'|[B1*Delta R+R0*Delta B],
Delta B=-Delta T/Pi1-(Theta-T0)*Delta Pi/(Pi1*Pi0).

35000<=T<=60000,Pi>=1.083에서 single-path K_T는0..P*M_T,M_T=(60000-Theta)/1.083에 있다. ON/OFF 차이도 |K_DT|<=P*M_T. 더 좁은 bound에는 b_T,b_Pi를 함께 운반한다. 임의 thermal/helium closure를 추가하지 않는다.

Adjoint source 방향 zeta_l=psi_h+(Ec-chi)*psi_w-psi_pj를 쓰면 W_l=zeta_l*R_l이고 Delta W=zeta1*Delta R+R0*Delta zeta다. 실제 adjoint/tube는 아직 계산하지 않았다.

## 4. 두 source-specific 계수 구간

TH02의 두 exact-real epsilon root와 |tau'| 구간은 재계산 없이 계승했다. H=1e-14/s,Eb=13.7eV,Ec=13.6eV,t*=8e11s,nH0=1e-4/cm3,c=29979245800cm/s 및 고정 Verner HI 계수는 exact decimal이다. p_b는 local153MB ON05B FROZEN_GRID의 두 실제 packet_number float를 exact dyadic으로 읽었다. 원격413MB 동명 archive와 혼합하지 않았다.

HI x=E/.4298,Pfit=2.963에서 sigma=54750e-18*(x-1)^2*x^(Pfit/2-11/2)*(1+sqrt(x/32.88))^(-Pfit). 로그미분
2x/(x-1)+Pfit/2-11/2-(Pfit/2)*sqrt(x/32.88)/(1+sqrt(x/32.88))
의 정확한 음의 상계로13.6..13.7eV에서 감소를 증명했다.

Lambda<=c*nH0*sigma(Ec)*(exp(-3Htb)-exp(-3Ht*))/(3H).

| birth / index | 안전한 Lambda 상한 | P 상한 | P*(1+Lambda) 상한 |
|---|---:|---:|---:|
|6.5e10s / 9|13.804|7.095e-6|1.051e-4|
|7e10s / 8|13.709|6.998e-6|1.030e-4|

따라서 각각 |K_Dh|<=1.051e-4*B_h, 1.030e-4*B_h다. 실제 B_h는 null이며 finite-grid endpoint 차이를 연속 B_h로 대입하지 않았다. 온도prior 상한은0.394K/shear,0.388K/shear로 넓다. 실제 부호/작은 신호의 검출은 여전히 미확정이다.

sigma(Ec)≈6.346296358990491267e-18cm2,a_cut≈1.857453645150412529e-11/s다. 이 fit에 대한 산술 구간이며 물리적 단면적 오차를 포함하지 않는다. TH02 root의 exact-real convention을 native 반복 normalize/pullback 인증으로 바꾸지 않는다.

## 5. BE source의 상관형 residual

eta=a*dt, rho_l=(1+eta*u_l^+)p_l^+-p_l^-를 recorded 값의 exact-real residual로 정의한다. 그러면

(1+eta*u1^+)Delta p^+=Delta p^-+eta*p0^+*delta^++Delta rho.

exact residual0의 positive cohort에서 log ratio 증분은 log1p[eta*delta^+/(1+eta*u1^+)]다. 이것은 discrete식이고 연속 int a delta와 같지 않다. 실제 residual과 이전차이를 보존하며 p,ne,1-h로 나누지 않는다.

eta1=eta0+Delta eta이면
(1+eta1*u1^+)Delta p^+=Delta p^-+[eta0*delta^+-Delta eta*u1^+]*p0^++Delta rho.

공통 opacity가 깨진 경우의 항도 버리지 않았다. source-only photon소거에는 쓸 수 있지만 실제fixed-grid수송에는 별도 operator와 remap residual이 필요하다. 이번은 native 구현/실행이 아니다.

## 검산과 미해결 조건

최종97assertions=기호14+exactrational64+고정밀보조19,2개의새sourceenvelope,exit0/stderr0. 첫Symbolic simplify가양의거듭제곱잔차를0으로정리하지못한실패를보존했다. 동일식의positive-square치환/together-cancel에서0확인후정규화만수정했다. 중간95성공후mismatch식2개를추가해최종97성공. 3invocations를3개의독립과학결과로합산하지않는다.

Interval산술은Fraction과10^-70outward grid, expTaylor64+tail/range-reduction, logatanh96+tail, integer sqrt를사용했다. mpmath110자리 대조는 보조다. 형식검증/TDD/독립agent심사 없음. BE대수36사례는물리시뮬레이션이아니다.

실제gas/optical-memory 구간, terminal group 정칙성, adjoint weight, actualONrootbox, 전체history/HH물리율 정확도는OPEN. Native/Rust/BEroot/IVP/history/HHfit/oldproofsuite실행0. 새photo단면적endpoint2개만평가했다. 연구ACTIVE/S0OFFcontrol/기존criteria/legacy를보존한다.
