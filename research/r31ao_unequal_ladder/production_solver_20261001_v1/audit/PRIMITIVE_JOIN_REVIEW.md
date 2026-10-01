# Independent primitive join and assembly-boundary review

Result: **No unresolved blocking defect found in the reviewed conditional Python/source boundary.** Native assembly/export remains uncompiled and unexecuted. This review does not admit a scientific target enclosure or a production solver.

Reviewed source SHA-256:

| File | SHA-256 |
|---|---|
| primitive_join/join.py | a9eedbc3c8c619058a5debec3185f914cd85f892c231d1fc9fc5a9cc1d653915 |
| primitive_join/assembly_exporter.cpp | a6ca3e7bab454f3db247346f9787b5b408930bbe0e48e2f81930dc2a6a31d8f7 |

The reviewer read both sources, tests and the imported endpoint/native contracts. Immutable assembly/callback source and the actual pinned FLINT interval serialization and `arb_add_error` implementation were also inspected. No implementation file was changed by the reviewer.

## Findings resolved

- **Persisted native envelope integration bug:** the first implementation passed wrapper/result-hash fields into the raw native result validator, which now requires exact raw-result keys. This rejected genuine persisted native records. The final join validates the seal and wrapper separately and removes only those two known envelope fields before exact raw-result validation. Extra payload fields still fail. The success fixture has the actual persisted wrapper structure.
- **Assembly input binding:** the initial exporter stamped primitive coverage input hashes without comparing them to its generated input/build identity. The final exporter includes `build_identity.hpp` and rejects archive/record mismatch. The preparation API checks the native BUILD document, exact generated Frozen107 header SHA, and exact build-identity header bytes before generating a new assembly directory. Header reads are bounded before allocation. Correct-byte and swapped-header refusal fixtures pass. Later native build/execution acceptance is still required; header preparation itself is not a build.
- **Trust-contract propagation:** both endpoint-engine and native-output assumed-execution conditions now survive joined records, complete coverage and final disk import. None is promoted by recomputing a document hash.

## Numerical and coverage assessment

A complex endpoint tail disk of radius B is added to the interior rectangle as `[lo-B, hi+B]` in each real/imaginary component, exactly once. This safely contains the tail disk. Normalization is not applied in the join. The join rejects interior records already marked endpoint-inclusive, normalized or full-domain. It verifies matching task index, exact window, plan, input, source, backend, binary and numerical limits through a shared Context and the wrapper's exact command arguments.

Collection requires exactly 2,592 unique canonical primitive indices. Missing, duplicate or mixed execution identities fail before initializer emission. Unordered arrivals are restored to canonical index order. The initializer emits two component assignments for every primitive. Exact rational centers and half-widths are converted with `arb_set_fmpq`; `arb_add_error` adds an outward absolute upper bound on the half-width ball. The existing center-rounding radius is retained. Pinned FLINT source confirms this addition semantics.

The existing immutable native assembly performs normalization and final phase/coefficient/conjugation operations once. The exporter uses `D_col` as 47×2 and `D_row` as 2×47, all 94 entries each, preserving the native storage order. It validates finite output and bounds serializer exponents, mantissas and allocation shifts before constructing the complete JSON. It emits no partial successful JSON if serialization fails. Its exact dyadic endpoint API is the same pinned implementation reviewed for the primitive native worker.

The final importer constructs each disk center from exact rectangular midpoints and radius from the outward upper bound on `sqrt(hx²+hy²)`. It does not use `max(hx,hy)`. The 3–4 corner fixture returns radius 5. Shape, exact source/coverage/input identity, finite canonical integer endpoints and precision bounds are checked. Both source assumptions and false scientific/production admission remain visible.

## Executed verification and limits

Fresh `python -B -m unittest -v test_join`: **10 tests passed**, no failures or errors, in 1.678 seconds. The suite constructs all 2,592 synthetic joined receipts and checks complete canonical coverage, identity/duplicate/missing refusal, once-only tail addition, exact header preparation and disk conversion. These are fabricated analytical receipt fixtures, explicitly not records of native execution.

Final verification used the independently reviewed endpoint outward policy at planner `bba157ff048a8955c25c140f7d44871d9c627c5197c7d115850428a481cbeaf5` and refreshed native dependency pins `8c76d06837320bdcb494a0412b66cde2f1722b022a5d49775b964bfa669ce23e`. The native source identity is `7f6e625c66921be84563548a9af315312050db961a5e83d4f1275e60f6c1255c`. The final 10-test boundary replay passed with these identities. Preparation now preserves the recorded absolute compiler path and hash for host reverification; it does not claim that compiler has run. Old and new plans/results must not be mixed. Actual complete endpoint/interior coverage, assembly compilation/linkage, achieved final D radii, historical ABI and independent scientific decision admission remain open.

## Final capped-majorant dependency readback

The final endpoint planner is `53fe8cea32fb24efe9ef2682f480d63595db2bf32525ed57f46df391fe3eb4e6`, reviewed separately in `ENDPOINT_INTERIOR_MASS_CAP_REVIEW.md`. The final native pin document is `295972acff814765aacd8b15c9bcf0be00c02ce2956d09d65139c1705170a7ba`, with source identity `8fc475d86f9e496ec1f3b3bdab99bb9ad76666b3d3227ab764c735f783b6b202`. The reviewer independently reran source-pin verification and confirmed the native driver, native worker, join and assembly-exporter source hashes are unchanged. Machine-readable readback is `FINAL_DEPENDENCY_PIN_REVIEW.json`. The author's post-majorant join evidence records 10/10 tests passing with these exact dependencies. Historical pin/evidence documents remain preserved; no unrelated suite was rerun by the reviewer. Native compilation/execution and scientific admission remain unestablished.
