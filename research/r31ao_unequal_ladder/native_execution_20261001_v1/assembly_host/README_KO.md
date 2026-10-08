# Guarded final-assembly host lifecycle

이 wrapper는 이미 존재하는 **2,592개 primitive coverage와 preparation**을 읽어 native assembly를 빌드하고, 제한된 subprocess로 실행한 후 exact final-D rectangle/disk를 반환한다. primitive를 계산하거나 누락된 coverage를 만들지 않는다. 실제 2,592개 HH 적분·endpoint 실행 또는 production certification을 완료했다고 주장하지 않는다.

기존 `production_solver_20261001_v1/primitive_join`와 native/Gram/입력·provenance 모듈 19개를 SHA로 고정하여 읽는다. 이전 파일은 수정하지 않는다. preparation의 compile argv를 그대로 신뢰해 실행하지 않고, source/header/compiler/prefix로부터 허용된 명령을 다시 만든다. strict flags와 immutable `assembly.cpp`의 합산 순서를 보존한다.

## 빌드와 실행

실제 host에서 기존 plan, native build, native task limits, coverage, preparation과 원 NPZ를 지정한다. 다음 SHA 중 preparation SHA는 `PREPARATION.json`의 raw file SHA가 아니라 compact/sorted canonical JSON SHA다. 다른 둘은 문서의 명명된 내부 digest다.

```bash
HOST=research/r31ao_unequal_ladder/native_execution_20261001_v1/assembly_host/assembly_host.py
python "$HOST" build \
  --plan "$PLAN" --native-build-directory "$NATIVE_BUILD" \
  --native-limits "$NATIVE_LIMITS" --coverage "$COVERAGE" \
  --preparation "$PREPARATION_DIR" --input-npz "$NPZ" \
  --native-build-sha256 "$NATIVE_BUILD_SHA" --coverage-sha256 "$COVERAGE_SHA" \
  --preparation-sha256 "$PREPARATION_CANONICAL_SHA" \
  --output-directory "$NEW_ASSEMBLY_BUILD"

python "$HOST" run --build-directory "$NEW_ASSEMBLY_BUILD" \
  --build-sha256 "$ASSEMBLY_BUILD_SHA" --output-directory "$NEW_ASSEMBLY_RUN"
```

build는 `BUILD.json`을 만들고 그 `build_sha256`을 stdout에 반환한다. run은 `FINAL_D_RECTANGLES.json`, `FINAL_D_DISKS.json`, `RUN.json`과 원 native stdout/stderr, linkage 기록을 만든다. `FINAL_D_DISKS.json`의 `target_disks`는 기존 composition 입력 필드와 동일한 envelope다. raw/model matrix는 별도로 정확히 제공해야 한다.

새 output directory는 원자적인 `mkdir(exist_ok=False)`로 먼저 확보한다. 같은 경로에서 중복 빌드·실행하지 않으며 실패 후 그 directory를 자동 재사용하지 않는다. 모든 실패에는 가능한 경우 `FAILURE.json`을 남기고, child 실패의 argv·limit·elapsed·exit·timeout·log identity를 보존한다. return code나 partial stdout만으로 성공 파일을 만들지 않는다.

## 실행 제한과 identity

`--limits-json`은 해당 단계의 모든 key를 요구한다. build 기본값은 `{"wall_seconds":300,"memory_mib":4096,"file_bytes":67108864}`이다. run 기본값은 `{"wall_seconds":60,"memory_mib":2048,"file_bytes":16777216,"precision_bits":128}`이다. hard cap은 wall 3,600 s, memory 8 GiB, 파일당 64 MiB, precision 32…4096이다.

subprocess는 shell 없이 argv로 실행한다. process group에 wall deadline을 적용하고 RLIMIT_AS/RLIMIT_FSIZE를 설정하며 core dump를 막는다. 단일 thread 환경을 사용한다. native primitive 계산의 MPI 병렬화와 별개인 최종 assembly 단계다. 원래 normalization·conjugation·sum order를 바꾸지 않는다.

빌드 전후에는 exact input/coverage/preparation, 3개 generated header, compiler, backend source/log/binary provenance를 다시 검사한다. build manifest는 wrapper/dependency/source, 생성 header, ELF binary와 실제 linkage를 묶는다. run은 binary, source, header, backend 및 system-library linkage의 일치를 확인하고 요청 precision과 실제 exporter precision의 일치도 검사한다. 출력 shape는 D_col 47×2, D_row 2×47이며 잘못된 key, nonfinite/float token, reversed interval, 다른 input/coverage identity를 거부한다.

파일 identity는 즉시 실행 경계에서 확인한다. host filesystem이 검사와 실행 사이에 안정적이라는 가정과 기존 provenance gate의 한계는 남는다. 공급된 기록의 byte chain 검증은 독립적으로 목격된 과거 빌드나 historical ABI 인증과 다르다.

## 수정된 native worker overlay

기본값은 이전 고정 native driver다. additive fixed-worker가 필요하면 build에 `--driver-module <repo 안의 driver.py> --driver-sha256 <실제 SHA>`를 명시한다. override는 기존과 같은 `FLAGS`, `DEFAULT_LIMITS`, `source_identity`, `limits_checked`, `dyadic_interval` 인터페이스를 제공해야 한다.

**새 worker coverage도 동일하게 설정한 Context로 생성해야 한다.** 기존 join CLI는 이전 driver로 고정되어 있으므로 새 build manifest와 혼합하지 않는다. Python에서 `configured_modules(path, sha)`로 `(join, gate, override)`를 얻고 `configured_context(join, plan, manifest, limits, archive_bytes, override)`를 사용한 뒤 해당 `join.join_task`, `join.collect`, `join.prepare_assembly`를 호출한다. 이 Context는 override의 path/size/hash를 execution identity에 추가한다. 이후 run은 guarded build manifest에 저장된 동일한 override를 다시 확인한다.

## 검증과 claim ceiling

`python -B -m unittest -v test_assembly_host`는 실제 Python subprocess로 wall/file/address-space 제한과 create-only 거절을 검사하며, 합성 자료로 preparation/header/argv/coverage/output contract를 검사한다. authority fixture의 compiler/backend provenance는 명시적으로 mock되어 있어 native build의 증거가 아니다. 과거 scientific suite는 재실행하지 않는다.

출력은 계속 조건부다. 공급된 endpoint/native 결과의 독립 replay, continuous-target enclosure premise, historical ABI, 원 floating predicate 및 independent decision review는 이 wrapper가 승인하지 않는다. 과학/production admission은 어떠한 입력으로도 true가 되지 않는다. 실제 native 컴파일·실행 여부는 향후 host BUILD/RUN의 실제 성공 기록으로 따로 판단한다.
