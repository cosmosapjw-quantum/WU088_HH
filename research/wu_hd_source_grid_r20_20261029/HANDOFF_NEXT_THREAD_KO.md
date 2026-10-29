# WU088_HH R20 → 다음 스레드 handoff | 2026-10-29

$physmath-research-loop $scispace $exa $wolfram

REPO=cosmosapjw-quantum/WU088_HH
R20_DRAFT_PR=https://github.com/cosmosapjw-quantum/WU088_HH/pull/157
R20_BRANCH=research/wu-hd-source-grid-exposure-r20-20261029
R20_HEAD=READ_CURRENT_PR_HEAD (metadata final SHA must be verified after all receipt commits)
R19_PARENT_PR=156
R19_PARENT_HEAD=218f353e67ac533b9fb6d54156ec3db6e8827db6
CANONICAL_WU_DAG=34/49_UNCHANGED
R20_SCOPED_WORKFLOW=18/20 (R6/C9 distinct-author NOT_RUN)
HH_R10=OFF; PRODUCTION=NOT_ISSUED; L4=false.

## Science and code actually established

Source: González-Lezana/Hily-Blant/Faure JCP157 214302 (2022), DOI10.1063/5.0128598. Original DIGITAL.CSIC PDF SHA256 a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754, 273554 bytes. R18 source NativeGrid provides only SQM reactive H+ + HD(v0,j2)->D+ + H2(v0,j1) printed nominal rate at discrete T=15,55,105,255,505,1005,1505,2005,2505,3005 K. Do NOT multiply p2 or odd-spin 3/4 again. No source true-rate uncertainty, interpolation, reverse rate or physical Q.

R20 exact nonautonomous theorem: with external positive v(t)=V/V0, N=v*n and one-channel forward reaction, dN/dt=(k[T(t)]/v(t))*nu*N_H*N_HD. Scalar time-dependent generators commute, so N(t)=Phi_{A(t)}(N0), A=integral k(T)/v dt. For each source-grid segment with constant theta=dlnv/dt, I_i=dt_i/v_i * (1-exp(-theta_i dt_i))/(theta_i dt_i) (continuous theta=0 limit), A=sum k_i I_i. Positivity, H/D/charge conservation in comoving densities, semigroup and dxi/dk_i=I_i(a-xi)(b-xi) proven. This does NOT extend to coupled multi-reaction or state-dependent temperature.

Actual source-bound synthetic example: initial H+=HD=1e6 m^-3, products0, v=1, 105K 5e9s then255K 5e9s: A=1.945e-6 m^3, reactants each339558.5738539898 m^-3, products each660441.4261460102 m^-3. Not an astrophysical history.

Verified: pytest25/25, Wolfram symbolic9/9 True, independent survivor-ratio mpmath80 160/160 (max abs5.960464477539063e-08 m^-3, max rel floor1 3.051806267813985e-14), DOP853 4/4 (max abs4.307366907596588e-09 m^-3). Synthetic GLn clock comparison for constant H, v~a^3: GL2 relative error0.00379545, GL8 ~1.06e-15, NOT a general enclosure. Local Python timing exact vs DOP853 at matched accuracy and excluding source-PDF parsing about139x/203x/219x/215x for 2/8/24/48 segments (read actual results JSON for exact values). Not whole production solver performance.

## Actual owner interface findings

REC PR155 HEAD861b7f8b3e52d580437a1b4ad448d9669b0d2706, `research/program_expansion_20261025/hd_adapter/lamda_hd.py:HDDataset.downward_rate`, blob632a8a094e7eedd24a1ec3132fec20765d6e39da: LAMDA nonreactive HD collisions, T=50/100/200K, NOT reactive source-grid consumer.
CR PR120 HEAD5a8e4ac85a19151a3f9625c91d8e87b38f7a32e7, `research/cr_c15_duhamel_20261015/src/continuous_source.py:proper_dt`, blob b60f3ef6487b340ecb519f9dd77445caf2975833: GL2 proper dt integral in ln a via model.hubble(a,q). R20 reproduces mathematical formula/signature only, does NOT execute actual owner namespace or bind HD chemistry. Correct exposure is k int d ln a/(H v), not k*proper_dt/v_mid. CR `species_resolved_affine` is H/He photon photoevents, NOT HD chemistry. REI PR261 17state lacks HD/H2. Do not claim owner chemistry integration.

## Replay and sources

Read R20 THEORY_KO.md, REPORT_KO.md, README_REPLAY.md, DAG_DELTA.json, authority/OWNER_INTERFACE_AUDIT.json, results/EXECUTION.json, delivery/PUBLICATION_INDEX.json and FINAL_EXTERNAL_RECEIPT.json (if present). Use source ZIP with original PDF and frozen R18/R19 modules, or exact source PDF from institution. Git public branch intentionally excludes original binary PDF.

In a checkout set WU_R20_SOURCE_PDF=/absolute/GL2022_CSIC_supplement.pdf, PYTHONPATH=repo_root:repo_root/research/wu_hd_source_grid_r20_20261029; run pytest tests/test_grid_exposure.py, independent_reference.py, numerical_benchmark.py and figures/render_r20.py from the R20 unit. Never assume runtime state from previous turn; probe it.

## Next gated work

1. Obtain actual owner REC/CR/REI four-state HD reactive chemistry function/path/commit and owner ACK; existing named clock is only a partial interface.
2. Require source-grid T or independently qualified source temperature extension, state order, number-density, proper-time/clock, volume, same-state Q/energy ledger and reverse/missing channel policy.
3. Request actual distinct-author R6/C9 review for R20. Alternative CAS/mpmath/SciPy algorithms do not substitute independent author.
4. Only then consider an actual owner test, full-A error propagation, uncertainty and production gates. Do not mutate other owner repos, merge Draft PRs, invent rate interpolation, or promote HH_R10/production/L4.

Backup semantics: stage-indexed Git source commits and Google Drive original ZIPs plus Dropbox Paper text receipts are different layers. Dropbox original binary ZIP remains NOT_UPLOADED unless a real provider ACK and SHA/readback prove otherwise. Each stage must state (WU complete)/(WU total) as 34/49 until a separate scientific admission occurs. Preserve all failure classifications and hashes.
