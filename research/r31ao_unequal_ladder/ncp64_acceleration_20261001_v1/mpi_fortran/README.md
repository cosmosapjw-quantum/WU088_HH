# Integer MPI dispatcher and isolated worker bridge

The Fortran `mpi_f08` program dispatches manifest task indices dynamically. Rank 0 reads the longest-cost-first worklist; ranks 1 through P−1 each run one Python worker at a time. P=1 uses the same order sequentially. Scientific payloads remain task-local files for the canonical Python collector. There is no MPI floating reduction, floating task cost, modified numerical tolerance, or scientific SIMD claim.

This host requires GNU Fortran, OpenMPI `mpi_f08` wrappers, and GNU/Linux glibc >=2.34 (`posix_spawn_file_actions_addclosefrom_np`). Compiler or runtime absence is a refusal, not simulated MPI success. **This environment has gcc/g++ but no gfortran, mpifort, mpicc or mpirun: only the C bridge was compiled/executed here. Fortran compile and 1/2/4-rank MPI runtime acceptance remain UNVERIFIED.**

## Frozen API

```
ABS_BUILD_DIR/ncp64_dispatch ABS_PYTHON ABS_WORKER ABS_MANIFEST ABS_WORKLIST
ABS_PYTHON ABS_WORKER --manifest ABS_MANIFEST --task-index ZERO_BASED_INDEX
```

`ABS_WORKER` is `executor/worker.py`. Exit 0 means COMPLETE/REUSED; nonzero means failure/inconclusive. The text worklist contains a first line task count N followed by exactly N rows `task_index supervisor_timeout_seconds`. Indices form a permutation of 0..N−1. `export_worklist.py` exports manifest `dispatch_order`, requiring cost_hint descending and task_id ascending for ties; absent order is computed the same way. Each deadline is task `wall_seconds+10`, bounded by 86410 seconds. Task cost is a scheduling hint only.

The exporter checks the metadata needed for scheduling. It does not confer provenance or synthetic authorization merely from a scope string. The executor and host launcher must independently verify complete task identities and allowed backend inputs before launch; the worklist is bound to its manifest by its SHA receipt and the launcher's exact content check. The dispatcher never parses an array or supplies an alternate numerical implementation.

Control messages carry only two default Fortran integers: task index/deadline or task index/status. Rank 0 keeps the active task for every rank, checks completion identity, and records dispatched/completed/failed/not-dispatched counts. The `!$omp simd` loop initializes integer job state and totals integer supervisor budgets; its report is compiler evidence about bookkeeping only. It is not a claim that any scientific kernel was vectorized or accelerated.

## Failure and process lifetime

Ordinary worker failure stops new dispatch. Rank 0 drains already active bounded workers, sends each a STOP message after its completion, broadcasts final failure, and finalizes MPI. Idle ranks receive STOP initially. Workers always send completion after the C bridge returns, including spawn errors, nonzero exits and watchdog expiry. Thus a failing Python task is not silently dropped and does not strand the coordinator waiting for an unreported result.

Every checked MPI error calls `MPI_Abort`. This is not an MPI fault-tolerant/ULFM implementation: abrupt loss of an MPI rank or a broken transport may require the **outer host launcher's whole-job deadline and descendant cleanup**. An arbitrary OS process stuck in an uninterruptible kernel wait is not guaranteed to be reaped within a user-space timeout.

The C bridge uses `posix_spawn`, never a shell or a post-MPI `fork` callback. All three path arguments are absolute, bounded regular files, and the interpreter is executable. Exact argv tokens preserve spaces/metacharacters. It removes OMPI/PMI/PMIX/MPI/MPICH/I_MPI/HYDRA environment variables, forces common thread-count variables to 1, and closes all inherited descriptors >=3 in the child. The Python worker has a new process group and inherits the rank's CPU affinity/resource limits.

`waitpid` retries EINTR. A monotonic watchdog or SIGTERM/SIGINT to the waiting rank sends SIGTERM to the worker group, permits five seconds for cleanup, then sends SIGKILL if necessary. The executor's SIGTERM handler must kill and wait for its separately grouped backend before returning. Any remaining member of the bridge's own worker group is killed on return; leader exit0 plus a remaining group returns failure 1106. Other reserved statuses: 1100 invalid arguments/files, 1101 environment allocation/cap, 1102 spawn attributes/actions, 1103 spawn/setup failure, 1104 wait error, 1105 clock error, 124 watchdog, 128+signal interrupted/signalled worker. Normal worker exit codes are preserved.

The worker's separately grouped backend is deliberately outside the bridge's group kill; it is managed by the Python worker and tracked by the outer launcher. SIGKILL of that Python worker or MPI rank cannot run its cleanup handler. The outer descendant guard is consequently mandatory for host runs. This is a stated containment limit, not an assertion that process groups alone provide an inescapable sandbox.

## Build and host acceptance

Use a user-selected Python on the target host. First record the exact wrapper SHA256 values (`sha256sum /ABS/mpifort /ABS/mpicc`); review their intended OpenMPI installation. Then:

```bash
python /ABS/NEW/mpi_fortran/build.py --output-dir /ABS/NEW_BUILD \
  --mpifort /ABS/mpifort --mpifort-sha256 EXACT_SHA256 \
  --mpicc /ABS/mpicc --mpicc-sha256 EXACT_SHA256
python /ABS/NEW/mpi_fortran/host_smoke.py \
  --mpi-binary /ABS/NEW_BUILD/ncp64_dispatch --output-dir /ABS/NEW_SMOKE
```

All placeholders denote actual absolute paths; outputs are create-only. The build records wrapper bytes, OpenMPI version, `--showme` command/compile/link, configured compiler identity/version, source/binary hashes and all command logs. Wrapper invocation paths are preserved rather than replacing a multi-call wrapper's name with its resolved symlink target. Flags include `-O3 -fno-fast-math -ffp-contract=off`; Fortran additionally uses `-fopenmp-simd` and emits `integer_vectorization.txt`. Wrapper-file pinning and captured compiler configuration do not constitute an independently pinned closure of all compiler/runtime dependencies.

`host_smoke.py` creates 12 uneven **integer CPU-work** fixture tasks for each of 1, 2 and 4 ranks using `executor/make_fixture.py`, exports worklists, then uses the existing topology/memory-aware `host_plan/launcher.py`. The launcher measures/validates host capacity, binds ranks and owns deadline/descendant cleanup. Each fixture has an independent exact expected payload hash. Acceptance requires all three runs to collect every task and yield identical `canonical_payload_digest`; manifests/output roots themselves differ intentionally. Insufficient capacity or missing MPI is INCONCLUSIVE. No MPI root bypass, oversubscription or synthetic-to-scientific promotion is requested.

After this acceptance, host performance measurements may report elapsed times and scheduling counts for these fixtures. This turn claims neither a NCP speedup nor a scientific-result certificate. Actual HH arrays, constants, integrals, archived comparator execution and physical promotion remain outside scope.

## Local evidence

`C_SHIM_GREEN.log` and `C_SHIM_EXECUTION.json` contain fresh gcc compilation and synthetic bridge tests. `REVIEW_GROUP_RED.log` records the genuine leaked-group regression before its fix; `TEST_FIXTURE_RED.log` separately records an initial test-helper name collision and is not counted as a production failure. `BUILD_REFUSAL.log` / `LOCAL_MISSING_TOOLCHAIN/BUILD.json` show the expected missing-toolchain refusal. `VERIFICATION.json` binds final files and states exactly which branches were exercised. No Fortran/MPI pass is inferred from C tests or static source review.
