# WU R33 | Source-qualified CMB radiation × H⁺–HD(v=0) chemistry before restricted exchange

2026-10-30 KST. Parent WU PR #171 exact HEAD `320b3a7252b0bb9fe8b3cbdb40f816545a33bed1`. Science source from **exact** original parent R32 SOURCE ZIP and the original R29 native source tokens, using R30 Sung et al. four fitted HD rotation line centers. The R33 unit does not modify parent, full astrophysical chemistry or production.

## Problem and source contract (R1–R3)

The R29 five-HD-state transient \, \(\mathrm{HD}(v=0,J), J=0,\dots,4\)\, includes (i) source-computed González-Lezana et al. 2022 H⁺-HD inelastic downward rate coefficients at seven printed temperatures, (ii) 2022 SQM source-computed restricted H⁺+HD→D⁺+H₂(v'=0,J'=0..9) rates, and (iii) REC161 independently transcribed, **not original bytes**, Leiden2021 Einstein A values J→J−1. Upward collisional rates are *derived* from detailed balance using the original CDMS2011 v2 **rendered** level information. R30 replaced only the rotational ladder with four 296-K Sung fitted line centers. In the R33 extension all existing reaction and collision rate tokens and the physical density policies remain unchanged. The line centers are not a full laboratory covariance or a temperature-dependent pressure shift.

The independent external Planck radiation temperature is \(T_r=T_0(1+z_r)\), \(T_0=2.7255\,\mathrm K\), at \(z_r\in\{0,5,10,30,100,300\}\), plus the **formal** no-radiation limit \(T_r=0\). At each source-exact \(T_g\in\{55,105,255,505,1005,2005,3005\}\,\mathrm K\), two original R29 spin policies, three source-defined n/ncrit(J2) ratios (0.1,1,10), and five initial J values are used. This is **not** a self-consistent mapping of redshift to gas density, gas temperature, proton abundance, HD abundance, or cosmic history. High z at low T_g is allowed only as a prescribed-boundary experiment.

## Generator, radiation, energy and event definitions (R4–R5)

Let \(C_{ij}\) denote original source-qualified collisional transition rates (s⁻¹) from level j to i after multiplying the original rate coefficient (cm³/s) by prescribed n(H⁺) (cm⁻³). Let \(Q_{\alpha j}\) denote the restricted chemical absorption rate to H₂ final J'=α. Let \(A_j\) be original transcription for spontaneous downward j→j−1 and \(\Delta E_j=h c\tilde\nu_j\), where c is SI and \(\tilde\nu\) is a wavenumber converted from cm⁻¹ by a factor 100. Define the Planck photon occupation

\[\bar n_j(T_r)=\frac{1}{\exp(\Delta E_j/(k_B T_r))-1}.\]

At prescribed isotropic external Planck intensity, the **radiative transitions per second** are

\[R_{j-1,j}^{\downarrow}=A_j(1+\bar n_j),\quad R_{j,j-1}^{\uparrow}=A_j\frac{2j+1}{2j-1}\bar n_j.\]

The degeneracy ratio \((2j+1)/(2j-1)\) is essential. It implies detailed balance at \(T_r\) in the zero-chemistry radiation-only subnetwork. No radiation-induced transitions between non-adjacent J are introduced. The column-convention transient generator \(G\) includes \(C\), both radiative transitions and chemical loss \(-q_j\) on its diagonal, \(q_j=\sum_\alpha Q_{\alpha j}\). Define the first-any-radiative-interaction killed generator \(G_0\), which removes all radiative off-diagonal transitions and instead adds their rates to diagonal killing, *without changing* collisions or chemistry.

For one initial molecule in state j, \(e_j\) is a unit vector and \(m=(-G)^{-1}e_j\) is integrated transient residence (s). The reaction product distribution \(P_\alpha=(Qm)_\alpha\); first-chemical-reaction-before-any-radiation is \(P^{(0)}_\alpha=(Q(-G_0)^{-1}e_j)_\alpha\). Their difference \(P_\alpha-P^{(0)}_\alpha\) is the joint product probability with at least one radiative *interaction*, whether emission or absorption. This is **not** the probability of at least one *emitted photon*.

For each line, the expected spontaneous emissions \(A_j m_j\), stimulated emissions \(A_j\bar n_j m_j\), and CMB absorptions \(A_j[(2j+1)/(2j-1)]\bar n_j m_{j-1}\) yield

\[E_{\rm rad}=\sum_{j=1}^{4}\Delta E_j\{A_j(1+\bar n_j)m_j-A_j[(2j+1)/(2j-1)]\bar n_j m_{j-1}\}.\]

Here **positive** \(E_{\rm rad}\) means energy leaving HD to radiation, **negative** means net energy entering HD from the radiation bath. Collisional energy gained by the fixed proton kinetic bath and terminal HD internal energy before chemistry are

\[E_{\rm bath}=\sum_{i\ne j}(E_j-E_i)C_{ij}m_j,\qquad E_{\rm terminal}=\sum_j E_j q_j m_j.\]

By multiplying \(-Gm=e_{j_0}\) with the internal energy row vector, the exact identity is

\[E_{j_0}=E_{\rm bath}+E_{\rm rad}+E_{\rm terminal}.\]

The identity holds for *internal HD rotational energy up to the instant of restricted chemical absorption only*. It **does not contain** the reaction's physical Q, H₂ final internal energy, gas thermal feedback, re-excitation from chemistry, a self-consistent radiation field or true sky intensity. Full energy closure cannot be inferred. The source spin policy `raw_SQM` versus `Eq6-7_spin_effective` is a declared alternative, never an uncertainty interval.

## New physical discriminant

For every source-state pair (T_g, spin policy, n/ncrit, J_initial), find roots of \(E_{\rm rad}[T_0(1+z_r)]=0\) only on \(z_r\in[0,300]\). A missing root in this interval is represented as NULL; no global uniqueness or no-go is asserted beyond this bounded search. In this dataset, 163 of 210 combinations exhibit an endpoint sign change, and a root is numerically obtained for each. At T_g=105 K, initial J=2, n=ncrit(J2), spin-effective policy: \(z_r^*=38.19417624108174\), \(T_r^*=106.82372734506828\,\mathrm K\). At this point chemistry-induced non-equilibrium shifts the zero away from simply imposing \(T_r=T_g\); do not confuse the root with global thermodynamic equilibrium. Sign changes are **conditional on source-qualified restricted five-state chemistry** and external radiation.

## Validation and scope

- 1470 actual (7 T_g ×2 policies ×3 densities ×5 J ×7 radiation conditions) coupled physics cases; 5880 line-resolved radiation rows, 14700 product joint probabilities, 735 **equal physical n(H⁺)** spin-policy comparisons, 210 radiation-balance entries.
- Source-lineage checks enforce parent exact R32 ZIP SHA, immutable R29 code SHA, exact original GL2022 source token hashes and original REC161/REC162/REC164 transcriptions. No restored faked EMAA file. Original EMAA HD–H⁺ dataset DOI 10.17178/emaa_hd_rovibration_805a7aa5 remains metadata only; 171×25 original numeric raw NOT_ACQUIRED.
- Python full tests including 210/210 R30 zero-radiation baseline cases and 2100/2100 product branch comparisons, eigenvalue/transient positivity, radiation-only thermal balance, chemical absorption normalization, bounded 163 roots. Same-author independently assembled mpmath85 420 cases/2100 aggregate metrics. Wolfram exact two-state identities `{True,True}, True, True` for energy balance, absorbing probability and blackbody detailed balance.
- **Canonical 34/49 unchanged**; R33 source-restricted auxiliary 1/1 after verified run. R6 and C9 different author NOT_RUN; native subagent NOT_EXPOSED. No main/parent/REC/CR mutation, no `FULL_A`, `PHYSICAL_Q`, native PES threshold, chemistry owner ACK, L4 or production claim.

## Literature and originals

- T. González-Lezana, P. Hily-Blant, A. Faure, *J. Chem. Phys.* 157, 214302 (2022), DOI 10.1063/5.0128598 (original supplementary PDF SHA locked).
- Sung et al., *JQSRT* 295, 108412 (2023 print / 2022 online), DOI 10.1016/j.jqsrt.2022.108412 (REC164 source transcription only).
- A. Faure et al., *The chemistry and excitation of H₂ and HD in the early Universe*, MNRAS (2024), DOI 10.1093/mnras/stae994 (CMB thermalization context, NOT numerical input).
- EMAA, dataset DOI 10.17178/emaa_hd_rovibration_805a7aa5, database DOI 10.1051/0004-6361/202554403 (source discovery only, original ASCII not acquired).
