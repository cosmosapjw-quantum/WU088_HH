# G6 Petras wrapper의 최종 한정 static review

검토 범위는 `interior_pilot/petras_host.cpp`, `petras_host.hpp`, `native_petras_synthetic.cpp` 세 파일이다. 구현 담당자의 ready 통지 후 읽었으며, 발견 사항 세 건의 수정만 재검토하여 `REVIEW.json`의 최종 SHA256에 결박했다. 이 검토자는 G1 정리 설계에 참여했으므로 theory-design 독립성은 없다. 구현 담당자와 분리된 artifact 검토이며 `independent_review_admitted=false`다.

**결과:** 세 finding은 정적으로 수정 확인했다. 지정 범위에서 추가로 열린 static correctness finding은 없다. Native compile/link/ABI/runtime 검증 및 실제 HH callback/적분은 모두 미수행이다. 이 결론으로 B01 backend verification, B02 actual enclosure 또는 B05 실제 feasibility를 닫지 않는다.

## Primary authority

FLINT 3.4.0 C01 source archive SHA256 `108ab51a4dd33918ff3308f0c63a63616ae30a2c174d50c9188676e85011346f`를 확인했다. `acb_calc.h`, `acb.h`, `arb.h`, `mag.h`, `arb_calc.h`, `flint.h.in`, `fmpq.h`의 API, `acb_calc/integrate.c` 및 `integrate_gl_auto_deg.c`의 callback order/return semantics, 보존된 `acb_calc.rst`를 대조했다. 호출 symbol 및 `acb_calc_integrate` signature는 pinned source에 존재한다. 특히 `depth_limit`은 queued intervals 수이고 `eval_limit`은 approximate bound이므로 wrapper의 별도 dispatch counter가 필요하다.

## Uniform nesting과 반환 radius

outer box는 `acb_set`으로 양쪽 component radius까지 통째로 inner context에 전달된다. Midpoint projection은 없다. Inner callback의 analytic request는 outer order1 또는 inner order1이면 1이며, joint holomorphy 및 whole-parameter-box inclusion 계약을 요구한다. 이 계약은 G1의 compact uniform domination lemma에 의존한다. Boolean flags와 proof-reference 문자열 자체가 수학적 증명을 검증하는 것은 아니므로 actual callback/hash binding은 후속 실행 계약의 책임이다.

`point_inner`와 `uniform_inner`는 tolerance/radius acceptance 정책을 달리한다. Intrinsic parameter-image width를 inner integration error로 오해하지 않도록 uniform range에는 별도 cap을 둔다. 어느 정책도 outer box의 radius를 제거하지 않는다. Outer callback은 inner가 돌려준 uniform range를 outer integral의 enclosing function value로 사용한다.

승인은 `ARB_CALC_SUCCESS`만으로 하지 않는다. 반환 ball의 finite 여부 및 real/imag 각각의 실제 radius 상계를 검사한다. Requested absolute/relative tolerance는 목표이며 achieved radius가 아니다. Accepted 및 valid-too-wide 결과의 actual mag radius dumps를 저장한다. Rectangle radius를 complex modulus radius로 쓰려면 G1의 outward `sqrt(r_re²+r_im²)` 변환이 추가로 필요하다.

## 최초 finding과 수정

| ID | 최초 문제 | 수정 후 정적 확인 |
|---|---|---|
| P01 | outer order1의 domain trial refusal이 inner order0으로 전달되면서 전역 NONFINITE stop을 만들어, outer subdivision을 막음 | speculative parameter-trial context를 전달하고 전체 inner real path의 사전 range query를 추가했다. Outer order1의 domain/no-convergence/width refusal은 비지속적 실패로 처리하여 후속 작은 box를 시도할 수 있다. Actual resource/contract failure와 real-path 실패는 계속 전역 중단한다. |
| P02 | 독립적으로 outward-rounded 된 `box*(1/3 ball)` 전체를 다른 valid result가 반드시 포함해야 한다고 요구 | Exact image `[1/3,2/3]+i[-1/3,1/3]`의 rational component endpoints를 직접 검사한다. |
| P03 | Valid but too-wide integral ball을 지우면서 achieved width 정보도 잃음 | Output invalidation 전에 real/imag mag upper radii를 Report에 직렬화한다. Acceptance는 false로 유지한다. |

P01에 대해 같은 budget에서 invalid outer trial을 거절한 다음 valid trial을 허용하는 synthetic native fixture가 추가됐다. 현재 확인은 그 소스 의미에 한정되며 native fixture가 실제 통과했다고 주장하지 않는다. 초기 상태는 `INITIAL_FINDINGS.json`에 보존했다.

## 적용 한계와 stop

Exact real `acb` endpoints는 실질적으로 정확히 표현 가능한 dyadic endpoints를 요구한다. 비dyadic rational의 midpoint를 대신 사용하면 적분 domain이 바뀐다. G5 tail과 G6 compact integral은 동일한 dyadic endpoints에 결박해야 한다.

전체 inner-path 사전 query는 넓은 box에서 보수적으로 실패할 수 있다. 실제 domain은 유효해도 dependency inflation 때문에 거절될 수 있으며, 이는 남은 feasibility 문제다. 실제 callback 비용·반환 width·subdivision 효율은 미측정이다.

Wrapper는 단일 FLINT thread, 최대 두 nested integration levels, 전역 dispatch/integration call cap을 검사한다. Cooperative wall checks는 backend 내부에서 멈춘 호출을 강제로 끊지 못하므로 외부 process resource guard가 필요하다. Native build와 synthetic execution, 실제 input/provenance binding, HH numerical authorization, full-D/epsilon/decision certificate는 후속 gate다.

이번 검토로 범위를 종결한다. Native compile=0, native runtime=0, HH evaluation=0, `certified_epsilon=null`, `certified_eta=null`, `rigorous=false`.
