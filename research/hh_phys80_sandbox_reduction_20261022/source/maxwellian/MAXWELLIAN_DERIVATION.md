# Threshold Maxwellian integral and energy moments

This is a derivation for a declared cross-section model, not a low-temperature accuracy certificate. Bell et al. (1983), [DOI 10.1063/1.555700](https://doi.org/10.1063/1.555700), Eqs. (1), (5), (8), supplies the primary representation/integration route. The formulas below are independently derived from the Maxwellian distribution.

## 1. Units and assumptions

Use electron kinetic energy E and thermal energy theta = k_B T in eV. Cross sections have units cm^2 and number rates cm^3 s^-1. Electrons are nonrelativistic and Maxwellian; targets are in the specified ground state and their translational velocity is neglected in this electron-rate model.

Let epsilon_eV = 1.602176634e-19 J/eV and

    C = 100 sqrt(8 epsilon_eV / (pi m_e)).

The factor 100 converts m/s to cm/s. The prototype fixes k_B = 1.380649e-23 J/K and m_e = 9.1093837139e-31 kg. The latter agrees with [NIST's 2022 CODATA electron-mass value](https://physics.nist.gov/cgi-bin/cuu/Value?me). The coefficient C reduces to the paper's approximately 6.692e7 at its printed precision.

The normalized energy density and speed are

\[
f_E(E;\theta)=\frac{2}{\sqrt{\pi}}\frac{\sqrt E}{\theta^{3/2}}e^{-E/\theta},
\qquad
v(E)=100\sqrt{\frac{2\epsilon_{\rm eV}E}{m_e}}.
\]

For a threshold I > 0 and sigma(E)=0 below I,

\[
K(\theta)=C\theta^{-3/2}\int_I^\infty E\,\sigma(E)e^{-E/\theta}\,dE.
\]

The incoming-electron energy moment is

\[
M_{\rm in}(\theta)=C\theta^{-3/2}
\int_I^\infty E^2\sigma(E)e^{-E/\theta}\,dE,
\quad \langle E_{\rm in}\rangle=M_{\rm in}/K.
\]

Its units are eV cm^3 s^-1.

## 2. Bell representation and stable shifted integral

The explicit parameter contract is

\[
\sigma(E)=\frac{A\ln(E/I)+\sum_{j=1}^{n}B_j(1-I/E)^j}{IE},
\quad E>I,\quad n\leq5.
\]

A and B_j have dimensional units eV^2 cm^2. Original Table 5 tabulates mantissas in units 1e-13 eV^2 cm^2; callers must convert them explicitly. The kernel never guesses that scale.

Set U=I/theta and x=(E-I)/theta. Define

\[
F_U(x)=A\log(1+x/U)+
\sum_j B_j\left(\frac{x}{U+x}\right)^j,\quad
J_0=\int_0^\infty e^{-x}F_U(x)\,dx,\quad
J_1=\int_0^\infty xe^{-x}F_U(x)\,dx.
\]

Then

\[
K=\frac{C}{I\sqrt\theta}e^{-U}J_0,\qquad
\langle E_{\rm in}\rangle=I+\theta J_1/J_0.
\]

To avoid an early underflow, compute

\[
\ln K=\ln C-\ln I-\tfrac12\ln\theta-U+\ln J_0.
\]

The implementation additionally divides A and B_j by their largest absolute coefficient, factors that scale into ln K, uses log1p(x/U), and uses compensated scalar summation. The mean excess energy theta J_1/J_0 is returned separately so it is not lost by subtracting two nearby energies.

Both quadratures use positive Gauss–Laguerre weights. The order-32/order-64 difference is a finite comparison; this alone does not bound continuum quadrature error. Checking F_U at the nodes rejects negative sampled cross sections but does not prove positivity on every interval.

## 3. Pure-A analytic witness

For B_j=0, equivalently the explicitly declared one-shell logarithmic model,

\[
\sigma_A(E)=A\ln(E/I)/(EI),\quad
K_A=\frac{CA}{I\sqrt\theta}E_1(U),
\quad E_1(U)=\int_U^\infty e^{-t}\frac{dt}{t}.
\]

Integration by parts proves the identity; no fitted thermal-rate extrapolation is used.

Writing S(U)=e^U E_1(U),

\[
J_0/A=S,\qquad J_1/A=1+(1-U)S,
\]
\[
\langle E_{\rm in}\rangle=\theta(1+1/S),
\quad \langle E-I\rangle=\theta(1+1/S-U).
\]

For U > 600, use

\[
S(U)=\frac1U\left[
1-\frac1U+\frac{2!}{U^2}-\frac{3!}{U^3}+\cdots
\right].
\]

This is an asymptotic expansion. From
\(S=\int_0^\infty e^{-x}/(U+x)\,dx\), a finite geometric expansion with its exact remainder shows that the first omitted factorial term bounds the truncation remainder. Terms are stopped while decreasing. This bound excludes arithmetic roundoff. If the bracket is 1+delta, compute mean excess using

\[
\langle E-I\rangle=\theta\left(1-\frac{U\delta}{1+\delta}\right)
\]

rather than subtracting U from a nearly equal reciprocal. For U <= 600 the oracle uses scipy.special.exp1, and no rigorous error bound is claimed for that library call.

The delivered pure-A witnesses do not fix a physical Lotz A for any species and do not replace the complete Lotz 1967/1968 fit.

## 4. Threshold asymptotics and source uncertainty

For the Bell representation,

\[
F_U(x)=(A+B_1)x/U+O(U^{-2}),
\]
\[
K\sim C\frac{A+B_1}{I^2}\sqrt{\theta}\,e^{-I/\theta}.
\]

More generally, if sigma(E) ~ a(E-I)^p near threshold,

\[
K\sim C I a\,\Gamma(p+1)\theta^{p-1/2}e^{-I/\theta},
\quad \langle E-I\rangle\sim(p+1)\theta.
\]

Thus a linear-threshold model has p=1 and mean excess about 2 theta. A Wannier-type exponent p≈1.127 changes both the algebraic temperature scaling and the selected incoming-energy distribution. The exponent by itself does not provide a usable cross section without a source for its normalization and matching range.

At 255 K, theta≈0.0219742 eV. With the rounded Bell neutral thresholds, U is approximately 619 for H, 1119 for He, and 245 for Li. The relevant excess energies are O(theta), which is why nominal broad-energy fit errors cannot be treated as a blanket 255 K uncertainty.

For a finite supported energy interval [I,Emax], write K=K_supported+K_tail. A conditional tail bound is possible only after specifying an actual envelope sigma(E)<=Smax there:

\[
K_{\rm tail}\leq
C S_{\max}\theta^{-1/2}(E_{\max}+\theta)
e^{-E_{\max}/\theta}.
\]

The formula is a deduction conditional on that envelope; neither small Boltzmann weight nor a truncated numerical integral proves an empirical envelope.

## 5. Incoming energy is distinct from net thermal loss

For a T-independent cross section with fixed target-state weights,

\[
\langle E_{\rm in}\rangle
=\theta\left(\frac32+\frac{d\ln K}{d\ln\theta}\right).
\]

Differentiating under the Maxwellian integral proves this identity. A fitted rate's derivative need not inherit the fit's stated number-rate accuracy.

For a ground-state, nonradiative, single-temperature CI event,

\[
A^q+e\to A^{q+1}+e+e,
\]

the shared kinetic pool loses the ionization defect, not the full incoming energy. The outgoing electrons share the remaining energy and remain part of that pool. With chemical potential b=epsilon·Y and total thermal particle abundance N,

\[
u=\tfrac32 k_BT N,\quad
q=-\sum_r\Delta\epsilon_r R_r,\quad
\dot T=-2HT+\frac{2q}{3k_BN}-\frac{T\dot x_e}{N}.
\]

The final term already accounts for the changing electron count. Adding an extra 3 k_B T/2 per new electron in q would double count that effect. The Bell kinetic threshold and the global chemical defect must have an explicit relationship before using this prototype inside the PHYS79 chemical/PI/RR network. That adapter remains OPEN.

Radiative branches, escaping electrons, multitemperature electron/ion pools, excited products and cascades need their own state or photon-energy contracts. The present M_in is not a substitute for those contracts.

