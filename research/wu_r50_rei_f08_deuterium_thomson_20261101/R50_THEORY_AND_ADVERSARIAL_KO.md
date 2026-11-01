# WU R50 | REI original F08 S0 Thomson sky: passive D+ electron ceiling

Date: 2026-11-01. Science status: DERIVED; NUMERICALLY_CHECKED; IMPLEMENTATION_VERIFIED_SCOPED; NOT_CANONICALLY_ADMITTED.

## Protected physical source

WU parent Draft PR188 HEAD f5d09daf5e70baa964aadda2156cd61facf495c4; read-only REI owner Draft PR349 HEAD 58f7ffb685c3758f1fed1113ff8134a24478c3df; original F08 source pair SHA256 0a2bec874a5aa1b12f882033a08497b913b44447148b50b6082093bb354868e8. Five archived public source inputs matched their exact SHA256/Git blob locks. Two distinct, paired S0 proper electron histories have 16,001 samples each. One 10,752-ray F08 photon observer source output. Original F08 remains a prescribed, homogeneous S0 Bianchi/FLRW model with scientific_admission HOLD, NOT the separate original 46,080-cell, 26-event F05 history. S0 background reference_z0=10 is not the redshift relative to the present observer. The four observer-relative redshifts are episode-relative.

## Exact conditional theorem

Use (-,+,+,+), c=2.99792458e10 cm/s, sigma_T=6.6524587051e-25 cm^2 and proper time t. The original frozen one-cell background has scale factors a_i=exp(H_i*t), H_i=(1.01,0.99,1)*1e-14 /s, Hbar=1e-14 /s, t_o=1e13 s, n_H0=1e-4 cm^-3, and exact n_H(t)=n_H0 exp(-3 Hbar t).

Assume deuterium is a nonbackreacting passive tracer with 0 <= n_D+(t) <= eta_D n_H(t) and eta_D=2.5e-5, the declared fiducial *maximum scenario assumption* inherited from WU R49. eta_D is NOT a measured upper confidence limit and n_D+(t) is NOT evolved here. At a source F08 sky ray's original emission proper-time t_e(n,z_rel),
\[
0 \le \delta\tau_D(n,z_{\mathrm{rel}}) = c \sigma_T \int_{t_e}^{t_o} n_{D^+}(t) dt
\le c \sigma_T \eta_D n_{H0} \frac{e^{-3\bar H t_e}-e^{-3\bar H t_o}}{3\bar H} =: \tau_D^{\max}(n).
\]
The equality case has every D nucleus ionized at every point of the ray, and is a ceiling, not a chemical prediction. The units of c sigma_T n_D dt are dimensionless.

The original source F08 differential Thomson visibility g0 at fixed relative z has, under this passive extension,
\[
g_D/g_0 = (1+n_{D^+}(t_e)/n_e(t_e))\exp(-\delta\tau_D),
\qquad
\exp(-\tau_D^{\max}) \le g_D/g_0 \le 1+\eta_D n_H(t_e)/n_e(t_e).
\]
For sky mean-centering C and equal-area positive-weight norm, the reverse triangle inequality and C's orthogonal-projection contraction give
\[
|\|C(\tau+\delta\tau_D)\|_2-\|C\tau\|_2|
\le\|C\delta\tau_D\|_2\le\|\delta\tau_D\|_2\le\max_n\tau_D^{\max}(n).
\]
The last ratio compared with the original source's nonzero geometric sky RMS is a conditional screen, not a general no-go theorem.

## Numerical science from original F08 data

All 10,752 model ray rows were re-evaluated; 12 groups from 4 relative-z windows and grids 8x16,16x32,32x64. On the primary 16x32 grid:

| z_rel | maximum extra tau_D | maximum perturbation RMS bound / original geometry RMS |
|---|---:|---:|
| 0.0253151205 | 9.687433970420443e-11 | 0.004333082571748222 |
| 0.0512710964 | 2.013709242790594e-10 | 0.004206500874411025 |
| 0.0778841509 | 3.140894836318601e-10 | 0.004096644388759257 |
| 0.0996588551 | 4.1061720261278543e-10 | 0.0040457501229315355 |

Across all 12 groups max relative perturbation to geometry RMS 0.004333894375530609 (0.433389%); max added optical depth/source optical depth 2.319289505716654e-5; maximum relative emitter electron-density increment 2.3810448438113965e-5. Full-ion template (not universal bound on anisotropic D ionization) last primary-window Qxx = -3.5659369141195043e-13, original F08 geometric Qxx approximately -2.615836400571423e-8.

Exact original source n_H volume law and 16,001-row paired n_e histories checked. Independently reconstructed original source sky tau at ALL 10,752 rays (max relative difference 0 at binary64) and emitter n_e (max rel difference 1.5619430906312492e-16). 12/12 Python tests in normal and optimized modes, source-tamper negative test, self-adversarial all-ray scan, independent 60-decimal-digit calculations at 26 ray witnesses (max relative difference 3.345225263695717e-16), and four-file clean replay byte-exact PASS. Different-author referee NOT_RUN; no native subagent.

## Hostile scientific review / watchdog

1. eta_D is an assumed cap, not an observational deuterium upper limit. Removing this assumption removes the numerical claim.
2. Only free-electron Thomson opacity is constrained. Deuterium photoionization, resonant radiation, chemical heating, and HD molecular cooling are separate and NOT excluded.
3. The fully ionized D template is not chemically derived, and n_H, n_e, metric, S0 photon transport and feedback are deliberately kept fixed. In a fully coupled H/He/D system the theorem does not bound feedback.
4. The F08 original observer is a prescribed one-cell numerical scenario. Its relative redshift is NOT the cosmological present-day redshift. Original REI F09 provider domain overlap remains blocked, F05 [160,161] remains blocked.
5. Geometric RMS is the original F08 Bianchi source-sky RMS. The <=0.434% conclusion pertains only to this explicitly frozen model and the extra D electron term, not to all Bianchi histories or real CMB inference.
6. Original sky was sampled with piecewise-linear n_e(t) and numerical angular quadrature, not interval-enclosed continuum Thomson histories. n_H(t) analytic bound is exact for the frozen exponential source prescription only.
7. 10,752 rays are deterministic numerical directions, not independent observations. No WU or REI canonical node can be promoted from this screen.
8. Positive stop decision: under the conditional source and cap, D-electron Thomson perturbation is sub-percent of the specified Bianchi geometric-sky RMS. Further WU isotope-electron opacity atlases for *this* S0 observer are scientifically unnecessary without a new actual source consumer or physical scope.

## Scientific gate and next owner action

WU canonical 34/49 (+0); REI central 28/88 (+0); REI working 33/88 (+0); Fast 4/7 (+0). F05 source accepted tick160/131072 and [160,161] HOLD. F08 scientific admission HOLD, F09 external source domain binding BLOCKED. This WU R50 is original REI-observer source-conditioned physics, not a new original ionization IVP, no original repo edits, no main merge, no production. Next CORE task is REI owner PR351 physical three-lane source/admission decision and then genuinely source-matched coupled H/He+photons+Bianchi observable. WU additional isotope microphysics should wait until a named receiver demonstrates a physical effect beyond its error budget.

HH_R10=OFF; REI_L4=false; NO_MAIN_MERGE; PRODUCTION=HOLD; AUTO_NEXT_NODE=false.
