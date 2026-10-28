# R6 독립 reference 1회 실행 결과

실행일: 2026-10-27 UTC. 작성 역할은 별도 수치 reference 기여자이며 최종 C9 독립 심사를 대신하지 않는다.

## 실행 결과

**NUMERICAL_CROSSCHECKS_COMPLETED, 109개 검사, 불일치 0개, exit 0.**

실제 명령:

```bash
python verification/reference_r6.py --input verification/REFERENCE_INPUT.json --output raw/INDEPENDENT_RESULTS.json
```

작업 디렉터리: `/workspace/scratch/16df962c9b4e/wu_resume_20261027/r6_worktree/research/provider_registry_molecular_r6_20261027`.

시작 `2026-10-27T12:24:13.053044+00:00`, 종료 `2026-10-27T12:24:13.816377+00:00`.

| 시간 항목 | 실제 기록 |
|---|---:|
| 실행 구간 CPU | 0.689574078 s |
| 전체 process CPU | 0.822867308 s |
| 스크립트 내부 wall | 0.763363920 s |
| exec tool wall | 1.023403557 s |
| 승인 CPU 상한 | 60 s |

승인된 새 R6 reference allowance 1회를 사용했으며 재실행은 0회다. PHYS91 및 옛 scope 실행은 0회다. 생산 코어를 import하지 않았다. 결과 파일은 create-only로 만들었고 첫 결과를 그대로 보존했다.

## 고정한 산출물

- Script SHA-256: `11650b677ebbd96f9bab9463d8b14d102185e233f402a26d8170fe3d6c1596a8`
- Reference input SHA-256: `de0c817c082f158bf6219e1e66a2a281204d8af324b8e5e1e083361a4860440c`
- Primary result SHA-256: `1a3b55f7c14a64a10a651de2df7b7f7d2df24d0b9e809b729f32d73377c90e84`
- Independent result SHA-256: `7e7bbae7ae5285230c14ef8fbb258ef15a92635eebfb0e0ca04df6933859c5ba`

원시 결과는 위 작업 디렉터리의 `raw/INDEPENDENT_RESULTS.json`이다. 별도 `REFERENCE_RUN_RECEIPT.json`에 명령, 절대경로, 해시, 버전, CPU와 scope를 기계 판독 가능하게 기록했다.

Python 3.12.14, Decimal 1.70/libmpdec 4.0.0의 250자리 ROUND_HALF_EVEN 계산, NumPy 2.3.5, SciPy 1.17.0을 사용했다. 고정밀 Decimal 지수함수 경로는 생산 코어의 교대 Taylor 및 dyadic 연산을 호출하지 않는다. 원천 LAMDA 파서도 별도로 작성했다.

## Native graph의 finite-block 수치

다음은 저장된 유리수 scalar를 표시용 소수로 변환한 값이다. 새로운 시간 스케일이나 계수를 탐색하지 않았다. 각 행은 이미 고정한 mu=lambda*H, polynomial 차수 N, 512-bit dyadic 하한에 해당한다.

| mu | N | H (무차원 tau) | beta 하한 | rho 상한 |
|---:|---:|---:|---:|---:|
| 8 | 64 | 0.9490433102022812 | 0.0006425056008177424 | 0.9993574943991823 |
| 32 | 128 | 3.7961732408091247 | 0.07600394043365614 | 0.9239960595663439 |
| 128 | 320 | 15.184692963236499 | 0.8347042690372266 | 0.16529573096277345 |
| 256 | 512 | 30.369385926472997 | 0.9916538785393707 | 0.008346121460629307 |

이는 제공된 HD para-H2 native 100 K 9상태 그래프의 결과이다. 무차원 시계는 tau = collider_density * (1e-11 cm^3/s) * proper_time이며 collider density는 미입력이므로 H를 물리적 초라고 표기하지 않는다.

각 H에서 별도로 계산한 SciPy 전파자의 Dobrushin 계수는 각각 0.9993574943991823, 0.9239960595663436, 0.1652957309627728, 0.008346121460628762였다. 마지막 값을 certificate의 0.008346121460629307과 비교하면 표시 정밀도에서 근접한 수축을 얻었다. 이것은 네 개 선택 블록 안의 관측이며 최적 블록 선택이나 일반적인 순간 gap의 발견을 뜻하지 않는다.

유효한 전파자 bound의 형태는 계속 rho^floor((t-s)/H)이다. 이를 -log(rho)/H의 prefactor 1 순간 수축률로 바꾸지 않는다.

## 비교의 엄밀성 수준

35개 고정밀 구간 비교 중 34개는 250자리 reference가 양 끝보다 충분히 안쪽에 있었다. 나머지 한 개는 ground-state z=0의 **정확한 [1,1] 구간**이다. 원시 값은 reference=1, lower=1, upper=1, strict margin=0이다. 일반 strict-interior 분류기가 이를 `NUMERICALLY_COMPATIBLE_BUT_NOT_RESOLVED_AT_250_DPS`로 표시했으나, 실제 뜻은 exp(0)=1인 정확한 경계 일치이다. 정밀도 부족으로 해석하면 안 된다. 코드와 원시 결과는 이 주석을 이유로 수정하거나 재실행하지 않았다.

생성자 구간, stochastic 전파자, semigroup powers의 SciPy 비교는 numerical corroboration이다. Source R_lower 대 exp(KH) 비교에서 가장 작은 표시 slack은 -2.7755575615628914e-15였으며 사용한 tolerance 2.2e-11 안에 있다. 이 미세한 음수는 엄밀한 lower bound 위반을 입증하는 수치가 아니다. 반대로 tolerance 안이라는 사실만으로 outward certificate를 증명할 수도 없다. 엄밀한 방향은 생산 코드의 exact rational/directed lower arithmetic와 별도 증명·심사에 의존한다.

Exact Fraction 경로는 beta의 pair overlap 재계산, rho 정합성, dyadic 성분 및 column-substochastic 조건을 직접 확인했다.

## 강제항 및 시간가변 controls

세 강제 fixture 각각 8블록, 33개 시간 표본에서 augmented linear exponential로 실제 x, X, Xbar, r를 계산했다. 블록 끝의 M/U/E와 whole-block 경계의 양 끝 및 내부 1/4, 1/2, 3/4 시점을 따로 비교했다.

| fixture | H | common killing kappa | 결과 |
|---|---:|---:|---|
| zero killing | 1/4 | 0 | 허용오차 초과 없음 |
| uniform killing | 1/4 | 2/5 | 허용오차 초과 없음 |
| noncommuting state-dependent killing | 1/2 | 1/5 | 허용오차 초과 없음 |

마지막 fixture에서 K와 reset generator의 commutator 1-norm은 약 0.6133333333333331이었다. 그러므로 교환 가능한 특수 경우만 검사한 것이 아니다. 전체 A로 구성한 certificate와 common-killing 분리의 전파자 오차는 4.440892098500626e-16이었다. 추가 형성항 총합 F와 F_upper 경계도 검사했다.

두 조각 3상태 switched fixture에서는 시간순 exp(A2*H2) exp(A1*H1)를 직접 계산했다. 공통 P_lower 조건은 원시 rational 생성자에 대해 확인했으며, R_lower와 시간순 전파자 사이의 최소 성분별 여유는 0.038973345032464315였다.

별도로 두 상태의 강제 해 닫힌 형식을 세 clock scaling과 kappa=0 또는 2/5에 적용한 6개 analytic controls도 일치했다. 이 fixture들은 수학적 controls이며 source에서 회수한 물리 파괴율이 아니다.

## 상태와 후속 조치

새 reference 실행 의무는 완료했다. 원시 파괴율 GL2022 배열, 실제 collider density, 명명된 physical consumer는 계속 미입력이다. Source-native graph certificate 및 조건부 forced-block 정리와 이들 물리 입력의 완성을 구분해야 한다. 최종 C9 독립 심사, root의 단계별 게시·백업 및 DAG 반영은 root가 처리한다. 추가 과학 재실행을 권하지 않는다.
