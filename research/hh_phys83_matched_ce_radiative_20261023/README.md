# PHYS83 — matched H I CE and optically thin radiative energy accounting

## S0 source and physics contract checkpoint

Parent actual HEAD: `ca9d53983459ea08f9992a8a24663e46b7180344` (PHYS82 Draft PR138).

This unit constructs a source-native H I LS 1s/2s/2p finite-support collision operator, a frozen-temperature/electron-density exact local population step, and separate thermal/atomic/radiative energy ledgers. The common positive W-PL kernel preserves paired finite-model detailed balance. The 2s two-photon and known small M1 branches are both included; 2p E1 is included. Each radiative event transfers the source-native 10.20435 eV gap in total.

The source investigation, scoped current-reference intake and constructive derivation are available here. Seven named Wolfram symbolic checks return zero. At this checkpoint no numeric implementation test or scientific profile has run. In-progress implementation is intentionally outside this source checkpoint. Subsequent stage records will distinguish code validation, new science, publication and backup.

Missing finite-splitting 2s/2p mixing, higher levels/cascades, absorption/stimulated emission/trapping, coupled T and charge, He/Li sources and nuclear closure remain OPEN. High-density results, once run, will describe this formal star subset. A held-temperature energy exchange ledger is not an evolved gas-temperature history. Source-native LS gaps are not isotope-resolved spectroscopy.

The accessible-current intake is bounded: six relevant repositories with five recent PRs each, eight actual refs, five descendant comparisons, three trees; the preceding 51-repository/2175-branch inventory is reused by identity. Unavailable private conversations were not surveyed. Existing completed science is not re-executed.

Non-tilted LRS Bianchi I; reacting gas pi=0 and collisionless-DM pi_m remain distinct. Sum signed tensors in the same normal orthonormal frame before taking their norm. Frobenius=sqrt(2)*half-contraction. HH_R10=OFF. Production admission NOT_ISSUED.
