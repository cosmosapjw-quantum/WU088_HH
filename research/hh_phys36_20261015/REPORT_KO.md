# WU088_HH PHYS36: R5 + C7A, two-centre source cancellation with local executable code

2026-10-15 KST. Scientifically authorized continuation of PHYS35 draft PR74, commit `ff1e82b223925870c35ae0405932a698d00bea10`. Coding happens in a new independent WU088_HH branch and actually executes on the user's Ubuntu workstation, **without Codex**. Current selected stage is C7, specifically the constructive partial substep **C7A_DIRECT_SOURCE_OVERLAP_AND_COUPLED_PREVIEW**, not a claim of completion of C7B/full global PHYS33.

## Original physics/units kept

Frozen spectator H(1s) two-centre direct potential with fixed residual proton B at origin:
`h_lambda=-Delta/2 -1/r -lambda S(s)`, `S(s)=(1+1/s)exp(-2s)`, `s=|r-R e_z|`, `R=kappa=7/10`, `lambda=1`, `epsilon=kappa²/2`, `h=H/Ea` with `Ea=2I0`. Coordinate r/R in Bohr radius `a0=5.29177210544e-11m`; source `I0=13.605693122990eV`, receiver thermal `chiH=13.598434599702eV` and c, hbar, kB remain distinct. Space metric Euclidean, background signature(-+++). Bound orbital `phi=e^-r/sqrt(pi)`. Same source-lift `eta=phi+lambda xi=F y`, `F=e^{lambda e^-s}`. No change to original transition operator `S(R)-S(s)`, parent Coulomb scattering phase, tagged reaction adapter, event thresholds or REI productions.

Parent transformed equation, multiplied by 2:
```
R[y] = (Delta+kappa²+2/r)y
     -2lambda e^-s shat.grad y -2 U_lambda(s)y
     -(1+kappa²)F^-1 phi =0,
U_lambda=lambda*(e^-s-e^-2s)/s-lambda e^-s/2-(lambda+lambda²/2)e^-2s.
```
From parent established `|U_lambda|<=lambda e^-s` for 0<=lambda<=1. **This unit certifies only broken bulk** on r0=1e-4..20 for the exactly dyadic-interpolated archived L20 degree10 piecewise radial trial. It does not include interface distribution, origin r<r0, high-l exterior Coulomb vs screened boundary, continuous low-Schur infsup or physical scattering rate.

## New exact direct source-overlap identity

Let `D=(Delta+kappa²+2/r)`, `S0=(1+kappa²)phi`. Angular harmonics are orthonormal with `Y00=1/sqrt(4pi)`; therefore `S0` has only reduced radial `l=0` coefficient `f0(r)=2(1+kappa²)r exp(-r)`.

For arbitrary exact finite polynomial `u_0(r)` on each panel,
```
Re <D y,S0> = 2(1+kappa²) Re integral_[r0,20]
  [r u_0''+(kappa²*r+2)u_0] exp(-r) dr.
```
The bracket is a genuine polynomial in physical radius even though the Coulomb reduced operator itself contains 1/r. Conversion of the stored IEEE-binary64 polynomial into physical-r rational coefficients is exact. For integer n>=0,
```
int_a^b r^n exp(-r)dr =
 n! [ exp(-a) sum_(j=0..n) a^j/j!
    - exp(-b) sum_(j=0..n) b^j/j! ].
```
Each exponential uses a positive rational exp(x) Taylor bracket with geometric tail, not a cancelling alternating series. Fraction cancellation is exact, **no MPFR required for the certificate**. Source squared norm on one panel is also explicit:
```
||S0||²_[a,b]=(1+kappa²)²
 [ exp(-2a)(1+2a+2a²)-exp(-2b)(1+2b+2b²) ].
```
Combining with PHYS35's genuine directed rational-log upper `||D y||` gives
`||D y-S0||²<= ||D y||_upper²+||S0||_upper² -2 Re<D y,S0>_lower`.

The independently derived exact **whole 3D angular convolution**
```
||exp(-s)phi||²=(3+6R+4R²)exp(-2R)/24
```
follows by integrating over mu via s and splitting r at R; at R=.7 equals `229 exp(-7/5)/600`. This is exact for the physical frozen orbital, not a fitted numerical factor. Since `0<=1-exp(-lambda exp(-s))<=lambda exp(-s)`, the source correction has norm at most `(1+kappa²)||exp(-s)phi||` for lambda1. Consequently
```
||R[y]|| <= ||D y-S0|| +2||exp(-s) grad y||+2||exp(-s)y||
                 +(1+kappa²)||exp(-s)phi|| .
```
The remaining screened norms retain the PHYS35 exact rational-log, 8-cell radial envelopes. Full angular cross terms are not yet directly cancelled, only the **exact l0 bare-source overlap** and the exact 3D Ephi convolution are now certified.

## Actual frozen input and local execution

Pinned source `research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz`, SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`, 21 angular waves, 6 panels, 11 radial nodes per panel, 1386 complex values. New code `src/wu088_hh/phys33_coupled_source.py` + runnable CLI `scripts/phys33_coupled_source.py`; second independent batched `src/wu088_hh/phys33_coupled_preview.py` computes the FULL differential strong residual at Gauss points with correct `(r-R mu)/s` radial and `R l(P_(l-1)-mu P_l)/(s*r)` angular derivative coefficient, and source `(1+kappa²)exp(-lambda exp(-s))phi`. The latter uses NumPy linear algebra / SciPy Legendre and is **NONCERTIFYING**. Off-centre cusp is not regularized by falsely replacing `s=0` on a Gauss grid.

Actual **certified C7A result**:
```
Re<Dy,S0> in [1.441417402798,1.441417402799]
||S0||²_[r0,20] in [2.220099999997,2.220099999998]
||D y-S0|| <=0.725518569620
||e^-s phi|| <=0.306786312012
previous PHYS35 screened-broken bulk <=4.001581079393
new direct-source screened-broken bulk <=2.603747132326
```
Output above is outward rounded and certificate uses exact rational internals. The new upper is ~1.54x narrower than PHYS35 and ~5.91x narrower than PHYS34 15.389831374480. No thermal ionization cross section or global physical observable is calculated.

1worker CLI runtime `11.55s` (shell wall `11.67s`, peak launcher RSS 37,968KB), 4worker CLI `4.30s` (shell wall `4.43s`, parent RSS37,648KB). 4workers preserve **exact same source panel/integer/rational fields** (not byte-equal JSON because execution-time field changes). Parallel workers are Python processes, NOT native subagents. User-owned separate Codex was not invoked. Output JSON intentionally gives outward decimal rational endpoints instead of the many-thousand-digit internal Fraction denominators. An initial Python integer-to-decimal string failure was corrected without relaxing scientific bounds.

Full-screened float64 angular Gauss diagnostic in m=0 reconstructed from actual Cheb nodal coefficients gives:
```
nr64,nmu96:    0.0017243410209536736
nr96,nmu160:   0.0017397736193707817
nr160,nmu256:  0.0017434463076317554
nr224,nmu384:  0.001744344341501646
```
These are **sampled** norms; the slow angular stabilization reflects spectator cusp and does not define rigorous uncertainty or "actual error". The independent D-minus-source sampled norm converges near 0.725518569619, inside the exact directed upper. Full angular coupled cross cancellation to reduce 2.6 toward sampled .00174 requires new interval angular representation near s=0.

## Verification and reuse

Observed actual Wolfram15.0.1: exact Ephi convolution, `Re<D,S0>` polynomial identity, bare source norm all literal-zero residuals. Local Wolfram Engine15 and actual xAct/xTensor1.3.0: 4 scalar zero residuals and Euclidean Green product 1 tensor zero with exit0. New mpmath170–200d numerical checks distinguished independent finite precision from the much tighter 256-term exact exponential rational bound. The first test erroneously treated finite mpmath as exact bracket witness; repaired tests compare a resolvable-width independent bracket while 256-term scientific values remain unchanged. Python's 4300-digit display limit fixed by exact outward decimal formatting. Fixed a mistaken test-note index and a preview variable-name error. Negative controls and original failures preserved.

Latest BASS_HE PR59 executes third warm P01 source cell with all photon carry; it is not this atomic continuum and supplies no scattering error coefficient. Latest bass_cr PR67's heap/ray vectorization and work allocation informed the separation of certified exact core versus quick NumPy preview; no source/RT physics was imported. REI owner worktree remained read-only. AX07 conditional ZERO complete, AX08 signed family active, AX11/12 pending, optional HH OFF; 50kK stellar source temperature is not cold gas thermal state.

## Next node and confidence

C7A source cancellation and explicit Ephi angular convolution are derived and actually implemented. **Full C7 angular-coupled interval certificate is PARTIAL**. Next `C7B_SCREENED_ANGULAR_COUPLING_INTERVAL_CERTIFICATE`: with kappa=R=.7 and exact finite radial polynomials, enclose angle-dependent screened operators including derivative/potential/source mixed cross terms, separate a small cusp neighbourhood, preserve Gaunt/partial-wave normalization, and connect interface/origin/outer dual later. Continuous inverse and two-centre thermal rate remain null.

No main merge or production admission; external independent science review and native subagents NOT_RUN. Full machine-readable evidence in results/*.json and the frozen input hash.
