# NCP64 정확도 보존 가속 전달 보고서

고정밀 callback 중복 제거, Fortran/OpenMPI 동적 분배, 정확한 결과 수집·재시작, 실제 자원 기반 실행기와 병렬 backend 빌더를 새 overlay로 구현했다. 로컬 구현 검사 59개를 통과했다. **실제 NCP 접속, native Arb 동등성 실행, Fortran/MPI 실행과 NCP 속도 검증은 아직 수행하지 못했다.** 현재 실행 환경은 CPU quota8과 memory limit8GiB이며 관련 toolchain이 없다.

## 계산 비용과 정확도

107항의 density 계산214회를 최대18회, spatial 계산107회를 최대9회로 줄인다. 동일 호출 안에서 같은 인자의 결과를 다시 사용한다. 원본 helper를 같은 translation unit에 포함하며 항별 곱셈·합산 순서, 정밀도와 full complex box를 유지한다. 약11.89는 해당 helper 평가 횟수 비율이며 전체 실행 속도 향상률이 아니다. fixture는 원본과 cached `acb_equal` 및 real/imag `arb_dump_str` 정확 일치를 요구한다. 실제 native 실행은 미검증이다.

MPI는 독립 task의 순서와 작업 배정만 바꾼다. payload의 수치 재직렬화나 MPI 부동소수점 합산을 하지 않는다. Fortran SIMD는 정수 제어 루프에만 적용하며 고정밀 scientific kernel SIMD 성공을 주장하지 않는다. 기존 per-term 연산과 error budget을 유지한 채 병렬성을 늘리는 방식이다.

## 64코어·128GB 사용 계획

64물리코어와 충분한 실제 메모리를 확인하면63workers와1coordinator를 사용한다. 64vCPU가32물리코어의SMT이면 기본31workers+1coordinator로 계획하고 SMT는 별도 측정 옵션이다. 실제 affinity·CPU quota·NUMA·cgroup ancestor 제한을 반영하고 숨은 thread 중첩을 막는다. OS CPU 번호를 hwloc 번호로 오인하지 않도록 rank별 affinity 설정 후 readback을 기록한다.

backend 빌드는 기존 strict floating flags를 유지하면서 CPU·메모리 예산으로 make jobs를 결정한다. 64CPU와112GiB job 예산 예에서는56개 compile slot이며, make check는 최대2다. 2GiB/compile 예약과 sampled RSS는 hard aggregate cgroup memory guarantee가 아니다. 사용자의128GB를128GiB로 가정하지 않는다.

## 검증 결과

| 구역 | 최종 검사 수 | 실제 검증 층 |
|---|---:|---|
| native_cache | 10 | STATIC_SOURCE_AND_EXACT_RATIONAL_EXPRESSION_MODEL |
| backend_build | 7 | PURE_BUILD_PLAN_AND_PRIOR_INPUT_LOCK |
| mpi_fortran | 10 | ACTUAL_GCC_C_PROCESS_BRIDGE_NO_FORTRAN_OR_MPI |
| host_plan | 16 | HOST_PLANNING_AND_SYNTHETIC_LAUNCHER_TEST_DOUBLES |
| executor | 16 | REAL_LOCAL_SUBPROCESS_EXACT_PAYLOAD_AND_FAILURE_CHECKS |

C bridge는 GCC로 실제 컴파일하고 합성 프로세스를 실행했다. host MPI orchestration 검사는 Python test double을 포함하며 native MPI 성공으로 세지 않는다. 독립 검토는 최신 자원 재검사, collector 완료 경계, 잔존 자식 프로세스, 종료 시점 race, PID namespace 변환, native library 환경 연결을 확인·보강했다. source hash와 검토 제한은 `review/`에 기록했다.

첫 두 성능 시도에서는 이전에 완료로 읽힌 checkpoint가 뒤에RUNNING으로 관측되는 저장 상태 불일치가 있었다. 근본 원인은 확정하지 않았다. collector는 이를 INCONCLUSIVE로 거부했고 성공 결과로 채택하지 않았다. metadata 저장과 COMPLETE 반환 전 readback을 추가했으며, 최종 benchmark는 모든 측정 뒤 보존된 결과를 다시 확인한다. 이전 시도 증거는 삭제하지 않았다.

## 로컬 성능

로컬 실제 CPU 합성 작업16개를 workers1/2/4로 각각3회 실행했다. sleep 기반 성능측정이 아니며, 각 task의 정확한 정수 제곱합을 독립 닫힌 식의 SHA256으로 검증했다. 실행 순서를 회전했고 작업 생성 시간을 제외한 spawn·해시 확인·수집 전체 시간을 쟀다. 모든 실행의 canonical digest가 같고 종료 후 저장 결과도 다시 수집하여 확인했다.

| workers | wall 중앙값(초) | 1worker 대비 |
|---|---:|---:|
| 1 | 4.2800 | 1.000× |
| 2 | 2.5922 | 1.651× |
| 4 | 1.5644 | 2.736× |

이 수치는 현재 quota8CPU 환경의 Python subprocess 실행기 측정이다. Arb cache, MPI 또는 NCP64코어의 속도 수치로 외삽하지 않는다. 소스 해시·9회 원시 timing·관측 자원은 `evidence/LOCAL_BENCHMARK.json`에 있다.

## 실행·게시·백업

`README_KO.md`부터 시작한다. ZIP에는 이 overlay와 변경하지 않은 의존 소스·증거, 고정 SHA256의 GMP6.3.0/MPFR4.2.2/FLINT3.4.0 source archives를 포함했다. native build → exact equality fixture → MPI1/2/4 smoke → 동일 정밀도 rank calibration 순으로 실행한다. 이전 source/library runtime은 덮어쓰지 않는다.

게시 대상은 기존 `research/r31ao-unequal-order-ladder-20260930` 브랜치의 새 디렉터리다. Git의 기존 blob은 유지하며 main merge는 하지 않는다. 최종 commit, ZIP 해시, Drive·Dropbox upload ACK/metadata 검증은 별도 `DELIVERY_RETURN.json`과 `BACKUP_RECEIPT.json`에 기록한다. 업로드 확인과 실제 restore 검증을 구분하며 RESTORE_VERIFIED는false다.

실제 HH배열/G7 적분/과거B192 재계산은0회다. production adapter 연결·native host gates·물리 인증은 남아 있다. certified epsilon/eta는 산출하지 않았고 rigorous와scientific promotion은false다.
