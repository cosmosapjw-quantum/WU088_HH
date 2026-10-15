# PHYS54 — weighted noncentral screened outgoing DtN: proved reduction and open exterior lemma

PHYS54는 PHYS49–52를 다시 실행하지 않고 그 범위를 접합했다. PHYS50은
`r=20..27`에서 ℓ>=21의 두 Dirichlet trace에 대한 양의 finite-collar DtN을,
PHYS52는 ℓ=21..28의 유한 400-channel outgoing Robin match를 보였다. 둘 중
어느 것도 무한 angular screened exterior DtN의 정리는 아니다.

경계 구면에서 `W Y_lm=(l+1)Y_lm`, `X=D(W^(1/2))`로 둔다. 중앙 Coulomb와
screened outgoing DtN을 각각 `Z_C`, `Z_S`라 하자. 다음은 실제 증명된
Hilbert-space reduction이다.

```
-Re <g,Z_C g> >= c_C ||W^(1/2)g||^2
|Re <g,(Z_S-Z_C)g>| <= epsilon ||W^(1/2)g||^2
-------------------------------------------------
-Re <g,Z_S g> >= (c_C-epsilon)||W^(1/2)g||^2.
```

따라서 `epsilon<c_C`이면 `Z_S:X -> X*`의 real-principal sector가 coercive다.
이는 triangle inequality와 form domain 완비성만 쓰는 보조정리이며, 전류의
uniform lower bound를 쓰지 않는다. 따라서 PHYS53의 central current decay는
이 방법의 반례가 아니다.

새 실제 diagnostic은 `r=27`, ℓ=21..256, depth 1152의 기존 Coulomb CF를
직접 평가해 `-Re Z_l/(l+1)`을 기록한다. 또한 원래
`S(s)=(1+1/s)e^{-2s}`, `s>=r-0.7`으로부터
`||2S||_{r>=27} <= 2(1+1/26.3)e^{-52.6}`을 분리해 기록한다. 이 multiplier
상계는 exterior resolvent를 거친 DtN 차이 `Z_S-Z_C`의 weighted norm 상계가
아니다. 이를 epsilon으로 대입하지 않았으며, finite CF 표본도 all-ℓ
certificate로 대입하지 않았다.

따라서 남은 정확한 lemma는
`||W^(-1/2)(Z_S-Z_C)W^(-1/2)||_Re <= epsilon < c_C`이다. 이는 noncentral
screened exterior Volterra/resolvent의 uniform weighted estimate를 요구한다.
PHYS54는 이 lemma를 OPEN으로 남긴다. 실제 driven `xi=Fy-phi`, regular origin,
incoming adjoint, sigma(E), identical-H Maxwellian k_HH(T)는 이 결과로부터
나오지 않으며 `HH_R10=OFF`다.
