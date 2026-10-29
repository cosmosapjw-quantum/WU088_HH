$physmath-research-loop $scispace $exa $wolfram
PROJECT=cosmosapjw-quantum/WU088_HH
CURRENT_UNIT=WU_HD_MOLECULAR_IONIZATION_CYCLE_R23
PARENT_R22_PR=161
PARENT_R22_HEAD=4a9cc6f701aacbb8d09bbf4a169d5edd4c4fed47
SIBLING_R22_PR160=9db6f91debf54af1cc129538cfd6f6a716a78a56
R21_PR159=fd351d0ff97ef0d7a9cf710bdecad922af7e885e
R23_DRAFT_PR=CHECK_FINAL_PUBLICATION
CANONICAL_DAG=34/49_UNCHANGED
R23_WORKFLOW=18/20; R6_DISTINCT_AUTHOR=NOT_RUN; C9_DISTINCT_AUTHOR=NOT_RUN
HH_R10=OFF; PRODUCTION=NOT_ISSUED; L4=false
PHYSICAL_Q=NULL; PHYSICAL_BATH=NULL; GL2022_PES_NATIVE_THRESHOLD=NULL

READ: research/wu_hd_molecular_ionization_cycle_r23_20261029/{THEORY_KO.md,REPORT_KO.md,DAG_DELTA.json,CROSS_REPO_PINNED.json,src/ionization_cycle.py,sources/,tests/,results/,figures/,delivery/}. Restore original R21 and R22 source ZIP by exact SHA, run normal/optimized 29 tests and independent mpmath100/SymPy checks. Compare R22 cross-paper PR160 and R22 spectroscopy PR161 WITHOUT automatically merging sibling branches.

RESULT: Exact thermochemical identity DeltaE_21=I(HD)+I(HD+)-I(H2)-I(H2+)+epsilon_H2(01)-epsilon_HD(02); with the six pinned external spectroscopy literals DeltaE=168.9733148142086 cm^-1, Q=-20.95002099384046 meV spectroscopy candidate. Independently R22 dissociation-based DeltaE=168.9733160842086 cm^-1, difference -1.27e-6 cm^-1=-38.073642166kHz. This validates algebraic source consistency within shared-source limitations, NOT the GL2022 PES-native BO threshold, source uncertainty or real physical bath. Physical Q is NULL.

NEXT: actual GL2022/Velilla2008 ionic channel asymptote/PES energy zero/input energies and isotope IP correction. Inspect the primary 2022 Fig1 and relevant PES levels with pagination, obtain raw source + SHA; derive (0,2)->(0,1) native kinetic threshold, compare to independent spectroscopy, preserve distinctions. In parallel inspect real reachable REC/CR chemistry call graphs and get explicit OWNER ACK before other-repo modification. Keep reverse/detailed-balance, thermal bath, full-A, production, distinct-author R6/C9 separate. Reuse real Git and provider receipts; no false dual backup.
