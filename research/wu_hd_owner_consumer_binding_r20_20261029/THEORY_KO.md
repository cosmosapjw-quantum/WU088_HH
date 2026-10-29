# WU R20: 105 K reactive HD owner-consumer binding, theory first

**Authority:** WU088_HH PR156 immutable R19 HEAD `218f353e67ac533b9fb6d54156ec3db6e8827db6`. Parent R18 source PDF SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`; source rate `23/200000000000000000 m³/s` at **105 K**, original specific channel `H+ + HD(v=0,j=2) -> D+ + H2(v'=0,j'=1)`, SQM printed nominal. Previous 24/24, 9/9, 160/160, 3/3 are **historical R19 evidence**, not newly executed results. No population weighting, spin 3/4, source uncertainty or reverse rate is added.

## Actual code search and refusal of false consumers

1. REC Draft PR156, HEAD `8806a4f757d916b6cf040625be931a66e2f0f6fe`: `research/rec_hd_multichannel_affinity_20261029/code/multichannel.py::generate` blob `029255494bf0a63b93bf8b2715327a8585afb5f3` has nine HD rotational states, 8 radiative + 18 collision edges, T nodes 50/100/200 K and collider density in cm^-3. It does **not** implement the four-species reactive exchange. `research/rec_hd_consumer_callsite_20261029/CALLSITE_MATRIX.json` is a scoped nine-callsite audit, not exhaustive negative proof. REC's `hyrec_source_adapter.py::one_photon_planck_null_residual` is a hydrogen one-photon helper, not the reactive chemical source.
2. CR Draft PR121, HEAD `6c3c91f9fd6261b6d79383ef7c5c8de7b6004fb6`: `research/cr_generic_budget_ssp_20261029/generic_budget_flow.py::ExactBudgetFlow` blob `fdde86ca6d57dcd5fcdbd8356825153a5fb65db6` is an exact *finite He high-low event budget* optimizer, not a four-species kinetic RHS. This distinction is source-code verified for the selected file. No whole-repo absence claim follows.
3. Owner ACK has not been provided or independently retrieved. Therefore candidate exact identity does **not** imply admissible cross-repo mutation or physical binding. Other owners' repositories remain untouched.

## General target-coordinate transport theorem (derived)

Let WU source state in order `x=(n_H+, n_HD02, n_D+, n_H2_01)^T` have units m^-3. Its stoichiometric vector is `nu=(-1,-1,1,1)^T`, and its **prescribed** homogeneous proper-time RHS is

`dx/dt = nu k x_1 x_2 - theta(t) x`, `k=1.15e-16 m^3/s` at fixed `T=105 K`.

For a consumer state `y`, let `x = Pi D y`, where `Pi` is an exact species-label permutation and `D` a positive, time-independent diagonal SI conversion matrix. If `s` is an increasing target coordinate and `g(s)=dt_proper/ds>0`, the only matching pullback is

`dy/ds = g D^{-1} Pi^T [nu k (e_1^T Pi D y)(e_2^T Pi D y) - theta Pi D y]`.

For a common density unit, `D=alpha I`, with `alpha=1` for m^-3 and `alpha=10^6` for cm^-3. The reaction coefficient in the latter consumer convention is `k_c=k alpha=1.15e-10 cm^3/s`. Thus `dy_i/ds = g[nu_i k_c y_H+ y_HD - theta y_i]` in source order, then permute outputs. Dividing a source term twice by `10^6`, using `dt/ds` with the wrong orientation, or using a 100 K/200 K HD *rotational* rate changes the physical equation, not merely its units.

The Jacobian is `J_y = g D^{-1} Pi^T [nu k (x_2,x_1,0,0)-theta I] Pi D`. Since `Pi D` is invertible, the eigenvalues for a fixed state are `-g theta` threefold and `-g[theta+k(x_1+x_2)]`. The chemical block is rank at most one. Wolfram on 2026-10-29 returned characteristic polynomial `(lambda+g theta)^3(lambda+g[theta+k(x_1+x_2)])`, trace `-k(x_1+x_2)` for the chemical block, determinant zero, and three conserved left covectors with zero contraction against `nu`. First symbolic query was invalid because `D` is a protected Wolfram symbol; the corrected second evaluation succeeded. This is same-context CAS verification, **not distinct-author R6/C9**.

The left null vectors `w_H=(1,1,0,2)`, `w_D=(0,1,1,0)`, `w_q=(1,0,1,0)` give `d(w^T y)/ds=-g theta w^T y` for homogeneous common units (after permutation). In particular `v(s) w^T n` is constant for `v=exp integral(g theta ds)>0`. The chemical extent solution transported from R19 requires `tau=integral g/v ds`; positivity of `g` and `v` on the *whole integration domain* must be supplied by the owner, not inferred from a positive point sample. A time-varying T(s) requires qualified k(T); the exact fixed-105-K solution is not authorized for such an interval.

## Owner interface requirements and stop condition

A future true consumer must present **actual** repo/path/function/commit/blob and a reachable call graph, names and state order (including rovibrational labels), density interpretation, rate kind/double-counting policy, 105 K temperature-domain certificate, proper-time conversion `g>0`, volume/expansion history and source/energy conventions. A positive clock sample or synthetic unit test cannot certify a real cosmological history. Require independent owner ACK before writing into another repo; never treat metadata declaring ACK as cryptographic/authenticated ACK.

Source uncertainty, reverse reaction, physical `Q_event`, thermal bath, pressure/work and full-A remain separate. In particular, `-Q_event * extent` is only a **formal** chemistry ledger unless actual source-matched level energies have been admitted. No reactive SQM rate is a replacement for the REC LAMDA HD radiative frequencies.

**Decision:** `PASS_DERIVED_UNIT_AND_CLOCK_TRANSPORT` and `HOLD_ACTUAL_OWNER_BINDING`. Canonical science DAG **34/49 (+0)**, R19 workflow **18/20**, R6/C9 independent review **NOT_RUN**, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`.
