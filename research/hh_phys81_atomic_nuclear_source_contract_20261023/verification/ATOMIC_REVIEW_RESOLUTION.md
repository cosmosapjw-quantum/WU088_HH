# PHYS81 atomic review — resolved findings and executed scope

## Decision

**PASS_SCOPED_DECLARED_FINITE_CI_OPERATOR_AND_POINTWISE_PARCEL.** The independent algebra review and the single authorized numerical run support the stated stationary-target, finite-support, piecewise-linear CI operator, its incident-energy moment and temperature derivative, and the seeded parcel's pointwise hazard/original-state equations and analytic Jacobian.

All 15 new check groups passed. This is a bounded numerical and model-consistency decision. Full physical-rate and production admission remain **NOT_ISSUED**. This verifier did not integrate an ODE or repeat a completed scientific suite.

The original `ATOMIC_STATIC_REVIEW.md` and `REVIEWED_INPUTS.json` remain unchanged. This document and `ATOMIC_REVIEW_RESOLUTION.json` supply the subsequent resolution and executed evidence without rewriting that history.

## Finding resolution

| Finding | Actual correction and remaining boundary |
|---|---|
| A1: collision approximation | `CONTRACT.json`, the theory, and the parcel API distinguish the stationary-target/electron-mass Maxwell average from the common-temperature thermal reservoir/EOS. The exact hazard reduction is a statement about those specified equations. Finite-mass double-Maxwell kinetic equivalence is outside the admitted model. |
| A2: units and hazard domain | Dimensionless abundances are per reference H, density is cm^-3, and thermal energy is eV/reference H. The contract requires positive initial neutrals, nonnegative initial ions below their species totals, and a positive electron seed. The zero-electron absorbing mathematical state is outside the selected active API. Strict domain guards and explicit neutral-underflow flags are implemented and checked. |
| A3: omitted channels | Bound-bound collisional excitation/de-excitation and associated radiative loss are explicitly omitted from the CI-only control. This condition is necessary for the written thermal-plus-chemical energy first integral. |
| A4: isotope provenance | The attached neutral He I evidence identifies 4He and matches the selected chemical energy. Li7 now uses the original Bushaw et al. isotope-specific literal, 43487.15940(18) cm^-1, converted by root with exact SI constants under a separate lease. The active loader and parcel use 5.39172060034581 eV. H is stated as an ordinary-H/HDEL convention. The source mismatch is documented without asserting an unverified natural-isotope-average explanation. |

The Li correction changes chemical energy accounting and its derivative through the temperature map. It leaves the cross-section samples, incident-energy windows, finite Maxwell rates, and their direct temperature derivatives unchanged. The executed active-loader check verifies propagation of the new chemical value into the actual parcel inputs.

The He and Li window ceilings remain below their daughter electronic excitation thresholds. That energy-conservation argument concerns ground-state targets and the specified single-impact ionization model. It does not prohibit neutral excitation in a real gas or supply a missing cross section.

## Actual execution and evidence

The reviewer compiled the finalized verifier without importing or evaluating the scientific modules:

```text
python3 -m py_compile /tmp/phys81_review/atomic/verify_atomic_finite.py
exit_code: 0
tool_chunk_id: 91cd78
```

Root then executed the exact finalized bytes once under the recorded shared lease, from the unit directory:

```text
python -B /tmp/phys81_review/atomic/verify_atomic_finite.py --output /tmp/phys81_work_20261023/WU088_HH/research/hh_phys81_atomic_nuclear_source_contract_20261023/verification/ATOMIC_FINITE_CHECKS.json
exit_code: 0
status: PASS_SCOPED
check_groups: 15
elapsed_wall_s: 1.0002963160077343
retained_H_evaluations: 1
old_science_suites: 0
ODEs: 0
```

The recorded environment was Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. The root lease receipt records one thread, no terminated processes, successful completion, and no old science runner invocation. Compilation and these run results are distinct evidence.

After the run, this reviewer read both receipts and rehashed every recorded input. All hashes still matched. The reviewer performed no additional scientific evaluation. The post-run work reduced already recorded error fields and created a byte-identical executable copy at `verification/verify_atomic_finite.py`.

| Evidence | SHA256 |
|---|---|
| Executed verifier and unit copy | `588f7a0f81f91bf3b6b92d4f4c5bfe3bfba2014ca2433b515cf352347c24042d` |
| `verification/ATOMIC_FINITE_CHECKS.json` | `6685db635de14da2cecb95946ec155342cf9ea742b5dbd8960504a9ea26a9d2a` |
| `verification/LEASE_ATOMIC_INDEPENDENT_001.json` | `15b3c56c9b038a22df644655417e64613d6bcceda692db8a69129f100fca970d` |
| `CONTRACT.json` | `d20e465c23defb28e1e0ae321b75e0120d5e0c632e24b9b655d227007fee1821` |
| `theory/ATOMIC_DERIVATION_KO.md` | `7bf21f07f60e7b481b3123bf7528fd8e5faa6b0c77470f9759179f16c77454d3` |
| `source/finite_ci.py` | `e582e83650f39fbaf38e66be848d736845b2bbf38f52613c464ae4e2c1d77674` |
| `source/parcel.py` | `e885bea7d9fb58ebf835facb2f54a2c24bce3e9c016dc78a0c41e8777f0ff758` |
| `source/registry.py` | `280925bc250252da29e159dc9ca99f893c39d7fccbaace252a276f086fdcdd5f` |
| Active admitted registry | `2415d357c318f1ff1307239f4f39c8009e6a7005b140c3ec67b492f631097641` |
| Immutable literal CSV | `522fd63bd4aead4314d7b4ea87f61e5454b23df0f046b1c8e48b2f2023272dad` |
| Li7 source-correction receipt | `ba8501980d048c7a9c69285c5406692d07379cc9e64b4dbad1e30a2dd641f940` |
| Preserved original review | `de33a0acafb1906ffc948d705fcb595ff9ce693e056ffbd88dcefb21c4420732` |

The JSON resolution additionally binds the retained vendor code/table/reuse identities and the initial input manifest.

## Numerical coverage and observed differences

Independent reference integration used original literal PL data, slope-based cells, and exponentials scaled at the window floor. It did not call the implementation's J0–J3 moment functions. This preserved a meaningful reference for cold He when the unscaled rate underflows.

| Comparison | Executed coverage | Largest recorded difference |
|---|---|---|
| Finite moments and analytic derivative versus independent quadrature | H1, He4, Li7 at 255, 25370.66308424773, and 50000 K; 9 pairs | Mean energy relative difference `2.8850826193261347e-16`; dlogK/dT relative difference `5.351065578384165e-16`; logK absolute difference `0.0` at these samples |
| J3 independent quadrature | 11 arguments, including zero, both sides of 0.5, and 1e6 | Absolute difference `5.551115123125783e-17` |
| Analytic log-rate derivative versus five-point differences | All three species at the new parent maximum temperature | Relative difference `2.6501278129246434e-12` |
| New H wrapper versus retained provider | Exactly one retained-provider evaluation at 25370.66308424773 K | Rate relative difference `7.075773050928895e-15` |
| Original seven-state RHS versus independent hazard pushforward | Initial, tiny positive hazard, and interior states | Relative difference `1.8345039892323955e-16` |
| Original seven-state RHS outside the invariant manifold | One deliberately nonconserving, valid-temperature state | Relative difference `3.772128761772459e-15`; no invariant projection |
| Analytic parcel Jacobian versus five-point RHS differences | One interior state, all three columns, balanced synthetic abundances and admitted rates | Maximum row-scaled difference `6.134794361557517e-11` |
| Analytic temperature gradient versus five-point differences | Same interior state | Maximum relative difference `3.733202102296468e-11` |

The nine zero recorded logK differences indicate agreement at the stored precision for those samples. They do not prove zero numerical error. The quadrature reference itself is numerical and its estimates remain in the full run receipt.

The constructor/evaluation checks rejected 31 invalid finite-kernel cases and 26 invalid parcel cases. Contents of the immutable array fields resisted ordinary write-enabling and caller input changes did not mutate the models. A synthetic zero prefix, negative temperature derivative, and rate-underflow case were exercised. The latter produced K = 0 while dK/dT = 1e-323 remained representable, confirming the intended separate logarithmic derivative path for that artificial example.

Tiny positive hazard increments remained stored with `expm1`. A separate synthetic saturation example reported all neutral-underflow flags and reached zero represented neutral abundance without a hidden floor. The analytical neutral positivity claim remains distinct from that floating-point outcome.

The initially suspected endpoint roundtrip risk did not fail for the selected conditioning case. Both hazard and original-state lifts returned exactly 255 K for the lower endpoint and 49999.99999999999 K for the 50000 K initial value, inside the accepted domain. No endpoint fix or rerun was needed. This is not an exhaustive guarantee for every possible abundance configuration.

## Remaining physical and evidentiary limits

The finite operator is explicitly zero outside its selected support. This defines the operator; it does not establish that omitted physical cross sections vanish. The executed Li7 chemical-to-source-floor gap is 0.6082793996541902 eV, and its low-temperature full-rate contribution is not bounded here. Upper omitted support is also not bounded.

The He author curve is described as unpublished as of 13-Apr-2026. Its method citation does not provide an experimental accuracy certificate or a complete uncertainty budget. The chemical isotope correction does not certify isotope-resolved CCC cross sections.

The selected stationary-target collision approximation, shared thermalization assumption, fixed density, positive seed, and omitted reaction channels remain model choices. Numerical accuracy within that model does not establish their physical accuracy.

This review proves the hazard reduction and rank-at-most-two Jacobian algebraically for the declared equations and checks selected binary64 evaluations. Its SVD result is pointwise consistency, not a separate rank theorem. Reconstructing thermal energy from a first integral is not independent trajectory evidence. Root's separate trajectory/refinement work, Bell positivity work, and nuclear review have their own scopes and receipts.

