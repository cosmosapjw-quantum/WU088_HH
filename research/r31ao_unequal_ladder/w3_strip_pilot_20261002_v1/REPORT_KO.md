# W3 새 구간 재사용 계약과 인접 strip 4셀 실제 검증

2026-10-02. 기준 commit: `48443cd754329cd6b76c99f6e9e887081df1e29e`.

이번 우선 연구 단계는 **W1의 기존 16타일을 새 W3 구간에 정확히 재사용하고, 인접 하단·상단 strip 4셀을 실제 계산하여 검증하는 것**이었다. 새 native 실행 4회 모두 `RADIUS_MET`를 얻었고, 독립 검토는 `PASS_SCOPED_PARTIAL_INTERIOR_WITH_OPEN_HOST_EVENT`다. 새 구간의 accepted coverage는 **20/289셀**이며 **269셀은 미계산·미상계**다. 전체 적분, 최종 D/epsilon 또는 production solver 완성을 뜻하지 않는다.

## 고정 표적과 집계 계약

표적은 Frozen107의 primitive 0, 전역 구간은 `[1/512,2^40]^2`, 정밀도는 128bit다. 원 signed coefficient 107개와 저장 순서, 좌표·위상·단위, kernel/backend를 보존했다. 기존 W1·W3 243파일의 SHA-256·크기·mtime은 회수 시점과 같다. 완료된 W1 적분과 직전 endpoint 계산을 재실행하지 않았다.

원 W1 `[1/16,256]^2`의 16타일을 원 raw 출력·host/terminal 기록·validator로 다시 검증하고 새 partition에 연결했다. 원 요청 radius 지수 `-52`를 유지한 채 실제 serialized interval의 radius가 새 할당 `2^-57` 이하임을 확인했다. 재검증은 새 적분 실행으로 세지 않는다.

새 collector는 같은 source·primitive·window·plan으로 연결되는 receipt만 받으며 중복 셀과 중복 출력은 거절한다. 실수·허수 dyadic endpoint를 정확한 유리수로 합산하여 추가 부동소수점 반올림 없이 accepted 셀 합집합의 enclosure를 만든다. 현재 구현의 신규 허용 셀은 아래 4개로 고정되어 있다. 289개 전체를 실행·집계하는 일반 collector의 승인은 별도다.

## 실제 실행 결과

| 셀 | t 구간 | u 구간 | 결과 | 평가 수 | 내부 integration calls | native wall (초) | 최대 component radius |
|---:|---|---|---|---:|---:|---:|---:|
| 20 | `[1/64,1/16]` | `[1/2,4]` | RADIUS_MET | 38,394 | 140 | 12.450247709 | 약 6.88332e-26 |
| 52 | `[1/2,4]` | `[1/64,1/16]` | RADIUS_MET | 40,823 | 280 | 18.922634683 | 약 4.35134e-25 |
| 105 | `[256,2048]` | `[1/2,4]` | RADIUS_MET | 23,149 | 220 | 9.650228366 | 약 9.15156e-24 |
| 57 | `[1/2,4]` | `[256,2048]` | RADIUS_MET | 19,130 | 100 | 6.389383475 | 약 4.53704e-24 |

두 변수 방향을 각각 계산했으며 전치·복소켤레 대칭을 가정하지 않았다. 모든 native/worker 종료 코드는 0이고 native wait 완료, source/input/plan/limits 일치, 보존된 stdout 및 radius 조건을 확인했다. 적응형 계산 중 일부 analytic-domain 시도는 거절되었으며 해당 counter를 원 receipt에 남겼다. 최종 성공이 모든 중간 box의 성공을 의미하지 않는다.

동시 worker는 최대 2개였다. native당 128bit, radius `2^-57`, relative goal 128, 평가 200,000회, integration calls 1,024회, 요청 120초/hard wall 125초, 메모리 1GiB를 적용했다. worker는 180초·1GiB로 제한했다. 첫 관측 거절 후 추가 배치를 멈추고 진행 중 작업을 회수하는 정책과 자동 재시도 금지를 유지했다.

이번 campaign은 dispatch부터 완료 검증·coverage 수집까지 **27.705733198초**였다. 초기 prepare와 W1 재검증 시간은 제외한다. 총 평가는 **121,496회**, nested integration calls는 **740회**, 각 native wall의 합은 **47.412494233초**다. 이 합은 직렬 실행 benchmark가 아니며 27.7초와 나누어 속도 향상률을 주장하지 않는다. 실제 host는 CPU quota 8코어·메모리 제한 8GiB였고 NCP 64코어/128GB나 MPI 실행을 측정하지 않았다. OpenMPI/Fortran 또는 새 SIMD 가속을 달성했다는 결과도 아니다.

## 오차의 정확한 의미

20셀 부분 합집합의 component radius는 다음과 같다.

`r_real = 496918691767025551 / 21267647932558653966460912964485513216`

`r_imag = 496918691890655019 / 21267647932558653966460912964485513216`

최댓값은 약 **2.3365004605418634e-20**이다. 이 radius는 열거된 20셀에만 적용된다. 나머지 269셀의 기여는 `NOT_BOUNDED_OR_INCLUDED`이며 0으로 대입하지 않는다. 직전 endpoint 상계는 전체 선택 직사각형 바깥만 덮으므로 이 부분 합에 더해도 전체 양의 영역에 대한 enclosure가 되지 않는다. Endpoint 결합과 normalization은 수행하지 않았다. 전체 2,592 primitive, source-prescribed contraction, D/epsilon과 최종 과학적 판정은 미완료다.

## B22 host 관측과 독립 검토

완료 RETURN 생성 시 셀 105는 native `.claim` 잔존을 기록했고 셀 57은 기록하지 않았다. 후속 readback에서는 **105와 57 두 파일**이 관측됐다. 두 시점 기록, 파일 bytes·SHA-256·mtime 및 worker PID 문자열을 `HOST_EVENTS.json`과 `review/CLAIM_OBSERVATION.json`에 보존했다. 원인은 **UNDETERMINED**다. 파일만으로 살아 있는 프로세스, I/O 원인 또는 race를 확정하지 않는다. 파일 삭제·격리·재시도는 하지 않았다.

수치 승인은 source-bound raw 출력, 엄격한 validator, native wait 완료와 worker 정상 종료에 근거한다. Host bookkeeping 종료가 완전히 해결되었다는 승인은 별개로 남아 있다. 따라서 B22 및 production lifecycle gate는 열려 있다.

Collector synthetic 검사 11개, controller 검사 5개와 별도 검토자의 추가 controller 검사 2개가 통과했다. 독립 검토자는 새 4개 raw enclosure와 20셀 정확 합을 재구성했고 추가 native 적분·endpoint 평가는 수행하지 않았다. DB builder의 synthetic 검사 23개와 별도 검토도 기록했다. 이는 최종 whole-target scientific admission을 대신하지 않는다.

## 데이터베이스·게시 경계와 다음 단계

`EXECUTION_LEDGER.json`은 **신규 native dispatch/관측/accepted 각각 4, W1 재사용 16, 후보 polynomial 평가 0, 별도 host event 2**로 구분한다. `STAGE_DELTA.json`은 원 연구 단계 G0–G9의 직전 상태를 보존하고 이번 근거만 연결한다. 기존 DB 보존 및 새 6개 `w3strip_` 테이블 추가 구현의 최종 build/SQL restore 결과, 동일 연구 branch 게시 결과, Drive/Dropbox 업로드 확인은 소스 동결 후 외부 delivery receipt에 기록한다. 이 문서 자체는 그 후속 작업의 성공 확인서가 아니다. 로컬 SQL restore와 원격 upload 확인도 서로 구분한다.

다음 연구 우선순위는 **먼 tail·corner를 포함하는 유한 예산 pilot 및 남은 269셀을 위한 명시적 실행·coverage 계약 확장**이다. 현재 4셀 성공을 그 영역의 수렴·비용으로 일반화하지 않는다. B22 원인 규명, NCP의 비특권 containment와 MPI adapter 결합·실측, 전체 primitive와 최종 D/epsilon gate도 남아 있다. 후속 작업은 이 완료된 4셀을 재실행하지 않고 새 source-bound continuation에서 시작한다.

주요 근거: `SCOPE.json`, `COLLECTION_CONTRACT_KO.md`, `MEASUREMENTS.json`, `runtime/SESSION_RESULT.json`, `runtime/COVERAGE.json`, `PRIOR_SOURCE_PRESERVATION.json`, `HOST_EVENTS.json`, `review/FINAL_REVIEW.json`, `audit_database/INDEPENDENT_REVIEW.json`.
