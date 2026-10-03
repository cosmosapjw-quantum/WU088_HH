# 정확한 끝점 오차 작업 모듈

`planner.py`는 고정 입력 어댑터의 exact rational record를 2592개의 primitive 작업으로 연결하고, 선택한 작업 하나의 양의 실수 전체 영역 중 compact rectangle 밖의 오차 상계를 계산한다. 적분 내부값, 최종 D, epsilon 또는 과학적 인증을 계산하지 않는다. 원본 scientific source는 수정하지 않는다.

고정된 `assembly.cpp`의 인덱스는 `((((active*3+field)*3+orbital)*12+ia)*12+ib)`이다. field는 O/G1/G2, orbital은 s/px/pz 순서다. 매개변수는 저장 exponents, mu=1, z=3/4, active에 따른 d1/d2=(-2,0,-3/4), q1/q2=v 배치를 그대로 사용한다. 저장 donor coefficient는 실수 exact dyadic이며 i,j,k 순서에서 정확한 0만 제외한다. 새 복소 계수를 가정하지 않는다. 별도 `complex_abs_upper` 함수는 일반 복소 유리수 절댓값의 outward 상계를 제공한다.

공개 API:

- `build_plan(record, window, *, precision_bits=64, panels=4, caps=None, source_archive_bytes=None)`
- `validate_plan(plan, *, source_archive_bytes=None)`
- `evaluate_task(plan, index, *, source_archive_bytes=None)`
- `validate_result(plan, result)`
- `run_task(plan_path, index, result_path, *, resume=False, npz_path=None, execute_pinned=False)`
- `collect(plan, results, *, source_archive_bytes=None)`

window는 `{l_t,T_t,l_u,T_u}` canonical 유리수 문자열이며 양수인 dyadic cutoff만 허용한다. native Petras와 동일하게 inner=t, outer=u다. plan은 입력 기록, 원본 archive/record SHA, 고정 소스 SHA, window, precision, caps, 정확한 canonical parameters와 donor term 순서, 각 task SHA 및 plan SHA를 결합한다. 실제 pinned scope는 원본 NPZ bytes로 adapter의 재decode 검사를 다시 통과해야 한다. self-hash만으로 실제 입력 신원을 주장할 수 없다.

각 task는 기존 exact-rational endpoint engine으로 다음 값을 계산한다.

`B = sum_ijk abs(c_ijk) * C_F(k,orbital,field) * [E_t(i)*W_u(j) + min(J_t(i),W_t(i))*E_u(j)]`에 명시적 upward rounding을 적용한다.

이는 `(outside_t × all_u) ∪ (inside_t × outside_u)`의 서로 겹치지 않는 분할이다. 동일 k의 field majorant와 동일 (i,j)의 mass bound만 재사용한다. 아래에 명시한 outward dyadic 상계 압축을 적용하며 screening/부호 cancellation/host 부동소수 연산은 없다. normalization, orbital contraction, phase, parity, conjugation은 이 값에 들어 있지 않다.

## 상계의 유한 표현 정책

첫 실제 128-bit cutoff probe에서 원래 유리수의 분모가 커져 문자열·결과 bit 제한에 걸렸다. 원래 planner 바이트는 `history/planner_before_dyadic.py`, SHA256 `fe979174ac77d962dc9877a7ea39c01950421011e495134b52745bba44a5b4e0`로 보존했다. 원래 plan/실패 결과도 유지한다. 이 history 사본은 변경 전 바이트 증거이며 디렉터리 상대 import로 직접 실행할 사본은 아니다.

현재 `RELATIVE_DYADIC_UPPER_CAPPED_INTERIOR_V2`는 source engine이 반환한 양수 q에 대해 정확한 정수 연산으로 e=floor(log2(q)), h=2^(e-bits+1), U=ceil(q/h)h를 계산한다. q=0은 정확히 0이다. q>0이면

`q <= U < q+h <= q*(1+2^(1-bits))`.

C_F, mass bound, 각 양의 coefficient-product, 저장 term 순서의 누적합에 이 올림을 적용한다. 모두 비음수이므로 상계 성질이 보존된다. 원래 exact coefficient/입력값 및 source-engine precision은 변경하지 않는다. 작은 값에 고정된 absolute 2^-bits floor를 넣지 않는다. 주어진 상계가 조금 커지는 효과는 명시적이며 이를 bound 개선으로 주장하지 않는다.

실제 V1 probe는 큰 T에서 고정 4-panel 상계 J_t가 panel width와 함께 커지는 문제를 보여 주었다. V2는 같은 i,mu,a에 대해 pivot=1의 `W_t=lower_mass_bound(i,mu,a,1)+upper_mass_bound(i,mu,1)`를 계산하고 올림한 뒤 J_t를 `min(J_t,W_t)`로 제한한다. inside-t 질량은 기존 J_t와 전체 positive-t 질량 상계 W_t에 모두 포함되므로 그 최솟값도 유효하다. Et, Eu, Wu 및 두 disjoint 영역은 그대로다. 정확한 새 식은 `E_t*W_u + min(J_t,W_t)*E_u`다. W_t cache는 a,mu가 고정된 한 task 내부에서 i별로만 재사용한다. 추가 engine call은 i당 두 번이며 최대 전체 108회로 기존 128-call cap 안에 든다.

V1의 source/evidence는 `history/before_interior_cap/`에 보존했다. V2가 임의 cutoff 전체에서 비용·단조성·목표 반지름을 보장한다는 주장은 없다. 실제 개선 폭은 별도 마지막 3-window 실행으로만 판단한다.

plan/result의 `arithmetic_policy`에 버전, significand bits, 계산 단계, 누적합 순서와 표현 caps를 기록한다. `validate_result`는 그 정책에 따라 보고된 product와 합을 다시 계산한다. quantizer 입력은 65536-bit, 정렬·shift 작업은 131072-bit로 제한하고 shift 전에 검사한다. 기록할 정수 성분은 13280-bit 이하여야 하므로 기본 Python decimal 변환 제한 아래에 머문다. 음수·float·비정상 표현 또는 한도 초과는 허용하지 않는다.

반환 `endpoint_radius=B`는 누락된 복소 적분에 대한 disk 반지름이다. 향후 native interior rectangle의 실수·허수 성분에 각각 ±B를 한 번 더하는 것은 보수적으로 유효하다. 그 결과를 disk로 변환할 때는 사각형 모서리의 거리, 즉 두 성분 반폭 제곱합의 제곱근을 사용해야 한다. B를 그대로 사각형의 disk 반지름으로 쓰거나 내부 적분 오차를 두 번 더하면 안 된다.

## 실행

아래 명령의 경로는 절대 경로로 지정한다. NPZ와 생성 plan은 실제 저장값을 포함하므로 기존 공개 Git 산출물과 분리된 실행 디렉터리에 둔다. 이 문서의 명령 예는 입력을 읽거나 실행한 증거가 아니다.

```bash
python -B ABS_NEW/endpoint_tasks/planner.py plan \
  --npz ABS_FROZEN107_NPZ \
  --expected-sha256 8482d2854ab620c58bb1d7a7a45cf88eb71fd75081242263a9ef48927f0a282c \
  --scope FROZEN107_PINNED --output ABS_NEW_PLAN_JSON \
  --l-t 1/4 --T-t 4 --l-u 1/4 --T-u 4 \
  --precision-bits 32 --panels 1 --wall-seconds 30 --memory-mib 512

python -B ABS_NEW/endpoint_tasks/planner.py run \
  --plan ABS_NEW_PLAN_JSON --npz ABS_FROZEN107_NPZ --task-index 0 \
  --output ABS_NEW_RESULT_JSON --execute-pinned-endpoint
```

`[1/4,4]²`은 수학적으로 유효한 시작 구간일 뿐 유용한 최종 반지름을 보장하지 않는다. plan 명령은 endpoint를 평가하지 않는다. run 명령만 선택한 한 task를 평가한다. 기본 실행은 synthetic scope이며 pinned 계산은 명시적 실행 옵션으로 구분한다. 이 옵션은 별도의 과학적 admission을 만들지 않는다.

결과와 plan은 create-only다. 완료된 동일 task를 다시 사용할 때만 `--resume`을 지정한다. 입력/소스/task identity가 다르거나 이전 결과가 inconclusive이면 거부한다. 실패한 작업은 새 output 경로로 새 시도를 기록한다. 소스가 바뀌면 기존 plan도 무효다.

```bash
python -B ABS_NEW/endpoint_tasks/planner.py collect \
  --plan ABS_PLAN_JSON --npz ABS_FROZEN107_NPZ \
  --results ABS_RESULT_0 ABS_RESULT_1 --output ABS_NEW_COVERAGE_JSON
```

2592개의 고유한 성공 결과가 모두 있어야 `COMPLETE_CONDITIONAL_ENDPOINT_COVERAGE`다. 부분 목록은 누락된 index를 기록한다. 중복/혼합 신원은 거부한다. 목록과 코드 검사를 통과해도 endpoint-only 조건부 결과다.

## 자원 및 증거 경계

`run_task`는 별도 프로세스에 주소공간 RLIMIT_AS, CPU limit, 전체 hard wall deadline을 적용한다. 기본값은 30초/512MiB이고 최댓값은 300초/2GiB다. `evaluate_task` 직접 호출은 cooperative wall/engine-call/result-bit 제한만 제공하므로 hard cap이 필요한 실제 실행에는 `run_task`를 사용한다. 환경에서 내부 thread 수를 1로 제한한다. HOME은 변경하지 않는다. 시간 측정에는 monotonic clock을 사용하며 수치 계산에 host float를 사용하지 않는다.

`CONDITIONAL_TAIL_BOUND`만 반지름을 가진다. 자원 소진은 `INCONCLUSIVE_RESOURCE_LIMIT`, 실행 불일치는 `INCONCLUSIVE_EXECUTION`이고 반지름은 null이다. worker가 요청과 다른 task 결과를 반환하면 거부한다. 요청 tolerance나 타임아웃 결과를 상계로 대체하지 않는다.

`validate_result`는 입력/작업/소스 결합, 기록 hash, term 순서, 비음수 보고값과 곱·합 산술을 검증한다. 보고된 C_F와 mass bound를 원래 engine으로 독립 재계산하지 않는다. 따라서 그 값을 바꾸고 self-hash를 다시 만든 문서는 수학적 bound의 독립 증명이 될 수 없다. 재개/수집 결과의 신뢰는 실제 관찰된 engine 실행 증거에 조건부다. 이를 명시하는 두 필드는 native join에서도 유지해야 한다.

- `evidence_contract=SOURCE_BOUND_ENGINE_OUTPUT_ASSUMED_NOT_INDEPENDENTLY_REPLAYED`
- `validation_level=IDENTITY_AND_REPORTED_ARITHMETIC_ONLY`

모든 결과의 `scientific_admission=false`다. 완성된 endpoint 목록만으로 실제 interior, 전체 D, raw ABI, 최종 epsilon/Pareto 또는 독립 과학 review를 인증하지 않는다.

## 검증

`python -B -m unittest -v test_endpoint_tasks.py`는 생성된 binary64 toy NPZ만 사용한다. 실제 Frozen107 bytes/values를 읽지 않는다. 초기 누락 구현 RED, worker 자원 상태/잘못된 task 결과의 RED, dyadic 정책 누락 RED와 min-cap 누락 RED를 보존했다. 17개 테스트는 canonical geometry/index, 원래 exact source식 상계 포함, scaling의 명시적 rounding 범위, 복소 절댓값 상계, disjoint accounting, identity/coverage/refusal 및 hard-subprocess 재개 경계를 확인한다. quantizer 검사는 매우 작은/큰 스케일, 2의 거듭제곱 바로 전후, 비dyadic 유리수, 0/음수/float/work-cap을 검증한다. cap 검사는 두 질량 상계의 최솟값 논리와 synthetic large-T panel-width 증가 억제를 검증한다.

`cutoff_probe.py`는 같은 실제 primitive index 0에서 세 가지 고정 dyadic 구간만 탐색하는 별도 도구다. 기본은 plan-only이며 `--execute`일 때만 각 30초/512MiB, 총 90초 예산 안에서 실행한다. 해당 실제 실행 증거는 `runtime/endpoint_cutoff_probe*`에 따로 남기며 합성 테스트 결과와 섞지 않는다.
