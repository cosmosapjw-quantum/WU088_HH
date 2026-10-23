# PHYS83 continuation 독립 검증 — S1 전 판정

## 1. 판정과 집계 경계

**PASS_SCOPED: 71개 named case, 2,111개 assertion.** CE·population 검증 1,885개,
핵 thermal/fast scalar adapter 검증 171개, runner 모의 제어 검증 55개가 모두
통과했다. 이 문서는 실제 저장된 세 `RESULT.json`과 완료된 lease receipts를
집계한다. 집계 과정에서 커널 또는 reference를 다시 실행하지 않았다.

| 검증 단계 | 실제 저장 결과 | Named case | Assertion | 판정 |
|---|---|---:|---:|---|
| Matched CE와 frozen H I star | `ce_attempt_02/RESULT.json` | 53 | 1,885 | PASS_SCOPED |
| Nuclear thermal/fast scalar ownership | `nuclear_attempt_01/RESULT.json` | 5 | 171 | PASS_SCOPED |
| Runner admission/resume, mock only | `runner_mock_attempt_01/RESULT.json` | 13 | 55 | PASS_SCOPED |
| 합계 | 위 세 결과의 직접 합 | 71 | 2,111 | PASS_SCOPED |

Runner 55개는 case 내부 54개와 실제 입력 bytes 불변의 전역 assertion 1개다.
고의로 실패시킨 mock callback 1회는 실패 보존 제어의 성공 사례이며 과학 실패가
아니다. 예상하지 못한 수치 case 실패는 0이다.

**이 검토 단계의 실제 science grid callback은 0이다.** 계약의 rate 132,
steady 324, transient 732행 격자, cosmological ODE, benchmark는 실행하지 않았다.
완료 identity 재실행은 0이고 상속된 symbolic 7개와 printed-rounding reciprocity
902개도 재사용했으며 재실행하지 않았다. 이 문서는 후속 과학 실행의 결과나
게시·백업 완료 증거를 대신하지 않는다. `HH_R10=OFF`,
`Production admission=NOT_ISSUED`를 유지한다.

## 2. 검토 대상과 독립성

물리 기준은 PHYS82 최종 `ca9d53983459ea08f9992a8a24663e46b7180344`의
후손 PHYS83 S0 `09289300ec2e500806aa2cb82365f00329e41c8c`에서 상속한
source-native LS H I 1s/2s/2p 유한 문제다. 현재 `CONTRACT.json` revision 2의
과학 설계와 gates를 변경하지 않았다. Source/theory 재사용과 새 코드 검증을
분리한다.

| 대상 | 작성자 | 이번 독립 검토 |
|---|---|---|
| `source/matched_ce.py` | `/root/ce_sources` | `/root/current_delta`의 별도 적분·미분 reference |
| `source/frozen_star.py` | `/root` | `/root/current_delta`의 mp80 generator reference; `/root/nuclear_ownership`의 독립 정적 수학 검토 |
| `source/nuclear_ownership.py` | `/root/nuclear_ownership` | `/root/current_delta`의 Decimal80 별도 회계·미분 reference |
| `source/run_study.py` | `/root` | `/root/current_delta`의 source 검토와 격리된 mock 제어 |

CE 작성자의 source 검토를 자신의 구현에 대한 독립 numerical review로 집계하지
않았다. 독립성은 생산 코드와 다른 reference 알고리즘 및 다른 검토 담당자의
구현·검토에 있다. 별도 외부 기관의 심사로 표시하지 않는다.

| 검증한 생산 입력 | SHA256 |
|---|---|
| `CONTRACT.json` | `d9eb980df5236e2b2ca3da313813c3ca2b21562f90486f1173d0ea509bc4dcc5` |
| `source/matched_ce.py` | `475ee6f84c5e19945324859a9c4c5e229d8ab5e92e8658ad5b3da39472c1744e` |
| `source/frozen_star.py` | `78421356c6b985d845f452f42e6b03c8ea657171ad826df51b3a1dbcf454578f` |
| `source/nuclear_ownership.py` | `be0739a0cc63d4f53f06b450b300bce09aa41878cd4462c0753798d6639684d2` |
| `source/run_study.py` | `dee42bcd164fbdfdceedc72200df53e2e687bf5978caddd1f5a40c63bc360f85` |
| `source/vendor/ci_finite_c22d.py` | `859cdf616ffa165c9fb3c3372d2202f5449e4b9a74a289a725fe456e26eb55b2` |

입력·verifier·결과·lease의 상세 SHA 및 실제 counters는
`INDEPENDENT_VERIFICATION_AGGREGATE.json`에 묶었다. 세 결과는 wrapper가
종료 후 쓰는 lease hash를 실행 중 알 수 없으므로 해당 필드를 명시적으로
비워 두었다. 이 집계 receipt가 완료된 실제 lease bytes의 SHA를 연결한다.

## 3. CE rate와 derivative reference

원래 문제는 source-native gap `10.20435 eV`, degeneracy `(2,2,6)`,
유한 excess-energy support `[0,958.40145] eV`에 대한 W 선형 보간이다.
각 cell에서 `W(epsilon)=(epsilon+Delta)*sigma_up(epsilon+Delta)`를 쓴다.
Reverse source를 별도로 보간하지 않고 같은 W로 matched deexcitation을
정의한다. 검증 reference는 raw forward source를 독립적으로 읽고 Decimal로
source knot 차를 구성한 다음, 각 cell의 **다항식×지수 integrand를 직접
QUADPACK 적분**한다. 생산 `_moments`와 incomplete-gamma 식을 reference로
호출하지 않았다.

두 channel 각각 `T=[255,777,3500,12000,25370.66308424773,50000] K`를
검사했다. 12개 rate reference pair를 위해 실제 direct scalar cell quadrature
10,552회를 수행했다. 생산 rate의 직접 비교 호출은 12회, 독립 finite-difference
stencil용 호출은 48회, population 입력 준비용 호출은 4회다. 이들은 검증용
호출이며 science grid 실행 수에 합치지 않는다.

`M0`, `M1`, up/down rate, log detailed balance, 반응으로 선택된 incoming
energy와 exact T derivative를 비교했다. 적분 moment에서 얻는 미분 reference와
별도로 5점 log-rate finite difference를 사용했다. 온도 domain 내부에서는
centered, 양 끝에서는 one-sided stencil이다. `M1/M0`는 excess 평균이며
excitation incoming 평균에만 gap을 더한다. Thermal event debit은 incoming
energy 전체가 아니라 준위 gap이다.

| 검사량 | 관측 최대 오차 | 계약 gate 또는 검사 기준 |
|---|---:|---:|
| M0/M1 direct quadrature 상대오차 | 8.8818e-15 | 1e-10 |
| Up/down rate 상대오차 | 7.1054e-15 | 1e-10 |
| Log detailed balance 절대오차 | 2.8422e-14 | 2e-12 |
| Moment derivative scaled error | 8.8471e-15 | 1e-7 |
| 독립 finite-difference derivative scaled error | 1.8730e-10 | 1e-7 |
| dq scaled error | 8.8668e-15 | 1e-7 |

Raw source SHA, forward 452행/reverse 451행, finite endpoints와 W shape,
immutable 배열, 지원 온도 domain을 별도로 검사했다. 이는 raw print의
902개 reciprocity 검사를 다시 한 것이 아니다. Source interpolation의 실제
물리 오차나 빠진 tail의 confidence interval을 산출하지 않았다.

## 4. Frozen star population·사건·에너지 reference

생산 코드는 두 감쇠 고유값의 analytic solution과 안정화된 적분을 사용한다.
독립 reference는 mpmath 1.3.0, 80 decimal precision에서 full 3-state generator와
세 occupation integral을 묶은 **6×6 augmented matrix exponential**을 계산한다.
두 구현은 같은 float rate 입력을 사용한다. 이 입력의 source 적분 정확도는
앞 절에서 별도로 검증했다. Steady reference는 full generator balance와
normalization을 직접 선형 연립방정식으로 풀었다.

28개 transient reference는 `T=3500,25370.66308424773 K`에서 다음 조합을
각각 사용한다.

| ne [cm^-3] | t [s] |
|---:|---|
| 0 | 0, 1000 |
| 1 | 1e-20, 1e-8, 1000 |
| 1e8 | 1e-12, 0.1 |
| 1e12 | 1e-8, 0.1, 1000 |
| 1e18 | 1e-20, 1e-12, 0.1, 1000 |

같은 두 온도의 `ne=0,1e8,1e18`에서 steady reference 6개를 검사했다.
추가 helper reference 6개는 반복근 `slow=fast=1`의 `t=1e-20,3`과
`fast*t=1/2`, `gap/slow=1/4` 양쪽에 배치했다. 반복근은 mp80 smooth-kernel
적분/미분 극한으로 비교했다. 총 population 관련 reference는 28+6+6=40개다.
분기 경계의 구체적 위험은 정적 검토 후 **첫 수치 실행 전에**
`PRERUN_BOUNDARY_COVERAGE.json`에 반영했다. 이미 완료한 matrix를 반복하지
않았다. A=0, 임의 초기 population 같은 API 밖의 물리 모형은 검증했다고
주장하지 않는다.

| 검사량 | 관측 최대 오차 | Gate |
|---|---:|---:|
| Transient population 절대오차 | 1.1102e-16 | 2e-12 |
| Resolved population 상대오차 | 2.2204e-16 | 1e-8 |
| Occupation integral·gross event·energy 상대오차 | 7.5495e-15 | 1e-8 |
| Raw energy residual/gross energy scale | 1.8196e-16 | 2e-11 |
| Nuclei sum residual | 0 | 2e-13 |
| Steady population 절대오차 | 1.1102e-16 | 2e-12 |
| Steady reference 상대오차 | 2.2204e-16 | 1e-8 |
| Root helper H2/H3 상대오차 | 1.3323e-15 | 1e-8 |

Resolved relative 검사에는 `1e-280` floor를 명시적으로 사용했고 population의
절대 gate도 함께 검사했다. H2/H3 분기 양쪽의 값 차이는 최대 5.6436e-12였다.
이는 조금 다른 두 입력의 연속성 비교이며, 같은 입력에서의 reference 오차와
구별한다. Clipping이나 silent repair를 허용하지 않았다.

상태별 occupation에서 얻은 upward/downward/radiative gross counts를 독립적으로
비교했다. `thermal_change_eV=-(Uatom+Egamma)`라는 안정화된 구성식의 closure만
검사하지 않고, raw gross-event 열 변화와 보존 residual도 mp80 결과와 비교했다.
두 광자 사건은 photon number에서 2, pair total energy에서 Delta 한 번이다.
이미 검증한 step 결과로 잘못된 immediate prompt-cooling과 잘못된 two-photon
2Delta energy mutant를 구별했다. 이를 위해 transient를 다시 실행하지 않았다.

Native radiative owner와 detached owner 동시 활성화, 잘못된 species/level,
온도·밀도·시간 domain, q/log 불일치, NaN log, underflow flag 및 finite-source
scope 위반을 거부하는지도 검사했다. `ne=0`의 exact-to-coronal factor 1은
분모·분자 모두 0인 비율의 analytic continuous extension이다.

`FROZEN_STAR_STATIC_REVIEW_KO.md`의 별도 정적 검토는 작은 시간·가까운 근·분리된
근의 식과 near-root series remainder, signed coefficient, ground probability
bound를 확인했다. 해당 정적 검토는 수치 호출 0이며 위 numerical assertion에
중복 합산하지 않았다.

## 5. Nuclear thermal/fast ownership 검증

이 단계의 대상은 공급받은 scalar normal-frame event energy와 상대 weight를
소비하는 detached adapter다. 독립 reference는 Decimal precision 80에서 signed
energy 합, 같은 weight로의 평균, particle/energy transfer 합 및 thermal EOS의
미분을 직접 구성했다. 생산 adapter를 reference로 사용하지 않았다.

- 유효 synthetic event 9개에서 `Egamma+Kc-Kin-Q`와 capture ledger의 같은
  signed residual을 확인했다. 작은 residual을 0으로 덮지 않았다.
- Weighted mean 4개와 subnormal 사례 1개를 포함해 모든 에너지 성분에 같은
  positive event measure를 사용하는지 검사했다. 총 weight 0의 conditional
  mean은 `None`이다.
- Exclusive transfer composition 3개에서 fast-first capture, energy-only
  stopping, 남은 에너지·입자수의 단회 assimilation을 합치면 명시적으로 선택한
  prompt-thermal ledger와 일치하는지 검사했다. Thermal과 fast particle 수를
  에너지와 별도로 확인했다.
- Synthetic EOS 5개에서 `u=(3/2)*n*kB*T`를 number source 및 expansion과 함께
  미분한 식을 비교했다. MeV→erg 변환과 particle number 항의 누락을 검사했다.
- Conditional NR mean 4개에서 equal-T, zero-drift, T-independent sigma 가정하의
  COM+reaction-selected relative mean `kB*T*(3+alpha)`를 확인했다. sigma flag,
  alpha domain, frame mismatch, 비유한/음의 energy·weight 및 immutability를
  별도 거절 검사에 포함했다.

관측 최대 signed event/capture residual은 1.0408e-16 MeV, weighted energy
residual은 1.2837e-16 MeV, weighted mean 상대오차는 2.2204e-16이었다.
Transfer composition, stopping/assimilation residual, EOS 및 조건부 selected
mean 비교는 저장된 float 비교에서 0이었다.

이 결과는 COM→normal four-vector 구성, mass shell, 실제 finite-T event measure,
isotope stoichiometry, 실제 nuclear rates, stopping law 또는 fast tensor/transport
검증이 아니다. 기존 PHYS81 event callback과 새 nuclear rates/stopping callback은
각각 0이다. 그 provider 의무는 OPEN이다.

## 6. Runner 모의 검증과 재실행 차단

`independent_verify_runner.py`는 `verification/runner_mock_attempt_01/MOCK_ONLY_cases`
안에만 synthetic output과 claim을 만들었다. `calculate`는 in-memory forbidden
sentinel로 바꾸었고 production scientific module을 import하지 않았다.
실제 계약·code·source bytes는 실행 전후 동일했다.

13개 case는 새 mock completion 후 completed resume의 0 callback, payload 손상
거절, COMPLETE certificate 변경 거절, 빈/identity-only manifest 거절, 기존 output
비덮어쓰기, ADMITTED·FAILED_PRESERVED claim 자동 재시도 차단, create-only claim의
배타성, callback 실패의 partial/FAILED 보존, 유효 완료 output의 metadata-only
복구, runtime metadata identity 제외, 복사한 mock bytes의 resume,
identity/summary/accounting 바인딩, production call 0을 검사했다.

동시 중복 claim의 핵심 `open(...,'x')` 배타성은 두 번째 claim을 순차적으로
시도하는 제어로 검사했다. Multi-worker stress test를 했다고 주장하지 않는다.
성공 mock callback 1회, 의도한 실패 mock callback 1회, forbidden callback 0회,
실제 `calculate` 호출 0회다. Runtime 버전 제외 검사는 격리된 synthetic input
unit을 사용했으며 실제 입력을 고치지 않았다.

Mock payload의 선언된 `EXPECTED` budget은 완료 validator에 맞춘 **가짜 데이터의
스키마 검사값**이다. 그 안의 132/324/732를 실제 과학 실행 수로 집계하면 안 된다.
Completed/resume 검사의 bytes 보존은 로컬 mock fixture에 대한 결과이며 원격
최종 backup 전체 다운로드·CRC·payload/blob 복원 검증을 대신하지 않는다.

## 7. 보존된 실패와 실행 전 수정

최초 `ce_attempt_01`은 `import mpmath`에서 환경 의존성이 없어 중단됐다.
`ENVIRONMENT_FAILURE.json`, START, `lease_ce_01.json`의 stderr를 보존했다.
Production module import 0, numerical reference 0, science callback 0이며,
nuclear 검증도 시작하지 않았다. 이는 환경/prevalidation 실패 1건이고 과학
실패 또는 실패한 numerical case가 아니다.

부모가 mpmath 1.3.0을 별도 local dependency 경로에 설치했다. 공식 wheel SHA는
`a0b2b9fe80bbcd81a6647ff13108738cfb482d481d826cc0e02f5b35e5c88d2c`이며
`MPMATH_DEPENDENCY_RECOVERY.json`이 복구를 기록한다. Core code나 물리 계약을
이 의존성 문제로 수정하지 않았다. 이후 CE attempt 02, nuclear attempt 01,
runner mock attempt 01을 각각 한 번씩 순차 실행했다.

두 정적 guard 결함은 해당 runtime 검증 **전에** 보고하고 작성자가 수정했다.

| 발견 | 수정 및 보존 증거 | 영향 |
|---|---|---|
| Frozen RatePair의 실제 q와 stored log 일치·유한성 미검사 | `PREVALIDATION_GUARD_FINDING.json`, `prevalidation_frozen_star_v1.py`; q/log/underflow/domain/scope 검사를 추가 | 첫 CE 수치 실행 전 수정; 무효화된 결과 0 |
| Runner의 빈/불완전 COMPLETE manifest 허용 가능성 | `RUNNER_PREVALIDATION_FINDING.json`, `PREVALIDATION_RUNNER_FINDING.json`, `prevalidation_run_study_v1.py`; 정확한 7 payload, canonical identity, summary/counter/status 및 certificate SHA 결합 | 첫 mock 실행 전 수정; CE/nuclear kernel 무영향 |

세 성공 실행은 모두 `source/leased_call.py`를 거쳤다. 각 receipt는 worker 1,
thread 1, cooperative lease 0.5 GiB, 다른 process 종료 0, old science runner 호출
false, exit code 0을 기록한다. 실제 순서는 CE→nuclear→runner mock이다.
검증 완료 뒤 성공 matrix를 재실행하지 않았다. 로그의 경과 시간은 운영 기록이며
benchmark 결과가 아니다.

## 8. 후속 의무와 해석 한계

이번 판정은 선택한 유한 operator·고정 T/ne·ground-start local star 및 detached
scalar ownership의 구현 검증이다. 다음을 OPEN으로 유지한다.

- Source interpolation의 실제 오차, omitted high tail, finite-mass/isotope
  spectroscopic threshold, finite-splitting 2s↔2p mixing, higher levels, CI/RR,
  photoabsorption, stimulated emission, opacity/trapping, two-photon spectrum.
- He/Li CE와 `HE_LI_CX_STATE_AND_PHOTON_ENERGY`; Li instrument response,
  deconvolution, isotope/target-state 및 실제 physical uncertainty.
- Nuclear physical frame/event provider, finite-T event weights, isotope number
  stoichiometry, 실제 nuclear rates와 fast-product stopping 활성화.
- `RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT`, `D_PI_RR_MATCHED_SOURCE_MOMENTS`,
  `LI_HARD_UV_INNER_SHELL_SPECTRAL_CONTRACT`, `FULL_GEOMETRY_SPECTRAL_BACKREACTION`.
- Coupled thermal/charge/geometry/spectral history와 전체 tensor pipeline.

고밀도 행은 finite star의 formal quenching·closure 진단이며 완전한 고밀도 H I
모형이 아니다. 고정 T/ne의 결과를 coupled history 경계로 사용하지 않는다.
같은 trajectory 성분 분석을 species-off 인과 실험으로 부르지 않는다.
Sampled quadrature와 sampled energy residual은 continuum certificate가 아니다.

Non-tilted LRS Bianchi I, reacting gas pi=0, 별도 collisionless DM pi_m을 유지한다.
Matter/radiation signed tensor는 같은 normal orthonormal frame에서 성분을 먼저
합한 뒤 norm을 취해야 한다. Frobenius=sqrt(2)×half-contraction 관계를 유지한다.
현재 scalar 검증으로 전역 tensor 합산의 새 인증을 주장하지 않는다.

S1 gate에 사용할 수 있는 결론은 **기록된 source/code identity의 scoped 독립 검증
통과**다. 과학 실행·게시·단계별 upload ACK·최종 양쪽 backup 복원은 별도 장부로
계속 진행해야 한다.
