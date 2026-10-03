# Independent endpoint-design review

Verdict: **PASS for the source-bound endpoint component and the conditional
future grid design.** No new-window interior, full D error, or production claim
is admitted. There are no unresolved blocking findings within this scope.

The pre-execution review found one implementation-contract issue: Python
optimization flags could disable the crosscheck worker's assertions. The owner
replaced them with explicit exceptions before either actual launch. The final
worker/controller/selector source identities are recorded in
`PREEXEC_FINAL_REVIEW.json`. The checked existing host supplies single-process
execution, creation-syscall refusal, parent-death signaling, and hard address
space/CPU limits, with external wall termination and wait. No host/kernel
implementation change or new MPI execution was involved.

`ACTUAL_RESULT_REVIEW.json` records independent exact readback of the two actual
root-owned endpoint results. The reviewer did not import or execute the endpoint
engine. A stdlib-only verifier reconstructed the positive 128-bit upward
arithmetic for all 107 ordered terms, aggregate polynomial coefficients, and all
five candidate predicates; it also checked source/input/plan/result/receipt
identities and zero native-integration counts. The 13,791 recorded checks are
repeated predicates inside these operations, not 13,791 independent tests.
Engine-generated mass and Gaussian-majorant constants remain conditional on the
unchanged, previously reviewed source engine.

The first passing tested upper cutoff is **T=2^40**, at lower cutoff **1/512**.
The selected positive-polynomial bound and the original-engine crosscheck both
meet 2^-21. Their tiny difference is due to different upward summation stages;
one must not require numerical equality or crosscheck<=selector. Retaining the
larger bound gives exactly

\[
 \frac{210391441856025388187544847887702514929}
 {2923003274661805836407369665432566039311865085952}
 \simeq 7.197783310056944\times10^{-11}.
\]

The previous actual W3 endpoint ceiling divided by this bound is about
7062.415899. This compares rigorous majorant values for two auxiliary windows;
it is neither a measured runtime gain nor a measurement of the true omitted
integral error. The lower range was expanded by one octave while the upper range
was contracted; the infinite-domain signed Frozen107 target is unchanged.

`FUTURE_GEOMETRY_REVIEW.json` separately confirms that the proposed exact
Cartesian partition covers [1/512,2^40]^2 with 289 cells, 17 intervals per axis,
and maximum log2 step 3. The preserved W1 knots identify its 16 original cells
without overlap or missing coverage. The remaining 273 cells have not been
executed. A source/input/backend/primitive/window-aware collector must explicitly
rebind old accepted W1 records; geometric identity alone does not admit reuse.

If all 273 new cells later achieve real and imaginary component radii <=2^-57,
and the existing W1 enclosure is validly rebound, the triangle inequality gives
the component bound

\[
 r_{\rm W1}+273\,2^{-57}
 =\frac{40288185673830959230763}
 {21267647932558653966460912964485513216}
 \simeq1.8943413865787084\times10^{-15}<2^{-48}.
\]

This is a conditional future interior budget, not an executable collection
contract, modulus bound, or final D budget. The step-3 tile-count change from
4489 to 289 is exact geometry; no runtime speedup has been measured. The present
campaign executed exactly two endpoint workers (one selection, one original
engine crosscheck), five candidate polynomial evaluations, and zero native HH
integrations. Archived W1/W3/B192 scientific values were not recomputed.
