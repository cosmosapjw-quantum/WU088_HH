# R10 실제 결과

Primary 175/175 PASS; independent 469/469 PASS, 9860 component comparisons /0failed. 각1회이며 Python 전체OS CPU합 0.511886s다. 아래 계산은 저장된출력을읽는후처리이고추가solver/ODE호출0이다.

| 사례 | R9 R최종 | R10 raw R | R10 capped R | R 감소% | R9 E최종 | R10 capped E | E 감소% |
|---|---:|---:|---:|---:|---:|---:|---:|
|2state no reaction|0.06103515625|0.0557825400371|0.0557825400371|8.6058864|0|0|NA: both zero|
|2state nonlinear|0.0678043993242|0.060211915866|0.060211915866|11.1976266|0.000516508447396|0.000396434054403|23.24732414319801|
|2state coarse defect|0.0678051452369|0.060211915866|0.060211915866|11.1986035|0.000685196005486|0.00056512078897|17.52421432037029|
|native9 conditional|3.64476161178e-05|0.0487007749553|3.64476161178e-05|0|6.19120080246e-07|6.19079240657e-07|0.006596392256240802|

## 정확한 성분 비교

이 카운트는 독립적인 물리 사례 수가 아니라 저장한 clock/cell의 R,E성분 수다. 다음 less/equal/greater는 Fraction exact 비교다.

| 모드/영역 | 작음 | 같음 | 큼 | 합계 |
|---|---:|---:|---:|---:|
|raw_endpoints|963|200|381|1544|
|raw_whole|963|193|380|1536|
|capped_endpoints|1156|388|0|1544|
|capped_whole|1343|193|0|1536|

## Native9의 순간 수축률과 남은 보수성

Native9 lambda(K)=0, lambda(full A)=2.08539320323e-07다. K의 sparse 구조는 한 단계의 column overlap이0이어도 유한시간에 혼합될 수 있다. 이번 순간계수는 그 다단계 혼합을 포착하지 못해 raw R최종이R9의 1336.18547배다. 실제 관측된native9 raw endpoint성분381개, whole성분380개가R9보다크다. 이 결과를유효한R9block인증의소멸이나물리적발산으로해석하지않는다.

동일시각의R9인증상계와교차하면최종R은그대로이고 E는0.00659639226%감소한다. 최종capped/sample비율은R 310.953728, E 906.981311다. 표본은cap이나연속구간인증으로사용하지않았다.

## 수치·자원과 한계

가장넓은raw ideal-comparison endpoint interval폭은 6.27155624e-35다. lower배열은비교방정식의해를둘러싼다. 실제물리오차lower를주지않는다. Dyadic128/Taylor96는고정했고Decimal160reference의1e-80guard도실행후변경하지않았다. 수렴차수나속도향상비교는수행하지않았다.

Wolfram은15개잔차0/all_zeroTrue와Infinity/Power경고를함께반환했다. QUALIFIED_SYMBOLIC_CORROBORATION으로보존하며원인을별도확정하지않았다. 직접증명과독립reference의zero/resonance/near-resonance검사를함께사용한다. 기존R8원래726/727PASS+1FAIL과별도phi24/24PASS는그대로다.

Actual HD reactive array, named physical consumer, density and clock remain INPUT_PENDING. HH_R10=OFF; production=NOT_ISSUED; L4_ready=false; physical/central delta0.

## 저장 표본과 해석적 상계의 작은 차이

No-reaction 사례에서 저장된 수치표본이 새 해석적 상계를 소폭 넘는 지점이 있다. 최대 초과는 4.00132064349e-12이며 사전에 고정한 containment 허용오차 4.37765637079e-11 이내다. 정확한 비교해를 둘러싼 dyadic interval과 유한오차의 과거 ODE 표본은 역할이 다르다. 저장표본의 strict containment 또는 그 표본 자체의 exactness를 주장하지 않는다.

## 그림의 범위

BOUND_COMPARISON 그림의 선은 저장 endpoint 값을 연결한 시각적 안내다. 점 사이의 선형 보간을 인증 상계로 사용하지 않는다. 전체 셀 인증은 별도의 whole_cells_upper 배열과 증명에 있다.
