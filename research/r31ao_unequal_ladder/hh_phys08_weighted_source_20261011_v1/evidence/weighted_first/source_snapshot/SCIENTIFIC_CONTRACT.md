# PHYS08 — weighted photon source directions

Frozen before the first PHYS08 scientific execution on 2026-10-11 UTC.

## Question and scope

For the two existing NCP PHYS07 first stages, can the sum of all signed photo-rate enclosures certify cooling and source-level competition with HH, although the older per-node heat condition is OPEN at node 32? Define separately the physical photo source P_N and the birth-parameter derivative P_M = partial_b F_gamma. M = partial_b incoming is a finite photon amount; it is neither the physical incoming stock N nor the source rate M/dt.

Use p=1+fhat+x+fhat*(y1+2*y2), T=C*w/p and B(v)=p*v_w-w*(v_x+fhat*v_y1+2*fhat*v_y2). fhat is the exact ratio of the captured density leaves, while stage f remains the captured fHe leaf in photo-rate conversion. C is the exact real ratio 2*ev_erg/(3*kb) of captured binary64 leaves. No scalar re-rounding of a product silently replaces these fixed real coefficients.

## Immutable source and inputs

- Repository: cosmosapjw-quantum/WU088_HH.
- Parent research delivery: e9272a1ffe0bd012e4e34718b7b2576bfd26772e; core 5cf77c2e56e9dc32596f9111620fd33de7d39e30.
- Latest NCP07 delivery: 4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b; core dfa574ce2c302ff2dce38d0e487903d57f1db977; PR #37 open at intake.
- Exact selected raw files and source provenance: inputs/ncp07/SOURCE_INTAKE_MANIFEST.json. All 81 selected raw files matched pinned Git blob SHA1 and size; 69 original-manifest members also matched SHA256. This is selective intake, not a complete NCP archive restore.
- PHYS07 archive recovery is separately attested in inputs/RECOVERY_INVENTORY.json. Its successful original scientific outputs are inherited and are not rerun.
- Only saved SOURCE_BOX, SOURCE_BOX_COMPONENTS, C2_DOMAIN, native constant leaves, PREBE and directional exports for full and first_half are used for numerical postprocessing. All 33 nodes, all three absorber channels, and every signed component used in each sum remain in the computation. Tiny positive, negative, and zero-touching enclosures are never clipped, screened or replaced by exact zero.
- Native binary64 endpoint bits define exact rational interval endpoints. Printed decimal JSON values are checked against those bits. The actual widened native X is used, not a reconstructed decimal box.
- Existing node32 OPEN witness remains byte-preserved. A new aggregate sufficient condition does not retroactively change it.

## Allowed work and bounded executions

One new Python exact-rational postprocessing run, on the two saved source exports, will assemble P_N and P_M, B/DT, HH/photo directional projections, and a bounded semantic-case oracle. The same run may evaluate a separate finite binary64 outward-rounding implementation on those fixtures and verify inclusion against exact rational expressions. The run is limited to wall 30 s, address space 256 MiB, CPU 30 s, and 8 MiB per output log/file. The tools/run_bounded.py wrapper binds all code and each actual numerical input before and after, writes stdout/stderr and EXECUTION.json to a create-only first-run directory, and preserves any failure. No unbounded loops, grid scans, transcendental source evaluations or sampling-based sign claims are allowed.

If the first run fails, preserve its code snapshot and raw failure. Classify the blocker, make only a justified targeted fix and allow at most one corrected bounded run. A second scientific failure stops execution pending a new concrete decision. Source hashes and final-code coverage must identify the tested revision. Inventory/hash/JSON readback and archival packaging are delivery checks, not additional scientific runs.

The host has Python 3.12.14. The explicit PATH inventory found neither rustc nor cargo. Rust gate and standalone tests may be authored and independently reviewed, but build and Rust execution remain NOT_BUILT/NOT_RUN here. No toolchain installation is authorized by this contract. The next NCP task is one bounded offline Rust build/test on saved fixtures; it must not repeat the NCP07 source producers.

## Scientific call ceilings and honest measurement

PHYS08 fresh PreBE, native residual, FT03, HH, provider, nonlinear root, endpoint, internal point, IVP, mixed implicit solver, finite interaction, historical suite, paired/carry and production executions all have ceiling zero. The new Python program has no bindings to those native routines. PHYS08 wrapper/diagnostic run counts are actual observations; inherited uninstrumented counters remain null rather than being recast as measured zero. NCP07 spent its two-source budget already.

## Gates and authority

1. Validate each used endpoint bit pair, finite/domain requirements, component dimensions and exact raw input hashes.
2. Assemble both source roles from their actual saved Jet slots; preserve signs and stage-f/fhat distinction.
3. Strict negative B upper endpoint gives a source-direction cooling theorem conditional on the archived source interval inclusion and fixed-coefficient family. Compute DT as a separate enclosure; never relabel a zero-touching numerical enclosure as strictly negative.
4. Use saved gradients/Hessians for source-level H_g P and P_g H. The exact identity ell*H_g P=0 follows from the HH reaction vector, not from cancellation of unrelated interval endpoints. Overlap of two representations is only a consistency diagnostic, not proof of identity.
5. Semantic fixtures include a small hot tail compatible with total cooling, a large hot tail that heats, zero/zero-touching, signed He dependence, exact positive scaling and invalid-domain/overflow cases. They do not replace native source evidence.
6. A noncreator reviewer must inspect the frozen math, source mapping, evidence and scope before scoped PROMOTE. Do not delegate final approval to the author of code, tests or theorem.

Native root authority, actual U/V/W/I, finite gas-energy interaction, carried second-half, full/two-half defect, time/continuum remainder, full49 and production remain OPEN/null. First_half begins from the same COMMON as full; it is not a carried step. This contract supplies an offline source-consumer obligation, not a native finite solver certificate.

## Delivery

Produce an additive Git research branch and scoped PR, a self-contained archive with source inputs/code/theory/results/review and the NCP handoff, uniquely named START/receipt/index/prompt files, and upload the needed bytes into both existing Drive and Dropbox backup folders. Use actual ACK/metadata identities; no self-hash cycles and no claim of downloaded-byte restore unless performed. The user must be able to start NCP using the prompt and backups without attaching a separate delivery file.
