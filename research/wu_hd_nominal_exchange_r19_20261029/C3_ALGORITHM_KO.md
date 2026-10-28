# R19 C3 수치 알고리즘

`m=min(a,b),M=max(a,b),delta=M-m`, `z=-expm1(-k*delta*tau)`를 계산해 `xi=m*(M/(delta+m*z))*z`를 얻는다. Survivor는 큰 수의 차 대신 `m*(delta/(delta+m*z))*exp(-k*delta*tau)`, `M*(delta/(delta+m*z))`로 구한다. `delta=0` 분기를 직접 구현한다.

부피 `v(t)>0`를 공급받으면 `tau=int_0^t ds/v(s)`를 **외부에서** 공급받거나 `theta=const`일 때 `tau=-expm1(-theta*t)/theta`를 계산한다. 반환된 comoving densities를 `v`로 나눈다.

시간 복잡도 O(1), 공간 O(1). 비유한 density/time/clock/expansion은 오류. float64 오차를 80자리 mpmath 및 DOP853/Radau와 비교. 소스 진위는 PDF SHA·source code blob에서 확보하고, 수치 오차를 source 불확실성으로 오인하지 않는다.