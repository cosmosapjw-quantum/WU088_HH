# 정확한 log2 좌표의 bounded native driver

기존 `native_execution_20261001_v1/refined_native_driver`에서 실행 API를 계승한 additive 구현이다. 기존 callback, cache, donor 순서, Frozen107 입력, Petras host와 endpoint planner는 SHA로 고정하며 수정하지 않는다. 기본 callback은 cached이고 baseline을 명시할 수도 있다. 기존 build manifest로 새 driver를 실행할 수 없다.

물리적 적분창은 원래 plan/task identity를 유지한다. Python과 C++에서 모두 양의 정확한 2의 정수승인 정규 유리수 endpoint만 허용하며, 반올림 없이 signed integer log endpoint를 만든다. `t=exp(x log 2)`, `u=exp(y log 2)`를 전체 복소 ball에 적용하고 원 callback 결과에 `(log 2)^2 t u`를 outward 곱한다. 전체 outer parameter image를 넘기며 midpoint 대입이나 양의 부분으로 clipping하지 않는다. FLINT order 1은 Taylor derivative 요구가 아니라 값과 해석성 요구이므로 원 callback의 order를 그대로 넘긴다. 기존 positivity guard와 물리적 endpoint에 따른 margin을 유지한다.

원래 128-bit precision, `2^-48` achieved component radius 및 shared 자원예산을 바꾸지 않았다. 큰 box가 거절되거나 실제 적분이 비수렴할 수 있다. 특히 W3의 200-bit 동적 범위에서는 exponential image의 직사각 ball이 양의 작은 endpoint를 보존하지 못할 수 있으므로 log 치환만으로 full-window 성공을 주장하지 않는다. 동일 shared budget의 소진은 fatal이며 자동 reset/retry하지 않는다.

`driver.py build`와 `run`의 명령행은 이전 driver와 같고 callback 기본값만 cached다. 결과 schema는 `WU088_LOG2_NATIVE_INTERIOR_RESULT_V1`, build schema는 `WU088_LOG2_NATIVE_DRIVER_BUILD_V1`이다. native 결과는 `coordinate_map=LOG2_EXACT_POWER_ENDPOINTS_V1`을 포함한다. wrapper는 physical/log window, source/build/binary/backend/command identity와 process 시작부터 종료까지의 `elapsed_wall_ns`를 저장한다. 실패한 native 실행에도 같은 binding과 stdout/stderr를 남긴다. 이 시간은 build나 provenance 검증을 포함하지 않는다.

검증 범위:

- Python boundary 22개: exact endpoints, scope/identity/radius, create-only claim, 캐시 build, 실패/잘못된 JSON/launch 실패 receipt.
- 실제 pinned FLINT/GMP/MPFR에 링크한 synthetic native 7개 검사: 정확한 endpoint와 잘못된 endpoint 거절, 비대칭 창 `[1/4,4]×[1/2,8]`의 `t+2u` 적분이 정확한 `19125/64` 포함, `[1,2]^2`의 `1/(tu)` 적분이 별도 log oracle과 겹침, 전체 outer box 보존, 큰 허수 입력의 domain 거절, shared budget 소진의 fatal 처리.
- 넓은 비대칭 창의 `1/(tu)` synthetic 적분은 20,000회 예산을 소진했다. 실패한 attempt 1/2를 보존했고, attempt 3의 작은 창 검증을 넓은 창 성공으로 바꾸어 쓰지 않는다. 오차 허용치는 완화하지 않았다.

이 디렉터리의 synthetic 실행은 HH 평가 0회다. 실제 Frozen107 적분과 타일 coverage 검증은 별도 source-bound 실행 결과로 보고해야 한다. endpoint/normalization/full-domain/최종 D/scientific/production admission은 모두 별도 gate다.
