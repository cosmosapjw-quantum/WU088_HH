# PHYS72 integration review

Review date: 2026-10-20 UTC. This is an independent read-only review of the
new PHYS72 integration code and saved execution evidence. It does not rerun
PHYS71 verifiers, panels, profiles, or numerical integrals. The review itself
performed no scientific execution.

## 1. Exact third-and-higher enclosure: accepted within its stated scope

Reviewed sources are `implementation/third_and_higher.py` and its imported
`implementation/bounds.py`, with the three adopted files under `inputs/`.
The enclosure execution receipt identifies source SHA-256
`b7550342bdc8b9f19ac7db5d6bafd327954738703065e26bc12d8927f886a6ab`
and exact-bounds source SHA-256
`2036fc4b0d76a825d98e3ea3f2342c67c3029f4ed6fbe67686c1d70042762e7c`.

The code checks all three input byte identities before parsing or adopting
the displayed enclosure:

| Input | Required SHA-256 |
|---|---|
| Frozen NPZ | `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d` |
| Corrected PHYS71 certificate | `f75d082e1966dd61a326c37b6ff14e8f330e010341a59a88eb4ca8d4734e6173` |
| PHYS71 displayed result | `b22a110aa08e44fd9560da215ff5955ab138586a37016c1578bd48ea96be1a47` |

These are identity guards for reuse of accepted evidence; they are not a
claim that the old numerical campaign was rerun. The displayed-result
schema, certificate reference, unit `a0^-1`, and `HH_R10=OFF` are also
checked. The center and error values are parsed as exact `Fraction` values.
The originally displayed decimal center strings are copied without a new
rounding step.

The adopted PHYS71 radius `7.121295358370E-79` already encloses printing
error. The code adds the PHYS72 order-four-and-higher radius once, and does
not add the old printing error a second time. The exact bound routine uses

\[
q=5.53311\times10^{-21},\qquad
R_{\ge4}=\frac{5929\delta}{2}\frac{q^3}{1-q},\qquad
\delta=3\times10^{-23}.
\]

The power is correct for retaining the coefficients through order three:
in general the tail after order `N` is
`(5929*delta/2)*abs(lambda)*(abs(lambda)*q)**N/(1-abs(lambda)*q)`.
It therefore contains `abs(lambda)**(N+1)`. The value `5929=77^2` is the
fixed exterior Poisson normalization for the two requested indices 21 and
20; it is not a substitute for an infinite-angular Green bound. The
infinite-angular bound enters independently through the proved sandwich
norm `q`.

The resulting enclosure applies precisely to

\[
[(Z_1-Z_0)-D_1-D_2]_{21,20,m=0},
\]

where the subtracted `D1` and `D2` are exact coefficients. Its center is the
unchanged PHYS71 `D3` center and its outward radius is
`7.271949342749E-79 a0^-1`, below `1E-78 a0^-1`. The output explicitly states
that a full numerical `Delta Z` enclosure has not been assembled; that
assembly would additionally require the `D1` and `D2` radii and any new
sum-display rounding. It also keeps the driven-source `xi` obligation
separate from this boundary-operator result.

The saved actual execution `THIRD_AND_HIGHER_EXECUTION.json` reports return
code zero, 0.06658712100033881 seconds, and output SHA-256
`94d3b4296c5cbb8d2aaa0f8e410f5840bbbc708831393a278e9b7033d481285e`.
The reviewer read that output and receipt; no second execution was made.
The output reports zero old-panel integrations, zero inherited-profile
integrations, zero new physical integrations, zero old-verifier runs, and
`HH_R10=OFF`.

## 2. Native formulas and scientific authority: correct separation

The initial native source reviewed was
`native/phys72_bounds.f90`, SHA-256
`0d2630204a8758258a3f50f1ac4ed82a79901d33e990ad752412fc6d876e7cc2`;
the initial wrapper was `ncp_delivery/run_native.py`, SHA-256
`35c44f02ee2a54d3d2fc831981682b874f9354716354c8f14c90c922826dc227`.
The formulas for `delta`, `Cstar`, `q`, the fixed-entry prefactor, the
contraction, and the geometric remainder agree with the exact Python
formulas. The native output and wrapper receipt correctly label the
calculation as a rounded scalar cross-check with `certified: false` or
`native_certified: false`; exact `Fraction` arithmetic remains the
certificate authority. A binary128 rounded denominator near the exact
boundary may choose a different branch, and that native branch must not
override the exact acceptance decision.

The wrapper preserves each command, exit status, stdout/stderr, hashes,
elapsed time, compiler or supplied-binary identity, and exact authority in
a create-only directory. The reviewed `native_attempt_02/EXECUTION.json`
reports successful compilation and a successful scalar native run, with
`native_certified: false`, zero physical integrations, and `HH_R10=OFF`.
Its reported agreement is diagnostic evidence, not an interval proof of
the analytic theorem.

## 3. Concrete native parsing findings at initial review

Two implementation findings were reported to the primary agent before
publication:

1. The direct Fortran CLI used list-directed reads for both arguments.
   Such reads accept inputs outside the advertised single decimal/integer
   token grammar, including extra list items and slash termination. A
   lexical check must precede each read if the direct CLI is supported.
2. The wrapper accepted any parseable JSON object returned by `--binary`
   without validating the native schema, `certified: false`, `HH_R10`,
   zero physical-integration declaration, retained-order echo, or finite
   numeric fields. It also did not convert malformed native JSON into a
   finalized failed execution receipt. Successful process exit alone is
   insufficient for accepting a native cross-check result. The wrapper
   should reject inconsistent output and preserve the failure receipt.

Neither finding changes the exact enclosure in section 1. They concern
the reliability of the optional native diagnostic and its receipt. The
primary agent assigned a narrow fix and focused regression to a separate
agent; its corrected lines and new evidence will be reviewed in an
addendum. Existing native receipts retain their original source hashes
and are not relabeled as executions of a revised source.

## 4. Review execution provenance

This review used file reads and saved evidence only. One read attempt
encountered `exec-server transport disconnected` with `SERVICE_ERROR`;
the subsequent read succeeded. This was a transient tool transport event,
not a scientific or compiler failure. It is not counted as an additional
scientific run, and no failed scientific result has been omitted.

Initial disposition: exact third-and-higher enclosure accepted within its
explicit scope; native scalar formulas accepted as diagnostics; the two
native input/output validation findings await the narrow correction
review described above. This initial native disposition is superseded by
the completed addendum below.

## 5. Correction review addendum: both native findings closed

The corrected source lines were read independently, without executing
them again. The final reviewed Fortran SHA-256 is
`dcde24319db227201ec8654623731077319d2bd08ec75a8569623a6ad047212d`;
the final reviewed wrapper SHA-256 is
`2a9965c90ffbf7df01627b1e744821b26b0d98ff8ff379cb59f1eb7a6978df5a`.

The Fortran CLI now validates each entire decimal/integer argument before
list-directed conversion. Slash termination, multiple list items,
whitespace suffixes, and non-decimal forms therefore cannot be accepted
as a single advertised token. It emits a separate exact decimal-input
echo in addition to its rounded binary128 value.

The wrapper now checks schema, authority, `certified: false`, `HH_R10=OFF`,
zero physical integrations, the requested retained order, exact decimal
input echo, binary128 metadata, and finite nonnegative decimal output
fields. It checks that the rounded lambda agrees with the sent value
within an explicitly diagnostic rounding allowance. It also validates
the finite-tail, underflow, and nonpositive-denominator status branches.
Invalid native output produces a finalized `NATIVE_PAYLOAD_INVALID`
receipt, preserving the already captured process stdout/stderr and
execution record. The exact authority remains independent of all these
rounded checks.

The reviewer read the narrow regression source
`verification/native_contract_audit.py`, its saved report
`verification/native_contract_audit/AUDIT.json`, and the corrected
compile/default-run receipt
`verification/native_contract_fixed/EXECUTION.json`. Their reported
source and binary identities agree. The two evidence-file SHA-256 values
were also checked directly from the saved files:

| Evidence | SHA-256 |
|---|---|
| Contract audit | `8b18e2319c6de2a37c1af8e488cd1a8548fc1b9d8bb4a8dff40b53a6c41f5add` |
| Corrected compile/default-run receipt | `26a40e8e95cce7f1d2034e6e1fede9a55e5d0efa2f306c77aff2fd9a0ae1c118` |

The audit records 19 successful scoped checks: acceptance of the actual
corrected default payload; rejection of six malformed direct CLI calls;
rejection of ten inconsistent payload variants; a successful native
nonpositive-denominator diagnostic with a null tail; and rejection,
through the actual runner's `--binary` path, of an otherwise valid payload
echoing the wrong retained order. The last rejection leaves the expected
failed receipt. The corrected default run compiled and executed
successfully, and its receipt marks native payload validation as passed.
This addendum read those existing results; it did not rerun them.

Final disposition: the exact third-and-higher enclosure is accepted
within section 1's explicit mathematical and error-accounting scope.
The optional native implementation and runner are accepted as rounded
scalar diagnostics after closure of the two identified validation
findings. No remaining issue was found in this scoped integration
review. This review does not promote a point check, a native floating
result, or a regression test into the all-angular analytic proof, and it
does not claim a full numerical `Delta Z` or driven-source `xi`
certificate.
