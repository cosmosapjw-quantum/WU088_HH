# Codex continuation — R31T/M3 after H0 authority blocker closure

This prompt continues draft PR #12 after `BLOCKED_M3_AUTHORITY_INPUT`.

## 0. What changed

The blocker was valid, but the dependency audit had one path error:

- reported: `r31a/wide_reference.py`
- actual CP4 path: `completion/mixed_h/wide_reference.py`
- exact SHA-256: `ba9bea3b58977b19cf993b082e1518dafb9c8122501fc629761db5b90ff6c6e4`

Historical `WideReference` inherits `Production`, so construction performs extra
GuardedH/foreign initialization before replacing `h0` with `H0Fused`.
For the bounded M3 screen this transitive initialization is unnecessary.

A minimal exact H0 authority closure is now in the central branch:

`research/r31s_ncp/authority_m3/`

It contains exact CP4:
- `h0_fused.cpp`
- `radial_wide.cpp`
- full `FROZEN_INPUTS.npz`
- `m3_h0_authority.py`
- manifest + sandbox regression

Sandbox regression compared the minimal adapter against historical CP4 H0Fused for
B160/B192 x pairs [3,7], [5,11], [10,11] x active 0/1: 12/12 output arrays exact,
12/12 sumabs exact, all max deltas zero.

This closes the INPUT blocker only. It does NOT close NCP full-pair equivalence or M3 throughput.

## 1. Refresh / merge authority

On the NCP VM:

```bash
cd "$HOME/WU088_HH"
git fetch origin

git switch codex/r31t-ncp-m3-production-screen
git status --short
```

Require a clean worktree.

Record current head/tree, then merge the current central authority branch:

```bash
git merge --no-edit origin/r31s-ncp-c64g3-redesign
git status --short
git rev-parse HEAD
git rev-parse HEAD^{tree}
```

Do not force-push. Do not rebase shared PR #12 history.

Read:

- `research/r31s_ncp/authority_m3/M3_AUTHORITY_MANIFEST.json`
- `research/r31s_ncp/authority_m3/M3_H0_SANDBOX_REGRESSION.json`
- `research/r31s_ncp/authority_m3/m3_h0_authority.py`
- `research/r31s_ncp/authority_seed/AUTHORITY_MANIFEST.json`
- existing PR #12 evidence under
  `research/r31s_ncp/evidence/ncp_host/20260928T073318Z_af5832c4/`

Repository content is SSOT.

## 2. Exact identities that must verify

Require:

```text
FROZEN_INPUTS.npz
8482d2854ab620c58bb1d7a7a45cf88eb71fd75081242263a9ef48927f0a282c

h0_fused.cpp
d019713f8a9c6e864d60cc796104a0cdef629e491e6ab8de757995aa4f3672f2

radial_wide.cpp
2c20c3e3de8a69a64363806512dde8b3dbae6b818c8aec458893906d9b21399a

historical completion/mixed_h/wide_reference.py
ba9bea3b58977b19cf993b082e1518dafb9c8122501fc629761db5b90ff6c6e4
```

Do not fetch full CP4 merely to satisfy M3 if these repository authority files verify.

## 3. Focused authority verification

Use the existing NCP M1/M2 venv.

Run:

```bash
python -m pytest -q   research/r31s_ncp/tests/test_m3_h0_authority.py   research/r31s_ncp/tests/test_authority_seed.py   research/r31s_ncp/tests/test_ncp_probe.py
```

Preserve exact command and exit code.

Then fresh-build H0 in a NEW M3 build namespace with loader variables removed:

```bash
env -u LD_PRELOAD -u LD_LIBRARY_PATH python - <<'PY'
from pathlib import Path
import importlib.util, json

p=Path('research/r31s_ncp/authority_m3/m3_h0_authority.py').resolve()
s=importlib.util.spec_from_file_location('m3_h0_authority',p)
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)

root=Path.home()/'wu088_hh_ncp_work_v2'/'m3_h0_build'
lib, manifest=m.build(root)
print(json.dumps({
  'status':'PASS_NCP_FRESH_M3_H0_BUILD',
  'binary_path':str(lib),
  'binary_sha256':manifest['binary_sha256'],
  'spec':manifest['spec']
},indent=2))
PY
```

The binary is host-local and MUST NOT be committed.

Commit only its path/size/SHA/build identity in evidence.

If source identity or fresh build fails:
STOP with `BLOCKED_M3_AUTHORITY_INPUT` or a more precise runtime/build classification.

## 4. Do not instantiate historical WideReference

For M3, use:

`authority_m3/m3_h0_authority.py::H0Authority`

for H0.

Use the already admitted M2 same-host foreign reference/candidate implementations for
foreign arithmetic.

Do NOT instantiate historical `WideReference` solely to obtain H0.
That constructor pulls in redundant GuardedH/production initialization and is not needed
for the bounded M3 screen.

This adapter is scoped to M3. It is not a production-runtime admission.

## 5. Full-pair reference/candidate exactness gate

Before throughput, implement/test a bounded full-pair adapter that reproduces the
scientific pair semantics of `vendor/orchestration/wide_hybrid_run.py`:

For each pair:
1. exact H0 active=0
2. exact H0 active=1
3. foreign reference OR foreign candidate
4. apply the same frozen normalization, including exact `pref`
5. return/compare all numerical pair components

Use the existing exact B160/B192 g80 z=2 grid authority.

Representative set must include at least:

B160:
- [3,7]
- [5,11]
- [10,11]

B192:
- [3,7]
- [4,10]
- [10,11]

You may add deterministic intermediate-cost pairs, but stay <=12 unique pairs.

For every row require exact numerical equality between full reference and full candidate:

- H0 active-0 array
- H0 active-0 sumabs
- H0 active-1 array
- H0 active-1 sumabs
- normalized foreign array
- normalized foreign sumabs
- any deterministic per-pair assembled H representation if an existing authoritative helper produces one

Use `np.array_equal` for scientific arrays.

Do NOT use raw `.tobytes()` hashes of x86 complex long-double arrays as the equality gate,
because unused long-double storage padding is not scientific identity.

Record numeric max deltas; all must be zero.

If any full-pair row is non-exact:
STOP as `BLOCKED_M3_FULL_PAIR_EQUIVALENCE`.
Do not run throughput after failure.

## 6. Evidence update after blocker closure

Create a NEW M3 continuation RUN_ID under:

`research/r31s_ncp/evidence/ncp_host/<RUN_ID>/`

Do not overwrite the blocker evidence directory.

Commit:
- `M3_AUTHORITY_RESTORE.json`
- `M3_H0_BUILD.json`
- `M3_FULL_PAIR_EQUIVALENCE.json`
- `TESTS.json`
- `COMMANDS.md`
- `MANIFEST.json`
- `RETURN.json`

Push immediately after full-pair exactness closes.

Update PR #12. Do not open a separate M3 PR.

## 7. If full-pair exactness passes, resume original M3A/M3B

Then continue the production-shaped persistent-worker benchmark from the original M3 prompt.

M3A:
- B160/g80/z=2
- deterministic mixed-cost pair set
- shortlist at least:
  - 64x1
  - 32x2
  - 32x1
  - 16x4
  - one inner-thread-heavy control
- include 60x1 / 30x2 operational-reserve variants when legal and cheap
- warm persistent pool once
- record startup separately
- 2 measured repetitions if bounded cost permits

M3B only after M3A passes:
- B192/g80/z=2
- top 3 M3A configs + one control
- 3 measured repetitions if bounded

Do NOT run a full 144-pair scientific basis.

Repeated benchmark tasks are `PERFORMANCE_REPETITION_ONLY`, never new scientific pair state.

Primary ranking metric:
`steady_state_pairs_per_second`

Also record:
- CPU seconds/pair
- startup wall
- RSS/PSS
- memory.current/high/events
- cgroup throttling
- swap
- major faults
- observed teams/affinity

Do not select a profile if leading finalists are within 5%; report co-finalists.

## 8. Hard stops remain

Do NOT execute:
- z=1
- full 144-pair B160/B192 scientific node
- M4 async compute/backup overlap
- trajectory
- production admission
- merge
- force-push

No tolerance change, no fast-math, no FMA reassociation, no precision downgrade.

## 9. GitHub visibility

Push evidence after:
1. authority merge + fresh H0 build
2. full-pair exactness
3. M3A
4. M3B or blocker
5. final return

All small non-secret evidence must be in PR #12.
Large binaries/build directories remain host-local with path+size+SHA only.

## 10. Final return

Return human summary + JSON including:

- status
- old blocker evidence directory
- new continuation evidence directory
- merged central authority commit
- current branch/commit/tree
- PR #12
- authority source hashes
- fresh NCP H0 build identity
- full-pair equivalence rows / all_exact
- M3A/M3B configurations
- profile_candidate or null
- tests and exit codes
- large host-local artifacts
- heavy_scientific_nodes_executed
- full_144_pair_nodes_executed
- z1_executed=false
- trajectory_runs=0
- production_admitted=false
- durability_policy_changed=false
- failure_classification
- not_performed
- next_minimal_action

Stop after push and wait for independent review.
