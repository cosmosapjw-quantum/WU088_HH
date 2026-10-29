# WU088_HH R24 | GL2022 exact-row Maxwell–Laplace threshold-support audit

2026-10-29 KST. Scoped theory-first result, independent of physical promotion.
Parent **WU PR162** exact HEAD `2f214319ca8600475b1d4e85d1ca21a0249136a8` (R23 molecular-ionization cycle); read-only sibling WU PR160 `9db6f91debf54af1cc129538cfd6f6a716a78a56`. No main/parent/REC/CR/REI mutation. Central science DAG **34/49 unchanged**. Native distinct-author R6/C9 **NOT_RUN**. HH_R10 OFF, L4 false, production NOT_ISSUED.

## R1–R3. Exact original channel and source identity

The sole source-locked target is the **ionic** reactive single channel

    H+ + HD(X,v=0,j=2) -> D+ + H2(X,v'=0,j'=1,ortho).

GL2022: González-Lezana, Hily-Blant & Faure, *J. Chem. Phys.* **157** 214302 (2022), DOI [10.1063/5.0128598](https://doi.org/10.1063/5.0128598), equation (4) and Supplement **Table 2**. Original CSIC supplement PDF 273,554 bytes SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`; R21 source ZIP SHA256 `5ace176fdba1b1ed01cedbd11e381b98ee242475ef1a401d89dcfcf0b7a3d220`. The original R18 native parser Git blob `be2a845263b215b604f255ffe5deabe55be9dd7b` was byte-verified, imported, and executed. Table 2 notation `3.99(14)` means **3.99 × 10^(-14) cm³/s**, not a statistical ±14. All ten original temperature nodes and raw tokens are kept; no extra 3/4 nuclear-spin factor, p2 Boltzmann factor, interpolation, fabricated rate uncertainty, or reverse reaction is allowed.

GL2022 Sec II reports the ground-electronic-state **H3+ Velilla2008 PES**: Velilla, Lepetit, Aguado, Beswick & Paniagua, *J. Chem. Phys.* **129** 084307 (2008), DOI [10.1063/1.2973629](https://doi.org/10.1063/1.2973629). Their reported electronic/dissociation arrangement value 37170 cm^-1 is **measured from the H3+ electronic potential minimum**, not the isotopic state-specific HD(0,2)→H2(0,1) reaction threshold. The source-native entrance/exit rovibrational eigenenergies, nuclear masses and isotope ionization-potential offset used in the 2022 SQM rate are not yet authenticated in original input bytes.

Lepers, Guillon & Honvault (2019), *MNRAS* **488** 4732, DOI [10.1093/mnras/stz1797](https://doi.org/10.1093/mnras/stz1797), §3.2 explicitly give an approximately **3.4 meV BO/TIQM** endothermic threshold for **HD(0,2)→H2(0,0)** while neglecting the H/D ionization difference. That is a different final J, a different scattering implementation, and not a numeric GL2022 SQM energy certificate. The R23 external spectroscopy threshold +20.95002099384045759056749544382632657967 meV is separately source-typed and explicitly **not** admitted as the GL2022 PES-native threshold.

## R4–R5. Constructive conditional literature transport

For a fixed common asymptotic energy reference, define Δ₍₂→₁₎=Δ₍₂→₀₎+ε_H2(0,1)-ε_H2(0,0), with positive Δ endothermic and Q_release=-Δ. Inserting **2019 rounded different-channel BO threshold** 3.4 meV and external H2 rotational separation 118.48684 cm^-1 yields the deliberately mixed-source diagnostic

    Δ_mixed,approx = 18.09049588228285015972265140398995 meV.

The external R23 molecular-ionization spectroscopic threshold is 20.9500209938404575905674954438263 meV, hence their cross-source discrepancy is 2.8595251115576074308448440 meV. It is **not** an uncertainty bar or GL2022 energy zero. Under a pure shifted-shape toy assumption Eσ_D(E)=g(E-D)1[E≥D], the Maxwell–Boltzmann rate ratio for a rigid ΔD is exp[-ΔD/(k_B T)]; actual GL2022 temperature-dependent scattering shape is unknown, so toy shifted rates must never overwrite the ten source nodes. Earlier nine adjacent *p=0* Arrhenius effective barriers vary from -12.38549830 to +26.06622710 meV and thus cannot be interpreted as one PES threshold.

### New stricter source-grid lemma: positive Maxwell–Laplace support bound

**Assumptions.** There is one fixed entrance state, one temperature-independent and measurable **nonnegative** state-resolved cross section σ(E), with E the entrance **relative collision kinetic energy** (E≥0). It vanishes below a common endothermic opening threshold Δ≥0, and its thermal rate obeys the standard Maxwell–Boltzmann two-body convolution with fixed reduced mass μ,

    k(T)=sqrt(8/(π μ)) β^(3/2) ∫_Δ^∞ E σ(E) exp(-βE) dE, β=(k_B T)^-1.

All integrals are finite/positive at the two temperatures used. No assumption is made about resonance shapes, partial waves, energy smoothness, or monotonicity of σ above threshold. Define F(β)=k(T) β^(-3/2)/sqrt(8/(πμ)) = ∫_Δ^∞ Eσ(E)e^{-βE}dE. For β_c>β_h, **pointwise on E≥Δ**,

    e^[-(β_c-β_h)E] ≤ e^[-(β_c-β_h)Δ].

Multiply this by Eσ(E)e^{-β_h E}≥0 and integrate. Then

    F(β_c)/F(β_h) ≤ exp[-(β_c-β_h)Δ]

and, after taking logs, the necessary support bound is

    Δ ≤ k_B ln[k(T_h)T_h^(3/2)/(k(T_c)T_c^(3/2))]/(1/T_c-1/T_h).

The upper bound is optimal in the class of nonnegative finite spectral measures: a monochromatic Dirac spectral measure concentrated at E=Δ saturates it, while ordinary narrow positive functions approach equality. This is a limiting mathematical sharpness statement and not a physical single-resonance cross section.

This proof is direct from **positivity and a common collision-energy zero**. It is not a universal prohibition against different SQM implementations, varying cross sections, nonthermal incoming beams, or a different interpretation of the paper's energy variable. Constant state nuclear-spin multiplicities cancel in this *ratio* but thermally averaged **initial-state populations** would not; the source row is state-specific.

### R6–R7. Actual source-grid evaluation and robustness

Original Table 2 prints at 15 K `3.99(14)` and 55 K `2.92(11)` in cm³/s, hence the immutable native SI rates are 3.99×10^-20 and 2.92×10^-17 m³/s. With exact SI k_B and e, their **nominal necessary threshold upper bound** is

    Δ_max(15,55)=15.18630382175889727368776395345 meV.

Treating only the printed **three-significant-digit mantissas** as rounded ±0.005, not as source uncertainties, the favorable extremal pair 3.985×10^-20 and 2.925×10^-17 gives a conservative printed-digit upper bound 15.19157320477320978458 meV. The other eight adjacent-temperature bounds are larger, so the first pair controls all-pair necessary bound. The mixed 18.0904958823 meV candidate would require a low/high source Laplace ratio at least **5.124455180... times smaller** than the actual printed ratio. The external 20.9500209938 meV candidate requires at least **25.608308931... times smaller**. This is a **conditional input-vs-hypothesis feasibility failure** under the lemma, **not** an empirical or direct PES-native Q value, not a certified error in GL2022's algorithm, not a physical rate uncertainty, and not a new strong general no-go theorem.

Additional caution: the low-T original rate is a printed SQM numerical result. Published cross-section values, collision energy reference/threshold, interpolation and finite integration cutoff may affect whether all lemma assumptions apply **exactly** to the published numbers. This comparison is not a direct reconstruction of the original cross section or a demonstration of a numerical bug. To close the gap, reconstruct source-native E, E_HD02, E_H201, mass convention and isotope asymptote and the raw 15/55 K cross-section quadrature. Do not retroactively treat an unrelated model's quoted 3.4 meV as GL2022's internal energy.

## R8–R10. Computation and scientific decision

`src/threshold_audit.py` verifies original R21 PDF SHA and R18 native parser Git blob, reads **all ten** original T/rate tokens, preserves exact source `Fraction`s, evaluates all nine model-free adjacent pair support inequalities and the printed-digit limit using `Decimal(70)`, checks the toy-multiplier and p=0 surrogate separately, and retains explicit Q/bath/reverse/owner NULLs. Negative source identity tests check DOI, state, source rates, quantum labels, PES identity, mass/IP admissions and DAG/production gates. Independent C++20 long-double implementation and Wolfram high-precision arithmetic reproduce the pair bound and both violation factors, without constituting a distinct-author review. Synthetic plots are source diagnostics only.

**Decision:** `PASS_SCOPED_ORIGINAL_RATE_LAPLACE_SUPPORT_BOUND / HOLD_GL2022_NATIVE_PES_THRESHOLD`. Canonical 34/49, physical delta 0, R6/C9 distinct-author `NOT_RUN`, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`. Physical `Q_event`, physical bath heat, reverse rates, numerical physical rate uncertainty, full-A, owner REC/CR binding all remain NULL/held. The next physical research input must be *original same-PES state-specific channel asymptote energies plus the actual scattering-energy convention and low-T source quadrature*, not another external-model guess.
