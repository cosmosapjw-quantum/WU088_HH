# Per-invocation cache equivalence

This is a structural candidate with a native exact-equality fixture. No FLINT compilation, native equality test or native benchmark has run in this environment. Static checks and an exact rational interval model do not establish native Arb equivalence.

## Bound baseline and scope

`cached_callback.cpp` includes the immutable old `validated_callback/callback.cpp` once. It thereby compiles the original `wu088::polynomial_field`, original `density` and `spatial` implementations, and the added cached entrypoint in one translation unit. No original file is edited, no formula is copied into a competing implementation, and no old scientific runtime or array is loaded. `SOURCE_LOCK.json` binds both old files, all new build inputs, and the existing backend provenance gate.

The comparison baseline is the old **source** compiled with the same compiler, flags and libraries as the candidate; it is not an assertion of equality to a previously cached production binary. The build uses C++17, `-O3`, no fast math, no reassociation, no unsafe math and no floating contraction. Arbitrary-precision numerical arithmetic remains in the pinned FLINT backend. Host floating values are used only for elapsed-time reporting.

## Exact-expression argument

Fix one invocation with unchanged complete t/u complex balls, exact parameters, orbital, field, margin, working precision and rounding/backend context. Inputs/outputs must not alias, and callers must not mutate inputs or share mutable `Contract`/`CacheStats` concurrently. Each baseline helper is a deterministic function of these values and its degree. In particular, no helper consumes the callback budget; `check(c)` is called once by the polynomial entrypoint.

For each term n, the original tree is

`value_n = ((Ball(coefficient_n) * density(i_n,t)) * density(j_n,u)) * spatial(k_n,t,u)`

and `sum_n = sum_(n-1) + value_n`, with original term order and a zero initial ball. The candidate changes only the three helper leaves to local lookups. On first use, the same original helper runs on the same full balls and precision. Its returned ball is moved into an `optional<Ball>` using the original exact `acb_swap` move; subsequent lookup returns a const reference to that same ball. Multiplication/addition operators produce new balls and do not modify their operands.

Inductively each lookup supplies the identical ball that recomputation would supply, each term follows the same left-associated multiplication tree, and each accumulator step follows the same addition tree. Thus successful result balls are identical under deterministic backend execution, not merely overlapping mathematical enclosures. No zero coefficient is screened, no signed cancellation is rearranged, and coefficients are converted afresh at their original per-term position. Helper-call operand evaluation order in C++ is not a promised total order in either implementation; their numeric expression tree and sequential term order are preserved. A caller supplying several simultaneously invalid operands must not rely on a portable first-error-message priority.

Caches are three automatic arrays of nine optional balls. They are destroyed at return. Left and right density caches are distinct even if t=u. The spatial cache is confined to the same field/orbital/parameters for that invocation. There is no cross-call, cross-precision, midpoint, rounded-key, MPI-rank or thread-shared cache. Invalid degree paths call the original helper and retain its failure behavior rather than indexing out of range. Precision, positivity and call-budget checks are unchanged. Any exception invalidates output using the original failure helper. Extra allocation/resource failure is fail-closed; this structural proof is not a guarantee of host resource success.

## Operation counts and memory

For a successful N-term call let d_i,d_j,d_k be the distinct left, right and radial degrees. The original source calls density `2N` times and spatial `N` times. The candidate calls them `d_i+d_j` and `d_k` times, respectively, with each d at most nine. The observable counters count attempted calls, cache hits and completed terms, not FLOPs. Failure counters can stop partway through a term.

The synthetic 107-term recipe covers all nine indices: density calls fall from 214 to 18 and spatial calls from 107 to 9, a helper-count ratio of 107/9. This is **not** a wall-time speedup claim. Per-term multiplications, coefficient conversions and 107 accumulator additions remain. At most 27 cached balls live per invocation; total FLINT temporary memory and peak host memory must be measured and guarded separately. Geometry and radial-moment expression trees are unchanged inside the original spatial helper.

## Native acceptance fixture

`native_cache_synthetic.cpp` uses only fixed artificial rational parameters and a signed 107-term recipe. For all nine orbital/field pairs, both implementations receive identical real points, complex points or whole complex boxes and the requested precision. Every successful comparison requires both `acb_equal` and identical `arb_dump_str` strings for real and imaginary components. Overlap is never accepted. Repeated calls must also match the first result exactly. The expected 9+9+9 evaluations and cache hits are checked after every valid call.

The error case checks empty/oversized terms, invalid i/j/k, zero mu/a, invalid field/orbital, a whole box crossing zero, invalid precision caps, zero and exhausted call budgets, callback order 0/1/2, null callback state, and precision mismatch. Failure outputs must have identical component dumps and be nonfinite; contract calls/failures/error text must match for the single-failure fixtures. Unsupported order invalidates every requested coefficient slot.

Scientific payload files contain deterministic exact component dumps, precision, case, fixed parameters/term recipe, and equality status. Timing, operation counters, output path and repeat count are excluded from these payloads. Repeated timing alternates baseline/candidate order and is reported separately on stdout. Process/rank scheduling can therefore compare raw payload hashes without reducing or reserializing any scientific value.

## Evidence and remaining gates

Ten static/exact-model checks passed; shell syntax passed. The first exact-model negative-control fixture accidentally produced equal enclosures under reassociation, so its assertion failed. `STATIC_FIRST_FAILURE.log` preserves that test-data error. A bounded exact search supplied `(1/9,1/9,4/7)`, whose two multiplication trees produce different model intervals; the repaired fixture passes. This did not alter the native implementation.

Native compilation, exact-ball equality, benchmark timing, multi-rank native payload identity, target NCP topology/resource measurements, and scientific admission remain unverified. No source pin or structural proof is used as native execution evidence. Actual HH runs remain zero; epsilon/eta remain null and rigorous/production admission remain false.
