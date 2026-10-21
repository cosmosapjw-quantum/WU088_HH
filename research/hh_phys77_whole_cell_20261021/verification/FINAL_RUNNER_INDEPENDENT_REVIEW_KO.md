# PHYS77 최종 runner 독립 검토

**판정: PASS_SCOPED. Blocking bug는 발견하지 않았다.** Source와 기존 증거를 읽었으며 runner, engine, RHS, ODE, 테스트를 실행하지 않았다.

## 최종 source와 검증 binding

- `run_enclosures.py`: `0700ee87672bdf062bd616e256472524caab006a4138f129d8b24e3d0ee2aea4`
- `test_run_enclosures.py`: `e21b138b10ff36941020c38c9ed6effac64d8a13f0fc4e5a19ebdbfdf862b59e`
- 기존 17개 fake-worker contract test receipt의 source·test·log·설명 문서 SHA와 size가 실제 파일과 모두 일치한다. 테스트를 재실행하지 않았다.

## 보존과 identity

최종 변경은 올바르다. 반환된 JSON을 `RESULT_UNVERIFIED.json`으로 먼저 create-only 저장한 뒤, 결과 identity와 호출 후 source/input을 검사한다. 후속 검사에 실패하면 그 JSON과 hash를 `FAILED.json`과 함께 남기고 결과를 채택하지 않는다. 완료 재개는 request bytes, canonical identity, provisional/result equality, receipt seal과 prefix coverage를 검사한다. 손상된 완료를 자동으로 재실행하지 않는다.

Source lock은 실행 중 runner, engine과 local dependency, 외부 PHYS76 transport, 고정 HH74 resource helper를 묶는다. Import 경로와 이미 import된 동명의 다른 module을 검사하고, source/runtime을 호출 전후 다시 대조한다. 실제 entry point는 `cell_enclosure.certify_request`다.

## Lease와 취소 경로

공유 admission 실패 시 독자 실행으로 넘어가지 않는다. Worker 생성 전 lease를 얻고, child PID/start tick에 lease를 넘긴 뒤 gate를 열어 engine 진입을 허용한다. Gate는 child가 종료할 때까지 유지된다. 정상 경로에서는 child 종료와 join 뒤 자신의 lease를 해제한다. 다른 작업에 signal을 보내거나 종료하는 경로는 없다.

Dispatch horizon은 새 작업의 시작을 제한한다. 활성 worker를 강제로 종료하는 timeout이 아니다. 외부에서 dispatcher가 갑자기 종료되면 STARTED만 남거나 종료된 worker의 lease가 다음 protocol 관측에서 정리될 수 있다. 그런 경우를 완료로 표시하지 않는다. 이 제약은 source 설명에 이미 명시돼 있다.

## 최종 배치 확인과 해결 사항

`unit/source/run_enclosures.py`와 `unit/tests/test_run_enclosures.py`는 검증된 파일과 byte-identical하다. Unit이 `research/` 아래에 있는 현재 배치에서 HH74 resource와 인접 PHYS76 transport의 상대 경로가 맞는다.

발견했던 request-directory 혼입 문제는 최종 배치로 해결됐다. Runner는 해당 directory의 모든 JSON을 request로 읽으므로 metadata가 함께 있으면 거부한다. 현재 `inputs/pending_ncp/`에는 세 request만 있다. 원본 manifest와 preparation receipt는 별도 `evidence/`에 byte-identical하게 보존돼 있다. Runner 수정은 필요하지 않다.

최종 source lock SHA는 `8d1bf0ca0ea7467516c9dbd804443b557c67119d73011389a283b11124bd7ebb`다. Root의 기존 로컬 preflight는 eligible 3개, blocked 0개를 기록했다. 당시 quota 8 CPU, RAM 한도 8 GiB, reserve 16 GiB로 admissible slot은 0이었다. 이번 관측의 PID liveness는 true이며, 앞선 false 관측은 과거 기록으로 유지한다. 이는 로컬 preflight 증거이며 **NCP 실행 또는 실제 공유 lease handoff 성공 증거가 아니다**.

## 범위

Advisory lease는 kernel CPU/RSS reservation이 아니다. 공통 host·shared path·PID namespace가 전제이며, NCP handoff는 아직 실행하지 않았다. 이 독립 검토에서 새 테스트·engine·RHS·ODE·benchmark·NCP 작업은 모두 0회다. `HH_R10=OFF`, production admission은 미발급이다.
