# WU088_HH PHYS35, R5 + C6/C8: rational-log moments, screened residual, batched preview and safe parallelism

2026-10-15 KST. Scientific/coding successor of real PHYS34 C5 parent commit `45ed04e4ec3d29397b67bb7b3c447f8203d4b664`, draft PR73. **New runnable scientific sources changed inside WU088_HH**: `src/wu088_hh/phys33_moments.py`, `src/wu088_hh/phys33_preview.py`, `scripts/phys33_moments.py`, and source-bound regression tests. Actual Ubuntu runtime, same PHYS34 frozen NPZ input, no local Codex used. Native subagents NOT_RUN because host native dispatch tools were not exposed. The separate currently progressing rei_bianchi owner worktree was read-only.

## 1. Preserved scientific model and scope

Hamiltonian `h_lambda=-Delta/2-1/r-lambda S(s)`, `S(s)=(1+1/s)exp(-2s)`, `s=|r-R e_z|`, frozen spectator 1s, source lift `eta=phi+lambda xi=F y` and `F=exp(lambda exp(-s))` are unchanged, here `R=kappa=7/10`, `lambda=1`, `epsilon=kappa²/2`. Lengths are in Bohr radii `a0`; energies are in `Ea=2I0`, where source `I0=13.605693122990 eV` and receiver `chiH=13.598434599702 eV` are distinct. Keep physical c,hbar,kB, signature(-,+,+,+), Euclidean electron-space metric, original direct transition `S(R)-S_R`, continuum phase and event-tag network adapter. Existing one-centre Coulomb rate and P01 response certificates not changed.

Parent PHYS34 certifies only a *broken* full-angle L2 residual of the transformed cusp-wave `y` over `r0=1e-4<r<20` using the exact degree10 polynomial through the **actual** IEEE-binary64 stored collocation abscissae and 1,386 complex nodal values. It excludes origin r<r0, high-angular outgoing boundary mismatch, distributional interface residuals, continuous low-Schur inverse and actual scattering amplitude. The parent geometric32 bound **15.389831374480** takes ~25.22 seconds on the same user Ubuntu. The faster Gauss point evaluation ~.001665 is a *diagnostic*, not a rigorous bound.

## 2. New R5 mathematics: exact polynomial radial moments

On panel `r=m+h x`, `x in[-1,1]`, `u_l(x)` is the unique rational-coefficient Lagrange polynomial through stored dyadics. Define `N_l=r² u_l''+(kappa² r²+2r-l(l+1))u_l`, `G_l=r u_l'-u_l`. The positive squared radial integrals are

```
D² = sum_l integral |N_l(r)|²/r^4 dr,
G² = sum_l integral (|G_l(r)|²+l(l+1)|u_l(r)|²)/r² dr,
M² = sum_l integral |u_l(r)|² dr.
```

For each exact polynomial `P(x)=sum c_j x^j`, shift it into powers of r. Every monomial moment `integral_a^b r^n dr` is rational if n!=-1 and is `log(b/a)` otherwise. Therefore **every weighted squared integral is exactly A+B log(b/a)** for rational A,B. Log is enclosed by (i) extracting powers of 2, `b/a=2^k q`, `1<=q<2`; (ii) for `t=(q-1)/(q+1)<=1/3` using

```
log q in [L_N, L_N+2 t^(2N+1)/((2N+1)(1-t²))]
L_N=2 sum_(j=0..N-1) t^(2j+1)/(2j+1).
```

Positive elementary remainder bounds are rational, including all cancellation signs; arithmetic uses Python `Fraction`. Each panel's 21 angular modes share one cache of common monomial moments. All generated numbers are correctly enclosed outward, including sqrt lower floors and upper ceilings. This eliminates the old radial-minimum integration overestimate and many redundant integrations.

## 3. New stronger screened cusp bound

The exact conjugated scalar coefficient is

```
U_lambda(s) = lambda(E-E²)/s -lambda*E/2 -(lambda+lambda²/2)*E²,
E=exp(-s).
```

For 0<lambda<=1, `E <=(1-E)/s<=1` implies `-1<=U_lambda/(lambda E)<=1/2` and thus **|U_lambda(s)|<=lambda E** (continuous s=0 limit). The derivative coupling is `lambda E shat.grad`. From `s>=|r-R|` derive

```
||R_transformed_broken|| <= D + 2lambda||exp(-s) grad y||
                                 +2lambda||exp(-s) y||+(1+kappa²)||F^-1 phi||,
||F^-1 phi||<=1.
```

The positive weight `exp(-2s)` has on any radial cell `[a,b]` a sufficient rational upper

```
w_cell = 1/(sum_(j=0..64) (2d_cell)^j/j!),
d_cell = min_(r in [a,b]) |r-R| >=0.
```

This is safe because the 64-term positive Taylor sum is <= exp(2 d_cell). The weighted radial integrals reuse EXACT rational-log moments per cell for gradient, and exact polynomial moments for state. The entire angular polynomial is aggregated once before these subcell integrations. Geometric cell endpoints become exact dyadics and are emitted as exact rational strings. This proof is independent of float Gauss preview.

## 4. Actual native workstation science results

All values below are **upper bounds for the same broken transformed PDE bulk norm**, not physical ionization-rate errors:

| implementation | bound |
|---|---:|
| Parent PHYS34 geometric32, positive radial minimum | 15.389831374480 |
| New exact rational-log, no screened weight | 15.305581223915 |
| New exact rational-log, screened whole panels | 4.806959349323 |
| New exact rational-log, 8-screening cells/panel | **4.001581079393** |
| New exact rational-log, 16-screening cells/panel | **3.949959801991** |

The 8-cell version is the balanced default because 16 cells decrease the bound by only ~1.3% with higher runtime. All 1/2/4/6-process computations gave precisely identical bound/interval/panel/interface/input content for the same 1-screen-cell science, and forkserver preserves multi-thread safety. Default CLI: 4 workers and 8 screening cells, avoiding background Codex execution. Lightweight NumPy batched Chebyshev preview uses BLAS vectorisation across 21 ell and 96 radial Gauss nodes; it takes a few milliseconds per full diagnostic and is **NOT certified**. A 32-node preview overshoots the rigorous Coulomb-diagonal upper by ~5.7e-12 (float quadrature effect); 64-384 node previews stabilize near the certified upper. The preview is used for hot-spot selection, not for error admission.

Actual measured host: Ubuntu 24.04, Ryzen9 5900X (24 threads), runtime NumPy2.4.2 (historical pyproject requires==2.3.5, not silently revised). Parent geometric32 ~25.2s; initial new1-worker 8.55s; screened whole-panel 1/2/4/6 workers 8.55/4.63/2.52/2.36s under first fork process experiment; final robust `forkserver` four-worker 8-screen cell ~3.60s and retained correct science, parent peak RSS ~37MB (NOT aggregate all child RSS). Final fixed-source tests 104/104 pass with zero fork warnings. Numerical speedup refers to the exact scientific task at this input, not complete collision solver or full physical accuracy.

## 5. Run and verification

```bash
cd /home/cosmosapjw/rei_worktrees/hh-phys34-coding-20261015
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 scripts/phys33_moments.py \
  --workers 4 --screen-cells 8 \
  --output /tmp/new_unique_phys35_result.json
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src OPENBLAS_NUM_THREADS=1 pytest -q tests/
```

`scripts/phys33_moments.py` refuses overwriting its output; the SHA256 of the immutable `FROZEN_U_SUBSET.npz` is `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`. Parent PHYS34 commit and previous exact rational claims remain. Tests independently compare manufactured moments against mpmath160-digit quadrature, logarithm tails, negative inputs, source identity, serial-vs-parallel scientific identity, screening-cell monotonic improvement, dyadic endpoint jumps, and fast vectorized non-certified previews. Parent baseline tests still pass.

Actual cloud Wolfram15.0.1: original weighted moments and rational atanh formulas reduce to exact0, quantified screening inequality True. Local `wolframscript` and xAct/xTensor1.3.0: screened U conjugation, two exact integral identities and Euclidean Green tensor identity all exact0 after a pinned local CAS expression repair. Preserve the previous symbol-shadowing/errors separately; no native subagents and no external independent scientific review.

## 6. Cross-repo decisions and remaining science

Actual latest BASS_HE PR58 has completed second warm P01 cell with all photon carry; it remains physically separate from the one-centre/two-centre HH scattering continuum. bass_cr PR66 has proposed and tested SOURCE07 extended-energy threshold-safe cohort compression; its finite-energy RT and cross-section budgets cannot be imported as neutral H-H atom-rate calibration. Actual rei_bianchi AX07 conditional ZERO is completed, AX08 signed family in progress, AX11/12 pending; before any purported owner transition read current live STATE. This task does NOT use local Codex and does NOT launch/restart/modify the REI owner, active solver or queue. HH is OFF/nonblocking for cold IGM baseline; stellar source 50000K is not cold gas temperature.

**Remaining**: whole angular cross-term/source cancellation rather than triangle bound, origin r<r0, interface H^-1 distributions, full screened outgoing trace, continuous low Schur inf-sup and dual amplitude. Global two-centre thermal near-rate and P01 transmission remain `null`. Recommended next selected C7: `C7_COUPLED_SCREENED_ANGULAR_RESIDUAL_CERTIFICATION` with an actual interval-controlled angular/radial residual; reuse all completed rational-log moments and source identity. No main merge or production HH activation.
