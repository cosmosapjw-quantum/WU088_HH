# PHYS15 검산 기록의 범위

이 폴더의 검산은 이론의 대수·차원·시간 순서·정규화 연결을 판별한다. 새로운 WU088_HH physical source·root·history 실행은 없다.

- `photon/PHOTON_EXACT_CHECKS.json`: 원 captured leaf와 제조 spectrum/Jet를 사용하는 exact Fraction 네-slot 검산. 39개 관계, 3148개 scalar equality.
- `photon/SECTOR_SIGN_CHECKS.json`: 원 HI 단면적·heat·birth-redshift 부호 조건의 정확한 비교.
- `NONLINEAR_TRANSFER_CHECKS.json`: 네 변수 quadratic residual과 off-diagonal coupling에서 평균 Jacobian, finite T, 동일 adjoint 및 Neumann 포함을 구별하는 14개 관계.
- `WOLFRAM_ALGEBRA.json`: 실제 Wolfram 명령과 네 유리식의 차가 모두 0인 출력.
- `../review/INDEPENDENT_THEORY_CHECKS.json`: 후보를 import하지 않은 별도 검토자의 26개 항목.

`photon/`는 분과에서 제출한 실행·초기 인계 기록을 원본으로 보존한다. 그 안의 초기 peer-review pending은 제출 시점의 상태이며, 현재 단위의 최종 판정은 `../review/DECISION.json`의 PROMOTE_SCOPED다. 수학 표기 교정의 이전 원고와 교정 원고도 해당 분과 기록에 함께 남아 있다.

재현 시 입력을 변경하지 않고 각 checker의 `--project`·`--output` 인수를 사용한다. 새 결과는 별도 경로에 기록하여 원 실행 결과를 보존한다. 문서화된 일반 증명과 실제 출력의 적용 범위를 함께 읽는다.
