# R9 구현과 실행 경로

공개 API는 `src/causal_resolvent.py:sweep`다. B,g,delta,initial과 저장된 kernel/coarse_factors, 동일 family/state/clock binding을 받는다. 기본 raw 모드에는 선행 whole-trajectory envelope가 필요 없다. 선택적 whole_caps/point_caps는 해당 R8 원본의 동일 닫힌 셀/정확한 시각에 결속한다.

정확한 Fraction 산술에서 D를 그대로 유지하고, 지정된 scalar만 128-bit dyadic 상방 반올림한다. 반환값은 powers, A/B, current raw/selected whole, forcing F/L, raw/selected endpoint를 모두 보존한다. float/bool, 범위 밖 입력, 잘못된 grid/family/cap와 D≤0을 거부한다. 실제 인증 부등식은 원천 전제이며 generic metadata 검사로 새 인증을 만들지 않는다.

primary는 SHA256으로 고정된 R8 raw 결과에서 4 HD 사례와 5 control을 읽고 raw/capped 각각 계산한다. 새 생성자, exponential 또는 ODE를 호출하지 않는다. 독립 reference는 생산 함수를 import하지 않고 Decimal100 직접 convolution 및 E-first Gaussian 소거를 수행한다. 실제 rounding site를 따라 epsilon=2^-128과 1/D를 전파한다.

S05는 세 Python 파일의 실제 AST 검사와 계약·증명·입력·CAS를 포함한 9개 파일의 bytes/SHA256 동결만 수행한다. S06과 S07은 동결 파일을 검증한 뒤 각각 단 한 번 실행한다. 실제 결과를 확인하기 전 runtime PASS로 표시하지 않는다.

생산 코드는 /root/r9_recovery_implementation, 독립 reference와 R6/C9 검토는 /root/r9_recovery_review가 작성했다. 통신 장애 후 root가 원문을 전달받아 게시한다. 독립 reference 21118 bytes의 SHA256은 3f4b38f79de2690dd470b67608c8275b6c1f5149af42247c6dc468e8b33e3dcb로 전송 전후 일치한다.
