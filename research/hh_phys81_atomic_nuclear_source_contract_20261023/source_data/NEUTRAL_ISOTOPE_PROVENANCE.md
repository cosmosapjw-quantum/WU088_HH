# PHYS81 neutral chemical ionization isotope provenance

Scope: read-only source review of the three chemical first-ionization values. This review does not certify isotope-dependent electron-impact cross sections, kinetic closures, rate accuracy, or any completed PHYS/C22D science. No science code was imported and no numerical conversion, quadrature, ODE, or numerical verification was run.

## Decision relevant to the source contract

| Project label | Adopted literal | Primary-source finding | Accurate status |
|---|---|---|---|
| H1 | 13.598434599702 eV | The existing ASD H I page supplies this value and HDEL reference. The official NIST hydrogen handbook explicitly identifies its levels with 1H, but its co-located ionization value is the older 13.598433 eV. | Ordinary-H-to-H1 convention has official support. The reviewed exact-number ASD page does not itself supply the explicit 1H note; do not describe this as same-page isotope proof at the quoted precision. |
| He4 | 24.587389011 eV | A newly fetched **neutral He I** ASD page explicitly qualifies the data as 4He and contains this exact Limit value, uncertainty 0.000000025 eV, reference L17714. | Direct co-located isotope provenance closed. This uses neutral He I evidence, independently of the existing residual He II note. |
| Li7 | 5.391714996 eV | The neutral Li I ASD page gives this value, uncertainty 0.000000022 eV, reference L12261. Its units=0 version gives 43 487.11420 cm^-1, uncertainty 0.00018 cm^-1. L12261 resolves to Bushaw et al. (2007), whose original-author institutional abstract instead explicitly gives **7Li: 43487.15940(18) cm^-1**. | Do not call the adopted elemental ASD number an explicitly isotope-qualified 7Li chemical defect. There is a concrete source-number discrepancy, not merely a missing label. |

No numerical conversion of either lithium value was performed. The natural-isotope-weighted interpretation of the elemental ASD value is a plausible inference, but this review found no explicit NIST statement establishing it. It must remain unconfirmed rather than becoming contract fact.

## Minimum corrected contract wording

If retaining the existing literals:

> Chemical ionization energies use the identified NIST ASD H I, He I, and Li I values. The neutral He I data explicitly refer to 4He. H1 follows the official ordinary-hydrogen/1H convention, with the exact-number H I source linked to HDEL. For project Li7, 5.391714996 eV is an adopted elemental Li I value and is not certified here as the 7Li-specific spectroscopic limit: the cited original paper reports 43487.15940(18) cm^-1 for 7Li. The cross-section curves remain electronic-target data without newly certified isotope-shift corrections.

If isotope-specific Li7 chemical bookkeeping is required, prefer the explicitly qualified primary literal:

\[
I(^{7}\mathrm{Li})=hc\,[43487.15940(18)\ \mathrm{cm}^{-1}].
\]

The root may convert this using the declared unit-conversion policy under its shared numerical lease. The source-window knots must remain separately identified as source data. An updated chemical defect does not license shifting the source energy axis or claiming a newly isotope-resolved cross section. This is a correction option, not an edit performed by this reviewer.

## Exact neutral-source evidence and stable URLs

### Helium: direct qualification at the adopted value

- Source query: <https://physics.nist.gov/cgi-bin/ASD/energy1.pl?spectrum=He+I&units=1&conf_out=1&term_out=1&level_out=1&j_out=1&unc_out=1&biblio=1>
- Raw snapshot: `nist_hei_levels_eV.html`.
- Raw line 176, short exact note: “The energy level data refer to the isotope 4He.” Superscript markup has been flattened in this quotation.
- Raw Limit row at lines 12660–12665: 24.587389011 eV; uncertainty 0.000000025 eV; L17714.
- Retrieved web references: `turn37view0` and numeric find result `turn38view3`. The web query contains additional output options but selects the same neutral spectrum and eV units. Web line 8 is the isotope note; line 1307 is the Limit row.
- Web URL: <https://physics.nist.gov/cgi-bin/ASD/energy1.pl?biblio=on&conf_out=on&de=0&format=0&j_out=on&lande_out=on&level_out=on&multiplet_ordered=0&output=0&page_size=15&perc_out=on&spectrum=He+I&submit=Retrieve+Data&temp=&term_out=on&unc_out=1&units=1>

### Lithium: original 7Li limit differs from the adopted elemental value

- Neutral eV query: <https://physics.nist.gov/cgi-bin/ASD/energy1.pl?spectrum=Li+I&units=1&conf_out=1&term_out=1&level_out=1&j_out=1&unc_out=1&biblio=1>
- Raw snapshot `nist_lii_levels_eV.html` is **Li I**, despite its compact filename. Raw lines 1943–1945 give 5.391714996 eV, 0.000000022 eV, L12261.
- Neutral cm^-1 query: <https://physics.nist.gov/cgi-bin/ASD/energy1.pl?spectrum=Li+I&units=0&conf_out=1&term_out=1&level_out=1&j_out=1&unc_out=1&biblio=1>
- Raw snapshot `nist_li_i_levels_cm_inv.html`, lines 1943–1945: 43 487.11420 cm^-1, 0.00018 cm^-1, L12261. No explicit isotope qualifier was found in these Li I snapshots.
- Web references for the cm^-1 table: `turn40view0`, `turn43view1`; web line 192 gives the Limit row. Stable web URL: <https://physics.nist.gov/cgi-bin/ASD/energy1.pl?biblio=on&conf_out=on&de=0&format=0&j_out=on&lande_out=on&level_out=on&multiplet_ordered=0&output=0&page_size=15&perc_out=on&spectrum=Li+I&submit=Retrieve+Data&temp=&term_out=on&unc_out=1&units=0>
- NIST bibliography query: <https://physics.nist.gov/cgi-bin/ASBib1/get_ASBib_ref.cgi?db=el&db_id=12261&comment_code=&element=Li&spectr_charge=1&ref=12261&type=I>. Raw lines 53–55 identify B. A. Bushaw, W. Nörtershäuser, G. W. F. Drake, H.-J. Kluge, *Physical Review A* 75, 052503 (2007), DOI [10.1103/PhysRevA.75.052503](https://doi.org/10.1103/PhysRevA.75.052503).
- Original-author institutional abstract: <https://www.pnnl.gov/publications/ionization-energy-li-6li-7-determined-triple-resonance-laser-spectroscopy>.
- Raw snapshot `pnnl_bushaw_2007_primary_abstract.html`, line 1170; web reference `turn41view0`, lines 237–238. Short exact numeric text: “EI (7Li) = 43487.15940(18) cm-1” and “IS(EI)7,6 = 18067.54(21) MHz.” The surrounding abstract identifies the first quantity as the spectroscopic ionization energy from measured 7Li Rydberg series. The citation on the same page matches the NIST bibliography DOI.
- The primary abstract was reviewed; the full journal paper was not retrieved. No eV value has been invented or inferred from it in this review.

### Hydrogen: explicit convention, different precision record

- Existing exact-number source: <https://physics.nist.gov/cgi-bin/ASD/energy1.pl?spectrum=H+I&units=1&conf_out=1&term_out=1&level_out=1&j_out=1&unc_out=1&biblio=1>.
- Existing raw snapshot `/tmp/phys81_intake/sources/nist_hi_levels_and_limit_eV.html`; Limit 13.598434599702 eV, uncertainty 0.000000000012 eV, HDEL. Its HDEL link redirects to an official NIST landing page that currently says the data site is being updated; no replacement numerical table was reviewed.
- Explicit 1H source: <https://physics.nist.gov/PhysRefData/Handbook/Tables/hydrogentable1_a.htm>.
- Raw snapshot `nist_hydrogen_handbook_isotope.html`, line 47: “The wavelengths and energy levels given below are for the isotope 1H.” Superscript markup flattened.
- Same handbook page, line 58, gives the older 109678.7717 cm^-1 (13.598433 eV), Ref. MK00a. Thus it supports the isotope convention but is not a numerical match to the adopted many-digit value.
- Retrieved web reference: `turn41view1`, isotope note line 19 and ionization entry line 24. Exact-number elemental ASD search reference: `turn44search17`, <https://physics.nist.gov/cgi-bin/Elements/elInfo.pl?context=noframes&element=1>; this has the numeric value but does not add an explicit isotope qualifier.

## Raw-byte hashes and retrieval receipts

These hashes were computed from the actual saved bytes. Web references are separately identified above; no hash is attributed to unavailable or merely indexed web text.

| File, relative to this review folder unless absolute | SHA256 |
|---|---|
| `nist_hei_levels_eV.html` | `5add21e3ceaf75424abbd1b5a1c7176131f377a53c8bbc66caf123feb64f4186` |
| `nist_lii_levels_eV.html` | `be98a61185db0a1e941fba606f73ceac576a0d8e4b1cd89dfe8eeff34d51ee60` |
| `nist_li_i_levels_cm_inv.html` | `ecbd99d96fa8571eb2f0340155f144bc2e00dbd709c28b625f05f8b6458b5a01` |
| `nist_li_reference_L12261.html` | `75e6f54f83a4c10a7e705c2b2bcf0310d15e3928de90a3fccd58743ae21598ef` |
| `pnnl_bushaw_2007_primary_abstract.html` | `dfe6056f9915ddbf0ef98bfa7e28b24606e7f484c81979ec650ecd45ebaab1e0` |
| `nist_hydrogen_handbook_isotope.html` | `2cae16198d9c8bb01b15de55b035456bb1cba716725db51826816e7455d08c8d` |
| `/tmp/phys81_intake/sources/nist_hi_levels_and_limit_eV.html` | `360e7363a1b1dd1b792ec866c57a4d7d54e10c122ab207a9e40e59788ef9f19d` |
| `/tmp/phys81_intake/sources/PHYS81_ATOMIC_CI_SOURCE_REGISTRY.json` | `bca14bfb596e29f478ef50fb1aab2b721eae3a2cff5ab8746f0e511a68a31aec` |
| `/tmp/phys81_intake/sources/NIST_GROUND_PRODUCT_WINDOW_EVIDENCE.json` | `37bfee34144ab9584f13b2586a0406da8ca7e97db4ebf5774f6dd44d83da059d` |

`PRIMARY_FETCH_NEUTRAL_ISOTOPE.json` records failed default-sandbox requests (network permission errors). `PRIMARY_FETCH_NEUTRAL_ISOTOPE_ESCALATED.json` records the successful approved public fetches of the He I, Li I eV, and L12261 pages, each HTTP 200. `PRIMARY_FETCH_FINAL_RECEIPTS.json` records the successful approved public fetches of the Li I cm^-1, PNNL, and hydrogen-handbook pages, each HTTP 200.

## Commands and scope receipt

- Executed `python /tmp/phys81_review/atomic/isotope/fetch_final_primary_sources.py`; command exited **0** (initial tool chunk `9fcd69`, completion chunk `2842af`). It performs fixed public URL GETs, raw-byte writes, and metadata hashes only. Source text is included in this folder.
- Executed `sha256sum /tmp/phys81_intake/sources/PHYS81_ATOMIC_CI_SOURCE_REGISTRY.json /tmp/phys81_intake/sources/NIST_GROUND_PRODUCT_WINDOW_EVIDENCE.json /tmp/phys81_intake/sources/nist_hi_levels_and_limit_eV.html`; exit **0**, chunk `a6d62c`.
- Source extraction with `rg -n -C` against the above raw pages and intake records completed with exit **0** (chunks `7fee63`, `f17369`, `34e66a`). These are textual inspections, not numerical verification.
- The earlier approved fetch recorded in `PRIMARY_FETCH_NEUTRAL_ISOTOPE_ESCALATED.json` completed with exit **0**, chunks `1c95c9` and `be0ab5`. Its inline command is not reconstructed here; the exact URL, HTTP status, size, time, and raw-byte hash are in that receipt.
- Narrow official NIST searches found no explicit statement explaining the Li value as a natural-isotope average. This is a search limitation, not proof that no such documentation exists.
- No unit/intake source file was modified. No numerical test, ODE, quadrature, science-code import, old suite, remote mutation, or process termination was performed.

Before citing web references in the root answer, reopen the stable URLs or reference IDs from the root agent as required by the tool citation rules.
