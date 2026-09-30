# Large-positive radial representation

For x=a+ib, a>0, define F_n(x)=integral_0^1 t^(2n) exp(-xt²) dt. Principal sqrt gives the complete-Gamma part C_0=sqrt(pi)/(2 sqrt(x)), C_n=(2n-1)C_(n-1)/(2x). This comes from the defining gamma integral (DLMF8.2 E1/E2/E3), independently of any truncated asymptotic expansion.

By triangle inequality |F_n-C_n| <= T_n(a)=integral_1^infinity t^(2n)exp(-at²)dt. Since t>=1, T_0<= exp(-a)/(2a). Integration by parts gives T_n=exp(-a)/(2a)+(2n-1)T_(n-1)/(2a). Therefore for n=0,1,2 use exp(-a)/(2a) times [1, 1+1/(2a), 1+3/(2a)+3/(2a)^2]. This is valid for complex x in the right half-plane and is NOT the real-only first-neglected-term rule.

Let odd p=2k-1 and M_p=c v^(p/2)[A_k(x)F_0+B_k(x)E], c=sqrt(2/pi), E=exp(-x). Differentiating with x=s/(2v) and F_n'=-F_(n+1) gives the original matched derivatives:

M_s=c v^(p/2)/(2v)[A'F0-A F1+(B'-B)E],
M_ss=c v^(p/2)/(4v²)[A''F0-2A'F1+A F2+(B''-2B'+B)E].

For a>=64 this candidate substitutes F_n=C_n and E=0. With K=abs(c v^(p/2)), omission bounds are

B0=K[|A|T0+|B|exp(-a)],
B1=K/(2v)[|A'|T0+|A|T1+|B'-B|exp(-a)],
B2=K/(4v²)[|A''|T0+2|A'|T1+|A|T2+|B''-2B'+B|exp(-a)].

These bounds concern exact arithmetic truncation. Floating-point evaluation, polynomial cancellation, and contraction errors are separate and controlled numerically; no end-to-end interval guarantee is claimed. At large a, exp(-a) is never evaluated by the C++ branch. The bound is computed only in small mp controls. Even p values remain exact finite polynomials before floating-point rounding. The shared seed lower branch and negative direct hypergeometric branch remain unchanged.

Finite API domain is v in [1e-100,1e100], Re(x) in [-32,1e12], |Im(x)|<=2, p=-1..8 and derivative order0..2. Maximum possible intermediate polynomial magnitude is safely within the required longdouble exponent range. This scalar domain must be checked against each future actual H geometry; it is not an automatic H promotion. No epsilon or physical tolerance was adjusted.

## Native buffer contract and review repair

C callers must supply contiguous, live variance/sr/si buffers with at least n longdouble elements and an output buffer with at least 2*(order+1)*10*n longdouble elements. Output must not alias any input. C cannot infer allocation capacity from raw pointers. Null arguments, invalid order, gross lengths that exceed PTRDIFF_MAX/(60*sizeof(longdouble)), unsupported rounding, and all invalid scalar inputs are rejected before output writes. A nonzero later computation status invalidates the entire output buffer. The Python adapter owns fresh output and satisfies capacity/nonalias requirements.

The initial source had an element-count-only SIZE_MAX/60 guard. Independent reviewer identified byte-address representability as a missing defense. The initial source is preserved as radial_large_initial.cpp; current source uses the stricter byte/PTRDIFF bound. This is ABI robustness repair, not a numerical algorithm change.
