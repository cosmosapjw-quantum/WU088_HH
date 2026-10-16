# PHYS59 C5–C8: 원래 비중심 H–H screened exterior 오프셸 DtN의 Born 나머지 정리와 실제 radial/angular 코드 검산

2026-10-16 KST, based on PHYS59 R5 Git HEAD `a61747c2221d86ad357bee062f2a87a651221ae2`, Draft PR #101, which itself is stacked on PHYS58 PR #100 `e9a80d7a7280a4b944a7a9d0a2ce3bb4ca971a2f`.

## Scientific contract and limitation

Original `h=-Δ/2-1/r-S(s)`, `S=(1+s^-1)e^-2s`, `s=|x-0.7 zhat|`, `kappa=7/10`, original `eta=Fy`, `xi=Fy-phi` preserved. Frozen original 1386 complex128 SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d` verified in actual sandbox source. Original potential used unchanged across full noncentral radial and angular calculation.

The computed/reference operator is at **real negative E=-49/200 Hartree, decaying off-shell exterior** on `r>=27`, with all angular modes in the rigorous operator theorem. This is **NOT** the physical **positive** E=+49/200 Coulomb *outgoing* scattering DtN. No rho/kappa phase ambiguity. `Z=+∂r`, and original P ell<=20 / Q ell>=21 coupling retained. Actual positive-energy LAP, `xi`, incoming adjoint, physical `sigma(E)`, Maxwellian `k_HH(T)`, `HH_R10` remain OPEN/OFF.

## New R5→C5 remainder theorem (infinite angular, exact rational)

Let `A_C=-∂²+L²/r²+kappa²-2/r` be the negative-energy Coulomb operator with zero outer Dirichlet trace domain, `G_C=A_C,D^-1`, `P_C` its decaying Poisson map, and let `V=2S` be the actual full noncentral screened multiplication. The original full screened Poisson map obeys `u_S=(I-G_C V)^-1 P_C g`. Green identity yields

`D:=Z_S^- - Z_C^- = P_C^* V (I-G_C V)^-1 P_C`.

The first Born term `D1=P_C^* V P_C` therefore has exact residual

`D-D1 = P_C^* V G_C V (I-G_C V)^-1 P_C`,

where no intermediate mode was suppressed. PHYS59 R5 proved `||P_C||_(X→L²)^2 <=C_X/beta<=3`, `||G_C||<=1/beta_C`, with physical `beta_C=1123/2700>2/5`, and exact physical `||V||<delta=3e-23`. Hence `q=||G_C V||<delta/(2/5)=3/(4*10^22) <1`. Entire original all-angular operator obeys

`||D-D1||_(X→X*) <=3 delta q/(1-q) <7e-45`.

For the unnormalized raw m0 boundary matrix element `(ell output21,input20)`, `||e21||_X||e20||_X=sqrt(462)<22`, yielding the explicit **true full noncentral off-shell DtN vs Born** bound

`|D21,20 - D1_21,20| < 154e-45 = 1.54e-43`.

**This upper is exactly rational and all-angular**, not measured finite-grid error. It does not certify the floating quadrature value of `D1` unless that approximation's quadrature error is independently bounded.

## Constructive physically original first-Born radial integral

At this negative energy, the exact decaying central Coulomb radial Poisson functions normalized at B=27 are

`p_l(r)=WhittakerW[1/kappa,l+1/2,2kappa r]/WhittakerW[1/kappa,l+1/2,2kappa B]`.

The original P20/Q21, m0 Born element is

`D1_21,20 = integral_{27}^infty dr p21(r) V21,20(r) p20(r)`, with

`V21,20(r)=integral_{-1}^1 dmu b21(mu)b20(mu)*2*(1+1/s(r,mu))exp(-2s(r,mu))`, `b_l(mu)=sqrt((2l+1)/2) P_l(mu)`.

This uses original displaced screening at every radial/angle node, no centralization, and exact outgoing sign replaced by decaying negative-energy boundary. `mpmath.whitw` Poisson solves the actual Coulomb negative-energy equation and is independently checked against `-p''+(k²-2/r+l(l+1)/r²)p=0` to ~1e-53 relative at r28.5.

An independent two-dimensional Gauss-Legendre test uses 10×96, 18×128, 26×192, 34×256 radial×angular nodes on r27..39; 70-75-digit Whittaker. All rows are **NONCERTIFYING floating quadrature values**:

| GL radial × angular | Born P20/Q21 m0 element [atomic units] |
|---|---:|
| 10×96 | 1.61913030748356e-24 |
| 18×128 | 1.62165104639885e-24 |
| 26×192 | 1.62165104690361e-24 |
| 34×256 | 1.62165104690235e-24 |

Difference between final two rows is 7.7740852e-13 relative, a diagnostic, not a strict inclusion proof. The omitted r>=39 radial tail has the **independent rigorous** direct-bound expression

`|tail|<=delta exp[-(2+2sqrt(beta_C))*12]/(2+2sqrt(beta_C)) ~6.5283e-41`.

The tail inequality follows from scalar Poisson comparison `p_l(r)<=exp[-sqrt(beta_C)(r-B)]` and `||V(r)||<=delta exp[-2(r-B)]`, not from unproved numerical convergence. The actual full DtN includes a mathematically bounded Born multi-hop correction <1.54e-43 for this raw entry. The fixed rational PHYS59 R5 **strict lower** `D21,20>1701/(2216*3^60)=1.8107533e-29` independently ensures actual nonzero P/Q boundary coupling.

## Numerical and independent symbolic validation

- Original 1386 complex128 SHA gate PASS on actual recovered frozen NPZ.
- New 15 pytest parametrized tests PASS (27.82s, peak RSS 143596 KiB; process wall30.37s). Tests include normalized Whittaker at B, ODE residual, bracket Poisson radial upper/lower comparison, m0/m1/m2 original 2S nonzero, ±m symmetry, independent 128/256 angular grids, radial convergence, invalid inputs, source identity.
- R5 separate scoped 26/26 PASS (0.59s) preserved in R5 receipt. Combined long pytest was attempted twice but sandbox time budget interrupted at 13/15 new tests (and next at 39/41); the interrupted runs are **NOT_PASS**, first failure/timeouts preserved, stage-local split commands run independently to exit0. Thus verified total 26+15=41 tests by separate commands.
- Source-guarded C5–C8 producer exit0 (18.97s wall, 110860KiB max RSS). Independent connected Wolfram exact rational `q` and Born remainder `27/(39999999999999999999997...0000)` and raw offdiagonal guard PASS after transient failed evaluator attempt. This was NOT native wolframscript.
- No NCP job required, original full WU088_HH suite NOT_RUN, native subagents NOT_RUN. No original REI/BASS_HE/bass_cr mutation.

## Per-stage science DAG

**R5:** PROVED/PR101 published/source-NPZ capsule and independent cloud-provider evidence.
**C5-C8:** PROVED_SCOPED_BORN_OPERATOR_REMAINDER, NUMERIC_WITNESS_NONCERTIFYING / new Draft PR / independent capsule.
**PHYS60:** READY_THEORY physical **positive-energy** Coulomb outgoing LAP, Poisson boundary mapping, resolvent control and genuine `Z_S^+` along all angular P/Q.
**PHYSICAL XI/RATE:** HOLD until original driven `xi=Fy-phi`, regular origin/incoming adjoint, physical sigma(E) and identical-pair Maxwellian k_HH(T). REI `HH_R10=OFF`.
