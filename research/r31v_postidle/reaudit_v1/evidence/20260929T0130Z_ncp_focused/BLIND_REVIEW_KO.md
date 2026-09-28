# R31V 제한된 독립 검토 (동결본)

- 대상: commit `928470d4cc9e969dac85b5f1524375f816128489`, tree `6b4dbc30b14bfddbed5c1980bef04b0cfd95f442`. 이 값은 orchestrator 제공이며 Git 접근 금지로 직접 검증하지 못했다.
- 세션: `CODEX_SESSION_ID=01a0e802-64fc-7a62-b4bc-92348b99629c` (환경 변수 관측). 별도 agent 문맥에서 검토했으나 harness 신원과 공식 reviewer admission은 독립 증명되지 않았다.
- 노출: task의 commit/tree·blind 경계, 사용자 AGENTS.md, 허용된 HOST_INVENTORY의 과거 프로세스 명령줄. 구현 보고서, 새 테스트, PR 논의 및 금지된 작업 디렉터리는 읽지 않았다.
- 읽은 파일의 SHA-256은 [BLIND_REVIEW.json]에 모두 기록했다. native kernel 실행, benchmark 재실행 및 소스 변경은 없었다.

## 관측과 범위

준비 기록에는 12개 `EXPLICIT_REFERENCE_COMPUTE`, benchmark 기록에는 같은 순서의 12개 `CACHE_READ`가 있다. 두 기록의 numeric context, pair set, 132-task workload가 일치한다. 복사된 12개 cache 파일은 context·pair·payload digest가 일치하고 H0/foreign 및 두 sumabs 배열의 기록된 dtype·shape를 가졌다. 64×1, 32×2, 30×2, 4×16의 각 3회 측정은 132 tasks와 12 unique pairs, `all_exact=true`, throttling 및 memory event 증가 0을 기록했다. 중앙 throughput은 각각 0.748270, 0.824053, 0.798815, 0.552832 pairs/s다. cgroup 사용량은 공유 계층의 관측이며 독점 실행 증거가 아니다.

## Findings

1. **BR-01 — 실행 소스 귀속 누락 (medium).** `m3_postidle.py:296-310`의 state에는 adapter 자신과 `controls.py`의 해시 또는 Git commit/tree가 없다. 두 버전의 control code가 동일한 numeric context와 schema를 낼 수 있다. 현재 raw만으로 exact reviewed code가 실행됐다고 증명할 수 없다. 준비와 benchmark 생성 시 두 파일의 SHA-256 및 commit/tree를 함께 기록하고 별도로 대조해야 한다.
2. **BR-02 — 준비·측정 사이 cache byte 연결 누락 (medium).** `controls.py:210-254`, `m3_postidle.py:346-361`에서 cache의 payload digest는 로컬 작성자가 갱신할 수 있으며 두 phase 기록에 각 entry의 고정 digest가 없다. 준비 이후 entry를 바꾸고 digest를 다시 계산하면 read는 수용한다. 실제 변경의 증거는 없다. 준비 완료 시와 측정 read 시 pair별 cache SHA-256을 기록하고 동등성을 요구해야 한다.
3. **BR-03 — 초기 입력 오류 checkpoint 누락 (low).** `m3_postidle.py:272-298`에서 layout 변환은 state 생성보다 앞선다. NumPy가 없는 로컬 Python에서 inert `controls` stub을 주입한 경량 검사는 `--configs 64x1,bad`가 `ValueError`로 끝나고 `--out`이 생성되지 않음을 재현했다. native import는 없었다. preflight 전 최소 시도 기록을 만들고 실패를 기록해야 한다. 직접 스크립트 실행은 NumPy 부재 때문에 import 단계에서 막혔다.

## 미검증

복사본 밖의 원 C++/binary byte, 실제 compiler·CPU·precision의 재측정, native scalar arrays와 sumabs 재계산, host 전역 독점성, 현재 시점의 grant 유효성 및 production/scientific admission은 확인하지 않았다. SOURCE_BUILD_AUDIT의 source/build/ABI 항목은 기록으로 검토했으나 원본을 재해시하지 않았다. Pilot/equality receipt의 6개 sample은 metadata로만 검토했다. 심각한 실제 오작동을 관측하지 않았다는 사실은 production 승인과 다르다.
