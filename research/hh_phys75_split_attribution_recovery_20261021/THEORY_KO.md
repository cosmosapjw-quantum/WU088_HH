# PHYS75: 물질·복사 응력의 조건부 전단 기여 분해

## 물리 범위와 단위

이 문서는 이미 저장된 non-tilted LRS Bianchi I 이력의 후처리다. 새로운 우주론적 해를 생성하지 않는다. Metric signature는 (-,+,+,+), proper time은 초, H는 s^-1, 압력은 J/m^3다. a_perp=a exp(-b), a_parallel=a exp(2b), s=db/dt로 둔다. 같은 정규직교 normal frame에서

sigma=diag(-s,-s,2s), pi_X=diag(-p_X,-p_X,2p_X), p_X=(P_parallel,X-P_perp,X)/3.

물질과 복사는 각각 pi_m, pi_r로 보존하며 total은 pi_m+pi_r다. 현재 coupled pilot의 matter는 기존 massive nonbaryonic Vlasov species다. Isotropic gas/cold matter의 응력은 이 closure에서 0이다. Radiation에는 photon, massless neutrino와 UV가 포함된다. Massive species를 질량이 있다는 이유로 dust로 바꾸지 않는다.

Proper-time 압력 결합은 K=8*pi*G/c^2다. Einstein equation의 kappa=8*pi*G/c^4를 쓰는 표기에서는 K=c^2*kappa이다. c=1을 암묵적으로 넣지 않는다.

## 정규화와 부호

Full Frobenius norm은 ||sigma||=sqrt(6)|s|, ||pi_X||=sqrt(6)|p_X|이다. 기존 half-contraction norm은 sqrt(3)|s|, sqrt(3)|p_X|이다. 서로 sqrt(2)만큼 다르지만 동일 이름으로 섞지 않는다.

c_n=sqrt(3) 또는 sqrt(6)를 명시하고 signed coordinates를
S=c_n*s/H, P_X=c_n*K*p_X/H^2
로 정의한다. 사용자 norm 관측량은 Sigma=|S|, Pi_X=|P_X|이다. 특히
Pi_total=|P_m+P_r|
이며 Pi_m+Pi_r로 대체하지 않는다. General STF의 경우에는
||pi_m+pi_r||^2=||pi_m||^2+||pi_r||^2+2*pi_m:pi_r
가 필요하다. LRS 정렬 축의 부호 두 개가 일반적인 tensor orientation 전체를 대표하지 않는다.

## 정확한 연속식

원 LRS shear equation이 ds/dt+3 H s=K(p_m+p_r)이면 N=ln(a)에 대해

S' + (3+H'/H) S = P_m+P_r.

I(N)=exp(3(N-N0))*H(N)/H(N0)라 놓으면

S(N)=S(N0)/I(N)+J_m(N)+J_r(N),
J_X(N)=I(N)^(-1) integral[N0,N] I(v) P_X(v) dv.

이는 H와 각 응력이 실제 동일 trajectory의 값일 때 성립하는 정확한 integrating-factor identity다. J_m과 J_r는 같은 trajectory 안의 impulse attribution이다. Matter를 끄거나 radiation을 끄고 다른 H를 생성한 반사실적 해의 차이가 아니다. 새로운 ODE state를 추가할 필요가 없고, 저장 이력을 읽어 독립적으로 계산할 수 있다.

Anisotropic work는 W_X=sigma:pi_X=6*s*p_X이다. 따라서 K W_X/H^3은 Frobenius signed variables에서 S P_X, half-contraction variables에서 2 S P_X이다. 응력 norm만 저장하면 이 부호 정보를 잃는다.

## 구현과 오차의 의미

shear_attribution.py는 입력 N,H,S,P_m,P_r를 검증하고 overflow를 줄인 공통 integrating-factor rescaling, 고정 순서의 Neumaier prefix sum, composite trapezoid로 J_m/J_r를 계산한다. 같은 배열의 every-other-node coarsening 차이를 별도로 반환한다. 출력의 sampled_closure_defect는 저장 grid, 보간·quadrature, 원 solver 오류와 roundoff가 혼합될 수 있는 diagnostic이다. 이를 continuum error certificate 또는 인과적 분해로 승격하지 않는다. Signed input과 norm이 명시되지 않거나 grid/H가 부적합하면 거부한다. Clip, source renormalization, tolerance relaxation은 없다.

## 이미 게시된 장구간 response fit의 재표현

REI PR198, commit 8bd35af5f11c7ea5945b656be1c013d1c1933498에 게시된 collisionless zbar20→4 half-contraction fit:

S_end ≈ 0.11438019418589546 S0 + 0.11914730406637555 P_m0 + 0.24184661410997463 P_r0.

P_plus=P_m0+P_r0, P_minus=P_m0-P_r0로 바꾸면

S_end ≈ 0.11438019418589546 S0 + 0.18049695908817509 P_plus - 0.06134965502179954 P_minus.

따라서 initial total stress=0인 대각선에서도 성분 차이 방향의 response가 남는다. 이것은 게시된 유한-grid fit의 대수적 재표현이며 새 fit이나 일반적 선형 이론, 오차 경계가 아니다. Warm C15 a=0.1999→0.2 729점 결과에 이 계수를 적용하지 않는다.

## 보존한 의무

HH_R10=OFF. PHYS73 완료15 jobs, PHYS71 완료76 panels 및 inherited152 profiles, PHYS74 control63, REI split729와 PR198 완료 이력을 재적분하지 않는다. 미완성 physical HH rate를 오늘 pilot의 필수 의존성으로 추가하지 않는다. Cold EoR, full radiation-source Q^a closure, general non-LRS와 continuum error는 별도다.
