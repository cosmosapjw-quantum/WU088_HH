# PHYS81 nuclear component: independent review

## Status and scope

**Decision: CONFIRMED_SCOPED** for the pinned two-body COM event kinematics, explicit ζ energy partition and stated source/domain contract. Static review found no blocking inconsistency with the supplied equations. The parent subsequently executed the verifier once under the shared lease; the reviewer inspected that existing receipt without new numerical evaluation. All 663 assertions passed. One bounded observation concerns malformed-input Decimal flags; it does not change valid event energies.

The numerical coverage consists of 15 unique `(reaction,K)` inputs, 45 ζ partitions, 38 domain-rejection checks, three source-tamper rejection paths and three changed caller-context profiles. The 663 assertions are not 663 independent physical inputs. The review does not issue nuclear-rate, thermal-ODE or production admission.

The reviewed implementation is `/tmp/phys81_work_20261023/WU088_HH/research/hh_phys81_atomic_nuclear_source_contract_20261023/source/nuclear_recoil.py`. The review owns only `/tmp/phys81_review/nuclear`. No reviewed file was edited. No other process was stopped. No remote write or main merge was performed.

This is an independent code and algebra review in a separate agent context, not an independent experimental validation or an independently retrieved CODATA measurement. Saved source evidence was reused. Its representation identity is distinguished from origin HTML/PDF byte identity.

## Reviewed identities

| Input | SHA256 |
|---|---|
| `source/nuclear_recoil.py` | `e8b7ad216113932d0844e424ca6e5e17dd644e07ca883e463c0c6c325c4fcf0e` |
| `source_data/NUCLEAR_MASSES_CODATA2022.json` | `ee87900f698e59029a1aafce3d4184870ccc6fa16a8ba50326bd13a10de60aaf` |
| Intake `SOURCE_PINNED_MASSES.json` | `ee87900f698e59029a1aafce3d4184870ccc6fa16a8ba50326bd13a10de60aaf` |
| Intake `NUCLEAR_RECOIL_THEORY_KO.md` | `566b5cb4f2b704e9553d5aa558372599d65ffe9dcf9dda90ab28ae1cb09eba18` |
| Intake `NIST_CODATA2022_RELEVANT_ROWS.txt` | `b2c5b86f1d2e8068418d200d5e12d3b28e2bb8dc930f3ddecbcb905ed304abce` |
| Intake `EVIDENCE_MANIFEST.json` | `e664978fcbbeb7f505ed3eda4aa74878d93c34aa591849146e46163b940d0571` |
| Unit `CONTRACT.json` | `e815c3850f2916269986d3a43a58d73f889c7040adf4992f006950d91145d22c` |
| Unit `POLICY_OVERRIDE.json` | `a435743ad5dd9762da3a8e2a1f788df1d17a2df9a87e09eca05419ce95f3aae1` |

The source table exactly matches the intake transcription hash. The kg and MeV values and their separate standard uncertainties agree with the supplied selected primary rows. This review did not refetch already pinned evidence or propagate an unavailable mass covariance matrix.

## Findings against the equations

### 1. Relativistic two-body kinematics

The theory's Sections 2–3 and 6.2 distinguish rest mass from rest energy. The implementation makes that conversion convention explicit: its `initial`, `final`, `Q`, `W`, and all result energies are MeV. Thus, writing `Mi` and `Mf` for rest energies in this paragraph,

\[
Q=M_i-M_f,\quad W=M_i+K,\quad \Delta=Q+K=W-M_f.
\]

The COM conservation equation is

\[
W=E_\gamma+\sqrt{M_f^2+E_\gamma^2},\qquad p_fc=-E_\gamma
\]

where the final equality specifies an opposing momentum component along the photon direction. It implies

\[
E_\gamma=\Delta\left(1-\frac{\Delta}{2W}\right),\qquad
K_R=\frac{\Delta^2}{2W}.
\]

The code implements exactly these expressions at lines 263–273, using a bounded ratio before multiplication. It does not replace the final relativistic energy by `p^2/(2Mf)`, substitute `Mf` for the denominator `W`, mix kg with MeV, or omit incoming COM energy. For `K=0`, the implementation reduces to the supplied exact cold-COM result. The finite-K option remains a caller-supplied event input and does not infer a Maxwellian moment from a temperature.

### 2. Energy ownership with supplied ζ

Theory Sections 5 and 6.2 require explicit recoil deposition and an incoming-kinetic debit when that initial kinetic energy is owned by the same designated thermal reservoir. The code at lines 309–336 uses

\[
\Delta E_{\rm rest}=-Q,\quad
\Delta U_{\rm th}=\zeta K_R-K,\quad
\Delta E_{\rm nt}=(1-\zeta)K_R,\quad
\Delta E_\gamma=E_\gamma.
\]

Their analytic sum vanishes because `E_gamma + K_R = Q + K`. In particular, the rest-energy debit is `-Q`, while the initial kinetic debit is accounted for separately. ζ is required as a keyword argument and restricted to the closed interval [0,1]. Both boundary assignments are represented. The residual is reported rather than forced to zero by reallocating energy.

The assignment of incoming K to the thermal reservoir is an explicit caller precondition in the class docstring and metadata. It is a conditional ledger convention, not a derived stopping model. The escaping-photon counter is not a radiation stress tensor or a normal-frame transport result.

### 3. Counts and thermal-number ownership

Theory Section 4 supplies the three stoichiometric columns in order `(n,p,d,t,h)`. All three columns in `REACTIONS` agree. With `A=(1,1,2,3,3)` and `Z=(0,1,1,1,2)`, each column conserves baryon number and nuclear charge, reduces total nuclear particle count by one, and leaves the neutrality-derived electron count unchanged. `_validate_stoichiometry` checks these declarations against the admitted source rows.

Crucially, the code labels this as total nuclear particle count; it does not assign a thermal bath particle-count change from ζ. Metadata explicitly says `thermal_particle_number_ownership="unassigned"`; the public event result supplies no thermal-number or temperature equation. This respects the theory's warning that an energy deposition fraction does not determine daughter membership of a thermal bath.

### 4. Source identities, rounding and guards

`load_nuclear_masses` reads and verifies the source bytes on every call. The fixed SHA256, bare-nucleus convention, source symbols, A/Z values, positive decimal strings, and species set are checked before evaluation. Immutable rows and mappings prevent ordinary caller mutation. The API retains the distinction between saved transcription bytes and source-origin bytes.

The mass-energy column is used consistently for every channel. Eighty-digit arithmetic controls numerical rounding of the supplied decimals; it does not increase their experimental precision. The code explicitly declines to propagate the missing joint covariance. No neutral-atom mass or atomic binding energy is silently substituted into a bare-nucleus channel.

The private arithmetic context fixes precision 80, ROUND_HALF_EVEN and exponent bounds, with range failures trapped. Positive finite output energies and `0 < available < W` are required. Negative K, invalid channel names, nonfinite values, booleans and unsupported containers are rejected. If very large K makes the final rest energy unresolved at fixed precision, the domain guard rejects the calculation. This is a finite-precision admissibility boundary, not a claim that arbitrarily large physical COM K is forbidden.

### 5. Bounded nonblocking observation: malformed-input context state

`_decimal_scalar`, lines 120–135, calls `Decimal(str(value))` before entering the private arithmetic context. The executed receipt confirms that malformed decimal text sets the caller's `InvalidOperation` flag. The rejection message depends on whether the caller traps `InvalidOperation`: the observed messages are `INCIDENT_COM_KINETIC_MEV_INVALID_DECIMAL` with the trap, and `INCIDENT_COM_KINETIC_MEV_MUST_BE_FINITE` without it.

Both paths reject the input with `ValueError`. Valid finite event outputs are still computed in the fixed local context. The API's arithmetic isolation claim is therefore supportable for valid calculations, while a stronger promise that every rejected call preserves caller flags and returns the same validation message would need a parsing-context adjustment. This is recorded as an observation, not a kinematic or energy-ownership failure. The verifier records the two malformed-text behaviors separately and requires valid-call output/context independence.

## Independent verifier

`verify_nuclear_independent.py` is pinned to the reviewed source, table, theory and selected-row hashes. If any reviewed identity changes, it writes a failure receipt without admitting numerical checks for the changed source. It never writes the reviewed source or mass file. A temporary in-memory `Path.read_bytes` substitution tests hash rejection after earlier successful calls, including absence of a stale admitted source cache.

Coverage executed by the parent once and read back by this reviewer:

- All three actual CODATA channels at K = 0, 10^-12, 0.001, 1 and 1000 MeV: 15 independent event references.
- A separate 180-digit Decimal square-root/bisection solve of the unsquared conservation equation, with at most 640 bisections per event. The production split formula is not the numerical oracle.
- The independent energy equation and the momentum/mass-shell identity `(Mf+K_R)^2 - E_gamma^2 - Mf^2 = 0` evaluated using returned production energies.
- ζ = 0, 0.5 and 1 for each event: 45 conditional reservoir partitions, including explicit incoming-K debits.
- Baryon, charge, total nuclear particle count, unchanged derived electrons, immutable source rows and explicit thermal-number non-ownership.
- Domain rejection, missing ζ, malformed/nonfinite scalars, arithmetic range and deposition-underflow cases.
- Three caller Decimal contexts with changed precision, rounding, exponent range, traps and preexisting flags. Valid outputs must match baseline and leave caller context unchanged.
- First-receipt preservation: `--out` refuses an existing file.

The numerical tolerance is fixed at 128 nominal last-place units at 80 significant digits, with the actual energy or squared-energy scale recorded for every comparison. The oracle uses 180-digit arithmetic. This provides an independent numerical check of the bounded cases; it is not an outward-rounded interval certificate or a physical uncertainty bound.

### Exact command for the parent lease

```bash
python -B /tmp/phys81_review/nuclear/verify_nuclear_independent.py --unit /tmp/phys81_work_20261023/WU088_HH/research/hh_phys81_atomic_nuclear_source_contract_20261023 --out /tmp/phys81_review/nuclear/NUMERIC_RECEIPT_001.json
```

The parent executed this exact command once. The wrapper receipt records exit code 0, one thread and a 0.5 GiB reservation. The reviewer did not execute it. Do not rerun the completed identity. A source change requires a fresh reviewed identity and explicit adaptation of the verifier pin; the old receipt is not overwritten.

## Observed numerical receipt and decision criteria

The parent run began at `2026-10-22T23:03:11.660853+00:00` and completed at `2026-10-22T23:03:11.954476+00:00`, according to the numeric receipt. `NUMERIC_RECEIPT_001.json` has SHA256 `c8c46e9e5c925aea288bf48420c7d81169e9482096cd58c09e901bbcfc00778e`. The parent wrapper `verification/LEASE_NUCLEAR_INDEPENDENT_001.json` has SHA256 `90f7bf835fafd476205cf51e5727a1b733a6b55955e544be47b2251dfede97e0`.

The confirmation criteria were met: the source/table/theory/selected-row hashes match the reviewed identities; the verifier hash matches its syntax receipt; the parent wrapper has exit code 0; every stored assertion passes; independent square-root reference and momentum-invariant checks are present for every event case; explicit ownership boundaries are retained. A hash mismatch, invariant or partition failure would have rejected the pinned result. Missing execution evidence or incomplete oracle coverage would have made the numerical conclusion inconclusive.

The malformed-input observation limits the context claim to valid numerical calculations. It does not warrant rejecting the documented physical event and energy ledger. Three changed caller contexts produce unchanged valid outputs and preserve their preexisting context state, including traps and flags.

### Three cold-COM rows read from the existing receipt

| Channel | Q (MeV) | Photon (MeV, rounded display) | Recoil (MeV, rounded display) |
|---|---:|---:|---:|
| n+p → d+γ | 2.22456637 | 2.22324871192134 | 0.00131765807866001 |
| n+d → t+γ | 6.25723026 | 6.25027636127258 | 0.00695389872742194 |
| p+d → h+γ | 5.49342331 | 5.48806102630795 | 0.00536228369204934 |

The full stored strings are preserved in `COLD_ROWS_FROM_RECEIPT.json`. These are conditional arithmetic outputs of rounded recommended masses; the displayed precision is not a propagated physical uncertainty. This extraction did not recompute the event energies.

## Observed execution and limits

`SYNTAX_RECEIPT.json` records successful AST parsing and in-memory compilation of verifier SHA256 `6213f2f165c124471579574737feafe970038a877174086e57e044421162b28f`, with zero numerical checks executed. `COMMAND_LOG.json` preserves read/hash/syntax command exit codes, including an initial `rg` exit code 2 because the review output directory did not yet exist. That read-only inventory failure did not execute scientific code.

No nuclear rate, cross section, finite-temperature weighting, thermal population ownership, stopping process, normal-frame source, radiation transport, cosmological coupling or production admission is established here. `HH_R10=OFF` and `production_admission=NOT_ISSUED` remain in force. No completed historical scientific identity was rerun.
