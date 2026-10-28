# R11 구성 선택과 자원 계약

## 선택한 경로

먼저 요청된 Duhamel 후보를 직접 증명한다. 이 경계는 perturbation이 크면1이 되어 strict block 정보를 잃는다. 동일한 fixed K/pi/d와 nonnegative w family에서 H+b_H I>=0이라는 구체적인 구조를 사용하면 U_A>=exp(-b_H∫w)exp(Ktau)가 나온다. 따라서 q_minor=1-exp(-epsilon)(1-q_K)는 q_K<1, finite epsilon 아래 strict하다. 이는 K-only rho를 full A에 그대로 대입하는 경로와 구별되는 실제 full-generator 증명이다.

q_minor<=q_K+epsilon(1-q_K)<=q_K+epsilon<=q_K+2epsilon이므로 exact arithmetic에서는 additive 후보보다 강하다. 생산 코드는 사용자가 요청한 후보를 따로 보존하고, 두 outward upper의 min을 선택한다. epsilon=0에서 exact 이론값은 q_K이며, 구현은 이 값을 덮는 dyadic upper로 기록한다. q=1도 valid nonexpansive case로 구현하고, q0은 supplied abstract kernel의 산술 control에서만 쓴다.

## 블록 기억과 forcing

tau/64 grid,3tau horizon이라는 저장 grid를 유지한다. R을 매 셀 다시 시작하면64개 subcells 동안 수축을 잃으므로 전체 source-age convolution을 보존한다. 새 forcing에 이미 경과한 initial age를 쓰지 않는다. h0=1을 첫 forcing 항으로 검증한다. 각 셀의 affine R envelope를 signed scalar E의 양의 Bernstein moments로 적분한다. 이 방식은 d_c=0과 nearzero에서 subtraction cancellation을 피하며 새 구조는 실제 함수·검사·저장 출력에 사용된다.

## 유한 실행 DAG

고정 입력·계약 → 명제/증명 → production 및 독립 reference 작성 → 독립 정적검토 → 전체 freeze → primary1회 → reference1회 및 CAS1회 → 저장출력 분석/그림 → final C9 → scoped science adoption → report/handoff와실제delivery 순서다. Primary/reference 각각CPU60s,wall90s, CASwall30s. 별도 wrapper가 OS user+system CPU와 wall을 측정한다. Import/serialization을 포함한다. 기존 모든 실행allowance는0 그대로이고 globalremaining/fullhistoricalCPU는null이다. Metadata/plotting은 저장출력만 읽고 과학 runner를 부르지 않는다.

## Strong no-go NG1–NG7 심사

새 불가능성 정리를 제안하지 않는다. NG1의 대상·전제·양화는 PREMISES_AND_MAP과 계약, NG2는 직접 증명, NG3은 analytic 및 native-conditioned models, NG4의 배제 메커니즘은 적용대상 없음, NG5는 sparseK finite mixing을 fullA forcing bound에 연결하는 실제 계산 전략, NG6는 Mitrophanov2005 Theorems2.1/3.1과Gaubert–Qu의 수축계수 원전 대조, NG7은 별도 reviewer의 R6/C9이다. Additive bound=1이나 특정raw regression을 impossibility로 부르지 않는다. 일반 Duhamel·Dobrushin·block convolution의 신규성을 주장하지 않는다.

## Watchdog

b_H는 실제 norm identity와 positive minorization에, h_n은 forcing-age convolution에, Bernstein weights는 signed-d stable integration에 사용된다. Input certificate metadata 검사는 source identity를 확인하며 물리 전제를 대신하지 않는다. 독립 review에서 발견된 cap float-cell type누락은 freeze 전에 최소 수정하고 실제 planned negative-control로 닫는다. 완료된 R10 리뷰·ODE를 다시 여는 절차는 추가하지 않는다.
