# WU R39: native Velilla three-body PES, mass-defined Jacobi geometry, 2021 spin erratum

**Scope:** source-owned exploratory R39 auxiliary 1/1. **Canonical WU DAG: 34/49 unchanged (+0)**; physmath R/C 18/20 scoped, distinct-author R6 and C9 NOT_RUN. **Draft only; no main/parent merge, no production admission.**

## New source-derived physics

- Original source: Velilla et al., *J. Chem. Phys.* **129**, 084307 (2008), DOI [10.1063/1.2973629](https://doi.org/10.1063/1.2973629), private authenticated Fortran `h3plus.f` SHA-256 `8dbf8b7e3852d02504ba92317f79593051d689f1357263ac0891a3a24084ed8c`.
- **5,376** actual electronic three-body native PES evaluations: two isotope-reaction arrangements x three fixed bond lengths 1.2/1.4/1.6 Bohr x 28 radii x 32 angular quadrature nodes.
- **168** Legendre multipoles, **192** exact coordinate-change PES checks, **24** isotropic ion-induced-dipole centrifugal barrier diagnostics. Full third-party-dependent physical sample grid is in the private source archive, not redistributed here.
- Long-range isotropic reference at fixed `r=1.4 a0`: `C4=2.5884219506088395 Eh a0^4`. The mass-dependent COM radial reduced masses are 1377.00057810 and 1835.69696555 electron masses. `ell=1` isotropic-only barrier heights 0.0160847556 and 0.0090506700 K; **not** verified reactive thresholds or cross sections.
- COM/midpoint invariant native PES check: maximum absolute residual `8.22e-14 Eh` (192 points). The odd Legendre moments on heteronuclear HD at mass center arise from coordinate translation; do not interpret as a new intrinsic electric dipole.

## Original published literature correction

- Lepers, Guillon & Honvault, *MNRAS* **488**, 4732–4739 (2019), DOI [10.1093/mnras/stz1797](https://doi.org/10.1093/mnras/stz1797).
- **Mandatory erratum:** same authors, *MNRAS* **500**, 430–431 (2021), DOI [10.1093/mnras/staa3146](https://doi.org/10.1093/mnras/staa3146). Para-H2 even product J' multiplicity 1/4 and ortho-H2 odd product J' 3/4 in total **thermal** rates. Corrected low-T fit `9.94e-10 exp(-439/T) cm^3/s` for T approximately 100–400 K; do not reweight already spin-weighted GL2022/R37 probabilities.
- Public CSVs: **70** prior BO kinematic-channel source/erratum crosswalk metadata, **12** literature thermal fit samples, **24** isotropic barrier diagnostics. Literature fits are not new quantum collision predictions.

## Reproduction, evidence, and protected gates

`generate.py`, `plot_science.py`, `test_science.py` and `replay.sh` implement source-bound regeneration when the private original input ZIP is available and hash-validated. Clean private-master extract: **53/53 manifest SHA/size**, ZIP CRC PASS, **6/6 regenerated CSVs byte-identical**, new tests **13/13 normal** and **13/13 Python -O**. Source-private master ZIP SHA-256 `74a2ee988b263b00ad3334fbb333722fa6aaeb99c108b3736f9ae0e836710996` (1,904,631 bytes).

Current blocked items: no actual 3body S-matrix, no full physical Q, GL2022-vs-EMAA 50 printed rate-cell owner reconciliation unresolved, no R6/C9 distinct-author. `HH_R10=OFF`, `L4=false`, `PRODUCTION=NOT_ISSUED`. No foreign repository mutation. Do not silently start a further node.

Backups: Library `/WU088_HH/R39_NATIVE_3BODY_ERRATUM_20261031/` and Google Drive `/WU088_HH_R39_NATIVE_3BODY_ERRATUM_20261031/`, each with 20 stage ZIPs, 4 phase ZIPs and one master, verified original-master SHA/CRC on provider readback. Full public code/data and scientific reports are included in this Draft PR; copyrighted third-party sources omitted.
