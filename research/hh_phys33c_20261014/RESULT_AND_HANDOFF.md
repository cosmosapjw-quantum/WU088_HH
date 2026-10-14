# PHYS33C: screened high-channel collar and live REI supplier review

2026-10-14. R5 constructive derivation/local checks. Scientific parent is PR66 db88ed7c4054094bcff62668bafc0fef927f559d; actual incoming DtN evidence is the distinct attached PHYS33B archive e3273655212237b19164846f0026641363dc13961cada96c121f6c90d0499e33. Root AGENTS was read and preserved; its historical PHYS19 priority is not the current per-unit DAG. Global PHYS33 remains PARTIAL. No old rate, BVP, P01, native or HPC producer was rerun.

## Exact scoped result

Retain h_lambda=-Delta/2-1/r-lambda*S_R, S_R=(1+1/s)exp(-2s), s=|r-R ez|, original transition S(R)-S_R, initial1s and the exact old-overlap multiplier. r=rphys/a0,R=Rphys/a0,kappa=a0*p/hbar,epsilon=kappa^2/2,h=H/Ea,Ea=2I0. I0=13.605693122990eV differs from receiverchiH=13.598434599702eV. Keep a0=5.29177210544e-11m,c,hbar,kB and parent normalization; background(-+++), Euclidean atomic space.

The theorem concerns R=kappa=7/10,lambda in[0,1], physical bare Q=1_(ell>=29), ALL m, in the collar4<r<8. Use projected QS_RQ, prescribed inner trace at4 and exact PURE-COULOMB outgoing DtN at8. This compressed high-only map is NOT the Q block of the full exterior map: low return and screened r>8 remain separate.

For zero inner trace the continuous collar inverse has L2 norm<=1/6. The Poisson map from L2(S4) trace to collar L2 has norm<=287/1000, also for the incoming adjoint. The difference of collar DtN maps, with inner derivative in the +r direction, satisfies

    ||T_Q,lambda-T_Q,0||_(L2(S4)->L2(S4))
       <=741321/2500000000 =.0002965284.

The difference is bounded on L2; neither individual DtN is asserted L2-bounded. With Bpartial=4 sum_(ell,m)(ell+1)|b_lm|^2,

    |<b,(T_Q,lambda-T_Q,0)b>|
       <=247107/6250000000 *Bpartial
       =.00003953712 *Bpartial.

This component fits the parent's .19 Bpartial allowance. It does NOT prove that the full screened exterior fits it.

## Coulomb boundary and continuous form proof

Reuse the parent's exact ell29 d29(4) rectangle; do not rerun its100->4 producer. For d=u'/u, u''+[49/100+2/r-870/r^2]u=0. Sixteen Taylor steps of1/4, degree192, use elementary directed mpmath.iv110digits and Cauchy majorant3^100 on radius1. The remainder is3^100*(1/4)^192/(1-1/4). All denominator intervals exclude0. The resulting d29(8) rectangle is centered near-3.520164105991489; a separate85digit CoulombF/G derivative is enclosed, not used as the seed.

With alpha_n=n/8-1/n,beta_n^2=kappa^2+1/n^2, the exact ladder is d_n=-alpha_n+beta_n^2/(alpha_n-d_(n-1)). The certified base and

    1/2-1/n-(1+1/n^2)/[(2n-5)/8-1/n]
       =(2n^2-25n+2)/[2(2n^2-5n-8)]>0

prove for everyell>=29 that Re d_l<=-l/8+1/2, |d_l|<=l/8+1/2. The numerator is2(n-30)^2+95(n-30)+1052. Physical t_l=d_l-1/8 hence Re t_l<=-(l-3)/8 and |t_l|<=(l+5)/8. The incoming adjoint has the same real/norm bounds.

On the collar, S_R<=S(3.3)<9/5000=:Vstar and1/r+epsilon+lambda*S<=621/1250=:c0. Set N=||u||,K=||grad u||. Angular energy gives K^2>=870N^2/64. The outer DtN term in the weak form has nonnegative real part, so

    Re a(u,u)>=K^2/2-c0*N^2
       >=252003/40000*N^2>6N^2,
    Re a(u,u)>=84001/181250*K^2>23K^2/50.

Continuity of the trace/DtN pairing and Lax-Milgram give the continuous inverse, not a finite-matrix inference. Zero inner trace permits extension by0 intoB4, yielding ||u||_S8^2<=8K^2/29. For bulk f and outer boundary load g8 the sufficient estimates are N<=(||f||+||g8||)/6, K<=3(||f||+||g8||)/5, with boundary load carrying the kinetic1/2 factor.

For inner data b use the harmonic lift Lb=sum(4/r)^(l+1)b_lmY_lm. Its L2 norm is<=sqrt(4/57)||b||; its outer mismatch is<=(31/4)2^-29||b||. Thus the Poisson bound is

    sqrt(4/57)*(1+c0/6)+(31/24)*2^-29 <.287.

The proof starts with H1/2 traces and extends the bounded volume map to L2. It does not assume all L2 boundary data have finite-energy harmonic lifts.

## Exact perturbation, source and a bounded first correction

For u_lambda=P_lambda b and incoming-adjoint v=P_0^-c, Green's identity cancels the outer flux and gives

    <c,(T_lambda-T_0)b>=2lambda integral_collar conjugate(v)*S_R*u_lambda.

The inner normal is opposite the collar outward normal; the factor2 is fixed by -Delta/2. The Poisson norms imply the stated DtN difference. A zero-inner-trace source produces normal data with norm<=.574||f||. The parent wphi norm bound1.106e-4 therefore gives6.34844e-5 for this source part. Xi's source and the lifted isotropic Y source are not mixed; low-induced high source is retained.

Here q=||R_0,D lambda*QS_RQ||<=Vstar/6=3/10000<1, so first Born is genuinely norm-controlled even atlambda1 in this collar. If P1=P0+R0 lambda*QS_RQ P0,

    ||P_lambda-P1||<=.287*q^2/(1-q)
       <2.58377513254e-8,
    ||(T_lambda-T0)-T1||<=.0002965284*q/(1-q)
       <8.89852155647e-8.

T1=2lambda*(P0^-)^*S_RP0. These bounds concern EXACT Born integrals, not numerical quadrature error. An actual ell29,m0 diagonal probe atlambda1 used5radial panels,10/16points per panel,96angular points and42digit Coulomb evaluation. Its real values are7.8185276333112015e-5 and7.8185276333112088e-5; imaginary part is approximately1.144e-54. This is numerical checking. The integrand uses [H_l^+(r)/H_l^+(4)]^2, not its modulus square, and no extra r^2 after boundary normalization.

The all-L induction and form bounds above are analytic with interval-checked seeds. Infinite low/high return, actual screened potential/source beyond8, global reference bulk residual and amplitude-functional error remain open. Global intensity/weighted inverse/two-centre thermal rate remain null. No new physical calibration or observational omission budget is asserted.

## Live REI Codex support, with attribution

The user's parallel request was executed against the ACTUAL live AXBI worktree, not just public PR summaries. Its cold MD14/stellar-blackbody scenario is distinct from warm P01/SHEAR12. Stellar50000K is not the gas temperature; gas starts near8.098K and the completed pilots reach about22.566K. The HH certificate's49999.63846..50000.36154K gas domain is inapplicable. HH is explicitly OPTIONAL_OFF_NONBLOCKING. This is source-contract separation, not a physical bound proving omitted HH negligible.

Initially AX06 was stopped by224MiB output cap: old spectra.csv221886108bytes. While this task proceeded, the OTHER CODEX SESSION repaired spectrum cadence and ran both revised pilots. It produced FLRW and SHEAR_PLUS throughz19.8, each3882accepted steps with exit0. This HH task did NOT change its driver, STATE, allocation or production switches and launched no REI solver.

A new HH-owned read-only reviewer actually checked every3883state rows per case, all abundance/recorded ledger rows,66complete392-node spectra per case and18output hashes against the producer receipt. All50conditions passed: coverage, positivity, actual helium normalization, proper dilution, nuclei/charge, J1/reflection, photon/energy ownership sums, E*n=u, initial/terminal snapshots and recorded resource/feedback diagnostics. These are saved-data and ledger checks, not continuous-time convergence or underlying cumulative-source re-integration. Numerical maxima: charge1.02e-19,baryon2.23e-16,J1relative4.72e-16,spectralstockrelative1.69e-15. Separate implementation identity is retained in the archive.

The07:26:42UTC supplier decision is PASS_SCOPED_SAVED_PILOT_DATA_READY_FOR_AX07_AX08_OWNER_TRANSITION. At that instant the owner awaited review. LATER actual STATE and FULL_START_CHECKPOINT reads show AX06 COMPLETED/SCOPED_PILOT_PASS and AX07/AX08 IN_PROGRESS/FULL_INTERVAL_RUNNING. The owner's checkpoint is dated2026-10-14T07:43:36.333192Z; its full binary SHA256 is32d11e733155d355a1fa748597b48ea1c8196adba3c871722a7a598f0b6cbfca. Partial checkpoints reachz19.54686644798 and19.65889433408, notz4. The owner has its OWN decision records; no evidence proves our supplier review caused its transition. Do not duplicate or cancel its running campaign.

The immutable science archive contains the earlier07:26snapshot. The separate late observation below is intentionally post-archive metadata, not retroactive alteration. No private raw REI history is published in Git.

## Evidence and continuation

Actual Wolfram15.0.1:18scalar literalzeros in12groups,6True conditions. Actual xAct/xTensor1.3.0:4Euclidean Green/potential/gradient/normal zeros; official source hashes matched. New collar generator12conditions, separate30checks and actual50supplier checks passed. Counts overlap; same-author arithmetic/CAS, no external independent scientific reviewer or native subagent. No old BVP/rate/chemistry/native/HPC campaign.

Full Korean proof, source, exact interval outputs, actual Born probes, supplier reviewer, selected inputs, CAS submissions/observations and failures are in the immutable36-member ZIP,35manifest payloads,66167bytes,SHA256691565d705a33772a1ee3128966fd77b70a4ed8dab79fe2d03c155fc2c864a36. [Complete Drive bundle](https://drive.google.com/file/d/1YSA9DBJfJkvTHB67TcHurHibfBVQxUe3/view). [Supplier handoff](https://drive.google.com/file/d/1US5z_gUqqv_dfzuYM0mPN4BCR9jPLAqi/view). Local CRC/all35hashes,11assemblychecks and relocated/altered/restored verifier are preserved. Provider ACK is not remote restoration. Post-upload receipt records Dropbox outcome separately.

Preserved failures include live pilot-receipt schema evolution, missing remote output folder, rejected malformed optional text transport, remote cwd warnings, one safety-status-blocked metadata request not retried, and prior PHYS33B Dropbox ALREADY_EXISTS with no overwrite. Source, thresholds and tolerance were not relaxed. SciSpace/Exa supplied primary DtN/Poisson method discovery; DLMF33.4 defines the Coulomb recurrence. The constants here are directly derived, not imported from free-Helmholtz papers.

Next same-node task: SCREENED_COLLAR_LOW_RETURN_AND_FAR_EXTERIOR. Reuse the closed high collar, bind low-return Schur/source/readout, actualr>8 weighted exterior and residuals. In parallel read the live REI owner's next actual checkpoint and supply only relevant HH-scope blockers; keep optional HH out of the baseline gate. Existing model-specific rate/response certificates, HH_STRICT_NATIVE, HH_SINGLET, globalRUX and production OFF are unchanged. No merge or external-repo mutation.
