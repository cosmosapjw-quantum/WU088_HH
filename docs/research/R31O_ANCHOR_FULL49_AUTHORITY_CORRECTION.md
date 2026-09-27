# R31O anchor full49 authority correction

Status: `PASS_ALL_FIVE_ANCHOR_FULL49_LOCAL_ADMISSION_AUTHORITY_CORRECTED`

Five anchors z=0,16,32,48,64 were assembled from admitted H192, source-bound OD192/JVP192 and admitted ionic providers. No trajectory propagation was run.

A mechanical application of every R31H diagnostic gave PASS at z=0,16,32,48 and a single z=64 failure in the supplemental global-relative raw-dotO Hermiticity diagnostic. All original R10/R29 matrix-authority gates passed at all five anchors.

At z=64:
- raw-dotO relative defect = 2.5672207072523307e-10
- absolute anti-Hermitian norm ~= 2.28656e-14
- max anti-Hermitian entry = 6.189736203175193e-15
- independent metric elementwise failures = 0
- independent generator anti-Hermiticity = 8.21248398830715e-14

An 80-digit direct Gaussian derivative control of the worst neutral pair (5,7) gives
`|dotO_57-conj(dotO_75)| = 5.532798945926188e-80`,
while the binary64 path gives `6.189736203175193e-15`.

Therefore the relative-only diagnostic failure is a cancellation/scale pathology rather than physical non-Hermiticity. No matrix was symmetrized and no tolerance was relaxed.

Admission follows the original authority gates:
- raw O Hermiticity
- raw H Hermiticity
- positive reduced overlap
- elementwise independent metric consistency
- independent reduced generator anti-Hermiticity

The z=64 raw-dotO relative diagnostic remains recorded as a warning. Claim ceiling remains local full49 admission only; trajectory and production remain false.
