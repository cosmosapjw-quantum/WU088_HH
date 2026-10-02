# Independent strip-pilot review

Verdict: **PASS for four source-bound compact-cell enclosures and the exact
20-cell partial union; host cleanup bookkeeping remains unresolved.** This
verdict does not admit the full selected rectangle, the full positive-domain
integral, final D/epsilon, NCP performance, or production use.

## Source, execution and numerical evidence

The fixed cells 20, 52, 105 and 57 are the adjacent lower-t, lower-u, upper-t and
upper-u strips against the core log2 interval [-1,2]. Both orientations were
executed; no exchange symmetry was used. Far tails and double-tail corners were
not sampled by this pilot. The scope and exact geometry were checked before
execution in `SCOPE_MATH_REVIEW.json`.

The final controller and collector source identities are bound in
`PREEXEC_FINAL_REVIEW.json`. The readback verified that all sixteen original W1
raw receipts, unchanged rectangles and original requested exponent -52 were
retained, while their actual serialized radii also meet -57. Their exact union
matches the previously accepted W1 result. New cells use precision 128 and
requested exponent -57, relative goal 128, at most 200,000 evaluations and 1,024
integration calls, 120-second native budget, 125-second hard native lifetime and
180-second guarded Python-worker limit. At most two workers were permitted.

The reviewed queue drains all observed completions before dispatching more
work, stops on an observed rejection, drains already running work, and does not
retry. Five owner controller tests and eleven owner collector tests passed.
Two additional independent synthetic controller checks covered a rejection in
the second observed completion and cleanup of another active worker when
completion handling raises an unexpected exception. None of these tests ran
an HH integral or endpoint evaluation.

All four actual native results are `RADIUS_MET`, with zero process exit codes,
reported successful native wait completion, exact source/input/plan/limits
binding, preserved raw stdout, and serialized real and imaginary radii <=2^-57.
The four results used 121,496 dispatched evaluations and 740 nested integration
calls in total. The campaign wall time was 27.705733198 seconds. The adaptive
callback and analytic-domain refusal counters are nonzero and remain in the
receipts; successful final enclosure does not mean every attempted analytic
box was accepted. This is one measured two-process campaign, not a speedup
benchmark against a serial reference or NCP.

`ACTUAL_REVIEW.json` records strict native normalization replay and independent
Fraction-based reconstruction of the raw dyadic rectangles and accepted-union
sum. The reviewer performed zero native integrations and zero endpoint-engine
evaluations. Revalidation of existing executable/library/source identities is
not a new scientific execution.

## Coverage and error meaning

The exact accepted union contains the original sixteen W1 cells plus four new
cells: **20 of 289**. The remaining **269** contributions are neither evaluated
nor bounded by this partial collector. The reported partial component radii are

\[
 r_{\Re}=\frac{496918691767025551}
 {21267647932558653966460912964485513216},\qquad
 r_{\Im}=\frac{496918691890655019}
 {21267647932558653966460912964485513216}.
\]

These are radii of the integral over the listed union only. The endpoint bound
from the preceding step covers the complement of the full selected rectangle,
not the 269 missing cells inside that rectangle. Adding that endpoint bound to
this partial sum would therefore not create a full-domain enclosure. The
collector correctly keeps coverage/global-complete, endpoint-included,
normalization, scientific-admission and production-admission flags false.

## Preserved host anomaly

At terminal RETURN creation, cell 105 reported a residual native `.claim` file
and cell 57 reported none. Later independent readback found both files. Their
bytes, SHA-256 and timestamps are preserved in `CLAIM_OBSERVATION.json`, with
the separate terminal and later visibility observations also retained in
`ACTUAL_REVIEW.json`. The reviewer initially rejected an assumption that the
claim snapshot must remain unchanged; the recorded observation establishes
that this assumption does not hold here. No numerical acceptance predicate was
weakened as a result.

The files contain the corresponding worker PID text, but file contents and
timestamps do not establish that a worker is still alive or explain why claim
visibility differs after completion. No causal attribution to I/O, filesystem
behavior, process races or any other mechanism is justified by the available
evidence. Root cause remains **UNDETERMINED**. The files were not deleted,
quarantined or used to trigger a retry.

The guarded native terminal evidence, preserved source-bound output and exact
enclosure validation support the limited numerical acceptance above. They do
not establish successful cleanup of all host bookkeeping. B22 remains open,
and no fully resolved lifecycle or production claim is approved by this review.
