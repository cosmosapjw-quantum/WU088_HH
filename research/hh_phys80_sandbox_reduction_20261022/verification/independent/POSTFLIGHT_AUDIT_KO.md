# PHYS80 저장 실행 결과 독립 postflight 감사

## 판정

**PASS_SCOPED. 새 isolated ODE 3개가 모두 완료되었고 실패는 0개다. 동일 CLI 재진입은 세 identity를 모두 검증하여 건너뛰었으며 새 ODE 호출은 0개였다.**

case receipt, receipt checksum, NPZ, 원 solver 반환 배열, attempt별 STARTED/call marker/RETURNED/POSTFLIGHT, 최초 stdout 및 resume stdout을 서로 대조했다. 실행에 묶인 20개 source/input 파일의 바이트 수와 SHA256을 실제 파일과 확인했다. 핵심 reduced/bridge/runner 소스는 사전 독립 검토를 통과한 버전과 동일하다.

감사자는 ODE, RHS, Jacobian, source rate, equilibrium root 및 기존 test suite를 호출하지 않았다. 새 연산은 이미 저장된 상태의 유한 후처리와 ledger metadata 대조뿐이다. 그림 생성이나 시각 QA에 관여하지 않았다.

**HH_R10=OFF. Production admission NOT_ISSUED.**

## 실제 실행량

| 새 identity | 차원 | nfev = RHS callbacks | njev = Jacobian callbacks | nlu | accepted mesh points | 부모 궤적 최대 scaled-state 오차 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| C01_REDUCED_BASE | 4 | 463 | 2 | 22 | 66 | 3.585878342592928e-9 |
| C02_REDUCED_BASE | 1 | 933 | 1 | 58 | 134 | 8.882968114922326e-10 |
| C01_REDUCED_REFINED | 4 | 1422 | 2 | 26 | 203 | 4.0196554386103516e-11 |
| 합계 | — | 2818 | 5 | 106 | 403 | — |

mesh points는 각 실행의 초기점을 포함한다. 실제 accepted step 수는 각각 65, 133, 202로 합계 **400**이다. dense sample은 실행당 161개, 총 483개다. accepted mesh와 dense sample은 일부 시점이 겹치므로 두 행 수를 더해 서로 다른 물리 시점 수라고 해석하지 않는다.

case별 scientific identity, source binding, solver 통계 및 acceptance check는 stdout, case receipt와 attempt 파일에서 일치했다. call marker는 정확히 3개이고 identity당 하나다. 실제 과학 attempt의 FAILED 파일은 없었다. 새 control 2개와 별도 refinement 1개이며, 기존 PHYS79 control을 다시 실행한 것이 아니다.

총 실행 시간은 성능 benchmark로 판단하지 않았다. nfev와 nlu는 이 수치 설정의 실행 기록이며 다른 host나 다른 solver의 속도 보장을 뜻하지 않는다.

## 저장 배열의 독립 유한 후처리

`postflight_readonly.py`는 생산 model과 runner를 import하지 않는다. 저장된 species 순서를 고정 명세와 대조한 뒤 isotope별 합, charge, 입자수, 온도와 total energy를 `math.fsum`을 이용하여 새로 계산했다. 원 solver의 accepted theta/z와 최종 NPZ의 theta/z가 정확히 같고, 첫 저장 상태가 physics binding의 초기 y/u와 정확히 같은 것도 확인했다.

### 모든 accepted endpoint

| identity | isotope 상대 최대 | absent isotope 절대 최대 | total energy 상대 최대 | 최소 thermal u (eV/reference H) |
| --- | ---: | ---: | ---: | ---: |
| C01_REDUCED_BASE | 2.220446049250313e-16 | 0 | 0 | 3.766511299207479 |
| C02_REDUCED_BASE | 2.220446049250313e-16 | 0 | 1.2944659544520907e-16 | 0.06135012762997668 |
| C01_REDUCED_REFINED | 2.220446049250313e-16 | 0 | 1.6887248530737853e-16 | 3.76651129920748 |

403개 accepted endpoint 전체에서 species는 음수가 없고 thermal energy는 양수다. isotope gate 1e-10 및 total-energy gate 2e-10을 통과한다. 이 후처리는 사전 검토에서 별도로 남겨 두었던 accepted-mesh isotope 수치 보고 범위를 실제 저장 배열에 대해 닫는다. 생산 case receipt를 수정한 것은 아니다.

483개 dense sample도 같은 검사를 통과했다. 독립적인 합산 순서 및 정규화 식 때문에 roundoff 수준의 최대값은 생산 receipt의 값과 약간 다르며, 이는 gate 판정의 차이가 아니다. 독립적으로 복원한 T와 저장된 T의 최대 절대 차이는 C01에서 1.0913936421275139e-11 K, C02에서 5.684341886080802e-14 K였다.

C01의 온도는 약 24461.95–25370.66 K로 활성 neutral CI의 하한 1 eV/kB보다 높고 CX source domain 안에 있다. C02의 온도는 약 299.99979308–300 K로 CX source domain 안에 있으며 CI는 활성화되지 않는다. 모든 저장 mesh/dense 상태에서 이 domain 부등식을 확인했다. source rate 자체를 다시 평가하지 않았다.

### 부모 궤적·정련·C02 열 관계

부모 NPZ와 같은 161개 theta grid에서 상태 차이를 직접 계산했다. 위 표의 세 parent scaled-state error가 receipt의 수치와 정확히 일치하며 모두 1e-6 gate보다 작다.

C01 baseline과 refined의 최대 scaled-state 차이는 **3.5481474702780957e-9**로, 사전에 정한 1e-6 gate를 통과했다. 최초 invocation과 resume invocation의 refinement readout도 일치한다.

C02에서는 저장된 equilibrium oracle을 재사용했다. 최종 DII의 equilibrium 거리/D inventory는 **3.670510399273328e-9**, extent–temperature 관계의 절대 오차는 **5.684341886080802e-14 K**이다. 각각 1e-6 및 1e-9 K gate를 통과한다. 저장 equilibrium 상태의 balance를 대입하여 얻은 잔차는 1.6940658945086007e-21이다. 새로운 brentq 호출이나 equilibrium root 재계산은 하지 않았다. 유한 시간에 정확히 평형에 도달했다는 주장은 하지 않는다.

energy residual은 first-integral 좌표 구성의 일관성 검증이다. 독립 동역학 증거는 앞서 완료한 원 event operator 접선 비교와 이번 저장 부모 궤적 비교를 함께 사용해야 한다.

## strict guard와 실행 경로의 근거

세 execution binding은 `strict_nonnegative_trials=true`, `projection=NONE`, `Radau`, `analytic_jacobian=true`를 기록한다. 실제 실행 소스 해시는 사전 검토의 다음 해시와 동일하다.

```text
source/reduced.py
2029eac4b5e23e25158742ae79ba47bb9dcacaf95faba59237c7518195b201a9
source/phys79_bridge.py
53d01690dadf20d526e3e352cf01906538b45659dcadcc08210c8c0abc915262
source/run_reduced.py
396c59328ae3cec8f31b06fb9fa97de20b9717526ae8770950c73247ae3da320
```

이 고정 소스의 모든 RHS/Jacobian 진입은 raw 좌표와 lifted abundance의 음수, 비양의 thermal state 및 활성 source-domain 위반을 예외로 거부한다. clipping, projected trial 또는 signed-state extension을 적용하는 분기가 없다. guard 예외를 완화하거나 잡아서 계속 진행하는 코드도 없으므로, bound code와 성공 receipt의 결합은 실제 callback들이 이 guard 경로를 통과했다는 근거다. 이것은 모든 내부 trial 좌표를 별도로 저장한 로그를 읽었다는 뜻은 아니다. 실제 저장 accepted endpoint와 dense sample의 비음수성은 위 후처리로 직접 확인했다.

세 실행 모두 양수 admissible slot의 lease observation 및 서로 다른 lease key를 기록했다. 본 감사는 lease를 새로 취득하거나 다른 프로세스에 조작을 가하지 않았다.

## verified skip과 보존

최초 CLI 및 resume CLI는 모두 exit code 0이며 stderr는 비어 있었다. resume의 세 entry는 모두 `SKIP_COMPLETE_VERIFIED`, 각 entry의 `new_ODE_calls=0`, 합계 `new_ODE_calls=0`이다. source manifest, identity 집합과 refinement 결과는 최초 실행과 같다. durable invocation JSON과 각 stdout도 일치한다.

현재 case receipt/checksum/NPZ의 모든 바이트를 검증했고, attempt RESULT의 NPZ 해시와 final case NPZ 해시도 일치한다. 감사 시작과 끝의 case 파일 해시가 동일하다. 감사는 original case 파일을 수정하지 않았다.

## typed ledger 감사

검증한 `EXECUTION_LEDGER.json` snapshot의 SHA256은 다음과 같다.

```text
093e8217b91fbbe24e30f97ca75a8f9bd1fdadd2ea4d220eac6cd5e6051299c7
```

저장된 receipt와 정적으로 읽은 test method 목록에 대해 12개 metadata 대조 항목이 모두 통과했다. 이 12개는 새로운 numerical test suite 수가 아니다.

| ledger 범주 | 확인한 집계 | 해석 |
| --- | --- | --- |
| 새 isolated ODE | 3 calls / 3 complete / 0 failed | control 2개, distinct refinement 1개 |
| resume | verified skips 3 / new ODE 0 | 새 과학 실행에 더하지 않음 |
| 독립 reduction review | logical groups 16; 최초 15 PASS / 1 fixture FAIL | 최초 실패 receipt 원본 바이트 보존 |
| Jacobian 보완 | 미완료 영역 새 3점; 완료점 재실행 0 | 최종 완료 12점/39열; 별도 ODE 0 |
| generic Maxwellian | unittest method 6 / 실행 6 / 실패·error 0 | reduction의 16개 논리 그룹과 다른 단위 |
| generic Maxwellian 내부 점 | pure-A witnesses 9 / order profiles 18 / scalar quadrature sums 36 / E1 oracles 9 | witness·profile·observable 합을 독립 test 수로 더하지 않음 |
| Wolfram | context 1 / evaluator 3 / 성공 algebra 2 / 보존 syntax 실패 1 | transport의 `isError=false`만으로 실패를 성공 처리하지 않았음 |

Maxwellian receipt와 ATTEMPT_001 파일은 byte-identical하며 같은 한 번의 실행 기록이다. 두 파일을 두 번의 실행으로 세지 않았다. 해당 source 및 verification script의 SHA도 receipt와 일치한다. Wolfram의 보존 syntax failure에는 `$Failed`가 있고, 수정 후 receipt와 원 실패 receipt가 모두 남아 있다. 이 감사에서는 새로운 Wolfram 호출을 하지 않았다. 저장 Wolfram receipt의 존재와 typed count를 확인한 범위이며 전체 symbolic 유도에 대한 별도 재심사를 주장하지 않는다.

과거 PHYS78/79의 inherited historical 총계는 이번 감사에서 다시 검증하거나 실행하지 않았다. figure visual QA, Git publication과 backup delivery 상태도 별도 의무로 남긴다. ledger에 이 감사를 추가한다면 다음과 같이 구분할 수 있다.

- saved-result postprocessing audit: 1회, accepted rows 403, dense rows 483, ODE/RHS/Jacobian/rate/root 0.
- metadata ledger reconciliation: 1회, saved metadata 대조 12항목, 새 numerical kernel/기존 suite 실행 0.

## 명령·환경·증거 해시

다음 두 명령을 각각 한 번 실행했고 모두 exit code 0이었다.

```text
python -B /tmp/phys80_review/postflight_readonly.py
python -B /tmp/phys80_review/ledger_readonly.py
```

후처리 환경은 Python 3.12.14, NumPy 2.3.5이며 수치 thread 환경값은 모두 1이다. SciPy/ODE module을 import하지 않았다. 검사 대상의 실행 dependency는 기존 receipt의 Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0과 연결된다.

| 증거 | SHA256 |
| --- | --- |
| 실행 source manifest | `8e6952c96c0754c58f4fa73c2d782629c4bdff58f6ff098c3e7335d0c1af230f` |
| SCIENCE_STDOUT.json | `44c1bef716285512f8ba860fcf3e0c5f170c58f53777323493fc39917c4f3878` |
| RESUME_STDOUT.json | `32791e92cad13aa575bbe7e090bbc5557ee2bbce8a230d53d5b4af44e469add6` |
| postflight_readonly.py | `d9cfad9438b36507d61fe8ce207ccd8742d0075977e1e767eacb00c15c42e574` |
| postflight_audit_001.json | `868ec30c8ea5e9684d14d81c8e5ed722b8757e51e35c1665d6884f4606737c51` |
| ledger_readonly.py | `559d961fa1efb94e3346383defa9253d30ed4615ca1eab96215b61a018e43784` |
| ledger_audit_001.json | `0bf9bc39c964251c56bd9d404850a9a42a11541e1e0014a21942502d3416eef5` |

| 완료 case | receipt SHA256 | NPZ SHA256 |
| --- | --- | --- |
| C01_REDUCED_BASE | `0118cbe30c01087b6e15ac9c0f8bb0241d3f7708c383e63bdb020402a2f28b2f` | `c3fdbd080f378e7e80ff9da5b923d8b0874dc64f929415e32244a51f8f7822a0` |
| C02_REDUCED_BASE | `acbf4511962ff798a89eb0003e2cebfa6b24c08cc5fc475565c0babbe0c41324` | `7fa81242d082d1febbbc14e2187d9789766796077e139d6ce02f7a2a78f58960` |
| C01_REDUCED_REFINED | `3361538b09c2e597ca5c309518bb8570ecd5cf337c64543e3363a576d9282dab` | `cc1b631312568c17aecf10214c02743f845a7aa2a401e2297195c75dcf0a22b3` |

이 판정은 저장된 유한 endpoint/sample, 고정 부분계의 수치 일치와 실행 이력에 한정된다. 전체 dense interpolant 또는 시간 연속 구간의 인증, 저온 CI 정확도, He/Li state-resolved CX/radiative energy, full PI/RR adapter 및 cosmological production admission을 닫지 않는다.

**HH_R10=OFF. Production admission NOT_ISSUED.**
