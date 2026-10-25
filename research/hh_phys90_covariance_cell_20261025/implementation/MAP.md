# PHYS90 implementation map — ready for frozen S1 review, not executed

## Owned implementation

* `source/kernel.py`: exact rational input/shape/symmetry/radius checks; symmetric shared-entry support; Fraction fixture algebra; common integer-scaled all-pair predicate scans; doubling and 40 exact dyadic bisections.
* `source/primary.py`: one prescribed finite primary application, exact scientific JSONs, one PNG and one PDF from new saved-in-memory checkpoint counts. Probe centers are pinned reused PHYS89 values; only their box support is newly evaluated.
* `source/reference.py`: independently written per-pair integer scaling, every saved checkpoint (including all t=1 pairs/singletons), final bracket/witness, 0,10 threshold identity, all eight 2×2 vertices and all nine support entries. It imports neither kernel nor primary.
* `source/evidence.py`: metadata-only frozen identity and read-only resume before scientific imports. Create-only outputs and manifest, including both figure hashes.
* `source/leased_call.py`: parent wrapper adaptation, same vendor lease APIs and source SHA, same `/tmp/rei-bianchi-cooperative-leases`, CPU0 child / CPU8 coordinator, 20 CPU-second / 45 wall-second caps, one thread and worker, 1.5 GiB reserve plus 0.5 GiB job, no retries or peer termination.

## Exact data flow

The contract's two cached parent inputs are read after SHA/size validation, without ENDF decoding. `SOURCE_TABLE.matrix` is checked against its packed upper triangle; `TOKEN_ROUNDING.halfULP` fills the symmetric H in i-major upper-triangle order. Every scalar uses Fraction first. The primary table rescales F and H to one exact common integer unit. At t=p/q it checks diagonal numerators and `(max(abs(fij)*q-hij*p,0))² ≤ (fii*q+hii*p)(fjj*q+hjj*p)` for all 11628 pairs, plus 153 singleton checks. No float enters a scientific predicate.

At t=0 and t=1 all failed pairs are retained, including indices and complete singleton lists. Subsequent exact checkpoint counts and one failed pair are recorded. A successful final bracket has failed lo, all-pair-pass hi and exactly the initial width divided by 2^40; hi does not assert full PSD compatibility. If all pair conditions already pass at zero, [0,0] is returned. If 4096 fails, the result is lower-bound-only with a witness.

The independent reference uses a different scale for each six-entry pair and an independently written integer determinant path. It crosschecks scientific rational quantities, not presentation float values or packaging hashes. Primary payload hashes bind which result was examined; reference resume verifies that dependency as metadata.

## Freeze identity recipe (root-owned next step)

Create `implementation/FROZEN_FILES.json` with shape `{"files":{"relative/path":"sha256",...}}`, hashing at least:

* `CONTRACT.json`
* `theory/COVARIANCE_CELL_AND_CONSUMER_KO.md`
* `source/kernel.py`
* `source/primary.py`
* `source/reference.py`
* `source/evidence.py`
* `source/leased_call.py`

The manifest must not hash itself. `identity()` verifies those bytes and both contract-pinned cached input size/SHA pairs. It constructs a canonical JSON binding of the unit id, parent HEAD, contract SHA, frozen files and pinned input list. Its SHA is the PHYS90 scientific identity and necessarily differs from the PHYS89 identity. The source wrapper is also pinned by this manifest; its vendor lease source is independently checked against the original contract SHA.

## Expected commands (only after root S1 and explicit authorization)

From repository root, with `U=research/hh_phys90_covariance_cell_20261025`:

```bash
python "$U/source/leased_call.py" --kind primary --label phys90-primary1 --receipt "$U/execution/PRIMARY_ATTEMPT1.json" --admission-receipt "$U/execution/PRIMARY_ADMISSION1.json" -- python "$U/source/primary.py" --output "$U/verification/primary"
python "$U/source/leased_call.py" --kind reference --label phys90-reference1 --receipt "$U/execution/REFERENCE_ATTEMPT1.json" --admission-receipt "$U/execution/REFERENCE_ADMISSION1.json" -- python "$U/source/reference.py" --primary-output "$U/verification/primary" --output "$U/verification/reference"
python "$U/source/primary.py" --output "$U/verification/primary" --resume
python "$U/source/reference.py" --primary-output "$U/verification/primary" --output "$U/verification/reference" --resume
```

The two scientific commands are sequential and create-only. A failed output or receipt must be preserved, never overwritten or automatically retried. Resume checks frozen code/input bytes and all output hashes before SKIP, imports no scientific module, calls no scientific callback and writes no file. The reference skip additionally checks the primary manifest against its saved dependency digest.

## Verification performed in implementation stage

Only `python -m py_compile` on all five source files. This checks syntax without importing/executing the scientific modules. No primary/reference/fixture/guard/plot callback, scientific child, old witness callback, ENDF decoder, eigensolver, integral, ODE or benchmark was run. Generated py_compile cache files are removed as disposable structural-check output.

## Scope and unresolved inputs

No implementation physics/tolerance choice remains open under the frozen contract and root clarification. The actual consumer ACK, nuclear nominal/mass/state/kernel/tail obligations, full 153×153 PSD compatibility, physical confidence intervals, source formatter guarantee, rates and histories remain outside this finite child's admission. Metadata is PARTIAL_INPUT_DEPENDENCIES at parent scope; HH_R10 OFF and production NOT_ISSUED.

## Authorized pre-execution correction: radius-specific PSD conclusion

Before S1 freeze, primary/reference/kernel bytes were preserved create-only under `implementation/history_preexec/t1_classification/`. No scientific application had run. The correction emits `at_t1_full_PSD_compatibility=INCOMPATIBLE_BY_PAIR_OR_SINGLETON` precisely when the exact t=1 singleton/pair scan fails, together with `t1_witness` from the exact table. When all t=1 conditions pass, that radius-specific global PSD compatibility remains `UNRESOLVED` and the witness is null. The independent reference recomputes and checks the classification, selected index and every rational witness quantity. `full_PSD_threshold` remains `UNRESOLVED`; no upper-bound claim for full PSD is emitted from the pair bracket. This implements the contract's existing `UNRESOLVED_UNLESS_ACTUAL_CERTIFICATE` boundary without changing the contract, math or tolerance.

Verification after this correction remains py_compile only; no scientific callback, child, fixture, guard or figure generation has run.
