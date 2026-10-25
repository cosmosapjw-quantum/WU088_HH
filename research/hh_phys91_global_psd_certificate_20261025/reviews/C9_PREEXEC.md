# PHYS91 C9 독립 구현 검토 — 실행 전

**판정: PASS_PREEXEC_STATIC_IMPLEMENTATION. 현재 BLOCK_NOW 0, required repair 0.**

이 문서는 C9의 실행 전 부분이다. 실제 C6–C8 결과와 최종 scientific C9는 **PENDING_OUTCOMES**다. R6의 완료된 이론 증명을 재실행하지 않았으며, 현재 고정 CONTRACT/theory가 R6에서 검토한 원 SHA와 같음을 읽기로 확인했다. 다음 전이는 root의 S1 동결·게시와 원 lease 아래 승인된 primary1/reference1 실행이다.

## 검토의 독립성과 범위

검토자 /root/central_recovery는 frozen theory/contract 및 source 다섯 파일의 작성자가 아니다. PhysMath1.3.0의 C9, integrated finite-review 정책을 읽고 적용했다. 원 과학 계약의 workflow1.0.0과 물리·수치 기준은 바꾸지 않았다. 이것이 하나의 독립 pass이며, 실행 후 같은 pass에서 실제 raw outcomes와 figures를 확인한다. 별도 이론 재심이나 검토의 검토를 만들지 않는다.

읽은 변경 파일은 kernel.py, evidence.py, primary.py, leased_call.py, reference.py다. 정확한 SHA와 위치별 검토 근거는 C9_PREEXEC.json에 있다. Author AST PASS는 준비 증거로 읽었으며 독립 과학 실행으로 세지 않았다.

## 수학–구현 대응

Correlation scale S=diag(sqrt(U))에 대해 primal factor는 S를 곱하고, negative-mode dual factor는 S의 역수를 곱한다. Dual의 공통 양수 rescaling은 모든 entries에 동일하게 적용된 뒤 dyadic 정수로 저장된다. 후보 score는 float지만 admission은 항상 원 F/H 좌표의 exact 값만 사용한다.

Primal의 공통 정수 denominator에서 D_i=max(U_i-Gram_ii,0)를 만들며, 최종 C의 diagonal overshoot도 alpha에 포함한다. 모든11,781 upper entries를 검사한다. Reference는 정수 numerator 식을 import하지 않고 rational diagonal differences에서 padding을 다시 구성하며 선택된 alpha와 witness를 비교한다.

Dual은 **전체 Gram Y를 먼저 합한 뒤** abs(Y_ij)를 계산한다. Production은 offdiagonal에2를 곱하고 independent reference는 ordered i,j 전체 합을 사용한다. 따라서 factor 사이 entry cancellation을 잃는 별도 support 합이 들어가지 않는다. 네 차원 manufactured fixture의 trace/support와 분리 support 차이도 실제 검증 항목에 포함된다.

alpha<=1은 닫힌 셀의 inclusive 존재 기준, beta>1은 strict 배제 기준이다. beta=1은 배제가 아니다. beta가 inherited strict lower와 같거나 작으면 open endpoint를 유지한다. beta>alpha 또는 alpha<=inherited는 tolerance 없이 STOP_NO_ADMISSION으로 연결한다.

## 탐색·reference·resume 경계

탐색은 고정 두 반경, 각2048/전체4096 projections, q=2^48, 최대18 exact checkpoints에 묶인다. 모든 positive modes와 negative modes를 각각 후보에 사용하고 raw F의 eigensolve는 없다. Exact B1 인증을 얻으면 추가 탐색을 멈춘다. 유한 search의 성공이나 최적해 도달을 보장하지 않는다.

Reference는 kernel/primary를 import하지 않는 standard-library integer/Fraction 경로다. 선택된 primal과 dual의 전체 exact certificate를 재계산한다. 모든 checkpoint의 원문 SHA·scalar·index와 저장된 min/max 선택은 확인하지만 **선택되지 않은 모든 checkpoint factor를 다시 계산했다고 주장하지 않는다**. 이는 최종 endpoint의 독립 인증에 맞춘 검증 범위다.

Primary resume는 identity 및 complete manifest를 검증한 뒤 kernel·NumPy·SciPy import와 출력 생성 전에 반환한다. Reference resume는 primary dependency와 reference manifest를 확인한 뒤 Fraction checker 구성·출력 생성·쓰기 전에 반환한다. 실제 SKIP0-write 결과는 실행 후 확인할 항목이다.

## Lease·자원·결과 보존

기존 pinned lease 파일에서 필요한 API와 import 경계만 읽었다. 원 공유 directory, one worker/thread, CPU0/8, memory reserve1.5GiB+job0.5GiB, primary60CPU/90wall 및 reference30CPU/45wall이 코드와 계약에 일치한다. Peer lease가 있으면 WAIT하고, retry는 자동 수행하지 않는다. Timeout은 자신의 child에만 적용하고 자신의 lease만 해제한다.

Exact checkpoint는 원 factors를 포함해 early-stop·contradiction 검사 전에 create-only로 남는다. 오류는 failure receipt로 남고 COMPLETE manifest는 성공한 payload 게시 뒤에 생성된다. PNG/PDF는 같은 primary에서 이미 계산된 certificate/checkpoint 결과를 시각화한다. 실제 프로세스가 자원 한도와 출력 요구를 충족했는지는 아직 관측하지 않았다.

## 유지되는 과학적 의미

이 코드는 조건부 nearest-formatting box의 유한 PSD distance를 다룬다. Source covariance 채택, 실제 formatter guarantee, physical CI, named consumer ACK 또는 물리적 no-go를 발급하지 않는다. Parent PARTIAL_INPUT_DEPENDENCIES, HH_R10 OFF, production NOT_ISSUED를 유지한다.

**후속 확인은 한 번의 실제 primary/reference·metadata-only resume·figures의 관측 결과에 한정한다.** 현재 구현의 재작성이나 추가 과학 실행 요청은 없다. 검토자의 scientific imports, fixtures, eigensolve, Dykstra, source 계산, 기존 science 재실행, 외부 변경은 모두0이다.
