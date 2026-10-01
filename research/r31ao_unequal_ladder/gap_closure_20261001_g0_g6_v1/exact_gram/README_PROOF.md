# Exact represented Gram and gap engine

Status: `IMPLEMENTATION_VERIFIED` on synthetic inputs. Actual B192/prediction
arrays were neither decoded nor evaluated. No continuous Frozen107 error bound,
actual eta, HH gap interval, or scientific certificate has been acquired.

The runtime has no third-party dependencies. Its radical backend is
`EXACT_INTEGER_SQRT_RATIONAL_ENCLOSURE`; this is a separately justified exact
integer alternative for this square-root-only component, not a claim that
FLINT/Arb or MPFR was built, loaded or verified. The FLINT 3.4.0 pin for validated
callbacks remains unchanged.

## Interface and identity boundary

An exact complex number is `(Fraction(real), Fraction(imag))`. A matrix is a
finite nested row list/tuple. `from_decoded` accepts the G2 decoder's `shape` and
`values_c_order`; it does not reinterpret NPY order, floating ABI or padding.
The decoder/provenance caller owns those obligations. No float, complex, decimal
string or approximate object is silently converted to an exact matrix value.
Exact rational inputs are accepted as a mathematical superset of dyadic lifts.

`gram2`/`spectral_norm` accept n by 2 or 2 by n matrices. `construct_k` requires
`D_col` n by 2 and `D_row` 2 by n. `represented_errors` requires independently
stored prediction fields `D_col`, `D_row`, and `K`. Predicted K is never derived
from predicted D. `represented_gaps` requires exactly R31AK/R31Z/R31AD and reuses
one R31AK error computation in the PRIMARY and SECONDARY subtraction.

Canonical shapes in a future HH admission are 47 by 2 and 2 by 47; the arithmetic
engine deliberately also permits small synthetic matrices. A permissive
arithmetic shape is not permission to substitute an HH basis or ordering.

## Rational radical enclosure

For q=n/d >= 0 in reduced form, first test whether both n and d are perfect
integer squares. If so, return their exact rational root. Otherwise choose a
finite integer p>0, set N=floor(n 2^(2p)/d), k=isqrt(N), and return

    [k/2^p, (k+1)/2^p].

By the definition of integer square root, k^2 <= N < (k+1)^2. Since
N <= n 2^(2p)/d < N+1 and k and N are integers,
k^2 <= n 2^(2p)/d < (k+1)^2. Thus both endpoints enclose sqrt(q);
the enclosure width is exactly 2^-p. No rounding-mode assumption or real
floating operation enters this proof or its implementation. The p parameter
sets an absolute rational-grid step, not a relative-accuracy guarantee.

For an enclosing nonnegative interval [l,u], monotonicity of sqrt gives an
enclosure by taking the lower endpoint of sqrt_interval(l) and the upper
endpoint of sqrt_interval(u). Near zero a nested square root can enlarge
absolute widths; an unmet final budget remains inconclusive.

## Gram reduction and spectral norm

For rows (x_i,y_i), exact rational arithmetic forms

    a = sum |x_i|^2,
    d = sum |y_i|^2,
    b = sum conj(x_i) y_i.

Therefore A†A=[[a,b],[conj(b),d]] is a Hermitian positive semidefinite matrix.
Its characteristic equation gives

    lambda_max = (a+d+sqrt((a-d)^2+4|b|^2))/2,
    ||A||_2 = sqrt(lambda_max).

All sums/products and the discriminant are exact. Only the two square-root
stages use the outward rational procedure above; addition and multiplication
by 1/2 preserve enclosing order. For 2 by n data, applying the same procedure
to A† gives AA† and the identical nonzero singular values. No symmetrization,
generic SVD, diagonal truncation or approximate dot-product reduction occurs.

The independent tests use a separate Decimal accumulation/eigenvalue formula
at 160 decimal digits and direct A/A† power iteration at 140 decimal digits.
Those approximate cross-checks corroborate implementation behavior; the exact
integer inequalities above supply the enclosure argument. The initially
attempted optional mpmath cross-check was unavailable in this environment;
its failed import is preserved and the dependency-free independent algorithm
was then used. No third-party package installation or science build occurred.

## K, Dmax, represented gaps and source perturbation

Raw K=(C-R†)/2 is formed exactly, including conjugation. For each frozen model,
the engine encloses the exact represented norms of predicted-minus-raw K, C
and R. If C and R norm intervals are [lc,uc] and [lr,ur], Dmax lies in
[max(lc,lr),max(uc,ur)]. This remains valid when the maximizing block changes.

For local interval [al,au] and other interval [bl,bu], the other-minus-local
gap lies in [bl-au,bu-al]. PRIMARY uses R31Z minus R31AK; SECONDARY uses R31AD
minus R31AK. Subtractions are exact rational operations.

Given *externally proven* target complex disks with centers c_ab and radii
r_ab, each raw-to-target error satisfies
|raw_ab-target_ab| <= |raw_ab-c_ab|+r_ab. Outward square roots bound each distance
and then sqrt(sum bounds^2), giving a spectral error bound through the
Frobenius norm. `source_error_bound_disk` implements this arithmetic but cannot
admit a disk as the required continuous target without target/provenance proof.

The triangle inequality and adjoint isometry give
epsilon_K=(epsilon_C+epsilon_R)/2. The reverse triangle inequality and max's
1-Lipschitz property give epsilon_Dmax=max(epsilon_C,epsilon_R). Each candidate
error changes by at most its metric epsilon; a difference of two errors
changes by at most twice that bound. Consequently

    direct L = g_minus - 2 epsilon

is a valid sufficient lower bound. The audit alternative uses exact chosen
ghat (decimal and binary64 interpretations must be labeled separately),

    eta=max(|ghat-g_minus|,|ghat-g_plus|),
    legacy L=ghat-eta-2 epsilon <= direct L.

This one eta already compares the complete serialized diagnostic to the exact
represented gap. It is not added to the authoritative direct route. Old
X0..X8 producer-error categories are not added to an end-to-end epsilon.

## Real predicates versus frozen binary64 expressions: B08

The real sufficient rule is both L_j >= -tol and at least one L_j > tol.
Equality at +tol does not pass the strict test. Crossing either required
threshold returns `DECISION_BOUND_UNRESOLVED`. The default exact threshold is
the unchanged frozen binary64 token, hex `3ddb7cdfd9d7bdbb`, equal to
7737125245533627 / 77371252455336267181195264. The distinct exact mathematical
decimal threshold 1/10^10 can be selected explicitly; the result records which
interpretation was used. Arbitrary tolerance changes are rejected.

The frozen source expressions differ:

| Scope | Weak predicate | Strict predicate |
| --- | --- | --- |
| PRIMARY, B192 comparator lines 100–101 | local <= RNE(other+tol) | RNE(other-local) > tol |
| SECONDARY, refinement_gain.py lines 45–46 | local <= RNE(other+tol) | local < RNE(other-tol) |

These expressions are equivalent over the reals but need not agree after
binary64 round-to-nearest, ties-to-even. `audit_frozen_binary64` reproduces each
scalar operation by exact integer rounding. It never calls the old comparator,
SVD or source arrays. Actual scalar input bits and historical rounding-mode
authority remain admission requirements. The source SHA/line bindings and
machine-readable witnesses are in REPRESENTED_GAP_CONTRACT.json.

Witness 1: local bits (3ff000000006df38,0), other bits (3ff0000000000000,
3ff0000000000000). The first local value is RNE(1+tol), which is strictly
greater than the real sum 1+tol. Both machine weak predicates pass; the real
gap rule fails nonworsening. The second metric supplies strict improvement.

Witness 2: local bits (3feffffffff24190,0), other bits (3ff0000000000000,0).
The first local is RNE(1-tol). PRIMARY's rounded difference exceeds tol, but
SECONDARY's local < RNE(1-tol) is false by equality. Moving local one binary64
step down makes SECONDARY's strict predicate true. Thus a universal rule that
rewrites both source expressions into the same gap comparison is unsound.
No blanket nextafter/ULP relaxation is applied: exact RNE is performed at the
actual source operation, with ties-to-even, normal/subnormal transitions and
finite overflow rejection. Next-representable witnesses appear only in tests.

`pareto_sufficient` returns an arithmetic real-rule result with
`machine_predicate_certified=false` and `continuous_target_certificate=false`.
It deliberately does not emit `CERTIFIED_PARETO_PRESERVED`. An integrated
certificate must bind genuine epsilon/target/prediction identities and keep the
legacy machine audit as a separate, authenticated trace. Existing archived
finite-order verdicts remain unchanged.

## Finite work and failure behavior

Default caps: 4096 radical precision bits; 1024 entries per matrix; 131072 bits
per rational numerator/denominator; 270336 bits for temporary integer products
or shifts; 100000 exact operations per public matrix computation. Inputs are
checked before arithmetic, products/shifts are bounded before allocation, and
intermediate rational sizes are checked. There is no adaptive loop.

These deterministic caps bound arithmetic work, not wall-clock time on every
host. They may reject valid extreme-exponent data or a too-small approved
budget with `ResourceLimit`; a limit failure returns no certificate. The
future authorized runtime must additionally impose wall/memory limits and
record observed resource use. Overflow, unsupported shape/type, nonfinite
binary64 bits, negative bounds and malformed intervals raise `ContractError`.

Run only the synthetic suite from the loop directory:

    python -m unittest exact_gram.test_engine -v

The retained red/failure/green logs distinguish the initial missing module,
one corrected strict-Fraction test fixture, optional dependency absence and
the final passing tests. No old scientific suite was run.
