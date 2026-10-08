# Accuracy contract for the NCP acceleration candidate

The optimized object is the current source-bound, arbitrary-precision ball
callback and its independent task execution. The archived finite-order producer
and already completed anchor states are not reinterpreted or rerun. This is an
additive candidate, not an installed production replacement.

## 1. The actual repeated work

For one fixed `(t,u,parameters,orbital,field,precision,margin)` invocation, the
immutable callback evaluates a polynomial with at most 107 signed terms:

\[
S=\sum_{n=0}^{N-1}c_n U_{i_n}(t)U_{j_n}(u)I_{k_n}(t,u).
\]

The degrees are bounded by eight. The existing implementation calls both
densities and the spatial primitive separately for every term. The candidate
caches the first evaluation of each distinct left density, right density and
spatial degree during this invocation only. Hence the expensive evaluation
counts become `|{i_n}|+|{j_n}|<=18` and `|{k_n}|<=9`, compared with `2N` and N.
For N=107 this is up to 214→18 and 107→9 for the full degree set. These are
operation-count reductions, **not measured wall-clock speedups**. Different
densities, moments and allocations have different costs.

No cache survives a callback invocation, so a different whole argument box,
precision, parameter set, analytic trial, or domain margin cannot accidentally
reuse an old value. Concurrent jobs have independent process memory and
contracts. Degree validation occurs before using a degree as a cache index.

**Equivalence argument.** At fixed arguments and backend, an evaluation of a
cached subexpression performs the same immutable code and precision operations
as its uncached counterpart. Subsequent uses copy the resulting ball exactly.
The candidate retains the original coefficient multiplication parentheses and
the same sequential term accumulation order. By induction over n, every term
ball and every accumulated sum ball is identical, provided the backend is
deterministic for identical calls. Thus memoization changes the number of
computations, not their arithmetic dependency graph at each use. Native
`acb_equal`/serialization checks test this implementation obligation; a loose
overlap test would not establish the stronger equality claim. Refused invalid
arguments and exhausted budgets must remain refused; acceptance is never
inferred from a finite midpoint.

## 2. Parallelize independent targets; preserve each target's operation order

The existing assembly object contains 2592 primitive entries indexed by
`active × field × orbital × ia × ib = 2×3×3×12×12`. This supplies ample potential
coarse-grained parallel work without splitting a compensated or ball sum.
The new executor is also usable for other independently authorized tasks with
an explicit complete manifest. It does not generate an actual HH manifest or
grant a full-certificate run.

For a declared ordered set of tasks `(J_0,...,J_{m-1})`, assume each successful
task returns its complete exact payload P_j under its fixed input/backend
identity. Execution on different ranks changes only completion order. The
collector requires exactly one valid committed payload per declared task,
orders by the manifest's canonical task index, and preserves the payload
bytes. Therefore the collected sequence equals serial execution's sequence
whenever each task is deterministic. No rank count or scheduling estimate
enters the scientific expression. Timing, PID and observed affinity belong to
receipts rather than the scientific payload digest.

The MPI dispatcher transmits integer task IDs and statuses. Arbitrary-precision
balls are not cast to Fortran real64/real128 or reduced with `MPI_SUM`.
Final source assembly remains in its canonical sequential operation order.
Fortran provides an efficient native MPI control layer; it does not replace
the FLINT arbitrary-precision backend with fixed-width arithmetic.

The task ledger's `COMPLETE` is an execution-integrity status. It is not
`RADIUS_MET`, an HH certificate, or a scientific admission. Those require the
separate evaluator's actual inclusion/radius and source gates. A backend may
successfully execute and return an inconclusive scientific result; collection
does not upgrade that result.

## 3. Resource and failure boundaries

The target is user-described as 64 cores and 128 GB. A cloud vCPU count does
not prove 64 physical cores. The launcher must measure allowed OS affinity,
physical core/SMT topology, NUMA information, ancestor CPU quotas, ancestor
memory limits and current available memory before selecting ranks.
Use one numerical thread per worker by default. For 64 available physical
cores and sufficient memory, a 64-rank dispatcher has 63 numerical workers
and one coordinator. If the machine exposes 32 physical cores with two SMT
threads, physical-only and explicit SMT trials are distinct configurations.

Longer predicted tasks are dispatched first, with the next task sent to the
next idle rank. Cost estimates affect order only; they cannot screen terms,
relax accuracy, or change a cutoff. A fixed synchronous wave can leave cores
idle behind its slowest job. Dynamic dispatch avoids that particular barrier
within the newly declared task batch. It does not bypass the legacy producer's
checkpoint/dual-backup ACK barriers or combine old incompatible partial states.

Failure, timeout, missing output, duplicate identity, changed executable/input,
or corrupt committed bytes yields an incomplete/refused result. A crash may
leave evidence and temporary files; none becomes an accepted checkpoint merely
because a filename exists. Restart reuses only identity-matched complete
records. Parent/worker process groups and wall/memory checks are operational
guards, not mathematical error bounds or a privileged cgroup guarantee.

## 4. Vectorization and compilation

Use `-O3` for the new native candidate with explicit `-fno-fast-math` and
`-ffp-contract=off`; record actual compiler version, flags, binary and linked
libraries. The pinned backend build may retain its prior strict `-O2` flags
while parallelizing compilation. No `-Ofast`, reassociated floating reduction,
precision downgrade, fast transcendental replacement or global fast-math flag
is an accepted acceleration.

Fixed-width integer job metadata is a valid SIMD target. FLINT ball objects,
x87 long double and software binary128 special-function loops are not silently
replaced by hardware binary64 SIMD. A Fortran rewrite alone is not a speed
argument; a compiler vectorization report and same-workload timing are required
for a vectorization claim. CPU-specific instructions are valid only for the
measured build/run host; no AVX-512 capability is presumed from the NCP label.

## 5. If integration panels are split later

The present default is independent primitive/task parallelism. Splitting a
single integral into panels needs a stronger scientific manifest: disjoint
complete coverage, identical exact endpoints, and outward accepted errors
`e_j` with a certified total budget `sum e_j <= epsilon_interior`. Giving every
panel the full global tolerance is invalid. Endpoint bounds are charged once;
post-integral conjugation and final assembly remain outside complex callbacks.
Deterministic panel reduction may differ from the old arithmetic graph even
when both enclose the same integral, so bitwise equality and inclusion are
separate gates. The executor does not invent this additional panel proof.

## Evidence classes

- **Derived:** memoization equivalence and scheduling independence under the
  explicit contracts above.
- **Implementation-verified:** only behavior exercised by recorded fresh tests.
- **Numerically checked:** only the exact synthetic/native runs actually recorded.
- **Unverified until NCP execution:** MPI/Fortran build and execution, FLINT
  baseline/cached ball equality, native wall-clock gains, and scaling to the
  actual 64-core machine.
- **Unchanged:** actual HH epsilon/eta remain null, rigorous=false and production
  admission=false until their existing scientific gates are met.
