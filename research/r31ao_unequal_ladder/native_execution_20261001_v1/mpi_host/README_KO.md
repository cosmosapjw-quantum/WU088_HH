# 실제 Fortran/OpenMPI 빌드 검증

기존 `ncp64_acceleration_20261001_v1/mpi_fortran`의 source를 변경하지 않고 GNU Fortran 13.3.0과 OpenMPI 4.1.6으로 컴파일·링크했다. 최종 증거는 `build_attempt_4/BUILD.json`이다. C bridge는 기존 `/usr/bin/gcc` 13.3.0을 사용했다. `-O3 -fno-fast-math -ffp-contract=off`와 Fortran `-fopenmp-simd`를 유지했다. wrapper·compiler·source·binary identity 및 정확한 invocation은 BUILD receipt에 있다.

Ubuntu snapshot의23개 패키지44,749,810bytes를 일반 curl 전송으로 확보하고 apt-cache가 제공한 SHA512와 모두 대조했다. `dpkg-deb -x`로 scratch sidecar에만 추출했으며 시스템 설치나 기존 runtime 교체는 없다. 배포 패키지의 relocation은 OPAL_PREFIX, OMPI_FC, OMPI_CC, OMPI_LDFLAGS로 명시했다. 전체 컴파일러 의존성에 대한 독립 pin closure를 주장하지 않는다. package URL·hash·환경·동적 library identity는 `toolchain_provenance/`에 보존했다.

세 초기 실패는 모두 남겼다. 첫 시도는 compiler companion의 liblto_plugin 누락, 두 번째는 sidecar C compiler의 cc1 누락, 세 번째는 Debian Fortran stub library의 선행 검색으로 발생했다. 정확한 compiler companion을 추가하고 기존 C compiler를 사용했으며, 동일 OpenMPI 패키지의 실제 f08 심볼을 가진 library 디렉터리를 명시해 마지막 시도가 성공했다. 과학 소스, 정밀도, 허용오차를 변경한 해결책이 아니다.

compiler report는 dispatcher61/63행의 정수 초기화·budget 합산에16-byte SIMD를 기록한다. 과학 kernel SIMD, 수치 정확성 검증, NCP64 성능 측정을 의미하지 않는다. linked binary의 모든 동적 의존성은 선택된 환경에서 해석된다.

2-rank 실행은 완료하지 못했다. 현재 uid0에서 정상 `mpirun -np 2 --host localhost:2 --nooversubscribe /usr/bin/true`를 호출하자 OpenMPI가 root 실행을 거절했다(rc1). 비특권 subprocess 전환도 EPERM이었다. 기존 계약의 root bypass·oversubscription 금지를 유지했으며 MPI rank가 시작되지 않았다. `MPI_ROOT_REFUSAL.json`과 stderr가 직접 증거다. 이는 과학 실패가 아닌 host 실행 제약이며, 빌드 성공을 MPI runtime 성공으로 승격하지 않는다.

## NCP 비특권 계정에서 이어갈 명령

호스트에 정상 설치된 GNU Fortran/OpenMPI wrapper SHA를 확인하여 기존 `mpi_fortran/build.py`로 새 경로에 다시 빌드한다. 다음은 wrapper를 선택하고 해시를 고정한 뒤 실행하는 기존 API다. REPO, OUT, MPIFORT, MPICC, 각 HASH는 실제 절대경로와 검증한 SHA로 설정한다. 아래 명령은 이번 환경에서 실행했다고 주장하지 않는다.

```bash
python "$REPO/research/r31ao_unequal_ladder/ncp64_acceleration_20261001_v1/mpi_fortran/build.py" \
  --output-dir "$OUT/build" \
  --mpifort "$MPIFORT" --mpifort-sha256 "$MPIFORT_HASH" \
  --mpicc "$MPICC" --mpicc-sha256 "$MPICC_HASH"
python "$REPO/research/r31ao_unequal_ladder/ncp64_acceleration_20261001_v1/executor/make_fixture.py" \
  --output-manifest "$OUT/two_rank.json" --output-root "$OUT/tasks" \
  --task-count 12 --cpu-units 50000
python "$REPO/research/r31ao_unequal_ladder/ncp64_acceleration_20261001_v1/mpi_fortran/export_worklist.py" \
  --manifest "$OUT/two_rank.json" --output "$OUT/two_rank.worklist"
python "$REPO/research/r31ao_unequal_ladder/ncp64_acceleration_20261001_v1/host_plan/launcher.py" \
  --manifest "$OUT/two_rank.json" --mpi-binary "$OUT/build/ncp64_dispatch" \
  --worklist "$OUT/two_rank.worklist" --output "$OUT/two_rank_host" \
  --ranks 2 --reserve-gib 16 --worker-mib 1024 --wall-seconds 120 --execute-synthetic
```

출력은 새 경로여야 한다. 기존 launcher의 topology/quota/memory/identity/descendant guard와 collector를 유지한다. 성공 기준은 HOST_RUN의 `EXECUTION_COMPLETE`,12개 complete task, expected payload hash 및 rank binding receipt다. 그 뒤 actual callback 연결과 target-host1/2/4…64 calibration은 별도 gate다. 이번 결과의 actual_HH_runs=0, production_admitted=false다.
