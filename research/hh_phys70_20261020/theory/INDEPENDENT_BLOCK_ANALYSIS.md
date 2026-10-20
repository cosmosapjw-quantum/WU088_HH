# Independent HH shifted-block analysis and pinned API reuse

Status: DERIVED_SCOPED; source/API review completed. This document reports algebra and a source read, not a new physical integration or measured speedup.

## 1. Source and scope

The actual HH parent is PR119 HEAD efd1520dfc0643220f729307583ff0bc04b059e9; its numerical source commit is b9f3b2a9419bdafb59dc19a8b80ec611e3a0dada. The reviewed original client is native/phys69_vigilode/src/lib.rs, SHA256 d0f86cf84de9d4437c742fe7518f9ecd88891236987f3a28bb790eb876f0d211. The exact GitHub GET content is retained in intake_opt_20261020/github/content/wu_native_lib.rs.

The dependency was also inspected from the actual fetched local Git checkout. Its HEAD is a21d573980f66fe02891bd216153443b5352f921, not a newer VigilODE research branch or main. No upstream or original HH file was edited for this analysis.

The equations retain atomic B=27, k=7/10, E=49/200 Hartree, radial time tau=65-r, external channels a=21 and b=20, finite L, the original off-center screened potential, and the exact power-of-two A/B and z normalizations. This does not alter eta=F y, xi=F y-phi or Coulomb eta_C=-10/7. PHYS63 remains ESTABLISHED_REUSED and HH_R10 remains OFF.

## 2. Frozen Jacobian and exact block inverse

Write n=L+1. At a fixed tau and state, set

\[
q_j=k^2+2/r-j(j+1)/r^2,\qquad
c_{aj}=2^{80}V_{aj}(r),\qquad c_{bj}=2^{80}V_{bj}(r).
\]

The complex state is (f,g,A,B,z), with n components in each of the first four blocks. The original RHS is

\[
f'_j=-g_j,\quad g'_j=q_j f_j,\quad
A'_j=c_{aj}f_a f_j,\quad B'_j=c_{bj}f_b f_j,\quad
z'=\sum_j A_jB_j/f_j^2 .
\]

All derivatives below are at the same frozen state and time. There are no conjugates. The maps are holomorphic wherever every f_j is nonzero, and their complex differential equals the ordinary real Jacobian action under the existing interleaved real/imaginary storage.

For a direction x,

\[
(Jx)_{f_j}=-x_{g_j},\qquad (Jx)_{g_j}=q_jx_{f_j},
\]
\[
(Jx)_{A_j}=c_{aj}(f_ax_{f_j}+f_jx_{f_a}),\qquad
(Jx)_{B_j}=c_{bj}(f_bx_{f_j}+f_jx_{f_b}),
\]
\[
(Jx)_z=\sum_j\left[
 (x_{A_j}/f_j)(B_j/f_j)+(A_j/f_j)(x_{B_j}/f_j)
 -2(A_j/f_j)(B_j/f_j)(x_{f_j}/f_j)\right].
\]

The shared external channels are not exceptional cases to omit: when j=a, both product-rule terms contribute and give 2 c_aa f_a x_fa. The same holds for j=b in the B row. The z component of x is absent from Jx.

For the shifted problem (I-sJ)x=b, first solve each independent oscillator block:

\[
d_j=1+s^2q_j,\qquad
x_{f_j}=(b_{f_j}-s b_{g_j})/d_j,\qquad
x_{g_j}=b_{g_j}+s q_jx_{f_j}.
\]

Then complete A/B in one forward pass:

\[
x_{A_j}=b_{A_j}+s c_{aj}(f_ax_{f_j}+f_jx_{f_a}),
\]
\[
x_{B_j}=b_{B_j}+s c_{bj}(f_bx_{f_j}+f_jx_{f_b}).
\]

Finally compute the preceding z differential from the already solved f/A/B directions and set x_z=b_z+s(Jx)_z. Substitution into every block gives b exactly in exact arithmetic. In block order ((f,g),(A,B),z), the matrix is block lower triangular; its complex determinant is the product of d_j and its real-embedding determinant is the product of d_j squared. The action uses O(n) arithmetic and storage. It needs neither a dense Jacobian nor Arnoldi basis construction.

This is an exact algebraic action for the frozen Jacobian; binary64 evaluation has rounding error. It is not bit-identical to an iterative GMRES solve and does not imply bit-identical adaptive trajectories.

## 3. Nonsingularity in the intended HH range

For the analytic original q_j, r in [27,65] and 0<=j<=64 give

\[
-374879/72900\le q_j\le 1523/2700.
\]

For negative lower bounds, j=64 and r=27 give the minimum. The source-bound coefficient snapshot has gamma=0.21193756319429014<53/250. Hence, for 0<h<=1/2 and s=h gamma,

\[
d_j\ge1-\frac{(53)^2\,374879}{(500)^2\,72900}
=\frac{17171964889}{18225000000}
>0.94222029569.
\]

The actual L64 request has max_step=0.25, which leaves an even larger margin. All upstream raw-U stage abscissae c_i are in [0,1], so a correctly clipped step within tau in [0,38] keeps physical stage radii in [27,65].

The exact inequality is an analytic range statement, not an interval proof of each binary64 operation in the solver. A runtime denominator/finite check remains necessary, and a broader h or radial domain requires a new bound or typed refusal. Nonsingular oscillator blocks alone do not bound the full inverse norm: the A/B/z couplings can be nonnormal and contain 1/f_j. Reject zero/nonfinite denominators and retain the original state-domain checks.

## 4. Minimal reuse of VigilODE at a21d573

The public API has no arbitrary shifted-solve callback for the protected matrix-free fast path. OdeProblem exposes RHS, JVP, partial_t and Jacobian capabilities. Rodas5pMfFastWorkspace is public and reexported; its attempt, y_new and stage methods are public. Its actual stage solve implementation and its IdentityPreconditioner field are private, and its setters choose existing Krylov/telemetry policies. The earlier interim description of the workspace itself as private was incorrect; the absence of an injected solve hook is the relevant restriction.

The smallest additive implementation is an HH-specific raw-U step loop that calls the existing public coefficient and controller APIs:

- rodas5p_core::rodas5p_coefficients(): source-bound cached eight-stage tableau, a, c_matrix, c, b_code, gamma and gamma_rows.
- rodas5p_integrators::{AdaptiveStepConfig, AdaptiveControllerState, rodas_next_step_after_attempt}: unchanged PI policy and embedded estimator order.
- Original HhModel RHS and explicit partial_tau, or a source-equivalent optimized kernel with its own parity evidence.
- The derived frozen shifted solve in place of GMRES, with true shifted residual diagnostics.

For each raw stage,

\[
(I-h\gamma J_0)U_i=
h\gamma f(t+c_i h,y+\sum_{j<i}a_{ij}U_j)
+\gamma\sum_{j<i}C_{ij}U_j
+h^2\gamma\,(\mathrm{gamma\_rows})_i f_t(t,y).
\]

The accepted candidate is y_new=y+sum b_code_i U_i. The embedded error vector in this transformed storage is U_7. Its WRMS scale is atol+rtol*max(abs(y),abs(y_new)), using real components exactly as the existing client does.

Do not pass raw U stages directly to public finish_step: that routine combines K-coordinate b and btilde weights. Raw U and K are related by the tableau's gamma_matrix, and an unrecorded mix of those coordinates gives the wrong method.

For rejected steps, reusing f0, f_t and frozen J is legitimate only at identical time/state/model data. A changed h changes the shifted inverse; it does not change the frozen Jacobian. A failed refresh must invalidate all cached frozen data before any retry.

The public workspace is useful for one-step parent controls: configure the same GMRES tolerances, set_gmres_into(true), set_ls_workspace(true), call attempt at the same frozen t,y,h, then inspect stage(i) and y_new. This avoids replaying an already completed physical campaign merely to check algebra.

Clock/output collection helpers such as output::represent and OutputCollector are pub(crate). An external HH companion therefore must implement and test its narrow endpoint-only represented-clock contract. It can still call the original PI controller. It must report this as a new specialized driver, not as an unchanged upstream integration function.

## 5. Relation to newer upstream optimization work

PR73 at 3c0157910076ce552283c831c2be000c66671fab specializes banded LU and exact factor reuse. The existing HH MF evidence records zero direct factorizations and zero assembled Jacobians. Those banded benchmark gains are therefore not measurements of the HH bottleneck.

PR74 at 15c43ce76734d0a560fcec5909ac49f1e6f2d347 and PR75 at 6c945b6c6e0e024d8f733c21da8d35fbcc3c5f2a are standalone coupled stage research for autonomous identity-mass ODEs. PR75 changes derivative scheduling after a preserved projected residual. The HH equations here are explicitly nonautonomous and already admit a simpler triangular exact shifted action. The new coupled solver is not a drop-in replacement; its counted work, exact-output controls, and preserved failed speculation are useful benchmarking patterns.

The original upstream pin and protected tableau can be retained for the HH optimization. No approximate stale Jacobian, changed original physics, new all-angular D3 claim or full response certification is needed to evaluate this finite-dimensional kernel improvement.

## 6. Required validation and claim boundary

A meaningful new check must include nonzero complex A and B, shared j=a/b, arbitrary b_z, and q of both signs; testing only the initial A=B=0 state leaves much of the Jacobian unexercised. Compare the action with an independently assembled real Jacobian and retain the actual residual (I-sJ)x-b. A same-frozen-state U-stage comparison against the public parent workspace detects coefficient, sign, f_t and coordinate mistakes.

Finite-L endpoint accuracy can be assessed against already published authoritative enclosures with exact stored-value arithmetic; ordinary RODAS tolerance is not itself a global bound. CPU time, wall time, memory, number of callbacks/shifted solves and parallel worker counts should remain separate. Measured improvements apply only to admitted identical-input comparisons. No physical integration, benchmark, upstream mutation or new global certification was performed by this analysis.

Source references: original HH PR119 source; VigilODE a21d573 crates/rodas5p-core/src/coefficients.rs, fixtures/rodas5p_coefficients_snapshot.json, crates/rodas5p-integrators/src/{problem.rs,rodas5p_matrix_free_fast.rs,sequential.rs,adaptive.rs,output.rs,lib.rs}; latest upstream PR73/74/75 raw sources and COST summaries in the GitHub intake.
