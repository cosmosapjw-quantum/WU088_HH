# Numerical design and claims

## Contract
The callable core accepts decimal or rational strings, never an unlabelled binary64 number. It performs exact BigInt rational arithmetic. Column-generator, normalization, sign, dimension and finite state count checks are exact. Decimal inputs define the declared finite rational model; a source's measurement or fit uncertainty is not inferred from arithmetic exactness. Max n=9 in this bounded unit.

## General projection
For x'=Kx-hDx+f, X=1^Tx and r=x-pi X, define Q=I-pi1^T, dbar=d^Tpi, b=Dpi-pi dbar, B=pi d^T-D. Then r'=(K+hB)r+cX+Qf with c=Kpi-piDot-hb. Sum(c)=0. Fixed stationary pi gives c=-hb. Forming B does not add a physical event to the original system.

## Continuous comparison and exact rational enclosure
Set k=h min(d), a=delta(K+hB), q=||c||1, g=||Qf||1, b0=h dbar, s=h osc(d)/2, F=1^Tf. M'=-kM+F, U'=-aU+qM+g, E'=-b0E+sU. Start M>=X, U>=||r||1, E>=|X-Xbar|.

For one constant-coefficient interval of length dt>=0 use Mstar=M+F*dt, C=q*Mstar+g, Ustar=U+C*dt. The endpoint upper bounds are Mplus=M/(1+k*dt)+F*dt, Uplus=U/(1+a*dt)+C*dt, Eplus=E/(1+b0*dt)+s*Ustar*dt. The inequalities exp(-z)<=1/(1+z) and integral_0^dt exp(-a u)du<=dt imply the step bound. It remains valid when a,k,b0 vanish and preserves nonnegativity for arbitrary dt. It is first-order consistent; meshes provide an observed convergence diagnostic for the fixed exact fixture. The step is an upper enclosure of the comparison ODE, not forward Euler applied to the physical population ODE.

## Validation
1. Exact projection on independently assembled 2,3,9-state fixtures.
2. Exact B column conservation, nonnegative offdiagonal entries, common-rate shift, n=1, h=0, constant d, pi with zero components, nonstationary pi and piDot.
3. Analytic 2-state solution and independent Wolfram high-precision comparison; unbalanced formation test prevents omission of Qf.
4. Refinement nsteps8,16,32,64,128,256 of the rational envelope on t=1. Continuous comparison benchmark and physical-model defect remain separate quantities.
5. One native source-conditioned supplied-edge graph built from reused HD T100K para-H2 values. Missing channels are outside the declared graph, not physical zeros. A rational approximation to the conditional Boltzmann weights is explicitly recorded; resulting exact stationary weights belong to that declared approximation. Do not repeat the old54DB/24LTE suite.

No actual GL2022 destruction d, physical consumer clock/density, chemical Q or photon transport is supplied. All physical gates stay unchanged.
