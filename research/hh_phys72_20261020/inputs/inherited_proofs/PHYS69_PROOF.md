# PHYS69: an explicit all-angular second Born enclosure

Date: 2026-10-19 UTC. Independent derivation and sign review:
[INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md). Exact applications:
`../angles/RESULTS.json`. Numerical execution and publication are separate
from the theorems below.

## 1. The fixed object

All coordinates are atomic. Keep B=27, k=7/10, E=49/200 Hartree,
R0=7/10, and

\[
h=-\Delta/2-1/r-(1+1/d)e^{-2d},\quad
d^2=r^2+R_0^2-2rR_0\mu,\quad V=2(1+1/d)e^{-2d}.
\]

For each angular degree j set

\[
H_j(r)=G_j(-10/7,kr)+iF_j^C(-10/7,kr),\quad
f_j(r)=H_j(r)/H_j(B),\quad
\nu_j(r)=k^2+2/r-j(j+1)/r^2.
\]

The Coulomb parameter eta_C=-10/7 is distinct from the original source
eta=Fy and xi=Fy-phi. Derivatives here are with respect to r, so
partial_r=k partial_rho. The DtN convention is Z=+u'(B)u(B)^-1.
The original frozen NPZ is guarded by SHA256
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`.
That guard does not constitute an application of the original driving source.

Let A_lambda=2h_C-k^2-lambda V and write its outgoing boundary map near
lambda=0 as Z_lambda-Z_0=lambda D1+lambda^2 D2+O(lambda^3).
Thus D2=Z''(0)/2. The new quantitative result is entrywise for this
actual all-angular coefficient. It does not assert a numerical radius
of convergence reaching lambda=1 or an all-order nonlinear remainder.

## 2. Identification of the coefficient with the actual boundary map

Reuse the established PHYS63 real-axis Coulomb exterior LAP and Poisson
maps in

\[
\mathcal H_s=L^2([B,\infty),(1+r^2)^sdr;L^2(S^2)),\qquad
X=H^{1/2}(S^2).
\]

In particular R0+=(2h_C-k^2)^-1 maps H1 boundedly to H-1 and P0+
maps X to H-1 and local H1. This resolvent is half the corresponding
physical h_C resolvent. The original screen has
V<=delta exp[-2(r-B)], delta=3e-23; hence

\[
\|V:\mathcal H_{-1}\to\mathcal H_1\|
\le\sup_{r\ge B}(1+r^2)V(r)\le730\delta.
\]

K=R0+ V is bounded on H-1. For |lambda| ||K||<1, the Neumann inverse
defines the actual outgoing Poisson map
P_lambda+=(I-lambda K)^-1 P0+. Local elliptic regularity and the weak
normal trace give analytic Z_lambda:X->X*. No numerical value of ||K||
is required to identify its derivatives at zero. V is a bounded
multiplier, not a compact multiplier. Compactness of K, when needed,
follows from local elliptic smoothing, Rellich compactness and weighted
tail control; it is not needed for this local inverse.

The bilinear boundary identity, equivalently the Hermitian identity
with the incoming Coulomb Poisson adjoint, yields

\[
D_2=(P_0^-)^* V R_0^+ V P_0^+.
\]

The fixed-m polar basis is real and orthonormal. In this basis V_lj^m
is symmetric and the conjugated incoming factor becomes outgoing.
Consequently the radial product below is complex bilinear.

For the j channel of A0=-d^2/dr^2-nu_j, let
w_j(r)=f_j(r) integral_B^r f_j(t)^-2 dt. Then w(B)=0, w'(B)=1,
W(w,f)=-1, and

\[
G_j(s,t)=f_j(s)f_j(t)
\int_B^{\min(s,t)} f_j(r)^{-2}\,dr.
\]

The derivative jump is -1 and partial_s G_j(B,t)=+f_j(t), fixing the
sign for A0 u=lambda V u and Z=+u'(B). With

\[
q_{\ell j}(r)=\int_r^\infty f_\ell(s)f_j(s)V_{\ell j}^m(s)\,ds,
\]

the actual coefficient is

\[
\boxed{(D_2)^m_{\ell p}=\sum_{j=|m|}^\infty\int_B^\infty
q_{\ell j}(r)q_{pj}(r)/f_j(r)^2\,dr.} \tag{1}
\]

Angular projections commute with the central resolvent and converge
strongly in the weighted spaces. Sections 3--5 bound the absolute
triple integral and the angular sum, justifying Fubini and (1).
No extra conjugation, factor two, or radial k enters (1).
The auxiliary Coulomb adjoint used here does not close the separate
original-source incoming-adjoint node.

## 3. All-j Coulomb ratio theorem

For every integer j>=20 and all B<=r<=t<infinity,

\[
\boxed{|H_j(t)/H_j(r)|\le C_j:=\frac{800}{189}(j+1).} \tag{2}
\]

Put a_j=(j-1)/k, R_j=(j+1)/k, Lambda=j(j+1). Exact substitution gives

\[
\nu_j(a_j)=-\frac{7j+91}{100(j-1)^2}<0,\quad
\nu_j(R_j)=\frac{189}{100(j+1)}>0.
\]

Here a_j>B, R_j<Lambda/2, and on r>=R_j,
nu_min=nu_j(R_j)<k^2 and nu_max=k^2+1/Lambda<1/2.
For E_j=|H'|^2+nu|H|^2 use the exact identities
E_j'=nu'|H|^2 and (E_j/nu)'=-nu'|H'|^2/nu^2.
Fixed-j outgoing asymptotics give E_j(infinity)=2k^2.
Since nu'=2(Lambda-r)/r^3, first E_j<=2nu on r>=Lambda,
then E_j<=2nu_max back to R_j. It follows that

\[
|H|^2+|H'/k|^2\le\frac{2\nu_{\max}}{\nu_{\min}}
\le \frac{100(j+1)}{189}\qquad(r\ge R_j).
\]

For Y=(H,H'/k), the forward and backward Euclidean logarithmic norms
are bounded by mu(r)=|Lambda/r^2-2/r|/(2k). On [a_j,R_j] this is
positive and decreasing. Therefore the trace grows by at most

\[
\exp[2\mu(a_j)(R_j-a_j)],\quad
2\mu(a_j)(R_j-a_j)=2+\frac{14j+182}{49(j-1)^2}\le41/20.
\]

For j=n+20, the last inequality has positive polynomial numerator
49n^2+1582n+8449. An exact positive Taylor sum with a geometric
remainder proves exp(41/20)<8. Hence the trace is <=C_j for r>=a_j.

The outgoing Wronskian gives Im(conj(H)H')=k. The real Gram matrix
of (H,H'/k) has determinant one; its eigenvalues therefore belong
to [1/C_j,C_j] wherever that trace bound holds. In particular H
does not vanish on the real positive axis.

On B<=r<=a_j, nu_j(r)<=0. In the backward coordinate x=a_j-r,
the real fundamental solutions A,B0 obey y''=-nu_j(a_j-x)y,
A(0)=1,A'(0)=0,B0(0)=0,B0'(0)=k. Their positive Volterra kernels
give A>=1, B0>=0 and inward-monotone A^2+B0^2. Since
H(r)=A(x)H(a_j)-B0(x)H'(a_j)/k, the fixed Gram bounds at a_j show
|H(t)/H(r)|^2<=C_j^2 for r<=t<=a_j. The two crossing/exterior cases
follow from the trace upper and Gram lower bounds. This proves (2)
for every real r,t in the stated domain. Finite witnesses are code
checks only; no finite angular or radial scan substitutes for this proof.

## 4. Angular analyticity and exact selection

Reuse PHYS67's whole-exterior E10 bound for S=V/2:

\[
|S(r,z)|\le M e^{-2(r-B)},\quad M=1/(4\,10^{19}).
\]

The degree-N Chebyshev projection has real-axis error
(2M/9)10^-N exp[-2(r-B)]. Multiplication by cos(theta) changes
angular degree only by plus or minus one and preserves m. A degree-N
polynomial therefore has zero matrix element between ell and
j>ell+N, for every allowed signed m. Set N=j-ell-1 and use
orthonormality and the multiplier sup norm. Including V=2S once gives

\[
\boxed{|V^m_{\ell j}(r)|\le v_{\ell j}e^{-2(r-B)},\quad
v_{\ell j}=\frac{4M}{9}10^{\ell+1-j},\quad j>\ell.} \tag{3}
\]

There is no channel-count factor and no numerical angular quadrature
in this theorem. Its m coverage includes negative m.

## 5. An explicit infinite angular sum

For fixed external ell,p<=28, reuse Gamma_ext=5929 as a bound on
C_ell C_p. For external degrees up to 64, Gamma_ext=32400 is available.
For j>L>=max(ell,p,19), (2)--(3) imply

\[
\left|q_{\ell j}(r)/f_j(r)\right|
\le C_\ell C_jv_{\ell j}e^{-2(r-B)}/2.
\]

Thus each omitted term in (1), including its absolute triple-integral
form, is at most Gamma_ext C_j^2 v_lj v_pj/16. The factor 1/16 is
(1/2)^2 from the inner integrals times 1/4 from the outer integral.

With x=1/100 the exact infinite sum is

\[
S_L(x)=\sum_{j>L}(j+1)^2x^j
=x^{L+1}\left[\frac{(L+2)^2}{1-x}
+\frac{2(L+2)x}{(1-x)^2}+\frac{x(1+x)}{(1-x)^3}\right].
\]

Consequently

\[
\boxed{|(D_2-D_{2,L})^m_{\ell p}|\le\mathcal A_{\ell p,L}
=\frac{\Gamma_{\rm ext}}{16}\left(\frac{800}{189}\right)^2
\left(\frac{4M}{9}\right)^2 10^{\ell+p+2}S_L(1/100).} \tag{4}
\]

All constants and sums in the implementation use Fraction. The
authoritative records contain exact numerators and denominators;
`upper_decimal` fields round upward. For ell=21,p=20:

| L | Upward rounded angular bound, a0^-1 |
|---:|---:|
| 28 | 7.456541759063896e-49 |
| 35 | 1.134074004678017e-62 |
| 36 | 1.196186052654912e-64 |
| 64 | 3.607608748474182e-120 |

Thus L36 is the smallest implemented cutoff meeting either an angular
budget of 1e-62 or 1e-63. The growing C_j is retained inside the
infinite sum; this is not a uniform Gamma_infinity assertion. The
explicit bound is entrywise, not a computed norm of the full DtN map.

## 6. Reusing L28 and computing only the missing band

At common T=65 replace infinity by T in q and in the outer integral.
Neither V_lj nor f_j depends on the angular cutoff. Therefore

\[
D_{2,36}^T=D_{2,28}^T+B_{29:36}^T,\quad
B_{29:36}^T=\sum_{j=29}^{36}\int_B^T
q_{21,j}^Tq_{20,j}^T/f_j^2\,dr. \tag{5}
\]

Only sixteen new primitive profiles are needed. The completed PHYS68
57 profiles and 76 panels are read by identity, with zero reintegration.
Their certificate SHA256 is
`ddaae206009a276def281af5526851ceb717baf2e0de5f8472552a9db340de9a`.

If z28 and zband are the exact stored dyadic midpoints and e28,eband
their numerical absolute radii, the complete error is

\[
\boxed{|D_{2,\infty}-(z28+z_{\rm band})|
\le e_{28}+e_{\rm band}+\beta_2(\Gamma_{64},65)
+\mathcal A_{21,20,36}.} \tag{6}
\]

Fraction addition of midpoints has zero rounding error. The old
`D2_numerical_absolute_error_l1` supplies e28. Its historical
full-radial radius is not also added. The PR115 beta2 with Gamma64
applies once to the whole finite L36 quantity, and the exact rational
decimal 7.541139e-66 is a verified upward endpoint for it.

The new band integrator uses the unchanged PHYS68 certified Coulomb
Taylor disks, exact angular moment recurrence, reciprocal zero-free
gate, Cauchy remainders, and outward Arb arithmetic. Its numerical
radius includes integration truncation, Coulomb evaluation, angular
coefficient error and roundoff. New code changes only intermediate
coverage and its bound request/receipt chain. A returned local tolerance
from the separate binary64 VigilODE implementation is never inserted
in (6) as a rigorous error certificate.

For a printed complex center rounded to a finite number of decimal
digits, the exact L1 difference from z28+zband must additionally be
included in the displayed radius. Numerical completion of (6), the
fixed 1e-62 goal, native execution, Git publication and backups are
reported by their actual certificates and delivery receipts.

## 7. Source attribution and remaining nodes

Primary conventions: [DLMF 33.2](https://dlmf.nist.gov/33.2) and
[33.11](https://dlmf.nist.gov/33.11). Exact angular recurrence:
[DLMF 14.10](https://dlmf.nist.gov/14.10). Analytic Chebyshev
projection: [Trefethen ATAP chapter 8, Theorems 8.1--8.2](https://github.com/chebfun/ATAP/blob/development/chap8.m).
The accepted hard-core LAP mapping uses
[Adachi--Itakura--Ito--Skibsted, Theorem 1.7 and Corollaries 1.9--1.10](https://arxiv.org/html/1804.07874v1),
with the source-specific PHYS63 mapping preserved in
`inputs/PHYS63_REPORT_KO.md`. The new explicit constants and band
composition are derived here and independently in the review.

PHYS63 all-angular qualitative LAP/Poisson/DtN remains ESTABLISHED_REUSED.
Higher-order all-angular nonlinear remainder, original source-driven
xi, origin and original incoming adjoint, sigma(E), and Maxwellian
k_HH(T) remain distinct research obligations. HH_R10=OFF.
