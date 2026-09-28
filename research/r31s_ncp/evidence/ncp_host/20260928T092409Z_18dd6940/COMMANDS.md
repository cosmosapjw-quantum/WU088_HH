# R31T M3 continuation commands

- `git fetch origin`; `git pull --ff-only origin codex/r31t-ncp-m3-production-screen`: exit 0.
- `git merge --no-edit origin/r31s-ncp-c64g3-redesign`: exit 0; merge `e4b043121b16cbec7e5202d711893ebd490413ba`; pushed.
- Focused authority tests: exit 0, 20 passed in 0.56s.
- Fresh H0 build: exit 0; binary and source identities in `M3_H0_BUILD.json`.
- Full-pair TDD: red exit 1 (module absent), green exit 0 (2 passed).
- Six B160/B192 full-pair reference/candidate rows: exit 0, all components numerically exact.
- Focused M3 tests: exit 0, 22 passed in 0.48s.
- M3 throughput helper TDD red/green: red exit 1 twice, green exit 0 (5 passed).
- B192 1x1 memory pilot: exit 0; private worker memory 32,454,656 bytes.
- M3A 64x1: exit 0; two 128-task batches, 64 active workers each, effective cgroup parallelism 56.48 and 54.56.
- Remaining M3A layouts 60x1,32x2,32x1,16x4,30x2,4x16: exit 0; all exact, affinity/team valid, no throttling.
- Focused M3 tests: exit 0, 25 passed in 0.54s.
- M3B attempt: exit 143 after a separate 61-child BASS workload appeared in the same session cgroup; no valid M3B configuration accepted. See `M3B_INTERRUPTION.json`.
- Final focused tests: exit 0, 25 passed in 0.89s.
