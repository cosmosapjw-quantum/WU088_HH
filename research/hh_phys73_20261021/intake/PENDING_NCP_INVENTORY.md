# Pending NCP jobs and validated L64 reuse

## Jobs that still need an actual host return

The six PHYS66 longtail requests are `L28_T55`, `L28_T65`, `L28_T75`, `L64_T55`, `L64_T65`, and `L64_T75`. Each has `m=0, join=39, orders=3, nodes=128, rtol=2e-11, max_step=0.25`. Their exact request records are in `PENDING_NCP_INVENTORY.json` and originally in `research/hh_phys67_20261019/ncp_delivery/REQUESTS_LONGTAIL.json`.

The inherited PHYS64 extended 18-case ledger contains cutoffs 35/39/43. No complete request in that ledger equals one of these six. Earlier PHYS66 smoke cases have only two selected modes, so they also do not replace the full L28/L64 longtail matrix requests. Six jobs can run independently. A change in case scheduling does not change per-case quadrature, tolerances, order, physics, or acceptance.

These runs return binary64 diagnostics. Their existing gates are second-order quadrature relative defect at most 2e-7 and transpose-symmetry defect at most 1e-10. Numerical total-error certification is a separate property.

The old PHYS69 native L64 request is **exactly equal** to `physics_request` inside the completed PHYS70 optimized L64 request. PR123 supplies its actual optimized return. Running the superseded native implementation again would add a duplicate same-physics case, so the new batch reuses that result.

## Validated L64 extension without old integration

The original PHYS68 L64 runner integrates every intermediate mode 0..64. Since PHYS68 already completed 0..28 and PHYS69 completed 29..36, the new driver computes only 37..64. This is a finite-L64 numerical extension of the completed all-angular D2 result. It does not reopen PHYS69.

For normalized outgoing Coulomb functions \(F_j(B)=1\), the exact cutoff primitives obey

\[
q_{aj}'(r)=-F_a(r)F_j(r)V_{aj}(r),\qquad q_{aj}(65)=0,
\]

and

\[
D_{2,[0,64],65}(B)=\sum_{j=0}^{64}\int_B^{65}
\frac{q_{21,j}(r)q_{20,j}(r)}{F_j(r)^2}\,dr .
\]

Each intermediate-j summand requires only its own two backward primitives. Thus 28 one-j jobs are mathematically independent. The existing validated kernel is reused byte-for-byte. Each new job preserves the original L64 parameters `h=1/8, rho=1/4, R=2, degree96, precision768bits, coefficient2048bits, T65`. There are 152 new radial panels per mode, 4256 new panels in the full extension.

The exact sum reuses the two immutable certificates:

- PHYS68 L28: SHA256 `ddaae206009a276def281af5526851ceb717baf2e0de5f8472552a9db340de9a`.
- PHYS69 j29..36: SHA256 `e123f084bea390a25162826f306c115d683b7c9fd3157b15967c88814787d0c8`.

No old profile is re-integrated and no old certificate is rewritten. The old 73 unique D1 row pairs plus 56 new pairs give 129 unique pairs for the two external rows over 0..64.

The final error is

\[
\epsilon_{2}=\epsilon_{\mathrm{old},0:28}
+\epsilon_{\mathrm{old},29:36}
+\sum_{j=37}^{64}\epsilon_j
+\beta_{2,L64}(65)+\epsilon_{\mathrm{display}} .
\]

Only the numerical radii of inherited cutoff certificates enter this sum. One full-L64 radial beta2 is then added. Each D1 pair uses its saved cutoff radius plus one L64 beta1. Exact Fraction arithmetic decides the original goals 1e-62 for D2 and 1e-45 for D1. The 1e-64 per-new-mode budget is an internal allocation, with the final global goal checked explicitly.

This finite-L64 radial estimate does not replace the growing all-j Coulomb constants. PHYS72's all-angular operator bounds and remainder remain a separately completed input.

## Implemented execution contract

```bash
python3 research/hh_phys73_20261021/implementation/validated_l64.py \
  --out runs/phys73/validated_l64 --workers 28 --worker-memory-gib 2 --run
```

Without `--run`, the command reads pinned inputs and prints a plan. It evaluates no special function, integrates no panel, and creates no output directory.

FLINT's global precision state is isolated in separate processes. Each worker has one BLAS thread and a Linux 2 GiB address-space ceiling by default. Twenty-eight workers have a 56 GiB aggregate address-space ceiling. The master launcher can schedule the six 4 GiB longtail jobs concurrently within its host resource plan; the validated driver does not claim to have measured 64-core speedup.

A successful complete mode is checked by an exact saved-payload/chain verifier and reused without entering the integration kernel or changing its certificate. Partial modes resume through the existing source/request/engine/runtime binding. A changed binding is rejected for explicit reconciliation.

The master must require `<out>/CERTIFICATE.json` with:

- `schema == PHYS73_VALIDATED_L64_CERTIFICATE_V1`;
- `status == CERTIFIED_GOALS_MET`;
- `D1_goal_met == true`;
- `D2.goal_met == true`.

A bounded partial invocation can exit 0 while its status is `PARTIAL_CHECKPOINT_NO_FINAL_CERTIFICATE`; it creates no aggregate certificate. A valid complete enclosure that fails a fixed goal has `VALID_ENCLOSURE_GOAL_NOT_MET` and exits 2.

## Actual sandbox work

Fourteen focused tests passed. They include exact error composition, global-goal boundary decisions, mode coverage, 129-pair assembly, a D1 goal failure case, corrupt-chain rejection, and a synthetic 152-panel complete-mode fixture proving no kernel call or certificate rewrite, and three atomic publication/retry checks.

One actual new j37 panel was integrated under the original L64 precision with a 2 GiB ceiling: worker 1.189256332 s, wrapper 1.350276377 s. It remains a partial checkpoint, with no final L64 certificate and no NCP claim. Full host execution is still pending. The exact command, executed source hash, and outputs are in `verification/validated_l64/LIGHT_CHECK_RECEIPT.json`. The subsequent atomic JSON writer revision preserves the executed source snapshot and records an AST comparison and 14 passing tests in `verification/validated_l64/ATOMIC_WRITER_REVISION.json`; it changes no scientific function and performs no additional integration.

`HH_R10=OFF`.
