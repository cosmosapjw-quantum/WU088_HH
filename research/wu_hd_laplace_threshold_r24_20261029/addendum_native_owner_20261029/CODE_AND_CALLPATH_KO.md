# WU R24 add-only typed chemistry call-path evidence

This file is a **review sidecar**, not a new owner integration. Parent PR162 HEAD `2f214319ca8600475b1d4e85d1ca21a0249136a8`, sibling R22 PR160 independently held, original R24 PR163 remains DRAFT/HOLD.

## Pin and actual reachability examined
REC PR157 head `e209cd0180c8bf199fc476c37e3cbf8d50394b6c`:
- `research/program_expansion_20261025/hd_adapter/lamda_hd.py` Git blob `632a8a094e7eedd24a1ec3132fec20765d6e39da`: LAMDA rotational levels; `line_coefficients -> einstein_B` and separate `require_energy_frequency_bridge`, not molecular creation/destruction.
- `research/rec_hd_multichannel_affinity_20261029/code/multichannel.py` blob `029255494bf0a63b93bf8b2715327a8585afb5f3`: 9-level 26-edge Markov generator, not four molecular species.
- `research/rec_hd_cycle_space_20261029/code/cycle_space.py` blob `7421cf7650797243dc5bf3c7abda7ea0b4057a3a`: level-graph cycle algebra, not molecular chemistry IVP.

CR PR124 head `a6b49b352fed31587955d55b1cad30c0b55a81eb`:
- `research/cr_c23e_d43_source_binding_20261024/implementation/dispatch_d_binding.py` blob `7c8b5b608db8bbb8aad44b94ebbc34c83557a31d` dispatches `validate_d_binding.py` (manufactured point states), which calls `d_binding.source`.
- `research/cr_c23e_d43_source_binding_20261024/implementation/d_binding.py` blob `cbd76337f65ca040f8c4b66b46953dde74e6e305`: event named `HD_CX` actually atomic `D0+H+ <-> D+ + H0`, with `43*kB` energy. NO molecular HD or H2 molecular species. A similar chemical event name does not constitute owner ACK.
- `research/cr_c17_species_20261015/src/species_events.py` blob `a5d83dede19d11e4bb0fb4018676613839f8f5c3`: HI/HeI/HeII photoevents, not molecular exchange.
- `history/superseded_v1/hdx.py` is a historical, superseded atomic D/H fit, not an active four-molecular-species owner.

Both reactions conserve H and D nuclei, charge, and particle count but have **different typed species and state identities**; a conservation-only adapter can silently bind the wrong reaction. The isolated `native_owner_gate.py` explicitly checks H/D counts, charge, atom-versus-diatom, v/J state labels, and refuses external Q/ACK certification. It was executed separately with **14/14 normal and 14/14 Python -O**; runtime `assert` guards were replaced with raised exceptions and tested by invalid-species mutations.

**Original source-inclusive supplement** in the user's Library: `/WU088_HH/R24_native_owner_admission_20261029/WU_R24_NATIVE_OWNER_ADMISSION_SOURCE_ORIGINAL_20261029.zip`, 326174 bytes, SHA-256 `e88788f629eaf098073ddbc63a7ffdcded3bca5c7bdfc8124fbbabb7f819e1ed`, 18 ZIP entries, 17 verified SHA-256 payloads, Library ACK `libfile_40f67051a99c8191bb4543b3f4da0046` and successful raw-byte readback. The ZIP includes the actual executable Python source, tests, diagnostic figure and original GL2022 supplementary PDF (SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`). Source ZIP was not altered during Git posting.

**Do not overinterpret:** selected pinned function imports/calls only; not all dynamic native/generated/private call graphs. No named molecular owner ACK, no actual GLS2022 native ionic PES threshold, no physical Q, no REC/CR foreign mutation; R6/C9 NOT_RUN; central DAG 34/49 and historical R23 scoped 18/20 unchanged; production NOT_ISSUED, HH_R10 OFF, full-A not issued, L4 false.
