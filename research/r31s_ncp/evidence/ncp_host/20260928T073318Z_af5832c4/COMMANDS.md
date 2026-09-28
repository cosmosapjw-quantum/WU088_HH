# R31T M3 command record

- `git fetch origin`; `git switch codex/r31s-ncp-m1-m2`; `git pull --ff-only`: exit 0.
- Baseline HEAD `3b72fd4af65752e020bf5a3699ed2f2341497881`; tree `18d74d7305a4ed80b2fbb0ba24173ac520b885dc`; clean.
- `git switch -c codex/r31t-ncp-m3-production-screen`: exit 0.
- `python3 research/r31s_ncp/probe/ncp_probe.py --workspace "$HOME" --out /root/wu088_m3_probe.GMIpty/HOST_PROBE_M3.json`: exit 0.
- Source audit: `rg` and `sed` of `vendor/orchestration/wide_hybrid_run.py`, `vendor/orchestration/r31m_tuned_local_adapter.py`, `scripts/r31n_provider_fill.py`, `research/r31s_ncp/evidence/RUNTIME_SOURCE_INVENTORY.json`, and M2 authority evidence: exit 0.
- `/root/wu088_hh_ncp_work_v2/venv/bin/python -m pytest -q research/r31s_ncp/tests/test_authority_seed.py research/r31s_ncp/tests/test_ncp_probe.py`: exit 0, 18 passed.
- No CP4 download, H0 build, full pair, pool, or benchmark command was executed.
