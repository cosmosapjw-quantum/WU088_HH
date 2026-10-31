# R39 | 2026-10-31 원전 기반 신규 3체 PES·핵스핀 정오표 생성 결과

## 검증된 입력
- Git parent: WU #177 HEAD `93d5eb0aefb9a94d722e9e4107a09b2e3066677c`, Draft/Unmerged.
- R38 master ZIP: 1,378,885 B SHA256 `284cb1f0ac67b81c6088c5c1ac8dcf55d816f2e45acdc3983e2af95c49de4257`.
- AIP EPAPS zip SHA `a781d3b6f7d3cdffc210f2e8abd436e7378eb3716af80eb96b102a542eaba304`, raw `h3plus.f` SHA `8dbf8b7e3852d02504ba92317f79593051d689f1357263ac0891a3a24084ed8c`. Native 2008 paper and Fortran remain **private**.

## 실제 신규 데이터
| input/output | entries | role |
|---|---:|---|
| `NATIVE_PES_3BODY_JACOBI_5376.csv` | 5376 | native e1-h2; 2 arrangements×3 fixed r×28 R×32 angular points |
| `NATIVE_PES_LEGENDRE_168.csv` | 168 | angular a0..a4, isotropic C4, minima/maxima |
| `COM_MIDPOINT_TRANSLATION_192.csv` | 192 | exact geometric COM-to-midpoint checks |
| `ISOTROPIC_C4_CENTRIFUGAL_24.csv` | 24 | C4-only barrier estimate, explicitly diagnostic |
| `R38_TI_QM_ERRATUM_CHANNEL_70.csv` | 70 | source-locked R38 kinematic Q + 2021 para/ortho correction metadata |
| `PUBLISHED_THERMAL_ERRATUM_12.csv` | 12 | published rate fit, original vs corrected vs separate para/ortho |
| `FIG01`–`FIG04` | 4 PNG +4 SVG | physics figures |

- C4 from original frozen-bond PES at r=1.4 a0: `2.5884219506088395 Eh a0^4`; long-R fit max residual `2.955e-7` in -R^4 a0 (fit error, not complete physical error budget).
- Reduced masses `mu_R(H+HD)=1377.0005781 me`, `mu_R(D+H2)=1835.6969656 me`; C4-only l=1 radii 84.4305/97.4839 a0, barrier temperatures 0.01608476/0.00905067 K respectively.
- 192 exact COM-vs-midpoint source PES comparisons: max abs `8.22e-14 Eh`. The H+HD fixed-geometry odd multipole originates in the mass-defined coordinate origin, not a new non-BO permanent dipole.
- At T=205 K the corrected Lepers thermal fit gives ~`1.16778e-10 cm3/s` versus as-published 2019 fit ~`2.41720e-10 cm3/s`. These are *analytic fit evaluations*, not freshly calculated cross sections.

## Verification and boundaries
- Original Fortran compiled with native gfortran and LAPACK/BLAS. Original untouched; compiler source warnings preserved.
- 13 scoped tests normal and 13 scoped tests `-O` PASS, including source hashes, native permutations, midpoint translation, odd-parity, quadrature cross-check, mass/barrier Wolfram-independent formula, erratum domain, branch source identity.
- No quantum scattering S matrix solved; no new physical Q full; no rate fitting to observational data. Parent original GL2022 and EMAA reaction rates/first-exit probabilities unchanged. 50 GL–EMAA rate cells remain owner-unresolved.

**DAG:** canonical 34/49 unchanged (+0), R39 isolated auxiliary 1/1 source-scoped. R/C scoped 18/20, distinct-author R6/C9 NOT_RUN. `HH_R10=OFF`, `L4=false`, `PRODUCTION=NOT_ISSUED`, `NO_MAIN_MERGE=true`, `AUTO_NEXT_NODE=false`. Draft-only isolated publication is allowed, never production admission.
