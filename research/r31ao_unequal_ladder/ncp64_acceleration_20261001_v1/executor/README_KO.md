# 합성 exact-byte 작업 실행기

이 실행기는 `SYNTHETIC_ONLY` 작업의 입력·명령·실행 파일·라이브러리·결과 bytes를 결박한다. 실제 HH, B192 또는 과학적 적합 판정은 실행하거나 승인하지 않는다. Python 표준 라이브러리와 Linux `/proc`, `flock`, `resource`가 필요하다. native build/run은 이번 구현 검증에서 0회다.

## 바로 실행하는 Python 합성 경로

다음 변수는 사용자가 선택한 절대 경로다. `RUN_PARENT`는 기존 디렉터리이고 새 manifest와 output root는 아직 없어야 한다. 실제 사용한 Python 및 source bytes는 manifest와 RUN.json에 기록된다.

```bash
PY=/absolute/path/to/python
NEW=/absolute/path/to/ncp64_acceleration_20261001_v1
RUN_PARENT=/absolute/path/to/existing/scratch
"$PY" -B "$NEW/executor/make_fixture.py" \
  --output-manifest "$RUN_PARENT/tasks.json" --output-root "$RUN_PARENT/tasks" \
  --task-count 16 --cpu-units 1000000
"$PY" -B "$NEW/executor/prepare.py" --manifest "$RUN_PARENT/tasks.json"
"$PY" -B "$NEW/executor/run_local.py" --manifest "$RUN_PARENT/tasks.json" --workers 4
"$PY" -B "$NEW/executor/collect.py" --manifest "$RUN_PARENT/tasks.json"
```

`cpu_units`는 각 작업의 최대 정수 반복 횟수이며 1..5,000,000이다. 작업마다 부호가 있는 유리수와 다른 반복 수를 사용한다. backend가 직접 계산하는 정수 제곱합은 독립적인 닫힌식 `N(N+1)(2N+1)/6`으로 만든 기대 bytes hash와 대조된다. 부하 분포는 고정이고 sleep으로 CPU 성능을 대신하지 않는다. local 1/2/3-worker tests는 정확히 같은 payload digest를 검증했다. 실제 성능 측정과 NCP 64-core 결과는 이 unit test에서 주장하지 않는다.

## Native fixture 연결

`native_cache/build_host.sh`가 생성한 **기존** `BUILD_READY.json` 및 sidecar `PREFIX/lib`가 필요하다. 아래 생성 명령은 컴파일·실행을 하지 않는다.

```bash
BUILD=/absolute/path/to/native-build
PREFIX=/absolute/path/to/verified-sidecar-prefix
"$PY" -B "$NEW/executor/make_fixture.py" \
  --output-manifest "$RUN_PARENT/native_tasks.json" --output-root "$RUN_PARENT/native_tasks" \
  --build-ready "$BUILD/BUILD_READY.json" --backend-library-path "$PREFIX/lib" \
  --case point107 --case complex_point107 --case complex_box107 \
  --precision 128 --repeat 1
# 별도 허용된 host synthetic 실행 시:
"$PY" -B "$NEW/executor/run_local.py" --manifest "$RUN_PARENT/native_tasks.json" --workers 3
```

`--backend ABS_BINARY`는 선택 옵션이며 주면 receipt의 binary와 같아야 한다. binary·세 backend library(FLINT/GMP/MPFR)·기록된 system library·source·compiler·log·archive의 현재 bytes를 검사한다. `BUILD_READY.json` 자체도 input hash로 결박한다. sidecar 세 library는 한 개의 지정된 절대 디렉터리에 있어야 한다. `LD_LIBRARY_PATH`는 해당 디렉터리로 **task.env에 명시**되므로 supervisor 환경을 초기화해도 backend까지 전달된다. 빈 library pin 또는 ambient 환경 상속으로 대체하지 않는다.

이 adapter는 공급된 receipt와 현재 bytes를 연결한다. source pin/build log의 작성 경위, 올바른 컴파일 또는 runtime linkage를 독립적으로 증명하지 않는다. 기존 `verify_inputs.py`/provenance gate의 빌드 검증과 이후 native equality 실행·검토는 별도다. metadata tests의 fake receipt는 이 연결만 검사하며 native acceptance 증거가 아니다. loader 경로, symlink 및 파일이 실행 중 외부에서 바뀌지 않는 신뢰된 host를 전제한다.

정확도 gate의 세 case만으로는 63 worker를 채울 수 없다. 같은 세 case를 반복해 96개의 독립 작업을 만들 수 있다. CLI의 `--case`를 반복하거나 Python에서 다음과 같이 사용한다. task_id는 원래 index로 구별된다. 모든 worker 수에서 같은 case 목록·순서·precision·repeat를 사용하고, 측정은 최소 2개의 독립 새 output root에서 반복한다. 이 명령 예시는 측정을 실행했다는 뜻이 아니다.

```python
import sys
sys.path.insert(0, NEW + "/executor")
from make_fixture import create_native_fixture
create_native_fixture(MANIFEST_ABS, OUTPUT_ROOT_ABS, None,
    ["point107", "complex_point107", "complex_box107"] * 32,
    precision=128, repeat=1,
    build_ready=BUILD_READY_ABS, backend_library_path=PREFIX_LIB_ABS)
```

`errors` case는 `repeat=1`만 허용한다. 다른 case의 repeat 범위는 1..100, precision은 32..4096이다. 반복 작업에서도 payload의 scientific bytes는 backend에서 생산한 그대로 수집한다. stdout의 timing/cost metadata는 payload에 섞지 않는다.

## 명령 및 Python API

| 명령 | 성공 stdout status | 성공 exit | 역할 |
|---|---|---:|---|
| `prepare.py --manifest ABS` | `READY` | 0 | RUN identity 검증, complete/missing indices 반환 |
| `worker.py --manifest ABS --task-index N` | `COMPLETE` 또는 `REUSED` | 0 | 원래 tasks 배열의 0-based index 하나 |
| `collect.py --manifest ABS` | `COLLECTED` | 0 | 정확한 전체 task set과 payload 검증 |
| `run_local.py --manifest ABS --workers N` | `COLLECTED` | 0 | 1..63 worker의 local fallback 및 수집 |

거절·실패는 `INCONCLUSIVE`, exit 2다. CLI usage 오류도 2다. Python API는 `core.load_manifest`, `core.prepare_manifest`, `core.run_task`, `core.collect`, `run_local.run_local`, `make_fixture.create_fixture` 및 `make_fixture.create_native_fixture`다. 각 모듈은 `executor` 디렉터리를 Python import path에 놓고 사용한다.

Fortran bridge는 shell 없이 다음 argv를 호출한다:

```text
ABS_PYTHON ABS_WORKER --manifest ABS_MANIFEST --task-index N
```

MPI는 정수 task index/status만 교환한다. 최종 성공은 MPI exit만으로 결정하지 않고 collector의 `COLLECTED`, declared/complete count 일치 및 digest를 요구한다. full `dispatch_order`에는 모든 task index가 정확히 한 번 포함된다. 비용 내림차순, task_id 오름차순 tie-break다. 비용은 scheduling hint이고 과학적 계산 순서를 바꾸는 지시가 아니다. collector는 task_id 순으로 canonical digest를 생성한다.

## Manifest 및 정확성 경계

최상위 필드는 `schema`, `scope`, `output_root`, `tasks`, 선택적 `dispatch_order`다. schema는 `WU088_NCP64_TASK_MANIFEST_V1`, scope는 `SYNTHETIC_ONLY`만 허용한다. 8 MiB manifest, 최대 4096 tasks, 중복 JSON key, 중복 ID, traversal 경로, 잘못된 index permutation을 거절한다.

각 task는 `task_id`, `executable`, `argv`, `inputs`, `env`, `cost_hint`, `limits`, `semantic_identity`를 요구한다. `library_pins`, `expected_output_sha256`는 선택이다. 파일 identity는 정확히 `{path, bytes, sha256}`다. executable과 입력은 실행 전·후 및 재사용·수집 때 다시 hash 검사한다. precision·full parameter box·error budget 등 backend의 계산 계약은 `semantic_identity`와 argv/input bytes에 명시해야 한다. 실행기는 이 metadata의 과학적 타당성을 판정하지 않는다.

argv는 완성된 문자열 배열이며 shell expansion이 없다. 정확히 한 개의 standalone `OUTPUT_PATH`를 worker의 독립 working directory에 있는 `payload.bin` 경로로 치환한다. 다른 절대 argv 입력 경로는 선언된 입력 또는 library pin이어야 한다. task별 working directory, stdout/stderr, checkpoint, payload는 분리된다. 내부 BLAS/OpenMP 등 thread 수는 1로 고정한다.

payload는 nonempty bounded regular file이어야 한다. exact ball, 유리수 또는 어떤 serialization이든 **opaque bytes**로 이동·hash하며 float로 변환하거나 재직렬화하지 않는다. 기대 hash가 있으면 그 값까지 대조한다. 기대 hash가 없는 generic native task에서는 backend의 exit 0 및 정확한 byte collection을 검증할 뿐 payload의 수학적 유효성을 증명하지 않는다. native backend 자체의 equality gate가 별도로 필요하다.

`RUN.json`은 raw manifest SHA256, core/guard/worker source SHA256 묶음, 전체 task identity에 결박된다. task identity는 scheduling cost를 제외한 모든 필드를 포함한다. 동일한 작업과 precision/env/library pins라도 manifest bytes가 바뀌면 기존 run 재사용을 거절한다. canonical payload digest는 task_id, task identity, payload hash/length의 정렬 목록을 hash하므로 output root와 worker 수에 독립적이다. floating MPI reduction은 수행하지 않는다.

## Checkpoint와 resume

manifest와 output root는 create-only로 생성한다. `prepare`는 같은 identity의 이미 완료된 task만 재사용한다. `COMPLETE`는 child exit 0, guard 정상 종료, 현재 input hashes, 최종 payload hash가 모두 일치해야 한다. atomic metadata write는 tempfile/fsync/replace/directory-fsync 이후 byte readback을 하고, worker는 최종 checkpoint 전체 내용과 payload를 다시 읽은 후에만 COMPLETE를 반환한다.

이미 완료된 작업은 backend를 다시 실행하지 않는다. 부분 파일, RUNNING/INCONCLUSIVE checkpoint, hash 불일치 또는 손상된 journal이 있으면 자동 복구·자동 재실행 없이 INCONCLUSIVE다. 이런 artifact는 보존하고 새 manifest/output root를 별도 선택해야 한다. 동시에 같은 task를 호출하면 lock으로 거절한다. collector는 누락·추가 task directory도 거절하며 각 checkpoint와 payload를 재검증한다.

이번 root의 초기 두 benchmark attempt에서 worker가 COMPLETE를 반환한 뒤 수집 시 checkpoint가 RUNNING으로 관측되는 저장 상태 이상이 있었다. 원인은 **UNRESOLVED**이고 atomic write 코드의 원인이라고 단정하지 않는다. 초기 evidence는 parent가 보존한다. 최종 readback은 그 시점의 상태 검사이며, 이후 외부 변경이나 저장소의 변동까지 영구히 막는 보장은 아니다. collector가 이 불일치를 거절한 사실과 깨끗한 별도 경로의 최종 검증은 구분한다.

## 자원 및 host 한계

`limits`는 정수 `wall_seconds`, `address_space_bytes`, `rss_bytes`, `poll_ms`, `max_output_bytes`를 모두 요구한다. wall은 1..86400초, address space는 64 MiB..64 GiB, RSS는 16 MiB..address space, poll은 10..1000 ms, payload cap은 1..64 MiB다.

* RLIMIT_AS/CPU/FSIZE는 **개별 process**에 상속되는 OS limit이다. RSS는 같은 process group의 합을 주기적으로 측정하는 관측 guard이며 hard aggregate cgroup limit이 아니다.
* backend는 새 process group에서 실행한다. timeout, SIGTERM/SIGINT 또는 guard 오류 때 group을 종료하고 leader를 회수한다. leader 종료를 관측한 뒤 fresh group scan 및 killpg 존재 검사를 하므로 남은 자식이 있으면 결과를 승인하지 않는다.
* `/proc`가 ancestor PID namespace를 보여 주는 환경도 `NSpid`/`NSpgid` 및 PID namespace identity로 정규화한다. PID namespace metadata가 없는 플랫폼은 지원하지 않는다.
* 신뢰된 backend는 `setsid`/group escape를 사용하지 않아야 한다. 임의의 악성 process tree를 감금하는 sandbox가 아니다. supervisor 자체의 SIGKILL, uninterruptible kernel sleep, 프로세스별 limit의 합, poll 사이 peak RSS는 hard bound로 주장하지 않는다. 전체 job guard와 OS/cgroup admission은 host launcher의 별도 책임이다.
* local ProcessPool 경로의 timing은 dispatch·subprocess·hash 검사·collection을 포함하고 fixture 생성과 build를 제외한다. 많은 작은 task에서는 이 overhead가 우세할 수 있다.

## 검증

```bash
cd "$NEW/executor"
"$PY" -B -m unittest -v test_executor test_make_fixture
```

12개의 실제 Python subprocess tests와 4개의 native receipt metadata tests를 실행한다. 기록된 red/green 로그는 정확한 exit status를 포함한다. timeout, descendant, sampled RSS, SIGTERM cleanup, shell 문자 literal, resume, stale/hash mismatch, duplicate/traversal, partial/failed payload, 최종 readback 거절을 검증한다. 가짜 native receipt fixture는 metadata adapter test 전용이며 C/native code를 컴파일하거나 실행하지 않는다. 독립 reviewer의 race 및 MPI bridge 검증은 상위 `review/`의 별도 evidence다.
