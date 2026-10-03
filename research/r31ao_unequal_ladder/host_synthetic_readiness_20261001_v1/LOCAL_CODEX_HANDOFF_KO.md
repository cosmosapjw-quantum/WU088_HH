# WU088 HH: 오프라인 native 합성 실행과 historical ABI 증거 반환

이 문서와 ZIP은 `HOST_SYNTHETIC_READINESS_20261001_V1`의 로컬 실행 인계다.
게시된 정확한 commit/tree와 ZIP/provider identity는 함께 전달한
`DELIVERY_RETURN.json`을 따른다. 시작 HEAD는
`7e9a2ac73f694450d4dd1e95b201d50bace8f25f`다.

목표는 고정 backend를 새 sidecar에서 실제 빌드하고, 이미 작성된 callback 및
Petras 합성 executable 두 개를 실행해 증거를 반환하는 것이다. 실제 HH 입력,
상수, 적분, archived raw gap 또는 certificate 실행 승인은 포함하지 않는다.
다음 절차를 완료할 수 있는 범위까지 수행하고 실제 도구/역사적 자료 부재만
정확히 분류하라. 같은 preflight나 성공한 검증을 이유 없이 반복하지 않는다.

## 패키지와 계획

ZIP을 새로운 디렉터리에 해제한다. 구조는 `research/`와
`backend_sources/`를 포함한다. 세 archive는 이미 확보된 원본이며 공개 Git
tree에는 포함하지 않았다. source/기존 코드 변경 없이 실행해야 한다.

압축을 해제한 최상위에서 다음 명령을 실행한다. 예시 출력 경로는 이 디렉터리
바깥의 존재하는 부모 아래 새 경로로 선택해도 된다.

```bash
python3 research/r31ao_unequal_ladder/host_synthetic_readiness_20261001_v1/backend_runner.py \
  --source-dir "$PWD/backend_sources" \
  --output "$PWD/wu088_backend_run_20261001_v1"
```

기본 명령은 계획만 출력하며 output 디렉터리를 만들지 않는다. 입력 archive
SHA/크기 및 이전 코드 56개 잠금이 모두 맞아야 한다. Linux GCC/G++, make,
pkg-config, m4, autoconf/autoreconf, automake, libtoolize 등이 필요하다.
누락되면 `missing_tools`와 실제 환경 정보를 보존한다. runner는 네트워크
다운로드, 패키지 자동 설치, sudo, 기존 runtime 교체를 하지 않는다.

## 실제 host synthetic build

계획이 준비됐으면 같은 output 경로에 다음을 한 번 실행한다.

```bash
python3 research/r31ao_unequal_ladder/host_synthetic_readiness_20261001_v1/backend_runner.py \
  --source-dir "$PWD/backend_sources" \
  --output "$PWD/wu088_backend_run_20261001_v1" \
  --execute-host-synthetic
```

순서는 GMP 6.3.0 → MPFR 4.2.2 → FLINT 3.4.0 → callback fixture → Petras
fixture다. source archives를 바꾸거나 버전을 자동 업그레이드하지 않는다.
`make -j2`, 전체 wall 10,800초, 프로세스당 address space 4 GiB, 단계별 cap은
`BACKEND_PLAN.json`과 같다. 이는 전체 process-tree RAM 제한이 아니다.
정해진 cap을 자동 확대하거나 실패한 directory를 재사용하지 않는다.

`HOST_RESULT.json`, `PREFLIGHT.json`, `BACKEND_BUILD_PROVENANCE.json`, 모든
stage receipt/stdout/stderr, 실제 linked-library identity, native binary SHA,
두 synthetic process receipt를 반환한다. 실패하면 실패 전 evidence를
보존하고 `IMPLEMENTATION`, `RUNTIME_ENVIRONMENT`, `RESOURCE_LIMIT`,
`EVIDENCE_AUTHORITY`를 구분한다. 입력/소스 변경이 없는 동일 명령의 무한
재시도는 하지 않는다. 원 code의 재현 가능한 구현 결함은 별도 새 overlay에서
수정하고 old source/RED evidence를 보존하며 변경 후 합성 검증을 수행하라.

Backend build 성공이나 fixture PASS를 actual HH feasibility, continuous
target enclosure 또는 historical NumPy admission으로 승격하지 않는다.
`rigorous=false`, ε/η=null을 유지한다. 실제 G7는 기존 미승인 scope를 별도로
완성·검토하기 전까지 실행하지 않는다.

## Historical ABI evidence

`README_ABI_KO.md`와 `ABI_EVIDENCE_RETURN.json`을 읽는다. R31AL 당시 기록은
NumPy 2.3.5 및 longdouble 16바이트/64-bit significand를 지지하지만, 과거
extension/config 바이너리와 B192 output을 연결하는 근거는 아직 없다.

현재 호스트에서 새로 만든 동일 버전 venv를 과거 환경이라고 부르지 않는다.
원래 보존된 Python/NumPy 실행 환경이 실제로 발견되면 그 실행 파일 경로로
아래 `python3` 두 곳을 바꾼다. 두 output 디렉터리는 새 경로여야 한다.

```bash
python3 -B research/r31ao_unequal_ladder/gap_closure_20261001_g0_g6_v1/host_guard/run_guarded.py \
  --wall-seconds 20 --memory-mib 1024 \
  --output-dir "$PWD/wu088_abi_guard_20261001_v1" -- \
  python3 -B research/r31ao_unequal_ladder/host_synthetic_readiness_20261001_v1/abi_witness.py \
  --output-dir "$PWD/wu088_abi_witness_20261001_v1"
```

이 수집기는 고정 합성 NPY만 생성한다. 실제 HH 배열 입력 옵션은 없다.
과거 환경이 없으면 current witness는 현재 진단일 뿐이다. historical link
manifest는 참조의 형식만 검사하며 모든 경우 admission=false다. 과거 파일의
보존 경로·시점·실제 내용과 serializer→output 연결을 별도 검토한 evidence가
없으면 B03은 `RAW_ABI_AUTHORITY_BLOCKED`로 반환한다.

## 보존·게시·반환

R31AK, z=0.75 holdout, B128/B160 consumed authorization, B192 reuse-only,
기존 finite-order verdict와 source-accuracy blocker를 보존한다. source mutation,
actual HH evaluation, native build/run 횟수를 별도로 기록한다.

Code/report/receipt만 같은 `research/r31ao-unequal-order-ladder-20260930`
브랜치에 ordinary non-force 게시한다. 새 branch·force·merge/rebase·main 변경은
없다. 제3자 원 archive·native binary·large object files를 공개 Git에 올리지 않는다.
중요한 host 결과는 원 archive와 hash로 연결된 로그·설치 shared libraries·native
fixture binaries 중심의 새 패키지로 보존한다. build object tree는 과학 결과가 아니다.

기존 Google Drive parent `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM` 및 Dropbox
`/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928`
에 create-only 이중 백업한다. 연결 수단이 없다면 로컬 결과를 보존하고 미전송을
명시한다. 실제 provider ACK·ID·경로·metadata size가 확인되기 전 백업 성공을
주장하지 않는다. 실제 복원 검증 전에는 `RESTORE_VERIFIED=false`다.

반환에는 최소 START/END_HEAD, TREE, 실제 명령·exit·로그, archive/compiler/
binary/linked-library SHA, fixture 결과, ABI linkage 상태, 발견·수정한 결함,
actual_HH_count, scientific gates, backup receipts와 다음 최소 조치를 포함한다.
