# Independent production-composition component review

Result: **No blocking defect found in the reviewed component.** This is an independent code and bounded-arithmetic review of the conditional T5 composition adapter, not an independent scientific-decision review or a production admission.

Reviewed adapter: `research/r31ao_unequal_ladder/production_solver_20261001_v1/composition/adapter.py`

- Adapter SHA-256: `e878c7468c78c909b5cd7a682f856b8908d1555580ea47fc8eedcee55ff493fe`.
- Immutable exact-Gram SHA-256: `e10f206d63be1a99a441780108619574605014a9b01b3b327e21fecb18c5b9cc`.
- Authority read: root AGENTS.md and its four required documents; immutable exact-Gram engine; `theory_closure_20261001_v1/T5_SHARP_RESIDUAL_CERTIFICATE.md`; adapter and its component tests.
- No reviewed source file was modified. No external write, native backend execution or actual HH producer run was performed.

## Formula and contract findings

1. Each source and model residual uses the spectral norm of the exact center residual and an outward upper bound on the Frobenius radius. Lower endpoints are clipped at zero. This implements T5.1; it does not replace the center residual by its Frobenius norm.
2. Raw and target K use `(C - R†)/2`, with transposition and imaginary conjugation handled correctly. Target K radii use `(rC + rR)/2`. Exact cancellation remains in the center. The minimum of the direct K residual upper bound and the separate-block upper bound is valid.
3. Every model's stored K is parsed independently and retained in both represented and target errors. It is not reconstructed from the model D blocks.
4. Model Dmax uses interval max. Gaps have the frozen other-minus-R31AK direction, with R31Z for PRIMARY and R31AD for SECONDARY. Direct target gap intervals are intersected with represented-gap intervals expanded by ±2 epsilon. An empty intersection fails closed. No old producer uncertainty or diagnostic eta is added.
5. The real Pareto test preserves `gap >= -tol` for each weak condition and `gap > tol` for at least one strict condition. Equality at +tol does not count as strict improvement. The frozen binary64 tolerance token is converted exactly. The reported negative condition is sufficient to exclude the real conjunction; unresolved cases remain unresolved. The code does not claim equivalence to either archived floating comparator expression.
6. Input identities use canonical JSON SHA-256 envelopes. Hashes establish payload identity only. The adapter explicitly refuses promotion from documentary evidence hashes. All scientific, continuum, ABI, machine-predicate and production admissions remain false.
7. The byte parser rejects duplicate keys, floating/nonfinite tokens and oversized documents. Matrix shapes, model set, object keys, canonical reduced rational syntax, radii and lowered resource limits are checked. One shared exact-operation budget spans the calculation. Input and intermediate bit bounds and radical work bounds fail closed. The CLI creates a result atomically without replacing an earlier output.

## Executed verification

- Final fresh `python -B -m unittest -v test_composition`: **21 tests passed**, no failures or errors. The earlier 18-test replay and this final replay do not increase the author's unique test count. The final adapter explicitly exposes epsilon.D_col and epsilon.D_row as aliases of the already calculated source upper bounds; this does not change the reviewed arithmetic. The three added tests cover deterministic/default precision, oversized rational-token refusal before integer conversion, and immutable dependency source corruption.
- Independent probe: `production_audit/composition_independent_probe.py`; result: `production_audit/COMPOSITION_INDEPENDENT_PROBE.json`.
- The probe constructed dense complex rational matrices with independently stored model K and four actual target samples on the exact entry-disk boundaries. It checked **57 norm-containment inequalities**: 9 represented model residuals and 48 source/model residuals across the four samples.
- The independent oracle used exact rational Hermitian positive-semidefinite/principal-minor inequalities. It did not call the adapter's or immutable engine's spectral-norm/radical routines to establish containment. For an upper endpoint u, it checked that `u² I - A†A` is positive semidefinite; the lower endpoint check used the maximum diagonal or the characteristic-polynomial sign. All 57 checks passed. These are bounded sample checks, not a new all-input theorem or 57 new test cases.

## Scope that remains open

The component consumes supplied final-entry disks. It does not construct the continuous target enclosures, validate their source/domain/normalization binding, authenticate historical ABI or model provenance, serialize native Arb results, connect the 2,592-primitive integration controller, or prove an archived floating-machine predicate. No actual HH input was evaluated here. A full solver run and independent final scientific decision review remain separate. The tested source hash above defines this review's scope; subsequent source changes require assessing the affected paths again.
