# PHYS30: a whole-model Coulomb near-rate enclosure

2026-10-14. Actual PHYS29 PR62 parent `2410c0d8ffd62abf204c1ca38b19a64814058717`. Selected node PHYS30_COULOMB_FINITE_QUADRATURE_CERTIFICATE, R5 constructive derivation/local checks. External independent scientific review is not performed.

## Result and fixed contract

For T in[49999.63846,50000.36154]K, the unchanged PHYS28 one-centre Coulomb continuum/S65 sudden-classical-path model on CM E/I0 in[1,2] satisfies

    k_C(T) in[2.20545380e-12,2.21081970e-12] cm3/s.

Exact-endpoint full width5.365888883074583e-15 is below the predeclared1e-14 target. The center-T enclosure is approximately[2.205530604231724e-12,2.210742718824994e-12]. Exact Fractions, not rounded displays, are the SSOT. This includes the parent's numerical2.2056248383253494e-12 but does not certify every printed digit of that point value.

Using the inherited restored-PW uniform interval[7.6320925e-12,7.6326272e-12] gives C/PW in[.2889508,.2896742], a same-model-window reduction of[71.03258,71.10492]percent. Empirical atomic calibration, complete exchange/two-centre distortion, E>2I0 physical tail and measured-constant uncertainty remain separate.

Preserve r=physical_r/a0, R=physical_R/a0, kappa=a0*p/hbar, x=kappa^2; I0=13.605693122990eV, a0=5.29177210544e-11m, inherited mH=1.67262192369e-27kg, reduced mass mH/2, kB=1.380649e-23J/K, eV_J=1.602176634e-19. Receiver chiH=13.598434599702eV is distinct. Keep sigma_event=2sigma_tag, k_network=<sigma_tag*v>, spin weights1:3. Signature(-,+,+,+), Euclidean atomic space; no natural-unit substitution.

## Flat endpoint: positive factor, not false holomorphy

For the parent's u_l=sqrt(kappa)*F_l(-1/kappa,kappa*r)/(kappa*r)=N_l*r^l*f_l, use its exact recurrence

    a_-1=0, a_0=1, a_n=-(2a_(n-1)+x a_(n-2))/(n(n+2l+1)).

Factor the squared normalization as N_l^2=h(x)*p_l(x), where

    p_l=2pi*4^l*product_(j=1..l)(1+j^2*x)/((2l+1)!)^2,
    h(x)=1/(1-exp(-2pi/sqrt(x))), h(0)=1,
    1<=h(x)<=h*=1.0018709365986606441007763455974....

Let J_l,N=1/2 integral_0^(R+b) r^(l+2)e^-r s_l f_l,N dr. The stripped intensity sum(2l+1)p_l J_l,N^2 is nonnegative on the physical domain, and the exact truncated intensity is h times that sum. Thus K_strip<=K_truncated<=h*K_strip. This encloses the ORIGINAL normalization; it is not a new h=1 physical model. Only the stripped function is analytically continued, so no holomorphic claim across the flat x=0 endpoint is required. p_l is polynomial; square roots do not appear in the continued squared normalization.

## Exact finite radial moments

Use s_l=(1-d_alpha)[I_(l+1/2)(alpha*r_<)K_(l+1/2)(alpha*r_>)/sqrt(rR)] at alpha2. With b_lj=(l+j)!/[j!(l-j)!4^j], define B_±(R)=sum(±1)^j b_lj/R^j and J_± with one extra factor j. Define polynomial P_±(r)=r*f_l,N(r)*sum(±1)^j b_lj*r^(l-j); P_(±,j) includes extra j. All powers are at least1.

Let Im=integral_0^R P_- e^r, Ip=integral_0^R P_+ e^-3r, Op=integral_R^(R+b) P_+ e^-3r. Subscript j changes P to P_j; subscript r inserts an extra r. With s=(-1)^(l+1), exact differentiation gives J_l,N=(Inner+Outer)/(8R):

    Inner=e^-2R {[(3/2+R)B_+ +J_+/2](Im+s Ip)
                  +B_+[(Ijm+s Ijp)/2-Irm+s Irp]},
    Outer=e^2R {[(3/2-R)B_- +J_-/2]Op+B_-[Ojp/2+Orp]}
         +s e^-2R {[(3/2+R)B_+ +J_+/2]Op+B_+[Ojp/2+Orp]}.

The moment M_m(beta,R)=integral_0^R r^m exp(-beta*r)dr, beta=-1 or3, is seeded at m=154 by

    M_m=R^(m+1)e^(-beta R)*sum_(j>=0)(beta R)^j/(m+1)_(j+1).

Terms j=0..512 plus the first omitted term divided by1-|beta R|/(m+515) bound the remainder. Then M_(m-1)=(beta M_m+R^m e^(-beta R))/m. All seed/recurrence/subtraction rounding and cancellation is propagated with directed MPFR intervals. This eliminates finite electron-r quadrature AND runtime Bessel/Coulomb library evaluation. Plain binary64 evaluation of these cancelling finite expressions is not recommended or claimed accurate.

## New finite outer proof

The original positive Maxwell energy primitive W=[(e0+1/q-V)e^-qe0-(2+1/q-V)e^-2q]/q remains exact. q=I0/(kBT/eV_J), V=U+R U'/2. R panels are[r(2),r(1+x)],[r(1+x),1],[1,2],[2,4],[4,8],[8,10]. Map R=A(x)+D(x)t. On panel0 e0=U; elsewhere e0=1+x, removing the max kink. The stripped integrand is D R W Hstrip/[2(1+x)^2]. The rate prefactor is the unchanged P=25600sqrt[8eV_J/(pi*(mH/2))]*(kBT/eV_J)^(-3/2)*(100a0)^2 I0^2.

Complexify only x or only t on the rho2 Bernstein ellipse, inside[-1/8,9/8]+i[-3/8,3/8]. Directed50-digit complex boxes prove positive ReR and valid turning log/sqrt branches. Set v=infReR>0, Z=sup|R|, w=sup|ImR|, zeta=min(Z-v,w^2/(2v)), B=Z+b. Along0->R->R+b, |r|-Re(r)<=zeta and total length<=B.

With X=sup|x| and lambda>=1,lambda^2>=X, induction gives |a_n|<=lambda^n/n!. Use lambda=11/10 for complex x and1 for real x. Positive I series and the half-integer K formula give |I_nu(z)|<=I_nu(|z|), |K_nu(z)|<=exp(|z|-Re(z))K_nu(|z|). Positive-real derivative ratios zI'/I,z|K'|/K<=z+nu, and the real Yukawa angular coefficient bound1/r_>, imply

    |s_l|<=exp(2zeta)*(l+3/2+|r|+|R|)/v,
    |J_l,N|<=B^(l+3)*(l+3/2+B+Z)/(2v)
                 *exp[(lambda-1)B+3zeta].

Combine with |p_l(x)|<=p_l(X) and directed D/R/W/denominator bounds. Exact upward-rounded pairs(M_x,M_t) for panels0..5:

    singlet:(2^56,2^48),(2^59,2^53),(2^56,2^51),
            (2^60,2^56),(2^70,2^65),(2^72,2^63);
    triplet:(2^56,2^48),(2^62,2^50),(2^55,2^50),
            (2^60,2^55),(2^70,2^65),(2^72,2^63).

Chebyshev degree2n-1 truncation plus the norm-one positive integration/Gauss operators gives |I-Q_n|<=8M*2^-2n. Telescope IxIt-QxQt=(Ix-Qx)It+Qx(It-Qt). n_x=n_t=56 and spin1:3 yield E_Q<3.006421e-18cm3/s. This is a complex-domain remainder, not an observed refinement estimate. Full box endpoints are in ANALYTIC_OUTER_BOUNDS.json.

## Actual roundoff closure and full assembly

All56 Gauss roots have disjoint width3e-200 rational sign-changing brackets verified by exact Fraction recurrence. Degree56 proves exactly one root in each and exhaustion. The weights are directed evaluations of2(1-z^2)/(56^2 P55(z)^2), with positivity and total-mass inclusion.

Actual GNU MPFR4.2.2 at512bits, g++14.2.0 -O2, directed arithmetic/exp/log/sqrt/FMA and moment tails enclose every computed value. The default installed libmpfr.so.6 was used; a preserved minimal MPFR4 ABI declaration was needed where mpfr.h was absent. Build/source/header/binary/library identities are recorded. Four LOCAL numeric processes are not native subagents or HPC. Pilot node0 completed and all8 remaining node batches returned0; all56 nodes occur exactly once. Hex binary64 RNDD/RNDU endpoints are converted to exact Fractions for assembly.

The stripped exact product quadrature is near2.2055336106912008e-12, with export width3.5317475426866125e-28cm3/s. The certifier uses L32,M10,b12,N120, different numerical cutoffs from the parent L40/M14 point run. SAME inherited omission theorems are evaluated at the NEW cutoffs:

    ell>32:3.827779e-16; R>10:6.969048e-16 (positive),
    r>R+12:3.896187e-23; seriesN120:4.473124e-42 (two-sided).

Let Epos be the two positive bounds, Esym the two symmetric bounds. Full center-T rate lies in

    [Qlo-E_Q-Esym, h*(Qhi+E_Q)+Esym+Epos].

Positive Maxwell-kernel endpoint ratios0.99996518039423805868... and1.00003482023621036653... cover the entire inherited T box. The final width is dominated by the conservative h envelope(~4.12642e-15) and positive tails(~1.07968e-15), not roundoff. The target is met; optional tightening was not made another gate.

## Evidence and applicability

Actual Wolfram15.0.1:31scalar zeros in13groups. Actual xAct/xTensor1.3.0:4Euclidean Green/norm/Gram zeros, xTensor.m SHA25604e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36. Scripts precede submissions; stored outputs are selected normalized transcriptions. Separate mpmath220digit checks cover40moments and13radial values;4complete intensity probes use the parent's distinct radial/Bessel formula.27interval utility conditions and the final source/result verifier are recorded. Same author and actual CAS, not external independent scientific review.

Failures preserved: unavailable streaming container call before execution, confirmed absent driver followed by supported bounded subprocess execution, formal-symbol Wolfram pre-analysis warnings, and an OPTIONAL hand-rounded comparison display rejected by exact outward assertions. Exact floor/ceiling repairs only that display; main certificate/model/target are unchanged. Tests-after; no full TDD claim.

Read NEW CR56 moving seeded event proof at34f8a64232892679f772465eab02200805e43d47 and HE45 R10 source-column closeout at1da6581d6435a312fd4c3d36dd754554279aeb05. Fresh REI115 head8bf8e3c18d607334614cfea734f9b10961fbd4d4 R7 now closes its same-source saved-node/bin time error; do not repeat its older pending label. Reuse exact-lift/remaining-defect and active-source versus passive-column distinctions, not their foreign coefficients. No old PHYS27 optical result is rescaled by the new Coulomb rate.

Next PHYS31_COULOMB_RATE_SOURCE_BOUND_TRANSFER: use actual P01 source/tube/clock/thermal/event coefficients and this rate interval; verify changed-source domain/gap before observable transfer. This next node was NOT run. No old PW/source512/chemistry ODE/native/HPC replay, no physical calibration, no merge/production activation. HH_STRICT_NATIVE, HH_SINGLET ion-pair, globalRUX and HH/CR/RCT OFF stay unchanged.

Full Korean proof, exact outputs, tested code, parent29 inputs, failures and handoff are in the immutable archive identified by EVIDENCE_INDEX.json. Primary references: NIST DLMF10.49/8.7 and GNU MPFR4.2.2 manual. SciSpace/Exa literature was discovery/abstract scope, not an attributed proof of this source-specific theorem.
