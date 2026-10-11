# PHYS09 saved-input Rust consumer interface

This is a developer interface and part of the frozen delivery. The scientific contract controls scope.

## Input

`results/projected_first/GATE_INPUTS.tsv` (or the explicitly recorded corrected run) contains a header `stage\tkey\tlo_bits\thi_bits`, then the following exact keys for each of `full` and `first_half`. Duplicate, missing, extra, malformed, nonfinite or reversed entries are errors. Binary64 bit words are lowercase 16-hex. Every interval is a captured original interval or exact point binary64 leaf; no rounded scientific result is used as an input.

- `dt`, `fHe`, `nH`, `nHe`, `kb`, `ev`, `hmean`, `chi.0` to `chi.2`: points.
- `X.i`, `center.i`, `radius.i`, `gc.i`, i=0..3. centre and radius are points.
- `C.i.j`, i,j=0..3: point matrix from saved fixed_C.
- For each prefix `G.i` (i=0..3), `NP.i` (i=0..3), `RATE.j.a` (j=0..32,a=0..2), and `HHQ`: all 57 Jet intervals using suffix `.v`, `.g.k` (k=0..6), `.h.k.l` (k,l=0..6).
- `HEAT.j.a`, j=0..32,a=0..2: captured point leaves.

The expected row count per stage is 10+16+16+108*57+99 = 6297. There are 108 Jets: G4+NP4+RATE99+HHQ1. The actual writer and reader must derive and assert the count rather than silently pad.

## Arithmetic

Use finite binary64 interval arithmetic with outward nextafter at every elementary operation. Preserve signed zeros and subnormal endpoints; reject overflow/nonfinite/reversed/divisor touching zero. Exact identity/zero inputs may have interval inflation under outward arithmetic; do not treat inflation as a native source call. No external crates, fast math, fused substitutions, clipping or tolerance.

Compute ell from exact captured leaves with outward arithmetic. Assemble energy Jet from NP and each RATE with coefficient `HEAT.j.a + chi.a`, then expansion `-2*hmean*w` with the exact linear thermal coordinate Jet. HH cancels algebraically and is not subtracted as unrelated intervals.

Set K=I-C A, A[i][j]=G.i.g.j. Use weighted gamma=max_i sum_j |Kij| radius[j]/radius[i]. beta=|C gc|; strict margins=radius-beta-|K|radius. Validate radius>0, centre+[-radius,radius] subset X, gamma<1. Validate fixed C nonsingularity (exact Python oracle establishes it; Rust may use a safely certified interval determinant not containing zero).

For each rhs s, enclose inverse action via four Neumann terms sum(k=0..3)K^k Cs and tail radius[i] * gamma^4 * norm_radius(Cs)/(1-gamma). U rhs=-G_lambda, V rhs=-G_b. W rhs is negative of G_lambdab+G_g_lambda V+G_g_b U+G_gg[U,V]. Preserve every signed raw term.

Compute direct ell W; projected components `feedback=d E_g W`, `hessian=d E_gg[U,V]`, `lambda_gradient_tail=d E_g_lambda V`, `birth_gradient=d E_g_b U`, `lambda_birth_tail=d E_lambdab`; their sum is projected W_e. Compute mixed T if convenient, but required Rust comparison fields below are sufficient for this gate.

## Output and exact oracle

JSONL stdout: one `{"type":"semantic_checks",...}` row; one `{"type":"stage","stage":"full",...}` and one first_half row; one `{"type":"summary",...}` row. Each scalar interval object uses `lo_bits`, `hi_bits`, and `sign` equal to STRICT_NEGATIVE / STRICT_POSITIVE / ZERO_CONTAINING as determined from actual endpoints. Output fields per stage: `gamma` interval, `margins` length4, `U`,`V`,`W` length4, `direct_energy`, `projected_energy`, `energy_terms` keyed as above, and `det_C` interval.

Python `GOLDEN_ORACLE.json` schema has `stages` list with corresponding fields, exact rational lo/hi pairs, plus original input file/manifest identities. The consumer must prove each Rust enclosure contains the exact rational oracle enclosure, with exact Fraction comparisons. Mere overlap is not acceptance. Endpoint sign labels are checked; strict source-stage projected energy claims are only made if the actual Rust upper bound is below zero. Semantic tests distinguish cancellation, positive/negative/zero-touching, retained signed subnormal input, a nontrivial inverse-tail enclosure, and rejection of invalid domain/contraction data. They do not establish native root authority.

NCP wrapper: existing rustc -vV once, one offline build (60s,512MiB), one gate (15s,256MiB), one consumer (15s,256MiB), logs/output <=16MiB each. Create-only run directory, code/input and binary hashes before/after, raw stdout/stderr, actual elapsed/RSS/exit, no automatic retry or installation. Output includes HOST.json, per-command EXECUTION.json, ORACLE_CHECK.json, PROJECTED_ENERGY_SIDECAR.json, NCP_RUN.json; actual native root/U/V/W/I and authority remain null/false. PHYS08 pending task is managed by handoff separately and is not automatically called by this wrapper.
