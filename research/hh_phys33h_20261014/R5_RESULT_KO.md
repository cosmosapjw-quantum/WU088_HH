# PHYS33H: continuous low-Schur Fredholm structure and actual PDE-defect separation

2026-10-14. Selected **R5 constructive derivation/local checks**. Authoritative parent PR71 head `e45af695aeea4803840cef6aba0eade14e0de1b3`. Actual immutable parent PHYS33G ZIP SHA256 `d65f481b901c7ea2913d860742d66e6562244f162c1a537d89aea372c299078e`. The fixed frozen-direct Hamiltonian and exact phase/transition remain; global PHYS33 is **PARTIAL**.

## Exact physics and mathematical result

With Bohr-radius lengths, Hamiltonian in `Ea=2I0` units and `I0=13.605693122990 eV` distinct from receiver `chiH=13.598434599702eV`, let `h_lambda=-Delta/2-1/r-lambda*S(|r-R ez|)`, `S(s)=(1+1/s)exp(-2s)`, R=kappa=.7, epsilon=.245 and lambda in[0,1]. Physical c/hbar/kB preserved, signature(-+++), atomic Euclidean. Source lift `eta=phi+lambda xi=F y`, F=exp(lambda exp(-s)), original 1s and `S(R)-S_R` unchanged.

Attach the **actual full-screened exterior** DtN at r=4. For `V=H1(B4)` the complex outgoing weak form is `a_lambda(u,v)=1/2<grad u,grad v>-<(1/r+lambda S_R+epsilon)u,v>-1/2<T_lambda gamma u,gamma v>`. The exact translated potential has
`
 ||S_R||_(L2(R3))²=4pi integral_0^infty (1+s)^2 exp(-4s)ds=13pi/8.
`
Since `H1(B4)->L4(B4)` is compact and `S_R in L2`, the interior potential quadratic form is a compact `H1->H-1` perturbation. Parent PHYS33E bounds `T_lambda-T_C` as an L2(S4)-bounded map; compact `H1->L2(S4)` trace makes this boundary term compact too. Coulomb reference outgoing B4 operator is invertible by regular/outgoing radial Wronskians in each fixed low ell and the inherited uniform high-ell coercivity. Thus the **full exact screened interior operator is Fredholm index0**. Parent PHYS33F supplies Q21 inverse, so exact low Schur `S_P=A_PP-A_PQ A_QQ^-1 A_QP`, P=ell<=20, is also **Fredholm index0** by triangular operator factorization. This does *not* yield a quantitative low inverse, rule out a kernel by itself, or certify a scattering amplitude.

## New complete screened exterior bound for the ACTUAL frozen trial at r20

Apply the inherited PHYS33E full-radial/all-ell/m theorem at a=20, R=kappa=.7:
`
 V=(1+1/19.3)*exp(-38.6),
 q=V*(40+1/kappa),
 p²=V*(20+1/(2kappa))²/20,
 delta=2p²/(1-q).
`
Real analytic values are V=1.81205646898766e-17, q=7.50709108580602e-16, `delta=7.77520148172767e-16`, and exterior screened particular-normal bound 7.00688792669517e-24. A 180-term Taylor positive rational lower estimate for exp(x) bounds exp(-x) from above with exact Fractions. Twelve rational sufficient conditions passed. The exact **dyadic squared norm** of the archived trial reduced coefficient vector at r20 is below (521/1000)²; with F<=e<3 and 40exp(-20)<1e-7, the screening-induced boundary mismatch of that particular trial obeys

`|| (T_lambda-T_C) gamma xihat || + ||g_lambda-g_C|| <1.23e-15`.

Crucial scope: this excludes the additional **high-angular mismatch of the approximate truncated Coulomb BC itself**. It is NOT an error bound on the continuum state or full boundary defect.

## Actual off-grid PDE residual diagnostic: non-negligible interior defect

Reconstruct the immutable degree10/ell<=20 Lobatto radial polynomials on the six inherited panels. At independently chosen Gauss radial points use exact polynomial derivatives, the original finite-angle coefficient formula with angular180 points, and project the strong **transformed** equation to ell<=36. Reconstruct residual L(y)=y''-2By'-My-(1+kappa²)t, keeping the high output source/couplings. Three levels give:

`
 n_rad=20: low(ell<=20)=.00125648155, high(21..36)=.00109264081, combined=.00166511556;
 n_rad=36: low=.00125648736, high=.00109274566, combined=.00166518875;
 n_rad=64: low=.00125648300, high=.00109274566, combined=.00166518546.
`
Maximum panel-interface reduced derivative jump about 5.4943e-13. Low residual is dominated by r10..20 and r.7..2, high residual by off-centre r.1..2. **These are sampled Gauss integrals, not rigorous whole-cell L2 upper bounds or physical h-action residuals**; ell>36 and radial origin/outer high boundary remain open. They concretely show why the frozen1386x1386 binary64 inverse defect <3.185e-8 cannot stand in for the continuum PDE error.

For the unscreened shifted Coulomb singular source only, a separate exact benchmark yields `||Q_(ell>L)[phi/|r-R ez|]||_L2² <=2R(1/(2L+1)+1/(2L+3))`, at L20 R=.7 exactly `588/8815`. This is NOT the screened/cusp-transformed partial-wave error bound.

## Physical dual and exact remaining gate

For bulk residual `r=f-(h-epsilon)xihat` and boundary residual `d=g_lambda-(partial_n xihat-T_lambda gamma xihat)`, the exact -Delta/2 weak Green identity gives
`
 a_lambda(xi-xihat,v)=<r,v>+1/2<d,gamma v>.
`
The outgoing observable's adjoint uses an **incoming** reference boundary. With actual dual z, `delta A=<r,z>+1/2<d,gamma z>+delta A_exterior_particular`. None of the full continuous low inverse, whole-cell residual majorant, high-angular BC defect, or dual operator norm is closed; physical amplitude and thermal rate remain null. Once a justified angular amplitude L2 bound epsA exists, `|delta I|<=2||Ahat|| epsA+epsA²` is the next decision formula.

## Actual sources, CAS, REI

Wolfram15.0.1 returned exact `13pi/8`, Coulomb tail identity and exact zero Schur residuals; verified xAct/xTensor1.3.0 (official xTensor.m SHA256 04e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36) returned four Euclidean tensor zero residuals. Actual local science checks 21, exact exterior rational checks12, 26 zip payload SHA and CRC, relocated verification, changed-copy rejection/restoration passed. Same-author arithmetic/CAS, external independent science review and native subagents NOT_RUN. No old BVP, near-rate, ODE, native/HPC or REI science reruns.

Read latest CR63: observed HeI/HeII threshold-centroid source-weighted absorption differences 10.40854%/38.59412% versus continuous source (not abundance/tau errors). Separate source-representation physical model review is appropriate; do not mutate current REI science or relabel these as ion fraction biases. HE54 covariant electron current and HE53 already-integrated AXBI reducer were read; don't reapply prior source-pair patch.

Latest actual live REI owner at 2026-10-14T14:30:55Z: HEAD1cb70de50b821901563b6bdf2434651be3c7f9e5, AX07 scoped ZERO complete, AX08 signed in progress, AX11/12 pending, next_ready_ids empty; owner requests natural PLUS recovery completion before further handoff. No scientific solver launched, killed or owner STATE mutated by HH. Optional HH remains OFF and stellar50000K does not equal cold-gas temperature.

## Durable evidence and next

Full27-member ZIP (26manifest payloads) **64,997 bytes SHA256 e792f06520ca64feec9c737541658b9b1f3042c16744a86ecd7544283a486872** has Korean theorem, frozen u/r exact subset identity, original source code, reproducible analytical and sampled checks, Wolfram submissions and selected outputs, REI handoff, original failure classification. [Drive archive](https://drive.google.com/file/d/1hvZbitN3xcOn-TOJfMUAWC7LRmVa1sxi/view?usp=drivesdk), Dropbox id `id:BSpOijBcT10AAAAAAD7Jig` at existing HH destination; both acknowledged exact size. Local CRC/26 SHA and relocated science21, altered-copy rejection/restored pass. No remote full-archive restoration claim. Next `LOW_INF_SUP_CERTIFICATE_AND_WHOLE_CELL_RESIDUAL`. No merge or production promotion.
