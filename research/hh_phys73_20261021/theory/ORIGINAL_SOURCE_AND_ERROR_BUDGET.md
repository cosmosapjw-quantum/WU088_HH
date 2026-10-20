# PHYS73: original driven exterior source and explicit error components

## Result

The original source equation reduces, at lambda=1, to

\[
 (A_0-V)u=V\chi,\qquad u=r\xi,\quad
 \chi=r\phi=\frac{r e^{-r}}{\sqrt\pi}.             \tag{1}
\]

This gives an executable outgoing, zero-Dirichlet exterior particular
solution using the fast Green application. An explicit Bernstein-ellipse
bound controls every omitted angular mode of this source; an exponential
moment controls its radial tail; the completed PHYS72 contraction controls
the source Born tail. At L=64, outer radius T=44 and one exact source Born
term, these analytic components sum to at most

\[
 4.918263356868373\,10^{-53}
\]

in X- norm. This number is a continuum analytic-component bound. The
finite-grid preparation and native sweep retain their separate quadrature,
special-function and arithmetic errors. The numerical grid is not declared
certified by this number.

## 1. Original variable and source mapping

Readback sources are PHYS36 REPORT_KO.md, PHYS44 REPORT_KO.md,
src/wu088_hh/phys33_coupled_source.py and phys33_coupled_preview.py. They
preserve F=exp(lambda exp(-d)), eta=F y=phi+lambda xi, and the transformed
equation equivalent to

\[
 (\Delta+k^2+2/r+\lambda V)\eta=(1+k^2)\phi.
\]

Since (Delta+k^2+2/r)phi=(1+k^2)phi, subtraction at lambda=1 gives
(Delta+k^2+2/r+V)xi=-V phi. Multiplication by -r yields (1).
Thus the sign and the V=2(1+1/d)e^(-2d) factor are fixed by the original
Hamiltonian. The Coulomb parameter eta_C=-10/7 is a separate symbol.

Let g=u(B). For the actual matched solution,

\[
 u=P_0^+g+R_0^+V(\chi+u),
\]
\[
 z=\sqrt V(\chi+u),\quad b_0=\sqrt V\chi,\quad
 (I-S)z=b_0+B_+g,\quad u=P_0^+g+R_0^+\sqrt V z,  \tag{2}
\]

where S=sqrt(V)R0+sqrt(V) and B+=sqrt(V)P0+. For g=0 this is the unique
outgoing zero-Dirichlet particular solution u_p=R1+(V chi). Formula (2)
identifies the remaining boundary input rather than guessing it from a
finite source array. The frozen NPZ ends at r=20 and is an interpolated
y-state on its inherited interior panels. It is not a physical u(27)
trace or an exterior radial source. Its SHA remains
f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.

The new particular problem uses the known original analytic forcing and
g=0. The matched g, regular origin, incoming adjoint, sigma(E) and thermal
rate retain their separate obligations. HH_R10 remains OFF.

With Y_j0=sqrt((2j+1)/(4pi)) P_j(mu), the reduced source coefficient is

\[
 f_{j0}(r)=r e^{-r}\sqrt{2j+1}
             \int_{-1}^1 V(r,\mu)P_j(\mu)\,d\mu,\qquad
 f_{jm}=0\ (m\ne0).                              \tag{3}
\]

This fixes the angular normalization used by the Python preparation. The
default preparation evaluates this exact moment using the analytic
Yukawa formula in `ANALYTIC_SCREEN_SOURCE.md`. The radial quadrature
weights are subsequently inserted once in x_i=w_i f_j(r_i).

## 2. Continuum inverse and source Born tail

Use the same PHYS72 spaces X+=L2(r^2 dr dOmega), X-=L2(r^(-2) dr dOmega)
for reduced radial states. Their norms are ||rf|| and ||u/r||. The
unchanged rational constants are

\[
 c=253/1000,\quad \delta=3\,10^{-23},\quad
 M=B^2\delta,\quad q=cM=553311/10^{26}<1.
\]

The exact outgoing inverse satisfies ||R0+||_(X+->X-)<=c and
K=R0+V has ||K||_(X-->X-)<=q. Therefore

\[
 u_p=\sum_{n=0}^\infty K^nR_0^+ f,\quad f=V\chi,
\]
\[
 \|u_p-u_N\|_-\le \|R_0^+f\|_-\frac{q^N}{1-q},
 \quad u_N=\sum_{n=0}^{N-1}K^nR_0^+f.             \tag{4}
\]

For any outgoing zero-trace reconstructed approximation v whose *continuous*
strong residual f-(A0-V)v lies in X+, the actual inverse gives

\[
 \|u_p-v\|_-\le\frac{c}{1-q}\|f-(A_0-V)v\|_+.    \tag{5}
\]

A residual vector of a finite quadrature matrix is not the continuous
residual in (5). A point-source Nyström reconstruction has distributional
sources; it cannot be assigned an X+ strong residual by reading the matrix
residual. Product integration or another specified reconstruction must
supply the norm and its error bound before (5) is used numerically.

## 3. Source norm and radial tail

The original screen satisfies V(r,mu)<=delta exp[-2(r-B)]. Define

\[
 I_4(T)=\int_0^\infty(T+t)^4e^{-6t}\,dt
 =\frac{T^4}{6}+\frac{T^3}{9}+\frac{T^2}{18}
   +\frac{T}{54}+\frac1{324}.                     \tag{6}
\]

The angular measure is 4pi and |phi|^2=e^(-2r)/pi. Consequently

\[
 \|f\|_+^2\le4\delta^2 e^{-2B}I_4(B),
 \qquad \|b_0\|^2\le\delta e^{-2B}
                (B^2+B/2+1/8).                   \tag{7}
\]

The latter polynomial is 5941/8 at B=27. The factorization through
sqrt(V) also gives ||R0+f||_-<=c sqrt(M)||b0||; the smaller of this and
c||f||_+ is a valid first-application bound.

For T>=B,

\[
 \|\mathbf1_{r>T}f\|_+^2
 \le4\delta^2 e^{-(6T-4B)}I_4(T).                 \tag{8}
\]

Equations (6)--(8) involve only elementary scalar moments. They require no
reintegration of the completed PHYS71 panels or inherited profiles.

## 4. Explicit infinite-angular source tail

Use the Bernstein ellipse E_8 in the complex mu-plane, whose real
semimajor axis is 65/16. The principal square root of
d^2=r^2+(7/10)^2-2r(7/10)mu is analytic there, because

\[
 \Re d^2\ge r^2+(7/10)^2-2r(7/10)(65/16)>0.
\]

At B the right side is 230371/400>23^2. If s(r) is its positive square
root, then s'(r)=(r-(7/10)(65/16))/s(r)>1 for r>=B; the numerator is
positive and its square exceeds s(r)^2. Hence Re d>=s(r)>23+r-B.
Also |d|>=s(r). Throughout the ellipse,

\[
 |V(r,\mu)|\le\frac{48}{23}e^{-46}e^{-2(r-B)}
 <\delta_8e^{-2(r-B)},\qquad \delta_8=3\,10^{-20}. \tag{9}
\]

The final strict comparison is certified in source_budget.py by
48/[23 S_128(46)]<delta8, where S_128 is a positive exact rational
partial sum of exp(46). Since S_128(46)<exp(46), this proves (9) in the
correct direction.

The standard contour argument for Chebyshev coefficients gives a
degree-L polynomial p_L with

\[
 \sup_{[-1,1]}|V-p_L|
 \le\frac{2\delta_8}{7}\,8^{-L}e^{-2(r-B)}.       \tag{10}
\]

One can obtain (10) directly by moving the Joukowsky-contour integral to
|z|=8, obtaining coefficient bounds 2 M 8^(-n), then summing n>L.
This is Theorems 8.1--8.2 of Trefethen's *Approximation Theory and
Approximation Practice*. The orthogonal Legendre projector P_L is the
best L2([-1,1]) polynomial approximation, so its error is no larger than
that of p_L. Restoring the azimuthal integral and chi gives

\[
 \|Q_L f\|_+^2\le
 \frac{16\delta_8^2}{49}\,8^{-2L}e^{-2B}I_4(B).  \tag{11}
\]

This is a bound on the full omitted source, including every j>L. It uses
neither a supremum of growing C_j nor a finite-L Gamma64 replacement. The
source is special: its orbital chi is isotropic and its screen is analytic
well beyond the real angular interval at r>=27. Equation (11) is not a
general angular-tail claim for arbitrary boundary data.

For ideal Q-point Gauss--Legendre quadrature, one can separately bound the
mathematical coefficient quadrature. If 2Q-1>=L, approximate V in (3) by
a degree 2Q-1-j Chebyshev polynomial. The product with P_j is integrated
exactly by Gauss quadrature. Positivity, total weight two and |P_j|<=1
then give coefficient error

\[
 |\Delta f_{j0}(r)|\le\frac{8\delta_8}{7}
 r e^{-r-2(r-B)}\sqrt{2j+1}\,8^{-(2Q-1-j)}.       \tag{12}
\]

Squaring (12), summing j<=L and integrating with r^2 dr bounds the ideal
angular quadrature in X+. Actual rounded nodes, weights, exponentials and
Legendre recurrence add their own errors. This applies to the optional
Gauss comparator. The default analytic Yukawa multipoles have no angular
quadrature truncation error for retained modes; their floating Bessel and
arithmetic errors still require a separate bound before certification.

## 5. Combined statement and executable budget

Let f_LT=P_L 1_[B,T] f and use N exact continuum Born applications to
f_LT. The source omission is at most eps_rad+eps_ang in X+. By the
finite geometric inverse bound and (4), define the universal first-action
majorant

\[
 A_* = \min\{c F_*,\;c\sqrt M\,b_*\},
 \quad F_*\ge\|f\|_+,\quad b_*\ge\|b_0\|.
\]

It bounds both ||R0 f||_- and ||R0 f_LT||_-. For the second assertion,
R0 commutes with the angular projector P_L, which is contractive in X-,
and the radial indicator commutes with sqrt(V). Therefore
R0 P_L 1_[B,T] f=P_L R0 sqrt(V) 1_[B,T] b0, and its norm is at most
c sqrt(M) b_*. The ordinary X+ bound also gives c F_*. No commutation
between P_L and the noncentral V is assumed. Hence

\[
 \|u_p-u_{N,LT}\|_-
 \le\frac{c}{1-q}(\epsilon_{rad}+\epsilon_{ang})
       +A_*\frac{q^N}{1-q}.                       \tag{13}
\]

For N>1 this statement uses the full K at subsequent steps. Replacing K
by a finite angular multiplier additionally needs its operator defect.
For the N=1 pilot there is no subsequent multiplication, so this extra
term is absent. If a validated implementation supplies an additional
X- error eps_num relative to u_(N,LT), the right side of (13) plus eps_num
is the complete particular-solution error. A sampled grid difference alone
does not supply eps_num.

The stdlib-only implementation/source_budget.py verifies the PHYS72
bounds.py SHA before loading its constants. Every exponential upper is a
positive-Taylor rational; every square-root upper is checked by exact
integer squaring; decimal displays round upward. It rejects float/bool
inputs for rational parameters and writes output with create-only mode.

At L64,T44,N1 the actual saved exact evaluation is
verification/SOURCE_BUDGET_L64_T44_N1.json:

| Component | Upper bound |
|---|---:|
| ||f||_(X+) | 3.398182960240250e-32 |
| ||u_p||_(X-) | 8.597402889407831e-33 |
| Source Born tail after first term, X- | 4.757037590141137e-53 |
| r>44 source, X+ | 6.372559949693160e-54 |
| j>64 source, X+ | 1.546747939001964e-87 |
| Source omissions after inverse, X- | 1.612257667272370e-54 |
| Sum of analytic components, X- | 4.918263356868373e-53 |

The theory selects a short first-application diagnostic because the
all-order correction is already explicitly bounded. It does not require
a new Born panel campaign to exercise the NCP cores.

### Primary approximation reference

L. N. Trefethen, *Approximation Theory and Approximation Practice*,
Chapter 8, Theorems 8.1--8.2. The author-maintained executable book source
was read through Exa:
https://github.com/chebfun/ATAP/blob/development/chap8.m

The elementary contour argument and all HH-specific constants used here
are written above; no foreign model's coefficient or error constant is used.
