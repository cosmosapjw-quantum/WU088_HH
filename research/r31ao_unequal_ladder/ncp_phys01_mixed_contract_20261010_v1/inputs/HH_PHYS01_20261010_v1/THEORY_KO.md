# HH-PHYS01: near-threshold 광이온화와 HH의 비가산 응답

연구일 2026-10-10. 직접 유도와 경량 대수 검산. 본문은 새로운 actual-owner root/시간이력/물리적 fit 인증이 아니다. ENERGY06E의 수치 인증 경로와 별도 물리 분석이며 canonical 설정을 변경하지 않는다.

## 1. 무엇을 비교하는가

서명은 (-,+,+,+), 시간은 proper seconds이다. 국소 물질 frame의 zero-tilt, 공통온도 H/He 상태를 사용한다. source-stage 안에서 n_H,n_He,E를 고정한다. 기체 좌표 y=(x,y_1,y_2,w), x=x_HII, w=eV/H, 광자수 P=photons/H이다. 고정 stage는 원 coupled_primary.rs가 지원하는 의미이며, 우주론 전체에서 밀도/에너지가 일정하다는 뜻은 아니다.

동일한 초기 전체 상태 z_0에서

    z'=F_0(z)+lambda H(z)+S B

를 정의한다. F_0에는 원 FT03의 모든 비광자 H/He CI/RR/DR와 열·팽창 항 및 기존 광자의 photo source가 남아 있다. 새 source가 넣는 광자는 단색 E_*∈(13.6 eV,chi_HeI)이고 rate S는 photons/(H s)이다. B는 gas 성분0, 해당 photon 성분1이다. H=(q,0,0,-chi_H q,0_photon), q=n_H(1-x)^2 k_LCS(T). lambda는 고정 LCS의 수학적 강도이며 KS 혼합·물리적 error distribution이 아니다. 추가 1/2를 넣지 않는다.

임의의 관측량 O에 대해 비가산성은

    I_O(delta;lambda,S)
      = O(delta;lambda,S)-O(delta;lambda,0)
        -O(delta;0,S)+O(delta;0,0)

이다. 모든 경로는 같은 z_0를 공유한다. 따라서 이는 서로 다른 과거를 가진 원 G의 ON/OFF 차이도, Bianchi-FLRW 이중차이도 아니다. I_x<0은 HH가 이온화를 감소시킨다는 뜻이 아니라, HH와 새 광자의 동시 효과가 두 개별 효과의 합보다 작다는 뜻이다.

수학적 조건: 양의 온도·Pi·물리 분율을 포함하는 국소 compact 영역에서 F_0,H가 충분히 매끄럽고(예: 관련 joint derivatives를 가진 C5), 해 및 작은-delta BE 분기가 그 영역에 존재한다. 빛의 threshold/hat-cell crossing 및 불연속 birth/reset은 이 frozen smooth stage 내부에 없다. 원 T=3000K floor는 현재35000..60000K 영역 밖이다. Taylor 식은 delta→0이며 실제delta에 대한 remainder 상계는 계산하지 않았다.

## 2. 열·입자수로 결정되는 HH 억제

    u=1-x, r=n_He/n_H,
    Pi=1+r+x+r(y_1+2y_2), C=2 E_eV/(3 k_B), T=Cw/Pi.

C는 K/eV이며 E_eV는 eV→erg 상수다. g=E_*-chi_H>0, T_gamma=Cg라 둔다. 광이온화 사건당 dy=(1,0,0,g)이므로

    dT/dJ_photo = (T_gamma-T)/Pi.

열에너지 주입 g가 양수여도 T_gamma<T이면 자유입자수 증가가 우세해 해당 photo 채널의 온도 기여는 음수다. 이는 전체 열 RHS나 시간 진화의 냉각을 의미하지 않는다.

LCS k=k0 (T/K)^p exp(-T_a/T), p≈1.2,T_a=157800K에 대해

    L_T = d ln k/dT = p/T + T_a/T^2,
    nu = T L_T,
    Xi = (u/Pi) nu (1-T_gamma/T),
    (q_x+g q_w) = (q/u)(-2-Xi).

마지막 식은 u>0에서 해석에 편리한 표현이다. 구현·중성분율 경계에서는

    q_x+g q_w = -2 n_H u k
      + n_H u^2 k'(T)(T_gamma-T)/Pi

를 사용하므로 1/u 특이점을 만들지 않는다. u=0에서 최종 혼합항은0으로 유한하게 간다.

T>T_gamma이면 Xi>0이다. 같은 중성수소 두 개를 요구하는 q의 target depletion과 photo에 의한 온도 감소가 모두 q를 줄인다. beta_thermal로 저장한 코드 변수는 이 Xi이며 cosmological shear/tilt 매개변수가 아니다.

## 3. 새 연속 source의 혼합항은 세 번째 시간 차수에서 처음 생긴다

A=c n_H sigma_H(E_*)라 하자. 단위는 s^-1이고 실제 opacity는 A u이다. c는 명시적으로 cm/s로 유지한다.

F=F_0+lambda H+S B, J=F_z일 때

    z(delta)=z0+delta F+delta^2 JF/2
       +delta^3[J^2F+F''(F,F)]/6+O(delta^4).

H는 photon-independent이고 F_0는 photons에 선형이므로

    partial_lambda partial_S F=0,
    partial_lambda partial_S(JF)=H'B=0.

따라서 처음 나타나는 혼합계수는 delta^3이다. 일반 H/He 비광자 source를 미지 함수로 그대로 두어도

    partial_lambda partial_S(J^2 F)=X=H'F_0'B,
    partial_lambda partial_S F''(F,F)=2Y=2F_0''(B,H).

가 성립한다. 구체적으로 gas와 새 photon 합의 좌표에서

    X=A u(q_x+gq_w)(1,0,0,-chi_H,0),
    Y=A q(-1,0,0,-g,+1).

즉 nonphoto 반응의 도함수가 사라진 것은 H/He를 제거해서가 아니라 이 lowest mixed order의 구조적 소거다. 그 반응들은 다음 차수와 전체 궤적에서는 중요하다.

x에 대입하면

    I_x = -lambda S A q (4+Xi) delta^3/6
          +O(lambda S delta^4).

고정된 유한lambda,S의compact범위에서 같은 third-order coefficient를 가진다. delta^3 이하에서는 lambda^2 S 또는 lambda S^2 혼합항이 없다. 따라서 finite lambda=1에 대해서도 국소 시간계수는 같다. 임의 유한delta에서 leading term이 정확한 답이라는 주장은 아니다.

Xi>=0,A>0,q>0,S>0,lambda>0이면 충분히 작은delta에서 I_x<0이다. 실제사용delta가 그 충분히 작은 범위에 들어간다는 remainder 증거는 아직 없다.

사건수와 열에 대해서는

    I_JHH    = -lambda S A q (2+Xi) delta^3/6 + O(delta^4),
    I_Jphoto = -lambda S A q delta^3/3 + O(delta^4),
    I_P      = +lambda S A q delta^3/3 + O(delta^4),
    I_w      = lambda S A q [chi_H(2+Xi)-2g] delta^3/6+O(delta^4).

따라서 초기의 photo/HH 상호작용은 두 채널의 누적 사건수를 모두 개별효과의 합보다 줄인다. 생존 photon 혼합항은 양수다. 이는 instantaneous Gamma나 모든 시각에서의 각 raw rate 부호의 일반정리가 아니다.

    I_x=I_JHH+I_Jphoto,
    I_P=-I_Jphoto,
    I_w+chi_H I_x+E_* I_P=0

가 leading mixed order에서 정확히 성립한다. 비광자 사건수/escape/work의 mixed 기여는 이 차수에서0이고 다음 차수부터 필요하다. 전체 실제 장부가 이 식만으로 닫힌 것은 아니다.

## 4. 실제 chronology를 드러내는 leading causal kernel

관측 종료delta 전의 birth시각 b에 아주 작은 photon 질량 m을 넣자. HH는0부터 작용한다. 초기 q,A,Xi의 frozen local coefficient를 쓰면 lambda*m에 곱해지는 leading kernel은

    K_HH(b) = -Aq(2+Xi)(delta-b)^2/2,
    K_photo(b) = -Aq(delta^2-b^2)/2,
    K_x=K_HH+K_photo, K_P=-K_photo,
    K_w=-chi_H K_HH+g K_photo.

첫 항은 birth 이후 photon이 q를 바꾸는 시간이고, 두 번째는 birth 전에 이미 HH로 달라진 중성수소까지 photon이 만나므로 delta^2-b^2를 포함한다. K_x(delta)=0, K_x(0)=-Aq(3+Xi)delta^2/2이며

    dK_x/db=Aq[b+(2+Xi)(delta-b)]>0

이다. 현재 가정에서는 먼저 태어난 photon일수록 HH 비가산 억제의 시간이 더 길다. constant S로0..delta를 적분하면 §3의 cubic 계수가 정확히 재현된다.

이는 O(delta^2)의 local impulse kernel이지 인증된 all-time Green function이 아니다. Actual owner의 '끝점 birth 추가 후 길이delta의 BE'는 연속시간의 t=delta 순간kick후 진화0과 다르다. 둘을 같은 연산으로 평가하지 않는다.

## 5. Backward Euler full과 two-half의 다른 혼합계수

같은 frozen G=F_0+lambda H와 constant birth rate S에 대해 각 step은

    z_new=z_old+delta S B+delta G(z_new)

이므로 F=G+SB의 BE와 동일하다. 이것은 기존 owner의 한 source-law insertion 규칙에 대응하는 축소된 frozen subproblem이다. 원 time-dependent source_weights, redshift/remap, 기체밀도 및 H의 실제macro 전체를 대체하지 않는다.

Taylor 계수는

    BE_full: delta F+delta^2 JF
                 +delta^3[J^2 F+F''(F,F)/2],
    BE_half2: delta F+3delta^2 JF/4
                 +delta^3[J^2F/2+5F''(F,F)/16].

따라서 lambda S A q delta^3로 나눈 x혼합계수는

    continuous: -(4+Xi)/6,
    BE_full: -(3+Xi),
    BE_two_half: -(13/8+Xi/2),
    BE_two_half-BE_full: +(11/8+Xi/2).

paired mixed defect가 양수여도 물리적인 source-HH synergy가 양수인 것은 아니다. 두 방법 모두 같은 부호의 음의 혼합항을 다르게 근사한다. 전체 HH paired defect에는 기존 photon/background와의 O(lambda delta^2)항도 있어, 새 S와의 혼합항만으로 전체오차를 제한할 수 없다. 이 표는 fixed-source의local coefficient이며 ENERGY06C의 실제 nonlinear family·acceptance를 계산한 것이 아니다.

## 6. 온도는 EOS Hessian 교차항까지 포함한다

위 표의 각 방법에서 I_x=lambda S A q delta^3 f_x, I_w=lambda S A q delta^3 f_w라 두고, source S에 대한 gas의 두번째시간차수 계수를 c2=(1/2,1,3/4)로 둔다. 그러면

    I_T/(lambda S A q delta^3)
      = (C f_w-T f_x)/Pi
        +c2*u*(2T+Cchi_H-Cg)/Pi^2.

두번째항은 Hess(T)[c_H,c_photo]에서 생긴다. 단순히 I_w/I_x만 선형 변환하면 누락된다. 현재 nearthreshold 상태에서는 I_T와 I_w의 혼합항이 양수다. 이는 두 cooling/dilution 효과를 단순합했을 때보다 덜 식는다는 뜻이며, total T_ON-T_OFF나 전체 gas heating의 부호를 뒤집는 주장이 아니다.

## 7. 다방향·다주파의 국소 범위

gas-independent normalized birth 방향 weights b_d와 동일 E_* 및 scalar unpolarized sigma라면 A=c n_H sigma(E_*) sum b_d=c n_H sigma(E_*). 따라서 같은국소gas에서 이lowest mixed coefficient는 방향 재분배에 독립이다. 실제 raw source_weights의합산오차는별도이며 원native를정규화하지 않았다. Bianchi의 redshift·비등방수송·다른gas이력은 이후차수/후속연산에 나타난다. 전역epsilon^2법칙이나 cutoff를 넘는매끄러움은주장하지 않는다.

다색 birth는 A=sum a_j b_j, gbar=sum a_j b_j(E_j-chi)/A를 사용하면 같은 gas계수 구조를 가진다(HI-only support 필요). 이는 당장 code profile을확장하는승인이아니며HE photo/secondary/tilt가활성인경우 식을다시유도해야한다.

## 8. 저장 상태의 수치점 진단과 인증 상한

inputs/SELECTED_SOURCE.json는 ENERGY05의 봉인 입력 bytes다. old_gas를그대로사용하고source에등록된nH, nHe, sigma(13.7),기초상수를exactbinary64실수로해석했다. 새근은구하지않았다.
T≈49489.0775K,T_gamma≈785.7450K,Xi≈0.1769024684,q≈1.597241607e-19/s,A≈1.856507144e-11/s.
광이온화 사건당 dlogq의target기여≈-23.02516146,thermal기여≈-2.03660395다. thermal추가기여/target크기≈8.84512%이며새physicalfit오차가아니다.

S=5e-15,delta=1.25e9s,lambda=1을leading term에넣은 x진단은continuous -2.0159064e-17,BEfull -9.1996470e-17,BEhalf2 -4.9617974e-17,그차이+4.2378496e-17이다. 실제delta에서의truth/error/certificate가아니다. Higher-order remainder,actualstagegeom/timecoefficients,birthorder support 및guard를닫아야실제예측/오차상계가된다.

## 9. 출처 및 구분

- 1차 SSOT: 동봉된 원 source6개/선택 JSON 및 INPUT_IDENTITY.json; 기초물리·에너지owner·LCS율은 이코드모형을계승한다.
- 배경 문헌: Verner et al. 1996, https://arxiv.org/abs/astro-ph/9601009 및 저자자료 https://www.pa.uky.edu/~verner/photo.html . 기존fixedsigma의origin만확인했고fit교체/재평가/물리불확실성인증은없다.
- Hybrid sensitivity 배경: Corner,Sandu,Sandu, https://arxiv.org/abs/1802.07188 . 일반event tangent 배경이며 이번H–H/localTaylor계수가그논문에있다고주장하지않는다.
- 새 식·계수·부호·causal kernel은직접유도다. Point90digit와symbolicverification은형식증명기/제3자심사/전시간구간오차증명과다르다.
