# WU088_HH — HH Atomic-Reuse research plan v2

The [current research plan](research/r31ao_unequal_ladder/hh_atomic_reuse_plan_20261012_v2/DEVELOPMENT_PLAN_KO.md) maps the user's 17-node REI Atomic-Reuse DAG into eight HH tasks. The [HH DAG](research/r31ao_unequal_ladder/hh_atomic_reuse_plan_20261012_v2/NEXT_DAG.json), [provider contract](research/r31ao_unequal_ladder/hh_atomic_reuse_plan_20261012_v2/contracts/HH_REI_EXPORT_CONTRACT.json), and [handoff](research/r31ao_unequal_ladder/hh_atomic_reuse_plan_20261012_v2/HANDOFF_KO.md) are the active planning entry points. See [CURRENT_DEVELOPMENT_PLAN.json](CURRENT_DEVELOPMENT_PLAN.json).

The scientific baseline remains [PHYS12](research/r31ao_unequal_ladder/hh_phys12_absolute_response_20261012_v1/REPORT_KO.md), with its existing scoped independent decision. The successor registers PHYS12 as S14_PHYS12 while preserving the supplied REI DAG and all earlier science. No new scientific run or external RUX completion is claimed.

HH source-family admission and observable screening can proceed when a concrete consumer request exists. Actual optional EoR ON/OFF histories follow RUX11 and reuse matching cached cases. The REI baseline proceeds without optional HH completion; independent HH singlet and strict-native research keep their own admission.

Current NCP status: **NO_HEAVY_JOB_READY**; heavy_queue=[]; launch=false. [Lane-specific policy](research/r31ao_unequal_ladder/hh_atomic_reuse_plan_20261012_v2/NCP_TASKS.json). Producer contracts are prepared, but no new HH rate table, coupled consumer runtime, or whole-history result has been admitted.

## Historical R31K-B/R31M native-lane guide

The following original text is retained as historical scope. Its benchmark commands are used only for an actual admitted native task, not automatically after fetching this repository.

# WU088_HH

Source-bound research and performance work for the frozen107 two-electron H-H model.

See [한국어 사용 안내](README_KO.md), [research results](docs/research/RESULTS_KO.md), [mathematical derivations](docs/research/MATHEMATICS.md), and [verification evidence](evidence/FINAL_VERIFICATION.json).

This repository is a non-destructive overlay for the existing local runtime. Five-anchor H order comparisons pass; new-anchor full49 admission and trajectory/production promotion remain blocked. The native performance candidate has component-level checks only and is not installed into the production provider.

The local hardware task is `bash scripts/benchmark_host.sh` after setting `WORK` and `RUNTIME` as described in the Korean guide. It does not regenerate completed anchor pair states.


R31M adds topology-aware CPU pinning, an SMT probe, and a host/build-bound tuning profile. See `docs/coding/R31M_HOST_AUTOTUNE.md`. The profile does not automatically promote the candidate native provider.
