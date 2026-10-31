# WU R40 | GL2022 original-source-restricted HD vibrational first-hitting kinetics

## Definition and actual source

This is a NEW observable computed from protected WU R36 EMAA 19-level source data, not a new source publication. The user-supplied `214302_1_epaps.zip` contains exactly the original 14-page 2022 supplementary PDF already locked in R36: SHA-256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. GL 2022 *J. Chem. Phys.* 157, 214302 (2022), DOI `10.1063/5.0128598` Eqs. (1)-(4), and Supplement Tables 1-28; Lepers/Guillon/Honvault 2019 MNRAS 488,4732–4739 DOI `10.1093/mnras/stz1797` plus 2021 erratum MNRAS 500,430–431 DOI `10.1093/mnras/staa3146` are references. The 2021 erratum correctly weights H2 para even J' by 1/4 and ortho odd J' by 3/4 for *thermal chemical rates*, not for nonreactive HD vibrational hitting probabilities.

## Model, physical assumptions and derivation

Fix one original source gas temperature T in {15,55,105,255,505,1005,1505,2005,2505,3005} K and a prescribed H+ number density `n=1 cm^-3` for time-unit display. The internal HD rovibrational levels and energies come from the same 19-state subset of authenticated EMAA RADEX `HD.Rovibration.805a7aa5.radex`, SHA-256 `b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94`.

Transient levels U are HD(v=1,J=0..6), seven states. Absorbing destinations A are HD(v=0,J'=0..11), twelve states. Collisional de-excitation rates `k_{u→l}(T)` are preserved at exact original source temperatures. The reverse rates are constructed by thermal detailed balance `k_{l→u}=k_{u→l}(g_u/g_l) exp[-(E_u-E_l)/(k_B T)]` with `g=2J+1` and `E=h c(100 m^-1/cm^-1) E_cm-1`. External radiation, chemical reactions and states beyond HD19 are *not included*, and there is no inference of a full cosmic reaction network. The 19-state collision-only column-generator K has rate units s^-1 at n=1 cm^-3.

For an initial unit transient state, probability density of first absorption in A at time t is `K_AU exp(K_UU t) e_i`. Because the restricted U-subgenerator is transient (all eigenvalues have strictly negative real parts for the evaluated source cases), integrate:

`B = K_AU (-K_UU)^(-1)`; `P(first HD v0 J' | initial v1 J)=B_{J'J}`.  The mean first-hitting time is `tau_i=[1^T (-K_UU)^(-1)]_i`, scaling as `1/n_H+` for collision-only dynamics. The net internal energy release over the entire (potentially multi-step) trajectory is the state difference, `Qbar_i=E_i - Σ_a B_ai E_a`; the intermediate v1-v1 energy exchanges telescope, but Qbar is **not** a full gas heating or reaction enthalpy prediction. Dimensions: B dimensionless, tau in s, Qbar in joules. Boundary `v0` absorbing is an event definition, not a physical assertion that v0 never returns.

Two original-source representations are compared: EMAA direct 171 transition ×25 T data and the protected R36 GL-printed hybrid, which swaps only available and correctly parseable published GL2022 inelastic rate cells at common T, retains EMAA entries for all unprinted or unreliable cells, and independently preserves all 50 source disagreements across seven state-transition groups (no imputation). This is a source-choice sensitivity experiment, not a correction of the owner source. The same baseline comparison in R36 concerned *stationary* 19-state level populations and external radiation, a different observable from first hitting.

The structural unaffected result follows exactly: differences in a transition `v0J2→v0J0` do not alter B because only columns corresponding to U enter K_AU and K_UU. In contrast a `v1J6→v0J10` rate difference changes an exit-channel column of K_AU and the corresponding K_UU diagonal.

## Source thermal audit as distinct restricted task

Supplement Tables 1-10 supply 10 product-J' tables × seven HD reactant J × ten T = 700 printed tokens. A self-contained `pdftotext -layout` parse agrees with all 700 cells of existing R33 source tokens; Table 11 matches its ten printed thermal-rate tokens. For the *j=0..6 printed-source reconstruction only*, use `k^7(T)=Σ_{j=0}^6 [(2j+1)e^{-(E_j-E_0)/k_BT}/Z_7] [1/4 Σ_{j' even} k_{jj'} + 3/4 Σ_{j' odd} k_{jj'}]`. The main article Eq.(5) includes j up to 8; the supplementary says it uses j up to 6. Hence `k^7` is a different observable and differences from printed Table 11 are not unilaterally declared table errors. Twenty-two source tokens `0.00(00)` and equivalent are censored printed numbers, *not physical zeros*; their lower-bound contribution to this displayed truncated sum is set to zero without asserting the actual rate vanishes.

Direct original PDF inspection confirms 10-row duplication for HD j=5 between H2 j'=0 and j'=1 tables, and the anomalous Table 8 HD j=3→H2 j'=7 entry at 2505 K `6.72(16)` against neighboring values. Both remain uncorrected and are reported as source-risk flags. The GL–EMAA 50 rows have **no author-approved correction**.

## Limits and decision

This solves the source-scoped first-hitting calculation, NOT molecular non-Born–Oppenheimer corrections, reactive scattering amplitudes, chemical Q, post-v0 return, cosmic propagation, or the R6/C9 distinct-author gates. Protected canonical DAG 34/49 unchanged. No autonomous further canonical node admission or production issue is authorized.
