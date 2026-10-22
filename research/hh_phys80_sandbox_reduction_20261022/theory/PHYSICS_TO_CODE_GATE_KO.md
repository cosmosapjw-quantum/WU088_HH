# PHYS80 물리 → 코드 진입 계약

부모: PR134 최종 3304d16db1dc9bf868c185a8eeb6cc9dbc270e50.
기존 C01/C02 결과는 byte-pinned 입력으로 재사용한다. 동일 완료 identity를 다시 풀지 않는다.

## 이번 닫힌 물리 부분

고정 proper density, H=0, PI=RR=0, neutral CI rows(0,1,3)와
D/H ground-state detailed-balance CX만 있는 PHYS79 isolated subnetwork이다.
T isotope/neutron inventory와 모든 double/higher charge는 0이다.
원소별 CI rate의 isotope 공유는 부모의 명시적 kinetic model 가정이다.
새 isotope injection, recombination, expansion, photon bath는 포함하지 않는다.

H,D,B,L은 H1,D,He3+He4,Li6+Li7의 보존 inventory이다.
Q=HII+DII, v=DII, h=(He3II+He4II)/B, l=(Li6II+Li7II)/L.
electron x=Q+Bh+Ll, particle N=H+D+B+L+x이다.
HII=Q-v, HI=H-Q+v, DII=v, DI=D-v이다.
He/Li 중성 isotope 비는 동일 elemental CI 때문에 보존된다.
따라서 초기 중성 비율을 고정한 affine lift를 쓰면 서로 다른 초기
ion fraction도 허용하며, 같은 초기 fraction은 그 특수한 경우이다.
유한정밀도 복원 오차를 수학적 exactness와 구분한다.

u=u0−IH(Q−Q0)−δ(v−v0)−IHe B(h−h0)−ILi L(l−l0),
T=u/[(3/2)kB N].
IH,IHe,ILi와 δ는 실제 부모 global ionic potential에서 가져온다.
특히 δ=eps[DII]−eps[HII]이며, DB exponent의 선언값 43K와
stored-potential subtraction의 부동소수 차이를 숨기지 않는다.
Voronov fit threshold(He24.6/Li5.4eV)를 thermodynamic
potential(He24.59/Li5.392eV)로 대체하지 않는다.

FQ=nH kH x(H+D−Q).
Fv=nH[kH x(D−v)+kf(D−v)(Q−v)−kr v(H−Q+v)].
Fh=nH kHe x(1−h), Fl=nH kLi x(1−l).
C02는 CI=0이므로 Q,h,l이 고정이고 v 하나만 동적이다.
이는 QSS, trace-D 제거, equilibrium 강제, source rate 변경이 아니다.

Jacobian은 J=nH[M+w outer gradT] 형태로 직접 미분한다.
gradT=−[bgrad+(3/2)kB*T*xgrad]/[(3/2)kB*N].
Wolfram 독립 유도에서 21-state lift, energy/temperature chain,
4x4 Jacobian residual은 모두 symbolic 0이었다.
원 호출/응답과 독립 유도 파일을 theory/에 함께 보존한다.

## 코드 진입 조건과 사전 고정 gate

1. 입력/부모 source SHA256을 확인하고 source-domain 예외를 유지한다.
2. 구현된 lift-RHS를 부모의 별도 21-species event operator와 비교한다.
3. analytic Jacobian을 독립 수치 미분과 비교한다.
4. implicit Radau의 모든 RHS/Jacobian trial에도 strict positivity와
   source-domain guard를 적용한다. exception은 실패로 기록한다.
   자동 clipping/projection이나 signed trial extension은 없다.
5. solver가 받아들인 모든 step endpoint와 161 dense samples를 검증한다.
   이는 전체 dense interpolant/continuum positivity certificate가 아니다.
6. 새 algorithm identity의 C01/C02와 C01 정련만 shared lease에서 실행한다.
   저장된 PHYS79 궤적 대비 scaled-state error <=1e-6를 사전 gate로 쓴다.
   isotope<=1e-10, energy<=2e-10, C02 extent-T<=1e-9K,
   최종 D equilibrium distance/inventory<=1e-6도 유지한다.
7. energy first-integral의 작은 residual 자체는 독립 검증이 아니다.
   별도 full-operator tangent 비교와 저장된 다른 solver 궤적을 함께 쓴다.

## 남아 있는 의무

LOW_T_CI_SOURCE_COVERAGE, He/Li state-resolved CX, radiative energy,
full PI/RR potential adapter, recombination→z20 charge initial contract,
Li hard-UV inner-shell/spectral closure는 열려 있다.
일반 Maxwellian 단면적 적분은 별도 수학/계산 노드이며 실제 저온 rate
정확도나 기존 trajectory에 대한 activation 허가로 승계하지 않는다.

HH_R10=OFF. Production admission NOT_ISSUED.
