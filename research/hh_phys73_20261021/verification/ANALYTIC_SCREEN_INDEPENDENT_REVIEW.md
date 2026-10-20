# PHYS73 analytic screen source: independent review

Reviewer: optimization_theory, independently of the implementation author.

Reviewed implementation:
`implementation/analytic_screen_source.py`, SHA256
`0353ab972cee0403bd5b4dcb5e864dd07da0aa5aef503924df5dabb561c7bee5`.

## Decision

**PASS for the exact original-source correspondence, normalization,
positive formula and stated diagnostic boundary.**

The code evaluates equation (A3) in `theory/ANALYTIC_SCREEN_SOURCE.md`:
the factor `4*KAPPA`, offset `7/10`, physical screening value 2,
`(2/pi)*spherical_kn`, and the zero-mode `kbar_-1=kbar_0` all agree.
The returned source adds exactly `r*exp(-r)*sqrt(2*ell+1)` and contains
no radial quadrature weights. Thus the source normalization remains the
original reduced m=0 forcing. The collision wavenumber and Coulomb
parameter are separate metadata.

The proof of `i_l-a*i_(l+1)>=101/150*i_l` uses positive series terms.
The implemented lower-factor check 0.67 is deliberately looser and is
correctly labelled a gross-error guard, not an interval guarantee.
Positive-normal checks reject nonfinite, nonpositive and subnormal
values, and the bounded runtime domain is explicit. The source
coefficients are not set to zero on underflow. Code metadata consistently
states binary64 and `certified:false`.

## Independent proof and actual verification evidence

The reviewer fetched DLMF 10.60, 10.47 and 10.51 through Exa and derived
the formula independently from the original potential. A separate actual
Wolfram call compared the elementary zero-mode integral, the Bessel
coefficient derivative, the positive formula and derivative sign. It
returned `{0,0,0,0}`; its exact input/output is in
`theory/YUKAWA_SYMBOLIC_AND_SOURCE_EVIDENCE.json`.

The reviewer read the author's actual `ANALYTIC_SCREEN_CHECK.json` and
matched its source SHA to the current file. It reports four independent
180-digit direct angular integrals and five high-precision Bessel
references at (ell,r)=(0,27),(1,28),(16,44),(64,27),(128,65).
The largest binary64 difference from those five references is
1.987834073364309e-14 relative. The maximum positive-form versus SciPy
derivative-form difference over ell0..128 at r=27,44,65 is
2.246869357236392e-12. Those are distinct diagnostics and are not
interchanged as one uniform accuracy claim.

All387 selected source values are positive normal binary64 numbers;
the smallest is 6.040809277732225e-293. All8 invalid-domain cases were
rejected. The author's elapsed time was 0.3854918269935297 seconds.
These selected checks do not prove a uniform floating error bound over
the full declared domain.

The receipt also exposes the concrete former failure: at ell64,r27,
Gauss128 binary64 projection returned 1.6243403382944696e-37 while the
analytic moment is approximately 9.26315777465742e-109. Its ratio is
1.753549251572089e71. This observation justifies changing the default
coefficient preparation; the optional comparator is labelled diagnostic.

No existing source-budget test or closed campaign was rerun by this
review. It performed source/receipt reads and symbolic identities only.
The author's four new angular checks are source-formula verification,
not PHYS71 panel or inherited-profile reintegration. Old panel/profile
integrations and Coulomb evaluations in this receipt are all zero.

The radial Green application and its continuum reconstruction retain
their own error obligations. This review does not certify the physical
interior trace, the full matched xi, or HH_R10.
