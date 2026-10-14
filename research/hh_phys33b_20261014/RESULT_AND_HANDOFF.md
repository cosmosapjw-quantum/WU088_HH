# PHYS33B: outgoing exterior and infinite high-channel control

2026-10-14. R5 continuation at actual PR66 parent db88ed7c4054094bcff62668bafc0fef927f559d. Full PHYS33 remains PARTIAL_LOW_SECTOR_CONTINUOUS_CONTROL. This entrypoint summarizes the new constructive proof; the complete Korean/English derivation and executable evidence are in the pinned archive.

## Exact model and quantitative result

Use h=H/Ea=-Delta/2-1/r-lambda*S(s), S=(1+1/s)exp(-2s), s=|r-R ez|; r=rphys/a0, k=a0p/hbar, epsilon=k^2/2, Ea=2I0. Retain I0=13.605693122990eV, receiverchiH=13.598434599702eV, c/hbar/kB, original transition source and incident normalization. Y=phi+lambda*xi satisfies(epsilon-h)Y=(epsilon+1/2)phi. Do not omit its exterior source.

For R=.7,a=4,k in[.5,1],lambda in[0,1], eliminate the FULL exterior first and then compress the INTERIOR to bare ell>=29, all m. The resulting continuous high-block inverse satisfies

    ||A_Q(epsilon)^-1||L2(B4)->L2(B4) <=17424/203243
      =.0857298898363043253642191859006... .

For physical H the inverse has an extra1/Ea. This is not a finite matrix norm, a full low/high inverse, an ordinary allspace L2 resolvent, or a k=0 theorem.

## Exterior proof

Reduced u=r*psi obeys L u=u''+DeltaOmega*u/r^2+(k^2+2/r+2lambda*S)u=f. For zero trace at a define

    E=integral(||u'-iku||^2+||gradOmega u||^2/r^2)dr,
    B(f)=||r*f||L2+(1/k)integral sqrt(r-a)||f(r)||Omega dr.

With Coulomb outgoing phase kr+log(2kr)/k, the multiplier M=r*u'-i*(kr+1/k)*u gives

    E+a||u'(a)||^2+2lambda integral<u,(S+r*S_r)u>
      =-2Re integral<M,f>.

The infinity boundary is zero only when the Coulomb1/k term is retained; without it the unit outgoing asymptotic leaves1. At d=a-R=33/10,

    nu=lambda*(a+1)/2*(2+2/d+1/d^2)*exp(-2d)<.01,
    sqrt(E)<=2B(f)/(1-nu), ||u'(a)||<=B(f)/sqrt(a*(1-nu)).

Existence is constructed from the exact Coulomb Dirichlet kernel. H_l=G_l+iF_l, D_l(r)=F_l(kr)G_l(ka)-G_l(kr)F_l(ka), and g_l=-D_l(r_<)H_l(r_>)/(kH_l(a)) has derivative jump1. Finite-angular compact sources extend by the uniform energy bound. Since S<=C exp[-2(r-a)], C<9/5000, the full-angular perturbation map has energy norm

    gamma<=4lambda*C*(sqrt(163/128)+1/(4k))
         <=1467/125000=.011736<1.

Thus the exterior outgoing Dirichlet solution exists by contraction with ALL angular modes, not by extrapolating a finite-band inverse.

For high boundary data, harmonic lift sum(a/r)^ell*g_lm*Y_lm gives

    Tred=-Lambda/a+Remainder,
    ||Remainder Q28||<=a*qstar/sqrt(1-nu)
       *(1/sqrt55+Beta(3/2,55/2)/k)
       <=461104/515625<.9,
    qstar=3759/2500.

All output angular modes are included. Physical Tphys=Tred-1/a therefore has -Re<g,Tphys*g>/2>=(33/10)||g||boundary^2.

## Interior with nonzero outgoing trace

For interior high u let N=||u||,K=||grad u||,t=||trace u||,X=||u/s||. Translated Hardy WITH its surface term gives X^2<=2KX+t^2/d, hence X<=2K+t/sqrt(d). Angular energy gives K^2>=870N^2/16 and ||u/r||<=K/sqrt870. Since S<=1/s, the exterior-eliminated form satisfies

    Re a>=K^2/2-(2lambda+1/sqrt870)NK-epsilon N^2
                +beta*t^2-lambda*N*t/sqrt(d), beta=33/10.

Completing the boundary square and using the inherited interior quadratic lower bound187/16 gives Re a>=(203243/17424)N^2. Also Re a>=K^2/5, so bounded-form Lax-Milgram establishes the inverse, not only injection. Retaining half the trace yields mu_t=202843/17424 and

    ||u||<=sqrt(||volume_f||^2/mu_t^2
                       +||boundary_defect||^2/(2beta*mu_t)).

The weak boundary forcing has factor1/2. In cusp coordinates the projector is J^-1 Q J with metric J^2, not standard angular Q on the transformed field.

## Actual reference/trace evidence

The attached PHYS33 archive c0f98131... (23915453bytes,F=exp(lambda exp(-s))) and published c67f817b... (33013608bytes,J=exp[(lambda/2)exp(-2s)]) are distinct. Both are preserved. This unit consumes the published actual L28 cubic and interior proof; it does not combine finite-space results as byte-identical evidence.

New axial m=0 exterior maps integrate T'=Q_lambda-T^2 and d'=f-T*d over24..4 with the correct affine Coulomb/source endpoint. L20,L32 and stronger same-L32 profiles completed. Final diagnostics atR=k=.7,lambda1:

    ||T-T_C||2=.0012090681763315266;
    ||d-d_C||2=3.2018174886876395e-5;
    pure-C interface mismatch2.3537532702100353e-4;
    screened-map/ACTUAL cubic derivative mismatch8.005840129366742e-8;
    source-omitted mismatch.18470860801111574.

Mismatch ratio2940.05 is not a full solution-error improvement. The actual polynomial derivative differs from the separately interpolated slope state by8.01394407296851e-8. Substituting that slope would report1.05495e-10 instead; we do NOT do that. A lambda0 control agrees with the exact Coulomb DtN to5.41e-13. A separate analytic bound at24 is||(T_lambda-T_C)P_ell<=32||<3.573e-18, all output modes, plus phi-source correction<5.686e-29. This is not automatically an r4 propagated-error bound.

Interface matching keeps(T_i-T_e)g=d_e-d_i. The induced source and readout remain in the low/high Schur problem. New high control does not certify the remaining low continuous radial inverse or the whole-reference coefficient/residual inclusion.

## Verification, failures and next

Actual Wolfram15.0.1:17/18 initial literal zeros; one unexpanded equivalent zero left allFalse and was closed by a targeted Expand. Actual xTensor1.3.0:4Euclidean virial/current/Hardy/norm zeros.58new conditions pass, including exact rational inequalities,7input hashes,4independent high-precision Coulomb derivatives, manufactured virial tests and source/derivative/low-Schur controls. Same author plus CAS; external independent review/native subagents NOT_RUN.

Optional independent exterior BVP did NOT complete:45s timeout, equivalent BLAS contraction hitting5000-node cap, then same-tolerance12000-node budget timeout. These are preserved, excluded from passing evidence, and not diagnosed as an upstream library bug. Completed primary numerical evidence is Riccati plus exact Coulomb control. No old rate/P01/native/HPC or parent science-suite replay; new exterior radial ODEs did run.

Read NEW HE49 full R4 and CR59 full partition results; reuse exact reference and eliminated-source distinctions, not their numerical constants. REI117 remains an execution overlay. DLMF33.2/33.11 supplies Coulomb conventions; Baskin-Spence-Wunsch1504.01037 is gluing method context, not these constants or a novelty claim.

Next SAME-node subunit PHYS33C_LOW_SECTOR_CONTINUOUS_DEFECT: continuous low Schur stability, full residual/boundary/evaluator inclusion and functional error. k<.5 threshold control remains separate. Full intensity, full low/high inverse and two-centre thermal rate remain null. Old alternatives/model certificates, HH_STRICT_NATIVE, HH_SINGLET, globalRUX and production HH/CR/RCT OFF are unchanged. No merge, forced patch, external-repo or permission change.
