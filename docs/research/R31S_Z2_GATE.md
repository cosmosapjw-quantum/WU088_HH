# R31S z=2 depth-first interpolation gate

Status: `FAIL_INTERVAL_0_4__DESCEND_TO_Z1`

Direct z=2 source is durable. B160/B192 H convergence passes with max all-94 mixed-H difference `9.312542793123333e-10 Eh` and zero failures. The H_row companion block has the same maximum difference and zero failures.

Direct z=2 full49 passes every original/corrected authority gate:
- raw O Hermiticity
- raw H Hermiticity
- full and reduced overlap positivity
- H directional consistency
- OD/JVP overlap consistency
- independent elementwise metric identity
- compatible and independent reduced-generator anti-Hermiticity
- parity-subspace closure

The preregistered provider-block piecewise-linear interpolation across z=0 and z=4 fails at the direct z=2 sentinel:

- mixed-H max error: `1.1911459223785104 Eh` (threshold `2e-7 Eh`)
- whitened independent generator relative error: `0.34502624594182096` (threshold `2e-12`)
- interpolated raw structural authority gates: PASS

Literal full-raw-matrix interpolation also fails, so the adaptive decision is invariant to that interpolation-semantics ambiguity.

No threshold or interpolation method is changed. Under the R31J depth-first bisection rule the next direct discriminator is z=1 for child interval [0,2]. z=3 remains deferred.

Trajectory runs remain zero. Trajectory and production remain unadmitted.

Local evidence bundle SHA-256:
`71faca367134a4df7f1838b85a2445c21fca20066fd2386a2f4769639eeec044`
