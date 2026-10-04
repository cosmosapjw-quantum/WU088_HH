# HH-F1C: cutoff를 통과하는 raw HH implicit source의 비유일성

## Source와 범위

기존 Grackle 3.4.1 k57 reference의 정확한 십진수 식만 분석한다. k(T)=1e-20 for 0<T<=3000 K, k(T)=1.2e-17*T^1.2*exp(-157800/T) for T>3000 K, 단위 cm3/s. floor는 물리적으로 승인된 저온 rate가 아니다. 실제 Grackle 전체 solver/보간 table/native binary64/경험적 오차의 인증은 아니다. KS에는 새 cutoff를 추가하지 않는다.

원 Grackle pin: af7939494ce65007887ada7b98d1813df6843346, src/clib/rate_functions.c SHA256 a900e726413da39bb24fc506846a09f7e0e4addbd5152197ca76d0e22ad02cea. 그대로 보존한 F1B hh_external.py SHA256은 8c02df302adc895be1327cb2e55bae03ebed8ec06ee7496ff4eeda20fdcdc197이다.

## 실제 F03 좌표와 source guard

Y=(h,y1,y2,u,N0,N1,N2), P=nH(1+h)+nHe(1+y1+2y2), T=2u/(3kB P). 밀도와 kB가 고정이면

S=2u-3kB*3000*P, sign(T-3000)=sign(S).

population simplex 안에 놓인 직사각형 box에서 S_min은 u_min과 모든 population maxima로, S_max는 u_max와 population minima로 정확히 계산한다. S_min>0은 SMOOTH_ANALYTIC, S_max<0은 SMOOTH_FLOOR다. 0에 닿거나 교차하면 일반 smooth certificate 경로를 거절한다. 정확히 cutoff인 값은 floor이지만 global derivative는 인정하지 않는다. nH=0은 HH source가 항등적으로 0인 별도 경우다.

이 predicate는 supplied box의 source 분기만 분류한다. actual trajectory enclosure, 전체 F04 Jacobian/root/remainder, 물리 domain 또는 positive-state certificate가 아니다. variable-density box 또는 simplex와 교차한 비직사각형의 sharp extrema까지 구현했다고 하지 않는다.

## 정리

HH-only source q=nH(1-h)^2 k, fHH=(1,0,0,-chi*nH,0,0,0)^T q. no extra 1/2이며 chi는 binding energy, kB*157800이 아니다. helium/photon을 고정하고 x=h-h0라 두면

u(x)=u0-chi*nH*x, P(x)=P0+nH*x,
T'(x)=-2nH(chi*P0+u0)/(3kB(P0+nH*x)^2)<0.

w=1-h0, e=u0/(chi*nH), d=(2u0-3kB*3000*P0)/(nH*(2chi+3kB*3000))라 둔다. 가정은 nH>0, hot start, 0<d<min(w,e), dt>0이다. 물리 domain은 0<=x<=w, x<e다. x=e는 금지된 u=0 경계다.

G(x)=x-dt*nH*(w-x)^2*k(T(x)). 각 smooth branch에서 q'(x)<=0이므로 G'(x)>=1이다. 따라서 branch마다 root는 최대 하나다. 그러나 ka=k(3000+) 약 2.5576257963333753e-36, kf=1e-20이라 kf/ka 약 3.909876110233189e15이다. x=d에서 G는 아래로 도약한다:

G(d-)=d-dt*qa, G(d)=d-dt*qf,
qa=nH*(w-d)^2*ka, qf=nH*(w-d)^2*kf.

tau_a=d/qa, tau_f=d/qf로 두면 hot root는 dt<tau_a일 때만 하나다. hot branch는 x<d이므로 dt=tau_a의 limit zero를 root로 세지 않는다.

e<w일 때 tau_E=e/(nH*(w-e)^2*kf)로 두면 cold root의 필요충분조건은 tau_f<=dt<tau_E다. dt=tau_f의 root는 cutoff 그 자체이며 dt=tau_E의 zero는 u=0이므로 제외된다. w<=e이면 tau_E=+infinity로 읽는다. w=e에서도 끝점은 제외되지만 G의 극한은 w>0이다.

그러므로 tau_f<=dt<min(tau_a,tau_E)에서는 서로 다른 두 양의 온도 root가 존재한다. 두 root가 모두 smooth interior에 있으려면 dt>tau_f를 요구한다. 이는 HH-only 정리이며 전체 coupled REI residual의 root 개수 주장이 아니다. F1B는 이미 smooth 결과의 적용 범위를 제한했다. 이번 결과는 F1B의 잘못된 전역 주장을 정정하는 것이 아니라 그 제한을 구체화한 것이다.

## 적분 없는 증거

합성 pure-H nH=1 cm^-3, h0=0, kB=1.380649e-16, chi=13.598434599702*1.602176634e-12 erg를 썼다. 이는 진단 상수이지 F07 domain 승인이 아니다. 각각 T0=3001과 T0=3000+1e-12 K에서 dt=2*tau_f를 택했다.

정해진 네 점의 outward signs는 G(0)<0<G(d/2), G(3d/2)<0<G(2d)다. 각 bracket box 전체가 hot/cold 내부임도 exact separator로 확인했다. 중간값 정리와 branch 단조성으로 정확히 두 root가 따른다. root finder는 호출하지 않았다.

두 step은 각각 약 1.848425638034438e15 s와 1848.3914720504585 s다. 둘째 예의 가장 작은 positive residual margin은 약 3.41655e-34이며 native binary64로 같은 분해를 얻었다고 하지 않는다. cutoff 여유 없이 고정 양의 timestep 상한만으로 uniform uniqueness를 주장할 수 없다는 점을 보여주며, 실제 시간간격 권고가 아니다.

별도로 T0=2000 K floor-only 예에서 dt=2*tau_E를 택하면 G'>0임에도 x->e에서 G의 supremum=-e<0이다. 양의 온도 root가 없다. T=0에서 rate를 호출하지 않고 exact one-sided limit만 사용했다.

## 소비자 전달과 검증 한계

full/half1/half2 각각의 실제 인증 box 전체에 separator를 적용한다. smooth 판정만으로 F04가 닫히지 않는다. crossing이면 기존 smooth 경로를 거절하고 소비자가 branch-preserving step, 명시적 piecewise boundary/continuation, 또는 별도 승인된 model scenario를 선택해야 한다. silent smoothing/clipping/zero replacement와 arbitrary root selection을 하지 않는다. accepted two-half events는 half1.events+half2.events이며 최종 endpoint 하나로 대체하지 않는다.

신규 unit 20개는 RED 20 assertion failures 뒤 GREEN, 이후 최종 동일 20개도 PASS다. 신규 SymPy identity 8개, 두-root 사례 2개, residual enclosures 8개(analytic 4개 mpmath150, floor 4개 exact rational), no-root 사례 1개. proof script는 1회 실행했다. SymPy 항등식 검산이 모든 부등식 가정의 자동 증명은 아니며 존재/유일성 논증은 위 수학적 가정과 증명을 따른다. 원자 primitive/NCP/root finder/state stepper/consumer/history/old suite 실행은 모두 0이다. 독립 제3자 과학 검토는 하지 않았다.

HH-F1 WAITING_ON_REI_DOMAIN, HH-F2 NOT_INTEGRATED, physical/production admission=false, legacy 24/289·265 unbounded·epsilon null·B22 OPEN은 유지한다. 전체 증명과 정확한 witnesses는 START_KO.md의 sealed ZIP에 있다.
