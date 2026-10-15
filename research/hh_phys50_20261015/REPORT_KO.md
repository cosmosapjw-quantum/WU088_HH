# WU088_HH PHYS50: 비영 고차채널 경계 trace와 엄밀한 Dirichlet-to-Neumann

2026-10-15 KST. Parent [PHYS49 PR #88](https://github.com/cosmosapjw-quantum/WU088_HH/pull/88),
commit `ce519958d930aa778cfce94134dba608ce552cd7`.
Selected stage: constructive R5, C5 implementation and bounded C6-C8 verification.
No local Codex and no native subagents (capability absent).

## Original physical source and previous theorem

The immutable H(1s)+H(1s) one-electron spectator is
\[
h=-\tfrac12\Delta-\tfrac1r-(1+s^{-1})e^{-2s},\quad
s=|\boldsymbol r-R\hat z|,\quad R=\kappa=\tfrac7{10}.
\]
Original variables \(\eta=Fy\), \(F=e^{e^{-s}}\), \(\xi=Fy-\phi\) and
the source/receiver energy convention stay unchanged. Atomic units \(a_0\)
and \(E_a=2I_0\); original frozen six-panel, 21-mode, 1386 complex128
NPZ SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`.
The saved original trial ends at \(r=20a_0\); no exterior low field
or high outgoing boundary data have been fabricated.

PHYS49 proved all \(m\), all \(\ell\ge21\) high-channel **zero-Dirichlet**
coercive inverse on \(B=20\le r/a_0\le T=27\). This work removes the
zero-trace requirement in the finite-radial Dirichlet class.

## Mathematical construction and proof

Use the reduced-radial, angular \(Y_{\ell m}\)-normalized high block
\[
A_H=Q[-\partial_r^2+\ell(\ell+1)/r^2-2/r-\kappa^2-2S(s)]Q,
\quad S(s)=(1+s^{-1})e^{-2s},\quad Q=P_{\ell\ge21}.
\]
On this fixed collar, exact centrifugal floor
\(b_{\min}=1693/24300\). Original PHYS45 rigorously upper bounds
the screen by \(\delta=\|2S\|_\infty\le
3.624112937975321688970\,10^{-17}\). Thus for arbitrary traces,
\[
a_H(u,u)\ge\|\partial_r u\|_2^2+(b_{\min}-\delta)\|u\|_2^2.
\]

The high angular trace norm is
\[
\|g\|_X^2=\sum_{\ell\ge21,m}(\ell+1)
(|g_{B,\ell m}|^2+|g_{T,\ell m}|^2).
\]
For each \(\ell\) use the **exact rational** boundary-hat width
\(w_\ell=d/[2(\ell+1)]\), \(d=T-B=7\). Set
\(v_\ell(B+x)=g_{B,\ell}(1-x/w_\ell)\) on \(0\le x\le w_\ell\)
and \(v_\ell(T-x)=g_{T,\ell}(1-x/w_\ell)\), zero in between.
The two supports are disjoint for every high \(\ell\).
Per amplitude, the integrals \(\int|\partial_r v|^2=1/w_\ell\),
\(\int|v|^2=w_\ell/3\) are EXACT, with no numerical quadrature.
Since \(0<V_\ell(r)\le\ell(\ell+1)/B^2\) and \(-2S\le0\),
\[
a_H(v,v)\le\sum_{\ell m}
\left(\frac{2(\ell+1)}d+\frac{\ell d}{6 B^2}\right)
(|g_B|^2+|g_T|^2)
\le C_{\mathrm{tr}}\|g\|_X^2,
\]
where
\[
\boxed{C_{\mathrm{tr}}=\frac2d+\frac d{6B^2}
=\frac{4849}{16800}\simeq0.288631.}
\]
The exact algebraic margin of the second inequality, per boundary
amplitude pair, is **\(7/2400\)**. No upper angular cutoff was imposed.

Lax–Milgram on the positive high form proves a unique homogeneous
screened high solution \(u_g\) with arbitrary \(g\in X\), minimizing
energy among affine extensions. The positive selfadjoint
two-boundary **Dirichlet-to-Neumann quadratic form** has outward
flux \(\Lambda_D g=(-\partial_r u_g(B),+\partial_r u_g(T))\) and
\[
\boxed{0\le\langle g,\Lambda_Dg\rangle=a_H(u_g,u_g)
\le(4849/16800)\|g\|_X^2.}
\]
It defines a bounded operator \(X\to X^\ast\).
The continuum trace-to-radial \(L^2\) gain obeys
\[
\|u_g\|_2\le\gamma\|g\|_X,\quad
\gamma^2=C_{\mathrm{tr}}/(1693/24300-\delta),\quad
\gamma\le2.03538284099708551686806.
\]

For an arbitrary original low-channel field \(u_P\) on the collar,
the screened forcing \(f=+2QSPu_P\) has PHYS49 zero-boundary
particular solution \(\|u_f\|_2\le\alpha\|u_P\|_2\),
\(\alpha\le1.43050924568208798481524\,10^{-16}\).
The complete **conditional** estimate is
\[
\boxed{\|u_H\|_2\le\gamma\|g\|_X+\alpha\|u_P\|_2.}
\]
The return screened source \(2PSQ u_H\) has separate trace
coefficient \(\delta\gamma\le7.37645728779050463115817\,10^{-17}\)
and low source coefficient
\(\delta\alpha\le5.18432706516977314852665\,10^{-33}\).

This is an **infinite-angular** but **finite-radial and
two-Dirichlet-boundary** theorem, not the physical Coulomb outgoing
DtN at \(r=27\). The physical high boundary trace \(g\) remains
UNKNOWN; setting it to zero is not justified by the new theorem.


## Actual local tests, Wolfram, and numerical/CPU evidence

Implementation: `src/wu088_hh/phys50_trace_dtn.py`,
`scripts/phys50_trace_dtn.py`, and independent
`scripts/phys50_trace_preview.py`, with
`tests/test_phys50_trace_dtn.py`.
Original SHA locked at the start of every authoritative exact source run.
The rigorous \(C_{\rm tr}\), \(\delta\), \(\beta\), \(\alpha\) and
\(\gamma\) come from Python Fraction/isqrt and exact source-locked
positive exponential Taylor remainder, not sampled special functions.

Real local Wolfram Language15 and separately connected Wolfram
evaluate exactly:
- both triangle-hat energy primitives;
- \(C_{\rm tr}=4849/16800\) and per-ell margin \(7/2400\);
- barrier \(1693/24300\), PHYS49 Poincare \(\lambda_D=301657/1190700\);
- nonzero-trace \(\gamma\simeq2.03538284099708551686805\);
- source response \(\alpha\simeq1.43050924568208798481524\,10^{-16}\);
- constant-positive-barrier analytic DtN eigenvalues
  \(\omega\coth(7\omega/2),\ \omega\tanh(7\omega/2)>0\).
Local CAS exits 0.

Initial 80-digit mpmath triangle quadrature regression failed
because an independent test used Python's floating `L/400`
rather than `mp.mpf(L)/400`. The independent oracle was repaired
**without relaxing the tolerance or changing the mathematical
bound**. Thereafter **24/24 new targeted tests PASS** and
**357/357 entire WU repository pytest PASS**, actual 191.25s, exit 0.
Actual Ubuntu runtime Python3.12, NumPy2.4.2 and SciPy1.17;
declared NumPy2.3.5 exact pin does not match, so this is
host-verified rather than pinned CI-equivalence.

The independent *NONCERTIFYING* finite difference diagnostic
uses original noncentral screened potential at every radial and
Gauss angular point, modes \(m=0\), \(\ell=21\dots28\)
(plus \(\ell\le32\) comparison) with **manufactured prescribed**
nonzero high boundary traces. The actual original frozen input
is NOT extrapolated beyond r20. The numerical boundary flux
\(-u'(20),+u'(27)\) gives a discrete SPD DtN matrix; independent
interior gradient+potential energy equals \(g^\ast\Lambda g\)
up to floating error below \(4\times10^{-15}\).

| n_r / n_mu / ellmax | max weighted DtN eigenvalue | measured trace response L2 | common certified DtN upper |
|---|---:|---:|---:|
| 32/128/28 | 0.03526859234 | 0.930647226 | 0.28863095238 |
| 64/128/28 | 0.03760003675 | 0.958749850 | 0.28863095238 |
| 128/192/28 | 0.03885853725 | 0.973476612 | 0.28863095238 |
| 64/192/32 | 0.03921671087 | 0.958749850 | 0.28863095238 |

This is not convergence of the exact infinite angular DtN
since the diagnostic uses finite \(\ell\) truncations.

Numerical optimization: the sparse LU factorization is cached
once. Solving the full boundary RHS as one matrix batch is
about **1.35–2.51x** faster than separate RHS columns under
the same factorization, accuracy and original numerical grid.
No native H-H scattering or `rei_bianchi` chemistry acceleration
is claimed. In this tiny exact Fraction proof, a serial execution
is appropriate; native subagents are NOT exposed.

## Latest crossrepo readback and scientific next step

At readback latest `rei_bianchi` PR #144 (SHA
`f85394d50078fc384ce6aff55e669da866dfca35`)
constructs photon/He gas \(Q^0,Q^z\) recoil and sharp positive
Case-A moment constraints, and PR #145 (SHA
`54e29dff5a90c0a785cb6dcfb004403614ca403b`)
constructs positive Lagrangian massive Vlasov cells.
These are **different source families** from WU088_HH
microscopic positive-energy scattering. Both highlight the need
for real source-owned energy/momentum/gas-frame rate, but neither
supplies \(k_{\rm HH}(T)\). Active original
`rei_bianchi` owner checkout still has HEAD
`0fcb2dddf5de6b583c2e00f150abff0b2afb6315`,
unchanged by this PHYS50 research.

Relevant mathematical source:
Clark–Gesztesy–Mitrea,
`Boundary Data Maps for Schrödinger Operators on a Compact Interval`,
[arXiv:1002.0606](https://arxiv.org/abs/1002.0606),
addresses compact-interval boundary maps and Krein resolvent
formulas. DLMF [33.2](https://dlmf.nist.gov/33.2)
fixes the Coulomb outgoing \(H^+=G+iF\) and Wronskian.
Neither is presented as an external independent proof of
this particular original H-H source-lock constant.

**Next PHYS51 substantive action:** bound or construct the actual
noncentral screened **outgoing** high-\(\ell\) logarithmic
derivative at \(r=27\) and compute/limit its high trace
\(g_T\) from the true physical incoming/outer radiation
condition. Couple that boundary data to the present positive
finite-collar DtN and PHYS46–49 source/Schur machinery.
Further continue the original driven \(\xi=Fy-\phi\),
origin, incoming adjoint, microscopic cross sections and
identical-neutral-H Maxwellian \(k_{\rm HH}(T)\). Until then
physical `HH_R10` production in REI stays **OFF**.
