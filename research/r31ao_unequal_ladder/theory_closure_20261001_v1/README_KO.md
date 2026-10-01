# 이론 증명 패키지 읽기

`RESEARCH_REPORT_KO.md`가 결과 요약이고 T1–T5 본문이 전체 증명이다.
`THEORY_CLOSURE_LEDGER.json`은 기존 36개 의무의 상태를 보존하면서 새 증명 위치를
대응시킨다. 독립 검토 결과는 `INDEPENDENT_THEORY_REVIEW.*` 및
`T3_INDEPENDENT_REVIEW.*`에 있다.

선택한 source-defined 연속 목표 경로에서 확인된 추상 정리 의무를 해소했다.
정리의 입력 전제를 실제 파일·ABI·backend에 연결하고 실제 수치 구간을 산출하는
일은 별도이다. 이 패키지에는 실제 HH 데이터가 들어 있지 않으며 수치 실행의
새 권한을 부여하지 않는다. 실제 epsilon/eta는 null, rigorous는 false다.

합성 검산만 재현하려면 압축을 풀어 디렉터리 구조를 유지하고 다음을 실행한다.
Python 표준 라이브러리만 필요하며 실제 입력·네트워크·native library는 사용하지 않는다.

```sh
cd research/r31ao_unequal_ladder/theory_closure_20261001_v1/theory_checks
python -B t1_test_bounds.py
python -B t2_exact_checks.py
python -B t3_test_predicate.py
python -B t4_constructive_checks.py
python -B t5_test_sharp_residual.py
```

T3/T5는 함께 포장된 이전 `gap_closure_20261001_g0_g6_v1/exact_gram/engine.py`를
SHA256 검증 후 합성 행렬/스칼라에만 사용한다. 그 엔진의 기존 자원 한도와
임의 자원 증가를 허용하는 수학적 존재 정리는 구별한다.

패키지의 `PACKAGE_MANIFEST.json`은 새 파일과 재현에 포함한 이전 파일의 hash를
기록한다. 이전 파일은 그대로 복사되며 새 Git commit에서는 게시하지 않는다.
`BACKUP_RECEIPT.json`은 자신이 증명하는 ZIP 내부에 넣지 않는다. 게시 commit/tree와
백업 ID의 최종 결박은 별도 `DELIVERY_RETURN.json`에 있다. 백업 성공은 업로드 및
대상·크기 확인 수준이며 별도 복구 시험을 뜻하지 않는다.
