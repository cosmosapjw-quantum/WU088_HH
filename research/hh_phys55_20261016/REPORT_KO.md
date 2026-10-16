# PHYS55 | infinite-high screened collar + central Coulomb outgoing hybrid DtN

2026-10-16 KST. WU088_HH research successor to PHYS54 in Draft PR #94,
parent commit `9a3054487db04feea99ff7d5714398043e15425d`. Scope is **new operator-theoretic hybrid**:
original noncentral screened high-angular `Q S Q` on finite collar `[20,27]`,
**central Coulomb only** for exterior `r>=27`. NOT the full physical screened exterior.

## Original source and definitions

Original atomic hamiltonian `h=-Δ/2-1/r-(1+s^-1)e^-2s`,
`s=|x-(7/10) zhat|`, `R=kappa=7/10`, original eta=`F y`, xi=`F y-phi`.
Keep the original 1,386 complex128 frozen source `research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz`
SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d` unchanged.

Define `Q=P_{ell>=21}` and `X_T={g: sum_(ell>=21,m)(ell+1)|g_lm|^2 <∞}`;
its norm is `||g||_X²=sum W_l |g_lm|²`, `W_l=ell+1`.
The parent PHYS50 trace `X_B⊕X_T` and bounded real/Hermitian positive
collar DtN `Lambda_D` are reused, not reimplemented here.

## New Theorem A: rigorous unconditionally positive collar TT form

For any `g_T∈X_T`, set the lower collar trace `g_B=0`. Let `u_g` solve
the original screened high-channel positive form on `[B,T]=[20,27]`:

`a(u,u)=int_B^T {||u'||²+sum_(ell,m)[ell(ell+1)/r²-2/r-kappa²]|u_lm|²-2< u,S(s)u >_Ω} dr.`

Since `s>=r-R>=B-R=193/10`, the original physical screen satisfies

`0<=2S(s)<=delta_0=2(1+10/193)e^(-193/5)`.

For the exact positive Taylor `E_30=sum_(n=0)^30 (193/5)^n/n! < e^(193/5)`,

`delta_0 <= delta_30=2(1+10/193)/E_30 <10^-12`.

**No sampled angular matrix** is needed for this all-ell bound. With `d=7`,

`a(u,u)>=sum_(ell,m) int_B^T (|u'_ellm|²+a_ell²|u_ellm|²)dr`,

`a_ell²=ell(ell+1)/27²-2/20-49/100-10^-12 >0 (ell>=21)`.

For the 1D minimization `v(B)=0`, `v(T)=g_T,ellm`, the exact minimizing
function is `sinh(a_ell(r-B))/sinh(a_ell d)` times the boundary trace;
its energy is `a_ell coth(a_ell d)|g_T,ellm|²>=a_ell|g_T,ellm|²`.

The *exact rational* weighted squared lower ratio

`a_ell²/(ell+1)² = ell/(729(ell+1)) - (59/100+10^-12)/(ell+1)²`

has strictly positive derivative for every real ell>=21 and is minimized at ell=21.
At this endpoint,

`a_21² = 10629999999757 / 243000000000000`,

`a_21²/22²-(9/1000)² = 1103427999757 / 117612000000000000 >0`.

Therefore, for **all ell>=21 and all m without angular cutoff**,

**`<g_T,Lambda_D,TT g_T> >= (9/1000)||g_T||_X².`**

Here `Lambda_D,TT` is the TT block of the original noncentral screened
collar DtN, with homogeneous B trace, and retains its off-centre angular mixing.
It is bounded `X_T→X_T*` by PHYS50 `C_trace=4849/16800`.

## New Theorem B: complete CENTRAL outgoing high-angular operator

For `r=T=27`, `rho=kappa T`, `eta_C=-1/kappa=-10/7`,
let `H_ell^(+)=G_ell(eta_C,rho)+i F_ell(eta_C,rho)` and
`z_ell=kappa (H_ell^(+))' / H_ell^(+)` (prime wrt rho).
The real Coulomb functions are independent with nonzero Wronskian,
so `H_ell^(+)!=0` for every finite ell and positive rho. Thus

`Im z_ell=kappa/(F_ell²+G_ell²)>0`.

DLMF §33.5(iv) (33.5.8-9) states at *fixed rho, eta_C* as ell→∞:
`G_ell ~ exp(pi eta_C/2)(2ell-1)!! rho^(-ell)` and `F_ell/G_ell→0`.
Using the **exact** DLMF §33.4 recurrence

`H_ell'/H_ell=(ell+1)/rho+eta_C/(ell+1)
  -sqrt(1+(eta_C/(ell+1))²) H_(ell+1)/H_ell`,

and `H_(ell+1)/H_ell ~ (2ell+1)/rho`, we obtain

**`z_ell/(ell+1) -> -1/T`** with `Im z_ell/(ell+1)->0`.

Consequences established as **operator facts**, no finite sampling assumption:

1. The exact diagonal central `Z_C=diag(z_ell)` is bounded `X_T→X_T*`.
2. `D=W^(-1/2) Z_C W^(-1/2)` on `ℓ²({ell,m})` satisfies
   `D+(1/T)I` compact: its diagonal entries approach zero and each
   ell shell has finite multiplicity `2ell+1`.
3. There exists a finite *unspecified* `L0` such that
   `-Re z_ell>=0` for all ell>=L0. This is an existence assertion,
   NOT a certified explicit numeric cutoff.
4. The imaginary form is strictly positive for every nonzero `g∈X_T`:
   `Im<g,Z_C g>=sum j_ell|g_lm|²>0`, even though `inf j_ell=0`.

## New Theorem C: unconditional infinite-angular **HYBRID** gluing

Define the hybrid high-to-high matching map `M=Lambda_D,TT-Z_C :X_T→X_T*`.
Theorem A supplies `Re<g,Lambda_D,TT g> >= cD||g||_X²` with `cD=9/1000`.
By Theorem B there are only finitely many ell values where `Re z_ell>0`.
Define the finite-rank nonnegative Hermitian boundary correction

`<g,Kg>=sum_(21<=ell<L0,m) max(Re z_ell,0)|g_lm|²`.

This is well-defined finite rank (finite shell degeneracy),
and `Re<g,(M+K)g> >=cD ||g||_X²`. The complex Lax–Milgram theorem
implies `M+K : X_T→X_T*` is bijective. Since K has finite rank,
M is Fredholm of index zero. If `Mg=0`, then

`0=Im<g,Mg>=-sum_(ell,m) Im z_ell |g_lm|²`.

Every `Im z_ell>0`, so `g=0`; the Fredholm alternative proves M onto,
with bounded inverse. Thus, **for every abstract h∈X_T***, there exists
exactly one `g_T∈X_T` satisfying `M g_T=h`.

This is a true infinite-angular theorem, unlike PHYS52's finite 400-channel
outgoing matching. Crucially it is **not the full screened physical exterior**:
`Z_S` and its `P-Q` off-diagonal exterior Schur coupling remain OPEN.
The inverse norm is known to be finite but is NOT assigned an explicit
numeric upper bound, because L0 and the finite exceptional block have
not been certified with interval arithmetic. The exterior central
ODE modes are the outgoing Coulomb waves; this theorem establishes the
weighted boundary operator isomorphism, not the original physical `xi`.

## Constructive verification and diagnostics

- Exact Python Fraction exponent/Taylor source bound and monotone ell margin,
  with immutable original NPZ input lock.
- Connected Wolfram independently verifies exact endpoint margin,
  derivative monotonicity and the recurrence principal limit `-1/27`.
- Multiprecision `mpmath.coulombg/coulombf` outgoing diagonal evaluated for
  `ell=21,22,28,29,40,64,128,256`, `r=27`.
- NONCERTIFYING actual off-centre screened angular matrix in `m=0`, ell21..23:
  scalar FE energy minimization 20..27 with 96 angular Gauss nodes,
  20,40,64 radial elements, and **central** exact outgoing exterior.
  At r20 the offdiagonal S_21,22=3.938083625263274e-18 a.u., so the
  original noncentral potential is actually evaluated, not set to zero.
- The discrete small-grid weighted collar lowest eigenvalues are about
  0.01636444, 0.01636946, 0.01637048 and hybrid min singular values
  0.02532958, 0.02533446, 0.02533546 (noncertifying discretization).
- Floating numerics do not establish the all-ell theorem; the two operator
  theorems above depend on exact rational energy and DLMF asymptotics.

The initial focused test had 2 failures (one `f64` underflow on `~10^-510`
positive current and one invalid negative-test assumption excluding
perfectly valid `delta=0`). A first rushed edit misattached a pytest
parametrization, causing collection failure. Each is corrected without
changing original physics or weakening acceptance; initial errors are
recorded as implementation/test design, not scientific no-go.

## Sibling inputs and remaining work

GitHub readback as of 2026-10-16 KST: WU PR94 commit
`9a3054487db04feea99ff7d5714398043e15425d`; `rei_bianchi`
PR157 `710f08b2bebaefbd6a28690d450d759877053ebb` (native H/He
photochemistry and energy ownership), `BASS_HE` PR70
`45b940f1d190713eb4c15bd5560112b6c542c9e4` (total H nuclei
density contract), `bass_cr` PR74
`caf587b3edf4e27d038c6a918419be498d7d389c` (NCP source
and ledger recovery). These are distinct input/source lanes,
not the missing actual H-H reaction-rate provider.

Sources: NIST DLMF §33.2 Wronskian and H+, §33.4 Coulomb derivative recurrence,
§33.5(iv) fixed eta/rho large-ell asymptotic, §33.23 computation.
M. Behrndt et al., *Spectral shift functions and Dirichlet-to-Neumann maps*
(2017), DOI 10.1007/s00208-017-1593-4 motivates operator-valued Weyl maps,
but does NOT independently prove this particular source-specific theorem.

**PHYS56 next:** extend Theorem C from Z_C to the *original screened*
exterior Z_S, including full noncentral low/high P-Q coupling and quantified
`X→X*` screened resolvent difference. This requires an actual outgoing
construction and a bound relative to the hybrid Fredholm gap, not merely
`sup|2S|<1e-22`. Then resolve physical nonzero g_B, driven
`xi=F y-phi`, incoming adjoint, cross section sigma(E), Maxwellian
identical-H k_HH(T). `rei_bianchi HH_R10=OFF` throughout.

Scope/execution: Sandbox Python only; NCP NOT_RUN in this step; full WU
pytest NOT_RUN (original full repo not mounted). Native subagents NOT_RUN
(no native dispatch tool exposed). Publication and cloud preservation
must be recorded separately from science validation.
