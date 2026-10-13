# PHYS27: restored near-rate exposure and a direct paired-sign theorem

2026-10-14. Selected node: PHYS27_RESTORED_NEAR_RATE_EXPOSURE_TRANSFER; R5 plus local checks. Parent PR59 head200bcc3e8c815d3426b850c6adc1f9b583d84049. Derived/exact-rational/implementation checked, with inherited source-certificate premises. External independent review was not performed.

## Source-bound results

The actual PHYS25 archive and its PHYS22/local23 inputs were recovered. Keep the exact-real warm P01 gas4/photon2904, common IC/HM12 source/prescribed Bianchi-I geometry, zero tilt, proper h=1e11s and original thermal event ledger. The restored and original S65 rates are defined only on CM I0..2I0 and set to zero outside ONLY as near-window diagnostics. Physical high-energy coverage remains open.

At h, outward bounds are:

| Difference | electrons/H | temperature K | finite Thomson depth |
|---|---|---|---|
| restored ON minus OFF |[2.6100713,2.8414488]e-14|[-2.0026464,-1.9133912]e-9|[1.5448581,1.6818179]e-21|
| restored ON minus original near-only ON |[-1.5720238,-1.3337845]e-14|[0.97777085,1.1079587]e-9|[-9.3046114,-7.8944507]e-22|

The second row is a new direct paired bound, not a subtraction of separately rounded ON-OFF estimates. Restoring the vertex reduces electron production and cooling within this declared model. It does not heat the gas above OFF. No ODE, atomic quadrature or native receiver was rerun.

## Finite signed-source proof

Use g=(x,y,z,w), f=3/38, ell=(1,f,2f,0), e=ell.g, Pi=1+f+e, T=C_T*w/Pi, C_T=2eV_J/(3k_B), and nu=(1,0,0,-chiH). The source threshold I0=13.605693122990eV differs from chiH=13.598434599702eV. Keep sigma_event=2sigma_tag and k=<sigma_tag*v>; the identical-pair factor is consumed once. Signature(-,+,+,+), c,hbar,k_B retained.

The unchanged equations are g'=F0(g,m,t)+nu*q, m'=s(t)-K(g,t)m, K diagonal nonnegative, q=nH(t)*(1-x)^2*k(T). F0 is HH OFF but includes all original gas/photo/geometry terms. For two histories with common initial state, source and geometry, diagonal photon absorption and the original derivative majorants imply

    |delta m(t)| <= integral_0^t Cplus*|delta g(s)|ds,
    D(t) <= |nu|Q(t)+P_t D(t),
    P_t=t*Aplus+t^2*Bplus*Cplus/2 <= P_h=P,

where D is the componentwise running supremum and Q=integral |q_j-q_i|. The actual chemistry need not be cooperative. If the source difference has a fixed sign epsilon, positivity of the comparison inverse gives

    W=(I-P)^(-1)|nu|, V=P*W,
    D(t)<=W Q(t),
    |delta g(t)-epsilon*nu*Q(t)|<=V Q(t).

The last inequality follows by subtracting the exact signed forcing before bounding feedback. The saved scale diag(1,1,1,32) gives norm0.0368847153857105285<1. Current exact checks verify P from saved Aplus/BplusCplus, W-V=|nu| and PW=V; old campaigns are not replayed.

First-exit is closed safely by ADDING h|nu|q_new_upper to the old tube Picard bound, without subtracting any guessed old contribution. New maximum radius ratio0.622721138337326419; joint original/restored ratio0.622721140343522599. Both histories stay in the inherited common tube.

Let a-=1-x_initial-radius_x, a+=1-x_initial+radius_x and n-<=nH(t)<=n+. The prescribed density is common, not constant. For the restored rate,

    q_R in[n-*a-^2*kR-, n+*a+^2*kR+]
        subset[2.7026692,2.7473210]e-25/s.

Retain density as a shared factor in the paired source. On the WHOLE two-state tube,

    d-=n-*(a-^2*kO- - a+^2*kR+) >0,
    d+=n+*(a+^2*kO+ - a-^2*kR-),
    d-<=q_O(gO,t)-q_R(gR,t)<=d+,
    [d-,d+] subset[1.3811034,1.5199479]e-25/s.

Thus restored-minus-original uses epsilon=-1 and Z=integral(qO-qR)>0. Same-state microscopic rate order alone would not establish this: the explicit cross-state source gap is essential.

For electron response, eps_e=ell.V=0.0342616546039232289; ae=1-eps_e, be=1+eps_e. The positive forcing has deltae in[ae Q,be Q], negative forcing in[-be Z,-ae Z]. Temperature uses the EXACT finite quotient

    Tj-Ti=(C_T*deltaw-Ti*deltae)/Pi_j.

With the inherited T/Pi tube, define

    G-=(C_T*chiH+T- -C_T*Vw-T+*eps_e)/Pi+,
    G+=(C_T*chiH+T+ +C_T*Vw+T+*eps_e)/Pi-.

These are70796.3523467931244 and72894.5184086573505K. Positive forcing gives deltaT in[-G+Q,-G-Q]; negative forcing gives[G-Z,G+Z]. Combining Q,Z with their all-time rate bounds yields the table. Each direct paired interval is nested in the independent ON-OFF interval subtraction. Nonlinear observable fractional reduction is not assumed equal to microscopic rate reduction.

## Optical age/current binding

Latest HE42 R7 is actively used: for dx=c*k*ds and alpha=c*grad(theta), u.alpha=1, D=-u.k, A=alpha.k. Proper ticking alone does not imply A=D. The current formula is

    J_e=c*nH*e*u,
    d tau=-(sigmaT/c)J_e.dx,
    tau=c*sigmaT*integral (D/A)*nH(theta)*e(theta)dtheta.

The actual pinned BASS P01 contract d520c5e47ebf5cf218351082430ae3ef5e1ab3ec, research/warm_p01_bass_history_20261011/CONTRACT.json, specifies zero tilt and proper-age=normal seconds. Hence D/A=1 HERE. For an observer at h,

    delta_tau_R(t) in c*sigmaT*[n-*ae*qR-, n+*be*qR+]*(h^2-t^2)/2.

At t=h the depth difference is exactly zero. The factor1/2 retains electron birth time; endpoint deltae(h)*h is not the integral. The paired deficit uses d and the opposite sign. This is a continuous exact-real IVP bound, not a fresh native sampled BASS history.

Preserve two source constants: PHYS25 diagnostic sigmaT=6.6524587051e-25cm2, BASS sigmaT=6.6524587e-29m2. Their ratio is66524587000/66524587051. The displayed8-digit depth intervals coincide, but exact diagnostic and BASS-convention fractions remain separate.

## Evidence and scope

Actual Wolfram15.0.1:11 scalar zero residuals and positive paired gap. Actual xAct1.3.0:5 spacetime current/clock/product-rule tensor zeros; xTensor.m SHA25604e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36. Scripts saved before submission; observed outputs are selected normalized transcriptions, not raw transport bytes. Compact outward CAS leaves agree with separate exact arithmetic and enclose the full source-bound outputs.

Python transfer33checks; separate validation49checks, including14input identities,39outward intervals, endpoint source-gap extrema and synthetic negative controls. Counts overlap, not independent scientific reviews. Synthetic wrong endpoint-time integration, duplicated pair factor and D-only clock were rejected; no upstream bug is asserted. Sandbox raw-GitHub DNS failure and Wolfram pre-analysis warnings are preserved. Native subagents were not exposed.

Latest CR53 moving-source work and HE42 age/current were read at exact commits; no CR/HE numerical coefficient was imported. REI114 remains a5c958c414dea41216b445c05f58df837f05cacb with HH/CR/RCT OFF. Same geometry/source/clock, separate binding/thermal thresholds and single event ownership are retained. Physical exchange/continuum, E>2I0 tail, observational omission budget and global RUX remain open. No source or production mutation, main merge, ODE or HPC launch.

Next: PHYS28_CONTINUUM_ORTHOGONALITY_AND_CHANNEL_CALIBRATION. Compare actual S65 continuum orthogonality/prior-post amplitudes and form a same-neutral-channel Coulomb-continuum or exchange comparison. Retain the certified current model as a reference; do not default to another unchanged quadrature/ODE campaign. HH_SINGLET ion-pair and HH_STRICT_NATIVE keep their own scope.

Full Korean derivation, exact results, selected source members, code, CAS records, failures and handoff are in the immutable bundle identified by the adjacent EVIDENCE_INDEX.json. Primary literature was consulted at abstract/definition scope via SciSpace/Exa/web: Angeli-Sontag2003 math/0206133 and Younsi-Wu-Fuerst2012 arXiv1207.4234. The source-specific proof above is supplied directly, not attributed to an unread theorem.
