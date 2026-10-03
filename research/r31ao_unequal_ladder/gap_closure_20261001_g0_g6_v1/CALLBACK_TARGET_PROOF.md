# G4 callback target and proof boundary

Status: analytic formulas are derived and source-bound; the C++ backend implementation is a draft, neither compiled nor runtime verified. This document does not close B01's validated-backend gate.

Authority is `SOURCE_FUNCTIONAL_MAP.json` SHA256 a493ba1dd19c13c7b5b819cb5c9a4e6f939791a46b215489f4b1e0a1e6ad6ad1 and `EXACT_INPUT_AND_CALLBACK_BINDING.json`. The inspected S03 h0_fused.cpp has SHA256 d019713f8a9c6e864d60cc796104a0cdef629e491e6ab8de757995aa4f3672f2, exactly as the map. S03 geometry, E[3], der[4]/der[5] and exported O/G paths determine the bounded implementation target. The legacy numerical radial approximation is not invoked or wrapped. No historical source bytes are edited.

Let A=a+t, B=b+u, h1=a/A, h2=b/B, m1=ad1/A+i q1 e_z/(2A), m2=bd2/B+i q2 e_z/(2B), n1=m1-d1, n2=m2-d2, delta=m1-m2. The radial parameters are sigma=(1/A+1/B)/2 and s=sum delta_j², with a bilinear square. At fixed q1,q2, define L1=2a n1z, L2=2b n2z, s1=2h1 delta_z, s2=-2h2 delta_z. Sigma is independent of d1z,d2z. All a,b,d,q are exact real rationals supplied from the exact lift at eventual assembly.

For M=M_k(sigma,s), F=partial_s M and F2=partial_s² M, E_s=M and E_l=n1_l M+delta_l F/A for l=x,z. Direct product differentiation gives:

```
d1 E_s = s1 F
d2 E_s = s2 F
d1 E_l = delta_lz (h1-1) M + n1_l s1 F
           + delta_lz h1 F/A + delta_l s1 F2/A
d2 E_l = n1_l s2 F - delta_lz h2 F/A + delta_l s2 F2/A
O  = base E
G1 = -base (L1 E + d1 E)
G2 = -base (L2 E + d2 E)
```

Here delta_lz is the Kronecker symbol. In particular, the pz G1 term includes the positive polynomial derivative after the overall minus sign; px has no such term. These equations agree with source S03's dp[4], np[4], dp[5], sp and der loops. An independent theorem task in this same artifact generation derived the same formulas; this is not admitted project-level independent scientific review.

The implemented radial expression uses unregularized 1F1 with shifted exact half-integer parameters and the exact rising-factorial derivative factor. For even k, r>k/2 gives exact zero before evaluating 1F1. No division by s occurs, so the entire continuation at s=0 is retained. Principal `(2 sigma)^(k/2)` is fixed on Re(sigma)>0. The density is the finite signed Hermite expansion from theorem A; no absolute coefficient replacement occurs in the callback. There are no quadrature weights or coordinate Jacobians in U_i(t), so eventual dt du integration must apply its chosen measure exactly once.

For real positive t,u, Gaussian completion yields the source primitive. On the connected right-half-plane product domain, compact Gaussian domination establishes joint holomorphy of the original spatial integral. Re(A),Re(B)>0 implies Re(1/A),Re(1/B)>0, hence Re(sigma)>0. Analytic continuation gives equality of the completed-square expression there; this does not require a nonanalytic contour shift of |r1-r2|^k. Bounds and derivative-exchange premises are recorded by the G1 theorem task. The implementation nevertheless checks every input and derived ball for a positive real margin, so an enclosure that cannot prove the domain is rejected conservatively.

`polynomial_field` implements the finite signed sum C_ijk U_i U_j times these O/G primitives. The successor `assembly.cpp` implements normalization by stored pref and a,b, primitive orbital contractions, parity/reflection signs, phases using stored phase_E/v, final D formulas and post-integral conjugation. This is a separate translation unit accepting completed real-domain primitive integral balls. It does not call or conjugate the analytic integrand. Exact-input loading and actual integrated ball acquisition remain required to obtain the final Frozen107 target. No substitute physical constants, regenerated inputs, H components, VU/UV fields or independent dotO are introduced. A scalar slice callback retains the entire outer box but does not by itself prove or compute uniform nested integration.

The assembly draft was checked directly against S01 od_run.py (SHA256 63c0925ff938340feceb5768aba40da348b3afe323214a9792012e9d0bbc664d) and S02 h0_backend.py (SHA256 128e13bd475ce6aeb57e3c601239318e00f6bfbfee6f99a85ba081aa97b1a9e5). Its factor N_l is exactly the ideal normalization declared by the binding. The original binary64 adapter's rounding is not imported into the ideal continuous target. The 47-row registry, 12x12 coefficient products, active XOR cusp selection, p-channel/G-field reflection signs, phase and D formulas use the source order and signs. G1/G2 passed to D_row are already phased, so the entire complex values are conjugated after real integration. See `validated_callback/ASSEMBLY_SOURCE_BINDING.json` and `ASSEMBLY_INTERFACE.md`.

Open implementation obligations: verified pinned backend build and ABI; native synthetic execution with odd/even/derivative/domain and assembly cases; exact-input decoder-to-native loader; validation of every outward conversion and final ball serialization; actual interior/endpoint execution under separate authorization. Until these close, compiler/binary identity is null, B01 remains open and no source accuracy certificate exists.
