# R31R depth-first interpolation discriminator

R31Q established that every initial piecewise-linear interpolation interval fails the frozen accuracy gates, while direct midpoint H convergence/full49 and interpolated raw structural gates pass.

The preregistered adaptive rule allows only bisection of failing intervals. A breadth-first round would open ten direct nodes:
`[2,6,10,14,20,28,36,44,52,60]`.

R31R changes only execution order, not the scientific method or thresholds. Because global interpolation admission is impossible once any single interval remains unresolved at the minimum width, R31R follows the most severe failed interval [0,8] depth-first.

First discriminator:
- parent failed interval: [0,8]
- known direct midpoint: z=4
- child interval under test: [0,4]
- new direct node: z=2
- sibling z=6 deferred until needed
- H: B160/B192 with R31M tuned 2x12 route
- OD192/JVP192: recovered CP4 source, 12x1 physical pair parallelism
- ionic z=2: reuse admitted CP4 node
- interpolation is not evaluated locally

After z=2 returns:
- if [0,4] fails, next allowed nodes are z=1 and z=3; R31R prefers z=1 depth-first
- if [0,4] passes, open z=6 to test sibling [4,8]

This is a scheduling optimization only. Frozen thresholds remain H <= 2e-7 Eh, whitened independent generator relative error <= 2e-12, raw gates pass, minimum interval width 1 a0. No propagation is run.
