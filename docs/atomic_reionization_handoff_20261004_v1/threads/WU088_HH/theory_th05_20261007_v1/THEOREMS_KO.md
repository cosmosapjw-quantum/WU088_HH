# HH-TH05: 부호 정리와 적용 범위

전체 증명과 exact rational 값은 START의 sealed ZIP/THEORY_KO.md 및 results/SIGNED_RESPONSE_BOUND_01.json에 있다. 아래는 별도 검색용 요약이다.

## 1. 정의와 계승한 모형

시간은 proper seconds, signature(-+++), H_i=H(1+eps,1-eps,1), H=1e-14/s, |eps|<=.01, L=8e11s, nH=1e-4 exp(-3Ht)cm^-3, r=.083이다. Y=(h,x,z,v=w/w0), w[eV/H], 초기 h=.9,x=.3,z=.6,T=50000K. 동일 exact-decimal FT03 CI/RR/2DR, 열/He EOS 피드백, 단열팽창, 같은 fixed160birth dyadic counts, soft HI-only absorption을 유지한다. lambda는 고정 LCS source q=nH(1-h)^2*1.2e-17*T^1.2*exp(-157800/T)의 강도0..1이다. +lambda*q와 -lambda*chiH*q가 H/열식에 들어가며 extra1/2가 없다. 각 lambda 대 OFF를 비교하고, LCS/KS 혼합이나 물리적 오차분포로 해석하지 않는다.

TH04의 공통 convex box, 더 좁은 first-exit h범위, J(B), |DeltaY_k|<=lambda*B_k를 계승한다. J는 HH/photo를 제외한 gas collision+thermal/adiabatic field의 Jacobian이다. a_j=c*nH*sigmaHI(E_j)>=0, a_j<=astar, 공급광자 Pstar=.055/H이다. 동일 birth와 characteristic에서만 a_j가 공통이다.

## 2. 정확한 signed 부분계

d=h_lambda-h_0, dp_j=p_lambda,j-p_0,j라 두면 두 상태 사이 평균 Jacobian Jbar를 사용하여

d'=(Jbar_hh-Gamma0)d+sum_j(1-h_lambda)a_j dp_j+r(t),
r(t)=lambda*q(Y_lambda,t)+Jbar_hx Delta x+Jbar_hz Delta z+Jbar_hv Delta v,
Gamma0=sum a_j p_0,j,
dp_j'=-a_j(1-h_lambda)dp_j+a_j p_0,j d.

C_k=max(|J_hk^-|,|J_hk^+|), k=x,z,v,
E_fb=sum C_k B_k,
q_min=nH_min(1-h_max)^2*k_min,
m=q_min-E_fb,
mu=max(0,-J_hh^-)+astar*Pstar

를 정의한다. nH_min=nH0 exp(-3HL)의 하한, k_min은 이미 TH04에서 구한 전체 T구간의 rate 하한이다. 그러면 r>=lambda*m, Jbar_hh-Gamma0>=-mu이다.

## 3. 정리와 증명

m>0이면 동일 초기값/birth에 대해 각0<lambda<=1,0<t<=L에서

d(t)>=lambda*m/mu*(1-exp(-mu*t))>0,
dp_j(t)>=0.

실제 기체 경로를 고정한 뒤 Z=(d,dp_1,...,dp_N)를 비자율 선형계로 읽는다. 비대각 계수 (1-h_lambda)a_j 및 a_jp_0,j는 비음수이고, inhomogeneous vector (r,0,...)도 비음수다. 유계 diagonal에 충분한 양의 shift를 더한 적분방정식의 Peano-Baker 전개는 각 항이 비음수이므로 transition matrix가 비음수다. Z(0)=0에서 Z>=0. 동일 additive birth는 차이를 뛰게 하지 않고 처방된 cutoff도 상태를 연속으로 유지한다. 따라서 유한 시간 조각 전체로 결론이 이어진다.

이제 d'>=-mu*d+lambda*m에 적분인자를 곱하면 하한식이 나온다. 이는 전체 thermal network의 monotonicity를 가정한 논증이 아니다. 임의 lambda2>lambda1 사이의 순서, h(t)의 시간 단조증가, DeltaT의 부호는 증명하지 않는다. mu=0의 일반 극한은 lambda*m*t이며 현재 계수는 mu>0이다.

실제 부호 여유(표시는 근삿값, 판정은 exact fractions):
q_min=1.872985947890858e-20/s,
E_fb=6.941477134229718e-21/s,
m=1.1788382344678861e-20/s>0,
mu=1.1334246789829652e-12/s.

따라서 L에서 안전하게 6.200e-9*lambda<Delta h<2.874e-7*lambda. 오른쪽은 TH04 상계다. t=0 또는 lambda=0에는 Delta h=0이다. Thermal-v 역효과 상한은6.941166025154114e-21/s이며 나머지는 He항이다. 원 최소 HH source가 이를 앞선다는 것이 새 결과다.

## 4. 광학기억과 생존의 부호

TH03의 동일 cohort 항등식 S_j=int_birth^t a_j(s)d(s)ds, p_lambda/p_0=exp(S_j)를 계승하면 S_j>=0, dp_j>=0이다. 양의 birth와 양의 길이의 active 생애에서는 둘 다 엄격히 양수다. birth에서는 차이0, cutoff 이후 기억은 보존되며 reset하지 않는다. p_b=0에는 ratio 대신 dp=0을 쓴다. 누적 photo 사건 차이는 DeltaJ_photo=-dp_j<=0이다.

순간 흡수율은 DeltaR=a_jp_0[(1-h_lambda)expm1(S_j)-d]이므로 여전히 부호가 결정되지 않는다. 생존광자 증가와 현재 중성분율 감소가 경쟁한다. 누적 광흡수 감소를 순간율 감소라고 바꾸지 않는다.

두 기존 terminal label의 active 생애에는 a_j>=a_minus=c*nH_min*sigmaHI(13.7). 따라서
S_j(L)>=lambda*a_minus*m/mu*[(L-tb)-(exp(-mu*tb)-exp(-mu*L))/mu],
S_j(L)<=lambda*Lambda_j^+*B_h.

lambda1의 안전 구간:
- tb6.5e10/index9: S in[5.1462e-8,3.9660e-6], dp in[1.0109e-14,3.0985e-12]photons/H.
- tb7e10/index8: S in[5.1392e-8,3.9387e-6], dp in[1.0191e-14,3.0772e-12]photons/H.

p0는 p_b exp(-u_max Lambda^+)..p_b exp(-u_min Lambda^-)에 있으며, dp_lower=p0_lower*expm1(S_lower), dp_upper=p_b*(1-exp(-S_upper))를 사용했다. TH03 단면적 구간과 TH02 root/tauprime는 재평가하지 않았다.

TH02 terminal prehistory/group 가정 아래 K_Dh=-|tau'|a_cut*p0[(1-h_lambda)expm1(S)-d]의 구간은 각각[-1.643e-12,1.201e-12],[-1.615e-12,1.189e-12]이다. 둘 다0을 포함하고 실제 총 kink 또는 그룹 정칙성을 인증하지 않는다. Binding classification에 두 번째 physical source jump를 넣지 않는다.

## 5. 검증과 주장 한계

새 core38 + 별도55 checks(후자 symbolic7 포함)=93, 두 script 각1회 exit0/stderr0. 같은 작성자의 별도식 checker이며 formal proof assistant/independent agent review/TDD는 아니다. TH04의 first-exit 및 rate/J/bounds는 계승 전제이며 hash만으로 그 과학적 타당성을 새로 증명했다고 하지 않는다. 새 원자율/native/Rust/IVP/BE/geometryroot/actualadjoint/oldproof 실행0.

대상은 exact-real FT03+LCS 기준모형의 양의 응답과 기억이다. Native rounding/time error, 실제 IGM/우주 정확도, 전체1e13s, tiny four-path anisotropic contrast, production integration과는 별개다. 원천/IC/방향/온도 guard/기존 실패·tolerance는 변경하지 않았다. HH ACTIVE, canonical S0 OFF control, legacy24/289·265unbounded·epsilonnull·B22OPEN·consumed scopes 보존.

일반 배경으로 Angeli/Sontag, Monotone Control Systems, arXiv:math/0206133, DOI10.1109/TAC.2003.817920의 공식 abstract/저자 metadata를 확인했다. 위 H/photo 부분계의 증명과 S0 수치 상계는 이번 직접 유도이며 해당 원전에 이미 있는 결과라고 하지 않는다.
