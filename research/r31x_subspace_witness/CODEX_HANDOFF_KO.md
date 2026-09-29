# Codex handoff: R31X full49 point witness와 mixed-block authority 추적

목표는 R31X의 stored-point linear-algebra certificate를 NCP에서 경량 재현하고, 그 다음 `direct_Q` 및 mixed endpoint common-frame authority를 read-only로 찾는 것이다. R31W full-cell blocker를 새 계산으로 우회하지 않는다.

## Authority

Repo: `cosmosapjw-quantum/WU088_HH`
Research branch: `research/r31x-subspace-witness-20260929`
Stack base: `research/r31w-covariant-metric-20260929`
Pinned parent: `6cb5d023f80301ba3efad4f1af1d25c327600f15`
Parent tree: `0153f0a7bd900ff3d0e922fa7252b201ccbdec60`

먼저 remote HEAD/tree를 읽는다. 후속 commit이 있으면 diff를 읽고 영향만 반영하며 과거 SHA로 reset하지 않는다. 기존 R31V/R31W raw, dirty worktree, backup object를 덮지 않는다. force push/main merge/다른 owner PID 또는 cgroup mutation 금지.

먼저 `REPORT_KO.md`, `RESULT.json`, `SOURCE_PINS.json`, `subspace_witness.py`, `replay_snapshot.py`, tests를 읽는다. Companion archive의 exact input member와 SHA를 확인한다. Git에는 71,481-byte NPZ를 넣지 않는 정책을 유지한다.

## 1. NCP 경량 재현

Companion archive에서 `inputs/EXISTING_METRIC_INPUTS.npz`를 새 read-only 경로로 추출한다. 요구 SHA-256:

`565a9ee6d831f5f9e3e69010270f5319aa3328432950efcfda81cfabf325c079`

검증된 `/root/wu088_hh_ncp_work_v2/venv/bin/python`이 있으면 사용하고, 없으면 기존 프로젝트의 검증된 environment를 찾는다. 새 패키지/native build를 자동 설치하지 않는다.

```bash
set -euo pipefail
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
export WU088_R31X_INPUT="$SNAPSHOT"
export PYTHONPYCACHEPREFIX="$RUN/pycache"

"$PY" -m py_compile \
 research/r31x_subspace_witness/subspace_witness.py \
 research/r31x_subspace_witness/replay_snapshot.py \
 research/r31x_subspace_witness/test_subspace_witness.py \
 research/r31x_subspace_witness/test_replay_snapshot.py \
 research/r31x_subspace_witness/VERIFY_EXACT_SYMPY.py

"$PY" -m pytest -q -p no:cacheprovider \
 research/r31x_subspace_witness/test_subspace_witness.py \
 research/r31x_subspace_witness/test_replay_snapshot.py \
 --junitxml="$RUN/TESTS.xml"

"$PY" research/r31x_subspace_witness/replay_snapshot.py \
 --input "$SNAPSHOT" --out "$RUN/POINT_WITNESS.json"

"$PY" research/r31x_subspace_witness/VERIFY_EXACT_SYMPY.py \
 > "$RUN/EXACT_FALLBACK.json"
```

각 command/exit/stdout/stderr를 보존한다. 예상 PASS 수13에 맞추기 위해 test를 삭제/skip하지 말고 actual collected/pass/fail/error/skip을 보고한다.

이 실행은 저장된 49x49 matrices의 generalized eigensolve일 뿐이다. 새 H/native integral/node/trajectory가 아니다. 다만 새로운 pointwise scientific linear algebra이므로 `new_lightweight_stored_full49_eigensolve=true`와 `new_heavy_scientific_nodes=0`을 둘 다 기록한다.

## 2. 필수 판정

다음을 독립적으로 확인한다.

- `eta_reduced <= eta_full` 및 generalized interlacing.
- positive/negative reduced witness를 `x=Qy`로 lift했을 때 ambient Rayleigh quotient가 동일.
- 현재 snapshot에서 full49/reduced25 extremal eigenvalues가 roundoff까지 같은지.
- full spectrum의 interior nonzero modes가 reduced spectrum에는 없다는 점. 따라서 `eta equality != spectral equivalence`.
- O-orthogonal projection residual을 기록하되 작은 값만으로 exact subspace identity를 주장하지 않는다.
- `minimum connection correction = eta_full/2`는 metric-compatible connection까지의 mathematical distance이며 physical repair 승인 아님.
- 47+2 block attribution과 mixed interpolation decomposition closure.

Wolfram connector가 NCP/Codex에서 사용 가능하면 `VERIFY_EXACT_SYMPY.py`와 별도로 작은 symbolic crosscheck를 해도 된다. 사용할 수 없으면 `WOLFRAM_BLOCKED`로 기록하고 결과를 만들지 않는다. Wolfram 성공은 production/scientific admission 조건이 아니다.

## 3. Q authority read-only 추적

다음 질문은 왜 z=2 `direct_Q(49x25)`가 양 extremal generalized eigenvector를 수치적으로 포함하는가이다.

repo와 companion/inherited archive에서 다음을 read-only로 찾는다.

- `direct_Q` 생성 코드/원자료/commit 또는 source archive identity
- Q의 column 의미: symmetry, parity, channel selection, orthogonalization, numerical truncation, eigenvector basis 중 무엇인지
- 49 basis index의 channel/quantum-number ordering
- Q가 O-orthonormal인지 단순 full-rank transform인지
- Q selection threshold, tolerance, rank decision 및 provenance
- Q가 z=2 전용인지 다른 z에도 정의되는지

찾은 자료마다 exact path/object, source commit/archive hash, line/member range를 `Q_AUTHORITY.json`에 기록한다. 추측으로 channel label을 붙이지 않는다. 권위 자료가 없으면 `Q_AUTHORITY_BLOCKED`로 종료한다.

Authority가 확보된 경우에만 stored ambient witness의 큰 component를 기존 basis labels에 매핑한 `WITNESS_CHANNEL_MAP.json`을 만든다. 이것은 transition probability나 state occupation이 아니라 norm-defect witness 방향이다.

## 4. mixed endpoint frame/derivative authority 추적

R31X stored arrays에서는 mixed block secant slope와 endpoint `z0_j_dotO`, `z4_j_dotO`가 크게 다르다. 그러나 R31W는 canonical endpoint phase/order map을 확보하지 못했다.

다음을 read-only로 찾는다.

- z0/z4 mixed 47x2 O,D,dotO의 실제 producer
- endpoint basis ordering과 complex phase/gauge convention
- z0→z4 canonical identification 또는 transport matrix
- `j_dotO`의 정확한 정의와 단위
- direct z2와 endpoint mixed blocks가 동일 coordinate field인지 여부

공통 frame authority가 확보되면 `MIXED_FRAME_AUTHORITY.json`에 근거를 기록하고, 새 native 계산 없이 archived arrays의 affine derivative compatibility 판정을 재실행한다. 공통 frame이 없으면 `MIXED_FRAME_AUTHORITY_BLOCKED`로 유지한다.

endpoint secant mismatch를 공통 frame 증거 없이 physical source nonaffineness라고 부르지 않는다. Dephase/transport matrix를 임의로 선택해 mismatch를 줄이는 fitting도 금지한다.

## 5. 현재 금지·claim ceiling

- full-cell interval bound는 계속 `AUTHORITY_INPUT_BLOCKED`.
- neutral47 O0/O4/D0/D4를 추정 생성하지 않는다.
- dotO_actual을 D+D†로 정의해 metric test를 자명하게 만들지 않는다.
- 새 z node, full144, trajectory, H-skip, M5, production/provider admission 금지.
- M3A/M3B/reference preparation 및 기존134 controls 재실행 금지.
- independent_review_admitted=false와 BR01/BR02 historical gap을 보존.
- 25D PASS는 full49 PASS로 올릴 수 없고, 이번 FAIL-lift만 one-sided gate다.

## 6. 반환·게시·백업

`RETURN.json`에는 executed/reviewed commit+tree, input SHA, environment, actual command/exits/JUnit, full/reduced spectra, witness hashes/residuals, block attribution, Q authority, mixed-frame authority, unresolved gates를 기록한다.

정상 재현이면 기존 R31X code를 다시 설계하지 않는다. 재현 가능한 bug가 있으면 failing test→minimal patch→focused retest 순서만 허용한다.

ordinary non-force push 후 새 create-only checkpoint를 다음에 백업한다.

- Drive parent `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM`
- Dropbox parent `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928`

provider ACK/object ID/size/checksum을 detached receipt에 남긴다. raw restore 없이 `RESTORE_VERIFIED`라고 하지 않는다.

Stop condition: R31X 경량 replay + Q_AUTHORITY + MIXED_FRAME_AUTHORITY 판정까지 반환하면 종료. 둘 다 blocked여도 blocker를 정확히 기록하고 unauthorized computation으로 확장하지 않는다.
