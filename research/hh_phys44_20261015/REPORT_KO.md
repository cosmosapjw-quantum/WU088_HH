# WU088_HH PHYS44: Coulomb reference boundary and REI consumer source gate

2026-10-15 KST. Based on [PHYS43 draft PR82](https://github.com/cosmosapjw-quantum/WU088_HH/pull/82),
commit `20923b28cc74fde2548f50f663a1df2580f922a1`.
User goal: make *actual* WU088_HH scattering progress directly useful to
`rei_bianchi` while retaining the existing production OFF/scientific admission.
Selected incomplete task: origin/exterior outgoing boundary R5 + C5–C8,
plus focused consumer PHYS20 compatibility screening.
Only one bounded result is claimed, not full physical cross-section/rate.

## 1. Immutable physical model and competing provider lanes

Frozen spectator two-centre one-electron transformed Hamiltonian:
\[
h=-\frac12\Delta-\frac1r-(1+s^{-1})e^{-2s},\quad
s=|\mathbf r-R\hat z|,\quad R=\kappa=\frac7{10}.
\]
Length \(a_0=5.29177210544\cdot10^{-11}\,\mathrm m\);
energy \(E_a=2I_0=27.211386245980\,\mathrm{eV}\).
The atomic source \(I_0=13.605693122990\,\mathrm{eV}\) is
different from receiver heating \(\chi_H=13.598434599702\,\mathrm{eV}\).
Do not silently set \(c,\hbar,k_B=1\) for consumer conversions.
Physical electron-space is Euclidean; cosmological signature (-,+,+,+).

The original \(y\) variable obeys \(\eta=Fy\) with
\(F=e^{e^{-s}}\); the physical scattered correction is
\(\xi=Fy-\phi\) with \(\phi=e^{-r}/\sqrt\pi\).
Frozen 21 radial partial waves \(0\le\ell\le20\),
six actual IEEE-binary64 panels and 11 nodes/panel,
1386 complex128 original coefficients are unchanged.
Original SHA256:
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`.
The original \(r_0\) is the **binary64 exact rational**
\(\frac{7378697629483821}{73786976294838206464}\), not
the mathematical fraction \(1/10000\).

**Distinct project lanes:**
- PHYS43 is a microscopic two-centre frozen spectator scattering
  residual certificate, \(H^{-1}\) on \(r_0<r<20\), upper
  \(0.917114942873\). It does NOT supply \(\sigma(E)\), thermal
  \(k(T)\), a controlled solution error, or ionization rate.
- The older PHYS19 conditional FT03/LCS local HH gas-source response
  is a separate fixed-COMMON source/thermal model. Its temperature
  and electron response coefficients are not a substitute for a
  microscopic cross section and must not be silently transported to
  the live source-scoped AX08 chemistry history.

## 2. Exact central Coulomb outgoing reference theorem

At large \(r\), the *central* reference Hamiltonian
\(h_C=-\Delta/2-1/r\) has homogeneous radial equation
\[
u_\ell''+\left[\kappa^2+\frac2r-
 \frac{\ell(\ell+1)}{r^2}\right]u_\ell=0.
\]
Put \(\rho=\kappa r\), \(\eta_C=-1/\kappa=-10/7\).
The DLMF Coulomb outgoing wave is
\(H_\ell^{(+)}(\eta_C,\rho)=G_\ell+iF_\ell\).
Its exact reduced-radial Coulomb reference DtN is
\[
\boxed{z_\ell^C(r)=\kappa
 \frac{\partial_\rho H_\ell^{(+)}(\eta_C,\rho)}
 {H_\ell^{(+)}(\eta_C,\rho)},\quad\rho=\kappa r .}
\]
Recurrence (§33.4, NIST DLMF) gives
\[
\partial_\rho H_\ell^{(+)}
=\left(\frac{\ell+1}{\rho}+\frac{\eta_C}{\ell+1}\right)
 H_\ell^{(+)}
-\sqrt{1+\frac{\eta_C^2}{(\ell+1)^2}}\,H_{\ell+1}^{(+)} .
\]
The Wronskian (§33.2) is
\(\Im[\overline{H_\ell^{(+)}}\partial_\rho H_\ell^{(+)}]=1\),
so \(\Im z_\ell^C=\kappa/|H_\ell^{(+)}|^2>0\).
Consequently no real positive \(\rho\) has \(H_\ell^{(+)}=0\),
and the reference outgoing channel admits a regular finite-radius
logarithmic derivative without an unverified arbitrary phase.
This theorem is **central homogeneous Coulomb only**, NOT the
full noncentral screened exterior DtN.

Computational implementation:
`src/wu088_hh/phys44_boundary.py`, exact source readback through
`_physical_radial_data`, all \(\ell=0,\dots,20\) at \(r_B=20\).
One 22-wave special-function cache suffices for all 21
derivatives. mpmath arbitrary precision and local Wolfram
`CoulombH1[l,\eta,\rho]` use independent representations.
Examples (radius \(r_B=20a_0\), \(\eta_C=-10/7\)):
| \(\ell\) | \(\Re z_\ell^C\) (per \(a_0\)) | \(\Im z_\ell^C\) (per \(a_0\)) |
|---|---:|---:|
| 0 | 0.00210850167707212723 | 0.76799235802943506127 |
| 1 | 0.00191472741974421892 | 0.76474712999553541802 |
| 4 | 0.00001533411579252306 | 0.73492251295120085179 |
| 20 | -0.61556379959797260128 | 0.00163284699919638562 |

For the actual frozen **reduced y-mode** endpoint trace
(\(u_\ell,u'_\ell\)) the numerical quantity
\[
\left(\sum_{\ell=0}^{20}|u_\ell'(20)-z_\ell^C(20)u_\ell(20)|^2
\right)^{1/2}
\simeq 1.0006312403800173190391\times10^{-7}
\]
is a high-precision REFERENCE mismatch only.
The exact original physical outgoing \(\xi=Fy-\phi\)
includes noncentral lifting and screening, and may excite
\(\ell>20\). No full scattering boundary-error upper is
inferred from the small reference number.

## 3. Exact regular-origin Frobenius reference

For each fixed \(\ell\), regular *homogeneous central Coulomb*
\[
u_{\ell,\mathrm{reg}}(r)=r^{\ell+1}\sum_{n=0}^\infty a_{\ell n}r^n,
\quad a_{\ell0}=1,
\]
has the rigorous coefficient recurrence
\[
n(n+2\ell+1)a_{\ell n}
+2a_{\ell,n-1}+\kappa^2 a_{\ell,n-2}=0,
\qquad a_{\ell,-1}=0.
\]
For \(\kappa^2=49/100\),
\(|a_{\ell n}|\le 2^n/n!\) follows by induction because
\([1+\kappa^2(n-1)/4]/(n+2\ell+1)\le1\).
Writing \(z=2r_0\), the omitted state tail after degree \(N\)
satisfies
\[
T_N\le\frac{z^{N+1}}{(N+1)!}
\frac1{1-z/(N+2)}.
\]
For \(D=(\ell+1)\sum a_nr^n+\sum na_nr^n\), its
tail is bounded by
\[
(\ell+1)T_N+
\frac{z^{N+1}}{N!}\frac1{1-z/(N+1)}.
\]
Positive numerator/denominator enclosures then rigorously bound
\(u_{\ell,\mathrm{reg}}'/u_{\ell,\mathrm{reg}}\).
All 21 *archived* r0 traces are separately compared to these
reference intervals using exact dyadic coefficients.

**Scientific distinction:** the true original two-centre
near-origin equation contains a smooth noncentral screened term,
and its transformed/driven source may have an inhomogeneous
regular particular solution. These Coulomb-only Frobenius results
certify the **reference** and its mismatch to actual archived
trace, not a full physical origin extension.

## 4. Newly certified screened exterior and angular lift envelopes

For \(r\ge B=20>R=7/10\), \(s\ge r-R\).
The original *untransformed Hamiltonian* screening obeys
\[
0<S(s)=(1+s^{-1})e^{-2s}
\le(1+(r-R)^{-1})e^{-2(r-R)}.
\]
Thus in the radial equation, which contains \(2S\),
\[
\boxed{\int_{20}^{\infty}2\|S(r,\cdot)\|_\infty dr
\le\left(1+\frac1{20-R}\right)e^{-2(20-R)}
<1.813\times10^{-17}.}
\]
Exact Fraction bounds come from the positive-exp Taylor
192-term reciprocal enclosure, not finite-grid float quadrature.
**This is a radial \(L^1\) coefficient tail**, NOT an outgoing
Volterra resolvent perturbation bound, because no Green/inverse
operator norm is yet controlled.

Writing \(q_B=e^{-(B-R)}<1\) and
\(d_B=q_B/(1-q_B)\), we have
\[
|F-1| \le d_B,\qquad |\partial_r F|\le d_B
\quad (r\ge B),
\]
since \(e^{q_B}\le(1-q_B)^{-1}\).
The original \(y\) has only \(\ell\le20\),
and \(\phi\) has only \(\ell=0\). Therefore
\[
\begin{aligned}
\|\eta-y\|_{S^2}&\le d_B\|y\|_{S^2},\\
\|\xi-y\|_{S^2}&\le d_B\|y\|_{S^2}+2e^{-B},\\
\|P_{\ell>20}\xi\|_{S^2}&\le d_B\|y\|_{S^2}.
\end{aligned}
\]
Analogous radial derivative inequalities follow with
\(d_B(\|y_r\|+\|y\|)\) and an additional \(2e^{-B}\) for \(\xi\).
Using exact frozen partial-wave coefficients and directed sqrt
bounds at the archived outer endpoint:
- \(\|\eta-y\|_{S^2}\le1.0793018123\times10^{-10}\);
- \(\|\xi-y\|_{S^2}\le4.23023742610\times10^{-9}\);
- \(\|P_{\ell>20}\xi\|_{S^2}\le1.0793018123\times10^{-10}\).
These are actual original field **boundary trace** bounds,
not a bound on the \(\ell>20\) exterior solution or scattering amplitude.

## 5. rei_bianchi consumer source and authority check

The actual local owner checkout at readback is
`/home/cosmosapjw/Dropbox/bianchi/rei_bianchi`,
branch `codex/rux-science-delivery-20261014`,
HEAD `0fcb2dddf5de6b583c2e00f150abff0b2afb6315`.
The *latest public* independently stacked [rei_bianchi
PR125](https://github.com/cosmosapjw-quantum/rei_bianchi/pull/125)
head `7ac15b6078666d61c023103f79bfd47a033de41f`
is a DIFFERENT revision. No automatic semantic transfer of
private running AX08 data and accepted source clocks.

Actual owner files inspected read-only:
- `rust/rei_microphysics/src/coverage.rs`: `HH_R10`
  excluded and `require_physical_source` always returns
  `MissingAuthority("NO_EXTERNAL_PHYSICAL_SOURCE_ADMITTED")`.
- `axbi_sources.rs`: `MD14_Z002_FESC_BB50K_13P6_100_V1`
  photon emissivity source, not an HH collision-rate provider.
- `ft03_controlled.rs`: `REI_FT03_HG_RATE_MOMENT_CASE_A_CONTROLLED_V1`,
  separately scoped temperature-dependent H/He fixture.
- WU PHYS19 `NEXT_CONSUMER_CONTRACT.json`: the local
  consumer binding is unverified; source family and COMMON,
  rate coefficient, process owner, clock and density need binding.

Real read-only preflight:
`src/wu088_hh/phys44_rei_guard.py` and
`scripts/phys44_rei_guard.py`.
It attaches exact source SHA and current local Git identity and
fails closed on changed HH source authority; it NEVER mutates REI
or schedules science. Status is `HOLD`,
not `RATE=0` or `NOT_SUPPORTED_BY_PHYSICS`.

### Conditional same-family FT03 source algebra

Let \(f=n_{\rm He}/n_H\),
\(e=x+f(y+2z)\), \(\Pi=1+f+e\),
\(C_T=2/(3k_B)\) with thermal \(w\) in eV/H and
\(k_B\) in eV/K. Define \(T=C_Tw/\Pi\).
If, and ONLY if, the **effective identical-pair convention
corrected** rate \(\,k_{\mathrm{HH,eff}}(T)\) is admitted
in units cm\(^3\) s\(^{-1}\), the original PHYS19
local FT03/LCS channel states
\[
q_{\mathrm{HH}}=\lambda n_H(1-x)^2k_{\mathrm{HH,eff}}(T),
\qquad
\dot e_{\mathrm{HH}}=q_{\mathrm{HH}},\quad
\dot n_{e,\mathrm{HH}}=n_Hq_{\mathrm{HH}},
\]
\[
\boxed{\dot T_{\mathrm{HH}}=
 -\frac{C_T\chi_H+T}{\Pi}q_{\mathrm{HH}} .}
\]
All dots are *gas-frame proper seconds*, not a redshift
derivative or comoving density. This follows exactly from
\(T=C_Tw/\Pi\), \(\dot w=-\chi_Hq\),
\(\dot\Pi=\dot e=q\).
A raw collision pair average \(\langle\sigma v\rangle\)
would generally involve a symmetry factor \(1/2\) for
identical neutral reactants; this factor must be reconciled
with the original effective coefficient before use.
No rate coefficient is supplied by PHYS43 or by the verified
local consumer branch, and \(\lambda\) default remains OFF.

The unit test uses an **explicitly synthetic** manufactured
state \(n_H=10^{-4}\,\mathrm{cm}^{-3}, x=0.9,
k_{\mathrm{HH,eff}}=10^{-10}\,\mathrm{cm}^3\mathrm{s}^{-1}\),
\(\lambda=1\). It gives \(q=10^{-16}\,\mathrm{s}^{-1}\),
\(\dot n_e=10^{-20}\,\mathrm{cm}^{-3}\mathrm{s}^{-1}\),
and \(\dot T<0\). This is NOT a real AX08 or astrophysical HH
prediction, and the function rejects non-test application.
Exactly zero source at \(\lambda=0\), invalid fractions,
density, sign and coefficient are also tested.

## 6. Execution, CAS and performance

Local: Python 3.12.3, mpmath 1.3.0, NumPy 2.4.2,
SciPy 1.17.0, frozen original source SHA preserved.
`numpy==2.3.5` is the declared package pin, so the
real Ubuntu runtime is not claimed identical to pinned CI.

Actual 21-mode Coulomb numerical evaluation at 50dps:
- optimized one 22-function set + forward \(\ell\)
  recurrence 0.629 s;
- independent naive 21× `mp.diff` Coulomb evaluation
  4.781 s;
- microkernel speedup **7.60×** at 21 matched modes.
- Max complex log-derivative difference
  \(4.89\times10^{-39}\), with 38 published significant
  digits; this is below the explicit decimal
  representation acceptance \(10^{-36}\).
An initial benchmarking check demanded \(10^{-40}\) from
an only-38-digit serialized result, causing a preserved
`REPRESENTATION_PRECISION_CONTRACT_ERROR`. This was
diagnosed and fixed without changing physics or easing
an actual scientific tolerance.

At 72dps, original 21-mode/trace/evidence output is
identical between 1 and 2 `forkserver` workers after
excluding workers/time; process wall was **1.82 vs 1.93 s**.
For this tiny workload the **serial path is preferable**.
Neither speedup refers to the full native HH scattering
solver or the `rei_bianchi` physics/chemistry RHS.

Wolfram (actual local Kernel15) checks:
- selected \(\ell=0,1,4,20\) `CoulombH1=G+iF`
  and normalized outgoing Wronskian;
- **72/72 exact Frobenius recurrence scalar zeros**;
- exact exterior screening majorant integral residual 0;
- exact FT03 thermal Jacobian residual 0.
A separate Wolfram plugin call agreed at high precision
with Python/mpmath outgoing Coulomb log derivatives.

The new focused Python tests exercise original 1386
input identity, actual binary64 origin, Coulomb recurrence,
signed outward tail, 21-mode Wronskian, independent Wolfram
numbers, false promotion guards, source IDs, synthetic
stoichiometry and negative inputs. Actual targeted **25/25 PASS**.
The complete local project regression returned **264/264 PASS**,
pytest 171.04 s, exit0. The actual test stdout and resource
receipt are stored under `results/FULL_SUITE`.
This is verified on actual NumPy 2.4.2, not the 2.3.5
declared project pin.

An initial dps50 execution mislabelled the incoming 1s
contribution 2 exp(-B) as part of eta-y rather than xi-y.
Classification: FIELD_SEMANTICS_BUG, repaired, without changing
frozen physics. Its original bytes are preserved as
COULOMB_DPS50_INITIAL_SUPERSEDED_LIFT_LABEL.json and are
excluded from the accepted surface conclusions.
Corrected dps72 W1/W2 outputs are authoritative and
scientifically identical after omission of timing/worker data.


## 7. Literature and unresolved production gate

References:
- NIST DLMF [§33.2](https://dlmf.nist.gov/33.2)
  (Coulomb \(F,G,H^\pm\), Wronskians);
  [§33.4](https://dlmf.nist.gov/33.4)
  (log-derivative recurrence), independently followed
  by actual Wolfram `CoulombH1` numerical checks.
- Volkov, Yakovlev et al.,
  [Potential splitting approach to multichannel Coulomb
  scattering, arXiv:1102.0549](https://arxiv.org/abs/1102.0549).
  Its driven-equation/potential-splitting theory supports
  the **direction** of source/coulomb separation, but
  our two-centre outgoing inverse is NOT yet constructed.
- Hornyák & Kruppa,
  [Phys. Rev. A 85, 022702 (2012)](https://doi.org/10.1103/PhysRevA.85.022702).
  Exterior complex scaling addresses the long-range
  boundary problem; no hidden use of its result as our proof.

For an actual rei_bianchi HH source, still require:
(i) rigorous original \(\xi\) exterior Coulomb-plus-screened
DtN with actual noncentral \(\ell\)-coupling;
(ii) driven regular origin and matching at archived \(r_0\);
(iii) continuous limiting-absorption/low-Schur inverse and
incoming adjoint;
(iv) microscopic \(\sigma(E)\), correct flux/identical-pair
symmetry, threshold and Maxwellian thermal \(k(T)\);
(v) adopted `rei_bianchi` specific gas-frame
state/source/clock/closure/ownership and matched comparison
history. No rate, electron-source table, history or
temperature perturbation can be claimed for a live consumer
until the necessary selected conditions are verified.
The original production `HH_R10` remains OFF,
and all changes in this research phase are **WU088_HH-only**.
