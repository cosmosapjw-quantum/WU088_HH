# PHYS31: source-bound Coulomb response and time-resolved electron column

2026-10-14. R5 constructive derivation/local checks, actual successor of WU088_HH PR63 at13869fbd0ab6849613be694af3b0841c85a68b14. The complete PHYS30 rate certificate is consumed with the preserved PHYS27/22/local23 P01 source coefficients. No old atomic, ODE, native or HPC producer is rerun. Same-author exact arithmetic and actual CAS; external independent scientific review NOT_RUN.

## Source-bound result

For the same exact-real warm FT03/HM12 Case A P01 gas4/photon2904, prescribed LRS Bianchi-I geometry, zero tilt and h=1e11 proper seconds:

| Difference | electrons/H | temperature K | finite depth, BASS P01 sigma |
|---|---:|---:|---:|
| Coulomb minus OFF |[7.54235048,8.23036508]e-15|[-5.80074197,-5.52914674]e-10|[4.51698539,4.81765791]e-22|
| Coulomb minus restored PW |[-2.03369207,-1.84156883]e-14|[1.35001739,1.43334140]e-9|[-1.19042504,-1.10288424]e-21|
| Coulomb minus original S65 |[-3.55955284,-3.21845764]e-14|[2.35938711,2.50876448]e-9|[-2.08359018,-1.92747952]e-21|

These are outward displays. Exact fractions in results/TRANSFER.json are authoritative. Every atomic channel is the explicitly declared CM I0..2I0 near-window diagnostic; physical higher-energy ionization is not set to zero. C cools relative to OFF but less than the PW/S65 models. Paired results are derived directly from cross-state source gaps, not by passively rescaling old optical data.

## Definitions and inherited comparison

Keep g=(xHII,yHeII,zHeIII,w), e=ell.g with ell=(1,3/38,3/19,0), Pi=1+3/38+e and T=C_T*w/Pi, C_T=2eV_J/(3kB). w is eV/H and nu=(1,0,0,-chiH). chiH=13.598434599702eV differs from atomic I0=13.605693122990eV. sigma_event=2sigma_tag and identical-pair1/2 combine once to k_network=<sigma_tag*v>. c=299792458m/s, kB=1.380649e-23J/K, eV_J=1.602176634e-19; hbar and the original atomic normalization retained. Signature(-,+,+,+).

    g'=F0(g,m,t)+nu*q, q=nH(t)*(1-x)^2*k(T),
    m'=s(t)-K(g,t)m, K diagonal nonnegative.

The prescribed proper density is the SAME function for both solutions, not a constant. Shared photon forcing cancels only from the difference equation. The old absolute gas/photon majorants A,B,C are retained; no assumption that the actual nonlinear chemistry is cooperative is introduced. The new k derivative is not hidden in an old Jacobian: the full event-rate difference remains forcing.

For fixed forcing sign epsilon and Q(t)=integral_0^t |qj-qi|, the old comparison gives

    D(t)<=|nu|Q(t)+P(t)D(t),
    P(t)=t A+t^2 BC/2<=P(h),
    W=(I-P(h))^-1|nu|, V=P(h)W,
    D(t)<=W Q(t).

Subtract the exact signed forcing before bounding feedback. The NEW retained-time statement is

    |delta g(t)-epsilon*nu*Q(t)|<=P(t)W Q(t).

Use u=t/h for normalized time, distinct from the event vector nu. Put v1=h*A*W, v2=h^2*BC*W/2, e1=ell.v1, e2=ell.v2. Actual e1=.0342613989677312419..., e2=2.55636191986985925...e-7. Then for positive forcing bounded q-..q+,

    h q- u (1-e1*u-e2*u^2) <=delta e(t)
       <=h q+ u (1+e1*u+e2*u^2).

Negative forcing reverses the entire interval. P(h)W=V, W-V=|nu| and the original scaled norm.0368847153857105285<1 are checked from actual retained fractions. Every new rate's Tbox covers the complete original temperature tube.

## Whole-tube rate order and finite temperature

Set a-=1-x0-radius_x, a+=1-x0+radius_x and n-<=nH(t)<=n+. A safe first-exit test ADDS h|nu| n+ a+^2 k+ to the old tube Picard bound. Maximum radius ratios are C.622721135683525388, PW.622721138337326419, S65.622721140343522599, all<1. No old source term is guessed and subtracted.

C forcing is bounded by[n- a-^2 kC-,n+ a+^2 kC+], within[7.80993166,7.95772041]e-26/s. For high=PW orS65, retain the common density before bounding both states:

    d-=n-*(a-^2 khigh- -a+^2 kC+) >0,
    d+=n+*(a+^2 khigh+ -a-^2 kC-).

The PW-C gap lies in[1.90690246,1.96632261]e-25/s, S65-C in[3.33263937,3.44163667]e-25/s. Explicit monotonicity proves the continuous box bounds; all endpoint combinations independently reproduce them. Same-state microscopic rate ordering alone would not suffice.

Use the exact finite quotient Tj-Ti=(C_T*deltaw-Ti*deltae)/Pi_j, not a tangent. With ev=e1*u+e2*u^2 and vw=v1w*u+v2w*u^2,

    G-=(C_T chiH+T- -C_T vw-T+ ev)/Pi+,
    G+=(C_T chiH+T+ +C_T vw+T+ ev)/Pi-.

Positive forcing yields deltaT in[-G+q+hu,-G-q-hu]; negative forcing reverses the interval. The new electron contribution to heat capacity is included. The PHYS29 emitted-electron kinetic moment is not inserted as an extra heat source into the unchanged one-temperature ledger.

## Time-resolved, cross-section-free column

For dx=c*k ds and material age theta, alpha=c grad(theta), D=-u.k, Aage=alpha.k. The physical current is J_e=c*n_e*u+j_e, u.j_e=0. Its column satisfies

    dC/dtheta=(c D n_e-k.j_e)/Aage.

The actual pinned P01 contract has zero tilt, j_e=0 and Aage=D=1. In the SAME geometry, delta ne=nH*deltae and delta ne'+3H delta ne=nH*deltae'. Proper density is not divided by a_rel^3 again.

For arbitrary0<=a<=b<=1 with source births starting at0, define

    Fplus/minus=(b^2-a^2)/2
         +/-e1*(b^3-a^3)/3 +/-e2*(b^4-a^4)/4.

Then positive forcing gives

    deltaC_[ah,bh] in c*1e6*h^2*[n- q- Fminus,n+ q+ Fplus] [m^-2].

Negative forcing reverses the interval. The1e6 converts cm^-3 to m^-3 once. This is an all-time analytic response envelope, not a newly sampled trajectory. Pre-bin births are retained: the leading term is(b^2-a^2)/2, not(b-a)^2/2. Two half-bin interval endpoints add exactly to the full result; the remaining column at the observer h is zero.

Keeping P(t) reduces the feedback integral from(e1+e2)/2 to e1/3+e2/4=.0114205302316250773785.... The new interval is contained in the old constant-P(h) bound. Width reduction is26.1712833% forC-OFF,23.0224992% forC-PW,22.6802243% forC-S65; this is a bound-width improvement, not a physical or measured-error ratio.

Full differential columns are[6789948.79,7241920.81],[-17894512.3,-16578595.9],[-31320603.0,-28973942.0]m^-2. Apply sigma once afterward. Preserve diagnostic sigma6.6524587051e-29 and BASS P01 sigma6.6524587e-29m2 separately; exact ratio3913211000/3913211003. Table uses the latter.

For common foreground, relative survival changes obey Snew/Sref-1=exp(-deltaTau)-1. Rational elementary bounds evaluate this ratio without fabricating an absolute baseline. Absolute true-IVP baseline column and observer probability remain null. A missing foreground does not prevent a matched survival RATIO, but cannot be guessed for an absolute probability.

## Actual latest-source use and checks

NEW HE46 HE17 R1 at0542d23cf3ef93451c4effe99035779c13e18073 binds the actual same warm native P01. Its17-node linear proper-ne reconstruction gives an arithmetic column1.9240752418279585787...e21m^-2, not a true-IVP baseline certificate. Do not add our small differential bound to that approximate center and assert total absolute accuracy. No HE native source was changed.

NEW CR57 ef27d056b2f65e46fca3ba1bc8729015877b6f54 specifies a separate cold-source positive-overdrive/right-limit thermal closure. Reuse the need to bind closure and active source explicitly, not its event-time or donor bounds. NEW REI116 at2df18a7238b3e52d0eb844fd45aa706dbf883ab3 was read at overview/PR level; its HYREC/Puchwein/hydrogenic candidates do not replace the frozen P01 HM12 source. REI115 SAME SHEAR12 nodal/bin certification remains complete, not a warm numeric certificate. No cross-repo mutation or old optical rate-ratio rescaling.

Actual Wolfram15.0.1:12scalar literalzeros and finite column agreement. Actual xAct/xTensor1.3.0:6Lorentzian current/age/product-rule zeros, official xTensor.m SHA25604e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36. Submitted scripts precede evaluation; normalized selected observed outputs are not raw transport bytes. New transfer49checks and distinct validation83checks, including13input hashes and101outward interval records, passed. Counts overlap. Actual source-gap negative controls reject a same-state order whose cross-state gap changes sign. No external independent reviewer or native subagents.

Preserved intake TypeError: old and new manifest fields differ(files/entries). The schema mapping was repaired after inspecting both; original failed script retained. Wolfram formal H pre-analysis warning and shell TERM diagnostic remain. Source/model/tolerances unchanged. Primary-method discovery used SciSpace/Exa; Arcak-Maidens1709.06661 is comparison context, not the source of this specific certificate.

Next PHYS32_TWO_CENTRE_CONTINUUM_DEFECT: construct the same-channel final-state residual and minimal two-centre distorted-wave/resolvent correction with explicit orthogonality/prior-post/normalization conditions. Retain existing model-specific certificates. Full exchange/calibration, physical E>2I0 tail, observer omission budget, HH_STRICT_NATIVE/HH_SINGLET/globalRUX and production OFF remain separate. The successor was not executed here. Complete tested code, input leaves, proof, output fractions and failures are in the immutable archive named by EVIDENCE_INDEX.json.
