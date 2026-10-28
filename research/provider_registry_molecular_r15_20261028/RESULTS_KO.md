# R15 실제 결과와 해석

R15의 직접 증명, 운영 구현, 독립 기준 계산과 단일 CAS 검증을 수행했다. 이 단계의 판정은 **명시한 전제 아래의 수학·코드 결과**다. R8/C8 시점 DAG는 **29/46**이며 두 신규 노드의 채택은 다음 독립 C9 검토 후 결정한다.

## 1. 실제 검증

| 항목 | 관측 결과 | 근거 |
|---|---|---|
| 독립 정적 심사 | 24/24, 미해결 중대 사항0 | reviews/R6_STATIC_REVIEW.json |
| Primary | 302/302, 21models, 68거부 조건, 14depth rows | raw/PRIMARY_RESULTS.json |
| 독립 reference | 302/302 records, 21models, 실패0 | raw/REFERENCE_RESULTS.json |
| Reference 세부 | pure exact238, mixed exact/guarded21; guarded 비교784, 실패0 | verification/REFERENCE_ASSESSMENT.json |
| Wolfram | 72unique exact-zero residuals, 관측 경고0 | raw/CAS_RAW_RESPONSE.json |
| 동결 identity | 30파일 유지 | verification/FROZEN_FILES.json |
| 그림 | PNG2/SVG2, 실제 PNG2개 열람 PASS | figures/VISUAL_REVIEW.json |

Primary와 reference는 서로 다른 계산 경로를 사용한다. 운영 코드는 positive Simpson/Bernstein overlap을 구성하고 derivative sign variation으로 세분한다. Reference는 원래 source primitive J0..J3를 사용해 다섯 내부 유리수 값에서 power quartic을 구성하고, 별도 네 값에서 확인한다. 모든 셀에서 U-P의 비음수성을 squarefree 홀수 중복도 인수와 exact Sturm count로 판정한다. 903회의 비음수 판정, 771회의 원래 적분 질의, 48331회의 original overlap 평가가 저장됐다. 지정한 7개 모델 셀에서는 근 구조를 따로 확인했다.

## 2. 엄격한 Decimal 포함과 고정 guard

Decimal160 reference를 exact Fraction으로 바꾸어 원래 유리수 구간과 비교하면 strict 포함 실패가 **59건**이다. 총수를 보존했고 상세 예시50개를 남겼다. 고정 기준 1e-80*max(1,abs(reference),abs(lower),abs(upper))를 적용한 784개 비교는 모두 통과했다. 이 기준은 실행 전에 동결했으며 결과를 보고 바꾸지 않았다.

첫 보관 예시는 z=0의 W1이다. Production은 정확한 [1/5,1/5]를 반환했고, 독립 monomial-phi 조합은 유한 Decimal 연산으로 0.1999…9990을 반환했다. 해당 값은 exact singleton 구간 밖에 있으며 고정 guard 안에 있다. 이를 rigorous interval reference의 성공으로 바꾸지 않는다. Exact 유리수 항등식·Sturm 판정은 tolerance 없이 별도 통과했다. 과거 CAS warning 원인이 밝혀졌다는 주장도 하지 않는다.

## 3. 직접 증명의 내용

원래 source cell마다 비음수 Bernstein-B3 계수 네 개가 주어진다. 정확한 source/observation/age 격자에서 겹침 끝점 L,U와 중점 M은 affine이다. Cubic Simpson identity에 따라 I=(U-L)*(g(L)+4g(M)+g(U))/6이고, positive B1×B3 곱으로 비음수 B4를 얻는다. q^k 가중합과 원래 t0의 초기 기억을 더하여 각 셀의 quartic을 한 번 구성한다.

Quartic의 도함수 B3 계수는 4(B[i+1]-B[i])다. 인접 평균 삽입과 항 삭제가 zero-dropping sign variation을 늘리지 않는다는 직접 논증으로 Vleft+Vright<=Vparent를 얻는다. Shared midpoint가0인 경우와 반복근도 포함한다. 따라서 깊이마다 mixed nodes는 최대3, 깊이D에서 splits<=3D, visits<=6D+1이다. D=96이면 셀당288/577이다. 이 종료는 root separation을 요구하지 않는다.

Restricted derivative 계수로부터 coefficient-hull spread<=width*M_B를 얻는다. M_B=4max|B[i+1]-B[i]|일 때 exact supremum gap은 M_B*2^-96 이하이고, 원래 B4가 비음수이므로 4*Cmax*2^-96 이하이다. Dyadic128 변환은 폭을 최대2*2^-128만큼 더한다. 실제 끝점과 left-limit supremum은 별도로 저장한다.

Signed scalar 전달은 B4의 양의 exponential moments를 사용한다. Beta_i(n)=choose(4,i)*i!*(n+4-i)!/(n+5)!이며 양수 z에는 Taylor0..96과 첫 누락항97 이후의 기하급수 꼬리를 쓴다. |z|<=16에서 이후 비는16/98 이하이다. 음수 z는 exp(z)*W_(4-i)(-z)의 reflection으로 처리한다. Whole-E는 incoming upper와 같은 signed-d 상수 forcing majorant의 오른쪽 upper 중 큰 값으로 감싸고, 다음 셀에는 별도의 polynomial endpoint interval을 전달한다.

전체 증명과 단위·가정은 theory/PROOF_KO.md, 구현 대응은 design/IMPLEMENTATION_TRACE.json 및 design/REFERENCE_C5_FUNCTION_MAP.json에 있다. Classical Bernstein 도구와 subdivision variation은 R2에 원전·위치를 기록했고, 이번 finite-work/gap 연결은 직접 유도했다. 학술적 최초성이나 새로운 strong no-go를 주장하지 않는다.

## 4. 실제 수렴과 비용

21개 full model에서 기본 셀75개, 총 splits677, visits1429가 관측됐다. 셀당 최대는191splits/383visits다. 이 값은288/577의 증명된 상한 안에 있다.

| 고정 depth 진단 | D=96 exact gap | 증명된 gap bound | 실제 splits/visits |
|---|---:|---:|---:|
| 유리 임계점 | 0 | 약1.70920e-30 | 3/7 |
| 비유리 임계점 포함 | 약3.89386e-60 | 약2.49806e-30 | 191/383 |

위 소수는 저장된 exact rational의 표시용 변환이다. 실제 수용은 rational 비교로 이루어졌다. 유리 임계점 예에서는 D=4부터 exact gap0이었고, 비유리 임계점 예에서는 D=96에서도 양의 gap을 보존했다. 두 곡선과 작업량 그림은 저장된14개 진단 행만 읽어 만들었다. 이는 모든 입력에 대해 같은 수렴률이나 성능이 나온다는 주장으로 확장하지 않는다.

Primary CPU0.568891초, reference CPU약2.060271초, 합계약2.629162초다. 각 프로세스의 imports·입력 읽기·serialization이 포함된다. Renderer CPU약3.270585초는 별도 postprocessing이다. Python3.12.14/Linux에서 측정했으며 각 실제 OS 기록에 원래 수치를 보존했다. CAS CPU, 전체 과거 CPU와 전역 남은 예산은 알려져 있지 않다. Primary/reference/CAS/renderer 각각1회, 수정 재실행0회, ODE0회다. 최대 허용 domain 전체가 같은 CPU/memory 안에 끝난다는 보장은 하지 않는다.

## 5. 대표 exact 대조군

g_r(t)=t^3,q=1,t0=0,T=1,R0=E0=0,c=1,d=0,g_e=0이면 R(1)=1/4,E(1)=1/20이다. q=0,tau=1,R0=1의 대조군에서는 실제 R(1)=1/4, 왼쪽 극한 및 whole supremum=5/4,E(1)=21/20이다. 저장 그림이 이 구별을 보여 준다.

Canonical GLOBAL_MEMORY는 q=1/2,tau=1/2,T=5/4이며 R=2337/4096,E=12013/81920이다. R4의 별도 tau=1 예제와 매개변수를 혼용하지 않는다. Signed d=±16, zero/constant/affine/quadratic/cubic, nonaligned clocks, singleton, states13/source16/observation32/blocks8, simple/double/triple/endpoint/rootless/constant derivative를 검증에 포함했다.

## 6. 적용 범위와 다음 판단

입력은 **원래 B3 계수가 모두 비음수인 명시된 원뿔**이다. (u-1/2)^2는 함수가 비음수지만 B3=(1/4,-1/12,-1/12,1/4)이므로 이 원래 계수 조건을 만족하지 않는다. R14의 pointwise-nonnegative quadratic 전처리 결과는 별도 유효한 결과로 보존된다.

Full-A block certificate는 실제 evolution operator의 허용된 모든 start/history에 결속되어야 한다. Constant-w 인증을 switching history로 자동 확대하지 않는다. 제공된 source가 whole fine/coarse-domain forcing bound라는 전제도 유지된다. R/E lower는 이상 비교함수의 하한이며 실제 물리 오차의 하한이 아니다. q0 사례는 산술 경계 대조군이다.

실제 GL2022 HD reactive array 및 named physical consumer/state/density/clock는 이번 조사 범위에서 INPUT_PENDING이다. native v UNSPECIFIED, MISSING_NOT_ZERO, TIQM/SQM DISTINCT, HH_R10 OFF, production NOT_ISSUED, L4 false, central/physical delta0이다. C9에서는 이 실제 결과와 source/그림/수용 metadata의 변경분만 검토한 뒤 두 조건부 노드의 채택을 결정한다.
