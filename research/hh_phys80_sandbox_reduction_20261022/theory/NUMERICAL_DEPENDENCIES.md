# Numerical/source dependency notes

Actual runtime for the reduced controls: Python3.12.14, NumPy2.3.5,
SciPy1.17.0. The version-pinned official Radau documentation describes
fifth-order Radau IIA, a third-order embedded error estimate and cubic
collocation dense output; callable analytic Jacobians are supported:
https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.integrate.Radau.html

The implementation supplies the Jacobian derived in
EXACT_REDUCTION_AND_JACOBIAN_KO.md, keeps the original finite proper-time
interval and samples, and removes the former explicit trace-rate step cap.
Accepted endpoints and 161 requested samples are checked; no claim is made
about every point of the dense interpolant or a rigorous global error bound.

The generic Maxwellian prototype fixes electron mass to CODATA2022
9.1093837139e-31kg. Its official source is
https://physics.nist.gov/cuu/pdf/wallet_2022.pdf .
Its eV-to-joule factor1.602176634e-19 and kB1.380649e-23J/K use exact SI
definitions. These constants are numerical model leaves rather than new
low-temperature atomic-data validation.

Source search and direct text extraction, raw PDF-byte retrieval, and visual
table reading are distinct. The Bell1983 text was retrieved by the source
researcher, while direct NIST PDF download in this session was denied by
the default network boundary and returned HTTP403 after approved escalation.
Root's later web open timed out. No raw Bell PDF or visual table verification
is claimed. The source candidate table and H transcription conflict are
preserved under source/maxwellian; no table is automatically admitted.
