# Nuclear ownership detached coding adoption

Implementation: `research/hh_phys83_ce_completion_20261023/source/nuclear_ownership.py`.
This additive file has no external package dependency or parent scientific-kernel import.
It consumes supplied energy records/weights. It does not compute Lorentz boosts,
four-vector mass shells, isotope stoichiometry, nuclear rates, stopping power or a history.

| Theory result | Implemented API | Contract |
|---|---|---|
| Eq. (4), normal event energy closure | immutable `EventEnergy(Kin_MeV, Kc_MeV, Egamma_MeV, Q_MeV, frame)` | Kin/Kc nonnegative; Egamma/Q positive; all finite real nonbool scalars; supplied normal frame required; relative signed closure tolerance `2e-12` |
| Eq. (6), same positive event measure | `weighted_event_mean(events, weights)` | Matching lengths; nonnegative finite weights; identical frame strings including optional frame suffix; zero total returns `None`; same normalized weights for every energy |
| Section 3, exclusive fast-first | `capture_ledger(mean, mode='FAST_FIRST')` | ΔNthermal=-2, ΔNfast=+1; rest=-Q, thermal=-Kin, fast=Kc, photon=Egamma |
| Section 3, explicit alternative | `capture_ledger(mean, mode='PROMPT_THERMAL')` | ΔNthermal=-1, ΔNfast=0; thermal=Kc-Kin, fast=0, remaining signed fields unchanged |
| Eq. (5), stopping without assimilation | `stopping_transfer(energy_MeV, frame=...)` | thermal=+energy, fast=-energy; no particle transfer; supplied transfer only |
| Eq. (5), actual residual energy at assimilation | `assimilation_transfer(mean_kinetic_MeV, frame=...)` | thermal/fast particle changes +1/-1; actual remaining kinetic energy transferred once |
| Eq. (13), thermal EOS | `thermal_temperature_source(T_K, nthermal_cm3, thermal_power_MeV_cm3_s, number_source_cm3_s, theta_s_inv=0)` | Returns K/s; T/n positive; power/number/expansion signed finite; MeV→erg exact-unit constants represented binary64 |
| Eq. (12), conditional NR incoming mean | `nr_selected_kinetic_mean(T_K, dlnK_dlnT, temperature_independent_sigma=True)` | Explicit literal True required; T positive; derivative finite and >-1.5; returns MeV; equal-T, zero drift, valid NR support and differentiation conditions remain caller preconditions |

The valid frame tag is `normal_orthonormal` or `normal_orthonormal:<shared-id>`.
The suffix can identify a common cell/frame/epoch; averages require exact string
equality, including for zero-weight records. The energy-only record cannot verify
that a producer physically transformed to this frame; its provider identity is a
separate prerequisite.

Returned `Ledger` is immutable and carries literal aggregate particle counts,
signed rest/thermal/fast/photon MeV increments, frame, actual signed energy residual
and normalized residual. Residuals are evaluated from all supplied signed terms
with scale-normalized `math.fsum`; none is overwritten with zero. A zero-rate mean
cannot be passed to `capture_ledger`; the caller assembles zero sources directly.

Positive averages scale weights by their maximum, then scale each nonnegative energy
field by its maximum. This avoids overflow in unnormalized weight sums and loss of
a constant subnormal mean merely because each term was multiplied by a fractional
weight first. This is a design choice; runtime edge-case verification is assigned
to the independent verifier.

Actual execution here: **static compile only**; no module import or sample/event/rate
execution. `CODING_STATIC_COMPILE.json` contains the exact code hash. Independent
runtime verification is owned by `current_delta`. The earlier theory file's
`NO_NEW_PRODUCTION_ADAPTER_IN_THIS_CHILD` entry describes its previous delivery;
this follow-up implements the explicitly bounded detached ledger, not the future
full phase-space/frame/source adapter.

Remaining physical providers: normal-frame on-shell event construction, isotope/state
source and stoichiometry, finite-T physical weights/angle distribution, nuclear rates,
fast tensor/transport, stopping law and thermal matching, radiation geometry/spectrum.
HH_R10=OFF; production admission NOT_ISSUED.
