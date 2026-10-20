# PHYS72 optional native arithmetic cross-check

The full all-angular/all-radial theorem and exact rational certificate are
implemented in `../implementation/bounds.py`. No HH coefficient integration
is required to obtain this result. The small Fortran program independently
evaluates the same scalar q and remainder formulas in REAL128 arithmetic.
Its printed values are rounded diagnostics and never replace the exact
rational certificate or decide membership near the open convergence radius.

## Standard host command

From the repository root, with a Fortran 2008 compiler providing REAL128:

```bash
python3 research/hh_phys72_20261020/ncp_delivery/run_native.py \
  --fc gfortran \
  --out runs/phys72_native_scalar_crosscheck \
  --lambda-abs 1 --terms 3
```

The output directory is create-only. If it already exists, retain its
original receipt; inspect that result instead of using its path for a new
attempt. `--lambda-abs` accepts an exact rational string in the Python
runner, which records an 80-significant-digit decimal native input.
`--terms` accepts positive integers through 10,000. Defaults are lambda=1,
N=3, and a 60-second timeout per compiler/version/native command. This
program calculates scalar formulas only; physical integrations are zero.

The native binary itself accepts a decimal lambda absolute value and N as
positional arguments. It validates each complete token before conversion:
lambda permits decimal digits with an optional decimal point, an optional
leading `+`, and an optional `e`/`E` exponent; N permits decimal digits only.
Whitespace, slash terminators, commas, and additional list items are rejected.
Its denominator branch is explicitly a rounded
diagnostic. `EXACT_AUTHORITY.json` in each runner output records the exact
Fraction sufficient-condition decision, even when a native rounded branch
cannot be compared at the boundary.

The runner preserves compiler version, exact argv, exit codes, timings,
stdout/stderr bytes and SHA-256, source/runner/binary identity, the native
JSON and exact-rational comparison. `--binary /exact/path` may reuse an
explicit existing binary while preserving its distinct hash and skipping
compilation; it does not infer scientific identity from the filename.
Before accepting returned JSON, the runner validates the schema, the
uncertified diagnostic scope, HH_R10=OFF, zero reported physical integrations,
the exact order and decimal input echoes, binary128 metadata, and finite
nonnegative rounded values consistent with the reported denominator branch.
Invalid payloads produce a preserved `NATIVE_PAYLOAD_INVALID` receipt. This
contract validation never replaces the exact Fraction convergence decision.

## Actual session execution

The initial current-session probe found no Fortran compiler. Two Ubuntu
packages were downloaded and extracted under `/tmp/wu088_phys72_fortran`;
no system packages were installed. The compiler is GNU Fortran 13.3.0.
`verification/FORTRAN_SETUP.json` records package hashes and setup failures.

The first compile failed because the extracted driver did not find the
existing system `liblto_plugin.so`. The first receipt and stderr are kept
in `verification/native_attempt_01`. Explicit search paths resolved this
environment issue; the successful command was:

```bash
python3 research/hh_phys72_20261020/ncp_delivery/run_native.py \
  --fc /tmp/wu088_phys72_fortran/root/usr/bin/x86_64-linux-gnu-gfortran-13 \
  --fc-arg=-B/tmp/wu088_phys72_fortran/root/usr/lib/gcc/x86_64-linux-gnu/13/ \
  --fc-arg=-B/usr/lib/gcc/x86_64-linux-gnu/13/ \
  --fc-arg=-L/tmp/wu088_phys72_fortran/root/usr/lib/gcc/x86_64-linux-gnu/13/ \
  --out research/hh_phys72_20261020/verification/native_attempt_02 \
  --lambda-abs 1 --terms 3
```

These absolute paths describe the actual recorded session. A normal NCP
installation uses its own `gfortran` command above and records its resulting
compiler and binary identity. It needs no solver design or new mathematical
choice. The already successful session output must not be overwritten.

The initial implementation had one successful compile after the preserved
failed attempt. Three scalar native calls completed: lambda=1,N=3;
lambda=0,N=3; lambda=3/2,N=4. The latter two reused the same binary. These
original receipts remain unchanged, and `FORTRAN_SETUP.json` records that
initial setup stage.

Independent review then found the direct Fortran list-input acceptance and
missing returned-payload validation described above. The corrected source
was compiled once and run at lambda=1,N=3 in
`verification/native_contract_fixed`: compile wall time 0.155806 s, native
wall time 0.001931 s. Its default tail's relative difference from exact
arithmetic remains below 1.979e-34.

The focused follow-up in `verification/native_contract_audit/AUDIT.json`
passed 19 checks. Six malformed CLI calls were rejected; ten inconsistent
payload variants were rejected; the corrected default payload was accepted;
one actual native call with rounded rho>=1 returned no tail; and one
existing-binary payload fixture was rejected by the actual runner. The
audit script and the rejected-payload execution receipt are retained.

Across both implementation stages, the recorded totals are two successful
compiles, one preserved environment compile failure, five successful native
scalar calls, six intentionally rejected CLI calls, and one payload fixture
process. These are arithmetic diagnostics and contract checks, with zero
physical HH integrations. Existing PHYS71 panels and PHYS70/69 trajectories
are untouched. HH_R10 remains OFF.
