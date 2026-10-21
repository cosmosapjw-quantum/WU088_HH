# 기존 z=4 endpoint에서 z=2까지의 동일 모델 연장

## 과학적 허용 범위

실제 원본 `pilot.py`, `component_pilot.py`, `SourceLock`, `CanonicalMomentumFV`를 읽었다.
기존1231개의 이력은 \(a_{\rm ref}=1/21\)에서 \(a_{\rm end}=0.2\), 즉 평균 redshift
\(\bar z=20\to4\)까지 저장되어 있다. 현재 사용자의 \(20\to2\) 목표에는
\(a=1/3\)까지의 후속 구간이 필요하다. 완료된 \(20\to4\) 적분은 재실행하지 않는다.

원본8개 상태는 \(y=(\tau,b,v,E_0,E_2,E_4,E_6,E_8)\)이며
\(\tau=H_{\rm ref}t_{\rm elapsed}\), \(v=s/H_{\rm ref}\)다.
원본 코드의 `q`라는 state 변수는 여기서 \(v\)로 썼으며 deceleration parameter \(q\)와 다르다.
저장 endpoint의8개 값을 모두 그대로 사용하고, \(x=\ln(a/a_{\rm ref})\)도 원래 원점을 유지한다.
\(\tau,b\)나 radiation multipole을 재설정하면 다른 초기값 문제다.

`SourceLock.aend`는 `xmax=log(aend/aref)`를 통해 실행 구간만 정한다.
실제 `Reduced.rhs`와 진단식은 \(H_0,\Omega_m,\Omega_r,\Omega_\Lambda,a_{\rm ref},H_{\rm ref}\),
현재 \(x,y\)를 사용한다. 원래 고정된 \(a_{\rm end}\)에서 끝나는 외삽 table은 이 경로에 없다.
Massive canonical moments는 원래 질량/온도비30, \(A_m\),24×12 Gauss3 weights와
\(e^{-x},b\)에서 직접 평가된다. \(x\ge0,|b|\le1\)이라는 구현 domain을 유지한다.
\(a_{\rm end}\)만1/3로 바꾼 새 실행 객체는 같은 방정식을 더 긴 구간에서 평가한다.
기존 vendor lock의 bytes와 기존 결과 identity는 그대로 보존한다.

기존 matter/radiation 성분 계약의 \(\bar z=20\to4\) 범위는 당시 실행 범위다.
현재 사용자의 \(\bar z=20\to2\) 요청에 따라 새로운 \(4\to2\) 실행 계약을 추가한다.
모든 cosmology·canonical distribution·closure·frame·단위·정밀도 기준은 유지한다.
이 연장은 finite even \(L=8\) collisionless 모델의 preliminary 결과에 해당한다.
Native H/He chemistry, UV source, Thomson coupling 또는 전체 angular convergence를 추가하지 않는다.
다른 warm729/HH74control63 모델의 이력과 하나의 과학 ensemble로 합치지 않는다.

## 재개 입력과 실행 점검

각 case마다 원본 NPZ/JSON hash와 저장 endpoint를 묶는다.
Radiation slice는 \(A_m=0\), matter/mixed slice는 원본 sidecar의 \(A_m\)를 사용한다.
이 값으로 같은 canonical packet distribution을 복원하고 원래 \(a_{\rm ref},H_{\rm ref}\)를 유지한다.
`initial()` 및 초기 target inversion을 호출할 이유가 없다.
새 적분의 첫 sample은 원본 endpoint와 일치해야 한다.

각 tail에서 finite state, positive \(H,E_0\), chart \(|b|\le1\),
sampled angular brightness와 massive packet nonnegativity를 기록한다.
Sampled brightness 검사는 angular continuum positivity certificate와 구별한다.
새 적분 실패는 원본 이력의 실패로 바꾸지 않고 해당 tail의 결과로 남긴다.
이 문서와 `TIME_DOMAIN_PHYSICS_PREFLIGHT.json` 작성 시점에는 새 ODE 실행이0회였다.
후속 실제 실행 횟수·결과는 별도 execution receipt가 결정한다.

## 두 sampling 구간의 기억량 연결

기존 구간과 새 tail의 sampling 간격은 일반적으로 다르다.
각각의 홀수 node 균일 grid에 composite Simpson을 적용하고,
합쳐진 비균일 display grid에는 균일-grid 구현을 다시 적용하지 않는다.
원본 endpoint를 \(x_*\)라 하고 원본 기억량을 \(D_*,J_{m,*},J_{r,*}\)라 두자.
Tail에서 zero-source unit-initial solution

\[
G_*(x)=e^{-3(x-x_*)}H_*/H(x)
\]

및 tail-only source integrals \(j_m(x),j_r(x)\)를 계산한다. 그러면

\[
D(x)=G_*(x)D_*,\qquad
J_A(x)=G_*(x)J_{A,*}+j_A(x).
\]

원본 endpoint의 sampled reconstruction defect가
\(\delta_*=S_*-D_*-J_{m,*}-J_{r,*}\)이고
tail의 local sampled defect가
\(\delta_{\rm tail}=S-G_*S_*-j_m-j_r\)이면

\[
\boxed{\delta_{\rm global}(x)=\delta_{\rm tail}(x)+G_*(x)\delta_* .}
\]

따라서 이전 오차를 새로운 초기조건에 흡수하여 숨기지 않는다.
그림에서 이어붙이는 원본 samples는 그대로 보존하며 중복 join sample만 한 번 표시한다.
위 기억량과 residual은 같은 trajectory의 sampled 진단이며 연속시간 인증은 별도다.

## 독립 확인

Radiation case와 mixed case 한 개씩의 실제 원본 endpoint를 읽어,
`aend=.2`와 `aend=1/3` 객체에서 같은 \(x,y\)의 RHS와 모든 diagnostics가
byte-identical임을 확인했다. 원본 aref/href/mpref도 같았다.
\(x=\ln7\)에서 동일 저장 vector를 넣은 RHS point evaluation은 finite였다.
이 마지막 확인은 더 늦은 시각의 실제 해를 계산한 결과가 아니라 RHS domain 점검이다.
정확한 source hashes와 6개 RHS 평가 기록은 `evidence/TIME_DOMAIN_PHYSICS_PREFLIGHT.json`에 있다.
`HH_R10=OFF`; production admission은 발급하지 않는다.
