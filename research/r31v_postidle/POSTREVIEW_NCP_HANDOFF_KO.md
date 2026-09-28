# R31V post-review NCP revalidation handoff

현재 canonical remote HEAD는 이 파일을 추가하기 직전 `71a8311625945cfa9eaf8f74e8dc119e82723d72`이다. 먼저 실제 remote ref를 다시 읽고 이후 commit이 있으면 내용을 읽어 반영하라. 과거 SHA로 reset하지 않는다.

## 목적

완료된 bounded B192/M3B를 다시 실행하는 것이 목적이 아니다. independent decision review에서 발견한 **receipt provenance-binding hardening**만 실제 NCP Python 환경에서 재검증하고, 그 결과를 evidence로 게시한다.

읽을 파일:

- `research/r31v_postidle/INDEPENDENT_DECISION_REVIEW_KO.md`
- `research/r31v_postidle/INDEPENDENT_DECISION_REVIEW.json`
- `research/r31v_postidle/m3_postidle.py`
- `research/r31v_postidle/test_driver.py`
- 완료 run의 `RETURN.json`, `SOURCE_BUILD_AUDIT.json`, `MEASUREMENT_REVIEW.json`

hardening commits:

- `45ca6b03566307f0946ee883371ff17adeb1cae6`
- `830390f9bf319d8589f700ad116119c36e335407`
- `187002d7340079ea582eb841cc6ff3d600e2fd67`

검토 finding은 완료된 M3B의 수치 mismatch가 아니다. 실제 pilot/exactness receipt에는 이미 `n=192,g=80,z=2.0` 및 1x1 exact-resource evidence가 존재했다. 새 코드는 이를 future reuse 시 명시적으로 재검사하도록 강화한다.

## 실행 범위

새 clean worktree를 사용하고 기존 raw evidence를 덮지 않는다. system Python을 억지로 수정하지 말고 이전 run에서 확인된 NCP venv 또는 현재 repo에서 검증된 equivalent environment를 사용한다.

최소 검증:

```bash
python -m py_compile \
  research/r31v_postidle/m3_postidle.py \
  research/r31v_postidle/test_driver.py

python -m pytest -q \
  research/r31v_postidle/test_controls.py \
  research/r31v_postidle/test_metric_controls.py \
  research/r31v_postidle/test_driver.py

python research/r31v_postidle/m3_postidle.py --phase describe
```

필요하면 기존 관련 M3 tests를 추가로 실행할 수 있지만 새 native benchmark, reference preparation, M3A/M3B, z=1, z=0.5, full144, trajectory, M5를 실행하지 않는다. 이 단계에서 host-exclusive grant도 필요하지 않다.

특히 새 tests가 다음 rejection을 실제로 검사하는지 확인한다.

1. pilot receipt의 잘못된 n/g/z
2. pilot의 1x1 resource-screen 불일치 또는 non-exact warmup
3. top-level private bound보다 큰 recorded PSS
4. exactness row의 잘못된 g 또는 z

테스트가 실패하면 먼저 재현 evidence를 보존하고 최소 patch만 수행한다. 성공하더라도 과거 NCP M3B를 새로 실행한 것으로 표현하지 않는다.

## 반환 및 게시

create-only run directory에 최소 다음을 기록한다.

- exact remote HEAD/tree
- Python/NumPy/pytest identity
- exact commands/exits
- collected/pass/fail count
- changed files, 있다면 diff/hash
- `M3B_RERUN=false`
- `NEW_SCIENTIFIC_NODES=0`
- production admission이 여전히 닫혀 있다는 상태

`POSTREVIEW_REVALIDATION.json`과 한국어 handoff를 ordinary non-force push한다. 테스트 성공 후 current hardening/review delta를 작은 additive checkpoint로 Google Drive + Dropbox에 create-only 백업할 수 있다. 기존 restore-verified core M3B archive를 overwrite하지 않는다. provider ACK 없이 dual-backup success를 주장하지 말고, raw readback을 하지 않았다면 RESTORE_VERIFIED라고 쓰지 않는다.

## 다음 gate

focused NCP revalidation이 통과하면 R31V bounded M3B independent review node는 닫는다.

그 이후에도 32x2는 **exclusive B192 wall-clock 목적의 provisional candidate**일 뿐 production-final/global winner가 아니다. production layout을 실제로 동결해야 하는 경우에만 32x2 vs 30x2의 interleaved confirmation을 별도 preregistration 후 시행한다. 단순히 검증 루프를 늘리기 위해 benchmark를 반복하지 않는다.
