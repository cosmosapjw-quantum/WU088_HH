# PHYS32: two-centre residual, restored identity term and outgoing correction

2026-10-14. R5 constructive derivation/local checks from actual PR64 head `6320b23cba96abf12b150eea439e458f86aa1d69`. Existing PW/Q/one-centre Coulomb rate and P01 certificates remain attached to their original models. This unit constructs a frozen-direct final-state comparison, not a new full HH rate or independent review.

## Operator and an exact term that must return

Use r=physical_r/a0, kappa=a0*p/hbar, Ea=2I0, epsilon=kappa²/2, h=H/Ea, phi=exp(-r)/sqrt(pi), eb=-1/2. Retain I0=13.605693122990eV, a0=5.29177210544e-11m, the parent mass/tagged adapter and separate receiver chiH=13.598434599702eV. Background signature(-+++), Euclidean atomic coordinates; no natural-unit substitution.

The frozen spectator1s electrostatic field is exactly

    w_R=-1/s+4[ integral_0^s t²exp(-2t)dt/s+integral_s^infinity t exp(-2t)dt ]
       =-S(s), S(s)=(1+1/s)exp(-2s), s=|r-R|.

Choose h_lambda=hC+lambda*w_R, hC=-Delta/2-1/r,0<=lambda<=1, with original transition source v_R=S(R)+w_R FIXED. Lambda is a diagnostic homotopy, not a fitted physical strength. Nuclear motion, exchange, spectator polarization/excitation and empirical calibration are not added. w is short range but NOT L-infinity bounded near the spectator nucleus. The asymptotic reference remains charge+1 Coulomb.

For the unit-incident incoming final state and G_C^±=(epsilon-hC±i0)^-1:

    (h_lambda-epsilon)chiC=lambda*w_R*chiC,
    psi_lambda^-=chiC^-+lambda*G_C^-*w_R*psi_lambda^-,
    (h_lambda-epsilon)(chiC+lambda G_C^- w_R chiC)
          =lambda² w_R G_C^- w_R chiC.

These identities do not alone certify the size of the state error at lambda1. Maintain the original d3kappa/(2pi)^3 continuum measure.

The old phi is not an h_lambda eigenstate. The exact left eigen-equation gives

    (epsilon+1/2)<psi_lambda^-|phi>=lambda<psi_lambda^-|w_R|phi>.

Let B_lambda=<psi_lambda^-|w_R|phi>/(8sqrt(pi)). The original transition source therefore yields

    A_lambda=[1+lambda*S(R)/(epsilon+1/2)]B_lambda.

Thus the electronic identity term previously removed by one-centre orthogonality returns. AtR=kappa=.7,lambda1 the factor is1.80386354496784469951632618929512.... This does NOT replace the spatially distorted B_lambda by a constant multiple of B0.

The first amplitude correction is

    A1=<chiC^-|w_R G_C^+ w_R|phi>/(8sqrt(pi))
          +S(R)A_C/(epsilon+1/2).

With fixed h_tot=hC+w_R+S(R), hi=hC,hf=h_lambda, vi=S+w,vf=S+(1-lambda)w, the exact prior-minus-post difference is lambda<psi|w|phi>=(epsilon-eb)<psi|phi>. Frozen electronic energies differ. Full collision on-shell prior/post equality still requires nuclear channel energies/wavefunctions and matching boundaries; it is not manufactured by forcing the old overlap to zero. Dressing the initial bound state too would define another source/threshold model.

## Exact 1s elimination

P=|phi><phi|,Q=I-P,b_R=Qw_R phi and D(R)=exp(-2R)(3/8+3R/4+R²/6). Write psi=alpha phi+q. Then

    alpha=lambda<b_R|q>/(epsilon+1/2+lambda D),
    h_eff=QhC Q+lambda Qw_R Q+Sigma,
    Sigma=lambda²|b_R><b_R|/(epsilon+1/2+lambda D).

The denominator is positive for the declared real energies; Sigma is positive rank one. Dropping Sigma after projecting changes the frozen operator. This P removes only the old1s state, not all bound states and not exchange. For normalizable algebraic vectors at a fixed real energy,

    ||psi||²=<q|[Q-d_epsilon Sigma]|q>,
    Q-d_epsilon Sigma=Q+lambda²|b_R><b_R|/(epsilon+1/2+lambda D)².

This is an induced metric, not arbitrary flux normalization of a continuum state. Feshbach/Schur elimination is standard; the explicit source term and application are provided here.

The exact source norm is ||b_R||²=D2-D², D2=<phi|S_R²|phi>. Two independent one-dimensional representations were evaluated at55digits: a spectator-centred angular integral and

    Y_alpha=4exp(-2R)/(alpha²-4)
           -16[exp(-2R)-exp(-alpha R)]/[R(alpha²-4)²],
    D2=-d_alpha Y_alpha|4+2Y4+integral_4^infinity Y_alpha d alpha.

AtR0, D2=25/27 and variance=1357/1728 exactly. AtR.7, D=.242076019602677...,D2=.362568928966203...,||b||²=.303968129699527.... Atkappa.7/lambda1, ||Sigma||=.307948044185981... inEa units. These high-precision moment values are numerical checks, not a rate error or a Born-convergence parameter.

## Actual outgoing numerical witness

Solve (epsilon-h_lambda)xi=w_R phi. The axisymmetric driven source needs only m0 and reconstructs the full final-direction amplitude. For xi=sum xi_l(r)Y_l0/r,

    w_lm=-sqrt[(2l+1)(2m+1)] sum_j(2j+1)s_j(r,R)*(3j(l,j,m;0,0,0))²,
    t_l=-2sqrt(2l+1)r exp(-r)s_l,
    xi_l''=[l(l+1)/r²-2/r-kappa²]xi_l+2lambda sum_m w_lm xi_m+2t_l.

The retained j<=2L exactly exhausts each projected matrix element. A distinct direct angular quadrature confirms the Hermitian negative matrix. No cusp smoothing is applied. At finite r0 andrmax impose CoulombF regular andH+=G+iF outgoing log derivatives; their finite-endpoint error remains separate.

DLMF W{G,F}=1 gives the radial Green kernel -2F(r_<)H+(r_>)/kappa, with derivative jump+2. Independent direct s-angle source and mpmath F/G integrals match l0/l1 driven probes to relative1.079e-11/1.790e-11. This validates sign/normalization numerically, not the global limiting-absorption inverse.

Output coefficients use B_l=sqrt(2l+1)/4 integral(F_l/kappa)[t_l+lambda(w xi)_l]dr and A_l=(1+lambda S/Delta)B_l. The angle average is sum|A_l|²/(2l+1).

AtR=kappa=.7 andL6:

    lambda0 intensity .00584549577865749,
    lambda.02 .00602957386740975,
    lambda.04 .00621547540393448,
    lambda.08 .00659237443391884,
    lambda1 .0149886625416591.

The small-lambda remainder norm divided bylambda² is.0471250,.0472257,.0474215. The first-corrected amplitude squared atlambda1 is.0208460033789864, about39.08% above the finite-couplingL6 result. Local O(lambda²) evidence is NOT sufficient to call first order accurate atlambda1.

Lambda1 partial-wave profiles:

    L6 .0149886625416591;
    L8 .0150317148452140;
    L10 .0150493278839064;
    L12 .0150578243121220.

A same-L12 control withr0=5e-5,rmax24,tol1e-8 gives.0150578243122200, relative change6.51e-12, whereasL10->12 shifts about5.65e-4. The tiny old high-l OUTGOING amplitude tail does not control V G V's INTERMEDIATE partial waves. Infinite-L convergence, endpoint/all-roundoff enclosure and the two-centre thermal rate remain OPEN/null. No model-family rate or P01 observable certificate is inherited for this new operator.

## Error contract and evidence

Use v=sqrt(S_R),K=v G_C^+ v and zeta=v psi in an appropriate weighted limiting-absorption space. Then(I+lambda K)zeta=vchi. IFq=|lambda| ||K||<1, the first Neumann error is<=q²/(1-q)||vchi||. Otherwise residual control requires an actual inverse-norm bound. Neither is numerically closed on the physical real axis here. The complex-energy1/Im(z) resolvent bound is not extrapolated to+i0. solve_bvp residual tolerance is not a continuum error certificate.

Actual Wolfram15.0.1:15groups/19scalar zeros. Actual xTensor1.3.0:4Euclidean Laplacian/Green/commutator/norm zeros; xTensor SHA25604e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36. Submitted scripts were saved first; selected outputs are normalized transcriptions, not raw transport.71stage-local conditions passed, including separate moment/Green, exact-matrix and numeric/domain tests. Counts overlap and are not external independent reviews. Native subagents/external reviewNOT_RUN. Tests-after, no full TDD claim.

Preserve the initial complex-BVP timeout and max-node failure. Equivalent explicit real/imag blocks with analytic Jacobians solved the same pilot without changing physics/tolerance; no SciPy upstream bug is claimed. Pre-analysis Wolfram and primary HTML retrieval warnings remain. NEW bounded atomic radial BVPs actually ran; old rate/chemistry/native/HPC campaigns did not.

Read NEW HE47 R2 at60654dbf241d097114319910f2fd78c1f6712aab, CR58 at808d11c1869c6334572554edcb24370e35c69f44 and REI115 R8 at39dce6702dcadbb516fc8e25e7ba5a6991f64c22. Use residual-versus-forward-error, projection-versus-eliminated-dynamics and model-specific-reference distinctions. No foreign coefficients or current/opacity numbers were imported. REI116 was metadata only. All original production switches remainOFF.

Primary context: actual DLMF33.2 definitions; Foulis0806.0574 and Volkov et al1102.0549 primary abstracts; Feshbach1962 and Domcke1983 primary metadata/abstract viaExa; SciSpace electron-H exchange methods remain method references, not same-neutral-channel calibration. No novelty claim for standard projection/LS theory or unseen full-text theorem.

Next PHYS33_TWO_CENTRE_MULTIPOLE_RESOLVENT_CONTROL: omitted intermediate-channel/self-energy and real-axis inverse control for the fixed new operator, separate from finite radial error. Preserve old physical/source/receiver constraints. No new total rate, merge, production activation or physical calibration. Full Korean proof, executable code, inputs, observations and failures are in the immutable archive referenced by EVIDENCE_INDEX.json.
