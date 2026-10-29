# WU088_HH R26 | source-locked 700-cell multi-J collision atlas

Theory-first phase P01. Original GL2022 JCP157,214302 supplementary PDF SHA256 a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754; 700 printed rate cells (HD v0,J0..6 -> H2 v0,J'0..9, T 10 nodes). Canonical WU DAG 34/49 unchanged. Parent PR164 24302ab37ecc3b1220fb90a705ed375fe431b54e; sibling R22 PR160 read-only.

The complete original theory and source PDF are preserved byte-for-byte in the immutable P01 Library ZIP; this landing file is a short guide to prevent unreviewed source copies in public Git. Main article Eqs (5)-(7) apply H2 nuclear-spin factors (even 1/4; odd 3/4) to a separate thermal rate; main Eq(5) uses HD J0..8 while the supplement tabulates J0..6, so Table11 cannot be exactly reconstructed from just the 700 entries. Literal anomalies: Table1/Table2 input J5 rows duplicate and Table8 (J3,J'7,T2505K) token 6.72(16); preserve printed bytes, no silent correction.

For a fixed-volume, externally prescribed T, no reverse or level redistribution, let q_JJ'(T) be raw SQM or Eq(6-7)-weighted source-defined rate, K_J=Σq_JJ', y_J=n_HD,J, p=n_H+. Then dy_J/dt=-p K_J y_J, dp/dt=-pΣ K_J y_J, dz_J'/dt=pΣ q_JJ'y_J, dd/dt=pΣ K_J y_J. H,D,charge,particle counts conserve; with collision exposure u=∫p dt, y_J=y_J0 exp(-K_J u). Multi-J temperature-segment order generally changes product and total extent; distinguish from single-J R25. Source rates are computed SQM data; source-native PES asymptotic Q, owner ACK, production and full-A remain NULL/HOLD; R6/C9 distinct-author NOT_RUN.

Detailed original text SHA256 103261f705cb6d28d401ed90efa4f480728d8b091e624931b380b5f6782c5657. Preserve P01 original as separate archive; later code phases add proof/test and do not mutate parent.
