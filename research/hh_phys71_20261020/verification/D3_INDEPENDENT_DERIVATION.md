# PHYS71 independent finite-D3 derivation and analytic-panel review

Review date: 2026-10-20 UTC. Reviewer: a separate agent from the producer.
Current core status: **PASS_SCOPED_DERIVATION_AND_CORE_UNIT_DISCRIMINANTS**.
The independently written eight new unit methods all passed on their first
execution in 1.978 seconds (process wall 2.16443 seconds). Exact source and
AST bindings are in `D3_CORE_INDEPENDENT_REVIEW.json`; raw output is retained
in `D3_CORE_TESTS_01.*`. These tests execute no real HH panel, Coulomb
evaluation or completed Volterra trajectory. Campaign/aggregate acceptance
is a separate later review, not inferred from this core result.
This review neither recomputes the completed PHYS68/69 profiles nor changes
their certificates. The current PHYS70 optimized D2 trajectories are not replayed.

## 1. Green identity, sign, coefficient and finite-cutoff domain

In the original atomic convention set `A0=-d²/dr²-QC`,
`QC_j=k²+2/r-j(j+1)/r²`, `V=2(1+1/d) exp(-2d)`, and
`f_j=H_j^+(r)/H_j^+(B)`. The inherited outgoing choice is `H+=G+i F_C`
and the boundary derivative is `Z=+u' u^-1`. Retain `B=27`, `k=7/10`,
`E=49/200`, `etaC=-10/7`, `R=7/10` and `HH_R10=OFF`.

For `w_j(r)=f_j(r) int_B^r f_j(s)^(-2) ds`, the Wronskian
`W(w_j,f_j)=-1`. Therefore

\[
G_j(r,t)=f_j(r)f_j(t)\int_B^{\min(r,t)}f_j(s)^{-2}\,ds
\]

has derivative jump `-1` and is the Dirichlet outgoing inverse kernel of
`A0`. Its boundary derivative is `partial_r G_j(B,t)=+f_j(t)`.

The original perturbation equation is `A0 u=lambda V u`, so the
Poisson series has **positive** powers of `R0 V`. The coefficient of
`lambda³` in the boundary map is

\[
D_3=(P_0^-)^* V R_0^+ V R_0^+ V P_0^+.
\]

This is `Z'''(0)/6`, without another numerical factor. In the real fixed-m
basis, reciprocity is transpose symmetry of `G_j` and `V_jk`. The incoming
Poisson adjoint converts to the outgoing left factor. Hence the resulting
fixed-entry formula is bilinear, with **no complex conjugation**.

For the cutoff screen `V^T=1_[B,T] V`, define the already computed profiles

\[
q_{aj}^T(s)=\int_s^T f_a(t)f_j(t)V_{aj}(t)\,dt,\qquad B\le s\le T.
\]

Fubini in the finite sum and compact radial triangle gives

\[
U_{aj}(r):=(R_{0,j}^+ V_{ja}^T f_a)(r)
=f_j(r)P_{aj}(r),\qquad
P_{aj}(r)=\int_B^r\frac{q_{aj}^T(s)}{f_j(s)^2}\,ds .
\]

The exact finite-cutoff, finite-L coefficient is consequently

\[
\boxed{(D_{3,L}^T)_{ab}=
\int_B^T\sum_{j,k=0}^{L} U_{aj}(r)V_{jk}(r)U_{bk}(r)\,dr.}
\]

This identity requires all ordered internal pairs `(j,k)`, including the
diagonal and off-diagonal couplings. It requires only the two external
first-Born rows, not the full first-Born matrix or newly integrated D2.
At `r>T`, the physical cutoff source vanishes and `P` stays constant;
no integral there contributes because the middle multiplier is `V^T=0`.
At a complex Cauchy disk crossing `T`, the analytic continuation is instead
the primitive of the original uncut kernel. It agrees with the physical
profile on `[B,T]`; imposing a Heaviside cutoff in that disk is invalid.

## 2. Forward carry and Cauchy remainder

Let a panel be `[c-h,c+h]`, with `0<h<rho`, and let the inherited saved
`q_center` be a complete ball containing the exact `q^T(c)` for this
physical request. Regenerate only its nonconstant coefficients from
`q'=-K`, `K=f_a f_j V_aj`, using the unchanged enclosing kernels:

\[
q_0=q^T(c),\qquad q_{n+1}=-K_n/(n+1).
\]

This is coefficient reconstruction; it does not redo the old backward
profile integral. The old center uncertainty must remain in `q_0`.

Assume the saved `Mq` bounds the same analytic `q^T` on `|z-c|<=rho`,
and a strictly positive recomputed or inherited zero-free lower bound
`m_j` holds there for `f_j`. Then

\[
S_{aj}=q_{aj}^T/f_j^2,\qquad M_{S,aj}=M_{q,aj}/m_j^2
\]

is an analytic majorant. Each coefficient through degree N is enclosed
by truncated series division: terms above N cannot affect those terms.
Set `E_S=M_S (h/rho)^(N+1)/(1-h/rho)`. If `P_left` contains the exact
forward carry at `c-h`, use

\[
P_0=P_{\rm left}+\int_{-h}^{0}\sum_{n=0}^N S_n x^n\,dx
+\text{disk}(h E_S),
\]

\[
P_{\rm right}=P_{\rm left}+\int_{-h}^{h}\sum_{n=0}^N S_nx^n\,dx
+\text{disk}(2h E_S).
\]

The nonconstant local coefficients obey `P_(n+1)=S_n/(n+1)`.
`P(B)=0` initializes the first panel. Computing the right carry directly
from the left avoids unnecessary duplication of half-panel uncertainty.
Independent interval operations lose correlations but retain inclusion.

For any point in the radius-rho disk, the straight segment from `-h`
has length at most `rho+h` and remains in the convex disk. Therefore

\[
M_{P,aj}=|P_{\rm left}|_{\rm upper}+(\rho+h)M_{S,aj},
\qquad M_{U,aj}=M_{f,j}(\rho)M_{P,aj}
\]

are valid. The proposed use of the **left**, not the right, carry matches
the forward primitive. The old `q` carry remains backward-defined; these
opposite carry directions are consistent because the q profiles are
already fixed functions.

The normalized-angular-entry majorant `Mv` then implies

\[
M_I=M_V\left(\sum_j M_{U,aj}\right)
           \left(\sum_k M_{U,bk}\right).
\]

The degree-N polynomial panel integral encloses the full analytic integral
after an additional error disk

\[
2h M_I\frac{(h/\rho)^{N+1}}{1-h/\rho}.
\]

No angular quadrature or radial grid interpolation enters this bound.
All majorants, lower bounds and coefficient arithmetic must use outward
balls. Disk errors added to both Cartesian radii are containing boxes;
the reported scalar absolute error must then use an enclosing L1 or
Euclidean box radius. A printed center needs its own rounding budget.

## 3. Polar contraction and the factor of two

In the normalized polar basis
`phi_j(mu)=sqrt((2j+1)/2) P_j(mu)`, set

\[
A(r,\mu)=\sum_j\sqrt{2j+1}\,U_{aj}(r)P_j(\mu),\qquad
B(r,\mu)=\sum_k\sqrt{2k+1}\,U_{bk}(r)P_k(\mu).
\]

The contraction is

\[
I(r)=\int_{-1}^1 A(r,\mu)B(r,\mu)(1+1/d)e^{-2d}\,d\mu.
\]

Here the two `1/sqrt(2)` basis factors cancel the physical `2` in V.
With `t=d-r`, one has

\[
\mu=-t/R+(R^2-t^2)/(2Rr),\qquad
(1+1/d)|d\mu|=R^{-1}[1+(t+1)/r]\,dt.
\]

Thus, if `A B=sum_n C_n(r) mu^n` and the existing exact monomial
Laurent pairs are `(A_nk,B_nk)`, then

\[
\boxed{I(r)=\frac{e^{-2r}}{R}\sum_n C_n(r)
 \sum_k\big(A_{nk}e^{2R}+B_{nk}e^{-2R}\big)r^{-k}.}
\]

There is no extra factor two, angular dimension factor or factorial.
Every radial coefficient through N can be computed by finite series
convolution and the exact Fraction angular coefficients. Precision used
for canceling monomial Laurent constants is separate from the ordinary
radial series working precision and must be recorded. The result remains
an enclosure if cancellation widens it; a tolerance claim requires the
actual final ball to pass.

## 4. Exact manufactured discriminant

For a single channel with `f=1`, `V=kappa` on an interval of length L,

\[
q(x)=\kappa(L-x),\quad
P(x)=\kappa(Lx-x^2/2),\quad
D_3=\frac{2\kappa^3L^5}{15}.
\]

Independently the exact boundary map is
`sqrt(lambda*kappa) tan(sqrt(lambda*kappa)*L)` whose cubic coefficient is
the same. Taking `kappa=i` makes D3 negative imaginary and detects an
incorrect conjugation; the coefficient `2/15` detects a factor/factorial
mistake. This is a test of the algebra, not a replacement for the HH model.
For a constant complex symmetric matrix C and `f_j=1`, the corresponding
matrix check is `D3=2 L^5 C^3/15`, including every ordered cross coupling.

## 5. Scope and implementation acceptance items

The derivation is accepted subject to the stated analytic and data-binding
premises. Implementation review must still check:

1. Both old campaigns are read by their exact saved certificate/request/
   panel hashes; their two rows cover every j=0..36 once with no omission.
2. Saved centers and majorants are restored as containing exact dyadic balls;
   endpoint text is never silently parsed through binary64.
3. New profile reconstruction uses the same normalized Coulomb and V kernels,
   with complete old center uncertainty and saved rho-domain majorants.
4. The P carry is forward from B and preserves full uncertainty in every panel.
5. The full ordered angular contraction is retained and normalization matches
   Section3; complex conjugation is absent.
6. Every reciprocal disk gate and Cauchy truncation error is retained;
   only actual achieved bounds can close numerical acceptance.
7. Finite-L radial error `beta3(Gamma64,T65)` is added exactly once. Its use is
   valid for the L36 subspace; it does not bound omitted angular modes.
8. An independently proved D3 omitted-angular bound is added separately.
   The inherited D2 angular bound is not a D3 bound.
9. Higher-order nonlinear remainder, actual source-driven xi and physical
   rates retain separate obligations unless separately established.
10. Tests, real D3 panels, old-profile reuse, publication, backups and NCP
    submissions are counted separately. No old D1/D2 trajectory is rerun.

The Green identity uses the inherited PHYS69 proof and PHYS63 existence
result. Analytic Taylor and Cauchy estimates use the inherited validated
PHYS68 proof. This independent calculation introduces no strong no-go
claim and does not reopen established qualitative existence.
