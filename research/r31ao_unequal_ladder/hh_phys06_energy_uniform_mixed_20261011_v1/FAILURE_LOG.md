# PHYS06 failure and limitation ledger

## Intake: zero-byte historical log

Git raw connector rejected PHYS05 `check_first.stderr` because its content is
empty. The authoritative tree records zero bytes and Git empty-blob SHA
`e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`. Exactly zero bytes were materialized
and their identity verified. Classification: connector/runtime empty-content
routing, not scientific failure. No historical suite was rerun.

## Literature access

The author-hosted Rump Acta Numerica 2010 PDF timed out through the web retrieval
tool. The publisher's primary article/abstract and bibliographic metadata were
retrieved. No claim of reading the inaccessible full PDF is made. All PHYS06
specialized theorems are derived in this package; the article is context only.

## Host capabilities

Python 3.12.14 is available. sympy, mpmath, cargo and rustc are absent from the
probed host. New reference calculations use Python standard-library exact
rationals. No local Rust compilation is claimed.

## Derivation correction before final candidate freeze

The initial energy-source summary simplified the nonphoto energy row using
stage.fHe as exactly equal to stored nHe/nH. Source inspection and independent
exact rational checks found a nonzero density-leaf difference. The active theory
retains Jnorm; the prior text, hashes and calculation transcript are preserved in
`theory/correction_history/` and `inputs/ncp_v2/`.

A second source inspection found rounded `ic(E-CHI[a])` excess-energy leaves.
The active theory restricts the ideal Gram theorem appropriately and retains the
general heat-leaf defect. A new bounded leaf check proves the defect vanishes in
all nonzero-sigma channels on the archived 33-node grid; the 100 eV HI witness
prevents a general native-source claim. No original physical source was modified
to force either identity. The archived-point diagnostic was not replayed.

## Transient execution-server transport failure

At approximately 2026-10-10 22:48 UTC, two independent read requests failed to
create a process: transport disconnected, executor key changed during session
recovery. The theory agent also observed an interrupted edit. A read-only `pwd`
probe succeeded at 22:48:27 UTC; files were inspected before resuming edits.
No completed scientific run was repeated. Classification: runtime transport,
not mathematical or physical failure.

## Reference execution

`reference_first`: exit 0, 275 assertions and 17 intentional invalid-input
rejections. No repair or repeated reference run was needed. Domain/precondition
rejections in this successful test are expected negative cases, not hidden fails.

## Delivery-locator edit

The first patch adding the exact detached-receipt Git directory contained an
unnecessary unmatched context hunk and was rejected before applying. The original
handoff hash remained `8acdafb3ce5e4470fdbb8083ce843cb839d72f973e6dbbda17cf64ea46a881c4`.
A single-hunk locator edit then succeeded. This was a document-edit failure;
no scientific code or completed calculation changed.
