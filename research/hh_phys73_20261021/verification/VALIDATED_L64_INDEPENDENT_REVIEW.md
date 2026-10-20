# PHYS73 validated L64: independent scientific and code review

Reviewer: optimization_theory, independently of the fresh_intake author.
Reviewed scientific driver SHA256:
`41c9c1410070a9bcf161ca497978b21bac7788bb312b7396fdd4e3298e6c6aa4`.
Review scope is the new split/reuse/assembly dependency. No old numerical
campaign was re-executed. Any later write-only revision is identified below
or in its separate receipt rather than relabeling the executed source.

## Decision

**PASS for the scientific split, inherited-evidence reuse, exact error
assembly and fixed-goal decisions. Full L64 execution is pending.**

The original `research/hh_phys68_20261019/ncp_delivery/REQUEST_L64.json`
requests finite L64, external (21,20), m=0, B27/T65, half-width1/8,
zero-free radius1/4, majorant radius2, degree96, precision768bits and
angular coefficient precision2048bits. The new j37..64 requests retain
those settings. The original D1 goal1e-45 and D2 goal1e-62 remain exact
Fraction thresholds in the final certificate and exit decision.

## Mathematical correspondence

The normalized Coulomb ratio is F_j(r)=H_j^+(r)/H_j^+(B), hence F_j(B)=1.
For each requested pair,

\[
 q_{aj}(r)=\int_r^{65}F_a(t)F_j(t)V_{aj}(t)\,dt,
 \qquad D_{1,aj}^{65}(B)=q_{aj}(B),
\]

and the original second Born coefficient is

\[
 D_{2,21,20}^{L64,65}(B)=
 \sum_{j=0}^{64}\int_B^{65}
 \frac{q_{21,j}(r)q_{20,j}(r)}{F_j(r)^2}\,dr.
\]

Thus every summand depends only on its own two Volterra primitives. The
28 new one-j jobs are mathematically independent. Their addition uses
complex bilinear products from the unchanged validated kernel; there is
no conjugation, added factor2, or factorial.

PHYS68 supplies j0..28 and PHYS69 supplies j29..36 at the same exact B,
T, outgoing normalization, potential and external pair. Their older
meshes/precisions produce certified enclosures of those same mathematical
summands. Reusing these enclosures preserves the L64 target even though
their meshes differ from the new request. It does not imply that the old
profiles had been generated at768bits. The additive assembly retains their
actual radii and pins their exact certificate bytes.

The old57 unique pairs plus16 band pairs plus56 new pairs give129. The
dict key coverage check enforces precisely the unordered pairs
{(20,j),(21,j):j=0..64}, counting the shared pair(20,21) once. The endpoint
normalization above justifies merging old `D1_B_cutoff` and band
`D1_q_B_cutoff` without an extra F factor.

## Error assembly and actual read-only arithmetic

`combine_boxes` sums dyadic midpoints and component radii as Fractions,
adds one full-L64 radial beta2, rounds the displayed midpoint, and charges
the exact difference between its rational midpoint and the displayed
decimal. The sum of rectangular component radii bounds complex absolute
error. The D1 decision uses exact dyadic midpoint authority and adds one
beta1 per pair; no uncharged rounded D1 center is claimed.

The code reads cutoff boxes, not previously radial-inflated full-result
error totals. Consequently it does not add old radial tails a second time.
The finite-L64 radial proof implementation is itself pinned through the
inherited engine. It is used for finite L64 only; no infinite-j bound is
replaced by this finite constant.

A separate read-only calculation decoded the two stored certificates and
evaluated only the exact analytic radial budget. The exact fractions are
saved in `VALIDATED_L64_INDEPENDENT_ARITHMETIC.json`. Readable values:

| Component | Value |
|---|---:|
| j0..28 inherited numerical D2 radius | 8.228100454490794e-67 |
| j29..36 inherited numerical D2 radius | 3.164889152292244e-71 |
| One L64 beta1(T65) | 4.789119177450072e-52 |
| One L64 beta2(T65) | 7.541138621579980e-66 |
| Sum of28 allocated new-mode budgets | 2.8e-63 |
| Combined budget before final display | 2.808363980315921e-63 |
| Remaining headroom before display | 7.191636019684078e-63 |

The headroom calculation assumes every new mode meets its allocated
1e-64 numerical budget. The actual final acceptance uses the actual
stored boxes and display error, so neither this allocation nor a per-mode
success is substituted for the final D1/D2 decisions. The largest inherited
D1 error after one L64 beta1 is below1e-45. New D1 errors remain to be
measured; failure of even one prevents `CERTIFIED_GOALS_MET`.

## Workchain and execution evidence

The new verifier binds the one-j request, source and numerical engine,
then requires all152 consecutive panels, exact panel coordinates, two
pair rows, one intermediate-j term, positive zero-free lower endpoints,
predecessor serialization hashes and enclosing right/left carries. It
checks that the final D2 box encloses the exact sum of saved increments.
A completed mode goes through this verifier and returns without invoking
the numerical integration kernel or rewriting its certificate.

The author's11 focused tests already passed. They include a complete
synthetic152-panel chain for reuse behavior and corrupted-chain rejection;
that fixture is labelled synthetic and is not a physical result. This
review did not repeat those tests solely to re-establish them.

The reviewer separately read the actual new j37 panel and its partial
certificate: exactly one panel, [259/4,65], zero terminal q carry,
`PARTIAL_CHECKPOINT`, no D2_B_cutoff/full-L64 certificate. Thus the actual
new panel demonstrates a kernel/runtime application, while the complete
152-panel chain and 28-mode scientific return remain NCP obligations.

This independent review ran zero new numerical integrations, zero old
integrations and zero special-function evaluations. It performed source
reads, exact rational assembly and one new partial-output readback.

## Operational finding and verified resolution

**Finding L64-WRITE-1:** the initially reviewed exclusive-create text
writer can leave a truncated REQUEST, aggregate or invocation file if the
wall-limited process is interrupted during the write. It rejects that
file safely on resume, but automatic continuation would then need a small
file repair. **Resolved:** the revised writer uses a same-directory
temporary file, flush/fsync, atomic no-replace link and directory fsync.
An incomplete pre-publication REQUEST temporary is ignored only when it
is an ordinary file matching the writer's exact name pattern; its bytes
are never parsed or promoted. The existing immutable target cannot be
overwritten by this writer.

The independently rechecked revised driver SHA256 is
`12348bfe8810807d7ede7bd7fff605ca4afd1584a36addc76f8c15c3fcb2cd6d`.
`validated_l64/ATOMIC_WRITER_INDEPENDENT_REVIEW.json` records an actual
AST comparison: replacing `write_new` and only the precise REQUEST
temporary guard makes the entire revised module equal to the preserved
executed snapshot. Scientific functions are unchanged. The author ran
14 focused tests including collision, injected pre-link interruption and
leftover-REQUEST retry; their receipt and log SHA were read and checked.
The reviewer did not repeat unchanged scientific or fixture tests.

The one real panel remains bound to the preserved pre-atomic driver
snapshot. It is an immutable verification artifact, not a resume target
for the revised campaign binding. No new integration was performed to
check this filesystem correction. Finding L64-WRITE-1 is closed.

No scientific critical finding remains. The optional finite-L64 extension
does not reopen the completed PHYS69 all-angular D2, PHYS71 D3 or PHYS72
operator remainder. Original source/origin/observable claims are not
attached to this coefficient certificate. HH_R10 remains OFF.
