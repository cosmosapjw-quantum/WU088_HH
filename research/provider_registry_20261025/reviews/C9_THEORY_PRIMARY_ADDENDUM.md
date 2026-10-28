# C9 addendum: theory equations and corrected primary checker

**The C9 scoped acceptance is unchanged.** No blocking sign, unit, conservation or claim-scope error was found in the reviewed theory note. The corrected primary checker subsequently passed all 20 groups. The independent 448-check result was reused unchanged.

## Theory review

Reviewed source: `REGISTRY_ENERGY_AND_LEPTONS_KO.md`, SHA256 `57e8ba1f483d006fa4bb5b6a363eac991b858f46026636adced52cdb087d7304`. Root may copy these exact bytes into `theory/REGISTRY_ENERGY_AND_LEPTONS_KO.md`. This review independently derives the equations by hand; it performs no numerical Q, rate, uncertainty or radiation integral.

| Equations | Independent finding |
|---|---|
| (1)–(3) |Multiplicity, isotope conservation for chemical events, and baryon/charge conservation for nuclear transmutation are distinct and consistent. A common collider has zero net column entry but remains in the reactant/rate identity.|
| (4) |For a nonconserved reference density the correction is negative: `-x*(dn*/dtau + theta*n*)/n*`. It vanishes under the declared conserved reference-density equation.|
| (5)–(7) |`Z-q` counts bound electrons; electron +1, positron -1, electron neutrino +1 and antineutrino -1 close the stated weak vertices. Atomic tritium retains one spectator bound electron in the illustrated daughter-ion branch. This does not select its real electronic final-state distribution.|
| (8)–(10) |`Mq = M0 - q*me + (B0-Bq)/c^2` has the correct electron-removal sign and restores the bare-nucleus limit. Molecular binding and excitation use a consistent separated-nuclei/electron reference.|
| (11)–(12) |`Q = -c^2*nu^T*M` is positive for rest-mass loss. For a charge-conserving strong nuclear reaction the electron rest-mass terms cancel and `Qbare = Qatom - sum(nu*B0)`. Binding terms remain; weak charged branches need their full species ledger.|
| (13) |Non-rest reservoir increments sum to Q. Removing an incoming photon gives a negative radiation increment. Neutrino rest energy is excluded from its transport energy if it is already in the rest-mass term. An immediate heat allocation is a separate deposition assumption.|
| (14)–(15) |The full covariance quadratic form and the marginal standard-deviation triangle inequality are correct. Their stated premises do not justify an independent-mass covariance or a numerical confidence interval.|
| (16) |The m-body coefficient has units `m^(3*(m-1))/s`; binary `cm^3/s` converts by `10^-6`. Factors for identical reactants depend on whether the provider defines pair encounter, species loss or event count.|
| (17)–(18) |Total RR leaves state weights, cascade yields and spectra unresolved. Equation (18) describes **emitted** photons; escape, absorption and case-dependent effective transport still need the separate radiation/consumer contract.|

The note explicitly preserves the source-only status and synthetic-compiler approval boundary. It does not issue physical rate/Q, energy partition or uncertainty admission. The cited source definitions and separately recovered raw packets remain the provenance inputs; this addendum checks the mathematical signs, dimensions and stated scope.

## Primary checker correction

The original `primary01` failed result and original checker are preserved. Direct diff inspection found exactly one assertion-literal change: the LiH qualifier test now searches for `ISOTOPOLOGUE_CANDIDATE_ONLY` instead of `ISOTOPE`. The actual registry always used the former qualifier for its two model projections and retained null native source isotopes/state.

The final primary result is **PASS: 20/20 groups** with no failed check IDs. Actual `primary02` receipt: CPU 0.260768 s, wall 0.266345563 s, peak RSS 40,536 KiB, exit 0, no timeout. This corrected implementation check does not replay a scientific rate or Q calculation.

| Artifact | SHA256 |
|---|---|
| Final primary results |`8cf1923c726ea9ce23081f49b655310c2de7b4e056c586b45356f6d67aaf8250`|
| Final primary checker |`2336a811e46a3221e08a311c70db82c59974bf41c70a611fb65a4a9d4a8a7a68`|
| Preserved failed checker |`078389146ced0d72f65e8d73550e89e6672ff186ba4ccdc03176dcb29cb2985f`|
| Preserved failed primary result |`54a2e21c0cebf2104ced88c064669a968b63fa12e59575aa94722d9512fed8af`|
| Independent results, unchanged |`d03ed4769cd580fb573c100f9f6392f81193f500d9dd0feb860354d504ec8034`|
| C9 decision extended by this addendum |`7666dc1e17af1c3986dfeaea7499774ef4bc4a94a93031d6061bc057db5e2f8e`|

All nine source/code/registry identities in the independent review's frozen-input manifest still match after the checker correction. No builder, adapter or registry change was required. The initial C9 decision, independent execution receipt and both observed primary outcomes remain separate evidence.
