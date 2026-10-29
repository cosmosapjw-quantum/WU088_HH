# WU088_HH R25 | source-locked 100-cell H₂ product branching and two-stage order memory

**2026-10-29 KST. Status: PASS_SCOPED_SOURCE_NATIVE_SQM_PRINTED_CHANNELS / HOLD_PES_NATIVE_Q.**

## Physics and evidence

Primary: González-Lezana, Hily-Blant & Faure, *J. Chem. Phys.* 157, 214302 (2022), DOI https://doi.org/10.1063/5.0128598; supplementary PDF byte SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754` (273,554 bytes). Parsed original Tables 1–10 each `(v,J)=(0,2)` source row at the ten published T nodes. Original printed `mantissa(exponent)` indicates powers of ten, not statistical error. The source-native object is **computed state-to-state SQM thermal rate data**, not PES-native rovibrational threshold or experimental rates.

- 100 original `(J',T)` cells; 96 positive, four 15 K `0.00(00)` unqualified printed zeros at J'=6–9. No physical-exact-zero inference. Source tokens SHA256 `f1b8e438a0117688e2497af1434227a42c8c158bab9f810b536b3ad2c36e4174`. CSV preserves every printed token plus qualification.
- Published-final-state conditional rates `K_{0..9}=Σ_{j=0}^9 k_j`; 105 K `K=2.9180308002830054710000009610113E-10 cm³/s`, 255 K `K=5.42831870520559E-10 cm³/s`. Product J'=1 among reported at 105 K = 39.41013919%, 255 K = 50.47603409%. Odd-J' (ortho) among reported at 105 K = 39.41760999%, 255 K = 51.93903431%. These are **conditional on the ten published channels**. No extra 3/4 nuclear-spin weighting; no initial HD J2 Boltzmann fraction.
- 15 K source total and conditional branching remain NULL: omitted nonnegative channels may be below printed precision. Other nine temperature nodes are complete relative to the ten published channels; rates above J'=9/v'>0 were excluded.

## Constructive two-order calculation

Source-locked forward-only **synthetic physical-kinetic experiment**, not observed cosmological gas history: initial equal `n(H+)=n(HD(v0,J2))=10^6 m^-3`, zero product states, fixed volume, externally held two 5×10^9-s temperatures 105/255 K, ten channels. Mass-action `R_j=k_j(T)n_H+n_HD`, no reverse/thermal bath/rethermalization/expansion. Full two-stage exact solution:

- For 105K→255K and reverse total ξ=806695.105463136768062702730380958070790627348736018719213451974260197820250 m^-3 (identical). Generated H₂(J'=1) = `341530.071534800143332332197489955261809928126890739388140805671784047248996 m^-3` vs `398784.805320951364404599475118233583180814925278227508739688550570741826780 m^-3`, difference `57254.73378615122107226727763 m^-3`. No adjustment of the underlying original rates.
- H/D nuclei, charge, and total particle count conserved to Decimal75 numerical precision. SciPy DOP853 reference integration compared against the closed-form source results; tests 27/27 normal and 27/27 `-O` PASS, negative guards for changed DOI, state, original source PDF, physical Q/owner, census 15 K, and order-swap conservation. Initial test fixture at Decimal28 displayed a precision-budget failure; corrected test numerical context to Decimal90, with original failure preserved. No source-physics patch was needed.
- Exact derivation: with `a=n0 K_105 Δt105`, `b=n0 K_255 Δt255`, `X(z)=n0 z/(1+z)`, branching vectors `p_j=k_j/K`, the order asymmetry is `ΔN_j=(p_105,j-p_255,j) n0 a b(2+a+b)/[(1+a)(1+b)(1+a+b)]` where Δ means [105→255] minus [255→105]. Sum over j vanishes. SymPy and Wolfram independently verify algebra (same-author/model context, not distinct-author review).

## Actual release/admission status

**Central WU canonical scientific DAG 34/49 UNCHANGED.** New scoped R25 source product grid + conditional forward experiment is **1/1 scoped evidence data deliverable**, not a canonical science-node closure. R23 historical scoped workflow remains 18/20; R6/C9 distinct-author NOT_RUN. `GL2022_PES_NATIVE_THRESHOLD=null`, `physical_Q=null`, `source_uncertainty=null`, `physical_bath=null`, `reverse_rate=null`, `owner_ACK=null`, `HH_R10=OFF`, `full_A=null`, `L4=false`, `production=NOT_ISSUED`.

GL2022 Eq(3) total-energy vs Eq(4) entrance-kinetic zero, H/D isotope correction and Velilla2008 numeric PES remain unresolved. Existing R24 bound 15.186303821758897 meV cannot be promoted to source-native threshold; R23 20.95002099384 meV is independent spectroscopy-side candidate, not R25 native Q. REC PR159 LAMDA rotational and CR PR124 HD_CX atomic charge exchange do not establish four-species owner ACK. Foreign repositories remained untouched.

## Reproducibility

Use `PYTHONPATH=. python -m unittest discover -s tests -v` and `PYTHONPATH=. python -O -m unittest discover -s tests -v` inside source archive; rerun CLI with original PDF and **new output directory**, not overwriting immutable saved results. Source program requires `pdftotext -layout`, no OCR. Original PDF source byte identity and literal grid are re-extracted and cross-checked by tests. Generated diagnostic figures are visibly checked, not observables or physical uncertainty plots.
