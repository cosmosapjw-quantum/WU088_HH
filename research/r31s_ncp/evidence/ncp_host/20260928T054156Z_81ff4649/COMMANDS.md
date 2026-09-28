# R31S NCP M1/M2 commands and push record

Baseline `r31s-ncp-c64g3-redesign`:
commit `b90b27d2c886d616df2dff97759da795fa7a926f`,
tree `e3161f8c03a0d530861a4acd0fbb3dbb066c3fb2`.
The pre-existing Codex branch was advanced by cherry-picking this baseline commit,
keeping published history fast-forwardable. No merge or force-push was used.

## Executed setup

```bash
git fetch origin
git switch r31s-ncp-c64g3-redesign
git pull --ff-only
stat -c '%s %n' /root/wu088_ncp_probe.djNQYK/HOST_PROBE.json
sha256sum /root/wu088_ncp_probe.djNQYK/HOST_PROBE.json
python3 -m venv /root/wu088_hh_ncp_work_v2/venv
/root/wu088_hh_ncp_work_v2/venv/bin/python -m pip install --no-input -r research/r31s_ncp/authority_seed/requirements-m2.txt
/root/wu088_hh_ncp_work_v2/venv/bin/python -m pytest -q research/r31s_ncp/tests/test_authority_seed.py
/root/wu088_hh_ncp_work_v2/venv/bin/python research/r31s_ncp/ncp_build.py --probe research/r31s_ncp/evidence/ncp_host/20260928T054156Z_81ff4649/HOST_PROBE.json --work-root /root/wu088_hh_ncp_work_v2
/root/wu088_hh_ncp_work_v2/venv/bin/python research/r31s_ncp/m2_bridge.py --build /root/wu088_hh_ncp_work_v2/BUILD_STDOUT.json --out research/r31s_ncp/evidence/ncp_host/20260928T054156Z_81ff4649/M2_EQUIVALENCE.json
/root/wu088_hh_ncp_work_v2/venv/bin/python research/r31s_ncp/m2_tuning.py --build /root/wu088_hh_ncp_work_v2/BUILD_STDOUT.json --probe research/r31s_ncp/evidence/ncp_host/20260928T054156Z_81ff4649/HOST_PROBE.json --out research/r31s_ncp/evidence/ncp_host/20260928T054156Z_81ff4649/M2_TUNING.json --repeats 3
```

The native build used the strict flags `-fno-fast-math` and
`-ffp-contract=off`. The build wrapper removed `LD_PRELOAD` and
`LD_LIBRARY_PATH` for trusted compiler children. The seed was used only for
bounded H-foreign M2 work. The old full-runtime blocker in the earlier
historical evidence directory is superseded for this bounded scope by the
repository authority seed.

The bridge process finished all six selected B160/B192 z=2 rows. The daemon
restart lost its shell exit code; the generated JSON was validated and all six
rows were checked for exact output/sumabs equality and observed team 1.
The tuning process exited 0. Its current cgroup path was
`/sys/fs/cgroup/user.slice/user-0.slice/session-2.scope`; the original M0
probe was captured in `session-6.scope`. The current mapping was resolved
again before tuning, and its affinity and budget matched the M0 observation.

## Completed pushes

| Milestone | Branch | Commit | Tree | New evidence files |
|---|---|---|---|---|
| M0 raw probe | `codex/r31s-ncp-m1-m2` | `245f83a640944f33f223d36a34f78f2e773466b5` | `bcdd527e45090543b1613d6984d73f2322908592` | `HOST_PROBE.json`, `HOST_PROBE_SHA256.txt` |
| M1 environment and seed test | `codex/r31s-ncp-m1-m2` | `8b15395a02cb6b910a9061e707f39fcf942a46c2` | `c53403e2a3ef014387137bfcb40b875ae6a0ad66` | `ENVIRONMENT.json`, `TESTS.json` |
| Same-host native builds | `codex/r31s-ncp-m1-m2` | `213c0eeb49f391d2cc11950b182b0f31a453a3f3` | `0a924a48339c29d74be22959298f002c9fa3cb27` | `SOURCE_AND_BUILD_IDENTITY.json`, `REFERENCE_BUILD.json`, `CANDIDATE_BUILD.json` |
| M2 equivalence | `codex/r31s-ncp-m1-m2` | `54c2fd55cdf7c056bf88559b9f9e7442d41db47b` | `dab838df1f1fa91c35f415619a7d439be4978ea6` | `M2_EQUIVALENCE.json`, `TESTS.json`, `COMMANDS.md` |
| M2 tuning | `codex/r31s-ncp-m1-m2` | `d3ab89a29032fb0259a81c411cb493fb6e324100` | `dd21f9057cd3f100fbaa85798acb487d96a782db` | `M2_TUNING.json`, `TESTS.json`, `COMMANDS.md` |

Further pushes are recorded in the final return and Git history.
