# R11 연구 판단: uniform full-A 인증을 채택할 조건

## 실제로 해결한 의무

R10의 후속 후보였던 Duhamel 식은 고정 K/pi/destruction, 같은 전체 w box, 모든 시작시각, 같은 보존적 생성자라는 전제 아래 직접 증명됐다. nominal K의 rho를 full A에 그대로 옮기는 단계는 없다. positive minorization을 추가하여 q_K<1과 유한한 b_H M_w tau에서 full-A의 strict finite-block 수축을 얻었다. 유한 구현이 저장한 rational q<1인지도 별도로 반환한다.

forcing은 주입시각 u마다 age t-u를 갖는다. h(0)=1을 포함한 causal convolution, 블록 경계 왼쪽 극한을 포함한 닫힌 셀, signed scalar coupling의 양의 Bernstein moments, 같은 source/state/clock/cell의 R10 cap 결속까지 증명과 구현이 연결됐다. 새 ODE나 native matrix exponential 계산은 없다.

## 수치적으로 개선된 것과 유지된 것

Actual primary214/214, independent reference900/900,19195 components, failed0이다. 생산 dyadic128/Taylor96와 독립 Decimal160 및 실행 전 고정1e-80 guard를 사용했다. 이것은 정해진 유한 API와 고정 사례의 검증이며 전체 family 정리의 권위는 해석적 증명이다.

저장된 네 사례의 R11 capped endpoint는 R10 capped endpoint와 모든193×2성분에서 exact equality다. 최종 R/E 개선율은0%다. Raw endpoint는 무반응 사례192성분, 나머지 각384성분에서 R10보다 크다. 따라서 full-A block 유효성과 raw 성능 우위를 동일시하지 않는다.

반응 사례의 첫 whole R 한 성분이2^-128만큼 감소했고, 두2state 반응 사례의 일부 whole E 상한에는 작은 개선이 있다. 이 차이는 같은 닫힌 셀의 상한 교차와 scalar propagation에 한정된다. endpoint 개선이나 실제 물리 오차 개선으로 바꾸어 표현하지 않는다. 정확한 수치와 원소 수는 analysis/SAVED_OUTPUT_SUMMARY.json과 RESULTS_KO.md가 권위다.

## CAS와 sample의 판정

새 Wolfram call1회는15zero residual과 all_zero=True를 반환했지만 Power::infy3개와 General::messages 경고도 반환했다. 원인은 NOT_ESTABLISHED, 판정은 QUALIFIED_SYMBOLIC_CORROBORATION이다. 원래 frozen script에 전송 LF1개가 더해진 실제 제출문과 실제 응답을 별도로 보존했다. 경고를 숨기거나 재시도하지 않았다.

저장 sample3088성분은 기존 tolerance 안에서 통과했다. R11 Decimal160 비교의 최대 양의 초과4.0013321747316471235e-12는 고정 tolerance4.377656370786352e-11보다 작다. strict sample containment는 false다. R10의 원래 float 후처리 기록4.0013206434938575e-12는 변경하지 않는다. Raw lower는 선택한 rational-q ideal comparison의 lower다.

## 채택의 범위

독립 C9의 열린 중대 지적0을 확인한 후 새 이론·코드 노드 각1개를 조건부 채택한다. 기존36개 노드 객체는 그대로 보존하며 과학 DAG는21/38에서23/38로만 바뀐다. workflow20/20, 과학 DAG, provider receipt 수는 서로 다른 계수다.

Native9는 native K + synthetic conditional reaction fixture다. Actual HD reactive array와 named physical consumer/density/clock은 INPUT_PENDING이고 HH_R10=OFF, production=NOT_ISSUED, L4=false, central/physical delta0다. 이 단위는 실제 HD reactive closure를 제공하지 않는다. Native v=UNSPECIFIED, MISSING_NOT_ZERO, TIQM/SQM 구별을 유지한다.

Duhamel, Dobrushin, geometric-block convolution은 문헌에 있는 방법이다. 새 일반 정리의 우선권, sharpness, 보편적 raw 우위 또는 strong no-go를 주장하지 않는다. 채택 대상은 현재 source와 전체 family 전제에 결속한 구성적 full-A 인증 및 검증된 유한 계산이다.

## 종료와 다음 입력

R11 primary/reference/CAS는 각1회 소비했고 잔여0/0/0이다. 두 Python process의 import/serialization 포함 OS CPU는0.796703+0.680732=1.477435초다. old R10/R9/R8/R7/R6/PHYS91 allowance는 늘리지 않았고 global remaining/full historical CPU는 null이다. 실행이 끝난 이 단위를 통상 재개 절차로 반복하지 않는다.

실제 reactive array 또는 WU consumer가 도착하면 source family/state/clock/density/whole-domain binding을 먼저 수행한다. 추가 연구가 필요하면 비정렬 셀과 forcing 주입 breakpoint를 정확히 분할하는 별도 유한 계약을 먼저 작성한다. 이것은 R11에서 실행·채택한 결과가 아니다.
