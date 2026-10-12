# PHYS14 validation, fixed before the first scientific run

The scientific case is one continued isotropic two-half history. Repeated node/coordinate checks are assertions within this case, not independent physical experiments.

| Evidence | Acceptance condition | Scope |
|---|---|---|
| Source and carry identity | Input file digests match pinned copies; binary layout and exact leaves agree | Integrity; inherited results |
| Isotropic geometry | Exact-real common rho and normalized weights lie in all original ray enclosures | Geometric subfamily; independent reviewer |
| New root | Full original X is a strict self-map, scaled-infinity contraction < 1 | Every parameter and fixed coefficient tuple of the stated subfamily |
| Source reuse | Same terminal time and same endpoint leaves; new root domain stays inside original X | Nonphoto and HH rate only |
| U/V/W | Four-dimensional Neumann sum with outward interval tail; mixed forcing uses the same new U,V | Global lambda,b in both halves |
| Carry closure | Original grid and guard maps; source-aligned photon quotient; four-component absorption identity contains zero | Gas and aggregate observables |
| Finite response | Uniform C2 first/mixed derivative inclusions and FTC | Same-family finite parameter differences |
| Remap split | Exact original-node operator formula and zero number/energy moments, with lower-guard boundary | Transport operator diagnostic, not total gas endpoint defect |
| Final decision | A distinct reviewer examines actual results/code/source bindings and issues a scoped decision | No self-promotion by candidate author |

Resources per new scientific run: wall 90 seconds, CPU 90 seconds, address space 768 MiB, file size 32 MiB. A failed attempt is preserved and classified before a changed retry. No old successful full suite is rerun.
