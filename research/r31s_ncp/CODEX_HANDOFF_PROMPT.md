# Codex handoff prompt — WU088_HH R31S NCP c64-g3 M1/M2

Paste the block below into Codex while logged into the NCP c64-g3 host.
This prompt authorizes M0 ingest, M1, and bounded M2 only. It does not authorize
M3/M4/M5, z=1, full scientific basis execution, merge, force-push, or production admission.

---

You are the host-local implementation and bounded benchmark agent for
`cosmosapjw-quantum/WU088_HH` on an NCP c64-g3 VM.

Your task is **R31S NCP M1/M2 only**.
Scientific claims, thresholds, and the transition to M3/M4/M5 remain external review gates.

## 0. Authority and baseline

Repository:
`https://github.com/cosmosapjw-quantum/WU088_HH`

Authoritative baseline branch:
`r31s-ncp-c64g3-redesign`

Before changing anything:

```bash
cd "$HOME/WU088_HH"
git fetch origin
git switch r31s-ncp-c64g3-redesign
git pull --ff-only
git status --short
git rev-parse HEAD
git rev-parse HEAD^{tree}
```

Require a clean worktree. Record the exact HEAD and tree.
Read, in this order:

1. `research/r31s_ncp/README_KO.md`
2. `research/r31s_ncp/DESIGN_KO.md`
3. `research/r31s_ncp/evidence/RESULT.json`
4. `research/r31s_ncp/evidence/NCP_M0_USER_REPORTED.json`
5. `research/r31s_ncp/probe/ncp_probe.py`
6. relevant existing build/autotune/native code before editing it

Do not infer current repo state from this prompt if the files disagree.
Repository content is SSOT.

Create a new branch only after the readback:

```bash
git switch -c codex/r31s-ncp-m1-m2
```

Do not force-push and do not merge.

## 1. Frozen scientific state

Preserve exactly:

- z=2 direct H convergence/full49 result
- [0,4] z=2 linear interpolation FAIL
- H threshold = 2e-7 Eh
- whitened independent generator relative threshold = 2e-12
- next scientific depth-first node = z=1
- trajectory runs = 0
- trajectory_admitted = false
- production_admitted = false

Do not execute z=1 in this task.

Do not modify frozen/reference/vendor scientific authority merely to make a test pass.
Do not symmetrize failed data, relax tolerances, downgrade precision, enable fast-math,
allow FMA reassociation, change canonical reduction order, or fabricate independent dotO.

## 2. M0 full probe ingest

A host-local probe was already run and the user reported:

- status = PROBED_NOT_BENCHMARKED
- planning_cpu_budget = 64
- heavy_execution_allowed = false
- report = /root/wu088_ncp_probe.djNQYK/HOST_PROBE.json

First inspect that exact file.

Compute and return:

```bash
stat -c '%s %n' /root/wu088_ncp_probe.djNQYK/HOST_PROBE.json
sha256sum /root/wu088_ncp_probe.djNQYK/HOST_PROBE.json
python3 -m json.tool /root/wu088_ncp_probe.djNQYK/HOST_PROBE.json >/dev/null
```

Validate its schema/status and read:
allowed CPU set, planning CPU budget, cgroup CPU/memory constraints,
guest topology, compiler/version/precision macros, filesystem free, warnings.

Do not equate 64 vCPU with 64 physical cores.
Do not claim guest package/core/L3/NUMA values prove host topology outside the VM.

If the report contains credentials, tokens, private keys, or other secrets:
STOP with `BLOCKED_SENSITIVE_EVIDENCE`; do not commit it.

Otherwise create a provenance-preserving evidence copy or normalized report under
`research/r31s_ncp/evidence/ncp_host/`, including original SHA-256 and byte size.
Never silently rewrite the original report and call it byte-identical.

If cgroup mapping is ambiguous or probe warnings require inspection:
STOP before build benchmarking and return the blocker.

## 3. M1: fresh NCP execution environment

Implement an additive, reversible NCP bootstrap.

Requirements:

- work root separate from repository, e.g. `$HOME/wu088_hh_ncp_work`
- project-local/new venv only
- fresh build namespace keyed by source/compiler/host identity
- source/reference inputs read-only where practical
- no reuse of the 5900X .so or host tuning profile as production authority
- no global/system Python mutation
- no automatic apt/system package installation
- no credential/firewall changes
- trusted native child processes must not inherit LD_PRELOAD/LD_LIBRARY_PATH
- record Python/compiler/binutils/NumPy/SciPy and relevant precision macros

If a system dependency is missing, STOP with
`BLOCKED_MISSING_SYSTEM_DEPENDENCY` and name the minimal dependency.
Do not install it unless separately authorized by the user.

Write tests first for any new behavior. Keep existing scientific files unchanged unless
a narrowly justified adapter is required; prefer additive files under
`research/r31s_ncp/`.

## 4. M2: fresh same-host reference/candidate bridge

Build both a reference and candidate on this same NCP host from authoritative source.

Preserve:

- `-fno-fast-math`
- `-ffp-contract=off`
- long-double / complex precision contract
- binary128 cancellation lane where the existing source requires it
- canonical gamma/reduction order
- model/grid/source identity

Do not use cross-host byte identity as the gate.
The main numerical promotion gate is **same-host reference vs candidate**.

Use a bounded representative set only, covering:

- B160 and B192
- z=2
- cheap / median / expensive pair classes
- at least one existing complex/cancellation stress case

Do **not** run a full 144-pair basis in M2.

For scheduling/implementation variants, require actual selected-sample arrays to be
exactly equal to the same-host reference, plus unchanged sumabs/conditioning auxiliaries
where defined. Record observed OpenMP team size and affinity.

If cross-host results differ from the old 5900X lane:
do not invent a tolerance. Separate compiler/ABI/math-library/source/build causes.
Return `BLOCKED_CROSS_HOST_NUMERICAL_EQUIVALENCE` if no authorized bridge closes it.

## 5. Bounded host tuning

Generate benchmark candidates from the actual effective CPU budget, including when legal:

- 64 x 1
- 32 x 2
- 16 x 4
- 8 x 8
- 4 x 16
- 2 x 32
- 1 x 64
- half-budget variants

Here x means outer processes x kernel threads.

Do not mark any configuration selected before measurement.
Do not exceed affinity/cgroup CPU or measured memory limits.
A pure 64-slot benchmark configuration is not automatically a production setting because
coordinator/uploader control resources also need budget.

This M2 benchmark is bounded representative work only.
Record at least:
wall time, CPU time, actual thread teams, affinity,
RSS/PSS if available, cgroup cpu.stat throttling deltas,
memory.current/high/events, swap activity, and major page faults.

Run configurations in rotated order and use >=3 repetitions only where the bounded test
cost is small enough. Otherwise report the limitation instead of extending into M3.

## 6. Durability scope

The existing `credit_model.py` is an in-memory specification, not a production executor.

Do not implement or promote the persistent asynchronous uploader/executor in this task.
Do not overlap new scientific computation with Drive/Dropbox production backup.

You may unit-test/specify state transitions, but M4 requires a separate gate with:
persistent WAL/restart, producer crash, fsync failure, orphan,
half-receipt, changed bytes, duplicate ACK, lost lease, OOM,
deadline/quota-change fault injection.

## 7. Hard stops

STOP before any of these:

- M3 production-shaped full H0+foreign queue benchmark
- full B160/B192 144-pair node
- z=1 scientific node
- real production compute/backup overlap
- production durability policy change
- trajectory propagation
- production admission
- merge or force-push

The output of this task is an M1/M2 candidate admission package for review, not production.

## 8. Tests and mutation discipline

For every code change:

1. add/modify a focused test that fails for the old behavior when applicable
2. implement the minimal change
3. run focused tests
4. run only the relevant R31S/NCP suite unless a dependency change justifies more
5. record exact commands and exit codes

Never claim PASS without executed evidence.

Classify failures as one of:

- PHYSICS_MATH_ERROR
- NUMERICAL_PRECISION_ERROR
- IMPLEMENTATION_ERROR
- RUNTIME_ENVIRONMENT_ERROR
- TRANSPORT_DURABILITY_ERROR
- PERMISSION_POLICY_BLOCKER
- BLOCKED_HOST_ACCESS
- BLOCKED_MISSING_SYSTEM_DEPENDENCY
- BLOCKED_CROSS_HOST_NUMERICAL_EQUIVALENCE
- UNRESOLVED

## 9. Git output

Commit only intentional source/docs/tests/evidence.
Do not commit venvs, compiled build trees, credentials, caches, or giant raw runtime outputs.

Push:

`codex/r31s-ncp-m1-m2`

Open a **draft** PR with base:

`r31s-ncp-c64g3-redesign`

Do not merge it.

## 10. Return contract

Your final return must include a machine-readable JSON block and a concise human summary.

Required fields:

```json
{
  "status": "...",
  "baseline_branch": "r31s-ncp-c64g3-redesign",
  "baseline_commit": "...",
  "baseline_tree": "...",
  "codex_branch": "codex/r31s-ncp-m1-m2",
  "final_commit": "...",
  "final_tree": "...",
  "changed_files": [],
  "host_probe": {
    "path": "/root/wu088_ncp_probe.djNQYK/HOST_PROBE.json",
    "sha256": "...",
    "bytes": 0,
    "status": "...",
    "planning_cpu_budget": 0,
    "warnings": []
  },
  "environment": {},
  "reference_build": {},
  "candidate_build": {},
  "representative_samples": [],
  "tuning_candidates": [],
  "selected_configuration": null,
  "tests": [],
  "heavy_scientific_nodes_executed": 0,
  "z1_executed": false,
  "trajectory_runs": 0,
  "production_admitted": false,
  "durability_policy_changed": false,
  "backup_tier": "NONE_OR_DESCRIBE_EXACTLY",
  "failure_classification": null,
  "not_performed": [],
  "next_minimal_action": "..."
}
```

If any requested field is not known, use null and explain why.
Do not infer it.

End after push/draft-PR and return. Wait for ChatGPT/user review before M3/M4/M5.
