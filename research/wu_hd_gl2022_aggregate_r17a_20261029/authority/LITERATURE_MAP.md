# R2 source triage and literal source mapping

**Anchor:** González-Lezana, Hily-Blant, Faure, *J. Chem. Phys.* 157, 214302 (2022), DOI 10.1063/5.0128598, the **Section III A Figure 5 prose** (two published SQM reactive *total* thermal rates, two experimental centers with quoted ± values, and separately fitted Arrhenius α/γ). Transcribed into `PUBLISHED_TWO_POINT_TRANSCRIPTION.json`. These are rounded representations of author-printed quantities; neither original HTML nor supplementary native raw bytes were received. Web source: https://pubs.aip.org/aip/jcp/article/157/21/214302/2842276/A-statistical-investigation-of-the-rate-constants .

**Native source:** AIP supplementary link https://aipp.silverchair-cdn.com/jcp/article-supplement/2842276/zip/214302_1_epaps/ returned HTTP 403 through Exa and remained inaccessible through web click and container fetch. The original R17 R1 selected row HD(v0,j2)→H₂(v′0,j′1) has no numeric value in inspected files.

**Separate nonreactive data:** EMAA DOI 10.17178/emaa_hd_rovibration_805a7aa5 gives 171 H⁺ projectile collisions in **HD internal rovibration**; not H⁺+HD→D⁺+H₂. REI S6 `private_inputs/lamda_hd_20261025.dat` is 2,289 bytes of HD spectroscopy and is not a reactive rate table. The user-supplied H–Li catalog 26 ground plus five nuclear excited states, 102 formal charges and 621 missing process cells does not imply new solver species.

**Separate reactive method:** Lepers et al., 2019, DOI 10.1093/mnras/stz1797, TIQM and erratum DOI 10.1093/mnras/staa3146, different rate family and thermal spin averaging. Do not silently reweight native SQM product rows.

**What evidence supports:** Two actual paper-printed SQM total rates, printed experimental centers and halfwidths, two published Arrhenius constants. It does not support state-level source values, source-specific experimental sampling law or covariance, full-A operator, named consumer density/clock, or cross-method rate substitution.
