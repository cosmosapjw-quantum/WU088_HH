# PHYS81 runner and rate-profile static review

## Decision and execution scope

**STATIC_READY_SCOPED for the declared fresh three-ODE cohort and fresh diagnostic rate-profile run, after the observed corrections below.** No blocking logic or dimensional inconsistency remains in the reviewed changed functions. This is a static conclusion, not a numerical acceptance decision. The parent owns syntax checks, the shared lease, the first scientific executions and their actual result receipts.

The reviewer did not import the numerical modules, evaluate a rate, call an RHS/Jacobian, execute an ODE or rerun a completed scientific identity. The review used source reads, hashes, and AST extraction of changed function text only. No reviewed code was edited. One bounded child review independently inspected the rate-profile normalization and source/API usage; it performed no numerical execution and wrote no files. No further reviewer recursion was used.

## Reviewed identities

| File | Initial SHA256 | Corrected SHA256 reviewed |
|---|---|---|
| `source/run_science.py` | `f39f9deb5cab58de2edfb541bdf7dbf6899f4699f9d2a832460069255d246a03` | `f7b7443c80fef386e070bbcd4019c59c16143c0b9b285e83c076c04d70eae4f4` |
| `source/rate_profiles.py` | `ac3cd76be25f40b48e2758d059303583195f0a443dc9da88bcf40de61c79d963` | `54063b5feb68851816535ae0aca3adceef423004524900ff1093d08eb864a936` |

Unchanged supporting files inspected:

| File | SHA256 |
|---|---|
| `CONTRACT.json` | `d20e465c23defb28e1e0ae321b75e0120d5e0c632e24b9b655d227007fee1821` |
| `source/parcel.py` | `e885bea7d9fb58ebf835facb2f54a2c24bce3e9c016dc78a0c41e8777f0ff758` |
| `source/finite_ci.py` | `e582e83650f39fbaf38e66be848d736845b2bbf38f52613c464ae4e2c1d77674` |
| `source/registry.py` | `280925bc250252da29e159dc9ca99f893c39d7fccbaace252a276f086fdcdd5f` |
| `source/vendor/bell_kernel_phys80.py` | `075f24cb0315f5d812b422f151f76ccc5ff8f2932306da4e88f848cc3e5951a1` |
| `source_data/BELL1983_VISUAL_TABLE_TRANSCRIPT.json` | `1c05cee3d7704857b20e8442ee8d9b9f86acdf70550a92a6d9c966f9ab7dbf4c` |

The Bell kernel/transcript identities and dimensional conventions were inspected by the bounded independent profile reviewer. The current runner/profile function bodies and their new hashes were then read directly by the integrating reviewer.

## Concrete initial findings and observed resolution

### R1. Resume could bypass a failed cohort comparison — resolved

Initially, `run_science.py:81–82` returned `RESUME_VERIFIED` after checking individual COMPLETE records and NPZ hashes, without reading the cohort summary. Individual invariant gates can pass while the independent-coordinate/refinement comparison fails, so that path could return a successful resume exit for a failed cohort.

The corrected `main`, lines 95–101, recomputes comparisons from saved arrays and requires a saved `PASS_SCOPED` summary, the same binding digest, the same trajectory-hash map, identical stored comparison results, and passing comparison gates. `one`, lines 37–40, also requires the individual record's `status == COMPLETE` and `ODE == 1`. Thus resume is an integrity/readback check, not an alternate route around failed scientific acceptance. It does not call `solve_ivp` for completed records.

### R2. Normal invocation could overcount newly executed ODEs — resolved

Initially, the cohort summary used `len(records)` for both new ODE attempts and completions, even though `one` can return `VERIFIED_SKIP` with `ODE=0`. This could label reused records as new integrations.

The corrected lines 102–103 use `sum(r['ODE'] for r in records)` and separately report reused completed identities. The summary is written only after the returned cohort is complete. An exception during a solve instead leaves the per-attempt failure receipt; no successful cohort summary is inferred.

### R3. The full7 comparison included an avoidable normalization roundtrip — resolved

Initially, `decoded` multiplied the original normalized state by B/u0 in `full_lift` and divided those decoded values again to build `scaled7`. It did not apply a conservation projection, but this was not literally the raw solver state and added an avoidable rounding operation.

The corrected `decoded`, lines 28–31, stores `y.T.copy()` for full7. The original normalized seven coordinates therefore enter the comparison verbatim. `full_lift` remains the independent diagnostic decoder for T and electron abundance; it decodes energy from w[6], sums the actual neutral and ion populations, and does not reconstruct an invariant state.

### R4. Profile identity and output completion were insufficiently bound — resolved for the create-only fresh-run scope

Initially, the profile output recorded only the registry hash. It omitted the Bell transcript/kernel, finite implementation, grid and runtime. JSON was written before CSV, so CSV failure could leave an apparently finished JSON output.

The corrected `binding`, lines 16–18, binds all directly used code/source files, the temperature grid, quadrature settings and Python/NumPy/SciPy versions. A science ID is derived from that binding. `main` creates an exclusive claim before numerical evaluation, writes the CSV exclusively, hashes it, and writes the final JSON last with `COMPLETE_SCOPED`, its full identity, the CSV hash and quadrature receipts. An exception preserves partial completed rows, counters and diagnostic traceback in a failure receipt.

The profile tool remains deliberately create-only. Its existing-JSON guard refuses a second invocation; it is not an identity-validating profile resume API. An interrupted final JSON write still requires explicit inspection of the claim/failure/output bytes rather than treating mere file existence as a verified completed profile. This is a limitation of recovery behavior, not a path that returns a successful scientific result on corrupted input.

### R5. Adaptive quadrature discarded error status and allowed a nonfinite failure path — resolved

Initially, `quad(...)[0]` discarded reported errors and warnings. The test `result <= 0` alone would not reject NaN, and the old JSON serialization allowed NaN.

The corrected `bell_window`, lines 24–34, retains every segment's integral and reported absolute error, captures warnings, checks that the combined result/error are finite and the result is positive, and rejects warning-bearing or excessive-reported-error results. The profile row also rejects nonfinite float fields; `write_once` uses `allow_nan=False`. These are numerical diagnostic gates, not certified quadrature error enclosures.

### R6. Profile execution-count label described newly computed values as reused — resolved

The initial loop actually evaluated `maxwellian_at_order(...,64)` for every row but labeled its count `reused_generic_Bell64_profiles`. Only the generic code and cached quadrature nodes were reused, not saved profile values.

The corrected counter is `new_Bell64_evaluations_using_reused_kernel`. For a successful complete grid, the intended work is 27 finite-operator evaluations, 27 new Bell64 values and 27 new finite-window Bell integrals. These counts are to be confirmed from actual execution, not assumed from this review. The counters increment after successful returns; if a call fails, the failure receipt's counters describe completed calls before that failure, while the attempted failing call is evidenced by its traceback/detail. An aggregate execution ledger should retain that distinction.

## Confirmed model and coordinate relationships

### Exact time-coordinate scaling

The runner integrates s in [0,1] with t = s t_end. Its RHS is `t_end * parcel.rhs(t_end*s, z)` or the full7 equivalent; its hazard Jacobian is `t_end * parcel.jac(t_end*s, z)`. This is the exact chain rule for a fixed positive t_end. It does not shorten the physical time interval or approximate time dependence. The saved physical time is s times t_end. State tolerances remain tolerances in the selected dimensionless state coordinates.

The parcel API uses K in cm^3/s, nref in cm^-3 and electron abundance per reference H. Thus `nref * xe * K` has inverse-second units before multiplication by t_end. Thermal u is in eV per reference H. The chemical defects enter as event energy losses; the profile's incoming-energy mean is not added as an extra heat loss.

### Independent raw seven-state comparison

The full7 reference integrates `[N/B, X/B, u/u0]` directly with its own RHS and DOP853. It does not enforce `N+X=B` or reconstruct energy from the hazard first integral. The hazard runs use Radau, with base and refined tolerances, and are lifted into the same normalized seven-component coordinates for comparison.

The corrected `saved_comparisons` also requires exact equality of the saved sample grids. Comparisons use all seven normalized state entries and T differences normalized by the declared fixed T0. The Li7 abundance is small, but its N/B and X/B coordinates are directly compared instead of being hidden in an absolute abundance norm.

This is independent-coordinate and different-solver trajectory evidence on the saved grid. Both paths intentionally share the admitted rate implementation, source data and selected physical closure, so the comparison does not independently validate those shared inputs. It is not a continuum or uniform-in-time error certificate, and it is not a performance benchmark.

### Conservation gates and their limits

The per-run conservation gates evaluate nuclei closure and thermal-plus-chemical energy on the accepted solver mesh. Nonnegativity is checked on both accepted and saved sample states; trial/domain guards are also enforced by the parcel API. No clipping or invariant projection is applied to full7.

Hazard energy conservation is construction-based and cannot establish trajectory accuracy alone; the record says this explicitly. The raw full7/refinement comparisons provide the separate numerical obligation. The 161 dense-output samples bound only the saved sampled comparison, not the interpolation error between samples.

The current `minimum_fraction` gate value is zero and the implementation tests zero directly. Conservation tolerances apply to accepted mesh points; the review does not describe them as separately enforced dense-sample conservation gates. Any successful report must retain those scopes.

### Rate-profile normalization and units

For the Maxwellian rate

\[
K=C\theta^{-3/2}\int_l^h E\sigma(E)e^{-E/\theta}\,dE,
\qquad \theta=k_BT,
\]

the substitution E = l + theta*x gives dE = theta*dx. The transformed logarithmic prefactor is therefore `log(C) - 0.5*log(theta) - l/theta`, matching `bell_window`. There is no missing or double-counted Jacobian factor.

The Bell transcript's coefficients are in 10^-13 eV^2 cm^2; conversion by 1e-13 matches the Bell API. The finite and Bell kernels use consistent electron-mass and kB/eV conventions. All nine fixed temperatures lie within 255–50000 K, and the registry enforces H1/He4/Li7 order before the zip with the three Bell labels.

The finite operator remains zero outside its selected support by model definition. The full Bell result is a separately labeled analytic comparison model. The window fraction is a fraction within that Bell model, not an estimate of the physical missing CCC support. The x=800 truncation and the absence of a certified physical tail/interpolation/fit bound are disclosed. The full Bell order64 quadrature is not promoted to a proven convergence certificate by this static review.

## Identity/recovery boundaries retained

The ODE source/input/runtime/model/gate binding determines each solver's science ID. Existing completed identities are skipped only after record/hash checks. Claims and first failures are preserved; no completed ODE is relaunched by the reviewed resume path.

`results/parcel/PLAN.json` freezes this cohort. A changed-code or changed-tolerance recovery cannot reuse that same plan silently; it needs an additive new cohort namespace or equivalent explicit new-identity arrangement. Deleting prior claims/results is not part of the reviewed workflow. The review does not assert an automated recovery path for a failed claimed identity.

## Observed review commands and status

- Initial source/contract/API reads and SHA256 commands: exit 0.
- Read of the previously truncated `parcel.full_lift`/`full_rhs` section and registry: exit 0.
- `nl -ba` of the initial runner for finding anchors: exit 0.
- `rg --files` under the then-empty results directory: exit 1, with no output; this was a read-only inventory, not a scientific attempt.
- AST parsing and text extraction of corrected functions, without importing or executing them: exit 0.
- SHA256 readback of the corrected runner, corrected profiles and contract: exit 0.
- Readback of the corrected profile imports/serialization helper: exit 0.

Reviewer numerical evaluations, RHS/Jacobian calls, ODE attempts, completed-identity reruns and reviewed-code edits: **zero**. The actual first execution and its numerical verdict remain the parent's next obligation under the shared lease.

`HH_R10=OFF` and `production_admission=NOT_ISSUED` remain unchanged. No cosmological ODE, normal-frame transport or nuclear-rate activation is admitted by this runner review.
