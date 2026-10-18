# PHYS66 R5: individual Born-order radial cutoff bounds

2026-10-18. Inherited theorem: PR114 bad80f7729015c84c8dde27f1b1dec3a1f8b2c9f,
research/hh_phys65_20261018/r5/PROOF.md. This work does not overwrite the
unpublished PHYS65 first-order tail/split work supplied as an attachment.

## Object and conventions
Original atomic-coordinate radial equation at E=49/200 Hartree, k=7/10:
u''+[diag(k²+2/r-l(l+1)/r²)+V_L(r)]u=0, r>=B=27,
V=2(1+1/d)exp(-2d), d=|r n-(7/10)zhat|. V_L is the orthogonal
full ell<=L projection, 0<=L<=64, including all signed m and all intermediate
channels inside this fixed projection. D=Z_L-Z_C uses +d/dr at B, not the
outward normal of the exterior domain. D_n means the physical order-n term
(including epsilon^n, epsilon=3e-23), not the unscaled coefficient Y_n.
D_(n,T) is the same exact Born term with screen set to zero for r>T.

The inherited original normalized Coulomb ratio lemma proves
||P(r,t)||_2²<=Gamma=32400, all B<=r<=t<infinity, where
P(r,t)=diag(H_l^+(t)/H_l^+(r)). It uses the outgoing convention H+=G+iF
and Im(conj(H)H')=k in radial coordinates, NIST DLMF33.2 and33.11.
We re-use the uniform Gamma64 also for smaller L; no optimization is implied.

Define ||F||_w=sup_(r>=B) e^(2(r-B))||F(r)||_2, delta=3e-23,
a=Gamma delta/2, b=Gamma/4, chi=4ab=1.57464e-14.
PR114's convergent ordered Volterra series supplies, for both full and
cut source, ||D_n||_w,||D_(n,T)||_w <= A_n=Cat_(n-1)b^(n-1)a^n.
This is the required continuum premise, not a bound inferred from samples.

## New component-sensitive estimate
Let E_n=sup_(r>=B)||D_n(r)-D_(n,T)(r)||_2 and theta=exp[-2(T-B)].
The first forcing difference is the omitted V integral, so E_1<=a theta.
For n>=2 use the exact noncommutative difference
AB-CD=A(B-D)+(A-C)D in every ordered convolution.
One factor can be bounded by its weighted A_j bound and the other by its
unweighted E_(n-j) bound. Since integral_r^infinity exp[-2(t-B)]dt <=1/2,

E_n <= (Gamma/2) sum_(j=1..n-1)
       [A_j E_(n-j)+E_j A_(n-j)]
    = Gamma sum_(j=1..n-1) A_j E_(n-j).

No matrices were commuted; the final equality only reindexes scalar majorants.
Put h_0=1 and h_n=4 sum_(j=1..n) Cat_(j-1)h_(n-j). Induction gives

E_n <= theta a^n b^(n-1) h_(n-1).

The generating series H(x)=1/(2 sqrt(1-4x)-1) has coefficients
1,4,20,104,548,2904,... . In particular
E_1<=a theta, E_2<=a chi theta, E_3<=(5/4)a chi² theta.
These are a0^-1 numerical bounds in the inherited atomic-coordinate convention.
They apply to operator norms, hence to any normalized individual matrix entry
inside the finite projection; no excluded-ell estimate is present.

For comparison of the exact full radial D with exact first N cut-source terms,
the valid analytic subtotal is sum_(n<=N)E_n+a chi^N/(1-chi).
To compare D with FLOATING approximations, numerical coefficient errors must
be added. To compare with the full angular operator, excluded angular errors
must also be added. Both remain None/OPEN in the machine ledger.

## Exact arithmetic and implementation
exponential_decay_upper(x) is the reciprocal finite positive Taylor sum for
exp(x); it is an upward bound for exp(-x). All factor recurrences and tests of
absolute budget inequalities use Fraction. The hexadecimal rational codec
preserves exact values without modifying the Python integer conversion limit.
Floats are diagnostic displays only. No measured D_n is used as an exact
relative-error denominator; minimum_cutoff takes explicit absolute budgets.

At T65 the outward approximate displays are E1=4.78911917745e-52,
E2=7.54113862158e-66,E3=1.48432231489e-79. Original Coulomb and screen constants
are unchanged. They do not establish physical cross sections or rates.

## Evidence and limits
22 new tests passed in the isolated sandbox, including exact formulas, scopes,
source tamper and 600-digit independent exponential comparisons. The first
missing-bound test was actually RED before implementation. Connected Wolfram
reproduced h0..h5, zero generating-series residual, chi and T55/T65 displays.
The literature search found Smooke, SIAM J Numer Anal20(1983)279-295,
doi:10.1137/0720019, as related perturbation/numerical-error work; its abstract
was read, not its full proof, and this bound is not attributed to it.
Native subagents NOT_RUN (not exposed); NCP NOT_RUN; HH_R10=OFF.
