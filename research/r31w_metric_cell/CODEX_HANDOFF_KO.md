# Codex handoff: R31W 경량 연구 재현과 cell 적용성 판정

목표는 제공된 연구 코드를 검토·재현하고 다음 이론 계산에 필요한 기존 입력을 확인하는 것이다. M3B 재실행이나 controls 재감사가 아니다. 기존 NCP134 PASS를 새 R31W PASS로 가져오지 않는다.

## Authority

Repository: cosmosapjw-quantum/WU088_HH
Research branch: research/r31w-covariant-metric-20260929
Pinned parent: b05db60ff8db75ed6bb2497bffea8b87f57617be
Parent tree: f90e638d3a33a2dcf5a44b32ab77dc1e03111f7e
Base: codex/r31v-postidle-controls-20260928 (PR14)

새 branch의 실제 remote HEAD/tree와 companion PUBLICATION_RECEIPT.json을 대조하라. 이후 commit이 있으면 diff를 읽고 갱신하며 과거 SHA로 reset하지 않는다. 기존 dirty worktree/raw는 보존하고 새 detached worktree 또는 분리된 publication worktree를 쓴다. R31V runner와 기존 source/evidence를 수정하지 않는다.

먼저 REPORT_KO.md, SOURCE_PINS.json, FILE_MANIFEST.json, metric_cell.py, replay_snapshot.py를 읽어라. Git manifest는 covered code/contracts에만 적용하며 archive evidence/root tree 전체의 hash라고 하지 않는다. 정확한 full derivation은 companion archive THEORY_KO.md에 있다.

## 최소 재현

Companion archive WU088_HH_R31W_METRIC_CELL_20260929_v1.zip의
  overlay/research/r31w_metric_cell/inputs/EXISTING_METRIC_INPUTS.npz
를 새로운 read-only 입력 경로로 꺼낸다. 경로를 추정하지 말고 실제 unzip 목록과 extraction root로 확인한다. 다른 snapshot이나 synthetic arrays로 대체하지 않는다. 입력은 71481 bytes, SHA256
  565a9ee6d831f5f9e3e69010270f5319aa3328432950efcfda81cfabf325c079
이다. Git에는 이 binary가 없으므로 test_replay_snapshot.py 실행 전에 WU088_R31W_INPUT을 명시해야 한다.

기존 NCP venv /root/wu088_hh_ncp_work_v2/venv/bin/python의 존재를 확인한다. 존재하지 않으면 검증된 프로젝트 환경을 찾고 없으면 ENVIRONMENT_BLOCKED로 끝낸다. 자동 package 설치/native build를 시작하지 않는다. SciPy는 필요한 의존성이며 Python/NumPy/SciPy/pytest의 실제 version을 기록한다.

다음 PY,RUN,SNAPSHOT은 확인된 절대 경로로 설정한다. RUN은 mktemp 등으로 새로 만든 경로다. run 함수는 실패 exit와 stdout까지 보존한다.

```bash
set -euo pipefail
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
export PYTHONPYCACHEPREFIX="$RUN/pycache"
export WU088_R31W_INPUT="$SNAPSHOT"
run() {
  local name="$1"; shift
  printf '%q ' "$@" > "$RUN/$name.command"; printf '\n' >> "$RUN/$name.command"
  set +e
  "$@" > "$RUN/$name.log" 2>&1
  local rc=$?
  set -e
  printf '%s\n' "$rc" > "$RUN/$name.exit"
  return "$rc"
}
run COMPILE "$PY" -m py_compile \
 research/r31w_metric_cell/metric_cell.py \
 research/r31w_metric_cell/replay_snapshot.py \
 research/r31w_metric_cell/test_metric_cell.py \
 research/r31w_metric_cell/test_replay_snapshot.py
run TESTS "$PY" -m pytest -q -p no:cacheprovider \
 research/r31w_metric_cell/test_metric_cell.py \
 research/r31w_metric_cell/test_replay_snapshot.py \
 --junitxml="$RUN/TESTS.xml"
run REPLAY "$PY" research/r31w_metric_cell/replay_snapshot.py \
 --input "$SNAPSHOT" --out "$RUN/POINT_REPLAY.json"
```

예상 숫자가 아니라 actual collected/pass/fail/error/skip을 그대로 기록한다. 이번 원 실행은33 PASS였으나 그 수에 맞추어 test를 삭제하거나 skip하지 않는다.

## 이론·데이터 적용 gate

반환은 한국어와 machine-readable JSON으로 작성한다. 다음 경계를 유지한다.

1. GL(t) 변환의 D'에는 T†O dotT가 필요하다. 같은 방정식이면 R'=T†RT, eta invariant이다. Dephase 후 새로 보간하는 approximation을 같은 frame 변환과 혼동하지 않는다.
2. Affine endpoint 정리는 complete O,D가 같은 coordinate field에서 실제 affine이고 endpoint SPD, dt>0일 때만 적용한다. Nonaffine 함수나 arbitrary truncation에 확대하지 않는다.
3. Ionic2x2의 uniform diagnostic과 full25/49 HH interval bound는 다르다. 현재 replay는 certified=false이며 physical transition error나 H-skip을 승인하지 않는다.

기존 source/archive 안에서만 read-only로 조사하여 neutral47x47의 O0,O4,D0,D4 또는 continuous provider, actual derivative 경로, atomic-time conversion, basis ordering/phase, common retained subspace/rank 증거가 있는지 확인한다. 알려진 direct z2와 mixed/ionic endpoint 외의 값을 추정으로 채우지 않는다. dotO_actual을 D+D†로 정의하여 검사를 자명하게 만들지 않는다. 원 source가 없으면 AUTHORITY_INPUT_BLOCKED로 missing field를 명시한다. 새로운 native integral이나 z node는 계산하지 않는다.

CELL_APPLICABILITY.json에는 field명, 실제 path/object ID, hash, source commit, 읽은 범위, coordinate/time/geometry 계약, available/missing/ambiguous를 기록한다. 전체 matrix가 확보되어도 exact affine model을 정의하는 것과 physical source가 affine인 것은 구분한다. 24x13 synthetic grid checks를 interval proof라고 하지 않는다.

## 수정·반환·게시

새 research script에서 재현 가능한 bug가 나오면 failing test와 최소 patch를 보존한다. 그렇지 않으면 old134/M3B/BR-01/02를 이 노드 때문에 다시 실행·감사하지 않는다. 별도 reviewer의 formal admission이 없으면 independent_review_admitted=false를 유지한다. Historical gaps를 보존하고 사후 증명을 만들지 않는다.

RETURN.json에 reviewed/executed HEAD+tree, 입력SHA, 환경, commands/exits, JUnit, point witness와 ionic 수치·gap, CELL_APPLICABILITY 판정, source mutation 범위, unverified를 기록한다. Native evaluations=0, new heavy scientific nodes=0, HH trajectory=0, production_admitted=false를 유지한다.

Ordinary non-force push를 research branch에 수행하고 기존 raw를 덮어쓰지 않는다. 새 checkpoint를 create-only로 다음 두 곳에 백업한다.
Drive parent: 1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM
Dropbox parent: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928

양쪽 provider의 실제 ACK/object ID/size/checksum을 detached receipt에 보존한다. R1/R2로 충분하면 반복 download하지 않는다. Raw restore 없이 RESTORE_VERIFIED라고 하지 않는다. M3A/M3B/reference preparation,z1/z0.5/full144,trajectory,M5,provider promotion,main merge,force push,타 owner PID 조작은 금지다.

Stop condition: 새 script의 focused 재현과 CELL_APPLICABILITY evidence를 반환하면 종료한다. 입력 부족이면 정확한 blocker를 반환하고 끝내며, unauthorized scientific run이나 반복 감사로 확대하지 않는다.
