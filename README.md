# WU088_HH — current development plan

The active priority is observable-based HH research. Start with [the current plan](research/r31ao_unequal_ladder/hh_observable_first_plan_20261012_v1/DEVELOPMENT_PLAN_KO.md) and [CURRENT_DEVELOPMENT_PLAN.json](CURRENT_DEVELOPMENT_PLAN.json).

The next HERE result will assess fixed-source-family HH-on/off changes in hydrogen ionization fraction and gas energy, separately from the already completed PHYS11 mixed response. It is not yet executed. PHYS11 at 328372568144c4cdb6cdecd94c9c9bff984e103e remains the scoped scientific baseline. Full native certification and microscopic singlet ion-pair research retain their own requirements and do not block every effective-model result.

Current NCP status: **NO_HEAVY_JOB_READY**; heavy_queue=[]; launch=false. [NCP handoff](research/r31ao_unequal_ladder/hh_observable_first_plan_20261012_v1/HANDOFF_KO.md). Heavy work is selected only for actual unfinished physics with measured cost and useful independent partitions.

## Historical R31K-B/R31M native-lane guide

The following original text is retained as historical scope. Its benchmark commands are used only for an actual admitted native task, not automatically after fetching this repository.

# WU088_HH

Source-bound research and performance work for the frozen107 two-electron H-H model.

See [한국어 사용 안내](README_KO.md), [research results](docs/research/RESULTS_KO.md), [mathematical derivations](docs/research/MATHEMATICS.md), and [verification evidence](evidence/FINAL_VERIFICATION.json).

This repository is a non-destructive overlay for the existing local runtime. Five-anchor H order comparisons pass; new-anchor full49 admission and trajectory/production promotion remain blocked. The native performance candidate has component-level checks only and is not installed into the production provider.

The local hardware task is `bash scripts/benchmark_host.sh` after setting `WORK` and `RUNTIME` as described in the Korean guide. It does not regenerate completed anchor pair states.


R31M adds topology-aware CPU pinning, an SMT probe, and a host/build-bound tuning profile. See `docs/coding/R31M_HOST_AUTOTUNE.md`. The profile does not automatically promote the candidate native provider.
