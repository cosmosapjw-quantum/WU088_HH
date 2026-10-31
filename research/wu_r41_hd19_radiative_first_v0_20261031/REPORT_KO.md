# WU088_HH R41 | Physical output and claim admission report

**Completed bounded work:** R41 source-qualified radiative/collisional first-v0 and known external HD19 radiative first-exit. Official canonical DAG remains **34/49** (+0); auxiliary R41 **1/1 scoped**; R/C stages **18/20 scoped**, distinct-author R6 and C9 NOT_RUN.

## Physical novelty and source

Actual immutable EMAA 52-level HITRAN spectroscopy (368 A-lines) and H⁺ collision source 171 rates ×25 original temperatures provide a finite first-passage event-competition problem. Earlier R40 PR179 solved proton-collision-only first v0. R41 adds explicit Einstein-A spontaneous + prescribed blackbody stimulated emission/absorption, marked emitted/absorbed photons, and source-known radiation exits outside collision-covered HD19. GL printed-valid hybrid stays unapproved and does not replace canonical source. Original source checks in `INITIAL_CHECKPOINT.json`.

## Real generated data

| Kind | Rows |
| --- | ---: |
| HD19 photon/collision first-v0 mechanism case summary | 3,500 |
| HD19 final J and final mechanism event probabilities | 126,000 |
| GL-vs-EMAA first-v0 source sensitivity | 1,750 |
| source-owned emitted/absorbed photon line event outcomes | 4,704 |
| density where first-v0 collision/radiative balance | 700 |
| compared crossover density between sources | 350 |
| original spectroscopic HD19 lines ledger | 63 |
| known 52-level radiative first outside-HD19 escape summaries | 3,500 |
| 55 K source external line-resolved escape examples | 124 |

**Total new derived/source-indexed data rows = 140,691** (not 140,691 independent observations).

For Tgas=55K, initial HD(v1,J6), radiation OFF, the EMAA first-v0 collision mechanism fraction grows from 1.914422738489295e-5 at nH+=1cm⁻³ to 0.9533206031985293 at nH+=1e6cm⁻³. Radiative/collisional first-v0 crossover is n_half_EMAA=49796.718888 cm⁻³ versus n_half_GLhybrid=56221.346533 cm⁻³, a +12.9017% source-conditioned difference; **not an astrophysical density inference**. Largest source-choice terminal destination L1 on this bounded grid = 0.175944024087 at {'P_first_v0_L1': 0.1759440240873162, 'T_gas_K': 55.0, 'initial_J': 6, 'n': 1000000.0, 'z': 'OFF'}.

**Critical source-limit finding**: R36 source supplies 62 upward photon absorption transitions from transient HD(v1,J0..6) to higher spectroscopic levels outside the 19 collision-supported states. At Tgas=55 K, nH+=1e3cm⁻³, external prescribed blackbody z300, initial J6: known outside HD19 first escape P=0.14762297184385717 (EMAA); probability of first v0 before that exit = 0.8523770281561428. GL hybrid Poutside≈0.147893. Largest known source outside escape in grid is P=0.150146461991 at {'P_escape': 0.15014646199072976, 'T_gas_K': 2505.0, 'initial_HD_J': 6, 'n_Hplus_cm_minus3': 1.0, 'source_lane': 'GL_printed_hybrid', 'z_boundary': '300'}. Outside collisions/return are unknown; these are **first source-coverage exits**, not final astrochemical destruction.

**Energy/photons**: gross spontaneous and stimulated photon counts and absorption count are integrals of source Einstein rate against transient occupation time. 7×7 marked resolvent enforces Qrad+Qcoll=E_init-Σ P_exit E_final, not an observed emissivity nor macroscopic gas heat. Computed maximum mass residual 6.661e-16, open-exit mass 6.661e-16, internal energy residual 7.222e-35 J and open version 7.222e-35 J. Numerically checked within the source restrictions.

## Actual tests / evidence

- Normal 25/25 and Python `-O` 25/25 unit+physics PASS in this source worktree; includes independent 80-digit mpmath open/closed matrix checks.
- Source A matrix equals R36 `radiative_generator` within justified floating-point summation error. Source parent pure collisions compare to R40 frozen CSV, original exact input hashes pinned.
- Wolfram exact rational two-transient marked CTMC confirms nonnegative event probabilities and unit column mass; it is a formula sanity check, not author-independent R6.
- Clean extraction and deterministic output hash readback recorded separately. GitHub CI result must be observed from actual remote workflow, not inferred from local tests.

## Claim gate

Accept: source-conditional microscopic first-event probabilities, provenance-locked source-level photon marks, spectral source-coverage escape, density crossover within stated approximation. Hold: outside HD19 proton collisions and return; no reaction scattering S matrix or non-BO Q; no actual cosmic gas cooling/HD destruction; no 50-cell author correction; no independent-author R6/C9. Source owner Tomás González-Lezana, JCP 157 214302 (2022) DOI 10.1063/5.0128598; EMAA database paper DOI 10.1051/0004-6361/202554403. No production, no main merge.
