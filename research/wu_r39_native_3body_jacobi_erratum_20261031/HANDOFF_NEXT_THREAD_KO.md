# WU088_HH R39 source-owned 3-body native PES handoff | 2026-10-31

Copy below verbatim into a new thread; the latest PR/HEAD must be re-read live before changing anything.

```text
$physmath-research-loop $scispace $exa $wolfram
PROJECT=cosmosapjw-quantum/WU088_HH
PROTECTED_PARENT_PR=177
PROTECTED_PARENT_HEAD=93d5eb0aefb9a94d722e9e4107a09b2e3066677c
READ_LIVE_HEAD_FIRST=true
COMPLETED_AUXILIARY=WU_R39_NATIVE_3BODY_JACOBI_PES_TI_QM_ERRATUM
CANONICAL_DAG=34/49_UNCHANGED
R39_AUXILIARY=1/1_SCOPED_EXPLORATORY
R_C_SCOPED=18/20
R6_DISTINCT_AUTHOR=NOT_RUN
C9_DISTINCT_AUTHOR=NOT_RUN
R38_MASTER_SHA256=284cb1f0ac67b81c6088c5c1ac8dcf55d816f2e45acdc3983e2af95c49de4257
NATIVE_FORTRAN_SHA256=8dbf8b7e3852d02504ba92317f79593051d689f1357263ac0891a3a24084ed8c
NATIVE_3BODY_ROWS=5376
LEGENDRE_MOMENT_ROWS=168
COM_TRANSLATION_WITNESS=192
ISOTROPIC_BARRIER_DIAGNOSTICS=24
R38_TI_QM_ERRATUM_MATCHED_CHANNELS=70
CORRECTED_THERMAL_RATE_FIT_ROWS=12
SCIENTIFIC_FIGURES=4_PNG_4_SVG
TESTS_NORMAL=13/13_PASS
TESTS_OPT=13/13_PASS
C4_R1p4_BO_AU=2.5884219506088395
LEPERS_2019_DOI=10.1093/mnras/stz1797
LEPERS_2021_ERRATUM_DOI=10.1093/mnras/staa3146
LEPERS_CORRECTED_A=9.94E-10_cm3_s
LEPERS_CORRECTED_B=439_K
PES_NATIVE_SCATTERING_THRESHOLD=NULL
PHYSICAL_Q_FULL=NULL
GL_EMAA_50_CELL_OWNER_RESOLUTION=UNRESOLVED
OWNER_ACK=NOT_OBTAINED
HH_R10=OFF
L4=false
PRODUCTION=NOT_ISSUED
NO_MAIN_MERGE=true
NO_FOREIGN_REPO_MUTATION=true
AUTO_NEXT_NODE=false
NEXT_CANDIDATE_ONLY=TIQM_MACHINE_READABLE_S_MATRIX_OR_FULL_COUPLED_CHANNEL_SCATTERING_OR_GL_EMAA_50_OWNER_RECONCILIATION
```

## Scientific boundary and next productive step
1. Read new R39 master ZIP/Source manifest and do one clean reproduction: `bash replay.sh` from extracted root; compiled gfortran+LAPACK source is **private**, do not publish original AIP EPAPS or Fortran.
2. The new 5,376 records are genuine **electronic 3-body PES evaluations** and their mass-dependent coordinates, **not** reactive quantum scattering. The 24 centrifugal barriers are a useful isotropic C4-only diagnostic, not new rate coefficients or a certified threshold.
3. The 2021 MNRAS *erratum* corrects 2019 nuclear-spin weighting (even-H2 j' para 1/4, odd-H2 j' ortho 3/4), thermal low-T fit A=9.94e-10 cm3/s B=439 K for T≈100–400 K. Do not multiply GL2022 already-weighted rates by weights again.
4. Need original 2019 author TIQM state-to-state S-matrix/cross-section/rate grids or machine-readable supplementary data. Article: Lepers, Guillon, Honvault, MNRAS 488, 4732–4739 (2019), DOI 10.1093/mnras/stz1797, supplementary at article page. Erratum DOI 10.1093/mnras/staa3146, MNRAS 500, 430–431 (2021). Corresponding author: maxence.lepers@u-bourgogne.fr as printed in published article. Request state-to-state sigma(E), k(T), j/j' conventions and corrected total thermal weights; no author response yet.
5. For 50 GL–EMAA printed state-rate discrepancies: González-Lezana, Hily-Blant, Faure, JCP 157, 214302 (2022), DOI 10.1063/5.0128598, corresponding `t.gonzalez.lezana@csic.es` (publisher). Request primary machine-readable rate grids with row/temperature identifiers, handling of rounded scientific notation and Eq.(6-7) spin normalization, not a silent source correction.
