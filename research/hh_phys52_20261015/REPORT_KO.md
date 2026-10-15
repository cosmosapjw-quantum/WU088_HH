# WU088_HH PHYS52: outgoing–collar Robin matching and axial m-block computation

2026-10-15 KST. Source parent PHYS51 PR90, commit 31af344a69686b02bcad5c6220048fc16001303c. Selected constructive theory R5 and coding C5–C8.

## Fixed physics and source identity

The original hydrogen spectator Hamiltonian in atomic units is h=-Delta/2-1/r-(1+1/s)exp(-2s), with s=|x-(7/10) zhat| and k=7/10. Preserve the original eta=Fy and xi=Fy-phi and the 1386 frozen complex128 numbers at research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz, SHA256 f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.

The scientific scope is the angular Galerkin subspace 21<=ell<=28, all m, 400 channels. Both the PHYS50 finite collar r=20..27 and the PHYS51 exact outgoing screened Hamiltonian r>=27 are restricted to this SAME band. This is NOT the original infinite-angular collar solution, not a physical H-H cross section.

## Exact finite-band matching lemma

Let u_inside=u_D(g_B,g_T)+A_D^{-1}f, where u_D is the homogeneous screened collar solution with prescribed high traces g_B,g_T and the particular solution has two zero Dirichlet traces. With Lambda_D the real positive finite-band collar boundary form and Z_out=U'(27)U(27)^(-1) from the genuine screened outgoing finite-band Jost solution, derivative continuity yields

(Lambda_D,TT-Z_out)g_T = -Lambda_D,TB*g_B - partial_r(A_D^{-1} f)(27).

Both finite-band operators retain the original physical off-centre screened multiplication S(s). PHYS50 gives Lambda_D,TT=Lambda_D,TT^dagger. Real Hermitian S and the outgoing Coulomb normalization give conserved radial current

Im(g^dagger Z_out g)=k ||U(27)^(-1)g||_2^2.

PHYS51's source-locked exact rational Coulomb Volterra q<2.863005967246512e-9, selected energy patch T=43, M=43 and C=4/5 prove

||U(27)||_2 <=43 exp[(4/5)(43-27)]/(1-q).

Consequently j_*=k(1-q)^2/[43^2 exp(2(4/5)(43-27))] >0 and

|| (Lambda_D,TT-Z_out)^(-1) ||_2 <= 1/j_*.

This follows directly from |Im(g^dagger (Lambda_D,TT-Z_out)g)| >=j_*||g||_2^2 and finite-dimensional injectivity implies surjectivity. The exact Fraction and positive exponential Taylor remainder certify a conservative display j_low=2.885508710e-15 Bohr^-1 and inverse upper 346559342044058.498094084768851728747685 Bohr. The displayed inverse was computed from the downward-rounded displayed j_low to preserve a coupled outward-bound contract, rather than independently rounding two reciprocal quantities.

PHYS50 also gives ||Lambda_D,TB*g_B||_2 <=sqrt(29)*(4849/16800)||g_B||_X <=1.554325247011620||g_B||_X. Thus the theorem bounds g_T once the actual g_B and physical source-derivative forcing are known, but does not generate them.

## Axisymmetric kernel implementation and numerical diagnostics

Since s=sqrt(r^2+R^2-2rR cos theta), [L_z,S]=0. All m are separately conserved; the ±m angular matrices are identical for real axisymmetric S. Channel counts: 400; 57 signed-m blocks; 29 unique nonnegative-m blocks; max block size 8. Dense matrix 160000 entries, signed-m nonzeros 3032 and 29 independent matrices 1548 entries. Dense-cubic 64 million arithmetic units versus 12048 independent small-block cubic units is a complexity comparison, not a radial solver speedup.

The original S(r,mu) angular integral is evaluated using normalized associated Legendre functions with the Condon–Shortley convention, Gauss–Legendre nodes, and a PSD factorized Gram matrix A=(B sqrt(wS))(B sqrt(wS))^T. At r27, max projected angular screen operator norm=1.378971190771564e-23 and direct node-wise screen max=1.4866466977148222e-23. The 128->256 node relative differences are m=0:2.39784859444773e-13, m=1:1.52475737708969e-14, m=21:6.57455565565556e-15, m=28:6.82681465244039e-15. These are floating quadrature comparisons, not proof of the exact continuous angular matrix.

Local Ubuntu (one BLAS thread), 7 matched-input assembly medians: scalar 0.00208340701647s; batched 0.00029828201514s; 6.984688686x measured assembly acceleration. No NCP runtime or entire radial solver benchmark claimed. Original source checked before all authoritative computations.

## Failures and corrected evidence

Initial targeted run 28 PASS/2 FAIL: (a) independent reciprocal decimal roundings were incorrectly assumed to multiply to >=1, a representation-level mismatch; the output inverse was changed to the upward-rounded exact reciprocal of the displayed lower bound, without changing underlying math. (b) the 192-node floating Gauss reference had worse Gram-weight numerical conditioning than 256 nodes and deviated by around 7e-13 from the 96-node case; replaced with a more accurate 256-node reference while retaining the 3e-13 test threshold. After change targeted pytest 30/30 PASS (0.43s). Full project pytest 407/407 PASS, exit0, 201.19s (time wall 202.07s, peak RSS 129312 KiB). Recorded in results/FULL_SUITE.{stdout,resource,exit}.

First Wolfram attempt exit5 because Wolfram protected symbol C was reused as a variable. Renamed rateC. Local Wolfram15 exit0 in 6.85s, exact all-m counts, exact outgoing matrix-current and DtN anti-Hermitian flux identities 0, exact denominator checks all passed. See results/CAS_LOCAL.*. xAct tensor infrastructure is not required by the present scalar radial/channel current proof. No independent infinite-dimensional theorem validation claimed.

Versions: Ubuntu Python 3.12.3, NumPy 2.4.2, SciPy 1.17; declared NumPy2.3.5 project pin mismatch not eliminated.

## Literature and sibling research

NIST DLMF sections 33.2, 33.4, 33.23: https://dlmf.nist.gov/33.2 ; https://dlmf.nist.gov/33.4 ; https://dlmf.nist.gov/33.23 . Ian J Thompson, Introduction to R-matrix Theory (2016), https://www.osti.gov/biblio/1281675. These supply the Coulomb wave convention and boundary matching context, not independent verification of these source-specific constants.

Cross-repo readback: WU088_HH PR90; BASS_HE PR65 at 8e759508317f5ffbc891c5876ff10771ad79297b; bass_cr PR72 at e91ffe368c4e6db64c4b6c5962566302a33402b6; rei_bianchi PR151 at 13ebaff2d7c41f389140a3ea8af82e606889cae7; PR152 at 9cd36354e46b8a75e3cb70d87e78f9e3c3c2f0a7; production PR150 at efd7c4a1f64519185462def0c369d459a449ec47. Their chemistry/source/opacity and atomic data do not yet provide the actual WU high channel boundary g_B, incoming adjoint or physical k_HH(T). No other checkout mutated.

NCP read-only SSH preflight for ubuntu/root/ncp principals was denied; no 64c/128GB job was submitted. NCP Rust installation is user-reported, not independently verified. Local Rust1.94.1 was verified. No native subagent tools exposed; native_subagent NOT_RUN.

## Next science

PHYS53 must address infinite ell>=29 outgoing screened operator and weighted trace X->X* with a uniform inverse bound (or scope-specific failure), then the actual original driven xi=Fy-phi, regular origin, incoming adjoint and physical scattering sigma(E). Thermal identical neutral-H k_HH(T) and REI HH_R10 adoption remain OFF.
