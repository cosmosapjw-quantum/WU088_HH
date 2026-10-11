# WU088_HH PHYS09 — projected finite gas-energy interaction

Frozen before PHYS09 scientific code execution, 2026-10-11 UTC.

## Goal, motivation, and authority

Continue the HH/photo competition investigation from PHYS08. The current observable is the mixed and finite thermal-plus-ionization gas energy response on each of the two existing NCP07 first-stage families. The new obligation is to remove artificial interval dependence by applying the exact HH energy identity before the mixed-response projection, and then bound every finite-step remainder. Repeating the PHYS07 reference result or the PHYS08 weighted-source calculation is not this objective.

Latest scientific source: cosmosapjw-quantum/WU088_HH NCP07 delivery commit 4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b, source core dfa574ce2c302ff2dce38d0e487903d57f1db977. Research predecessor PHYS08 delivery 3490c77ea548fa810443b06546ba847856a7eaea. NCP08 has no observed return at intake; absence is a timestamped observation, not a claim about all future states. Its saved-data Rust task remains pending and may be included as a prerequisite in the attachment-free NCP handoff.

The user has authorized continuation, bounded local work, additive repository publication and uploads to both existing backups. No repeated approval is required. Frozen native sources, physical closures, atomic coefficients, incoming history, signs, tolerances and source-law semantics remain intact.

## Mathematical family and invariants

Gas g=(x_HII,y_HeII,y_HeIII,w[eV/H]); lambda,b in [0,1]^2. Use the actual widened native thermal-w X, centre and radius from the original source exports. The closed Banach ball Y=centre+[-radius,radius] must lie inside X. Existence is in Y; uniqueness and derivative enclosures use the entire convex X. Each admitted constant/coefficient vector is held fixed across the entire parameter rectangle. The derivative enclosures and open C2 source chart are inherited source-inclusion premises, not newly formalized proofs of the original interval kernel.

G(g,lambda,b)=g-g_old-d F(g,lambda,b), F=R+lambda H, H=q(1,0,0,-chi_H). R is saved nonphoto plus all 33 by 3 photo-rate channels minus 2 Hmean w in the thermal component. The old COMMON source, finite amount M=partial_b incoming, stage f and stored-density fhat=nHe_stored/nH remain distinct. No carried second-half is present. c,k_B,eV-to-erg leaves retain their dimensional source roles. Metric convention is (-,+,+,+), though no metric operation occurs.

ell=(chi_H, f chi_HeI, f(chi_HeI+chi_HeII),1), e=ell g, and E=ell F. The source identity ell H=ell H_g=ell H_gg=0 follows using the identical exact captured chi_H leaf. Thus assemble E directly from ell nonphoto + sum_(j,a)(heat_(j,a)+chi_a)rate_(j,a) - 2 Hmean w. Keep the exact sum of captured heat and threshold leaves; do not replace it silently by E_j. All signed nonphoto and photo derivative interval tails, including numerical lambda and lambda-b tails, enter the projected computation. Structural cancellation of the HH reaction vector is explicitly derived and is not interval clipping.

With A=G_g, U=-A^-1 G_lambda, V=-A^-1 G_b and W=-A^-1{G_lambdab+G_g_lambda V+G_g_b U+G_gg[U,V]}, include every original signed residual term. The scalar identity is

W_e=d{E_g W+E_gg[U,V]+E_g_lambda V+E_g_b U+E_lambdab}.

This is evaluated on the original thermal-w domain; no independent energy-box authority is inferred. The finite interaction I_e=e(1,1)-e(1,0)-e(0,1)+e(0,0) equals the double integral of W_e for the same C2 family. A uniform strict upper/lower bound transfers to this integral. No corner subtraction, finite difference, point root or Taylor leading coefficient substitutes for the finite bound.

## Computational plan and acceptance

Reuse the PHYS08 exact Fraction interval primitive unchanged. New code consumes pinned SOURCE_BOX, SOURCE_BOX_COMPONENTS, SOURCE_CENTRE, UNIFORM_ARITHMETIC, C2_DOMAIN and constant leaves for full and first_half. Validate every endpoint display against bits, dimensions, hashes and domain predicates. Use the saved fixed_C as an exact binary64 coefficient matrix, verify its determinant is nonzero, and form K=I-C A. Check the strict Banach inequalities using exact rational arithmetic. Enclose A^-1 s with four fixed Neumann terms sum_(k=0..3) K^k C s and a rigorous radius-weighted tail gamma^4||Cs||/(1-gamma). No iterative root search occurs.

Compute U,V,W, temperature mixed response including T_gg[U,V], direct componentwise ell[W], and the early-projected energy expression. Record all scalar contributions, including retained numerical lambda tails. Strict energy sign is a contingent research outcome, not a required assertion: a zero-containing result is OPEN and must be published honestly. Supporting mathematical-domain and interval-integrity checks are required. A semantic fixture set must distinguish a true cancellation, a sign reversal, zero-touching, matrix-feedback/tail effects, subnormal preservation and invalid domain/contraction data.

Allowed new scientific dispatch: one Python exact-arithmetic diagnostic, wall/CPU 45 s, address space 384 MiB, output file/log 16 MiB each. This includes two named saved source stages and a small fixed semantic set; no source evaluation or transcendental call is needed. Bind all code and actual numerical inputs before/after and preserve raw logs, exit, elapsed and RSS in a create-only run directory. If a concrete failure occurs, preserve first code and raw failure, classify it, and allow one targeted corrected run under the same limits. Stop identical blind retries. Serialization may save outward binary64 endpoints and bounded exact rational values; it must not silently round computation intermediates.

Existing rustc/cargo availability will be observed before claiming any build. If absent, a dependency-free Rust consumer and exact-oracle checker may be authored but remain READY_NOT_RUN here. NCP may perform one bounded offline build and one gate execution per pending PHYS08 and new PHYS09 task, with actual compiler/flags/binary/source identities. No installation, source producer replay or hidden retry. The Rust consumer must include the oracle's exact rational enclosure, not merely overlap it, and report signs from its actual endpoints.

Fresh native PreBE, residual, FT03, HH, provider, endpoint, implicit point/root, IVP, carried step, paired/full49/production and historical scientific suite calls have ceiling zero. Python/Rust postprocessors do not link to those routines. Inherited uninstrumented counters remain null rather than being converted into observed zeros.

## Decision and delivery

A noncreator reviewer examines the frozen source mapping, mathematical identities, new code, first-run evidence, claim ceilings and handoff. This review is not a rerun or recursive audit. The owner integrates corrections but does not self-approve PROMOTE. Mathematical source-family claims, exact arithmetic, runtime implementation and native issuer authority are separate. Actual native root/U/V/W/I stay null; native authority, carried second-half, full/two-half defect, time/continuum remainder, full49 and production remain OPEN.

Deliver Korean report, theorem/claims, all necessary saved source inputs, exact results and execution records, pending PHYS08 package, PHYS09 NCP code/tasks/prompt, independent decision, manifest and checksums. Publish to a new additive research branch/PR and both existing Drive/Dropbox backup folders. Every handoff dependency must be available from the Git/backup package without additional user attachments. Record actual ACK/metadata and immutable Git identities; do not claim a downloaded restore unless remote bytes were actually downloaded and checked.
