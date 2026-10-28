# R17A: published two-temperature reactive thermal-total audit, conditional theory

## Scientific inputs (source-derived, printed precision)
González-Lezana, Hily-Blant and Faure, JCP 157, 214302 (2022), DOI 10.1063/5.0128598, Sec. III A / Fig. 5 adjacent prose gives *thermalized total* SQM reactive rates for H⁺+HD→D⁺+H₂: k(205 K)=1.21 and k(295 K)=2.21 in units 10⁻¹⁰ cm³s⁻¹. The experimental centers are 1.1 and 1.7, both with printed ±0.2, same units. Separately the paper prints its global phenomenological Arrhenius fit k_fit(T)=8.57×10⁻¹⁰ exp(−405 K/T) cm³s⁻¹. These transcription decimals are exact *strings*, not unrounded scientific true values. The unobserved cross-temperature or experimental covariance is NOT assumed known.

## Exact rate normalization (direct derivation)
Let N=10⁻¹⁰ cm³s⁻¹=10⁻¹⁶ m³s⁻¹. Define m_T=k_SQM(T)/N and o_T=k_exp(T)/N. Use exact rational representations of the printed values:

- (m_205,o_205,h_205)=(121/100,11/10,1/5)
- (m_295,o_295,h_295)=(221/100,17/10,1/5)
- d_T=m_T−o_T=(11/100,51/100)
- z_print_T=d_T/h_T=(11/20,51/20)=(0.55,2.55)

The symbol z_print means *difference in units of a printed halfwidth*; it is **not** a normal z score, probability, confidence interval, or p-value. A paper expression "±0.2" does not by itself establish a Gaussian standard deviation or a rigorous deterministic error bar. The two printed SQM-to-experiment differences in SI units are 1.1×10⁻¹⁷ and 5.1×10⁻¹⁷ m³s⁻¹.

## Two-temperature Arrhenius diagnostic (derived, not author model fitting)
Because both printed m-values are strictly positive, the **unique exponential passing exactly through these *two printed points*** has

\[
\gamma_{2p}=\frac{\log(221/121)}{1/205-1/295}\,\mathrm{K},\quad
\alpha_{2p}=(121/100)\exp(\gamma_{2p}/205)\,N.
\]

Its values are approximately 404.7606236591465 K and 8.715145953651002 N. The authors' separately published all-temperature fit uses 405 K and 8.57 N; do **not** force it through either printed point or alter the author's fit. The adjacent agreement of slopes is a numerical comparison, not an independent physical validation nor a source-state certification.

## What the aggregate cannot resolve (conditional linear algebra, not a novel strong no-go)
Suppose at any fixed T a physically declared thermal aggregate has nonnegative resolved rates r_a(T), weights w_a(T)>=0, with at least two positive weights, and K(T)=sum_a w_a(T) r_a(T). Then for any target a with w_a>0, 0<=r_a<=K/w_a, but no unique r_a follows. The vectors (K/w_a)e_a and (K/w_b)e_b with a≠b, w_a,w_b>0 give identical aggregates and different target r_a. For strictly positive rates, v=e_a/w_a−e_b/w_b is a nonzero null vector; sufficiently small signed perturbations preserve nonnegativity. At two temperatures, **unless a time/temperature model couples them and the weights are known**, the two aggregate constraints do not establish an individual native table entry. The real HD thermal weights, state-resolved rows, and their source uncertainty are not supplied by these two printed total values. This is a scoped elementary linear-algebra explanation, not a claim that *no future information* could resolve the states.

The reverse D⁺+H₂ channel, HD+H⁺ internal excitation, and neutral H+HD collisions are different sources. Spin-averaging across states is not justified without source-specific conventions. The earlier R17 R1 stoichiometry S=(-1,-1,+1,+1) remains exact for the exchange reaction; an aggregate rate alone supplies neither density/clock nor full-A and whole-domain forcing certificates.

## Code contract and exactness
Use rational integer Fraction arithmetic for transcribed decimals, units, differences and z_print. Evaluate only the **published two temperatures** for input/output; evaluate published α exp(−γ/T) only for a *diagnostic at those two temperatures*. Use Decimal≥80 digits for the production exponential with bounded remainder cross-check to independent 100-digit mpmath/Wolfram. Do not synthesize state rows, interpolate a rate table, or call a physics solver. The output explicitly reports `state_resolved_admitted=false` and `physical_consumption_admitted=false`.

## Scope / power & limits
This standalone two-temperature comparison adds a source-backed actual aggregate arithmetic diagnostic, not a new WU DAG science node, not a physical solution, not a quality claim about 0.2 printed halfwidth, and not evidence that the original native supplemental table was downloaded. WU33/48, REI28/88, R17 source/state/consumer INPUT_PENDING remain unchanged. The user's requested full physical next node remains blocked on the native supplemental numeric bytes and its independent row reviewer.
