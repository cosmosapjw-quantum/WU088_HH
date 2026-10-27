# Interval/block implementation

`interval_block.py` uses only the Python standard library. Certified inputs
are integers, `Fraction` values or exact decimal/fraction strings. Binary
floats and booleans are rejected. Returned certificate quantities are exact
rational strings, with arbitrary-size decimal conversion implemented in
chunks so saved large fractions can round-trip without changing Python's
global integer digit limit.

## Formula-to-function map

| Mathematical operation | Callable |
|---|---|
| Range-reduced alternating Taylor enclosure, then outward dyadic squaring | `exp_neg`, `exp_neg_interval` |
| Coordinatewise sharp normalization of positive weight boxes | `normalize_weights` |
| Literal wavenumber/SI Gibbs weights | `thermal_from_levels` |
| Direct Gibbs pair ratio, preserving the shared equilibrium construction | `pair_ratio` |
| Conservative column-generator boxes | `generator_from_offdiagonal`, `exact_generator`, `GeneratorBox` |
| Full reset generator after common-killing extraction | `reset_generator_bounds` |
| Uniformization rate and common lower transition matrix | `uniformization_lower` |
| Positive lower propagator polynomial and pair overlap | `finite_block` |
| Rational endpoint and distinct whole-block comparison updates | `forced_step` |
| Exact coefficients for declared constant synthetic fixtures | `constant_coefficients` |
| Pinned REC parser with new literal thermal/source graph enclosure | `native_hd_source` |

`finite_block` floors every nonnegative matrix product, Poisson-weight update
and weighted contribution to a common denominator `2**bits`. Its matrix is
therefore an entrywise lower bound. Dropping positive terms beyond the
specified degree preserves that direction. The degree is finite and explicit;
no adaptive unbounded search is performed.

`forced_step` requires interval-wide coefficient bounds from the caller. Its
`rho` must belong to the full generator after extracting `kappa`, and the
certificate's block length must equal the update's `H`. The function returns
`endpoint`, `whole_block`, `forcing_bound` and `integral_U_bound`; the endpoint
residual cannot be substituted for the within-block bound. A scalar function
cannot independently verify the provenance of caller-supplied bounds, so
the fixtures and source caller retain that binding in their exported records.

## Prepared primary execution

From this research leaf:

```sh
python3 verification/run_primary.py \
  --input verification/PRIMARY_INPUT.json \
  --output raw/PRIMARY_RESULTS.json
```

The output path is create-only. The runner records source/code/input hashes,
actual CPU/wall time, per-case outcomes and partial failure information. It
has a 58 CPU-second interrupt within the separately declared 60-second new
allowance. Existing physical and scientific campaigns are not invoked.

The fixed input specifies four native-source block cases, three declared
forced mathematical controls of eight blocks each, and one switched
three-state family. Their generated export is consumable by the separate
independent reference without importing this production module. Actual
execution status belongs in the result and execution ledger, not this README.
