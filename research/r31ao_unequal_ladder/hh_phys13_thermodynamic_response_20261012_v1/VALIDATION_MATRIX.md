# PHYS13 validation matrix

| Requirement | Actual evidence | Status |
|---|---|---|
| Source-aligned temperature/electron definition | Captured ft03_interval and coupled_primary source plus leaves; SOURCE_IDENTITY.json | PASS, inherited interval-source premises retained |
| Same-family finite response | FTC derivation on fixed-alpha C2 branch, exact U readout | PASS within stated family |
| Positive p, Ue; negative Uw and UT | thermo_v2 exact endpoints, both stages | PASS |
| Root value enclosure | gc ± (beta+B r), positive inherited margins | PASS, no new root solve |
| Correlated cooling fraction | First energy projection and positive weighted-average theorem | PASS |
| Birth heating/cooling distinction | Vw>0, Ve>0, Vw/Ve < w/P, VT<0 | PASS |
| Output-normalization bridge | Same-g factored exact response, equal-normalization limit | PASS |
| Independent arithmetic and decision | Separate implementation, 196 assertions incl. 86 outward-display checks and 8 small semantic cases, review/DECISION.json | PROMOTE_SCOPED |
| Native roots, actual second_half, continuum/time convergence | Outside this new postprocessing scope; not executed | NOT_EVALUATED |
| Consumer applicability and global RUX completion | No actual consumer bound in targeted intake | NOT_EVALUATED |
| PDF layout and references | Seven rendered pages; no missing glyph or overfull box; REPORT_QA.json | PASS |

Two actual first-stage source families were evaluated. Assertion counts are not additional independent physical cases. First and second postprocessing executions both succeeded; the second added a birth-response physical criterion and preserved every previous result exactly. Reviewer environment events are retained separately from scientific failures.
