# WU088_HH — latest scoped physics result

[PHYS12 report](research/r31ao_unequal_ladder/hh_phys12_absolute_response_20261012_v1/REPORT_KO.md) now executes the fixed-family future HH-on/off response planned in PR45. Both archived first stages have positive hydrogen-ionization-fraction response and negative thermal-energy response, conditional on the inherited source inclusion and same-alpha C2 family. See [CURRENT_DEVELOPMENT_PLAN.json](CURRENT_DEVELOPMENT_PLAN.json) and the [independent decision](research/r31ao_unequal_ladder/hh_phys12_absolute_response_20261012_v1/review/DECISION.json).

The PHYS11 source/native boundaries and original scientific files are preserved. Full and first_half are separate first stages, not a continuous history. The mixed response is reused and is distinguished from the absolute HH contribution.

Current NCP status: **NO_HEAVY_JOB_READY**; heavy_queue=[]; launch=false. [NCP handoff](research/r31ao_unequal_ladder/hh_phys12_absolute_response_20261012_v1/handoff/NCP_LOCAL_CODEX_HANDOFF_KO.md). The bounded question is answered; no automatic refinement or empty-queue benchmark is selected.

## Historical R31K-B/R31M native-lane guide

The following original text is retained as historical scope. Its benchmark commands are used only for an actual admitted native task, not automatically after fetching this repository.

# WU088_HH

Source-bound research and performance work for the frozen107 two-electron H-H model.

See [한국어 사용 안내](README_KO.md), [research results](docs/research/RESULTS_KO.md), [mathematical derivations](docs/research/MATHEMATICS.md), and [verification evidence](evidence/FINAL_VERIFICATION.json).

This repository is a non-destructive overlay for the existing local runtime. Five-anchor H order comparisons pass; new-anchor full49 admission and trajectory/production promotion remain blocked. The native performance candidate has component-level checks only and is not installed into the production provider.

The local hardware task is `bash scripts/benchmark_host.sh` after setting `WORK` and `RUNTIME` as described in the Korean guide. It does not regenerate completed anchor pair states.


R31M adds topology-aware CPU pinning, an SMT probe, and a host/build-bound tuning profile. See `docs/coding/R31M_HOST_AUTOTUNE.md`. The profile does not automatically promote the candidate native provider.
