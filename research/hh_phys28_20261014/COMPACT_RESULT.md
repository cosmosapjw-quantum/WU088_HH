# PHYS28: continuum orthogonality and Coulomb threshold comparison

2026-10-14. Parent PR60 c56cae5662a4c44b4f387699b5602355e63cb7dc. Selected PHYS28_CONTINUUM_ORTHOGONALITY_AND_CHANNEL_CALIBRATION, R5 constructive derivation and local checks. The model comparison is completed; empirical calibration and the full finite-window Coulomb thermal rate remain open. Same-author evidence, not external independent scientific review.

## 1. Exact projected-free comparison

Keep S65 spectator1s, the original classical spin potentials and sudden formula, CM E/I0 in[1,2], I0=13.605693122990eV, a0=5.29177210544e-11m, inherited mH=1.67262192369e-27kg, reduced mass mH/2 and the tagged adapter sigma_event=2sigma_tag, k=<sigma_tag v>. r=physical_r/a0, kappa=a0*p/hbar, Ea=2I0. Source I0 and receiver chiH=13.598434599702eV remain distinct. No natural-unit substitution; background signature(-,+,+,+).

Actual NASA PDF page images4–6 confirm the product bound initial state and plane-wave final state. The spectator-averaged perturbation is V_R/Ea=S(R)-S(|r-R|), S(r)=(1+1/r)exp(-2r). For phi=exp(-r)/sqrt(pi), reduced M/(8sqrt(pi)Ea*a0^(3/2)) is A_PW=S(R)o-C, o=(1+kappa^2)^(-2), C=(8pi)^(-1)integral exp(-r)S_R exp(-i*kappa.r)d3r.

The plane-wave overlap is <kappa|phi>=8sqrt(pi)o. Q=1-|phi><phi| gives exactly

    A_Q=D(R)o-C,
    D=<phi|S_R|phi>=exp(-2R)*(3/8+3R/4+R^2/6).

Density and screened-potential Fourier transforms give Dhat=64pi/(q^2+4)^3+256pi/(q^2+4)^4. An independent split radial convolution agrees. D(0)=3/8. An electronic identity shift lambda(R) changes A_PW by lambda*o but cancels from A_Q.

The Q states are not mutually delta-orthogonal free eigenstates. Their Gram kernel is delta-s(kappa)s(kappa')*. The declared diagnostic uses the positive compressed free spectral measure Q P0(dE) Q, with total Q. Its integrated transition strength is the exact variance <V^2>-<V>^2. Q removes1s only, not every bound state; no new density of states or ad-hoc normalization is inserted.

At50000K, actual new quadrature yields k_Q=9.6944439098188e-13cm3/s. Orders20,32,44 give9.694443909818787e-13,9.694443909818777e-13,9.694443909818763e-13. This is refinement evidence, not a new interval certificate. The ratio to the reported restored-PW reference is approximately0.127018. The Q threshold is0.808969155590*delta^(3/2), delta=E/I0-1. Parent PHYS25–27 certificates remain attached to their original model.

## 2. Prior/post residual identity

For H=Hi+Vi=Hf+Vf, ri=(Hi-Ei)Phi_i, rf=(Hf-Ef)Phi_f and a self-adjoint pairing with appropriate boundary conditions,

    Mprior-Mpost=(Ef-Ei)<f|i>+<rf|i>-<f|ri>.

This follows directly from Vi-Vf=Hf-Hi. In the frozen electronic example hc/Ea=-Delta/2-1/r, h0/Ea=-Delta/2, Ei/Ea=-1/2 and Ef/Ea=kappa^2/2. Hi=hc,Hf=h0 gives the explicit reduced discrepancies

    DeltaA_PW=1/[2(1+kappa^2)],
    DeltaA_Q=(kappa^2-1)/[2(1+kappa^2)^2].

The second remains nonzero despite bound overlap0, because Q|kappa> is not an h0 eigenstate. Frozen electronic energy differences are distinct from full on-shell collision energy. The consistent one-centre comparison uses Hi=Hf=hc and its exact bound/continuum states. This supplies a consistent electronic partition, not an exact two-electron nuclear scattering solution.

## 3. Exact one-centre Coulomb final state

For attractive eta=-1/kappa, choose the unit incident amplitude bra

    chi_minus_star=N_k exp(-i*kappa.r)
      *1F1(i/kappa;1;i*kappa*(r+khat.r)),
    N_k=exp(pi/(2kappa))Gamma(1-i/kappa),
    |N_k|^2=2pi/[kappa*(1-exp(-2pi/kappa))].

Use the corresponding spectral measure d3kappa/(2pi)^3. Same-hc bound/continuum orthogonality removes the electronic identity term exactly:

    A_C=-(8pi)^(-1)integral exp(-r)S_R chi_minus_star d3r.

With standard regular Coulomb functions F_l, define

    s_l(r,R)=(2rR)^(-1) integral_|r-R|^(r+R)
                 (s+1)exp(-2s)P_l((r^2+R^2-s^2)/(2rR))ds,
    c_l=1/2 integral r^2 exp(-r)s_l F_l(-1/kappa,kappa*r)/(kappa*r)dr.

The exact angular intensity is the positive sum sum_l(2l+1)c_l^2. This retains spatial continuum distortion and cannot be replaced by a constant Sommerfeld multiplier. Finite-kappa code and independent zero-energy3D quadrature are included.

Exact origin benchmark:

    c0(kappa,0)=1/2 sqrt[2pi/(kappa*(1-exp(-2pi/kappa)))]
       *(kappa^2+13)/(kappa^2+9)^2*exp[-2atan(kappa/3)/kappa].

The l0 bound overlap follows by differentiating in b the Laplace transform proportional to exp[-2atan(kappa/b)/kappa]/(b^2+kappa^2). Its negative derivative is proportional to2(b-1)/(b^2+kappa^2)^2 and vanishes at b=1. Actual CoulombF origin/overlap/ODE checks agree.

## 4. Global Coulomb threshold law

At fixed r,l,

    sqrt(kappa) F_l(-1/kappa,kappa*r)/(kappa*r)
       ->sqrt(pi/r)J_(2l+1)(sqrt(8r)).

Let L_l=sqrt(pi)/2 integral r^(3/2)exp(-r)s_l J_(2l+1)(sqrt(8r))dr and H0(R)=sum_l(2l+1)L_l^2. The common Coulomb phase is removed before the amplitude limit; it cancels from intensity.

For a=r+khat.r in[0,2r] and0<kappa<=1/4,

    |(i/kappa)_n(i*kappa*a)^n| <=(1/4)^n(4)_n a^n,
    |1F1(i/kappa;1;i*kappa*a)|
       <=exp(a/4)[1+3a/4+3(a/4)^2/2+(a/4)^3/6].

Together with bounded sqrt(kappa)|N_k| and the exponential source, convolution with S is bounded by a constant times(1+R^3)exp(-R/2). Its square is integrable against the path weight. Dominated convergence therefore applies to all angles, the moving turning radius and kappa=sqrt(delta)t. The original sudden phase-space integral gives

    sigma_C,s/a0^2=128G_C,s*delta+o(delta),
    G_C,s=integral_r_s(1)^infinity R J_s(R,1)H0(R)dR >0.

For positivity, L0(0)=13sqrt(2pi)exp(-2/3)/162>0. Writing f(R)=exp(-R)J1(sqrt(8R))/sqrt(R), one has L0=(8sqrt(pi))^-1(f*S) and (-Delta+4)^2L0=(sqrt(pi)/2)(-Delta+8)f. The radial equation is analytic for R>0, so L0 cannot vanish on the entire halfline above the positive turning radius. The positive path measure yields G_C,s>0.

Numerically the unpolarized linear coefficient is0.4557183066460,0.4557183066552,0.4557183066552 for Lmax6,10,14 with simultaneous radial refinement. Singlet0.718850709020, triplet0.368007505867. The linear threshold law is derived; displayed coefficients are numerical, not full truncation/roundoff certificates. Parent restored PW has4.087702111604*delta^(3/2), Q has0.808969155590*delta^(3/2). Different powers imply Coulomb dominance sufficiently near threshold within these specified models. The finite-window Coulomb thermal rate and any finite crossover remain uncomputed.

## Evidence, reuse and continuation

Actual Wolfram15.0.1:11 scalar literal-zero residuals. Actual xAct/xTensor1.3.0:5 projector/Green tensor zeros. xTensor.m SHA25604e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36. Thirty changed-model numeric/algebra checks passed. Thirty-nine release/source-binding checks passed separately and overlap the evidence; no independent scientific review is claimed.

Two larger scalar requests returned502 with no mathematical output. Short rational Fourier/derivative checks succeeded on a different bounded route. Failed inputs and pre-analysis warnings are preserved. NASA images and SHA were obtained through Wolfram after web screenshot cache misses and container DNS failure. Interpreter caches were excluded from source-manifest checks after a packaging-only KeyError; no science changed.

Read current CR54 event/current/saltation, HE43 clock/source conditions and REI115 finite-bin memory proofs. Their numbers are not transferred into HH. Fixed-map projection/current preservation does not establish equivalence of changed ionization dynamics. PHYS27 observable intervals are not reassigned to Q/Coulomb. REI HH/CR/RCT OFF, HH_STRICT_NATIVE, HH_SINGLET ion-pair and globalRUX remain unchanged.

S65 primary equations and NIST DLMF33.2/33.10 conventions were read. SciSpace/Exa supplied orthogonality-method literature at explicit abstract/discovery scope; electron-impact/helium results are not same-neutral-channel calibration. No same-channel empirical benchmark was recovered in this bounded search.

Next: PHYS29_COULOMB_FINITE_WINDOW_RATE, the explicit finite-kappa/radial/partial-wave thermal calculation with its own error contract. No old PW precision, gas/photon ODE, native receiver or HPC run occurred. Two-centre distortion, exchange, E>2I0 physical tail and empirical calibration remain open. Full Korean proof, tested implementation, inputs, results and failure records are in the immutable archive listed by EVIDENCE_INDEX.json.
