# PHYS77 최적화·경량화·재사용 결정

2026-10-21. 이 문서는 실제 구현과 완료된 검토에 근거해 PHYS77의 계산 구조를 설명한다. 대상은 `FINITE_OWNER_WHOLE_CELL_SOURCE_OR_RESIDUAL_ENCLOSURE` 의무다. PHYS76에서 끝낸 1231개 long history와 z20→2 preliminary plot은 재사용한다. PHYS77은 그 그림을 다시 만드는 작업이 아니라, 저장 표본만으로는 알 수 없었던 **한 cell 전체의 finite-owner source bound**를 구성한다. 새 ODE 적분, 기존 ODE 재실행, benchmark 및 NCP 실행은 이번 결과에서 모두 0회다. [CONTRACT.json](CONTRACT.json), [LOCAL_CELL_SUMMARY.json](results/LOCAL_CELL_SUMMARY.json)

## 1. 실제로 채택한 계산 구조

| 대상 | 구현한 선택 | 유지하는 조건 |
|---|---|---|
| 원본 model 입력 | binary64 coefficient를 exact Decimal 문자열과 hash로 capture | 원본 packet, normalization, amplitude 및 전체 matrix |
| 반복 cell 평가 | owner 생성 시 상수와 packet별 invariant를 한 번 계산 | case마다 고정된 table identity |
| Einstein 식 | `H²/h0²`와 `gamma=href/h0`로 무차원화 | 같은 RHS와 source normalization |
| kinetic moments | 공통 exp, packet당 sqrt·inverse 재사용, 다섯 합의 fused reduction | 2592개 원래 packet rule |
| coefficient A | 양의 `rho-pbar` 형태와 captured monopole defect 보존 | `A=3+H'/H`의 정확한 실수화 |
| tube 구성 | affine predictor와 strict first-exit defect inclusion | node extrema를 solution bound로 가정하지 않음 |
| candidate 개선 | 포함되지 않은 component의 radius만 확대 | 매번 전체 coupled box를 다시 검사 |
| 여러 case | pending-only process jobs, job당 thread 1개 | 공유 lease와 CPU·memory 상한 |

실행 구현은 [export_owner.py](source/export_owner.py), [owner_interval.py](source/owner_interval.py), [cell_enclosure.py](source/cell_enclosure.py), [run_enclosures.py](source/run_enclosures.py)에 있다. 위 표는 구조적인 중복 연산 제거와 증명 가능성을 설명한다. 비교 benchmark를 하지 않았으므로 몇 배 가속되었다거나 64-core 효율이 측정되었다고 해석하지 않는다.

## 2. Self-contained coefficient table과 cache

Exporter는 source와 case identity를 확인한 원본 constructor 및 `set_amplitude`에서 coefficient를 읽는다. 이 단계는 원래 trajectory의 `initial`, `rhs`, `solve`를 실행하지 않는다. Canonical radial 좌표 72개, angular `mu²` 36개, 72×36 packet population, 5×5 Legendre matrix와 physical constants를 저장한다. 각 binary64 값을 `Decimal.from_float`의 정확한 표현으로 변환하고 JSON hash와 little-endian binary64 array hash를 함께 기록한다. 원본 file SHA와 case의 raw NPZ·receipt·amplitude binding도 별개로 남긴다. [ACTUAL_ONE_CASE_EXPORT_FIRST.json](verification/ACTUAL_ONE_CASE_EXPORT_FIRST.json), [FEASIBILITY_AND_EXPORT_KO.md](evidence/FEASIBILITY_AND_EXPORT_KO.md)

이렇게 준비한 request는 interval 검증 시 원래 constructor를 다시 실행하지 않고 읽을 수 있다. 원본 코드·입력과의 관계는 export receipt가 설명하고, 해당 table 자체는 이후 계산의 완결된 수학적 입력이 된다. Hash가 동일하면 어떤 계수로 계산했는지를 대조할 수 있지만, hash만으로 과거 다른 runtime에서 생성된 모든 내부 배열이 같았음을 증명하지는 않는다.

`FiniteOwner`는 한 table과 한 precision에 묶인다. `gamma`, `gamma²`, mass², reference dust/radiation coefficient, sqrt(2), sqrt(3), matrix row 및 packet별 `n/N`, `q²(1-mu²)`, `q²mu²`를 초기화 때 준비한다. 이 곱·나눗셈의 결과는 exact point라고 가장하지 않고 outward interval로 cache한다. 같은 owner의 다음 cell에서는 이 interval을 그대로 사용한다. State에 따라 변하는 H나 moments를 다른 coupled trajectory에 공유하지 않으며, amplitude가 다른 case를 같은 table로 취급하지 않는다.

이 cache는 임의의 x,b 값을 반올림하여 lookup하는 interpolation cache와 다르다. 원본의 고정 입력과 그 입력만으로 결정되는 연산을 재사용한다. Cell마다 반복되는 constructor·array conversion·상수 연산을 없애면서 새로운 근사 모델을 도입하지 않는 것이 목적이다. 실제 cache hit-rate나 성능 향상 수치는 이번 범위에서 측정하지 않았다.

## 3. 무차원 H²와 공통 coefficient

원본 proper-time shear는 `s=href*q`이며, state q는 deceleration parameter가 아니다. 구현은

\[
T={H^2\over h_0^2}=d+\mu\rho+rE_0+\Omega_\Lambda+\gamma^2q^2,
\quad \gamma={h_{\rm ref}\over h_0},\quad w={\gamma q\over\sqrt T}
\]

를 사용한다. `d=(1-fm)Omega_m/a³`, `r=Omega_r/a⁴`, `mu=mpref`다. 따라서 `tau'=gamma/sqrt(T)`, `b'=w`, `q'=-3q+3Q/(gamma sqrt(T))`를 계산한다. 매우 작은 SI H 값과 그 제곱을 모든 중간식에서 반복하는 대신, dimensionless positive denominator를 공통으로 사용한다. 최종 H는 `h0*sqrt(T)`로 되돌린다.

이는 같은 captured 상수를 사용하는 대수적 변형이다. 새로운 cosmology, clock, state 축약 또는 ODE method를 도입하지 않는다. Interval의 `T.lo>0` 확인은 모든 division과 square root의 regular domain을 확보하는 데도 사용한다. Independent point review는 무차원 fused 구현을 별도의 dimensional finite-sum 계산 및 120-digit reference와 대조했다. 이 검토는 old binary64 RHS와의 마지막 비트 차이를 source 변경으로 숨기거나 bitwise identity로 승격하지 않는다. [OWNER_CORE_INDEPENDENT_POINT_REVIEW.json](verification/OWNER_CORE_INDEPENDENT_POINT_REVIEW.json)

## 4. Shared exp와 fused 2592-packet moments

Massive moment에서 모든 packet은 `exp(-2x+2b)`, `exp(-2x-4b)`, `exp(-3x)`를 공유한다. 이 세 값을 packet loop 밖에서 계산한다. 전체 `evaluate`에는 dust와 radiation의 `exp(-3x)`, `exp(-4x)` 평가도 있으므로 현재 구현의 전체 호출 수를 “exp 세 번”이라고 쓰면 정확하지 않다. Dust volume exp를 moments와 합쳐 한 번 더 줄이는 변경은 이번에 채택하지 않았다.

Packet마다 transverse·parallel momentum square를 만들고, `sqrt(m²+u+v)`와 weight/energy를 재사용한다. 한 loop에서 rho, perpendicular pressure, parallel pressure, signed pi, `rho-pbar`의 다섯 accumulator를 갱신한다. 한 moment마다 전체 packet을 다시 순회하거나 모든 candidate를 큰 3차원 임시 tensor로 동시에 만들지 않는다. Persistent packet coefficient 저장공간은 packet 수에 비례하고, streaming 합산 중에는 소수의 interval만 추가로 필요하다.

원래 규칙은 24 radial cell×12 angular cell×3×3 subcell nodes, 총 2592 packets다. Nonzero packet을 pruning하거나 angular rule의 node 수를 줄이지 않았다. 정확히 population 0인 packet만 합에서 제외할 수 있으며, 이는 해당 유한합의 값이 0이라는 사실을 이용한다. 모든 나머지 합산은 outward rounding을 유지한다. 이 구조는 workload를 줄이려는 선택이지만 binary64 SIMD 수준의 throughput을 주장하는 근거는 아니다.

## 5. 양의 moment와 full-row A 식

Signed matter stress는 packet별 `(v-u/2)/(3 epsilon)`의 합으로 계산한다. `rho-pbar`는 두 큰 총합의 차 대신

\[
\rho-\bar p=\sum_k c_k{3m^2+2(u_k+v_k)\over3\epsilon_k}
\]

라는 양의 형태를 사용한다. 유한 packet 실수화 안에서 정확히 같은 식이며, interval dependency 때문에 불필요하게 넓어질 수 있는 subtraction을 줄이는 목적이다. 구현은 원래 pressure들도 함께 반환하여 독립적인 chain-rule 계산과 대조할 수 있게 했다.

`g0=(M E)_0`, `delta0=g0+2E2`라 두면 무차원 표현의 A는

\[
A={\frac32d+\frac32\mu(\rho-\bar p)+rE_0+3\Omega_\Lambda
+\frac12rw\delta_0\over T}.
\]

Captured matrix는 Gauss64와 binary64 연산으로 만든 실제 배열이므로 작은 첫-row 성분을 없애거나 분석적 `(0,-2,0,0,0)`으로 강제하지 않는다. `delta0`를 보존해야 같은 real lift의 `A=3+H'/H`다. Matter kinetic derivative와 shear work를 대입하여 얻는 cancellation은 exact-real algebra이고, 별도의 `A_chain_rule`은 그 식을 독립적인 형태로 확인한다. 이 유도와 Wolfram symbolic 결과는 [THEOREM_KO.md](theory/THEOREM_KO.md), [RESEARCH_EVIDENCE.json](evidence/RESEARCH_EVIDENCE.json)에 있다.

## 6. Directed interval core에서 NumPy fast path를 쓰지 않은 이유

이 core의 반환값은 단순한 고정 precision approximation이 아니라 실제 coefficient를 포함해야 하는 interval이다. Ordinary NumPy binary64 연산을 호출한 뒤 작은 epsilon을 붙이는 방식으로는 모든 elementary function·cancellation·sum의 포함성을 자동 보장할 수 없다. Fast-math의 연산 순서 변경이나 contraction 역시 현재 rounding proof와 다른 산술을 만들 수 있다. 따라서 해당 경로는 채택하지 않았다.

현재 implementation은 Python 표준 `decimal`의 C/mpdecimal 기반 arithmetic과 명시적인 local Context를 사용한다. 기존 PHYS76 directed endpoint 연산을 SHA로 고정해 재사용하고 square·sqrt 등 필요한 연산만 더했다. 정확히 반올림된 exp/sqrt의 결과는 인접 representable endpoint로 감싸며, exponent boundary에서 조용히 생기는 subnormal은 명시적으로 거부한다. 전체 process의 ambient Decimal precision을 바꾸지 않는다. [Python Decimal 공식 문서](https://docs.python.org/3/library/decimal.html), [INDEPENDENT_PORTABLE_FINAL_TESTS.json](verification/INDEPENDENT_PORTABLE_FINAL_TESTS.json)

새 Julia runtime, MPFR build, native interval extension 또는 GPU dependency를 설치하지 않았다. Exporter와 기존 owner에는 이미 존재하는 NumPy/SciPy가 사용되지만 인증 arithmetic은 별도다. 이는 NumPy 자체에 대한 일반적 판단이 아니라 현재 inclusion proof에 맞춘 구현 선택이다. 이미 vectorize된 원본 solver·diagnostics와 PHYS76 누적 attribution은 그대로 유지한다.

## 7. Selective radius inflation과 실제 수정

Saved nodes는 affine predictor를 고르는 데만 사용한다. 실제 acceptance는 `Einit+[0,h]D`가 후보 error box 내부에 strict하게 들어오는지로 결정한다. 첫 실제 mixed-case cell 검사는 선언한 8회 candidate 반복 안에 이 조건을 얻지 못했다. 모든 radius를 동시에 두 배로 키우면서 이미 포함된 q 등의 폭까지 커졌고, 그에 결합된 작은 higher-multipole component가 계속 확대되는 source를 따라가는 현상이 관찰됐다.

수정은 현재 포함되지 않은 component만 확대하고, 이미 포함된 component의 radius는 유지하는 것이다. 다음 반복에서 전체 coupled RHS와 모든 inclusion 조건을 다시 계산한다. 반복 수, precision 또는 acceptance tolerance를 완화하지 않았다. 수정 후 같은 input에서 4개의 candidate box 평가를 거쳐 strict inclusion이 성립했다. 최초 실패와 수정 후 결과는 각각 보존했다. [FIRST_CELL_FIRST_ATTEMPT.json](results/FIRST_CELL_FIRST_ATTEMPT.json), [FIRST_CELL_AFTER_RADIUS_FIX.json](results/FIRST_CELL_AFTER_RADIUS_FIX.json)

Independent regression은 `y1'=0, y2'=20 y1`의 닫힌 solution family를 사용한다. 이미 충분한 y1 enclosure를 계속 키우지 않으면 y2 enclosure가 닫히는 regular 문제다. 이 검산은 특정 implementation 줄을 따라 만든 검사가 아니라, first-exit inclusion이 풀어야 할 알려진 문제다. Candidate 선택의 실패와 물리 해의 부재를 구분하는 역할도 한다.

## 8. 독립 case 병렬화와 공유 자원

Case 사이에는 서로 다른 고정 input과 독립 IVP가 있으므로 process job으로 나눌 수 있다. 한 case 안의 cell은 이전 certified endpoint error를 운반해야 하므로 시간 순서를 유지한다. Runner는 identity가 확인된 pending request만 dispatch하고, 완료 receipt를 재사용하며, 기존 실패·부분 결과를 무조건 덮어쓰거나 자동 재시도하지 않는다. 같은 case에서 이미 계산한 table context는 이어지는 cell 평가에 재사용한다.

자원 계약의 상한은 64 CPU, 128 GiB RAM, reserve 16 GiB, job당 thread 1개다. Actual affinity, cgroup quota, available memory 및 기존 shared lease 상태를 보고 그 아래에서 슬롯을 정한다. 현재 job memory admission 값은 1 GiB다. 이 예약은 cooperative scheduling 계약이며 kernel이 RSS와 CPU를 강제로 격리해 주는 보장이 아니다. 다른 process를 signal하거나 종료하지 않고, 다른 Codex 세션이 있다는 이유만으로 전체 작업을 취소하지 않는다. [CONTRACT.json](CONTRACT.json), [run_enclosures.py](source/run_enclosures.py)

현재 로컬 preflight에서는 container capacity 8 GiB가 reserve 16 GiB보다 작아 admissible slot이 0으로 계산됐다. 이는 읽은 현장의 자원 결과이며 NCP의 실제 64-core 측정이 아니다. Pending 세 case request는 각 4-cell prefix로 준비되어 있으나 실행·인증되지 않았다. 원래 1231개 science trajectory의 미완료분을 뜻하지도 않는다. 향후 NCP에서는 그 현장의 fresh resource snapshot과 shared lease를 사용한다. [LOCAL_RUNNER_PREFLIGHT.json](verification/LOCAL_RUNNER_PREFLIGHT.json), [PENDING_INPUT_PREPARATION_RECEIPT.json](evidence/PENDING_INPUT_PREPARATION_RECEIPT.json)

## 9. 외부 문헌·코드의 실제 채택 범위

[TaylorModels.jl](https://github.com/JuliaIntervals/TaylorModels.jl/blob/9f3d2a669bfac0fba04d084744d9886bba06c452/src/valid_integ/validated_integ3.jl)의 polynomial+remainder Picard pass는 가까운 구현 참고다. Approximate polynomial을 만드는 단계와 interval self-map을 검사하는 단계를 나누고, polynomial arithmetic의 rounding difference도 range bound에 넣는 원리를 재사용했다. 현재 Python core에 Julia 코드를 복사하거나 번역하지 않았다. 확인한 commit은 `9f3d2a669bfac0fba04d084744d9886bba06c452`이며 실제 [LICENSE.md](https://github.com/JuliaIntervals/TaylorModels.jl/blob/9f3d2a669bfac0fba04d084744d9886bba06c452/LICENSE.md)는 MIT Expat이다. 검색 metadata의 `NOASSERTION`을 license 판정으로 사용하지 않았다.

[Nedialkov–Jackson–Pryce 논문](https://doi.org/10.1023/A:1014798618404)은 IVP의 존재·유일성과 whole-step enclosure를 검증하는 문헌적 맥락을 제공한다. Publisher abstract와 bibliography를 읽었으며 유료 본문을 읽었다고 주장하지 않는다. [Bréhard의 author-deposited manuscript](https://hal.science/hal-03161118)는 approximation과 rigorous a posteriori validation의 분리를 뒷받침한다. 그 논문의 linear Newton–Picard machinery 전체를 nonlinear owner에 적용한 것은 아니다.

[CAPD 공식 문서](http://capd.ii.uj.edu.pl/html/odes_rigorous.html)의 Taylor/Hermite–Obreshkov 및 doubleton/tripleton solver는 더 큰 범위의 재사용 후보다. Repository COPYING의 GPLv3를 확인했고, 이번 작은 Python kernel에 dependency나 vendored code로 도입하지 않았다. SciSpace와 Exa는 원문 탐색에 사용했다. 읽지 못한 문헌의 세부 정리, tool context 오류 및 symbolic warning도 삭제하지 않고 [RESEARCH_EVIDENCE.json](evidence/RESEARCH_EVIDENCE.json)에 남겼다.

## 10. 실제 한 cell이 말해 주는 것

성공한 case는 `mixed_s+0_m+1`이며, 명목 z=20에서 약 19.53435까지의 첫 cell이다. 정확한 coordinate와 Decimal bound는 [LOCAL_CELL_SUMMARY.json](results/LOCAL_CELL_SUMMARY.json)에 있다. 다음 짧은 표는 원문 interval을 바깥쪽으로 반올림한 보고용 값이다.

| 양 | Whole-cell 또는 endpoint enclosure |
|---|---|
| A | `[1.39910, 1.60104]` |
| signed matter Pm, half | `[3.29804e-4, 4.59977e-4]` |
| signed radiation Pr, half | `[-4.27900e-4, -3.65683e-4]` |
| endpoint signed S, memory bound | `[-2.181828e-6, 2.099674e-6]` |

따라서 이 finite-owner cell 전체에서 matter source는 양수이고 radiation source는 음수다. Total signed memory enclosure에는 0이 들어가므로 이 enclosure만으로 total shear 부호를 결정하지 않는다. 같은 정규직교 normal frame에서 `Pm+Pr`를 먼저 합하고 norm을 취하며, Frobenius는 half-contraction의 sqrt(2)배다. 두 양의 species norm을 더해 total이라고 표시하지 않는다. 이 분해는 같은 coupled trajectory의 조건부 기여 분석이고 species-off causal experiment가 아니다.

## 11. 검토·실행·게시 상태의 분리

독립 generic kernel 검산은 최종 16/16 PASS다. 최초에는 역순 initial interval을 거부하지 않는 입력 계약 문제가 1건 발견됐고, initial/RHS finite-ordering guard로 수정했다. 최초 실패, guard 수정 확인 및 portable test 확인을 각각 남겼다. Guard 추가 전 실제 cell 결과는 다시 실행하지 않았다. 계산 본문의 AST 동일성과 저장 interval 134개의 guard 통과를 대조한 bridge가 원래 실행 hash와 현재 코드를 연결한다. [INDEPENDENT_MATH_CODE_REVIEW.json](verification/INDEPENDENT_MATH_CODE_REVIEW.json), [INPUT_GUARD_VALIDATION_BRIDGE.json](verification/INPUT_GUARD_VALIDATION_BRIDGE.json)

Runner의 fake-worker 검산과 original-owner point 검토는 서로 다른 담당자·receipt를 가진다. Fake-worker PASS를 실제 NCP 실행으로 세지 않는다. Actual one-cell PASS도 전체 1231-case history 인증으로 세지 않는다. Timing이 receipt에 있어도 실행 회계이며 benchmark speedup이 아니다. 게시·remote readback·백업 완료는 별도의 delivery evidence와 최종 DAG가 선언한다. 이 문서는 reviewer receipt를 합치거나 담당 역할을 바꾸지 않는다.

## 12. 완료 데이터와 다음 의무

PHYS76의 기존 z20→4 1231개 이력, 완료된 z4→2 continuation, 누적 attribution과 preliminary plots는 그대로 사용한다. Long collisionless 1231개, REI warm 729개, HH74 control 63개는 별도 물리 범위다. 새로운 표를 만들기 위해 어느 계산도 다시 실행할 필요가 없다. 기존 vectorized solver와 O(KN) saved-history 처리의 근거는 [PHYS76 최적화 정리](../hh_phys76_time_transport_20261021/OPTIMIZATION_REUSE_KO.md)와 [analysis summary](../hh_phys76_time_transport_20261021/results/analysis_z20_z2/SUMMARY.json)에 있다.

다음 작업은 현재 DAG의 full-history enclosure에 직접 연결한다. 준비된 짧은 prefix request를 가용 자원 안에서 실행하고, 실패한 특정 cell이 있으면 그 증거를 기준으로 predictor·subdivision·centered bound를 개선한다. Endpoint error는 cell 사이에 반드시 운반한다. Momentum quadrature와 angular truncation의 continuum error는 다른 OPEN 의무로 남긴다. 근거 없는 GPU/MPI·fast-math 전환이나 이미 완료된 sweep의 benchmark queue를 추가하지 않는다.

현재 인증 대상은 **정확히 capture한 coefficient와 저장된 초기 point가 정의하는 smooth real-lift IVP**다. 과거 runtime의 알려지지 않은 내부 coefficient bits나 모든 floating-point 연산을 소급하여 인증하지 않는다. 이 구분을 유지하면서 한 cell의 constructive source producer를 실제로 확보한 것이 PHYS77의 기여다. [DAG_OVERLAY.json](DAG_OVERLAY.json), [THEOREM_KO.md](theory/THEOREM_KO.md)

`HH_R10=OFF`. Production admission은 발급하지 않는다.
