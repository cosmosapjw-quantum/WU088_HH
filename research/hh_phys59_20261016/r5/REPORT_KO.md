# PHYS59 R5: 원래 비중심 screened exterior의 무한 angular DtN, 음의 에너지에서 구성

2026-10-16 KST. Parent PHYS58 C5-C8 Draft PR100, HEAD `e9a80d7a7280a4b944a7a9d0a2ce3bb4ca971a2f`. 이 연구는 원래 H(1s)+H(1s) spectator의 **실제 off-centre screened potential**, 모든 ell>=0와 m, 모든 P(ell<=20)/Q(ell>=21) 결합을 보존한다. 다만 여기서는 물리적 산란 E=+49/200 Hartree가 **아닌** E=-49/200 Hartree의 *decaying, self-adjoint, off-shell* 외부 문제를 해결한다. 음의 에너지 DtN을 positive-energy outgoing DtN이라고 부르지 않는다.

## 1. Protected input and full actual noncentral exterior

고정 Hamiltonian `h=-Δ/2-1/r-S`, `S(s)=(1+1/s)e^-2s`, `s=|x-(7/10)zhat|`, original `eta=Fy, xi=Fy-phi` preserved; `kappa=7/10`. 원래 frozen complex128 1,386개 NPZ SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d` from previously independently restored PHYS58 capsule, checked byte-exact. Let `B=27 a0`, use reduced radial u=r psi; radial inner boundary `g=u(B)` with weighted angular space

`||g||_X²=sum_(ell>=0,m) (ell+1)|g_lm|²`, and all-sector `X*` dual. For `t in [0,1]`, define on `r>=B`

`A_t=-∂r²+L²/r² + kappa² -2/r - t V`, with **original** `V=2S(r,angle)`. At `t=0` obtain central negative-energy Coulomb, at t=1 obtain actual full off-centre screened potential. This is exactly the original Hamiltonian spectral equation `(2h+kappa²)psi=0`, not a modified angular potential, but it is evaluated at **E=-kappa²/2**, not the scattering E=+kappa²/2.

Let `Z_t(g)=+∂r u_t(B)`, the **increasing-r derivative** (not the positive exterior-domain outward normal), for the unique L2-decaying solution with u_t(B)=g. The `Z_t` are selfadjoint maps `X -> X*`, with `-Z_t` positive energy forms.

## 2. Certified exterior positivity, all angular Poisson trace lifting

At `r>=B`, the exact source-screen pointwise bound is

`||V||_infinity <= delta_160 = [2*(1+10/263)] / sum_(j=0)^160 [(263/5)^j / j!] < delta :=3/10^23`.

This uses only positive rational Taylor coefficients of exp(263/5), no floating exponent bound. The all-angular operator is symmetric and bounded. The 1D diagonal form for every ell is

`q_ell(r)=ell(ell+1)/r²+kappa²-2/r`, and `q_ell-tV >= beta_C-delta`, with

`beta_C=kappa²-2/B=1123/2700`, `beta_C-delta > beta=2/5`.

Choose boundary hat width `w_ell=min(1,B/(ell+1))`, and the real affine lift `v_ell(B+x)=g_ell(1-x/w_ell)_+`. All support on the exterior. Omitting the *negative* `-2/r-tV` yields the rigorous energy upper per |g_ell|²:

`E(v_ell)<=1/w_ell + (kappa²+ell(ell+1)/B²)*w_ell/3`.

For `ell<=26`, divide by ell+1 and bound by
`1+kappa²/3+26/(3 B²)=257021/218700 <6/5`.
For `ell>=27`, bound by
`4/(3B)+kappa²B/(3*28²)=7129/129600<6/5`.

Thus `C_X=6/5` is an exact uniform lift constant. Lax–Milgram, the positive zero-boundary form and energy minimization yield a unique full angular decaying u_t(g), and

`||u_t(g)||_L2² <= (C_X/beta)||g||_X² <=3 ||g||_X²`

for all t∈[0,1], **all ell,m without angular truncation**. Consequently `Z_t:X->X*` is bounded; the square-root boundary form equivalence is inherited from the uniformly elliptic positive form and explicit lift.

## 3. Actual screened exterior DtN difference and source-specific norm

Real Green/Alessandrini identity with boundary convention `Z=+partial_r` is

`<h,(Z_1-Z_0)g> = ∫_B^∞ dr <u_0(h), V u_1(g)>_(S²)`.

No low/high coupling was removed: u_1 is the full all-angular solution of the *original* noncentral screened Hamiltonian. Thus

`||Z_1-Z_0||_(X->X*) <= delta*C_X/beta < 9/10^23 = 9e-23`.

The form difference is also **positive semidefinite** (though nonzero off-diagonals can be positive): since `A_1=A_0-V`, `V>=0`, the zero-boundary resolvent is positive and energy minimization shows `-Z_1 <= -Z_0` as forms. Equivalently the identity can be written with a direct positive term and an additional nonnegative resolvent quadratic term. The operator bound here holds **only at E=-49/200**, with no positive-energy limiting-absorption or outgoing claim. The exact zero-boundary Neumann contraction is at most `delta/beta_C < 10^-20`, but this fact **does not** transfer to the positive real scattering energy without proving the appropriate outgoing resolvent bound.

## 4. Rigorous *nonzero* actual P20/Q21 off-shell boundary DtN, m=0

PHYS58 R5 proved every original Legendre `A_n(r)>0` for all `r>=27`. For real zonal harmonics,

`<Y_{ell,0},P_n(cos theta)Y_{ell',0}> = sqrt((2ell+1)(2ell'+1))*(3j(ell,ell',n;0,0,0))² >=0`.

Therefore original V=2S is a nonnegative matrix in the m0 harmonic channel basis, **including every intermediate ell**. Each scalar central zero-boundary Green kernel is positivity preserving because q_ell>=beta_C>0. The genuine noncentral Lippmann–Schwinger Neumann expansion `u_1=(I-A_{0,D}^-1 V)^-1 P_0g` converges in L2 (operator norm <10^-20) and is channelwise nonnegative for nonnegative m0 boundary data. For g=Y20,0, `u_1,20(r)>=p_20(r)>0`.

Let p_ell(B)=1 be the positive central negative-energy decaying Poisson radial profile. Green's identity gives

`<Y21,0, Z_1 Y20,0> = <Y21,0,(Z_1-Z_0)Y20,0> >=∫_B^∞ dr V_21,20(r) p_20(r)p_21(r)>0`.

A *source-specific exact rational* lower is obtained using only r∈[27,28]:

- For `mu>=1/2`, `s_- -s_+ >=B R/(B+R)` and `S(s_+)-S(s_-) >=2 [B R/(B+R)] exp[-2(B+1+R)]`.
- Hence the actual original first Legendre coefficient has the **uniform** lower `A_1(r)>=(9/8)*[BR/(B+R)]exp[-2(28+R)]` throughout the one-Bohr band.
- PHYS58 `A_n>0` and exact `Gaunt_{21,20,n=1}=21/sqrt(41*43)>1/2` imply `V_21,20(r)>=A_1(r)`.
- Comparison with `p_ell(r)>=exp[-a_ell(r-B)]` where `a_ell²=kappa²+ell(ell+1)/B²<(11/10)²` for ell=20,21 yields 

`<Y21,0,Z_1 Y20,0> > (9/8)[BR/(B+R)]exp[-298/5] > 1701/[2216*3^60] = 1.8107532542396058...e-29`.

Last inequality only uses rational `e<3` and `298/5<60`. This is a fully coupled **actual off-shell DtN P/Q element** with a strict positive lower, not merely the previously established angular multiplication V21,20. No false norm lower for other m is asserted.

## 5. Validation and scope

- Exact source lock and 160-term rational exponent gate checked in Python `Fraction`, 26/26 focused tests PASS, independent connected Wolfram exact rational/3j checks PASS: betaC=1123/2700, two lift maxima 257021/218700 and 7129/129600, `delta<3e-23`, `DtnDifference<9e-23`, m0 nonzero rational lower.
- First focused run had 26 passes plus one warning about a docstring escape; removed warning and replaced a vacuous Wigner identity test by exact SymPy equality. Reran 26/26 with no warnings. Test/producer actual stdout/exit/resource recorded. Full original WU088_HH regression and NCP Rust NOT_RUN; native subagents not available, serial sandbox fallback.
- Background primary sources: variational exterior DtN and Green/Alessandrini identities (Gesztesy et al. `arXiv:1002.0390`, related papers; Alessandrini 1988), PHYS58 multipole positivity and original spectral identities (PR99/100). The current constants and m0 positivity are new source-scoped derivations, not copied literature theorems.
- Scientific admission: **REAL_NEGATIVE_ENERGY_ALL_ANGULAR_ACTUAL_NONCENTRAL_DTN_CERTIFIED**, with `HH_R10=OFF`; physical positive-energy outgoing `Z_S^+(+49/200)`, original driven `xi`, regular origin, incoming adjoint, `sigma(E)`, identical H Maxwellian `k_HH(T)` all OPEN.
