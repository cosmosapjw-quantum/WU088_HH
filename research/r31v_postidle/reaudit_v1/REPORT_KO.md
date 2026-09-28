# R31V 적대적 재감사 v1

## 범위와 판정

대상 HEAD는 `7472171a3ff0e343dab2131cf063082e4740f7ff`, tree는 `b2bae4e294f06de3a567ef8fdc519f3bfd4385a8`이다. 원 실행은 `20260928T132239Z_r31v`이다. 이 대화에 과거 결론과 구현 이력이 이미 노출되어 있으므로 이번 검토는 완전한 blind 또는 독립 reviewer admission이 아니다. 판정 문서를 증거로 재사용하지 않고 source-first 반례 검사와 raw JSON 재계산을 수행했다. 외부 CodeRabbit은 CLI 부재와 설치 호스트 DNS 실패로 실행하지 못했다. 별도 엔진 검토 결과는 0건이다.

최종 상태는 `ADVERSARIAL_REAUDIT_COMPLETE_CONTROLS_FIXED_NCP_REVALIDATION_PENDING`이다. 완료된 M3B를 폐기하거나 새 heavy run을 요구할 근거는 발견하지 않았다. 단, 이전의 독립심사 종결 표현은 적격 reviewer admission을 뜻하지 않는다. production/provider/full49/trajectory gate는 계속 닫혀 있다.

## 재현된 구현 문제

현재 HEAD의 원래 focused tests는 72/72 통과했다. 별도로 작성한 첫 반례군은 43 tests 중 40 실패, 3 통과였다. 이는 40개의 독립 버그라는 뜻이 아니라 다음 세 문제군의 재현 사례 수다. 32건은 거절해야 할 변형이 통과했고, 8건은 거절되지만 AttributeError로 잘못 분류됐다.

**F01, 중요: 측정 완료 gate가 관측 이상을 승인했다.** `perform_measured_batches`는 leaf throttling과 일부 CPU engagement만 검사했다. memory high/oom, swap, ancestor throttling, 관측 누락, truthy non-boolean exactness, 잘못된 task count, 비유한 시간·처리량·CPU 값 등의 15개 변형이 성공 경로로 통과했다. raw 계측을 수집한다는 것과 실제로 그 값을 검사한다는 것은 달랐다. timed-row 검사와 rejection checkpoint를 추가했다. NaN/Inf는 정상 숫자로 바꾸지 않고 명시적 tagged failure JSON으로 보존한다. 이 수정은 timed-row gate이며 범용 자원 격리·감시 시스템을 구현한 것이 아니다.

**F02, 중요: pilot의 잘못된 메모리 관측을 버리고 승인했다.** `observed`에서 유효한 정수만 남기던 코드 때문에 PSS 누락, None, 음수, NaN, bool, 문자열 등의 이상이 startup 값 하나로 가려졌다. True가 1과 같은 Python 비교도 1x1 검사에 들어갔다. object/type/geometry 및 두 메모리 관측을 명시적으로 검사하도록 수정했다. malformed object 8건의 AttributeError는 ValueError로 분류했다. 기록된 PSS 기반 engineering estimate를 rigorous peak/private-memory upper bound로 부르지 않는다.

**F03, 중요: exactness의 요약과 세부 기록의 모순을 승인했다.** top-level/row `all_exact=true`가 component false, nonzero/NaN delta, component 누락, 잘못된 shape/dtype, 모순된 duplicate row를 가렸다. required n/g/z/pair 집합과 중복 여부, 네 component의 dtype/shape/exact/max_abs_delta를 검사하도록 수정했다. 이는 기록의 내부 일관성 검사이지 candidate 배열 재계산 또는 서명 인증이 아니다.

원 kernel, H0, grid, native arithmetic, tolerance, reference cache numerical context는 수정하지 않았다. 기존 synthetic control-flow fixtures는 실제 batch가 제공하는 resource/component 필드를 포함하도록 보강했다. 검사를 약화시켜 GREEN으로 만든 것이 아니다.

## 실제 검증

수정 후 47개 새 tests, 72개 기존 R31V tests, 14개 관련 R31S tests를 합쳐 **133/133 통과**, pytest exit 0이다. py_compile과 describe도 성공했다. Python 3.13.5, NumPy 2.3.5, SciPy/pytest 및 플랫폼 identity는 RESULT.json에 있다. 이 검증은 ChatGPT sandbox의 경량 구현 검증이며 NCP Python 3.12/GCC 13 환경 검증이 아니다. 이전 84 PASS나 앞선 답변의 별도 validator 실행 주장을 새 HEAD 증거로 가져오지 않았다. 앞선 답변에는 그 별도 실행의 durable log가 제시되지 않았으므로 이번 actual logs로 대체한다.

원 M3B의 12 timed rows는 강화된 검사에도 모두 통과했다. 7개 RETURN-bound 파일의 size/SHA, reference context, 12개 cache payload, preparation/benchmark 분리, workload identity, worker task/CPU 합계 및 affinity/team 기록을 대조했다. 처리량과 median은 원 기록과 일치한다. 32x2 median은 0.8240526251440508 tasks/s, 30x2는 0.7988149948941909 tasks/s로 관측 차이는 3.1593836384%이다. 이는 해당 실행의 기술통계다. 세 반복의 CV를 신뢰구간으로 쓰지 않는다. 구성 순서가 고정되어 있어 n/workload/order/host 효과를 분리한 원인 실험도 아니다.

## 철회·제한할 해석

**F04, 증거 해석:** root CPU delta minus leaf CPU delta가 12개 중 10개에서 음수였다. 최소값은 약 -88.23 CPU-seconds다. 이 기록만으로 원인을 확정하지 않는다. ancestor와 leaf는 동시 계측도 아니므로 기존 `other_session_cpu_upper_seconds`라는 이름을 엄밀한 타 세션 사용량 상계로 받아들이지 않는다. 원문은 보존하고 재분석에서는 `observed counter difference`로만 표기했다. host 독점성 인증이나 interference bound는 아직 없다.

**F05, provenance:** 기존 FILE_MANIFEST.json은 최초 R31V checkpoint를 가리켜 현재 driver/test 두 파일과 다르다. 이를 corruption으로 오인하거나 무조건 현재 manifest PASS라고 하면 안 된다. 원본은 보존하고 새 REVIEWED_FILES.json이 이번 범위의 현재 bytes를 명시한다. 원 NCP 실행 시점의 즉시 source-tree attestation을 사후에 새로 만들었다고 주장하지 않는다.

**F06, 독립성·exactness:** timed candidate 출력 배열은 전부 보존되어 있지 않다. 이번 검토는 runtime exactness summaries, comparator source, serial reference cache를 검증한 것이다. 1,584개의 candidate 계산을 독립 재실행해 equality를 증명한 것이 아니다. 5,178 native calls도 source dispatch에서 유도한 수이며 독립 계측기의 호출 count가 아니다. 같은 대화의 재감사와 테스트 PASS만으로 적격 blind reviewer를 대신할 수 없다.

## 다음 단계와 금지

새 CODEX_HANDOFF_KO.md를 사용한다. 새 reviewer에게는 BLIND_REVIEW_BRIEF_KO.md와 허용된 source/raw 자료만 먼저 제공한다. 리뷰를 hash로 동결한 뒤 이 보고서 및 새 tests와 비교한다. 동시에 NCP에서는 새로운 source SHA를 기록하고 focused 133-test 범위와 raw replay만 수행한다. 수정이 더 필요하면 failing test와 최소 patch를 보존한다. 독립 reviewer가 없으면 그 admission만 명시적으로 미완료로 남긴다.

새 M3B/reference preparation, M3A, z=1/z=0.5/full144/trajectory/M5, provider promotion, main merge, force push, 다른 owner PID 조작을 승인하지 않는다. 기존 raw와 core archive는 변경하지 않았다. 정상 R1 publication/backup receipt가 닫히면 검증 반복을 중단한다.
