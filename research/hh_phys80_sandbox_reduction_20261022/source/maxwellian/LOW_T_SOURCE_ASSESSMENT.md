# PHYS80 — LOW_T_CI_SOURCE_COVERAGE: source decision

Date: 2026-10-22 UTC. Authoring scope: independent source and derivation work.
Inherited science: PHYS79 PR134 head 3304d16db1dc9bf868c185a8eeb6cc9dbc270e50.
No PHYS79 file was changed and no ODE was executed.

## Decision

A constructive next implementation is available: Maxwellian averaging of an explicitly supplied, thresholded electron-impact cross section. Bell et al. (1983), DOI [10.1063/1.555700](https://doi.org/10.1063/1.555700), supplies a cross-section representation and a shifted Gauss–Laguerre formulation. This closes the mathematical route from a declared cross-section model to a number rate and an incoming-electron energy moment. It does not establish physical accuracy at every low gas temperature.

The delivered **generic prototype has no species coefficient table, isotope mapping, automatic admission, cosmological adapter, or cooling adapter**. The input must identify its coefficients and source. The specific H/He/Li source candidates are recorded separately in SOURCE_COEFFICIENTS.json. In particular, the H row has an unresolved original-text versus later-transcription discrepancy. The source table is not executable default data.

Status:

| Obligation | Present result |
|---|---|
| Maxwellian integral, dimensions, threshold, logarithmic calculation | Derived and implemented |
| Explicit Bell-parameter prototype | Implemented |
| Independent pure-A analytic witness | Six new lightweight tests PASS; receipt retained |
| New scalar quadrature workload | 18 order profiles, 36 quadrature sums, 9 E1 evaluations |
| New ODE / inherited ODE replay | 0 / 0 |
| Neutral species admission | NOT_ISSUED |
| Physical low-temperature CI uncertainty | OPEN, specifically near-threshold cross-section behavior |
| Full collisional/thermal closure | OPEN |
| Production admission / HH_R10 | NOT_ISSUED / OFF |

## Primary-source evidence and limits

The original Bell PDF is hosted by NIST at
https://srd.nist.gov/jpcrdreprint/1.555700.pdf .
Its Eq. (1), Table 5 and source discussions were read through extracted primary text. The PDF contains 27 pages including its cover; printed page 910 is PDF index 20. Eq. (5) and the rate-fit domain occur at printed page 911; Eq. (8) and the H threshold discussion at 912; atomic source assessments at 913.

The paper's polynomial rate approximation has domain I/10 < k_B T < 10 I. It is therefore unsuitable for silently replacing Voronov below its published lower temperatures. Directly integrating the cross-section representation is a distinct calculation. The authors also qualify their nominal 67%-confidence uncertainties near threshold. No Table 5 percentage is inherited as a uniformly certified error at 255 K.

Evidence fidelity matters: Exa and another extractor returned primary PDF text, not the original PDF bytes. The web screenshot call exposed textual image placeholders without an accessible image payload. No visual verification, PDF checksum, or original-byte validation is claimed. A later paper, [Haque et al. 2006](https://doi.org/10.1103/PhysRevA.73.012708), transcribes H B1 as -0.00186, whereas the original NIST extraction reads -0.0186. Remaining H coefficient placements agree. The discrepancy is recorded, not resolved by averaging or choosing a convenient value.

Independent primary evidence identifies the physical limitation: [McGowan and Clarke 1968](https://journals.aps.org/pr/abstract/10.1103/PhysRev.167.43) studied H ionization with approximately 0.06 eV electron-energy resolution. The result near threshold approaches a power about 1.13 with stated uncertainty 0.03; even higher powers remain compatible within 0.05 eV. A linear relation is more appropriate farther above threshold. At 255 K, k_B T is about 0.022 eV, so the thermal integral samples precisely this narrow excess-energy region. A numerically precise linear-threshold model cannot erase that uncertainty.

The [NIST BEB database introduction](https://physics.nist.gov/PhysRefData/Ionization/intro.html) provides another primary route for H and He. It describes a nonrelativistic, orbital-parameter model and its usual accuracy, and excludes use above 10 keV. The [atomic inventory](https://physics.nist.gov/PhysRefData/Ionization/atom_index.html) lists H and He ionization data but lists Li only for excitation; Li ionization parameters cannot be inferred from that inventory. Direct links to the H and He total-cross-section CGI returned server errors in this session, so no orbital-parameter implementation was admitted.

[Kim and Rudd 1994](https://doi.org/10.1103/PhysRevA.50.3954) provides the BED/BEB theory and a linear threshold model. [Lotz 1967](https://doi.org/10.1007/BF01325928) and [Lotz 1968](https://doi.org/10.1007/BF01392963) are relevant model alternatives, but the original 1968 full coefficient table was not obtained here. The simple pure-A model used in verification is explicitly an analytic witness; it is not presented as the complete Lotz fit or a universal empirical rate.

## What can be coded now

bell_kernel.py implements an explicit BellParameters record with coefficients in eV^2 cm^2. The B coefficients are an immutable tuple. There are no built-in H, He or Li rows. A caller can examine a chosen model only after providing all parameters and a nonempty provenance label.

The calculation returns 32- and 64-point results, their finite comparison, a finite log rate, representable rate, underflow/subnormal flags, mean incident energy, mean excess energy, and the incident-energy weighted rate. A zero floating-point rate with a finite negative log rate is reported as numerical underflow. It is not substituted for a physically zero reaction channel.

The prototype rejects nonfinite/invalid input and a negative cross section at an evaluated point. It never clips a negative numerator to zero. Positivity at the chosen quadrature nodes is a finite diagnostic, not a proof between nodes. Similarly, order agreement is a numerical comparison, not a rigorous quadrature certificate or a physical source-error bound.

For ground-state nonradiative CI, the net energy transferred out of a shared thermal pool is the chemical ionization defect per event. The incident-energy moment is a diagnostic of which electrons cause the reaction. Outgoing electron kinetic energy remains within the shared pool. The prototype deliberately supplies no cooling shortcut that could confuse these two quantities. Multitemperature transport, escaping secondary electrons, excited products and photons require additional moments and state contracts.

## Uncertainties requiring a concrete next step

1. Resolve H Table 5 against readable original page pixels or an original author table. The generic kernel remains useful while this local transcription issue is open.
2. Establish near-threshold cross-section normalization and shape for each admitted target, including a meaningful uncertainty interval. A fractional power alone is insufficient: its normalization and matching range are required.
3. Preserve isotope thresholds and chemical potentials explicitly. An H cross-section reuse for D/T is an approximation, and the existing 43 k_B D–H chemical defect must not silently become an independently validated isotope-resolved CI model. Threshold shifts enter the low-temperature exponential.
4. For a finite cross-section energy domain, partition the integral and account for the omitted high-energy tail using an explicit bound or declared continuation. Gaussian quadrature to infinity is not itself a bound on unavailable physical data.
5. Keep excited-target, indirect-ionization, resonance and photon branches separate from the ground-state direct model. Li inner-shell/radiative contracts remain open; none of this work promotes their omission to a zero theorem.

The fresh sibling inventory supplied by /root/identity_inventory is consistent with these obligations: REC120 and REI221 add thermal/provider contracts, not a low-temperature CI source closure. Their derivative-of-fit radiative moments also do not inherit independent physical derivative accuracy.

## Verification evidence

One new batch was executed via:

    python /tmp/phys80_sources/verify_bell_kernel.py

BELL_KERNEL_VERIFY_ATTEMPT_001.json preserves the complete attempt.
BELL_KERNEL_VERIFY_RECEIPT.json records the same successful result.
Six unique unittest methods passed. Their grid has nine abstract pure-A U values and two quadrature orders: 18 order profiles, each evaluating a number and first-moment sum, for 36 scalar sums. Nine independent E1 identities were evaluated. These are not ODE histories or new species trajectories.

The largest relative rate discrepancy against the E1 identity was 1.6697754290363748e-13 for order 32 and 1.1368683772160957e-13 for order 64. The corresponding maximum relative mean-excess discrepancies were 3.7181369094696493e-13 and 8.881784197001252e-15. These describe the tested abstract model and finite grid.

The asymptotic E1 remainder field bounds the analytic series truncation only. It excludes floating-point roundoff and constant uncertainties. The direct scipy.special.exp1 route carries no certified library-error bound; the receipt records null for that field.

No production admission follows from these tests.

