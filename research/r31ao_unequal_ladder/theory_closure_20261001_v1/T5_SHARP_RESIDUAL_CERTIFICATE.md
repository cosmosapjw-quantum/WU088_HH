# T5: final-entry enclosures and asymptotically sharp spectral residuals

Status: **PROVED under premises P1–P6 below; actual-input values not evaluated.** This refines the existing continuous-target plus archived-raw comparison theorem. It changes no scientific source, comparator, tolerance, stored model, or implementation in the prior overlay. All examples below are synthetic exact matrices.

## Fixed objects and premises

P1. The source-bound continuous targets are the existing $C^*=D_{col}^*\in\mathbb C^{47\times2}$ and $R^*=D_{row}^*\in\mathbb C^{2\times47}$ of `source_functional_review_20260930/SOURCE_FUNCTIONAL_MAP.md` and `endpoint_enclosure_review_20260930/EXACT_INPUT_AND_CALLBACK_BINDING.json`. In particular, the stored input values, 47-row registry, phases, normalization convention and final conjugations are unchanged. Set $K^*=(C^*-R^{*\dagger})/2$.

P2. $C_0,R_0$ are fixed exact complex numbers represented by the archived raw bytes, with the separately required historical ABI, ordering and provenance admitted. Define $K_0=(C_0-R_0^\dagger)/2$ **in exact arithmetic**. These are fixed finite-order source outputs, not improving approximations indexed by the enclosure refinement level.

P3. Proven final-entry disks enclose these same continuous targets:

$$|C^*_{ij}-c^C_{ij}|\le r^C_{ij},\qquad |R^*_{ji}-c^R_{ji}|\le r^R_{ji},\quad r\ge0.$$

Every endpoint, center and stated radius is exact rational/dyadic or outward enclosed. The disks include all final assembly, tail, interior and arithmetic uncertainties. Mere midpoint estimates, source byte equality, or a successfully evaluated unvalidated callback do not supply P3.

P4. Center residual norms are enclosed outward, without floating SVD assumptions, using the exact two-column/two-row Gram construction below. The old exact-Gram proof and rational radical algorithm are reused. Denote its certified interval by $[s_-(A),s_+(A)]$.

P5. Every model has fixed independently stored matrices $P_{j,C},P_{j,R},P_{j,K}$. In particular, **do not replace stored $P_{j,K}$ by $(P_{j,C}-P_{j,R}^\dagger)/2$**. Model identity and exact bit interpretation are separate admission premises.

P6. For a limit or finite-accuracy statement, there is a sequence of P3 enclosures with the Frobenius radius tending to zero, its computed outward upper bound $\bar\rho$ also tending to zero, and the center-norm intervals refined so their widths tend to zero. In particular, a fixed nonzero upward radical rounding floor is not retained. T4 supplies the mathematical enclosure construction under its premises. P6 is not a claim that a fixed host wall/memory/precision cap suffices.

## 1. Rectangular complex balls to disks

Suppose one final entry lies in $[x_-,x_+]+i[y_-,y_+]$. Use exact midpoints $c_x=(x_-+x_+)/2$, $c_y=(y_-+y_+)/2$, half-widths $h_x=(x_+-x_-)/2$, $h_y=(y_+-y_-)/2$, and

$$c=c_x+ic_y,\qquad r\ge\sqrt{h_x^2+h_y^2}.$$

Then $|z-c|^2=(\Re z-c_x)^2+(\Im z-c_y)^2\le h_x^2+h_y^2\le r^2$. Take the **upper** endpoint of an outward rational square-root interval for $r$. The disk radius is not $\max(h_x,h_y)$; the corner $3+4i$ of half-widths 3 and 4 requires radius 5. With another exact center, replace each half-width by the maximum distance to its two corresponding endpoints. Conjugation reverses the imaginary interval and preserves disk radius.

## 2. Exact center norm from a 2×2 Gram matrix

For $A\in\mathbb C^{n\times2}$ with rows $(x_i,y_i)$, calculate exactly

$$a=\sum_i|x_i|^2,\quad d=\sum_i|y_i|^2,\quad b=\sum_i\overline{x_i}y_i.$$

The positive semidefinite matrix $A^\dagger A=\begin{pmatrix}a&b\\\bar b&d\end{pmatrix}$ has largest eigenvalue

$$\lambda_+=\frac{a+d+\sqrt{(a-d)^2+4|b|^2}}2,\qquad \|A\|_2=\sqrt{\lambda_+}.$$

This follows by solving its quadratic characteristic polynomial. For $A\in\mathbb C^{2\times n}$, use $A^\dagger$ and hence $AA^\dagger$. The operator norm is unchanged by adjoint. Exact rational products/sums followed by monotone outward square roots give P4; no diagonal omission or symmetrization occurs.

For completeness, the existing integer radical enclosure for $q=u/v\ge0$ takes $k=\lfloor\sqrt{\lfloor q2^{2p}\rfloor}\rfloor$ and encloses $\sqrt q$ by $[k2^{-p},(k+1)2^{-p}]$, with exact rational roots returned exactly. If each square-root interval has width at most $\delta=2^{-p}$, the nested norm interval has width at most

$$w_s\le \sqrt{\delta/2}+2\delta.$$

Indeed the inner radical changes $\lambda_+$ by at most $\delta/2$, and $\sqrt u-\sqrt l\le\sqrt{u-l}$ for $0\le l\le u$; outward rounding of the two outer endpoints adds at most $2\delta$. This bound is valid at zero and at repeated singular values. Thus finite precision can make the center-norm interval arbitrarily narrow without a positive singular-value gap assumption.

## 3. Sharp-centered source-residual theorem

Let a fixed target $D^*$ and fixed raw matrix $D_0$ have one of the shapes above. Given entry disks with center matrix $c$ and radii $r$, put

$$E=D^*-c,\quad A=D_0-c,\quad \rho=\Big(\sum_{ij}r_{ij}^2\Big)^{1/2},\qquad \bar\rho\ge\rho.$$

Then the exact source discrepancy $e=\|D_0-D^*\|_2$ satisfies

$$\boxed{\max\{0,s_-(A)-\bar\rho\}\ \le e\le\ s_+(A)+\bar\rho.}\tag{T5.1}$$

**Proof.** Entry containment gives $\|E\|_2\le\|E\|_F\le\rho\le\bar\rho$. Since $D_0-D^*=A-E$, the two triangle inequalities give $|\|A-E\|_2-\|A\|_2|\le\|E\|_2$. Insert P4 and clip the lower endpoint to zero. This uses Frobenius only for the shrinking enclosure uncertainty $E$, not for the nonzero center residual $A$.

Write $L=\max(0,s_--\bar\rho)$, $U=s_++\bar\rho$, $w_s=s_+-s_-$. Then

$$0\le U-e\le w_s+2\bar\rho,\quad 0\le e-L\le w_s+2\bar\rho,\quad U-L\le w_s+2\bar\rho.\tag{T5.2}$$

The final width bound follows directly before clipping; clipping only decreases width. Therefore under P6, and with the outward $\bar\rho$ refined to zero, both endpoints converge to **the exact spectral discrepancy $e$**.

This theorem does not assert that $e\to0$. The raw $D_0$ is fixed. Target enclosure radii can be zero while $e>0$. The old bound

$$U_F=\left[\sum_{ij}(|(D_0-c)_{ij}|+r_{ij})^2\right]^{1/2}$$

instead tends to $\|D_0-D^*\|_F$, which can strictly exceed $e$. T5.1 is asymptotically sharp; it need not be the smallest possible bound for every finite box. Taking the minimum of independent valid upper bounds $U$, $U_F$, or another certified estimate is allowed. It never licenses subtracting an observed midpoint cancellation from a radius.

**Finite budget implication.** If an allowed error budget is $B>e$, let its strict mathematical margin be $m=B-e>0$. Any refinement satisfying $w_s+2\bar\rho<m$ yields $U<B$. P6 and the explicit radical-width estimate give finite existence. If $e>B$, no valid certificate can give $U\le B$. At $e=B$, arbitrarily narrow intervals alone do not force finite acceptance of a strict test. None of these existence statements guarantees success under a fixed execution cap or supplies the unevaluated actual margin.

## 4. Coupled K enclosure and center cancellation

Set

$$c^K_{ij}=\frac{c^C_{ij}-\overline{c^R_{ji}}}{2},\qquad r^K_{ij}=\frac{r^C_{ij}+r^R_{ji}}2,\qquad \rho_K=\left(\sum_{ij}(r^K_{ij})^2\right)^{1/2}.$$

By P3 and conjugation isometry, $|K^*_{ij}-c^K_{ij}|\le r^K_{ij}$. Apply T5.1 **directly** to $A_K=K_0-c^K$ to obtain $[L_K,U_K]$ for $e_K=\|K_0-K^*\|_2$. This preserves exact cancellation between the two fixed center residuals. No independence of C and R uncertainties is needed; their possible correlation can only make the disk enclosure conservative.

The separate-block bound remains valid:

$$e_K\le(e_C+e_R)/2\le(U_C+U_R)/2.$$

Consequently one may choose $\epsilon_K=\min\{U_K,(U_C+U_R)/2\}$ and $\epsilon_{Dmax}=\max(U_C,U_R)$. Minkowski also gives $\rho_K\le(\rho_C+\rho_R)/2$. The direct K upper bound converges to $e_K$, whereas the separate-block expression generally converges to $(e_C+e_R)/2\ge e_K$. This theorem constructs **raw and target K only**; stored model K remains P5's independent field.

## 5. Direct target model-error/gap intervals and intersection

For every fixed model $j$, apply T5.1 with $D_0$ replaced by its stored $P_{j,C}$, $P_{j,R}$ or $P_{j,K}$ and the corresponding target disks. This yields target-error intervals $I_{j,C}^*,I_{j,R}^*,I_{j,K}^*$. The Dmax error interval is

$$I_{j,Dmax}^*=[\max(L_{j,C},L_{j,R}),\max(U_{j,C},U_{j,R})].$$

No fixed active block is assumed: max is 1-Lipschitz in the coordinate sup norm. For local model $l$ and other model $o$, the unchanged other-minus-local gap satisfies

$$g_m^*=e_{o,m}^*-e_{l,m}^*\in I_m^{direct}=[L_{o,m}-U_{l,m},\ U_{o,m}-L_{l,m}].\tag{T5.3}$$

Use local R31AK and other R31Z for PRIMARY; use local R31AK and other R31AD for SECONDARY, exactly as in the existing Gram contract.

Independently, if $I_m^0=[g_-^0,g_+^0]$ encloses the exact represented raw gap, reverse triangle and the max property give $|e_{j,m}^*-e_{j,m}^0|\le\epsilon_m$ for **each** model, hence

$$g_m^*\in I_m^{raw}=[g_-^0-2\epsilon_m,\ g_+^0+2\epsilon_m].\tag{T5.4}$$

Both intervals concern the identical scalar $g_m^*$, so their intersection is valid:

$$I_m^*=I_m^{direct}\cap I_m^{raw}=[\max(L_{direct},L_{raw}),\min(U_{direct},U_{raw})].$$

An empty intersection is a premise/identity/arithmetic failure requiring investigation, not a permissible choice of the preferred interval. Do not add the two uncertainties, and do not add old X0…X8 producer terms or a legacy diagnostic $\eta$ to this direct target comparison. Those would count the same discrepancy again. A separately labeled diagnostic audit may retain its own $\eta$; it does not alter T5.3–T5.4.

Under P6 each direct model-error interval, its Dmax interval and the direct gap interval converge to their exact target quantities, by T5.2, the max property and interval subtraction. Their valid intersections do too. The raw perturbation interval alone need not collapse because its $\epsilon_m$ can have a nonzero source-error limit. Thus direct target error intervals can resolve a strict target gap even when the raw perturbation route is unnecessarily wide. This is the same fixed-model/continuous-target theorem, without changing the frozen comparator's machine semantics. Admission to an original floating predicate still requires its separate rounding/tolerance proof.

**Explicit accuracy allocation for the fixed 47×2/2×47 shapes.** If every final C/R disk radius is at most an exact rational $r$, then $\rho_C,\rho_R,\rho_K\le\sqrt{94}\,r\le10r$. For this allocation, explicitly choose the exact rational upper bound $\bar\rho_C=\bar\rho_R=\bar\rho_K=10r$ in T5.1; do not assume a separately rounded radical upper endpoint is at most $\sqrt{94}r$. If each required center norm interval has width at most $w$, every model's K-error interval has width at most $w+20r$. The same bound holds for its Dmax-error interval: the width of $[\max(L_C,L_R),\max(U_C,U_R)]$ is at most the maximum of the two input widths. Thus each direct gap interval has width at most

$$2w+40r.\tag{T5.5}$$

Suppose the exact target gaps have an admitted positive margin $m$: every required weak real comparison has $g_q^*\ge-\mathrm{tol}+m$, and a required strict improvement has $g_q^*\ge\mathrm{tol}+m$. Choose $r\le m/160$ and $w\le m/8$. T5.5 is at most $m/2<m$. Therefore every interval lower endpoint satisfies its weak test and the selected lower endpoint satisfies the strict test. T4 supplies final disks at this requested radius; the radical-width construction supplies finite $w$. This is an explicit finite mathematical procedure conditional on the genuine target margin, not a prediction that that margin exists for the archived models. Original machine predicates require their own rounding margins. Equality boundaries have no positive-margin guarantee.

## 6. Exact synthetic witnesses

Let $a=1/1000$, $B=1/800=5a/4$, $D^*=c=0$ and $D_0=aI_2$ (embed the two rows in 47×2 with zeros if desired). The Gram matrix is $a^2I_2$, so $e=a$. With zero radii, T5.1 returns exactly $[a,a]$ and satisfies $U<B$. The old $U_F=\sqrt2a$ fails because $2a^2>B^2=(25/16)a^2$. Target radii are already zero and $e$ is still nonzero.

For all four 2×2 radii $r=a/100$, $\rho=2r=a/50$ and the same exact target is contained. T5.1 gives $U=51a/50<B$. The old squared upper bound is $2(a+r)^2+2r^2>2a^2>B^2$. The improvement is therefore not confined to the degenerate zero-radius case.

For K cancellation, choose $C_0=aI_2$, $R_0=aI_2$, and $C^*=R^*=c^C=c^R=0$ with zero radii. Then $e_C=e_R=a$ but $K_0=K^*=c^K=0$, so $U_K=0$ while the separate-block bound is $a$. A synthetic model with $P_C=P_R=0$ and independently stored $P_K=2aI_2$ has target K error $2a$; rebuilding its K from model D would incorrectly report zero.

The executable checks in `theory_checks/t5_sharp_residual.py` use exact `Fraction` arithmetic and the immutable exact Gram/radical engine on synthetic matrices only. They do not implement or replace a production certificate route. Actual target disks, raw/model values, error budgets, gaps, $\epsilon$ and $\eta$ remain unevaluated; `rigorous=false` for the actual scientific result.
