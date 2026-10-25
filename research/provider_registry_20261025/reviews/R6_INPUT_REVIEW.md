# Independent R6 source/contract review — WU provider registry

Date: 2026-10-25. Reviewer scope: source semantics and proposed inactive provider-row projections; no review of a finished root implementation yet. No physical rate, integral, IVP or Q evaluation performed. Existing finite compiler249-check result is reused, not rerun.

## Decision at input-review time

**CHANGES_REQUIRED_BEFORE_ADOPTION** for findings F1 and F2 below. These concern the new extraction/representation, not a request to change or replay the historical PHYS78 model. The proposed separation of native source records, explicitly assumed isotope projections, inactive event rows and unqualified physical energy is appropriate provided the final implementation enforces it. Root has been notified before execution/adoption.

## Concrete findings

### F1 — Preserve the two different He I RR source rows

Observed: `provider_rows/extract_provider_rows.py` initially indexed RR rows by `(Z,N)` in a dictionary. The original `rec_table1.dat` has HeI a on line2 and HeI b on line3, both with `(Z,N)=(2,2)`. The second silently replaces the first. Historical PHYS78 source/atomic_network.py intentionally retains the b coefficient tuple; preserving that historical model does not justify collapsing two source identities in the new all-provider registry.

Required minimal correction: retain independent provider IDs/row locators for HeI a and b, or include a as an explicit inactive alternative while tagging b as the historical selected fit. The exact official format documentation, https://www.pa.uky.edu/~verner/dima/rec/table.txt, specifies a valid3K<T<10^6K with2.5%rms and b valid3K<T<10^10K with4.7%rms. Those are fit approximation errors, not empirical confidence intervals or covariance. The general rec.html3–10^9K statement must not silently overwrite these row-specific notes. Root/source agent were sent this finding.

### F2 — Aggregate RR does not specify total escaping photon multiplicity

Observed: initial `historical39_direction_coverage` represents every RR direction with `gamma:escaping:1`. Its provider is a total Case A recombination coefficient toward a charge state. Captures to excited states and subsequent cascades are not state-resolved in that coefficient. A one-photon schematic radiative-capture symbol does not certify the number of all escaping cascade photons, their spectrum or their energy distribution.

Required minimal correction: preserve raw source schematic notation if desired, but physical photon count/spectrum/branch must be null or explicitly unresolved for aggregate RR. Never compare this aggregate row as the exact inverse of a ground-target PI row. A state-selected single capture/decay can receive a photon count only from that provider's state/branch contract. This applies also to symbolic PHOTON products in UMIST RR/RA/REA: source notation must be separated from qualified radiation-count admission.

## Source semantics required in final implementation

### Actual target set versus source catalogue

The original PHYS78 explicit target set is21charge populations over8nuclides; electrons have distinct pool identities. Its ground/aggregate state mapping must be preserved: a charge aggregate cannot silently be the exact ground state required by a selected source. The downloaded NUBASE catalogue has5843nuclear state rows. These rows are a provider catalogue, not5843configured thermochemical populations,5843decay events or a recovered full reaction network. The original nuclear-network picture/full target list remains unrecovered; an all-target physical-completion claim is not available.

Source-native isotope labels must remain separate from model projections. UMIST H/He have nominal companion masses1/4, but the rows do not certify isotope shifts, specific isomers or electronic/rovibrational levels. H->1H andHe->4He may be explicit inactive model bindings; they may not overwrite the native unresolved-isotope fields. Leiden LiH has no explicit6Li/7Li orH/D/T assignment. Candidate Li6H1/Li7H1 projections must share their single source identity with mapping-unresolved status, not become two independent isotope-specific measurements.

Unknown state/isomer must not be silently converted to ground. Nuclear provider index0 is ground; nonzero NUBASE indices include isomers, levels, resonances and IAS. Retain state index, symbol and ordering markers. NUBASE source header explicitly permits some p/q/r/x states to be further isomers; conservative ambiguity is preferable to a false all-isomer label. Preserve measured/estimated# markers, inequality/asymmetric uncertainty literals, stable/p-unst/unknown lifetimes, and IS= abundance as distinct from decay branches.

### Chemical and radiative source records

UMIST reaction74 has disjoint10–100K and101–3000K segments; the unbound100–101K gap must not be silently interpolated into supported coverage. Other segments retain exact provider bounds and no extrapolation. Gamma is a fitting/attenuation parameter, not reaction Q. CP/CR require their native cosmic-ray reference normalization and dust albedo convention; PH requires source ISRF/dust attenuation and does not supply arbitrary-spectrum or self-shielding admission. CRP/CRPHOT are external drivers, not consumed proton/neutrino species. Repeated products and catalysts on both sides retain multiplicity and event identity.

H3+DR1577/1578 are separate supplied product-channel rate coefficients. Their ratio is not automatically a complete normalized branching law. UMIST accuracy codes A/B/C/D and Leiden accuracy codes use different definitions and cannot be mixed. Missing covariance remains null; category-level accuracy is not a covariance model.

HD source gives9levels,8radiative lines and18downward collider pairs at50,100,200K. Distinguish para-H2 and ortho-H2 collider state keys even where coefficients coincide; retain the collider on both sides. Supplied J labels are available; vibrational/electronic assignment is not inferred from a conflicting webpage label. No upward-rate detailed-balance construction or REC adapter is executed in this WU intake. LiH table sample support91.2–351.1nm and summary threshold579nm remain separate source facts. The table's1nmFWHM Gaussian representation does not become a natural line profile; its zero photoionisation literals do not establish global physical absence.

### Nuclear and weak records, masses and uncertainty

NUBASE mass excess belongs to the neutral-atom evaluated mass convention (neutron excepted). It is not directly the bare nuclear mass. For an ion with chargeq, a consistent relation is

`m_ion(q) = m_atom - q*m_e + [B_e(neutral)-B_e(ion)]/c^2 + E_exc/c^2`,

with positive electronic binding energies defined consistently. This is a convention identity, not a numerical Q evaluation. An event Q is `c^2*(sum_reactant m - sum_product m)` using the actual electronic/nuclear states and explicit leptons once. If rest-mass differences are already in the total-energy ledger, do not add Q again as heat. Missing source covariance forbids assuming independent errors or a joint Q confidence interval.

LiveChart neutron613.9±0.6s and NUBASE609.8±0.6s are distinct evaluations. Keep both inactive alternatives; do not average or activate either by freshness alone. LiveChart beta-radiation CSV repeats `unc_me`; preserve positional columns. Ground qbm uncertainty and beta-table q uncertainty500 are different source fields; the unresolved latter is not substituted for the former. Beta endpoint, atomic mass Q, mean electron energy, mean antineutrino energy and recoil are distinct quantities.

For a material species with nuclear-charge sumZ_tot and ionic chargeq, bound-electron lepton count is `Z_tot-q`. Add free electrons withL_e=+1,positrons with-1,nu_e with+1 andantinu_e with-1. For the proposed neutralT -> He3+ +e_beta+antinu_e projection, one spectator bound electron is retained on each side; daughter atomic shake-up/off/manifold branches remain unresolved. The free-neutron row has no bound electron initially. Branch uncertainty and electronic-state resolution cannot be certified by checking this integer identity.

All other NUBASE branch tokens remain uncompiled metadata until actual products/state/particle types are resolved. In particular the legacy compiler has no positron/neutrino species pool; neutral leptons belong in a separately checked sidecar, and a future beta-plus row cannot pass a material-only charge check by discarding the positron.

## Exact implementation obligations for C9

1. Hash the immutable compiler to60a502895266b6feb96964abc4b24db61c2faed2344db0f7d12f16bb47ed62af; do not modify or replay its old fixture suite.
2. Validate source exact-row locators and original decimal strings against raw files, with provider-specific duplicate-key handling.
3. Reject unknown material species; retain full reactant/product multiplicities and catalysts; check chemical isotope+charge and nuclear baryon+charge with the applicable particle sidecar.
4. Separate provider identity from physical-event identity. Different evaluated providers for the same branch are inactive alternatives; actual branches, isomers, states and particle signs alter canonical event identity.
5. Preserve native rate unit/normalization; compiler normalization metadata is an unbound prospective conversion, never proof that cm^3/s or per-target s^-1 is an event rate per reference nucleus. No artificial test-rate source should be reported as a physical rate.
6. Every real event uses provider-only energy qualification. `compile_reaction` must yield unqualified energy, neverSYNTHETIC_EXACT. No thermal residual is fabricated to force energy closure.
7. Registry availability/completeness counters distinguish source rows, bound candidate projections, configured historical populations, implemented compilation, scientific rate evaluation and consumer admission.
8. New rows remain inactive; no HH_R10 or production activation. Named consumer, actual mass/Q/branch/recoil/thermal/fast/radiation ownership and native-domain checks are future gates.

## Budget separation

Historical PHYS91 primary/reference/Wolfram allowances remain0; global historical remaining staysnull. The completed finite compiler's30CPU/120wall/512MiB cap does not transfer unused credit to this new registry. The new current-user-requested lightweight metadata/structural checking contract must state its own actual resource cap/lease and measured usage, without fabricating a historical global balance. Independent checking should run once on final frozen output with changed-input repair only after a concrete failure. It will validate actual new provider-row transformation, not replay an old scientific calculation.

## Review status

R6 source inspection complete; F1/F2 required repairs sent. C9 finished-output review and independent checker pending the root's final files. Source availability is not empirical validation. No full rate or nuclear-Q approval is issued by this review.

## Addendum: supplied source correction reviewed

Source agent supplied separate immutable CORRECTION_V1.json SHA256`3e46d7a8a82aa1c0ff4f90db05da62269a1cfcfc46c5d5a85308500e8a2adffd`; original extraction bytes remain preserved. Both HeI literal rows match raw table lines2/3, a/b retain separate IDs and the official row-specific domains/rms. All13aggregate RR directions receive unresolved total-cascade photon count while preserving the single primary capture symbol separately. **F1/F2 source-correction design accepted; final root integration remains to verify.**

Static wrapper finding F3: extended external-side identity sorted raw pairs but did not combine repeated identical photon/lepton labels. Equivalent one count2 versus two count1 representations need canonical summation or explicit duplicate-label rejection. This differs from preserving total event normalization. Root notified. Final alternative-source rows must share physical branch identity independently of provider identity; check NUBASE/LiveChart and HeIa/b explicitly.

## Addendum: concrete missing-CI source recovery

Root is recovering the six actual Z<=3 Voronov1997 direct electron-impact ionization fit rows through official Verner col.html/cfit.dat links. Independent source-document reading of https://www.pa.uky.edu/~verner/dima/col/cfit.txt confirms byte fieldsZ,N boundelectrons,dE(eV),P,A(cm^3/s),X,K,Tmin(eV electron temperature),Tmax(keV electron temperature). Preserve these native units; neither Tmin nor Tmax is inK or incident-photon energy. The source supplies thermal coefficients, not differential collision or daughter-state/energy kernels. The coarse dE token remains a fit parameter/ionization-energy source field; it must not replace a separately qualified precise isotope chemical-defect energy. Adding these rows as inactive isotope-blind candidates addresses a concrete inventory gap without issuing a rate or Q approval.
