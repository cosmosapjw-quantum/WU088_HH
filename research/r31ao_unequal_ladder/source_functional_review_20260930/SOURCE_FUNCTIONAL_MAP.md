# SOURCE_FUNCTIONAL_MAP — fixed Frozen107 mixed derivative blocks

## Authority and target

This is a read-only design review of the completed R31AO transaction. No producer, native build, quadrature sample, old postprocessor, or historical test is executed. The inspected source publication is `e89ff30f508731b8e2694d51cef1b3223794af4d`, tree `fc624042129ed3decd9b0e8ed2df64440886cd10`. The original RETURN blob is `d417b95c3c56c767bb546d9304b331fc4d1b93e7`. The consumed scope and its preflight reviewed_commit are unchanged.

Actual source root: `/root/WU088_R31AL_Z075_RUNTIME_20260930`. Original producer archive: `/root/WU088_R31Y_PRODUCER_INTAKE_20260929/WU088_HH_C21_TRANSFER_CP4_20260923.zip`, SHA256 `c10c932a6cdad817982e00920a893733b367827b116d058791bf5aacad517cd9`. File SHA256, bytes, exact archive members, functions and line spans are in SOURCE_FUNCTIONAL_MAP.json. All 34 original SOURCE_CONTRACT_LOCK records were available and matched their pins. Additional donor/input semantics are traced to actual archived files, not substituted implementations. Byte identity does not establish an error bound.

Define I_F as the exact real values represented by the stored FROZEN_INPUTS floating bits, including exponents, orbital coefficients, phase_E, C, pref and v. Define D_col*, D_row* by the continuous ideal mathematical operations below on I_F, at z=3/4, transverse displacement 2, and tau=z/v. This fixes a mathematical target for the archived finite model. Stored pref and v are inputs: do not silently replace them by newly evaluated normalization or physical constants. Accuracy relative to a different ideal physical/input authority I_A requires an additional input-model bound and its own decision. No complete-HH adequacy or invariant-sector proof follows from this definition.

## Donor coefficients, inverse Laplace variables and domain

`r10_blocks.prepare`, lines 41–51, reads CUSP_TRIAL.json polynomial triples and assigns `C[i,j,k]=float(Fraction(c))`. These are direct monomial coefficients of the 107-term donor polynomial in r1,r2,r12, with degree at most eight; they are not exponential-generating coefficients. The normalization pref is prepared from the donor's rational norm certificate. The certificate is input-normalization authority, not a mixed D certificate. The frozen neutral basis is copied, not recomputed. The source uses a 12-primitive Gaussian expansion and s,px,pz channels.

For mu=1 and physicists' Hermite H_i, define unweighted densities

\[
V_i(t)=\frac{e^{-\mu^2/(4t)}H_i(\mu/(2\sqrt t))}
 {\sqrt{\pi t}(2\sqrt t)^i},\qquad U_i(t)=V_{i+1}(t).
\]

For r>0, their exact transforms are

\[
\int_0^\infty U_i(t)e^{-tr^2}\,dt=r^i e^{-\mu r},\qquad
\int_0^\infty V_i(t)e^{-tr^2}\,dt=r^{i-1}e^{-\mu r}.
\]

These follow by (-d/dmu)^i applied to the elementary inverse-Laplace transforms. Their extension through coincident electron coordinates is an integration/limit statement, not a pointwise assertion for V_0 at r=0. Mixed O/G use U_i U_j only. Individual higher-order densities are signed; only the underlying Gauss weights are positive.

`mixed_h.native.nodes` lines 16–19 uses Gauss-Legendre on x in (0,1), then t=x/(1-x), with dt/dx=(1-x)^(-2); there are two variables t,u in (0,infinity). `exact_weights.exact_weights` lines 29–43 already multiplies each density by its transformed quadrature weight. `contract` lines 46–48 forms W_UU,k=U^T C[:,:,k] U, and also VU/UV planes. Do not apply the Jacobian or quadrature weights twice. The historical Cauchy weights in r10_blocks are not the active OD/JVP weight implementation.

There is no explicit finite integration cutoff in these variables. The largest quadrature node is not an integral-tail boundary. OD generates its node/weight arrays through the locked source; JVP reads the archived frozen_grid_n{n}.npz and its UU plane. Their authority remains the original source/grid lock, not a newly regenerated grid in this review.

## Continuous primitive and analytic radial contraction

Let r1,r2 denote electron positions relative to the cusp center and R=(2,0,z). For canonical active=0 set d1=0,d2=-R,q1=0,q2=v; for active=1 set d1=-R,d2=0,q1=v,q2=0. For ell=s,px,pz let P_ell(r1-d1)=1,(r1-d1)_x,(r1-d1)_z respectively. Define

\[
I_{k,\ell}^{a,b}(t,u)=\int_{\mathbb R^3}\int_{\mathbb R^3}
 |r_1-r_2|^k P_\ell(r_1-d_1)
 e^{-a|r_1-d_1|^2-b|r_2-d_2|^2-t|r_1|^2-u|r_2|^2
   +i q_1r_{1z}+i q_2r_{2z}}\,d^3r_1d^3r_2.
\]

The primitive overlap is

\[
N_\ell(a,b)\sum_{ijk} C_{ijk}\int_0^\infty\int_0^\infty
 U_i(t)U_j(u) I_{k,\ell}^{a,b}(t,u)\,dt\,du,
\]

where N_ell=sqrt(2) pref (2a/pi)^(3/4)(2b/pi)^(3/4) times 1,2sqrt(a),2sqrt(a). This uses the existing singlet assignment normalization. G1 and G2 replace I by -partial_(d1z) I and -partial_(d2z) I at fixed q1,q2, including the displacement derivative of P for p orbitals. Smooth Gaussian derivatives and finite donor degree explain this source functional; quantitative bounds for exchanging derivatives/integrals and for its numerical evaluation still need certification.

`h0_fused.geo`, line 15, completes the square with A=a+t, B=b+u,

\[
m_1=ad_1/A+i q_1\hat z/(2A),\quad
m_2=bd_2/B+i q_2\hat z/(2B),\quad
\sigma=1/(2A)+1/(2B),\quad s=(m_1-m_2)\cdot(m_1-m_2).
\]

The dot product defining s is bilinear, not a squared Hermitian norm. Gaussian base factors are (pi/A)^(3/2) exp[-at|d1|^2/A-q1^2/(4A)+i q1 a d1z/A] and the analogous B factor. The radial moment is

\[
M_k(\sigma,s)=(2\sigma)^{k/2}\frac{\Gamma((k+3)/2)}{\Gamma(3/2)}
 {}_1F_1(-k/2;3/2;-s/(2\sigma)).
\]

Use its analytic s derivatives of order zero through two. `h0_fused` lines 28–49 forms E_s=M, E_px=n1x M+(delta_x/A) partial_s M, E_pz similarly, then the analytic d1,d2 derivatives. Lines 54 and `od_run.calc` 15–19 export only O,G1,G2. The implementation internally evaluates additional fields, but no H matrix is exported by the OD command. The VU/UV and foreign-nucleus gamma terms do not enter this mixed O/G/D definition.

## Basis, phase and exact D assembly

`od_run.assemble`, lines 21–36, fixes the 47-row registry to center0 states j=0..23 followed by center1 j=1..23; the duplicated ground row is excluded. j//8 selects s,px,pz and j%8 selects the frozen orbital column. The two columns are the cusp centers c=0,1. Each field contracts 12 by 12 primitive coefficients C_neutral[:,j%8] C_ground[:,0]. The canonical active index is active XOR c. Reflection uses p-channel parity (-1 at c=1); G fields receive an additional minus sign at c=1. These are declared ordering/frame conventions, not a new physical invariance claim.

Set k_c=(+v/2,-v/2)_c, c_z=(+z/2,-z/2)_c, k_a=(+v/2,-v/2)_active, k_b=-k_a, E_N=phase_E[ch], E_I=phase_E[47+c]. Multiply each contracted field by

\[
\exp\{i[2k_c c_z+(E_N-E_I)\tau]\},\quad\tau=z/v.
\]

After these operations define the exact continuous source blocks entrywise by the unchanged source formulas:

\[
D_{col,chc}^*=k_c(G_1^*+G_2^*)+
i[k_c(2k_c-k_a-k_b)-E_I]O_{chc}^*,
\]

\[
D_{row,cch}^*=-k_a\overline{G_1^*}-k_b\overline{G_2^*}
-i E_N\overline{O_{chc}^*}.
\]

D_col is 47x2, D_row is 2x47; units are 1/t_a. O is dimensionless. Source conjugation and row construction are preserved without symmetrizing data or fitting phase. The velocity and phase_E remain the Frozen107 values.

## Independent dotO and implementation arithmetic

`mixed_derivative.jvp.field` lines 13–33 differentiates the completed Gaussian square directly in z, with sigma'=0, s'=2 dz b/B and log(base)'=-2bu z/B-i qb/B. `mj_pair` lines 50–61 uses the UU and transposed-UU contractions. `run.assemble` lines 17–30 handles remote exponent order and parity and returns

\[
\dot O=\mathrm{parity}\,\mathrm{phase}
 [v\,\partial_z O_{primitive}+i(v^2/2+E_N-E_I)O_{primitive}].
\]

It does not construct dotO from D_col+D_row†. Existing O/dotO metric diagnostics and their provenance are retained. The present decision-bound task does not confer their source certification.

Nodes, weights and adapter normalizations are binary64; native Gaussian geometry, compensated sums and fields use longdouble/complex longdouble; radial wide-series basic arithmetic uses binary128 in its declared strip. Actual archived raw arrays are complex256 (16-byte longdouble components with 64-bit significand on this host), distinct from frozen complex128 model-error diagnostics. Compiler/CPU/flags and cached-binary identities are preserved in the original PRODUCER_CACHED_BUILD_IDENTITY and ACTUAL_STAGE_ENVIRONMENT, with no build or native call here.

`radial_wide` uses terminating even polynomials; odd moments use Boys seeds/recurrences on Re(x)>=-0.5, and the generic hypergeometric branch below that. The |Im(x)|>2 series path uses binary128 basic operations. At Re(x)>=64 the complete-Gamma Boys approximation omits exponentially small tails and exp(-x) terms. The real-arithmetic tail lemma and the exact-arithmetic geometric series remainder argument are available; their floating implementation and propagation to the contracted D blocks are not enclosed. Runtime guards and sampled scalar controls do not supply that enclosure. No source identity required for the mapped core functional is missing; quantitative proof obligations are missing as detailed separately.
