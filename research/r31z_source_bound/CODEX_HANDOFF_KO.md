# Codex handoff: R31Z source-bound interpolation replay + withheld-data inventory

Repo: `cosmosapjw-quantum/WU088_HH`
Branch: `research/r31z-source-bound-interp-20260929`
Stack base: `research/r31y-lowrank-20260929`
Pinned parent: `d573e7b40446b07b1a5544644cf3f977b89264a6`
Parent tree: `374a17cff99bed80cc7e356f2e03a1c9d1f1a077`

목표는 R31Z의 새 이론/경량 계산을 NCP에서 재현하고, **fitting에 쓰지 않은 기존 intermediate mixed-node 자료가 이미 존재하는지**와 **full-cell blocker를 줄일 기존 neutral/dotQ authority가 producer archive에 있는지**를 read-only로 한 번 조사하는 것이다. 새 scientific node를 자동 생성하지 않는다.

## 0. 시작 identity와 범위

먼저 remote HEAD/tree와 companion `PUBLICATION_RECEIPT.json`을 확인한다. 후속 commit이 있으면 diff를 읽고 현재 authority를 갱신하되 과거 SHA로 reset하지 않는다. 기존 R31V/W/X/Y source, raw evidence, worktree 및 provider backup을 덮지 않는다. main merge, force push, 타 owner process/cgroup mutation 금지.

읽기 순서:

1. `research/r31z_source_bound/REPORT_KO.md`
2. `RESULT.json`, `SOURCE_PINS.json`
3. `source_bound.py`, `test_source_bound.py`
4. parent `research/r31y_lowrank/ncp_followup_20260929/PRODUCER_INTAKE.json`
5. parent `RETURN.json`

Parent producer intake가 이미 닫은 source/member binding을 다시 같은 snapshot만 읽어 재감사하지 않는다.

## 1. hash-locked 입력과 경량 재현

Companion archive의 `inputs/EXISTING_METRIC_INPUTS.npz` 또는 기존 NCP의 동일 file을 read-only로 사용한다.

- bytes: `71481`
- SHA-256: `565a9ee6d831f5f9e3e69010270f5319aa3328432950efcfda81cfabf325c079`

검증된 NCP venv `/root/wu088_hh_ncp_work_v2/venv/bin/python`이 있으면 사용한다. 없으면 기존 검증 environment를 찾고, 없으면 `ENVIRONMENT_BLOCKED`로 종료한다. 새 package/native build를 설치하지 않는다.

```bash
set -euo pipefail
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
export WU088_R31Z_INPUT="$SNAPSHOT"
export PYTHONPYCACHEPREFIX="$RUN/pycache"

run() {
  local name="$1"; shift
  printf '%q ' "$@" > "$RUN/$name.command"; printf '\n' >> "$RUN/$name.command"
  set +e
  "$@" > "$RUN/$name.stdout" 2> "$RUN/$name.stderr"
  local rc=$?
  set -e
  printf '%s\n' "$rc" > "$RUN/$name.exit"
  return "$rc"
}

run COMPILE "$PY" -m py_compile \
  research/r31z_source_bound/source_bound.py \
  research/r31z_source_bound/test_source_bound.py

run TESTS "$PY" -m pytest -q -p no:cacheprovider \
  research/r31z_source_bound/test_source_bound.py \
  --junitxml="$RUN/TESTS.xml"

run REPLAY "$PY" research/r31z_source_bound/source_bound.py \
  --input "$SNAPSHOT" --out "$RUN/POINT_INTERPOLATION.json"
```

실제 collected/pass/fail/error/skip을 기록한다. ChatGPT 환경에서는 최종 11 PASS였지만 그 숫자에 맞추어 test를 제거하거나 skip하지 않는다. 기존 20/13/33/134 tests를 이 node 때문에 다시 실행하지 않는다.

## 2. 재현해야 할 과학적/수학적 판정

### 2.1 source-bound affine rejection

Parent producer intake는 z0/z4 mixed OD/JVP의 common frozen basis/phase, `j_dotO`의 independent definition/units, direct z2 assembly pipeline을 source/member와 array identity에 연결했다.

따라서 아래 값이 재현되면 archived represented-data 수준에서 affine mixed O를 FAIL로 판정한다.

- midpoint chord error 2-norm `1.1608909908205545`
- secant-dotO z0 `0.5495713714162325 /t_a`
- z2 `0.2910484768338663 /t_a`
- z4 `0.33156843070467085 /t_a`

이 판정을 physical exact source function의 error bound로 승격하지 않는다.

### 2.2 curvature lower bound

C2 path에 필요한 necessary bound를 재현한다.

- combined time-curvature lower bound `0.1228983778317182 /t_a^2`
- equivalent z-curvature lower bound `0.6143870602870756 /a0^2`

이것은 exact represented input을 가정한 analytic lower bound다. Float/source uncertainty에 대한 certified enclosure가 아니다.

### 2.3 structure-preserving candidate

세 node `z=0,2,4`의 `O,dotO`를 맞추는 degree<=5 Hermite O와, 각 node의

`K=(D_col-D_row†)/2`

를 맞추는 quadratic K를 사용한다. 그 다음

`D_col=dotO/2+K`, `D_row†=dotO/2-K`

로 정의한다. Node reproduction과 metric compatibility residual을 확인한다. 이 construction이 node-exact하더라도 between-node physical accuracy를 PASS로 하지 않는다.

Two-endpoint cubic Hermite의 z2 O/dotO mismatch도 재현하여 “endpoint derivative를 보존하면 충분하다”는 주장을 기각한다.

## 3. withheld existing-data inventory

새 native 계산 전, 이미 복원한 producer archive/Drive/Dropbox/local runtime에서 **fitting에 사용하지 않은 direct mixed block node**가 존재하는지 한 번 찾는다.

Target은 z∈(0,4), z≠2이며 최소 O,D,independent dotO가 동일 producer contract로 묶인 direct node다. z=1 또는 z=3이 우선이지만 다른 중간점도 허용한다.

`INTERMEDIATE_NODE_INVENTORY.json`에 각 후보의

- exact z/time,
- archive/object/member/path,
- SHA/size,
- producer source identity,
- O,D,dotO availability,
- basis/order/phase compatibility,
- fitting에 사용되었는지 여부

를 기록한다.

### 중요 stop rule

- 기존 direct node가 **없으면** `INTERMEDIATE_VALIDATION_DATA_BLOCKED`로 종료한다.
- 그 경우 z1/z3을 새로 계산하지 않는다. 새 science-node 실행은 별도 승인 대상이다.
- partial/synthetic array를 validation node로 대체하지 않는다.
- 후보가 있으면 R31Z quintic candidate와 **withheld comparison만** 한다. Fit을 다시 하지 않는다.

## 4. full-cell blocker용 existing authority inventory

같은 recovered producer archive에서 다음이 이미 존재하는지만 read-only로 한 번 확인한다.

- complete neutral47 `O,D,dotO` at z0,z4 또는 continuous provider,
- Q(z) 또는 `dotQ`/time-dependent subspace transport source,
- neutral/H phase/order bridge를 z0→z4에 연결하는 authority,
- full49 interpolation/trajectory code가 실제로 어떤 neutral source를 사용하도록 설계됐는지.

`FULLCELL_EXISTING_AUTHORITY.json`으로 available/missing/ambiguous를 exact member/source lines와 기록한다. 없으면 `FULLCELL_AUTHORITY_INPUT_BLOCKED`를 유지한다. 새 neutral arrays를 계산하거나 `dotO=D+D†`로 만들어내지 않는다.

## 5. Q sector claim policy

Producer source에서 Q의 **declared s=0 inversion-sector map**과 pair-sign rule은 회수되었다. 따라서 source-description 수준에서는 그 표현을 사용할 수 있다.

그러나 다음은 여전히 별도다.

- independent physical adequacy of that sector in the complete HH model,
- time-dependent `dotQ`,
- whole-cell sector preservation,
- propagation decoupling.

작은 commutator/cross-sector norm만으로 위 네 항목을 PASS로 올리지 않는다.

## 6. 반환과 mutation

`RETURN.json`에는 다음을 분리한다.

- reviewed/executed commit+tree,
- environment/commands/exits/JUnit,
- source-bound affine rejection,
- curvature lower bounds,
- quintic candidate node reproduction,
- `INTERMEDIATE_NODE_INVENTORY` verdict,
- `FULLCELL_EXISTING_AUTHORITY` verdict,
- mutation scope,
- unresolved claim gates.

정상 재현이면 R31Z code를 다시 설계하지 않는다. 실제 bug가 재현될 때만 failing test→minimal patch→focused retest를 수행한다.

금지:

- M3A/M3B/reference preparation 재실행,
- 기존 R31Y/R31X tests의 무의미한 반복,
- 새 z node/native integral/H 계산,
- full144, trajectory, M5, H-skip,
- provider/production admission,
- main merge/force push.

새 evidence는 ordinary non-force push 가능하다. Create-only 이중백업 위치:

- Drive parent `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM`
- Dropbox parent `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928`

실제 ACK/object ID/size/checksum 범위를 receipt에 기록한다. raw download를 하지 않았으면 `RESTORE_VERIFIED=false`다.

## Stop condition

다음 두 항목까지 반환하면 이 node를 닫는다.

1. R31Z 경량 재현.
2. 기존 withheld intermediate node + full-cell authority inventory.

Intermediate validation data가 없으면 다음 행동은 **새 z1/z3 science node의 별도 preregistration/승인 여부 결정**이지, polynomial order를 더 올리거나 동일 세 node를 재감사하는 것이 아니다.
