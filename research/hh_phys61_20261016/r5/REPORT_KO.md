# WU088_HH PHYS61-R5: upper-half-plane all-angular actual noncentral screened exterior DtN

## Scope and provenance

Parent WU088_HH PR104 HEAD `94908dce03b7cacf288ed33f916ab4b9f7d3efe7` (PHYS60: **real** positive spectral E=49/200 finite-angular Coulomb-Jost). Original physical frozen 1386 complex128 source `research/hh_phys34_20261015/inputs/FROZEN_U_SUBSET.npz` SHA256 `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`. The source was recovered from the previously independently restored PHYS60 ZIP and hashed byte-for-byte. No original source mutation. Frozen original `h=-Delta/2-1/r-S`, `S=(1+s^-1)exp(-2s)`, `s=|x-(7/10)zhat|`, `eta=Fy`, `xi=Fy-phi` unchanged. No actual original driven solution or physical rate.

The new result is at **complex spectral energy z=49/200+i/100 Hartree**, not the physical real energy. Set `k²=49/100`, `tau=2 Im(z)=1/50`, `B=27`, `u=r psi`. Work on `H=L²([B,∞),ell²(all ell,m),dr)`, with trace `X=weighted ell²` and `||g||_X²=Σ(ell+1)|g_lm|²`. Angular real Y_lm basis, off-centre screened potential couples ell within fixed m and preserves ±m. Retain ALL angular labels and all radial r>=B.

## New source-locked theorem: explicit, all-angular, noncentral, absorptive DtN estimate

Define the **selfadjoint** real zero-boundary Coulomb reference `A^D_0=-∂r²+ell(ell+1)/r²-2/r-k²` (selfadjoint on full H with Dirichlet at B; bounded below), and its complex Dirichlet resolvent `G_C(tau)=(A^D_0-i*tau)^-1`. Since A^D_0 is selfadjoint and `tau>0`, its spectrum is real and

`||G_C(tau)||_(H->H) <=1/tau` for ALL angular modes. This bound does **not** survive as a bounded L² resolvent at tau=0.

The physical original noncentral multiplier is `V=2S(r,theta)>=0`, `s>=B-R+(r-B)=263/10+(r-B)`. A **source-lock exact rational 160-term positive Taylor lower** for `exp(263/5)` yields

`||V(r)||_(S²->S²) <= δ_B exp[-2(r-B)]`, with
`δ_B=2(1+10/263) exp[-263/5] < δ=3/10^23`.

Now prove a *quantitative* all-angular Coulomb Poisson bound. For arbitrary g∈X choose the explicit lift

`v_lm(B+x)=g_lm exp[-a_l x]`, `a_l=(ell+1)/B`, `x>=0`.

By direct integrals, `||v||_H <=sqrt(B/2)||g||_X` and, since

`|ell(ell+1)/r²-a_l²| <=(ell+1)/B²+2ell(ell+1)x/B³`, 

`||(A_0-i*tau) v||_H <= [sqrt(B/2)*(B^-2+2/B+k²+tau)+B^-3/2]||g||_X`.

These follow using `∫exp[-2a x]dx=1/(2a)`, `∫x² exp[-2a x]dx=1/(4a³)`. No angular truncation occurs. Since `sqrt(B/2)<15/4`, `B^-3/2<1/B`, define the conservative **exact rational**

`C_P(tau)=15/4 + [(15/4)*(B^-2+2/B+k²+tau)+1/B]/tau`.

Then `P_C(tau)g=v-G_C(tau)(A_0-i*tau)v` has boundary g, solves homogeneous exterior equation, is unique in H, and satisfies

`||P_C(tau)||_(X->H) <= C_P(tau)`.

At source-lock tau=1/50,

`C_P=224285/1944≈115.37294`, `q=δ/tau=3/(2*10^21)=1.5e-21`.

The original fully off-centre screened Poisson solution is

`P_S(tau)g=[I-G_C(tau)V]^-1 P_C(tau)g`, 

and `||G_C V||<=q<1`; hence all-angular existence is constructive via the L² Neumann series. For smooth boundary data, the **complex bilinear (no conjugate) Green identity** gives

`<h,(Z_S-Z_C)g>_bilinear = ∫_{B}^{∞} (P_C h)^T V (P_S g) dr`.

This extends continuously to `X×X`, giving a bounded `X->X*` difference (the individual DtNs are continuous by standard elliptic forms/trace or via the explicit lift). Therefore

`||Z_S-Z_C||_(X->X*) <= δ*C_P²/(1-q) <4*10^-19`.

The exact rational operator upper `δ*C_P²/(1-q)` and its arithmetic are in `results/UPPER_PLANE_CERTIFICATE.json` and independently verified via Wolfram connector. This is NOT an estimate for `tau->0+`: `C_P(tau)` diverges like `tau^-1` and the bound like `tau^-2`, so it cannot certify real-energy Coulomb limiting absorption.

For the Hermitian, conjugated current, `J(r)=Im <u(r),u'(r)>_(S²)` obeys `J'(r)=-tau||u(r)||²`, and decays at infinity for tau>0. Therefore **at any nonzero g** `Im <g,Z_S(z)g> = tau||P_S(z)g||²>0` (strictly positive but not uniformly coercive in high ell). Do not confuse this with the bilinear identity above.

## Scientific distinctions and dependencies

This result is a mathematical *regularization of positive real-part spectral energy with strictly positive absorption*. It is more physical in angular structure than PHYS60 finite-L since no angular cutoff is imposed, but it is **NOT the boundary value from the upper half-plane**. The actual positive-energy screened outgoing `Z_S^+(49/200+i0)`, limiting absorption with exp-weight or polynomial-weight resolvent, and the sharp interior P/Q Schur remain **OPEN**. PHYS59 negative E=-49/200 was fully selfadjoint/coercive but not physically outgoing; that positivity was *not* carried to PHYS61.

Conjectural next step: obtain weight-space `H_{+a}->H_{-a}` Coulomb outgoing LAP/Poisson bounds independent of tau, then continue the small-screen perturbation and physical full P/Q Schur. A small `sup V` by itself never proves that missing weight-space bound. New original source/resolvent numerical tests are bounded sandbox tasks, not NCP heavy jobs.

## Evidence and original literature

- Fresh sandbox Python3.13, exact `Fraction` source-aware producer exit0, focused 19/19 pytest PASS; file source SHA guard pass; negative tau and smallness guard tests; independent Gauss integral for the exponential lift residual at ell0/1/20/21/64/160.
- Connected Wolfram Language exact rational checks for `C_P=224285/1944`, `q=3/(2*10^21)`, DtN difference `<4e-19`, source original exp160 screen upper PASS. No native wolframscript or NCP run; native subagents unavailable (`NOT_RUN`). Full WU repository pytest NOT_RUN in isolated sandbox.
- Source context: outgoing vs limiting absorption as treated in [Martin, arXiv:1510.03543](https://arxiv.org/abs/1510.03543) and [Ito and Skibsted, arXiv:1804.07874](https://arxiv.org/abs/1804.07874) (not offered as an independent proof of these source-specific constants). Previous PHYS60 physical real-energy finite-L Jost results and NIST DLMF Chapter 33; no mixing on-shell with upper-half-plane.
- Sibling read-only: latest observed REI PR172, BASS_HE PR74, bass_cr PR78. None supplies the microscopic `HH_R10` rate; no sibling repository modifications.

**DAG:** PHYS61_R5_UPPER_HALF_PLANE_ALL_ANGULAR `PROVED_WITH_TAU_POSITIVE`; C5-C8 independent complex Coulomb/finite-grid science `READY`; real real-energy LAP/all-angular screened exterior `OPEN`; physical driven `xi=Fy-phi`, incoming adjoint, sigma(E), identical H-pair Maxwellian k_HH(T) HOLD, REI `HH_R10=OFF`.
