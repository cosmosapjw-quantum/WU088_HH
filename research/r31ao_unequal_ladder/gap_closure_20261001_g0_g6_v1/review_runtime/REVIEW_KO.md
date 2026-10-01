# Host guard·synthetic interior pilot 제한 검토

읽기 전용 artifact 검토이며 `independent_review_admitted=false`다. 실제 HH
실행, native compile, 새 Petras draft 및 광범위 재감사는 제외했다. 구현 원본을
수정하지 않았다. 기존 guard 4개와 pilot 21개 테스트는 종료 코드 0으로 통과했다.

## RUNTIME-R01 / B13 — 남은 descendant의 wall-time 제한 누락, 수정 확인

Process-tree wall guard 관점에서는 P1, 문서에 적힌 single-process scope에서의
계약 강제 관점에서는 P2다. `run_guarded`는 직접 child인 leader의
`process.wait(timeout=...)`만 관측한다. Leader가 자식을 생성한 뒤 먼저 종료하면
그룹에 남은 자식이 있어도 `PROCESS_COMPLETED`를 반환하고 wall timeout을
더 이상 감시하지 않는다.

제한된 합성 재현에서 parent는 같은 process group의 child를 만들고 즉시
종료했다. Child는 0.6초 후 sentinel을 쓰고 종료하도록 했다. Wall cap 0.2초인
guard는 약 0.033초에 성공을 반환했으나, 반환 직후 그룹이 살아 있었고 cap 이후
sentinel이 실제 생성됐다. 그룹 이탈은 사용하지 않았다. 모든 작업은 합성 입력이며
child의 수명도 유한하다. 재현 코드와 관측치는 `guard_descendant_probe.py/json`에
보존했다.

최소 수정은 leader의 정상/비정상 종료 및 예외 경로에서도 남은 process group을
정리한 뒤 output snapshot과 receipt를 작성하는 것이다. Descendant 정리 또는
single-process contract 위반을 별도 상태로 기록해야 한다. 대안으로 Linux job
boundary 전체를 deadline까지 감시할 수 있다. 단순히 단일 프로세스라고 부르는
것만으로 해당 제약이 강제되지는 않는다. 이 누락은 과학 결과의 정확성 오류가
아니지만, 기록 이후에도 output이 바뀔 수 있는 실행 수명 문제다.

Root 수정 후 원래 재현만 다시 실행했다. Guard는 이제 남은 process group에
SIGKILL을 보내고 `PROCESS_CONTRACT_VIOLATION`을 반환했으며, cap 이후 sentinel이
생성되지 않았다. `finally`의 예외 경로에도 group cleanup이 존재함을 source에서
확인했다. **발견된 B13 경로는 implementation-verified로 닫혔다.** 최초 실패 증거를
보존하고 `guard_descendant_postfix.json`에 수정 후 결과를 기록했다.

측정상의 제한: 반환 직후 `killpg(pid,0)`는 여전히 성공했다. 이는 process group의
존재만 관측하며 zombie나 pending termination도 포함할 수 있으므로, 계속 실행
중이라는 증거나 모든 descendant가 완전히 reap됐다는 증거로 해석하지 않는다.
이번 closure는 계약 위반을 성공으로 보고하지 않고, 재현된 지연 실행을 차단한
것에 한정한다. 수정 source의 SHA256은 `REVIEW.json`에 별도로 기록했다.
최초 hash 수집 전에 root의 동시 수정이 반영됐으므로, 저장된 guard hash는
수정 후 identity다. 수정 전 hash는 확보하지 못했으며 이를 null로 명시했다.
최초 실패 관측을 수정 후 hash에 귀속시키지 않는다.

## 확인된 나머지 의미론

`RLIMIT_AS`는 per-process virtual address space이며 aggregate RSS가 아니라는
구분이 코드와 receipt에 명시돼 있다. CPU cap도 per-process, 파일 크기 제한은
per-file이다. Parent의 stdout/stderr preview는 각각 최대 65,536 bytes를 읽는다.
Leader가 살아 있는 상태에서 timeout이 발생하면 그룹에 SIGKILL을 보낸다.

Pilot의 `RangeClaim`은 요청된 전체 integration panel과 전체 complex parameter
rectangle이 일치하고 `uniform=True`이며 proof reference가 있어야 한다. 임의의
callback 선언의 수학적 진실까지 engine이 증명한다는 주장은 없으며, 이 구분은
적절하다. Nested toy의 inner enclosure는 전체 outer panel에 대한 image이고,
unused outer parameter에 대해서는 상수이므로 uniform claim이 타당하다.

Shared `Budget`은 inner 작업을 합산한다. Parent contribution은 두 자식이 모두
성공하고 replacement가 검증된 뒤 교체한다. 교체 계산은 같은 exact endpoint를
빼므로 interval subtraction에서 생기는 불필요한 확대를 일으키지 않는다.
ResourceLimit의 partial subdivision에서 이전 complete total을 보존하는 것도
타당하다. Domain/contract/implementation 실패에서는 결과를 폐기한다.

이 경계를 직접 확인하려고 우측 자식 callback 3번째 및 5번째 호출에서
ResourceLimit를 발생시키는 두 합성 사례를 실행했다. 각각 마지막 complete
enclosure `[0,1]`, `[1/8,5/8]`를 유지하여 exact integral `1/3`을 포함했고,
종료 후 shared budget의 live panel/state count는 모두 0이었다. 코드는
`pilot_partial_probe.py`, 결과는 `.json`이다.

Cooperative wall checks, tracked-state estimate, hard process limits의 구분은
적절하다. 이 pilot의 결과를 실제 HH feasibility나 rigorous reference certificate로
승격할 근거는 없다. 입력 source identity와 machine-readable finding은 `REVIEW.json`에
기록했다.
