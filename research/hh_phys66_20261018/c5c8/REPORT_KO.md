# PHYS66 C5-C8: inherited NCP ledger and complete long-radius runner

## Intake and authority

Backups were inspected BEFORE new research. In checked WU Dropbox/GDrive paths the newest numerical campaign remains the completed PHYS64 2-smoke+18-extended campaign, not a new PHYS65 run. Archive d7fa0b50ed803e19dfcec8f781219c03acbd21f8f3ee47fe922754f8fdb5ea79 was restored and actually verified:149 manifest hashes,20 SUCCESS receipts,18 extended case/request/config/runtime bindings and36 result payload hashes. Stored coefficient arrays were compared with JSON values; all original execution source hashes and NPZ original hash were checked. NO inherited case rerun; no raw file or old certification flag edited.

PR114 bad80f7729015c84c8dde27f1b1dec3a1f8b2c9f supplies proved all-radial finite-L64 Coulomb ratio and nonlinear majorants. Exact upstream src/wu088_hh/phys65_exterior_bounds.py Git blob935d8ec1b765e5f1bd7c6ad0d95c9c74acf33512 was recovered and byte checked. Before closeout PR115 445d82db9c42b4f2f81e4ac1b107dec3b69b3c24 was found: its order-radial theorem matches our local derivation after hbar_n=4^n h_n. Upstream PROOF.md/NEXT_DAG are NOT overwritten; local verification is in local_verification/.

The conversation-mounted old PHYS65 ZIP is a repaired147-entry/146-payload snapshot, SHA7f7f15f42d9bc62ec586fd9e32867d6ae45ba3bfc5ecdcf97eb18331ce202cf0, not the stale displayed historical checksum. Every payload and original input was actually checked. Old false exit0 with failed stdout is historical and NOT admitted as PASS; fresh tests are used.

## New completed implementation

- phys66_radial_budget.py: exact mode-specific Gamma_L, order-specific radial beta_n, absolute component-only radius planner, bounded domains and lossless rational-hex serialization. For L64,T65 beta1=4.789119177450071e-52, beta2=7.541138621579980e-66, beta3=1.484322314885588e-79 a0^-1. Chosen planning goals1e-30/1e-54/1e-78 return integerT65. They are not user-prescribed total tolerances.
- phys66_campaign_ledger.py: strict old NCP ZIP/manifest/source-code/array/config verification. Adds new analytic components without changing raw old flags. Numerical/Coulomb/quadrature/roundoff and excluded angular errors stay None. No arbitrary scalar can enable total_error_certified.
- phys66_endpoint.py: unchanged original potential, central normalization and noncommutative PHYS64 recurrence, integrated on [T,39] then[39,27] carrying z,logp,Y1,Y2,Y3. No reset to0 at join, no total-minus-Born subtraction. T<=80 explicitly supported, unlike original PHYS64 limit55.
- phys66_campaign.py and scripts/phys66_ncp.py: fully implemented direct-host preflight/compile, per-case child processes, nice10, BLAS1, VM/time limits, deterministic fingerprint, payload-hash resume, atomic metadata, preserved failure attempts, profile-specific campaign files and checked result ZIP. Smoke2 distinct from longtail6. Longtail6 =L28/64 times T55/65/75,m0; old20 cases never repeated.

## Actually executed science

A new source-locked L28,m0,T65,join39,orders3,GL128,DOP853 rtol2e-11 step0.25 pilot ran in THIS SANDBOX, not NCP. Its reported21,20 physical entries are:
D1=2.766042245979935e-24+4.500676730174401e-25 i;
D2=7.017743632831646e-48+3.200163222312005e-48 i;
D3=2.1430013546605525e-71+1.7186514963020187e-71 i.
Independent coefficient quadrature (shared central dense path) relative defect1.8320844897521165e-12. This comparison does not certify numerical integration. Actual pilot wall7.916s. Mode-specific Gamma28=5929 gives analytic RADIAL-component bounds8.76379247009e-53,4.62110934025e-68,3.04586336444e-83; full higher-Born remainder after3 is1.30387268892e-65, separate from third term.

Actual subprocess smoke:2 cases completed, then identical fingerprint resume reused2 with0 new computations. New six-case longtail NCP campaign NOT_RUN. Actual selected regression was174/174 PASS before late purely doc-path update and one normalization test addition; final fresh count and restored-source receipt supersede the count below when present. These are available recovered PHYS63-65 tests plus new PHYS66, NOT the full historical original WU suite. New tests include real baseline RED then GREEN for order weights, analytic-vs-numerical claim separation and nonzero original endpoint source. Other added regression tests were tests-after, not relabeled TDD.

## Error interpretation

Fixed finite projection and continuum radial analytic error are rigorously separated from numerical outputs and omitted modes. No angular truncation bound or numerical error is known. The exact mathematical coefficients may have small radial tails while their computed f64 approximation has larger integration error. Full all-angular qualitative LAP from PHYS63 is retained, not reopened. xi=Fy-phi, origin/incoming adjoint, sigma(E), Maxwellian k_HH(T) remain open; HH_R10=OFF.

## Publication and preservation

This session's GitHub tools expose reads but no create/update/push actions. Dropbox/Drive have no exposed upload operation; direct container network access failed DNS resolution. No unauthorized account or credential change was attempted. New remote push/cloud upload is BLOCKED/NOT_RUN, not PASS. Stage R5 and C5 are locally committed and archived with exact payload checks. Existing PR115 is read and inherited, not falsely claimed as our write. Local source snapshot Git parent is NOT the real upstream Git ancestry. The final add-only patch targets PR115 and avoids all six changed PR115 paths, with a full source package for recovery. Native subagents NOT_RUN.

## Final tested checkpoint
After late PR115 synchronization and adding exact normalization regression, the current restored selected regression returned175/175 PASS (24.18s pytest). This includes118 inherited selected tests and57 new PHYS66 tests, not the entire historical WU repository. The final new-source ZIP is independently unpacked and its57 new tests rerun; see external DELIVERY for actual result. The smoke occurred before final code commit, so recorded git_head identifies the checkout only; exact code_sha256/fingerprint identifies executed working-source bytes. Those same numerical source bytes are in the final commit.
