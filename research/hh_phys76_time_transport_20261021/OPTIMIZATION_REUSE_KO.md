# PHYS76 최적화·재사용 연구 정리

2026-10-21. 실제 채택한 계산 경로와 별도 계보의 후보를 구분한다.
1231개 기존 z20→4 이력은 보존했고, 필요한 z4→2 tail 1231개가 완료됐다.
현재 이 실행의 failed/pending case는 각각 0개다. 같은 계산을 다시 NCP에 제출할 필요는 없다.
과학적 기준은 PR128이며, PR129 standalone 도구가 그 구현을 대체하지 않는다.

## 1. 이번에 실제로 채택한 개선

| 대상 | 실제 선택 | 보존한 것 |
|---|---|---|
| 전체 시각의 shear memory | 두 node씩 전진하는 누적 Simpson recurrence | PR128 최종 endpoint의 동일한 실수 산술식 |
| integrating factor | 인접 node 사이의 국소 전달비 | 같은 저장 trajectory의 H와 signed source |
| vectorization | species 축과 모든 case 축을 NumPy로 함께 계산 | 시간 순서와 두 sector의 독립 부호 |
| 추가 과학 계산 | 저장된 8-state endpoint에서 필요한 tail만 실행 | 원본 RHS, cosmology, a_ref, href, A_m |
| 진단 연결 | old/tail grid를 따로 적분한 뒤 전달법칙으로 결합 | 기존 sampled residual의 독립적인 전파 |
| 입력과 재개 | native 파일 직접 읽기, SHA-bound 완료 case skip | 원본 파일과 실행 identity |
| 자원 공유 | 기존 HH74 cooperative lease와 process pool | 다른 세션의 실행과 원본 resource source |
| 조건부 enclosure | Decimal outward arithmetic의 독립 API | 실제 whole-cell enclosure라는 입력 전제 |

`source/cumulative_memory.py`, `source/continue_saved.py`, `source/analyze_saved.py`가 실행 구현이다.
`source/interval_transport.py`는 별도의 조건부 증명·검산 경로이며 sampled packet에 자동 적용하지 않는다.

## 2. 복잡도 개선의 정확한 의미

case 수를 K, 저장 node 수를 N이라 하자. 각 node까지 prefix를 처음부터 다시 적분하면 O(KN²)가 된다.
이번 recurrence는 모든 node를 O(KN) 연산으로 계산하고, 출력 보존에 O(KN) 저장공간을 사용한다.
PR128의 **단일 최종 endpoint** 계산 자체는 이미 O(KN)이다.
따라서 기존 endpoint 구현이 N배 느렸다는 주장이나 측정 speedup은 성립하지 않는다.
개선한 것은 새로 필요한 전체 time-history attribution의 계산 구조다.

전달비는 다음과 같다.

\[
T_{ij}=\exp\{3(x_i-x_j)+\log H_i-\log H_j\}.
\]

짝수 node에서는 직전 두 node의 Simpson panel을 기존 memory에 더한다.
홀수 node는 같은 세 표본의 quadratic primitive를 쓰므로 다음 저장 표본 하나와 음의 weight가 들어간다.
이 방식은 offline sampled-data 처리이며 causal time-stepper 또는 positivity-preserving solver가 아니다.
전 구간에서 커지는 integrating factor 배열을 만들지 않아 불필요한 전역 크기 증가를 피한다.
국소 전달비 자체의 overflow 가능성은 남으며, 구현은 nonfinite 산술을 실패로 보고한다.
감쇠 항의 binary64 underflow는 허용하지만 clipping이나 tolerance 완화는 하지 않는다.

species/case 축은 동시에 처리하고, 시간의 재귀 의존성은 순서대로 유지한다.
각 trajectory의 적응적 ODE step을 강제로 같게 만드는 dense batch 적분은 도입하지 않았다.
이 선택은 다른 case의 상태를 섞지 않으면서 저장 데이터 처리의 Python 반복을 줄인다.

## 3. 8-state owner와 완료 데이터 재사용

REI198의 기존 `ComponentReduced`는 이번 연구에서 새로 만든 축약이 아니다.
그 원본 8-state RHS와 canonical-momentum 표현을 byte-pin하여 그대로 사용했다.
상태는 `[tau,b,q,E0,E2,E4,E6,E8]`이며 여기서 q는 s/href이다.
이 q를 deceleration parameter로 해석하거나 A=2−q_dec에 대입하면 안 된다.
원래 x=ln(a/(1/21))와 href를 유지하고, 저장 z4 상태에서 x=ln(7)까지만 진행했다.
원본 `initial()`이나 원본 전체 구간 `solve()`는 호출하지 않았다.
원본 DOP853의 rtol=3e-11, atol=3e-13과 각 case의 원래 A_m을 유지했다.

old 65표본과 tail 33표본은 경계 하나를 공유하므로 표시 packet은 case당 97표본이다.
서로 다른 두 uniform grid를 합친 좌표에는 한 번의 uniform Simpson 공식을 적용하지 않는다.
tail 전달비 G에 대해 J_A=G J_A,old+j_A,tail, D=G D_old를 사용한다.
combined residual도 tail-local residual과 G×old residual로 분리해 보존한다.
자세한 유도는 `theory/CONTINUATION_KO.md`와 `evidence/STITCH_INDEPENDENT_REVIEW.json`에 있다.

## 4. 물리량과 부동소수점 순서

같은 정규직교 normal frame에서 pi_A=diag(−p_A,−p_A,2p_A)를 사용한다.
물질·복사 signed component를 합한 뒤 norm을 취하며, Frobenius는 half-contraction의 sqrt(2)배다.
이 memory 분해는 같은 coupled trajectory의 조건부 기여 분석이다.
species-off 인과 실험이나 서로 다른 물리 계보 사이의 대응 증거로 쓰지 않는다.

실제 검토에서 단일 행 GEMV와 다중 행 GEMM의 sampled brightness가 84개 endpoint에서 마지막 비트만 달랐다.
같은 endpoint를 33행으로 반복한 진단은 1231개 모두 정확히 일치했다.
before-solver 진단을 이 batch 형상에 맞췄으며 상태 보정이나 시간 진행은 없다.
이 발견은 vectorization이 실수 산술식뿐 아니라 reduction 순서도 바꿀 수 있음을 보여 준다.

total norm의 최악 상대 비교차 5.92e-14는 절대차 3.68e-22였다.
그 표본의 cancellation condition number는 1335.46이고, 각 sector norm 차이는 약 4.8e-16였다.
90-digit Decimal 비교로 별도 정규화 후 합산의 cancellation-amplified roundoff임을 확인했다.
원자료와 최초 발견을 보존했으며 `evidence/TENSOR_CANCELLATION_ROUNDOFF_REVIEW.json`에 설명했다.

## 5. 병렬화와 실제 실행 범위

worker 내부 BLAS/OpenMP 계열 thread 수를 1로 제한해 중첩 병렬화를 피한다.
각 독립 case는 process에 배분하며, 원본 모델 context를 worker에서 재사용한다.
NCP 설정의 상한은 64 CPU/128 GiB이고 실제 affinity/cgroup/가용 메모리와 shared lease를 확인한다.
NCP reserve는 16 GiB, local reserve는 2 GiB이며 case당 0.25 GiB를 예약한다.
이번 실제 실행은 local 2 workers였다. NCP 64-core 실측 결과라고 표기하지 않는다.
실행 회계는 wall 115.23 s, case CPU 합계 50.18 s이며 benchmark 비교가 아니다.
새 tail ODE 1231회, 기존 trajectory 재실행 0회, benchmark 0회, NCP 실행 0회다.
완료 case는 identity/history hash를 확인한 뒤 skip하며 실패·중단 증거는 자동 재시도하지 않는다.
가용 자원만 새로 예약하고 다른 프로세스를 signal하거나 종료하지 않는다.

## 6. 외부 기법에서 재사용한 부분과 채택하지 않은 부분

| 원문·공식 문서 | 실제 반영 | 적용 한계 |
|---|---|---|
| [SciPy cumulative_simpson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.cumulative_simpson.html) | 세 표본의 누적 quadratic primitive와 odd-node convention | 검증한 식을 custom recurrence로 구현; SciPy 호출의 성능을 측정하지 않음 |
| [Python Decimal](https://docs.python.org/3/library/decimal.html) | directed arithmetic, correctly-rounded exp를 이웃 decimal로 감싼 enclosure | next_plus/next_minus의 quiet subnormal 경계를 별도로 거부 |
| [Niesen–Wright phi-functions](https://arxiv.org/abs/0907.4631) | exponential response의 phi 표현과 안정한 작은 인자 처리 배경 | 행렬 Krylov solver 또는 새 ODE method를 도입하지 않음 |
| [SciPy exprel](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.exprel.html) | (exp(z)−1)/z의 removable singularity를 비교하는 참고 | binary64 exprel을 interval certificate로 사용하지 않음 |

작은 |a h|의 response는 Decimal interval series와 명시적인 geometric remainder bound로 계산한다.
a=0에서는 response=h를 정확히 사용한다. 일반 a에서는 양의 Green kernel bound를 사용한다.
SciSpace/Exa의 검색 결과는 원문 탐색에 사용했고, abstract나 검색 요약을 증명으로 취급하지 않았다.
Wolfram 검산의 실제 출력과 경고는 `evidence/THEORY_TOOL_AND_TEST_EVIDENCE.json`에 보존했다.
새 JIT, MPI, GPU, fast-math, interpolation table 및 species 통합 근사는 이번 실행에 채택하지 않았다.

## 7. 다른 최신 계보의 재사용 후보

| 계보 | 확인한 identity와 내용 | PHYS76에서의 처리 |
|---|---|---|
| REI PR214 ACCEL01 | HEAD `98fcf3943fa54e089b0292d166c3a47becb5edb8`; 고정 model의 exact (x,b) cache와 완료729 case-aware work plan | warm C15 후보로 보존; 이 8-state RHS에 복사하지 않음 |
| REI PR215 native moments | HEAD `231df3ab717dbc112f63b77953f64def08e9bcb5`; optional C++17 fused three-moment evaluator | 별도 수치-equivalence 경로; 현재 tail 실행에 미사용 |
| BASS PR178 | HEAD `7fe0e25a28c0e48110c522378e203ffb934cc504`; 위 native lane의 동일한 top-level 15 entries | repository 이름만으로 독립 결과 두 건으로 세지 않음 |
| REI PR199 unified 결과 | HEAD `744438f4512c7df1646aad0136ddc435b27200b0`; 40/56-state, 153-node 계보의 237 unique long histories | wrapper/state/grid/axis identity를 분리하고 raw alias를 만들지 않음 |

PR214 cache는 정확한 binary64 (x,b) key와 고정 kinetic binding에서 기존 연산을 그대로 재사용한다.
geometry가 다른 coupled trajectory에 값을 공유하거나 source-only cache로 H 전체를 대체하지 않는다.
PR215는 원래 96 radial×32 angular quadrature를 16 reflected pairs로 계산한다. 새 16-node rule이 아니다.
O3/C++17, no-fast-math, fp-contract=off, Neumaier sum 및 명시적인 parity rejection이 보고되어 있다.
native-vs-owner 일치는 numerical equivalence이며 bitwise equivalence로 승격하지 않는다.
게시 DAG의 local verification과 `IMPLEMENTATION_IDENTITY.json`의 review/delivery 상태 차이는 그대로 남긴다.
PR213 warm 729개, HH74 control 63개, 이번 long 1231개를 하나의 계산 범위로 합치지 않는다.
REI199는 같은 vendor kernel을 쓰므로 명시적인 norm/state map 뒤 공통 성분을 비교할 수 있다.
그 상태는 `[tau,b,s/href,u_th/rhocrit0,E_gamma,N_gamma,E_nu,N_nu]`의 hierarchy 블록이며 L8에서 40성분, L12에서 56성분이다.
Lane B의 Frobenius 초기축은 Sigma={0,0.0003,0.001,0.003,0.01,0.03,0.1}, Pm={−0.0003,−0.0001,0,0.0001,0.0003}, Pr={−0.001,−0.0003,0,0.0003,0.001}다.
검토된 source HEAD는 `3a525e3e16f1ba9393818a800327cc58597fd7b5`이며 live HEAD와 구분한다.
121+32=153 epochs, 별도 wrapper와 초기축이므로 이 8-state 65+32=97 packet과 raw-run identity를 합치지 않는다.
최신 원문 상태와 source hash는 `evidence/FINAL_REMOTE_IDENTITY_CHECK.json`, 최초 intake는 `evidence/INVENTORY.json`을 따른다.

## 8. 실제 미완료 DAG에 연결되는 다음 작업

| 기존 node | 구체적인 다음 의무 | 이번 결과가 제공하는 출발점 |
|---|---|---|
| `CONTINUUM_TIME_ANGULAR_CERTIFICATE` | 실제 전체 cell의 A,P_m,P_r enclosure를 제공하는 upstream 계약·유도 | conditional interval response theorem, signed interval 구현과 검증 |
| `CONTINUUM_TIME_ANGULAR_CERTIFICATE` | 인증된 cell/trajectory들을 독립 배치하면서 outward enclosure와 provenance를 보존 | species별 전달 API; float sampled packet과 별도 경로 |
| `FULL_NATIVE_COLD_EOR` | 선택된 full owner의 kernel binding을 확정한 뒤 exact cache/native 후보의 적용 범위를 대조 | PR214/215의 source-bound dependency map; warm 검증을 cold 인증으로 전용하지 않음 |

`GENERAL_NON_LRS`와 `HH_PHYSICAL_MATCHED_XI_AND_RATE`는 이번 LRS time-plot 목표로 닫히지 않는다.
가속 작업은 위 실제 의무와 필요한 입력에 연결될 때만 추가한다.
global convergence, 전체 angular positivity 및 continuum residual 인증도 계속 별도 의무다.
이번 sampled radiation-work residual 5.39e-14와 shear reconstruction residual은 그 인증의 대체물이 아니다.

## 9. 재개 시 사용할 실제 증거

수학은 `theory/THEOREM_KO.md`, 실행 구간은 `theory/CONTINUATION_KO.md`에 정리했다.
구현 검토는 `evidence/CONTINUATION_INDEPENDENT_FINAL_REVIEW.json`과 `evidence/NATIVE_LOADER_INDEPENDENT_REVIEW.json`이다.
1231-case 과학 결과 검토는 `evidence/SCIENTIFIC_RESULT_REVIEW.json`이며 검토 자체의 ODE/benchmark는 0회다.
실제 그림·수치는 `results/analysis_z20_z2/`와 `figures/z20_z2/`의 source-bound 산출물을 재사용한다.
게시·백업·최종 remote HEAD는 root의 delivery/handoff를 확인하며, 이 문서가 그 상태를 대신 선언하지 않는다.
`HH_R10=OFF`; production admission은 발급하지 않는다.
