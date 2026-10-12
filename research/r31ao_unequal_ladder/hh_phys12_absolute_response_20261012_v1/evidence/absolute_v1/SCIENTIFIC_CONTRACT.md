# PHYS12 — fixed-family absolute future-HH response

Frozen before the new arithmetic run, 2026-10-12. This executes L0–L3 of
PR45 (`78536cbaab84601ba93e62c0d47debc1c5dd2953`).

## Question and scope

For each archived first-stage family and each one fixed admissible coefficient
tuple alpha, evaluate D_HH O(1)=O(1,1;alpha)-O(0,1;alpha), O=x_HII,w.
The switches are future LCS HH strength lambda and future photon-birth amplitude
b_amp, both dimensionless. COMMON, historical HH, compensation and pre-existing
photons remain fixed. b_amp=0 does not remove pre-existing photons. The fixed
family may differ between full (1.25e9 s) and first_half (6.25e8 s); these are
separate first stages, not a sequential history or convergence pair.

## Source and mathematical premises

Reuse PHYS09 PROJECTED_RESULTS from PHYS11 without source, root, inverse or
historical-suite replay. SHA256 is
c6329fed8c411e1592bd1a0c63ebd9ca6151e81500ed1f46fb6b40f4b7758444;
Git blob is 9dd38e85bd52aa5d9e367a84413b3c531272f0fe.
The inherited source-inclusion/open-C2 premise and the adopted uniform Banach
certificate give one C2 real-source root family over [0,1]^2, at each fixed
alpha. U=partial_lambda g encloses derivatives on this whole rectangle.
This run checks correct premise application and exact saved endpoint arithmetic;
it does not reprove the original interval producer or issue native root authority.

For G=g-g_old-d F=0, A=G_g, A U=-G_lambda=d H, with
H=q(1,0,0,-chi_H), q=nH_proper(1-x_HII)^2 k_LCS(T).
No new factor 1/2 is applied to the selected closure. nH is cm^-3 and k is
cm^3/s, so q is per H nucleus per proper second; chi_H is eV, w is eV/H.
Constants c, k_B and eV-to-erg conversion retain the original source roles.
The metric signature is (-,+,+,+), but no metric operation is needed here.
The other microscopic singlet H+ / H- channel is outside this LCS response.

## Derivation and outputs

D_HH O(1)=integral_0^1 U_O(lambda,1) d lambda. Since the interval length is
exactly one, the inherited uniform U interval is also a finite on/off enclosure.
This is a finite response in the discrete implicit stage, not a linearization
at lambda=0 and not a continuous-time solution.

Retain the previously computed mixed interaction I_O=D_HH O(1)-D_HH O(0)
with explicit REUSED attribution. If the signs exclude zero, optionally report
-I_x/D_HH x(1) and I_w/(-D_HH w(1)): relative modulation of the HH response
by the selected extra photon birth. They are not HH omission criteria or global
efficiencies. All ratio denominators are at b_amp=1.

## Arithmetic, acceptance and stop

Read original exact rational endpoints; verify their outward binary64 displays
and bit identities. New arithmetic uses Python Fraction. No floating subtraction
of four large corner values, endpoint clipping, symmetrization, changed precision
or tolerance is allowed. Output exact endpoints and outward decimal intervals.
For each primary interval the result must equal the selected U enclosure times
the exact lambda length; all input bytes must remain unchanged. Positivity or
negativity is an outcome, not a prerequisite; zero-containing is reportable.
Use a small analytic competing-channel family, a nonunit-interval FTC case, and
a changed-alpha counterexample to check semantic distinctions. These fixtures
are not substitutes for the archived physical inputs.

One new exact-arithmetic run: <=30 s wall/CPU, <=384 MiB address space, <=16 MiB
per file; preserve raw stdout/stderr, exit, wall/CPU/RSS and source/code identities.
Repair only an observed concrete failure under the same contract. Figure creation
uses saved results and does not constitute another source/science solve.
Stop after L2 answers the bounded question and independent noncreator review;
do not refine merely to reduce an already sign-definite interval.

## Evidence and limitations

Use derived / numerically checked / implementation-verified separately.
The inherited enclosure contains coefficient-domain dependence, interval dependency
and the original linear-inverse remainder; it is not a statistical confidence
interval or an identified pure numerical error bar. This transfer introduces
zero rational arithmetic error and explicit outward display rounding. Closure
uncertainty, astrophysical uncertainty, time/continuum error are not quantified.
Consumer-significance tolerance remains unspecified. No cosmological negligibility,
actual native root/U/V/W/I, carried second_half, global conservation, full49 or
production claim is made. Existing failures remain preserved in the parent.

## Delivery and execution location

All short work is performed HERE. Current NCP heavy_queue=[] and launch=false.
Prior user authorization covers additive WU088_HH branch/PR publication and
existing Drive/Dropbox backups; no main merge or third-party message is included.
Root owns candidate generation and integration. A separate noncreator reviews
the frozen inputs/code/results/interpretation and owns any PROMOTE_SCOPED decision.

Host label is GPT-6 Astra Pro; the exact Pro alias is absent from the router.
Continue the previously selected, hash-verified Astra v4 workflow; do not claim
backend attestation or a model switch.
