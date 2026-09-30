# Wide-strip scalar radial and Boys evaluation

Scope: the same frozen two-electron HH matrix integrands. No ionic polynomial,
Gaussian exponent, phase, finite basis, or quadrature weight is changed.
`radial_wide.cpp` and `analytic_wide.cpp` are isolated replacements for their
reviewed parent source; both are needed. `create_sources.py` records parent hashes.

## 1. Exact scalar representation and derivatives

For completed-square variance v>0, squared complex displacement s, and x=s/(2v),

M_p(v,s) = (2v)^(p/2) Gamma((p+3)/2)/Gamma(3/2)
             * 1F1(-p/2;3/2;-x), p=-1,...,8.

The j-th s derivative is obtained analytically by the rising-factorial identity

d_s^j M_p = C_p (-1/(2v))^j (-p/2)_j/(3/2)_j
             * 1F1(j-p/2;3/2+j;-x), j=0,1,2.

Even nonnegative p terminate as exact polynomials before rounding. Odd moments
can share Boys functions F_n(x)=integral_0^1 t^(2n) exp(-x t²)dt. The existing
polynomials A_k,B_k give M_(2k-1)=sqrt(2/pi)v^(k-1/2)[A_k F_0+B_k exp(-x)].
Their first and second derivatives use F'_n=-F_(n+1), retaining the same physical
Cartesian covariance derivatives needed by the weak kinetic matrix. No finite
difference enters this backend. This transfers C21's compatible principle of
analytic derivatives of the actual finite representation, without importing its
one-electron H2+ Hamiltonian or dilation family into the HH model.

## 2. Failure mechanism and stable new sector

The old finite domain was |Im x|<=2. Merely enlarging its guard is incorrect.
The recorded initial trial with binary128 hypergeometric seeds but the old
longdouble F_9-to-F_0 downward recurrence had normalized error 6.49296e-13 near
x=-31.9i. The multiplier 2x/(2n+1) amplifies a rounded high-order seed and each
subtractive step. `INITIAL_FAILURE.json` records this failure.

For 2<|Im x|<=32 and Re x<64 the new method evaluates each required Boys order
independently:

F_n = 1F1(n+1/2;n+3/2;-x)/(2n+1), Re x<0;
F_n = exp(-x) 1F1(1;n+3/2;x)/(2n+1), Re x>=0.

The latter is the exact Kummer transformation. Radial shared Boys orders 0..2
likewise use independent seeds in the new strip. All series recurrence arithmetic,
including every ratio of half-integer coefficients, uses IEEE binary128 basic
operations. Casting coefficients from a prior longdouble division would lose the
benefit under cancellation and is deliberately avoided. Compensated summation
and conversion only after the series has converged control the actual observed
roundoff. Transcendental prefactors and final fields remain longdouble. Neither
`quadmath` special functions nor a runtime precision change is required.

For term k, subsequent series ratios are bounded in the complex l1 norm by

q = (|Re z|+|Im z|)/(k+1) max(1,(k+a)/(k+b)), once k+a>0.

The rational factor either decreases to 1 or is bounded by 1. Hence for q<1 the
exact-arithmetic remaining series is at most norm1(term_k) q/(1-q). The code stops
only below eps_binary128*norm1(sum)/8, or rejects after 1024 terms. This proves the
series truncation test in exact arithmetic. It is not a formal interval proof of
all floating-point operations: the separate exact-input mp100 controls measure
roundoff, with mp150 cross-checks and independent defining-integral quadrature.

The |Im x|<=2 path is unchanged, including its arithmetic order. The full inherited
1,408-case radial registry is bitwise equal for all requested orders 0,1,2; the
sampled old-domain Boys results are separately checked. No threshold was widened.

## 3. Large positive real part

For a=Re x>=64 the complete-Gamma representation is retained:
C_0=sqrt(pi)/(2sqrt(x)), C_n=(2n-1) C_(n-1)/(2x).

The missing tail satisfies |F_n-C_n|<=T_n(a), where
T_0<=exp(-a)/(2a), T_n=exp(-a)/(2a)+(2n-1)T_(n-1)/(2a).
This bound follows from integration over [1,infinity] and is valid for any
imaginary part. Therefore the former proof does not assume |Im x|<=2. The same
odd-polynomial derivative omission bounds in production/radial/DERIVATION.md apply
using these T_n and |exp(-x)|=exp(-a). Radial orders need n<=2; foreign even
integrals need n<=9. Actual near-a=64 controls include |Im x|=32. Large x is never
passed to the hypergeometric series and exp(+x) is never evaluated.

## 4. Uniform actual HH geometry enclosure

Let R=(2,0,z), q=+-v_e, a,b be frozen positive Gaussian exponents, and t1,t2>=0.
For a foreign insertion, only one of e1,e2=gamma² can be nonzero. Set
A=a+t1+e1, B=b+t2+e2 and
c=(b+e2)/B-e1/A. Both fractions are in [0,1], so |c|<=1.
The complex displacement is delta=cR-iq/(2B) zhat, and

x = [c²|R|²-q²/(4B²)-icqz/B]/(1/A+1/B).

Consequently |Im x|<=|qz| and Re x>=-q²/(4b_min). Also
Re x<=|R|² min(A,B)<=|R|²(a_max+t_max), since one Gaussian has no foreign extra.
The radial variance v=(1/A+1/B)/2 is between
1/[2(a_max+t_max)] and 1/a_min, uniformly in nonnegative gamma.

For the even analytic Coulomb insertion: side 1 has x=A|R|² real; side 2 has
x=(t2²|R|²-q²/4+it2qz)/B. The same lower, upper and imaginary bounds follow.
Electron exchange and sign conjugation preserve the bounds.

For every frozen primitive pair, all B192 nodes, all gamma>=0, and |z|<=64,

- Re x >= -25.00426558753802546;
- Re x <= 105204881.034973157875;
- |Im x| <= 28.624111772637522932;
- 1.9485787920035007e-5 <= v <= 500.

Thus the new guarded scalar domain [-32,1e12]+i[-32,32], variance [1e-100,1e100],
contains the actual requested trajectory for B192. Other B grids must recompute
t_max in the stated enclosure; this is not an automatic unlimited-grid claim.

## 5. Acceptance and use

The frozen threshold is 128 longdouble epsilon = 1.3877787807814457e-17.
Radial errors use max(|reference|, C_p/(2v)^j). Boys errors use the positive
defining integral at Re x, which bounds the absolute integrand norm and remains
meaningful near complex zeros. `RESULTS.json` gives all 14,720 exact-input
comparisons, not an end-to-end Hamiltonian error bound.

`GEOMETRY_RESULTS.json` checks 38,880 actual radial sampled quadrature points and
12,960 even foreign Boys points, across all 144 primitive pairs and z=0,8,16,32,64.
The uniform algebraic enclosure covers unsampled nodes/gamma; numerical accuracy
is measured at specified adversarial and extremal points. Quadrature convergence,
matrix cancellation, interpolation, and propagation still require their own tests.

Build via `backend.Backend()` or inject both source paths into the existing
content-addressed native builders. The radial source remains compatible with
`GuardedH(...,radial_source=...)`. Strict IEEE, FE_TONEAREST, finite-domain and
buffer guards remain active; a failed call returns no valid candidate output.

Reproduce with PYTHONPATH=completion/deps and the scripts validate.py,
geometry_controls.py, and guard_controls.py from this directory. The actual
immutable C21 references read were derivative_theory/ALGORITHM_CONTRACT.md and
DERIVATION_KO.md; they motivate analytic derivative consistency, not these
independently derived scalar formulas.
