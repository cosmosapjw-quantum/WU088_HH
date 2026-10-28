## Scoped scientific completion, not an all-repository CI pass
BF3-E COMPLETE_SCOPED_STATIC_LAPSE_SOURCE_MEMORY. Parent BF3-D PR226/aca22f4b7287b642d65caf2c820b681b76ab1309. Dedicated child branch only. S0 commit44637dd280dd7407f5b2723ed11b59f7efdf88e8; verified numerical S1 commit60c1ebbb5ef68f8072bc689764f362d6c4df1e4d; final S2 HEAD90b600519712939e3db123191dcaea0361fdea9e. Expected-SHA non-force update succeeded. S1-to-S2 compare confirms only six added report/results/DAG/handoff/receipt files; numerical core/tests unchanged. No merge or main/owner/integration-parent/default-route mutation.

## Actual package construction
bianchi.nonperturbative.lapse_memory, explicit backend='python_oracle'. Static periodic lapse N=exp(epsilon cos x), Y=N^4W, scaled local source S=N^4M, physical J=N^-4EYE^T. Coordinate opacity=N*n_e_star*sigma_T*c*Tstar. Independent source equation S=L exp(tA)Y_initial+integral L exp((t-s)A)B S(s)ds with A the SAME finite Fourier/Legendre streaming-loss collocation generator as the parent. Exact exponential polynomial panel weights use an augmented matrix and require no A inverse. Two unknown source stages per panel, dimension18nx. The solver never calls parent radiation rhs/direct/split/gain. Full initial carrier and local final-angle weights retained, no global phase Jacobian at local source.

Continuum inverse-ray retarded kernel is separately evaluated. Finite remapping is not silently identified with the collocation semigroup. Dense reference, not a nine-state Markov closure, performance claim or generic positivity/global-tail theorem.

## Executed scientific evidence
One campaign; source solves15,direct IVPs3,Strang1,640x640 full-generator exponential1,actual inverse-ray IVPs4(three kernel plus one inside Strang). Current/historical science replay0. Tests and auto-CI separate. No physics/tolerance repair.

Main epsilon.55,u<=.4,nx17,nmu10,nphi8,nu_star=1.1+.3sinx. Panels8/16/32/64 source endpoint errors2.62141e-9/1.63566e-10/1.02187e-11/6.39488e-13; carrier errors1.47137e-9/9.20816e-11/5.75273e-12/3.55604e-13. First orders4.00240/4.00059. Same-grid comparison, not continuum certification.

Joint(nx,nmu) continuum inverse-ray kernel-action gaps:7x6 1.34542e-3;13x10 1.54640e-5;21x14 1.22146e-8. Wrong global-Jacobian weighting remains.05019 at fine resolution. Spatial solution comparison was atx=0 only; angular refinement separate. Source polynomial offgrid2.59e-9 differs from reconstructed source2.80e-12. Initial scaled .1cosx P4 source-null field returns atx0,u.4 with direct/memory Mxx-.00038573529502942115/-.00038573529502525944. Whole initial and gain-history contributions retained.

Global Killing relative defect1.55e-14 DOES NOT remove the coarse local energy residual3.39e-5. Both are published. No clipping or normalization. CAS checks scalar panel consistency and weighted-divergence identities, not an independent-model review.

## Targeted CI PASS, inherited policy CI FAILURE
BF3-E run40667431443/job122745367879 SUCCESS:13 unique tests passed, actual wheel built/installed outside checkout and numerical source-equilibrium check passed. Executed core blob5ff27159e919a8ef7327bc6c8c7a75b7ec87db93 and tests271d8459884683a68c5af598c8c66d6c61632636 match remote readback.

Separate RF00 run40667473221 FAILED. Portable job122745511607:62pass/2skip/1fail, parent root exports runtime while exact __all__ test omits it. Both source/test conflicts verified at parent. Native job122745511139:fmt/clippy,existingRust134tests,nativewheel build/install PASS, followed by Pythonpolicy86pass/1fail. runtime_plan_warm_construct output is repeatable but digest differs from registry; root cause unresolved. Expected76d6d0db86a80c0ab01155dd3be2061cfe0c0874bd955b47502557fd1d70fc84; actual7b718708513a04993aaeb61947e090587e327395404c4c0d744010440928b26f. Existing CI reported unverified native SBOM-size warning. No expected hashes/policy/tests changed to force a pass. New BF3-E native implementation remains NOT_IMPLEMENTED/NOT_RUN. Overall repository/native merge admission is NOT granted. See REPOSITORY_CI_STATUS.json.

## Staged dual preservation
S0 scope8/15:2735bytes,SHA256c421b07648bcb23f36cf3887502ab264261f7d10eb4d71d20fedd36815d31c80.
S1 code8/15:9518bytes,SHA2564800b3fc8321bec31855212789844a3622ceb92231e19752bf2be116ec9b51cd.
S2 final9/15: BASS_BF3E_FINAL_20261028_fc095394.zip,217005bytes,49files,SHA256fc09539429e2cfeb1e55f62d94cfe12e4dfc5d4a96809492e48afa13c2c7cdb9.
Drive https://drive.google.com/file/d/1tIgVI9_S6mGdYlRCRYbKA4aN3RvO3TcF/view?usp=drivesdk . Dropbox /BASS_BACKUPS/BASS_BF3E_FINAL_20261028_fc095394.zip,id:BSpOijBcT10AAAAAAEFU2w.
Every listed stage has Drive FULL_BYTE_READBACK_MATCH and Dropbox PROVIDER_CONTENT_HASH_AND_SIZE_MATCH; full Dropbox readback NOT_RUN. All details in PRESERVATION.json.

Initial S2 seal5a81613e was retained unchanged. Final fc095394 adds subsequently inspected repository-policy failures and corrects an unverified timestamp-bearing hand-written CI excerpt to an explicitly semantic extract. Core/tests/raw numerical results/gates remain byte-identical, no science rerun. Supplemental closeout5bf48817 also preserved. Git is runnable core/tests plus concise evidence; final ZIP includes full derivation, scientific/saved-data validators, all rows,CAS,logs,figure,detailedDAG and selected exact package projection, NOT a full repository/wheel.

## Admission and next boundary
BF3-C/D/E close BF-3 only for selected prescribed static periodic lapse bolometric normal-rest smooth-field benchmark. Upper scoped/source-mapped DAG9/15, original15nodes/edges retained; stages are not extra nodes. Generic metrics,full-frequency,Einstein/material feedback,native production,independent-model review and general positivity/tail remain open. production_ready=false,merge_ready=false. No scientific results erased because separate policy CI failed.

Next candidate CE1-A_ONLY: constraint-admissible collisionless homogeneous Bianchi-I radiation initial data and scoped source-to-geometry error propagation, then a minimal coupled pilot within its derived contract. CE-1 error-propagation obligation is OPEN. No new node automatically executed. Read HANDOFF_KO.md and exact archive first; use validate_saved.py for saved evidence, not a repeated science campaign.