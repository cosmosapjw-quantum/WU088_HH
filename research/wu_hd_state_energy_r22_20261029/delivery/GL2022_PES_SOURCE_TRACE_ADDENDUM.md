# R22 detached scientific addendum | GL2022 exact PES provenance and outstanding threshold gate

Date (KST): 2026-10-29. Scope: original ionic H+ + HD(v=0,j=2) -> D+ + H2(v'=0,j'=1), **not neutral H+HD**. Source R21 PR159 commit `fd351d0ff97ef0d7a9cf710bdecad922af7e885e`. This addendum postdates and DOES NOT MODIFY immutable R22 SOURCE ORIGINAL ZIP (95,734 bytes, SHA256 `5d92267615c91e9c34c9c496956bdf58473ee41f1db6e58ccbbbfbf4fd95477c`).

## 1. New original-article evidence

González-Lezana, Hily-Blant and Faure, *Journal of Chemical Physics* 157 (2022) 214302, doi:10.1063/5.0128598, Section II ("THEORY"), original publisher PDF textual extraction by Exa at https://aip.scitation.org/doi/pdf/10.1063/5.0128598, explicitly states that **all SQM calculations employ the ground electronic H3+ (1 1 A') potential energy surface of Velilla et al. (2008)**. It describes a time-independent coupled-channel log-derivative propagation for capture probabilities from roughly 1.5 to 36 Å, SQM factorization in an intermediate complex, and a full PES with revised long-range terms R^-3 and R^-4. Original source citation: L. Velilla, B. Lepetit, A. Aguado, J. A. Beswick and M. Paniagua, *J. Chem. Phys.* **129**, 084307 (2008), doi:10.1063/1.2973629.

The paper's Fig. 1 is an energy-level diagram for the considered HD and H2 rovibrational channels, but the text extraction provides **no authenticated numerical values for the exact (0,2)->(0,1) threshold, nor a precise energy-zero/isotope-ionization-offset instruction**. The paper's total thermally averaged fit gamma=405 K (~0.035 eV) is *NOT* the state-specific threshold; it includes Boltzmann/nuclear-spin factors.

This is primary-article **textual provenance**, not an independent original PDF-byte SHA verification. The original 2022 supplemental TABLE 2 PDF remains pinned at SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`.

## 2. Same-PES independent warning, not a proof of GL2022 implementation details

M. Lepers, G. Guillon, P. Honvault, *MNRAS* **488** (2019) 4732, doi:10.1093/mnras/stz1797, Introduction/Method, https://academic.oup.com/mnras/article/488/4/4732/5527325, explicitly uses the Velilla2008 VLABP H3+ ground PES and states their Born-Oppenheimer scattering computation **neglected the H/D ionization-potential difference of about 3 meV**. They give a *ground-ground* physical 39.5 meV endothermicity with 35.8 meV zero-point and 3.7 meV ionization parts; their own BO computation omits the latter. The article's §3.2 describes HD(0,2)->H2(0,0) as approximately 3.4 meV endothermic *in that uncorrected BO convention*. It is a different product rotational channel and a different TIQM computation, **not** a numerical calibration of the GL2022 target channel.

Consequently, using the **same PES** is not sufficient to prove that GL2022's SQM code included an electronic/isotopic asymptotic offset. It is also not evidence that it definitely omitted it. The explicit source grid rates must remain unchanged.

## 3. Updated gate classification

| Obligation | New status | Evidence limit |
|---|---|---|
| GL2022 statistical-mechanical PES identity | **LITERATURE-SUPPORTED_TEXTUAL_MATCH** | Original full article II -> Velilla et al 2008 DOI |
| Source-native energy zero, channel threshold (0,2)->(0,1) | **UNRESOLVED** | No direct numeric threshold extracted from GL2022 |
| Isotope ionization (H vs D) offset included in GL2022 SQM | **UNRESOLVED**, high-priority P0 | 2019 *other code* explicitly omitted; cannot infer 2022 |
| Spectroscopic candidate Q | **DERIVED / NUMERICALLY_CHECKED, NOT_ADMITTED** | -20.9500211513003896 meV, corrected external spectroscopy; NOT source-native |
| Physical event Q / physical bath heat | **NULL/NULL** | No owner admission |
| REC/CR executable chemistry owner | **NOT_BOUND / ACK_NOT_OBTAINED** | Full trees and selected code read, no full runtime call graph |

The H2(0,1) rotational interval 118.48684(10) cm^-1 reported in Salumbides et al 2011 Table II was **quoted there from Jennings et al. (1984)**, not a 2011 direct measurement. This genealogical correction preserves the numerical spectroscopic candidate and makes the original measurement dependency explicit.

## 4. Minimal next falsifier and stop rule

1. Obtain the original complete GL2022 main article PDF with **byte identity** and visually inspect Fig. 1 and Sec. II with genuine pagination; then retrieve Velilla2008 PES's channel asymptote specification and any GL2022 calculation input/data for rovibrational threshold energies.
2. Construct, in one declared frame/energy convention, `E_HD^PES(0,2)` and `E_H2^PES(0,1)`; specify where the H/D isotope ionization correction enters. Calculate `DeltaE_PES` and compare independently against the external spectroscopic `+168.9733160842086 cm^-1`. Keep separate **BO-native threshold**, **metrologically corrected physical event energy**, and **rate-model source convention**.
3. Until the exact native threshold and correction are authenticated, do not insert a numerical physical Q into R21 `thermal_ledger.py`, do not infer the missing Q from the R21 rate grid or the total thermal Arrhenius fit, do not compute physical `B(Q)`, reverse rates or detailed balance.
4. For foreign REC/CR modification, additionally require the named actual four-species molecular chemistry callsite + **explicit owner ACK**, no substitute atomic D/H charge exchange or nonreactive HD rotational transitions.

**DAG/claims unchanged:** 34/49 central, 18/20 inherited R21 scoped workflow, distinct-author R6/C9 NOT_RUN, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`. This addendum is an additional independent **documentary** source check and NOT an independent-author science review or production validation.
