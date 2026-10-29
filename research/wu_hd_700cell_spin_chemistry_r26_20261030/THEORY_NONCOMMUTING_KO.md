# R26 physical derivation addendum | Two-temperature multi-J reaction ordering

Consider positive density p=n(H+), y1=n(HD,J1), y2=n(HD,J2), and two piecewise constant temperature stages A,B with K_A=(k1,k2), K_B=(l1,l2), all m³/s. The restricted irreversible forward reaction source vector field is

\[
F_A(p,y_1,y_2)=(-p(k_1y_1+k_2y_2),-pk_1y_1,-pk_2y_2),\qquad
F_B(p,y_1,y_2)=(-p(l_1y_1+l_2y_2),-pl_1y_1,-pl_2y_2).
\]

Fix the commutator convention `[F_A,F_B] := (D F_A)F_B - (D F_B)F_A`. Exact differentiation gives

\[
[F_A,F_B]=p y_1y_2(k_1l_2-k_2l_1)(0,1,-1).
\]

Thus the second-order ordering term is composition-changing, but its proton and summed-HD components vanish. The total conversion can acquire ordering dependence only at higher degree (or through longer histories), not at the leading mixed second-order commutator. If k1*l2 = k2*l1, e.g. the two temperature rate vectors are proportional, this bracket vanishes and their flows commute. For a single initially occupied HD state, one obtains the R25 special case of total conversion depending only on integrated exposure; product branching may retain order dependence. These are precise model-specific statements, not an unrestricted chemical kinetics theorem.

For the source-qualified examples, select only original HD J=2 and J=4 inputs (do not use flagged J=5 or censored 15 K). Their K ratios between 105 K and 255 K are not proportional, and explicit finite-time noncommutation is supported by source-derived output and an independent direct ODE trajectory check.

Verified same-author by Wolfram Jacobian algebra and SymPy 1.14.0 separate symbolic evaluation. Under this model: p−(y1+y2) invariant, H/D/charge/particle conservation, positivity if p0>y1,0+y2,0. Computational stage uses m³/s source units; nuclear-spin Eq(6-7) weighting is a separate alternative policy, not a stochastic uncertainty range. Endothermal threshold Q and bath remain NULL.
