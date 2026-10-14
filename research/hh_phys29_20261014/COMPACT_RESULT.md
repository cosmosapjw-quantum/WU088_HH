# PHYS29: finite-window Coulomb rate and analytic omission bounds

2026-10-14. Selected node PHYS29_COULOMB_FINITE_WINDOW_RATE, R5 constructive derivation with local checks. Parent PR61 f4e7d717dc9d358026d86bab3836bdcf5f476323. The finite-rate calculation and mathematical omission bounds are completed. The finite quadrature/all-roundoff certificate remains open; no external independent scientific review or native subagent was run.

## Result and preserved model

At50000K, the unchanged PHYS28 one-centre attractive Coulomb continuum gives k=2.2056248383253494e-12cm3/s (practical numerical display2.205625e-12). Singlet3.0611019243546637e-12, triplet1.920465809648911e-12. Ratios to recorded original S65, restored-PW and projected-free Q are0.188599703,0.288983378 and2.275143225. These are numerical model comparisons, not empirical calibration or certified physical suppression.

Retain spectator1s, original classical spin potentials and Rosen sudden formula, CM E/I0 in[1,2], I0=13.605693122990eV, a0=5.29177210544e-11m, mH=1.67262192369e-27kg and reduced mass mH/2, kB=1.380649e-23J/K, eV_J=1.602176634e-19. Source I0 and receiver chiH=13.598434599702eV remain separate. r,R are in a0; kappa=a0*p/hbar; no natural-unit substitution. Signature(-,+,+,+), Euclidean atomic derivatives. Unit incident continuum amplitude and d3kappa/(2pi)^3 are unchanged; sigma_event=2sigma_tag and k_network=<sigma_tag*v>.

No PHYS25–27 PW certificate/observable is reassigned to Coulomb. Full exchange, two-centre final-state distortion, same-neutral-channel empirical calibration and E>2I0 physical tail remain open. The derived linear threshold law and this smaller finite-window rate relative to restored-PW coexist: local asymptotic order does not determine the thermal integral over the whole window.

## Exact reduction and endpoint-regularized implementation

Set x=kappa^2 and u_l=sqrt(kappa)F_l(-1/kappa,kappa*r)/(kappa*r). From the Coulomb radial equation,

    u_l=N_l(x)*r^l*sum_n a_n*r^n,
    a_-1=0, a_0=1,
    a_n=-(2a_(n-1)+x*a_(n-2))/[n(n+2l+1)],
    N_l=sqrt[2pi/(1-exp(-2pi/sqrt(x)))]
            *2^l*product_(j=1..l)sqrt(1+j^2*x)/(2l+1)!.

At x=0 use the exact endpoint sqrt(pi/r)J_(2l+1)(sqrt(8r)), not a small arbitrary momentum. The normalization has a smooth real endpoint with a flat exponential term; holomorphic extension across0 is not assumed.

For S(s)=(1+1/s)exp(-2s), introduce Y_alpha=exp(-alpha*s)/s. Its exact Legendre multipole is

    Y_l=I_(l+1/2)(alpha*rmin)*K_(l+1/2)(alpha*rmax)/sqrt(rR),
    s_l=(1-d/dalpha)Y_l at alpha=2.

This removes the parent's s-angle quadrature. Scaled ive/kve and adjacent-order derivative recurrences prevent compensating special-function over/underflow. There is no smoothing at r=R. Define

    d_l=1/2 integral r^2 exp(-r)*s_l*u_l dr,
    H(x,R)=sum_l(2l+1)d_l^2=kappa*<|A_C|^2>.

Then kappa^2<|A_C|^2>d kappa=H dx/2. Reuse the parent's exact Maxwell-energy primitive, with U3=3.6exp(-1.48R), U1=.35(z^2-2z), z=exp[-1.08(R-1.5)], V=U+RU'/2, theta=kBT/eV_J, q=I0/theta, e0=max(1+x,U):

    W=[(e0+1/q-V)exp(-q e0)-(2+1/q-V)exp(-2q)]/q,
    k_s=P/2 integral_0^1 dx/(1+x)^2 integral_r_s(2)^infinity R W H dR,
    P=25600 sqrt[8eV_J/(pi*(mH/2))]*theta^(-3/2)*(100a0)^2 I0^2.

Six R panels split at r_s(1+x),1,2,4,8,M. The first has e0=U, the others e0=1+x. Electron radius panels split at R andR+3. This preserves the physical max-domain. Finite computation uses M14,b12 (r<=R+b), L40 and Frobenius degree120.

## Explicit analytic omissions, independent of grid differences

Directed65-digit elementary intervals verify P<3.28e-7cm3/s, q>3, both r_s(2)>.3 and0<=W<.4. A sufficient global |V|<17 follows from exp1.62<6, exp3.24<26 and maxima of t exp(-t), t exp(-2t); W<=19exp(-3)/3<.4.

For l>=3 the normalization satisfies N_l<=exp(pi/2)/(2l+1)!!. When kappa<=1/4, coefficient induction gives |a_n|<=(1/4)^n/n!. When kappa>=1/4, the Euler Kummer integral and gamma product give

    |1F1(l+1+i/kappa;2l+2;2i*kappa*r)|
      <=(l!)^2/|Gamma(l+1+i/kappa)|^2
      =product_(j>l)(1+1/(kappa^2*j^2))<=exp(16/l).

Thus |u_l|<=exp(pi/2+16/l)*r^l exp(r/4)/(2l+1)!! uniformly. With normalized Y_lm, S*(exp(-r)u_l Y_lm)=8pi d_l Y_lm and ||S||1=2pi. Young's inequality yields integral R^2 d_l^2<=1/16 integral r^2exp(-2r)|u_l|^2. Consequently

    E_l>L <=P exp(pi)/(160 rmin)
       *sum_(l>L)(2l+1)exp(32/l)*(2l+2)!/[(2l+1)!!]^2*(2/3)^(2l+3).

The nonexponential term ratio is4(2l+4)/[9(2l+1)], and exp(32/l) decreases. The geometric tail atL40 is below6.589e-19cm3/s.

The full Coulomb continuum spectral projection is a contraction. For g_R=exp(-r)S_R, integral_0^1 kappa^2<|A|^2>dkappa<=||g_R||2^2/32, including the incident-wave normalization. Since ||g_R||2^2<=5pi exp(-2R),

    E_R>M <=.4P*5pi/32*(M/2+1/4)exp(-2M)
            <3.229e-19cm3/s at M14.

A loose auxiliary full-rate upper is Kaux=P*pi/64. Cutting electron source r>R+b changes an amplitude, not a positive probability domain. Its rate-norm squared is bounded by

    B_b<=P*pi/20*(1+1/b)^2 exp(-6b)*(b^2/24+7b/72+17/216),
    E_r<=2sqrt(Kaux*B_b)+B_b <3.897e-23cm3/s at b12.

For x<=1 all l have |a_n|<=1/n!. On r<=B=M+b=26, tau_N=B^(N+1)/[(N+1)!*(1-B/(N+2))]. Using |s_l|<=s0 and integral R^2 C0^2<=1/64 gives

    B_N<=P*tau_N^2/(640rmin)*sum_l<=L(2l+1)exp(pi)B^(2l)/[(2l+1)!!]^2,
    E_N<=2sqrt(Kaux*B_N)+B_N <1.987e-32cm3/s at N120.

The exact upper formulas sum to below9.819e-19cm3/s, about4.4512e-7 of the numerical rate. They certify only the stated mathematical omissions. Finite x/R/r Gauss remainder and all Bessel/node/weight/elementary/summation roundoff remain unbounded globally. Accordingly global_rate_enclosure_cm3_s=null; no rate plus/minus this omission sum is issued as a total certificate.

## Actual computation and verification

Completed profiles(nx,nR,nr,L)=(12,12,24,12),(20,20,36,20),(28,24,44,40) give2.205624838277680e-12,2.2056248383252775e-12,2.2056248383253494e-12. Runtime7.11,58.77,244.43s. The predeclared refinement target was1e-5 relative. A different18-node kappa integration gives2.2056248382946613e-12, relative difference1.3914e-11. These are numerical checks, not rigorous error estimates.

The same stored x-integrands give mean emitted kinetic energy2.7229510993813193eV, a selected-model diagnostic rather than receiver thermal heating. Numerical partial-wave shares l0/l1/l2 are32.6298%,57.1107%,9.24669%.

31 new check groups include252 source-weighted samples versus55-digit mpmath Coulomb/Bessel functions, with max weighted absolute difference3.901e-17; new Yukawa versus original s-angle integrals; original finite-kappa coefficients; zero-energy endpoint; ODE residuals; positive sums and domain negatives.14 further elementary sufficient conditions and a portable retained-result assembly close the stated bound premises. Counts overlap and do not represent independent scientific reviews.

Actual Wolfram15.0.1 returned23 scalar zeros in15groups. Actual xAct/xTensor1.3.0 finally returned4 zero Euclidean projector/norm/Gram residuals, xTensor.m SHA25604e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36. Two earlier calls left Scalar trace wrappers unresolved; a package-qualified after-load canonicalization corrected the representation. Original failed inputs/residuals and pre-analysis warnings remain. No physical equation or tolerance changed.

The first foreground20-profile timed out; no result was adopted. Per-k checkpoints and a separate local process within this invocation completed the same settings. Final results and RESULT logs were retained. No absent OS returncode receipt is invented. Main runtime uses longdouble with64mantissa bits plus binary64 SciPy, not directed arbitrary-precision arithmetic.

## Cross-repo intake and next action

NEW CR55 actual4abd195f1a3124e59b0fa498b446b590ef0116e5 proof preserves source-specific finite errors when the active process changes. NEW HE44 f5ed7c1e70e87a174b1fef25b9bd7c5bc5979c10 formalizes cross-section-free electron columns and passive sigma/bin consumption. These clarify that a changed Coulomb ionization rate is active chemistry, not passive opacity rescaling. No foreign center/error coefficient or PHYS27 observable is multiplied by the new ratio. REI115 head7782c0fd819400ae9e06a97e283d72779ddfc40c retains prior science4716c469535422ba6c293a26e3478cedd3923e6b, D/A and pre-bin memory.

SciSpace/Exa were used for Coulomb numerical-method discovery; DLMF33.2,13.4,10.60 primary formulas were read. No new same-neutral-channel empirical calibration was found/adopted. No source/chemistry ODE, native receiver, HPC, old PW campaign, production activation or main merge. HH_STRICT_NATIVE, HH_SINGLET ion-pair and globalRUX retain scope.

Next PHYS30_COULOMB_FINITE_QUADRATURE_CERTIFICATE: bound only the remaining finite integrals/all-roundoff in this fixed model, reuse the omission proofs, and handle the x0 flat normalization explicitly. Set the numerical certificate width before that run. Full reproduction material is in the immutable archive indexed by EVIDENCE_INDEX.json.
