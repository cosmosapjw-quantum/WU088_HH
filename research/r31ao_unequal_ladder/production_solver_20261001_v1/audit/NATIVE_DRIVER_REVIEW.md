# Independent native-driver source and boundary review

Result: **No remaining blocking defect found in the reviewed source/boundary scope. Native C++ remains uncompiled and unexecuted in this environment.** Static API agreement and Python fixtures do not establish successful compilation, actual interior enclosure or production readiness.

Reviewed SHA-256 identities:

| File | SHA-256 |
|---|---|
| native_driver/driver.py | a7386e5543dd7a95c214f86af4beb875d6be4425bd2bfa93b8cb4e6daf2af515 |
| native_driver/primitive_worker.cpp | efec6cfe6e90be4e43626d991655f6b8eb5aec79ac4cfacd83e01b61e39373fc |
| native_driver/dependency_pins.json | e47c3a5ade1631b928c96fa1c994928cfc0e51290288ab38374260edc0788001 |

## Findings resolved during review

1. Repeating a run with an existing output previously launched the primitive before the eventual create-only write failed. The final wrapper refuses at entry before dependency/input work and process launch. An atomic `.claim` also prevents concurrent duplicate execution for the same output. Existing/stale claims fail closed. Focused regression fixtures confirm both behaviors.
2. The initial result validator did not enforce an exact top-level schema, FLINT success status or refusal-counter bounds. Final validation rejects additional claim fields, requires integer FLINT status zero and bounded nonnegative counters, and preserves all admission flags as false. The affected negative fixtures pass.

## Static API and interval serialization

The FLINT archive's actual SHA-256 was verified as `108ab51a4dd33918ff3308f0c63a63616ae30a2c174d50c9188676e85011346f`. The reviewer read the pinned declarations and the implementation of `arb_get_interval_fmpz_2exp`. Signature evidence and member hashes are recorded in `NATIVE_PINNED_HEADER_REVIEW.json`.

`arb_get_interval_fmpz_2exp(lower, upper, exponent, x)` returns the exact finite Arb midpoint-minus-radius and midpoint-plus-radius as integer mantissas with a common power-of-two exponent. The worker checks finiteness; midpoint/radius exponent and mantissa sizes; the exponent gap before the potentially allocating alignment; and final endpoint sizes. With a gap at most 4,096 bits and initial mantissas at most 4,096 bits, alignment and addition remain bounded before the final 8,192-bit acceptance check. This is exact dyadic serialization, not a decimal midpoint conversion. The Python parser reconstructs exact rational endpoints and independently checks each returned component half-width against the requested accepted radius.

Pinned APIs checked include `arf_get_fmpz_2exp`, `arf_set_fmpz_2exp`, `arf_set_mag`, `fmpz_val2`, `fmpz_bits`, `fmpq_div_2exp`, and `flint_version`. C++ uses the actual declared `Rational`, `Slice`, `Contract`, `Bivariate`, `NestedPlan`, `SharedBudget` and `Report` interfaces. This was not a syntax-only compilation with substitute headers and is not described as any form of successful build.

## Identity, target and acceptance checks

The worker reverses the same 2,592-entry index mapping, then calls immutable canonical geometry and donor constructors. It integrates the selected compact positive rectangle only, without endpoint tails or normalization. The positivity guard is made smaller for small positive cutoffs; this does not change the mathematical target or quadrature-error tolerance. Whole outer parameter balls are passed through the existing nested integration wrapper. Acceptance requires actual finite returned radii, successful Petras status and an unstopped shared budget.

The build/run wrapper re-decodes the pinned original NPZ, verifies the generated input record, immutable source dependencies, explicit external build/plan hashes, binary bytes, backend provenance and linked library bytes. Current pins include the decoder package initializer and endpoint planner/engine. Native task identity and requested index are checked against the exact plan. The frozen input and mathematical target are not inferred from a filename. Unsafe fast-math flags are not enabled.

The native subprocess has explicit memory, output-file and external wall caps. Scalar outputs use exact mantissa/exponent fields. Successful output still declares compact-interior-only scope, no endpoint, no normalization, no full-domain integral and no scientific/production admission. Byte/source identity and reported-radius validation assume source-bound native output; they are not independent re-execution. This conditional evidence contract must survive later joining and assembly.

## Executed verification and remaining limits

Fresh `python -B -m unittest -v test_driver`: **11 boundary tests passed**, no failures or errors. These tests use analytical result fixtures and refusal paths; none executes native HH calculations. The existing-output test proves no dependency or native process call occurs, and the existing-claim test confirms duplicate refusal. No native compilation was attempted by the reviewer.

Actual target-host compilation and linkage, native callback acceptance, interior feasibility, achieved radii, target source provenance and final independent scientific decision remain open. This review cannot supply those observations or substitute a single component for the complete production solver.

## Endpoint-policy pin addendum

After the endpoint arithmetic-policy revision, the dependency pin document changed to `8c76d06837320bdcb494a0412b66cde2f1722b022a5d49775b964bfa669ce23e`, binding planner `bba157ff048a8955c25c140f7d44871d9c627c5197c7d115850428a481cbeaf5`. Driver and worker source hashes above are unchanged. The reviewer reran the affected immutable-dependency test successfully and independently confirmed source identity `7f6e625c66921be84563548a9af315312050db961a5e83d4f1275e60f6c1255c`. The author's fresh full 11-test result is recorded separately in `native_driver/verification/POST_QUANTIZER_VERIFICATION.json`. The original pin/evidence documents remain historical; this change does not establish any native execution.

## Final capped-majorant dependency readback

The final endpoint planner is `53fe8cea32fb24efe9ef2682f480d63595db2bf32525ed57f46df391fe3eb4e6`, reviewed separately in `ENDPOINT_INTERIOR_MASS_CAP_REVIEW.md`. The final native pin document is `295972acff814765aacd8b15c9bcf0be00c02ce2956d09d65139c1705170a7ba`, with source identity `8fc475d86f9e496ec1f3b3bdab99bb9ad76666b3d3227ab764c735f783b6b202`. The reviewer independently reran source-pin verification and confirmed the native driver, native worker, join and assembly-exporter source hashes are unchanged. Machine-readable readback is `FINAL_DEPENDENCY_PIN_REVIEW.json`. The author's post-majorant join evidence records 10/10 tests passing with these exact dependencies. Historical pin/evidence documents remain preserved; no unrelated suite was rerun by the reviewer. Native compilation/execution and scientific admission remain unestablished.
