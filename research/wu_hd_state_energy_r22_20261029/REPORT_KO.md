# WU088_HH R22 | GL2022 HD 반응의 상태별 에너지 분광 후보, 미승인 PES 구별

2026-10-29, auxiliary scoped research. Authoritative parent R21 Draft PR159 HEAD `fd351d0ff97ef0d7a9cf710bdecad922af7e885e`; R20 source-grid PR157 HEAD `52f9ff3213ac8f156bc47d610624cce061fdf485`, sibling owner-preflight PR158 HEAD `1a5c6f47350da2b74e0b7e3071c4db3502810500` separate. **Canonical WU 34/49 unchanged**, R21 scoped 18/20 unchanged. Distinct-author R6,C9 NOT_RUN. HH_R10 OFF, production NOT_ISSUED, L4 false.

## Scope: one exact ionic state channel

`H+ + HD(X,v=0,J=2) -> D+ + H2(X,v=0,J=1,ortho)` with GL2022 JCP DOI `10.1063/5.0128598`, native SQM printed nominal rates only on 10 original T nodes. Restored R21 original ZIP 432135 bytes SHA256 `5ace176fdba1b1ed01cedbd11e381b98ee242475ef1a401d89dcfcf0b7a3d220` from user-linked Google Drive; source PDF 273554 bytes SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754` in R21 ZIP. No physical rates revised.

## Independent spectroscopy candidate (derived, numerical checks)

Take neutral free atomic H and D electronic ground-state energies as common asymptotes, include atomic ionization potentials and 0 K molecular dissociation energies. With **positive energy required** `DeltaE=E_out-E_in`, **positive heat released** `Q=-DeltaE`:

`DeltaE=(I_D-I_H)+(D0(HD)-D0(H2))+(epsilon_H2(0,1)-epsilon_HD(0,2))`.

Source-literal components in cm^-1:

| Component | Input/output | Provenance |
|---|---:|---|
| I_D-I_H | +29.84280987 | Hölsch et al PRA108 022811 (2023) Table IV |
| D0(HD)-D0(H2) | +287.7128654 | Hölsch2023 TableIV 36405.78253; Doran et al 2026 PRX Accepted 36118.0696646 |
| H2(0,1)-HD(0,2) | -148.5823591857913917 | Salumbides et al PRL107 043005 TableII (2011) 118.48684; Cozijn et al EPJD76 220 (2022) 8006533168 kHz / (29979245800 cm/s) |
| Delta E | **+168.9733160842086083** | independent source-derived |
| Q_spectroscopic_candidate | **-20.9500211513003896 meV/event** | -3.3565634370419263e-21 J/event |

The updated 2023 HD ground-state D0 supersedes a previously used 2010 value. The candidate is ENDOTHERMIC. The 2019 39.5 meV ground-to-ground value is not this state-resolved event, even though ground-ground 39.37 meV from these numbers is a consistent rough comparison. The atomic ionization offset is +3.7 meV *in Delta E*, and is neither dropped nor double counted.

**CRITICAL SOURCE HOLD**: The calculation reconstructs accurate **spectroscopy-side physical energy levels** but does NOT demonstrate that GL2022 SQM used the same PES-native channel thresholds, exact ionization asymptote or non-Born-Oppenheimer corrections. Without the main-paper PES mapping and state term-energy table, `GL2022_PES_native_Q=null`, `physical_Q_event=null`, `physical_bath_delta=null`. In particular, physically correct spectroscopy does not retroactively change a precomputed original source rate's dynamical threshold.

The six *quoted marginal* absolute uncertainty figures have numerical magnitude sum 0.00017693726665 cm^-1 = 0.00002193742518 meV; **not** an uncertainty interval or error bar or independent one-sigma combination, because the 2023 HD D0 and atomic ionizations share the same energy cycle and the 2026 H2 D0 shares atomic reference inputs. A joint covariance/mass-constant rebase must be obtained before a physical Q uncertainty is issued.

## Verified execution, errors and audit

- Python result generated from frozen source literal+DOI+year+quoted error fields and strict PDF/ZIP/HEAD/state-label locks; `src/state_energy.py` does NOT import R21 heat module and cannot issue a physical Q.
- Current local R22 unittest: **22/22 PASS**, `python -O` **22/22 PASS** (normal exit 0). Source identity, wrong channel, uncertainty change, HEAD drift, NaN, attempted production and physical admission fail as expected; CLI exclusive-create and semantic replay PASS.
- Independent numerical check mpmath 90-digit and Wolfram exact-string rational arithmetic agree with Decimal60. Wolfram symbolic cancellation of neutral atomic reference energies gives zero residual. Wolfram originally emitted warning about undefined placeholder names while returning symbolic equality, no independent author review.
- R21 source original clean-restored from actual Drive and inherited 18/18 unittest PASS (R21 tests; not all R21 benchmark/reviewer gates re-run here).
- Figure `figures/R22_STATE_ENERGY_COMPONENTS.png` plotted from frozen source values, manually inspected after correcting overlapped annotation. This is not astrophysical heat or SQM threshold measurement.
- Initial local R22 test used default Decimal28 instead of production Decimal60, causing three equality test failures before `localcontext(prec=60)` test fix. Separate from the physical source missing. This failure is preserved as historical record; no physics value was silently adjusted.
- Source uncertainty is a diagnostic literature magnitude sum; no numerical physical bath heat, not even provisional physical uncertainty.

## Foreign-repo read-only completeness and permissions

REC PR156 `8806a4f757d916b6cf040625be931a66e2f0f6fe`, GitHub HEAD tree 7489 files, selected `src/full_bianchi_hyrec/trajectory/primitive_rates.py`, `rust/rec_microphysics/src/lib.rs`, `research/rec_hd_multichannel_affinity_20261029/code/multichannel.py`, `research/rec_hd_cycle_space_20261029/code/cycle_space.py`: atomic HyRec/hydrogen, HD rotational radiative/inelastic, NOT proven 4-species target GL2022 reactive consumer.

CR PR122 latest `f152e28fd4e9a727b23e068603c0359c5e0d1303`, tree 16428 files, selected `research/cr_c21o_hheli_z2_20261021/atomic_network.py` (photoionization/Case-A, molecular excluded); `research/cr_c22a_thermochemical_20261022/model.py` (atomic photo/RR) and `research/cr_c15_duhamel_20261015/src/continuous_source.py` (H/He transport); `research/cr_c23e_d43_source_binding_20261024/history/superseded_v1/hdx.py` is atomic **D+H+ ↔ D++H** charge exchange, NOT molecular H+ + HD. R21's older CR pinned HEAD stays immutable; latest observed HEAD is a new surveyed ref. This is *full tree file inventory plus selected actual function inspection*, not exhaustive dynamic call graph. No actual owner ACK or foreign mutation; do not claim absence theorem.

## Required next gate, stop conditions

P0: fetch GL2022 **main article** and source PES identity/threshold, energy zero and whether isotope ionization is included; recompute exact two arrangements state thresholds and compare to the independent spectroscopy candidate. Failure to authenticate = hold no numeric Q in physical ledger. P1: build joint covariance from 2023/2026 shared metrological energy cycles, isotope mass constants. P1: identify REC/CR explicit reachable 4-species chemical source-owner `function+code SHA+caller+frames`, obtain owner written ACK. P1: keep reverse detailed balance, partial ionization, actual thermal bath/photons, nonisothermal molecular capacities, full-A and production separate. No canonical DAG promotion or main merge.

**VERDICT**: `PASS_SCOPED_SPECTROSCOPY_CANDIDATE`, `BLOCKED_GL2022_PES_NATIVE_Q`, `HOLD_PHYSICAL_HEAT_AND_OWNER`, `WU_DAG_34_OF_49_UNCHANGED`.
