# PHYS19 Wolfram·xAct 순수 곡률 검산

## 실제 실행 결과

Wolfram 15.0.1 Linux에서 독립적인 두 요청을 실제 실행했다. 첫 요청은 공식 xAct 1.3.0 archive의 SHA256을 대조한 뒤 xTensor 1.3.0과 xPerm 1.2.4를 로드했다. 모든 tensor canonicalization에는 `$xpermQ=False`인 Wolfram Language group backend를 사용했다. 패키지 초기화의 external xPerm 연결 메시지는 원 응답에 남아 있고, 실제 검산의 backend 선택은 별도 필드로 기록했다.

`RUN01`은 6 tensor 항등식, 13 scalar 항등식, 14 matrix component에서 모두 정확한 0을 반환했다. Peano kernel의 두 branch 부호, 양의 interpolation weights, 최대 kernel 질량 1/8은 모두 True였다. 도구 호출 경과는 13.222 s, kernel의 대수 연산 경과는 1.999516 s다. `RUN02`의 generic Hessian 방향 수축 두 항등식도 정확히 0이며, 제공된 세 interval에서 strict axis concavity, negative determinant, opposite-sign directional curvature를 exact rational arithmetic으로 확인했다. 두 요청의 timeConstraint는 각 60 s였다.

## 검산 범위

- C3: 임의의 local C2 two-state jet에서 pure implicit second derivative와 `2 H_gtheta p`.
- C6–C8: rational survival의 ordinary second derivative, carried incoming의 `2 A_theta Q_theta`와 nonzero `Q_thetatheta`, carried gas second derivative.
- C10: symmetric residual Hessian의 pure contraction 차이와 correlated defect 식.
- C12: stage Hessian 및 parameter-gradient 차이, factored zeta, survival difference의 pure product.
- Common adjoint: 임의의 primal·adjoint residual을 남긴 scalar identity와 symmetric Hessian의 dummy-index canonicalization.
- C13: `b f`의 pure birth derivative factor 2, arbitrary symbolic two-slot remap에서 일곱 sector value 및 lambda-lambda/b-b derivative. R과 diagonal survival의 순서를 유지했다. Local absorption/outgoing partition도 검사했다.
- C15–C16: finite temperature quotient의 second derivative와 같은 Full temperature covector.
- C17–C20: four-corner bilinear coefficient identity, Peano kernel 질량·부호·convex weights·1/8 bound. Polynomial kernel identity는 임의 계수의 6차까지 확인했다. 전체 C2 정리의 범위는 부분적분 유도로 연결한다.

R, R_F, birth vector와 stage physical coefficients는 lambda,b에 대해 고정되어 있다. Survival functions는 generic C2 함수로 두고 rational denominator가 0이 아닌 영역에서 단순화했다. Photon 검산의 matrix는 2 slots다. 원 33 groups와 두 guards의 실제 수치 interval, source callback, nonlinear root, history, 수치 plot 데이터는 이 symbolic 요청의 입력이 아니다.

## Hessian의 구성적 방향 판정

Root가 제공한 Kelvin 단위 입력은 다음과 같다.

\[
F_{\lambda\lambda}\in[-4.510292217171,-3.084478303660]\,10^{-14},\quad
F_{bb}\in[-4.912098573204,-4.450662359403]\,10^{-11},
\]
\[
F_{\lambda b}\in[-2.668505746423,-2.118796636045]\,10^{-12}.
\]

이 decimal endpoints를 정확한 유리수로 취급한 독립 Wolfram interval 계산은

\[
\det H\in[-5.748125770243094508263431,-2.2737991884457307123134366]\,10^{-24}\ {\rm K}^2
\]

를 준다. `v=(1,-1/24)`에 대해

\[
v^{T}Hv=F_{\lambda\lambda}-\frac{F_{\lambda b}}{12}+\frac{F_{bb}}{576}
\in[4.6183975047248333\,10^{-14},1.1426225209234792\,10^{-13}]\ {\rm K}
\]

이고, `w=(1,0)`에서는 `w^T H w=F_lambdalambda<0`이다. 따라서 좌표축 두 방향의 concavity와 양·음 방향곡률이 공존하는 indefinite Hessian geometry를 구체적 방향으로 확인한다. Exact endpoints는 `HESSIAN_GEOMETRY_EXECUTION.json`과 원 출력에 있다. 이 계산은 위 세 포함을 전제로 한다.

## 관찰된 진단과 provenance

첫 요청에서 `Symbol::undefined2`가 일부 temporary symbol 이름을 경고했다. 제출한 Module은 해당 이름들을 local로 선언하고 사용 전에 값을 대입한다. Kernel은 모든 지정 residual을 literal 0으로 반환했고 모든 명시적 logical check를 True로 반환했다. 경고 및 패키지 메시지를 원 요청·응답과 함께 보존했으며 동일 검산을 반복하지 않았다. 두 번째 요청에는 경고가 관찰되지 않았다.

- xAct archive SHA256: `7a6c5f600868a3922668b020a15c0692f76574ff2a559808c62d460cef1b07be`.
- 로드한 xTensor.m SHA256: `04e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36`.
- 첫 요청 source SHA256: `42c1caaf335d946c74ca12525d6cdf21772f04ad46fc59801a38164c1ae5516b`.
- 둘째 요청 source SHA256: `ec63e7b2fd0069750a3a0f3fc0b3a1e6bb0a36a91f4d18845a25c6564cd125de`.

`RUN01_REQUEST.json`, `RUN02_REQUEST.json`은 실행 전에 기록했으며 변경하지 않았다. `RUN*_RESPONSE.json`은 실제 provider response를 포함하고 `RUN*_OUTPUT.txt`는 text content를 그대로 보존한다. `WOLFRAM_XACT_EXECUTION.json` 및 `HESSIAN_GEOMETRY_EXECUTION.json`은 원 출력에서 확인한 결과와 범위를 정리한다. 이 검산은 PHYS19 수치 application의 scientific interval review와 별도로 연결한다.
