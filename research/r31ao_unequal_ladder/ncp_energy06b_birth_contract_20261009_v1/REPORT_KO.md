# WU088_HH ENERGY06B: birth-measure / paired-defect 경계 연구

## 판정

`SOURCE_BOUND_DISCRETE_BIRTH_ALGEBRA_VERIFIED__COUPLED_OWNER_PAIRED_ACCEPTANCE_OPEN`

2026-10-09 KST. NCP return의 `ENERGY06_SOURCE_MEASURE.json` 및 ON06G 두 원 source SHA를 결속한 **새로운 경량 수학·수치 연구**다. 원 연구 승인 범위 내 read-only 실행이고 새로운 H–H field/적분/BE nonlinear root/actual paired macro를 dispatch하지 않았다.

### 새로운 정확 결과

- 원 저장 source는 full에 `W` 한 번, two-half에 `W/2` 두 번을 서로 다른 endpoint에 주입한다. `W=0.000006250000000000000299510850149... photons/H`는 actual binary64 제품이다.
- 같은 physical constant source의 timestamp 차이에서 NCP의 정확 dyadic first time-moment `-1953.1250000000000935971406716... s photons/H`를 재계산했다.
- 보조 스칼라 상수-opacity BE 식에서 `Δ=(twohalf-full) = x(W-xP)/[4(1+x)(1+x/2)^2]`를 직접 유도·구현했다.
- 실제 원 저장 W를 사용하는 **synthetic** `x=1/4` 사례: `P=0`이면 `Δ=+2.46913580246913592079e-7 photons/H`, `P=W/x`이면 `Δ=0`, `P=2W/x`이면 `Δ=-2.46913580246913592079e-7 photons/H`다. 여기서 x=1/4는 임의 시험광학깊이이며 실제 HH opacity가 아니다.
- 또 다른 반례 `W=0,P>0,x>0`에서는 같은 0 birth measure를 사용해도 BE 분할오차로 `Δ<0`다.
- 따라서 "두 이산 birth measure가 같아야 full/two-half paired estimator를 정의할 수 있다"는 조건은 일반적으로 **필수조건이 아니다**. 정확한 gate는 같은 연속 source law 및 초기조건을 보존하면서, 서로 다른 이산 schedule이 만들어낸 defect를 비교하는 것이다. 단, **no-birth ENERGY05와 owner의 실제 birth-included source 비교를 허용한다는 뜻이 아니다**.

### 검증

- 소스 원 bytes pinned SHA `8322d796...` / `f47958a8...` 일치. 두 owner 함수의 순서, 동적 각도 가중치 시각, accepted-half 진단 항목을 문맥 검사했다.
- 원 NCP 반환 ZIP SHA `c0cb24b95a06471b427b310eedd929ff2e0a1650fdaf248122f55a5faf05b9f6`, 3,079,967 bytes, ZIP CRC 확인. 원 원자 셀 데이터를 다시 계산하지 않았다.
- 신규 단위시험 **15개 통과**, 정확 rational scalar 비교 18개, 독립 120자리 직접 비교 18개, exact 미분/접선 5개와 mpmath 5개가 일치했다. 최대 120자리 직접 비교 절댓값 차이는 `2.82546132942247331616039e-123` (입력 고정 같은 scalar식의 산술 대조).
- 첫 test-first stub 실행은 예상대로 `NotImplementedError` 13개로 종료했다. 이것은 missing behavior 확인용 scaffolding이고 **성공한 assert RED→GREEN을 13개 얻었다고 주장하지 않는다.** 같은 시험 명세를 구현한 후 15개 통과를 기록했다.
- 최신 독립 owner ref 스냅샷: HH NCP `d8aeaec783c143600e38cbb1b48d1fa5cdb3799e`, REI `40ea171d6be12275f9ee8b4f50f68b9dad59ed0a`, HE `54d99a3af01ac7eabb907be05c634bcc06570357`, CR `58295e59e1c1815832a26769b05a3b5fcb96b47b`. 서로 다른 owner의 PASS를 이 정리의 근거로 전용하지 않았다.

### 소스・주장의 한계

Toy scalar BE의 부호/차이식은 실제 다주파·128방향·기체/HH coupled map에 대한 판정이 아니다. `SOURCE=5e-15`, `BIRTH=13.7eV`, 온도/threshold/원자율/기하 규약 및 저장된 G checkpoint는 그대로다. `24/289`, `265 unbounded`, `epsilon_C/R=null`, B22 OPEN, canonical S0 OFF, production HOLD를 유지한다.

### 다음 실행

`LOCAL_CODEX_HANDOFF_KO.md`에서 full/two-half common-law/individual-discretization 구분과 동일 θ/λ tangent, 실제 owner source 생일·방향보존, 소모된 과거 scope·새 승인준비를 상세 정의했다. 이 항등식만으로 새 정확한 owner acceptance를 선언하지 않는다.
