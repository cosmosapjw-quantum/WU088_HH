# PHYS64 R5: ordered Riccati coefficients and a conditional Catalan bound

Parent PR110: 653db0dfaa57f04d7c0a93017c60a5902bdb319e. Original atomic model, source NPZ SHA256 f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d unchanged. PHYS63 qualitative all-angular real-axis LAP remains inherited, not reopened.

## Backup intake first
Current Dropbox /WU088_HH and Google Drive /WU088_HH/latest PHYS63 contents were checked before science. Newest found source capsule: PHYS63_C5C8_20261018.zip, 58193 bytes, SHA256 4c3bbc0db6fdcae48b6297394b5cff2d1fd019dac1676cb583e208bb9da08604. Both provider copies independently downloaded and byte-equal. Latest delivery contains prior 24 tests, no newer NCP run. No newer execution was found in CHECKED paths; other folders were not exhaustively searched. Dropbox recursive listing is unsupported. Git latest PR110 agrees.

## 1. Exact hierarchy for a fixed finite angular projection and finite [27,T]
Keep original V=2(1+1/d)exp(-2d), d=|x-0.7 zhat|, in the full chosen m block, and set V=epsilon W with epsilon=3e-23 and ||W||<=1. Screen is zero outside T ONLY for this numerical boundary problem. Coulomb Z_C=diag(H_l'/H_l), H_l=G_l+iF_l, k=.7, E=49/200 Hartree. Increasing-r derivative is used.

For an auxiliary coupling lambda, Delta=Z_lambda-Z_C satisfies
 Delta'=-Z_C Delta-Delta Z_C-Delta^2-lambda W, Delta(T)=0.
Write Delta=sum_{n>=1}lambda^n Y_n. Then
 Y1'=-Z_C Y1-Y1 Z_C-W,
 Yn'=-Z_C Yn-Yn Z_C-sum_{j=1}^{n-1}Yj Y(n-j), n>=2,
 Yn(T)=0.
The n3 source is Y1 Y2+Y2 Y1, NOT 2Y1Y2. All intermediate channels in the projection remain present. Physical Dn=epsilon^n Yn must be stored separately, not obtained by subtracting total f64 responses. A computed D2 is a Taylor coefficient contribution, not automatically the full nonlinear remainder.

## 2. Derived sufficient remainder theorem
E(r,t)=diag(H_l(t)/H_l(r)), T[F](r)=int_r^T E(r,t)F(t)E(r,t)dt, with NO conjugation. If ||T||<=K and ||W||<=w, set A=Kw. Induction using the ordered Catalan convolution gives
 ||Yn||_sup <=Catalan(n-1) K^(n-1) A^n.
For q=4|lambda|KA<1 the series converges uniformly to the branch connected to zero and
 ||Delta-sum_(n=1)^N lambda^n Yn|| <= |lambda| A q^N/(1-q).
This is exact conditional mathematics. A sampled or f64 K is not a certified upper bound. q>=1 does not prove physical divergence. Spatial truncation and numerical roundoff errors are separate.

## 3. Fully proved continuum special case: ell subset {0,1}
For ell0 or1 on r>=27, q_l=k^2+2/r-l(l+1)/r^2>0 decreases to k^2. For unit outgoing amplitude, E_l=|H_l'|^2+q_l|H_l|^2 has E_l'=q_l'|H_l|^2, E_l(infinity)=2k^2. Since E_l'/E_l>=q_l'/q_l, integration gives E_l(r)<=2q_l(r). Hence |H_l|<=sqrt2, |H_l'|<=sqrt(2q_l); conserved current Im(conj(H_l)H_l')=k implies |H_l|>=k/sqrt(2q_l). Therefore |H_l(t)/H_l(r)|^2<=4(k^2+2/27)/k^2.
For T=39, K<=24368/441; w<=1 follows from the exact original screened exp160 bound. q<=3.6639019174109554e-19, and the continuum tail after D1+D2 is <2.225308513480369e-58<3e-58.
Scope: this is the TWO-CHANNEL PROJECTED original potential cut at T, not full physical P20-Q21, not all-angular, and not a certificate of the floating ODE/quadrature.

## Evidence and attribution
Actual exact Fraction tests12/12 PASS; zero-q baseline failed first, preserved in ZIP. Source-guarded producer exit0. Connected Wolfram confirms ordered second/third products, K, q, and tail bound. Full owner suite/NCP/native subagents NOT_RUN. No original production or sibling mutation, HH_R10 OFF.
Riccati perturbation expansions are established: G.W.Rogers, J.Math.Phys.26,567-575(1985), DOI10.1063/1.526592. Coulomb normalization/recurrence: https://dlmf.nist.gov/33.2 and https://dlmf.nist.gov/33.4. These do not independently certify our constants. The recurrence and low-block bound here are direct derivations, not claimed as a novel general theorem.

Next C5-C8: compute second/third coefficients without subtraction, independent quadrature and nonlinear control, bounded resumable NCP runner. High angular/radial error certification and actual source cross section remain open.
