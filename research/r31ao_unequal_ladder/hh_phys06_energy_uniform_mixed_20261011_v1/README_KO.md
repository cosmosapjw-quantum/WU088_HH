# WU088_HH PHYS06 연구 전달본

이 전달본은 PHYS05 연구 PR #34와 NCP PHYS04 v2를 이어서 만든 PHYS06이다.
새 결과는 에너지 좌표의 HH/photo 구조, binary64 density-leaf 정규화 잔차,
uniform implicit-family의 충분조건과 finite mixed rectangle 적분 정리다.
Actual native endpoint/root/IVP 실행은 0이며 actual W, I_h, continuous error는
아직 null이다. 최종 채택 범위는 `review/DECISION.json`을 따른다.

## 읽는 순서

1. `REPORT_KO.md` — 연구 결론, 실제 검산 결과, 남은 물리 조건.
2. `theory/ENERGY_COORDINATE_KO.md` — 에너지식과 source 정규화 주의점.
3. `theory/UNIFORM_MIXED_RECTANGLE_KO.md` — 증명과 finite interaction 연결.
4. `src/uniform_mixed.py` — exact rational arithmetic reference.
5. `evidence/reference_checks.json`, `evidence/archived_energy_*` — 새 검산.
6. `handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md` — NCP에 그대로 전달할 전체 prompt.
7. `handoff/NCP_TASKS.json`, `handoff/NCP_RETURN_TEMPLATE.json` — 작업·반환 계약.

## 입력과 재현성

`inputs/ncp_v2/`에는 실제 common seed와 필요한 NCP source snapshots, source
hash/commit pins, 기존 완료 evidence 및 초기 정규화 문구의 정정 기록이 있다.
`inputs/phys05/`는 이전 연구 결과·checker·review의 snapshot이다. 이들 과거
checker를 자동으로 실행하지 않는다. 새 검산만 이 전달본의 실행 기록에 포함된다.

새 reference check의 보존된 최초 실행은
`python tools/run_bounded.py reference_first tests/check_reference.py`였다.
`reference_first` 디렉터리는 immutable하여 같은 이름으로 다시 실행할 수 없다.
필요한 변경이 생겼을 때만 새 run id를 주고 관련 검사만 실행한다. Python 3.12
표준 라이브러리로 동작한다. 실제 source에 대한 native root solver는 포함하지 않는다.

## 배포와 복구

ZIP과 그 SHA256, publication commit/tree, 백업 file IDs는 ZIP 밖의
`WU088_HH_PHYS06_DELIVERY_RECEIPT_20261011_v1.json`에 둔다. Receipt를 ZIP 안에
넣어 순환 hash를 만들지 않는다. 동일한 receipt와 시작 안내를 Git delivery
디렉터리 및 기존 Google Drive/Dropbox 백업에도 제공한다.

추가 첨부 없이 시작하려면 `WU088_HH_PHYS06_NCP_START_FROM_BACKUP_20261011_KO.md`의
절차를 따른다. 기존 NCP v2와 이 PHYS06의 commit을 혼동하지 않는다. 복구 확인
후에는 source content changes와 실제 native 실행 권한을 별도로 구분한다.
