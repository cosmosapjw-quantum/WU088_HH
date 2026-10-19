# PHYS68: cached exact angular kernels and their Taylor coefficients

## Model and scope

Use the original atomic-coordinate Hamiltonian and the radial-equation
potential

\[
V(r,\mu)=2(1+d^{-1})e^{-2d},\qquad
d^2=r^2+R^2-2rR\mu,\qquad R=7/10.
\]

Radii are numerical values in units of a0 and V has units a0^-2.
The normalized m=0 angular basis is
e_l(mu)=sqrt((2l+1)/2)P_l(mu), with its ordinary real bilinear matrix
element V_lp=int[-1,1] e_l V e_p dmu. The full field is not projected
to a different Hamiltonian. Each selected angular matrix element is
integrated exactly; finite-L truncation in subsequent products is a
separate obligation. No conjugation is introduced in the analytic r
continuation.

This unit changes coefficient preparation and constructs finite Taylor
coefficient enclosures. It does not compute D1/D2 radial integrals,
source-driven xi, a complete scattering solution, or a rate.

## Exact factorization by angular monomials

For real r>R, put d=r+t. Then -R<=t<=R and

\[
\mu=-t/R+(R^2-t^2)/(2Rr),\qquad
-d\mu=(r+t)/(rR)\,dt.
\]

The factors 2 from the physical V and 1/2 from the two normalized
angular basis functions give

\[
V_{lp}(r)=\frac{\sqrt{(2l+1)(2p+1)}}R e^{-2r}
\int_{-R}^{R}e^{-2t}P_l(\mu)P_p(\mu)
\left(1+\frac{t+1}r\right)dt.
\]

Write P_l(mu)P_p(mu)=sum_j p_j mu^j with exact rational p_j. Define
J_j(r) as the preceding integral with that product replaced by mu^j.
The exact binomial expansion is

\[
\mu^j=\sum_{k=0}^{j}\sum_{s=0}^{k}
\binom jk\binom ks
\frac{(-1/R)^{j-k}}{(2R)^k}
R^{2(k-s)}(-1)^s t^{j-k+2s}r^{-k}.
\]

For n=j-k+2s, each term contributes its factor times M_n to r^-k
and its factor times (M_n+M_(n+1)) to r^-(k+1), where

\[
M_n=\int_{-R}^{R}t^n e^{-2t}dt
 =A_n(-R)e^{2R}-A_n(R)e^{-2R},
\quad
A_n(t)=\sum_{s=0}^{n}\frac{n!t^{n-s}}{(n-s)!2^{s+1}}.
\]

Consequently J_j(r)=sum_(k=0)^(j+1)
(A_jk exp(2R)+B_jk exp(-2R))r^-k, with exact Fraction endpoint
pairs. The final pair is the exact linear combination

\[
(A_{lp,k},B_{lp,k})=\sum_j p_j(A_{jk},B_{jk}).
\]

PHYS67 repeated the same monomial construction inside each pair.
PHYS68 computes each J_j once, for lazily requested j in 0..128,
then combines it linearly. The physical formula and all rational
coefficients remain identical. Symmetric requests share the key
(min(l,p),max(l,p)); this is matrix symmetry, not Hermitian symmetry.

For largest polynomial degree D and P requested pairs, the number of
Fraction operations is reduced from roughly O(P D^3) to
O(D^3+P D^2), ignoring the varying integer bit lengths. This is an
operation-count statement, not a universal time or memory bound.
The cache holds at most 129 monomials and 512 angular-pair entries;
the complete symmetric L28 block has 435 pairs and fits this bound.
The constant ball cache is separately bounded by 512 entries and its
key includes precision_bits.

## Taylor coefficient arithmetic

For an exact real center c>R and N>=0, use the formal series r=c+x
modulo x^(N+1). Evaluate 1/r by series inversion, the Laurent polynomial
by Horner evaluation, and exp(-2r) by FLINT's acb_series exponential.
The product with sqrt((2l+1)(2p+1))/R returns balls containing

\[
v_n=\frac1{n!}\left.\frac{d^n V_{lp}}{dr^n}\right|_{r=c},
\qquad 0\le n\le N.
\]

Every exact rational coefficient is converted to an arb ball and
exp(+-2R) is enclosed at coefficient_bits. Endpoint cancellation is
retained in those balls. The Taylor operations then run at
precision_bits<=coefficient_bits. No floating-point input is silently
converted to a claimed exact center. Finite output alone is not a
relative-accuracy gate; downstream consumers retain all returned radii.

In python-flint, acb_series.prec counts known coefficients and ctx.cap
is the global upper series order. The implementation sets both to
N+1, then returns a plain tuple of the N+1 acb coefficients. It restores
ctx.cap in finally and uses ctx.workprec for arithmetic precision.
The public API documents that different FLINT contexts must not be
run concurrently in separate Python threads; separate processes keep
independent contexts. See the primary documentation:

- https://python-flint.readthedocs.io/en/latest/acb_series.html
- https://python-flint.readthedocs.io/en/latest/general.html

The installed python-flint 0.8.0 API was also directly probed: constructor
prec, inv, exp, indexing and exact upper endpoints behaved as documented.

## A rigorous complex-disk majorant

Let c,s be exact real numbers with s>=0 and a=c-s-R>0. For any r=x+iy
in |r-c|<=s and real mu in [-1,1], put u=x-R mu>0 and
v=R^2(1-mu^2)>=0. Then d^2=(u+iy)^2+v. Its imaginary part is 2uy,
so this expression never meets the principal square-root cut: it is
nonreal if y!=0 and positive if y=0.

Write d=A+iB with A>0. The equations A^2-B^2=u^2-y^2+v and
AB=uy imply that X=A^2 is the nonnegative root of

\[
f(X)=X^2-(u^2-y^2+v)X-u^2y^2=0.
\]

Since f(u^2)=-vu^2<=0, its nonnegative root obeys A^2>=u^2.
Thus Re(d)>=u>=x-R>=a and |d|>=a. It follows throughout the disk that

\[
|V(r,\mu)|\le M_V(c,s)
 =2(1+a^{-1})e^{-2a}.
\]

The normalized basis has unit L2 norm. Cauchy--Schwarz gives
int |e_l e_p|<=1, so |V_lp(r)|<=M_V. More generally every finite
orthogonal angular compression has operator norm <=M_V. No channel
count is multiplied into this bound. All arithmetic in M_V is ball
arithmetic and the function returns its upward, exact arb endpoint.

For s>0 and 0<=h<s, Cauchy's coefficient estimate gives, for |x|<=h,

\[
\left|V_{lp}(c+x)-\sum_{n=0}^N v_nx^n\right|
\le M_V\frac{(h/s)^{N+1}}{1-h/s}.
\]

This is the analytic truncation component only. Horner evaluation of
the returned coefficient balls propagates coefficient and arithmetic
uncertainty separately. The implementation does not drop those radii.
For fixed h/s<1 the bound tends to zero as N increases; for h=0 it is
exactly zero. The disk condition is strict, so the closed Cauchy circle
has a surrounding analytic neighborhood. The bound has units a0^-2;
the numerical ratio h/s is dimensionless.

## Actual verification and preparation

The new focused tests passed 35/35 in 0.87 s. They include exact
Fraction equality to the existing formula for (21,20) and (20,28),
an independent elementary l=p=0 formula at new radii 29,61/2,73,
an independent finite-binomial formula for Taylor coefficients,
real and complex subpoints with the proved Cauchy remainder, whole-ball
domain checks, context restoration and rejection of invalid inputs.
The original test process is recorded in TEST_EXECUTION.json; it was
not repeated merely to create a log file.

Two fresh child processes prepared the 57 unique pairs required by
rows l=20,21 with j=0..28. Their exact coefficient hashes all agreed.
The measured exact preparation times were 6.375268320 s for the old
per-pair construction and 0.702180275 s for the shared monomials, a
single observed ratio of 9.079. Both timings include identical canonical
Fraction serialization and SHA256 work. The fresh-process policy prevents an
already filled cache from being timed as the cold preparation.

The optimized process then actually prepared 57 degree-24 Taylor
expansions at c=61/2 with 384/1024 bits, totaling 1425 finite coefficient
balls in 0.053534 s. These are angular coefficients, not D1 or D2
solutions. The full 435-pair L28 exact coefficient block was constructed
in another 0.818195 s with the row cache already populated. That latter
time is explicitly a warm extension. PREPARATION_RESULT.json and the
two phase output files preserve values, hashes and scopes.

No PHYS64/66 campaign, completed PHYS67 integration or NCP solver was
rerun. PHYS63's qualitative existence and the original source/proofs
remain unchanged. HH_R10 stays OFF.
