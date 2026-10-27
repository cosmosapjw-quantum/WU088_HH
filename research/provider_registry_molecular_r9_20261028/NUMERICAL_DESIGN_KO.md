# R9 수치 설계

연속 Duhamel 비교를 시간 셀 supremum 부등식으로 이산화한다. 현재 셀의 결합은 정확한 양의 determinant D로 소거하며, 과거 항만 causal recurrence에 사용한다. raw 모드는 전체 궤도 초기 envelope가 필요 없다. capped 모드는 기존 R8 whole-cell/point 인증과 정확히 같은 cell/clock에서 min을 취한다.

입력: R8 primary SHA520110d1...의4HD×192cells,5controls×8cells에서 B,g,delta,initial,h,e_upper,phi_upper 및 선택caps를 직접 읽는다. 새 producer/지수평가/ODE는0이다. 정확한Fraction합·곱 뒤 지정scalar만dyadic128상방반올림한다. D는exactpositive로 유지한다. 단순유효상계의raw우열,반올림된벡터의discrete supersolution은전제로쓰지않는다.

독립reference는Decimal100 직접convolution과E-firstGaussian소거다. 2^-128을실제연산위치와1/D조건수에따라전파한오차예산을사용하고Decimal자체의scale×1e-80guard를분리한다. 동일저장phiupper를입력으로비교하므로R8의정확한phi대비고정1e-30closeness오류를반복하지않는다. R7저장193시각의binary64값은atol2e-12+rtol2e-10보조대조이며cap이아니다.

새primary와reference는각60CPU/90wall1회다. 완전processCPU는외부Actionswrapper가import·serialization까지계상한다. 출력create-only,requeststage/action고정,run_attempt1,sourcefreeze검증후실행한다. S05에서AST와9개실제sourcehash를고정하고S06/S07의변경의존성만검사한다. 첫실패는원본그대로보존하며구체진단없는재시도는없다.
