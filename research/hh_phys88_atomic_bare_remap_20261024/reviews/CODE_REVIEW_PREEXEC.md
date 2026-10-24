# PHYS88 독립 코드 실행 전 검토

## 판정과 결속

**PASS_SCOPED_STATIC_READY_FOR_S1. 새 blocking code finding은 없고 열린 material finding은0개다.** 실제 파일을 직접 읽고 동결 계약 revision3·R6 유도·양의 branch 증명에 대조했다. 후보 import·수치 실행·시험·evaluator 호출은 모두0이다. 이 판정은 S1 게시 준비 상태이며 수치 검증 완료를 대신하지 않는다.

- 계약 SHA256: `8f45d6a70d7cf7ffcc556b74636f25087167a3372f781eee4078f5dd00e4154d`.
- Frozen manifest: 26개 파일의 실제 bytes/SHA 모두 일치. Manifest SHA `9d2c0a45b74dc1e328f537aefa08cb930a2903091db53ff4e26321f710e10873`.
- Canonical primary identity를 파일 hash·JSON으로 독립 재구성: `2712595494bd9d784539d470c4ad0b178314c1ca55d2b0b9a75cb5dc1e6a2774`. 저장 descriptor 및 실제 source 파일 집합과 일치.

## 물리와 source 구현

`MassConvention`은 표시 mass/Q/binding token을 Fraction으로 읽고 native h,D와 Delta/rho 및 exact residual을 구성한다. QS−Qb=BD−BH+rhoH−rhoD가 보존되고81.63eV 전체를 전자 결합, 규약 잔차만 또는 heat로 바꾸지 않는다.

`ConditionalMap`의 LAB 사상은 bare b,Mb, FIXED_COM_K는 native h,Ms로 안정화한 K를 만든다. Jacobian은 각각 bEs/Wb와 hEs/Ws다. Bare Eb 변환·역변환의 질량 선택이 맞고 원 단면적·angular coefficients는 늘 native Es에서 원 보간기를 호출한다. Sigma에는 추가 coordinate Jacobian이 없다. 원·사상 support 밖 및 비유한 값은 거부한다. Endpoint equality의 label 지정은 support 검사를 지난 정확히 같은 endpoint에만 적용되어 외부 입력 clipping이 아니다.

새 `BareThermalIntegrator`는 원152cells의 logEs에서 positive GL16/32를 사용하고 barn→cm²를 적용한다. Bare lambda, exp(−K/theta), scaled K1과 c/[4a²b²theta scaledK2a scaledK2b] normalization은 유도와 맞다. Underflow를 기록하며 음수·비유한 weight와 소실된 normalizer를 거부한다. 기존 native integrator 또는 positivity campaign을 호출하지 않는다.

평균은 안정화한 K+W(G−1), e*G, kd*+(d+kd*)(G−1)이고, variance/covariance는 conditional 항과 centered-between 항을 더한다. Photon angular variance e*²G/z가 photon/daughter variance에는 더해지고 두 출력 covariance에는 반대 부호로 들어간다. Score·un/up/ud 및 owner caloric 식도 계약과 일치한다. 큰 전체 second moment 두 개를 마지막에 빼는 구현은 없다.

`relabel_event`와 `bare_event`는 별개다. 전자는 native neutron/photon와 H/D four-velocity를 유지한 채 C=DeltaH UH−DeltaD UD, reservoir=−C를 직접 계산한다. 후자는 mapped Eb의 새 bare pair를 구성하고 두 출력을 COM→같은 normal z frame으로 boost하며 carrier를 더하지 않는다. 실제 fixture 범위는 계약의18source relabel·36bare 사건이며 일반방향 수치 검증을 주장하지 않는다. (−+++) shell과 네 성분 conservation scale은 revision3의 정의 그대로다.

소유권은 thermal h−2, fast1−h, electron0이며, −Qb rest-energy 열·단일 photon route를 포함한 여섯 에너지 열을 사용한다. Caloric 식은 −Kin+un+up+h(Kd−ud)다. h=1은 instantaneous birth 선택으로 기록되어 실제 stopping 완료를 뜻하지 않는다.

## 독립 reference의 판별력

Reference는 production 모듈을 import하지 않는다. 별도 Decimal/fixed-width parser가 원 MF3/MF6와 frame/양·보간 조건, table의612숫자 필드를 대조한다. Scalar 적분에서 angular coefficients를 다시 물리 입력으로 곱하지 않는다.

그 적분 좌표는 primary의 logEs와 다른 x=Es/theta이고, 독립 항등식

\[
\frac{\lambda_b}{4a^2b^2}=\frac{E_b(2a+E_b)}{a^2}
\]

및 dK/dEs를 사용한다. Bare Eb를 쓰는 이 식과 각각의 target/native_w derivative는 두 사상 모두에서 맞다. 최고 T에서 actual SciPy kve와 adaptive quad로 rate·세 평균을 사상별로 비교한다. 총8개 필드의 분모·허용오차가 사전에 고정되고, 실제 primary RESULT SHA와 한 개의 order32 행을 요구한다.

Reference는 각 source cell의 QUADPACK 진단·callback·오차 추정·부분 실패를 기록한다. 높은 T의 평균 비교 범위이며 low-T variance 독립 oracle, rigorous global quadrature certificate 또는 physical CI를 제공한다고 쓰지 않는다.

## 실행·resume·자원 경계

Primary는 fixed `primary001` create-only 경로에서16full+4FD 적분을 수행하도록 작성됐다. 새 fixture·owner 및 개별 acceptance/guard를 기록하고 실패를 보존한다. 저장 PHYS87 baseline과153knots/152cells positivity witness는 hash로 재사용한다. 이 witness를 새 scalar assertions나 새 positivity campaign으로 집계하지 않는다.

Resume 분기는 candidate/numpy import 전에 실행된다. 동결 input/code identity, 완료 status와6개 payload의 실제 bytes/SHA를 확인한 뒤 SKIP·callback0·rewrite0을 반환한다. Runtime 버전만으로 identity가 바뀌거나 새 output 경로로 자동 replay하는 경로는 없다.

Wrapper는 고정 PHYS78 gate에서 실제 own lease·peer 부재·fresh available memory와 CPU0/CPU8을 확인한다. 별도 admission receipt가 child 전에 생성되며 reference argv가 바로 그 파일을 받는다. Primary24CPU/60wall, reference30/60, figure8/30 및 thread/worker1을 유지한다. Raw stdout/stderr·비용·affinity·own lease release를 저장하고 자동 retry나 타 process 종료를 하지 않는다. 실제 자원 허가는 각 child의 미래 관측이며 이 정적 검토가 발급하지 않는다.

Renderer는 passed RESULT와 그 안의 저장 parent baseline만 읽어2PNG+2PDF를 만든다. Supplier/parser import 또는 integral 재계산이 없다. Map difference와 connecting line을 uncertainty/continuum으로 표시하지 않으며, 실제 그림 시각 검토는 생성 후 별도로 해야 한다.

Freeze script는 AST literal extraction·hash·JSON만으로 identity/commands를 준비한다. 이번 검토자는 그 script나 후보를 실행하지 않았다. Frozen commands는 reference의 실제 성공 RESULT SHA 하나만 runtime substitution으로 허용한다.

## 다음 단계와 claim gate

Root가 S1 게시·단계별 백업 ACK를 완료하고 각각 fresh gate를 확인한 뒤 별도 GO를 발급할 수 있다. 새 primary·independent reference·saved-only figures의 실제 raw와 resume 결과는 이후 C9가 검토해야 한다.

R6의 metric/acceptance 수정 및 실제 symbolic reporting 실패·복구 이력을 보존한다. CAS18scalarzero와 별도 양의 branch 증명을19CASzero로 바꾸지 않는다. 기존 비용과 새 symbolic2회 사용분을 유지하며 예산 reset은 없다.

실제 kernel/electron-state 동등성, covariance·tail·consumer·stopping은 OPEN이다. 원 remap·physical supplier 부모는 PARTIAL, HH_R10=OFF, production NOT_ISSUED다.

세부 검토 대상 function·판정 근거·실제 파일 bytes/SHA는 동반 `CODE_REVIEW_PREEXEC.json`에 결속했다. 신규 소스 수정·Git/provider mutation·과학 실행은0이다.
