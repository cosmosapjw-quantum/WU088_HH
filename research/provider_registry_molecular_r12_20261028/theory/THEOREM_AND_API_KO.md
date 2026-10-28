# R12 정리와 실행 API

## 재사용 가능한 정리

동일 family/state/clock의 all-starts full-A block q와 nonexpansive remainder, zero-mass residual forcing 및 whole fine/coarse-domain scalar bounds를 전제한다. Source forcing이 정확한 유한 partition에서 상수이고 c>=0,d_c가 sweep전체상수이면, PROOF_KO.md의 positive overlap 식은 임의의 rational observation partition에서 같은 raw ideal comparison을 준다. 모든 translated source knot, initial block jump 및 old cap boundary를 합치면 각 subcell에서 R이 affine이다. 양의 signed Bernstein weights로 E endpoint를 적분하고 constant R majorant로 closed-cell E를 인증할 수 있다.

같은 실제 source의 old closed-cell cap은 exact interval inclusion으로 세분cell에 전달된다. Old point cap은 exact point equality에서만 전달된다. Global R memory는 유지하며 observation whole upper는 gap-free subcell upper의 최대다. 이는 조건부 비교방법 정리이고 실제 HD reactive closure나 physical consumer의 채택이 아니다.

## 호출 경로와 입력

- src/nonaligned_convolution.py의 nonaligned_sweep(q,tau,c,d,g_r,g_e,source_knots,observation_knots,initial, binding=...,certificate=...)가 일반 산술 경로다. Certificate의 all-starts/full-family/whole-domain fields는 명시적 외부 전제이며 metadata검사가 그 과학 전제를 새로 증명하지 않는다.
- saved_case_sweep(r11_source_bytes,case_id,grid_variant)는 실제 R11 PRIMARY_RESULTS 원 bytes SHA80ed0f8df5c785e47ce737acb8b029485db54b543d57498bf182427093f29b1b를 검증한 후 저장 q/tau/초기값/계수/binding/caps를 선택한다.
- grid_variant는 aligned 또는 nonaligned다. Nonaligned의 내부 관찰점은 n=1..191에서 홀수(n+1/3)delta, 짝수(n-1/5)delta이며 양끝0,192delta를 유지한다. Saved constant forcing192cell은 전 값의 정확한 equality 후 onecell로 압축한다.
- 일반 함수의 cap_source_bytes와 cap_case_id는 함께 지정한다. 임의 label/배열로 old cap을 꾸밀 수 없으며 actual pinned bytes를 읽어 선택한다.
- Exact int/Fraction/rational text를 사용한다. Bool/float grid, 중복·역순·영길이 cell, 다른 horizon/source/state/clock/case, 음수 forcing, unsupporteddimensions 및 자원초과는 DomainError다.

## 주요 출력

| 필드 | 의미 |
|---|---|
| parameters/source/requested_times | 실제 exact q,tau,c,d,초기값,certificate와 원 forcing 위치 |
| refined_times/refinement | 모든 필요한 event knots와 source/observation inclusion map |
| exact/F_at_refined,R_at_refined | exact Fraction positive-overlap 결과 |
| exact/R_affine_cells | 각 subcell의 L,V 및 closed-cell R sup |
| raw/endpoints_lower,upper | 선택 rational-q ideal comparison의 outward enclosure |
| raw/whole_cells_upper | 관찰 closed-cell의 upper; endpoint 연결선과 다름 |
| capped | 실제 source-bound upper만; lower는 null |
| caps/subcell_to_old_cell | 기존 closed-cell에 포함됨을 증명할 map |
| caps/refined_point_to_old_point | exact equal point만 old point index,나머지는null |
| work/rounding | 실제 refinedcells/overlapterms/길이종류와128/96산술범위 |

Raw lower는 실제 물리 오류 lower가 아니다. Capped 결과는 physical error upper로서의 조건부 동일 source 교차이며 chosen raw comparison 자체의 interval enclosure라고 부르지 않는다. Native9는 native K + synthetic conditional reaction fixture다.

## 유한 오차·실행 계약

R12는 quadrature 없이 exact overlap을 계산한다. Exponential integration은 R11 proved dyadic128/Taylor96 purefunctions12개를 그대로 복사하고 outward tail을 유지한다. Signed/nearzero d는 같은 양의 weights로 처리한다. Independent reference는 production을 import하지 않고 Fraction primitive J 및 Decimal160 closed forms를 사용한다. 1e-80relativeguard는 실행 전에 고정하며 reference의 intervalrigor로 승격하지 않는다.

실제 scientific command는 verification/execute_once.py primary와 reference 두 경로다. 각1회60CPU/90wall, Wolfram새script1회30wall이며 overwrite를 거절한다. Source와 정확한 freeze를 먼저 게시한다. 결과가 생성된 뒤의 후처리는 저장값만 읽는다. 이전 R11/R10/R9/R8/R7/R6/PHYS91 runner·ODE·CAS의 재실행은 이번 계약에 포함되지 않는다.

Raw ideal의 observation refinement equality와 rounded값의 bitidentity를 구별한다. Capped E는 세분화로 유효upper가바뀔 수 있으므로 값 불변을 요구하지 않는다. 실제 결과·성능 수치는 raw/PRIMARY_RESULTS와 REFERENCE_RESULTS 및 PROCESS기록 이후에만 보고한다.
