# Independent native execution findings

The existing cache now passes **actual compiled equivalence checks**, and the suspected interval-refinement defect is now directly reproduced. These observations supersede the runtime-pending portions of `INITIAL_NATIVE_REVIEW.md`; old reports remain historical.

Both probes were compiled using GCC C++17 at `-O3` with fast-math, associative-math, unsafe-math optimizations and contraction disabled. The pinned FLINT 3.4.0 / GMP 6.3.0 / MPFR 4.2.2 build record and actual dynamically linked library bytes were verified before execution and afterward. Each process had a 1-GiB address-space cap and 120-second external wall bound. The compile and run commands, compiler identity, library hashes, source hashes, output hashes and actual exits are in each `*_runtime/REVIEW_RUN.json`. Both compilation logs are clean and both probes exited zero.

## Actual Frozen107 cache equivalence

All **72 distinct callback conditions and 88 paired comparisons** passed exact `acb_equal`, component-dump equality, identical contract counters/error state, and complete 107-term ordered evaluation. The donor retains its 55 positive and 52 negative coefficients. The four configurations cover both 128/256-bit precision, real points and small complex boxes, exponent-pair corners, and every active/field/orbital combination. The exact source NPZ and generated rational input record are separately hashed; there was no host-float conversion of the input values.

Each cached invocation actually evaluated 8 left densities, 8 right densities and 9 spatial functions. The original source requests each of these three helpers for all 107 terms. Memoization is local to one invocation and leaves the ordered signed products/sum unchanged.

Eight selected conditions received three alternating paired timing samples each. Ratios of baseline median time to cache median time range from **9.06 to 16.66**, with median **11.37** across the eight case ratios. These short measurements describe only this callback component in the current workspace. They are not a 64-core NCP benchmark, confidence interval, complete-integrator speedup or all-target coverage claim. All 88 comparisons ran in approximately 0.618 seconds, excluding compilation and provenance checks.

This supports using the cache in the authorized bounded native pilot. It does not by itself admit any quadrature result, tail bound, final D matrix or production solver.

## Reproduced refinement defect

For the regular positive-path analytical integral

\[
\int_{2^{-8}}^{2^{192}}\frac{dt}{t}=\log(2^{192})-\log(2^{-8}),
\]

the immutable wrapper at 128-bit precision stops with `NONFINITE_CALLBACK` after **one** dispatched evaluation and a stopped global budget. With the same endpoints, precision, requested accuracy, 20,000 evaluation limit, 256 queued-panel limit and degree limit 64, direct pinned FLINT returns success and an enclosure overlapping the independently computed logarithmic reference. The probe took approximately 9.2 ms.

Thus a nonfinite initial range enclosure can be a refinable condition, rather than an intrinsically invalid pointwise integrand. The old wrapper prematurely turns that condition into a global failure. It remains fail-closed: the review found no incorrectly accepted integral. An additive fix must retain fatal shared-resource and invalid-contract paths, exact-point refusal behavior and unchanged final achieved-radius checks. Subsequent review of that change is separate.

The analytical probe computes no HH integral. Neither probe grants scientific or production admission.
