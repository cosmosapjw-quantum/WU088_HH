# HH-TH02 정리와 인증 범위

전체 증명은 START의 ZIP/THEORY_KO.md에 있다. 아래는 직접 유도의 검색용 요약이다.

## 정의

Prescribed H_i=H(1+eps,1-eps,1),H>0,|eps|<1,서명(-+++),proper seconds,공통온도/zero tilt를 쓴다. nH=nH0 exp(-3Ht),r=nHe/nH고정,gas y=(h,y1,y2,w),w=eV/H,광자p_j=photon/H다. Pi=1+h+r(1+y1+2y2),C=2*eV_erg/(3kB),T=Cw/Pi. 고정 단일 HH provider의강도lambda만수학적으로변화시키며LCS/KS혼합이나물리오차분포가아니다.

D(eps)=O(eps,lambda)-O(eps,0),A(e)=D(e)-D(0),e>=0. 고정birth와prescribedgeometry의photoevent tau_j(eps)는gas/lambda와독립이다. 현재retained모형의13.6eV는physicalphotojump,chi=13.598434599702eV는별도binding상수이며그분류경계에두번째physicaljump는없다.

## A. 조각별 shear 응답

D연속,유한분할의각조각에서C2,각끝점까지D'절대연속및일방극한을가정한다. c0=D'(0+),m=D''regular,K_j=D'(e_j+)-D'(e_j-)이면

A(e)=e*c0+integral_0^e (e-s)m(s)ds+sum_(0<e_j<e)(e-e_j)K_j.

각조각의D'기본정리를연결하고다시적분한정확한식이다. |m|<=M이면 |A|<=e|c0|+e^2 M/2+sum(e-e_j)|K_j|. 이식은positiveeps에서parity를요구하지않는다. 원점부근C1짝함수는c0=0을주지만구간내부K=0까지주지않는다. 전체C1이면내부K도0이다. 단순piecewiseC2만쓰며singularcontinuouspart를몰래제외하지않도록D'의조각별AC를명시했다.

root e_j가[l,u]에있으면hingeweight는[max(e-u,0),max(e-l,0)]다. 실제S0의모든eventsector와c0/m/K를이번에상계한것은아니다.

## B. 관측종료시각을통과하는photoevent

tau(e_c)=tstar,tau'!=0,source가before에+X/after에0,identityreset,smoothprehistory와다른topology변화없음을가정한다. activecontinuation z_a를쓰면
z(tstar,eps)=z_a(tstar,eps)-X_c*(tstar-tau(eps))_++O((eps-e_c)^2).
따라서smoothscalarO의increasingeps기울기jump는

[O_eps]_(e_c)=-abs(tau')*gradO.X.

유한동시terminalgroup의일차항은합산할수있으나비정칙prehistory와내부ordering의이차항을대신하지않는다. 실제HIchannel에서a=c*nH*sigma(Ec),R=a*(1-h)*p_j,X=R*(1,0,0,Ec-chi,-e_j)다. 그러므로 K_h=-abs(tau')R이며

K_T=-abs(tau')*[C(Ec-chi)-T]*R/Pi.

정확한상수에서C(Ec-chi)=12.110477417080599688986846041245819900640930460964...K. 35000<=T<=60000K이면photoheat>0이어도이채널의Tdot은음수이고terminalK_T는양수다. 전체thermalRHS부호주장이아니다.

유한ON/OFF차이는
K_Dh=-abs(tau')*a*[(1-h1)*(p1-p0)-p0*(h1-h0)].
B_l=[C(Ec-chi)-T_l]/Pi_l라두면
DeltaB=-DeltaT/Pi1-[C(Ec-chi)-T0]*DeltaPi/(Pi1*Pi0),
K_DT=-abs(tau')*(B1*DeltaR+R0*DeltaB).

neutral감소와photon생존이경쟁하므로K_D부호는단일경로K_h에서추론하지않는다. 실제endpointpositivity/correlation/prehistory는아직없으므로actualS0cuspamplitude는미인증이다. binding분류경계에서는X=0이다. 불연속inventory관측에는smoothO정리를바로적용하지않는다.

## C. 두 exact-real parameter근

H=1e-14/s,Eb=13.7eV,Ec=13.6eV,tstar=8e11s는exactdecimal이다. TH01의공급binary64방향성분v를정확dyadic으로읽고n_i^2=v_i^2/sumv^2로정규화한다. a=tstar-tb에서
G(eps)=Eb^2*[nx^2 exp(-2H(1+eps)a)+ny^2 exp(-2H(1-eps)a)+nz^2 exp(-2Ha)]-Ec^2.

exp는라이브러리값이아니라유리수TaylorP_N과tail B_N=|x|^(N+1)/(N+1)!/(1-|x|/(N+2))로enclose한다. N24,|x|<=1. omitted절대항의비를기하급수로상계한식이다.

- tb6.5e10s,index9: [0.00491733430631354120048607500286,0.00491733430631354120048607500287]. 양끝G는엄격히음수/양수,전체[0,.01]G'>0.
- tb7e10s,index8: [0.00538116358643261432341304937449,0.00538116358643261432341304937450]. 양끝G는엄격히양수/음수,전체[0,.01]G'<0.

각폭1e-32,각각존재/유일성이증명된다. 서로다른cohort의epsilon근2개이며BE근이아니다. tau_eps는각각약+4.88860883236667e11s,-4.82177695176021e11s로시간횡단도0을배제한다. 실제native반복normalize/pullback의근이나gas응답을인증한것은아니다.

추가로declaredcoarsebirth t_b=5e9*k,k0..160에대해모든정규화방향에서|eps|<=.0032에terminalfitcrossing이없다는부호상계를얻었다. youngage<=7.30e11,oldage>=7.35e11와최대/최소H의exp경계를쓴다. finebirth/내부event순서/C2/nativeparity까지승격하지않는다.

## D. 같은event시각오차의정확한관측량식

fixedgeometry/birth/IC,orderedprescribedevents,공통smoothactivetube를가정한다. tau_j^theta=tau_j+theta*deltatau_j가theta0..1에서순서/birth/종료경계를넘지않는sector를쓴다. -psi'=DF^T psi,psi(tstar)=gradO,identityreset의처방event에서adjoint연속이다. 일반state-dependentevent에는saltationtranspose가필요하다.

W_lj^theta=psi_l,theta(tau_j^theta)^T X_j(tau_j^theta,z_l,theta)이면

D(tau+deltatau)-D(tau)=integral_0^1 sum_j(W_1j^theta-W_0j^theta)*deltatau_j dtheta.

이는finitehomotopy항등식으로linearizationremainder를생략한식이아니다. |deltatau_j|<=eta_j, sup_theta|W1-W0|<=B_j이면|E_D_event|<=sumB_j*eta_j다. 실제adjoint/weight차이는미계산. 네경로에는각geometry의실제timingerror를따로쓰며의도된기하학적시각차이를numericalerror로세지않는다. Sector변화/terminalevent는별도접속한다. BE/원천quadrature/각도/전체flow오차를이식으로대신하지않는다.

ExactE(t_hat)의오차deltaE<Ec가인증되고 -dlogE/dt>=Hmin>0이면
abs(t_hat-tau)<=deltaE/[Hmin*(Ec-deltaE)].
Native관측energyresidual만으로deltaE를인증하지않는다. photoenergycovector는X를소거하지만hcovector는R>0이므로에너지PASS가관측량timing오차상계는아니다.

## 검산과남은의무

최종symbolic14를포함한총53assertions,정확parametercertificates2개통과. 첫11/50과후속14/53두proof호출,양쪽exit0/stderr0. manufacturedpiecewise10사례는gas모형이아니다. 동일2근재검사를4고유근으로세지않는다. Native/Rust/BE/IVP/history/실제adjoint/새원자율평가0. 형식증명기와독립agent검토없음.

실제전체sectorpartition/ON-OFFendpoint구간/K와곡률/adjointweights/전구간continuouserror/ONrootbox/물리율오차는OPEN이다. Sourcepoint계산과interval인증은계속같은provider로결속해야한다. TH01J/H/rankone는계승하고재검산하지않았다.

배경원전: Kong etal arXiv2306.06862v3 DOI10.1109/JPROC.2024.3440211; Burden etal arXiv1407.1775v3 DOI10.1137/15M1016588; Corner/Sandu/Sandu arXiv1802.07188v1. 이번공식abstract/metadata를확인했고HTMLfulltextcachemiss를기록했다. 위HH특수식과rational수치는직접증명이며원전에이미있다고하지않는다.
