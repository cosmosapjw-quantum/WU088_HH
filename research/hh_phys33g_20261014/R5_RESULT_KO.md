# PHYS33G: finite low-Schur numerical enclosure and outgoing readout (R5)

2026-10-14 KST. Parent PR70: `95808cbddd4e8a5415c61f9430ef018ec3c3a63f`. User-selected next node `INTERIOR_LOW_SCHUR_NUMERICAL_INCLUSION_AND_PHYSICAL_AMPLITUDE_DUAL`. The complete tested Korean proof/code/inputs is in immutable 30,661,452-byte ZIP SHA256 `d65f481b901c7ea2913d860742d66e6562244f162c1a537d89aea372c299078e`. **Global PHYS33 remains PARTIAL**; this unit certifies frozen binary64 discrete objects and algebraic identities, NOT the continuous two-centre scattering amplitude.

## Fixed physics and protected conventions

`h_lambda=-Delta/2-1/r-lambda S(|r-R ez|)`, `S(s)=(1+s^-1)exp(-2s)`, `R=kappa=7/10`, `lambda=1`, `epsilon=kappa²/2`. Here `r=rphys/a0`, `kappa=a0*p/hbar`, `h=H/(2I0)`, `a0=5.29177210544e-11 m`, `I0=13.605693122990 eV`, and receiving heat ledger `chiH=13.598434599702 eV` is distinct; physical `c,hbar,kB` retained. Background signature (-,+,+,+); atomic space Euclidean. Keep frozen spectator-direct source, initial1s, `S(R)-S_R` transition, Coulomb phase and old overlap factor.

The m=0 subspace is invariant under the axial Hamiltonian/source. A sufficiently uniquely selected outgoing solution has no sourced m!=0 component. For partial-wave coefficients `a_l`, `A(mu)=sum_l(-i)^l exp(i sigma_l) a_l P_l(mu)`, with `<|A|²>=sum_l |a_l|²/(2l+1)`. The invariant subspace statement does not prove full-space real-energy uniqueness.

## Frozen discrete matrix and actual certificate

Construct 6 radial Chebyshev-Lobatto panels with boundaries `[1e-4,.1,R,2,5,10,20]`, degree 10, `l=0..20`, 144 angular nodes, bounded cusp transform `F=exp(lambda exp(-s))`, source lift `eta=phi+lambda xi=F y`. The outer BC at r20 is a truncated **pure-Coulomb** outgoing condition, NOT the certified full-screened exterior DtN. The exact object is the stored IEEE binary64 coefficient array `A_h` of size1386x1386 and stored approximate inverse `Y_h`. With norm `max_i sum_j (|Re|+|Im|)`, no under/overflow, IEEE nearest and explicit gamma_m roundoff accounting:

`
 ||I-Y_h A_h||_infty <3.184495e-8<1,
 ||A_h^-1||_infty <6582.633.
`

These numbers rigorously enclose the *stored matrix* under the specified floating model. They do not enclose coefficient-generation errors, radial/angle discretization, boundary DtN error, or the continuum inverse. Degree6 (882) and degree8 (1134) are independent discretizations, not successive enclosure refinements of one fixed object.

## Exact source-preserving Schur identities and measured discrete bounds

For any block split `A=[[A_PP,A_PQ],[A_QP,A_QQ]]`, `S=A_PP-A_PQ A_QQ^-1 A_QP` and `f_eff=f_P-A_PQ A_QQ^-1 f_Q`. Then `p=S^-1 f_eff`, `q=A_QQ^-1(f_Q-A_QP p)`. The readout is `J=J_Pp+J_Qq+J_exterior`; omitting either source or readout changes the original problem.

For a frozen matrix split at l<=8, validated feedback `||T||<=.167867256`, one-step **whole discrete state** error <8.045e-8 and dropping effective source changes the low solution point by4.0842e-6. For split l<=12, `||T||<=.105990403`, whole state error<2.959e-8 and omitted source difference6.1319e-7. The high block in these splits remains finite to l20, and must NOT be identified with the continuous exterior Q21 or Q29 theorems.

## Frozen readout, adjoint and intensity

An outgoing functional `J_h` was constructed by the stored Coulomb/Gamma phase, radial weights, cusp angular multiplication and Lagrange panel basis, and its IEEE binary64 coefficients were frozen separately. For a fixed angular direction `mu`, `A_h^dagger z_mu = j_mu^dagger` gives the exact discrete adjoint identity

`
 j_mu(u_h-u_hat) = z_mu^dagger(f_h-A_h u_hat).
`

Observed `mu=-1,0,+1` adjoint-versus-direct probes were within1e-14; this is a *point check*, not a continuum error certificate.

Discretization-specific nonmonotone intensity point values for degree6,8,10 are `0.0143251346193553, 0.0152692438277173, 0.0150635787993417`, respectively. Bound intervals for each frozen object only:

* deg6: [0.01432512892111412875,0.01432514031759647481]
* deg8: [0.01526922891213142088,0.01526925874330326381]
* deg10: [0.01506354286685719726,0.01506361473182613241]

The differing intervals are not evidence of three different physical scattering answers; they enclose three different stored discretizations. Special-function evaluation, quadrature and continuous defects remain independent unresolved errors.

## Verification, cross-repo reuse and next

Actual Wolfram15.0.1: exact4x4 rational Schur, adjoint and intensity/azimuthal identities reduce to literal0 after a protected C symbol naming correction. Actual xAct/xTensor1.3.0, official source `xTensor.m` SHA256 `04e1cf3c7e81f1eff61ca633c84537c3f3cbb0fdd42ea01441e89172086d8b36`: four zero Euclidean tensor residuals. Local/relocated frozen ZIP verifier:42/42, 32 payload hashes, CRC; deliberately changed copy refused, restored copy passed (evidence in full archive). Overlapping same-author CAS/numerical tests, no external independent scientific review or native subagents. No BVP/rate/P01/HPC replay.

Actual live rei_bianchi at2026-10-14T13:37:32Z: owner AX07 scoped ZERO completed; AX08 signed family active, AX11 T1 prepared-not-run, AX12 variants prepared-not-run. New BASS_HE PR53 combined reducer source `0ccc3bc0d1db0c82634ee856d7f8f4915a0905c08958e1fd06cb93fc82e6f2bb` is present in live worktree, including source relation; DO NOT reapply old standalone HH guard or duplicate currently active solver. HH is optional OFF/nonblocking and the 50000K stellar spectrum parameter is NOT the cold gas temperature. No owner repository mutation. CR62 PL-support already exists and should not be reimplemented.

Next node: `CONTINUOUS_LOW_SCHUR_AND_OUTGOING_AMPLITUDE_CERTIFICATION`. Use existing full screened exterior and Q21/Q29 theorems, explicitly enclose the low source's PDE/boundary/coefficients defects and full outgoing dual. `continuous_low_inverse/global_two_centre_intensity/two_centre_thermal_rate` remain null. No main merge, production, visibility or permission change.
