# PHYS78 결합 모델 구현·검증·실행 기록

## 완료 범위와 현재 상태

`phys78_impl/source/coupled_model.py`는 준비된 비등방 collisionless 물질·복사 모멘트, 등방 이상기체 H/D/T/He3/He4/Li6/Li7 이온 네트워크, 3개 gray UV bin, 재결합 탈출 복사, 유한 광원 에너지 저장고를 같은 LRS Bianchi-I 배경에서 결합한다. 실제 baseline 한 이력이 z=20부터 z=2까지 완료되었고, 동일 바이트·동일 과학 identity를 pilot의 `P013`으로 편입했다. 편입은 ODE를 호출하지 않았다.

단독 원자 모듈의 고유 테스트 14개와 결합 방정식 고유 테스트 8개가 PASS다. 이 lane의 고유 테스트 합계는 **22개**이며, 앞선 5개·6개 부분 집합을 다시 더하지 않는다. 부모가 실행한 kinetic 테스트와 다른 agent의 runner/plot 테스트는 별도 집계한다.

실제 결합 적분 시도는 **3회 = 실패 2회 + 완료 1회**다. 완료 baseline을 재실행하지 않았다. NCP 실행과 benchmark는 이 lane에서 각각 0회다. `HH_R10=OFF`; production admission은 발급하지 않았다.

## 과학적 모델 경계

- 모든 21개 핵종·전하 상태 좌표와 전하 중성으로 유도한 전자를 보존한다. 실제 활성 원자 반응은 원전 표의 PI 13개 + RR 13개다. 동일 원소의 isotope는 같은 원자 전이 계수를 사용한다.
- 기본 n/T와 Li III/IV는 0이다. 60 eV 이하 광원에서 Li II/III의 상향 광이온화는 문턱보다 낮아 0이며, 이 기본 실행에서 고차 Li 상태는 끝까지 정확히 0이었다. 핵반응·베타 붕괴·분자 반응은 실제 RHS에 포함하지 않는다.
- 기체의 비등방 응력은 등방 유체 closure로 0이다. 별도로 보존되는 `pi_m`, `pi_r`는 collisionless warm matter와 free radiation의 signed stress다. 이것을 각 이온의 독립 kinetic 비등방 응력으로 해석하면 안 된다.
- 동일 정규직교 normal frame에서 signed stress를 먼저 합한 뒤 Frobenius norm을 취한다. Half-contraction 값은 Frobenius보다 sqrt(2) 작다.
- 광자 평균에너지 `U/N`가 실제 광단면적 및 흡수 에너지에 동일하게 쓰인다. 광원 주입은 포함된 유한 reservoir에서 차감되며, RR 결합에너지와 전자 포획 운동에너지는 탈출 복사에 더한다.
- CI, DR, CX, CE, free-free, Compton, 분자, 핵반응, 베타 붕괴 및 Thomson angular collision은 제외된 모델 채널이다. 완료 baseline의 온도가 후기에 24,036 K까지 올라갔으므로 CI의 물리적 중요성이 작다는 판정을 내리지 않는다.
- sampled instantaneous exchange identity는 소스·원자·gray 에너지 전달 방정식의 국소 대수 잔차다. 연속체 또는 전역 오차 certificate가 아니다. 기존 1231 collisionless 이력, 729 warm 이력, 63 control을 이 새 계산으로 재분류하지 않는다.

## 수치 구현과 실제 수정

| 단계 | 실제 관측 | 수정/결과 |
|---|---|---|
| 첫 시도 | z=10.323에서 비활성 neutron 좌표가 −5.89e−39/H였다. 초기 총량 0에서 유도한 허용 음수 bound가 정확히 0이어서 중단했다. | 비활성 isotope의 별도 절대 roundoff 허용량 1e−28/H를 명시했다. 물리 상태를 clip하거나 rate/state floor를 도입하지 않았다. |
| 두 번째 시도 | z≈6.57에서 BDF Newton trial이 약 1e48 크기의 비물리적 상태를 제안해 중단했다. 이 상태는 accepted trajectory가 아니다. | H≈1과 Li6≈1e−14의 좌표 크기 차이를 제거하는 고정 대각 선형 변환으로 BDF를 실행한다. physical RHS, 물리 atols 및 저장 상태는 정확히 대응한다. |
| 세 번째 시도 | 동일 물리 baseline이 z20→2까지 완료했다. 음수 stage와 domain-rejected stage는 모두 0회였다. | 성공 소스 바이트를 동결하고 `P013`으로 편입했다. 추가 적분은 하지 않았다. |

species solver 좌표는 각 isotope 초기 총량으로 나눈 분율이며, 정확히 부재한 isotope에는 수치 변환용 고정 1e−20/H scale을 쓴다. 이 값은 물리 밀도나 초기조건이 아니다. 절대 허용오차를 같은 scale로 나누므로 원래 physical component 오차 제어도 유지된다. 고정 좌표 변환은 반응 stoichiometry와 에너지 식을 바꾸지 않는다.

### BDF domain 처리의 정확한 한계

`solver_rhs`는 열거된 물리 domain 예외에만 nonfinite RHS를 반환한다. 설치된 SciPy BDF는 **Newton 반복 중**의 nonfinite RHS를 수렴 실패로 다룬다. 그러나 predictor 자체가 domain 밖이고 Jacobian 재계산이 필요하면 NaN Jacobian의 LU 검사가 먼저 실패할 수 있다. 따라서 모든 invalid stage가 자동 복구된다고 주장하지 않는다. `evaluate`와 저장 후 검사는 계속 엄격하며, 이 상황이 실제 sweep에서 발생하면 실패를 보존한 후 그 경로만 수정해야 한다.

이 문서의 설명은 동결된 Python docstring의 “reduces/retries” 문구를 좁게 해석하도록 정정한다. 성공 실행의 invalid-domain stage 수가 0이므로 성공 baseline은 이 복구 경로에 의존하지 않았다. byte identity와 재실행 금지를 보존하기 위해 실행 완료한 과학 소스의 주석만을 변경하지 않았다.

## 성공 baseline 증거

- 실행 identity: `ae604dcf96ddce8f9f970c7d2a4da22231a6bff4dc24d76b886dd602d870ca4b`.
- 실제 source snapshot과 manifest: `coupled_trials/20261021T152026_608503Z/`.
- NPZ SHA256: `9101008f160908c7cabde566e20183f3f1cda1a5829d89844cd5ee2425605ee5`.
- 결합 소스 SHA256: `1a7ad66d5d14aac906e1f5968730efa48902b811f5bdc2861ae255072c98b781`.
- 최대 isotope 상대 보존 오차: `2.5370208048771667e-15`.
- 최대 sampled 국소 에너지 교환 상대 잔차: `2.400999891848623e-16`.
- 최소 species abundance: 0; 최소 photon number: 1e−10/H.
- 광원 reservoir 최소값: 805.3431 eV/H.
- 기체 온도 범위: 275.9796–24036.205 K; 최종 `xe=1.1554368734`.
- 실제 solve wall time: 10.5454 s; 저장 전 postflight 포함 10.7061 s. 이는 한 실제 실행의 기록이며 성능 benchmark 또는 speedup 측정이 아니다.
- BDF 통계: nfev 2920, njev 84, nlu 294; Jacobian 평가를 포함한 RHS 호출 5970.
- 등방 control의 최대 수치 잔여값: Sigma_F≈3.99e−18, Pi_m_F≈2.53e−19, Pi_r_F≈1.38e−17. 이 값은 유한 quadrature roundoff 수준이다.

원본 trial은 유지되고 `phys78_impl/results/pilot/cases/<identity>.npz/.json`으로 편입되었다. `BASELINE_ADOPTION_RECEIPT.json`의 readback 상태는 COMPLETE다. 원본 source manifest와 현재 source manifest가 일치하며 편입의 새 ODE 호출 수는 0이다.

## 보존·게시·DAG 경계

세 시도의 입력, manifest, 실패/성공 receipt와 source snapshot이 로컬에 보존되어 있다. 첫 시도의 source snapshot은 두 번째 snapshot에서 단일 guard 수정을 역적용해 복원했으며, 실행 직전 캡처했던 5개 파일 SHA256 모두와 일치함을 별도 증명 파일에 기록했다. 이 사후 복원을 실행 전 snapshot이라고 표기하지 않는다.

원격 draft PR·Drive·외부 백업 및 전역 DAG 게시 상태는 부모 lane이 담당한다. 이 문서만으로 원격 게시 완료를 주장하지 않는다. 다음 실제 실행 의무는 정확히 동일한 `P013`을 건너뛰고 아직 실행되지 않은 pilot 30개를 가용 공유 자원 내에서 수행하는 것이다. 기존 완료 이력은 건너뛴다. 이후 저장 이력만으로 plot을 생성하며, 추가 accuracy/refinement 검증은 독립 질문과 별도 identity로 기록해야 한다.
