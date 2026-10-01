# G3 독립 artifact 검토

검토자는 `/root/review_gram`이며 구현 담당자와 분리된 구성요소 검토다.
`independent_review_admitted=false`를 유지한다. 이 문서는 프로젝트의 독립
과학 판정 심사를 대체하지 않는다. 실제 HH 배열·상수·적분·옛 comparator를
실행하지 않았고, 원 구현은 수정하지 않았다.

핵심 수학과 구현에서 부정확한 enclosure나 판정 반례는 발견하지 않았다.
다만 사용자 지정 중간 정수 크기 제한을 우회하는 경로 한 건을 재현했다.
Root가 두 발생 지점을 수정한 뒤 원래 재현만 제한적으로 다시 실행하여
해당 finding이 닫혔음을 확인했다. 실제 과학 인증은 이번 검토 범위 밖이다.

## G3-R01 / B10 RESOURCE_CAP_BOUNDARY — P2, 자원 계약

`exact_gram/engine.py`의 `_sqrt` 188–191행은 `max_work_bits` 검사보다 먼저
`pn*pn`과 `pd*pd`를 계산하고 perfect-square이면 조기 반환한다.

```python
sqrt_interval(Fraction(2**200), limits=Limits(max_work_bits=8))
```

이 호출은 `2**100`을 반환한다. 그 전에 계산하는 `pn*pn`은 201-bit 정수다.
따라서 선언된 8-bit 중간 곱 제한이 적용되지 않는다. 수학적 결과는 맞다.
기본 설정의 `max_integer_bits`는 여전히 입력과 작업량의 유한 상한을 주며,
이번 문제는 기본 설정의 enclosure를 반박하지 않는다.

최소 수정은 제곱 판별 곱을 만들기 전에 해당 크기를 검사하거나, 모순되는
`Limits` 조합을 생성 시점에 거절하는 것이다. `round_binary64`의 지수 판별
shift도 제한 검사보다 먼저 실행되므로 같은 자원 계약을 일관되게 적용해야
한다. custom-small-cap 회귀 검사를 추가하면 이 finding을 닫을 수 있다.

추가로 `round_binary64`에 합성 입력 `2**200`과 `2**(-200)`,
`max_work_bits=8`을 주고 실행 행을 관측했다. 두 경우 모두 201-bit alignment
shift를 포함한 비교가 완료된 뒤 다음 행에 도달했고, 그 후에야
`ResourceLimit`가 발생했다. 잘못된 결과는 반환하지 않으므로 output fail-closed는
유지되지만 allocation 전 cap은 지키지 않는다. 이 두 건의 제한된 재현은
`alignment_cap_probe.py`와 `.json`에 보존했다.

수정 후 검증: root는 `_sqrt`의 첫 `isqrt`보다 먼저 입력의 numerator/denominator
bit size와 square-test 여유를 검사하고, `round_binary64`는 exponent alignment
shift보다 먼저 예상 크기를 검사하도록 변경했다. 독립 검토자는 원래
perfect-square 입력 1건과 alignment 입력 2건만 다시 실행했다. 실행 행 관측으로
`isqrt`/square shortcut 및 alignment 비교에 도달하기 전에 `ResourceLimit`가
발생함을 확인했다. **B10은 이 수정 범위에서 implementation-verified로 닫혔다.**
광범위한 8,000-case 검사는 반복하지 않았다. 최초 실패 증거는 보존하며,
수정 후 결과는 `sqrt_cap_postfix.json`, `alignment_cap_postfix.json`, 변경된
source identity는 `REVIEW.json`의 `postfix_closure`에 있다.

## 확인된 근거

- Exact sqrt 800개 입력에서 `lo² ≤ q ≤ hi²`, 비음수 하한과 dyadic 폭을
  exact rational arithmetic으로 별도 확인했다.
- 양·음의 binary64 지수 전 범위를 샘플한 midpoint/quarter/endpoint 8,000건에서
  독립적인 Python `Fraction → float` 변환과 RNE bits가 일치했다.
- 합성 복소 행렬 100개에서 반환된 상한 제곱에 대해 `u² I − G`의 두 대각 원소와
  행렬식의 비음수성을 exact arithmetic으로 검사했다. 하한은 최대 고유값 이하인지
  대각 하한 또는 characteristic polynomial의 부호로 검사했다. Adjoint norm도
  일치했다. 이 검사는 근사적인 고유값 oracle에 의존하지 않는다.
- 기존 합성 테스트 20개도 통과했다. 실행 종료 코드는 0이다.
- 계약의 canonical source 6개 모두 byte count와 SHA256을 다시 확인했다.

`K_raw=(C−R†)/2`를 exact하게 만들고 `K_prediction`은 저장 필드를 사용하는
구분은 기준 `DECISION_BOUND_DERIVATION.md`와 일치한다. Dmax interval max,
PRIMARY/SECONDARY의 other-minus-local 방향, source disk의 Frobenius 상한,
`epsilon_K=(epsilon_C+epsilon_R)/2`, `epsilon_Dmax=max(epsilon_C,epsilon_R)`,
`g_minus−2 epsilon`, legacy eta의 중복 계상 방지도 타당하다.

Pinned PRIMARY source의 `RNE(other−local)>tol`과 SECONDARY source의
`local<RNE(other−tol)`은 실제로 다르다. 기존 synthetic witness를 독립적으로
재현했고 두 코드 경로의 판정이 각각 true/false인 것을 확인했다. 새 arithmetic
helper는 real Pareto sufficient condition과 frozen machine trace를 분리하며
`machine_predicate_certified=false`, `continuous_target_certificate=false`를
남긴다. 이 분리는 적절하다.

실제 archived scalar bits, 역사적 rounding mode, HH target disk, epsilon,
ABI 및 전체 certificate admission은 검증되지 않았다. 현재 증거를 이들
의무가 닫힌 것으로 승격할 수 없다. `certified_epsilon=null`,
`certified_eta=null`, `rigorous=false`를 유지한다.

재현 파일은 `review_gram/independent_checks.py`, 실행 결과는
`independent_checks.json`, 기존 suite 기록은 `existing_suite.log`, 입력 identity와
finding의 기계 판독 기록은 `REVIEW.json`에 있다.
