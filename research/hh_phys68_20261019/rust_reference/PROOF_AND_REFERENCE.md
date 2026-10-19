# PHYS68: independent Rust finite-L28 second-Born reference

## Fixed definition and decomposition

This unit retains the original atomic coordinates, B=27, T=65,
k=7/10, E=49/200 Hartree, eta_C=-10/7, and shift R=7/10.  The original
Hamiltonian is h=-Delta/2-1/r-S, where S=(1+1/d)exp(-2d) and
d=sqrt(r^2+R^2-2rR mu).  The radial equation uses V=2S.

Let f_l=H_l^+(r)/H_l^+(B), H^+=G+iF^C.  For m=0 the normalized real
angular functions after the azimuthal integral are

    phi_l(mu)=sqrt((2l+1)/2) P_l(mu),
    V_lj(r)=int_-1^1 phi_l(mu) phi_j(mu) 2(1+1/d)exp(-2d) dmu.

Define the truncated first-forcing primitives

    q_lj(r)=int_r^T f_l(t) f_j(t) V_lj(t) dt.

Because the angular potential is symmetric, q_lj=q_jl.  These are
complex bilinear products, without conjugation.  The finite second Born
coefficient with zero terminal first- and second-order corrections is

    D2_(21,20)(B;T,L)
       = int_B^T sum_(j=0)^L q_(21,j)(r) q_(20,j)(r)/f_j(r)^2 dr.

To see the cancellation, the first-order DtN contribution at r is
q_lj(r)/(f_l(r)f_j(r)).  Multiplying the quadratic forcing by the outer
transport f_21(r)f_20(r) cancels those two external factors, leaving
exactly q_(21,j)q_(20,j)/f_j^2.  There is no conjugation or factor 1/2.

The backward differential system is therefore

    f_l'=g_l,
    g_l'=-[49/100+2/r-l(l+1)/r^2]f_l,
    q_(21,j)'=-f_21 f_j V_(21,j),
    q_(20,j)'=-f_20 f_j V_(20,j),
    D2'=-sum_(j=0)^L q_(21,j)q_(20,j)/f_j^2.

The terminal data at T are the outgoing Coulomb f_l(T),g_l(T), q(T)=0,
D2(T)=0.  All 29 internal j=0,...,28 are retained in each RK4 stage.
The resulting D2 has units a0^-1 after restoring the atomic length.
This finite-cutoff reference does not itself add the T-to-infinity tail.

## Independent numerical implementation

`scripts/phys68_rust_reference.rs` uses Rust's standard library only.
It implements its own binary64 complex arithmetic, Legendre recurrence,
Gauss-Legendre nodes and weights (Q=96), angular projection, and backward
RK4 integrator.  The same RK4 stage function is used for the manufactured
problem and the original coupled system.  No external Rust crates,
Python scientific integration, PHYS66 campaign, or NCP process is used.

The starting Coulomb values are shared special-function input.  The
Python driver evaluates the unchanged PHYS67 Arb initializer at 512 bits,
preserves the full dyadic H/H(B) and H'/H(B) seed balls, then writes the
chosen binary64 values in decimal round-trip form.  It records their
hexadecimal binary64 values and the exact input-text SHA256.  Thus the
Rust angular/ODE/integration path is independent, while the initializer
is explicitly shared.  The exported binary64 seeds are not described as
interval certificates.

The driver verifies the original frozen NPZ SHA256 before creating output:

    f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d

Prepared seed text can be reused with `--seed`, avoiding a FLINT
dependency or another special-function evaluation on the receiving host.
The source and complete seed are delivered, so the receiving host only
needs its compiler and the actual execution step.

## Actual compile, tests, and two new runs

The available compiler was actually invoked and reported:

    rustc 1.94.1 (e408947bf 2026-03-25)

Both test and optimized scientific executables compiled with exit 0.
Five Rust tests passed: complex bilinear arithmetic, Gaussian moments and
orthonormality, the independent closed form of V00, a manufactured second
Born sign/factor check, and fourth-order convergence for exp(i*k*r).
The optimized compile issued one preserved dead-code warning for the
single-element angular helper used by the test build.  This warning has
no numerical or execution failure status.

For constant V=v and f=1 on an interval of length Delta,
q(r)=v(T-r) and D2=v^2 Delta^3/3.  The common backward RK4 implementation
returned 0.0146484375 for v=0.15 and Delta=1.25, exactly matching the
computed manufactured value in binary64.  The test also checks one, two,
and sixteen steps and enforces the positive sign.

The two original-model runs were performed once each:

| Steps | h | Re D2 [a0^-1] | Im D2 [a0^-1] | integration seconds |
|---:|---:|---:|---:|---:|
| 2432 | -1/64 | 7.017743691499148e-48 | 3.2001632200665314e-48 | 0.058214621 |
| 4864 | -1/128 | 7.017743636578995e-48 | 3.200163222139536e-48 | 0.096436988 |

Their absolute difference is 5.4959262654049e-56 a0^-1 and relative
difference is 7.12557230146345e-9, below the fixed 1e-6 refinement goal.
No extra refinement run was needed.  The maximum diagnostic deviation
of f_l(B) from its exact normalization 1 decreased from
3.977567140893462e-9 to 2.486009454988155e-10.  The code did not correct
that measured drift by post-hoc renormalization.

`run_20261019/EXECUTION_RECORD.json` pins the Rust source, driver and seed,
every compile/run command, actual exit status and timing.  The numerical
results, raw streams, manufactured check and refinement record are next
to it.  Compiled executables are reproducible build outputs and are
excluded from Git; BUILD_ARTIFACTS.json preserves their actual hashes.

The Python driver tests validate source rejection before launch, actual
seed parsing, exact binary64 provenance, finite result contracts, input
matching, the difference between refinement and certified error, and the
existing execution-record identities.  They do not rerun either physical
integration.

## Claim gate and remaining link

Adopt this result as a numerically checked independent integration
reference for the finite L28,m0,T65 original second Born entry.  Agreement
between two step sizes is not an interval error bound.  A comparison
against the parent's separately validated PHYS68 ball is a distinct gate,
recorded by the parent when that certificate is available.  The finite-L
cutoff tail, higher Born terms, excluded angular channels, original xi,
origin/incoming adjoint, sigma(E), and k_HH(T) retain their own obligations.
HH_R10 remains OFF.

## Reproduction with the prepared seed

From the repository root on the receiving host:

```bash
rustc --edition=2021 --test -O scripts/phys68_rust_reference.rs -o /tmp/phys68_rust_tests
/tmp/phys68_rust_tests
rustc --edition=2021 -O scripts/phys68_rust_reference.rs -o /tmp/phys68_rust_reference
/tmp/phys68_rust_reference 2432 research/hh_phys68_20261019/rust_reference/run_20261019/SEED_INPUT.txt
/tmp/phys68_rust_reference 4864 research/hh_phys68_20261019/rust_reference/run_20261019/SEED_INPUT.txt
```

These commands are provided for an independently required receiving-host
execution.  The two recorded sandbox runs are already complete and
should be reused when that is the scientific question.
