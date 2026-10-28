# C9 independent review: source registry and integer event projections

**Decision: ACCEPT_SCOPED_SOURCE_ROWS_AND_INTEGER_PROJECTIONS.** There are no remaining blocking implementation findings within this scope. This decision does not approve any new physical rate, nuclear Q, heat partition, or consumer activation.

The independent reviewer was `/root/authority_survey`, separate from the builder/adapter author. The reviewed source base is WU088_HH commit `34dd7d1d018abff8a0a4ebd1d3f3579ac46d2fad`. Current local AGENTS and HEAD were read, and the parent's captured live central/parallel/backup receipts were inspected. Publication still needs a fresh remote expected-SHA check at the time of the non-force update.

## What was checked

The single bounded independent run passed **448/448 checks**, with **0 failures**. It directly parsed source rows and recomputed the exported event columns with ordinary integer arithmetic, without importing the assembler or frozen compiler for those comparisons. The adapter was imported only afterwards for specific rejection and identity controls. Source-row selectors, raw byte identities, and hashes were checked separately from finite conservation.

| Inventory | Verified count | Meaning |
|---|---:|---|
| Provider variants |102|Recovered source entries and explicit alternatives|
| Candidate event projections |125|Inactive columns with exact B, q and electron-lepton ledgers|
| Material/electron/state identities |92|Identity catalogue, not a population vector|
| Historical configured populations |21|Inherited configured view remains separate|
| Historical direction cells |39|Every cell has a source candidate; old admission state retained|
| NUBASE source nuclear states |5843|3558 ground and2285 non-ground source records|

Every candidate column has zero baryon, charge and electron-lepton residual. Chemical columns also preserve every isotope/isomer count. For weak rows the independent electron-lepton count includes the bound-electron contribution `sum(Z*count)-charge` and explicit neutrino/antineutrino sidecars. Missing antineutrino and wrong neutrino sign were rejected. Unknown species, attempted activation and attempted physical-Q promotion were also rejected. These are structural controls and do not qualify the beta energy partition.

The Voronov intake retains six literal elemental CI coefficient rows and their original eV/keV temperature units, producing thirteen explicitly isotope-blind candidate projections. No coefficient was evaluated. Fit `dE` is not approved chemical Q; the original Fortran `u>80` return rule remains a numerical rule, not an observed physical zero. The historical29 source-admission cells and ten missing CI admissions remain visible beside the39 newly sourced candidate cells.

The original frozen compiler bytes have SHA256 `60a502895266b6feb96964abc4b24db61c2faed2344db0f7d12f16bb47ed62af`. The old249 synthetic checks were not replayed or broadened. Every new event retains `UNQUALIFIED:ENERGY`, unbound rate normalization, inactive status and no reverse-rate inference.

## Resolution of the R6 findings

| Finding | Resolution and direct evidence |
|---|---|
| F1: He I fit a was overwritten by b |Both literal rows now have separate provider IDs. Open domains3K<T<1e6K and3K<T<1e10K and rms2.5%/4.7% are preserved. The historical alias selects b. Both alternatives share a conservative ownership group. The original extraction and correction packet remain separate.|
| F2: Total RR photon count was over-specified |The thirteen historical RR directions retain `total_photon_count=null`; compiled total-RR events assert no escaped photon count. Primary capture is separated from unresolved cascades.|
| F3: External-particle identity was representation-dependent |One `gamma:escaping` term of multiplicity2 and two terms of multiplicity1 give the same keys. Different branch IDs remain different. Two active HeI a/b or neutron-evaluation alternatives are rejected.|
| F4: Provider-ID JSON pointers did not resolve list rows |All101 row selectors resolve exactly one source row, and all102 native provider records match their payloads and identity hashes. LiH's whole-document source is bound separately. Original build01 is archived.|

## Source semantics preserved

The37 UMIST reaction rows and38 fit segments retain exact source strings. Reaction74 keeps its100–101K gap. Elemental H/He labels are not silently converted into source-qualified isotopes; the H1/He4 event instances remain explicit model projections. Native cosmic-ray and photon drivers are not protons or a newly bound cosmological radiation field. UMIST gamma fit parameters are not Q.

HD retains nine source levels, eight radiative lines, eighteen collider transitions and the three source temperature nodes. Para-H2 and ortho-H2 remain different catalyst identities on both sides of every corresponding transition. LiH retains1562 exact tabulated samples, native unspecified Li/H isotopes and unresolved source state. The91.2–351.1nm samples and579nm summary threshold remain separate, without support extrapolation.

All5843 NUBASE rows were matched against their exact fixed-width source lines, including mass-excess/uncertainty strings, state index/symbol and branch-or-abundance text. That catalogue is not a recovered complete nuclear reaction list, and nonzero provider state index is not automatically interpreted as a physical isomer. NUBASE and LiveChart neutron lifetimes remain different inactive source alternatives. Duplicate LiveChart uncertainty columns remain positional. Native atomic-mass/Q conventions do not become a bare nuclear Q.

## Preserved primary-check false negative

The primary run remains recorded as `FAIL` for the single group `native_molecular_isotopes_not_fabricated`. Inspection of `verification/check_registry.py` line426 shows a literal predicate that searches for `ISOTOPE`; the two actual LiH event qualifiers are `ISOTOPOLOGUE_CANDIDATE_ONLY; FRAGMENT_BRANCH_UNRESOLVED`. The preceding primary assertions already preserved native Li/H isotope and state nulls. Independent C9 verified the native source, all source wrappers, LiH samples, and all event ledgers.

This is a checker predicate defect, not a registry defect. The failed primary result is preserved and must not be rewritten as a successful run. No registry modification or scientific replay is needed for this finding. Any later targeted checker correction must have its own receipt.

## Remaining obligations and admission boundary

This review accepts source-row transcription and finite integer projections. It does not establish whole-network physical completeness. The original nuclear network locator, isotope/state rate validity, mass covariance, atomic-to-bare conversion, PHYS91 B1 source covenant, physical energy partitions and named consumer binding remain open. Additional molecular formation/destruction and requested isotope transfers remain explicit source gaps.

All new rate, Q and activation flags remain false; `HH_R10=OFF`, `production=NOT_ISSUED`, `L4_ready=false`, and global physical completion is null. There is no residual-to-heat conversion and no additional source-rate or Q computation.

## Execution and resource receipt

Bounded child limits were30 CPU seconds,120 wall seconds,512MiB, one worker and one thread. The actual child receipt records CPU **0.186854s**, wall **0.215610475s**, peak RSS **46,908KiB**, exit0 and no timeout. This is one new lightweight validation child, not a debit to exhausted PHYS91 execution allowances or a transfer of old compiler budget. Historical extraction/network costs remain unmeasured, not zero; no exact global budget balance is asserted.

- Checker: `verification/independent_check.py`, SHA256 `4d7f6095d92c8ffc4babb183d33ff6ec30a52909a1f883f4d41dc5806a7ccfcf`.
- Results: `raw/INDEPENDENT_RESULTS.json`, SHA256 `d03ed4769cd580fb573c100f9f6392f81193f500d9dd0feb860354d504ec8034`.
- Execution: `raw/independent01/RECEIPT.json`, SHA256 `b282e9ac01a495001fb7572d324df985ccc47edd19d63b10d7a548093297255a`.
- Primary failure remains: `raw/PRIMARY_RESULTS.json`, SHA256 `54a2e21c0cebf2104ced88c064669a968b63fa12e59575aa94722d9512fed8af`.
- New rate evaluations0; physical Q evaluations0; IVPs0; old249 replay0.

## Frozen reviewed inputs

The independent run compared its input hashes before and after and found no changes.

| Relative path under research/ | SHA256 |
|---|---|
| `provider_registry_20261025/registry/species.json` | `a18052f6db432192e1e0d4c75f8f2d49c71f3a5eb7cac206e7bc445fec2e8f80` |
| `provider_registry_20261025/registry/providers.json` | `23d5bee7323a083d23a8a811eb7312a35c0eb613381ce28a22a5f989b1077664` |
| `provider_registry_20261025/registry/events.json` | `abeea067660b0898315935ffd07bb6a443bbb1bd6111c700215b72be220baa90` |
| `provider_registry_20261025/registry/compiled.json` | `d4836befd465ebd8130e5fd1f910b1fea30348c5e5785bfc66f8275735123f8c` |
| `provider_registry_20261025/registry/coverage.json` | `67e6757038de2783d7b08f4bc840314a7bb2d04a8839c3a821a6be18be4f27f5` |
| `provider_registry_20261025/registry_adapter.py` | `9a093eed42f9ff5858d7bae11c726988ddbde4feeed38888b1c90fe329be816c` |
| `provider_registry_20261025/build_registry.py` | `b0f9387fecf18a9e66be9328bee0fb71b3055a1fb6f083cccd891e81269a792f` |
| `provider_registry_20261025/CONTRACT.json` | `aa58fd2683b54760bdf2e51165207dac3a96477b261c86923e6fcaca8e880f46` |
| `rei_chem_ledger_20261025/chem_ledger.py` | `60a502895266b6feb96964abc4b24db61c2faed2344db0f7d12f16bb47ed62af` |

The companion `C9_FINAL.json` contains machine-readable findings, exact authority/result hashes and the bounded execution statement. Git publication and dual-provider backup are separate operational receipts owned by the root task.
