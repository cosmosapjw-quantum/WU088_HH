# PHYS60 R5: 양의 에너지 원래 비중심 screened 유한-angular Coulomb Jost / outgoing boundary DtN

2026-10-16 KST. Parent WU088_HH PHYS59 PR102 source head `f6e678156102332e3300a188529f37a1736fdacc`. 원래 spectator `h=-Δ/2-1/r-(1+s^-1)exp(-2s)`, `s=|x-(7/10) zhat|`, `kappa=7/10`, Coulomb eta_C=-10/7, 원래 eta=Fy, xi=Fy-phi 보존. Spectral E=+49/200 Hartree (PHYS59 negative E와 구분). Original 1,386 complex128 NPZ SHA `f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`, sandbox에서 실제 파일 해시 확인. `rei_bianchi HH_R10=OFF`.

## 정리 (고정된 임의 유한 angular Galerkin cutoff L)

모든 정수 L>=0, 모든 signed m, |m|<=ell<=L. 원래 potential의 **전체 진짜 angular multiplication matrix** `V^L_ij(r)=<Y_i,2S(r,mu)Y_j>`를 각 m에 대해 사용한다. 축대칭이므로 m이 보존되고, 각 블록은 실수 대칭이다. 이는 finite angular Galerkin projection이지 원래 무한 L 모델 그 자체가 아니다. `r>=B=27`, reduced radial ODE는

`u''+[K²+2/r-ell(ell+1)/r²]u+V^L(r)u=0`, `K=7/10`.

1. 원래 source 그대로 `||V^L(r)||<=2(1+1/(r-7/10))exp[-2(r-7/10)] <= δ_B exp[-2(r-B)]`, `δ_B=2(1+10/263)exp[-263/5] <3×10^-23`. Exact source-locked Fraction Taylor160 bound executes. 따라서 `∫_B∞||V^L||dr<=δ_B/2`이며 **L과 독립**이다. 단 Coulomb reference function의 경계 진폭 상수는 L과 함께 증가할 수 있다.
2. DLMF §33.2–33.4의 `H_l^+=G_l+iF_l`, `H_l^-=G_l-iF_l`로 `W_r(H_l^-,H_l^+)=+2iK`. Fixed finite L에서는 모든 r>=B에서 `H_l^±(r)`가 bounded다 (finite radius compact+large-r asymptotic), 그래서 Volterra row kernel

`K_l(r,t)=[H_l^+(r)H_l^-(t)-H_l^-(r)H_l^+(t)]/(2iK),   B<=r<=t`

는 고정 L에서 유한 균일 상수 `C_L`를 가진다. `K_l(t,t)=0` 및 `∂_r K_l(t,t)=1`, `(∂r²+q_l) ∫_r∞ K_l(r,t)V(t)u(t)dt=-V(r)u(r)`.

Outgoing Jost fundamental solution `U_L(r)`은 `U_L=diag(H_l^+)+∫_r∞ K(r,t)V^L(t)U_L(t)dt`의 유일해다. Volterra n차 반복은 `[C_L ∫_B∞||V^L||]^n/n!`에 의해 수렴한다. **No smallness assumption beyond integrability is needed at each fixed L**. H+ outgoing amplitude identity normalized to I.
3. Hermitian real V에서 `J=Im(u†u')`는 일정하며 모든 outgoing solution의 `J(∞)=K||a||²`. 만약 `U_L(B)a=0`라면 `J(B)=0`이므로 `a=0`; U_L(B) invertible. 경계 map `Z_L^+(B)=U_L'(B)U_L(B)^-1`는 모든 g에 대해 정의되고

`Im<g,Z_L^+ g>=K||U_L(B)^-1g||²>0 for nonzero g`.

4. Bilinear Green identity는 `h^T(Z_{S,L}^+-Z_{C,L}^+)g = ∫_B∞ [P_{C,L}^+(r)h]^T V^L(r)[P_{S,L}^+(r)g]dr`. 두 함수 모두 outgoing이므로 무한 경계의 bilinear Wronskian term이 0이다. **복소켤레가 아닌 transpose**를 사용해야 reciprocal *complex-symmetric* Born expression과 일치한다. `Im(g†Zg)`는 별개의 conjugate-current identity이다.

## 중요한 제한

이 정리는 임의 유한 L (각 m 유한 차원)에 대해 실제 exterior screen을 전 반경 r>=B 포함한다. 하지만 L→∞의 uniform Poisson/LAP, `X=H^(1/2)->X*` boundedness, full infinite-angular screened `Z_S^+`, 정량 Jost-inverse, 실제 low-to-high scattering `xi=Fy-phi`, regular origin/incoming adjoint, `sigma(E)`, 동일 H쌍 Maxwellian `k_HH(T)`는 **OPEN**. 기존 PHYS55 양의 에너지 hybrid collar+central exterior, PHYS59 음의 에너지 all-angular 실제 exterior와 혼동하지 않는다. PHYS58의 exact angular multiplication 상계는 Volterra의 V 부분만 재사용하고 Coulomb H_l 고차 growth를 숨기지 않는다. 높은 l에서 `C_L`의 무한 균일 상수는 존재한다고 주장하지 않는다.

## 실제 검증

`src/wu088_hh/phys60_finite_jost.py`, `scripts/phys60_finite_jost.py`, `tests/test_phys60_finite_jost.py` 신규. Original SHA guarded real source. `python -m pytest -q` **29/29 PASS** exit0, producer exit0; output/exit/resource files stored. 직접 원래 off-centre V 128/160/192 quadrature m0,m1,m2,m20, signed-m parity, positive definite Gram, H+ exact recurrence+positive Wronskian 75dps, Volterra kernel diagonal & real checks included. Connected Wolfram independent exact Taylor160/physical E/Hermitian flux arithmetic PASS. This does **NOT numerically solve U_L beyond first Volterra identity**; the nonperturbative R5 statement has a mathematical Volterra/fixed finite L proof, numerical Jost matrix is next computational step. Full WU suite NOT_RUN, NCP NOT_RUN, native subagents NOT_RUN.

## Literature and cross-repo intake

[DLMF 33.2](https://dlmf.nist.gov/33.2), [DLMF 33.4](https://dlmf.nist.gov/33.4); Rakityansky & Elander [2013, DOI:10.1063/1.4853855](https://doi.org/10.1063/1.4853855) multichannel Coulomb-tail Jost analytical structure and [Rakityansky et al. 1998, arXiv:nucl-th/9808034](https://arxiv.org/abs/nucl-th/9808034). These contextualize construction, not a source-specific independent proof. Latest sibling rei_bianchi PR171, BASS_HE PR74, bass_cr PR77 are different H/He cosmological native consumer tracks; none furnish source-locked actual positive-energy H-H rate. No sibling mutation.

## DAG: positive transition

R5 FINITE_L_OUTGOING_EXISTENCE_AND_FLUX_PROVED → C5–C8 R5-first-Born complex physical P20/Q21 numerical witness READY → PHYS61 all angular uniform outgoing LAP/Poisson HIGH_PRIORITY_OPEN → driven/observable HOLD, HH_R10 OFF.
