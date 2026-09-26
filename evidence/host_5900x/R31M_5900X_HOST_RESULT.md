# R31M Ryzen 9 5900X host result

Source files:
- `POOL_Z64_TOPOLOGY.json` SHA-256 `de9755fd9a2c4f778f66aaba6a482ca1ca78af40bee979af43760d264a0d1b4f`
- `HOST_TUNING_PROFILE.json` SHA-256 `720d9b7bc4f2e6fe3b95c05b0f47a6c790286251c8214a38b7705a2e8d399b61`

## Result

The measured host is AMD Ryzen 9 5900X with 12 physical / 24 logical CPUs and two L3 groups (CCDs).
All 36 candidate samples preserved exact reference arrays, observed the requested OpenMP team size,
and used disjoint process affinity sets.

The selected configuration is:

- outer processes: `2`
- inner kernel threads: `12`
- SMT: `True`
- cross-L3 workers: `0`
- median 12-pair wall: `1.488254210999` s
- selection: `FASTEST_MEDIAN_EXACT_CONFIGURATION`

For comparison:

| configuration | median wall s | speedup vs 12x1 |
|---|---:|---:|
| 12x1 physical | 3.327793676001 | 1.000 |
| 2x6 physical | 1.664738640000 | 1.999 |
| 3x8 SMT | 1.488767831999 | 2.235 |
| 2x12 SMT | 1.488254210999 | 2.236 |

`2x12 SMT` is only `0.0345%` faster than `3x8 SMT` by median, so those timings
are effectively tied at this sample count. The selected layout is nevertheless preferable for the current
policy because both 12-thread workers remain entirely within one L3/CCD, whereas the 3x8 layout has one
cross-L3 worker.

SMT improves the corresponding CCD-local 2-process layout from 2x6 to 2x12 by
`11.86%` in wall time, while increasing aggregate pair CPU time. The tuning target
here is wall-clock throughput, not energy efficiency.

## Claim ceiling

This is a host scheduling result. It does not promote the native candidate into the scientific provider.
The next gate is the B160/g80 representative native exactness regression at z=16 and z=64 using the
host-bound tuning profile. Completed anchor pair states remain immutable.
