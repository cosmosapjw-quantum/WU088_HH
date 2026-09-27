# R31T full-pair performance research loop

Scope: preserve frozen107 scientific arithmetic and checkpoint identity while finding a faster host layout for the next z=1 discriminator on the Ryzen 9 5900X host.

## Baseline from durable z=2 H states

The current R31M host profile was selected using a foreign-component benchmark. The z=2 full-pair traces show that the complete pair has a different bottleneck structure because each pair performs two serial H0 calls before the threaded foreign kernel.

Measured durable z=2 baseline:

| basis | compute-wave sum | observed first-wave-to-last-wave end | non-compute gaps | pool worker utilization | mean CPU-seconds / pair-wall-second | max worker RSS |
|---|---:|---:|---:|---:|---:|---:|
| B160 | 491.90 s | 953.78 s | 461.88 s | 97.64% | 6.75 | 124.5 MiB |
| B192 | 720.83 s | 1855.39 s | 1134.55 s | 97.46% | 6.64 | 157.8 MiB |

The current 2-process x 12-thread wave scheduler is therefore already close to fully occupied **at the worker-slot level**. Reordering pairs alone has little headroom. The main CPU question is process/thread decomposition, because a 12-thread pair consumes only about 6.6-6.8 CPU equivalents on average.

The 12 delta archives for each basis total only about 0.46 MB. The large inter-wave gaps therefore do not look like bulk-bandwidth cost; provider transaction/readback latency dominates the non-compute wall.

The user's 96 GB RAM is not a current capacity constraint. Even a conservative 12-worker extrapolation from measured B192 RSS is under 2 GB before extra cache headroom. RAM can instead be spent on more outer workers, persistent workspaces, or later source-exact caches.

## First discriminating benchmark

Before changing the production route, benchmark the **actual full pair** at B192,z=2. Existing completed z=2 pair checkpoints are the exact reference. The benchmark recomputes 12 wall-time quantile pairs in memory and requires exact equality of:

- H0 array
- H0 sumabs
- normalized foreign array
- foreign sumabs

Any mismatch or overlapping affinity disqualifies a layout.

Screen layouts:

- 12x1 physical
- 6x2 physical
- 12x2 SMT
- 6x4 SMT
- 4x6 SMT
- 3x8 SMT
- 2x12 SMT (current route)

The script records H0 and foreign wall times separately. This directly tests the hypothesis that more outer processes hide the serial H0 fraction better than the foreign-only 2x12 optimum.

No benchmark result is automatically applied to the scientific provider or checkpoint route.

## Secondary candidates after topology measurement

1. **Cross-resolution validation.** Confirm the selected full-pair layout on B160 before changing the z=1 route.
2. **Exact H0 concurrency.** The two active=0/1 H0 calls are independent and the native H0 source has no mutable shared scientific state. A benchmark-only dual-call experiment can test whether concurrent H0 calls improve layouts with at least two physical cores per worker. Exact arrays are mandatory.
3. **Exact H0 cell parallelism.** If H0 remains dominant, compute independent (i,j) cells in parallel, store cell contributions, then merge in canonical i,j order. This can preserve the defined accumulation order at the cost of tens of MB per worker, trivial on 96 GB. This is a new scoped provider candidate and needs its own exact regression before promotion.
4. **Per-exponent/gamma cache.** The foreign kernel repeatedly recomputes exponent-specific `powl/exp` tables across the 12x12 exponent matrix. A process-local immutable cache can trade tens of MB for fewer transcendentals. It must preserve the exact expression association used by the admitted candidate.
5. **znver3 compile probe.** `-march=znver3 -mtune=znver3` can be benchmarked with `-fno-fast-math -ffp-contract=off` retained. Do not promote unless science-resolution arrays remain exact.

## Durability bottleneck is separate

The z=2 traces show more non-compute gap than compute wall. Two acceleration policies are scientifically neutral but have different durability semantics:

- **strict current policy:** at most 12 unacknowledged H pairs, stop for dual raw-readback ACK after each delta;
- **cross-state pipeline:** while B160 delta backup is in flight, compute a bounded B192 wave (and vice versa). This preserves <=12 unacknowledged pairs per state but can expose up to 24 globally;
- **node-close remote backup:** keep create-only pair checkpoints on local NVMe and dual-back up only the completed H basis state. This has the largest expected wall reduction but relaxes the present remote-durability cadence.

The benchmark branch does not change durability policy. A separate explicit decision is required before either alternative is used.
