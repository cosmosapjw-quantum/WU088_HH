# R9 실제 결과와 수치 판정

## 실행된 범위와 판정
새 primary는 **150/150 PASS**, 독립 reference는 **438/438 PASS**, reference의 성분 비교는 **34590개, 불일치0**이다. 이는 34590개 독립 물리 시나리오라는 뜻이 아니다. 실제 source는 4 HD 사례×192 cells와 5 analytic controls×8 cells이며 raw/capped 두 모드다.

전체 child process CPU는 primary **1.162604 s**, reference **1.108081 s**, 합계 **2.270685 s**다. import와 serialization을 포함한다. 두 프로세스 모두 exit0, timeout false, 실제 실행 각각1회이며 상한은 각각60CPU/90wall이다. CAS CPU는 별도로 계측되지 않았다. 이전 과학 계산, 새 ODE, 새 generator 또는 source certificate 호출은0이다.

## 기존 R8 대비 최종 상계
아래 소수는 표시용 근삿값이다. 인증의 정확한 유리수 원문은 PRIMARY_RESULTS 및 RESULT_ANALYSIS에 있다. 감소율은 (R8−R9 capped)/R8×100으로 계산했으며 0/0은 정의하지 않는다.

| 사례 | R8 R | R9 capped R | R 감소율 | R8 E | R9 capped E | E 감소율 |
|---|---:|---:|---:|---:|---:|---:|
| 2-state, 무반응 | 0.061035156 | 0.061035156 | 0.000000% | 0.0000000 | 0.0000000 | — |
| 2-state, 비선형 | 0.067804487 | 0.067804399 | 0.0001297900% | 0.00051653394 | 0.00051650845 | 0.004935867% |
| 2-state, coarse source 차이 | 0.067805234 | 0.067805145 | 0.0001314250% | 0.00068522190 | 0.00068519601 | 0.003779431% |
| native9, 조건부 피드백 | 0.000036447643 | 0.000036447616 | 0.00007381191% | 6.1915408e-7 | 6.1912008e-7 | 0.005490601% |

native9의 최종 감소는 R 약 **0.00007381191%**, E 약 **0.005490601%**다. 저장된 R7 binary64 마지막 표본은 R=1.1721234642357073e-7, E=6.825711107438792e-10이고, 새 상계는 각각 약 **310.953728배 / 907.041143배**다. 작은 개선을 큰 물리적 정확도 향상으로 표현하지 않는다. R9의 주요 구성적 성과는 현재 셀을 양의 소거식으로 닫아 초기 전체 궤도 envelope 의존을 없앤 점이다.

## raw와 capped는 다른 보장을 제공한다
두 비선형 2-state 사례에서 각각 raw whole 성분1개(0-based cell63, R)와 endpoint 성분8개가 기존 R8 인증보다 크다. 따라서 raw의 보편적 no-worse를 가정하지 않은 이론 구분은 실제로 필요했다. 정확한 유리수 반례 값/indices는 RESULT_ANALYSIS에 보존했다.

capped에서는 4 HD 사례의 모든 whole1536성분과 endpoint1544성분이 기존 인증 이하이다. 이 중 whole1150성분 및 endpoint1136성분이 엄격히 작다. 동일 닫힌 셀·정확한 시각의 source-qualified cap 교차가 이 보장을 준다. raw/capped 모두 저장된193시각의 참조 표본과 양쪽 셀 경계 containment를 통과했다. 이 표본 대조 자체를 새 연속 궤도 인증으로 승격하지 않는다.

## 반올림, 조건수 및 검증의 범위
생산 계산은 exact Fraction 합·곱, 정확한 D, 지정 위치의 dyadic128 상방 반올림이다. 독립 Decimal100 계산은 E-first Gaussian 소거와 직접 convolution을 쓴다. 실제 지정 위치를 따라 epsilon=2^-128과1/D를 전파한 예산으로 비교했다.

모든 field에서 관찰된 생산−독립 값의 최대는 약2.859409286e-37이고 전파 예산의 전역 최대는5.642372884e-37이다. 각각의 비교는 해당 field/component 예산으로 판정했으며 전역 최대 하나로 판정한 것이 아니다. 최저 표시 차이−1e-99는 별도로 정한 Decimal100의 scale×1e-80 guard 안이다. phi는 같은 저장 유리수 upper를 입력으로 사용했으며 기존 R8 fixed1e-30 exact-phi 비교 실패를 재현하거나 지우지 않았다.

D는 네 HD 사례에서 약1,0.9999531241,0.9999531241,0.9999982917이다. 별도의 정확한 D=1/1000 control도 통과했다. 현재 forcing h0, signed-d 양/음 분기, 무반응·상수 forcing·nilpotent 해, source/grid/family 거부,8192-bit rational roundtrip을 검증했다. 이 작업은 고정 grid/128bits의 유효성·조건수·오차 예산 검증이다. 별도 mesh-refinement 수렴 차수나 hardware 속도 향상을 주장하지 않는다.

## CAS와 독립 검토
실제 새 Wolfram 호출1회에서 행렬/해 algebra 잔차7개와 exact control 잔차4개가 모두0이다. 양성 명제4개는1True+3unreduced로 반환됐다. 상태는 QUALIFIED_SYMBOLIC_CORROBORATION이다. D>0과 비음수 입력에서 1−δa=D+δbφc>0, R*≥0, E*≥0은 본문 직접 증명과 독립 R6 검토로 확립했다. CAS가3개 명제를 최종True로 축약했다고 기록하지 않는다.

독립 R6와 source-bound static preflight는 PASS_SCOPED다. 최종 C9는 실제 primary/reference/process/rounding 결과를 같은 한 번의 독립 검토 흐름에서 확인한다. 별도 과학 노드 채택은 최종 C9 기록에 결속한다.

## 과학적 해석과 다음 의무
이 결과는 동일 명목 generator family, state order, l1 residual, clock, uniform-all-starts kernel 및 source-qualified factor/cap을 전제로 한 조건부 비교 정리와 구현이다. HD의 E는 |eta|이며 전체 coarse l1은4E다. 실제 reactive array/consumer/density/clock의 입력 의무는 해결되지 않았다. HH_R10=OFF, production=NOT_ISSUED, L4_ready=false, physical/central delta0이다.

다음 의미 있는 연구는 실제 physical binding을 공급하거나, 남은 native9의 큰 보수성을 propagation/forcing geometry로 분해하는 별도 계산 가능한 의무를 선택하는 것이다. 이번의 작은 시간 셀 결합 보정이 큰 기존 보수성을 해결했다고 해석하지 않는다. 완료된 R9를 같은 입력으로 반복하지 않고 새 연구 계약에서 정확한 변경 의무를 정한다.
