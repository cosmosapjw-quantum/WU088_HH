# PHYS87 독립 C9 실행 전 코드 검토

## 판정과 범위

**PASS_SCOPED_PREEXEC — 선택된 동결 실행을 막는 미해결 항목 0건.**

검토자는 fresh independent Astra `/root/independent_review_87`다. CONTRACT revision 2, S0의 현재 이론 원문, 독립 R6 유도와 실제 구현을 대조했다. 구현의 동결 manifest SHA256은 `8dea0e64e9b6b7f8f84b04fe1b6ab50f992a8ff81c3a01d80d9a78d47cfdbd58`다. Manifest가 참조하는 source/implementation 9개 및 계약·이론·원자료·전사표 4개의 실제 bytes/SHA를 모두 확인했다. 과학 source 4개와 독립 reference 1개는 AST만 읽었다. Candidate import, source 계산, guard 실행, 과학 실행, lease 취득, Wolfram 호출 및 기존 identity 재실행은 모두 0이다.

이 판정은 **S1 동결과 root가 정한 첫 실행 경로에 대한 정적 판정**이다. 실제 source positivity, 수치 오차, energy residual, FD comparison, resource 사용량, reference 비교, resume SKIP은 아직 실행 근거가 없으므로 PASS로 집계하지 않는다. S1 게시·단계별 ACK 이후 root가 실제 shared lease와 자원을 확인하고 실행해야 한다. Full C9 결과 판정은 저장된 raw를 읽은 다음 별도로 한다.

## 계약과 이론 identity

- CONTRACT revision 2: `464df6f83a7ac8bd64813dc9da3ca34f19398a2f970f3d69c706e3d089f6fd38`
- 현재 S0 이론: `36f6a9a08433bf59af9178e36a50d861380bd82a0ef9949e9bb67e0d3196a84d`
- R6 당시 이론: `abbcac3cdcf3679d941528460b109c1f4da51eb9180a7c6683b532c83392572b`
- Canonical ENDF: `3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af`
- SOURCE_TABLE: `b14ad9b4a2379166ec2b2c04b2a77efb4c819498924682072d74a6b4e31c5014`

R6 때 도구로 읽어 보관했던 이론 원문을 회수해 실제 SHA가 이전 값과 정확히 일치하는지 확인하고, 현재 S0 원문과 diff를 대조했다. 실제 차이는 두 곳이다. 첫째, 네 온도는 sample points이고 숫자 입력 guard는 FD satellites를 포함하는 255–101000000K이며 finite z≥1e5라는 설명을 추가했다. 둘째, 원전 절 제목 `原典・既存根拠`를 `원전과 기존 근거`로 고쳤다. 수식과 asymptotic expansion은 바뀌지 않았다. Historical R6 receipt는 보존하고, 이 검토는 현재 실제 SHA를 명시적으로 채택한다.

## 핵심 구현 검토

### 원자료와 보간

`NativeSource`는 bytes671232/SHA와 frozen table SHA를 먼저 검사한 뒤 MAT125의 MF3/102, MF6/102를 고정 폭으로 읽는다. ENDF exponent 표기, Decimal 전사, TAB1/TAB2/LIST의 cursor 이동, 54/315개 section record, ZA/AWR, QM/QI, LCT2, photon LAW2/LANG0/NL2, recoil LAW4, 두 yield1 branch와 전체 소모 여부를 확인한다. 153개 energy/sigma/a1/a2가 숫자와 원 literal 양쪽으로 table에 연결된다.

MF3의 NBT33은 zero-based lower cell index0..31까지 INT5이고 이후 INT2다. 코드의 `idx<32`가 이를 구현한다. MF6 angular coefficients는 모든 구간에서 lin-lin이다. 마지막 source endpoint는 마지막 유효 cell을 선택하며, 모든 exact represented knots는 literal 값을 직접 반환한다. Support 밖·NaN·Inf를 먼저 거부하므로 이를 clipping이나 zero extension으로 바꾸지 않는다.

Quadratic angular density의 계수는 `(15a2/4, 3a1/2, 1/2−5a2/4)`다. 양 끝점과 구간 안에 있는 convex vertex의 Fraction 값 중 최소를 검사한다. 연속 energy 구간의 coefficient interpolation은 양쪽 density의 convex combination이므로, 실제 모든 knot minima가 양수이면 표현된 법칙의 전체 cell positivity가 따른다. 그 실제 minima 계산은 primary가 수행한다. 이 정적 검토로 153개 수치 판정을 미리 선언하지 않는다.

### 물리식과 안정성

Mass/Q는 명시된 neutron scale, source AWR, QI에 고정되어 있다. Parent bare mass를 고치거나 recoil AWP로 residual mass를 재구성하지 않는다. Source convention guard는 bare consumer 요청을 거부한다.

`source_kinematics`는 작은 K를 `2 eps_H E/(W+M)`로 계산하고, `q=Q+K`, `kStar=q²/(2W)`, `eStar=q−kStar`, `EDStar=epsD+kStar`를 사용한다. 큰 rest energies의 차감으로 daughter kinetic energy를 만들지 않는다. Lambda의 factored expression과 log-energy Jacobian `eps_H*E/W`는 R6의 invariant rate 식과 일치한다. barn→cm² 변환은 한 번, 상대속도의 c prefactor도 한 번 적용된다. 두 reactants가 다르므로 추가 symmetry factor1/2는 없다.

`ScaledBesselSix`는 terms0..6의 coefficient를 Fraction으로 구성한다. `P2−P1`, `P1−P2`, `P1²+3t P2 P1−P2²`를 정확한 coefficient 단계에서 만든 후 Horner 평가한다. Variance numerator의 두 선행 coefficient가 0임을 확인하므로 큰 z에서 O(1) 두 값을 수치 차감하지 않는다. 이 방식은 지정된 finite z≥1e5 영역의 근사 구현이며 exact Bessel 함수라는 주장은 없다.

같은 양의 quadrature mass에서 normalizer와 Kin/photon/recoil 평균을 계산한다. 총 variance는 conditional variance와 conditional mean의 centered spread 합이고, 세 covariance도 within/between 조건부 분해와 일치한다. Photon의 conditional angular variance는 `eStar²*G/z`; recoil에도 같은 항이 들어가며 photon–recoil covariance에서는 부호가 반대다. Single-species thermal energy와 selected rate slope의 부호도 R6와 일치한다.

Owner h는 정수0/1, radiation route는 하나만 허용한다. Thermal/fast incidence는 h−2와1−h, free-electron incidence는0이다. Six energy columns와 caloric composition term은 같은 평균을 사용한다. `nuclear_rest`라는 기존 열 이름에 저장되는 −Q는 여기서 명시한 source-native effective mass 회계이며 bare-network의 수치로 재해석하면 안 된다. h=1은 instantaneous caloric birth이고 stopping 결과가 아니다.

### 실행 계획과 판정 경계

Primary driver는 네 온도×order16/32의 full integration8개, 두 온도의 FD satellites rate-only4개로 정확히12개 valid integration을 요청한다. 152개 native cell을 매 적분에 유지한다. Boltzmann underflow point와 wholly underflowed sampled cell은 수량을 별도로 남기고 exact tail-zero로 주장하지 않는다. Conditional angular case18개와 order32 owner row16개도 계약과 일치한다.

Acceptance는 동결 계약의 값에서 읽는다. Mean/owner/event closure, 16–32 비교, FD slope, 양의 variance 및 guard 결과는 실제 raw에 기록되도록 되어 있다. 높은 boost의 conditional checks와 thermal residual은 실제 각 값을 보아야 하며, 이번 정적 PASS는 수치 허용오차 충족을 미리 보장하지 않는다. Figure 코드는 saved RESULT만 읽고, native knots/네 온도를 잇는 선을 visual guides로 명시한다.

## Identity, resume와 shared resource 경계

Root가 정적으로 구성한 `implementation/PRIMARY_IDENTITY.json`의 descriptor와 실제 9개 dependency bytes를 대조했고, canonical JSON SHA가 `bc8a07546cab87dc79de5efee1e0d1917f7e88e851cdd8d5e7856f50f8c1c53d`임을 독립적으로 확인했다. 이는 실행할 primary의 입력·코드 binding이며 아직 완료된 과학 결과의 identity라는 뜻은 아니다.

선택된 command는 고정 `results/primary001`을 사용한다. 최초 디렉터리·ATTEMPT·결과 파일은 create-only이고 first failure를 보존한다. Primary binding은 계약, 현재 이론, canonical source/table 및 전체 source Python bytes를 포함한다. `--resume`은 complete status와 binding 및 manifest에 기록된 결과 bytes를 읽고 수치 module import 전에 SKIP으로 돌아간다. Runtime version은 해당 binding의 재실행 이유로 사용되지 않는다. Controller는 같은 identity를 다른 output path로 다시 시작하지 않는다.

Wrapper는 원래 full PHYS78 gate의 SHA `76ff57ba687fd9830b84c3fcff69eb8ed0e9f6ceab4551e61c67c84d3ea65124`를 확인하고 원래 resource/lease API만 호출한다. Historical scientific runner는 호출하지 않는다. 계약/gate identity, 허용 affinity의 CPU0/8, 기존 live leases, own acquire 이후 peer conflict, 실제 MemAvailable 및 cgroup memory를 순서대로 확인한다. Reserve1.5GiB+job0.5GiB를 유지하고 coordinator CPU8, child CPU0, 1 thread/worker를 적용한다. Hard CPU/wall은 primary12/60, reference20/60, figures8/30초다. 실제 사용량은 outer receipt에 기록한다. 자기 child의 timeout 처리 외에 peer process를 종료하거나 다른 lease를 해제하지 않는다. Gate failure는 child0 WAITING 근거이며 자동 retry 허가가 아니다.

이는 실제 launch 직전 observation에 대한 설계다. Shared cooperative protocol 자체를 전역적인 race-free scheduler라고 주장하지 않는다. 각 child의 실행 가능 여부는 root의 fresh gate 결과에 달려 있다.

## 발견 및 교정 — C9-P01

**발견자:** root controller. 독립 검토자가 동일한 call 순서와 repair를 직접 확인했다.

- **대상:** `source/leased_call.py`와 reference의 `--controller-admission-receipt` 연결.
- **이전 wrapper SHA:** `383c48a861d821946f750bed61d1d7bdd9044983773ae699dc4b16cdde815b34`.
- **근거:** Reference는 시작 시 existing admission JSON을 요구하지만 이전 wrapper의 final receipt는 child 종료 후 `finally`에서 생성됐다. 그 final path를 넘기면 reference가 필요한 파일을 읽지 못한다.
- **영향:** 첫 reference child가 science integration 이전에 실패할 수 있는 concrete dispatch incompatibility.
- **최소 교정:** 선택적 `--admission-receipt`를 추가해 own lease/no-peer/fresh-memory/실제 coordinator affinity 확인 후, child 시작 전에 별도 create-only JSON을 쓴다. Final receipt는 그 실제 bytes/SHA를 연결한다.
- **교정 wrapper SHA:** `d0825fe2349b29035fb8209e4c99cfa478b27d468fad70bffd6536bc83a7d7d1`.
- **연결 확인:** `EXECUTION_COMMANDS.json`의 wrapper admission path와 reference consumer path는 모두 `results/reference001_admission.json`이다. Final receipt path와 다르다. 아직 알려지지 않은 primary result SHA는 실제 완료 bytes에서 root가 치환해야 한다.
- **상태:** **CLOSED_VERIFIED_STATIC**. Physics/accuracy/budget 변경과 source 실행 없이 닫았다.

## 실행 후 남은 C9

Root의 한 번의 primary 뒤, actual RESULT·positivity witness·CSV·output manifest·lease/admission receipts와 counts/비용을 읽어야 한다. 독립 reference는 같은 lease 정책의 별도 한 child 안에서 T=1e8K의 실제 SciPy kve/adaptive quadrature를 사용하고, primary rate와 세 평균을 상대1e−7로 비교한다. Reference에는 source implementation import, 저온 variance 차감, 별도 mpmath 실행이 없다. 이어 actual read-only resume가 SKIP/scientific callback0인지 확인한다. 저장 결과 figure와 publication/backup verification은 각자 별도 ledger에 남긴다.

이론의 formal residual12개, source positivity proof 구조, sampled quadrature comparison, independent highest-T comparison을 서로 혼동하지 않는다. Source 밖 tails, physical covariance/confidence interval, atomic-to-bare remap, actual consumer/stopping/ODE 및 coupled thermal/charge history는 이 판정으로 닫히지 않는다. **HH_R10=OFF, Production admission NOT_ISSUED.**
