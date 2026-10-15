# PHYS51: finite-high all-m screened outgoing Jost

2026-10-15 KST. Parent PHYS50 commit 6db2b278aeed8c938098a92fb874e5b996d68e2e; Draft PR #89. Selected R5 / C5–C8 local execution. This report records original screened Galerkin finite-band science, NOT full physical H-H rates.

## Source identity and domain

Original spectator h=-Delta/2-1/r-(1+1/s)exp(-2s), s=|x-(7/10) zhat|, kappa=7/10. Original eta=Fy, xi=Fy-phi, archived 1386 complex128 coefficients unchanged.
Immutable source research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz SHA256 f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.

Exterior r>=B=27 Bohr; angular Galerkin projection to 21<=ell<=28 for ALL -ell<=m<=ell, exactly 400 channels. The full two-centre noncentral screened multiplication S(s), not a central surrogate, is included as P_band S P_band. Low/high cross terms and ell>=29 are NOT included.

## Constructive theorem

Define q_ell(r)=kappa²+2/r-ell(ell+1)/r². Coulomb outgoing H+=G+iF has eta_C=-1/kappa=-10/7. Its reduced-radial Wronskian gives |K_ell(r,t)|<=|H+(r)H+(t)|/kappa and positive outgoing flux Im[kappa H_ell'(rho)/H_ell]=kappa/(F_ell²+G_ell²)>0.

For r>=T, q_ell>=qstar=kappa²+2/T-28*29/T²>0, and int_T^infty |q'_ell| dr <=V=2/T+28*29/T². Energy E=|H_r'|²+q|H|² with E(infty)=2*kappa² yields
  |H|²+|H_r'/kappa|² <=2*kappa² exp(V/qstar)(1/qstar+1/kappa²)<M².
These majorants are computed as exact Fraction bounds using positive-Taylor remainders, integer sqrt ceiling, and original frozen source hash.

For 27<=r<=T, Euclidean logarithmic norm of first-order Y=(u,u'/kappa) is
  mu_2(r,ell)=|ell(ell+1)/r²-2/r|/(2*kappa).
Monotonicity for ell=21..28 and T=42..46 gives max mu=3790/5103 < C=4/5.
Therefore w(r)=M exp[C(T-r)] for 27<=r<=T, and w(r)=M after T, bounds all Coulomb outgoing channel amplitudes.

Since S(s)=(1+1/s)exp(-2s) and s>=r-R, the actual Hermitian noncentral projected screen obeys
  ||P_band S P_band|| <=(1+1/(r-R)) exp[-2(r-R)].
The Volterra operator u(r)=H+(r)a+int_r^infty 2K(r,t)(P_band S P_band)(t)u(t) dt
therefore satisfies
  ||V_operator||_w <= (M²/kappa)(1+1/(B-R))
      [exp(-p1)/(1+C)+exp(-p2)],
  p1=2(B-R)-2C(T-B), p2=2(T-R).

The exact rational exponential search chooses T=43, M=43, p1=27, p2=423/5, giving
  q <= 0.000000002863005967246512 < 1.
Neumann-series existence follows for 400 coupled outgoing finite-band channels, with weighted source response <=q/(1-q).

Because the finite projected angular multiplication is Hermitian real,
  J(r)=Im[u(r)^dagger u'(r)]
is constant. For outgoing amplitudes a, J(infty)=kappa ||a||². If the Jost boundary matrix U(27) had a nonzero kernel, J(27)=0 would contradict J(infty)>0. Hence U(27) is invertible in finite dimension, and
  Im <g,Z_out g> = kappa ||U(27)^(-1) g||² >0
for g!=0, with Z_out=U'(27)U(27)^(-1). No quantitative inverse norm is claimed.

## Connections and limits

PHYS50 finite collar r20..27 has a two-boundary positive form Lambda_D. At r27, the outgoing interface condition is (Lambda_D g)_T=Z_out g_T plus the source-induced derivative boundary term. The physical g_B, g_T, low-channel coupling, and original driven xi remain UNKNOWN. A band Galerkin outgoing theorem does NOT establish the infinite angular DtN, complete physical cross section sigma(E), or identical-pair Maxwellian k_HH(T). REI owner HH_R10 remains OFF.

Actual code: src/wu088_hh/phys51_finite_outgoing.py; scripts/phys51_finite_outgoing.py; tests/test_phys51_finite_outgoing.py; result FINITE_HIGH_OUTGOING.json. Targeted 20/20 pytest PASS on local Ubuntu 2026-10-15. Independently connected Wolfram calculated mu=3790/5103, margin=1462/25515, qstar=18001/184900, V=898/1849, p1=27, p2=423/5 and direct noncertifying exponential q=2.863005967246511099879883...e-9. High-ell Coulomb ell=21 r27 outgoing log derivative -0.18253880022977345+0.12712470573077846 i (Bohr^-1) with flux identity checked. Full project regression results stored separately, verify before release claims. Runtime NumPy2.4.2 differs declared 2.3.5, so CI-equivalence not claimed.

64-core/128-GB NCP heavy_queue empty for this exact-rational local task. A root SSH BatchMode test to the configured NCP host returned Permission denied (publickey,password), so no NCP work was performed. Other repos remain unchanged.

Primary mathematical references:
NIST DLMF 33.2 https://dlmf.nist.gov/33.2
NIST DLMF 33.4 https://dlmf.nist.gov/33.4
NIST DLMF 33.23 https://dlmf.nist.gov/33.23
Leis and Roach (1988), DOI 10.1098/RSPA.1988.0065, long-range Coulomb exterior Dirichlet theory (context only, not an independent proof of the new 400-channel source-specific bound).

Next: infinite ell>=29 outgoing uniform X->X* exterior estimate, physical low/high + driven xi origin/adjoint match, then sigma(E) and k_HH(T). Stop science promotion until these dependencies close.
