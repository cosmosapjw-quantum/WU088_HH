# 독립 source 검사기의 portable adaptation

`check_source_portable.py`는 독립 감사에서 사용한 검사기의 배포용 사본이다.
원 checker와 최초 실패 script/log는 수정하지 않았다. 원 checker SHA256은
`1d55fd0951b99e02210ce10b60d8e97e40f90f12729fe98a6eca581e8463062d`이며,
최초 comparator 수정 전 checker SHA256은
`8e35c3865ebae64b497616b5cf8ff85510fbdec461e38cadefdcc5fb7dffb287`이다.

변경은 실행 경로·identity 회수·출력 계약에 한정된다.

- ROOT는 `Path(__file__).resolve().parents[1]`이다. 과거 workspace와 deps의 절대경로 삽입을 제거했다. Package의 `src`만 ROOT에 상대적으로 import한다.
- 외부 parent directory와 bytes를 비교하던 여섯 source/input 검사는 고정 `INPUT_IDENTITY.json`의 각 path/size/SHA256과 비교한다. 여섯 exact 경로와 parent archive identity도 확인한다. 입력을 자기 자신과 비교하지 않는다.
- `--output`이 필수다. 기존 output은 검사 실행 전에 거절하고 최종 JSON도 exclusive create로 쓴다.
- 원 source oracle, formal Lie derivative와 hyperdual 비교식, precision 및 tolerance는 변경하지 않았다. 일곱 계산/비교 함수의 AST identity도 원본과 확인했다.

원 최초 실패는 high-precision scalar를 다시 Arb ball로 바꾼 뒤 그 전체 containment를 요구한 auditor comparator의 문제였다. 그 실패와 이미 수행된 수정은 원 감사 기록에 보존돼 있다. 이번 portable adaptation은 추가적인 tolerance 변경이나 candidate core 수정이 아니다.

배포 파일 루트에서, 의존성 `python-flint`, `mpmath`, `sympy`가 있는 Python으로:

```bash
python -B independent/check_source_portable.py --output NEW_OUTPUT_PATH.json
```

이번에 기존 deps를 PYTHONPATH로 제공하여 portable checker를 정확히 한 번 실행했다.
`results/SOURCE_AUDIT_PORTABLE.json`의 130개 scalar assertion이 모두 통과했고 exit 0이었다.
39 RHS·39 coefficient 비교는 서로 다른 세 scalar 상태의 숫자 검사이며,
40 formal-flow 및 4 nonlinear-HD 성분, 6 source identity 및 2 bin/density 검사와 합친 수다.
독립 science test 130개를 뜻하지 않는다. Native/BE/IVP trajectory 실행은 없었다.

실제 stdout/stderr와 invocation은 `results/SOURCE_AUDIT_PORTABLE.*` 및
`results/SOURCE_AUDIT_PORTABLE_EXECUTION.json`에, 원본/portable checksum과 adaptation 정보는
`independent/SOURCE_AUDIT_PORTABILITY.json`에 있다. 경로가 포함된 실행 기록은 이번 실행의 provenance이며
portable checker의 런타임 의존성이 아니다.
