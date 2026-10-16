# PHYS60 C5–C8: original noncentral positive E Coulomb outgoing *complex* Born, m-block parity and independent CF

2026-10-16 KST. Parent PHYS60 R5 PR103 commit `789bd912e61aeccca38b218b3771aaa7f52e6775`, PHYS59 PR102 `f6e678156102332e3300a188529f37a1736fdacc`. Original 1386 complex128 NPZ SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d` verified. Original `h=-Δ/2-1/r-(1+s^-1)exp(-2s)`, s=|x-(7/10)zhat|, k=7/10 and **physical positive energy** E=+49/200 Hartree. Original eta=Fy, xi=Fy-phi unchanged, HH_R10=OFF.

## Real positive energy math-to-code

PHYS60 R5 established the genuine original noncentral *finite angular Galerkin* outgoing Jost matrix for any fixed L and all m, preserving all P<=20/Q>=21 couplings **within** L. Analytic linear response of the outgoing boundary DtN to V at λ=0 is

`D1_(l m,l' m)= integral_27^infty dr p_l^(+)(r) V_(l m,l' m)(r) p_l'^(+)(r)`

with `p_l^(+)=H_l^+(etaC,k r)/H_l^+(etaC,k*27)`, `H^+=G+i F`, `etaC=-10/7`. `V=2(1+1/s)e^-2s`, exact displaced physical `s=sqrt(r²+0.7²-1.4 r μ)`. `V_(ll')` integrates normalized associated Legendre products and is real symmetric, m is conserved and ±m sectors equal. Outgoing Green identity uses the **complex bilinear transpose** (two outgoing factors, not conjugate). The flux sign uses a separate Hermitian conjugate pairing. This formula is identical as a first derivative for all finite angular projections containing both l20 and l21; it is not a full all-angular positive-energy DtN certificate.

## Actual independent, source-bound numerical results

Physical `P_{20,m}->Q_{21,m}` first Born integral over finite `r∈[27,39] a0`: radial n=10/18/26/34 Gauss–Legendre and angular n=96/128/192/256. Actual `mpmath` CoulombG/F dps55, scipy associated Legendre Gram of original screen, no substituted central potential. Final n34/256 values:

- m0: `(2.76604224601234271232180706e-24 + 4.50067673015530586117232465e-25 i)`
- m1: `(2.76138101406124845984998988e-24 + 4.49309512471894333343848087e-25 i)`
- m2: `(2.74740042649530514397842145e-24 + 4.47035530717896904302573659e-25 i)`.

These 24-digit representations come from numerical quadrature and **are not rigorous enclosures**. Compare independent CoulombH1 log derivative DLMF §33.8.2 truncated CF depths768/1152 with outgoing CoulombG/F recurrence, physical positive Wronskian κ; check m↔-m, ell channel exchange exact real symmetric V, incoming Born complex conjugate of outgoing, complex Born imaginary ≠0 (the preceding PHYS59 negative-energy Whittaker Born is real and must not be reused here). Code source and signed-m selection rules use the original displacement along z.

A separate fully rational analytic original **multiplier radial-L1** tail is `∫_39^∞||V(r)||dr < delta_B exp(-24)/2`, evaluated by Fraction Taylor. This is **NOT a bound on the Born integral tail**, because `|p_l^+ p_l'^+|` needs its own certified outgoing Poisson bound. Numerically comparing rmax39 and rmax45 diagnoses tail/refinement only; never promote to interval quadrature.

## Tests and independent review

- New C5-C8 27/27 focused pytest PASS, together with R5 29/29 = **56/56 combined pytest PASS**, exit 0 (15.37s pytest). Source-locked producer `scripts/phys60_positive_born.py` exit0; actual stdout/exit/resource stored. Tests include wrong SHA, invalid angular r/m/depth, real source matrix, ±m and reciprocity, complex incoming conjugation, positive current and independent truncated CF. Test scientifically changing source prohibits promotion, not simply test success.
- Connected Wolfram independent exact small 2×2 outgoing Green transpose identity residual0 and real-symmetric V current cancellation0, Gaunt 21/sqrt1763, PASS. It is algebra rather than a direct independent numerical Born integral.
- No NCP, no user's local host, no original full repository pytest, no native delegated subagents in this run. All heavy campaign not required to establish this finite-dimensional/finite-domain **numerical** unit.

## Literature and DAG

References: NIST DLMF [33.4](https://dlmf.nist.gov/33.4), [33.8](https://dlmf.nist.gov/33.8), finite multichannel Coulomb Jost analytic context Rakityansky & Elander (2013) [DOI:10.1063/1.4853855](https://doi.org/10.1063/1.4853855). Retain PHYS58 rigorous all-angular screen multiplication, PHYS59 rigorous negative-energy all-angular DtN as distinct earlier results. Cross-repo recent REI PR171, BASS_HE PR74, bass_cr PR77 have photo-gas/donor ownership but supply no microscopic H-H scattering rate and no code mutated.

**Final DAG:** R5 finite-L positive-energy outgoing Jost `PROVED/PUBLISHED/BACKED_UP`; C5–C8 physical complex Born finite-boundary numeric `IMPLEMENTED/SCOPED_TESTS_PASS`; PHYS61 actual infinite-angular weighted positive-energy outgoing Coulomb resolvent/Poisson and fully noncentral `Z_S^+` `READY_THEORY`; physical low+high matching/regular-origin driven xi/adjoint and sigma(E), identical neutral H k_HH(T) `HOLD`. `HH_R10=OFF`.
