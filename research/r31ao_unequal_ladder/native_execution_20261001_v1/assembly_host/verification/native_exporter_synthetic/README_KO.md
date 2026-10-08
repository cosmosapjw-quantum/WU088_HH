# 최종 조립 exporter의 실제 native 실행 검증

`run1/VERIFICATION.json`은 수정하지 않은 기존 `assembly_exporter.cpp`를 고정된 GMP 6.3.0 / MPFR 4.2.2 / FLINT 3.4.0 백엔드에서 컴파일하고 실행한 결과다. 컴파일과 실행은 모두 종료 코드 0이었다.

입력은 **실제 Frozen107 매개변수 헤더와 합성 0 원시 적분값 2,592개**의 조합이다. 실제 HH 적분은 계산하지 않았다. 조립이 원시 적분값에 선형이므로 기대 결과는 정확한 0이다. 출력 `D_col`의 47×2개와 `D_row`의 2×47개, 총 188개 복소 원소의 실수부·허수부 구간 376개가 모두 정확히 `[0,0]`임을 검사했다. 정밀도는 128비트다.

이 기록은 기존 조립 코드의 native 컴파일, 백엔드 링크, 0 입력에 대한 조립·직렬화 동작을 검증한다. 실제 2,592개 HH 적분의 성공, 전체 영역 coverage, 실제 최종 D, 비영 입력의 수치 정확도 또는 조립 호스트의 실제 coverage 기반 전체 수명주기를 검증하지 않는다. `scientific_admission`과 `production_admission`은 모두 `false`다.

exporter 출력의 `coverage_sha256` 필드에는 합성 fixture 설명의 해시를 넣었다. 이것은 성공한 HH coverage 영수증이 아니다. 합성 범위는 `SYNTHETIC_FIXTURE_SCOPE.json`, 생성한 원시 적분 헤더의 주석 및 최종 검증 기록에 명시했다. endpoint/interior 성공 영수증은 만들지 않았다.

실행 한도 및 관측 시간:

| 단계 | 벽시계 한도 | 주소 공간 한도 | 파일별 한도 | 관측 시간 |
|---|---:|---:|---:|---:|
| 컴파일 | 300초 | 4,096 MiB | 64 MiB | 5.438초 |
| native 실행 | 60초 | 2,048 MiB | 16 MiB | 0.017초 |

정확한 컴파일 인수, 컴파일러·소스·생성 헤더·바이너리·공유 라이브러리 해시, 프로세스 제한, stdout/stderr는 `run1/`에 보존했다. `run_fixture.py`가 재현 진입점이며 출력 디렉터리는 새 경로여야 한다. 컴파일에는 `-O3 -fno-fast-math -ffp-contract=off`를 사용했다.
