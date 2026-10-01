# NCP 64코어·128GB 고정밀 가속 구현

현재 채택한 FLINT/Arb 인증 callback의 반복 계산을 줄이고, 독립 작업을 MPI rank에 동적으로 분배하는 추가 구현이다. 기존 과학 소스와 합산 순서, 정밀도, 전체 복소 box, 오차 예산을 유지한다. 이 패키지는 새 `ncp64_acceleration_20261001_v1` 디렉터리에만 추가되며 기존 완료 계산을 다시 실행하지 않는다.

## 구현된 가속

| 변경 | 기대 효과와 정확도 조건 |
|---|---|
| 호출 내부 캐시 | 107항의 density 214회를 최대18회, spatial 107회를 최대9회로 줄인다. 같은 helper와 곱셈·합산 순서 사용. 이 비율은 시간 단축률이 아니다. |
| Fortran `mpi_f08` dispatcher | 비용이 큰 작업부터 idle rank에 배정한다. 과학 값에 대한 MPI 부동소수점 reduction은 없다. |
| 정확 payload와 재시작 | 입력·실행 파일·선언 라이브러리·정밀도·실행기 identity가 같은 완료 결과만 재사용하고 모든 task의 원본 bytes를 모은다. |
| 자원 계획 | 실제 CPU affinity·SMT·quota·NUMA·가용 메모리를 읽는다. 충분한 메모리와64물리코어일 때64ranks=63workers+1coordinator. |
| backend 병렬 빌드 | 기존 `make -j2` 고정 대신 CPU·메모리 예산으로 결정. 64CPU/112GiB job 예산이면56 compile slots, 검사 단계는최대2. |
| 벡터화 | Fortran 정수 제어 루프만 SIMD 후보로 둔다. scientific high-precision 값을 double로 바꾸지 않는다. 실제 vector report는 호스트 빌드 시 생성한다. |

현재 환경에서 실행한 범위와 결과는 `RESEARCH_REPORT_KO.md`, `evidence/FINAL_VERIFICATION.json`, `evidence/LOCAL_BENCHMARK.json`에 구분한다. **Fortran/MPI 및 native Arb 캐시의 실제 빌드·동등성·NCP 성능은 아직 확인되지 않았다.** 구현 검사 성공을 물리 결과나 인증 성공으로 승격하지 않는다.

## NCP에서 시작하는 순서

아래의 경로는 실제 NCP의 절대 경로로 정한다. ZIP의 `research/...` 구조를 유지해서 풀고, 실행 출력은 소스 디렉터리 밖의 새 디렉터리로 둔다. 일반 사용자 계정의 GNU/Linux 환경에서 Python3, GNU C/C++/Fortran, OpenMPI4또는5, make/autotools/m4/pkg-config와 glibc2.34이상이 필요하다. 도구 설치나 SSH 접속은 이 패키지가 수행하지 않는다.

```bash
export WU088_ACCEL=/absolute/unpacked/research/r31ao_unequal_ladder/ncp64_acceleration_20261001_v1
export WU088_RUN=/absolute/new-ncp-run
export WU088_SOURCES=/absolute/unpacked/backend_sources
mkdir "$WU088_RUN"
python3 -B "$WU088_ACCEL/host_plan/planner.py"
```

계획에서 물리64개인지 SMT를 포함한64vCPU인지 확인한다. 기본은 SMT를 제외한다. 사용 가능한 메모리를128GiB로 가정하지 않으며 관측값에서16GiB 여유를 남긴다. `BLOCKED` 사유가 있으면 실제 도구/자원 조건을 해결한다.

1. **backend를 새 prefix에 빌드한다.** 기존 런타임을 덮어쓰지 않는다. ZIP의 `backend_sources`에는 고정 해시의 GMP6.3.0·MPFR4.2.2·FLINT3.4.0 소스 archive가 들어 있다.

```bash
python3 -B "$WU088_ACCEL/backend_build/build_fast.py" \
  --source-dir "$WU088_SOURCES" --output "$WU088_RUN/backend"
python3 -B "$WU088_ACCEL/backend_build/build_fast.py" \
  --source-dir "$WU088_SOURCES" --output "$WU088_RUN/backend" --execute
export WU088_BACKEND_PREFIX="$WU088_RUN/backend/prefix"
export WU088_BUILD_PROVENANCE="$WU088_RUN/backend/BACKEND_BUILD_PROVENANCE.json"
export WU088_CACHE_BUILD_OUT="$WU088_RUN/cache-build"
bash "$WU088_ACCEL/native_cache/build_host.sh"
```

2. **고정밀 캐시를 합성 입력으로 검증한다.** `executor/README_KO.md`의 native manifest 생성기를 사용한다. point107/complex_point107/complex_box107을64·128·256bit에서 확인하고, errors case를128bit에서 확인한다. fixture 안에서 원본과 cached `acb_equal` 및 exact Arb dump 일치를 요구한다. manifest를 `run_local.py --workers 1`로 먼저 실행하고, 같은 task payload를 다른 output_root의 여러worker 실행과 비교한다. 작업별 한도 아래에서 실행하며 실제 HH 입력을 사용하지 않는다.

3. **MPI dispatcher를 빌드하고 검증한다.** `mpi_fortran/README.md`의 `build.py` 명령에 선택한 OpenMPI wrapper 경로와 SHA256을 넣는다. 이어 `host_smoke.py`로1/2/4ranks의 정확 payload 일치를 확인한다. 빌드에는 정수 SIMD vector report와 compiler/link/source/binary receipt가 남는다.

4. **실제 NCP에서 rank 수를 조정한다.** `host_plan/README_KO.md`의 launcher로 같은 native synthetic manifest를1/2/4/8/16/32/64 총ranks 중 관측 예산 안에서 실행한다. task argv·precision·library identity는 고정하고 output_root와 host attempt 디렉터리만 새로 만든다. 각 단계 canonical digest 일치를 먼저 확인한 뒤 wall time 중앙값이 가장 좋은 rank 수를 선택한다. rank2는 계산worker1개이므로 rank1과 같은 계산 병렬도에 coordinator 비용이 추가된다. SMT는 기본 off이며 별도 측정 결과가 좋아야 선택한다.

실패하거나 중단된 attempt를 재개할 때는 같은 manifest, `--resume`, 새 host attempt 디렉터리를 사용한다. 완료된 task만 재사용하고 실패·부분 task는 자동 성공 처리하지 않는다. 실패 원인을 고친 뒤 새 run으로 수행할 task를 명시적으로 다시 준비해야 한다.

## 사용 범위

이 전달물의 실행기 허용 scope는 `SYNTHETIC_ONLY`다. 2592개의 독립 primitive 슬롯이라는 과학 계산 분해는 기존 assembly 계약에서 도출되지만 실제 HH integrator와 전체2592작업을 이번에 실행하거나 인증하지 않았다. 각 슬롯의 내·외부 적분과 tail charge를 보존한 production adapter 연결, 실제 G7 수행 및 반경 기준 통과는 별도 단계다. 패널을 임의 분할해서 각각 전체 허용오차를 주는 최적화는 하지 않았다.

메모리의2GiB/compile과1GiB/worker는 예약·프로세스 한도 정책이다. RSS polling은 hard aggregate cgroup enforcement가 아니며, 외부 job deadline도 임의 kernel hang을 복구하는 수단은 아니다. 기존 archive와 checkpoint backup ACK 규칙을 이 scheduler가 대체하지 않는다.

상세 문서: `ACCURACY_AND_PARALLELISM.md`, `native_cache/README.md`, `executor/README_KO.md`, `mpi_fortran/README.md`, `host_plan/README_KO.md`, `SOURCE_REFERENCES.md`. 최종 commit과 백업 식별자는 detached `DELIVERY_RETURN.json`에서 확인한다.
