# PHYS63 R5: 실수축 외부 LAP의 문헌 가정 대조와 full screened Poisson/DtN 구성

## 결과와 근거 수준

이 단계는 새로운 일반 LAP 정리를 발명한 것이 아니다. Adachi, Itakura, Ito,
Skibsted (AIIS), arXiv:1804.07874v1의 이미 확립된 hard-core 이론을 원래 WU088_HH
외부 모형에 적용하고, 경계 Poisson 및 DtN으로의 연결을 직접 유도한다.
근거: **literature-supported + derived**. 유한 표본, Fraction tests 또는
작은 행렬 검산이 무한차원 정리 자체를 증명했다고 주장하지 않는다.

Parent PR108: ba78fd280af1e2c716e75ac0727511be988c9ace.
기존 PHYS62의 fixed-ell Abel flux와 Born 연속성은 보존한다.
원래 NPZ SHA256: f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d.
입력은 21029 bytes, 1386 complex128으로 알려진 원본 NPZ이며 이번에 실제 해시를 확인했다.
이 파일은 기존 입력 identity이고, 본 스펙트럼 정리의 증명 전제는 potential와 영역이다.

## 1. 정의, 단위, 공간

기존 프로젝트의 원자단위 표기를 유지한다. 아래 r는 r/a0, h는 h/Eh이다.
Omega={x in R^3: |x|>B}, B=27, R=7/10, k=7/10, E=k^2/2=49/200.
원래 h_S=-Delta/2-1/r-S(d), d=|x-R zhat|,
S(d)=(1+1/d) exp(-2d). h_C=-Delta/2-1/r. 둘 다 내경계에 Dirichlet
조건을 둔 자기수반 Friedrichs realization이다. 경계는 연결된 외부를 갖는 매끄러운 구다.
두 singularity x=0,R zhat는 영역 밖이다. 잠재함수는 실제 외부영역에서 실수, bounded,
real analytic이다. original eta=Fy와 xi=Fy-phi는 변경하지 않는다.

L_t=2h_t, t=0(C),1(S), radial V=2S. 유니터리 사상 u=r psi로 radial Hilbert
space는 H=L2([B,infinity),dr;L2(S2))이다. H_s의 노름은
||u||_Hs^2=int (1+r^2)^s ||u(r)||_S2^2 dr.
경계 X=H^{1/2}(S2)는 ||g||_X^2=sum_(ell,m)(ell+1)|g_lm|^2와 동등하다.
X*=H^{-1/2}. g=u(B), Zg=+u'(B). 물리적 외부법선은 -partial_r라서
psi에 대한 통상 exterior DtN Lambda_psi와 Z는 Zg=g/B-B Lambda_psi(g/B).
영역을 radial space로 옮겨도 모든 ell,m과 비중심 결합을 유지한다.

## 2. 외부 문헌의 정확한 가정 대조

Primary SSOT: AIIS arXiv:1804.07874v1, 38 pages, PDF pp4,7,9-10;
Condition1.1/1.3, Cor1.6(2), Theorem1.7, Cor1.9/1.10.
https://arxiv.org/abs/1804.07874
https://arxiv.org/pdf/1804.07874
https://ar5iv.labs.arxiv.org/html/1804.07874
Published: Reviews in Mathematical Physics33(2021),2150015,
DOI10.1142/S0129055X2150015X. The exact theorem numbering above refers to v1.

N=1 specialization: cluster family has only the free zero-dimensional subsystem and
full three-dimensional subsystem; the threshold set is {0}. Negative bound states
of the full exterior hydrogen operator are NOT additional subsystem thresholds.
Condition1.1 permits a compact excluded region, so this is not a whole-space-only transfer.
Choose the paper's decay parameter delta_lit=1/2. Set Vlr=-1/r, Vsr=-tS, Vsi=0.

(a) Vlr,Vsr are bounded and tend to zero. Multiplication by either is compact
H1_0(Omega)->H^-1(Omega): use Rellich compact embedding after a compact cutoff,
then let the cutoff radius grow; the remaining operator norm is bounded by the tail sup.
(b) <r>^2 |grad Vlr|=(1+r^2)/r^2 <=730/729. Thus the required weighted first derivatives
are bounded even L2->L2, hence also H1_0->H^-1.
(c) The original screen obeys V(r)<=delta_V exp[-2(r-B)], delta_V=3e-23,
with exact positive-Taylor proof in the code. Since d/dr[(1+r^2)e^-2(r-B)]<0,
<r>^2 S <= (730/2)delta_V. Hence <r>^2 Vsr maps H1_0 to L2 boundedly.
(d) Condition1.3 UCP holds: the coefficients and potential are real analytic on the
connected Omega; elliptic analytic regularity and identity continuation imply that a
solution vanishing on an open set vanishes identically. There is no interior Coulomb
singularity to audit in this auxiliary exterior boundary problem.

Thus Cor1.6(2) excludes positive eigenvalues, Theorem1.7 supplies uniform Besov LAP,
and Cor1.9 supplies norm-continuous weighted boundary values for every s>1/2.
For I=[1/5,3/10] Hartree and any s>1/2:

sup_(E in I,0<eps<=1) ||(h_t^D-E-i eps)^-1||_(L2_s->L2_-s) < infinity,
and the limit eps->0+ exists in that operator norm.

Gradient resolvent bounds also hold. At s=1 one may choose Holder exponent beta=1/8,
since beta<min(1/4,s-1/2). This is uniform over the upper/lower spectral approach
for each of the two fixed operators, not a quantified numerical constant over every
t or modified physical potential. For radial L_t the resolvent is half the h_t
resolvent evaluated at half the spectral argument. No angular cutoff is imposed.
Cor1.10 fixes the outgoing/incoming branch by its microlocal radiation condition.

**The central AND original screened on-shell weighted LAP existence obligation is
therefore closed qualitatively by an applicable prior theorem.** Its norm constant
C_{I,s,t} has not been numerically bounded. Prior project OPEN statements must now
be split into qualitative existence (closed) versus usable numerical constants (open).
The earlier unweighted 1/eps divergence is compatible with this statement.

## 3. Direct boundary Poisson construction, X=H1/2

Choose a bounded smooth annulus B<r<T and its positive reference operator
A_ref=-partial_r^2+L_ang^2/r^2+1. Let v(g) solve A_ref v=0 on the annulus,
v(B)=g, v(T)=0. Standard positive variational elliptic theory gives a bounded
X->H1(annulus) lift. Choose smooth radial chi equal to1 near B and zero on a
neighborhood of T; set Jg=chi v(g), extended by zero.

Crucially do NOT demand an arbitrary H1/2 boundary lift be H2. Instead use the
local equation for v. With lambda=2E, F_t(lambda)=(L_t-lambda)J,

F_t g= -chi(1+lambda+2/r+tV)v -2chi' v'-chi''v.

Every term is L2 and compactly supported; hence F_t:X->H_s is bounded for all
finite s. Formula remains analytic in the spectral lambda. Define

P_t^+(lambda)=J-G_t^+(lambda)F_t(lambda),
G_t^+(lambda)=(L_t^D-lambda-i0)^-1.

It has trace g, solves the original exterior equation, is outgoing outside the lift
support, and maps X boundedly to H_-s and to local H1. Uniqueness follows from
AIIS Cor1.10 after subtracting two solutions (their difference has zero trace).
Different valid lifts give the same outgoing map. Norm convergence of G plus its
gradient and the affine spectral dependence of F imply norm convergence of P
in X->H_-s and local H1. Thus no fixed-ell passage or interchange of unproved
infinite sums is being used.

The increasing-r normal derivative is defined weakly through a compact boundary
test lift and Green's identity; its norm in X* is controlled by the local H1 norm
of P and the PDE. Therefore Z_t^+(E):X->X* exists and is bounded for both full
central and full original screened problems, and Z_t(E+i eps)->Z_t^+(E) in this
boundary operator norm. This is not an estimate for the numerical inverse of any
collar matching or for a specific scattering experiment.

## 4. Actual screened difference and compactness

In radial normalization L_S=L_C-V, so the exact identity is
P_S^+-P_C^+=G_S^+ V P_C^+ (zero trace on the right).
For s=1, multiplication V:H_-1->H_+1 has the explicit bound
mu_V <=730*3e-23=2.19e-20. Coupling P<=20/Q>=21 is retained in all operators.
Resolvent identities imply (I-G_C^+V)^-1=I+G_S^+V on H_-1; no Neumann-smallness
assumption is needed for this algebra because both limiting resolvents exist.
One may prove compactness of G_C^+V by local H2 smoothing and tail control in
an intermediate weight s0 with1/2<s0<1. None of this states ||G_C V||<1.

For boundary data g in X, f=V P_Cg is locally H1. Zero-boundary elliptic regularity
then gives G_S^+ f locally H3 up to the smooth sphere. Hence
D=Z_S^+-Z_C^+ maps H1/2(S2)->H3/2(S2) boundedly, and is compact as X->X*.

For smooth boundary data the outgoing bilinear Green identity is
h^T D g=int_B^infty (P_C^+h)^T V(P_S^+g) dr.
It extends to X by the weighted estimates; Hermitian notation uses the incoming
Poisson adjoint, (P_C^-)^*, not (P_C^+)^* at real outgoing energy.
Thus ||D|| <= mu_V ||P_C^+||_(X->H_-1)||P_S^+||_(X->H_-1), with finite but
uncomputed Poisson constants. This is NOT a numerical bound of size2.19e-20.

## 5. What is and is not completed

Closed at qualitative, literature-supported level: full central/screened exterior
on-shell weighted LAP; all-angular outgoing Poisson and DtN existence; compact
screened boundary correction; retained P/Q offdiagonal definitions.
Open: explicit LAP/Poisson constants; certified truncation/tail errors; numerical
all-angular screened DtN; invertibility/numerical conditioning of an interior
matching or selected block Schur complement; original xi=Fy-phi, incoming adjoint,
regular origin, sigma(E), identical-H k_HH(T), HH_R10. HH_R10 remains OFF.
The exterior sphere is an auxiliary boundary, not a new physical hard nucleus.

## 6. Evidence and limitations

Source-specific Fraction guards and8 new tests run in the sandbox with exit0.
They check conditions, not the external theorem. Connected Wolfram verifies radial
u=r psi identity, weight monotonicity, 730/729 and2.19e-20 arithmetic; its output had
an undefined-symbol warning although the scoped residuals were zero, preserved
as such. Exa full HTML provided exact theorem hypotheses and statements; web parsed
PDF confirmed pages. Web PDF screenshots failed internally and container direct
PDF retrieval failed DNS. No figure/table inference was needed or made. Native
subagent execution NOT_RUN because no dispatch tool is exposed. No NCP job or full
historical WU suite was run. No sibling repository or original file changed.
