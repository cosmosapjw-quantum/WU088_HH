# PHYS02 재현

완료 결과를 읽는 데는 재실행이 필요하지 않다. 새 환경 수입은 `MANIFEST.json`과 입력 identity 검사로 시작한다. 아래 경량 suite는 검증할 이유가 있거나 독립 재현을 요청받았을 때 새 빈 출력 디렉터리에 실행한다. 원 evidence 파일은 덮어쓰지 않는다.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -B verify_delivery.py
.venv/bin/python -B reproduce.py --output /absolute/path/NEW_EMPTY_PHYS02_RESULTS
```

`reproduce.py`는 패키지를 새 출력 하위 staging으로 복사하고, 14개 새 단위시험, 256 bit remainder 상계, 독립 4차 유리수 fixture, portable source oracle을 실행한다. 이전 PHYS01, native, BE, IVP trajectory, NCP 또는 원자 적분을 호출하지 않는다. 384 bit 비교는 이미 동봉된 선택적 roundoff 점검이며 기본 재현에서 중복 실행하지 않는다.

직접 한 상계만 평가하려면:

```bash
.venv/bin/python -B bound_remainder.py --output /absolute/path/NEW_REMAINDER.json
```

기본은 h=1.25e9 s와 precision=256이다. 다른 `--h-seconds`는 새 분석으로 취급한다. 원 frozen guard나 모형을 변경하지 않으며, 실패는 값을 잘라내거나 허용치를 바꾸지 않고 반환한다. 이 옵션 자체가 새로운 실제 owner 시간 단계의 사용 승인은 아니다.

exact binary64 leaf constants와 mathematical pow/exp를 사용한다. Native per-operation rounding을 재현하는 프로그램이 아니고, 16 zero-sigma photon 좌표의 제거는 수학적으로 exact이다. 입력/소스는 원본 그대로 포함되어 있다.

`independent/source_audit_checks.py`와 초기 실패 스크립트는 당시 실행한 원본 보존물이라 원 workspace 경로를 포함한다. 실행 가능한 이동용 검사는 `independent/check_source_portable.py`이며 경로와 output·identity 읽기만 이동 가능하게 바꿨다. 원 과학식·비교와 기준은 보존했다.

환경·원 실행·실패·수정·최종 독립 판단은 `results/`, `logs/`, `failures/`, `independent/`에서 구분한다. 최초 `REMAINDER_256_INITIAL.json`의 endpoint 표시문자열은 outward certificate가 아니며, `_FINAL`의 exact dyadic/direct decimal endpoint가 정본이다.
