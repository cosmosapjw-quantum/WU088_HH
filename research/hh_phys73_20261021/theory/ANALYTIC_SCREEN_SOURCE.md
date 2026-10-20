# PHYS73: analytic multipoles of the original screened source

## Result and fixed mathematical target

The source used by the new zero-Dirichlet exterior problem is exactly

\[
 f_{\ell0}(r)=r e^{-r}\sqrt{2\ell+1}\,M_\ell(r),\qquad
 M_\ell(r)=\int_{-1}^1 2(1+1/d)e^{-2d}P_\ell(\mu)\,d\mu,
 \quad d=(r^2+a^2-2ra\mu)^{1/2},\quad a=7/10.
\]

An analytic positive-term formula for every retained multipole replaces
the signed Gauss projection in the default source preparation. This
preserves the complete original screen, its factor 2, and the spherical
harmonic normalization. It also avoids subtracting large positive and
negative quadrature contributions to obtain very small high-order
coefficients. The continuum source norm and omitted-mode bounds in
`ORIGINAL_SOURCE_AND_ERROR_BUDGET.md` remain unchanged.

The auxiliary parameter \(\kappa\) below varies the screening exponent.
Its physical value is 2. It is distinct from the collision wavenumber
\(k=7/10\) and the Coulomb parameter \(\eta_C=-10/7\).

## 1. Yukawa addition theorem and normalization

Define

\[
 i_\ell(z)=\sqrt{\frac{\pi}{2z}}I_{\ell+1/2}(z),\qquad
 \bar k_\ell(z)=\frac{2}{\pi}\sqrt{\frac{\pi}{2z}}K_{\ell+1/2}(z).
\]

In particular, \(i_0(z)=\sinh(z)/z\) and
\(\bar k_0(z)=e^{-z}/z\). DLMF 10.47.7 and 10.47.9 define the
unscaled spherical functions; the explicit \(2/\pi\) above is necessary
when using SciPy `spherical_kn` or DLMF's \(k_\ell\).

For \(r>a\), DLMF 10.60.3 gives

\[
 Y_\kappa(r,\mu):=\frac{e^{-\kappa d}}d
  =\sum_{\ell=0}^{\infty}(2\ell+1)C_\ell(\kappa,r)P_\ell(\mu),
 \qquad C_\ell(\kappa,r)
  =\kappa i_\ell(\kappa a)\bar k_\ell(\kappa r).       \tag{A1}
\]

Its stated addition-theorem condition holds throughout this problem:
\(u=\kappa r\), \(v=\kappa a\), \(w=\kappa d\), real
\(\alpha=\arccos\mu\), and
\(|v e^{\pm i\alpha}|=\kappa a<\kappa r=|u|\).
Legendre orthogonality therefore gives
\(\int_{-1}^1Y_\kappa P_\ell\,d\mu=2C_\ell\).

Because \(\partial_\kappa Y_\kappa=-e^{-\kappa d}\), the original
screen satisfies

\[
 V=2(Y_\kappa-\partial_\kappa Y_\kappa)|_{\kappa=2},
 \qquad
 M_\ell=4(C_\ell-\partial_\kappa C_\ell)|_{\kappa=2}. \tag{A2}
\]

Differentiation is justified directly under the projected coefficient
integral: for fixed \(r>a\), \(d\) lies in the compact positive interval
\([r-a,r+a]\), so the integrand and its parameter derivative are bounded
uniformly for \(\kappa\) in any compact positive interval. This route
does not require an unproved termwise differentiation of the infinite
series.

## 2. Stable evaluation without a derivative cancellation

The modified spherical recurrences in DLMF 10.51.5 imply

\[
 i_\ell'(z)=i_{\ell+1}(z)+\frac\ell z i_\ell(z),\qquad
 \bar k_\ell'(z)=-\bar k_{\ell-1}(z)
                    -\frac{\ell+1}{z}\bar k_\ell(z).
\]

For \(\ell=0\), use \(\bar k_{-1}=\bar k_0\), which also follows
directly from \(e^{-z}/z\). Upon differentiating the prefactor in (A1),
the terms proportional to \(1+\ell-(\ell+1)\) cancel exactly, leaving

\[
 \partial_\kappa C_\ell
 =\kappa\left[a i_{\ell+1}(\kappa a)\bar k_\ell(\kappa r)
       -r i_\ell(\kappa a)\bar k_{\ell-1}(\kappa r)\right].
\]

Thus the implemented moment is

\[
 \boxed{M_\ell(r)=4\kappa\left[
  (i_\ell(\kappa a)-a i_{\ell+1}(\kappa a))\bar k_\ell(\kappa r)
  +r i_\ell(\kappa a)\bar k_{\ell-1}(\kappa r)
 \right]_{\kappa=2}.}                              \tag{A3}
\]

The one subtraction in (A3) is uniformly separated from cancellation.
The positive power series following from the defining \(I\)-series is

\[
 i_\ell(z)=\frac{z^\ell}{(2\ell+1)!!}
 \sum_{m=0}^{\infty}
 \frac{(z^2/2)^m}{m!\prod_{s=1}^m(2\ell+2s+1)}.
\]

Every denominator in the sum increases upon replacing \(\ell\) by
\(\ell+1\). Comparing the positive terms yields

\[
 0<\frac{i_{\ell+1}(z)}{i_\ell(z)}\le\frac z{2\ell+3}.
\]

At \(z=\kappa a=7/5\), this proves for every \(\ell\ge0\)

\[
 i_\ell-a i_{\ell+1}
 \ge\left(1-\frac{a z}{2\ell+3}\right)i_\ell
 \ge\frac{101}{150}i_\ell>0.                       \tag{A4}
\]

The two summands in (A3) are positive. The ratio of the sum of magnitudes
of the two operands of its subtraction to their exact difference is at
most \(199/101\). Thus this subtraction does not have the exponentially
growing relative cancellation of high-order Legendre projection.
This is an algebraic conditioning statement; it does not assign certified
relative errors to a floating Bessel implementation.

For a grid of \(N_r\) radii and modes through L, the values
\(i_\ell(2a)\) and \(i_{\ell+1}(2a)\) can be prepared once. The
remaining formula is evaluated for each radius and mode. It removes the
Q-point angular sum and its O(Q L N_r) multiply-add work. The default
analytical preparation still checks finite positive values and rejects
unhandled range failures. An out-of-range zero is not treated as a
certificate that a physical coefficient vanishes.

## 3. Independent zero-mode identity

At \(\ell=0\),

\[
 C_0=\frac{e^{-\kappa r}\sinh(\kappa a)}{\kappa a r}.
\]

Changing variables from \(\mu\) to \(d\) in the direct integral gives

\[
 \begin{aligned}
 M_0(\kappa,r)=\frac2{ra}\bigg[
 &e^{-\kappa(r-a)}
       \left(\frac{r-a+1}{\kappa}+\frac1{\kappa^2}\right)\\
 -{}&e^{-\kappa(r+a)}
       \left(\frac{r+a+1}{\kappa}+\frac1{\kappa^2}\right)\bigg].
 \end{aligned}                                    \tag{A5}
\]

The actual Wolfram evaluation recorded in
`YUKAWA_SYMBOLIC_AND_SOURCE_EVIDENCE.json` returns `{0,0,0,0}` for:
(A5) minus \(4(C_0-C_0')\), (A3) at \(\ell=0\) minus the same
quantity, the sign of \(\partial_\kappa Y_\kappa\), and the exact
\(101/150\) lower factor. These are independent normalization and
sign checks; no radial or angular campaign is invoked.

## 4. Error interpretation and verification boundary

Equations (A1)--(A5) are continuum identities. The analytic default has
no angular integration truncation error for a retained coefficient.
Its numerical evaluation still has floating special-function and
arithmetic errors. The implementation's high-precision and direct
low-order integral comparisons quantify diagnostics, not interval bounds.
The radial Green quadrature, omitted modes, radial tail and source Born
tail keep their separate meanings.

The exact-node Gauss bound (12) in the source budget remains useful for
the optional Gauss comparator. It no longer describes the default source
preparation. The unchanged source budget is not a finite-grid certificate.
No claim about the missing physical boundary trace \(u(27)\), the
interior matching problem or HH_R10 follows from these source identities.

Primary references, actually fetched through Exa:

- [DLMF 10.60.3: Yukawa addition theorem](https://dlmf.nist.gov/10.60.E3).
- [DLMF 10.47.7: modified spherical i normalization](https://dlmf.nist.gov/10.47.E7).
- [DLMF 10.47.9: modified spherical k normalization](https://dlmf.nist.gov/10.47.E9).
- [DLMF 10.51.5: modified spherical derivative recurrences](https://dlmf.nist.gov/10.51.E5).
