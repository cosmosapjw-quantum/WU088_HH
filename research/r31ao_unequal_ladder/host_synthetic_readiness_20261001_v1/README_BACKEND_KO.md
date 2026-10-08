# 고정 backend의 오프라인 호스트 합성 실행

`backend_runner.py`는 GMP 6.3.0 → MPFR 4.2.2 → FLINT 3.4.0을 새 sidecar에 설치한 뒤, 기존 callback 및 Petras 합성 실행 파일 두 개를 빌드·검사·실행한다. 기본 동작은 계획 출력이다. 이 채팅 환경에서는 소스 추출과 Python 합성 경계 테스트만 수행했다. **라이브러리 빌드와 native 실행은 아직 검증되지 않았다.**

실제 Frozen107 또는 HH 입력 파일을 받는 옵션은 없다. 기존 scientific runtime, 이전 G0–G6 코드, 과학 배열을 수정하지 않는다. 호스트 합성 테스트가 성공해도 historical ABI, 실제 HH 적분, ε/η 또는 scientific admission을 승인하지 않는다.

## 실행

전체 저장소 overlay와 비공개 `backend_sources` 폴더를 같은 호스트에 복원한다. source 폴더에는 원래 바이트의 `C09.tar.xz`(GMP), `C08.tar.xz`(MPFR), `C01.tar.gz`(FLINT) 세 파일이 필요하다. 인터넷 접속과 패키지 설치는 runner에 없다.

```bash
python3 backend_runner.py \
  --source-dir /absolute/backend_sources \
  --output /absolute/work/wu088_backend_new
```

이 명령은 소스 SHA/크기, 이전 코드의 `INPUT_LOCK.json`, 필수 실행 파일의 존재와 identity를 확인하고 JSON 계획을 출력한다. 출력 디렉터리를 만들거나 compiler/version/configure/native 명령을 실행하지 않는다. `missing_tools`가 비어 있는지 확인한다. 필수 도구는 Linux의 GCC/G++, GNU make, sh/bash, Python 3, pkg-config, ldd, sha256sum, m4, autoconf/autoreconf, automake, libtoolize다. FLINT 원본이 release configure를 포함하지 않는 Git archive이므로 bootstrap 도구가 필요하다. 이 환경에서 관측한 누락 목록은 `evidence/backend/PLAN_ONLY_OBSERVED.json`에 보존했다.

로컬 호스트에서 명시적으로 실행할 때만 다음 옵션을 추가한다.

```bash
python3 backend_runner.py \
  --source-dir /absolute/backend_sources \
  --output /absolute/work/wu088_backend_new \
  --execute-host-synthetic
```

`--output`은 존재하지 않는 절대 경로여야 하고 부모 디렉터리는 존재해야 한다. upstream configure/make의 경로 처리 때문에 공백·쉘 메타문자가 있는 경로는 거부한다. 기존 출력 재사용·덮어쓰기·자동 재시도는 없다. 실패한 출력과 로그는 남기고 중단한다.

## 소스 및 실행 순서

핀과 기본 한도는 `BACKEND_PLAN.json`에 기록했다. 실행 코드는 같은 상수를 내장하며 외부 JSON이 임의 명령이나 flags를 주입하지 않는다. 실제 archived INSTALL, README, configure.ac와 FLINT building 문서를 읽고 다음 순서를 작성했다. 문서 SHA 및 실제 archive intake 결과는 `evidence/backend/PINNED_ARCHIVE_INTAKE.json`에 있다.

| 대상 | 순서와 선택 |
|---|---|
| GMP | configure `--prefix`, `--libdir` → `make -j2` → `make -j2 check` → install |
| MPFR | 같은 순서, `--with-gmp=<sidecar>` |
| FLINT | `sh bootstrap.sh` → configure `--with-gmp`, `--with-mpfr`, `--with-blas=no`, `--with-ntl=no` → build → `check MOD=arb acb acb_hypgeom acb_calc` → install |
| callback 합성 | 잠긴 `validated_callback/build_host.sh` → 새 binary의 ldd → provenance/path/byte gate → 기존 process guard |
| Petras 합성 | 잠긴 `interior_pilot/build_petras_host.sh` → 같은 linkage gate → 기존 process guard |

세 소스의 핀을 모두 검증한 뒤에만 추출을 시작한다. 압축 크기 16 MiB, 풀린 tar 128 MiB, member 20,000개, member 파일 16 MiB, 파일 합 96 MiB를 상한으로 검사한다. 절대·상위 경로, 중복, 파일/디렉터리 충돌, 모든 link/sparse/special member를 거부한다. 고정된 실제 archive 세 개는 모두 이 정책으로 추출되었으며 link가 없었다. 원본 upstream payload는 공개 저장소에 추가하지 않았다.

## 한도와 증거

- `make -j2`, 전체 10,800초, configure/bootstrap/install 각 180초, build 각 2,400초, check 각 1,200초, native build/run 각각 180초다. 남은 전체 예산이 더 작으면 그 값을 적용한다.
- child process마다 address space 4 GiB, CPU 시간과 파일 크기 2 GiB 한도를 적용한다. stdout/stderr 각각 8 MiB, workspace 16 GiB/200,000파일은 주기적으로 검사하며 초과하면 process group을 종료한다. **주소 공간은 process tree 전체 RAM 한도가 아니며, 주기 검사에는 짧은 초과 구간이 가능하다.** 의도적으로 process group을 탈출하는 프로그램은 계약 밖이다.
- 외부 `LD_PRELOAD`, Python 경로, MAKEFLAGS, proxy, compiler flags를 전파하지 않는다. sidecar의 `LD_LIBRARY_PATH`와 pkg-config 경로를 고정한다. 사용자 HOME을 다른 경로로 지정하지 않는다.
- 단계별 `logs/<stage>/STAGE.json`, 실제 stdout/stderr, compiler 바이너리/버전, archive 및 설치 library SHA를 보존한다. `BACKEND_BUILD_PROVENANCE.json`은 이 실행기 영수증을 연결하며 독립적인 과거 실행 증명으로 취급하지 않는다.
- `provenance_gate.verify_backend`와 `verify_linkage`를 사용한다. 실행 직전 링크된 GMP/MPFR/FLINT 경로와 SHA를 기록과 대조한다. fixture stdout의 마지막 JSON marker를 확인하고 Petras의 앞선 두 diagnostic 줄도 보존한다.
- `HOST_RESULT.json`은 성공 또는 실패를 남긴다. 실제 host가 수행하기 전에는 `HOST_SYNTHETIC_ACCEPTED`를 주장할 수 없다. 소스/hash 일치는 실행 허가와 같지 않다.

## 여기서 수행한 검증

`python -m unittest test_backend_runner -v`는 toy tar, 악성 경로/중복/압축 예산, create-only, 계획 순서, 환경 오염 제거, Python process timeout, 합성 최종 marker를 검사한다. compiler나 실제 HH 값을 실행하지 않는다. RED → GREEN 로그를 `evidence/backend/`에 보존했다. 실제 native compile/runtime의 최종 확인은 사용자의 Linux 호스트 실행과 별도 검토가 필요하다.
