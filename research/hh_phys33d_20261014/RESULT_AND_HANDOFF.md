# PHYS33D: all-angular collar inverse, low return and REI source-pair binding

2026-10-14. Selected R5 construction/local checks. Parent PR67 b7746cdcfe692d90ac343bc4f04d6c440dd053a6 and actual attached PHYS33C archive691565d705a33772a1ee3128966fd77b70a4ed8dab79fe2d03c155fc2c864a36. Global PHYS33 remains partial. No old atomic-rate/BVP/chemistry/native/HPC producer is replayed.

## New quantitative result

Keep h_lambda=-Delta/2-1/r-lambda*S_R, S_R=(1+1/s)exp(-2s), s=|r-R ez|, R=kappa=7/10, lambda in[0,1]. r=rphys/a0,kappa=a0*p/hbar,epsilon=kappa²/2,h=H/Ea,Ea=2I0. I0=13.605693122990eV differs from receiverchiH=13.598434599702eV; a0=5.29177210544e-11m. Preserve the1s source, transitionS(R)-S_R, old-overlap readout and tagged-channel normalization. Physical c,hbar,kB retained; background(-+++), Euclidean atomic space.

In the exact collar4<r<8, inner Dirichlet and pure-Coulomb outgoing boundary at8, the NEW all-angular/all-m continuous inverse satisfies

    pure Coulomb ||R_C,D|| <=28,
    screened ||R_lambda,D|| <=35000/1187 <29.487.

For physical Q=ell>=29 and P=I-Q, the previously omitted low-return DtN contribution is

    ||Q T_all,lambda Q-T_Q,lambda||
       <=46703223/2967452750000 <1.573849e-5.

Adding the parent high-only correction gives

    ||Q T_all,lambda Q-T_C,Q||
       <=9266372390331/29674527500000000 <.000312266890.

The boundary-energy relative bound, for Bpartial=4 sum(l+1)|b_lm|², is

    eta_boundary=3088790796777/74186318750000000 <4.163559e-5.

It fits the parent's .19 allowance. Joining it to the physical B4 high form gives mass coercivity>10 and inverse<=1/10. The low return is included in4..8, not in the whole interior/exterior. Actual screened r>8 and interior low-channel/global readout duties remain separate. Individual DtN maps are not asserted L2-bounded; these potential-induced differences are. Norms use the stated dimensionless coordinates; physical inverse and DtN carry1/Ea and1/a0.

## Constructive continuous proof

Use H_l^+=G_l+iF_l, d_l=Hprime/H and physical t_l=d_l-1/r. The parent's exact100->4 fundamental/Volterra disk is consumed unchanged. Only new4->8 propagation is performed. For ell0..8 define z_l(4)=0,z_lprime(4)=1 and h_l(8)=1,h_lprime(8)=d_l(8). The exact Wronskian is W(z,h)=-h(4), hence

    g_l(r,t)=2 z_l(r<)h_l(r>)/h_l(4)

is the kernel of(h_C-epsilon)^-1 with derivative jump-2. Reduced u/r maps radialL2(dr) unitarily to the physical angular volume norm.

Use64whole cells of width1/16 and degree64 interval Taylor polynomials. For ell<=8, complex radius1 about r0>=4 gives first-order matrix norm<10 and unit-state sup exp10<3^10. The common value/derivative tail is3^10*(1/16)^64/(1-1/16). All elementary operations use mpmath.iv100digits; exact rational endpoints are retained. No Coulomb point value is an enclosure input. All h_l(4) intervals exclude0.

Tiling the full64x64 kernel square with whole-cell ranges gives Hilbert-Schmidt upper bounds. Upward short values for ell0..8 are27.442862562,18.714036499,12.959917053,12.067109151,9.956946486,7.479557611,4.960892000,3.057918157,2.043476521. Diagonal cells use their entire square area as an overbound. Exact cell intervals are in the archive; no grid-refinement difference is used as the norm bound.

The actual seed Re d8(8)<0 closes all higher modes. Let alpha_n=n/8-1/n and beta_n²=.49+1/n². Then

    d_n=-alpha_n+beta_n²/(alpha_n-d_(n-1)),
    alpha_n²-beta_n²=n²/64-.74>0 for n>=9.

Re d_(n-1)<=0 implies Re d_n<=-alpha+beta²/alpha<0. Also |d_n|<=n/8+1, supplying trace continuity. In ell>=9 the pure-Coulomb form obeys

    Re a >=K²/2-(1/4+.245)N²>=333/1600 N²>N²/5,
    K²>=90N²/64.

The outgoing boundary has nonnegative real energy. Continuous coercivity gives inverse<=5. The direct sum of the9low kernel inverses and infinite high block has norm<=28; angular degeneracy is not summed into an operator norm.

S_R<=V*=9/5000 in the collar gives q0=28V*=63/1250=.0504<1. Bounded perturbation yields35000/1187 for the full screened inverse and also for the compressed lowP inverse. This is a norm certificate for a continuous finite-collar realization, not whole-space unweighted positive-energy resolvent control.

## Low-return, source and readout

The blocks are A_Pp-lambda*S_PQ q=fP and -lambda*S_QP p+A_Qq=fQ. Eliminating p retains p=R_P(fP+lambda*S_PQ q), the induced high source lambda*S_QP R_P fP, and the full readout Jp+Jq. A noncommuting exact finite-matrix check rejects omission of the source term.

For high inner trace b and zero low trace,

    q=q0+R_Q lambda*S_QP R_P lambda*S_PQ q.

Parent R_Q<=1/6 and high Poisson C_Q<=.287 imply

    alpha_return<=(1/6)V*²(35000/1187)=189/11870000<1.

The high zero-inner-trace source-to-normal gain is2C_Q by the incoming-adjoint Green identity. Thus the DtN return is bounded by2C_Q²V*²(35000/1187)/(1-alpha_return), giving the fraction above. The added inner-high form costs at most eta_boundary*Kstar²/2. Parent quadratic coercivity becomes

    mass >=345/32-(435/16)eta_boundary >10.

This closes an actual continuous inner-high/collar join; it does not remove the interior low or far exterior obligations.

## Explicit far first-Born component

For ell0..8 and r>=8, q_l=.49+2/r-l(l+1)/r² lies in[-77/200,37/50]. All nine actual d_l(8) rectangles satisfy |d_l|<1. A normalized outgoing state(h,hprime) then has squared norm<=2exp[7(r-8)/5]. With S_R<=6e-7 exp[-2(r-8)],

    ||sqrt(S_R)P_C,8 P_(ell<=8)||²<=2e-6,
    ||P_(ell<=8)T_far,firstBorn P_(ell<=8)||<=4e-6.

This is the exact first-Born low-low far map onS8. Higher Born terms and all-angular far control are not included. Do not add this S8 norm to S4 quantities without a trace adapter. Full far inverse, global intensity and two-centre thermal rate remain null.

## Live REI development support

Read the actual AXBI worktree at10:18:07UTC, HEAD64b7dd6a7cbe77795a4dbb66d3530ceae6885a90. The blocker was accepted-step resource exhaustion, not the previous pilot outputcap. ZERO/PLUS stopped after200000accepted steps atz10.269313869154184; owner-reviewed continuation and signed-family execution were active. Existing exact prefix-composition preparation was already reviewed and was not repeated.

The actual convergence reducer SHA256b49fbed5f31a45e866915846357d1ddfdef8708ff7ba97ed17695ec8a5c3dc60 checks each source file hash individually but did not bind the source pair before PAIRED/REFINEMENT labelling. A valid synthetic completed3node pair with unequal source bytes and no semantic relation actually reached diagnostic reduction. The original reducer already withheld scientific admission; no current real-data corruption is alleged.

The HH-owned helper/patch accepts identical source bytes or an explicit reviewed-semantic relation bound to both hashes; otherwise it produces typed HOLD before a comparison CSV. The declaration's semantic truth remains the owner's review obligation. An actual temporary patched-copy test passed10conditions: unknown/wrong relation rejected, same bytes and declared equivalent relation admitted, same-byte numerical CSV unchanged, consumer hash unchanged. Final non-object relation parser hardening passed6local unit methods. A final remote end-to-end recheck timed out without an observed result, so its completion is not asserted. The completed initial integrated test and final local parser tests have separate identities.

Supplier status: READY_FOR_OWNER_REVIEW_AND_SCOPED_SOURCE_PAIR_INTEGRATION. No live patch or STATE mutation. AX11's true history/refinement dependencies remain. No REI solver starts by HH. Latest published actual STATE at02b0576e573adfd00c807e3c8dae5c847ce8bb86 records conditional AX07 ZERO z20->4 completed, AX08inprogress, AX11pending. These are the owner's results, not HH production or full raw-data review. Optional HH remains OFF/nonblocking; stellar50000K is not the gas temperature for the previous HH rate-domain certificate.

## Evidence, preservation and next

Actual Wolfram15.0.1 returned18scalarzero components in13groups and6True conditions. Actual xAct/xTensor1.3.0 returned4Euclidean tensorzeros; official archive and source hashes matched. Separate new formula/point/arithmetic verification88conditions, far7conditions and joined5conditions passed. Counts overlap. Same-author arithmetic/CAS; external independent scientific review/native subagents NOT_RUN.

The checker first duplicated the inputs path and failed; original failed source/stderr are retained and the path-only repair passed88checks. Also preserve sandbox DNS, remote initial cwd warnings and final remote transport timeout. No scientific source, model or tolerance relaxation. Actual HE50 and CR61 compacts were read and their first-cell/initial-derivative versus full-forward distinctions reused, without importing foreign numerical gains. SciSpace/Exa and DLMF primary methods were used; Arellano-Blanchon1806.05006 is method context, not the source of these constants or a neutral-HH calibration.

Complete44-member archive,43manifest payloads,314275bytes,SHA2562bd9fdd7ddaf7171bddda92b6a9c55664764d8cfdf8b6a550fe2b7ef2b43e6b5: [full Korean proof/code/exact intervals/CAS/failures/handoff](https://drive.google.com/file/d/1Em1zfZPZpXHd5hVaXnQkiz4qKb4B1a9w/view?usp=drivesdk). Dropbox completed the same314275-byte object, id:BSpOijBcT10AAAAAAD6V-Q, in the established HH folder. Local CRC/all43hashes, relocated70-condition verification, altered-source rejection and restored pass were observed. Provider acknowledgement/size is not remote restoration. No fonts/private raw REI histories are published here.

Next FAR_EXTERIOR_ALL_CHANNEL_RESOLVENT_AND_INTERIOR_MATCH: close weighted far all-channel/source/trace, interior low Schur and reference bulk/readout error. Do not replay the closed collar as a new gate. Preserve prior model-specific certificates, HH_STRICT_NATIVE, HH_SINGLET, globalRUX and production HH/CR/RCT OFF. No main/owner merge or external-repo mutation.
