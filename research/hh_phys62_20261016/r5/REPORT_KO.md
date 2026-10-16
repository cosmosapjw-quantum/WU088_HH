# PHYS62 R5: central Coulomb real-axis Abel-current and unweighted L2 divergence

Parent PHYS61 PR106: 35dee6a0b79efb925c4749a1a1db864feb1509ab.

Original spectator source h=-Delta/2-1/r-(1+1/s)e^-2s, s=|x-0.7 z|, kappa=0.7, B=27 Bohr. Frozen 1,386 complex128 NPZ SHA256 f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d verified.

## New exact fixed-ell lemma (not all-angular screened LAP)

Let tau=2 Im(E)>0 and p_l(tau,B)=1 be the central Coulomb upper-half-plane outgoing reduced-radial Poisson solution. Exact current J=Im(conj(p)p') satisfies J'=-tau|p|^2 and J(infinity)=0. Thus Im Z_l(tau)=tau int_B^infinity |p_l|^2 dr.

Analytic continuation near real k=0.7 and the Coulomb Wronskian imply, for every FIXED ell,
lim_{tau->0+} tau ||p_l(tau)||_L2^2 = j_l = (0.7)/(F_l(-10/7,18.9)^2+G_l(-10/7,18.9)^2)>0.
The normalized trace X norm^2=sum (ell+1)|g_lm|^2 therefore forces ||P_C(tau)||_(X -> UNWEIGHTED L2)^2 >= Im Z_l(tau)/((ell+1)tau), diverging as tau^-1. This only diagnoses the unweighted method; a spatially weighted real-axis LAP remains OPEN, not disproved. This is central Coulomb reference, not original noncentral screened real-axis DtN.

## Executed evidence and original package
Original source-locked full implementation src/wu088_hh/phys62_flux_abel.py plus 22/22 actual focused pytest PASS, stdout/exit/resources, exact free-wave flux negative control and Wolfram algebra residuals zero. Full source, original NPZ, manifest and evidence in WU088_HH_PHYS62_R5_SOURCE_EVIDENCE_20261016.zip SHA256 987c6615084b66e801a95d1b984f484b4203c60ad32fd364f996110be2a3e89b, 34,250 bytes. Dropbox /WU088_HH/WU088_HH_PHYS62_R5_SOURCE_EVIDENCE_20261016.zip and Google Drive /Google Drive/WU088_HH/PHYS62_R5_20261016/ both independently re-downloaded and exact SHA/CRC/manifest RESTORE_VERIFIED. GitHub quick verifier here is independently executed, source-bound and scoped. Full source files are in the two cloud capsules because the direct container-path-to-Library transfer returned container_session_expired; no unverified GitHub source claims.

Sources: NIST DLMF Chapter 33 sections 33.2, 33.11, 33.13; Derezinski-Faupin-Nguyen-Richard (2020) DOI 10.1007/s43036-020-00082-6.

Next: C5-C8 fixed (20,21,m) original screened P-Q FIRST BORN continuity tau->0 with noncertifying finite quadrature; PHYS62 weighted all-ell Coulomb outgoing LAP and actual all-ell screened Z_S^+ OPEN. Original xi, sigma(E), k_HH(T) HOLD; REI HH_R10 OFF.
