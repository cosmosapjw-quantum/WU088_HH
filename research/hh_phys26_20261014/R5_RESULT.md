# PHYS26: finite-momentum direct vertex and near-rate enclosure

2026-10-14. Selected stage: R5 constructive derivation with local checks, not a completion of all R1–R10 stages. Parent PHYS25: `a4476944dad44ae3ec6c5d5a39cca87fa432fbed`. The actual root plan and its DAG were read; the root still points to PHYS19, while PHYS25 HANDOFF and RESEARCH_STATE explicitly select `PHYS26_FINITE_MOMENTUM_DIRECT_VERTEX` next. The root and all existing scientific payloads are preserved.

## Exact finite vertex

Retain the S65 tagged direct-product/plane-wave/sudden model, its singlet/triplet classical potentials, and CM eta=E/I0 in [1,2]. R=Rphys/a0, kappa=a0*p/hbar, mu=khat.Rhat. I0=13.605693122990 eV, a0=5.29177210544e-11 m. Receiver chiH=13.598434599702 eV and parent mH=1.67262192369e-27 kg remain separate. No natural-unit substitution. Signature(-,+,+,+); the local angular tensor metric is Euclidean.

With S(R)=(1+1/R)exp(-2R), a=S/(1+kappa^2)^2,

    A=a-C,
    C=(1/(8*pi))*integral exp(-|r|)*S(|r-R|)*exp(-i*kappa.r) d^3r.

Fourier convolution and Feynman parameters give the exact one-dimensional expression

    C(kappa,R,mu)=integral_0^1 G(y;kappa,R)*exp(-i*y*kappa*R*mu) dy,
    lambda_y^2=4-3*y+y*(1-y)*kappa^2,
    G=exp(-lambda_y*R)*[
      y*(1+lambda_y*R)/(4*lambda_y^3)
      +y*(1-y)*(3+3*lambda_y*R+lambda_y^2*R^2)/(2*lambda_y^5)].

For real 0<=kappa,y<=1, 1<=lambda_y<=2 and G>=0. The momentum denominators are D_A=q^2+4 and D_B=(q-kappa)^2+1; their contributions are 1/(D_A D_B^2)+4/(D_A^2 D_B^2). Completing the square yields the lambda above. Yukawa-resolvent differentiation gives the cubic and quartic inverse transforms. At kappa=0 this reproduces exactly

    C0=exp(-R)*(7/18-11/(27*R))+exp(-2*R)*(1/9+11/(27*R)).

It also gives C(kappa,0)=(kappa^2+15)/(2*(kappa^2+9)^2). In particular C0(0)=5/54. The original configuration integral proves |C|<=C0.

## Positive angular form and controlled truncations

Let b_l=integral G(y)*j_l(kappa*R*y)dy. Legendre orthogonality gives

    F=<|A|^2>_mu=(a-b_0)^2+sum_(l>=1) (2*l+1)*b_l^2.

Thus the interference is retained at amplitude level. For K=kappa*R and q_L=K^2/[(2L+3)(2L+5)]<1,

    0<=F-F_L<=C0^2*(2L+3)*K^(2L+2)/[(2L+3)!!]^2/(1-q_L).

For R<=20,kappa<=1,L=48 this is below3.773e-30. Positive angular quadrature, the sinc Gram form and this Legendre form agree in separate checks.

On the Bernstein y ellipse rho=2, Re(lambda^2)>=31/64>4/9, |lambda^2|<=553/64<9. With R<=20 the combined exponential has modulus<=1 and the complex integrand is bounded by20000. Chebyshev approximation plus exactness of n-point Gauss gives |C-Q_n C|<=160000*2^(-2n), below4.702e-34 at n=64. This bounds the exact quadrature rule, not node/function roundoff. The angular n=40 exact-rule bound is below9.121e-40. Five exact-rational sufficient-condition checks are preserved.

For R>=M=20, J_s<=2 and S+C0<=D_M exp(-R), D_M=7/18+exp(-M)*(10/9+38/(27M)). The integrated radial remainder is at most2*D_M^2*(M/2+1/4)*exp(-2M). The resulting uniform cross-section tail is below4.812e-16 a0^2 and the specified-T-box rate tail is below1.011e-26 cm3/s.

## Exact Maxwell-energy integration and actual values

Keep U3=3.6 exp(-1.48R), U1=.35*(z^2-2z), z=exp[-1.08(R-1.5)], V_s=U_s+R U_s'/2 and J_s=1-V_s/eta. The restored cross section is

    sigma_s/a0^2=256*integral_0^sqrt(eta-1) kappa^2/(1+kappa^2)^2
                     *integral_(r_s(eta))^infinity R*J_s*F dR dkappa.

The positive Maxwell integral can be reordered. Put theta=kB*T/eV_J, q=I0/theta, e0=max(1+kappa^2,U_s(R)). Its energy factor is exactly

    W_s=[(e0+1/q-V_s)*exp(-q*e0)-(2+1/q-V_s)*exp(-2*q)]/q.

Use expm1 and the positive incomplete-gamma form near e0=2; split R at r_s(1+kappa^2). The unchanged model's energy integration is eliminated rather than sampled again.

At50000K the restored unpolarized partial rate converges to7.63235883e-12 cm3/s, versus the archived source1.1694741862013453e-11. The numerical ratio is0.652631663. A uniform multiplication by the threshold ratio0.662920192699918 would overestimate this new value by1.57647%. Cross-section ratios at eta=1.01,1.1,1.2,1.5,2 are0.661491727,0.651179691,0.644488635,0.645946174,0.683749714. These are numerical convergence results, not narrow interval certificates or physical calibration.

A genuinely conservative enclosure over the inherited T box[49999.63846,50000.36154]K is

    3.51310e-12 <= k_near_restored <= 2.46532e-11 cm3/s.

Proof: write k=||a-C||^2 in the positive weighted spin/Maxwell/path L2 space. The C0-squared radial moments are an exact finite exponential/E1 basis. Ninety-six positive energy bins with50-digit interval arithmetic give ||C||^2<=B=2.37187490902311819644402840025e-12. Reuse the parent source enclosure K_A in[1.1658244e-11,1.1731356e-11]. Reverse/direct triangle inequalities give [(sqrt(K_A,lo)-sqrt(B))_+]^2<=k<=(sqrt(K_A,hi)+sqrt(B))^2. Exact rational endpoints and outward displays are preserved. The interval is wide and does not certify the sign of the numerical reduction. mpmath iv elementary implementation and the inherited source certificate are explicit premises; unsupported interval special functions are avoided by an alternating-series E1 enclosure.

## Checks, reuse and boundary

Actual Wolfram15.0.1 returned12 scalar literal-zero residuals. Actual xAct/xTensor1.3.0 returned4 zero angular moment/STF tensor residuals. Official archive SHA2567a6c5f600868a3922668b020a15c0692f76574ff2a559808c62d460cef1b07be, xTensor.m SHA25604e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36. The first combined cloud call returned502 and is not successful evidence; split calls succeeded. Pre-analysis undefined-symbol warnings are preserved.

Thirty-five local numeric checks,13 enclosure checks and5 exact-rational y-domain checks passed. A separate prolate-coordinate integration, with the Coulomb denominator canceled by its Jacobian, reproduces finite vertices. The same author wrote these checks; external independent scientific review was not performed. Complete remaining outer kappa/R quadrature and all-roundoff certification around the converged number remains open.

Read and used: bass_cr PR52 stopping-norm erratum, BASS_HE THEORY16 exact-projection/error separation, and rei_bianchi PR114 SCIENTIFIC_CONTRACT. Do not import the invalid2(Ep-Ed) separated-energy norm or old downstream CR/HE certificates. No foreign numerical coefficient was relabeled as an HH bound. The REI consumer remains HH OFF. Retain sigma_event=2*sigma_tag and k_network=<sigma_tag*v>; pair symmetry is consumed once. No new thermal/spectral/tau history was generated. SciSpace/Exa were actually used; electron-impact, H-He mutual-ionization and keV data were not adopted as same-channel near-threshold calibration.

Next: PHYS26_TIGHT_RATE_CERTIFICATE, unchanged model, existing analytic y/angular/tail bounds, remaining outer quadrature and roundoff only. No parent512-bin/source/P01 replay. Exchange, Coulomb-continuum and high-energy physical calibration remain separate. HH_STRICT_NATIVE, HH_SINGLET ion-pair, global RUX and production are unchanged. Heavy queue empty; launch=false.

## Durable evidence

Complete30-member bundle: WU088_HH_PHYS26_20261014_RESEARCH_BUNDLE.zip,53797bytes, SHA256718a99f7fc08a2cc5b03b1a78d2aa507c28d79a1d08da372172bf260bc5461de. Local CRC and29manifest payload identities were verified. Full Korean derivation, executable code, actual outputs, inherited-input extraction, failures and next DAG are included; no fonts or source-paper PDFs.

[Google Drive evidence](https://drive.google.com/file/d/12KEFgKtjgIbSJXU77dr444EQCd2GbJJm/view?usp=drivesdk).

Dropbox: /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/WU088_HH_PHYS26_20261014_RESEARCH_BUNDLE.zip, ID id:BSpOijBcT10AAAAAAD4viQ. Both providers acknowledged53797bytes at the existing destinations. This is upload/metadata verification, not a remote restore test. No merge is requested.
