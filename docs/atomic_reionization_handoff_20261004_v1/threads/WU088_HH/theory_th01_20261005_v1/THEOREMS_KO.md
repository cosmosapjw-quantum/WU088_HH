# HH-TH01의 계산식과 주장 범위

전체 증명은 START에 지정한 ZIP의 HH_TH01_20261005_v1/THEORY_KO.md에 있다. 아래는 별도 검색용 요약이다.

## 축 교환과 비매끄러움

H_i=H(1+eps,1-eps,1), 서명(-+++), proper seconds, 고정 양의 H, 공통 온도의 등방 기체와 scalar observable를 가정한다. Photon birth measure와 모든 규칙이 x/y permutation P에 불변 또는 equivariant이고 해가 유일하면 O(-eps,lambda)=O(eps,lambda)다. D=O(eps,lambda)-O(eps,0), A=D(eps,lambda)-D(0,lambda)도 짝함수다. C2와 유계 혼합 미분의 추가 가정 아래

A=int_0^lambda dl int_0^eps (eps-s) O_lee(s,l) ds,
|A|<=lambda eps^2 sup|O_lee|/2.

짝함수라는 것만으로 C2는 나오지 않는다. Neutral fraction u=1-h에 대해 du/dt=-a_eps(t)u-lambda*b*u^2, a_eps=kappa/2[1_(t<t0/(1+eps))+1_(t<t0/(1-eps))]를 둔다. 상수 a의 정확한 흐름은 Phi_a(s,u)=u exp(-as)/(1+lambda*b*u*(1-exp(-as))/a)다. eps>0에서 t0의 해는 Phi_(kappa/2)(t0-tau_fast,Phi_kappa(tau_fast,u0))다. 미분하면 A=(kappa*t0/2)D(0,lambda)|eps|+O(eps^2)를 얻는다. 이는 quadratic-HH를 유지하는 해석적 반례이며 S0 물리 예측이 아니다.

Photon age a의 에너지는 E=Eb exp(-Ha)sqrt(nx^2 exp(-2epsHa)+ny^2 exp(2epsHa)+nz^2)다. S=nx^2-ny^2, P=nx^2+ny^2, a0=ln(Eb/Ec)/H이면 crossing의 eps 미분은 a1=-a0*S, a2=2a0*S^2+2H*a0^2*(P-S^2)다. |eps|<1에서 a0/(1+|eps|)<=a_cross<=a0/(1-|eps|). 새 parameter roots는 수치 진단이고 actual negative-shear history 또는 parity certificate가 아니다.

단일 횡단 event와 identity reset에서 DeltaF=after-before, z_eps^+=z_eps^- -DeltaF*tau_eps다. 처방된 geometry이므로 tau_lambda=0이고 z_lambda는 연속이다. Mixed jump는 -[D_zDeltaF*z_lambda+partial_lambda DeltaF]*tau_eps다. Photon cutoff의 명시적 HH source는 양쪽에서 같아 마지막 partial 항은 0이어도 state-sensitivity 항은 일반적으로 남는다. Binding 13.5984 경계의 retained full state에는 DeltaF=0이다. Inventory reporting boundary는 별개다.

일반 framework는 Kong etal, arXiv2306.06862v3, DOI10.1109/JPROC.2024.3440211 및 Burden etal, arXiv1407.1775v3, DOI10.1137/15M1016588을 확인했다. 개별 saltation과 동시 guard의 piecewise differentiability를 구별한다. HH 대입과 반례는 이번 직접 유도다.

## Source 미분과 근 인증

y=(h,y1,y2,w), w=eV/H, r=nHe/nH,
Pi=1+h+r(1+y1+2y2), C=2(eV_erg)/(3kB), T=Cw/Pi, W=1-h.
p=(1,r,2r,0), d=(1,0,0,0), e=(0,0,0,1).

Ti=T(ei/w-pi/Pi),
Tij=T[2pi*pj/Pi^2-(ei*pj+ej*pi)/(w*Pi)],
qi=nH[-2Wdi*k+W^2*k'*Ti],
qij=nH[2di*dj*k-2W*k'*(di*Tj+dj*Ti)+W^2*(k''*Ti*Tj+k'*Tij)].

k=A*T^p*exp(-B/T)에서
k'=k[p/T+B/T^2],
k''=k[p(p-1)/T^2+2B(p-1)/T^3+B^2/T^4].

적용 범위는 analytic 연구창이며 raw floor를 smoothing하지 않는다. h=1에서 gradient=0, qhh=2nH*k로 유한하고 1/ne나 1/W가 필요 없다. c=(1,0,0,-chi)에서 chi는 binding eV다. JHH=c gradq^T, Hessian 성분은 c_a*qij다. ell=(chi,0,0,1)은 HH channel의 source/J/H를 소거하지만, 팽창하는 기체 전체의 에너지가 보존된다는 뜻은 아니다.

Rlambda=y-y0-dt[F0(y)+lambda*c*q(y)], M0=I-dt*DF0(y)로 둔다. 같은 ON candidate에서 d=1-dt*lambda*gradq^T*M0^-1*c를 정의하면 detMlambda=detM0*d다. d!=0일 때 rank-one inverse 식을 쓸 수 있다. M0=[[1,0],[-3,1]], c=(1,-1), g=(-1,1), dtlambda=1의 정확한 반례에서는 gc=-2여도 det(M0-cg)=0이다. 실제 S0에서 singularity를 관측한 것이 아니다.

실제 근에는 새로운 physical ball B, 고정된 nonsingular preconditioner C0와 다음 조건이 충분하다.
kappa=sup_B||I-C0DRlambda||<1,
||C0Rlambda(center)||+kappa*radius<=radius.

서로 다른 단위의 state는 고정된 무차원 scales로 정규화한다. 원 OFF certificate의 중심·box·Hessian을 변경 없이 ON에 붙이지 않는다. Actual box에 이 조건을 적용하는 계산은 아직 수행하지 않았다.

## 네 경로의 연속오차 항등식

Smooth slab에서 e_lg=z_lg-zhat_lg, r_lg=zhat'_lg-F_lg(zhat_lg), J_lg=int_0^1 DF_lg(zhat+theta e)dtheta로 둔다. delta_g=e_1g-e_0g, DeltaJ_g=J_1g-J_0g, Deltar_g=r_1g-r_0g, ae=delta_B-delta_F이면

ae'=J_1B ae+(J_1B-J_1F)delta_F+DeltaJ_B(e_0B-e_0F)+(DeltaJ_B-DeltaJ_F)e_0F-(Deltar_B-Deltar_F).

실제 convex tube, derivative와 차이 residual의 상계, incoming error 및 event jump를 보존해야 한다. 이 식은 직접 유도했으며 이번에 actual global error를 인증한 것은 아니다. 비선형 T observable에는 gradient와 그 경로 간 차이도 필요하다.
