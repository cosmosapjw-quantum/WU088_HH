# PHYS33F R5: screened-exterior-bound interior Q21 theorem and live REI support

2026-10-14 (KST). Parent PHYS33E commit `3cfff53361a9cfa0d1c373b56a3762943334f815`. Scientific scope: **PARTIAL** continuation of `INTERIOR_LOW_SCHUR_AND_GLOBAL_AMPLITUDE_BOUND`. No change to operator, source, normalization, old model-specific rate/response certificates, or production.

## New derived theorem (continuous all-m high sector)

Fix `h_lambda=-Delta/2-1/r-lambda*S(|r-R ez|)`, `S(s)=(1+1/s)exp(-2s)`, `R=kappa=7/10`, `epsilon=49/200`, `lambda in[0,1]`. All radial variables are divided by `a0`; Hamiltonian is in `2I0` units; retain `c,hbar,kB` and distinguish source `I0=13.605693122990eV` from receiver `chiH=13.598434599702eV`. Signature(-+++), atomic Euclidean. Couple the ACTUAL full-screened exterior `r>4` through its DtN map, not the old finite collar.

For `Q_L=1_(ell>=L)` on B4 with L=21/all m and harmonic boundary extension, set `Kstar²=||grad u||²_B4+4 sum_(ell,m)(ell+1)|u_lm(4)|²`, `N²=||u||²_B4`. Talenti sharp Sobolev and the elementary upper quadratic for `(1+s)^(3/2)` give `<u,S_Ru><=467/1000 Kstar²`; this is independent of the shifted spectator center. The pinned exact Coulomb `Re d8(4)<0` and exact angular ladder give `-Re t_l>=(l+1)/4 theta_l`, `theta_l>=974/1000` for l>=21 (exact theta21=117067/120175). Parent full-screened exterior DtN difference is `<=9801/481684<51/2500`.

Using the angular barrier `Kstar²>=462/16 N²`, `int |u|²/r <=NKstar/sqrt462`, one obtains
`
Re a_lambda[u,u] >= (499/27500)Kstar²-NKstar/sqrt462-(49/200)N²
                 >= (193/192500) Kstar²
                 >= (579/20000) N².
`
Consequently `||R_Q21||_(L2(B4)->L2(B4)) <=20000/579 ~34.54`. This is a new **weaker bound but smaller low sector**: the previous Q29 inverse <=1/10 remains independently valid and preferable for some Schur estimates. Same sufficient method does not close L20; that is not a physical noninvertibility theorem. The full low Schur inverse, global amplitude, and two-centre rate remain `null`. No extension of this fixed-k theorem to kappa->0 is admitted.

## Actual low-source/output identity and boundary

For `P=ell<=20,Q=ell>=21`, use the full weak-form coupling and exterior particular source: `G_Q=A_QQ^-1`, `S_P=A_PP-A_PQ G_Q A_QP`, `p=S_P^-1(f_P-A_PQ G_Q f_Q)`, `q=G_Q(f_Q-A_QP p)`. The exact readout is `J=J_Pp+J_Qq+J_exterior`. For reference residual `rho`, the full error includes `delta_p=S_P^-1(rho_P-A_PQ G_Q rho_Q)` and `delta_q=G_Q(rho_Q-A_QP delta_p)`. Omitting the induced source or output is refuted by an exact noncommuting Fraction/SymPy manufactured example. Off-centre `S_R` is **not** a bounded L2 multiplication, so coupling uses H1/H-1 forms. No global amplitude error interval is issued before `S_P^-1`, bulk/interface residual and outgoing dual norms are all certified.

## Live REI collaboration

Actual 2026-10-14 12:31 UTC worktree HEAD `6fe1e8d03fadbc46bdc6dd0072a55b83cbd03d0d` and STATE were read. Owner AX07 ZERO full zbar20..4 is scoped conditional completed; AX08 signed family is running, AX11 T1 and AX12 variants are prepared but not launched; no global scientific admission. **Current** convergence reducer SHA256 `35e1499ef9a69180e5df442c198d3b4c28ea1090c9f6829aad1a68eba8c69cc9` differs from old PHYS33E patch target after owner electron-floor work. A new exact-target temporary patched-copy run passed all10 synthetic source-pair tests. Patched reducer SHA256 `7978ea5a60ea222b74a6f79317a9774c81e628aeb0f942b30572eff51167fd9f`. Source relation for actual baseline/T1 resource-only code change is retained from PHYS33E. Supplier is **ready for scoped owner review**, not already applied nor AX11-ready. No REI repo/state mutation or solver start; no optional HH baseline gate.

## Verification/provenance

Actual Wolfram15.0.1 gave exact moment `61*pi^(3/2)/(48sqrt3)`, Sobolev product cube `3721/(11664pi)`, exact gamma `499/27500`, H1 coefficient `193/192500`, mass `579/20000`, all required inequalities. Actual xAct/xTensor1.3.0 (official xTensor.m SHA256 `04e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36`) returned4tensor zero residuals after one failed fresh-expression attempt. Python exact Fraction12, exact Schur5, helper6 and remote revised-source integrated10 checks passed. These are overlapping same-author/CAS checks, **external independent scientific review NOT_RUN**. No native subagents, old BVP/rate/P01/native/HPC campaign.

Full20-member ZIP (19 payloads), 347495 bytes, SHA256 `bca6097cbaeab7843e12568bb7802e1930074ec65efad3ea7660fa080db8f71a`: [Drive full Korean proof, reproducible source, CAS, exact input and failure log](https://drive.google.com/file/d/1HNKKFXhViwQdvaODgnX71kzLBMqZ9XGU/view?usp=drivesdk). Dropbox destination existing HH folder, final receipt in EVIDENCE_INDEX sidecar. Local CRC/all19 hashes, relocated verifier, altered copy rejection and restored-copy pass. No separate remote restore test. No private raw REI histories included.

Next: `INTERIOR_LOW_SCHUR_NUMERICAL_INCLUSION_AND_PHYSICAL_AMPLITUDE_DUAL`. Maintain both Q21 and Q29 options, compute actual low Schur and whole-domain reference/flux residual, then dual physical amplitude. REI owner should consume exact-target guard and actual T1 source relation only when conditions are met. No main/owner merge or production promotion.
