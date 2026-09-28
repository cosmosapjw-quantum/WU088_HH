# Codex prompt addendum — publish NCP evidence to GitHub for ChatGPT review

This addendum is mandatory for R31S NCP M1/M2.

The previous host-local-only workflow is no longer sufficient. Every small, non-secret
NCP result needed for review MUST be committed to the Codex branch and pushed to GitHub
before you return. ChatGPT will audit the GitHub branch/PR directly.

## Authority seed

For bounded M2 H-foreign work, do NOT search the VM for the old full runtime.
Use the repository seed:

- research/r31s_ncp/authority_seed/AUTHORITY_MANIFEST.json
- research/r31s_ncp/authority_seed/M2_MODEL_SEED_SPARSE_HEX.json
- research/r31s_ncp/authority_seed/grid_seed.py
- research/r31s_ncp/authority_seed/requirements-m2.txt

Run the focused seed test before any M2 build/benchmark.
This seed is intentionally insufficient for M3/full H0/OD/JVP/ionic production work.
Do not expand into M3 merely because the full CP4 is unavailable locally.

## Mandatory GitHub evidence directory

On branch `codex/r31s-ncp-m1-m2`, create:

`research/r31s_ncp/evidence/ncp_host/<RUN_ID>/`

Use a deterministic RUN_ID based on UTC timestamp + short host-probe SHA, for example:
`20260928T061500Z_ab12cd34`.

Commit the following when available and non-secret:

- HOST_PROBE.json — exact raw probe bytes if secret scan passes
- HOST_PROBE_SHA256.txt
- ENVIRONMENT.json
- SOURCE_AND_BUILD_IDENTITY.json
- REFERENCE_BUILD.json
- CANDIDATE_BUILD.json
- M2_EQUIVALENCE.json
- M2_TUNING.json
- TESTS.json
- COMMANDS.md
- RETURN.json
- small stdout/stderr logs or log tails needed to diagnose failures

Every JSON must be valid and should contain its schema/status.
Every generated file must have size and SHA-256 recorded in RETURN.json or MANIFEST.json.

## Do NOT commit

Never commit:
- credentials, tokens, private keys, ~/.ssh, cloud metadata credentials
- venvs
- compiled .so files or build directories
- full CP4 archives
- raw 144-pair scientific states
- large profiler traces or core dumps
- Drive/Dropbox credentials
- files >5 MiB unless explicitly approved

For a large/noncommittable artifact, commit only an identity record containing:
absolute host path, byte size, SHA-256, generation command, and reason not committed.

## Required push cadence

Push after each durable milestone so ChatGPT can inspect partial progress:

1. M0 probe ingest/secret scan
2. M1 environment/bootstrap close
3. same-host reference/candidate build close
4. M2 equivalence close
5. M2 tuning close or blocker

Use normal commits. No force-push.

After every push, record:
- branch
- commit SHA
- tree SHA
- list of changed evidence files

## Failure behavior

If M1/M2 blocks, still commit the non-secret evidence accumulated so far plus RETURN.json
with the exact failure classification. A blocked run is still reviewable evidence.

Do not wait for a fully successful benchmark before pushing evidence.

## Final return

Your final chat response must give:
- GitHub branch
- latest pushed commit/tree
- draft PR URL/number
- evidence directory path in the repo
- host-local paths for any noncommitted large artifacts
- status/failure classification
- exact next minimal action

Do not merely say "files are on the VM". They must be visible on GitHub or explicitly
listed as noncommittable large artifacts with SHA-256 and host path.
