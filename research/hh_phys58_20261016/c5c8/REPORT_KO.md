# PHYS58 C5–C8: exact positive noncentral multipole coefficients and rigorous nonzero physical P/Q transfer

## Protected inputs and stage boundary

Parent R5 PR #99 HEAD `350efd1977c4d976000faa4371afc6e33915add3` (based on PHYS57B PR #98 HEAD `b6d95a931f596876eb2097b08fdb16ac542f9364`). Source identity frozen `FROZEN_U_SUBSET.npz` SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d` (1386 original complex128). Original atomic-unit h=-Delta/2-1/r-(1+1/s)exp(-2s), s=|x-(7/10) zhat|, k=7/10, eta=Fy and xi=Fy-phi preserved. This stage builds an *actual original physical screened angular multiplication* component but not an outgoing screened exterior Coulomb resolvent, DtN, physical scattering cross section or thermal rate.

## C5 exact finite elementary polynomial-exp integral, source-specific

For rational r>=27 and R=7/10, define x=s, c=(r²+R²)/(2rR), d=1/(2rR). The Legendre multipole

`A_n(r) = (2n+1)/(2rR) int_{r-R}^{r+R} (s+1)e^-2s P_n(c-ds²) ds`

is evaluated *without angular quadrature* by exact Fraction polynomial coefficients `Q_n(s)=(s+1)P_n(c-d s²)` and

`B_n(s)=sum_{j=0}^{deg Q_n} Q_n^(j)(s)/2^(j+1)`.

Indeed derivative of `-e^-2s B_n(s)` is `Q_n(s)e^-2s`, so

`A_n(r)=(2n+1)/(2rR) [B_n(r-R)e^-2(r-R)-B_n(r+R)e^-2(r+R)]`.

For positive rational y, the exact positive Taylor partial sum `E_N=sum_{j=0}^N y^j/j!` and rational geometric remainder `R_N=[y^(N+1)/(N+1)!]/[1-y/(N+2)]` certify

`1/(E_N+R_N) <= exp(-y) <=1/E_N`

for `N+2>y`; `N=320` is used. Rational signs are tracked when combining endpoint terms, producing an exact lower/upper Fraction enclosure for each `A_n`, not only a floating estimate. At r=27 we certified n=0..12 strictly positive by intervals, and at r=30 n=0,1,2,4,8,12. This is consistent with the full R5 all-n analytic positivity proof, but does not replace it.

## New rigorous physical P-Q nonzero theorem

For `m=0`, the Gaunt factor

`<Y_{ell0},P_n Y_{ell'0}> = sqrt[(2ell+1)(2ell'+1)] [3j(ell,ell',n;0,0,0)]² >=0`.

The full R5 Laplace representation proves all exact `A_n(r)>0`. At **r=27** exact `A_1(27)>6*10^-24`; its `n=1` Gaunt is

`<Y_21,0,cos(theta)Y_20,0> =21/sqrt(41*43)>1/2` (since 1763<1764).

Therefore the full ORIGINAL PHYSICAL off-centre `2S` operator has nonzero low/high transfer

`<Y_21,0, 2S(r27) Y_20,0> > A_1(27) > 6*10^-24`.

This is a genuine all-n angular coupling lower bound without discarding higher n. In particular a purely Q-only exterior approximation suppressing `V_QP` is not the full model, even when screen is tiny. This is compatible with the R5 far-high **upper bound** `||Q_ell>=29 2S P_ell<=20||<2.373114e-27`; both statements describe different high angular output sectors and do not contradict each other.

For arbitrary `m`, implement exact SymPy Wigner3j Gaunt coefficients with selection `m` conserved, triangle `|ell-ell'|<=n<=ell+ell'`, parity `ell+ell'+n` even and `+m/-m` symmetry. At arbitrary r the original screened multiplication is real self-adjoint and bounded by its scalar sup; these statements are **not** claims about `Z_S` or its resolvent.

## Executed independent numerical diagnostics (not certification)

Source-locked exact intervals and direct independent `mpmath` physical angular integral agree for n=0..12 at r27, n=0,1,2,4,8,12 at r30, with mp.dps=240 for narrow rational enclosures. Representative physical coefficients (1/Bohr² reduced-radial potential convention):

| n | A_n(27) from independent mpmath |
|---:|---:|
|0|4.9313778894149000407576014177699989e-24|
|1|6.1692201837483078893838676485409790e-24|
|4|1.6336511600174214724819145582005937e-25|
|8|4.7067933561762713573027385924254639e-29|
|12|2.2926986571208977537830722244035494e-33|

Actual original `2S` matrix `{ell=20,21,22}` at r27, Gaunt N=12 versus independent SciPy 128/256 Gauss–Legendre integrals, is real and symmetric, with observed `<Y_21,m|2S|Y_20,m>`:

|m|numerical original physical offdiag|
|---:|---:|
|0|6.47353037253661e-24|
|1|6.46261796762336e-24|
|2|6.42988810072094e-24|

Maximum Gaunt-vs-GL256 absolute discrepancy in targeted tested m blocks was <5e-35, as implemented, but finite floating quadrature is NONCERTIFYING. For exact degree-N multipole `S_N`, the R5 whole-space **rigorous** angular truncation bound `||2(S-S_N)||_op` remains independent of these numeric values; N=12 gives bound `3.3607681755829904e-31`.

## Review/first failure preservation

1. First direct numerical test run returned 26 failures / 16 pass. Most failures were **representation/test precision**: compared extremely tight rational exponential enclosures to only mp.dps=95 `mpmath` numbers, then falsely rejected valid exact bounds due to input rounding; a Gaunt parity fixture incorrectly expected nonzero (l,lp,n)=(20,21,40), sum odd. No modification to physical conventions or mathematical bounds.
2. Diagnosed repair run returned 20 failures / 22 pass because helper explicitly capped `dps<=150` while the new independent interval check requires ~230+, and one producer fixture still used 70 dps. Updated allowed precision to 180..450 for independent comparator, default 240, fixed parity fixture and precision. The exact Fraction endpoint mathematics remained unchanged.
3. Final combined PHYS58 R5+C5-C8 actual sandbox suite: **77/77 PASS**, source-locked producer exit0, peak RSS and wall time in receipts. Tests include invalid/tampered source, bounded exponent Taylor and 256-node GL independent reference, negative m parity and nonzero full physical P20-Q21 channel.
4. Connected Wolfram initially had a protected/ambiguous symbol in one attempted integral, and one subsequent internal failure; successful final independent algebraic evaluation gave A0=4.9313778894149e-24, A1=6.1692201837483e-24, `A1>6e-24 True`, `21/sqrt(1763)>1/2 True`, and `2 Gaunt*A1=6.17096957274809e-24`. This is only n1 partial term, not the full numeric matrix ~6.4735e-24.

## Scientific DAG and literature

R5 `COMPLETE_RIGOROUS_MULTIPLIER`: actual all-angular E10 geometric bound on P-Q direct source, original positive multipoles (complementary to PHYS47's radially integrated source bound). C5-C8 `COMPLETE_SCOPED`: certified finite endpoint-rational multipole intervals through n12 and actual source-backed original Gaunt m-block numerical comparison. The actual outgoing **screened exterior** DtN `Z_S`, its weighted LAP and Poisson mappings, high-block P/Q Feshbach and invertibility remain **OPEN**. User's original xi=Fy-phi, incoming adjoint, sigma(E) and Maxwellian k_HH(T) remain HOLD, and `rei_bianchi HH_R10=OFF`.

References: Huang–Jia–Zhang, FMM-Yukawa multipole (CPC 2009 DOI 10.1016/j.cpc.2009.06.028); Trefethen, Approximation Theory and Approximation Practice Theorems 8.1-8.2 (uniform Bernstein coefficient bound); PHYS47/49/55/57b frozen predecessors. Latest REI PR165, BASS_HE PR72, bass_cr PR76 consulted as distinct source/consumer stages, not a replacement for H-H microscopic potential or original rate.

No NCP was used or needed for these 3x3/fraction calculations. Whole original WU pytest was not executed in this sandbox. Native subagents not exposed, NOT_RUN. No sibling repository or original trial mutation.
