# PHYS26 tight rate certificate

Date: 2026-10-14. Selected scope: R5 and stage-local checks. Parent WU088_HH PR58: `0fad7e43b5131440ee15863e4295341c42c78f80`. The actual per-unit NEXT_DAG selects PHYS26_TIGHT_RATE_CERTIFICATE; the older PHYS19 root pointer is preserved, not replayed.

## Result

For the unchanged restored S65 direct-product/sudden/plane-wave model, original singlet/triplet potentials, CM E/I0 in [1,2], and T in [49999.63846,50000.36154] K:

    7.6320925e-12 <= k_near_restored(T) <= 7.6326272e-12 cm3/s.

The exact-endpoint full width is 5.346110465403657e-16 cm3/s, below the predeclared 1e-14 target. This is an analytic-remainder plus outward-arithmetic enclosure, not an error inferred from grid differences. The inherited original-source interval [1.1658244e-11,1.1731356e-11] gives restored/original in [0.6505720,0.6546979], hence a certified same-model reduction of 34.5302 to34.9428 percent. Multiplying the original near-rate by the zero-momentum threshold ratio instead overestimates the restored rate by1.2559 to1.8981 percent.

Status: derived, interval checked and implementation checked in the stated finite model. External independent scientific review is not performed. No experimental atomic calibration, complete exchange/Coulomb-continuum correction, E>2I0 physical tail, or production promotion is asserted.

## Fixed definitions

R=Rphys/a0, kappa=a0*p/hbar, eta=E_CM/I0. I0=13.605693122990 eV; receiver chiH=13.598434599702 eV remains distinct. a0=5.29177210544e-11 m, kB=1.380649e-23 J/K, eV_J=1.602176634e-19, parent mH=1.67262192369e-27 kg and reduced mass mH/2 are unchanged exact-decimal leaves. Keep sigma_event=2sigma_tag, k_network=<sigma_tag*v>. Background signature(-,+,+,+); no natural-unit substitution.

Reuse the parent finite vertex Cminus=integral_0^1 G(y)exp(-i*y*kappa*R*mu)dy, with lambda^2=4-3y+y(1-y)kappa^2 and

    G=exp(-lambda*R)*[y(1+lambda*R)/(4lambda^3)
        +y(1-y)(3+3lambda*R+lambda^2R^2)/(2lambda^5)].

Let a=(1+1/R)exp(-2R)/(1+kappa^2)^2. The correct holomorphic continuation of the real intensity is

    F_complex=1/2 integral_-1^1 (a-Cplus)(a-Cminus)dmu,

where Cplus has the opposite phase. Complex conjugation/absolute-square is NOT continued as a holomorphic operation. On real arguments the two definitions agree.

## Outer quadrature theorem

Put U3=3.6exp(-1.48R), U1=.35(z^2-2z), z=exp[-1.08(R-1.5)], V=U+R*Uprime/2. At T0=50000 K, q=I0/(kB*T0/eV_J). Use the inherited exact energy primitive

    W=[(e0+1/q-V)exp(-q*e0)-(2+1/q-V)exp(-2q)]/q.

For each spin split R into [r(2),r(1+kappa^2)], [r(1+kappa^2),1], [1,2], [2,4], [4,7], [7,10]. Map each panel to R=A(kappa)+D(kappa)*t, t in[0,1]. In the first panel e0=U; elsewhere e0=1+kappa^2. This removes the max kink without changing physics. Turning functions use r3=(log3.6-log e)/1.48 and r1=1.5-log(1+sqrt(1+e/.35))/1.08.

Define h=D*kappa^2/(1+kappa^2)^2*R*W*F_complex. The rate prefactor is

    P=25600 sqrt[8eV_J/(pi*(mH/2))]*(kB*T0/eV_J)^(-3/2)
                         *(100a0)^2*I0^2 <3.28e-7 cm3/s.

Complexify only kappa or only t on the rho=2 Bernstein ellipse, enclosed by [-1/8,9/8]+i[-3/8,3/8]; the other variable stays real. For kappa=x+iu,R=v+iw, let X,U,Vmax,Wmax,K,Z bound |x|,|u|,v,|w|,|kappa|,|R| and vmin>0. Then

    alpha=sqrt(1-U^2/4), beta=X*U/(4alpha), L=sqrt(4+K^2/4),
    Re lambda>=alpha>0, |Im lambda|<=beta, |lambda|<=L,
    |1+kappa^2|>=1-U^2>0,
    |a|<=(1+1/vmin)exp(-2vmin)/(1-U^2)^2,
    |Cplus/minus|<=exp(-alpha*vmin+beta*Wmax+X*Wmax+U*Vmax)
       *[(1+LZ)/(8alpha^3)+(3+3LZ+L^2Z^2)/(12alpha^5)].

The last expression integrates the y weights exactly. F_complex is bounded by(|a|bound+|C|bound)^2. Directed 50-digit complex intervals for R,D,W certify positive ReR and the log/square-root domains. Round each final |h| majorant upward to a rational power of two. The pairs (M_kappa,M_t) for panels0..5 are:

    singlet: (16384,2),(1024,8),(16,2),(128,16),(512,4),(64,1/16)
    triplet: (256,1),(8192,2),(16,1),(128,8),(512,4),(64,1/16).

Chebyshev coefficients obey |c_m|<=2M*rho^(-m). Truncation at degree2n-1 and the norm-one positive integral/Gauss operators imply |I-Q_n|<=4M*rho^(1-2n)/(rho-1)=8M*2^(-2n). Telescope the product error as (Ik-Qk)It+Qk(It-Qt). With n_k=n_R=32 and the1:3 spin mean,

    E_outer/P <=182849/36893488147419103232,
    E_outer=1.6242522007390675e-21 cm3/s (upper-bound evaluation).

This derivation is independent of observed convergence. Complete rational complex-box bounds and proof are in the archived ANALYTIC_OUTER_BOUNDS.json and REPORT_KO.md.

## Node and arithmetic closure

For degrees20 and32, all52 roots have disjoint rational sign-changing brackets of width2e-50 inside(-1,1), checked by exact Fraction Legendre recurrence. The degree count proves one root per bracket and exhausts the roots; high-precision seeds are not certificates. At each bracket evaluate w=2(1-x^2)/(n^2*P_(n-1)(x)^2) by directed MPFR arithmetic. Check positive weights and sum2 inclusion.

Actual execution used GNU MPFR4.2.2 at128bits, g++14.2.0, directed elementary arithmetic and transcendental functions. Sin/cos use directed endpoint evaluation plus the global1-Lipschitz interval width. The default host MPFR library was linked; failed python-flint installation is not claimed as a dependency. A minimal ABI declaration is used only when official mpfr.h is absent; recorded library/binary/source identity is retained.

All12 spin/panel runs completed with32x32 external nodes,32y nodes and20mu nodes (evenness uses the positive10 with full weights). The exported quadrature interval has width9.35601359543764e-28 cm3/s. RNDD/RNDU binary64 hex endpoints are converted to exact fractions; decimal printouts are not the SSOT.

## Remaining terms and temperature enclosure

Reuse the parent y bound at n_y=32: eps_y=160000*2^-64. For R<=10,a<=5,C0<=.1, the angular n_mu=20 bound is eps_mu=2^40(20!)^4*1.01*10^40/[41((40)!)^3]. The intensity error is at most eps_mu+(51/5)eps_y+eps_y^2. On the physical region |V|<=6,W<=.4,kappa^2/(1+kappa^2)^2<=1/4,R<=10; the positive weighted sum gives coefficient<=10. Thus E_inner<=2.900e-19 cm3/s.

For R>=10 prove |V_s|<1 from decreasing exponential majorants. With D_M=7/18+exp(-M)(10/9+38/(27M)), S+C0<=D_Mexp(-R), and J<=2, integrate R exp(-2R). Multiplying by pi/8-1/4 and the positive eta Maxwell weight gives 0<=tail_R>10<=2.512e-18 cm3/s. This is a distance-quadrature tail, not an E>2I0 physical tail.

The exact quadrature is near7.6323585930827e-12. Add the two-sided outer/inner bounds and the one-sided positive radial tail: at50000K the outward enclosure is[7.6323583e-12,7.6323614e-12]. The positive Maxwell kernel has logarithmic T derivative(-3/2+E/(kBT))/T>0 throughout the stated domain. Its endpoint ratios are bounded at E=2I0 by0.99996518039423805868... and1.00003482023621036653.... Applying them yields the full T-box result above without temperature sampling.

## Evidence, reuse and next

Actual Wolfram15.0.1 returned13 scalar zeros in12 named groups; actual xAct/xTensor1.3.0 returned4 tensor zeros for the two-real-component amplitude error algebra, not a spacetime geometry. Forty-five C++ utility checks,52 exact root brackets,24 directed complex majorants,16 assembly conditions and26 final read-only verification groups are preserved; these counts overlap and are not independent scientific reviews. A separate60-digit point integral agrees with the MPFR probe. First interval-expression failures, DNS failure, compiler warning, pre-analysis warnings, and a final-checker omitted-ROOT-argument failure are retained. Only the latter checker call was repaired; scientific results were unchanged.

Fresh latest-PR discovery found CR52,HE41 andREI114 unchanged from the read dependencies. Preserve the2Ep stopping-norm correction and exact-observable/error separation. No foreign numerical coefficient is imported as an HH bound. REI remains HH OFF; no new receiver/ODE/history or HPC run occurred. The compiled research quadrature did run.

Next: PHYS27_RESTORED_NEAR_RATE_EXPOSURE_TRANSFER. Recover actual PHYS25 near-only P01 exposure/first-exit coefficients and apply the new rate bound in that same diagnostic, without default ODE replay. That next task was not run here. HH_STRICT_NATIVE, HH_SINGLET ion-pair, globalRUX, physical calibration and independent-review status remain unchanged. heavy_queue=[]; launch=false.

Primary methods: Johansson-Mezzarobba2018, arXiv1802.03948 (abstract/method discovery); Johansson2018, arXiv1802.07942 (abstract); official FLINT acb_calc documentation (analytic-quadrature context, no FLINT runtime used); official GNU MPFR4.2.2 rounding/interface documentation. Full Korean proof, code, exact evidence, failures and source lineage are in the immutable bundle identified by EVIDENCE_INDEX.json.
