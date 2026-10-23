# PHYS83 저장 과학 결과의 독립 readback 검토

## 1. 판정과 실행 경계

**READBACK_PASS_SCOPED.** Scientific identity
`e09e64848d545d844590c6cc733cc870109d8fa4f3b44bff796afd11c0753d0c`의
완료 인증서, 7개 결과 payload, 실행·재개 영수증, CSV 및 그림 provenance를
읽어 21개 readback 점검군을 통과했다. 검토자는 `/root/current_delta`다.

이번 검토는 Python 표준 라이브러리의 파일 읽기·SHA256·JSON/CSV와 저장된
숫자에 대한 Decimal80 산술만 사용했다. **Kernel import 0, rate callback 0,
population solve 0, 새 grid/ODE 0, 기존 numerical validation 반복 0**이다.
생산 source, results, plots를 수정하지 않았다. 기존 독립 numerical matrix
**2,111 assertions는 그대로**이며 이번 21개 readback 점검군을 그 수에 더하지
않는다.

`INDEPENDENT_REVIEW_KO.md`의 science callback 0은 S1 이전 독립 검증 단계의
기록이다. 그 이후 실행된 이번 과학 identity의 장부는 다음과 같다.

| 항목 | 검토한 저장 영수증의 값 |
|---|---:|
| 새 과학 요청 / 완료 / 실패 | 1 / 1 / 0 |
| Paired CE rate callback | 132 |
| Steady callback | 324 |
| Transient callback | 732 |
| 실제 resume 시도 / 완료 skip | 1 / 1 |
| Resume의 과학 callback | 0 |
| 새 cosmological ODE / benchmark | 0 / 0 |
| 기존 완료 identity 재실행 | 0 |
| Nuclear rates / fast-product stopping 활성화 | 0 / 0 |

자세한 exact CSV 문자열, 해시, 점검군 및 산술 결과는
`SAVED_RESULTS_REVIEW.json`에 보존했다. 아래 표는 읽기 쉽도록 표시 자릿수만
줄였다. Source나 결과를 반올림해 덮어쓰지 않았다.

## 2. Identity·완료 인증서·실제 재개

`COMPLETE.json`은 정확한 7개 필수 payload를 포함하며 실제 bytes·SHA256이
7/7 일치했다. 완료 인증서 자체의 SHA256은
`6a69c5552a9a311c14c55575ae1ee058d746fd377a23a21f7636ad3cc7854761`이고
`delivery/scientific_claims/<identity>.json`의 `completion_SHA256`과 일치한다.
SCIENCE_IDENTITY의 canonical payload hash를 별도로 계산해 scientific identity와
대조했고, payload에 고정된 12개 실제 입력의 현재 bytes도 일치했다.

COMPLETE의 execution, SCIENCE_SUMMARY, `science_first.json`의 execution이
완전히 동일하다. Identity의 expected callback budget도 132/324/732와 일치한다.
Journal은 SCIENCE_STARTED 1개, SCIENCE_COMPLETED 1개, 각 122행인 transient
profile 6개를 기록한다. CSV는 rate 132행·66온도·2 channel, steady
324행·4온도·81밀도, transient 732행·6 profile이며 각 parameter key가 중복되지
않는다.

실제 `science_resume_01.json`은 동일 identity의 `SKIP_COMPLETED_IDENTITY`,
검증 payload 7개, 과학 callback 0을 기록한다. 최초 실행과 resume의 lease는
각각 exit 0, worker/thread 1, 다른 process 종료 0이며 시간 구간도 겹치지 않는다.
Lease stdout과 개별 영수증도 일치한다. Runtime metadata는 identity 밖에 있으며
버전 차이만으로 재실행하는 설정은 꺼져 있다.

## 3. 저장 rate의 주요 수치

이전 PHYS82 계열의 `Tmax=25370.66308424773 K`를 이 문서에서는 **anchor**로
표시한다. 이번 rate grid의 온도 상한은 **50000 K**다. 두 값을 같은 의미의
Tmax로 사용하지 않는다. 단위는 rate가 cm³/s, incoming energy가 eV다.

| T [K] | Upper | q up | q down | Mean incoming up [eV] |
|---:|---|---:|---:|---:|
| 10000 | 2S | 8.512547824e-14 | 1.182566623e-8 | 11.17700533 |
| 10000 | 2P | 1.464348190e-13 | 6.780928304e-9 | 11.30900179 |
| 25370.66308424773 | 2S | 7.529257186e-11 | 8.013171083e-9 | 12.47791840 |
| 25370.66308424773 | 2P | 1.695888796e-10 | 6.016284971e-9 | 13.41711912 |
| 50000 | 2S | 5.446136446e-10 | 5.816232092e-9 | 14.63141832 |
| 50000 | 2P | 1.744669661e-9 | 6.210765969e-9 | 17.19076270 |

저장된 66온도에서는 두 excitation rate 모두 증가한다. 10000 K→anchor의
증가비는 저장 rate의 나눗셈으로 각각 884.4893, 1158.1185다. Deexcitation을
같이 단조 증가한다고 해석하면 안 된다. 2S down rate는 표시한 세 온도에서
감소하며, 2P down rate의 저장 grid 최솟값은 `29493.54811627896 K`의
`6.004320602946893e-9 cm³/s`다. 이는 유한 표본의 최솟값이며 연속 함수의
극소 온도를 새로 구한 결과가 아니다.

Incoming up mean은 사건으로 선택된 전자 입사 에너지다. 원자 excitation에
저장되거나 radiative event로 나가는 에너지는 source-native gap
`Delta=10.20435 eV`다. Incoming mean 전체를 사건당 cooling debit으로 쓰지 않는다.

## 4. Critical density와 coronal 비교의 범위

저장된 네 온도에서 다음 값을 얻었다. 같은 온도의 81밀도 행에서 ncrit 열은
일정하다.

| T [K] | ncrit 2S [cm^-3] | ncrit 2P [cm^-3] |
|---:|---:|---:|
| 5000 | 5.459740522e8 | 7.580597391e16 |
| 10000 | 6.958595257e8 | 9.231774352e16 |
| 25370.66308424773 | 1.026934582e9 | 1.040509223e17 |
| 50000 | 1.414833928e9 | 1.007927208e17 |

정의는 `ncrit_i=A_i/q_down_i`, 즉 해당 준위의 collisional deexcitation rate
`c_i=ne*q_down_i`와 spontaneous rate가 같아지는 밀도다. 2S의 A는 two-photon과
알려진 M1 branch를 합한 `8.229002496/s`, 2P는 E1의 `626000000/s`다.
두 channel의 ncrit 차이가 약 7.12e7–1.39e8배이므로 선택한 star에서 2S의
collisional quenching이 훨씬 낮은 밀도부터 나타난다.

이 값은 전체 H I의 실제 임계밀도 또는 exact coronal 방출이 절반이 되는
일반적인 밀도가 아니다. 이미 유도된 이 star의 관계는

\[
\frac{j_i}{j_i^{\rm cor}}
=\frac{1}{(1+n_e/n_{{\rm crit},i})(1+R)},
\qquad R=\sum_i\frac{a_i}{c_i+A_i}.
\]

따라서 ground depletion도 coronal 차이에 기여한다. `ne=ncrit_i`에서의 factor는
`1/[2(1+R)]`이며, R을 무시해야 1/2가 된다.

저장된 최댓밀도 `ne=1e18 cm^-3`에서 전체 exact radiation power를 전체 coronal
reference power로 나눈 값은 다음과 같다. 새 steady 평가 없이 두 저장 열을
나눈 것이다.

| T [K] | Total exact/coronal | Ground population |
|---:|---:|---:|
| 5000 | 0.04381045 | 0.9999999998036877 |
| 10000 | 0.05344471 | 0.9999730323816325 |
| 25370.66308424773 | 0.06306498 | 0.966250969949543 |
| 50000 | 0.05173463 | 0.7413853786685264 |

이 고밀도 값은 finite star subset의 formal diagnostic이다. Higher levels,
finite-splitting 2s–2p mixing, CI/RR, photo-processes 및 opacity 등을 생략한
실제 고밀도 수소 플라스마의 예측으로 확대하지 않는다. 전체 ratio와 개별
channel ratio도 구분해야 한다.

## 5. 정확히 저장된 t=1 s와 1000 s의 에너지

아래 12개 행은 CSV에 `time_s=1.0` 또는 `1000.0`으로 실제 존재한다.
가까운 시간 선택·보간·새 step 호출을 하지 않았다. 모든 에너지는 초기 H 원자
1개당 eV이며, `Qwithdraw=-thermal_change`이다. `Tanchor`는 위의 정확한
`25370.66308424773 K`다.

| T [K] | ne [cm^-3] | t [s] | Atomic storage | Escaped radiation | Heat withdrawal |
|---:|---:|---:|---:|---:|---:|
| 10000 | 1 | 1 | 1.0553143e-13 | 2.2573909e-12 | 2.3629223e-12 |
| 10000 | 1 | 1000 | 1.0555960e-13 | 2.3628168e-9 | 2.3629223e-9 |
| 10000 | 1e8 | 1 | 9.2288371e-6 | 2.1730820e-4 | 2.2653704e-4 |
| 10000 | 1e8 | 1000 | 9.2295918e-6 | 0.22536934 | 0.22537857 |
| 10000 | 1e12 | 1 | 7.3405430e-5 | 1.4948492 | 1.4949226 |
| 10000 | 1e12 | 1000 | 7.3405430e-5 | 1494.8492 | 1494.8493 |
| Tanchor | 1 | 1 | 9.3341421e-11 | 2.4055146e-9 | 2.4988560e-9 |
| Tanchor | 1 | 1000 | 9.3366332e-11 | 2.4987627e-6 | 2.4988560e-6 |
| Tanchor | 1e8 | 1 | 0.0085000369 | 0.23514202 | 0.24364206 |
| Tanchor | 1e8 | 1000 | 0.0085010470 | 242.85767 | 242.86617 |
| Tanchor | 1e12 | 1 | 0.094894762 | 1715.2175 | 1715.3124 |
| Tanchor | 1e12 | 1000 | 0.094894762 | 1715215.6 | 1715215.7 |

시간이 길어지면 population·atomic storage가 stationary 값에 가까워져도
반복 excitation/radiation 사건의 누적 수와 escaped energy는 계속 증가할 수
있다. `Tanchor, ne=1e12, t=1000 s`의 정확한 저장 heat withdrawal은
`1715215.6733392552 eV/H`다. 이 값은 T와 ne를 외부에서 고정한 bath의 누적
교환 장부다. 유한 thermal reservoir에서 가능한 총 방출량이나 실제 coupled
T/xe history의 경계로 해석하지 않는다. Gross 사건 수와 photon 수는 확률이
아니므로 H 하나당 1을 넘을 수 있다.

## 6. 저장된 부호·보존·two-photon 의미

732개 transient 행에서 thermal change는 0 이하이고 atomic storage, escaped
radiation, heat withdrawal 및 gross counts는 0 이상이다. 저장 diagnostic의
최대 `abs(normalized_raw_energy_residual)`은 `2.433784209198325e-16`, 최대
nuclei residual은 `1.1102230246251565e-16`, 최소 population은 0이다. 이 값들은
SCIENCE_SUMMARY와 일치한다.

별도로 저장 CSV 문자열에 Decimal80 산술을 적용했다. 이는 새로운 물리
reference 계산이 아니라 column 사이의 회계를 읽어 확인한 것이다.

| 저장 열 사이의 회계 | 최대 불일치 |
|---|---:|
| Heat withdrawal + thermal change, relative | 0 |
| Atomic + escaped = withdrawal, relative | 1.8736e-16 |
| Photon number = 2 C2gamma + CM1 + CE1, relative | 2.0602e-16 |
| Radiation energy = Delta (C2gamma + CM1 + CE1), relative | 2.7599e-16 |
| Atomic energy = Delta (p2s + p2p), relative | 2.3974e-16 |
| Raw gross-event energy closure / saved gross scale | 2.9690e-16 |
| Population sum from Decimal CSV strings, absolute | 1.4594e-16 |

Stored float diagnostic과 Decimal로 다시 합한 column discrepancy는 반올림 경로가
달라 값이 조금 다르다. 둘을 동일한 residual로 덮어쓰지 않았다. 모든 값은
sampled gross-energy scale에 대한 기록이며 continuum certificate나 net-cooling
상대오차 bound가 아니다.

예를 들어 `Tanchor, ne=1e8, t=1000 s`에는 two-photon event
`6.854662311038762`, M1 event `2.0791392791776342e-6`, E1 event
`16.944761380634418`이 저장돼 있다. Photon 수는 `30.65408808185122`, pair-total
energy를 한 번씩 합한 radiation은 `242.85767036439012 eV/H`다. Two-photon
계수 2는 number ledger에만 들어간다. 에너지에 2Delta를 쓰거나 각 광자를
Delta/2 단색선으로 취급하는 해석은 이 결과가 아니다.

## 7. 그림 provenance와 남는 OPEN

Plot receipt의 입력 CSV SHA 3개는 완료 payload와 같고 PNG 3개/PDF 3개의
실제 bytes·SHA 6/6이 일치한다. Plotter receipt는 kernel import, rate callback,
population solve, 새 science run, historical replay를 모두 0으로 기록한다.
이번 검토자는 그림을 시각적으로 검토하지 않았다. Visual audit는 부모가
별도로 수행하며 이 readback 판정에 포함하지 않는다.

Finite-source W-PL interpolation과 omitted tail에 대한 실제 physical uncertainty,
isotope/finite-mass correction, He/Li의 state·photon-energy 계약, 2s two-photon
spectrum 및 coupled radiation/thermal/charge/geometry는 OPEN이다. Nuclear
ownership의 scalar 구현 검증과 실제 nuclear rates·finite-T provider·fast stopping
활성화도 구분한다. 현재 결과는 후자를 완료하지 않았다.

`RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT`, `D_PI_RR_MATCHED_SOURCE_MOMENTS`,
`LI_HARD_UV_INNER_SHELL_SPECTRAL_CONTRACT`, `FULL_GEOMETRY_SPECTRAL_BACKREACTION`
의 후속 의무를 유지한다. Reacting gas pi=0와 별도 collisionless DM pi_m, 같은
normal orthonormal frame의 signed tensor 합산 후 norm, Frobenius와 half-contraction의
sqrt(2) 관계는 이 scalar 결과로 바뀌지 않는다.

검토한 결과·receipt에서 해당 scope를 벗어난 물리 완료 주장은 확인하지 못했다.
전체 H I의 임계밀도, physical confidence interval, finite-reservoir cooling bound,
continuum certificate로 재서술하는 것은 허용되지 않는다. 로컬 readback은
원격 최종 양쪽 backup의 전체 다운로드·복원 검증을 대신하지 않는다.

**HH_R10=OFF. Production admission=NOT_ISSUED.**
