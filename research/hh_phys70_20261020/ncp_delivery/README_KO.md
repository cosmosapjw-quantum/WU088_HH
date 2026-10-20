# PHYS70 최적화 실행기 — 고정 요청과 NCP 반환 계약

이 디렉터리는 완성된 `scripts/phys70_ncp.py`와
`native/phys70_optimized` 실행 파일의 두 고정 요청을 전달한다.
NCP에서 필요한 작업은 의존성 준비, 컴파일, 필요한 작은 환경 수정과
실제 실행이다. solver 설계는 이 실행 계약의 미완료 항목이 아니다.

**현재 완료 상태:** `REQUEST_L28_PERF.json`의 샌드박스 pilot은 이미 완료됐고
`benchmark/ncp_pilot/`에 보존돼 있다. 같은 상태의 재실행은 필요하지 않다.
L64는 현재 `PREFLIGHT_ONLY`이며 실제 원격 호스트 상태는 UNKNOWN이다.
새 실행의 기본 후보는 아래 L64 요청이다. 이 문서의 L28 실행 명령은 별도
호스트에서 새 성능 질문을 승인한 경우의 사용 예로 남겨둔다.

측정에 사용한 x86-64 GNU binary는 `GLIBC_2.39`를 요구한다. NCP의 glibc가
오래된 경우 아래 고정 source/Cargo.lock으로 현지 컴파일한다. 제공한 binary의
hash는 측정·완료 resume의 identity이며, 모든 Linux host에서 실행 가능하다는
표시는 아니다.

## 먼저 기존 실행을 확인한다

최신 WU GitHub PR, PHYS70 배포 기록, 관련 백업 및 실제 호스트의
process/job/run 디렉터리에서 같은 request·seed·source·engine·binary의
완료 영수증을 확인한다. 기존 자료를 검색하지 못한 것은 NCP 실행이
없다는 증거가 아니다. 일치하는 완료본은 아래 `--resume`로 읽기 검증한다.
진행 중인 작업은 그 작업을 관찰한다.

PHYS64 NCP20, PHYS66 pilot/smoke, PHYS67 인증, PHYS68 완료 L28 panels와
기존 Rust 실행, PHYS69 완료 band 및 기존 VigilODE L28 두 실행은 반복하지
않는다. 여기의 `REQUEST_L28_PERF.json`은 PHYS70 engine과 별도 오차 설정을
가진 새 최적화 비교 요청이다. 과거 완료 PHYS69 요청으로 바꾸지 않는다.

## 물리 및 오차 목표

원래 atomic 좌표, `B=27`, `T=65`, `k=7/10`, `E=49/200 Hartree`,
`R0=0.7`, `H+=G+iF`, `Z=+u'u^-1`,
`V=2(1+1/d)exp(-2d)`를 보존한다. `eta=Fy`, `xi=Fy-phi`,
`eta_C=-10/7`은 서로 다른 정의다.

원본 frozen NPZ SHA-256:

```text
f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d
```

PHYS69 재사용 source pin:

```text
a21d573980f66fe02891bd216153443b5352f921
```

| 요청 | L | angular nodes | rtol | atol | max step | engine |
|---|---:|---:|---:|---:|---:|---|
| `REQUEST_L64.json` | 64 | 128 | `1e-10` | `1e-12` | `0.25` | `block_simd` |
| `REQUEST_L28_PERF.json` | 28 | 96 | `3e-11` | `3e-13` | `0.5` | `block_simd` |

L64의 내부 `physics_request`는 기존 PHYS69 L64 요청과 동일하다.
두 요청 모두 `initial_step=0.01`, `HH_R10=OFF`다. PHYS70의 보호 범위는
`initial_step <= max_step <= 0.5`다. scalar 또는 legacy 비교가 승인된
별도 비교 요청에서는 outer `engine`을 `block_scalar` 또는 `legacy_gmres`로
선택한다. 원본 요청은 보존하고 새 파일 및 새 output 디렉터리를 사용한다.

실행 성공, 같은 물리량의 오차 비교, 속도 비교, 전체 오차 인증은 별도로
기록한다. 이 wrapper는 source/input/engine identity와 완료 endpoint의
형식·유한성·`D2 = scaled_endpoint / 2^160`을 확인한다. 계산된 값의 ODE,
Coulomb, quadrature, roundoff 오차 전체를 자동 인증하지 않는다.
PHYS69의 특정 all-angular D2 인증과 PHYS63 qualitative LAP는 이미 확보된
범위에서 재사용한다. 전체 lambda=1 응답, 원래 source-driven xi,
원점/incoming adjoint, sigma(E), Maxwellian k_HH(T)는 각각의 의무를 유지한다.

## 가벼운 준비 확인

저장소 루트에서 실행한다. 아래 명령은 compiler나 special function을
호출하지 않으며 새 output 디렉터리에 preflight 영수증만 생성한다.

```bash
python3 scripts/phys70_ncp.py \
  --request research/hh_phys70_20261020/ncp_delivery/REQUEST_L64.json \
  --out runs/phys70_l64_preflight \
  --make-seed
```

preflight 디렉터리는 완료 과학 실행이 아니므로 실행 디렉터리로 재사용하지
않는다. 실제 실행에는 아래의 별도 새 경로를 사용한다. `--make-seed`가
있어도 `--run`이 없으면 Coulomb seed를 계산하지 않는다.

## 빌드와 실제 실행

Rust 1.94.1과 고정 Cargo.lock을 사용한다. build는 `--locked --release
--jobs 1 --bin wu088-hh-phys70-optimized`로 제한한다. Cargo cache가 준비된
호스트에서는 `--offline`을 추가할 수 있다. `--target-dir`는 실행 결과
디렉터리 밖에 둔다.

기존 L64 seed가 있으면 이를 먼저 사용한다.

```bash
python3 scripts/phys70_ncp.py \
  --request research/hh_phys70_20261020/ncp_delivery/REQUEST_L64.json \
  --seed /absolute/path/to/L64_SEED_INPUT.txt \
  --out runs/phys70_l64_block_simd \
  --run --timeout 900 --build-timeout 900 --memory-gib 4
```

일치하는 L64 seed가 없을 때만 기존 PHYS68/67의 512-bit initializer를
명시적으로 실행한다. 이 경우 기존 의존성 파일
`research/hh_phys68_20261019/ncp_delivery/requirements.txt`로 Python 환경을
준비한다. `create_seed`를 변경하거나 Born 적분을 새 seed 생성에 포함하지
않는다.

```bash
python3 scripts/phys70_ncp.py \
  --request research/hh_phys70_20261020/ncp_delivery/REQUEST_L64.json \
  --make-seed --out runs/phys70_l64_block_simd \
  --run --timeout 900 --build-timeout 900 --memory-gib 4
```

`--seed`가 명시되어 있으면 `--make-seed`보다 우선하며 생성기를 호출하지
않는다. 이미 준비된 binary도 사용할 수 있다. 이 경로는 Cargo나 Rust
version 명령을 실행하지 않고 binary의 정확한 SHA를 기록한다.

```bash
python3 scripts/phys70_ncp.py \
  --request research/hh_phys70_20261020/ncp_delivery/REQUEST_L28_PERF.json \
  --seed research/hh_phys69_20261019/vigilode/inputs/L28_SEED_INPUT.txt \
  --binary native/phys70_optimized/target/release/wu088-hh-phys70-optimized \
  --out runs/phys70_l28_perf_block_simd \
  --run --timeout 900 --memory-gib 4
```

각 child process는 POSIX process group, 지정 wall limit, `RLIMIT_AS`,
core dump 금지, nice 증가 10 및 BLAS/OpenMP/Rayon thread 1을 적용한다.
timeout이면 process group에 TERM을 보내고 필요한 경우 KILL로 정리한다.
stdout/stderr, 실제 exit code, timeout 여부, wall time과 주소 공간 한도는
각 command 영수증에 보존한다. 하나의 완전한 solver 실행 시간을 비교할
때는 build/seed 생성과 native integration 시간을 분리하고 동일 호스트의
동일 정확도 및 전체 work counters를 함께 사용한다.

## 완료본의 읽기 전용 재사용

```bash
python3 scripts/phys70_ncp.py \
  --request research/hh_phys70_20261020/ncp_delivery/REQUEST_L64.json \
  --seed /absolute/path/to/L64_SEED_INPUT.txt \
  --binary native/phys70_optimized/target/release/wu088-hh-phys70-optimized \
  --out runs/phys70_l64_block_simd --resume
```

생성된 seed를 가진 L64 완료본은 외부 `--seed` 없이도 저장된 seed를 검증해
재사용할 수 있다. 현재 binary가 보존되어 있어야 한다. 요청 원문 bytes,
frozen source, seed, binary, 두 Rust crate의 원문·Cargo.toml·Cargo.lock,
wrapper/기존 guard의 fingerprint, 모든 결과 payload SHA 및 성공 execution
영수증이 일치해야 `REUSED_COMPLETED`를 반환한다. `--run`이 함께 있어도
완료 resume는 subprocess 0, 새 적분 0, 파일 쓰기 0이다.

`PREFLIGHT_ONLY`, 부분 native JSON, nonzero exit, timeout, checksum 불일치,
중단으로 마지막 영수증이 없는 디렉터리는 완료로 처리하지 않는다. wrapper는
그 결과를 덮거나 자동으로 처음부터 재실행하지 않는다. 원인·실제 process
상태를 확인하고 구체적인 수정 후 별도의 새 output 경로를 사용한다.

## 반환해야 하는 원본 파일

`REQUEST.json`에는 제출한 요청의 원문 bytes를 그대로 저장한다. native가
기록한 `request_sha256`은 이 파일에 대한 SHA이며 JSON 재직렬화로 바꾸지
않는다.

- `REQUEST.json`, `FROZEN_U_SUBSET.npz`, `SEED_INPUT.txt`, 생성 시 `SEED_BALLS.json`.
- `INVOCATION.json`, 각 command의 `.EXECUTION.json`·`.stdout.txt`·`.stderr.txt`.
- native JSON이 나온 경우 stdout과 byte-identical한 `RESULT.json`.
- 최종 상태와 engine/binary/input identity를 담은 create-only `EXECUTION.json`.
- `EXECUTION.json`까지 포함한 create-only `CHECKSUMS.json`.

실제 checkout HEAD/tree, compiler/flags/CPU, 요청·source·seed·binary·engine
hash, 호스트와 시각, solver 완료 여부, 정확도 비교와 전체 timing/work를
반환한다. 허용된 additive Git branch/draft PR와 create-only 백업에 결과 ZIP을
게시하고 실제 ACK를 별도로 기록한다. 이 Python wrapper 자체는 Git push,
클라우드 백업, 원격 NCP job 제출 또는 DAG 승격을 하지 않는다.

## 새 wrapper 검증만 실행하기

```bash
python3 tests/test_phys70_ncp.py -v
```

이 표준 `unittest` 파일은 임시 디렉터리의 **NONPHYSICAL TEST FIXTURE**
프로그램으로 요청 보존, 고정 physics guard, receipt/hash resume, 실패·부분
결과·timeout·주소 공간 제한 및 빌드 명령 경로를 검증한다. 실제 native
solver와 Coulomb 생성기, 과거 과학 실행, 종전 test suite를 실행하지 않는다.
이 테스트 개수를 실제 물리 성공 실행 또는 성능 측정으로 세지 않는다.

게시·백업·DAG의 최종 상태는 PHYS70의 실제 배포 영수증을 따른다.
`HH_R10=OFF`를 유지한다.
