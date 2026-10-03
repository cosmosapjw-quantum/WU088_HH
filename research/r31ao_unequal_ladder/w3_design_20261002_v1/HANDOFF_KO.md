# 재개 지점

한 단계 완료: 하단/상단 endpoint 분리로 primitive 0의 `[1/512,2^40]^2` cutoff를 선택하고 기존 엔진으로 교차확인했다. `REPORT_KO.md`, `MEASUREMENTS.json`, `runtime/*_RECEIPT.json`, 독립 `review`부터 읽는다.

실행 재시도 금지: 이 차수의 selector 1회, crosscheck 1회는 모두 성공했다. `run_bounded.py`의 STARTED/receipt/result를 삭제하거나 이름을 바꿔 재실행하지 않는다. 기존 W1/W3 성공 계산도 재실행하지 않는다.

다음 연구 단계는 `FUTURE_INTERIOR_DESIGN.json`의 289타일 중 기존 W1 16타일을 검증해 재사용할 collector 계약과, 새 strip의 작은 대표 pilot이다. 이 JSON은 기하 및 조건부 오차 배분 설계이며 실행 가능한 기존 collector plan이 아니다. 새 타일 273개를 바로 전체 실행하지 말고 bounded pilot으로 비용·수렴 근거를 먼저 얻는다. 원 signed107·128bit·basis·geometry·final tolerance는 보존한다.

엔진/host/source pin은 현재 복구 snapshot의 계약이다. NCP64 접속·MPI 결합·portability는 이 차수에서 검증되지 않았다. 원 DB 복구 공백, 전체 D/epsilon, scientific/production admission, B22 원인 미확정은 열려 있다. DB와 delivery receipt의 보존·게시·백업 상태는 실제 기록을 사용한다.
