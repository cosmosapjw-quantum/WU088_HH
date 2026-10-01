# Historical layout witness: bounded local capture plan

Status: designed, not executed. A probe of an unrelated current host cannot
close B03. First identify the exact Python executable/NumPy extension artifact
that produced each archived NPY, and bind its binary/configuration hash to the
immutable B192/prediction provenance. If it is unavailable, retain
`RAW_ABI_AUTHORITY_BLOCKED` and recover an archived wheel/configuration or
equivalent contemporaneous layout witness.

Within that identified environment, capture without opening HH numerical arrays:

1. Python executable SHA256, NumPy version and imported package path, hashes of
   the compiled multiarray extension and NumPy generated `numpyconfig.h`;
   build/compiler flags and target; byte order; executable/shared-object ABI.
2. `dtype(np.longdouble).str/itemsize/alignment` and
   `dtype(np.clongdouble).str/itemsize/alignment`; `finfo` precision/iexp/minexp/
   maxexp, reported as integers. Capture `np.show_config()` as supporting data.
3. Synthetic arrays populated from exact integers and dyadic construction:
   +0, -0, 1, -2, 1+2^-63, 1+2^-112 where distinguishable; one smallest normal
   and one smallest subnormal. Preserve `.npy` bytes and component views.
4. A synthetic 2-element complex array with distinguishable real/imaginary
   values, and an asymmetric Fortran array. Preserve byte identity and NPY
   headers, inspect the meaningful/sign/exponent/padding offsets.
5. If a C probe is needed, compile a small standalone witness under the exact
   archived compiler/flags: print `sizeof(long double)`, `LDBL_MANT_DIG`,
   `LDBL_MIN_EXP`, `LDBL_MAX_EXP`; use `memcpy` into an unsigned-char buffer for
   long-double and complex-long-double sentinels. Compare with the NumPy
   witness. Do not claim C ABI alone identifies the NumPy build.
6. Review the linking evidence independently, then bind one `LayoutAuthority`
   to each exact NPY member SHA256 inside the known archive. The archive hash
   alone is not the `bound_npy_sha256` expected by the decoder.

Do not zero, rewrite, normalize, or reinterpret archived padding. Synthetic
fixture bytes have fixture scope only. A successful new probe without a
historical binary linkage remains supporting inference, not a closed
historical-producer identity.
