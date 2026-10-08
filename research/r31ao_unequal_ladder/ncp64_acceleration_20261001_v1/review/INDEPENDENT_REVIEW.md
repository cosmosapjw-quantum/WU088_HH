# Bounded independent implementation review

Status: bounded review complete; conditionally accepted at source/control-integration level. All six concrete implementation findings below have source-level repairs. Unresolved storage observations and unexecuted native/MPI/NCP gates remain explicit.

This is an owner-separated artifact review of the new acceleration overlay, not a scientific admission gate. `independent_review_admitted=false`; actual HH, Fortran/MPI, native callback equality, and NCP benchmark executions by this reviewer are all zero. Only Python synthetic/control fixtures and the local C process-launch shim were executed.

## Findings and closure

| ID | Severity | Concrete issue and minimum repair | Evidence / disposition |
|---|---|---|---|
| NCP-REV-01 | Medium | A successful C worker leader could leave a live same-group child while returning success. Kill any remaining group on every return; make successful-leader leftovers a failure. | Author preserved `mpi_fortran/REVIEW_GROUP_RED.log`. Current C code returns 1106 and kills the group. Reviewer reran the targeted status regression successfully. The original regression's direct `/proc/{child_pid}` liveness lookup is insufficient in this host PID namespace; that particular liveness assertion is not independent proof. |
| NCP-REV-02 | Medium | Fresh resource inspection checked feasibility but retained the old aggregate memory cap. A 128→96 GiB snapshot could keep 112 GiB instead of 80 GiB. | `refresh_plan` now retains the lower fresh/old cap and fresh host metadata. One targeted reviewer regression passed. |
| NCP-REV-03 | Medium | MPI stage completion alone did not prove the declared task set was complete. | Launcher now requires prepare READY, rank binding receipts, and collector COLLECTED with exact declared/complete counts and canonical digest before EXECUTION_COMPLETE. Targeted positive/negative Python control-double checks passed. |
| NCP-REV-04 | High | A group snapshot taken before polling the leader could miss a fork immediately followed by leader exit. The executor then committed a partial payload as COMPLETE and the collector returned COLLECTED. | `GUARD_EXIT_RACE_RED.json` reproduces `PARTIAL_NOT_FINISHED\n` as committed output. Fresh post-exit scan plus `killpg(pgid, 0)` presence check closes the interleaving: `GUARD_EXIT_RACE_GREEN.json` records DESCENDANTS_SURVIVE_LEADER, INCONCLUSIVE collection, and no committed payload. |
| NCP-REV-05 | High | Raw `/proc` PID/PPID values were compared to namespace-local Popen PID values, losing RSS and descendants in this actual environment. | The executor author independently found the failed RSS/child tests; reviewer confirmed `/proc/self` and `os.getpid()` differ and identified the same launcher defect. Both paths now filter by PID namespace and map NSpid/NSpgid; launcher maps PPid through host→local IDs and refuses unsupported self mapping. Reviewer reran the live-child/RSS/parent mapping regression successfully. |
| NCP-REV-06 | Medium | Native fixture `env={}` discarded the sidecar LD_LIBRARY_PATH before executing the dynamically linked backend. Launcher environment alone could not repair it. | Shared root/reviewer finding. Final `native_receipt` requires a canonical explicit library directory, reads and checks supplied BUILD_READY and referenced identities, binds library/source/compiler/chain bytes, and puts LD_LIBRARY_PATH in task.env. Reviewer read the change and four metadata tests; the author reports those tests pass. Source-level closed; no native execution inferred. |

## Boundary assessment

The invocation-local cache preserves the original source helpers, full complex input balls, working precision, coefficient conversion position, left-associated per-term multiplication tree, and sequential accumulation order. Its three nine-slot caches have no cross-call or cross-thread global state. Mutable Contract/CacheStats remain caller-owned. This establishes a conditional structural argument; native Arb exact-ball equality still requires the unavailable pinned backend/toolchain and has not been inferred from rational-model/static checks.

The parent's final fixture-only change explicitly sets FLINT to one thread and checks the readback before evaluation. Reviewer read the added header and set/get calls and bound the updated fixture hash. Native compilation remains zero. The BUILD_READY adapter binds supplied receipt bytes; it neither independently witnesses a build nor establishes current dynamic-loader behavior. Those checks remain host execution obligations.

Task manifests bind raw manifest bytes and exact executable/input/library identities, argv, explicit environment, semantic identity, and resource limits. Payloads are copied/renamed and hashed without scientific parsing or floating reduction. Existing task directories must pass COMPLETE identity checks; failed, partial, stale, missing, extra, duplicate, or tampered tasks cannot yield a successful collection. Optional semantic/library fields do not independently certify scientific meaning or a complete dependency closure.

The Fortran dispatcher exchanges only integer scheduling/status data and drains active workers after a reported failure. The normal successful-worker protocol has no evident message-count deadlock in source review. Actual MPI runtime behavior, rank loss, mpi_f08 compilation, wrapper ABI, and NCP scaling remain unverified. The local C shim uses literal argv, a distinct process group, signal relay, bounded timeout, environment filtering, and close-from descriptor actions.

The host planner uses observable affinity, distinct physical cores unless SMT is requested, visible ancestor quota and remaining-memory minima, coordinator reservation, and actual OS affinity readback. Per-process RLIMIT_AS and sampled aggregate RSS are separate claims. Neither task/group sampling nor build slot memory reservations are hard aggregate cgroup memory bounds. Deliberate process-group/session escape and externally killed supervisors remain outside the local task guard's guarantee. Hidden cgroup ancestors remain unobserved.

`backend_build/build_fast.py` changes bounded build concurrency while reusing the pinned extraction, stage execution, and provenance gates and retaining strict backend arithmetic flags. No concrete defect was found in that bounded source review. Build/equality/MPI/NCP performance claims remain conditional on host execution.

## Independent verification and unresolved observations

`INTEGRATION_GREEN.json` records one fresh two-task integration through the compiled local C shim, the real Python worker, and the real collector. Cost order was [1, 0]; both shim statuses were 0; both task results were COMPLETE; the collector returned exactly 2/2 and matched both independently constructed expected opaque payload hashes. This is C/Python control integration, not MPI or native scientific execution.

That integration used the frozen final core/guard and the general exact-rational factory branch before the independent native-receipt branch was added. The general branch was unchanged in the final source readback; no additional integration execution or native-receipt runtime test is claimed.

`FIX_CONFIRMATIONS.json`, the race RED/GREEN pair, and `PID_NAMESPACE_OBSERVATION.json` distinguish source review, independent reruns, and their limitations. The first race probe's own PID-observation mistake is preserved separately as `GUARD_EXIT_RACE_PROBE_FIXTURE_FAILURE.json`; it is not an implementation RED result.

The parent observed a benchmark checkpoint readback anomaly, and a reviewer temporary directory reappeared after a successful deletion readback. Root cause is **UNRESOLVED**; no causal explanation is asserted. The executor now reads back the final checkpoint/payload before returning COMPLETE and preserves failed readback evidence. This is a fail-closed mitigation, not proof that the storage issue is fixed. Final sequential parent verification is outside this review. Temporary `exit_race_*` and `integration_*` directories are reproducible scratch and must be excluded from delivery.

Final reviewed source identities and acceptance ceiling are recorded in `INDEPENDENT_REVIEW.json`. Parent final sequential tests, benchmark, packaging, publication, and backup are separate delivery actions.
