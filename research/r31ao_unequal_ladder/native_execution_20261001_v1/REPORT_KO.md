# WU088_HH 후속 연구 실행 기록 — 2026-10-01

이번 작업에서는 고정 정밀도 백엔드를 실제로 구축하고 Frozen107의 작은 구간 적분까지 실행했다. B192 두 원본 archive의 숫자 표현 복원도 완료했다. **전체 영역 적분, 최종 D·ε·gap 판정 및 NCP 64코어 production 승인은 아직 완료되지 않았다.** 원래 연구 단계별 대조는 `audit_database/STAGE_RECONCILIATION_KO.md`와 기계 판독 JSON에 기록한다.

| 항목 | 확인한 결과 | 판정 범위 |
|---|---|---|
| B192 입력 복원 | OD·독립 JVP 두 archive, 12 NPY 배열·4,586 논리 원소를 exact dyadic으로 복원 | 해당 원본에 한정된 x87 형식 승인. 독립 검산은 7,160 실수 성분 확인 |
| 수치 백엔드 | GMP 6.3.0·MPFR 4.2.2·FLINT 3.4.0 실제 빌드·링크 | GMP 3, MPFR 5 실행 시험과 FLINT 344개 명명 시험 통과. FLINT 전체 모듈 시험은 아님 |
| 실제 callback 최적화 | 72 조건·88 쌍에서 baseline/cache ball 및 순서·계수 동일 | 8개 조건의 callback 시간비 중앙값 11.37배. 전체 solver/NCP 속도비는 미측정 |
| 실제 작은 구간 적분 | primitive 0, `[1,2]²`, 128-bit, 성분 반경 ≤ `2^-48` | baseline·cache·수정 host의 세 실행 모두 통과, 반환 구간과 카운터 정확히 같음 |
| 넓은 구간 적분 | 수정 host의 `[1/16,256]²` 실행 | 11,771 평가·126 적분 호출 후 `INTEGRATOR_NO_CONVERGENCE`로 거절 |
| 조립 exporter | 기존 C++ 소스 실제 빌드·실행, 188 복소 원소·376 스칼라 구간 모두 정확히 0 | 실제 Frozen107 매개변수 + 합성 0 원시 적분 2,592개를 사용한 선형성 시험. 실제 D 아님 |
| Fortran/OpenMPI | 실제 컴파일·링크 통과, 정수 처리 SIMD 확인 | MPI rank 실행 0. 과학 커널 SIMD 또는 NCP 성능으로 해석하지 않음 |
| MPI 작업 adapter | 고정 입력·build·source·limits 검증, 12개 경계 시험 통과 | 실제 MPI용 host 검증·자손 종료·결과 수집 연결은 미완료 |

실제 primitive 적분은 총 네 번 실행했고, 같은 primitive의 같은 작은 창에서 세 번 통과했다. 서로 다른 세 primitive를 완료했다는 의미가 아니다. 넓은 창의 실패를 성공 coverage로 집계하지 않는다. callback 비교, 해석적 시험, exporter의 합성 시험, 이전 endpoint 계산은 이 네 실행에 합산하지 않는다.

## 수정한 수치 실행 경계

기존 복소 마진이 큰 상단 cutoff에서 실제 σ보다 커지는 문제를 정확한 양의 하한에 결합해 수정했다. Frozen107의 107개 signed term과 합산 순서, 식의 결합 순서, 실제 복소 입력 공은 보존했다. 캐시는 호출 안에서 정확히 같은 인수를 재사용하며 중점 대체, 항 생략, tolerance 완화, 낮은 정밀도 계산을 하지 않는다.

또한 Petras host가 재분할 가능한 넓은 구간의 nonfinite enclosure를 전체 계산 실패로 처리하던 문제를 재현했다. 추가 구현 `refining_petras.cpp`는 범위 요청을 거절하면서 FLINT의 재분할을 허용한다. 정확한 점의 실패, 예외, 계약 위반, 정밀도·차수 오류, 공용 자원 한도 초과는 계속 치명적으로 거절한다. 해석적 `1/t` 반례는 기존 1회 평가 후 실패에서 수정본 3,240회 평가 후 통과로 바뀌었다. 독립 재컴파일과 치명적 실패 시험도 통과했다.

이미 통과한 `native_driver/`와 그 빌드·실행 기록은 변경하지 않았다. 수정 host는 별도 `refined_native_driver/`와 별도 source identity를 가진다. 실제 CENTRAL 회귀 실행에서도 반환 구간과 모든 계산 카운터가 기존 결과와 같았다. W1 실패는 보존했으며, 반복 재실행이나 한도 상향으로 덮지 않았다.

W1 거절 기록은 입력·계획·task·source·제한과 native 실패를 직접 결합하지만, 성공 기록과 달리 build wrapper를 포함하지 않는다. cached build 지정은 별도 `runtime/REFINED_EXECUTION_RETURN.json`의 실행 명령 기록에 의존한다. 이 기록은 독립 실행 증명으로 취급하지 않는다.

## 데이터 출처와 재현성

B192 승인은 역사적 producer source·입출력 잠금 기록·C ABI 검사·NumPy 직렬화 소스·실제 raw byte discriminator를 함께 사용했다. 복소 슬롯의 순서는 94개 켤레 쌍의 유효 비트 비교로 확인했다. 디코더는 NumPy 로드나 float cast를 하지 않으며 signed zero, padding, C/F 순서를 구분한다. 역사적 NumPy wheel 자체가 복원됐다고 주장하지 않는다.

이전 production 묶음 137개 파일은 SHA256으로 재확인한다. 기존 DB는 보존하고 후속 감사 DB를 별도로 생성한다. 새 SQLite는 무결성·외래 키·SQL 복원 후 논리 해시 일치를 확인하며, 파일 이름만으로 완료를 추론하지 않는다. DB 행은 중복·상위 집계·이전 실행을 포함할 수 있으므로 행 수를 과학 실행 횟수로 합산하면 안 된다.

게시 대상은 기존 연구 브랜치의 추가 경로 `native_execution_20261001_v1/`다. 바이너리·큰 계획·raw 자료는 배포 ZIP에 보관하고, 컴파일된 backend prefix는 별도 `WU088_HH_PINNED_BACKEND_20261001_v1.tar.xz`로 보관한다. 이 backend 묶음은 현재 호스트의 정확한 백업이며 NCP용 휴대성 인증은 아니다. ZIP의 repo는 복원된 작업 snapshot으로 원격 저장소 전체 mirror가 아니다. 실제 게시 commit과 백업 식별자는 별도 배포 영수증에 기록한다.

## 남은 연구·실행 경계

1. W1/W3 넓은 영역을 인증 가능한 세부 창 또는 검증된 변수 변환으로 처리하는 실행 설계. 로그 변수 변환과 W3 40,000개 창은 설계 검토만 했고 구현·실행하지 않았다.
2. 2,592개 primitive의 필요한 전체 coverage와 전역 endpoint 오차의 한 번만 적용. 작은 창에 W3 endpoint를 바로 더해서 전체 적분으로 처리할 수 없다.
3. 실제 normalized D 조립, ε·모델 gap·최종 동결 판정 및 독립 과학 검토. 합성 0 exporter 통과는 이를 대신하지 않는다.
4. 비특권 NCP에서 native MPI host 검증·자손 프로세스 종료·수집 경계 연결, 2-rank 검증 후 64코어/128GiB 성능 측정. 현재 작업 환경은 8 CPU quota·8GiB이며 NCP가 아니다. OpenMPI의 root 거절을 우회하지 않았다.
5. 이전 조사에서 미복원으로 남은 원래 DeepResearch 자료와 v2 DB 원본의 출처 공백. 이번 B192 원본 복원이 이들을 자동 복구한 것은 아니다.

이번 실행의 기계 판독 결과는 `VERIFICATION.json`, 개별 검토는 `review/`, 고정 backend 근거는 `backend_build/evidence/`, 실제 성공·실패는 `runtime/`에 있다. 현재 허용된 것은 이 근거 범위의 후속 연구이며 최종 production 승인 플래그는 false로 유지한다.
