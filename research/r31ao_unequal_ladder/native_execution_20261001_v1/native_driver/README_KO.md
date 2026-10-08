# 추가 native primitive driver

이 디렉터리는 이전 `production_solver_20261001_v1/native_driver`를 보존한 채 추가한 실행 후보이다. 이전 파일 SHA와 복사 경로는 `SOURCE_ORIGIN.json`에 있다. 기본 API, `FLAGS`, `DEFAULT_LIMITS`, 인덱스, exact interval 출력과 조건부 결과 schema를 유지한다. 이전 build manifest/binary는 새 source identity로 재사용할 수 없다.

worker의 real-domain margin은 exact rational

`min(1,l_t,l_u,(1/(a+T_t)+1/(b+T_u))/2)/2^20`

이다. 큰 상한에서 sigma가 작아져 기존 lower-cutoff-only margin을 만족할 수 없던 문제를 해결한다. 값의 정의나 적분 tolerance는 변경하지 않으며 모든 complex box는 기존 callback domain guard를 그대로 통과해야 한다.

명시적인 두 build mode를 제공한다.

- `--callback-mode baseline`: 기본값. 기존 callback.cpp를 직접 컴파일한다.
- `--callback-mode cached`: 고정 `ncp64.../native_cache/cached_callback.cpp`를 대신 컴파일한다. 이 TU가 기존 callback.cpp를 포함하므로 callback.cpp를 별도로 중복 링크하지 않는다.

mode는 컴파일 옵션 `-DWU088_USE_CACHED=0/1`, build manifest의 `callback_mode`, `callback_mode_flags`, `callback_sources`, 실제 명령 및 binary SHA에 결합된다. 기존 정확한 helper 식, 계수 곱셈 트리와 합산 순서는 캐시 TU가 보존한다. CachedSlice bridge는 전체 outer complex box를 넘기며 midpoint로 바꾸지 않는다. cache lifetime은 단일 callback 호출이며 FLINT thread 수는 1이다. 캐시 사용은 실제 72-case equality gate 및 관련 독립 검토 통과 후 root가 선택한다. 이 문서나 build option이 그 검증을 대신하지 않는다.

```bash
python -B ABS_NEW/native_driver/driver.py build \
  --input-npz ABS_FROZEN107_NPZ --flint-prefix ABS_SIDECAR_PREFIX \
  --backend-provenance ABS_BACKEND_JSON --output-directory ABS_NEW_BUILD \
  --callback-mode baseline

python -B ABS_NEW/native_driver/driver.py run \
  --input-npz ABS_FROZEN107_NPZ \
  --plan ABS_NEW/runtime/pilot_plans/CENTRAL_PLAN.json \
  --plan-sha256 EXACT_PLAN_SHA --task-index 0 \
  --build-directory ABS_NEW_BUILD --build-sha256 EXACT_BUILD_MANIFEST_SHA \
  --limits-json ABS_NEW/runtime/pilot_plans/CENTRAL_LIMITS.json \
  --output ABS_NEW_INTERIOR_RESULT
```

결과가 성공해도 endpoint 미포함 compact-interior 결과다. `assembly_host`에서 새 driver 모듈의 경로와 SHA를 명시해 Context를 구성해야 한다. 이전 join CLI는 이전 driver source를 기본값으로 사용하므로 새 build를 그대로 승인하지 않는다.

작은 실제 pilot은 `[1,2]^2`, 필요 시 사전 지정한 `[1,257/256]^2`이며 128-bit, component radius2^-48, goal64를 유지한다. 거대한 W3 전체를 단일 적분으로 실행하는 것은 권장하지 않는다. margin 외의 broad-ball/refinable-refusal 문제와 tiling 계약은 `../interior_design/INTERIOR_FEASIBILITY.md`에 정리했다.

`python -B -m unittest -v test_driver.py`는 16개 Python/정확 산술 boundary 테스트다. native compile/runtime 성공을 주장하지 않는다. 실제 build/run과 cache equality evidence는 root가 별도로 기록한다.
