# WU R34 | GL2022 v1 first-quench → HD5 CMB×chemistry restricted source bridge

2026-10-30 KST. Mathematical and scientific scope: **derived, source-qualified, conditional auxiliary result**. This is not EMAA 171×25 numeric crosswalk or complete HD kinetics. Source owner of original data is not the author of this composition.

## Original sources and model domains

The full original byte-locked R33 SOURCE ZIP SHA256 `8036d1d4cae599a1dc113612e67146fa8b822224b074f827ae2c0d9684e7a362` contains an immutable nested R32 SOURCE ZIP SHA256 `01482fdefef303b8cc00bd0efe9b20c23d1886a69679d76eec9d67434fe643e7`. R32 computes source-based first vibrational-quench branching of HD(v=1,J=0..6) under H+ collisions, independent of the overall fixed proton density when only binary collision hazards are included. Its source-valid gas temperatures exclude malformed `2005 K`; source-allowed temperatures intersecting R33's restricted 5-level chemistry are **{55,105,255,505,1005,3005} K**. R32 uses historically rendered CDMS level energies, not byte-authenticated original 2011 fit files.

R33 defines a fixed prescribed H+ density, gas kinetic temperature, and external isotropic Planck radiation `T_r=2.7255(1+z)` K with `z∈{0,5,10,30,100,300}` plus `OFF` (no external background, **still with spontaneous emission**). R33 transient HD(v=0,J0..4) has source-computed H+ collisions, source-restricted H+ + HD→D+ + H2(v0,J'0..9) chemical absorption, Leiden A transcription and Sung 296K fitted rotational centers. It is not a self-consistent cosmological redshift trajectory.

## Exact probability composition

Let `B_{j|i}(T,p)` be the R32 probability of first *collisional* `v1,J_i→v0,J_j` quench, where `p` identifies R32 derived-upward or down-only counterfactual. `Σ_{j=0}^{10} B_{j|i}=1`. Define `W_i=Σ_{j=0}^4 B_{j|i}`. Only the probability branch of the first quench entering `v0,J≤4` is handed to the R33 network. The other probability `1−W_i` **leaves the defined problem**, not the real chemical system.

For a fixed R33 environment `x=(T_g,policy,n_H+,T_r)`, let `P^{33}_{α|j}` be the exact R33 first-chemistry H2 product probability, α=0..9, and `P^{33,0}_{α|j}` the joint probability of that chemistry before *any* radiative interaction (spontaneous, stimulated or absorption), as defined by the killed generator. Then

`P^{bridge}_{α|i}(x,p) = Σ_{j=0}^4 B_{j|i}(T,p) P^{33}_{α|j}(x)`,
`P^{bridge,0}_{α|i} = Σ B_{j|i}P^{33,0}_{α|j}`,
`P^{bridge,rad}_{α|i} = P^{bridge}_{α|i} − P^{bridge,0}_{α|i}`.

Normalization is `Σ_α P^{bridge}_{α|i}=W_i`, and `Σ_α (P^{bridge,0}_{α|i}+P^{bridge,rad}_{α|i})=W_i`, **not 1**. Conditional product ratios may divide by W_i only with explicit `given_J0to4_quench` semantics. For each R33 line ℓ, line-resolved spontaneous/stimulated/absorption expectation values and net energy exchange compose linearly with the same `B_{j|i}`. This yields physically meaningful **restricted joint probabilities and conditioned radiation exchange**, without extrapolating unobserved transitions.

## Source energy seam, not an added physical energy source

R32 uses rendered historical CDMS 2011 v2 energies `E^{32}_{v0,j}` while R33 uses four Sung fitted 296K rotational separations `E^{33}_{v0,j}`. They are close but **not exactly numerically identical**. Let `E^{32}_{v1,i}` be the R32 initial internal energy, and define

`H_q = Σ_{j≤4} B_{j|i}(E^{32}_{v1,i} − E^{32}_{v0,j})`,
`S_rep = Σ_{j≤4} B_{j|i}(E^{32}_{v0,j} − E^{33}_{v0,j})`,
`H_post=Σ_j B_{j|i} H^{33}_{bath|j}`, `R_post=Σ_j B_{j|i}E^{33}_{rad|j}`, `E_term=Σ_j B_{j|i} E^{33}_{prechem|j}`.

The R33 generator identity, restricted quench endpoint identity, and linearity imply the **exact model bookkeeping identity**

`W_i E^{32}_{v1,i} = H_q + S_rep + H_post + R_post + E_term`.

`S_rep` accounts for **representational mismatch between spectroscopic sources**. It is NOT photon energy, proton heat, reaction enthalpy or a new physical source. Alternatively one could reinterpret `H_q` under an aligned hybrid energy basis, but the source-preserving analysis explicitly retains both original representations and their difference. With seam omitted the joint energy ledger is not zero; do not repair by numerical tolerance inflation.

## Radiation neutrality discriminant

For a fixed selected quench distribution, define `R_i(z)=Σ_{j=0}^4 B_{j|i} E^{33}_{rad|j}(T_0(1+z))`. This is an energy *per initial v1 molecule* restricted to the modeled J≤4 branch. We search finite `z∈[0,300]` with fixed `T_g,nH+`, using the same R33 continuous blackbody generator for intermediate z, and report a root only when `R_i(0)R_i(300)<0`. Lack of an endpoint sign change is *not* a proof of no root (even-multiplicity roots and multiple crossings are not excluded). All roots are conditional radiation competition; they are NOT observed cosmological redshifts or thermal histories.

## Actual results and risks

Generated source-locked output: 3,528 physically distinct conditional cases, 35,280 H2 product rows, 14,112 line photon rows, 504 radiation-neutrality candidates and 324 bracketed roots. `W_i` ranges 0.2363696353977947–0.3686497092004765, so most first-quench branches fall outside the intentionally restricted v0 J0..4 postquench model. Max |S_rep|=2.0195212731651592×10^-27 J. Max absolute book residual=8.425943506694157×10^-35 J; probability defect <1.90×10^-14; root residual max 1.2001787917940749×10^-31 J (same-author internal tests, not independent-author review).

At `T_g=105 K`, R32 `DB_UPWARD_V1`, v1 J0, R33 `Eq6-7_spin_effective`, `n/ncrit_J2=1`, `nH+=3954.4181821071797 cm^-3`, and z100: `W=0.3587827519512391`; restricted radiative transfer `-2.8614878750948852e-21 J` per initial v1 molecule; joint at-least-one-radiative-interaction-before-chemistry probability `0.2974427926607483`. This is restricted probability mass, not full chemical probability. The same 105K scenario has bracketed radiation-neutrality `z*=46.717810` (T_CMB≈130.054892 K).

## Source status and admission

Actual official EMAA dataset `10.17178/emaa_hd_rovibration_805a7aa5` describes 171 proton-collision transitions×25 temperatures (5–3005 K), but its *original selectable H+ RADEX ASCII bytes remain unacquired*. GL2022/EMAA numerical equality and distinct-author validation are not established. The conservative preflight parser from the previous thread remains available, but this bridge produces **zero actual EMAA numerical comparisons**. No ad hoc rate interpolation, zero filling for missing species/channels, native PES Q, owner ACK, independent R6/C9 or full radiative network is manufactured. Canonical DAG stays 34/49; new auxiliary bridge 1/1 SCOPED; R6/C9 distinct-author NOT_RUN; no merge / production.