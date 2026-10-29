# WU088_HH R22 | source-typed state-specific reaction energy cross-paper calibration

2026-10-29 KST. Research unit `WU_HD_2021_2019_ENERGY_SOURCE_RECONCILIATION_R22` (auxiliary, not canonical science node). Parent WU PR159 immutable `fd351d0ff97ef0d7a9cf710bdecad922af7e885e`; sibling PR158 `1a5c6f47350da2b74e0b7e3071c4db3502810500` is not merged. Original GL2022 source PDF 273,554 B SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754` source-verified. Canonical DAG 34/49, production NOT_ISSUED, HH_R10 OFF, L4 false. Distinct-author R6/C9 NOT_RUN.

## R1–R3. Exact question and literature authority

The locked *ionic* selected channel is

\[H^+ + HD(v=0,j=2) \longrightarrow D^+ + H_2(v'=0,j'=1).\]

Its source-native SQM rate at **exact 105 K** is `1.15e-16 m^3 s^-1` (Table 2, row (0,2), column 105 K), already verified in R18 and used in R19–R21. Rate **is not** reaction heat. Its true physical uncertainty, source scattering energy-zero and compatible full-A consumer are not issued. No extra 3/4 spin or Boltzmann p₂ population weight is applied.

Primary donor I, **Lepers, Guillon & Honvault (2019), MNRAS 488 4732, DOI 10.1093/mnras/stz1797, Introduction** explicitly gives a *ground-to-ground* endothermicity of **39.5 meV** for HD(0,0) → H₂(0,0), split into 35.8 meV zero-point difference and 3.7 meV hydrogen/deuterium ionization-potential difference, all as rounded literature figures. Their Born–Oppenheimer scattering excludes the ionization-potential offset and reports a ~3 meV energy-scale omission. This is not GL2022's state (0,2)→(0,1), and neither 3.7 meV nor printed 39.5 meV is an authenticated exact Q or an error interval.

Primary donor II, **Zhou et al. (2021), MNRAS 507 6012, DOI 10.1093/mnras/stab2381, Table 2** provides printed level energies for a **neutral H+HD** scattering system, not the GL2022 **ionic H⁺+HD** process. For the four specified levels, the source text reads

| molecule/state | 2021 printed E (eV) |
|---|---:|
| HD(v0,j0) | `0.2344204966` |
| HD(v0,j2) | `0.2675344527` |
| H₂(v0,j0) | `0.2702721432` |
| H₂(v0,j1) | `0.2849632856` |

These are printed neutral-diatom level values from a separate PES. Their *literal decimals* are exactly decoded by `Decimal`, but the true physical energies are not exact decimals. GL2022 uses the Velilla ionic H₃⁺ ground-state PES; a separate 2021 neutral-reaction PES cannot be silently declared source-identical. The 2022 article's Fig.1 displays an energy-level diagram but, without independently authenticated model-specific asymptotic numerical levels/energy zero, a precise GL2022 state-specific Q is not admitted.

## R4–R5. Constructive derivation and three *competing*, conditional conventions

Set \(\epsilon_{HD,j}=E[HD(0,j)]-E[HD(0,0)]\), \(\epsilon_{H2,j}=E[H_2(0,j)]-E[H_2(0,0)]\). For any consistently defined ionic ground-channel endothermic threshold \(\Delta_{00}\), the *same-convention* state-specific threshold is the identity

\[\Delta_{21}=\Delta_{00}-\epsilon_{HD,2}+\epsilon_{H2,1},\qquad Q_{21}=-\Delta_{21}.\]

Here positive \(\Delta\) means endothermic; positive Q means energy released to the environment. It is a mathematical identity of asymptotic state energies, provided the reference energies share an energy zero/PES/mass convention.

From the **separate neutral donor**, exact printed-decimal arithmetic yields

\[\epsilon_{HD,2}=0.0331139561\,\mathrm{eV},\quad \epsilon_{H2,1}=0.0146911424\,\mathrm{eV}.\]

There are three diagnostic constructions, **none** admitted as GL2022's physical Q:

1. **2021 neutral-only printed level difference:** \(\Delta_{21}^{\rm neutral}=0.2849632856-0.2675344527=0.0174288329\) eV.
2. **2019 rounded ground threshold + 2021 neutral rotational increments:** \(\Delta_{21}^{\rm mixed,A}=0.0395-0.0331139561+0.0146911424=0.0210771863\) eV.
3. **2021 neutral level difference + 2019 rounded ionization offset:** \(\Delta_{21}^{\rm mixed,B}=0.0174288329+0.0037=0.0211288329\) eV.

Their A/B difference is \(0.0000516466\) eV = **0.0516466 meV**. Its exact decomposition

\[\Delta_{21}^{\rm mixed,B}-\Delta_{21}^{\rm mixed,A}= (E_{H2,00}^{2021}-E_{HD,00}^{2021})+\delta_{IP}^{2019}-\Delta_{00}^{2019}\]

identifies the origin as a cross-paper *baseline and rounding discrepancy*. It is **not** a symmetric confidence interval, a rate uncertainty, an upper bound on physical Q, or a model/PES error certificate. No assertion about actual GL2022 endothermicity sign is admitted from this mixture alone.

## R5 continuation. Transport to R21 without physical admission

The R21 exact source-derived comoving extent \(\xi\) and caloric intercept \(B_0=-\frac32N_{tot}k_B\Delta T-N_{tot}k_B\int T\,d\ln v\) yield a **conditional** affine function

\[B^{\rm diagnostic}(Q)=B_0+Q\xi,\quad \partial B/\partial Q=\xi.\]

With the *synthetic* R21 schedule 105 K and 255 K for 5e9 seconds each, v=1 and initial H⁺=HD=1e6 m⁻³, \(\xi=660441.4261460102\) events per reference m³; \(B_0=-6.2129205\times10^{-15}\) J per reference m³. The three cross-paper candidates give only model-conditional \(Q\xi\) of about `-1.84422e-15`, `-2.23027e-15`, `-2.23573e-15` J/ref m³, respectively. Those are *not physically predicted heating values*. Main JSON continues to contain `physical_Q: null`, `physical_bath_heat: null`, `source_uncertainty: null`.

Energy gauge invariance: for \(\nu=(-1,-1,+1,+1)^T\) the H, D, charge, and total-particle covectors each annihilate \(\nu\), hence \(Q=-\boldsymbol e\cdot\nu\) is invariant under any corresponding additive per-species reference energies. It does not reconcile different PES donor asymptotes without a physically justified energy zero.

## R6–R8. Scope-matched checks and adversarial alternatives

- Wolfram exact rational 9/9 verifies thresholds, difference identity, H/D/charge/particle covectors and gauge invariance; same-context symbolic verification, not an independent author.
- R22 Python tests detect source DOI, selected quantum state, temperature/method, source-PDF SHA, original rate and physical-null violations. Initial test actually found that altered reaction labels were incorrectly accepted; an exact state-label+DOI identity guard repaired it. Final 26/26 normal and `-O` run PASS.
- mpmath80 160/160 uses an independent inverse integral/bisection method for the R21 mass-action extent; max extent absolute difference `5.061769788523247e-11` events/ref m³. Cross-paper energy arithmetic is separately exact in printed decimal input. Alternative numerical methods are not different-author review.
- Two synthetic figures were generated and visually inspected; a lower-left legend hiding the Q-independent affine bath line was repaired. The bars are not probabilistic uncertainty bands.
- Strongest counterargument: 2021 neutral scattering levels and the 2019 *ionic* ground ionization offset are not known to share GL2022's asymptotic state Hamiltonian. Accordingly, **physical-source qualification is blocked**, not theoremically impossible. Conditional algebraic and implementation claims survive within that boundary.

## R9–R10. Computational contract, scientific disposition

`src/cross_paper_energy.py` retains a strict `source/CROSS_PAPER_LITERALS.json` typed literal transcription with DOI and state labels, exact decimal arithmetic, source code guard and a read-only call of the original R18→R21 source-verified flow. It creates three disjoint labeled cross-paper diagnostic rows, each `qualified=false`, `uncertainty=null`, and keeps `physical_Q_event=null`, `physical_bath_heat=null`, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`. Actual raw 2021 journal source bytes are not locked; the literal transcription's SHA is **our content identity only**. It must never be used as proof of original-byte source provenance.

Accept the analytic decomposition and testable numerical firewall only: **PASS_SCOPED_CROSS_PAPER_CALIBRATION / HOLD_GL2022_PHYSICAL_Q**. Maintain canonical WU **34/49** and physical consumer **NOT_BOUND**. Next smallest physical input is a **same-PES/source-native ionic HD(0,2), H₂(0,1) asymptotic energy and ionization convention** with version, raw identity, uncertainty and owner review. Reverse rate, actual bath coupling, rate uncertainty, full-A and production are separate obligations.

Primary URLs: https://doi.org/10.1093/mnras/stz1797 ; https://doi.org/10.1093/mnras/stab2381 ; https://doi.org/10.1063/5.0128598 .
