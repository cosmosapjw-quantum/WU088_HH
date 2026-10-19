# PHYS67: original first-Born D1(21,20), m=0, with numerical enclosure

## Result and exact meaning

For the original atomic model, this unit computes the individual physical
first-Born entry at B=27, k=7/10, E=49/200 Hartree, with Coulomb eta_C=-10/7:

\[
D_{1,21\,20}(27)=\int_{27}^{\infty}
\frac{H^+_{21}(r)}{H^+_{21}(27)}V_{21\,20}(r)
\frac{H^+_{20}(r)}{H^+_{20}(27)}\,dr.
\]

The sign is positive and neither propagator is conjugated. Here
H+=G+iF and Z=+u' u^{-1}; these conventions are inherited from PR114/115.
The approximate value is

\[
D_{1,21\,20}(27)\simeq
(2.7660422459784296+0.4500676730172737i)10^{-24}\ a_0^{-1}.
\]

The authoritative center and rectangle radii are exact dyadic numbers in
FIRST_BORN_CERTIFICATE.json, not the rounded decimal above. Relative to
that exact dyadic center, the validated integration over [27,65] has
complex Euclidean error at most the stored L1 radius

\[
e_{\rm num}=1088277045\,2^{-165}
=2.326966784543533084\ldots\,10^{-41}\ a_0^{-1}.
\]

PR115's analytic omitted radial tail, applied to the two external modes
with L=21, has Gamma21=3364 and a21=2523/(5*10^22). It gives

\[
e_{\rm tail}\le a_{21}e^{-76}
<4.973\,10^{-53}\ a_0^{-1}.
\]

The code uses an outward rational bound on this exponential. The full
infinite-radial value therefore lies within complex distance

\[
e_{\rm num}+e_{\rm tail}<2.328\,10^{-41}\ a_0^{-1}
\]

of the saved exact center. A Cartesian enclosure widened in each
component by the analytic tail is also stored. The numerical tolerance
requested from the integrator is not used as the error certificate;
the measured returned ball radius is the acceptance authority.

## Exact angular integration of the original potential

Let R=7/10, S=(1+1/d)exp(-2d), V=2S and
d=sqrt(r^2+R^2-2rR mu). For m=0 the normalized angular functions are
b_l=sqrt((2l+1)/2)P_l. Thus

\[
V_{ll'}(r)=\sqrt{(2l+1)(2l'+1)}
\int_{-1}^{1}P_l(\mu)P_{l'}(\mu)(1+d^{-1})e^{-2d}\,d\mu.
\]

For real r>R use d as integration variable. Because
dmu=-d dd/(rR), the singular-looking factor (1+1/d) becomes (d+1):

\[
V_{ll'}(r)=\frac{\sqrt{(2l+1)(2l'+1)}}{rR}
\int_{r-R}^{r+R}(d+1)e^{-2d}
P_l\!\left(\frac{r^2+R^2-d^2}{2rR}\right)
P_{l'}\!\left(\frac{r^2+R^2-d^2}{2rR}\right)\,dd.
\]

Set d=r+t, -R<=t<=R. The polynomial argument and prefactor become

\[
\mu=-\frac{t}{R}+\frac{R^2-t^2}{2Rr},\qquad
\frac{d+1}{r}=1+\frac{t+1}{r}.
\]

Expanding the finite Legendre product therefore gives an exact Laurent
polynomial, with no angular quadrature or multipole cutoff:

\[
V_{ll'}(r)=\frac{\sqrt{(2l+1)(2l'+1)}}{R}
e^{-2r}\sum_{j=0}^{l+l'+1}C_jr^{-j}.
\]

Each C_j is an exact rational combination of exp(2R) and exp(-2R).
The required elementary moments follow by differentiating a finite
antiderivative:

\[
M_n=\int_{-R}^Rt^ne^{-2t}\,dt
=A_n(-R)e^{2R}-A_n(R)e^{-2R},\qquad
A_n(t)=\sum_{s=0}^{n}\frac{n!\,t^{n-s}}{(n-s)!2^{s+1}}.
\]

The implementation computes all rational coefficients exactly, then
encloses the exponential constants and their cancellations at 1024-bit
precision. In particular, the tiny physical entry is not obtained by
subtracting two unbounded binary64 approximations.

Both the original angular integral and the Laurent formula are
holomorphic for Re(r)>R. For real mu in [-1,1], d^2 factors as
(r-R exp(i theta))(r-R exp(-i theta)), mu=cos(theta); its zeros lie on
|r|=R. The branch continued from positive real r is analytic on that
simply connected right half-plane. Equivalently if Im(r) is nonzero,
Im(d^2)=2 Im(r)(Re(r)-R mu) is nonzero, so d^2 avoids the negative real
axis; for real r>R, d^2>0. The identity theorem consequently licenses
the Laurent expression on the complex test balls used by the radial
integrator. The callback explicitly requires Re(r)>R for the entire
ball and returns an indeterminate value if this cannot be established.

## Validated radial integral and retained analytic tail

The outgoing Coulomb helper evaluates H+ with exact rational k and eta_C
using Acb. H_l(27) and H_l'(27) in the two denominator factors are
computed once as balls; neither contains zero. The prime on l' here
denotes the second angular index, not a radial derivative.

The implementation applies FLINT/Arb's validated complex quadrature to
ten panels of width at most four on [27,65]. Arb's integration algorithm
uses adaptive subdivision and analytic complex bounds with Gaussian
quadrature; see Johansson (2018), arXiv:1802.07942, and the official
acb_calc documentation. All evaluations, exponential and Coulomb
values, divisions, products and summations retain ball arithmetic
roundoff. The angular coefficients retain their 1024-bit enclosure
while the adaptive radial integration uses 256 bits.

The success request specifies abs_goal=1e-40, rel_goal=1e-22,
eval_limit=5000 per panel, depth_limit=30 and deg_limit=100. The
internal absolute budget is goal/(8*number_of_panels); the factor eight
reserves room for Cartesian-to-complex bounds and conservative radius
inflation. The final reported L1 radius, independently recovered from
the exact serialization, is less than the requested goal.

The omitted [65,infinity) contribution is covered by the already proved
PR115 beta1. No Coulomb ratio premise for ell>64 is introduced. The
bound at L=21 suffices because the integrand contains only the two
external Coulomb modes and this one exact potential element.

## Executed attempts and independent checks

The first attempt used abs_goal=1e-40, rel_goal=1e-18 and the original
per-panel absolute allocation. It returned a finite containing ball
after 3,143 evaluations and 8.63665 seconds, but its actual complex
radius exceeded the requested goal. FIRST_BORN_CERTIFICATE_ATTEMPT01.json
and its request are preserved. This is a resolved numerical-budget
failure, not evidence that the integral or model is ill defined.

The second attempt tightened the relative budget and the per-panel
absolute allocation. It succeeded after 3,269 evaluations in 7.68404
seconds with zero analytic-domain rejections. The Python process exited
0. No PHYS64 campaign or completed PHYS66 pilot was rerun.

The 22 new focused tests pass. They check the physical s-wave closed
antiderivative at three radii, two independent validated direct mu
integrals, high-order symmetric bilinearity on a complex radius, the
analytic guard, exact subnormal dyadic serialization, source tamper and
request boundaries, and one small new-kernel radial integration.

Two independent reviews accept the stated scope. A separately
implemented Legendre three-term recurrence plus integration-by-parts
moment recurrence checks five exact rational coefficient pairs,
including (21,20,27) and (21,20,65), with exact equality. Its script and
result are under ../coulomb/FIRST_BORN_INDEPENDENT_CHECK.json. The
angular scope and analytic continuation review is under
../angular/INDEPENDENT_SCOPE_REVIEW.md. These checks are distinct from
the actual adaptive radial integration receipt.

## Reuse of the completed PHYS66 pilot

The earlier package's PILOT_L28_T65.npz contains the stored complex128
physical contribution (order1,ell21,ellprime20). Its binary64 bits are
read exactly as rational numbers. Comparing this point with the new
full-radial rectangle proves

\[
1.514\,10^{-36}<
|\widehat D_{1,21\,20}^{\rm pilot}-D_{1,21\,20}|
<1.516\,10^{-36}\quad(a_0^{-1}).
\]

For each Cartesian component, the comparison computes the exact
distance from the stored rational point to the dyadic interval; the
square-root lower and upper bounds are then rounded outward. The
input NPZ, JSON and new certificate SHA256 identities are in
EXISTING_PILOT_COMPARISON.json. This closes the actual total error of
that one stored result without attributing its error to separate
quadrature, Coulomb, ODE or floating matrix sources. It makes no error
claim for the pilot's D2 or D3 entries.

## Scientific scope and next obligation

D1 has no intermediate angular sum. Its (21,20),m=0 entry is identical
in every finite projection containing those modes and is the same
entry of the unrestricted first forcing. This is the exact meaning of
all_angular_first_order_entry=true. D2 and higher terms do contain
intermediate sums; their excluded-angular response remains open.

This unit certifies one first-Born term, not the full nonlinear DtN
entry. In particular, a finite-L higher-Born majorant can exceed this
small individual D1, so no relative-accuracy statement for the full
nonlinear physical response follows. The source-driven xi=Fy-phi,
origin regularity and incoming adjoint matching, sigma(E) and
Maxwellian k_HH(T) remain separate unsolved obligations. PHYS63's
qualitative all-angular LAP/Poisson/DtN existence remains established.
The original frozen1386 complex128 source SHA is preserved and
HH_R10 remains OFF.

Reproduction uses scripts/phys67_first_born_certificate.py with
FIRST_BORN_REQUEST.json. Its default request is the successful one;
it refuses an existing output path so the completed certificate is
not silently overwritten. Read and reuse the stored certificate unless
a changed scientific obligation specifically requires another run.

Primary references: https://dlmf.nist.gov/33.2;
https://arxiv.org/abs/1802.07942;
https://flintlib.org/doc/acb_calc.html.
