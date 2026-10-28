# R2 target directions and number projections

Status: implementation prepared; this note does not report an executed build or a passed numerical check. The frozen R2 contract controls execution and budgets. R1 source commit `18a6804d7cbe4879701e83631f7e908bbb84cef1`, its 102 provider variants, 125 compiled projections and original checks remain unchanged.

## 1. Three separate kinds of input

The recovered image and its pinned transcription define nineteen user target identities. The second pinned contract defines eighteen conditional nuclear-model families: thirteen families cover the sixteen nuclear/weak target IDs, and five are separately declared closure additions. Primary supplier records are a third input layer. A source's quoted parameter, published rate table and the later model that uses or extrapolates it are separate records.

`build_network19.py` writes `target_declarations.json`, `conditional_models.json` and `primary_providers.json` separately. Primary packet classes `PRIMARY_SOURCE_ROW` and `REUSED_CONDITIONAL_MODEL_OUTPUT` remain distinct. The latter class does not enter the count of newly recovered primary rows. Record IDs, raw source hashes, original locators, native units and uncertainties survive unchanged inside their native records.

References:

- [Recovered nineteen-target transcription](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/c9deb933761a8d2593d1176aee028cd423bdbc05/research/atomic_nuclear_ssot_20261017/run19/metals/network/TARGET_NETWORK_19.json), SHA256 `96466ae646905c7f47509ea30898f677d12b922571e23d166426bf223fbf889a`.
- [Conditional eighteen-family contract](https://github.com/cosmosapjw-quantum/rei_bianchi/blob/9620e1fcc4bdda76e0311206f614234926600381/research/rei_tritium_production_audit_20261022/NUCLEAR_NETWORK_CONTRACT.json), SHA256 `68f69ea6288f3ba45abe4ef9416b3d0cbe507f61543a4ff045ad914061acbe3c`.
- `../../provider_registry_20261025/registry_adapter.py`: unchanged R1 adapter, SHA256 `9a093eed42f9ff5858d7bae11c726988ddbde4feeed38888b1c90fe329be816c`.
- `../../rei_chem_ledger_20261025/chem_ledger.py`: unchanged finite compiler, SHA256 `60a502895266b6feb96964abc4b24db61c2faed2344db0f7d12f16bb47ed62af`.

## 2. Direction map and aliases

IDs 1–8 and 11 carry reversible arrows. Together with the ten remaining forward-only IDs, they define 28 target-direction obligations. The builder retains all nineteen IDs. Overlaps (7,13), (8,12) and (11,19) refer to shared physical directions while remaining separate target obligations.

For IDs 4–8 and 11, the listed forward direction is photodisintegration. The corresponding conditional family's forward direction is radiative capture. A capture supplier therefore attaches to **target_reverse**, never directly to the listed photodisintegration direction. The builder rejects an explicit primary direction map that contradicts this relation. It neither derives inverse rates nor transfers the conditional soft-field photozero to a cross section.

An independently recovered photodisintegration packet can instead declare `family_reverse`. For example, D photodisintegration supplies target 8 forward and is physically the reverse of target 12 capture. Since ID 12 itself has no reversible arrow, the latter source reference is preserved under `additional_direction_evidence`; it does not create a twenty-ninth original target-direction obligation. An actual source row is required: the builder never creates it by reversing a capture coefficient.

Additional photo records must explicitly distinguish `EXCLUSIVE_NATIVE_CHANNEL`, `FACTORIZED_EXCLUSIVE_CANDIDATE` and `INCLUSIVE_ONLY`. Only the first class records an available exclusive native channel source. A total cross section and a separately supplied product yield remain a factorized candidate without multiplication; inclusive Li7 fragment yields do not close the exclusive alpha+T branch. These relations have separate direction-map fields and coverage counts. An available source relation does not imply physical state, rate or Q admission.

`EXCLUSIVE_SPECTRUM_AVERAGED_MEASUREMENT` is a fourth, separate source relation. A beam-spectrum average in an identified channel remains an actual measured record, with its native beam energy, spread and uncertainty. It is not relabelled as a pointwise cross section. Such rows use `beam_averaged_provider_refs`; beam folding, incident spectrum and energy-grid binding remain unresolved, with no new integration or inversion.

The six listed photodisintegration directions receive separately declared structural projections. The eighteen conditional family-forward directions receive model-qualified projections. Those are the only 24 new columns intended for compilation. Existing R1 electronic PI/RR, n/T beta alternatives and np/pd/nd source or cold-kinematic records are linked through their exact event/compiled/provider identities. They are not recompiled or reevaluated.

The electronic inverse references keep their existing state resolution: a ground-initial PI source and a total Case-A RR source are not exact state-by-state inverse processes. He-I RR fit variants remain alternatives, with no active provider selected. Cold capture kinematics remain a stored-result reference without a new rate or Q approval.

## 3. Declared material coordinates

The new nuclear columns use R1's existing bare, nuclear-ground identities for n, H1, D, T, He3, He4, Li6 and Li7. Each coordinate is selected by exact equality of composition, charge, state and pool; an ambiguous or missing match fails the build. No new species identity is manufactured.

This is a declared finite number projection. It is not a statement that the original image or every primary table selects those daughter states. For example, an inclusive source containing Li7 ground and first-excited transitions remains inclusive. Its reference is attached only at reaction-family/direction level; its branch fractions, excited-state population and cascade are not assigned to the ground coordinate. The same distinction applies to isomer resolution that the source does not supply.

The historical all-bare model and the image's ionic grid are separate. Li III in the image is doubly ionized Li, whereas bare Li has charge +3. A product labeled `p` is a proton coordinate and is never silently changed to neutral H I.

With product-minus-reactant multiplicities

\[
\nu_{sr}=\beta_{sr}-\alpha_{sr},\qquad
\dot{x}_s\big|_{\mathrm{events}}=\sum_r\nu_{sr}\mathcal R_r,
\]

the unchanged compiler supplies the finite integer column. Here its operator convention is
`events_per_reference_nucleus_per_proper_second`. No native coefficient, abundance normalization, factorial convention or volume/time conversion is bound to \(\mathcal R_r\) in R2.

For chemical events every isotope count is conserved. Nuclear transformations instead preserve baryon number and total electric charge. For material species, the bound-electron contribution is

\[
\ell_s=\sum_i Z_i N_{is}-q_s.
\]

The R1 adapter adds the explicit free-electron and neutrino sidecars. The two bare beta columns are

\[
n\to p+e^-+\bar\nu_e,
\qquad
T^+\to{}^3\!\mathrm{He}^{2+}+e^-+\bar\nu_e.
\]

Their electric charge and electron-lepton counts balance. R1's neutral-spectator T column remains a different, separately referenced projection; it is not overwritten. The reused `electron_fast` coordinate is a number carrier here, without an assigned spectrum, stopping history or deposited heat.

## 4. Photon, energy and source-domain qualification

Where the supplied target/model declares a gamma, a schematic photon token is carried as an external participant. Physical total photon multiplicity, cascades, line energies and branch probabilities remain unqualified. The builder supplies no `photon_energy_eV` or synthetic energy payload to the compiler. All new event-energy outputs must therefore remain `UNQUALIFIED:ENERGY`.

Every new event has activation false, native coefficient normalization unbound, physical Q null and physical rate/Q admission false. The existing adapter enforces this boundary. A failed number/charge/lepton check cannot be repaired by changing a source value or by replacing the compiler.

Conditional constant-S, 1/v, inverse-rate and mass-convention formulas remain quoted model metadata. No formula is evaluated. Source-native T9 tables remain in their native units and support, distinct from the conditional model's 100–10000 K range. Total absorption assigned to a chosen capture or alpha branch remains an explicit source-assignment limitation. The Li atomic-binding omission remains a historical model approximation and is not used to calculate a new bare-nuclear Q.

## 5. Intended execution and outputs

Execution is deferred until the root freezes the inputs. If `sources/primary/PROVIDER_ROWS.json` is present, the command requires its finalized public-derivative SHA256 through `--primary-sha256`; the original private intake identity remains in source provenance. Additional data are admitted only through an explicitly named `--additional-provider-packet RELATIVE_PATH=SHA256`, without mutating or automatically extending the frozen primary packet. If no actual separate photodisintegration packet is supplied, all six direct photo-supplier cells remain explicit gaps.

The builder verifies the frozen packet identities and any packaged raw source bytes. Non-CC full papers may be absent from the public numerical-facts packet. Such rows retain their source hash and are marked `RAW_SOURCE_NOT_PACKAGED`; they depend on the separately preserved source-intake audit rather than claiming a new local raw-byte verification. Numeric excerpts, original units, locators and uncertainty fields are preserved. The frozen contract, original image, both recovered JSON contracts, R1 adapter/compiler and R1 registry input files are checked by hash as well.

The AGENTS identity is pinned to `authority/AGENTS_AT_INPUT_FREEZE.md`. The root separately checks current AGENTS and actual HEAD before each new node; later legitimate priority updates do not mutate the archived input snapshot or require a completed calculation to be replayed.

The default destination is this leaf's `registry/`. All output payloads are assembled before writes; a differing existing output is rejected rather than overwritten. Primary evidence, target declarations, model records, target-direction maps, new compiled columns, selected R1 references, family aliases and coverage counts are separate files.

Only a later measured build and independent review can supply the new execution/acceptance receipts. Writing this implementation does not replay R1's checks, the original 249 synthetic checks, historical backgrounds, numerical rates or Q calculations.
