# WU088_HH

Source-bound research and performance work for the frozen107 two-electron H-H model.

See [한국어 사용 안내](README_KO.md), [research results](docs/research/RESULTS_KO.md), [mathematical derivations](docs/research/MATHEMATICS.md), and [verification evidence](evidence/FINAL_VERIFICATION.json).

This repository is a non-destructive overlay for the existing local runtime. Five-anchor H order comparisons pass; new-anchor full49 admission and trajectory/production promotion remain blocked. The native performance candidate has component-level checks only and is not installed into the production provider.

The local hardware task is `bash scripts/benchmark_host.sh` after setting `WORK` and `RUNTIME` as described in the Korean guide. It does not regenerate completed anchor pair states.
