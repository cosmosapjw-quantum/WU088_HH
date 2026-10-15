# WU088_HH PHYS37: C7B cusp-shell coupled angular residual certificate

2026-10-15, R5 constructive support + selected C7B scientific coding. Parent draft PR75 commit `2f06fc263a1162a1eb0fb2ce7fdfda2317e0f272`, based on PHYS36 C7A. No separate local Codex was used. A new isolated WU088_HH branch contains the actual Python source/tests/run results. **C7B is PARTIAL for the whole radial domain**, but the complete two one-sided `r=R` angular shell certificates and exact interface strong trace jump are closed.

## 1. Protected model and units

Frozen spectator H(1s), one-centre Coulomb reference, static neutral spectator screened potential
`h_lambda=-Delta/2-1/r-lambda*S(s)`, `S(s)=(1+1/s)exp(-2s)`, `s=|r-R ez|`, `R=kappa=7/10`, `lambda=1`, `epsilon=kappa²/2`. Radii are in `a0`, energies in `Ea=2I0`. Source `I0=13.605693122990eV` and receiver `chiH=13.598434599702eV` are different; physical `c,hbar,k_B` are retained. Signature(-,+,+,+), electron-space Euclidean. Bound orbital `phi=e^-r/sqrt(pi)`, source-lift `eta=phi+lambda xi=F y` with `F=e^(lambda e^-s)`, collision tag and original transition `S(R)-S(s)` unchanged. Only the 1s spectator-direct same-model numerical representation is altered.

## 2. Exact cusp-shell coordinate transform, not a cusp-smoothing replacement

The mathematical point is the second proton centre on `r=R`. Set `x=s/(2R)` and `mu=cos(theta)=1-2x²`, `0<=x<=1`. Then
```
P_l(1-2x²)=sum_(k=0..l)(-1)^k C(l,k) C(l+k,k) x^(2k)
T_l(x)=l(P_(l-1)(mu)-mu P_l(mu))
      =(1-mu²)P_l'(mu)=O(x²).
```
The `1/s` in angular advection cancels **exactly**: `H=x C -T/(2R x)`, with `T/x` an ordinary odd polynomial.

Normalize the physical residual `mathcal R` as `G(x)=sqrt(4pi)mathcal R(R,mu(x))`. Define `A=Σ_l sqrt(2l+1)D_lu_l(R)/R P_l(mu(x))`, `B=Σ_l sqrt(2l+1)u_l(R)/R P_l`, `C=Σ_l sqrt(2l+1)(u_l'(R)/R-u_l(R)/R²)P_l`, `T=Σ_l sqrt(2l+1)u_l(R)/R * l(P_(l-1)-mu P_l)` and `H=xC-T/(2Rx)`. Then, with `E=e^(-2Rx)`, `Q=(1-E)/(2Rx)`, `U=EQ-E/2-3E²/2`, the ORIGINAL transformed source equation is exactly
```
G=A -2E H -2U B -2(1+kappa²)e^(-R)e^(-E).
```
Its **physical angular** norm is exactly `||mathcal R||²_(L2(S²))=2∫_0^1 x |G(x)|²dx`; no missing 2pi or spherical-harmonic degeneracy factors.

The true input is the exact dyadic Lagrange interpolation polynomial through PHYS34's stored `FROZEN_U_SUBSET.npz`, SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`. The physical `R=7/10` is not silently equated to the nearby IEEE-binary64 stored interface node. Both panel polynomials are evaluated at the exact mathematical `7/10`.

## 3. Rigorous polynomialization and error

Each `sqrt(2l+1)` is enclosed in exact rational 64-decimal brackets using integer square roots. `E` and `Q` use their rational Maclaurin polynomials with Lagrange bounds `S^(N+1)/(N+1)!` and `S^N/(N+1)!` for `S=2R=7/5`. `g(s)=exp(-exp(-s))` has `g'(s)=exp(-s)g(s)`; a rational recurrence computes `g_N=e^(-1) Σh_n s^n` with the constant `e^-1` rigorously rational-bracketed. Complex Cauchy on `|s|=3`, with `|g|<=exp(exp(3))<2^31`, gives
```
||g-g_N||_(infty,[0,7/5])
 <=2^31(7/15)^(N+1)/(1-7/15)
   +||error(e^-1)||*sum_n |h_n|(7/5)^n.
```
Both exp(3)<21 and exp(21)<2^31 are independently established by positive rational Taylor sums and explicit geometric-tail bounds inside the code. The `P_l` and derivative bounds `|P_l(mu)|<=1`, `|P_l'(mu)|<=l(l+1)/2` on real `[-1,1]` provide an explicit coefficient/special-function rounding envelope. All finite polynomial squares and `2∫x dx` are **exact Fraction arithmetic**, with sqrt rounded outward. A true shell error is obtained from `||G||<=||G_N||+epsilon_N`, independent of NumPy previews.

## 4. Actual certified shell results

At Taylor `N=96`, 18 outward decimal digits, exact same frozen source:

| frozen polynomial radial side | rigorous `||mathcal R||_(L2(S²))` upper | independent float x-Gauss96 sample |
|:---|---:|---:|
| left panel j1 `r=R^-` | **0.001697685390802356** | 0.001697685390802352 |
| right panel j2 `r=R^+` | **0.009340991924804115** | 0.009340991924803815 |

Actual common certificate `SHELL_BOTH_N96_18.json` includes the polynomial norm upper, explicit uniform remainder upper and input/module SHA. Both sides executed in parallel through `forkserver`, `19.884s` elapsed / `20.05s` shell wall; serial n96 left `19.638s` + right `17.691s` =37.329s, **~1.88x observed speedup**. Parent process peak RSS34.1MiB is not cumulative worker memory. The fast NumPy/SciPy `x`-Gauss96 diagnostic takes ~0.002s/shell and agrees within the rigorous intervals; it is not an interval certifier. Legacy direct `mu` Gauss512 still gives a misleading higher value ~0.00934101038 at the cusp because of nonanalytic square-root geometry, while the `x`-Gauss stabilizes by ~40nodes.

## 5. Exact new interface evidence, and its careful meaning

Form an exact rational polynomial for `G_right-G_left` at the same physical shell and enclose its full angular squared norm. The true **strong residual trace difference** is

```
||mathcal R(R^+)-mathcal R(R^-)||_L2(S²)
 in [0.010477110356590, 0.010477110356593].
```
The field-value and first-radial-derivative interface angular jump uppers on the SAME frozen piecewise-polynomial trial are respectively `1e-15` and `9e-15`. Large strong residual trace discrepancy is **not a distributional delta**, whose source is determined by value and first-normal-derivative jumps. This exact interface accounting is a new input to later continuous low-Schur/boundary analysis.

## 6. Verification, literature, optimization, dependencies

Real Wolfram Engine15: 45/45 exact scalar identities zero, including Legendre `P_l(1-2x²)` up to ell20, cusp factor cancellation, angular Jacobian, q(0), and exact real-domain measure. Actual local xAct/xTensor1.3.0 Euclidean Green product 1 tensor zero. Python clean-source and full-repo pytest runs, manufactured rational tests, one-sided source/cusp tests, direct x-Gauss cross-check, exact Cauchy majorant, negative controls, rebuilt file SHA: see `results/FINAL_FULL_TEST.stdout`. Test/timing and failed initial shells are kept separate. Native subagents NOT_RUN because none exposed; no external independent scientific review.

Relevant contemporary research: literature on cusp-aware two-centre spherical harmonics (e.g. doi:10.1063/5.0124647 and arXiv:1203.6256) motivates treating off-centre singularities by their own coordinates; their published coefficients are NOT copied to this frozen-direct model. Latest BASS_HE PR61 finishes fifth warm P01 saved time-cell, distinct gas/photon source. Latest bass_cr PR68 has 48->22 threshold-safe cohorts with directed curvature, distinct RT source. Both are read-only and excluded from the HH scattering rate. Actual rei_bianchi owner is checked read-only, AX07 scoped ZERO completed, AX08 signed in progress, AX11/12 pending and owner work is not duplicated. Optional HH source is OFF for cold IGM; no 50k stellar spectrum temperature is treated as gas temperature.

## 7. Limits and next executable coding node

**C7B cusp-shell component is completed; global C7B is still PARTIAL.** A single `r=R` shell has measure zero in the 3D bulk integral and cannot replace PHYS36 C7A's `2.603747132326` broken-volume upper. Work remaining:
1. Extend the exact `s`-coordinate angular certificate to finite-width radial strips around `r=R`, using general `s ∈[|r-R|,r+R]` and rigorous radial interval bounds without a false analytic continuation through `s=0`.
2. Combine all actual radial panels, bound distributional interface, excluded origin `r<1e-4`, outgoing DtN and low-Schur inverse/dual physical amplitude.
3. Until this closure, global two-centre intensity, rate, chemistry/P01 transfer and physical calibration remain **null**. No change to original source/production/Codex owner.

Next select `C7B_RADIAL_STRIP_LIFT_AND_COUPLED_WHOLE_CELL` from the updated DAG.
