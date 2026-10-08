# G6 synthetic compact-interior pilot

구현 상태는 `IMPLEMENTATION_VERIFIED_SYNTHETIC_ONLY`다. 실제 HH primitive/entry,
Frozen107 constant, raw matrix를 평가하지 않았다. **B05는 UNMEASURED**, B02의
실제 endpoint/interior/final D enclosure는 미평가 상태를 유지한다. FLINT 3.4.0
Petras 경로는 이 component에서 native build·실행하지 않았다.

## 계산 정의와 포함 정리

유한 실구간 I와 복소 parameter rectangle Z에 대해, 모든 t∈I와 z∈Z에서
f(t,z)가 callback이 반환한 rectangle R(I,Z)에 속한다고 가정한다. 각 z에서
실부·허부가 적분 가능하면 각 coordinate의 점별 부등식을 적분하여
∫_I f(t,z)dt ∈ |I| R(I,Z)를 얻는다. 분할 I=∪P_j는 interior가 서로 겹치지
않으므로 ∑|P_j|R(P_j,Z)가 모든 z∈Z에 대해 같은 적분을 포함한다. 경계점은
측도 0이다. 이 단계에는 복소 contour integration이나 holomorphy 승격이 없다.

구현은 정수/Fraction 사칙연산으로 각 coordinate의 lower/upper endpoint를
정확히 계산한다. 오래된 panel을 두 자식으로 교체할 때 lower에서 이전 lower,
upper에서 이전 upper를 제거한다. 일반 interval subtraction으로 제거하여
쓸데없는 의존성 폭을 누적하지 않는다. Callback의 포함 명제 자체는 외부 증명
의무다. `uniform=True`와 proof reference만으로 임의 callback이 증명되지는 않는다.

TOY_T1: f(t,z)=z t², 0≤t≤1. Interval 곱셈과 복소 rectangle 곱셈의 포함성으로
whole-box range가 성립한다. 독립 antiderivative t³/3에서 ∫₀¹zt²dt=z/3.
Z=[1,2]+i[-1,1]의 정확한 image [1/3,2/3]+i[-1/3,1/3]을 포함함을 확인했다.
TOY_T2: f(t,z)=z는 parameter image가 그대로 적분되므로 Z=[0,1]이면 폭 1은
분할로 줄지 않는다. 이를 valid-but-wide로 분류한다.
TOY_T3: outer panel X 전체를 inner parameter rectangle X+i{0}으로 전달하고,
inner가 그 전체의 z/3을 포함한 뒤 outer 적분을 수행한다. 독립 expected value는
∫₀¹z/3 dz=1/6이다. Outer midpoint에서만 inner를 계산한 명시적 계약은 거부한다.

## 실제로 측정한 synthetic 결과

다음 값은 `interior_pilot/evidence/SYNTHETIC_PILOT.json`의 한 번 실행 결과다.
Wall time은 tracemalloc 계측을 포함하며 반복 benchmark나 HH 비용 추정이 아니다.
Width는 실부/허부 rectangle의 **전체 폭 중 최대**이며, parameter가 구간이면
고유한 parameter-image 폭도 포함한다. Requested width와 achieved width를 구분한다.

| Toy | 상태 | achieved width | callback 수 | 전체 nested split 수 | wall s | Python peak bytes |
|---|---|---:|---:|---:|---:|---:|
| toy_real_t_squared_width_1/16 | TARGET_WIDTH_MET | 121/2048 | 31 | 15 | 0.007419 | 19335 |
| toy_real_t_squared_width_1/64 | TARGET_WIDTH_MET | 1019/65536 | 119 | 59 | 0.029590 | 59224 |
| toy_real_t_squared_width_1/256 | TARGET_WIDTH_MET | 130881/33554432 | 477 | 238 | 0.126246 | 237736 |
| toy_uniform_complex_parameter_box | TARGET_WIDTH_MET | 12271/16384 | 27 | 13 | 0.007113 | 16568 |
| toy_nested_uniform_integral | TARGET_WIDTH_MET | 64150191/1073741824 | 2194 | 1090 | 0.610050 | 123248 |
| toy_evaluation_cap | CERTIFICATE_INCONCLUSIVE_RESOURCE_LIMIT | 1 | 1 | 0 | 0.000304 | 3648 |
| toy_width_floor | CERTIFICATE_INCONCLUSIVE_WIDTH | 1 | 7 | 3 | 0.000726 | 6176 |
| toy_domain_failure | CALLBACK_DOMAIN_FAILURE | — | 1 | 0 | 0.000077 | 2768 |
| toy_midpoint_only_refusal | INVALID_RANGE_CONTRACT | — | 1 | 0 | 0.000092 | 3064 |

## 유한 예산과 실패 의미

각 case는 실행 전에 Caps를 정한다. 기본값은 최대 callback 20,000, live panel
2,048, cooperative wall 10초, tracked-state estimate 16 MiB, rational endpoint
bit-length 32,768, subdivision depth 20이다. Nested case는 하나의 Budget으로
전체 callback을 최대 15,000, live panel을 1,024로 제한했다. 정확한 case별 cap과
peak live panel/state estimate는 JSON에 보존했다. Fraction에는 floating precision
오차가 없지만 bit-length/work cap을 별도로 적용한다.

Wall guard는 callback 전후와 분할 경계에서 확인한다. 실행 중인 callback을 강제로
종료하지 않는다. 따라서 이것을 hard deadline으로 취급하면 안 된다. 메모리 cap은
고정 panel allowance와 rational limb 크기를 합친 **추적 state 추정치**다. 실제
process RSS 또는 callback/native 임시 allocation의 hard limit가 아니다.
`require_hard_memory_limit=True`는 명시적으로 거부한다. `tracemalloc` peak 역시
Python allocation 측정치이며 RSS가 아니다. G7 host runner는 필요한 hard process
budget을 별도로 구현·검증해야 한다.

Eval/panel/depth/wall/state/bit cap은 `CERTIFICATE_INCONCLUSIVE_RESOURCE_LIMIT`,
줄지 않는 폭은 `CERTIFICATE_INCONCLUSIVE_WIDTH`로 반환한다. Resource stop 때
완성된 이전 enclosure가 있으면 유지하되 성공으로 승격하지 않는다. Domain 오류,
whole-box 계약 위반, callback 구현 예외는 서로 구분하고 accepted enclosure를
반환하지 않는다. 모든 종료 경로에서 nested tracked budget state를 해제한다.

## 검증과 해석

초기 RED: 18 tests, exit 1, 미구현 seam의 NotImplementedError. 최초 GREEN:
18 tests, exit 0. 최종 통합 component suite: **21 tests, exit 0**. 추가 synthetic
measurement runner: **9 cases, exit 0**. 불필요한 기존 scientific suite 재실행과
과거 test count 합산은 하지 않았다. 금번 명령은 synthetic/exact implementation
check이고 HH science command·native build·numerical certificate run은 각각 0이다.

Primary Petras, product Chebyshev, Taylor model, MPFR/MPFI의 실제 HH 측정치는 없다.
현재 자료로 이들 사이의 비용·폭 우열을 선언하거나 range-sum toy의 저렴함을 HH
feasibility로 승격할 수 없다. 다음 actual pilot은 backend/callback authority와
명시적 bounded execution scope가 성립한 뒤 수행해야 한다. Owner component
verification은 admitted independent scientific decision review가 아니다.

## Primary native caller 추가: 실행 검증 미완료

`interior_pilot/petras_host.hpp/.cpp`에 실제 `acb_calc_integrate` 호출, G4 Slice
연결, full outer complex box를 전달하는 nested caller, shared evaluation budget을
추가했다. Native source는 FLINT3.4.0 primary headers/docs/source와 이름·signature를
대조했고 10개 구조 검사를 통과했다. 이는 C++ compile/link/runtime 검증이 아니다.
Host용 synthetic fixture 10개와 build-only script를 작성했으며 실행하지 않았다.

반환 ball의 finite 상태·실제 real/imag component radius가 acceptance authority다.
요청 tolerance만으로 성공을 선언하지 않는다. Too-wide finite ball의 radius dump는
진단용으로 보존하고 accepted output은 nonfinite로 거부한다. Outer parameter box의
고유한 image width를 고려해 uniform/point용 inner cap을 분리하되 midpoint는
사용하지 않는다. Analytic trial domain refusal과 실제 domain/resource 실패를
구별하도록 별도 static review 발견사항 P01–P03을 수정했다. Native runtime 검증
전까지 B15 및 primary implementation에 관한 수치 성공을 주장하지 않는다.

상세 source/host 계약: `interior_pilot/PETRAS_HOST_README.md`. 별도 host guard는
process-group timeout 및 프로세스별 RLIMIT_AS를 제공하지만 aggregate process-tree
RSS cap은 아니다. 정확히 표현 가능한 dyadic endpoints를 택하고 G5 tail에도 같은
값을 사용해야 하며 비dyadic rational을 근사 midpoint로 몰래 대체하지 않는다.
