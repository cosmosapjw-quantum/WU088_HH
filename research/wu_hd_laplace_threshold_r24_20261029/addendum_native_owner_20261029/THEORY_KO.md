# WU088_HH R24 | GL2022 native threshold admissibility and actual-owner reaction identity

Scope: `WU_HD_GL2022_PES_NATIVE_THRESHOLD_R24`; read-only mathematical/source audit. Parent PR162 exact commit `2f214319ca8600475b1d4e85d1ca21a0249136a8`. R22 sibling PR160 at `9db6f91debf54af1cc129538cfd6f6a716a78a56` independently consulted, never merged. Independently posted R24 Laplace branch PR163 `c63f29fb2b6ede9ebb14b7df6aed91707a0c6d09` already provides the scoped Maxwell bound and four P01–P04 receipts. This supplement adds NO physical Q.

## 1. Exact physical channel and typed notation

`H+(ground) + HD(v=0,J=2) -> D+(ground) + H2(v=0,J=1)`, stoichiometry (-1,-1,+1,+1). Define asymptotic total channel energies in ONE declared Hamiltonian and ZERO:

`E_in = E_asym_BO^H+HD + eps_HD(0,2; nuclear masses, BO corrections) + delta_in^isotope`
`E_out = E_asym_BO^D+H2 + eps_H2(0,1; nuclear masses, BO corrections) + delta_out^isotope`

`Delta_native = E_out-E_in` and `theta_native=max(0,Delta_native)` measured with respect to incoming relative kinetic energy. Energy released per event `Q=-Delta_native`, not automatically `-theta_native` if exothermic. Under same common molecular electronic zero the BO neutral-charge-separated electronic asymptotes are related, but isotope-specific ionization and finite-mass/adiabatic corrections require explicit declarations. Spectroscopic and separate neutral PES levels cannot be inserted without a proven Hamiltonian/zero transformation. Numerical `Delta_native`, its uncertainty, and Q remain NULL.

## 2. Original GL2022 equations and the energy-axis ambiguity

González-Lezana, Hily-Blant, Faure, JCP 157,214302 (2022), DOI `10.1063/5.0128598`, Eq(3) writes the incident wave number squared as `k_vj^2 = 2 mu (E-E_vj)/hbar^2`, where E is a total energy; Eq(4) writes the Maxwell integral with an integrand `E sigma(E) exp(-beta E)` over E>=0. This notation can only be safely reconciled by explicitly defining incoming kinetic `eps = E_total-E_vj` and by confirming which variable was used for tabulated/coded cross sections and quadrature. This paper's text and currently recovered supplement do not give the source-native target cross-section input arrays, PES asymptotic eigenenergies, isotope/BO correction, or energy-zero change of variable needed to authenticate a numeric theta_native. Fig.1 is an energy-level diagram, not a tabulated uncertainty-qualified threshold.

The publicly accessible file named `H3p-singlet-pot.f` at `fama.iff.csic.es/personas/octavio/metodos-programas/PES/h3p/` explicitly identifies itself as Aguado et al. JCP 112 (2000) 1240, **not** Velilla et al. JCP 129 (2008) 084307. It cannot be passed off as the GL2022 named Velilla-2008 PES implementation.

## 3. Conditional source support bound, not recovered threshold

With entrance-relative kinetic `eps >= 0`, a fixed nonnegative cross section `sigma(eps)` independent of T, support beginning at theta, and one consistent reduced mass,

`k(T) = sqrt(8/(pi*mu)) beta^(3/2) int_theta^infty eps sigma(eps) exp(-beta eps) d eps`, beta=1/(k_B T).

For `T_c<T_h`, positivity gives `k_h/k_c >= (T_c/T_h)^(3/2) exp[theta*(beta_c-beta_h)]`. Thus

`theta <= [ ln(k_h/k_c)+(3/2)ln(T_h/T_c)] * k_B/(1/T_c-1/T_h)`.

The opposite inequality sign is an adversarial mutation rejected by the positive-kernel proof. The 15 K to 55 K GL2022 supplement printed rates are `3.99e-14` and `2.92e-11 cm^3/s`, yielding `theta <= 15.186303821758897... meV` (nominal printed decimals). The R23 external spectroscopic candidate 20.950020993840458 meV exceeds that conditional upper bound. This falsifies their **joint** assignment to the same positive temperature-independent entrance-kinetic Laplace kernel, not GL2022 itself. Spectroscopic candidate `Q=-20.950... meV` remains conditional and not native. Printed-digit nearest-mantissa rounding gives hypothetical bound 15.19157 meV, not a measured uncertainty.

Proof: write `F(beta)=k(T)/(C beta^(3/2))`; for beta_c>beta_h, `F(beta_h)/F(beta_c)= E_w[ exp((beta_c-beta_h) eps)]>=exp((beta_c-beta_h)theta)`. Take logs. Positivity is essential; changing the energy zero or allowing T-dependent sigma invalidates direct numerical comparison.

## 4. Molecular reaction versus atomic charge exchange

Actual CR PR124 pinned head `a6b49b352fed31587955d55b1cad30c0b55a81eb`, module `research/cr_c23e_d43_source_binding_20261024/implementation/d_binding.py` at Git blob `cbd76337f65ca040f8c4b66b46953dde74e6e305` computes

`J = k_f n(D:0)n(H1:1)-k_r n(D:1)n(H1:0)` and an event labeled `HD_CX`, with species `D:0,H1:1,D:1,H1:0`. This is **atomic** `D0 + H+ <-> D+ + H0`; it has NO diatomic HD or H2. The fit uses `Delta_atomic = 43 k_B` ~3.7054533027 meV and is not a molecule-reaction Q. In the code, `dispatch_d_binding -> validate_d_binding -> d_binding.source` runs bounded manufactured point tests, not a four-molecular-species chemistry IVP.

Actual REC PR157 pinned head `e209cd0180c8bf199fc476c37e3cbf8d50394b6c`, module `research/program_expansion_20261025/hd_adapter/lamda_hd.py` Git blob `632a8a094e7eedd24a1ec3132fec20765d6e39da` reads the 2289-byte LAMDA HD rotational spectroscopy source, 9 rotational levels, eight radiative and 18 H2 collisions. It exposes `line_coefficients -> einstein_B` on printed photon nu without `require_energy_frequency_bridge` enforced in this call; 7/8 original 35-Hz gaps failed. Separate `multichannel.generate` and `cycle_space` are marked channel-level rotational/Markov diagnostics, NOT `H+ + HD -> D+ + H2` material reaction integration.

Both atomic CX and ionic molecular exchange have the same signed integer sums for H nuclei, D nuclei, charge and total particle count, all zero; that does NOT make their physical species/type or state-specific energy sources identical. `native_owner_gate.py` enforces exact typed identity rather than conservation-only matching and fails closed even on a forged owner ACK/threshold string. This validates a safety/admission contract, not a live owner call graph.

## 5. Scientific status and remaining minimal evidence

NO recovered native `(0,2)->(0,1)` asymptotic rovibrational input, no model-specific entrance-energy zero or isotope corrections, no native σ(eps) arrays for 15/55 K re-integration, no named molecular reaction owner ACK. Thus `GL2022_PES_NATIVE_THRESHOLD=null; physical_Q=null; owner_ACK=null; full_A=null; source_uncertainty=null`. Continue only after original Velilla PES coordinate/model identification, isotopologue nuclear masses and corrections, native total-to-relative energy transformation, actual state-resolved scattering arrays with independently recomputed Maxwell k(T), and affirmative owner ACK.

Canonical DAG remains **34/49**; historical R23 scoped **18/20**; distinct-author R6/C9 **NOT_RUN**; HH_R10 **OFF**; production **NOT_ISSUED**; L4 **false**. No main merge, no full-A promotion, no foreign mutation. Scope is selected executable-reachable code paths at pinned heads, not an exhaustive guarantee across private/generated/archived programs.