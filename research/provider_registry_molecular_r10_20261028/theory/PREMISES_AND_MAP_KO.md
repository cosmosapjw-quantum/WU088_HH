# R3/C3 전제와 계산식 대응

## 고정 대상

HD fine state는 (u,v,w,x_1,...,x_n), X=Σx_i이고 pi와alpha는 simplex vector다. 정확한 잔차 r=x−pi X는 Σr_i=0이며 R=||r||_1이다. 같은H,D,charge 불변량을 공유하는 coarse state의 차이는 (-eta,-eta,eta,eta)이고 E=|eta|, coarse l1=4E다. K는 열합0인 Metzler 생성자다. d_i≥0는 소멸계수이고 이 문서의 signed coarse 계수 d_c와 구별한다.

고정 K,pi,d_i와 fine/coarse 전체 invariant box를 재사용한다. 변하는 w(t)는 [m_w,M_w]에 있다. R7의 q_*,theta_*,Delta_d,c,d_c,g_r,g_e와 원래 실패 이력은 유지한다. 실제 HD 반응률 데이터, 물리 consumer/density/clock은 INPUT_PENDING이다.

## 식–코드 연결

1. H=pi d^T−diag(d)와 A(w)=K+wH를 구성한다. H,A는 열합0인 Metzler다.
2. lambda(A)=min_(i<j)[A_ij+A_ji+Σ_(k≠i,j)min(A_ki,A_kj)]를 exact Fraction으로 계산한다. API generator_certificate는 고정 계수의 w_min에서 uniform minimum을 구한다. 명목 K block rho는 전용하지 않는다.
3. Fine-state box에서 ||f_r||≤g_r이므로 R'≤−lambda R+g_r, E'≤cR+d_cE+g_e를 얻는다. bE를 따로 더할 필요가 없다. 이 사실은 일반 비선형계가 아니라 정확한 HD 식과 whole fine-domain forcing에 의존한다.
4. M=[[-lambda,0,g_r],[c,d_c,g_e],[0,0,0]], z=(R,E,1)로 쓰면 endpoint 비교해는 exp(delta M)z다. sigma=max(lambda,−d_c,0), C=delta(M+sigma I)≥0를 사용해 양의 Taylor96와 geometric tail로 각 matrix entry의 lower/upper를 만든다. dyadic128 내림/올림을 분리하고 reciprocal scalar exponential의 양쪽을 곱한다.
5. Whole-cell은 Mplus=[[0,0,g_r],[c,max(d_c,0),g_e],[0,0,0]]의 단조 flow 상계로 덮는다. Raw lower는 ideal comparison해의 lower이며 physical error lower가 아니다. Capped에는 lower를 반환하지 않는다.
6. 같은 정확한 cell/clock의 R9 인증 whole/point 상계와 min을 취한다. R7 reference 표본은 포함 여부 확인에만 쓰며 cap이 아니다.

## 수치 설계와 판별 기준

4 HD 사례는 R7 정확한 입력·계수와 R9 grid를 연결한192cells/193endpoints다. 이외 9개 control은 zero, constant forcing, nilpotent, damping, resonance, lambda=0, positive d_c, d_c+lambda=±1e−30다. 정확한 branch 선택은 Fraction에서 수행한다.

독립 reference는 production code를 import하지 않고 exact Euler stochastic matrix의 column l1로 lambda를 다시 계산한다. Flow는 Decimal160의 scalar exp와 analytic divided differences로 구한다. 160자리는 근접공명에서 최대1e60 증폭을 고려해 실행 전에 선택했고 guard=1e−80×max(1,|reference|,|lower|,|upper|)를 고정한다. 저장된 trajectory의 containment는 기존atol2e−12,rtol2e−10을 그대로 사용한다. Reference 표본은 연속시간 증명이 아니다. 연속시간 보장은 전체box와 생성자/비교정리에서 온다.

원래 R8 726/727PASS+1FAIL 및 별도phi24/24PASS는 그대로다. 이번 단위는 해당 fixed-phi closeness 검사를 재사용하지 않는다. 예전과학예산을 reset하지 않고 새 계수/계산에만 primary1회, reference1회, CAS1회를 사용한다.

## 문헌과 직접 유도

Gaubert–Qu arXiv1307.4649v3 식(1)–(2), 정리6.2/예6.3은 stochastic Dobrushin coefficient의 선행 근거다. Euler I+hA에서 continuous generator overlap을 얻고 HD projected sink 및 fine forcing으로 연결하는 단계는 이번 proof에서 직접 유도한다. 보편적 raw 우월성이나 새 strong no-go를 주장하지 않는다. Capped no-worse는 같은영역 upper들의 min이기 때문에 성립한다.
