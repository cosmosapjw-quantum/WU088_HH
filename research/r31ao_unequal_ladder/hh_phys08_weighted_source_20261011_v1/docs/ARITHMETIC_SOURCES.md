# Arithmetic source notes

The weighted theorem is derived from the pinned project source graph, not a new empirical physics fit. See inputs/ncp07/raw/candidate/src/hh_primary_extension.rs, phys04_mixed.rs, phys04_transport.rs and inputs/ncp07/raw/src/sourcebox.rs. Scientific source identities are in the intake manifest.

Primary language documentation consulted 2026-10-11:

- Python fractions: https://docs.python.org/3.13/library/fractions.html . A float input preserves its binary rational value; it is not converted to the visually similar decimal fraction. Actual executed host was Python 3.12.14, as recorded in HOST_AND_HARNESS and EXECUTION. The executed code uses the longstanding Fraction(float) and integer arithmetic APIs.
- Rust f64: https://doc.rust-lang.org/std/primitive.f64.html . Bit representation, finite/subnormal distinctions and adjacent representable values support the gate design. This consultation does not attest a Rust build or the local floating-point mode. The gate includes runtime probes and rejects observed unsupported arithmetic; correctness still assumes ordinary IEEE binary64 operations without unsafe fast-math.

All reported source numbers come from the saved local evidence identified in WEIGHTED_RESULTS.json. No external documentation substitutes for those source arrays or a target-host run.
