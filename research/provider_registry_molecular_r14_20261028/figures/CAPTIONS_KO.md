# R14 저장 결과 figure captions

이 caption은 실행 전 작성한 표시 계약이다. 실제 그림은 root가 허용한 S08의 단1회 rendering에서 성공한 PRIMARY_RESULTS와 그 바이트에 결속된 REFERENCE_RESULTS를 읽어 만든다. 실제 생성 후 PLOT_MANIFEST/RENDER_RESULT 및 root의 PNG 시각 검토 기록을 함께 따른다. Caption 작성 자체를 rendering 성공이나 독립 visual PASS로 세지 않는다.

## 그림1 — source 비음수성과 closed-cell R 인증

**(a)** 원래 quadratic source `g_r(s)=(s−1/4)^2`와 그 원래 degree2 Bernstein control polygon을 비교한다. 원래 middle coefficient `−3/16`은 음수지만 source 함수는 비음수다. 표시한 `s=1/4` 분할은 저장된 exact source vertex다. Control polygon과 함수값은 서로 다른 대상이다. 곡선은 저장된 source coefficients의 표시용 평가이며 새 forcing-bound 검증이나 unknown forcing의 sample quadrature가 아니다.

**(b)** 하나의 irrational interior maximum을 갖는 저장된 cubic R을 표시한다. 수평선은 해당 닫힌 셀의 저장된 outward upper certificate다. 마커는 저장된 critical-root box의 midpoint와 그 저장된 polynomial value다. 96-step box 폭은 그림 해상도로 분해할 수 없으므로 marker 크기를 인증 폭으로 해석하지 않는다.

**(c)** 같은 base cell 안에 두 critical points가 있는 다른 fixture를 확대한다. 최대·최소 모두 저장된 rootbox에서 가져오며 그림을 위해 root를 다시 풀지 않는다. 수평 whole-cell certificate와 확대된 세로축을 구별한다.

**(d)** initial downward jump에서 실제 endpoint `R(1)=1/3`은 채운 점, 왼쪽 극한 `R(1−)=4/3`은 열린 점으로 표시한다. 닫힌 셀의 supremum은 왼쪽 극한을 포함한다. 세로 점선은 jump 위치를 설명하는 표시이고 연속 trajectory가 아니다. 따라서 endpoint 값만 이어서 whole-cell 인증을 대신하지 않는다.

## 그림2 — 조건부 비교·supremum gap·유한 자원

**(a)** 같은 horizon의 quadratic `s^2`, affine `s`, constant `1` source에 대한 고정 exact endpoint controls를 비교한다. 각각 R은 `1/3,1/2,1`, E는 `1/12,1/6,1/2`다. Quadratic의 constant 대비 감소비 `R:2/3`, `E:5/6`은 해당 ideal comparison의 합성 산술 결과다. 실제 물리 오차 개선, native9 결과, R10/R11 capped 개선률 또는 속도 향상을 뜻하지 않는다.

**(b)** signed `d=+2`와 `d=−2` 사례의 저장된 E endpoint upper를 점과 연결선으로 표시하고, 각 닫힌 observation cell의 E upper certificate는 별도 수평 막대로 표시한다. 연결선은 저장된 endpoint bounds 사이의 표시용 연결이다. 두 endpoint 사이 전구간을 인증하는 대상은 수평 whole-cell bound다. 새로운 E ODE 또는 exponential propagation을 실행하지 않는다.

**(c)** 서로 다른 세 irrational-root fixture에서 저장한 exact supremum enclosure gap, outward dyadic interval width, proved gap bound를 로그축으로 비교한다. Width는 저장된 upper/lower의 차이일 뿐 새 root isolation 결과가 아니다. Exact zero가 있을 경우 별도의 `0 exact` marker로 표시한다. 로그축 표시용 하한은 데이터의0을 양수로 교체하지 않는다.

**(d)** full-capacity control의 original16/effective48/observation32와 actual base-cell 수, full blocks, 실제 overlap/root counts 및 사전 charge를 저장 결과에서 읽어 표시한다. `tau=2/17`의 비정렬 clock과 원래 t0의 global forcing memory가 대상이다. 최대 허용 한도와 실제 관측 count를 같은 값으로 추정하지 않는다.

## 공통 범위와 provenance

두 그림은 synthetic conditional arithmetic controls이며 actual HD reactive array/named physical consumer 결속을 제공하지 않는다. Source polynomial 또는 저장된 cubic의 binary64 표시는 눈으로 읽기 위한 근사이고 exact rational 인증은 원 JSON에 남는다. Plotter는 production/reference/old scientific module을 import하지 않고 root·primitive·convolution·ODE를 다시 계산하지 않는다. Native9 physical plot과 R10 original readout은 읽거나 수정하지 않는다.

독립 reference의 PASS는 실행 전 고정한 Decimal160/1e-80 guard 아래의 수치 대조이며 물리 sample validation을 뜻하지 않는다. Unguarded Decimal containment는 원 reference 결과의 별도 항목으로 유지한다.

실제 입력 SHA-256, renderer source SHA, deterministic render ID, PNG/SVG/data SHA, warning 및 내부 renderer CPU는 새 manifest에 기록한다. 전체 OS process 자원은 root wrapper의 별도 기록을 따른다. 기존 출력이 있으면 덮어쓰지 않으며 실패 시 partial bytes와 failure record를 보존한다. 실제 PNG 두 장을 본 root의 시각 검토는 rendering 성공과 별도 단계다.
