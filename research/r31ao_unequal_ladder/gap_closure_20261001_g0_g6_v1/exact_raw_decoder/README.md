# Exact represented-array decoder (G2)

Implemented and tested on synthetic fixtures only. B03 as a whole remains
`RAW_ABI_AUTHORITY_BLOCKED`; no B192 or frozen-prediction values were decoded.

From the containing loop directory:

```sh
python -m unittest exact_raw_decoder.test_decoder -v
```

`decode_npy_bytes(data, *, authority=None, max_elements=1000000)` returns
`DecodedArray.shape`, `.values_c_order`, `.canonical_sha256`, `.raw_npy_sha256`,
`.payload_sha256`, `.header`, `.negative_zero_c_order`, and
`.padding_hex_c_order`. Real values are `Fraction`; complex values are pairs of
`Fraction`. There is no conversion through a host floating type in the decoder.

The supported subset is explicit-endian NPY v1.0/v2.0/v3.0 `f8/c16`, plus
`f16/c32` only with a `LayoutAuthority` bound to the exact NPY member SHA256.
Native `=` or byte-order-free `|` descriptors, object/record dtypes, arbitrary
integer metadata, nonfinite values, trailing bytes, malformed headers, and
unsupported extended layouts fail closed. Select only floating matrix members
from an NPZ; this module deliberately does not load every ZIP member or pickle.

The extended dispatch options are x87 extended (64-bit explicit significand,
15-bit exponent, exponent bias 16383; 10 meaningful bytes within each declared
16-byte component), and IEEE binary128 (113-bit implicit significand). An
authority states component order, endian, meaningful-byte offset, evidence
identity/hashes, scope, and exact member-byte binding. Complex components are
contiguous real then imaginary. x87 pseudo-denormals and unnormal/reserved
patterns are rejected rather than normalized implicitly. The meaningful bytes
may have explicit leading/trailing padding; raw padding is retained unchanged.

`LayoutAuthority` checks consistency, **not truth of historical provenance**.
Its `HISTORICAL_PRODUCER_LAYOUT_REVIEWED` scope is a caller trust boundary: the
caller must separately establish the evidence chain and admission. None has
been issued in this loop. `SYNTHETIC_FIXTURE_ONLY` is used in tests and must
never be admitted as historical producer evidence by a certificate runner.

Canonical mathematical encoding is UTF-8/ASCII JSON with sorted keys and compact
separators: schema `EXACT_DYADIC_ARRAY_V1`, logical shape, and C-order values as
real/imaginary pairs. Each rational dyadic is `[signed_hex_odd_significand,
binary_exponent]`; zero is `["0",0]`. Thus endian, storage order, signed zero,
and padding do not change the mathematical hash. Shape does change it. A real
value and a complex value with zero imaginary part have the same mathematical
encoding. Raw NPY/payload hashes preserve the disjoint representation identity.

29 tests cover hand-encoded golden normals/subnormals/signed zero/maximal finite
values, endian reversal, x87 padding/layout variants, binary128, asymmetric
2D/3D Fortran indexing, dtype/header/payload/authority refusals, and 1,000 finite
random binary64 patterns checked independently with `struct.unpack` followed by
`float.as_integer_ratio` **in the test oracle only**. Exact check count is
recorded in `RAW_DECODER_VERIFICATION.json`. Existing historical suite counts
are not modified. `TDD_RED.log` preserves the unimplemented seam failure;
`TDD_GREEN.log` is the first 22-test green run; `VERIFICATION_FINAL.log` covers
the expanded suite. This is implementation verification, not scientific
certification or an admitted independent decision review.

Primary authority is the archived NumPy 2.3.5 source, including
`numpy/lib/_format_impl.py`, `numpy/_core/include/numpy/npy_common.h`, and
`doc/source/user/basics.types.rst`, plus SysV AMD64 ABI Draft 0.99.6 pp.12–13
(PDF pages 13–14). The ABI describes a candidate historical layout; the NPY
`<c32` header and x86_64 label alone do not prove its use for these arrays.
Source/member hashes and remaining historical evidence obligations appear in
`RAW_ABI_AUTHORITY.json`.

The next bounded operation requires first closing the historical ABI binding,
then authorizing exact archived-array mathematical decoding if required by the
current execution contract. It needs no HH producer, integrand evaluation,
retraining, new geometry/order, native build, or frozen comparator rerun.
