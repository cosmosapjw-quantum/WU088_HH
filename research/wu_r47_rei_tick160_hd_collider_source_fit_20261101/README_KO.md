# WU R47 | Original REI tick160 HD collider eligibility and proton/H competition

**Scientific status:** SOURCE-CONDITIONAL, NUMERICALLY CHECKED; one original physical-model state, not observed data and not a completed central solver. Immutable parent WU Draft PR #185 HEAD `12289d44304bdcc7906dac3f1fa01e54ea19d2c2`. No main merge/production/new IVP.

## Exact source identity
- REI original 46,080-node accepted tick160 state ZIP SHA256 `48ad5c6f0922ad946a10a89ce17fefd2c7241ac956b6bac194892a42810312a7`; original full frozen archive SHA256 `a861278201313c55e08ba6323b5c1d2ad97bf5765f429807b4eba0a1c2465d0b`. Three lane labels share numerically identical states.
- EMAA original 52-level HD RADEX SHA256 `b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94`, neutral H 1326 pairs at 15 source T nodes 5–5000 K; proton 171 pairs at 25 nodes 5–3005 K within HD19, not HD52. H original DOI 10.1093/mnras/stac911; H+ original DOI 10.1063/5.0128598.

## New physical calculation
For the single **HD(v=0,J=1)->HD(v=0,J=0)** collisional downward transition, with REI H/He-only closure `n_HI=(1-x_HII)n_H,nuc`, `n_H+=x_HII n_H,nuc`, define the dimensionless rate competition
`R=Gamma_H+/Gamma_H=[x_HII/(1-x_HII)] [k_H+(T)/k_H(T)]`.
Both rate coefficients are original EMAA data at native temperatures. At the actual REI model T they are **derived log-log interpolants** within both native source spans. An alternative linear interpolation was separately computed; do not label it authored raw data.

Native temperature-span coverage on 46,080 **unique** accepted spatial nodes: **5616** joint H/H+ (12.1875%), **9216** H-only (20%), **31248** outside neutral-H (67.8125%), zero boundary-straddling nodes. Joint-span `R` min **612.251142933**, median **12693.4028571**, q95 **45201.959038**, max **52213.7000442**. For the chosen log-log interpolation model, the minimum outer rectangular marginal-bound lower value is **611.995525111**. Absolute linear-vs-log interpolation ratio variation max **1.1753324%**; this is sensitivity, not certified physical uncertainty.

### Admission boundary
Dominance applies only to the stated **one collisional de-excitation frequency**, **not** full HD cooling, the HD chemical budget, level populations, blackbody pumping or photon transfer. No original H+ rates for the higher 33 HD levels, no n_HD, actual n_H proper history, clock, source-matched radiation, REI accepted F05 first full interval or Bianchi donor geometry in this unit. This experiment identifies why R43 H-only HD52 is **not directly source-qualified** for these particular original REI states.

**DAG every stage:** WU canonical **34/49**, REI central **28/88**, working **33/88**, completed delta **0**. R1–R10/C1–C10 are one scoped study; R6/C9 same-model hostile review only, distinct-author **NOT_RUN**, native subagents user-disabled.

### Code/data availability
Original source-private ZIPs are not re-published on GitHub. [Source-free full executed code + 46,080-row derived CSV + tests + plots + theory + 20 stage receipts](https://drive.google.com/file/d/1yKZ9TA6r0Mqb0I2gvK5qN0W1Dwb3aY2S/view), **2,702,590 B**, SHA256 `431195b2c72412ebcc071db55d36d44d1c45c099f418084c46933786dfa62067`; direct Drive raw readback same SHA/cmp and CRC PASS. The Git-hosted 9-row witness and runnable checker are the public subset, not a disguised whole atlas. Full generator requires the separately preserved original input ZIPs.

**Verified local:** Python 14/14 normal, 14/14 `-O`; independent NumPy vectorized log-interpolation check, 3/3 deterministic output SHA replay, original input SHA and ZIP CRC; no original 26-event solver rerun.

**Next owner action:** REI source-shared original 26-event full/half Jacobian + nonlinear remainder on the whole correlated F05 parent, followed by original unchanged-gate single [160,161] trial only if the genuine certificate permits. Do not automatically make another WU molecular atlas. `HH_R10=OFF; L4=false; PRODUCTION=HOLD; AUTO_NEXT_NODE=false; NO_MAIN_MERGE=true`.
