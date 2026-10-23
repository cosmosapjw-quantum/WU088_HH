# PHYS82 Li I threshold source synthesis

## Result

The source campaign improves the empirical constraint on the missing interval, but does not close full physical low-temperature rate coverage. The strongest new reusable fact is the **published finite-resolution Li straight-segment slope**, not a new CCC table below 6 eV.

The public-safe contract is `PHYS82_LI_THRESHOLD_SOURCE_CONTRACT.json`. Full PDFs, images, downloaded ADAS files and search/fetch receipts in this directory are private source evidence and should not be published with code.

## Adopted empirical comparator

Zapesochnyi and Aleksakhin, *Soviet Physics JETP* **28**, 41–45 (1969), [primary journal PDF](https://jetp.ras.ru/cgi-bin/dn/e_028_01_0041.pdf), printed p44 table, gives for Li:

| Quantity | Printed value |
|---|---:|
| Ionization potential | 5.39 eV |
| Maximum location | approximately 13.0 eV |
| Linear interval in excess energy | 3.4 eV |
| Straight-segment slope mantissa | 0.9 |
| Maximum cross section | 4.2 × 10^-16 cm² |

**Unit issue:** the actual rendered slope heading reads `10^-16 cm^-2/V`. The negative area exponent is dimensionally inconsistent with a cross-section slope and with the paper's own axes and measurement formula. Preserve that literal typography in provenance. The physically usable interpretation is **0.9 × 10^-16 cm²/eV**, since an electron accelerating-voltage change of one volt changes its kinetic energy by one eV. This is a transparent dimensional correction; no published erratum was located.

The source supports the reconstructed comparison curve

```
sigma_ZA(E) = (0.9e-16 cm^2/eV) * (E - I_physical),
I_physical <= E <= 6 eV,
I_physical = 5.39172060034581 eV.
```

Replacing the historical 5.39 eV origin by the parent physical isotope threshold is an explicit transport assumption. It does not recalibrate the experiment or yield isotope-specific measurements. Keep this comparator separate from the CCC first node (6 eV, 5.18148e-17 cm²). In particular, do not normalize it to that node and then still describe its amplitude as an independently measured slope.

## What the experiment does and does not constrain

Printed p42 describes an effusive neutral-metal beam and a 127-degree electrostatic electron selector. Its final electron beam has a 0.1 eV energy spread containing 90% of electrons over 1–30 eV. The preceding 0.5 eV figure concerns the initial gun; the two numbers are not alternative uncertainty estimates for the final beam.

Printed p43 gives 0.1–0.2 eV uncertainty on the plotted electron-energy axis, without separating calibration, scanning or interpolation contributions. This is an experimental energy-coordinate uncertainty, not uncertainty in the physical ionization energy. The same page gives a relative error of absolute cross sections of ±15% and an rms error printed as +12%, with no stated confidence level. Absolute current was usually measured near the ionization maximum (p42). Section3 on p45 reports relative errors no larger than 3% for particularly careful threshold measurements.

Figure8 contains relative cross sections in arbitrary units. Its theory curves are normalized at excess energies zero and one eV. The paper gives no separate slope covariance, raw near-threshold numeric point table, full energy-response kernel, deconvolution, isotope assay or quantitative target-state purity measurement. A ±15% amplitude variation could be investigated as an assumption motivated by the absolute-scale statement; it is not a demonstrated uniform interval envelope.

The authors interpret their finite-resolution lithium measurements as linear and claim they do not confirm Wannier. That historical interpretation should not be promoted to a rejection of the asymptotic law.

## Threshold theory and transport assumptions

The original Wannier paper is [Physical Review90,817(1953)](https://doi.org/10.1103/PhysRev.90.817). Its primary abstract confirms the 1.127 neutral-atom exponent; fulltext was behind an authorization wall.

The exact expression was read in Friedrich, Ihra and Meerwald, *Australian Journal of Physics* **52**, 323–339 (1999), [DOI10.1071/PH98091](https://doi.org/10.1071/PH98091), Eq(2) on printed p323:

```
nu_W(Z) = 1/4 * [sqrt((100 Z - 9)/(4 Z - 1)) - 1].
```

The following page specifies an infinitely heavy Coulomb center and two outgoing electrons. Source E denotes excess energy. For neutral Li ionization, using Z=1 requires the long-range residual Li+ core description; using nuclear Z=3 would be the wrong transported convention. The source provides no Li-specific proof that the pure power law is accurate over the entire threshold-to-6-eV interval.

Peterkop and Tsukerman, *Soviet Physics JETP* **31**, 374–377 (1970), [primary PDF](https://jetp.ras.ru/cgi-bin/dn/e_031_02_0374.pdf), p376, directly discusses why the alkali nonlinearity region could be too small for Zapesochnyi's experiment to resolve. It distinguishes the region where the law is valid from the smaller region where its departure from a straight line is visible.

The parent's four endpoint-matched models

```
sigma_pq(E) = sigma6 * (6/E)^q * ((E-I)/(6-I))^p,
p in {1, nu_W(1)}, q in {0,1}
```

therefore remain explicit sensitivity models. Their finite-gap normalization and regular prefactor choices do not come with a source-certified coverage bound.

## Other primary/official evidence

- **Curtin CCC:** the preserved author selector contains 13 ground-Li nodes beginning at 6 eV. Its cited Bray1994 paper was found, but fulltext access was blocked. No lower-energy CCC table was obtained.
- **IAEA D107424:** actual official fit coefficients were retrieved through Exa. GroundLi uses a Wutte1997/Lennon1988 experimental-fit lineage: A=0.08500, A1=-0.004000, A2=0.7570, A3=-0.1780, I=5.390 eV in the logarithm/polynomial-over-EI formula. This is a rounded Bell-like fit, not independent new ground-state CCC data. Its stated10% uncertainty and fit precision do not supply new pointwise uncertainty information inside the physical gap.
- **Schweinzer1999:** official IAEA Eq2 fits were readable for excited Li states. The two-page author extended abstract was acquired. The full35-page paper was not obtained; no claim is made to have read its original ground-state coefficient table.
- **OPEN-ADAS:** both raw type1 and type3 Li files were obtained. Type1 uses collision strength versus X=E/I, with X beginning1.00,1.15,1.33. The nominal-threshold point has tiny nonzero Omega; the file threshold is43489cm^-1 and is not the parent physicalI. No resolved non-threshold sample fills the requested gap before the next sample atX1.15. The site widget labels this as temperature, but the official format says type1 is energy-scaled. Type3 S rows are exponentially scaled rates, not cross sections. The files' CCC-derived-fit comments and IAEA ground-fit lineage are not interchangeable provenance. Both remain unactivated.
- **NISTBEB:** the official Li holdings page provides excitation transitions only, with no neutral-Li ionization link or orbital-constant table. The generic BEB formula is insufficient to construct a source-backed Li curve.
- **Younger1982:** actual article text supplies distorted-wave fits, but explicitly reports disagreement with measurements below approximately10eV. It is unsuitable as empirical threshold closure.

## Execution and evidence

Actual Exa search/fetch calls and an actual SciSpace literature-search call were made. Returned objects are saved, including `SCISPACE_SEARCH_RAW_001.json`, `EXA_SEARCH_RAW_001.json`, `EXA_GROUND_LI_AND_PETERKOP_RAW.json` and later focused receipts. The SciSpace results were discovery only and included ion/neutral false positives.

The raw Zapesochnyi PDF was reused with exact SHA256 b9932a8413cd8b4f8a7e428a5da536fb8dcd55150c5a63c0747cf960d4742408. Printed pp42,43,44,45 were visually inspected; p44 table and Fig8 crops have a crop receipt. The raw Peterkop PDF and ADAS files were acquired and hashed. Friedrich's full primary text is preserved in `WEB_WANNIER_FORMULA_PRIMARY_RAW.json`; the PDF-byte request itself returned403, so that retrieval object is not represented as original PDF bytes.

No cross-section evaluation, rate quadrature, ODE, completed-test rerun or remote mutation was performed. The remaining scientific obligation is an independently justified deconvolved cross-section amplitude/shape enclosure for the unresolved threshold interval; the full-rate high-energy tail also remains outside this source campaign.

