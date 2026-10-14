# PHYS33E: full screened exterior and actual REI T1 source relation

2026-10-14. Selected R5 constructive derivation/local checks. Actual parent PR68 b8c6fef512cdc3b3b109749b9d4e76335a03aa1f; consumed archive SHA2562bd9fdd7ddaf7171bddda92b6a9c55664764d8cfdf8b6a550fe2b7ef2b43e6b5. Original operator/source/model-specific certificates remain. Global PHYS33 is partial: the exterior is now controlled, but interior low Schur and global amplitude remain open. No prior scattering BVP, rate, chemistry, REI science or HPC producer is replayed.

## Exact target and quantitative result

Keep h_lambda=-Delta/2-1/r-lambda*S_R, S_R=(1+1/s)exp(-2s), s=|r-R ez|, R=kappa=7/10,lambda in[0,1]. r=rphys/a0,kappa=a0*p/hbar,epsilon=kappa²/2,h=H/Ea,Ea=2I0. I0=13.605693122990eV differs from receiverchiH=13.598434599702eV; a0=5.29177210544e-11m. Original1s, transitionS(R)-S_R, old-overlap amplitude and tagged normalization are fixed. c,hbar,kB retained; background(-+++), atomic Euclidean.

The target is the ENTIRE exterior r>a, a=4 or8, Dirichlet inner trace and Coulomb outgoing condition at infinity. Actual nonradial S_R is retained to infinity; ALL ell,m and repeated low/high return are included. R_lambda is the radiation-selected real-axis Green operator, w=sqrt(S_R), P_lambda the Poisson map and T_lambda the physical +r inner-normal derivative.

At a4:

    ||w R_C w|| <=297/17500 <.017,
    ||w P_C||² <=9801/980000,
    ||r^-1 R_lambda r^-1|| <=532710/17203 <31,
    ||T_lambda-T_C|| <=9801/481684 <.020347365.

At a8:

    ||w R_C w|| <=183/17500000,
    ||w P_C||² <=11163/1960000000,
    ||r^-1 R_lambda r^-1|| <=539994978/17499817 <31,
    ||T_lambda-T_C|| <=11163/979989752 <1.139094e-5.

The a8 higher-than-first-Born DtN remainder is below1.191167e-10. Differences of DtN maps extend on L2(Sa); individual DtN maps are not asserted L2 bounded. All values use the stated dimensionless norms; physical Green/DtN carry1/Ea and1/a0. No unweighted positive-energy whole-space inverse or kappa->0 uniform estimate is asserted.

## Direct multiplier proof, including the nonzero Coulomb boundary term

Start with finite angular sums and smooth compact radial source. Put u=r psi, A=-Delta_S²>=0 in H=L2(S²). This is unitary for physical volume L2. For(h_C-epsilon)psi=f,

    u''+(k²+2/r-A/r²)u=F, F=-2r f, u(a)=0.

Let v=exp(-ikr)u, Fv=exp(-ikr)F. Then v''+2ikv'+(2/r-A/r²)v=Fv. Plane phase removal leaves the Coulomb log phase. DLMF33.11 at fixedell gives u~exp(i[kr+log(2kr)/k])C, v'~i v/(kr).

Define

    B=r||v'||²+2||v||²-<v,Av>/r.

Exact differentiation gives

    B'=||v'||²+<v,Av>/r²+2Re<rFv,v'>.

Crucially B(infinity)=2||C||², NOT0. At the Dirichlet sphere B(a)=a||u'(a)||². The exact current identity is k||C||²=Im integral F conjugate(u). Therefore with X=||v'||, Y²=integral<v,Av>/r², T=||u'(a)||,

    X²+Y²+aT²=2||C||²-2Re integral rFv conjugate(v').

Hardy from v(a)=0 gives Z=||v/r||<=2X; the local fundamental theorem gives ||v(r)||²<=(r-a)X². Let N=||r f||_physicalvolume and B0=2+4/k. Since ||rF||=2N, flux and Hardy yield ||C||²<=4NX/k, and

    X²+Y²+aT²<=2B0 N X.

Hence X<=2B0 N, Z<=4B0 N, and square completion gives T<=B0 N/sqrt(a). Thus ||r^-1 R_C^± r^-1||<=4B0=8+16/k.

Existence starts from the exact radial Coulomb Green functions, whose real-axis outgoing denominator cannot vanish by the F,G Wronskian. Homogeneous estimates imply uniqueness. Finite-angular compact-source density and the uniform energy/trace/radiation-amplitude estimates extend this radiation-selected Green operator to r f inL2. Fixedell asymptotics are not applied uniformly before this extension. This is the real-axis outgoing realization used here, not an unproved arbitrary distributional or complex-z norm assertion.

## Exponential localization gives all-order contraction

For a>=1 and S_R<=V exp[-2(r-a)], put

    A0=integral(r-a)Vexp[-2(r-a)]dr=V/4,
    M0=sup r²Vexp[-2(r-a)]=a²V.

The actual angular multiplier need not commute with A. For f=w g and G=||g||, local Hardy gives ||wu||<=sqrt(A0)X and flux bounds give

    X²+Y²+aT²<=4D GX,
    D=sqrt(A0)/k+sqrt(M0)=sqrt(V)(a+1/(2k)).

Then X<=4DG and T<=2DG/sqrt(a). For Dirichlet psi=0, the physical surface norm of partial_r psi equals the H norm of u'(a). The adjoint Green boundary formula includes the kinetic1/2, giving

    q=4sqrt(A0)D=V(2a+1/k) >=||wR_C^±w||,
    p²=D²/a=V(a+1/(2k))²/a >=||wP_C^±||².

Poisson starts on smooth/H1/2 traces and extends as a bounded weighted volume map toL2(Sa). Combining polynomial-source and localized Hardy gives both cross norms ||wR_C r^-1|| and ||r^-1R_C w|| <=B0sqrt(V), using the incoming adjoint.

For h_lambda=h_C-lambda*w² with q<1,

    wR_lambda w=(I-lambda*wR_Cw)^-1 wR_Cw,
    wP_lambda=(I-lambda*wR_Cw)^-1 wP_C,
    ||r^-1R_lambda r^-1||<=4B0+B0² V/(1-q).

This includes the actual far r>8 potential, all angular mixing and repeated scattering, not just a first Born term. V4=9/5000 and V8=3/5000000 follow from s>=r-R and monotonic S. Their sufficient exponential inequalities were checked with90digit elementary outward arithmetic; Fraction assembly is exact.

## DtN, source and actual Born probes

For outgoing P_lambda b and incoming-adjoint P_C^-c, Green's identity with +r inner normal gives

    <c,(T_lambda-T_C)b>=2lambda< wP_C^-c,wP_lambda b>.

Therefore delta=2p²/(1-q) bounds the full DtN difference. The exact first Born T1=2lambda(P_C^-)^*S_RP_C has norm<=2p², and the remaining terms have norm<=2p²q/(1-q). These are exact-integral operator bounds; numerical first-Born quadrature needs its own error estimate.

For bulk f=w g, the zero-trace particular solution has normal data <=2p||g||/(1-q). The original xi equation is(h_lambda-epsilon)xi=+S_R phi, so g=wphi, phi=exp(-r)/sqrt(pi), and

    ||wphi||²<=Vexp(-2a)(a²+a/2+1/8).

This is distinct from the lifted Y's isotropic source. The outward particular-source values are in EXTERIOR_CERTIFICATE.json.

A NEW35digit reference-Coulomb quadrature evaluated first-Born diagonalell0and29 onS8. At16nodes per each of5radial panels8..32 and96angular nodes, ell0 gives approximately9.651700644326e-8+i8.315028644634e-8; ell29 gives4.310081383386e-8+i8.7262e-41. The10/16rule comparison is numerical checking, not a certificate. The formula contains [H_l^+(r)/H_l^+(8)]², not its absolute square, and no extra r². Local Hardy applied to the r>32 indicator weight bounds that exact first-Born tail by2.927e-25. Finite quadrature and roundoff remain separate. No scattering BVP/rate was run.

## True exterior joined to the physical interior high space

Use the actual parent's B4 physicalQ=ell>=29 form with pure-Coulomb boundary. For Bpartial=4sum(l+1)|b_lm|², ||b||²_S4<=2Bpartial/15. The NEW full exterior has

    eta_boundary=(2/15)delta4=3267/1204210 <.19.

The parent's quadratic remains increasing on its angular-energy domain; exact sufficient inequalities are checked. New mass coercivity is

    345/32-(435/16)eta=5157627/481684 >10,

and gradient coefficient19/100-eta/2 is positive. Thus the continuous B4 HIGH realization joined to the TRUE full screened exterior has inverse<=1/10. Exterior low return is included; INTERIOR ell<=28 is not yet solved.

For remaining interiorP/Q blocks, keep

    (A_PP-A_PQ R_Q A_QP)p=fP-A_PQ R_Q fQ,
    q=R_Q(fQ-A_QP p), output=J_Pp+J_Qq.

The full exterior DtN and particular source enter A and f. The exact remaining obligations are the interior-low Schur inverse, preserved-reference bulk/interface residual and physical amplitude functional. Global intensity/two-centre thermal rate remain null. The k=.7 theorem is not a threshold-uniform thermal-window certificate; explicit constants diverge as k approaches0.

## Actual live REI supplier: consume the existing T1 preparation

At11:20:57UTC actual live HEAD was b07274e2880df22af33f7988cad5202232269fa0. AX07 fullZERO was owner-scoped complete; AX08 signed family ran; AX11 T1 and AX12variants were reviewed/prepared but not started. The owner had already repaired epoch tuple/list persistence and prepared a4096MiB T1 binary. Those tasks were not repeated or claimed as HH work.

The old final hardened source guard's previously unobserved remote recheck was actually completed now: exact consumer b49fbed5f31a45e866915846357d1ddfdef8708ff7ba97ed17695ec8a5c3dc60, helper741dd27921a8bc29f206c1394a5d6f981e46281914c064cd5b4c99319c36e4ad, all10temporary-copy integration conditions passed. Raw result SHA256ffbfdbc7caf6c1312b43a89061e53ea2a5d1cd426fd7c56024bdea84828aa4c9. This is a fresh completion, not retroactive success for the old timeout.

The ACTUAL baseline compiled source200497bytes hashes tod7676b9309ac9b084499bbf599e803baecd661c80765489be45839ef5a7cf185. Planned T1 source200590bytes hashes to4de69c1e68ebd395fe2d0b5580d901b9a82bde86cadbd11bdd07e5ad2042b4a1. Comparing entire bytes shows exactly3edits: add4096->3968MiBscience, add4096->128MiBreserve, and add4096to the admitted budget list. All other compiled-source bytes are equal.

Owner AX11_OUTPUT_ALLOCATION_REVIEW hash03a291a56b9f3b7b22c63f7a7e75ef69ef58e990e6fe4d2e0541c5b2275f3399 was actually read and accepts that resource-only scope. The separate config deliberately changes local_target1e-5to2.5e-6 and resource limits; no other physical keys change. This proves a scoped same-mathematical-source/step relation, NOT equal trajectories or identical stop behavior.

New actual source-pair map/guard checks passed13conditions, including rejection of unexplained code and unbound source relation. T1_SOURCE_RELATION.json is ready to put into the future completed REFINE manifest. The actual HH-owned host record is /home/cosmosapjw/hh_phys33e_T1_source_relation.json, SHA25680a72a938b53c37b55d91e27c3b42694127727456797011f6b54e45caa143b35. Convenience mapper functions have6local unit tests; the actual live proof used a separately submitted equivalent inline probe, not a full run of that convenience CLI.

Final live STATE read at11:46:22UTC, HEAD1cff09ef35196443d3a25d484c928b1512ae22c2, still had AX07complete/AX08inprogress/AX11-12prepared-not-run and next_ready_ids=[]. Actual consumer guard remains unapplied. Source relation supply is READY; owner adoption and wholeAX11 readiness are NOT asserted. Signed-family completion, sole controller queue/shared slots, new T1 staging/hash parity and resource allocation remain. No owner STATE/source mutation or science launch. Existing HE51 update16a990556ea72f87246b3bb0ae5a14fbbb650497 confirmed the same prepared T1; CR61 was unchanged. No foreign numerical gains imported. Optional HH stays nonblocking and gas temperature is not replaced by stellar50000K.

## Verification and immutable evidence

Actual Wolfram15.0.1:15scalar literalzero groups and6True conditions. Actual xAct/xTensor1.3.0:4Euclidean tensorzeros, official archive and source hashes matched. New exact/iv generator12conditions, complementary SymPy/mpmath continuum56conditions including9manufactured examples, coefficient6unit and source-map6unit methods passed. Manufactured Coulomb-log outgoing examples retain B(infinity)=2 and reject its omission. Same-author arithmetic/CAS, external independent scientific review/native subagents NOT_RUN.

Preserved expected RED: missing new exterior module before implementation; subsequent6testsGREEN. Formal-symbol CAS pre-analysis warning remains. No scientific source/tolerance was relaxed. Endpoint arithmetic is exact Fractions plus supported mpmath.iv90digit exp/sqrt/basic bounds, not a formal verification of the library. Primary sources used via SciSpace/Exa/web: DLMF33.11 fixed-l asymptotics; Barcelo-Fanelli-Ruiz-Vilela1105.2953 and Castella-Jecko-Knauf math/0702009 at abstract/method context. Current explicit constants are derived above, not imported from those papers.

[Complete Korean proof, code, inputs, exact results, source relation, CAS and failures](https://drive.google.com/file/d/1trz-tv5WWvSsmGapFlC9G2tbvx-OCmSf/view). ZIP330672bytes,74members/73manifest payloads, SHA25627946284a740a549b74015bdbc5678504989378ac83e523a23ba87c58c15580e. Both Drive and Dropbox completed matching size; Dropbox id:BSpOijBcT10AAAAAAD6Xxg. Local CRC/allpayloads, relocated read-only verifier, altered-copy rejection/restored pass were observed. No new remote full restore. Full tested source is in the archive, not claimed expanded into native production.

Next INTERIOR_LOW_SCHUR_AND_GLOBAL_AMPLITUDE_BOUND. Reuse the completed full exterior and consume existing REI T1 relation where owner-admitted. No main/owner merge, external-repo mutation, production switch or global rate promotion.
