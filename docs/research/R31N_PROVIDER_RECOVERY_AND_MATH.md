# R31N anchor dotO / ionic provider recovery and mathematical audit

Canonical node: `R31N_ANCHOR_DOTO_IONIC_PROVIDER_CLOSURE`.

## Scope

Positive anchors are `z = 0,16,32,48,64`. H192 is already closed by R31K-A/B. R31N does not change the frozen107 basis, 5-keV straight-line trajectory, ETF/phase convention, quadrature tolerances, or full49 gates.

## CP4 byte recovery

Dropbox retained the original three-part archive `WU088_HH_C21_TRANSFER_CP4_20260923.zip.part01..03`. Concatenation gives SHA-256

`c10c932a6cdad817982e00920a893733b367827b116d058791bf5aacad517cd9`

and ZIP CRC passes. This matches the CP4 parent identity in the R31A recovery receipt. The recovered scientific source hashes include:

- `completion/mixed_derivative/jvp.cpp`: `2ea30233...92cbd`
- `completion/mixed_derivative/native.py`: `247c9eca...1a22d`
- `completion/mixed_derivative/run.py`: `d092d3e8...de935`
- `completion/mixed_h/od_run.py`: `63c0925f...664d`
- `completion/mixed_h/h0_backend.py`: `128e13bd...1a9e5`
- `completion/mixed_h/h0_fused.cpp`: `d019713f...672f2`
- `completion/ionic/ionic.py`: `8b801a51...e6df54`
- frozen n=192 grid: `e1959e1b...96301`

The archive itself is the immutable authority. An extracted copy may acquire compiler caches; source-file identities are checked before execution.

## Provider census

Recovered source-complete/admitted inputs:

- independent JVP192: z=0,16,32,64
- ionic 2x2: z=0,16,32,48,64, all admitted
- mixed O/D192: z=0

Therefore only these direct source calculations remain:

- O/D192: z=16,32,48,64
- JVP192: z=48
- new ionic calculation: none

The earlier idea of reusing O/D arrays embedded in the R31K H seals was rejected. Both paths use the same H0Fused primitive implementation, but their declared `W` quadrature tensors have different identities. Their z=0 aggregate difference is only about 1e-17, but numerical closeness does not establish provider identity.

## Independent JVP derivative

The recovered JVP source has the mixed overlap form

`O(t) = p exp(i phi(z(t))) R0(z(t))`, with `z(t)=v t`,

`phi(z) = v z/2 + DeltaE z/v`, and `dR0/dz = R1`.

Thus

`dO/dt = p exp(i phi) [ v R1 + i (v^2/2 + DeltaE) R0 ]`.

A Wolfram Language symbolic differentiation returned an exact zero for `derived - target`; the phase-rate term in the recovered `run.py` is therefore the direct chain/product-rule derivative, not a compatible connection manufactured from D.

## Regression against CP4 authority

The new lightweight assembler in `src/wu088_hh/r31n.py` was applied to recovered CP4 arrays:

- JVP z=0,16,32,64: reconstructed O and dotO are byte/numerically array-exact to stored aggregates.
- OD z=0: reconstructed O, O_row, D_col, D_row are array-exact to stored aggregate.
- CP4 z=8 JVP and ionic aggregates are byte-identical to the later R31G provider snapshot.
- z=0 JVP O vs OD O max difference: `2.168404344971009e-19`.
- z=0 independent metric residual max: `4.4151592375630405e-19`, original elementwise fail count 0.

A scratch z=0 full49 assembly using R31K H192 + CP4 OD/JVP/ionic passed all 11 inherited R31H raw matrix gates. This is a genericization proof-of-path, not yet the durable R31N anchor admission.

## Parallel execution rationale

Every missing primitive pair is independent before the canonical aggregate contraction. R31N changes only pair scheduling:

- 12 outer processes, one physical core each;
- original serial native kernel inside each process;
- source-defined pair arithmetic unchanged;
- aggregate contraction performed after all 144 canonical coordinates are present;
- JVP z48 pair scheduling uses timing-only interpolation between the recovered z32 and z64 pair timings.

This is deliberately different from the R31M 2x12 tuned foreign-H kernel: OD/JVP native functions are serial and gain from pair-level parallelism instead.

Local pair files are create-only resume checkpoints. Because each new node is minute-scale and the immutable CP4 source is already remotely durable, remote dual backup occurs at node close rather than after every 12 pairs. This changes transport granularity, not the scientific or provider identity gate.

## Claim ceiling

R31N provider fill alone does not admit full49, trajectory, observables, or production. After the five missing nodes are dual-backed, full49 at z=0,16,32,48,64 must be assembled and each inherited R31H gate must pass before midpoint/interpolation work opens.
## New-geometry smoke and literature context

The recovered original native implementations were invoked directly at geometries not present in the corresponding CP4 aggregate: OD192 primitive pair (0,0) at z=16 and JVP192 primitive pair (0,0) at z=48. Both completed with finite source-bound outputs. These are ABI/path smoke tests, not node admission.

The external literature search was used only as context, not as an authority replacing the frozen model. Fatehi and Subotnik (J. Phys. Chem. Lett. 2012, DOI 10.1021/jz3006173) discusses electron-translation factors in derivative couplings, while Ryabinkin, Nagesh and Izmaylov (J. Phys. Chem. Lett. 2015, DOI 10.1021/acs.jpclett.5b02062) discusses efficient time-derivative nonadiabatic couplings. R31N nevertheless uses the recovered project-specific ETF and derivative formulas byte-bound to CP4.

