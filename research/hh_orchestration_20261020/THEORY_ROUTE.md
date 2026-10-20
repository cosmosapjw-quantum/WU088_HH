# HH outgoing Green operator: precise next all-order obligation

This note derives a conditional remainder formula and an implementable route to its missing operator estimate. It does not report a newly evaluated infinite-angular norm. Its inputs are the actual PHYS63 outgoing construction, PHYS69 all-angular D2, and PHYS71 D3 at PR121 HEAD `a5423e77ff1f3d2e7ea7f5db903fca9e9b2a0477`.

Use the original atomic-unit reduced radial convention, with lengths in a0 and energies in Eh: B=27, k=7/10, E=49/200 Eh, R0=0.7, eta_C=-10/7, outgoing H+=G+i F_C, and Z=+u' u^{-1}. The Hamiltonian is h=−Δ/2−1/r−(1+1/d)e^(−2d), d=|x−0.7 zhat|. In the original scaled radial equation A_lambda=A_0−lambda V, V=2(1+1/d)e^(−2d). The continuation parameter lambda multiplies this original potential; lambda=1 is its unchanged physical value. No temperature or material screening parameter is introduced.

Let G_D^+(E) be the outgoing inverse of A_0 with homogeneous Dirichlet data at B, as defined by PHYS63. Let f_b be the Coulomb outgoing Poisson column with unit original boundary datum b. After the same unitary radial reduction used in the source, take the Hilbert space H=L²([B,∞),dr; l²(angular modes)). V is a positive multiplication operator in the physical angular representation. Define

    K = V^(1/2) G_D^+ V^(1/2),   p_b = V^(1/2) f_b.

The scattering equation u_b=f_b+lambda G_D^+ V u_b becomes w_b=p_b+lambda K w_b for w_b=V^(1/2)u_b. The same boundary derivative identity fixing the PHYS71 positive D3 sign gives

    [Z_lambda−Z_0]_(ab) = lambda B(p_a,(I−lambda K)^(-1)p_b),
    B(p,q) = sum_modes integral p_mode(r) q_mode(r) dr.

B is complex bilinear; it is not a Hermitian expectation. Its absolute value still obeys |B(p,q)|≤||p||₂||q||₂. The coefficients are D_n,ab=B(p_a,K^(n−1)p_b). In particular this reproduces the established D3=Z'''(0)/6 normalization and introduces no extra factor two or factorial. The sign and boundary convention must be taken from the cited original operator, not a free-space replacement.

If an actual bound ||K||≤q with |lambda|q<1 is established, the exact resolvent identity gives

    Z_lambda−Z_0−lambda D1−lambda² D2−lambda³ D3
      = lambda⁴ B(p_a,K³(I−lambda K)^(-1)p_b),
    |R_(≥4),ab(lambda)| ≤ |lambda|⁴ ||p_a||₂ ||p_b||₂ q³/(1−|lambda|q).

This is derived under the stated boundedness condition. K is dimensionless, p norms have units a0^(-1/2), and the remainder has units a0^(-1), matching the saved DtN coefficients. The bound is a global operator route, unlike the completed fixed-entry D3 coefficient. At lambda=0 it vanishes at fourth order. A failed sufficient condition q<1 does not establish a physical no-go or nonexistence.

For implementation, choose an angular projector P_J and Q_J=I−P_J and rigorously bound the four blocks b_XY≥||X K Y||, X,Y in {P_J,Q_J}. If M is the nonnegative 2×2 matrix with entries b_XY, then ||K||≤||M||₂. A finite calculation may supply b_PP, but b_PQ,b_QP,b_QQ require explicit infinite-mode tail estimates for the outgoing Green kernel. Exponentially decaying angular matrix elements and centrifugal radial structure must enter those estimates. The fixed-L64 Coulomb ratio constant cannot replace polynomially growing all-j ratios.

One concrete certificate route is a weighted Schur bound on the actual reduced kernel K(x,y), with positive weight w and the original radial-angular measure. If

    A = ess sup_x [w(x)^(-1) integral |K(x,y)| w(y) dy],
    C = ess sup_y [w(y)^(-1) integral |K(x,y)| w(x) dx]

are finite, then ||K||₂≤sqrt(A C). Apply this either to the whole kernel or separately to the four blocks. Norms must include the full radial exterior and all requested angular modes; no finite mesh maximum is an essential supremum certificate. A split at a validated radial cutoff can reuse exact exponential tail integrals, but the oscillatory Coulomb Green factor must retain a uniform majorant on that tail.

The first unresolved mathematical deliverable is an explicit computable b_QQ and cross-block estimate at the original B,k,R0, together with ||p_20|| and ||p_21||. Once those exist, a small exact/interval calculator can form ||M|| and the above fourth-and-higher remainder. No all-order numerical certification, cross section, or Maxwellian rate is produced by this note. The established D1/D2/D3 values remain usable independently. HH_R10 remains OFF pending the distinct source-driven xi, original incoming-adjoint/origin, sigma(E), and thermal averaging obligations.

Sources actually read: PHYS71 `theory/PROOF.md`, `theory/ANGULAR_D3.md`, `NEXT_DAG.json`, and independent `verification/C9_INDEPENDENT_FINAL_REVIEW.json` at the pinned HEAD. The resolvent algebra and block/Schur reduction above are derived here; the missing infinite-mode constants remain unresolved. No new physical integration or performance campaign was run for this note.
