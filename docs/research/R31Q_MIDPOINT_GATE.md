# R31Q midpoint gate

Status: `FAIL_INITIAL_INTERPOLATION__BISECTION_REQUIRED`

R31P direct midpoint materialization is durable. All five midpoint H B160/B192 convergence checks pass, and all five direct midpoint full49 nodes pass the corrected original matrix-authority gates.

The correct R31J interpolation intervals include the exact reused z=8 R31H anchor:

- [0,8] -> z=4
- [8,16] -> z=12
- [16,32] -> z=24
- [32,48] -> z=40
- [48,64] -> z=56

The preregistered piecewise-linear interpolation accuracy gate fails in every interval. Interpolated raw structural gates pass; the failures are accuracy failures, not raw-matrix pathology.

| interval | midpoint | max mixed-H error [Eh] | whitened G relative error | raw gates | result |
|---|---:|---:|---:|:---:|:---:|
| [0,8] | 4 | 5.903055889096e-01 | 4.810910358399e-01 | PASS | FAIL |
| [8,16] | 12 | 8.744856587772e-02 | 3.995885764330e-01 | PASS | FAIL |
| [16,32] | 24 | 3.291939490133e-02 | 3.040792922847e-01 | PASS | FAIL |
| [32,48] | 40 | 2.113389676537e-02 | 8.656632447321e-02 | PASS | FAIL |
| [48,64] | 56 | 2.233400548525e-03 | 1.589842023175e-02 | PASS | FAIL |

Frozen thresholds remain H <= 2e-7 Eh and whitened independent generator relative error <= 2e-12. No tolerance or interpolation method is changed.

Under the preregistered adaptive rule every failing interval is bisected. The next direct nodes are:

`[2,6,10,14,20,28,36,44,52,60]`

Minimum allowed interval width remains 1 a0. Trajectory and production remain unadmitted; propagation runs remain zero.

Full local evidence bundle SHA-256:
`6d1b30777a4a9c1a28b35ad30ae2ef69327a3399a4efa5fb70cfe3afc700e69a`
