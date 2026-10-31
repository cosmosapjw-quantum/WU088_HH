# WU R44 | Chemically injected 52-level HD non-LTE photon current (2026-10-31)

**Research result**: `EXPLORATORY_SOURCE_CONDITIONAL`; source-derived numerical model, not observational data, full astrophysical chemistry, production cooling implementation, or a new canonical WU DAG node. **Canonical WU 34/49 unchanged (+0)**; auxiliary R44 1/1 scoped; R/C scoped 18/20, distinct-author R6 and C9 NOT_RUN. This is an **add-only Draft** child of protected R43 PR #182 at commit `03a884d4035194703307c243179ca5e74e028b72`. No main merge, production, HH_R10, L4 or auto-next.

## Original immutable sources and authoritative executable precedent

- Molecular 52-level Einstein A, energy levels and neutral H collisional rates: EMAA original HD rovibration RADEX `HD.Rovibration.805a7aa5.radex`, SHA256 `b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94`, DOI https://doi.org/10.17178/emaa_hd_rovibration_805a7aa5. Original parser SHA256 `c982bdd3a1dcf61bbd734295a68b2162b536068f4f65eb9e18ff188dd774252b`. Original H collisions Desrousseaux et al. 2022 DOI https://doi.org/10.1093/mnras/stac911.
- **Actually used code-authority chemical rates**: Grackle `grackle-project/grackle` pinned commit `01261db0cefc69d8d5558e76a671b0c1f6e48271`, `src/clib/rate_functions.c` blob `dfbab661e7c45981eed750baebff140849917152`. `k52`: H2+D+ → HD+H+; `k53`: HD+H+ → H2+D+, fits credited by original Grackle authors to Galli & Palla (2002). Grackle cooling library Smith et al. 2017 DOI https://doi.org/10.1093/mnras/stw3291.
- **Prior literature**: Faure, Hily-Blant, Pineau des Forêts & Flower 2024, *MNRAS* 531,340–354 DOI https://doi.org/10.1093/mnras/stae994, already computes coupled chemistry and level populations. R44 makes **no novelty claim** for that general class.

## Precisely scoped construction

Time-dependent HD level densities `n_i` [cm^-3] at fixed `Tgas` and fixed external blackbody `Trad=84.4905 K`; gas density `nH=1e4 cm^-3` and fixed physical volume over 20 years. Use only original neutral-H source temperature nodes `Tgas=70 K` and `100 K`. No unsupported high-level proton HD excitation rates. Proton is a **chemical reactant only**, not an excitation collision partner.

Chemistry: `x'=k52(a-x)(b-x)-k53(c+x)(d+x)`, with `a=nH2(0)=10`, `b=nD+(0)=0.2`, `c=nHD(0)=1e-4`, `d=nH+(0)=1` [cm^-3]. Time-dependent master: `n'=[C_H(Tgas,nH)+R(Trad)]n + F f - D n`, `F=k52(a-x)(b-x)` [cm^-3 s^-1], `D=k53(d+x)` [s^-1]; choose `f` as 52-state `(v0,J0)`, `(v0,J2)`, or source-energy Gibbs(`Tgas`) distribution. **None** of these nascent `f` choices are source-established state-selective chemical channels. `k53` same for all levels is an explicit aggregate closure, not an original state-resolved reverse rate.

Signed photon current `Pgamma = -1e6 E^T R n` [W/m^3]; positive means HD→photons. The **non-stationary exact internal-energy identity** is `Pgamma = 1e6 E^T C_H n + 1e6 F E^T f - 1e6 D E^T n - d(1e6 E^T n)/dt`. Total gas thermal temperature derivative and chemical Q are NOT determined.

| Tgas K | nascent f | photon at t=0 [W/m^3] | photon at t=20 yr [W/m^3] | first sign reversal [yr] | integral [J/m^3] |
|---:|---|---:|---:|---:|---:|
| 70 | v0J0 | -8.108023e-27 | -2.988245e-24 | none | -1.746886e-15 |
| 70 | v0J2 | +1.767055e-25 | -2.986553e-24 | 2.989783081 | -1.080946e-15 |
| 70 | Gibbs(Tg) | -3.883575e-27 | -2.988117e-24 | none | -1.697177e-15 |
| 100 | v0J0 | -8.108023e-27 | +3.859967e-24 | 0.556095885 | +2.112287e-15 |
| 100 | v0J2 | +1.767055e-25 | +3.866855e-24 | none | +2.741525e-15 |
| 100 | Gibbs(Tg) | +5.935530e-27 | +3.860928e-24 | none | +2.199965e-15 |

**Local numerical evidence**: 6×961 = **5,766** time-series rows; 6×961×52 = **299,832** state-population rows; 6×6×368 = **13,248** signed Einstein line rows; total **318,846** derived numerical rows; 4 PNG and 4 SVG physics plots. R44 Python tests normal **18/18 PASS** and `python -O` **18/18 PASS**; original recovered R43 suite normal **27/27** and -O **27/27 PASS**. Independent algorithmic BDF vs Radau crosscheck, not independent author. Clean-extraction scientific regeneration **4/4 SHA256 identical**; 20 individually local R/C stage ZIPs and 4 phase ZIPs checksum + CRC checked.

## Reproduction and publication boundary

The byte-verified R44 `r44_dynamic.py` published alongside this README expects an **external separately preserved private original R43 source** tree containing `source_private/HD.Rovibration.805a7aa5.radex`, `source_private/emaa_primary.py` and `generate.py`; code rejects source hash mismatch. Invoke:

```bash
OPENBLAS_NUM_THREADS=1 python r44_dynamic.py --source-dir /path/to/recovered_R43_root --out results
```

No private original EMAA bytes, old R43 source archive, complete large numerical atlas or executable tests need be assumed present in this public Git subtree. Full run package is preserved as separate local ChatGPT artifact, **not yet remotely binary-backed-up**. Historical R43 sign tally PR182 236/88 versus recovered explicit 224/100 remains `UNRESOLVED_GRID_IDENTITY`, not repaired by R44. No independent distinct-author R6/C9, `PRODUCTION=NOT_ISSUED`, `L4=false`, `HH_R10=OFF`, `AUTO_NEXT_NODE=false`.

**Positive next step**: compare one actually runnable public original Grackle 12-species or Faure2024 published 21-reaction reference trajectory to this HD52 time-dependent model. State-selective nascent HD chemistry, physical Q, gas energy evolution and FLRW expansion are separate, not claimed. Author correspondence or unpublished data is not a blocker for this conditional baseline.
