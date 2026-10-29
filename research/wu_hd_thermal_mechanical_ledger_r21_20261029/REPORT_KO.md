# WU088_HH R21 | 원본 HD 반응률에 연결한 조건부 열·역학 장부

**2026-10-29; scoped research only.** Parent WU PR157 `52f9ff3213ac8f156bc47d610624cce061fdf485`; sibling R20 owner binding PR158 `1a5c6f47350da2b74e0b7e3071c4db3502810500`, not merged. Original source PDF 273554 bytes SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`, new runtime verified against restored source original. New scientific DAG delta **0**; WU **34/49**; native distinct-author R6/C9 **NOT_RUN**; scoped workflow **18/20**. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`.

## 새로운 이론 결과
The source-verified GL2022 single-channel 105→255 K nonautonomous exact exposure from R20 was preserved. Under fixed 4-state labels, prescribed positive v(t), externally specified temperature on source grid, and ideal classical translational mixture (3/2 kBT per particle, p=n_tot kBT), the chemical extent is `xi = Phi_A` with `A=int k(T)/v dt` and comoving total particle number conserved. If (and only if) source-matched species rest/rovibrational energies were supplied, define `Q_event=e_H+ +e_HD02-e_D+ -e_H201` J/event. Material internal energy `U=e·N+(3/2)Ntot kBT`, expansion work per reference volume `W_by=Ntot kB int T d ln v`, bath-incoming heat:

`Delta B = Q_event xi - (3/2)Ntot kB Delta T - Ntot kB int T d ln v`.

Proof in `THEORY_KO.md` includes H/D/charge/additive-gauge invariance, first law sign, T jump, theta→0, expansion/compression; Wolfram exact 8/8 identities (same-context CAS). R19's bath=Q xi is recovered only at constant T and constant v. This is a **conditional classical-translational auxiliary closure**, not the full molecular caloric equation or physical Q. The 2019 Lepers/Guillon/Honvault paper gives 39.5 meV ground-to-ground endothermicity (35.8 meV zero-point,3.7 meV isotope ionization), **not** the required state `(0,2)->(0,1)` Q; PES asymptote and proper state energies are still unbound.

## 새 구현과 관측된 검증
- `src/thermal_ledger.py` directly calls the R20 source-issued `NativeGrid/evolve_source_grid`, rejects wrong temperature/label/negative density/forged issuance. It emits coefficient `xi`, intercept `B_known= - DeltaU_trans -W_by`, plus signed W and thermal contribution. **Physical Q and bath heat JSON remain null**. Exclusive-create CLI and synthetic-only energy-gauge helper.
- Fresh Python `unittest`: **18/18 PASS** and **-O 18/18 PASS**. Source original PDF size/hash checked, no external owner code mutated. Initial test harness source path was wrong (0 tests executed due FileNotFoundError), corrected source layout and fresh full 18/18 PASS; not a physics failure.
- Independent mathematical implementation with mpmath80 **160/160 PASS**, max exposure relative `3.6372800767221244e-16`; max bath intercept relative `6.294038968081972e-16`; maximum bath intercept absolute `1.332794447668463e-28 J/ref m3`, max extent absolute `3.783655574710243e-09 /ref m3`. Not independent *author*.
- SciPy DOP853 **4/4 PASS** in fixed-source single-segment chemical+dilution+pressure work, max density absolute error `2.0489096641540527e-08 m^-3`, max mechanical-work error `3.944304526105059e-31 J/ref m3`. Reference atol 1e-8 densities, 1e-25 energy, rtol2e-12.
- Two diagnostic 101-point synthetic figures were rendered and visually inspected: chemical Q coefficient decreases with positive expansion, while known bath contribution equals `-theta*dt` after normalization for fixed T; Q heat is not plotted. Not an observed astrophysical heating curve.

## Exact source-nominal example and units
105 K then 255 K, 5e9s each, v=1, initial H+=HD=1e6/m3, product0:

`xi=660441.4261460102 events/ref m3`, `DeltaU_trans=+6.2129205e-15 J/ref m3`, `W_by=0`, `B(Q)=660441.4261460102*Q_J_per_event -6.2129205e-15 J/ref m3`.

The coefficient is from the source-verified **nominal** rate. The intercept is an ideal-translation model value. Numerical Q is **not supplied**. Neither interval source uncertainty, reverse rates, real bath history, net astrophysical heating, global tilt, full-A nor production integration is issued.

## Cross-repo provenance and source constraints
`CROSS_REPO_PINNED.json` lists actual WU PR157/158; REC PR156 (`8806a4f...`, nonreactive rotational HD), CR PR122 (`06503adc...`, He exact flow budget), REI PR263 (`f52ecdb...`, H/He UVB tau response), BASS PR244 and BASS_HE PR107. They do not certify a direct source-compatible 105 K four-state chemical consumer. This is a scoped checked-file conclusion, not an exhaustive all-branch absence theorem. No actual owner ACK was obtained. No foreign repo, parent PR or main changed.

## Decision
**`PASS_SCOPED_AFFINE_ENERGY_LEDGER`, `HOLD_PHYSICAL_Q_AND_OWNER`.** New theoretical work and code are reproducible in a source-locked auxiliary scope. Canonical 34/49 unchanged. Next useful step: independently authenticate the *exact state-to-state* source energy convention (including isotopic electronic asymptotic offset) and get explicit REC/CR owner ACK before code transport. Do not substitute ground-state 39.5 meV, LAMDA rotational photon-field mismatches, HE deuteron nuclear reaction or an interpolated rate for that missing event Q.

References: GL2022 *J. Chem. Phys.* 157 214302 DOI10.1063/5.0128598; Lepers/Guillon/Honvault *MNRAS* 488 4732 DOI10.1093/mnras/stz1797. See exact PDF/coordinate/token source in inherited R18/R20.
