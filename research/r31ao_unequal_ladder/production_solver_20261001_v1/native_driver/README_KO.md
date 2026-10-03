# Frozen107 compact-interior native worker

이 모듈은 고정된 2,592개 primitive 중 하나를 실제 Frozen107 입력에서 구성하고, 기존 FLINT/Arb nested Petras 적분기로 양의 유한 직사각형을 적분하는 실행 경로다. `active → field → orbital → ia → ib` 순서를 유지한다. 내부 적분 변수는 t, 외부 변수는 u다. 원래 callback, donor 계수 순서, 정규화와 assembly 코드는 수정하지 않는다.

현재 검증은 Python 경계 검사와 실제 Frozen107 입력의 정확한 C++ initializer 생성까지다. 이 환경에는 pinned FLINT/GMP/MPFR 개발 환경이 없어 **native 컴파일·적분은 실행하지 않았다**. `verification/VERIFICATION.json`과 `verification/PREFLIGHT.json`에 구분해 기록했다. 정확한 직사각형 결과가 실행되더라도 endpoint, contraction, 전체 D 인증, historical ABI, 독립 심사와 production admission은 별도다.

endpoint planner의 엄밀한 상향 dyadic 양자화 정책 도입 후 dependency pin을 갱신하고 11개 경계 테스트를 다시 실행했다. 해당 단계의 source identity와 결과는 `verification/POST_QUANTIZER_VERIFICATION.json`에 있으며 이전 pin·검증 증거는 별도로 보존했다. native worker 및 wrapper API는 변경하지 않았다.

최종적으로 endpoint의 양의 t 내부 질량 상계를 전구간 질량 상계로 제한하는 정책을 반영했다. 현재 source identity와 마지막 11개 경계 테스트 결과는 `verification/POST_WHOLE_AXIS_CAP_VERIFICATION.json`이다. 앞의 두 검증 기록과 pin은 당시 상태의 이력으로 보존한다.

## 빌드와 한 primitive 실행

기존 `host_synthetic_readiness_20261001_v1/backend_runner.py`가 만든 FLINT 3.4.0 / GMP 6.3.0 / MPFR 4.2.2 sidecar와 그 provenance record가 필요하다. 이 모듈은 라이브러리를 설치하거나 기존 runtime을 교체하지 않는다. 아래 경로·SHA 값은 실제 출력값으로 지정한다.

```bash
python native_driver/driver.py preflight \
  --flint-prefix /absolute/pinned/prefix \
  --backend-provenance /absolute/BUILD_PROVENANCE.json

python native_driver/driver.py build \
  --input-npz /absolute/FROZEN_INPUTS.npz \
  --flint-prefix /absolute/pinned/prefix \
  --backend-provenance /absolute/BUILD_PROVENANCE.json \
  --output-directory /absolute/new-native-build

python native_driver/driver.py run \
  --input-npz /absolute/FROZEN_INPUTS.npz \
  --plan /absolute/endpoint-plan.json --plan-sha256 ACTUAL_PLAN_SHA256 \
  --task-index 0 \
  --build-directory /absolute/new-native-build --build-sha256 ACTUAL_BUILD_MANIFEST_SHA256 \
  --output /absolute/new-results/interior-0000.json
```

명령은 `production_solver_20261001_v1`에서 실행한다. PLAN은 `endpoint_tasks/planner.py`가 같은 NPZ로 만든 `FROZEN107_PINNED` plan이어야 한다. build manifest 내부의 `manifest_sha256`이 `--build-sha256` 값이다. 출력 부모 디렉터리는 미리 준비한다. 생성물은 create-only이며, 기존 결과를 발견하면 native 실행 전에 거절한다. 원자적 `.claim` 파일은 같은 출력의 동시 재실행을 막는다. 비정상 종료 후 남은 claim은 조사 후 처리하며 자동으로 지우지 않는다.

기본 worker는 128-bit Arb precision, 성분 반경 ≤2^-48, 총 callback dispatch 20,000회, 적분 호출 1,024회, 협력식 wall 30초, 외부 강제 종료 35초, 주소 공간 1GiB다. 한 worker의 FLINT thread는 1개다. `--limits-json`은 `driver.DEFAULT_LIMITS`와 같은 정확한 키 집합의 정수 JSON을 받는다. 반경 조건을 충족하지 못하면 정밀도/허용오차를 자동 변경하지 않고 거절한다. 내부 whole-parameter enclosure 반경은 outer integrator에 그대로 전달되며 최종 반환 성분 반경을 다시 검사한다.

기존 NCP MPI/Fortran dispatcher가 서로 다른 task index와 출력 경로의 위 `run` 명령들을 배분하면 된다. Python 프로세스 내부에서 MPI를 초기화하거나 Arb 공유 객체를 여러 thread로 호출하지 않는다. 동시에 실행하는 worker 수 × `memory_mib`를 host memory 예산에 맞추고 OS와 coordinator 여유를 남긴다. 64-core 성능이나 확장성은 아직 측정하지 않았다.

## 수치·증거 계약

- NPZ archive/member pin을 다시 확인하고 exact dyadic decoder로 생성한 initializer만 사용한다. task 파라미터나 donor 계수를 외부 임의 JSON으로 받아 native 입력으로 바꾸지 않는다.
- `task_sha256`와 `plan_sha256`은 입력, window, terms, source, endpoint 계획과 결합된다. Python wrapper가 선택 task를 검증하고 native 결과가 같은 identity를 반환하는지 검사한다.
- 결과의 `rectangle.real/imag`는 `lower_mantissa`, `upper_mantissa`, `exponent2` 정수 문자열로 `[lower, upper] × 2^exponent2`를 나타낸다. decimal floating 출력이나 midpoint-only 변환을 사용하지 않는다.
- FLINT `arb_get_interval_fmpz_2exp` 호출 전에 midpoint/radius exponent와 차이를 제한해 거대 정수 할당을 차단한다. 반환 후 정수 bit 수와 반경을 다시 확인한다. 유한하고 `RADIUS_MET`이며 모든 예산이 유지된 결과만 exit 0으로 반환한다.
- native 출력은 compact interior만 포함한다. endpoint 또는 Gaussian normalization은 포함하지 않는다. endpoint ±B를 정확히 한 번 결합한 뒤 2,592개 전체 coverage와 기존 `assemble_real_domain`을 확인해야 한다.
- build 시와 실행 직전에 기존 provenance gate로 pinned source archive, build log, 공유 라이브러리 bytes와 실제 linkage를 점검한다. 이 점검은 독립적으로 목격한 빌드나 수학적 실행 증명이 아니다. `scientific_admission`과 `production_admission`은 계속 false다.
- callback의 joint holomorphy 전제는 T1 문서와 callback의 whole-box positivity guard에 따른 source contract다. 실행 결과를 독립적으로 replay하지 않았으므로 wrapper의 evidence contract는 `SOURCE_BOUND_NATIVE_OUTPUT_ASSUMED_NOT_INDEPENDENTLY_REPLAYED`다.

FLINT 3.4.0의 실제 pinned source archive에서 endpoint/API 선언과 구현을 대조했다. API 의미를 확인한 공식 문서: https://flintlib.org/download/flint-3.4.0.pdf 및 https://flintlib.org/doc/arb.html. 현재 개발판 문서의 버전을 빌드 pin으로 대신하지 않는다.

```bash
python -m unittest discover -s native_driver -p 'test_driver.py' -v
```

이 테스트의 직사각형은 분석적으로 만든 boundary fixture다. HH 적분값 또는 native backend 실행 결과로 계산하지 않는다.
