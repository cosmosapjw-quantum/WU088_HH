# Primitive join → native assembly → final disk

이 부품은 compact interior rectangle과 그 보완 영역의 endpoint disk를 결합하고, 2,592개 primitive의 완전한 coverage를 native assembly에 연결한다. Python 조합·거부·coverage·disk 변환은 합성 자료로 검사했다. `assembly_exporter.cpp`는 **컴파일·실행하지 않은 native 후보**다. HH 과학 결과, 실제 endpoint/native 실행, 독립 enclosure proof 또는 production admission으로 승격하지 않는다.

primitive index는 `((((active*3+field)*3+orbital)*12+ia)*12+ib)`이며 모든 0…2591이 한 번씩 필요하다. 해당 index의 `UNNORMALIZED_POSITIVE_DOMAIN_ENDPOINT_ONLY` bound B는 `(outside_t × all_u) ∪ (inside_t × outside_u)`에 대한 하나의 합계다. interior `[x-,x+]+i[y-,y+]`에 **한 번만** B를 더해 `[x--B,x++B]+i[y--B,y++B]`를 만든다. normalization·phase·contraction·conjugation은 이전 immutable `assemble_real_domain`에서만 수행한다.

## Python API

- `Context(endpoint_plan, native_BUILD, native_limits, source_archive_bytes=...)`: endpoint plan 및 exact input, 현재 source pins, native build manifest, backend/binary/limits identity를 결합한다. pinned scientific plan은 원 archive bytes가 필요하다.
- `join_task(context, endpoint_result, persisted_native_result)`: 각 upstream validator, hash, index, window, command와 실행 제한을 검사한다. wrapper 없는 worker stdout, failed caps, 이미 endpoint/normalization이 적용된 결과를 거절한다.
- `collect(context, iterable_of_joined_results)`: 순서와 무관하게 모든 primitive를 요구하고 canonical order로 정렬한다. 중복·누락·혼합 실행 identity는 오류다.
- `initializer(coverage)`: 2,592 acb slot 각각에 exact rational midpoint/radius를 넣는 C++ header를 만든다. `arb_set_fmpq`의 outward rounding과 `arb_add_error`로 보존하며 decimal floating conversion은 없다.
- `prepare_assembly(context, coverage, native_build_directory, new_directory)`: 이전 native BUILD의 generated input header SHA와 identity header bytes를 확인하고 header 3개, compile argv를 포함한 `PREPARATION.json`을 만든다. 컴파일은 수행하지 않는다.
- `import_final_disks(context, coverage, final_D_rectangles, precision=128)`: native D_col47×2/D_row2×47 rectangle을 midpoint와 `sqrt(hx²+hy²)`의 outward upper radius를 가진 disk로 바꾼다. 반환 `target_disks` envelope를 composition request의 동명 필드에 넣는다. 별도의 exact raw/model 입력은 그대로 필요하다.

모든 rational 값은 기약 Fraction string이고 최대 8,192 integer bits다. 이는 upstream이 허용하는 일부 더 큰 표현을 의도적으로 거부하는 하위 component cap이다. 오차 tolerance를 느슨하게 하거나 precision을 낮추어 통과시키지 않는다. JSON은 최대 32 MiB이며 duplicate key, float, NaN을 거절한다. 출력은 create-only다. 과학 데이터 생성·archive 해석을 이 모듈이 대신 인증하지 않는다.

## Host CLI

다음 경로 변수는 이미 검증된 host 산출물에 지정한다. `COMMON`의 NPZ는 기존 input record와 동일한 archive이어야 한다.

```bash
JOIN=research/r31ao_unequal_ladder/production_solver_20261001_v1/primitive_join/join.py
COMMON=(--plan "$PLAN" --build-manifest "$NATIVE_BUILD/BUILD.json" --limits "$LIMITS" --npz "$NPZ")
python "$JOIN" join "${COMMON[@]}" --endpoint-result "$TAIL_RESULT" \
  --interior-result "$INTERIOR_RESULT" --output "$JOINED_RESULT"
python "$JOIN" collect "${COMMON[@]}" --joined-list "$PATHS_2592_JSON" \
  --output "$COVERAGE"
python "$JOIN" prepare "${COMMON[@]}" --coverage "$COVERAGE" \
  --build-directory "$NATIVE_BUILD" --output "$NEW_ASSEMBLY_DIRECTORY"
```

`PATHS_2592_JSON`은 실제 joined 결과 파일 경로 2,592개의 JSON list다. prepare 결과의 `compile_command`는 pinned FLINT prefix와 strict compiler flags를 사용하는 argv list다. host 실행기는 prefix provenance/linkage와 compiler identity를 native_driver와 같은 방식으로 다시 확인하고, 그 argv를 shell 재해석 없이 실행하며, binary/source/header hash 및 실제 exit/log를 기록해야 한다. 이 host build/run lifecycle의 자동 wrapper는 이 부품에서 구현하지 않았다.

native 후보는 `assembly_exporter 128`로 입력되어 전체 final D rectangle을 단일 stdout JSON으로 반환한다. 이전 `build_identity.hpp`의 archive/record identity와 primitive header의 identity가 다르면 실행 전에 거절한다. 그럼에도 generated header의 임의 교체를 막으려면 prepare의 hash 확인과 compile manifest를 보존해야 한다. 실행 시간·메모리 cap은 host runner가 제공해야 한다.

```bash
python "$JOIN" import "${COMMON[@]}" --coverage "$COVERAGE" \
  --final-rectangles "$NATIVE_FINAL_D_JSON" --precision 128 --output "$FINAL_DISKS_JSON"
```

final import는 endpoint와 native의 `SOURCE_BOUND_*_OUTPUT_ASSUMED_NOT_INDEPENDENTLY_REPLAYED` 조건을 모두 계승한다. 출력 hash나 wrapper의 실행 관측 필드는 실행 증거의 독립 검토를 대체하지 않는다. 원 historical ABI, source functional/domain, target disk proof, frozen machine predicate, 독립 decision review 및 production gate는 이 코드로 자동 닫히지 않는다.
