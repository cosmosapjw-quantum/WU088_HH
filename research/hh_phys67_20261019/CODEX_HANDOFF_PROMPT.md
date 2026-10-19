# WU088_HH PHYS67 continuation

Continue with physmath-research-loop 1.0.0. Read REPORT_KO.md, NEXT_DAG.json,
recovery/ARTIFACT_RECONCILIATION.json, first_born/PROOF.md and the latest
publication receipts before doing new computation. Keep derivation, code,
verification, actual scientific execution, NCP submission, Git publication,
backup and DAG states separate.

The scientific base is PR115 445d82db9c42b4f2f81e4ac1b107dec3b69b3c24.
Our actual Git parent is PR116 1a1e5b6df5e5f88de851bc4686949089e2444291,
which only added a historical artifact-access blocker. The final requested
993317b1 ZIP and 2d08f8da snapshot remain BLOCKED_ARTIFACT_ACCESS_EXACT_FINAL_VERSION.
The independently recovered earlier 84c29de7 ZIP has 91 verified payloads
and an 84-new-path patch. The recovery branch is built on actual PR116;
do not claim the earlier local 3794ac6b snapshot is a GitHub descendant.
Read publication/PUBLICATION.json for the actual new remote commit/PR.

Preserve atomic coordinates, B27, k7/10, E49/200 Hartree, R7/10,
h=-Delta/2-1/r-(1+1/d)exp(-2d), d=|x-R zhat|,
eta=Fy, xi=Fy-phi, eta_C=-10/7, H+=G+iF and Z=+u'u^-1.
Frozen NPZ SHA256:
f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
PHYS63 qualitative all-angular real-axis LAP/Poisson/DtN is ESTABLISHED.
PR114 finite-L64 all-r ratio/Born and PR115 order-specific radial cutoffs
are preserved. Do not replace the remote PHYS65 proof with an old local one.

Reuse, do not rerun:

- PHYS64 2 smoke +18 extended, original results ZIP d7fa0b50ed803e19dfcec8f781219c03acbd21f8f3ee47fe922754f8fdb5ea79; prior 149 payload/20 successes are accepted.
- Prior PHYS66 pilot and process smoke/resume; present first_born/EXISTING_PILOT_COMPARISON.json already certifies the stored pilot's individual D1 error.
- PHYS67 exact-Gauss angular bound, 20 Coulomb point certificates and the successful full-radial D1(21,20),m0 enclosure. Actual numerical radius <2.328e-41, analytic tail <4.973e-53 a0^-1.
- 57 recovered focused tests and 71 new focused tests are passed in the recorded environment. Use hash-bound validation; do not repeat a historical full suite for unchanged premises.

NCP longtail has six fully specified L28/64 × T55/65/75 cases. The runner
capsule SHA is 34a59dfe3158c454811ed6e6f47c82357e502ef8cdef9ee5f14640b37f73a835.
Its fresh-extract preflight passed. Consult the actual NCP receipt before
submission; inspect and reuse any matching successful campaign first.
The completed runner and commands are in ncp_delivery. NCP receives code
and exact requests, not a request to invent solver design.

Next bounded science: implement validated D1 radial profiles for m0,
ell0..28, then enclose the original finite-L28 D2(21,20) with every
intermediate j=0..28. Start from the exact m0 angular Laurent kernel and
outgoing_h_acb. Use a validated Volterra/profile or residual propagation
scheme, not unbounded interpolation of point certificates. Keep profile,
angular evaluation, Coulomb, integration, roundoff and PR115 radial tail
components explicit. First establish a concrete absolute budget and
prove that returned enclosures meet it. Reuse the existing noncertifying
D2 estimate only as a diagnostic target.

After that, address excluded-angular response and connect the original
source-driven xi, regular origin and incoming adjoint to sigma(E) and
Maxwellian k_HH(T). A single first-order element has no intermediate
angular sum; this does not settle higher-order excluded-channel bounds.
Do not assert a general no-go from a failed precision probe or open
certificate. HH_R10 remains OFF. Publish additive draft work, preserve
historical evidence, and bind actual cloud acknowledgements after success.
