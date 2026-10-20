# PHYS72 independent implementation and operator-composition review

## Decision and reviewed identities

**PASS_SCOPED.** No blocking implementation or mathematical-composition
finding remains in the reviewed Python exact-bound module or weighted
multiplier/remainder proof. This review covers the new PHYS72 scalar
certificate evaluator and its theorem correspondence. It does not claim a
review of subsequently added native code or kernel-probe implementations.

| Reviewed file | SHA-256 |
|---|---|
| `implementation/bounds.py` | `2036fc4b0d76a825d98e3ea3f2342c67c3029f4ed6fbe67686c1d70042762e7c` |
| `implementation/tests/test_bounds.py` | `4f22ddb938cece50e53b993c8df101c67ece554253d3485acf4564b83ad6dae4` |
| `theory/MULTIPLIER_REMAINDER_DRAFT.md` | `b2a91690d3e318440d0f7bdecc813b0693fff32a50c63649ac2e50253387c2b7` |

The reviewer independently developed the Green-kernel/Gram-transfer route
in `theory/GREEN_DERIVATION_DRAFT.md`, then independently derived the shifted
Morawetz identity before inspecting the implementation. The code was authored
by another lane. The reviewer made no changes to that implementation or its
tests. The separate audit source and raw result are
`independent_bounds_audit.py` and `INDEPENDENT_CODE_AUDIT.json`.

## Mathematical correspondence

The source equation, atomic coordinate, Coulomb parameter, and derivative
sign match the inherited A0=2h_C-k^2 and Z=+u'u^-1. The shifted multiplier
beta=r-B/2 leaves the exact positive angular term
(1-B/r)j(j+1)|u|^2/r^2. The actual outgoing asymptotic contributes
2||A||^2 at infinity; the flux identity has sign
k||A||^2=-Im integral f conjugate(u). Substituting it leads to the positive
quadratic inequality used by `resolvent_quadratic_witness`.

The exact rational witness 37701/7000000 proves C_*=253/1000 exceeds the
positive root. Since the quadratic has one negative root and the allowed
argument is nonnegative, no additional branch of the root test is missing.
The norm is the actual weighted Green inverse, not a sampled kernel or a
finite-angular approximation. The density/PHYS63 argument in the proof
identifies the bounded extension with the established outgoing inverse.

The noncentral multiplier remains multiplication before any harmonic
representation. The factorization S=(r sqrt(V))(r^-1 R0^+ r^-1)(r sqrt(V))
does not require commutation of the screen with J or R0^+. The equality of
the sufficient bounds for K=R0^+V on the minus-weighted space and S on bulk
L2 does not use an inverse of sqrt(V), which would be unbounded at infinity.

In the boundary identity the left factor is the **fixed free incoming**
Poisson adjoint B_-^*. It is not a lambda-dependent adjoint. Consequently

    Z_lambda-Z_0=lambda B_-^*(I-lambda S)^-1 B_+

is holomorphic for the stated disk, including complex lambda, and
D_n=B_-^*S^(n-1)B_+. In a real fixed-m polar basis, conjugation of the
incoming free factor produces the outgoing factor; the original bilinear
Born convention is preserved. The order-four remainder has exactly
lambda^4 S^3, with no extra factorial, complex conjugate of lambda, radial
k, or Hamiltonian factor two.

The explicit boundary norm contains C_j^2, with C_j increasing linearly
above 28. Its equivalence is to H1(S2), not a claimed sharp bound on the
natural H^(1/2) trace space. The prefactor 5929 is only the product for the
external degrees 21 and 20. The Python code and JSON metadata maintain this
distinction, including for very large j.

## Arithmetic and control-flow review

All admission tests, order searches, tail expressions and comparisons use
Fraction. Floats, booleans, negative values and non-finite strings are
rejected. `born_remainder_bound` computes

    P |lambda| (|lambda|q)^N/(1-|lambda|q),
    P=5929 delta/2,

which is the derived |lambda|^(N+1)q^N bound. It admits only the strict
condition |lambda|q<1. At or above the sufficient radius it returns no
error bound and states that this condition does not decide actual
convergence or divergence.

The exact recurrence used in `minimum_terms` is monotone under that strict
condition. Inclusive budget equality, lambda=0, a zero budget at nonzero
lambda, and search exhaustion have distinct meanings. Exhaustion is not
reported as a lower bound on the true error. `defect_bound` reports only
the supplied residual's error in the same Birman--Schwinger L2 space; it
does not invent a DtN trace conversion.

Decimal division is performed in a local ROUND_CEILING context after
exact integer-to-Decimal conversion. Thus displayed nonnegative endpoints
are outward. Large numerator/denominator strings are formatted through
exact Decimal integers without changing the process integer-string limit.
The upward display of 1/q could exceed the exact open-disk radius; the
report explicitly directs decisions to exact rationals or |lambda|q<1,
and the independent audit confirmed that the upward displayed radius is
not accidentally admitted.

File hashing is read-only, and output creation uses mode `x`. A requested
input mismatch sets BLOCKED_INPUT_IDENTITY_MISMATCH and exits 2. Input byte
identity and the mathematical scalar evaluation remain separately labeled.

## Actual new independent checks

One successful execution of `independent_bounds_audit.py` produced 22
PASS_SCOPED checks and exit code 0. Its exact output records both the
subject-source SHA and audit-source SHA. The comparisons include:

- Defining scalar inverse minus the explicitly summed finite Born polynomial
  for N=1,3,7 and lambda=0,1, half the sufficient radius, and three quarters
  of the radius. This checks lambda powers without reusing the implementation's
  closed-tail formula as the reference.
- The exact critical/above-critical branches and outward radius display.
- An independently constructed rational with a 10,500-digit denominator,
  its exact serialization and outward decimal, while preserving Python's
  integer-string limit.
- The affine high-j weight difference at j=100,000,000 and its distinction
  from the finite external prefactor.
- Same-space defect inversion at contraction 3/4.

These checks perform zero physical integrations, zero Coulomb evaluations,
zero old-suite runs, and zero modifications of inherited evidence.

## Evidence-version finding and closure

The first supplied implementation log contained 13 passed tests, whereas
the reviewed file contained an additional large-denominator test. This
would not support a claim that all 14 reviewed tests had passed. The
subsequently located `/tmp/phys72_bounds_tests_final.stderr.txt` explicitly
records all 14 tests, including that added test, and ends with `OK` in
0.027 seconds. The finding is therefore **closed by the actual later log**,
without this reviewer replaying the implementation suite. The first log
remains the evidence for its original 13-test run.

The first and final CLI results were also read and compared. The final JSON
adds only the explicit `radius_membership_rule`; its scientific constants,
results and input identities agree with the first JSON. They report exact
q=553311/10^26,
the exact rational tail, minimum sufficient N=3 for budget 10^-78,
the correct frozen-NPZ and corrected-D3 SHA matches, and HH_R10=OFF.
Scientific acceptance, these implementation checks, publication and backups
remain separate statuses. The current review does not claim a new
source-driven xi solution, origin/incoming-adjoint solution, cross section,
or HH rate table.
