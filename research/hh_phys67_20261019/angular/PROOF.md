# PHYS67: exact angular Gauss error for the original finite-L screen

Date: 2026-10-19.  Status: derived; exact arithmetic and bounded independent
checks executed.  This note closes the ideal Gauss angular quadrature
component for the original finite projection.  Publication and provider
backup are recorded by the parent work unit after their actual completion.

## 1. Object, normalization and retained premises

Use the original atomic coordinates, B=27, R=7/10, k=7/10 and
E=49/200 Hartree.  The Hamiltonian is h=-Delta/2-1/r-S and the radial
Schrodinger equation contains the screened multiplication V=2S, where

\[
 d(r,\mu)=\sqrt{r^2+R^2-2rR\mu},\qquad
 S(r,\mu)=(1+d^{-1})e^{-2d},\qquad -1\le\mu\le1.
\]

Here r and d are numerical radii in Bohr units.  The reported V bound is
the numerical coefficient of the physical radial equation in a0^-2.
The field notation eta=Fy, xi=Fy-phi and Coulomb eta_C=-10/7 is retained;
none is redefined by the angular variable mu.

The original NPZ identity remains
f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
The producer actually hashes the 21,029-byte source file before emitting
the certificate.  The source values are not used as a replacement for a
proof of the analytic geometry.

We reuse PHYS58's proved E_10 ellipse and M=1/(4*10^19) screen majorant.
The published premise can be read at commit
445d82db9c42b4f2f81e4ac1b107dec3b69b3c24,
research/hh_phys58_20261016/r5/REPORT_KO.md, blob
588e372698029c302d93e774d593e6966a51ab8b.  Its exact implementation is
src/wu088_hh/phys58_screen_multipoles.py.  No earlier spectrum, LAP or
PHYS64 campaign is recalculated here.

For a fixed signed m and a finite set |m|<=ell<=L<=64 define

\[
 b_\ell^m(\mu)=
 \sqrt{\frac{2\ell+1}{2}\frac{(\ell-|m|)!}{(\ell+|m|)!}}
 \mathsf P_\ell^{|m|}(\mu),\qquad
 \int_{-1}^1 b_\ell^m b_{\ell'}^m\,d\mu=\delta_{\ell\ell'}.
\]

This is the convention used by AngularScreen in
src/wu088_hh/phys63_scaled_riccati.py.  The azimuthal integral has already
been performed exactly.  Axisymmetry conserves m, and the negative-m
block is unitarily equivalent to the positive-m block.  See DLMF
[14.7.8](https://dlmf.nist.gov/14.7.E8) and
[14.17.6](https://dlmf.nist.gov/14.17.E6).

Let V_L(r) be the exact Galerkin multiplication matrix.  For Q exact
Gauss-Legendre nodes x_q and positive weights w_q define the ideal matrix

\[
 [V_{L,Q}(r)]_{\ell\ell'}=
 \sum_{q=1}^{Q}w_q b_\ell^m(x_q)V(r,x_q)b_{\ell'}^m(x_q).
\]

The ideal nodes, weights, functions and products in this definition are
mathematical exact values.  The implemented f64 matrix is another object
whose evaluation error is retained as an open component.

## 2. Weighted analytic screen majorant on the whole exterior

The ellipse E_10 has maximal real coordinate 101/20.  For its interior
and boundary,

\[
 \Re d^2\ge q(r):=r^2-\frac{707}{100}r+\frac{49}{100},
\]

and the exact identity

\[
 q(r)-(r-4)^2=\frac{93r-1551}{100}
 \ge\frac{48}{5}>0,\qquad r\ge27
\]

shows that d^2 stays in the open right half-plane.  Thus its principal
square root is holomorphic throughout the ellipse.  For a complex
number z with positive real part,
(Re sqrt(z))^2=(|z|+Re z)/2>=Re z.  Consequently

\[
 \Re d>r-4=23+(r-27),\qquad |d|\ge\Re d>23.
\]

It follows that

\[
 |S(r,z)|\le\frac{24}{23}e^{-46}e^{-2(r-27)}
 <M e^{-2(r-27)}.
\]

The last strict inequality is the inherited exact rational gate:
sum_(j=0)^46 46^j/j! > 5*10^19 and (24/23)/(5*10^19)<M.
PHYS58 stated the corresponding uniform unweighted majorant.  The
positive linear gap above supplies the new exponentially weighted form.

## 3. Polynomial approximation and the exact Gauss sampling isometry

For a fixed radius write S_N for the degree-N Chebyshev projection of S.
The Cauchy coefficient estimate on E_10 gives
|c_n|<=2M exp[-2(r-27)] 10^-n for n>=1.  Summing the geometric remainder
and using |T_n(mu)|<=1 gives

\[
 \|S-S_N\|_\infty
 \le \tau_N^{\rm Ch}e^{-2(r-27)},\qquad
 \tau_N^{\rm Ch}=\frac{2M}{9}10^{-N}.
\]

This is the projection estimate in Trefethen's
[Theorems 8.1 and 8.2, equation (8.2)](https://github.com/chebfun/ATAP/blob/development/chap8.m).
The comparison polynomial is used only in the proof; no sampled
Chebyshev interpolant is substituted into the physical solver.

For completeness, the coefficient estimate follows directly by setting
F(w)=S((w+w^-1)/2).  Its symmetric Laurent series has equal coefficients
at powers n and -n.  A Cauchy integral on |w|=10 bounds each Laurent
coefficient by M exp[-2(r-27)] 10^-n, and combining the pair into T_n
supplies the factor two.  Summing n>N yields the displayed remainder.

Rodrigues' formula gives

\[
 b_\ell^m b_{\ell'}^m
 =C_{\ell\ell'm}(1-\mu^2)^{|m|}
 \frac{d^{|m|}P_\ell}{d\mu^{|m|}}
 \frac{d^{|m|}P_{\ell'}}{d\mu^{|m|}}.
\]

Although an individual odd-|m| associated Legendre function contains a
square root, this product is a polynomial of degree ell+ell'<=2L.
Thus, when Q>=L+1, exactness of the Gauss rule through degree 2Q-1 gives

\[
 A^\dagger A=I,\qquad A_{q\ell}=\sqrt{w_q}\,b_\ell^m(x_q).
\]

Positivity and degree-2Q-1 exactness are stated in
[DLMF 3.5(v), equations 3.5.18--3.5.20_2](https://dlmf.nist.gov/3.5#v).
For a scalar remainder f, the exact multiplication and sampled
multiplication are therefore both contractions relative to its sup norm:

\[
 \|P_L M_fP_L\|_2\le\|f\|_\infty,\qquad
 \|A^\dagger\operatorname{diag}(f(x_q))A\|_2\le\|f\|_\infty.
\]

There is no factor depending on the number of ell or m channels.

## 4. All-signed-m finite-L quadrature theorem

Take any integer N>=0 satisfying 2L+N<=2Q-1.  With p_N=2S_N, every
entry b_ell p_N b_ell' is integrated exactly.  Splitting V=p_N+(V-p_N)
and applying the two preceding norm estimates yields

\[
 \boxed{\quad
 \|V_L(r)-V_{L,Q}(r)\|_2
 \le\epsilon_{LQ}e^{-2(r-27)},\qquad
 \epsilon_{LQ}=\frac{8M}{9}10^{-N},\qquad
 N=2Q-1-2L.\quad}
\]

The factor four multiplying the S remainder is the product of the
V=2S factor and the sum of the exact-integral and discrete residuals.
Taking the direct sum over signed m preserves this same operator bound.
Restricting to an arbitrary subset of the included ell channels is also
contractive.  The full ell<=L projection has (L+1)^2 channels, but this
dimension does not multiply epsilon_LQ.

Alternatively, PHYS58's exact Legendre remainder gives the valid bound
4*legendre_tail_upper(N).  Its ratio to the Chebyshev coefficient is
(180N+290)/81.  Both are carried in the machine result to expose the
normalization and selection-degree comparison.

At L=64, Q=128, N=127,

\[
 \epsilon_{64,128}=\frac{2}{9\,10^{146}}
 =2.222222\ldots\times10^{-147}\quad(a_0^{-2}),
\]

whereas the inherited Legendre route gives an outward value
6.35116598079561042524006e-145.  For AngularScreen.scaled, divide by
3e-23; the exact-rule component is at most
7.40740740740740740740741e-125 exp[-2(r-27)].

The theorem's criterion excludes L=64,Q=64.  This is the domain of this
specific certificate; it does not assert that every other bound at that
node count is impossible.  The existing Q=128 campaign lies inside the
proved criterion and is not rerun.

## 5. Computation, validation and remaining error components

The new module is src/wu088_hh/phys67_angular_certificate.py.  It uses
Fraction throughout the bound, rejects inadmissible degree/quantum
numbers, reuses the original source guard and writes rational-hex-v1.
The outward Decimal display keeps Q=256 and Q=512 coefficients positive
even below binary64's range.  RESULTS.json binds exact tested source
file hashes and contains L=64,Q=65/80/96/128/192/256/512 plus L=28,Q=128.

Actual focused tests: 25 passed, pytest exit 0, 0.67 seconds.  Independent
exact checks use SymPy on the Q=3 algebraic nodes and rational weights,
the normalized L=2 associated basis for every m=-2,...,2, and an actual
degree-one screen.  The polynomial integral and Gauss matrix are exactly
equal; the discrete Gram is exactly the identity.  The exterior gap is
verified as a polynomial identity, and serialization and source tamper
paths are exercised.  These checks accompany the analytic proof above.

The producer exited 0 in 3.22 seconds.  At L=4,Q=12 and r=27,39 it used
90-digit independent angular integration and a separately computed
Gauss rule for m=0,1,4; signed-m equality follows from the preserved
axisymmetric convention.  All six operator-norm differences lie inside
their analytic bound.  The largest residual/bound ratio is
0.0005052957646387370596353993.  These finite precision numerical
witnesses are marked separately from the rational analytic certificate.

The actual f64 AngularScreen sampling Gram at L=64,Q=128 has measured
2-norm defects 9.0880673e-12 (m=0), 1.5983101e-12 (m=1),
7.8885021e-14 (m=32), and 3.5083048e-14 (m=64).  This independently
shows that the stored floating sampling operator is not the exact
isometry used in the theorem.  These defects are diagnostics, not error
enclosures for the physical matrix.  Increasing Q cannot by itself
certify floating point nodes, weights, associated basis, potential or
matrix arithmetic.

This certificate therefore supplies no bound for floating point evaluation
or matrix roundoff, radial integration, Coulomb evaluation, or the excluded
angular response.  These remain separate components; other PHYS67 units
can certify their own stated scopes without altering this ideal-Gauss
theorem.  The present result is a finite-L multiplication-input certificate
for subsequent response error propagation.  It does not fill the physical source-driven xi,
regular-origin/incoming-adjoint, sigma(E) or Maxwellian k_HH(T) nodes.
PHYS63 qualitative all-angular LAP/Poisson/DtN remains closed;
HH_R10 remains OFF.  Actual radial-solver and NCP runs in this unit: zero.

## 6. Reproduction and provenance

From the repository root, with numpy, scipy, mpmath, sympy and pytest:

```bash
PYTHONPATH=src python -m pytest -q tests/test_phys67_angular_certificate.py
python research/hh_phys67_20261019/angular/produce.py --source research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz --output /tmp/phys67-angular-results.json --independent-checks
```

FOCUSED_EXECUTION.json and PRODUCER_EXECUTION.json contain the actual
current-host commands, elapsed times and exit codes.  This source-specific
application reuses established Gauss/Chebyshev and spherical-harmonic
facts; it makes no new general approximation-theory or no-go claim.
The original finite-L and source assumptions have not changed.
