# PHYS73 deterministic Green batch kernel

`green_batch.rs` implements the actual HH Coulomb Dirichlet Green matrix at a
supplied finite quadrature. The Python preparation manifest binds the Coulomb
parameters, grid, source, and input hash. This binary evaluates that finite
matrix; the PHYS72 exact all-angular, all-radial contraction certificate remains
the authority for the operator and Born-tail bounds.

## Build and run

No external Rust crates or Cargo downloads are needed. Use a Rust compiler
available on the actual host; the sandbox source was built with Rust 1.94.1.

```sh
rustc --edition=2021 -O -C target-cpu=x86-64 green_batch.rs -o green_batch
rustc --edition=2021 -O --test green_batch.rs -o green_batch_tests
./green_batch_tests
HH_R10=OFF ./green_batch INPUT.bin OUTPUT.bin --workers 64 --mode sweep --repeat 5
```

`target-cpu=x86-64` keeps the example build portable. Record the actual compiler,
flags, source SHA256, and resulting binary SHA256 in the host run receipt. If a
host-native target is selected, record that change with its separate binary and
same-input comparison. No fast-math flags are part of this implementation.

The output path must be new. Existing outputs are never overwritten. Errors
return exit code 2 and a diagnostic on stderr. A failed write may leave an
incomplete new output; the driver must accept only a successful exit plus an
exactly parsed result of the expected length. Setting `HH_R10` to any value
other than `OFF` is rejected. An unset value retains `OFF`.

## Input and output protocol

All integers and binary64 components are little endian. A complex number is a
real component followed by an imaginary component, with no conjugation.

| Field | Encoding |
| --- | --- |
| Input magic | Eight bytes `HHG73V01` |
| Task count | `u64` |
| Nodes per task | `u64` |
| Each task | `d[n]`, then `t[n]`, then `x[n]`, each an array of complex binary64 |
| Output magic | Eight bytes `HHO73V01` |
| Output dimensions | The same two `u64` values |
| Each output task | `u[n]` complex binary64 values |

The input length must be exactly `24 + 48*tasks*nodes` bytes. The output length
is exactly `24 + 16*tasks*nodes` bytes. NaN and infinity are rejected. The first
ratio `t[0]` is unused and must be complex zero. There is no padding, JSON
payload, normalization constant, or implicit quadrature weight.

For outgoing `f_i` and the Dirichlet solution `phi_i`, preparation supplies

\[
d_i=\phi_i f_i,\qquad t_i=f_i/f_{i-1}\quad(i>0),\qquad
x_i=w_i h(r_i).
\]

`x` already includes the quadrature weight. The Green matrix is complex
symmetric:

\[
G_{ik}=d_{\min(i,k)}\prod_{m=\min(i,k)+1}^{\max(i,k)}t_m.
\]

The empty product equals one. The production sweep evaluates

\[
L_0=d_0x_0,\quad L_i=t_iL_{i-1}+d_ix_i,\quad
T_{n-1}=0,\quad T_i=t_{i+1}(x_{i+1}+T_{i+1}),\quad
u_i=L_i+d_iT_i.
\]

Each diagonal entry appears once. `--mode dense` evaluates the same finite
matrix with explicit ratio products, taking quadratic work but linear storage.
It provides a changed-algorithm comparison on an identical payload.

## Floating-point and parallel contracts

The production sweep uses fixed arithmetic order within each task. Real and
imaginary Neumaier sums carry a correction through the complex recurrence.
The stored prefix is rounded to binary64 before adding the upper contribution.
Product errors are not rigorously enclosed. The result JSON therefore reports
`certified:false`; dense agreement alone does not enclose quadrature, Coulomb
input, omitted radial tail, angular truncation, or original-source error.

All arithmetic intermediates must remain finite. The binary counts subnormal
input/output components, subnormal arithmetic results, and nonzero
multiplications that underflow to zero. These diagnostics are explicit; they
are not an interval arithmetic certificate. Arithmetic event counts include
every requested repetition, whereas input/output component counts are counted
once.

Workers process independent tasks. There are no shared floating-point sums,
atomics, cross-task reductions, or scheduling-dependent reductions. The same
task has identical operation order for every worker count. The effective
worker count is the minimum of requested workers, task count, and Rust's actual
host `available_parallelism`. The static partition launches exactly that many
workers, dividing task counts as evenly as possible. Available host capacity
must be recorded again on NCP; sandbox resource observations are not NCP data.

`--repeat` reuses the parsed immutable input and allocated output. Stdout emits
one JSON object with each kernel wall time. Kernel timing includes worker
creation/join and arithmetic; it excludes input reading, output allocation,
and final file writing. The process wall time should also be recorded by the
driver. No warmup time is silently removed. The final repetition is written.

## Resource limits

| Guard | Limit |
| --- | ---: |
| Tasks | 65,536 |
| Nodes per task | 1,048,576 |
| Total task nodes | 16,777,216 |
| Requested workers | 1,024 |
| Repetitions | 10,000 |
| Dense pair evaluations, including repetitions | 1,000,000,000 |

Input/output arrays use `64*tasks*nodes` bytes, at most 1 GiB, plus small vector,
I/O, timing, and worker-stack overhead. The driver must budget concurrent jobs
and preparation memory separately. Larger independent workloads should be
split into payload batches. No old PHYS71 panels or inherited profiles are
integrated by this kernel.
