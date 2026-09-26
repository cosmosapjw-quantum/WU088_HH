# R31M host-autotune design and gate

Scope: hardware scheduling only. The frozen107 scientific model, quadrature tolerances,
checkpoint bytes, B160/B192 order gate, and full49/trajectory claim ceilings are unchanged.

## Motivation from the first Ryzen 9 5900X host benchmark

The first host run used the same 12-thread budget for every configuration.  The observed
median pool wall times were:

| outer processes | inner threads | median wall (s) | speedup vs 12x1 |
|---:|---:|---:|---:|
| 12 | 1 | 2.87427 | 1.000 |
| 6 | 2 | 1.82544 | 1.575 |
| 3 | 4 | 1.62588 | 1.768 |
| 2 | 6 | 1.60916 | 1.786 |
| 1 | 12 | 2.03275 | 1.414 |

For one foreign-component call, 12 OpenMP threads reduced the measured median from
1.79439 s to 0.277376 s, about 6.47x, while every reported numerical array remained
exactly equal to the reference.  These measurements did not explicitly pin each outer
process to a disjoint CCD/core set and did not probe the 24 logical CPUs, so they are
provisional evidence rather than a final host profile.

## R31M changes

1. Read Linux SMT sibling and L3 shared-CPU metadata in addition to package/core IDs.
2. Partition worker affinities into disjoint groups.  Keep a worker within one L3 group
   whenever possible.  For SMT configurations, keep sibling pairs in the same worker so
   two workers do not silently fight over the same physical cores.
3. Benchmark both the physical-core budget and, when available, the SMT logical budget.
   The 5900X candidate set includes 12x1, 6x2, 4x3, 3x4, 2x6, 1x12 and 12x2,
   6x4, 4x6, 3x8, 2x12, 1x24.
4. A worker-start barrier is part of the benchmark harness.  Timing does not start with
   only a lazy subset of the requested process pool alive.
5. Select only configurations whose candidate arrays and sumabs arrays are exactly equal
   to the reference and whose observed affinity sets are disjoint.
6. If multiple configurations are within 2% of the fastest median, prefer fewer workers
   crossing L3 boundaries.  This makes a CCD-local 2x6 configuration eligible to beat a
   marginally faster but cross-CCD 3x4 configuration without hard-coding the 5900X.
7. Bind the selected profile to CPU/topology/affinity metadata and the candidate native
   build key.  A changed build or host invalidates the profile.

## Commands

Run the topology-aware benchmark:

```bash
export WORK=/mnt/sn850x2t/hh_heavy_manual_20260926
export RUNTIME="$WORK/runtime/WU088_HH_LOCAL_RUNTIME_SEED_20260926_v2"
source "$WORK/venv/bin/activate"
cd "$HOME/WU088_HH"
bash scripts/benchmark_host.sh
```

The output directory contains `HARDWARE.json`, the component benchmark, the topology
pool benchmark, and `HOST_TUNING_PROFILE.json`.

Before any candidate native provider is promoted, run the science-resolution
representative gate:

```bash
python scripts/representative_native_regression.py \
  --runtime "$RUNTIME" \
  --tuning-profile "$WORK/wu088_hh_bench_<run>/HOST_TUNING_PROFILE.json" \
  --out "$WORK/wu088_hh_bench_<run>/SCIENCE_RESOLUTION_NATIVE_REGRESSION.json"
```

This uses B160/g80 at z=16 and 64 and chooses fast/median/slow pairs from the frozen
performance profile.  It compares candidate and reference foreign arrays and `sumabs`
with exact array equality.  It does not mutate completed pair states and it does not
install the candidate into the production runtime.

## Claim firewall

A host tuning profile is a scheduling result, not a scientific-provider admission.
Even a passing representative regression remains `NOT_PROMOTED` until the independent
provider decision gate is explicitly closed.  No fast-math, precision downgrade,
scientific interpolation, threshold relaxation, or completed-anchor rerun is introduced
by R31M.
