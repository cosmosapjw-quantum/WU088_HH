# 현재 NumPy ABI 증거 수집기

`abi_witness.py`는 선택한 Python 실행 파일로 작은 합성 NPY 8개를 생성하고, 그 실행 환경과 직렬화 바이트의 정체성을 기록한다. 현재 환경 증거만 수집한다. 과거 B192 직렬화 ABI를 승인하거나 HH 데이터를 읽지 않는다. `B03=RAW_ABI_AUTHORITY_BLOCKED`, `historical_layout_admitted=false`는 모든 반환 경로에서 유지한다.

## 이번 실행 결과

- `evidence/abi/current_probe_final/WITNESS.json`: 현재 Python/NumPy 환경의 최종 증거. NumPy 2.3.5, little-endian, longdouble 16바이트/가수 64비트, complex longdouble 32바이트를 관측했다.
- binary64/complex128 및 longdouble/clongdouble 각각 C/F 순서, 총 8개의 2×4 행렬을 검증했다. +0, -0, 1, -2, 1+ULP, 최소 normal, 양·음 최소 subnormal을 포함한다. complex의 실수부와 허수부는 다른 순열을 사용한다.
- x87의 10 유효바이트+6 padding 바이트 후보가 **이번 합성 바이트**의 정확한 dyadic 값 및 signed zero와 일치했다. 원본 NPY/payload SHA256, mathematical SHA256, signed-zero, padding을 따로 보존한다. dtype 이름 `float128`/`complex256`만으로 binary128을 선택하지 않는다.
- NumPy `_format_impl.py` SHA256은 `cdc437c57c4f7fb7a992db18adc7416c83ee38287d38f575837801ea085fe2b1`이며 기존 C04 원문 pin과 같다. 이것은 현재 source 파일의 일치일 뿐, 과거 wheel/extension binary의 증명이 아니다.
- `GREEN_FINAL.log`: 14 tests, exit 0. `RED.log`: 구현 전 import 실패 exit 1. `RED_SERIALIZER.log`: public module alias만 해시하여 실제 serializer 소스를 놓친 회귀를 포착한 exit 1. 이후 실제 `co_filename`의 write_array/save 소스를 해시하도록 수정했다.
- `current_probe_final_guard/PROCESS_RECEIPT.json`: wall 20초, 프로세스당 address space 1024 MiB, child exit 0. native build와 실제 HH 실행/배열 접근은 0이다.

`current_probe/`, `current_probe_guard/`, `GREEN.log`, `GREEN_ATTEMPT_1.log`, `PROBE_COMMAND.json`은 수정 전 기록으로 보존한다. serializer 구현 소스 해시를 포함한 최종 실행은 이름에 `final`/`FINAL`이 있는 기록이다.

## 실행

기존 checkout의 새 loop 디렉터리에서, 조사하려는 환경의 Python을 명시적으로 선택한다. 원래 생산 환경을 재생성하거나 패키지를 설치하지 않는다. 아래 두 경로는 실행 때마다 존재하지 않는 새 디렉터리여야 한다.

```sh
/chosen/python -B ../gap_closure_20261001_g0_g6_v1/host_guard/run_guarded.py \
  --wall-seconds 20 --memory-mib 1024 --output-dir /existing/parent/abi_guard_new \
  -- /chosen/python -B abi_witness.py --output-dir /existing/parent/abi_witness_new
```

NumPy가 없거나 import에 실패하면 `NUMPY_UNAVAILABLE`, exit 2를 기록한다. 자동 설치/다운로드/컴파일은 없다. 지원하지 않는 metadata, byte layout 불일치, 파일/출력 예산 초과는 `PROBE_REFUSED_OR_UNSUPPORTED`, exit 2다. exit 0은 현재 합성 증거 수집 성공만 뜻한다. historical references가 없거나 잘못되어도 현재 수집과 별도로 blocker를 기록하며 B03은 닫히지 않는다.

NPY 원본 바이트는 Git 텍스트 전달을 위해 `.npy.hex`로 보존한다. `bytes.fromhex(Path(file).read_text('ascii'))`로 정확히 복원한다. 재구성한 바이트의 SHA256은 WITNESS의 `raw_npy_sha256`과 같아야 한다. 이는 값으로 NPY를 다시 만드는 작업이 아니며 header/padding/signed-zero까지 포함한다. mathematical dyadic 값은 큰 정수의 십진 문자열 제한을 피하도록 `numerator_hex / 2**denominator_power_of_two`로 기록한다.

```sh
/chosen/python -B -m unittest -v test_abi_witness
```

NumPy가 없는 환경에서는 현재 NumPy 의존 테스트가 SKIP된다. 따라서 unit test의 성공만으로 현재 probe 성공을 주장하지 말고 WITNESS의 status와 외부 guard의 child exit를 함께 확인한다.

## 수집 범위와 한계

실행 파일, Python sysconfig/source/header/Makefile, 구성상 존재하는 shared Python library, NumPy init/config, write_array/save의 실제 구현 source, 로드된 NumPy extension, 생성된 numpyconfig headers를 해시한다. `np.show_config()`와 dtype/finfo의 정수 metadata도 보존한다. 이 목록은 모든 OS 동적 의존 라이브러리의 실행 시 정체성 전체를 보증하지 않는다. 디스크에서 해시한 파일과 이미 메모리에 로드된 코드 사이의 불변성을 증명하지도 않는다.

내부 cap은 파일당 128 MiB, 총 해시 512 MiB/64파일, show_config 256 KiB, sentinel당 8 elements/4096 bytes, 전체 출력 2 MiB, cooperative wall 60초다. import나 NumPy 호출 내부에서 멈추면 내부 wall 검사를 실행할 수 없다. Python/NumPy 전체 메모리 사용에 대한 내부 hard cap도 없다. 그래서 별도 process guard가 필요하다. 기존 guard의 RLIMIT_AS는 **프로세스별 address space** 제한이고 aggregate process-tree RSS 제한은 아니다. collector는 자체 subprocess/network/native build를 실행하지 않는다.

finfo가 지지하는 후보를 선택한 뒤 exact Fraction oracle로 실제 생성 바이트를 비교한다. 이번 호스트는 little-endian x87/offset 0 후보에 해당했다. binary64와 IEEE binary128 후보 경로도 구현되어 있으나 이번 호스트에서 binary128 NumPy 실행을 관측한 것은 아니다. 기타 extended 형식은 거절한다. 기존 exact decoder와 RAW_ABI_AUTHORITY를 source SHA로 확인하여 사용하고 동결된 파일은 수정하지 않는다.

## 과거 linkage 문서

선택 사항인 `--historical-links /path/links.json`은 최대 64 KiB의 JSON metadata references만 받는다. NPY/NPZ 입력 인자나 HH loader는 없다. 최상위 필드는 정확히 다음 다섯 개다.

1. `schema`: `WU088_HISTORICAL_ABI_LINK_REFERENCES_V1`.
2. `producer_runtime`: `/root/WU088_R31AL_Z075_RUNTIME_20260930`.
3. `output_archive_sha256`: collector의 `OUTPUT_PINS`와 일치하는 OD/JVP 기록.
4. `producer_source_sha256`: collector의 `PRODUCER_PINS`와 일치하는 OD/JVP run/native source 기록.
5. `references`: 아래 역할을 모두 포함하는 4~16개 참조.

각 참조는 `role`, `uri`(최대 2048자 HTTPS), `sha256`, `origin=INDEPENDENT_HISTORICAL_RECORD`만 갖는다. 필요한 역할은 `contemporaneous_environment`, `preserved_numpy_binary_chain`, `serializer_to_output_binding`, `layout_capture_under_identified_runtime`다. URI의 내용을 이 수집기가 가져오거나 독립성을 확인하는 것은 아니다. current probe의 자기 해시와 `verified: true` 같은 boolean은 linkage로 인정하지 않는다.

구조가 완전해도 `REFERENCES_STRUCTURALLY_COMPLETE_REVIEW_REQUIRED`, `reference_contents_verified=false`, B03 blocked다. 기록의 실제 내용/시점/보존 경로와 원래 output 정체성을 독립 검토한 별도 project admission이 필요하다. 이 수집기에는 admission을 true로 바꾸는 기능이 없다. 실제 NPY-member binding과 HH decode는 이 작업 범위 밖이다.

## 좁힌 과거 텍스트 조사

`evidence/abi/HISTORICAL_TEXT_SEARCH.json`은 시작 commit `7e9a2ac73f694450d4dd1e95b201d50bace8f25f`에 고정한 R31AL ENVIRONMENT, PRE_OUTPUT_LOCK, PRE_OUTPUT_RUNTIME_INVENTORY 원문 3개를 Git blob SHA와 SHA256으로 결박한다. ENVIRONMENT는 원래 runtime/Python 경로, NumPy 2.3.5, longdouble 16바이트/64-bit significand를 함께 기록한다. PRE_OUTPUT_LOCK은 producer run/native source 해시와 실행 경로를 기록한다. 이것은 dtype 헤더만보다 강한 단서이지만 exact NumPy extension/config binary와 해당 serializer가 B192 outputs를 썼다는 완전한 linkage는 아니다. 실제 scientific 배열은 읽지 않았다.
