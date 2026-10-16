# WU088_HH PHYS61 C5–C8: rigorous all-angular complex-energy Born remainder, source-original complex Coulomb radial/angular witness

## Original and strict scope

Parent science: WU088_HH PHYS61 R5 source `6c8f854dd2ba89c72c5730b848e37b7b85580cc1` stacked on PHYS60 PR104. Exact original Hamiltonian `h=-Δ/2 -1/r -(1+1/s)e^-2s`, `s=|x-(7/10)zhat|`, k²=49/100, original eta=Fy, xi=Fy-phi unchanged. Original 1386 complex128 NPZ SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d` was rehashed in sandbox.

Spectral energy here is **complex** `z=+49/200 +i/100 Hartree`. Set `tau=2Im z=1/50`. Physical real-energy *on-shell outgoing* `z=+49/200+i0` remains OPEN. No physical source/rate admission (`HH_R10=OFF`). All operator norm proofs retain full original off-centre angular `V=2S`, all ell,m, all radial r>=27. Numerical first Born samples use finite radial/angular grids only and are NONCERTIFYING.

## New C5 theorem: rigorous first Born remainder as all-angular X→X* operator

From R5, original Coulomb zero-boundary `G_C(z)` is bounded by `1/tau`, and 

`||P_C(z)||_(X->L²) < C_P=224285/1944`, `||V|| <delta=3e-23`, `q=delta/tau=1.5e-21<1`.

The actual noncentral Poisson map is `P_S=(I-G_C V)^-1 P_C`. Using the complex **bilinear transpose** (not conjugate) in Green's identity,

`D := Z_S(z)-Z_C(z) = P_C(z)^T V(I-G_C(z)V)^-1 P_C(z)`.

Let genuine all-angular first Born `D1=P_C^T V P_C`. The exact identity is

`D-D1=P_C^T V G_C V(I-G_C V)^-1 P_C`.

It includes all intermediate P-Q angular multi-hop paths, not a 2×2 approximation. Consequently the exact source-scope rational upper

`||D-D1||_(X→X*) <=delta C_P² q/(1-q) < 6e-40`.

For an **unnormalized** boundary matrix entry `ell20,m0 → ell21,m0`, Cauchy with `||Y_ell,m||_X=sqrt(ell+1)` gives `sqrt(21*22)<22`, hence

`|(D-D1)_(21,20)| <22*(6e-40)=1.32e-38`.

This is rigorous at fixed complex z. It is **not** an interval certificate of any numerical quadrature of D1. No tau↓0-uniformity is present because C_P~1/tau; no physical on-shell sigma(E) claim.

### Finite-domain Born omitted radial tail independent rigorous bound

For the entire original screen and *any* angular g,h, the omitted `r>=39` portion of `D1` obeys

`||D1_(r>=39)||_(X→X*) <=delta C_P² exp[-24] < 2e-29`.

The strict inequality uses the exact positive rational Taylor **lower** for `exp(24)` through order80, not floating exponential approximation. This is possible here only because R5 actually proved C_P for tau>0. Individual unnormalized ell20→ell21 raw tail `<22*(2e-29)=4.4e-28`. It improves the previous PHYS60 note that a screen multiplier tail **alone** was not an operator Born tail bound; however it is still too conservative to serve as sub-ppm quadrature convergence enclosure.

## Actual C5–C8 noncertifying original-source numerical experiment

Choose the analytic **upper-half-plane** Coulomb wavenumber `k_z=sqrt(49/100+i/50)` branch with `Im k_z>0`, Sommerfeld parameter `eta_z=-1/k_z`, outgoing Coulomb `H_l^+(eta_z,k_z r)=G_l+iF_l`, normalized `p_l(B)=1`. The original `V_21,20,m(r)` is the direct `2(1+1/s)e^-2s` displaced angular integral using normalized associated Legendre harmonics, with full m↔-m symmetry. It is real/symmetric and not centered.

The complex first Born sample is `D1_21,20(m;r≤39)=int_{27}^{39} dr p_21(r)V_21,20,m(r)p_20(r)` (no conjugation). Independent GL radial/angular refinement: (10×64),(14×96),(20×128),(28×192). Final values (approximate):

| m | Re D1 on [27,39] | Im D1 on [27,39] |
|---|---:|---:|
| 0 | 2.6923117268322988e-24 | 4.676676030302345e-25 |
| 1 | 2.687774700721683e-24 | 4.668797758037447e-25 |
| 2 | 2.674166648723211e-24 | 4.645168139479028e-25 |

All values are *floating quadrature witnesses*. A certified numerical inclusion would still require angular/radial quadrature remainders; the all-angular operator Born remainder and outer radial tail bounds above are different errors.

Independent local flux test at complex energy uses the exact Coulomb recurrence DLMF §33.4.4 for `p_l'`, and direct `mpmath` numerical quadrature of `|p_l|²`:

`J(B)-J(31)=tau∫_B^31 |p_l|²dr`, `J=Im(conj(p_l)*p_l')`.

Relative residuals: ell0 `9.78e-17`, ell20 `2.55e-16`, ell21 `3.60e-16`. Importantly this is **absorption**, not conserved real-energy current: J(r) decreases as r increases for tau>0. This sign is compatible with `Im Z(z)>0` at B and is distinct from PHYS60's real-energy constant J.

## Execution, first failure and optimization

- First full producer (four grids plus three radial flux identities) exceeded execution timeout, with no receipt. Diagnosed repeated evaluation of expensive CoulombH functions for identical radial nodes/m=0,1,2 and numerical differentiation `mp.diff` at ell20/21.
- Replaced `mp.diff` with mathematically equivalent DLMF 33.4.4 exact Coulomb derivative recurrence and added memoization for identical (`ell,r,dps`) calls. Independently checked the recurrence against `mp.diff` at ell0 to ~1e-36 without changing physics or any numerical tolerance. A bounded repair episode; no blind repeated long command.
- New C5–C8 focused pytest **16/16 PASS**, producer actual exit0, R5 focused 19 PASS. Combined 35-test run PASS and actual command/exit/resource recorded in `results/`.
- Connected Wolfram exact independent rational Born remainder <6e-40 and outer Born tail <2e-29 **PASS** after an initial syntax error (caught and fixed). Wolfram is a connector, not a local wolframscript calculation.
- Original full WU suite/NCP jobs/native subagents NOT_RUN. No sibling REI/HE/CR mutation.

## DAG

R5 **PROVED_UPPER_HALF_PLANE_ALL_ANGULAR**; C5–C8 **PROVED_RATIONAL_BORN_ERROR_AND_NUMERIC_WITNESS**, ready for bounded use only at z=49/200+i/100; PHYS62 real-energy tau↓0 outgoing Coulomb LAP/Poisson and true full off-centre screened `Z_S^+(k²/2)` **OPEN**. Physical low/high driven `xi=Fy-phi`, regular origin, incoming adjoint, sigma(E), identical-neutral-H Maxwellian k_HH(T) **HOLD**, REI `HH_R10=OFF`. NCP not needed this time; a true angle/radius grid of full source-driven positive-energy scattering would need a separate input and resource contract.

Literature: DLMF §33.4.4 for derivative recurrence, DLMF §33.8 for Coulomb CF context; Martin arXiv:1510.03543 and Ito–Skibsted arXiv:1804.07874 for on-shell LAP background, not a certificate that the tau→0 original H-H problem is solved.
