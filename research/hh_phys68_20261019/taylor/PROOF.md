# PHYS68: normalized outgoing Coulomb Taylor disks

## Definition, assumptions, and inherited inputs

Use the dimensionless atomic coordinate x=r/a0, B=27, k*a0=7/10,
E=49/200 Hartree and eta_C=-10/7.  Write H_l=G_l+i F_l^C for the outgoing
Coulomb solution, where F_l^C is the regular Coulomb wave.  In this proof
f_l(x)=H_l(x)/H_l(B); this f_l is neither the source operator F in eta=Fy
nor the Coulomb parameter eta_C.  No conjugation enters products below.

The inherited PHYS67 routine `coulomb_point` encloses H_l(c) and its first
derivative with respect to the atomic radius and checks its recurrence,
Wronskian, differential equation, and defining Tricomi derivative.  The
unchanged helper `outgoing_h_acb` supplies H_l(B), with an explicit right
half-plane guard and a nonzero denominator check.  Their ball arithmetic
and fixed physical parameters are reused.  This unit does not repeat the
old PHYS67 20-point campaign.

The admitted module inputs are 0<=l<=64, 27<=c<=100, degree 1<=N<=256,
128<=precision_bits<=4096, and exact positive radius R satisfying
c-R>7/10.  Int, Fraction, and exact strings are accepted.  Floats and bools
are refused as point inputs.  Explicit Arb/Acb balls are permitted only
for evaluation of an already constructed analytic Taylor disk.

## Exact coefficient recurrence

The standard Coulomb equation is

    d_rho^2 H + [1-2 eta_C/rho-l(l+1)/rho^2] H = 0.

With rho=(7/10)x and d_x=(7/10)d_rho this is exactly

    f_l''(x) + Q_l(x) f_l(x) = 0,
    Q_l(x) = 49/100 + 2/x - l(l+1)/x^2.

In particular the attractive Coulomb term has a plus sign in Q.  At c,
write z=x-c, Q_l(c+z)=sum_(n>=0) Q_n z^n and
f_l(c+z)=sum_(n>=0) h_n z^n.  The geometric-series identities give

    Q_n = (49/100) delta_(n,0)
          + 2(-1)^n/c^(n+1)
          - l(l+1)(n+1)(-1)^n/c^(n+2).

Equating powers of z proves

    h_0 = H_l(c)/H_l(B),
    h_1 = H_l'(c)/H_l(B),
    h_(n+2) = -sum_(s=0)^n Q_s h_(n-s)/[(n+1)(n+2)].

These are Taylor coefficients, not unnormalized derivatives.  The code
computes the Q_n as Fractions and encloses each conversion to Arb at the
working precision.  Induction over the finite recurrence therefore puts
each exact h_n inside the corresponding Acb coefficient.  It preserves
the uncertainty of the common initial values; independent ball operations
may enlarge the enclosure but cannot invalidate it.

## A proved majorant on the whole complex disk

The closed disk |z|<=R lies in Re(x)>7/10>0.  Q is analytic in a
neighborhood of this disk.  The initial-value problem therefore defines
the same analytic continuation of the outgoing Coulomb solution there.
No Coulomb zero-free claim is needed to construct f itself: the only
division is by the already resolved constant H_l(B).

Let Y=(f_l,f_l')^T and A(x)=[[0,1],[-Q_l(x),0]].  For every |z|<=R,

    |Q_l(c+z)| <= q_R
      := 49/100 + 2/(c-R) + l(l+1)/(c-R)^2,
    ||A(c+z)||_infinity <= a_R := max(1,q_R).

Parameterize a straight segment by x(t)=c+t z, 0<=t<=1.  The equation
d_t Y=z A(c+t z)Y and the integral triangle inequality give

    ||Y(t)||_infinity
       <= ||Y(0)||_infinity
          + |z| a_R int_0^t ||Y(s)||_infinity ds.

Gronwall's inequality now yields a bound for every point of the complex
disk, including its boundary:

    |f_l(c+z)| <= ||Y(1)||_infinity <= M_R,
    M_R := max(|h_0|,|h_1|) exp(R a_R).

All quantities here are dimensionless: h_1 differentiates with respect
to x=r/a0.  In physical coordinates d_r f_l=h_1/a0.  The use of an infinity
norm on Y thus does not add quantities of unequal dimension.

The implementation takes exact upward endpoints for |h_0| and |h_1|,
computes q_R and a_R as exact rationals, evaluates exp with an Arb
enclosure, and stores the upward endpoint of the result.  Thus the
returned majorant is a finite exact dyadic number >= the displayed M_R.
The same derivation can be evaluated at any smaller radius with c-R>7/10;
there is no obligation to use the large R majorant for a smaller disk.

## Cauchy remainder and interval evaluation

Cauchy's estimate on |z|=R gives |h_n|<=M_R R^(-n).  For 0<=x<R,

    |f_l(c+z)-sum_(n=0)^N h_n z^n|
       <= M_R (x/R)^(N+1)/(1-x/R),   |z|<=x.

`TaylorDisk.remainder(x)` returns an exact outward dyadic upper bound.
This is the truncation bound.  The stored coefficients also contain
initial-value and arithmetic uncertainty.  `evaluate` applies Horner's
rule in Acb and adds the analytic remainder as a Cartesian square that
contains the complex error disk.  Consequently its returned rectangle
encloses both finite arithmetic uncertainty and the infinite Taylor tail.
The complex radius of that rectangle can be larger than the scalar tail.

For an Acb offset, its exact upward modulus endpoint is used as x; the
whole input ball must lie strictly inside the certified majorant disk.
Boundary-crossing or nonfinite inputs fail.  Exact dyadic endpoints are
converted through integer mantissa/exponent pairs, never through float.

## Constructive zero-free disk and reciprocal

For 0<=rho<R, let

    b_rho = |h_0|_lower
            - sum_(n=1)^N |h_n|_upper rho^n
            - M_R (rho/R)^(N+1)/(1-rho/R).

The reverse triangle inequality and the Cauchy bound prove
|f_l(c+z)|>=b_rho on the closed disk |z|<=rho.  `zero_free_lower` returns
the signed lower endpoint of this expression.  A strictly positive
endpoint proves that 1/f_l is analytic in a neighborhood of the closed
disk and is bounded there by 1/b_rho.

A zero or negative endpoint is recorded as an unresolved bound.  It does
not prove that f_l has a zero.  For example exp(z) has no zeros, but the
triangle lower bound at rho=1 is negative.  The test suite explicitly
preserves this distinction and rejects reciprocal promotion in that case.

When b_rho>0, the reciprocal coefficients satisfy

    g_0=1/h_0,
    g_n=-sum_(j=1)^n h_j g_(n-j)/h_0.

`reciprocal_disk(rho)` encloses these coefficients and attaches the
justified radius rho and majorant 1/b_rho.  Its own Cauchy remainder is
therefore valid for smaller evaluation radii.  The returned certificate
never silently inherits the original, larger radius R.

## Actual validation and adoption scope

The new focused suite passed 28/28 tests in 0.51 s, exit 0.  Its physical
comparisons use l=0 and 21 at target radius 28.25 and l=28 and 64 at target
radius 39.25.  The Taylor polynomials use centers 28 and 39, degree 64,
R=2 and 384 bits; the separate direct Coulomb target evaluation uses
512 bits.  Each full Taylor rectangle contains the direct target ball.
For l<=28, the tested rho=1/2 lower bounds are positive; the l=64 test
uses rho=1/4.  These are fixed new point comparisons, not coverage of a
continuous radial profile by themselves.  Continuous coverage comes from
the proved disk bounds and a caller's actual recorded panel construction.

Synthetic tests independently use exp(i*7z/10), its exact coefficients,
complex offset balls, Cauchy tail monotonicity, the reciprocal, and the
zero-free failure counterexample.  The exact Q coefficients were also
compared against a separately expanded SymPy rational function through
order 7.  Tiny dyadic radii below binary64 underflow, invalid domain and
input types, insufficient coefficient data, and precision-context
restoration are covered.

The Wolfram context call returned provider error -32603.  The subsequent
evaluator returned seven Q_n checks, seven substituted ODE residuals and
one derivative-chain check, all exactly zero.  The provider also printed
undefined-symbol warnings about its global Q symbol; both the warning
and the returned association are preserved in WOLFRAM_VERIFICATION.json.
This is a finite algebra check, not the proof of the disk theorem.

The mathematical theorem is derived above; finite coefficient, endpoint,
and selected point behavior is implementation-verified by the new suite.
The module does not claim the complete D2 response, excluded angular
tail, source-driven xi, origin/incoming adjoint, sigma(E), Maxwellian
k_HH(T), or HH_R10.  PHYS63 stays ESTABLISHED and HH_R10 stays OFF.

## Primary references

- NIST DLMF 33.2, especially 33.2.1, 33.2.11 and 33.2.12:
  https://dlmf.nist.gov/33.2 (read in this unit).
- The installed python-flint 0.8.0 `arb.lower`, `arb.upper`,
  `arb.abs_upper`, `acb.abs_upper` and `acb.abs_lower` docstrings explicitly
  specify outward exact floating-point endpoints.  These installed API
  docstrings were read before using the bound conversions.
- The web documentation https://python-flint.readthedocs.io/en/latest/arb.html
  was also read but currently labels itself 0.9.0.  This unit's recorded
  executable is 0.8.0 / FLINT 3.3.1; no installed-version upgrade is inferred.
