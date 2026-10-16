# PHYS58 R5: off-centre screened exterior exact angular multipoles and uniform high-angular transfer

## Frozen science and accepted scope

Parent: WU088_HH PHYS57B Draft PR #98, HEAD `b6d95a931f596876eb2097b08fdb16ac542f9364`.  No prior owner or sibling repo edit. This is a new physical **screened exterior multiplier** result, not a claim of the screened **outgoing Dirichlet-to-Neumann map**.

Original atomic-unit spectator model:

\[
h=-\tfrac12\Delta-\tfrac1r-(1+s^{-1})e^{-2s},\quad
s=|\boldsymbol r-R\hat z|,\ R=7/10,\quad
\eta=Fy,\ \xi=Fy-\phi,\ \kappa=7/10.
\]

Original 1,386 complex128 source NPZ SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d` extracted and independently re-hashed from the preserved verified PHYS57B capsule. No original physical exterior trial/incoming source invented.

## R5 theorem 1: exact angular representation, strict positivity of Legendre multipoles

For all `r>=27 Bohr`, let `z=cos(theta)` and `s(z)=sqrt(r²+R²-2rR z)`. Expand the *actual* original `S` as

\[
S(r,z)=\sum_{n=0}^\infty A_n(r)P_n(z),\quad
A_n(r)=\frac{2n+1}{2}\int_{-1}^{1}(1+s^{-1})e^{-2s}P_n(z)\,dz.
\]

Substitute `s` as the integration coordinate to obtain a **finite polynomial-exponential integral for every n**:

\[
A_n(r)=\frac{2n+1}{2rR}\int_{r-R}^{r+R}
(s+1)e^{-2s}P_n\!\left(\frac{r^2+R^2-s^2}{2rR}\right)ds.
\]

This is exactly computable as rational endpoint polynomials times `exp[-2(r±R)]` when r,R are rational, with no phenomenological approximation or spherical quadrature.

Proof that **all exact `A_n(r)>0` for all n>=0**: at μ=2, the two positive heat/Laplace representations are

\[
\frac{e^{-\mu s}}s=\frac1{\sqrt\pi}\int_0^\infty t^{-1/2}e^{-t s^2-\mu^2/(4t)}dt,
\quad e^{-\mu s}=\frac\mu{2\sqrt\pi}\int_0^\infty t^{-3/2}e^{-t s^2-\mu^2/(4t)}dt.
\]

After `s²=r²+R²-2rRt z`, the angular factor `exp(2rRt z)` has expansion `sum_n (2n+1)i_n(2rRt) P_n(z)`, with the normalized modified spherical-Bessel `i_n(x)>0` at every `x>0`. Every factor of the resulting coefficient integrand is strictly positive. Smooth separated geometry `r>R` allows uniform convergence/termwise projection.

Reference background: Yukawa addition theorem and FMM multipole method, Huang–Jia–Zhang, Comput. Phys. Commun. DOI 10.1016/j.cpc.2009.06.028; related 2005/2006 Yukawa one-range addition theorems surfaced in SciSpace. The exact source-specific specialization and bound here are direct derivations, not novel claims about general special functions.

## R5 theorem 2: explicit infinite-angular geometric tail on the entire exterior

Use Bernstein ellipse `rho=10` in the complex `z`-plane, whose maximal real part is `101/20`. Then for all `r>=27`,

\[
\Re(s(z)^2)\ge r^2+R^2-2rR\frac{101}{20}
\ge\frac{2693}{5}>23^2.
\]

The principal square root is holomorphic in and on this ellipse, with `Re s>23` and `|s|>23`. Consequently `|S| <= (24/23)e^-46 < 1/(4*10^19)=:M`, uniformly in `r>=27`. The strict second inequality is fully **rationally certified** by `sum_{j=0}^{46} 46^j/j! > 5*10^19` and `(24/23)/(5*10^19) < M`.

By Bernstein/Trefethen's analytic Chebyshev degree n-1 truncation error and orthogonality of `P_n` against all polynomials of degree less than n, for every `n>=1` we get

\[
0<A_n(r)\le\frac{20M}{9}(2n+1)10^{-n}.
\]

For `N>=0` define `S_N=sum_{n=0}^N A_n P_n`. Then, pointwise on the full exterior and in `L²(S²)` angular multiplication-operator norm,

\[
\Vert S-S_N\Vert_{\infty}
\le\frac{20M}{9}\,10^{-(N+1)}
\left[\frac{2N+3}{1-1/10}+\frac{2/10}{(1-1/10)^2}\right].
\]

This is a uniform **all-n/all-m** theorem from analytic geometry, not a sampled truncation test. At N=8, for the original Schrödinger matrix potential `V=2S`,

\[
2\|S-S_8\|_\infty
\le \boxed{\frac{173}{729\cdot10^{26}}\simeq 2.373113854595336\times10^{-27}}.
\]

The multiplication of harmonics by `P_n` conserves m and obeys the exact Gaunt selection triangle inequality, `|ell-ell'|<=n`. Thus **without truncating the angular Hilbert space**,

\[
\boxed{\|Q_{\ell\ge21+N}\,2S\,P_{\ell\le20}\|_{L²(S²)\to L²(S²)}
\le2\|S-S_N\|_\infty\quad \forall r\ge27.}
\]

In particular `ell>=29` receives direct low-channel coupling bounded by `2.373114e-27` in original atomic radial operator convention. This is a **direct multiplication** transfer estimate: high modes 21..28 can still convey indirect multi-hop effects, and a propagated exterior high-block Schur/resolvent bound has **not** been obtained. Do not substitute this number for `||Z_S-Z_C||`.

## Correct scientific significance and reuse

PHYS47 earlier derived an analytic high-angular *radially integrated* source bound by Bernstein expansion; this PHYS58 result is complementary and source-specific: a simple positive exact elementary multipole representation, a uniform **pointwise-in-r exterior** operator bound, and ready-to-use deterministic Gaunt/Legendre band coupling selection. No claim of novelty over general Yukawa addition theorems. It creates an angularly certified input for the still-open PHYS58 actual noncentral screened exterior DtN, weighted outgoing Coulomb LAP, Poisson trace estimates, and full P-Q Feshbach Schur matching.

`HH_R10=OFF`. Do not equate REI/H/He native photo-source rate or BASS_HE/bass_cr chemistry with this microscopic H-H scattering potential.

## Verification / evidence

`src/wu088_hh/phys58_screen_multipoles.py` is source-gated and all bounds use exact `fractions.Fraction`. `tests/test_phys58_screen_multipoles.py` exercises original NPZ SHA, ellipse geometry, positive Taylor partial sum, explicit coefficient and tail formulas, low/high angular selection, reproducibility, tampered-input rejection. Connected Wolfram exact checks give `min_Re_s²=2693/5`, Taylor order46 strict PASS and `N8 V-tail=173/(729*10^26)` exactly, `PASS=True`. Wolfram monopole `A0=(-146+139 exp(14/5))/(378 exp(277/5))` provides an independent exact first coefficient check.

Tests and result producer were executed in the **isolated ChatGPT sandbox**, not NCP/owner desktop. `pytest` result bound to committed files only once source has been published. Native subagents absent (`NOT_RUN`). Full WU project regression `NOT_RUN`. No physical `xi`, `sigma(E)` or Maxwellian `k_HH(T)` admission.
