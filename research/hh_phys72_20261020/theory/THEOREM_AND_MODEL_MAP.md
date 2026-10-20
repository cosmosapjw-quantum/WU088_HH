# PHYS72: actual exterior operator theorem and implementation map

## Accepted result

For the original atomic exterior problem with `B=27`, `k=7/10`,
`E=49/200 Hartree`, and `eta_C=-10/7`, the actual outgoing Coulomb
Dirichlet Green inverse satisfies

\[
\|r^{-1}R_0^+f\|_{L^2(dr\,d\Omega)}
\le \frac{10+\sqrt{1423}}{189}\|rf\|_{L^2(dr\,d\Omega)}
<\frac{253}{1000}\|rf\|.
\]

This estimate covers every spherical harmonic and the full half-line
`r>=27`. The original noncentral screen gives

\[
\|\sqrt V R_0^+\sqrt V\|\le q=\frac{553311}{10^{26}}<1.
\]

Consequently the exterior Born series converges at `lambda=1`. For
`(ell,p,m)=(21,20,0)`, the sum of orders four and higher obeys

\[
|R_{\ge4}(1)|\le\frac{5929\delta}{2}\frac{q^3}{1-q}
<1.50654\times10^{-80}\,a_0^{-1},\qquad \delta=3\times10^{-23}.
\]

The complete derivation is in
[MULTIPLIER_REMAINDER_DRAFT.md](MULTIPLIER_REMAINDER_DRAFT.md), sections 1–6.
Its historical filename records the parallel derivation stage; the argument
has been accepted after independent review. The exact Green construction,
independent multiplier derivation, density argument, and second all-j kernel
bound are in [GREEN_DERIVATION_DRAFT.md](GREEN_DERIVATION_DRAFT.md).
[SCREEN_ENVELOPE_EXACT.md](SCREEN_ENVELOPE_EXACT.md) closes the original
potential envelope by a finite positive Taylor sum with exact rational
comparison. None of these proofs uses a finite-L constant as an all-j bound.

## Original Hamiltonian and actual Green construction

The atomic Hamiltonian and reduction remain

\[
h=-\tfrac12\Delta-\frac1r-\left(1+\frac1d\right)e^{-2d},\quad
d=|r\mathbf n-\tfrac7{10}\hat z|,
\]
\[
A_\lambda=2h_C-k^2-\lambda V
=-\partial_r^2+J/r^2-2/r-k^2-\lambda V,
\quad V=2(1+1/d)e^{-2d},\quad J=-\Delta_{S^2}.
\]

The radial wave has absorbed the three-dimensional factor `r`; the bulk
measure is `dr dOmega`. There is no extra factor two in `R0` or the Born
terms after this definition. `Z=+u'(B)u(B)^-1`, so physical DtN entries carry
`a0^-1`. Source variables `eta=F y` and `xi=F y-phi` remain separate from
the Coulomb parameter `eta_C=-10/7`.

Write `H_j^+=G_j(eta_C,kr)+i F_j^C(eta_C,kr)` and
`f_j(r)=H_j^+(r)/H_j^+(B)`. If `phi_j(B)=0, phi_j'(B)=1`, then

\[
\mathcal G_j(r,s)=\phi_j(\min\{r,s\})f_j(\max\{r,s\})
=f_j(r)f_j(s)\int_B^{\min\{r,s\}} f_j(t)^{-2}\,dt.
\]

Its derivative jump is `-1`, and `partial_r G_j(B,s)=+f_j(s)`.
It is complex symmetric. Hermitian conjugation belongs to the Hilbert norm
estimates; the inherited Born coefficient integrals retain their complex
bilinear convention. The finite-channel construction extends by density
and agrees with the completed PHYS63 outgoing LAP operator by uniqueness.

The Coulomb conventions and Wronskian are those of
[DLMF 33.2](https://dlmf.nist.gov/33.2). The large-radius phase and amplitude
used in the proof are from [DLMF 33.11](https://dlmf.nist.gov/33.11).
The point diagnostic uses [DLMF 33.4.4](https://dlmf.nist.gov/33.4#E4).

## Why the radial/angular estimate closes

Set `beta=r-B/2`, `w=u'-iku`. The exact identity contains

\[
E=\|w\|^2+B\|u/r\|^2+
\int_B^\infty\frac{r-B}{r^3}\|\nabla_\Omega u\|^2dr
+\frac B2\|u'(B)\|^2.
\]

The outgoing Coulomb asymptotic leaves a nonzero `2||A||^2` term at
infinity. The flux identity `k||A||^2=-Im integral f conjugate(u)` converts
it to the source term. Thus, with `F=||rf||`, `X=||w||`, `W=||u/r||`,

\[
E=2\Re\int f[\beta\overline w+(i/k)\overline u]
\le2FX+(2/k)FW.
\]

Completing the square in `X` proves the displayed resolvent constant.
The angular term is nonnegative for every `j` and vanishes at the
Dirichlet boundary with its actual weight. Also

\[
E\le\frac{5692}{1323}\|rf\|^2.
\]

The rational endpoint is certified by
`27(253/1000)^2-(20/7)(253/1000)-1=37701/7000000>0`.
This is a new explicit estimate for the inherited actual operator; the
qualitative PHYS63 existence claim is reused in its completed state.

## Weighted spaces and every Born order

Let `H_-` have norm `||u/r||`, `H_+` have norm `||rf||`, and `H=L2(dr dOmega)`.
The original multiplication operator satisfies

\[
\|V\|_{H_-\to H_+}\le B^2\delta.
\]

Both `K=R0^+ V` on `H_-` and `S=sqrt(V) R0^+ sqrt(V)` on `H` have norm
at most `q`. No commutation between the noncentral multiplier and angular
momentum is assumed. The factorization
`S=(r sqrt(V))(r^-1 R0^+ r^-1)(r sqrt(V))` is sufficient.

On the boundary use the explicit all-angular space

\[
\|g\|_C^2=\sum_{j,m}C_j^2|g_{jm}|^2,\qquad
C_j=\begin{cases}77,&0\le j\le28,\\
(800/189)(j+1),&j\ge29.\end{cases}
\]

The growing constants are retained. This norm is equivalent to `H1(S2)`;
the natural `H^(1/2)` existence statement remains the earlier PHYS63 result.
For `B_+=sqrt(V)P0^+` and `B_-=sqrt(V)P0^-`,
`||B_+||,||B_-|| <= sqrt(delta/2)` from this boundary space to `H`.
Using the fixed free incoming adjoint gives the holomorphic identity

\[
Z_\lambda-Z_0=\lambda B_-^*(I-\lambda S)^{-1}B_+,
\qquad D_n=B_-^*S^{n-1}B_+.
\]

For any positive integer `N` and `|lambda| q < 1`,

\[
\|R_{\ge N+1}(\lambda)\|_{H_C\to H_C^*}
\le \frac\delta2\frac{|\lambda|^{N+1}q^N}{1-|\lambda|q}.
\]

Multiplication by `C_21 C_20=5929` gives the fixed-entry bound. The
sufficient open radius is the exact fraction `10^26/553311`; membership
must not use an upward-rounded decimal radius. Failure of this sufficient
inequality does not decide actual divergence and is not a strong no-go.

## Concrete VigilODE correspondence

VigilODE PR77/78 study a different reflecting-grid model. Their finite
generator, invariant box, boundary fluxes, row gains, and solver defaults
are not assumptions or constants of this exterior HH theorem. The usable
abstract structure is a residual-to-solution inverse estimate:

| Abstract object | Actual HH realization |
|---|---|
| Equation `T z=b` | `(I-lambda S)z=B_+ g`, `z=sqrt(V)u` |
| Computed residual | `rho >= ||B_+g-(I-lambda S)z_tilde||_H` |
| Inverse control | independently proved `||(I-lambda S)^-1|| <= 1/(1-|lambda|q)` |
| Solution error | `||z-z_tilde||_H <= rho/(1-|lambda|q)` |
| DtN conversion | use the actual `lambda B_-^*` boundary factor if that observable is requested |

`implementation/bounds.py:defect_bound` implements only the same-space
solution bound with a supplied certified residual. No reflecting-grid
constant or unproved residual certification is imported. No new numerical
HH solver is needed to establish the analytic tail in this cycle.

## Formula-to-code map and scientific adoption

| Quantity or rule | Implementation | Acceptance evidence |
|---|---|---|
| Rational `C_*` root witness | `resolvent_quadratic_witness` | exact positive fraction; independent symbolic check |
| `q=C_* B^2 delta` | `Q_UPPER` | exact Fraction and independent scalar audit |
| All-j boundary weight | `c_j(j)` | growing high-j tests; inherited ratio lemma |
| All orders after `N` | `born_remainder_bound` | explicit inverse-minus-polynomial independent reference |
| Minimum sufficient `N` | `minimum_terms` | strict contraction, equality, exhaustion tests |
| Same-space defect error | `defect_bound` | independent contraction-3/4 case |
| Outward displays | `upward_decimal` | directed local Decimal division; exact comparisons |
| D3 plus higher orders | `third_and_higher.py` | three fixed hashes, exact radii, unchanged center |
| Native cross-check | `native/phys72_bounds.f90` | rounded binary128 comparison; exact Python is authoritative |

The completed D3 display already includes printing error. Its exact
decimal center is retained and only the new exact tail is added. The
result encloses `[(Z1-Z0)-D1-D2]_(21,20),m=0`, with exact subtracted
`D1,D2`. A numerical full `DeltaZ` sum requires the earlier `eps1,eps2`
and any new displayed-sum rounding; this cycle does not fabricate that sum.

## Literature relation

PHYS63's stored mapping to Adachi–Itakura–Ito–Skibsted,
[arXiv:1804.07874](https://arxiv.org/abs/1804.07874), supplies the reused
qualitative outgoing operator. E. A. Spence's
[wavenumber-explicit acoustic scattering paper](https://people.bath.ac.uk/eas25/sima_final.pdf)
provides multiplier-method context, not the present attractive-Coulomb
constant or boundary calculation. The explicit shifted identity above is
derived here and independently checked. No literature-priority or novelty
claim is made. Broader search results remain contextual discovery leads.

## Explicit joint radial/angular multiplier action

[ANGULAR_MULTIPLIER_ADDENDUM.md](ANGULAR_MULTIPLIER_ADDENDUM.md) also proves
the original multiplier's action with angular derivatives. Define
`X_-(Y)=L2(r^-2 dr;Y)` and `X_+(Y)=L2(r^2 dr;Y)`. The exact original geometry
gives `|grad_S d|<=7/10`, hence
`|grad_S log V|<=502943/358995<3/2`. The product rule is controlled by a
two-dimensional shear of norm 2. Central spectral commutation then yields:

| Angular space Y | `||V|| X_-(Y) -> X_+(Y)` | `||R0^+V|| X_-(Y) -> X_-(Y)` |
|---|---:|---:|
| `L2(S2)` | `B^2 delta` | `q=5.53311e-21` |
| `H1(S2)` | `2 B^2 delta` | `2q=1.106622e-20` |
| Original `H_C` | `77 B^2 delta` | `77q=4.2604947e-19` |

The last row uses the proved all-j equivalence
`2||g||H1<=||g||C<=77||g||H1`; it retains the growing C_j.
Every row admits lambda=1. The second and third rows concern `R0^+V`,
not a newly asserted H1/H_C norm for the sandwich. The DtN remainder
continues to use the sharper original L2 sandwich q. The additional exact
scalar evaluator and independent review are
`implementation/angular_weights.py` and
`verification/ANGULAR_MULTIPLIER_INDEPENDENT_REVIEW.md`.

Original source-driven `xi`, origin/incoming-adjoint matching, `sigma(E)`
and `k_HH(T)` remain separate obligations in the successor DAG. `HH_R10=OFF`.
