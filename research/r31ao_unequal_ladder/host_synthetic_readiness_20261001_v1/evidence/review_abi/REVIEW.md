# Bounded independent ABI witness review

No material unresolved defect found in the final collector and tests. **Pass within current-host synthetic scope.** Historical ABI admission remains false and B03 remains `RAW_ABI_AUTHORITY_BLOCKED`.

Reviewed `abi_witness.py` SHA256 `4ca229ad202a535ccca52b8df6b296b44f25c33fdb7ed0465c113e97b2928125` and `test_abi_witness.py` SHA256 `6b525d4f7a3e6afe8065bcf24707406e019e6e0a46b80fd0c6f1e70cfacdc941`. Target hashes were unchanged before and after execution. The reviewer did not modify these files.

| Requirement | Fresh evidence | Result |
| --- | --- | --- |
| Exact values, signed zero, complex component placement | Independent integer interpretation of 96 real components in 8 generated arrays | Pass |
| C/F logical indexing and reversible hex transport | All four scalar/complex dtypes in both orders; raw/payload hashes checked | Pass |
| Historical identity boundary | Complete-looking reference object still requires review; self-hash and wrong pins refused | Pass |
| Resource and output boundaries | Existing tests plus four small independent refusal checks; observed complete output 59,215 bytes | Pass |
| Actual serializer source identity | Current `_format_impl.py` and `_npyio_impl.py` hashes in generated witness | Pass for current environment only |

`focused_suite.log` records **14 tests passing, zero skipped**. `independent_check.log` records the separate bit-level oracle; `resource_check.log` records four refusal checks. Commands, interpreter, exit codes, timings, and hashes are in `EXECUTION.json`, `RESOURCE_EXECUTION.json`, and `REVIEW.json`. Each executed process had an external 20-second timeout and 1,024 MiB address-space limit.

The observed runtime is Python 3.12.14 / NumPy 2.3.5 on little-endian x86_64. This directly exercised binary64 and x87 extended components. It does not establish big-endian or IEEE binary128 host behavior, or any historical NumPy build identity. Current format agreement and source-file hash agreement are insufficient for historical output-to-runtime linkage.

The author corrected serializer wrapper/source identification before this final review. The final witness records actual callable implementation paths; the review asserts only current runtime identity. The old authority was read as metadata; archived scientific payloads were not opened or decoded.

Project-level `independent_review_admitted=false`, `historical_layout_admitted=false`, and `reference_contents_verified=false`; `rigorous=false`, epsilon/eta remain null. No actual HH payload, native build, integral, callback, or scientific comparator was run. This reviewer authored G3 previously; G3 is outside this review target and receives no independent-review claim here.

The scripts are bounded review evidence and create their witness directory only once. Re-execution of the independent probe requires a fresh output location; existing evidence is not overwritten by the collector.
