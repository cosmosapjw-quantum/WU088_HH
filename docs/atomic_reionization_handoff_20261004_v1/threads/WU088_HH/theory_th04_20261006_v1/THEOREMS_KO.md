# HH-TH04 핵심 정리와 검증 범위

전체 증명/계수/정확 구간은 START에 지정한 ZIP/THEORY_KO.md 및 results/GAS_BOUND_03.json에 있다. 아래는 검색용 직접 유도 요약이다.

## 1. 정의와 모형

서명(-+++), proper seconds, prescribed H_i=H(1+eps,1-eps,1), H=1e-14/s, |eps|<=.01. nH=1e-4 exp(-3Ht) cm^-3, r=.083. 공통온도/zero tilt/CaseA escape인 기존 FT03 HG CI/RR+2DR와 soft HI primary를 유지한다. y=(h,x,z,w)에서 x=HeII,z=HeIII,w=eV/H, Pi=1+r+h+r(x+2z), T=2w/(3(kB/eV_erg)Pi). 초기 h=.9,x=.3,z=.6,T=50000K로 w0=13.62077238747822...eV/H다. 비교 gas좌표는 Y=(h,x,z,v=w/w0).

한 LCS source qHH=nH(1-h)^2*1.2e-17*T^1.2*exp(-157800/T)에0<=lambda<=1을 곱한다. h source는+lambda*qHH, w source는-lambda*chiH*qHH다. chiH=13.598434599702eV, extra1/2없음. KS를 평가하거나 섞지 않았다.

상수/IC/기하는 정확 십진수 실수, 원160birth count는 기록된 binary64를 exact dyadic으로 해석한다. 원생성 에너지를 exact13.7eV로 정의한 이 기준모형은 모든 native literal의 exact-bit실수화 및 runtime반올림과 다르다. 초기+birth 총수의 유리수합<.055/H를 확인했다. .055는 proof상한이지 새 source가 아니다.

각 cohort p_j'=-a_j(1-h)p_j, a_j=c*nH*sigma_H(E_j)>=0. 소프트 광자는 He photo를 일으키지 않고 에너지가 감소한다. 13.6eV 아래 HI absorption0이고 photon은 retained. TH03의 sigma단조성/endpoint구간을 계승해 a_j<=a_*=c*nH0*sigma_H(13.6)을 쓴다. 같은 cohort 재주입·산란·재분배가 없으므로 총생존수와 누적Hphoto사건수는 .055/H 이하이다.

## 2. First-exit 공통영역

계산 전에 B: h[.89,.97],x[.29,.32],z[.59,.61],w[12.5,13.7]를 고정했다. B의Pi는[2.09501,2.18082], T는[44343.0992...,50590.6570...]K이고 He simplex/원temperatureguard 내부다. 최초 이탈 전을 가정하고 ne<=nH0*(.97+r(.32+2*.61))를 쓴다.

n_e beta,alpha,DR 및 RR kinetic 계수의 전체8Tcell구간상한으로 모든 positive inflow/loss를 따로 적분한다. h예시는
h>=h0-L*ne_max*hmax*alpha_Hmax,
h<=h0+Pmax+L*(ne_max*(1-hmin)*beta_Hmax+qHHmax).

HeII loss=ne*x*(alpha1+DR1+DR2+beta2), inflow=ne*((1-x-z)*beta1+z*alpha2). HeIII loss=ne*z*alpha2, inflow=ne*x*beta2를 같은 방식으로 제한한다. 양의 RR kinetic과DR에너지/CI threshold sink/HH sink를 Lsink로 상계하면
w>=w0*exp(-2HL)-L*Lsink,
w<=w0+(13.7-chiH)*Pmax.

L=8e11s에서 계산된 h [.8999879732...,.96140456996...],x [.29999489638...,.30025257202...],z [.59995663346...,.60000015016...],w [13.3170074381...,13.6263584845...]가 모두 B의엄격한내부다. 따라서 first-exit는 불가능하다. 안전하게47241<T<50319K다. 정확한 반올림 방향은 rationalJSON을 따른다.

유한cohort/fixedbirth/처방cutoff와 state-Lipschitz source, 위 compact영역으로 원IC의 유일한 piecewise-in-time exact-real해가L까지 존재한다. Shear에 대한C2나event순서불변은 이 시간별영역/차이상계의 가정이 아니다. 이것이 native solver의수락을증명한것도아니다.

## 3. Thermal/He feedback을 유지한 닫힌 비교계

같은eps의 ON(lambda)/OFF를1/0으로 쓰고 U=(|Delta h|,|Delta x|,|Delta z|,|Delta v|,V), V=sum_j|Delta p_j|로 둔다. 절댓값합을 |sum Delta p|로 바꾸지 않는다. Fcoll은 HH/photo를 제외한 전체기체CI/RR/DR+단열식이다. B에서 intervalJ로 A_ii=upperJ_ii, A_ik=sup|J_ik|를 만든다. 음의 diagonal을 유지한다.

Photo의 정확한 차이는
Delta R=(1-h1)*sum a_j Delta p_j-Gamma0*Delta h,
Gamma0=sum a_j*p0j>=0.
H행의 음의 photo damping만 버리고 |Delta R|를 전체절댓값으로 부풀리지 않는다. Thermal행에는 gamma_max*a_*Pmax/w0*|Delta h|와gamma_max*a_*(1-hmin)/w0*V를 더한다.

Photon에서는 Delta p_j'=-a_j(1-h1)Delta p_j+a_j*p0j*Delta h여서 D+V<=a_*Pmax*|Delta h|다. 따라서 constantMetzler M에 대해
D+U<=M U+lambda f,
f=(qHHmax,0,0,chiH*qHHmax/w0,0),U(0)=0.
M의4gasblock은A에위thermal항을더하며 M_hV=a_*(1-hmin), M_vV=gamma_max*a_*(1-hmin)/w0, M_Vh=a_*Pmax,M_VV=0이다.

같은 additivebirth에서 차이는 연속이고 cutoff 양쪽에서 동일상계가성립한다. 양의비교정리에따라
U(t)<=lambda*b(t), b(t)=integral_0^t exp(M(t-s))*f ds.
b'(t)=exp(Mt)f>=0이므로 b(L)이prefix전체의상계다. 물리적photonclosure나 순수H/isothermal 축약이아니다. Thermal/He피드백은gasJacobian에그대로남긴다. hON>=hOFF를가정하지않는다.

## 4. 구간평가와 실제 B_h

M은고정4gasbox와8개Tcell의 intervalfirstjets에서구한다. Tcell의rate도함수와전체box의EOS도함수를결합하는의존성손실은보수적이다. 원FT03의RR kinetic=(kB/eV)*T*alpha*(1.5+g)와그T미분까지유지했다. LCS/FT03구간평가는새로수행했다.

Q=[[LM,Lf],[0,0]]의6차증강matrix에positive shift를주고128차Taylor action과 nu^129/129!/(1-nu/130) tail을더한다. nu<130을확인했다. Fraction/10^-70outwardgrid, exp/log급수tail/isqrt산술을사용하며 mpmath100자리expm은보조대조다. Formal verification은아니다.

안전한uniform상한(lambda=1):
B_h<2.874e-7,
B_HeII<2.407e-10,
B_HeIII<1.150e-11,
B_w/w0<2.346e-7,
V<1.075e-7,
B_T<.01874K.

마지막은EOS유한차이 |DeltaT|<=(2eV/(3kB))*w0/Pimin*|Deltav|+Tmax/Pimin*(|Deltah|+r|Deltax|+2r|Deltaz|)에서나온다. 0<=lambda<=1에는상한도lambda배할수있다. 전체[0,L]와|eps|<=.01에uniform하므로TH02epsilon_c의cohort생애에도적용된다.

## 5. Terminal source 상계와 상한의 한계

TH03원천gain1.051e-4/1.030e-4를곱하면 두기존label(tb6.5e10,index9와tb7e10,index8)의 |K_Dh|<3.020e-11,2.960e-11. 기존Lambda와이번Bh를곱해 |S|<3.967e-6,3.940e-6. TH03온도식에DeltaT/Pi상계를넣으면 |K_DT|<8.155e-7,7.998e-7K다. sourcegain/geometryroot의oldproof를재실행하지않았다.

이것은TH02terminal prehistory/group정칙성가정아래의각label기여상계다. signed기울기,전체동시군,전체A의오차나2.4e-13신호검출은미인증이다. 원 ON/OFF효과의사전상계는native수치오차막대가아니다. sourceconstants의exactdecimal정의/물리fit오차/runtime반올림은서로다른문제다.

최종73core+220independent=293checks; symbolic7/ratepoint88/gasJpoint96/exactDini18등. 원2helper실패와수정을보존했다: Interval*Jet dispatch TypeError와exacttail정수직렬화제한. 수학적first-exit실패가아니며tail수정은outward상향으로만행했다. Native/Rust/BEroot/gasIVP/history/NCP/oldproofsuite0,형식증명/TDD/독립agent심사없음.

미해결은signedopticalmemory/parameter정칙성/4경로관측량오차/실제ON06의point+thermal+HHcounter+intervalJet/root/model/checkpoint통합,전체1e13s,경험적율정확도다. B_h를다시null입력대기로돌리지않는다. 본전체수식과조건부인증은직접유도이며원문헌이이S0수치를제시했다고하지않는다.
