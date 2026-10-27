# Theory to implementation and evidence

All scalar science inputs are exact decimal or fraction strings. Declared input exactness does not certify unknown physical inputs.

| Obligation | Callable/file | Scope | Evidence |
|---|---|---|---|
| Exact rational parsing and arithmetic | Rat.of / Rat operations | Declared decimal/rational strings; binary64 numbers rejected; canonical output is rehydratable | results/PRIMARY.json, results/ROUNDTRIP_REPAIR.json |
| Projection and coefficient assembly | coefficients / projectedState / initialBounds | Column K, simplex pi, optional piDot; c=Kpi-piDot-hb | theory/DYNAMIC_LIFT.md and actual exported API in coding/API.md |
| Generator contraction | contractionRate | Column convention, including valid zero instantaneous coefficient | results/PRIMARY.json |
| Comparison enclosure | envelopeStep | Exact endpoint and whole-interval bounds; arbitrary nonnegative dt | results/PRIMARY.json, reviews/R6_FINAL.json |
| Supplied-edge native HD application | source_geometry.mjs | 9-state para-H2 T100K conditional graph; exact rational pi, finite block only | results/HD_GRAPH.json, theory/HD_GRAPH_BLOCK.md |
| Source reuse | authority/reused/ | Exact pinned source/parser bytes; old DB/LTE evidence reused | authority/reused/PROVENANCE.json |

`envelopeStep` returns `.endpoint` and `.interval`. Interval damping must use nonnegative lower bounds; forcing and coupling must use upper bounds. No generic interval-validity oracle is provided. The accepted scope is the stated contract, including this caller obligation.

The primary188 assertions were executed on the original core06d13f...; current core8c8630... additionally accepts its own long canonical rational strings. This is an input-serialization repair with unchanged numeric arithmetic and fixture semantics. Twenty targeted checks plus three independent saved values verify the new behavior. The execution ledger never relabels the original188 as a fresh run of corrected code.
