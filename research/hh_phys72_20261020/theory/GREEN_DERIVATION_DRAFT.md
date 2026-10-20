# PHYS72 independent outgoing-Green derivation and audit

This is a new derivation for the actual exterior Coulomb operator. It reuses
the PHYS63 existence/uniqueness and PHYS69 Coulomb normalization, without
repeating a completed numerical campaign. The first proof below independently
checks the shifted Morawetz identity proposed by the multiplier lane. The
second proof was obtained separately from the inherited Gram-transfer lemma.
It supplies a coarser pointwise kernel estimate with an explicit infinite-j
argument. Neither proof identifies a finite-L constant with an infinite-j one.

All displayed radii and wave numbers are in the original atomic coordinates:
B=27, k=7/10, eta_C=-10/7, E=49/200 Hartree. Thus the numerical constants below
refer to this dimensionless-coordinate realization. The physical DtN and its
Born coefficients carry a0^-1. The equation is A0 u=f, with

    A0 = -d_r^2 + J/r^2 - 2/r - k^2,
    J = -Delta_{S^2},  u(B)=0,

and outgoing H_j=G_j(eta_C,kr)+i F_j^C(eta_C,kr). The source symbols eta=Fy
and xi=Fy-phi keep their original meaning and are unrelated to eta_C.

## 1. Actual Green kernel and its sign

For one degree j put J_j=j(j+1), nu_j=k^2+2/r-J_j/r^2, and
f_j(r)=H_j(r)/H_j(B). The outgoing Wronskian is
Im(conj(H_j) H_j')=k. Consequently H_j has no positive-real zero. Let
phi_j solve phi_j(B)=0, phi_j'(B)=1 and phi_j''+nu_j phi_j=0. Then

    G_j(r,s) = phi_j(min(r,s)) H_j(max(r,s))/H_j(B)
             = f_j(r) f_j(s) integral_B^min(r,s) f_j(t)^(-2) dt.

Its first-derivative jump in r is -1 and d_r G_j(B,s)=f_j(s). Therefore
it is the Green kernel of A0, rather than the negative of that inverse.
This is the PHYS69 kernel, with its sign checked from W(phi_j,H_j)=-H_j(B).
It is complex symmetric, not Hermitian. No complex conjugation is inserted
in a Born coefficient's bilinear radial integral.

## 2. Shifted Morawetz identity: a uniform all-angular bound

Start with a smooth compactly supported source containing finitely many
spherical harmonics. The exact kernel above produces a solution smooth on
[B,infinity), outgoing in each of these finitely many channels. All integration
by parts in this subsection is therefore justified directly. Use angular
Hermitian norms for energy estimates, and define

    w = u' - i k u,
    g = 2/r - J/r^2,
    beta = r - B/2.

Here J acts on the angular variable and is nonnegative and self-adjoint.
The differential equation gives w'=-ik w-g u-f. Taking real angular inner
products yields the exact identity

    d_r [ ||w||^2 + <u,g u> ]
       = <u,g' u> - 2 Re <w,f>.

For F_beta=beta[||w||^2+<u,g u>], the coefficient of |u|^2 is

    beta' g + beta g'
      = B/r^2 + (1-B/r) J/r^2.

Therefore

    F_beta'
      = ||w||^2 + B ||u/r||^2
        + (1-B/r) ||J^(1/2)u/r||^2
        - 2 Re beta <w,f>.                                      (1)

Every volume term preceding the forcing is nonnegative for r>=B. This
positivity is uniform in j; it uses the actual centrifugal term rather than
a bound on C_j.

The outgoing phase is kr-eta_C log(2kr)+sigma_j-j*pi/2. Since eta_C=-1/k,
its derivative is k+1/(kr). For each fixed j,

    u_j(r) = A_j exp(i[kr-eta_C log(2kr)+phase_j]) (1+O(1/r)),
    w_j(r) = i A_j exp(i phase(r))/(kr) + O(r^-2).

Thus beta||w||^2 tends to zero and F_beta(infinity)=2||A||^2.
At B, the Dirichlet condition gives F_beta(B)=(B/2)||u'(B)||^2.
The Coulomb boundary contribution at infinity is essential; it does not
vanish just because the solution is outgoing.

Independently, the exact flux identity is

    d_r Im <u,u'> = -Im <u,f>,
    k ||A||^2 = -Im integral_B^infinity <u,f> dr.                 (2)

With the usual inner product conjugate-linear in its first argument,
integrating (1), then using (2), gives

    X^2 + B W^2 + Y^2 + (B/2)||u'(B)||^2
      = 2 Re integral_B^infinity
          f [ beta conjugate(w) + (i/k) conjugate(u) ] dr,       (3)

where the product on the right includes the angular contraction and

    X = ||u'-ik u||_{L^2(dr dOmega)},
    W = ||u/r||_{L^2(dr dOmega)},
    Y^2 = integral_B^infinity (1-B/r)||J^(1/2)u/r||^2 dr.

Set F=||r f||_{L^2}. Since 0<beta<=r, Cauchy-Schwarz bounds (3) by
2FX+2FW/k. Completing the square in X gives

    B W^2 - 2FW/k - F^2 <= -(X-F)^2 <= 0.

Hence the exact weighted resolvent bound is

    ||r^-1 R0^+ f|| <= C_R ||r f||,
    C_R = [1/k + sqrt(B+1/k^2)]/B
        = [1+sqrt(1+B k^2)]/(B k).                            (4)

For the fixed parameters,

    C_R = (10+sqrt(1423))/189
        = 0.2525009112577779329... < 253/1000.                  (5)

The rational endpoint is proved without trusting a decimal square root:
the quadratic B C^2-2C/k-1 evaluated at C=253/1000 is exactly
37701/7000000>0, and this C is beyond the positive root's vertex 1/(Bk).

### Extension to the actual outgoing operator

Smooth compact radial sources with finite angular support are dense in
L^2(r^2 dr dOmega). Applying (4) to differences makes their exact outgoing
solutions Cauchy in L^2(r^-2 dr dOmega). Estimate (3) also bounds the
radiation derivative and local angular energy. PHYS63's established
outgoing limiting-absorption operator agrees with these exact finite-channel
kernels. Its uniqueness, together with the equivalence of r^2 and 1+r^2
on r>=27, identifies the continuous extension with R0^+. Therefore (4)
holds on the stated full angular and full radial domain. No interchange of
an unbounded C_j supremum with a limit is used.

This argument proves a quantitative bound for an already established
outgoing operator; it does not reopen PHYS63 qualitative existence.

## 3. Independent, coarser pointwise all-j kernel bound

The following second proof is useful as an independent check that the
actual kernel can be controlled after an exponential radial sandwich.
It is not required for the sharper result (4).

For j>=20 reuse only the established PHYS69 trace bound at
a_j=(j-1)/k:

    |H_j(r)|^2+|H_j'(r)/k|^2 <= C_j=(800/189)(j+1), r>=a_j.

At a_j the real Gram matrix of (H_j,H_j'/k) has eigenvalues in
[1/C_j,C_j]. On [B,a_j] define the positive backward basis A_j,B_j by
A_j(a_j)=1,A_j'(a_j)=0,B_j(a_j)=0,B_j'(a_j)=-k, each satisfying
y''=p_j y, p_j=J_j/r^2-2/r-k^2>=0. Both are nonnegative and decrease
outward. Define g_j=A_j+B_j, so g_j(a_j)=1 and g_j'(a_j)=-k.
The Gram inequality and the outgoing trace bound imply

    |H_j(s)/H_j(B)| <= sqrt(2) C_j g_eff(s)/g_j(B),
    g_eff(s)=g_j(s) if s<=a_j, and 1 if s>=a_j.                 (6)

Let r=min(r,s). When r<=a_j, phi_j is positive with positive derivative
on (B,r]. The Wronskian with g_j gives

    phi_j(r)g_j(r)/g_j(B)
      = 1/[phi_j'(r)/phi_j(r)-g_j'(r)/g_j(r)].                 (7)

Suppose j>=2kr. Then r<=j/(2k)<=a_j and p_j decreases throughout
[B,r]. Sturm comparison with the constant p_j(r)>0 gives
phi_j'/phi_j>=sqrt(p_j(r)) coth(sqrt(p_j(r))(r-B))
>=sqrt(p_j(r)). This can also be proved without citing comparison:
the quantity phi_j'^2-p_j(r)phi_j^2 starts at 1 and has nonnegative
derivative 2phi_j'phi_j[p_j(t)-p_j(r)]. Since g_j'/g_j<=0,
(6)-(7), together with g_eff(s)<=g_j(r), yield

    |G_j(r,s)| <= sqrt(2) C_j/sqrt(p_j(r)).                    (8)

For j>=20 and r<=j/(2k),

    p_j(r) >= (3/4-1/(kj)) j^2/r^2
             >= (19/28) j^2/r^2.

Also C_j/j<=(800/189)(21/20)=40/9. The squared constant in (8) is
(40/9)^2(56/19)=89600/1539<64. Thus |G_j(r,s)|<=8r throughout
this deep forbidden-region case, including s beyond the turning region.

For the complementary j>=20 with j<2kr=(7/5)r, the inherited ratio
bound in the exact Green formula gives

    |G_j(r,s)| <= C_j^2(r-B)
       <= [(800/189)(7/5+1/27)]^2 r^3 < 37 r^3.               (9)

Finally, the finite-sector PHYS65 Gamma64=32400 is used only for
j=0,...,19. On that finite sector |G_j|<=32400(r-B)<=32400r.
Since r>=27, 32400r<45r^3. This finite-sector statement and the separate
all-j argument (8)-(9) prove the uniform bound

    sup_{j>=0}|G_j(r,s)| <= 45 min(r,s)^3, r,s>=27.            (10)

All signed m multiplicities share the same central radial G_j, so (10)
is also an angular L^2 operator bound on the kernel. No angular counting
factor is required.

## 4. Consequences for the original multiplier

Use the already established pointwise screen bound
0<=V(r,Omega)<=delta exp[-2(r-B)], delta=3e-23. It remains the original
off-center multiplier, with no centralization. Equation (4) gives

    || sqrt(V) R0^+ sqrt(V) ||
      <= (253/1000) sup_{r>=B,Omega} r^2 V(r,Omega)
      <= (253/1000) B^2 delta
      = 5.53311e-21.                                        (11)

The last supremum follows because r^2 exp[-2(r-B)] decreases for r>=27.
As a separate check, (10) and Schur's test give

    || sqrt(V) R0^+ sqrt(V) || <= 45 delta B^3=2.657205e-17.    (12)

Indeed the kernel norm is bounded by
45delta exp[-(r-B)-(s-B)] min(r,s)^3, and
exp[-(r-B)]r^3 is decreasing on r>=27. Both constants are below 1;
the sharper (11) is the selected computational bound.

For the external degrees (21,20), the inherited finite external product
bound C_21 C_20<=5929 gives a screened Poisson-vector product at most
5929delta/2. The Born tail starting at order four at lambda=1 therefore
obeys

    |sum_{n>=4} D_n(21,20)|
      <= (5929delta/2) q^3/(1-q), q=5.53311e-21
      = 1.5065398437838842309...e-80 a0^-1.                   (13)

The multiplier/remainder document owns the detailed Poisson/DtN mapping
and analytic-family conclusion. Equation (13) is a majorant for omitted
exact coefficients; existing finite-precision D1/D2/D3 errors must be
included separately when evaluating a displayed nonlinear response.

## 5. Independent audit result and concrete checks

The audit separately derived w', the shifted multiplier's volume terms,
the nonzero attractive-Coulomb boundary limit, the sign of the flux, and
the positive quadratic root. It found no sign, angular-uniformity, or
domain defect in (1)-(5). Density and PHYS63 uniqueness are the explicit
extension mechanism. Neither a finite radial sample nor a finite angular
cutoff supplies a premise of that proof.

New exact Fraction checks evaluated the rational endpoint residual,
the two pointwise-bound constants, q, and the remainder expression.
Their values are reproduced in the equations above. These are new light
arithmetic checks, not Coulomb evaluations or re-integrations of PHYS71
panels. All original source and evidence bytes are preserved.

PHYS63 and PHYS69 completed states remain reused; HH_R10 stays OFF.
The original driven xi, original incoming-adjoint/origin matching,
sigma(E), and Maxwellian k_HH(T) remain separate obligations.
