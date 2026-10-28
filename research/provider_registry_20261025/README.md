# WU actual provider registry R1 — 2026-10-25

**Decision: source rows and exact finite number projections accepted within scope.**
This unit recovers actual provider payloads and reuses the frozen finite compiler.
It does not admit new empirical rates, physical nuclear Q, or a coupled consumer.

Read [REPORT_KO.md](REPORT_KO.md), [HANDOFF_KO.md](HANDOFF_KO.md),
[SCIENTIFIC_ADMISSION.json](SCIENTIFIC_ADMISSION.json), and [DAG.json](DAG.json).

## Saved result

| Object | Saved extent |
|---|---:|
| Historical configured populations | 21 |
| Historical CI/PI/RR directions with at least one source candidate | 39 / 39 |
| Distinct provider variants / source records | 102 |
| Candidate finite event projections | 125 |
| Compiler species/state identities | 92 |
| NUBASE source-state catalogue rows | 5,843 |
| Final primary implementation check groups | 20 / 20 |
| Independent raw-source / integer-projection checks | 448 / 448 |
| New physical rate / nuclear-Q / IVP admissions | 0 / 0 / 0 |

The 92 identities include state-resolved and aggregate views; they are not a
simultaneously evolved 92-species model. The 5,843 catalogue rows include
ground states, non-ground states, estimates and source qualifications; they do
not define an activated reaction network. The original configured nuclear
network image still has no recovered stable locator.

## Navigation

- `registry/species.json`: isotope composition, isomer, charge, electronic/
  internal state and view qualification.
- `registry/providers.json`: actual provider variants, payload selectors and
  record hashes; both He I RR fit a and fit b remain available.
- `registry/events.json`: branch, material stoichiometry, external particles,
  radiation qualification, rate-binding and activation boundaries.
- `registry/compiled.json`: 125 exact number columns using the unchanged core.
- `registry/coverage.json`: original 21 / 39 view, source candidates and
  unresolved source / consumer cells.
- `sources/`: original recovered bytes, native units/support, source locators,
  uncertainty qualifications and separate corrections. Large records use
  deterministic gzip with decoded hashes in `STORAGE_INDEX.json`.
- `theory/REGISTRY_ENERGY_AND_LEPTONS_KO.md`: derived conservation,
  density normalization, atomic/bare mass and energy-owner contracts.
- `raw/`: immutable execution attempts, including the first failed primary
  checker and both pre-correction registry snapshots.
- `reviews/`: independent C9 decision and addendum.
- `EXECUTION_LEDGER.json`: measured bounded children and unknown global costs.
- `delivery/`: actual publication and two-cloud backup receipts added after
  the source commit is published.

## Reproduction and reuse

Use the saved results for unchanged identities. The builder verifies immutable
output equality and refuses to overwrite a different existing result. The
bounded runner refuses an existing attempt directory. The old 249 synthetic
checks were reused from their saved admission, not replayed.

For a changed dependency, freeze a new contract and output location first.
A fresh checkout with a new authorized attempt may use:

```bash
python3 verification/run_bounded.py --attempt NEW_ATTEMPT -- python3 build_registry.py
python3 verification/run_bounded.py --attempt NEW_CHECK -- python3 verification/check_registry.py --output raw/NEW_PRIMARY_RESULTS.json
```

Run from this directory. A complete source ZIP also contains the unchanged
`research/rei_chem_ledger_20261025/` dependency. The normal repository already
contains it at the pinned base. The archival extraction scripts preserve the
original source-recovery procedure and staging paths; the authoritative offline
rebuild is `build_registry.py` using the saved payloads.

The per-child validation cap is 30 CPU seconds, 120 wall seconds, 512 MiB,
one worker and one thread. It is a current-request implementation validation
contract, not a reset or transfer of historical science budgets.

