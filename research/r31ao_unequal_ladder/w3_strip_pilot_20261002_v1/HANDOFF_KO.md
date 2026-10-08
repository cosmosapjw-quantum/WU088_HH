# W3 strip pilot 인계

선택한 한 단계는 완료됐다. 기존 W1 16셀을 재사용하고 셀 `20,52,105,57`의 실제 native 적분을 각 1회 실행하여 모두 `RADIUS_MET`를 얻었다. `runtime/SESSION_RESULT.json`은 `PILOT_COMPLETE`이며 새 실행 4회, accepted 부분 coverage 20/289, missing 269다. 이 완료된 과학 계산을 다시 실행하지 않는다. `RUN_STARTED.json`의 영구 재실행 방지 기록을 유지한다.

기준 branch는 `research/r31ao-unequal-order-ladder-20260930`, 기준 commit은 `48443cd754329cd6b76c99f6e9e887081df1e29e`다. 준비 계약 hash는 `8754c55599db81518438c2a2b72aa5728136ba1bf82fbefb8ef055f421bc5d33`다. 신규 source는 이 디렉터리에만 추가했고 기존 W1·W3 243파일의 SHA·크기·mtime을 보존했다.

독립 최종 검토는 `PASS_SCOPED_PARTIAL_INTERIOR_WITH_OPEN_HOST_EVENT`다. 부분 합의 최대 component radius 약 2.3365004605418634e-20은 20셀 합집합에만 적용된다. Missing 269셀을 0으로 간주하거나 기존 endpoint 상계를 더해 전체 적분으로 표시하지 않는다. Endpoint 포함, normalization, 전체 D/epsilon, scientific/production admission은 false다.

B22는 열려 있다. 셀 105는 완료 시와 후속 readback 모두 `.claim`이 관측됐고 셀 57은 완료 시에는 없다고 기록됐으나 후속 readback에서 관측됐다. 두 파일과 원 기록을 유지한다. Root cause는 `UNDETERMINED`이며 파일을 삭제·격리하거나 자동 재시도하지 않는다. 수치 검증 통과와 host lifecycle 완결은 구분한다.

남은 이번 delivery 절차:

1. 이 보고서·stage delta를 포함하여 `PUBLICATION_CONTENTS.json`을 만든 뒤 source tree를 동결한다.
2. 고정된 직전 W3 SQLite의 기존 19개 테이블과 schema/rows를 보존하고 새 6개 `w3strip_` 테이블을 추가한다. 결과와 local SQL restore 검증은 이 source tree 밖에 기록한다. Source 변경 후 기존 동결 결과를 그대로 사용하지 않는다.
3. 동일 연구 branch에 additive tree를 게시한다. 이전 tree 항목을 모두 보존하며 HEAD를 확인하고 nonforce update를 사용한다. Main merge는 하지 않는다.
4. ZIP·SQLite·보고서·delivery receipt를 기존 Drive/Dropbox 목적지에 create-only로 백업하고 개별 파일 ID·이름·크기를 확인한다. 원격 업로드 검증을 원격 복원 검증으로 표현하지 않는다. 게시·백업 결과는 외부 receipt를 정본으로 확인한다.

다음 연구 단계는 먼 tail·corner bounded pilot과 남은 269셀의 명시적 실행·집계 계약 확장이다. 현재 collector는 기존 16셀과 이번 고정 4셀만 받는다. 새 작업에는 별도 continuation, 제한 예산, source/plan binding과 coverage 근거가 필요하다. 이번 27.705733198초는 prepare를 제외한 2-worker campaign이며 직렬 비교·NCP/MPI benchmark가 아니다. NCP/OpenMPI/Fortran/벡터화 검증이나 전체 primitive 승격을 이 결과로 대체하지 않는다.
