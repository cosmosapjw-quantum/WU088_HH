# PHYS87 frozen implementation — preparation only

Scientific authority is CONTRACT revision2 SHA256 `464df6f83a7ac8bd64813dc9da3ca34f19398a2f970f3d69c706e3d089f6fd38` and `theory/NATIVE_FINITE_T_MOMENTS_KO.md`. S0 checkpoint is `b4e606c433bc0d7969227635b62f33e67a56c705`, with fixed PHYS86 parent `f4a6d5505c845a046e3b81d33a2992a239ab4c8b`. Requested executor gpt-6.1-sol/high; actual backend UNOBSERVED. No source, guard, quadrature, plotting or numerical test was executed during preparation. Only Python AST/compile-to-code-object syntax and byte identities were checked; no candidate code objects were executed.

## Equation → source → output

| Contract/theory obligation | Implementation |
|---|---|
| Raw source hash/153 MF3+MF6 rows | `source/native_moments.py`: NativeSource reads canonical bytes once; fixed-field ENDF Decimal parser; MF3 TAB1 and MF6 TAB1/TAB2/LIST branches; all raw literals and Decimal strings bound to SOURCE_TABLE. ZA/AWR, Q, LCT2, LAW2/LANG0/NL2, yield1, recoilLAW4 and interpolation checked. |
| Native interpolation | MF3 INT5 on lower indices0..31 (through one-based knot33), then INT2; MF6 coefficients INT2; exact represented knot returns; outside source support unavailable, never zero-filled or clipped. |
| Positive angular law | Exact Fraction quadratic endpoint/eligible-vertex minima for153 knots;152 exact coefficient-difference witnesses for whole-cell convex interpolation. |
| Conditional directed moments |18 frozen E/beta/axis cases; positive4GL-mu×8uniform-azimuth rule versus analytic a1/a2 moments; mean and centered variance residuals, actual per-event energy closure. |
| Eq(1), scaled Bessels | Positive log-E native-cell quadrature retaining all152 intervals, orders16/32. Terms0..6 K1/K2 polynomial coefficients constructed with Fraction; exact differences and exact gamma-variance numerator coefficients cancel before float evaluation. |
| Eq(3)-(4) | Same positive normalization supplies Kin/Egamma/Kd means, centered total variances and pair covariances; stable K, gamma-minus-one and daughter kinetic representation; no subtraction of raw O(rest-energy²) moments. |
| Eq(5), owner/caloric rows | Order32 only:4T×2h×2exclusive radiation routes=16 rows. Thermal/fast/nuclear/atomic/radiation columns, free-electron incidence0 and Cv*Tdot/R in eV/event. No R, density or Cv invented. |
| Finite-difference slope |10000K and1e8K; hlog=2^-8;4 extra order32 rate-only calls. Exact integration ledger8full+4scalar=12. |
| Guards | Energy/T/nonfinite, owner/routes, directed domains, quadrature order and bare-network convention rejection; no valid unplanned thermal integral. |
| Complete first output | `source/run_primary.py`, fixed `results/primary001/`: create-only initial marker, complete RESULT/CSV/positivity witness/output manifest, preservation of first failure. |
| Reuse | `--resume` reads input/code/output identities and returns SKIP/scientific_callbacks0; does not import native module or NumPy, start integrations or rewrite files. |
| Saved figures | `source/plot_saved_results.py` reads only RESULT;2PNG+2PDF. Native-knot and4T connecting lines explicitly labeled visual guides, with no continuum/INT2-curve claim. |

All angular/quadrature/FD/energy acceptance comes from the frozen CONTRACT values. Exact positivity and strict positive variances use their mathematical signs. Outputs remain conditional evaluated-source finite-window evidence, with root admission pending and HH_R10=OFF/production NOT_ISSUED. Underflowed Boltzmann nodes and wholly underflowed sampled cells are counted explicitly; no exact tail-zero claim follows.

## Actual primary schema agreed with independent reference

`results/primary001/RESULT.json` has `thermal_results`: exactly8 full rows with `T_K`, `order`16/32 and `rate_only:false`. The independent reviewer selects the unique row `T_K=100000000.0,order=32` and directly reads:

- `kappa_cm3_per_s`
- `mean_Kin_eV`, `mean_Egamma_eV`, `mean_Kd_eV`

Additional direct fields are the three `variance_*_eV2`, three pair `cov_*_eV2`, `u_n_eV/u_H_eV/u_D_eV`, selected log-rate slope, energy residual and underflow counters. Other report collections are `owner_rows`16, `angular_cases`18, `finite_difference_rates`4, comparisons, checks/failures, guard records, coefficient record, native knots and actual integration-call ledger. Source uncertainty/covariance propagation and continuum accuracy are not granted. `verification/independent_reference.py` belongs exclusively to the independent reviewer; this implementation does not import or edit it.

## Fresh pinned gate and fixed CPU mapping

`source/vendor/phys78_run_pilot.py` is an exact unchanged full28,068-byte gate, SHA256 `76ff57ba687fd9830b84c3fcff69eb8ed0e9f6ceab4551e61c67c84d3ea65124`. Its original resource/lease functions retain CPU-affinity/quota/ancestor-cgroup sampling, reserve1.5GiB+job0.5GiB and live-lease accounting. No parent gate function is modified or historical runner called.

`source/leased_call.py` checks exact contract/gate bytes and availability of CPU0+CPU8, observes other live leases before acquisition, calls the original LeasePool.acquire, rejects a post-acquire observed peer conflict, and reads fresh MemAvailable plus every original cgroup memory ancestor immediately before launch. It requires the unchanged reserve+job, pins the mechanical coordinator toCPU8 and the single scientific child toCPU0, sets thread env1, imposes RLIMIT_CPU and launch-inclusive wall timeout, records actual CPU/wall/affinity/resource observations, releases only its own lease, and restores its original affinity. No CPU55 fallback, cache credit, peer termination or automatic retry.

Optional `--admission-receipt` writes a distinct create-only **actual prelaunch** JSON after the acquired own lease, fresh memory pass and actual coordinatorCPU8 pin. It states that child affinity/caps will be enforced by preexec, without claiming a child result before launch. The final wrapper receipt binds its exact bytes/SHA. The independent reference receives this existing file via `--controller-admission-receipt`; it is not passed the not-yet-written final wrapper receipt.

Fresh gate failure returns a preserved WAITING receipt with child_invocations0. This is not permission for an automatic retry. Actual wrapper receipts preserve primary CPU12/wall60, referenceCPU20/wall60 and figureCPU8/wall30, plus coordinator CPU separately.

## Exact commands — only after S1, stage ACKs and root dispatch

Use the primary runtime Python and absolute unit path below. The primary output path is fixed; never launch a second output directory for the same scientific identity.

```bash
PY=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
UNIT=/workspace/scratch/ebcaaaa20861/WU088_HH/research/hh_phys87_endf_np_native_moments_20261024
"$PY" -B "$UNIT/source/leased_call.py" --kind primary --label primary001 --receipt "$UNIT/results/primary001_lease.json" --admission-receipt "$UNIT/results/primary001_admission.json" -- "$PY" -B "$UNIT/source/run_primary.py" --output "$UNIT/results/primary001"
```

Read-only completed-output reuse (no new lease or scientific child):

```bash
"$PY" -B "$UNIT/source/run_primary.py" --output "$UNIT/results/primary001" --resume
```

Reference runs only after actual primary output and root review/dispatch. The controller supplies the **actual SHA256 of the complete primary RESULT bytes** in place of `ACTUAL_PRIMARY_RESULT_SHA256`; this value cannot be known during preparation.

```bash
"$PY" -B "$UNIT/source/leased_call.py" --kind reference --label reference001 --receipt "$UNIT/results/reference001_lease.json" --admission-receipt "$UNIT/results/reference001_admission.json" -- "$PY" -B "$UNIT/verification/independent_reference.py" --unit "$UNIT" --primary "$UNIT/results/primary001/RESULT.json" --expected-primary-sha256 ACTUAL_PRIMARY_RESULT_SHA256 --output "$UNIT/results/INDEPENDENT_REFERENCE.json" --controller-admission-receipt "$UNIT/results/reference001_admission.json"
```

One saved-results render, only after root admission/dispatch:

```bash
"$PY" -B "$UNIT/source/leased_call.py" --kind figures --label figures001 --receipt "$UNIT/results/figures001_lease.json" --admission-receipt "$UNIT/results/figures001_admission.json" -- "$PY" -B "$UNIT/source/plot_saved_results.py" --result "$UNIT/results/primary001/RESULT.json" --output "$UNIT/results/figures001"
```

All commands are also structured in `EXECUTION_COMMANDS.json`. No automatic probe/retry/repair allowance is encoded. Preserve raw outputs and first failures; return concrete findings to Astra. Git publication, provider ACK/restore and scientific admission remain separate controller actions.
