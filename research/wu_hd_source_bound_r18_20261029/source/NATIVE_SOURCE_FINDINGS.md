# GL2022 native reactive source acquisition — 2026-10-29 KST

## Acquired primary source
The author-institutional DIGITAL.CSIC record https://digital.csic.es/handle/10261/305186 directly links both the published article and its original Supplementary Information. Actual HTTPS GET returned 200 for both PDFs on 2026-10-28T22:52:25Z. This source route resolves the prior absence of native reactive printed source data; the publisher ZIP endpoint itself still returns403.

- Article: GL2022_CSIC_article.pdf, 4,910,491 bytes, SHA256 5c9d97511c46fa83ddf8e9db0fec0b2fb362f6cca00f58666a63e86a63f25bbc.
- Supplement: GL2022_CSIC_supplement.pdf, 273,554 bytes, SHA256 a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754, 14 PDF pages.
- Institutional record HTML preserved in csic_record_response.bin; metadata receipt archive_probes.json includes SHA256 f188f82e5fef585fb547e7dc66e8e03377c762a1b120c288d7477563d522e550.
- Original article explicitly states CC BY4.0. No separate supplement-license statement was found in inspected pages. All source credits remain attached.

## Selected row
Supplement PDF page6 Table2 supplies H+ + HD(v0,j2) -> D+ + H2(v0,j1), SQM reactive state-to-state raw rate values. Ten printed cells were checked through independent Poppler and pypdf extraction and the rendered original page. Exact tokens and each cell locator are in GL2022_HD_j2_to_H2_j1_NATIVE_PRINTED_ROW.json (SHA256 1f22d3995860559fc598c777acea1d05e13a88d574534effa01357ad43fde8b2).

T(K): 15,55,105,255,505,1005,1505,2005,2505,3005.
Original tokens: 3.99(14),2.92(11),1.15(10),2.74(10),3.33(10),3.18(10),2.85(10),2.55(10),2.30(10),2.08(10).
Caption convention is mantissa times10^(-parenthesized number), cm^3/s. Thus15K=3.99e-14cm^3/s=3.99e-20m^3/s, and105K=1.15e-10cm^3/s=1.15e-16m^3/s. Each nominal exact printed decimal is serialized as a Fraction; it is not a rigorous enclosure of a true physical rate. Source rounding rule and physical/model uncertainty remain UNSPECIFIED.

The source grid is discrete. No interpolation/extrapolation, fitted rate, continuous temperature proof or ODE consumer is supplied by this extraction.

## Spin and total conventions
The published article PDF page5 (journal page214302-4) Eqs5–7 was rendered and inspected. It defines the thermal total by initial-HD Boltzmann averaging and an external1/4 factor on the sum of even H2 jprime raw state rates and3/4 on the odd sum. Initial j0..8 and final jprime0..9 produce sum of weights5. This agrees with R17B's operator.

For the selected odd product jprime1,3/4 remains a separate external thermal spin factor; Table2's raw value must not be silently preweighted or multiplied twice. A concrete consumer must declare its spin convention. Numerical values of actual HD energies and Boltzmann factors were not acquired here.

## Coverage distinction
Supplement section3 PDF page5 declares reactive Tables1–10 initial-HD j0..6 and thermal Table11 a j0..6 initial Boltzmann sum. Main article Eq5 declares j0..8. Table11's original10 printed thermal totals and metadata are separately saved in TABLE11_PRINTED_THERMAL_TOTAL.json, with Poppler/pypdf token equality. Do not infer absent j7,8 arrays or a90-channel complete native source from the selected row. The j2->r1 row itself is in both declared ranges.

Two source-table observations outside the selected row remain uncorrected: Table2 j5 repeats all10 tokens of Table1 j5; Table8 j3 at2505K displays6.72(16). These are observed source entries, not a proved author typo; no replacements were made. Full700-cell source validation has not been performed.

## Retrieval scope and remaining dependencies
Exa made six search calls requesting8+8+6+5+5+5=37 result slots; these are not37 verified or distinct sources. Three initial calls are search0,pass2_1,pass2_2, then pass3_0..2. SciSpace1call returned10 irrelevant near-neighbor dataset results and supplied no source evidence. Crossref current metadata links article PDF; Figshare resource DOI lookup returned[]; HAL API identifies hal-04285297 with article PDF only. DIGITAL.CSIC supplied the needed supplement.

Publisher source ZIP raw bytes and its SHA remain unavailable. AIP main article content is readable through Exa; direct raw AIP HTML GET403. Native institutional PDF is an independent source artifact with its own immutable SHA; do not claim byte identity with the inaccessible ZIP.

Named REC/CR consumer/state densities/time clock/full-A binding and uncertainty policy are still open. HH_R10/production/L4 activation is not authorized by source acquisition. This is a source-qualified finite printed-row payload and independently checked extraction, not full physical coupled evolution. Parent should bind this row to original source-node acceptance criteria and record a minimal provenance-route update if historical contracts require publisher ZIP specifically.

