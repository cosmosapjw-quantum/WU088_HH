# Primary-source and formula audit

Searches: SciSpace and Exa were actually invoked during PHYS22 before interruption. Main selected reference: Arnold Neumaier, *Global, rigorous and realistic bounds for the solution of dissipative differential equations. Part I: Theory*, Computing52(1994)315–336; author manuscript March1993, https://arnold-neumaier.at/ms/ode.pdf. Read the explicit first-exit/tube and mean-value interval conditions of Theorems3.5 and4.1. The present proof is written out for the selected diagonal-absorption gas–photon system. No claim of a new general comparison principle.

Wolfram official `Interval` documentation: https://reference.wolfram.com/language/ref/Interval.html, accessed2026-10-13. Approximate interval operations round lower limits down and upper limits up. v3 encloses transcendental operations using 40-digit Interval objects, then converts endpoints to outward exact decimal-grid rationals. Python Fraction independently verifies the remaining comparison algebra. The official arithmetic contract is an implementation assumption, not a substitute for the source-formula audit.

The author PDF text was read. Web screenshot attempts returned a cache-miss error; no claim in this package depends on a graph or table from that failed screenshot.

## Source map at receiver a5c958c414dea41216b445c05f58df837f05cacb

- `ft03_rates.rs`: H/He RR coefficients and logarithmic slopes; CI coefficients and their T derivatives agree with v3 real-decimal expressions.
- `ft03_controlled.rs`: two DR amplitudes and the 11605-K energy conversion; captured kinetic power is the source-matched RR moment kB T alpha(3/2+dlnalpha/dlnT); the second derivative term in its T derivative is retained.
- `axisym_conditional.rs`: event stoichiometry, explicit source owners, excess photon heating, threshold energy and proper/reference-volume/SI conversion. HH is absent in the fixed baseline and appears as the optional additive nu*q in this mathematical comparison.
- `background.py`: expanding dust+Lambda LRS Bianchi-I, monotone H, s/H bound and all ray energies enclosed by the exponential envelope. Density normalization nh0 is frozen from the chosen input.
- `hm12_data.py`: nonnegative ordinate interpolation in log energy and z, duplicate wavelength rows retain jumps; source upper bounds enclose all enclosing rows/columns. Source s_i uses emissivity rather than the UVB intensity.
- `atomic_provider.rs`: the three Verner cross-section fits and <=50000 eV domain. All 2904 fixed modes are retained; the time energy enclosure has zero opacity-threshold crossings for all three absorbers.

## Full derivative and comparison map

A is D_g(a+B*m) at fixed photon m and time, with all CI/RR/DR/PI and thermal terms. B=D_m F_g. C=-diag(m)D_g kappa. The exact finite photon difference is damped by K(g_lambda), not by a linearized signed generator. B and kappa are affine in gas, and positive majorants cover the common convex domain.

This inspection is same-assistant mathematical/source review. The Fraction checker treats the saved A+, B+C+ and tube-flow majorants as supplied interval inputs; it is not an independent implementation of all Wolfram interval operations.
