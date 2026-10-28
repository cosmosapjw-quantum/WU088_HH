# R11 독립 reference 설계

작성자는 /root/independent_theory다. 생산 코드 작성자와 분리되어 있다. 이 문서는 실행 전 설계이며, 실행·PASS·CPU 측정의 영수증은 raw/REFERENCE_RESULTS.json 및 root의 완전한 process 측정 기록으로 판정한다.

## 독립 계산 경로

생산 모듈·이전 solver를 import하지 않는다. 표준 라이브러리의 Fraction과 Decimal만 사용한다. Native 생성자의 행렬지수와 기존 HD ODE를 다시 계산하지 않는다.

먼저 저장된 생산 결과의 **실제로 선택된 유리수 q**를 읽는다. 이 q의 정당성은 별도로 exact H·출구율·노름과 Decimal full-A additive/minorization 식에 대조한다. q를 반올림 전 이상적인 minorization 계수로 대체하면 생산 lower가 둘러싸는 비교해가 달라지므로, 이후 모든 kernel·forcing·R 계산은 선택된 q를 그대로 쓴다.

각 n에서 h_n=q**floor(n/m)을 exact rational power로 계산하고, 전체 forcing을 직접 유한 convolution 합으로 계산한다. 생산의 매 블록 dyadic recurrence 및 rounded 누적을 재사용하지 않는다. R의 endpoint, 셀 왼쪽 값, 오른쪽 left limit와 whole-cell 최대를 모두 exact Fraction으로 비교하며 numerical guard를 적용하지 않는다.

E에는 생산의 positive Taylor96 대신 다음 닫힌 식을 사용한다. x=d*delta에 대해

\[
\phi_1(x)=\frac{e^x-1}{x},\qquad
\phi_2(x)=\frac{e^x-1-x}{x^2},
\]
\[
W_0=\Delta(\phi_1-\phi_2),\qquad
W_1=\Delta\phi_2,\qquad
\phi=\Delta\phi_1.
\]

d=0 분기는 exact rational delta로 먼저 선택한다. Decimal 정밀도 160자리, 상대 guard 1e-80*max(1,abs(reference),abs(lower),abs(upper))를 실행 전에 고정했다. 약 |d|=1e-30의 control에서는 phi2의 뺄셈·나눗셈이 약 60여 자리를 잃을 수 있어 이 정밀도와 guard를 사용한다. 생산 tolerance를 결과에 맞추어 바꾸지 않는다.

닫힌 셀 E에는 그 셀의 Rwhole을 상수 forcing으로 넣은 signed scalar 해를 사용한다. d가 음수일 때도 왼쪽 값, scalar endpoint와 실제 affine-comparison endpoint의 최댓값을 계산한다. Capped 모드는 이 이상적 비교와 실제 R10 point/whole arrays의 단조 교차를 독립 arithmetic으로 구성한다. 이는 바깥쪽 upper 계산의 하한 기준이며 실제 물리 오차의 하한이 아니다. 각 새 cap이 실제 R10 cap보다 크지 않다는 명제는 별도로 exact rational 대조한다.

## 입력 identity와 기존 근거

실행 전 freeze에 core, 두 runner, 두 input, 계약 및 필요한 기존 source의 경로·크기·SHA가 포함되어야 한다. Reference는 실제 파일 bytes를 검사하고 primary의 core/input/runner/freeze SHA도 대조한다. R6의 실제 status PASS_SCOPED_EXACT_CERTIFICATES를 유지하며 PASS로 다시 표기하지 않는다.

두 상태 nominal K에는 exact 대칭 생성자·tau=1/4·rho=5/8을 확인한다. Native9에는 저장 R6 native_mu_256의 tau/rho/N512 identity와 저장된 K_lo <= K <= K_hi의 81성분 관계를 읽기 전용으로 확인한다. 이 확인은 기존 exponential certificate를 다시 실행하는 절차가 아니다. 모든 시작시각에 대한 사용은 고정 homogeneous K라는 현재 정리의 전제와 결합한다.

R7 저장 reference의 case ID는 HD: 접두사를 가진다는 기존 결과를 적용한다. 표본 clock은 원래 binary64 값과 exact grid 간 one-ULP 대응만 검사한다. 표본은 cap으로 쓰지 않는다. 표본 포함 검사는 고정 atol=2e-12, rtol=2e-10을 사용하고 다음 상태를 별도로 기록한다.

- 실제 sample-upper의 최대 양의 초과와 그 위치·sample·upper·tolerance.
- tolerance 적용 후 최대 양의 초과.
- strict containment의 실제 성립 여부와 strict 초과 성분 수.

따라서 tolerance PASS를 strict sample containment로 바꾸어 보고할 수 없다.

## 실행·출력 보존

Reference에는 1회 CPU60초·wall90초 계약이 적용된다. 내부에서는 serialization 여유를 두어 CPU58초·wall88초에 중단하며, 전체 OS CPU는 root의 외부 process 측정이 권위다. 기존 output이 있으면 덮어쓰지 않고 거부한다. 최초 exception이나 실패 검사, 실제 component 비교 수, exact/Decimal/sample 비교 구분을 원 결과에 보존한다.

이 설계는 R11의 새 유한 obligation에만 해당한다. R10 및 R9/R8/R7/R6/PHYS91 allowance, 이전 실패·CAS 경고·sample tolerance, 물리 consumer 및 native missingness 상태를 변경하지 않는다.
