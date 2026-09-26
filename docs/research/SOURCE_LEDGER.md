# Source ledger

## User and project authorities

- User current request: execute research/coding optimization loops, preserve local-heavy vs sandbox-light division, publish to cosmosapjw-quantum/WU088_HH.
- R31K_A_ANCHOR_HEAVY_SUMMARY.json: the uploaded exact summary. Ten seals and identities remain the source of array provenance.
- Summary bundle SHA256: dea1f071c7ff218e87c1367144ba19f4f065c2f4ac81f751a42756ec8d7c02b3. Retrieved from the user's Dropbox through Files materialization, not reconstructed from terminal text.
- Original seed SHA256: 2d81f75dec9e1e94a12eadbb597483391d0718ec304ba6b4d82daa3911c6d256.
- Frozen driver SHA256: 5add2f769bdaa9721ce1fe90dd02a2c6dd6a2b3c617b6eeec0032bd38849acb6.
- Research harness: physmath-research-harness-gpt6-astra-v4.0.0-20260908.zip, SHA256 dae76c90f2e5d691bcdd595dadbe470bacacba3bb2a036ff9788ffe7d3bfabb7.
- Coding harness: physmath-coding-harness-gpt6-astra-v4.0.0-20260908.zip, SHA256 dc99e7ab2f9629dcce3ec0758d97e19acc5b645f86e208d1b338bb6430ff8d7a.
- The two harnesses are read from separate directories. An initial common extraction would overwrite common filenames; separate exact extraction was used for authoritative reads.

## Primary public sources checked on 2026-09-26

- https://arxiv.org/abs/1702.06784 : Fedorov, shifted correlated Gaussians. Abstract/metadata only in this turn; discovery source, not full-text numerical validation.
- https://arxiv.org/html/2407.17221v1 : Fedorov et al., tensor-prefactor correlated Gaussians. Sections2–4 support parameter/shift generation of analytic overlap/Coulomb matrix elements. The present fixed Hylleraas/ETF implementation is not certified by this paper.
- https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html : strict floating-point versus transformations enabled by unsafe flags. Actual optimization diagnostics are also preserved in the build records.
- https://www.openmp.org/spec-html/5.1/openmpsu48.html : worksharing-loop scheduling. Project reproducibility comes from private per-plane sums and canonical serial merge, not merely from schedule choice.
- https://rclone.org/commands/rclone_copyto/ : transport semantics. Copy success alone is not raw byte verification; project helpers additionally read the object back and compare SHA256/size.

SciSpace additionally surfaced Geursen2023, Harris2018 and Padhy2019. These were abstract-level method candidates, not newly imported physical authority. No paper-derived target value was inserted into the anchor arrays.

## Tool-level distinctions

Wolfram produced exact zero residuals for the displayed low-order moment/Boys/phase identities. A first evaluator response also carried undefined-symbol warnings; those are preserved in WOLFRAM_SYMBOLIC_CHECKS.json. These checks are not formal proof-assistant verification. mpmath80 provides the separate scalar recurrence counterexample.

GitHub metadata showed an empty public repository with user push permission. The connector exposes read actions only; that is distinct from repository permission. Git DNS/transport failure and final push result are recorded separately. No bearer download URL, credential or rclone token is committed.
