# PHYS33: cusp-adapted continuum and an interior high-channel inverse

2026-10-14. Actual PHYS32 PR65 parent15a9ee97d7c1b27f65e289e61c614ce3a1ab894c. Selected R5 construction and local checks. Status: PARTIAL_GLOBAL_OUTGOING_CONTROL. The exact representation and quantitative interior bound below are available; global weighted outgoing inverse, all-L intensity interval and thermal rate remain null.

## Exact unchanged operator

Keep r=physical_r/a0,R=physical_R/a0,kappa=a0*p/hbar,Ea=2I0,epsilon=kappa²/2; I0=13.605693122990eV and receiverchiH=13.598434599702eV remain distinct. Background(-,+,+,+), atomic Euclidean metric. With s=|r-R ez|,

    phi=exp(-r)/sqrt(pi), hC=-Delta/2-1/r,
    wR=-(1+1/s)exp(-2s), h_lambda=hC+lambda*wR,
    (epsilon-h_lambda)xi=wR*phi.

The original transition is S(R)+wR, not changed withlambda. First lift Y=phi+lambda*xi so that (epsilon-h_lambda)Y=(epsilon+1/2)phi. This removes the singular source; xi itself obeys the inhomogeneous averaged cusp xi'(A)=-lambda*xi(A)-phi(A).

Set J=exp[(lambda/2)exp(-2s)],Y=JZ. Exactly,

    htilde=J^-1 h_lambda J=-Delta/2-1/r+b.grad+V,
    b=lambda exp(-2s)shat,
    V=-2lambda exp(-2s)-lambda² exp(-4s)/2,
    (epsilon-htilde)Z=(epsilon+1/2)J^-1 phi.

1<=J<=exp(lambda/2),J->1. Spectator1/s is canceled, not replaced by a pseudopotential. Drift, source, boundary and readout must all stay. b is bounded but direction-discontinuous at the nucleus; no global analyticity or exponential convergence is asserted. The weak cusp has no point delta because s²(logJ)'->0.

htilde is symmetric in the J² metric, not ordinary L2. Physical current j[Y]=J²j[Z]. Resolvents satisfy G_lambda=J Gtilde J^-1; multiplication-weight norms incur at most exp(lambda/2), not an automatic bound on Gtilde. The finite Coulomb boundary becomes JZ'+(J'-LcJ)Z=phi'-Lcphi. Operator ordering is retained in angular matrices.

The old-overlap source identity remains

    B_lambda=<chiC^-|wR Y>/(8sqrt(pi)),
    A_lambda=[1+lambda*S(R)/(epsilon+1/2)]B_lambda.

Finite standard Pi_L Z and old Pi_L xi spaces differ. Infinite-dimensional equivalence is not equality of the two finite-L answers.

## Source-preserving Schur and local inverse theorem

For outgoing M=[[A,B],[C,D]],f=(f0,f1),u=A^-1f0,r1=f1-Cu,

    x1=(D-C A^-1 B)^-1r1,
    x0=u-A^-1B x1,
    (A-BD^-1C)x0=f0-BD^-1f1.

Keep the high source unless its vanishing is proved for the actual projector. If a=||A^-1B||,b=||D^-1C||,d=||D^-1r1|| and ab<1 in compatible outgoing spaces, ||x1||<=d/(1-ab). The amplitude error is (ell1-ell0 A^-1B)x1. Global numerical a,b,d are not yet enclosed.

A quantitative theorem DOES close for the physical Dirichlet interior. Restrict H1_0(B_a) to bare angular ell>=L+1, c=(L+1)(L+2). With N=||u||,K=||grad u||, angular energy gives K²>=c||u/r||²>=cN²/a². Since S(s)<=1/s, translated Hardy gives||u/s||<=2K. Thus

    <u,h_lambda u> >=K²/2-(2lambda+1/sqrt(c))NK.

When sqrt(c)/a>=2lambda+1/sqrt(c), the quadratic is increasing over the admissible K/N interval. The form of h_lambda-epsilon is bounded below by

    mu_L=c/(2a²)-2lambda*sqrt(c)/a-1/a-epsilon.

At a=4 and0<=lambda,kappa<=1, sqrt870<59/2 gives mu28>187/16, while sqrt462<43/2 gives mu20>47/16. Hence the restricted Friedrichs inverse, including INFINITELY MANY omitted angular modes, obeys

    ||(h_Q,D-epsilon)^-1|| <=16/187  for ell>=29,
    ||(h_Q,D-epsilon)^-1|| <=16/47   for ell>=21.

Physical inverse units are1/Ea. For ell>=29 the same energy inequality and exact rational root bounds give||grad(h_Q,D-epsilon)^-1||<=592/935. Eliminating these interior high channels gives a nonpositive low-Hamiltonian correction -Gamma with

    Gamma=lambda² P S Q(h_Q,D-epsilon)^-1 Q S P>=0,
    <u,Gamma u><=64lambda²/187*||grad u||².

The scattering field is NOT Dirichlet at r4. Interior/exterior trace, exterior screened potential/source and weighted real-axis stability remain to be joined.

Projector identity is mandatory: in Z coordinates the corresponding projector is Q^J=J^-1 Q J, orthogonal in J², not standard angular Q onZ. Reconstruct Yhat=JZhat before using the bare interior bound, or explicitly useQ^J. The gradient bound concerns physical JZ. Affine Y has isotropic source and zero bare-high forcing; standard Pi_L Z has generally nonzero J^-1phi high forcing. No incompatible norm/projector bound is multiplied into a diagnostic.

## Angular residual and the real-axis distinction

For standard angular projection ofZ, high residual is Q_L T with T=Delta J^-1phi+b.gradZhat+VZhat. Parseval gives

    ||Q_L T||2 <=||grad_Omega T||2/sqrt[(L+1)(L+2)].

The complete proof supplies explicit coefficient norms cb²=5pi lambda²(1+4R²)/8 and cV²=4pi[16lambda²(24/4^5+2R²/4^3)+16lambda³(24/6^5+2R²/6^3)+4lambda^4(24/8^5+2R²/8^3)], plus the remaining reference gradient/Hessian terms. Those reference norms have not been outward-evaluated globally.

A concrete Weyl packet prevents using the interior gap on allspace: f_n=n^-1/2 chi((r-n²)/n)exp(i*kappa*r), fixedell>L and normalized chi=(1-z²)^3 on[-1,1]. Its norm is1, while the residual is bounded by kappa||chi'||/n+||chi''||/(2n²)+1/(n²-n)+ell(ell+1)/(2(n²-n)²)+lambda*S(n²-n-R), tending to0. Exact derivative norms squared are39/10 and429/10. This rejects the unweighted global centrifugal-gap argument, not weighted outgoing control.

## Actual new numerical work

AtR=kappa=.7,lambda1, volume intensities are:

    L4 .015036203922730494; L6 .015064392922617733;
    L8 .015069195416908985; L12 .015070793054157006;
    L16 .015071014190247074; L20 .015071065123608975;
    L28 .015071086840479940.

SameL20 with stronger radial endpoints/tolerance gives.015071065155291328, relative2.10220e-9; L20->28 changes1.44096e-6. The old bareL12 .01505782431222 is preserved, not overwritten or called the same finite space. Boundary-flux/volume discrepancy declines from1.23061e-3 atL4 to1.66689e-7 atL28, but is not an error bound.

Actual saved cubic BVP references permit continuous-equation all-angle finite-shell residual quadrature. High-angular residual L2 is approximately.0216164,.00252836,.00107997,.000637710 atL4/12/20/28. L28 physical residual/source ratio is.00131724. These are diagnostics, not outward fullspace residual or intensity certificates. No new thermal rate or P01 transfer is issued.

## Evidence, actual repairs and latest-source use

Actual Wolfram15.0.1:19scalar zeros in corrected main call plus7zeros/4True interior conditions. Actual xAct/xTensor1.3.0:4Euclidean weighted-Green/kinetic/norm zeros. Scripts saved before calls; observed outputs are selected normalized transcriptions. Final75conditions pass, including exact Schur/interior/projector algebra, numeric representation, source hashes and negative controls. Same author plus CAS; external independent review/native subagents NOT_RUN.

First Wolfram Protected-C/derivative syntax failure remains. Strong realL20 hit4GiB OOM(-9); equivalent complex representation completed identical scientific settings. Large complex multiplication warning was traced to float allocation in a private SciPy helper; this fixed linear Jacobian has zero imaginary product. A scoped dtype-preserving adapter returned bit-identicalL28 and restored library binding. Saved-PPoly axis repair affected only the diagnostic reader. Original failed inputs/logs and formal-symbol warnings remain.

Read NEW HE48 full R3 result at4e72d4f648c106fce8feb44b3b40b5bac95cc2b3: coarse absolute warm-source interval now nonnull, fine residual pending. No warm gain imported as scattering inverse. Reuse the unchanged CR58 exact-projection/remaining-dynamics distinction. Read NEW REI117 README and PR at069d6c88306c58a98556b67f9955fcd720e7e95a: coupled execution overlay, not new physical admission. No external-repo mutation or foreign numeric import. SciSpace/Exa supplied primary cusp-method discovery; Bischoff2014 publisher abstract, DLMF33.2 equations and Foulis0806.0574 abstract were read within those scopes.

## Continuation and full durable evidence

Next SAME-node continuation:PHYS33B_INTERIOR_EXTERIOR_OUTGOING_CLOSURE. Bind the actual r4 trace/exterior and verified weighted residual before global inverse/intensity claims. The all-L intensity interval, global weighted inverse bound and two-centre thermal rate remain null. No old rate/source512/PHYS30/PHYS31/chemistry/native/HPC replay. Existing model-specific certificates, HH_STRICT_NATIVE,HH_SINGLET,globalRUX and production HH/CR/RCT OFF remain unchanged.

Full90-member ZIP,89manifest payloads,33013608bytes, SHA256c67f817bb0d8b3f8dbf863630b596412ed857c415647c29f6390d3362f8839d7. It includes full Korean/English proofs, tested code, actual dense references, parent source, CAS and failures. [Drive archive](https://drive.google.com/file/d/1MYjTeD4r2H25CuydIig3iSLSU4nA1iZI/view). Existing Dropbox ID id:BSpOijBcT10AAAAAAD5UVw completed with matching33013608bytes. Local CRC/all89payload hashes and relocation/altered-copy/restore checks passed. Both provider name/ID/size acknowledgements verified; no new remote full restore or permission change. This Git compact is not byte-identical to the longer archive proof. No merge or production promotion.
