# R31M scoped foreign-kernel promotion decision

## Decision

`PASS_SCOPED_FOREIGN_KERNEL_EXECUTION_PROMOTION`

Scope: future WU088 heavy-H source runs may use the R31M candidate for `mh_wide_foreign`
through the opt-in sidecar adapter. H0, grid, frozen R30 provider gate, scientific assembler,
B160/B192 convergence, full49, trajectory and production gates are unchanged.

This is a separate assistant decision review, not an independent human review.

## Evidence

Target host: Ryzen 9 5900X, 12 physical / 24 logical CPUs, two L3/CCD groups.
The host profile selected 2 processes x 12 OpenMP threads, SMT enabled, with each process
restricted to one CCD. All topology benchmark samples were exact-array equal to the reference.

Science-resolution gate: B160/g80 at z=16 and z=64. Fast/median/slow timing-profile pairs,
three at each z, all returned exact candidate/reference foreign arrays and exact `sumabs`; the
maximum observed component delta was zero and every candidate call observed 12 OpenMP threads.

Input SHA-256:
- HOST_TUNING_PROFILE.json: `720d9b7bc4f2e6fe3b95c05b0f47a6c790286251c8214a38b7705a2e8d399b61`
- SCIENCE_RESOLUTION_NATIVE_REGRESSION.json: `b8cb63344d82e84d5b2487d19b368ed9fe389c4ff472ef058fc233844f59c8ff`
- candidate source: `696afa2875490b0ebd82d43fe5e6c2852529d0cb7b5e1544cfa6ed71fff984a2`

## Arithmetic-equivalence argument

The candidate does not parallel-reduce the final gamma sum.

1. The reference evaluates each gamma plane independently. The candidate evaluates those same
   planes concurrently and stores each plane in `planes[h]`.
2. Inside one plane, the `active` index list is generated in the same row-major `(i,j)` order as
   the reference loop, using the identical exact-zero predicate. Therefore the compensated `Sum`
   update sequence inside a plane is unchanged.
3. After all planes complete, the candidate loops over `h=0..ngamma-1` in the original order and
   applies the same `total[c].add(gweight*plane[c])` sequence. OpenMP completion order is not used
   in the scientific accumulation.
4. Hoisted `powl`/`exp` terms are evaluated with the same inputs and the same multiplication
   association; fast-math and FP contraction remain disabled. Each OpenMP worker explicitly
   rejects a non-`FE_TONEAREST` environment.
5. Scientific shared data are read-only; each OpenMP iteration writes only its own `planes[h]`.

Thus the parallel execution changes scheduling, not the defined floating-point accumulation order.
The measured exact-array checks support this structural argument at low-order topology probes and
at B160/g80 representative science resolution.

## Runtime route

The frozen runtime shared object is not overwritten. `scripts/run_tuned_heavy.py` builds the
reference and candidate side by side, verifies the host-bound tuning profile and science regression,
and invokes `vendor/orchestration/r31m_tuned_local_adapter.py`. The adapter records candidate build,
binary, profile and regression identities in every new scientific checkpoint.

The cost-aware orchestrator now keeps one process pool alive across a bounded checkpoint wave.
With a 2-process profile and `max-new-pairs=12`, the two workers consume up to twelve cost-ordered
pairs without six separate pool spawns. The maximum unacknowledged pair count is unchanged.
If the wall-time budget expires, no new task is submitted; already-running tasks drain, then the
usual durable delta/dual-backup barrier applies.

## Claim firewall

This decision does not:
- rewrite or reinterpret completed anchor pair states;
- lower precision or enable fast-math;
- admit B192 convergence from B160 evidence;
- admit O/D/dotO/ionic full49 inputs;
- authorize interpolation, propagation, observables or production cross sections.
